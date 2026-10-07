#!/usr/bin/env python3
"""Check the actual assembled portal against content and section boundaries."""
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit

import discovery

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'html/aicc'
SECTIONS = ('aicc', 'discovery', 'initiatives', 'projects', 'lab')
# Discovery pages composed by the portal rather than built from the catalog records.
AUTHORED_DISCOVERY = {'regulatory-horizon/index.html'}


class Inspection(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.section = None
        self.groups, self.main_links, self.ids = [], [], []
        self.search = None
        self.in_main = False
        self.in_footer = False
        self.nav_footer_depth = 0
        self.nav_footer_links, self.footer_links, self.feedback_refs = [], [], []
        self.feedback_buttons = 0
        self.cards, self.card, self.depth = {}, None, 0
        self.horizon_cards = 0
        self.derived = None
        self.contexts, self.context_tag, self.context_card_count = [], None, 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        if 'card--horizon' in classes:
            self.horizon_cards += 1
        if 'problems-row' in classes or 'discovery-context-card' in classes:
            self.contexts.append([])
            self.context_tag = tag
            self.context_card_count += 'discovery-context-card' in classes
        if tag == 'body':
            self.section = attrs.get('data-portal-section')
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'main':
            self.in_main = True
        if tag == 'footer':
            self.in_footer = True
        if tag == 'div' and (self.nav_footer_depth or 'nav-foot' in attrs.get('class', '').split()):
            self.nav_footer_depth += 1
        if tag == 'dialog' and attrs.get('id') == 'fb':
            self.feedback_refs.append(attrs.get('data-ref', ''))
        if tag == 'button' and attrs.get('data-dialog') == 'fb':
            self.feedback_buttons += 1
        if tag == 'a':
            if 'data-section' in attrs:
                self.groups.append(attrs['data-section'])
            if self.in_main and not self.in_footer and 'href' in attrs:
                self.main_links.append(attrs['href'])
            if self.in_footer and 'href' in attrs:
                self.footer_links.append(attrs['href'])
            if self.nav_footer_depth and 'href' in attrs:
                self.nav_footer_links.append(attrs['href'])
        if tag == 'script' and 'data-search' in attrs:
            self.search = attrs['data-search']
        if 'horizon-chip' in attrs.get('class', '').split():
            self.derived = tag
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
        if tag == self.derived:
            self.derived = None
        if tag == self.context_tag:
            self.context_tag = None
        if tag == 'main':
            self.in_main = False
        if tag == 'footer':
            self.in_footer = False
        if tag == 'div' and self.nav_footer_depth:
            self.nav_footer_depth -= 1
        if tag == 'details' and self.card:
            self.depth -= 1
            if self.depth == 0:
                self.card = None

    def handle_data(self, text):
        if self.context_tag:
            self.contexts[-1].extend(text.split())
        if self.card and not self.derived:
            self.cards[self.card].extend(text.split())


def section_for(path):
    parts = path.strip('/').split('/')
    return parts[1] if len(parts) > 1 and parts[1] in SECTIONS[1:] else 'aicc'


def check():
    errors = []
    counts = Counter()
    references = {}
    for lang in ('en', 'ru'):
        seen_refs = set()
        pages = sorted((OUTPUT / lang).rglob('index.html'))
        discovery_pages = list((OUTPUT / lang / 'discovery').rglob('index.html'))
        source_pages = discovery.pages(lang)
        expected_pages = len(source_pages) + len(AUTHORED_DISCOVERY)
        if len(discovery_pages) != expected_pages:
            errors.append(f'{lang}: expected {expected_pages} Discovery pages, got {len(discovery_pages)}')
        source_cards = sum(len(Inspection(discovery.source(page, lang)).cards) for page in source_pages)
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
            legal = {f'/{lang}/privacy/', f'/{lang}/terms-of-use/'}
            for location, links in (('sidebar', parsed.nav_footer_links), ('footer', parsed.footer_links)):
                targets = {urlsplit(urljoin('http://portal' + path, href)).path for href in links}
                if not legal.issubset(targets):
                    errors.append(f'{path}: missing common {location} legal links')
            if parsed.feedback_buttons != 1 or len(parsed.feedback_refs) != 1 or not re.fullmatch(r'[0-9A-HJKMNP-TV-Z]{5}', parsed.feedback_refs[0]):
                errors.append(f'{path}: missing page feedback or reference')
            else:
                ref = parsed.feedback_refs[0]
                if ref in seen_refs:
                    errors.append(f'{path}: duplicate page reference {ref}')
                seen_refs.add(ref)
                key = path.split('/', 2)[2]
                if lang == 'en':
                    references[key] = ref
                elif references.get(key) != ref:
                    errors.append(f'{path}: language counterparts have different page references')
                counts['pages_with_feedback'] += 1
            duplicates = [key for key, count in Counter(parsed.ids).items() if count > 1]
            if duplicates and section != 'aicc':
                errors.append(f'{path}: duplicate ids {duplicates[:3]}')
            for href in parsed.main_links:
                target = urlsplit(urljoin('http://portal' + path, href))
                if target.netloc != 'portal' or target.scheme not in ('http', 'https'):
                    continue
                relationship = section == 'projects' and bool(re.fullmatch(r'/(en|ru)/initiatives/(ini-\d+/)?',target.path)) or section == 'initiatives' and bool(re.fullmatch(r'/(en|ru)/projects/(service-resolution/)?',target.path))
                if section_for(target.path) != section and not relationship:
                    errors.append(f'{path}: body link crosses section: {href}')
            if section != 'aicc':
                for marker in ('class="term"', 'class="xref"', 'class="doc-facts"'):
                    if marker in text:
                        errors.append(f'{path}: inherited charter metadata/link: {marker}')
            if section == 'discovery':
                if 'class="discovery-notice"' in text:
                    errors.append(f'{path}: removed Discovery notice is still rendered')
                relative = page.relative_to(OUTPUT / lang / 'discovery')
                if relative == Path('index.html') and parsed.horizon_cards != 1:
                    errors.append(f'{path}: overview must include one Regulatory Horizon card')
                if relative.as_posix() in AUTHORED_DISCOVERY:
                    continue
                original = Inspection(discovery.source(relative, lang))
                if original.cards != parsed.cards:
                    errors.append(f'{path}: scenario content or identity differs from the catalog record')
                if original.contexts != parsed.contexts or parsed.context_card_count != len(original.contexts):
                    errors.append(f'{path}: context cards omit or change source text')
                counts[lang + '_context_cards'] += parsed.context_card_count
                counts[lang + '_scenarios'] += len(parsed.cards)
        if counts[lang + '_scenarios'] != source_cards:
            errors.append(f'{lang}: expected {source_cards} scenario cards, got {counts[lang + "_scenarios"]}')
    for path in sorted((OUTPUT / 'assets').glob('search-*.json')):
        entries = json.loads(path.read_text())
        name = path.stem.removeprefix('search-')
        section = name.rsplit('-', 1)[0] if '-' in name else 'aicc'
        for entry in entries:
            if section_for(entry['u']) != section:
                errors.append(f'{path.name}: cross-section search result {entry["u"]}')
    from check_lab import check as check_lab
    lab_errors, lab_counts = check_lab(OUTPUT)
    errors.extend(lab_errors)
    counts.update(lab_counts)
    from check_project import check as check_project
    project_errors, project_counts = check_project(OUTPUT)
    errors.extend(project_errors)
    counts.update(project_counts)
    print(json.dumps({'counts': dict(counts), 'errors': errors}, ensure_ascii=False, indent=2))
    return errors


if __name__ == '__main__':
    raise SystemExit(bool(check()))
