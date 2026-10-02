#!/usr/bin/env python3
"""Build the AICC charter site (html/aicc) from the charter Markdown.

Source of the content: charter/**/*.md. Source of the structure: portal-scaffolding/sitemap.json.
Source of the chrome: portal/ui (the O! UI/UX kit), portal/site, portal/messages, portal/content.
Output: html/aicc/{index.html, en/, ru/, assets/}. The output is generated and is never edited by hand.

Usage: python3 portal/tools/build.py [--no-diagrams]
"""
import argparse
import concurrent.futures
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from urllib.parse import quote

from markdown_it import MarkdownIt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PORTAL = os.path.join(ROOT, 'portal')
OUT = os.path.join(ROOT, 'html', 'aicc')
SITEMAP = os.path.join(ROOT, 'portal-scaffolding', 'sitemap.json')
CACHE = os.path.join(PORTAL, '.cache', 'mermaid-v3')
NPX = os.environ.get('MMDC_NPX', os.path.expanduser('~/.npm/_npx/668c188756b835f3/node_modules'))
CHROME = os.environ.get('MMDC_CHROME', os.path.expanduser('~/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'))
FONT_FILE = os.path.join(PORTAL, 'ui', 'assets', 'fonts', 'golos-text', 'GolosText-variable.woff2')
CONTACT = {'name': 'Timur Alimbayev', 'email': 'talimbayev@obank.kg'}
PREFIX = {'about': 'ABT', 'what-aicc-does': 'WHT', 'how-aicc-works': 'HOW', 'organization': 'ORG', 'responsible-ai': 'RAI', 'governance': 'GOV', 'library': 'LIB', 'reference': 'REF'}
LANGS = ['en', 'ru']
DEFAULT_LANG = 'en'
BASELINE = {'revision': '1.0', 'date': '2026-10-02'}

FONTS = os.path.join(ROOT, 'portal', '.tools', 'pw-syslibs')
SHORT = {'Statement of Intent on the Adoption of Artificial Intelligence': 'Statement of Intent', 'Vocabulary and Style': 'Vocabulary'}


def disp(t):
    for a, b in SHORT.items():
        t = t.replace(a, b)
    return t
LIBS = os.environ.get('MMDC_LIBS', os.path.join(ROOT, 'portal', '.tools', 'pw-syslibs', 'usr', 'lib', 'x86_64-linux-gnu'))

DOC_NAMES = {
    'Statement of Intent': 'statement-of-intent',
    'AICC Charter': 'aicc-charter',
    'Charter': 'aicc-charter',
    'Business Model': 'business-model',
    'Operating Model': 'operating-model',
    'Portfolio Management Model': 'portfolio-management-model',
    'Solution Lifecycle Model': 'solution-lifecycle-model',
    'AI Policy': 'ai-policy',
    'Document Catalog': 'document-catalog',
    'Catalog': 'document-catalog',
    'Vocabulary': 'vocabulary',
}
XREF = re.compile(r'\b(Statement of Intent|AICC Charter|Charter|Business Model|Operating Model|Portfolio Management Model|Solution Lifecycle Model|AI Policy|Document Catalog|Catalog|Vocabulary)\s+(\d+(?:\.\d+)*)((?:\([a-z]\))?)')
LOCALXREF = re.compile(r'\b(sections?|clause)\s+(\d+(?:\.\d+)*)')
CLAUSE = re.compile(r'^(\d+(?:\.\d+)+)\.\s')


