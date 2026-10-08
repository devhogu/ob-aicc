#!/usr/bin/env python3
"""Static checks of the generated site html/aicc.

Checks: the layout is the gateway, the assets and, per language, the router and the five branches, nothing else;
every internal href and src of every page (the gateway included) resolves, with its anchor; both languages have the same pages;
every page has a language switch to the same page, a skip link, one h1, and a lang attribute; no resource load from another host (source citations
are allowed); every referenced asset and search index exists; every search result resolves to a page and anchor; every diagram is inlined
(no placeholder). Exit code 1 on any error.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser
from urllib.parse import urldefrag, urljoin

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PACKAGE = os.path.join(ROOT, 'html', 'aicc')
OUT = os.path.join(PACKAGE, 'v1')
BRANCHES = ('center', 'discovery', 'portfolio', 'program', 'lab')
errors = []


def tree_hash():
    h = {}
    for d, _, fs in os.walk(PACKAGE):
        for f in fs:
            path = os.path.join(d, f)
            with open(path, 'rb') as fh:
                h[os.path.relpath(path, PACKAGE)] = hashlib.sha256(fh.read()).hexdigest()
    return h


if '--idempotent' in sys.argv:
    before = tree_hash()
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'portal', 'tools', 'build.py')], capture_output=True, text=True)
    if r.returncode != 0:
        print('error: the build failed:', r.stderr.strip()[-400:])
        sys.exit(1)
    after = tree_hash()
    diff = sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))
    if diff:
        print('error: html/aicc is not a fresh build; %d file(s) differ, for example %s' % (len(diff), ', '.join(diff[:5])))
        sys.exit(1)
    print('build is repeatable: %d files unchanged' % len(after))


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.srcs, self.h1, self.langsw, self.skip = set(), [], [], 0, 0, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])
            if a.get('class') == 'o-skip':
                self.skip += 1
            if 'hreflang' in a:
                self.langsw += 1
        elif 'href' in a:
            self.srcs.append(a['href'])
        if 'src' in a:
            self.srcs.append(a['src'])
        # The search indexes a page script loads, its own branch and every branch for global search.
        for key in ('data-search', 'data-search-all'):
            if a.get(key):
                self.srcs.extend(a[key].split())
        if tag == 'h1':
            self.h1 += 1


def pages(lang):
    base = os.path.join(OUT, lang)
    out = {}
    for d, _, fs in os.walk(base):
        if 'index.html' in fs and d != base:
            out['/' + os.path.relpath(d, base).replace(os.sep, '/') + '/'] = os.path.join(d, 'index.html')
    return out


PACKAGE_ENTRIES = {'index.html', 'en', 'ru', 'v1'}
if set(os.listdir(PACKAGE)) != PACKAGE_ENTRIES:
    errors.append('the package root holds %s, expected exactly %s' % (sorted(os.listdir(PACKAGE)), sorted(PACKAGE_ENTRIES)))
for lang in ('en', 'ru'):
    for d, _, fs in os.walk(os.path.join(PACKAGE, lang)):
        rel = os.path.relpath(d, os.path.join(PACKAGE, lang)).replace(os.sep, '/')
        moved = os.path.join(OUT, lang, '' if rel == '.' else rel, 'index.html')
        if fs != ['index.html'] and fs:
            errors.append('redirect folder %s/%s holds %s' % (lang, rel, sorted(fs)))
        elif fs and not os.path.exists(moved):
            errors.append('redirect %s/%s has no page in v1' % (lang, rel))
expected_root = {'index.html', 'assets', 'en', 'ru'}
if set(os.listdir(OUT)) != expected_root:
    errors.append('html/aicc holds %s, expected exactly %s' % (sorted(os.listdir(OUT)), sorted(expected_root)))
for lang in ('en', 'ru'):
    found = set(os.listdir(os.path.join(OUT, lang))) if os.path.isdir(os.path.join(OUT, lang)) else set()
    if found != {'index.html', *BRANCHES}:
        errors.append('%s/ holds %s, expected exactly the router and the branches %s' % (lang, sorted(found), ', '.join(BRANCHES)))

all_pages = {l: pages(l) for l in ('en', 'ru')}
for lang in ('en', 'ru'):
    with open(os.path.join(OUT, lang, 'index.html'), encoding='utf-8') as fh:
        if 'url=center/' not in fh.read():
            errors.append('%s/ must forward to center/' % lang)
norm = lambda k: k.replace('/./', '/')
if set(map(norm, all_pages['en'])) != set(map(norm, all_pages['ru'])):
    errors.append('the page sets of en and ru differ')

parsed = {}
for lang, ps in all_pages.items():
    for url, path in ps.items():
        text = open(path, encoding='utf-8').read()
        p = P()
        p.feed(text)
        parsed[path] = (p, text)
        if not re.search(r'<html lang="%s"' % lang, text):
            errors.append('%s: wrong html lang' % path)
        if p.h1 != 1:
            errors.append('%s: %d h1' % (path, p.h1))
        if p.skip != 1:
            errors.append('%s: skip link missing' % path)
        if p.langsw < 2:
            errors.append('%s: language switch missing' % path)
        if '@@' in text:
            errors.append('%s: unresolved placeholder' % path)
        if any(re.match(r'^(?:https?:)?//', src, re.IGNORECASE) for src in p.srcs):
            errors.append('%s: request to another host' % path)

standalone = {}
for name in ('index.html',):
    path = os.path.join(OUT, name)
    if os.path.exists(path):
        p = P()
        text = open(path, encoding='utf-8').read()
        p.feed(text)
        standalone[path] = (p, text)
        if '@@' in text:
            errors.append('%s: unresolved placeholder' % name)
for path, (p, text) in list(parsed.items()) + list(standalone.items()):
    here = os.path.dirname(path)
    for h in p.links + p.srcs:
        if h.startswith(('mailto:', 'javascript:')):
            continue
        target, frag = urldefrag(h)
        target = target.split('?', 1)[0]
        if re.match(r'^(?:https?:)?//', target, re.IGNORECASE):
            continue
        if target.startswith('smb://'):
            continue    # the corporate folder that holds the charter and the Registry
        if target.startswith('/'):
            errors.append('%s: site-absolute link %s' % (os.path.relpath(path, OUT), h))
            continue
        dest = os.path.normpath(os.path.join(here, target)) if target else path
        if os.path.isdir(dest):
            dest = os.path.join(dest, 'index.html')
        if not os.path.exists(dest):
            errors.append('%s: broken link %s' % (os.path.relpath(path, OUT), h))
            continue
        if frag and dest.endswith('.html'):
            if dest not in parsed:
                q = P()
                q.feed(open(dest, encoding='utf-8').read())
                ids = q.ids
            else:
                ids = parsed[dest][0].ids
            if frag not in ids:
                errors.append('%s: missing anchor %s' % (os.path.relpath(path, OUT), h))

ids_of = {}
for lang in ('en', 'ru'):
    for branch in BRANCHES:
        name = 'search-%s-%s.json' % (branch, lang)
        index = os.path.join(OUT, 'assets', name)
        if not os.path.exists(index):
            errors.append('missing ' + name)
            continue
        for entry in json.load(open(index, encoding='utf-8')):
            target, frag = urldefrag(entry['u'])
            if not target.startswith('/%s/%s/' % (lang, branch)):
                errors.append('%s: result outside its branch %s' % (name, entry['u']))
            dest = os.path.join(OUT, target.strip('/'), 'index.html')
            if dest not in parsed:
                errors.append('%s: broken result %s' % (name, entry['u']))
            elif frag and frag not in parsed[dest][0].ids:
                errors.append('%s: missing result anchor %s' % (name, entry['u']))
leftover = sorted(f for f in os.listdir(os.path.join(OUT, 'assets')) if f.startswith('search-') and not re.fullmatch(r'search-(%s)-(en|ru)\.json' % '|'.join(BRANCHES), f))
if leftover:
    errors.append('search indexes outside the branches: %s' % ', '.join(leftover))

print('pages: en %d, ru %d' % (len(all_pages['en']), len(all_pages['ru'])))
if errors:
    for e in sorted(set(errors))[:60]:
        print('error:', e)
    print('%d error(s)' % len(set(errors)))
    sys.exit(1)
print('site check passed')
