#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Carry the scenario catalog over as it was: every page's content, styles and scripts, verbatim, into the Hub's own source.
#   SCOPE: One-time import. Reads a built catalog folder; writes aicc/v2/catalog (fragments and assets). Run again only to refresh from the same source.
#   DEPENDS: none
#   LINKS: C-HUB-V2
# END_MODULE_CONTRACT
"""Import the catalog: python3 aicc/v2/tools/import_catalog.py <built catalog folder, e.g. html/aicc/v1/ru/discovery>"""
import html
import json
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / 'aicc' / 'v2' / 'catalog'


def main(source):
    source = Path(source)
    shutil.rmtree(DEST, ignore_errors=True)
    (DEST / 'pages').mkdir(parents=True)
    shutil.copytree(source / 'assets', DEST / 'assets')
    shutil.copy(ROOT / 'portal' / 'site' / 'discovery.css', DEST / 'discovery.css')
    shutil.copy(ROOT / 'portal' / 'site' / 'discovery.js', DEST / 'discovery.js')
    count = 0
    for page in sorted(source.rglob('index.html')):
        rel = page.parent.relative_to(source).as_posix()
        rel = '' if rel == '.' else rel
        text = page.read_text(encoding='utf-8')
        main_html = re.search(r'<main[^>]*>(.*?)</main>', text, re.S)[1]
        main_html = re.sub(r'\s*<footer class="o-footer">.*?</footer>\s*$', '', main_html, flags=re.S)  # the old shell's footer
        title = html.unescape(re.sub(r'<[^>]+>', '', re.search(r'<h1[^>]*>(.*?)</h1>', main_html, re.S)[1])).strip()
        layouts = [re.sub(r'^.*assets/styles/', '', h) for h in re.findall(r'<link rel="stylesheet" href="([^"]*assets/styles/[^"]+)"', text)]
        summary = re.search(r'<p class="[^"]*(?:intent|lede)[^"]*">(.*?)</p>', main_html, re.S)
        meta = {'id': ('catalog/' + rel).rstrip('/'), 'title': title, 'styles': layouts,
                'summary': html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', summary[1]))).strip()[:220] if summary else ''}
        out = DEST / 'pages' / (rel or '.') / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text('<!--page ' + json.dumps(meta, ensure_ascii=False) + ' -->\n' + main_html.strip() + '\n', encoding='utf-8')
        count += 1
    relocate_regulation()
    print(f'imported {count} catalog pages')


MOVED = {'from': 'regulatory-horizon', 'id': 'hub/regulation', 'section': 'hub', 'order': 50}


def relocate_regulation():
    """The regulatory page is general information, not a scenario area: it moves to the Hub section, and every link follows it."""
    import posixpath
    old_dir = 'ru/catalog/' + MOVED['from'] + '/'
    new_dir = 'ru/' + MOVED['id'] + '/'
    src = DEST / 'pages' / MOVED['from'] / 'index.html'
    text = src.read_text(encoding='utf-8')
    head, body = text.split('-->\n', 1)
    meta = json.loads(head[len('<!--page '):].strip())
    meta.update({'id': MOVED['id'], 'section': MOVED['section'], 'order': MOVED['order']})

    def move(match):
        href = match[2]
        if href.startswith(('#', 'http', 'mailto')):
            return match[0]
        path, _, frag = href.partition('#')
        target = posixpath.normpath(posixpath.join(old_dir, path)) + ('/' if path.endswith('/') else '')
        return f'{match[1]}="{posixpath.relpath(target, new_dir) + ("/" if path.endswith("/") else "")}{"#" + frag if frag else ""}"'
    body = re.sub(r'(href)="([^"]+)"', move, body)
    body = body.replace('<a class="breadcrumb__link" href="../../catalog/">Каталог сценариев</a>', '<a class="breadcrumb__link" href="../../index.html">Хаб Компетенций</a>')
    out = DEST / 'pages' / '_moved' / 'regulation.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('<!--page ' + json.dumps(meta, ensure_ascii=False) + ' -->\n' + body, encoding='utf-8')
    shutil.rmtree(src.parent)
    # pages that pointed at it now point at its new place
    for page in (DEST / 'pages').rglob('index.html'):
        rel = page.parent.relative_to(DEST / 'pages').as_posix()
        here = 'ru/catalog/' + ('' if rel == '.' else rel + '/')
        s = page.read_text(encoding='utf-8')

        def repoint(match):
            path, _, frag = match[1].partition('#')
            target = posixpath.normpath(posixpath.join(here, path))
            if not target.startswith('ru/catalog/' + MOVED['from']):
                return match[0]
            return 'href="' + posixpath.relpath(new_dir + 'index.html', here) + ('#' + frag if frag else '') + '"'
        n = re.sub(r'href="([^"]+)"', repoint, s)
        if n != s:
            page.write_text(n, encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1])
