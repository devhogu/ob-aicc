#!/usr/bin/env python3
"""Check the actual assembled portal against content and section boundaries."""
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'html/aicc'
SECTIONS = ('aicc', 'discovery', 'initiatives', 'projects', 'lab')


class Inspection(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.section = None
        self.groups, self.main_links, self.ids = [], [], []
        self.search = None
        self.in_main = False
        self.cards, self.card, self.depth = {}, None, 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'body':
            self.section = attrs.get('data-portal-section')
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'main':
            self.in_main = True
        if tag == 'a':
            if 'data-section' in attrs:
                self.groups.append(attrs['data-section'])
            if self.in_main and 'href' in attrs:
                self.main_links.append(attrs['href'])
        if tag == 'script' and 'data-search' in attrs:
            self.search = attrs['data-search']
        if tag == 'details':
            if 'scenario-card' in attrs.get('class', '').split():
                self.card = attrs['data-urn']
                if self.card in self.cards:
                    raise ValueError(f'Duplicate scenario: {self.card}')
                self.cards[self.card] = []
                self.depth = 1
            elif self.card:
                self.depth += 1

    def handle_endtag(self, tag):
        if tag == 'main':
            self.in_main = False
        if tag == 'details' and self.card:
            self.depth -= 1
            if self.depth == 0:
                self.card = None

    def handle_data(self, text):
        if self.card:
            self.cards[self.card].extend(text.split())


def section_for(path):
    parts = path.strip('/').split('/')
    return parts[1] if len(parts) > 1 and parts[1] in SECTIONS[1:] else 'aicc'


def check():
    errors = []
    counts = Counter()
    for lang in ('en', 'ru'):
        source = ROOT / f'html-alt/financial-services/{lang}'
        pages = sorted((OUTPUT / lang).rglob('index.html'))
        discovery_pages = list((OUTPUT / lang / 'discovery').rglob('index.html'))
        if len(discovery_pages) != 76:
            errors.append(f'{lang}: expected 76 Discovery pages, got {len(discovery_pages)}')
        for page in pages:
            path = '/' + page.relative_to(OUTPUT).as_posix()
            text = page.read_text()
            parsed = Inspection(text)
            section = section_for(path)
            counts[section + '_pages'] += 1
            if parsed.section != section or parsed.groups != list(SECTIONS):
                errors.append(f'{path}: incorrect section identity/navigation')
            expected_search = f'search-{lang}.json' if section == 'aicc' else f'search-{section}-{lang}.json'
            if not parsed.search or parsed.search.rsplit('/', 1)[-1] != expected_search:
                errors.append(f'{path}: incorrect search scope')
            duplicates = [key for key, count in Counter(parsed.ids).items() if count > 1]
            if duplicates and section != 'aicc':
                errors.append(f'{path}: duplicate ids {duplicates[:3]}')
            for href in parsed.main_links:
                target = urlsplit(urljoin('http://portal' + path, href))
                if target.netloc != 'portal' or target.scheme not in ('http', 'https'):
                    continue
                if section_for(target.path) != section:
                    errors.append(f'{path}: body link crosses section: {href}')
            if section != 'aicc':
                for marker in ('class="term"', 'class="xref"', 'Version 2.2', 'Версия 2.2'):
                    if marker in text:
                        errors.append(f'{path}: inherited charter metadata/link: {marker}')
            if section == 'discovery':
                relative = page.relative_to(OUTPUT / lang / 'discovery')
                original = Inspection((source / relative).read_text())
                if original.cards != parsed.cards:
                    errors.append(f'{path}: scenario content or identity differs from retained source')
                counts[lang + '_scenarios'] += len(parsed.cards)
        if counts[lang + '_scenarios'] != 1101:
            errors.append(f'{lang}: expected 1,101 scenario cards, got {counts[lang + "_scenarios"]}')
    for path in sorted((OUTPUT / 'assets').glob('search-*.json')):
        entries = json.loads(path.read_text())
        name = path.stem.removeprefix('search-')
        section = name.rsplit('-', 1)[0] if '-' in name else 'aicc'
        for entry in entries:
            if section_for(entry['u']) != section:
                errors.append(f'{path.name}: cross-section search result {entry["u"]}')
    print(json.dumps({'counts': dict(counts), 'errors': errors}, ensure_ascii=False, indent=2))
    return errors


if __name__ == '__main__':
    raise SystemExit(bool(check()))
