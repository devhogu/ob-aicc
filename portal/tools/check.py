#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Static checks for portal sources and generated output.
#   SCOPE: Message and page parity, links, assets, external requests, lang attributes, language links, contrast, repeatable build.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-SOURCE, M-PORTAL-PROJECTION, V-M-PORTAL-SOURCE, V-M-PORTAL-PROJECTION
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   OUT - module-internal helper or constant
#   errors - module-internal helper or constant
#   warnings - module-internal helper or constant
#   err - module-internal helper or constant
#   Page - module-internal helper or constant
#   is_external - module-internal helper or constant
#   check_refs - module-internal helper or constant
#   check_css - module-internal helper or constant
#   check_output - generated site checks
#   check_sources - source-side checks
#   same_tree - module-internal helper or constant
#   check_idempotent - two builds and html/aicc must be identical
# END_MODULE_MAP
"""Static checks for the AICC portal build.

Fails on: differing ru/en message keys or page sets, missing assets, broken internal links, external
requests, a missing lang attribute, language links that do not reach the counterpart page, contrast
failures, and (with --idempotent) any difference between two builds or between a fresh build and html/aicc.
Missing content translations are reported as warnings.
"""
import argparse
import filecmp
import re
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
import tokens  # noqa: E402

OUT = build.DEFAULT_OUT
errors, warnings = [], []


def err(msg):
    errors.append(msg)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.refs = []       # (kind, url) for things the page loads or links to
        self.lang_links = []
        self._in_lang = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.lang = a.get('lang')
        if tag == 'nav' and a.get('class') == 'site-lang':
            self._in_lang = True
        if tag == 'a' and 'href' in a:
            self.refs.append(('link', a['href']))
            if self._in_lang:
                self.lang_links.append((a.get('data-lang'), a['href']))
        if tag == 'link' and 'href' in a:
            self.refs.append(('load', a['href']))
        if tag in ('img', 'script', 'source', 'iframe') and 'src' in a:
            self.refs.append(('load', a['src']))
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh':
            m = re.search(r'url=(\S+)', a.get('content', ''))
            if m:
                self.refs.append(('link', m.group(1)))

    def handle_endtag(self, tag):
        if tag == 'nav':
            self._in_lang = False


def is_external(url):
    return bool(re.match(r'^(?:[a-z][a-z0-9+.-]*:)?//', url)) or url.startswith(('http:', 'https:'))


def check_refs(base_file, refs):
    for kind, url in refs:
        if url.startswith(('#', 'mailto:', 'javascript:', 'data:')):
            continue
        if is_external(url):
            if kind == 'load':
                err(f'{base_file.relative_to(OUT)}: external request {url}')
            continue
        target = (base_file.parent / url.split('#')[0].split('?')[0]).resolve()
        if not target.is_file():
            err(f'{base_file.relative_to(OUT)}: broken reference {url}')


def check_css(css_file):
    text = css_file.read_text(encoding='utf-8')
    for url in re.findall(r"@import\s+url\(['\"]?([^'\")]+)", text) + re.findall(r"url\(['\"]?([^'\")]+)['\"]?\)", text):
        if url.startswith('data:'):
            continue
        if is_external(url):
            err(f'{css_file.relative_to(OUT)}: external request {url}')
            continue
        if not (css_file.parent / url.split('#')[0].split('?')[0]).resolve().is_file():
            err(f'{css_file.relative_to(OUT)}: missing asset {url}')


def check_output():
    if not OUT.is_dir():
        err(f'{OUT} does not exist; run portal/tools/build.py')
        return
    ru_pages = sorted(p.relative_to(OUT / 'ru') for p in (OUT / 'ru').rglob('index.html'))
    en_pages = sorted(p.relative_to(OUT / 'en') for p in (OUT / 'en').rglob('index.html'))
    if ru_pages != en_pages:
        err(f'page sets differ: ru={ru_pages} en={en_pages}')
    if not (OUT / 'index.html').is_file():
        err('site root index.html missing')
    for f in sorted(OUT.rglob('*.html')):
        rel = f.relative_to(OUT)
        p = Page()
        p.feed(f.read_text(encoding='utf-8'))
        expected = rel.parts[0] if rel.parts[0] in build.LANGS else 'ru'
        if p.lang != expected:
            err(f'{rel}: lang={p.lang!r}, expected {expected!r}')
        check_refs(f, p.refs)
        if rel.parts[0] in build.LANGS:
            inner = Path(*rel.parts[1:])
            got = dict(p.lang_links)
            for l in build.LANGS:
                want = (OUT / l / inner).resolve()
                href = got.get(l)
                if not href or (f.parent / href).resolve() != want:
                    err(f'{rel}: language link for {l} does not reach {want.relative_to(OUT)}')
    for css in sorted(OUT.rglob('*.css')):
        check_css(css)
    root = (OUT / 'index.html').read_text(encoding='utf-8')
    if 'url=ru/index.html' not in root:
        err('site root does not lead to ru/')


def check_sources():
    ru = build.json.loads((build.ROOT / 'messages/ru.json').read_text(encoding='utf-8'))
    en = build.json.loads((build.ROOT / 'messages/en.json').read_text(encoding='utf-8'))
    if set(ru) != set(en):
        err(f'message keys differ: only ru={sorted(set(ru)-set(en))} only en={sorted(set(en)-set(ru))}')
    for path in sorted((build.ROOT / 'content').glob('*.json')):
        if path.stem not in build.PAGE_ORDER:
            err(f'content {path.name} is not in PAGE_ORDER')
    for r in tokens.contrast_results(tokens.load_tokens()):
        if not r['pass']:
            err(f'contrast {r["theme"]} {r["foreground"]}/{r["background"]} = {r["ratio"]} < {r["target"]}')


def same_tree(a, b):
    diff = []
    def walk(cmp, prefix=''):
        diff.extend(prefix + n for n in cmp.left_only + cmp.right_only + cmp.diff_files + cmp.funny_files)
        for name, sub in cmp.subdirs.items():
            walk(sub, prefix + name + '/')
    walk(filecmp.dircmp(a, b))
    # dircmp compares by stat signature first; verify content of "same" files as well
    for f in sorted(a.rglob('*')):
        if f.is_file() and (b / f.relative_to(a)).is_file() and f.read_bytes() != (b / f.relative_to(a)).read_bytes():
            diff.append(str(f.relative_to(a)))
    return sorted(set(diff))


def check_idempotent():
    with tempfile.TemporaryDirectory() as t1, tempfile.TemporaryDirectory() as t2:
        a, b = Path(t1) / 'a', Path(t2) / 'b'
        build.build(a, quiet=True)
        build.build(b, quiet=True)
        d = same_tree(a, b)
        if d:
            err(f'two builds differ: {d[:5]}')
        d = same_tree(a, OUT) if OUT.is_dir() else ['html/aicc missing']
        if d:
            err(f'html/aicc is not the current build output: {d[:5]}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--idempotent', action='store_true')
    args = ap.parse_args()
    check_sources()
    check_output()
    site = build.Site()
    for pid in build.PAGE_ORDER:
        for lang in build.LANGS:
            build.render_page(site, pid, lang)
    warnings.extend(site.warnings)
    if args.idempotent:
        check_idempotent()
    for w in warnings:
        print('warning:', w)
    for e in errors:
        print('error:', e)
    print(f'{len(errors)} error(s), {len(warnings)} warning(s)')
    sys.exit(1 if errors else 0)
