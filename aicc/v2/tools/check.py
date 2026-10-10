#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Check the built Hub site (version 2), every edition: links, anchors, page identifiers, no Draft chip, forbidden wording, search; the Russian vocabulary convention on Russian pages.
#   SCOPE: Reads html/aicc/v2 and aicc/v2 only; never writes except through the build it runs for --idempotent.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: C-HUB-V2, C-HUB-V2-EN, V-M-PORTAL-PROJECTION
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   check - return the list of errors of the built site
#   tree_hash - checksum of every file of the built site
#   translations - parity, Russian text and staleness of each translated edition
# END_MODULE_MAP
"""Check html/aicc/v2: python3 aicc/v2/tools/check.py [--idempotent]"""
import hashlib
import json
import os
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / 'aicc' / 'v2'
OUT = Path(os.environ.get('AICC_V2_OUT') or ROOT / 'html' / 'aicc' / 'v2')


class Parsed(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.srcs, self.h1, self.chips, self.page_ids, self.text, self.skip = set(), [], [], 0, 0, [], [], []
        self.title = ''
        self._stack = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get('class') or '').split()
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])
        elif tag == 'link' and 'href' in a:
            self.srcs.append(a['href'])
        if 'src' in a:
            self.srcs.append(a['src'])
        if tag == 'h1':
            self.h1 += 1
        if 'status-chip' in classes:
            self.chips += 1
        if 'pagefb' in classes:
            self._stack.append('pagefb')
        elif tag in ('script', 'style', 'pre', 'code') or 'term-en' in classes or 'en' in classes or 'kb-step-en' in classes or 'mm' in classes or tag == 'title':
            self._stack.append('skip')
        else:
            self._stack.append('')
        if tag in ('br', 'img', 'meta', 'link', 'input', 'hr'):
            self._stack.pop()

    def handle_endtag(self, tag):
        if self._stack:
            self._stack.pop()

    def handle_data(self, data):
        if 'pagefb' in self._stack:
            if data.strip().startswith('ID:'):
                self.page_ids.append(data.strip())
        elif 'skip' not in self._stack:
            self.text.append(data)


def tree_hash():
    return {p.relative_to(OUT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.rglob('*')) if p.is_file()}


# START_CONTRACT: check
#   PURPOSE: Verify the built site against the rules of the Hub.
#   INPUTS: { }
#   OUTPUTS: { list - error strings; empty when the site is sound }
#   SIDE_EFFECTS: none
# END_CONTRACT: check
def check():
    errors = []
    site = json.loads((SRC / 'site.json').read_text(encoding='utf-8'))
    terms = []
    for path in sorted((SRC / 'vocabulary').glob('*.yaml')):
        terms.extend(yaml.safe_load(path.read_text(encoding='utf-8')) or [])
    ids = json.loads((OUT / 'assets' / 'page-ids.json').read_text(encoding='utf-8'))
    if len(set(ids.values())) != len(ids):
        errors.append('page identifiers are not unique')
    pages = {p.relative_to(OUT).as_posix(): p for p in OUT.rglob('*.html') if 'sources' not in p.relative_to(OUT).parts}
    parsed = {}
    for name, path in pages.items():
        parsed[name] = Parsed()
        parsed[name].feed(path.read_text(encoding='utf-8'))
    forbidden = [re.compile(re.escape(w), re.I) for w in site['forbidden']] + [re.compile(p) for p in site['forbidden_patterns']]
    english = SRC / 'i18n' / 'terms-en.yaml'  # the English forms of the forbidden wording, for the English edition
    listed = yaml.safe_load(english.read_text(encoding='utf-8')) if english.exists() else {}
    forbidden_by = {'en': [re.compile(r'(?<![\w-])' + re.escape(w) + r'(?![\w-])', re.I) for w in listed.get('forbidden_en', [])]
                    + [re.compile(p) for p in listed.get('forbidden_patterns_en', [])]}
    languages = site.get('languages', ['ru'])
    content_pages = {n for n in pages if n.split('/')[0] in languages}
    for name in sorted(content_pages):
        p, text = parsed[name], path_text(parsed[name])
        lang = name.split('/')[0]
        page_id = name[len(lang) + 1:-len('/index.html')] if name != f'{lang}/index.html' else 'index'
        if p.h1 != 1:
            errors.append(f'{name}: {p.h1} h1')
        if p.chips:  # the site is active (owner, 2026-10-10): no Draft chip on any page
            errors.append(f'{name}: a Draft chip is shown')
        if len(p.page_ids) != 1 or p.page_ids[0] != 'ID: ' + ids.get(page_id, '?'):
            errors.append(f'{name}: page identifier missing or wrong ({p.page_ids})')
        for pattern in forbidden + forbidden_by.get(lang, []):
            hit = pattern.search(text)
            if hit:
                errors.append(f'{name}: forbidden wording {hit[0]!r}')
        carried = 'class="discovery-content"' in pages[name].read_text(encoding='utf-8')  # carried over verbatim from the catalog
        if lang == 'ru' and name != 'ru/reference/vocabulary/index.html' and not carried:  # the Russian convention: an English term only beside its Russian word
            for term in terms:
                if term['ru'].lower().startswith(term['en'].lower()):
                    continue  # the Russian text itself uses the English word, as the terminology map prescribes
                for hit in re.finditer(r'(?<![\w-])' + re.escape(term['en']) + r'(?![\w-])', text, re.I):
                    errors.append(f'{name}: English term {term["en"]!r} outside the vocabulary form')
                    break
    for name, p in parsed.items():
        here = posixpath.dirname(name)
        for ref in p.links + p.srcs:
            parts = urlsplit(ref)
            if parts.scheme in ('http', 'https', 'mailto'):
                if parts.scheme in ('http', 'https') and ref in p.srcs:
                    errors.append(f'{name}: request to another host {ref}')
                continue
            if parts.scheme or parts.netloc:
                errors.append(f'{name}: odd reference {ref}')
                continue
            target = posixpath.normpath(posixpath.join(here, unquote(parts.path))) if parts.path else name
            if target.startswith('..'):
                errors.append(f'{name}: reference leaves the site {ref}')
                continue
            if not (OUT / target).exists():
                errors.append(f'{name}: broken reference {ref}')
            elif parts.fragment and target in parsed and unquote(parts.fragment) not in parsed[target].ids:
                errors.append(f'{name}: missing anchor {ref}')
    for lang in languages:
        index = (OUT / 'assets' / f'search-{lang}.js').read_text(encoding='utf-8')
        entries = json.loads(index[len('window.AICC_SEARCH_INDEX='):].rstrip(';\n'))
        for entry in entries:
            parts = urlsplit(entry['u'])
            if not parts.path.startswith(lang + '/'):
                errors.append(f'search-{lang}: result in another edition: {entry["u"]}')
            if parts.path not in parsed or parts.fragment and parts.fragment not in parsed[parts.path].ids:
                errors.append(f'search result does not resolve: {entry["u"]}')
    entry = OUT / 'index.html'
    if 'url=ru/index.html' not in entry.read_text(encoding='utf-8'):
        errors.append('the site entry must forward to ru/index.html')
    errors.extend(translations(site, languages))
    return errors