def read(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()


def jload(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def esc(s):
    return html.escape(s, quote=True)


def stem(path):
    return os.path.splitext(os.path.basename(path))[0]


# ---------------------------------------------------------------- markdown

def make_md():
    md = MarkdownIt('commonmark', {'html': False}).enable('table')
    return md


def split_sections(text):
    """Return (preamble, [(num, title, body)], changelog). Sections are the numbered '## ' headings."""
    lines = text.split('\n')
    infence = False
    marks = []
    for i, l in enumerate(lines):
        if l.startswith('```'):
            infence = not infence
        if not infence and l.startswith('## '):
            marks.append(i)
    pre = '\n'.join(lines[:marks[0]]) if marks else text
    secs, change = [], ''
    for k, i in enumerate(marks):
        end = marks[k + 1] if k + 1 < len(marks) else len(lines)
        block = '\n'.join(lines[i:end])
        title = lines[i][3:].strip()
        if title.startswith('Change log'):
            change = block
            continue
        m = re.match(r'(\d+)\.\s+(.*)', title)
        secs.append((int(m.group(1)) if m else None, m.group(2) if m else title, block))
    return pre, secs, change


def front_matter(pre):
    m = re.search(r'```yaml\n(.*?)```', pre, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                out[k.strip()] = v.strip()
    return out


def slug(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s or 'x'


def parse_table(text, header_start):
    """Rows of the first table whose header line starts with header_start, as lists of cell strings."""
    lines = text.split('\n')
    for i, l in enumerate(lines):
        if l.startswith(header_start):
            hdr = [c.strip() for c in l.strip().strip('|').split(' | ')]
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].startswith('|'):
                cells = [c.strip() for c in lines[j].strip().strip('|').split(' | ')]
                while len(cells) < len(hdr):
                    cells.append('')
                rows.append(dict(zip(hdr, cells)))
                j += 1
            return rows
    return []


class Renderer:
    """Renders Markdown to HTML with clause anchors, wrapped tables, and diagram placeholders."""

    def __init__(self, site):
        self.site = site
        self.md = make_md()

    def render(self, text, page_ctx):
        """Return html, outline (list of (level, id, text)), chunks, anchors, diagrams."""
        tokens = self.md.parse(text)
        out_tokens = []
        anchors = set()
        outline = []
        chunks = []
        diagrams = []
        i = 0
        cur = None
        while i < len(tokens):
            t = tokens[i]
            if t.type == 'heading_open':
                inline = tokens[i + 1]
                txt = inline.content
                level = int(t.tag[1])
                m = re.match(r'(\d+(?:\.\d+)*)\.\s+(.*)', txt)
                if level == 2 and m:
                    hid = 's-' + m.group(1).replace('.', '-')
                elif m:
                    hid = 'c-' + m.group(1).replace('.', '-')
                else:
                    hid = slug(txt)
                base = hid
                n = 2
                while hid in anchors:
                    hid = '%s-%d' % (base, n)
                    n += 1
                anchors.add(hid)
                t.attrSet('id', hid)
                if level in (2, 3):
                    outline.append((level, hid, txt))
                cur = {'anchor': hid, 'heading': txt, 'text': ''}
                chunks.append(cur)
            elif t.type == 'paragraph_open':
                inline = tokens[i + 1]
                m = CLAUSE.match(inline.content)
                if m:
                    cid = 'c-' + m.group(1).replace('.', '-')
                    if cid not in anchors:
                        anchors.add(cid)
                        t.attrSet('id', cid)
                        t.attrSet('class', 'clause')
                        t.meta = {'clause': cid}
                if cur is not None and len(cur['text']) < 700:
                    cur['text'] += ' ' + inline.content
            elif t.type == 'fence' and t.info.strip() == 'mermaid':
                cap = None
                if (i + 3 < len(tokens) and tokens[i + 1].type == 'paragraph_open' and tokens[i + 2].type == 'inline'
                        and re.match(r'Figure \d+', tokens[i + 2].content)):
                    cap = tokens[i + 2].content
                    skip = 3
                else:
                    skip = 0
                key = hashlib.sha1(t.content.encode('utf-8')).hexdigest()[:12]
                diagrams.append((key, t.content))
                label = cap or 'Diagram'
                h = '@@MM:%s:%s@@' % (key, esc(label))
                nt = type(t)('html_block', '', 0)
                nt.content = h
                out_tokens.append(nt)
                if cap:
                    fig = type(t)('html_block', '', 0)
                    fig.content = '@@CAP:%s@@' % esc(cap)
                    out_tokens.append(fig)
                i += 1 + skip
                continue
            out_tokens.append(t)
            i += 1
        # link rewriting
        for t in out_tokens:
            if t.type == 'inline' and t.children:
                for c in t.children:
                    if c.type == 'link_open':
                        href = c.attrGet('href') or ''
                        c.attrSet('href', self.site.map_link(href, page_ctx))
        r = self.md.renderer
        old_table_open = r.rules.get('table_open')
        html_out = r.render(out_tokens, self.md.options, {})
        html_out = html_out.replace('<table>', '<div class="o-table-wrap" role="region" tabindex="0" aria-label="Table"><table>').replace('</table>', '</table></div>')
        # permalink on clauses
        html_out = re.sub(r'<p id="(c-[0-9-]+)" class="clause">', lambda m: '<p id="%s" class="clause"><a class="permalink" href="#%s" aria-label="@@PERMALINK@@">&para;</a>' % (m.group(1), m.group(1)), html_out)
        return html_out, outline, chunks, anchors, diagrams


# ---------------------------------------------------------------- mermaid

def prep_mermaid(code):
    """Give the diagrams their shapes: a gate is a hexagon, and the classes are styled by the theme, not by the source."""
    if not code.lstrip().startswith(('flowchart', 'graph')):
        return code
    ids = []

    def gate(m):
        ids.append(m.group(1))
        return '%s{{"%s"}}' % (m.group(1), m.group(2))
    code = re.sub(r'(\b[A-Za-z][A-Za-z0-9_]*)\["(Gate: [^"]*)"\]', gate, code)
    code = re.sub(r'^\s*classDef .*\n?', '', code, flags=re.M)
    if ids:
        code = code.rstrip('\n') + '\n  class %s gate\n' % ','.join(ids)
    return code


def render_diagrams(diagrams, enabled):
    """Draw each diagram once per theme in one browser session, cached. Return key -> {'light','dark'} or None."""
    os.makedirs(CACHE, exist_ok=True)
    jobs, seen = [], set()
    for key, code in diagrams:
        if key in seen:
            continue
        seen.add(key)
        if not all(os.path.exists(os.path.join(CACHE, '%s-%s.svg' % (key, t))) for t in ('light', 'dark')):
            jobs.append({'key': key, 'code': prep_mermaid(code)})
    if jobs and enabled:
        env = dict(os.environ)
        env['LD_LIBRARY_PATH'] = LIBS + ':' + env.get('LD_LIBRARY_PATH', '')
        env['FONTCONFIG_PATH'] = FONTS + '/etc/fonts'
        env['FONTCONFIG_FILE'] = FONTS + '/etc/fonts/portal.conf'
        payload = json.dumps({'jobs': jobs, 'font': FONT_FILE, 'mermaid': os.path.join(NPX, 'mermaid', 'dist', 'mermaid.min.js'),
                              'puppeteer': os.path.join(NPX, 'puppeteer'), 'chrome': CHROME})
        try:
            r = subprocess.run(['node', os.path.join(PORTAL, 'tools', 'render-mermaid.js')], input=payload, capture_output=True, text=True, timeout=900, env=env)
            if r.stderr.strip():
                print(r.stderr.strip()[:1500], file=sys.stderr)
            out = json.loads(r.stdout) if r.stdout.strip() else {}
        except Exception as e:
            print('diagram renderer failed: %s' % e, file=sys.stderr)
            out = {}
        for key, res in out.items():
            if 'light' in res and 'dark' in res:
                for t in ('light', 'dark'):
                    with open(os.path.join(CACHE, '%s-%s.svg' % (key, t)), 'w', encoding='utf-8') as f:
                        f.write(res[t])
    result = {}
    for key in seen:
        paths = [os.path.join(CACHE, '%s-%s.svg' % (key, t)) for t in ('light', 'dark')]
        if all(os.path.exists(x) for x in paths):
            result[key] = {'light': open(paths[0], encoding='utf-8').read(), 'dark': open(paths[1], encoding='utf-8').read()}
        else:
            result[key] = None
    return result


# ---------------------------------------------------------------- site model

class Site:
    def __init__(self, args):
        self.args = args
        sm = jload(SITEMAP)
        self.sections = sm['sections']
        self.pages = sm['pages']
        self.by_id = {p['id']: p for p in self.pages}
        self.msg = {lang: jload(os.path.join(PORTAL, 'messages', lang + '.json')) for lang in LANGS}
        en_msg = self.msg['en']
        for lang in LANGS:
            self.msg[lang] = dict(en_msg, **self.msg[lang])     # a string not yet translated shows in English
        self.auth = jload(os.path.join(PORTAL, 'content', 'authored.json'))
        self._fill_untranslated(self.auth)
        self.section_page = {}
        self.file_page = {}
        for p in self.pages:
            if p.get('source_sections') and p.get('source'):
                for n in p['source_sections']:
                    self.section_page.setdefault((p['source'][0], n), p)
            if p['id'] in ('reference/change-history', 'reference/records-and-systems', 'organization/roles'):
                continue
            if p['type'] in ('document', 'workflow', 'guide', 'template', 'catalogue', 'reference') and p.get('source') and not p.get('source_sections'):
                self.file_page[p['source'][0]] = p
            if p['id'] == 'about/charter-outline':
                self.file_page['charter/README.md'] = p
        # first part of split docs for file links
        for p in self.pages:
            if p.get('source_sections') and p['source'][0] not in self.file_page and p.get('part', '').startswith('1 of'):
                self.file_page[p['source'][0]] = p
        for p in self.pages:
            if p['type'] == 'outline' and p['id'] == 'about/charter-outline':
                pass
        self.md = Renderer(self)
        self.extra_search = {}
        self.bodies = {}     # page id -> dict(html, outline, anchors, chunks, diagrams, extra)
        self.svgs = {}
        self.tables = {}
        self.catalog = {}
        self.load_catalogs()

    def _fill_untranslated(self, o):
        if isinstance(o, dict):
            if 'en' in o and 'ru' not in o:
                o['ru'] = o['en']
            else:
                for v in o.values():
                    self._fill_untranslated(v)
        elif isinstance(o, list):
            for v in o:
                self._fill_untranslated(v)

    # ----- catalogs of descriptions
    def load_catalogs(self):
        desc = {}
        for r in parse_table(read('charter/documents/document-catalog.md'), '| Identifier | Title | Purpose'):
            desc[r['Title']] = r['Purpose']
        self.doc_desc = desc
        wf = {}
        for l in read('charter/workflows/README.md').splitlines():
            m = re.match(r'\| \[[^\]]*\]\(([a-z\-]+)\.md\) \| (.*?) \| (.*?) \|', l)
            if m:
                wf['charter/workflows/%s.md' % m.group(1)] = (m.group(2), m.group(3))
        self.wf_desc = wf
        gd = {}
        for l in read('charter/guides/README.md').splitlines():
            m = re.match(r'\| \[[^\]]*\]\(([a-z\-]+)\.md\) \| (.*?) \| (.*?) \|', l)
            if m:
                gd['charter/guides/%s.md' % m.group(1)] = (m.group(2), m.group(3))
        self.gd_desc = gd
        tp = {}
        for l in read('charter/templates/README.md').splitlines():
            m = re.match(r'\| (\d+) \| (.*?) \| \[[^\]]*\]\(([a-z\-]+)\.md\) \| (.*?) \| (.*?) \|', l)
            if m:
                tp['charter/templates/%s.md' % m.group(3)] = {'order': int(m.group(1)), 'name': m.group(2), 'used': m.group(4), 'kept': m.group(5)}
        self.tpl_desc = tp

    # ----- urls
    def url(self, page, lang):
        return '/%s%s' % (lang, page['slug']) if page['slug'] != '/' else '/%s/' % lang

    def rel(self, from_url, to_url):
        """Relative link between two site urls (directory style)."""
        fd = from_url.strip('/').split('/') if from_url.strip('/') else []
        td, frag = (to_url.split('#', 1) + [''])[:2]
        tdl = td.strip('/').split('/') if td.strip('/') else []
        i = 0
        while i < len(fd) and i < len(tdl) and fd[i] == tdl[i]:
            i += 1
        parts = ['..'] * (len(fd) - i) + tdl[i:]
        href = '/'.join(parts) or '.'
        if td.endswith('/') or not parts:
            href = href if href == '.' else href + '/'
        if href == '.':
            href = './'
        return href + ('#' + frag if frag else '')

    def assets(self, from_url):
        fd = from_url.strip('/').split('/') if from_url.strip('/') else []
        return '/'.join(['..'] * len(fd) + ['assets'])

    # ----- link mapping from markdown files
    def map_link(self, href, ctx):
        if not href or href.startswith('#') or re.match(r'^[a-z]+:', href):
            return href
        path, frag = (href.split('#', 1) + [''])[:2]
        base = os.path.dirname(ctx['source'])
        target = os.path.normpath(os.path.join(base, path)).replace('\\', '/')
        page = self.file_page.get(target)
        if page is None:
            return '@@NOLINK@@'
        u = self.url(page, ctx['lang'])
        return self.rel(ctx['url'], u + ('#' + frag if frag else ''))

    # ----- cross-references
    def link_xrefs(self, html_text, ctx):
        stem_here = stem(ctx['source']) if ctx.get('source') else None
        parts = re.split(r'(<[^>]+>)', html_text)
        stack = []
        out = []
        skip_tags = {'a', 'code', 'pre', 'h1', 'h2', 'h3', 'h4', 'script', 'svg', 'style'}
        for part in parts:
            if part.startswith('<'):
                m = re.match(r'<(/?)([a-zA-Z0-9]+)', part)
                if m:
                    tag = m.group(2).lower()
                    selfclose = part.endswith('/>') or tag in ('br', 'img', 'hr', 'input', 'path', 'rect', 'line', 'circle', 'use')
                    if tag in skip_tags and not selfclose:
                        if m.group(1):
                            if stack and stack[-1] == tag:
                                stack.pop()
                        else:
                            stack.append(tag)
                out.append(part)
                continue
            if stack:
                out.append(part)
                continue
            out.append(self._xref_text(part, ctx, stem_here))
        return ''.join(out)

    def _target(self, docstem, num, ctx):
        sec = int(num.split('.')[0])
        key = 'charter/documents/%s.md' % docstem
        page = self.section_page.get((key, sec))
        if page is None:
            page = self.file_page.get(key)
        if page is None:
            return None
        anchors = self.bodies.get(page['id'], {}).get('anchors', set())
        if '.' in num:
            a = 'c-' + num.replace('.', '-')
            if a not in anchors:
                a = 's-%d' % sec
        else:
            a = 's-%d' % sec
        if anchors and a not in anchors:
            a = ''
        return self.rel(ctx['url'], self.url(page, ctx['lang']) + ('#' + a if a else ''))

    def _xref_text(self, text, ctx, stem_here):
        def sub(m):
            href = self._target(DOC_NAMES[m.group(1)], m.group(2), ctx)
            if not href:
                return m.group(0)
            return '<a class="xref" href="%s">%s</a>' % (href, m.group(0))
        text = XREF.sub(sub, text)

        def sub2(m):
            if not stem_here or not stem_here in DOC_NAMES.values():
                return m.group(0)
            href = self._target(stem_here, m.group(2), ctx)
            if not href:
                return m.group(0)
            return '%s <a class="xref" href="%s">%s</a>' % (m.group(1), href, m.group(2))
        return LOCALXREF.sub(sub2, text)


# ---------------------------------------------------------------- page bodies

ICONS = {}


def icon(name):
    if name not in ICONS:
        p = os.path.join(PORTAL, 'ui', 'assets', 'icons', 'ui-%s.svg' % name)
        if os.path.exists(p):
            s = open(p, encoding='utf-8').read()
            s = re.sub(r'\s+', ' ', s)
            s = s.replace('<svg ', '<svg class="o-icon" aria-hidden="true" focusable="false" ', 1)
            ICONS[name] = s
        else:
            ICONS[name] = ''
    return ICONS[name]


def source_text(p):
    text = read(p['source'][0])
    pre, secs, change = split_sections(text)
    if p.get('source_sections'):
        keep = [b for n, t, b in secs if n in p['source_sections']]
    else:
        keep = [b for n, t, b in secs]
    intro = ''
    first_part = (not p.get('source_sections')) or p.get('part', '').startswith('1 of')
    if first_part:
        intro = re.sub(r'```yaml.*?```', '', pre, flags=re.S)
        intro = re.sub(r'^# .*$', '', intro, flags=re.M).strip()
    body = ('\n\n'.join([intro] if intro else []) + '\n\n' + '\n\n'.join(keep)).strip()
    return body, front_matter(pre), change, text


def tr(site, lang, key):
    return site.msg[lang].get(key, site.msg['en'].get(key, key))


def h1_of(path):
    for l in read(path).splitlines():
        if l.startswith('# '):
            return l[2:].strip()
    return ''


def add_generated_pages(site):
    """Control pages, one for each control of Operating Model 8, are added to the page set."""
    om = read('charter/documents/operating-model.md')
    guide = read('charter/guides/unit-governance-guide.md')
    rows = parse_table(om, '| Ref | Control | Rule | Owner')
    grows = {r['Ref']: r for r in parse_table(guide, '| Ref | Control | Objective | Type')}
    site.controls = []
    for r in rows:
        g = grows.get(r['Ref'], {})
        c = {'ref': r['Ref'], 'title': r['Control'], 'rule': r['Rule'], 'owner': r['Owner'], 'when': r['When'],
             'evidence': r['Evidence record'], 'template': r['Template'], 'objective': g.get('Objective', ''),
             'type': g.get('Type', ''), 'test': g.get('How to test', '')}
        site.controls.append(c)
        pid = 'governance/controls/' + r['Ref'].lower()
        site.pages.append({'id': pid, 'section': 'governance', 'order': 200 + len(site.controls), 'type': 'control', 'slug': '/governance/controls/%s/' % r['Ref'].lower(),
                           'title': '%s %s' % (r['Ref'], r['Control']), 'source': ['charter/documents/operating-model.md', 'charter/guides/unit-governance-guide.md'],
                           'production': 'generated', 'control': c})
    site.by_id = {p['id']: p for p in site.pages}
    og = read('charter/guides/organization-guide.md')
    site.roles = {'om': {r['Role']: r for r in parse_table(om, '| Role | Does | Decides')},
                  'prof': {r['Role']: r for r in parse_table(og, '| Role | Purpose | Main responsibilities')},
                  'raci': parse_table(og, '| Activity | SP |')}


def short_id(key, taken, length=5):
    """A short page id: letters and digits without the confusing ones, taken from the hash of the stable page key."""
    alphabet = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
    h = hashlib.sha1(key.encode('utf-8')).digest()
    n = 0
    while True:
        chunk = int.from_bytes(hashlib.sha1(h + bytes([n])).digest()[:8], 'big')
        out = ''
        for _ in range(length):
            out += alphabet[chunk % 32]
            chunk //= 32
        if out not in taken:
            taken.add(out)
            return out
        n += 1


def assign_refs(site):
    """Every page has a short id that readers quote when they ask about it. It comes from the stable identifier of the page in the sitemap, so it does not change when pages are added."""
    taken = set()
    for q in sorted(site.pages, key=lambda x: x['id']):
        q['ref'] = short_id(q['id'], taken)


def load_terms(site):
    rows = parse_table(read('charter/documents/vocabulary.md'), '| Term | Meaning')
    terms = {}
    for r in rows:
        t = r['Term'].strip()
        mean = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', r['Meaning'])
        mean = re.sub(r'[*`]', '', mean).strip()
        if len(t) >= 3 and mean:
            terms[t] = mean if len(mean) <= 300 else mean[:297].rsplit(' ', 1)[0] + '...'
    site.terms = terms
    site.term_re = re.compile(r'(?<![\w-])(' + '|'.join(re.escape(t) for t in sorted(terms, key=len, reverse=True)) + r')(?![\w-])')


def link_terms(site, html_text, ctx, limit=40):
    vocab = site.by_id['reference/vocabulary']
    base = site.rel(ctx['url'], site.url(vocab, ctx['lang']))
    parts = re.split(r'(<[^>]+>)', html_text)
    stack, out, seen = [], [], set()
    skip = {'a', 'code', 'pre', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'script', 'svg', 'style', 'table', 'figure', 'details', 'button'}
    for part in parts:
        if part.startswith('<'):
            m = re.match(r'<(/?)([a-zA-Z0-9]+)', part)
            if m:
                tag = m.group(2).lower()
                if tag not in ('br', 'img', 'hr', 'input') and not part.endswith('/>'):
                    if m.group(1):
                        if tag in stack:
                            while stack and stack.pop() != tag:
                                pass
                    else:
                        stack.append(tag)
            out.append(part)
            continue
        if not stack or not ('p' in stack or 'li' in stack) or any(t in skip for t in stack) or len(seen) >= limit:
            out.append(part)
            continue

        def sub(m):
            t = m.group(1)
            if t in seen or len(seen) >= limit:
                return t
            seen.add(t)
            return '<a class="term" href="%s#t-%s" data-tip="%s" data-tip-title="%s">%s</a>' % (base, slug(t), esc(site.terms[t]), esc(t), t)
        out.append(site.term_re.sub(sub, part))
    return ''.join(out)


def desc_of(site, p):
    src = (p.get('source') or [None])[0]
    if p['type'] == 'document':
        if (not p.get('source_sections')) or p.get('part', '').startswith('1 of'):
            d = site.doc_desc.get(h1_of(src))
            if d:
                return d
        if p.get('source_sections'):
            pre, ss, ch = split_sections(read(src))
            return '; '.join(t for n, t, b in ss if n in p['source_sections'])
    if p['type'] == 'catalogue' and p.get('source_sections'):
        pre, ss, ch = split_sections(read(src))
        return '; '.join(t for n, t, b in ss if n in p['source_sections'])
    if p['type'] == 'workflow' and src in site.wf_desc:
        return site.wf_desc[src][0]
    if p['type'] == 'guide' and src in site.gd_desc:
        return site.gd_desc[src][0]
    if p['type'] == 'template' and src in site.tpl_desc:
        return site.tpl_desc[src]['used']
    if p['type'] == 'role':
        return site.roles['om'].get(p['title'], {}).get('Does', '')
    fixed = {
        'about/charter-outline': 'How the charter is organized, and how its documents, workflows, guides, and templates relate',
        'about/values-and-principles': 'The values and the principles of adoption, application, work, and delivery, and what each applies to',
        'reference/vocabulary': 'The defined terms of the charter and its style',
        'reference/change-history': 'The revision history of the documents',
        'reference/records-and-systems': 'Where each record is kept, and which control it evidences',
        'organization/roles': 'The seven Roles and their pages',
    }
    return fixed.get(p['id'], '')


def render_pages(site):
    diagrams = []
    for p in site.pages:
        t = p['type']
        if p['id'] in ('reference/change-history', 'about/values-and-principles', 'reference/records-and-systems', 'organization/roles', 'index') or t in ('section', 'home', 'role', 'control', 'index', 'records'):
            continue
        if not p.get('source'):
            continue
        if p['id'] == 'about/charter-outline':
            body = re.sub(r'^# .*$', '', read('charter/README.md'), count=1, flags=re.M).strip()
            fm, change, raw = {}, '', body
            src = 'charter/README.md'
        elif t == 'catalogue':
            body, fm, change, raw = source_text({'source': ['charter/documents/operating-model.md'], 'source_sections': p['source_sections'], 'part': 'x'})
            src = p['source'][0]
        else:
            body, fm, change, raw = source_text(p)
            src = p['source'][0]
        p_ctx = {'source': src, 'lang': 'en', 'url': site.url(p, 'en')}
        h, outline, chunks, anchors, dg = site.md.render(body, p_ctx)
        site.bodies[p['id']] = {'html': h, 'outline': outline, 'chunks': chunks, 'anchors': anchors, 'fm': fm, 'change': change, 'raw': raw, 'src': src}
        diagrams.extend(dg)
    return diagrams


# ---------------------------------------------------------------- layout

def nav_groups(site, section):
    items = []
    seen = set()
    for p in sorted([x for x in site.pages if x.get('section') == section and x['type'] not in ('section', 'control', 'role')], key=lambda x: (x['order'], x['id'])):
        if p.get('source_sections') and p.get('document'):
            if p['source'][0] in seen:
                continue
            seen.add(p['source'][0])
        items.append(p)
    return items


def nav_title(site, p):
    if p.get('source_sections') and p.get('document') and p['id'] != 'governance/delivery-records-controls-and-measures':
        return disp(h1_of(p['source'][0])) if p['type'] != 'catalogue' else disp(p['title'])
    return disp(p['title'])


def doc_parts(site, p):
    if not p.get('document'):
        return []
    return sorted([x for x in site.pages if x.get('document') == p['document'] and x['source'][0] == p['source'][0] and x['type'] in ('document', 'catalogue')],
                  key=lambda x: (x['section'] != p['section'], x['order'], x['id']))


def layout(site, p, lang, main_html, outline):
    m = site.msg[lang]
    url = site.url(p, lang)
    A = site.assets(url)
    home = site.rel(url, '/%s/' % lang)
    other = [l for l in LANGS if l != lang][0]
    sw = []
    for l in LANGS:
        href = site.rel(url, site.url(p, l))
        cur = ' aria-current="true"' if l == lang else ''
        sw.append('<a lang="%s" hreflang="%s" href="%s"%s>%s</a>' % (l, l, href, cur, l.upper()))
    nav = ['<a href="%s"%s>%s<span>%s</span></a>' % (home, ' aria-current="page"' if p['id'] == 'index' else '', icon('map'), esc(m['home']))]
    for s in site.sections:
        sec = site.auth['sections'][s['id']]
        sp = site.by_id[s['id'] + '/index']
        href = site.rel(url, site.url(sp, lang))
        here = p.get('section') == s['id']
        cur = ' aria-current="page"' if p['id'] == sp['id'] else (' aria-current="true"' if here else '')
        nav.append('<a href="%s"%s>%s<span>%s</span></a>' % (href, cur, icon(sec['icon']), esc(sec['label'][lang])))
        if here:
            sub = []
            items = nav_groups(site, s['id'])
            ids = {x['id'] for x in items}
            nested = {x['companion']: x for x in items if x['type'] == 'guide' and x.get('companion') in ids}

            def link(q, cls=''):
                qh = site.rel(url, site.url(q, lang))
                active = q['id'] == p['id'] or (q.get('document') and q.get('document') == p.get('document') and q['source'][0] == (p.get('source') or [''])[0])
                if q['id'] == 'organization/roles' and p['type'] == 'role':
                    active = True
                if q['id'] == 'governance/controls' and p['type'] == 'control':
                    active = True
                tip = desc_of(site, q)
                return '<a href="%s"%s%s%s>%s</a>' % (qh, ' aria-current="page"' if active else '', ' class="%s"' % cls if cls else '',
                                                      ' data-tip="%s"' % esc(tip[:200]) if tip else '', esc(nav_title(site, q)))
            for q in items:
                if q['type'] == 'guide' and q.get('companion') in ids:
                    continue
                sub.append(link(q))
                if q['id'] in nested:
                    sub.append(link(nested[q['id']], 'sub2'))
            nav.append('<div class="nav-sub">%s</div>' % ''.join(sub))
    crumbs = ['<a href="%s">%s</a>' % (home, esc(m['home']))]
    if p.get('section'):
        sp = site.by_id[p['section'] + '/index']
        label = esc(site.auth['sections'][p['section']]['label'][lang])
        crumbs.append('<a href="%s">%s</a>' % (site.rel(url, site.url(sp, lang)), label) if p['id'] != sp['id'] else label)
    if p['id'] != 'index' and not p['id'].endswith('/index'):
        crumbs.append(esc(disp(p['title'])))
    bc = '<nav class="o-eyebrow crumbs" aria-label="%s">%s</nav>' % (esc(m['breadcrumb']), ' / '.join(crumbs))
    nx = next_page(site, p)
    if nx:
        bc = '<div class="crumbbar">%s<a class="crumb-next" href="%s" rel="next"><span>%s:</span> <strong>%s</strong> &rsaquo;</a></div>' % (
            bc, site.rel(url, site.url(nx, lang)), esc(m['next']), esc(flow_label(site, nx, lang)))
    ctx = ''
    if outline:
        links = ''.join('<a class="lv%d" href="#%s">%s</a>' % (lv, i, esc(t)) for lv, i, t in outline)
        ctx = '<aside class="o-context" aria-label="%s"><strong>%s</strong>%s</aside>' % (esc(m['on_this_page']), esc(m['on_this_page']), links)
    reading = '<div class="o-reading"><div class="o-copy">%s</div>%s</div>' % (main_html, ctx) if ctx else '<div class="o-wide">%s</div>' % main_html
    ref = p.get('ref', '')
    subject = m['fb_subject'].replace('{ref}', ref)
    title = (p['title'] if p['id'] != 'index' else site.auth['home']['title'][lang]) + ' · ' + m['site_short']
    return f'''<!doctype html>
<html lang="{lang}" data-theme="light">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{esc(title)}</title>
<script>try{{var t=localStorage.getItem('aicc-theme');document.documentElement.dataset.theme=t==='dark'?'dark':'light';}}catch(e){{}}</script>
<link rel="stylesheet" href="{A}/ui/fonts.css">
<link rel="stylesheet" href="{A}/ui/tokens.css">
<link rel="stylesheet" href="{A}/ui/primitives.css">
<link rel="stylesheet" href="{A}/ui/workspace.css">
<link rel="stylesheet" href="{A}/charter.css">
<link rel="alternate" hreflang="{other}" href="{site.rel(url, site.url(p, other))}">
<script src="{A}/site.js" defer data-search="{A}/search-{lang}.json" data-t-none="{esc(m['search_none'])}" data-t-light="{esc(m['theme_to_light'])}" data-t-dark="{esc(m['theme_to_dark'])}" data-t-copied="{esc(m['copied'])}" data-t-mail-body="{esc(m['fb_mail_body'])}" data-t-dz-close="{esc(m['dz_close'])}"></script>
</head>
<body class="charter">
<a class="o-skip" href="#main">{esc(m['skip'])}</a>
<header class="o-header">
  <a class="o-identity" href="{home}"><img src="{A}/ui/assets/logos/o-mark.svg" width="34" height="38" alt=""><span>{esc(m['site_name'])}</span></a>
  <span class="header-scope">{esc(m['header_scope'])}</span>
  <div class="o-search" role="search"><label class="o-sr-only" for="q">{esc(m['search_label'])}</label><input id="q" type="search" autocomplete="off" placeholder="{esc(m['search_placeholder'])}" aria-controls="results"><div id="results" class="o-search-results" hidden></div></div>
  <div class="o-tools"><nav class="lang-switch" aria-label="{esc(m['language_label'])}">{''.join(sw)}</nav><button id="theme-switch" type="button">{esc(m['theme_to_dark'])}</button></div>
</header>
<div class="o-frame">
  <aside class="o-nav"><details open><summary>{esc(m['nav_summary'])}</summary><nav aria-label="{esc(m['nav_label'])}">{''.join(nav)}</nav></details>
    <p class="o-caption">{esc(m['baseline'])}</p></aside>
  <main class="o-main" id="main" tabindex="-1">
    {bc}
    {reading}
    <footer class="o-footer">
      <span class="foot-text">{esc(m['footer'])} <a class="contact" href="mailto:{CONTACT['email']}?subject={quote(subject)}">{esc(m['contact_us'])}</a></span>
      <button type="button" class="pagefb" data-dialog="fb" aria-haspopup="dialog"><span>{esc(m['pagefb'])}</span><span>ID: {esc(ref)}</span></button>
    </footer>
  </main>
</div>
<dialog id="fb" class="fb" aria-labelledby="fb-t" data-subject="{esc(subject)}" data-ref="{esc(ref)}" data-page="{esc(p['title'])}">
  <form method="dialog">
    <div class="fb-head"><h2 id="fb-t">{esc(m['pagefb'])}</h2><code>ID: {esc(ref)}</code><button type="button" class="fb-copy" data-copy-text="{esc(ref)}">{esc(m['fb_copy'])}</button></div>
    <div class="fb-body"><p>{esc(m['fb_prov'])} <a data-mail href="mailto:{CONTACT['email']}">{esc(m['fb_word'])}</a>.</p><button class="oc-button" value="close">{esc(m['fb_close'])}</button></div>
  </form>
</dialog>
</body>
</html>
'''


# ---------------------------------------------------------------- page content

def substitute(site, html_text, lang):
    def widen(svg):
        vb = re.search(r'viewBox="[-\d.]+ [-\d.]+ ([\d.]+) ', svg)
        if not vb:
            return svg
        w = float(vb.group(1))
        return svg.replace('style="max-width:', 'style="min-width:%dpx;max-width:' % int(min(w, 720)), 1)

    def fig(m):
        key, label, cap = m.group(1), m.group(2), m.group(3)
        svgs = site.svgs.get(key)
        if svgs:
            svgs = {k: widen(v) for k, v in svgs.items()}
        capt = '<figcaption>%s</figcaption>' % cap if cap else ''
        if svgs:
            return '<figure class="o-diagram" role="group" aria-label="%s"><button type="button" class="dz-open" aria-label="%s">%s</button><div class="mm mm-light">%s</div><div class="mm mm-dark">%s</div>%s</figure>' % (
                label, esc(tr(site, lang, 'dz_expand')), icon('maximize'), svgs['light'], svgs['dark'], capt)
        code = site.diagram_code.get(key, '')
        return '<figure class="o-diagram"><p class="o-callout">%s</p><pre>%s</pre>%s</figure>' % (esc(tr(site, lang, 'diagram_unavailable')), esc(code), capt)
    html_text = re.sub(r'@@MM:([0-9a-f]+):(.*?)@@\s*(?:@@CAP:(.*?)@@)?', fig, html_text, flags=re.S)
    html_text = re.sub(r'<a href="@@NOLINK@@">(.*?)</a>', r'<span class="nolink">\1</span>', html_text, flags=re.S)
    html_text = html_text.replace('@@PERMALINK@@', esc(tr(site, lang, 'permalink')))
    return html_text


def facts_html(site, p, lang, fm):
    m = site.msg[lang]
    items = []
    if fm.get('id'):
        items.append((m['identifier'], fm['id']))
    if fm.get('revision'):
        items.append((m['revision'], fm['revision']))
    if fm.get('revised'):
        items.append((m['revised'], fm['revised']))
    if fm.get('status'):
        items.append((m['status'], fm['status']))
    if items:
        items.append((m['owner'], m['owner_value']))
    if not items:
        return ''
    return '<dl class="doc-facts">%s</dl>' % ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % (esc(k), esc(v)) for k, v in items)


def parts_html(site, p, lang):
    parts = doc_parts(site, p)
    if len(parts) < 2:
        return ''
    url = site.url(p, lang)
    links = []
    for q in parts:
        label = q['title'].split(': ', 1)[1] if ': ' in q['title'] else ('Foundations' if q.get('part', '').startswith('1 of') else q['title'])
        if q['type'] == 'catalogue' or q['section'] != p['section']:
            pass
        cur = ' aria-current="page"' if q['id'] == p['id'] else ''
        links.append('<a href="%s"%s>%s</a>' % (site.rel(url, site.url(q, lang)), cur, esc(label)))
    return '<nav class="o-tabs parts" aria-label="%s">%s</nav>' % (esc(tr(site, lang, 'parts_label')), ''.join(links))


def flow_pages(site):
    if not hasattr(site, '_flow'):
        flow = [site.by_id['index']]
        for sec in site.sections:
            flow.append(site.by_id[sec['id'] + '/index'])
            flow += sorted([x for x in site.pages if x.get('section') == sec['id'] and x['type'] not in ('section', 'control', 'role')], key=lambda x: (x['order'], x['id']))
        site._flow = flow
    return site._flow


def next_page(site, p):
    """The page that follows in the reading flow: the next page of the section, then the next section."""
    if p['type'] in ('control', 'role'):
        sib = sorted([x for x in site.pages if x['type'] == p['type']], key=lambda x: (x['control']['ref'] if p['type'] == 'control' else '', x['order'], x['id']))
        ids = [x['id'] for x in sib]
        i = ids.index(p['id'])
        if i + 1 < len(sib):
            return sib[i + 1]
        p = site.by_id['governance/controls' if p['type'] == 'control' else 'organization/roles']
    flow = flow_pages(site)
    ids = [x['id'] for x in flow]
    if p['id'] not in ids:
        return None
    i = ids.index(p['id'])
    return flow[i + 1] if i + 1 < len(flow) else None


def flow_label(site, q, lang):
    if q['type'] == 'section':
        return site.auth['sections'][q['section']]['label'][lang]
    if q['type'] == 'control':
        return q['control']['ref']
    return disp(q['title'])


def prev_next(site, p, lang):
    if not p.get('section') or p['type'] in ('section', 'control', 'role', 'home'):
        return ''
    sib = [x for x in site.pages if x.get('section') == p['section'] and x['type'] not in ('section', 'control', 'role')]
    sib.sort(key=lambda x: (x['order'], x['id']))
    i = [x['id'] for x in sib].index(p['id']) if p['id'] in [x['id'] for x in sib] else -1
    if i < 0:
        return ''
    url = site.url(p, lang)
    m = site.msg[lang]
    out = []
    if i > 0:
        out.append('<a class="pn prev" href="%s" rel="prev"><span>%s</span>%s</a>' % (site.rel(url, site.url(sib[i - 1], lang)), esc(m['previous']), esc(disp(sib[i - 1]['title']))))
    nx = next_page(site, p)
    if nx:
        out.append('<a class="pn next" href="%s" rel="next"><span>%s</span>%s</a>' % (site.rel(url, site.url(nx, lang)), esc(m['next']), esc(flow_label(site, nx, lang))))
    return '<nav class="o-pn" aria-label="%s / %s">%s</nav>' % (esc(m['previous']), esc(m['next']), ''.join(out)) if out else ''


def companion_html(site, p, lang):
    c = p.get('companion')
    if not c or c not in site.by_id:
        return ''
    q = site.by_id[c]
    key = 'companion_guide' if q['type'] == 'guide' else 'companion_workflow'
    return '<p class="companion"><a href="%s">%s: %s</a></p>' % (site.rel(site.url(p, lang), site.url(q, lang)), esc(tr(site, lang, key)), esc(re.sub(r'^Guide:\s*', '', q['title'])))


def lang_note(site, lang):
    if lang == 'en':
        return ''
    return '<p class="o-callout lang-note" role="note">%s</p>' % esc(tr(site, lang, 'translation_missing'))


def content_page(site, p, lang):
    b = site.bodies[p['id']]
    ctx = {'source': b['src'], 'lang': lang, 'url': site.url(p, lang)}
    body = site.link_xrefs(b['html'], ctx)
    if p['id'] == 'reference/vocabulary':
        body = re.sub(r'<tr>\n<td>(.*?)</td>', lambda mm: '<tr id="t-%s"><td>%s</td>' % (slug(html.unescape(mm.group(1))), mm.group(1)), body)
    elif p['type'] not in ('template',):
        body = link_terms(site, body, ctx)
    body = substitute(site, body, lang)
    desc = desc_of(site, p)
    lead = '<p class="o-lead" lang="en">%s</p>' % esc(desc) if desc and p['type'] != 'catalogue' else ''
    head = '<h1>%s</h1>%s%s%s%s%s' % (esc(p['title'] if p['title'] in SHORT else disp(p['title'])), lead, facts_html(site, p, lang, b['fm']), companion_html(site, p, lang), parts_html(site, p, lang), lang_note(site, lang))
    extra = ''
    if p['type'] == 'catalogue':
        extra = controls_catalogue(site, p, lang)
    if p['type'] == 'template':
        extra += '<p class="tpl-tools"><button type="button" class="oc-button" data-copy="tpl-src">%s</button></p><script type="text/markdown" id="tpl-src">%s</script>' % (
            esc(tr(site, lang, 'copy_template')), b['raw'].replace('</script', '<\\/script'))
        # the template page starts with the "when used" line from the README
        tp = site.tpl_desc.get(p['source'][0])
        if tp:
            extra = ('<dl class="o-facts"><dt>%s</dt><dd lang="en">%s</dd><dt>%s</dt><dd lang="en"><code>%s</code></dd></dl>' % (esc(tr(site, lang, 'used_when')), esc(tp['used']), esc(tr(site, lang, 'kept_in')), esc(tp['kept'].strip('`')))) + extra
    change = ''
    if b['change']:
        ch = site.md.md.render(re.sub(r'^## .*$', '', b['change'], count=1, flags=re.M).strip())
        ch = ch.replace('<table>', '<div class="o-table-wrap" role="region" tabindex="0" aria-label="Table"><table>').replace('</table>', '</table></div>')
        change = '<details class="oc-disclosure change"><summary>%s</summary><div>%s</div></details>' % (esc(tr(site, lang, 'change_history')), ch)
    main = '%s%s<div class="o-doc" lang="en">%s</div>%s%s' % (head, extra if p['type'] == 'template' else '', body, change, prev_next(site, p, lang))
    if p['type'] == 'catalogue':
        main = '%s<div class="o-doc" lang="en">%s%s</div>%s' % (head, extra, body, prev_next(site, p, lang))
    return layout(site, p, lang, main, b['outline'])


def weight(p):
    """The weight of a page on its section page: a document leads, a workflow supports it, a guide supports a workflow."""
    if p['type'] in ('document', 'catalogue') or p['id'] in ('reference/vocabulary',):
        return 'primary'
    if p['type'] == 'guide':
        return 'support'
    return 'secondary'


def page_meta(site, p, lang):
    m = site.msg[lang]
    kinds = {'document': 'kind_document', 'catalogue': 'kind_document', 'workflow': 'kind_workflow', 'guide': 'kind_guide', 'template': 'kind_template',
             'outline': 'kind_page', 'reference': 'kind_reference', 'records': 'kind_reference', 'index': 'kind_page'}
    k = m.get(kinds.get(p['type'], 'kind_page'), '')
    bits = [k]
    if p.get('source_sections') and p.get('document'):
        n = len([x for x in site.pages if x.get('document') == p['document'] and x['source'][0] == p['source'][0]])
        if n > 1:
            bits.append('%d %s' % (n, m['kind_parts']))
    elif p.get('words'):
        bits.append('%s %s' % (format(p['words'], ','), m['kind_words']))
    return ' · '.join(b for b in bits if b)


def section_desc(site, q):
    """A document that is split over parts is described, in its section, by the sections of the parts that this section holds."""
    if q.get('document') and q.get('source_sections'):
        same = [x for x in site.pages if x.get('document') == q['document'] and x['source'][0] == q['source'][0] and x['section'] == q['section']]
        first = [x for x in site.pages if x.get('document') == q['document'] and x['source'][0] == q['source'][0] and x.get('part', '').startswith('1 of')]
        if first and first[0]['section'] != q['section']:
            pre, ss, ch = split_sections(read(q['source'][0]))
            nums = sorted({n for x in same for n in x['source_sections']})
            names = [t for n, t, bb in ss if n in nums]
            if names:
                return '; '.join(names)
    return desc_of(site, q)


def card(site, q, lang, url, cls, extra=''):
    d = section_desc(site, q)
    meta = page_meta(site, q, lang)
    tip = meta + (' · ' + q.get('ref', '') if q.get('ref') else '')
    return ('<li class="o-card linked %s" data-tip="%s"><p class="card-kicker">%s</p><h3><a href="%s">%s</a></h3><p class="card-desc" lang="en">%s</p>%s</li>' % (
        cls, esc(tip), esc(meta), site.rel(url, site.url(q, lang)), esc(nav_title(site, q)), esc(d), extra))


def cards_for(site, section, lang, from_url):
    m = site.msg[lang]
    items = nav_groups(site, section)
    ids = {x['id'] for x in items}
    guides = {x['companion']: x for x in items if x['type'] == 'guide' and x.get('companion') in ids}
    nested = {g['id'] for g in guides.values()}
    prim = [x for x in items if weight(x) == 'primary']
    sec = [x for x in items if weight(x) == 'secondary']
    sup = [x for x in items if weight(x) == 'support' and x['id'] not in nested]
    out = []
    if prim:
        out.append('<h2>%s</h2><ul class="o-grid card-list cards-primary">%s</ul>' % (esc(m['grp_documents']), ''.join(card(site, q, lang, from_url, 'card--primary') for q in prim)))
    if sec:
        cards = []
        for q in sec:
            g = guides.get(q['id'])
            extra = ''
            if g:
                extra = '<p class="card-guide"><a href="%s">%s</a></p>' % (site.rel(from_url, site.url(g, lang)), esc(m['kind_guide'] + ': ' + re.sub(r'^Guide:\s*', '', g['title'])))
            cards.append(card(site, q, lang, from_url, 'card--secondary', extra))
        out.append('<h2>%s</h2><ul class="o-grid card-list cards-secondary">%s</ul>' % (esc(m['grp_workflows']), ''.join(cards)))
    if sup:
        lis = ''.join('<li><a href="%s">%s</a><span lang="en"> &mdash; %s</span></li>' % (site.rel(from_url, site.url(q, lang)), esc(nav_title(site, q)), esc(desc_of(site, q))) for q in sup)
        out.append('<h2>%s</h2><ul class="support-list">%s</ul>' % (esc(m['grp_guides']), lis))
    return ''.join(out)


def section_page(site, p, lang):
    sid = p['section']
    sec = site.auth['sections'][sid]
    url = site.url(p, lang)
    m = site.msg[lang]
    if sid == 'library':
        out = []
        for q in sorted([x for x in site.pages if x['type'] == 'template'], key=lambda x: x['order']):
            tp = site.tpl_desc.get(q['source'][0], {})
            out.append('<li class="o-card linked card--secondary" data-tip="%s"><p class="card-kicker">%s</p><h3><a href="%s">%s</a></h3><p class="card-desc" lang="en">%s</p></li>' % (
                esc(tp.get('kept', '').strip('`')), esc(m['kind_template']), site.rel(url, site.url(q, lang)), esc(q['title']), esc(tp.get('used', ''))))
        cards = '<ul class="o-grid card-list cards-secondary">%s</ul>' % ''.join(out)
    else:
        cards = cards_for(site, sid, lang, url)
    main = '<h1>%s</h1><p class="o-lead">%s</p>%s' % (esc(sec['label'][lang]), esc(sec['intro'][lang]), cards)
    return layout(site, p, lang, main, [])


def home_page(site, p, lang):
    a = site.auth['home']
    url = site.url(p, lang)
    m = site.msg[lang]
    soi = read('charter/documents/statement-of-intent.md')
    pri = []
    lines = soi.split('\n')
    for i, l in enumerate(lines):
        mm = re.match(r'### (9\.\d+)\. (.*)', l)
        if mm:
            obj = ''
            for l2 in lines[i + 1:i + 4]:
                if l2.startswith('- **Objective.**'):
                    obj = l2.replace('- **Objective.**', '').strip()
                    break
            pri.append((mm.group(1), mm.group(2), obj))
    sp = site.by_id['about/statement-of-intent/strategic-priorities']
    sp_url = site.rel(url, site.url(sp, lang))
    pcards = ''.join('<li class="o-card linked card--secondary" data-tip="%s"><p class="o-tag">%s</p><h3><a href="%s#c-%s">%s</a></h3><p class="card-desc" lang="en">%s</p></li>' % (
        esc(o), 'PRI-%d' % (k + 1), sp_url, num.replace('.', '-'), esc(t), esc(o)) for k, (num, t, o) in enumerate(pri))
    levels = parse_table(soi, '| Maturity Level | Name | Capability')
    rp = site.by_id['about/statement-of-intent/capability-and-maturity-roadmap']
    rp_url = site.rel(url, site.url(rp, lang))
    lcards = ''.join('<li class="level"><span class="lv-n">%s %s</span><strong lang="en">%s</strong><span lang="en">%s</span></li>' % (esc(m['level']), esc(r['Maturity Level']), esc(r['Name']), esc(r['Capability'])) for r in levels)
    mapc = ''
    for k, item in enumerate(a['map'][lang]):
        to = item['to']
        target = site.by_id.get(to) or site.by_id.get(to.rstrip('/') + '/index')
        href = site.rel(url, site.url(target, lang)) if target else '#'
        mapc += '<li class="o-card linked card--primary" data-tip="%s"><h3><a href="%s">%s</a></h3><p class="card-desc">%s</p></li>' % (esc(item['text']), href, esc(item['title']), esc(item['text']))
        if k < 2:
            mapc += '<li class="map-arrow" aria-hidden="true">&rarr;</li>'
    scards = ''
    for s in site.sections:
        sec = site.auth['sections'][s['id']]
        sp2 = site.by_id[s['id'] + '/index']
        scards += '<li class="o-card linked card--secondary" data-tip="%s">%s<h3><a href="%s">%s</a></h3><p class="card-desc">%s</p></li>' % (esc(sec['intro'][lang]), icon(sec['icon']), site.rel(url, site.url(sp2, lang)), esc(sec['label'][lang]), esc(sec['intro'][lang].split('. ')[0].rstrip('.') + '.'))
    routes = ''
    for r in site.auth['routes']:
        links = []
        for pid in r['pages']:
            q = site.by_id.get(pid) or site.by_id.get(pid + '/index')
            links.append('<li><a href="%s">%s</a></li>' % (site.rel(url, site.url(q, lang)), esc(disp(q['title']))))
        routes += '<li class="o-card route"><h3>%s</h3><p class="route-reader">%s</p><p>%s</p><ol>%s</ol></li>' % (esc(r['title'][lang]), esc(r['reader'][lang]), esc(r['purpose'][lang]), ''.join(links))
    main = f'''<section class="home-hero"><p class="o-eyebrow">{esc(a['eyebrow'][lang])}</p><h1>{esc(a['title'][lang])}</h1><p class="o-lead">{esc(a['lead'][lang])}</p></section>
<section aria-labelledby="h-map"><h2 id="h-map">{esc(m['map_title'])}</h2><ul class="o-grid map-grid">{mapc}</ul></section>
<section aria-labelledby="h-pri"><h2 id="h-pri">{esc(m['strategic_priorities'])}</h2><ul class="o-grid card-list pri-grid">{pcards}</ul><p><a href="{sp_url}">{esc(m['card_open'])}: {esc(m['strategic_priorities'])}</a></p></section>
<section aria-labelledby="h-road"><h2 id="h-road">{esc(m['maturity_roadmap'])}</h2><ol class="levels">{lcards}</ol><p><a href="{rp_url}">{esc(m['card_open'])}: {esc(m['maturity_roadmap'])}</a></p></section>
<section aria-labelledby="h-sec"><h2 id="h-sec">{esc(m['nav_label'])}</h2><ul class="o-grid card-list">{scards}</ul></section>
<section aria-labelledby="h-routes"><h2 id="h-routes">{esc(m['reading_routes'])}</h2><ul class="o-grid card-list routes">{routes}</ul></section>'''
    return layout(site, p, lang, main, [])


def plain_md(t):
    return re.sub(r'\*\*([^*]+)\*\*', r'\1', re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t))


def vp_items(doc, num):
    """The items of one group of values or principles, read from the clauses of the document: (lead, text) pairs, and an introduction where the clause has one."""
    pre, ss, ch = split_sections(read('charter/documents/%s.md' % doc))
    body = [b for n, t, b in ss if str(n) == num][0]
    items, intro = [], ''
    for l in body.split('\n'):
        mm = re.match(r'^\d+\.\d+\. \*\*(.+?)\.\*\* (.*)$', l)
        if mm:
            items.append((mm.group(1), plain_md(mm.group(2))))
            continue
        mm = re.match(r'^\(([a-z])\) (.*)$', l)
        if mm:
            items.append(('', plain_md(mm.group(2))))
            continue
        mm = re.match(r'^4\.2\. (.*)$', l) if (doc, num) == ('statement-of-intent', '4') else None
        if mm:
            for sent in re.split(r'(?<=\.) ', mm.group(1)):
                lead = re.match(r'(Integrity|Prudence|Respect for people)', sent)
                items.append((lead.group(1), sent[len(lead.group(1)):].lstrip()))
            continue
        mm = re.match(r'^2\.1\. (.*)$', l) if doc == 'solution-lifecycle-model' else None
        if mm:
            intro = plain_md(mm.group(1))
    return items, intro


VP_DOC_NAMES = {'statement-of-intent': 'Statement of Intent', 'operating-model': 'Operating Model', 'solution-lifecycle-model': 'Solution Lifecycle Model'}


def values_page(site, p, lang):
    a = site.auth['values_page']
    m = site.msg[lang]
    url = site.url(p, lang)
    ctx = {'url': url, 'lang': lang, 'source': 'charter/documents/statement-of-intent.md'}
    out, outline = [], []
    for g in a['groups']:
        doc, num = g['source']
        items, intro = vp_items(doc, num)
        lis = []
        for lead, text in items:
            if g['id'] == 'values':
                lis.append('<li><span lang="en"><strong>%s</strong> %s</span></li>' % (esc(lead), esc(text)))
            elif lead:
                lis.append('<li><span lang="en"><strong>%s.</strong> %s</span></li>' % (esc(lead), esc(text)))
            else:
                first, _, rest = text.partition('. ')
                lis.append('<li><span lang="en">%s</span></li>' % (('<strong>%s.</strong> %s' % (esc(first), esc(rest))) if rest else esc(text)))
        href = site._target(doc, num, ctx)
        title = g['title'][lang]
        hid = 'g-' + g['id']
        outline.append((2, hid, title))
        intro_html = '<p class="vp-intro" lang="en">%s</p>' % link_terms(site, esc(intro), ctx) if intro else ''
        block = ('<section class="vp-group" aria-labelledby="%s"><h2 id="%s">%s</h2><p class="vp-applies"><strong>%s</strong> %s</p>%s<ol class="vp-list">%s</ol>'
                 '<p class="vp-source">%s: <a href="%s" lang="en">%s %s</a></p></section>') % (
            hid, hid, esc(title), esc(m['vp_applies']), esc(g['applies'][lang]), intro_html, link_terms(site, ''.join(lis), ctx), esc(m['vp_source']), href, VP_DOC_NAMES[doc], num)
        out.append(block)
        site.extra_search.setdefault(lang, []).append({'u': url + '#' + hid, 't': p['title'], 'h': title, 'x': (g['applies'][lang] + ' ' + ' '.join((l + ' ' + t) for l, t in items))[:360]})
    main = '<h1>%s</h1><p class="o-lead">%s</p>%s%s' % (esc(p['title']), esc(a['intro'][lang]), lang_note(site, lang), ''.join(out)) + prev_next(site, p, lang)
    return layout(site, p, lang, main, outline)


def about_page(site, p, lang):
    a = site.auth['about_page']
    sec = site.auth['sections']['about']
    m = site.msg[lang]
    url = site.url(p, lang)
    soi = read('charter/documents/statement-of-intent.md')
    sp = site.by_id['about/statement-of-intent/strategic-priorities']
    sp_url = site.rel(url, site.url(sp, lang))
    blocks = []
    for b in a['blocks']:
        extra = ''
        if b.get('priorities'):
            pri = re.findall(r'^### (9\.\d+)\. (.*)$', soi, re.M)
            lv = parse_table(soi, '| Maturity Level | Name | Capability')
            extra = '<ol class="about-pri" lang="en">%s</ol><p class="about-levels"><strong>%s</strong> <span lang="en">%s</span></p>' % (
                ''.join('<li><a href="%s#c-%s">%s</a></li>' % (sp_url, n.replace('.', '-'), esc(t)) for n, t in pri), esc(m['maturity_levels']),
                ' &rarr; '.join(esc(r['Name']) for r in lv))
        links = []
        for l in b['links']:
            q = site.by_id.get(l['to']) or site.by_id.get(l['to'] + '/index')
            links.append('<a href="%s">%s</a>' % (site.rel(url, site.url(q, lang)), esc(l['label'][lang])))
        blocks.append('<section class="about-block" aria-labelledby="a-%s"><h2 id="a-%s">%s</h2><div><p>%s</p>%s<p class="about-links">%s</p></div></section>' % (
            b['id'], b['id'], esc(b['title'][lang]), esc(b['text'][lang]), extra, ' '.join(links)))
        site.extra_search.setdefault(lang, []).append({'u': url + '#a-' + b['id'], 't': sec['label'][lang], 'h': b['title'][lang], 'x': b['text'][lang][:360]})
    deeper = ''.join(card(site, q, lang, url, 'card--primary') for q in nav_groups(site, 'about'))
    main = '<h1>%s</h1><p class="o-lead">%s</p>%s<h2 class="about-deeper">%s</h2><ul class="o-grid card-list cards-primary">%s</ul>' % (
        esc(sec['label'][lang]), esc(sec['intro'][lang]), ''.join(blocks), esc(a['deeper'][lang]), deeper)
    return layout(site, p, lang, main, [])


def change_history(site, p, lang):
    rows = []
    for key in ['statement-of-intent', 'aicc-charter', 'business-model', 'operating-model', 'portfolio-management-model', 'solution-lifecycle-model', 'ai-policy', 'vocabulary', 'document-catalog']:
        path = 'charter/documents/%s.md' % key
        pre, secs, change = split_sections(read(path))
        fm = front_matter(pre)
        tbl = parse_table(change, '| Revision | Date | Change | Decision')
        page = site.file_page[path]
        for r in tbl:
            rows.append('<tr><td><a href="%s">%s</a></td><td>%s</td><td>%s</td><td lang="en">%s</td><td>%s</td></tr>' % (
                site.rel(site.url(p, lang), site.url(page, lang)), esc(h1_of(path)), esc(r['Revision']), esc(r['Date']), esc(r['Change']), esc(r['Decision'])))
    m = site.msg[lang]
    main = '<h1>%s</h1><div class="o-table-wrap" role="region" tabindex="0" aria-label="%s"><table><thead><tr><th>Document</th><th>%s</th><th>%s</th><th>Change</th><th>Decision</th></tr></thead><tbody>%s</tbody></table></div>%s' % (
        esc(p['title']), esc(p['title']), esc(m['revision']), esc(m['revised']), ''.join(rows), prev_next(site, p, lang))
    return layout(site, p, lang, main, [])


def records_page(site, p, lang):
    m = site.msg[lang]
    url = site.url(p, lang)
    by_tpl = {}
    for c in site.controls:
        t = re.sub(r'\s+', ' ', c['template']).strip()
        by_tpl.setdefault(t, []).append(c['ref'])
    rows = []
    for src, d in sorted(site.tpl_desc.items(), key=lambda kv: kv[1]['order']):
        page = site.file_page.get(src)
        controls = []
        for t, refs in by_tpl.items():
            if t and (t.lower() in d['name'].lower() or d['name'].lower() in t.lower()):
                controls += refs
        ctl = ', '.join('<a href="%s">%s</a>' % (site.rel(url, '/%s/governance/controls/%s/' % (lang, r.lower())), r) for r in sorted(set(controls)))
        rows.append('<tr><td><a href="%s">%s</a></td><td lang="en">%s</td><td lang="en"><code>%s</code></td><td>%s</td></tr>' % (
            site.rel(url, site.url(page, lang)), esc(d['name']), esc(d['used']), esc(d['kept'].strip('`')), ctl or '&ndash;'))
    systems = [('Registry', 'Decisions, appointments, controls, backlogs, roadmap, calendar, and other evidence records, as closed and dated extracts'),
               ('Jira and Confluence', 'The working state of the Program Backlog, boards, and Work Items, and the working documents, from the cutover of the working state'),
               ('Service Management', 'Requests and incidents, including AI Incidents')]
    srows = ''.join('<tr><th scope="row">%s</th><td lang="en">%s</td></tr>' % (esc(a), esc(b)) for a, b in systems)
    intro = {'en': 'This site is static. It states the rules and the forms of AICC and holds no live record. The table lists each record by its template, with the place where it is kept and the controls that it evidences.',
             'ru': 'Этот сайт статичен. Он излагает правила и формы AICC и не содержит текущих записей. В таблице перечислены записи по их шаблонам с указанием места хранения и контролей, которые они подтверждают.'}[lang]
    main = '<h1>%s</h1><p class="o-lead">%s</p><h2>Systems</h2><div class="o-table-wrap" role="region" tabindex="0" aria-label="Systems"><table><tbody>%s</tbody></table></div><h2>Records</h2><div class="o-table-wrap" role="region" tabindex="0" aria-label="Records"><table><thead><tr><th>Template</th><th>%s</th><th>%s</th><th>Controls</th></tr></thead><tbody>%s</tbody></table></div>%s' % (
        esc(p['title']), esc(intro), srows, esc(m['used_when']), esc(m['kept_in']), ''.join(rows), prev_next(site, p, lang))
    return layout(site, p, lang, main, [])


def controls_catalogue(site, p, lang):
    m = site.msg[lang]
    url = site.url(p, lang)
    types = sorted({c['type'] for c in site.controls if c['type']})
    opts = ''.join('<option value="%s">%s</option>' % (esc(t), esc(t)) for t in types)
    rows = []
    for c in site.controls:
        href = site.rel(url, '/%s/governance/controls/%s/' % (lang, c['ref'].lower()))
        rows.append('<tr data-type="%s"><td><a href="%s">%s</a></td><td lang="en">%s</td><td lang="en">%s</td><td lang="en">%s</td><td>%s</td></tr>' % (
            esc(c['type']), href, esc(c['ref']), esc(c['title']), esc(c['owner']), esc(c['when']), esc(c['type'])))
    return ('<section class="catalogue" aria-label="%s"><div class="o-toolbar"><div class="oc-field"><label for="cf">%s</label><input id="cf" class="oc-input" type="search" data-filter="ctl"></div>'
            '<div class="oc-field"><label for="ct">%s</label><select id="ct" class="oc-input" data-filter-type="ctl"><option value="">%s</option>%s</select></div></div>'
            '<div class="o-table-wrap" role="region" tabindex="0" aria-label="%s"><table id="ctl"><thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table></div>'
            '<p class="o-caption">%s</p></section>') % (
        esc(p['title']), esc(m['controls_filter']), esc(m['controls_type']), esc(m['controls_all']), opts, esc(p['title']),
        esc(m['control_ref']), esc(m['control_title']), esc(m['control_owner']), esc(m['control_when']), esc(m['control_type']), ''.join(rows), esc(m['control_status_note']))


def control_page(site, p, lang):
    c = p['control']
    m = site.msg[lang]
    url = site.url(p, lang)
    parent = site.by_id['governance/controls']
    facts = [('control_rule', c['rule']), ('control_owner', c['owner']), ('control_when', c['when']), ('control_evidence', c['evidence']), ('control_template', c['template']),
             ('control_objective', c['objective']), ('control_type', c['type']), ('control_test', c['test'])]
    dl = ''.join('<dt>%s</dt><dd lang="en">%s</dd>' % (esc(m[k]), site.link_xrefs(esc(v), {'source': 'charter/documents/operating-model.md', 'lang': lang, 'url': url})) for k, v in facts if v)
    idx = [x['ref'] for x in site.controls].index(c['ref'])
    pn = []
    if idx > 0:
        q = site.controls[idx - 1]
        pn.append('<a class="pn prev" href="%s"><span>%s</span>%s</a>' % (site.rel(url, '/%s/governance/controls/%s/' % (lang, q['ref'].lower())), esc(m['previous']), esc(q['ref'])))
    if idx + 1 < len(site.controls):
        q = site.controls[idx + 1]
        pn.append('<a class="pn next" href="%s"><span>%s</span>%s</a>' % (site.rel(url, '/%s/governance/controls/%s/' % (lang, q['ref'].lower())), esc(m['next']), esc(q['ref'])))
    main = '<h1 lang="en">%s</h1><p class="o-lead" lang="en">%s</p>%s<dl class="o-facts control-facts">%s</dl><p class="o-caption">%s</p><p><a href="%s">%s</a></p><nav class="o-pn">%s</nav>' % (
        esc(c['ref'] + ' ' + c['title']), esc(c['objective']), lang_note(site, lang), dl, esc(m['control_status_note']), site.rel(url, site.url(parent, lang)), esc(parent['title']), ''.join(pn))
    return layout(site, p, lang, main, [])


def roles_index(site, p, lang):
    url = site.url(p, lang)
    out = []
    for q in sorted([x for x in site.pages if x['type'] == 'role'], key=lambda x: x['order']):
        d = site.roles['om'].get(q['title'], {}).get('Does', '')
        out.append('<li class="o-card linked card--secondary" data-tip="%s"><h3><a href="%s">%s</a></h3><p class="card-desc" lang="en">%s</p></li>' % (esc(q.get('ref', '')), site.rel(url, site.url(q, lang)), esc(q['title']), esc(d)))
    main = '<h1>%s</h1><ul class="o-grid card-list">%s</ul>%s' % (esc(p['title']), ''.join(out), lang_note(site, lang))
    return layout(site, p, lang, main, [])


def role_page(site, p, lang):
    m = site.msg[lang]
    name = p['title']
    om = site.roles['om'].get(name, {})
    prof = site.roles['prof'].get(name, {})
    cols = {'Executive Sponsor': 'SP', 'AICC Lead': 'AL', 'Solution Engineer': 'SE', 'Domain Owner': 'DO', 'Domain Expert': 'DE', 'Control Function Contact': 'CFC', 'Platform Owner': 'PO'}
    col = cols.get(name)
    raci = [(r['Activity'], r.get(col, '')) for r in site.roles['raci'] if col and r.get(col)]
    dl = ''
    for k, v in (('Purpose', prof.get('Purpose')), ('Main responsibilities', prof.get('Main responsibilities')), ('Authority', prof.get('Authority')), ('Reports in', prof.get('Reports in')), ('Typical competence', prof.get('Typical competence'))):
        if v:
            dl += '<dt>%s</dt><dd lang="en">%s</dd>' % (esc(k), esc(v))
    rows = ''.join('<tr><td lang="en">%s</td><td>%s</td></tr>' % (esc(a), esc(r)) for a, r in raci)
    om_page = site.section_page[('charter/documents/operating-model.md', 4)]
    main = '<h1>%s</h1><p class="o-lead" lang="en">%s</p>%s<h2>%s</h2><dl class="o-facts">%s</dl><h2>%s</h2><p lang="en">%s</p><h2>%s</h2><div class="o-table-wrap" role="region" tabindex="0" aria-label="RACI"><table><thead><tr><th>Activity</th><th>R / A / C / I</th></tr></thead><tbody>%s</tbody></table></div><p><a href="%s#c-4-2">Operating Model 4.2</a></p>' % (
        esc(name), esc(om.get('Does', '')), lang_note(site, lang), esc(m['role_profile']), dl, esc(m['role_decides']), esc(om.get('Decides', '')), esc(m['role_raci']), rows,
        site.rel(site.url(p, lang), site.url(om_page, lang)))
    return layout(site, p, lang, main, [])


def build_page(site, p, lang):
    t = p['type']
    if t == 'home':
        return home_page(site, p, lang)
    if p['id'] == 'about/index':
        return about_page(site, p, lang)
    if t == 'section':
        return section_page(site, p, lang)
    if p['id'] == 'about/values-and-principles':
        return values_page(site, p, lang)
    if p['id'] == 'reference/change-history':
        return change_history(site, p, lang)
    if p['id'] == 'reference/records-and-systems':
        return records_page(site, p, lang)
    if p['id'] == 'organization/roles':
        return roles_index(site, p, lang)
    if t == 'role':
        return role_page(site, p, lang)
    if t == 'control':
        return control_page(site, p, lang)
    return content_page(site, p, lang)


# ---------------------------------------------------------------- search and output

def plain(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def search_index(site, lang):
    out = list(site.extra_search.get(lang, []))
    for p in site.pages:
        u = site.url(p, lang)
        if p['id'] in site.bodies:
            for c in site.bodies[p['id']]['chunks']:
                txt = re.sub(r'\s+', ' ', re.sub(r'[*_`|]|\[([^\]]*)\]\([^)]*\)', lambda m: m.group(1) or ' ', c['text'])).strip()
                out.append({'u': u + '#' + c['anchor'], 't': p['title'], 'h': c['heading'], 'x': txt[:360]})
        if p['type'] == 'control':
            c = p['control']
            out.append({'u': u, 't': p['title'], 'h': c['ref'], 'x': ' '.join([c['objective'], c['rule'], c['owner'], c['test']])[:360]})
        if p['type'] == 'role':
            out.append({'u': u, 't': p['title'], 'h': p['title'], 'x': site.roles['om'].get(p['title'], {}).get('Does', '')[:360]})
        if p['type'] == 'section':
            sec = site.auth['sections'][p['section']]
            out.append({'u': u, 't': sec['label'][lang], 'h': sec['label'][lang], 'x': sec['intro'][lang]})
    return out


def copy_assets():
    dst = os.path.join(OUT, 'assets')
    shutil.rmtree(dst, ignore_errors=True)
    os.makedirs(os.path.join(dst, 'ui'))
    for f in ('fonts.css', 'tokens.css', 'primitives.css', 'workspace.css'):
        shutil.copy(os.path.join(PORTAL, 'ui', f), os.path.join(dst, 'ui', f))
    for d in ('fonts', 'logos', 'licenses'):
        src = os.path.join(PORTAL, 'ui', 'assets', d)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(dst, 'ui', 'assets', d))
    shutil.copy(os.path.join(PORTAL, 'ui', 'assets', 'FONT-USE.md'), os.path.join(dst, 'ui', 'assets', 'FONT-USE.md'))
    shutil.copy(os.path.join(PORTAL, 'site', 'charter.css'), os.path.join(dst, 'charter.css'))
    shutil.copy(os.path.join(PORTAL, 'site', 'site.js'), os.path.join(dst, 'site.js'))


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def gateway():
    links = ''.join('<li><a lang="%s" hreflang="%s" href="%s/">%s</a></li>' % (l, l, l, {'en': 'English', 'ru': 'Русский'}[l]) for l in LANGS)
    return f'''<!doctype html>
<html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark"><meta http-equiv="refresh" content="0; url={DEFAULT_LANG}/">
<title>AI Competence Center</title>
<link rel="stylesheet" href="assets/ui/fonts.css"><link rel="stylesheet" href="assets/ui/tokens.css"><link rel="stylesheet" href="assets/ui/workspace.css"><link rel="stylesheet" href="assets/charter.css">
</head><body class="charter"><main class="o-main gateway" id="main"><img src="assets/ui/assets/logos/o-mark.svg" width="48" height="54" alt="">
<h1>AI Competence Center</h1><ul>{links}</ul></main></body></html>
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--no-diagrams', action='store_true')
    args = ap.parse_args()
    site = Site(args)
    add_generated_pages(site)
    assign_refs(site)
    load_terms(site)
    diagrams = render_pages(site)
    site.diagram_code = {k: c for k, c in diagrams}
    site.svgs = render_diagrams(diagrams, not args.no_diagrams)
    missing = [k for k, v in site.svgs.items() if not v]
    if missing:
        print('warning: %d diagram(s) not rendered' % len(missing), file=sys.stderr)
    # clean output
    for d in LANGS + ['assets']:
        shutil.rmtree(os.path.join(OUT, d), ignore_errors=True)
    os.makedirs(OUT, exist_ok=True)
    copy_assets()
    count = 0
    for lang in LANGS:
        for p in sorted(site.pages, key=lambda x: x['id']):
            page = build_page(site, p, lang)
            page = page.replace('@@NOLINK@@', '#')
            rel = site.url(p, lang).strip('/')
            write(os.path.join(OUT, rel, 'index.html'), page)
            count += 1
        write(os.path.join(OUT, 'assets', 'search-%s.json' % lang), json.dumps(search_index(site, lang), ensure_ascii=False, separators=(',', ':')))
    write(os.path.join(OUT, 'index.html'), gateway())
    print('built %d pages, %d diagrams (%d not rendered)' % (count, len(site.svgs), len(missing)))


if __name__ == '__main__':
    main()
