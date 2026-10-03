#!/usr/bin/env python3
"""Static checks of the generated site html/aicc.

Checks: every internal link and anchor resolves; both languages have the same pages; every page has a language switch to the same page,
a skip link, one h1, and a lang attribute; no request to another host; every referenced asset exists; every diagram is inlined (no placeholder);
the search indexes exist. Exit code 1 on any error.
"""
import hashlib
import os
import re
import subprocess
import sys
from html.parser import HTMLParser
from urllib.parse import urldefrag, urljoin

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'html', 'aicc')
errors = []


def tree_hash():
    h = {}
    for d, _, fs in os.walk(OUT):
        for f in fs:
            path = os.path.join(d, f)
            with open(path, 'rb') as fh:
                h[os.path.relpath(path, OUT)] = hashlib.sha256(fh.read()).hexdigest()
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
        if tag in ('link',) and 'href' in a:
            self.srcs.append(a['href'])
        if tag in ('script', 'img') and 'src' in a:
            self.srcs.append(a['src'])
        if tag == 'h1':
            self.h1 += 1


def pages(lang):
    base = os.path.join(OUT, lang)
    out = {}
    for d, _, fs in os.walk(base):
        if 'index.html' in fs:
            out['/' + os.path.relpath(d, base).replace(os.sep, '/') + '/'] = os.path.join(d, 'index.html')
    return out


all_pages = {l: pages(l) for l in ('en', 'ru')}
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
        if re.search(r'(?:src|href)="https?://', text):
            errors.append('%s: request to another host' % path)

for path, (p, text) in parsed.items():
    here = os.path.dirname(path)
    for h in p.links + p.srcs:
        if h.startswith(('mailto:', 'javascript:')):
            continue
        target, frag = urldefrag(h)
        target = target.split('?', 1)[0]
        if target.startswith(('http:', 'https:')):
            continue
        if target.startswith('smb://'):
            continue    # the corporate folder that holds the charter and the Registry
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

for f in ('search-en.json', 'search-ru.json'):
    if not os.path.exists(os.path.join(OUT, 'assets', f)):
        errors.append('missing ' + f)

print('pages: en %d, ru %d' % (len(all_pages['en']), len(all_pages['ru'])))
if errors:
    for e in sorted(set(errors))[:60]:
        print('error:', e)
    print('%d error(s)' % len(set(errors)))
    sys.exit(1)
print('site check passed')