# START_CONTRACT: translations
#   PURPOSE: Hold every translated edition to the Russian one: page pairs share their structure (always), and while the edition is marked complete it has no Russian text and no missing or stale translation (reported as warnings while it is a draft).
#   INPUTS: { site: dict; languages: list }
#   OUTPUTS: { list - errors; warnings are printed }
#   SIDE_EFFECTS: Prints a summary of the translation state.
# END_CONTRACT: translations
def translations(site, languages):
    import parity
    errors = []
    for lang in languages:
        if lang == 'ru':
            continue
        strict = site.get('editions', {}).get(lang) == 'complete'
        incomplete = []
        ru_pages = sorted(p.relative_to(OUT / 'ru').as_posix() for p in (OUT / 'ru').rglob('index.html') if 'catalog/assets' not in p.as_posix())
        for name in ru_pages:
            own = OUT / lang / name
            if not own.exists():
                errors.append(f'{lang}/{name}: the page is missing in this edition')
                continue
            ru_sig, own_sig = parity.signature(OUT / 'ru' / name), parity.signature(own)
            errors.extend(parity.compare(ru_sig, own_sig, name, lang, ordered=name != 'reference/vocabulary/index.html'))  # the vocabulary is alphabetical in each language
            words = parity.cyrillic(own_sig)
            if words:
                incomplete.append(f'{lang}/{name}: Russian text ({len(words)} words, e.g. {", ".join(words[:3])})')
        extra = sorted(p.relative_to(OUT / lang).as_posix() for p in (OUT / lang).rglob('index.html') if 'catalog/assets' not in p.as_posix() and not (OUT / 'ru' / p.relative_to(OUT / lang)).exists())
        errors.extend(f'{lang}/{name}: a page without its Russian source' for name in extra)
        missing, stale = parity.staleness(lang)
        incomplete += [f'{lang}: no translation of {x}' for x in missing] + [f'{lang}: translation older than its Russian source: {x}' for x in stale]
        if strict:
            errors.extend(incomplete)
        else:
            print(f'{lang} edition (draft): {len(ru_pages)} page pairs; {sum(1 for x in incomplete if "Russian text" in x)} pages with Russian text; '
                  f'{len(missing)} translations missing; {len(stale)} stale')
    return errors


def path_text(parsed):
    return re.sub(r'\s+', ' ', ' '.join(parsed.text))


def main():
    if '--idempotent' in sys.argv:
        before = tree_hash()
        result = subprocess.run([sys.executable, str(SRC / 'tools' / 'build.py')], capture_output=True, text=True)
        if result.returncode:
            print('error: the build failed:', result.stderr.strip()[-400:])
            sys.exit(1)
        after = tree_hash()
        changed = sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))
        if changed:
            print('error: html/aicc/v2 is not a fresh build; %d file(s) differ, for example %s' % (len(changed), ', '.join(changed[:5])))
            sys.exit(1)
        print('build is repeatable: %d files unchanged' % len(after))
    errors = check()
    for error in errors:
        print('error:', error)
    if errors:
        print('%d error(s)' % len(errors))
        sys.exit(1)
    print('v2 site check passed')


if __name__ == '__main__':
    main()
