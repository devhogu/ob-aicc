#!/usr/bin/env python3
"""Check the portal scaffolding against the charter.

Every charter file supplies content to some page. Every document section, and every workflow, guide, and template, has exactly one canonical page.
Identifiers and addresses are unique, every page has its outline file, and the reading routes and companions name existing pages.
"""
import glob, json, os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scaf = os.path.join(root, 'portal-scaffolding')
sm = json.load(open(os.path.join(scaf, 'sitemap.json')))
errors, warnings = [], []

sections = {s['id'] for s in sm['sections']}
ids, slugs = set(), set()
by_source = {}
for p in sm['pages']:
    if p['id'] in ids: errors.append('duplicate id ' + p['id'])
    ids.add(p['id'])
    if p['slug'] in slugs: errors.append('duplicate address ' + p['slug'])
    slugs.add(p['slug'])
    if p.get('section') and p['section'] not in sections: errors.append('unknown section ' + p['id'])
    for s in p.get('source', []):
        if not os.path.exists(os.path.join(root, s)): errors.append('missing source %s for %s' % (s, p['id']))
    if p['type'] in ('document', 'workflow', 'guide', 'template', 'catalogue') and p.get('source'):
        by_source.setdefault(p['source'][0], []).append(p)

def numbered_sections(path):
    text = open(os.path.join(root, path), encoding='utf-8').read()
    return {int(m.group(1)) for m in re.finditer(r'^## (\d+)\.', text, flags=re.M)}

for src, pages in by_source.items():
    split = [p for p in pages if p.get('source_sections')]
    if split:
        if len(split) != len(pages): errors.append('%s mixes whole-document and part pages' % src)
        seen = {}
        for p in split:
            for n in p['source_sections']:
                if n in seen: errors.append('section %d of %s has two canonical pages: %s, %s' % (n, src, seen[n], p['id']))
                seen[n] = p['id']
        missing = numbered_sections(src) - set(seen)
        if missing: errors.append('%s sections without a canonical page: %s' % (src, sorted(missing)))
        for p in split:
            w = p.get('words', 0)
            if w and not (200 <= w <= 2000): warnings.append('%s has %d words' % (p['id'], w))
    elif len(pages) != 1:
        errors.append('more than one canonical page for %s: %s' % (src, ', '.join(p['id'] for p in pages)))

used = {s for p in sm['pages'] for s in p.get('source', [])}
for f in sorted(glob.glob(os.path.join(root, 'charter', '**', '*.md'), recursive=True)):
    rel = os.path.relpath(f, root)
    if rel not in used: errors.append('charter file without a page: ' + rel)

def outline_file(p):
    if p['id'] == 'index': return 'pages/index.md'
    sec = p['section']
    if p['id'].endswith('/index'): return 'pages/%s/index.md' % sec
    return 'pages/%s/%s.md' % (sec, p['id'].split('/', 1)[1].replace('/', '--'))

for p in sm['pages']:
    if not os.path.exists(os.path.join(scaf, outline_file(p))): errors.append('missing outline file ' + outline_file(p))
    c = p.get('companion')
    if c and c not in ids: errors.append('%s names an unknown companion %s' % (p['id'], c))

routes = os.path.join(scaf, 'reading-routes.md')
if os.path.exists(routes):
    for pid in re.findall(r'`([a-z0-9\-/]+)`', open(routes).read()):
        if pid not in ids: errors.append('reading route names an unknown page: ' + pid)

print('pages: %d, sections: %d' % (len(sm['pages']), len(sm['sections'])))
for w in warnings: print('warning: ' + w)
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('scaffolding check passed')
