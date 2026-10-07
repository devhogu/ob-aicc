#!/usr/bin/env python3
"""Build the AICC charter site (html/aicc) from the charter Markdown.

Source of the content: charter/en/**/*.md. Source of the structure: portal-scaffolding/sitemap.json.
Source of the chrome: portal/ui (the O! UI/UX kit), portal/site, portal/messages, portal/content.
Output: html/aicc/{index.html, en/, ru/, assets/}: the gateway, the language routers at {lang}/, and the
Center branch at {lang}/center/; the other branches are composed by neighbours.py. The output is generated and is never edited by hand.

Usage: python3 portal/tools/build.py [--no-diagrams]
"""
import argparse
import concurrent.futures
import glob
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys

from markdown_it import MarkdownIt
import workspace
from localization import Sources, canonical_path, front_matter, validate_translations

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PORTAL = os.path.join(ROOT, 'portal')
OUT = os.path.join(ROOT, 'html', 'aicc')
SITEMAP = os.path.join(ROOT, 'portal-scaffolding', 'sitemap.json')
CACHE = os.path.join(PORTAL, '.cache', 'mermaid-v6')
NPX = os.environ.get('MMDC_NPX', os.path.expanduser('~/.npm/_npx/668c188756b835f3/node_modules'))
CHROME = os.environ.get('MMDC_CHROME', os.path.expanduser('~/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'))
FONT_FILE = os.path.join(PORTAL, 'ui', 'assets', 'fonts', 'golos-text', 'GolosText-variable.woff2')
# where the charter and the Registry are published, on the corporate folder; a full copy of charter/en/ and registry/en/ of this repository.
# The link opens the share where the browser allows it, and the UNC path is offered for copying.
SHARE_HOST = '10.128.20.244'
CHARTER_BASE = 'smb://%s/aicc/governance/charter/' % SHARE_HOST
REGISTRY_BASE = 'smb://%s/aicc/governance/registry/' % SHARE_HOST


def unc(base_url, rel=''):
    """The UNC form of a share address, for copying on Windows: \\\\host\\share\\path."""
    path = base_url.split('://', 1)[1] + rel
    return '\\\\' + path.replace('/', '\\').rstrip('\\')
PREFIX = {'about': 'ABT', 'responsible-ai': 'RAI', 'services': 'SRV', 'portfolio': 'PFL', 'delivery': 'DLV', 'governance': 'GOV', 'organization': 'ORG', 'knowledge-base': 'KNB', 'reference': 'REF'}
LANGS = ['en', 'ru']
DEFAULT_LANG = 'en'
BASELINE = {'revision': '2.2', 'date': '2026-10-03'}  # English source edition; documents retain their own revisions.

FONTS = os.path.join(ROOT, 'portal', '.tools', 'pw-syslibs')
SHORT = {'Statement of Intent on the Adoption of Artificial Intelligence': 'Statement of Intent', 'Vocabulary and Style': 'Vocabulary', 'Portfolio and service delivery workflow': 'Service delivery workflow'}
SHORT['Заявление о намерениях по внедрению AI'] = 'Заявление о намерениях'
NAV_SHORT = {'AICC Charter': 'Charter', 'Portfolio measures: definitions and formulas': 'Portfolio measures', 'Delivery measures: definitions and formulas': 'Delivery measures',
             'Portfolio and service delivery workflow': 'Service delivery workflow'}      # shorter in the left navigation
PAGE_TITLE = {'AICC Charter': 'AI Competence Center Charter'}      # fuller as the page title


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
LOCALXREF = re.compile(r'\b(sections?|clause|раздел(?:а|е|ы|ов)?|пункт(?:а|е|ы|ов)?)\s+(\d+(?:\.\d+)*)', re.I)
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
        if title in ('Change log', 'Журнал изменений', 'История изменений'):
            change = block
            continue
        m = re.match(r'(\d+)\.\s+(.*)', title)
        secs.append((int(m.group(1)) if m else None, m.group(2) if m else title, block))
    return pre, secs, change


def slug(s):
    s = re.sub(r'[^\w]+', '-', s.lower(), flags=re.UNICODE).strip('-')
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
                        and re.match(r'(?:Figure|Рисунок) \d+', tokens[i + 2].content)):
                    cap = tokens[i + 2].content
                    skip = 3
                else:
                    skip = 0
                key = hashlib.sha1(t.content.encode('utf-8')).hexdigest()[:12]
                diagrams.append((key, t.content))
                label = cap or self.site.msg[page_ctx['lang']].get('diagram_label', 'Diagram')
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
        table_label = esc(self.site.msg[page_ctx['lang']].get('table_label', 'Table'))
        html_out = html_out.replace('<table>', '<div class="o-table-wrap" role="region" tabindex="0" aria-label="%s"><table>' % table_label).replace('</table>', '</table></div>')
        # permalink on clauses
        html_out = re.sub(r'<p id="(c-[0-9-]+)" class="clause">', lambda m: '<p id="%s" class="clause"><a class="permalink" href="#%s" aria-label="@@PERMALINK@@">&para;</a>' % (m.group(1), m.group(1)), html_out)
        return html_out, outline, chunks, anchors, diagrams


# ---------------------------------------------------------------- mermaid

def wrap_label(text, width=42):
    """Break the lines of a node label at word boundaries, so that no line is wider than the box the renderer draws for it."""
    out = []
    for seg in text.split('<br/>'):
        words, line = seg.split(' '), ''
        for w in words:
            if line and len(line) + 1 + len(w) > width:
                out.append(line)
                line = w
            else:
                line = (line + ' ' + w).strip()
        out.append(line)
    return '<br/>'.join(out)


def prep_mermaid(code):
    """Give the diagrams their shapes: a gate is a hexagon, and the classes are styled by the theme, not by the source; wrap long label lines."""
    if not code.lstrip().startswith(('flowchart', 'graph')):
        return code
    lines = []
    for l in code.split('\n'):
        if l.lstrip().startswith('subgraph '):
            lines.append(l)
            continue
        lines.append(re.sub(r'"([^"]*)"', lambda m: '"%s"' % wrap_label(m.group(1)), l))
    code = '\n'.join(lines)
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

def russian_reference_names(title):
    """Recognize inflected document titles without changing their corpus wording."""
    names = {title}
    prefixes = {
        'Операционная модель': ('Операционной модели', 'Операционную модель', 'Операционной моделью'),
        'Бизнес-модель': ('Бизнес-модели', 'Бизнес-моделью'),
        'Модель ': ('Модели ', 'Моделью '),
        'Каталог ': ('Каталога ', 'Каталоге ', 'Каталогу ', 'Каталогом '),
        'Положение ': ('Положения ', 'Положении ', 'Положению ', 'Положением '),
        'Политика ': ('Политики ', 'Политике ', 'Политику ', 'Политикой '),
        'Заявление ': ('Заявления ', 'Заявлении ', 'Заявлению ', 'Заявлением '),
        'Терминология и стиль': ('Терминологии и стиля', 'Терминологии и стиле', 'Терминологию и стиль', 'Терминологией и стилем'),
    }
    for prefix, forms in prefixes.items():
        if title.startswith(prefix):
            names.update(form + title[len(prefix):] for form in forms)
            break
    return names


class Site:
    def __init__(self, args, language='en'):
        self.args = args
        self.language = language
        self.sources = Sources(ROOT, language)
        self.english_sources = Sources(ROOT, 'en')
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
            if p['type'] in ('document', 'workflow', 'guide', 'template', 'catalogue', 'reference', 'outline', 'service', 'legal', 'regulation') and p.get('source') and not p.get('source_sections'):
                self.file_page.setdefault(p['source'][0], p)
            if p['id'] == 'about/charter-outline':
                self.file_page['charter/en/README.md'] = p
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
        for p in self.pages:
            p['english_title'] = p['title']
            p['content_language'] = 'en'
            if p.get('source') and p['type'] not in ('role', 'home', 'control', 'index', 'records'):
                selected = self.sources.resolve(p['source'][0])
                p['content_language'] = selected.language
                if selected.language != 'en':
                    title = h1_of(selected.path)
                    if p.get('source_sections'):
                        _, sections, _ = split_sections(selected.text)
                        section_title = '; '.join(t for n, t, _ in sections if n in p['source_sections'])
                        section_title = self.msg[language].get('part_titles', {}).get(p['id'], section_title)
                        first_part = p.get('part', '').startswith('1 of')
                        if p.get('series') and p['type'] in ('document', 'catalogue', 'guide', 'workflow'):
                            p['series_title'] = title
                            p['tab'] = self.msg[language]['foundations'] if first_part else section_title
                        if not first_part:
                            part_title = re.sub(r'^(?:Guide|Руководство):\s*', '', section_title) if p['type'] == 'guide' else section_title
                            subject = re.sub(r'^(?:Guide|Руководство):\s*', '', title)
                            if part_title.casefold() != subject.casefold():
                                title = disp(title) + ': ' + part_title
                    elif p.get('series'):
                        p['tab'] = self.msg[language].get('part_titles', {}).get(p['id'], title)
                    p['title'] = title or p['title']

        for p in self.pages:
            if p['id'] == 'index':
                p['title'] = self.auth['home']['title'][language]
            elif p['id'] == 'about/index':
                p['title'] = self.auth['sections']['about']['label'][language]
            p['title'] = self.msg[language].get('page_titles', {}).get(p['id'], p['title'])
            if p.get('series'):
                p['series_title'] = self.msg[language].get('series_titles', {}).get(p['series'], p.get('series_title', p['title']))

        self.doc_names = dict(DOC_NAMES)
        catalog_path = 'charter/en/documents/document-catalog.md'
        catalog_titles = {r['Identifier']: r['Title'] for r in self.sources.table(catalog_path, '| Identifier | Title | Purpose', ('Identifier',))}
        for name in set(DOC_NAMES.values()):
            source = self.sources.resolve('charter/en/documents/%s.md' % name)
            if source.language != 'en':
                self.doc_names[h1_of(source.path)] = name
            if self.language == 'ru' and self.sources.resolve(catalog_path).language == 'ru':
                identifier = source.metadata['id'].rsplit('-', 1)[0]
                title = catalog_titles.get(identifier)
                if title:
                    titles = [title]
                    if name == 'statement-of-intent':
                        titles.append(title.split(' по ', 1)[0])
                    for title in titles:
                        self.doc_names.update((alias, name) for alias in russian_reference_names(title))
        names = '|'.join(re.escape(name) for name in sorted(self.doc_names, key=len, reverse=True))
        self.xref = re.compile(r'\b(' + names + r')(?:\s*,\s*(?:раздел(?:ы|а|е|ов)?|пункт(?:ы|а|е|ов)?)\s+|\s+)(\d+(?:\.\d+)*)((?:\([a-z]\))?)')
        # Russian order puts the number first: «пункт 4.4 Операционной модели», «раздел 4 Бизнес-модели».
        self.xref_rev = re.compile(r'(?<![\w-])(?:раздел(?:ы|а|е|у|ом|ов)?|пункт(?:ы|а|е|у|ом|ов)?|[Пп]п?\.|[Рр]азд\.)\s+(\d+(?:\.\d+)*)((?:\([a-z]\))?)(?:(?:,\s*|\s+и\s+)\d+(?:\.\d+)*(?:\([a-z]\))?)*\s+(' + names + r')(?![\w-])')

    def combined_sources(self, paths):
        # Generated views require all their source fragments in the same language.
        return self.sources if all(self.sources.resolve(p).language == self.language for p in paths) else self.english_sources

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
        for r in self.sources.table('charter/en/documents/document-catalog.md', '| Identifier | Title | Purpose', ('Title',)):
            desc[r['Title']] = r['Purpose']
        self.doc_desc = desc
        wf = {}
        for l in self.sources.text('charter/en/workflows/README.md').splitlines():
            m = re.match(r'\| \[[^\]]*\]\(([a-z\-]+)\.md\) \| (.*?) \| (.*?) \|', l)
            if m:
                wf['charter/en/workflows/%s.md' % m.group(1)] = (m.group(2), m.group(3))
        self.wf_desc = wf
        gd = {}
        for l in self.sources.text('charter/en/guides/README.md').splitlines():
            m = re.match(r'\| \[[^\]]*\]\(([a-z\-]+)\.md\) \| (.*?) \| (.*?) \|', l)
            if m:
                gd['charter/en/guides/%s.md' % m.group(1)] = (m.group(2), m.group(3))
        self.gd_desc = gd
        tp = {}
        for r in self.sources.table('charter/en/templates/README.md', '| Order | Id | Template | File', ('Template', 'File')):
            m = re.search(r'\]\(([a-z\-]+)\.md\)', r['File'])
            if m:
                tp['charter/en/templates/%s.md' % m.group(1)] = {'order': int(r['Order']), 'name': r['_localized_Template'], 'canonical_name': r['Template'], 'used': r['Used when'], 'kept': r['Kept in']}
        self.tpl_desc = tp

    # ----- urls
    def url(self, page, lang):
        # The charter pages form the Center branch: /{lang}/center/ is its home.
        return '/%s/center%s' % (lang, page['slug'])

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
        if href and href.startswith('page:'):
            pid, frag = (href[5:].split('#', 1) + [''])[:2]
            page = self.by_id.get(pid) or self.by_id.get(pid + '/index')
            if page is None:
                return '@@NOLINK@@'
            return self.rel(ctx['url'], self.url(page, ctx['lang']) + ('#' + frag if frag else ''))
        if not href or href.startswith('#') or re.match(r'^[a-z]+:', href):
            return href
        path, frag = (href.split('#', 1) + [''])[:2]
        base = os.path.dirname(ctx['source'])
        target = os.path.normpath(os.path.join(base, path)).replace('\\', '/')
        page = self.file_page.get(canonical_path(target))
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
        key = 'charter/en/documents/%s.md' % docstem
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
            href = self._target(self.doc_names[m.group(1)], m.group(2), ctx)
            if not href:
                return m.group(0)
            return '<a class="xref" href="%s">%s</a>' % (href, m.group(0))
        def sub2(m):
            if not stem_here or not stem_here in self.doc_names.values():
                return m.group(0)
            href = self._target(stem_here, m.group(2), ctx)
            if not href:
                return m.group(0)
            return '<a class="xref" href="%s">%s</a>' % (href, m.group(0))
        # Resolve local references only outside complete document references.
        # Otherwise «Операционная модель, раздел 4» could link «раздел 4»
        # to the current document and nest that link inside the document link.
        def sub_rev(m):
            href = self._target(self.doc_names[m.group(3)], m.group(1), ctx)
            if not href:
                return m.group(0)
            return '<a class="xref" href="%s">%s</a>' % (href, m.group(0))
        matches = [(m.start(), m.end(), sub, m) for m in self.xref.finditer(text)]
        matches += [(m.start(), m.end(), sub_rev, m) for m in getattr(self, 'xref_rev', re.compile(r'(?!)')).finditer(text)]
        out = []
        end = 0
        for start, stop, fn, match in sorted(matches, key=lambda x: (x[0], -x[1])):
            if start < end:
                continue
            out.append(LOCALXREF.sub(sub2, text[end:start]))
            out.append(fn(match))
            end = stop
        out.append(LOCALXREF.sub(sub2, text[end:]))
        return ''.join(out)


# ---------------------------------------------------------------- page bodies

ICONS = {}


def icon(name):
    if name not in ICONS:
        p = os.path.join(PORTAL, 'ui', 'assets', 'icons', 'ui-%s.svg' % name)
        if os.path.exists(p):
            with open(p, encoding='utf-8') as handle:
                s = handle.read()
            s = re.sub(r'\s+', ' ', s)
            s = s.replace('<svg ', '<svg class="o-icon" aria-hidden="true" focusable="false" ', 1)
            ICONS[name] = s
        else:
            ICONS[name] = ''
    return ICONS[name]


def source_text(p, source=None):
    text = source.text if source else read(p['source'][0])
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


def lead_of(path):
    """The first paragraph of an authored page, after its title: its description on cards and in the navigation."""
    body = re.sub(r'^```yaml\n.*?```\s*', '', read(path), count=1, flags=re.S).split('\n## ', 1)[0]
    paras = [x.strip() for x in re.sub(r'^# .*$', '', body, flags=re.M).split('\n\n') if x.strip()]
    return re.sub(r'\s+', ' ', paras[0]) if paras else ''


def h1_of(path):
    for l in read(path).splitlines():
        if l.startswith('# '):
            return l[2:].strip()
    return ''


def add_generated_pages(site):
    """Control pages, one for each control of Operating Model 8, are added to the page set."""
    om_path = 'charter/en/documents/operating-model.md'
    guide_path = 'charter/en/guides/unit-governance-guide.md'
    control_sources = site.combined_sources([om_path, guide_path])
    site.control_language = control_sources.resolve(om_path).language
    rows = control_sources.table(om_path, '| Ref | Control | Rule | Owner', ('Ref', 'Template'))
    grows = {r['Ref']: r for r in control_sources.table(guide_path, '| Ref | Control | Objective | Type', ('Ref',))}
    site.controls = []
    for r in rows:
        g = grows.get(r['Ref'], {})
        c = {'ref': r['Ref'], 'title': r['Control'], 'rule': r['Rule'], 'owner': r['Owner'], 'when': r['When'],
             'evidence': r['Evidence record'], 'template': r['_localized_Template'], 'canonical_template': r['Template'], 'objective': g.get('Objective', ''),
             'type': g.get('Type', ''), 'test': g.get('How to test', '')}
        site.controls.append(c)
        pid = 'governance/controls/' + r['Ref'].lower()
        site.pages.append({'id': pid, 'section': 'governance', 'order': 200 + len(site.controls), 'type': 'control', 'slug': '/governance/controls/%s/' % r['Ref'].lower(),
                           'title': '%s %s' % (r['Ref'], r['Control']), 'source': ['charter/en/documents/operating-model.md', 'charter/en/guides/unit-governance-guide.md'],
                           'production': 'generated', 'control': c})
    site.by_id = {p['id']: p for p in site.pages}
    og_path = 'charter/en/guides/organization-guide.md'
    role_sources = site.combined_sources([om_path, og_path])
    site.role_language = role_sources.resolve(om_path).language
    site.roles = {'om': {r['Role']: r for r in role_sources.table(om_path, '| Role | Does | Decides', ('Role',))},
                  'prof': {r['Role']: r for r in role_sources.table(og_path, '| Role | Purpose | Main responsibilities', ('Role',))},
                  'raci': role_sources.table(og_path, '| Activity | SP |')}
    for p in site.pages:
        if p['type'] == 'role':
            original = p.get('english_title', p['title'])
            p['title'] = site.roles['om'].get(original, {}).get('_localized_Role', original)
            p['content_language'] = site.role_language
        elif p['type'] == 'control':
            p['content_language'] = site.control_language
        elif p['id'] == 'organization/roles':
            p['title'] = site.msg[site.role_language]['roles_title']
            p['content_language'] = site.role_language


def assign_refs(site):
    """Every page has a short id that readers quote when they ask about it. It comes from the stable identifier of the page in the sitemap, so it does not change when pages are added."""
    taken = set()
    for q in sorted(site.pages, key=lambda x: x['id']):
        q['ref'] = workspace.short_id(q['id'], taken)


def vocabulary_entries(site, source):
    """Keep concept, state and stage search targets distinct when names coincide."""
    entries, seen = [], set()
    for header, key in (('| Term | Meaning', 'Term'), ('| State | Meaning', 'State'), ('| Stage | Level', 'Stage')):
        for row in site.sources.table(source, header):
            label = row[key]
            anchor = 't-' + slug(label)
            if anchor in seen:
                anchor = 't-' + key.lower() + '-' + slug(label)
                label += ' (' + row['_labels'][key] + ')'
            seen.add(anchor)
            entries.append({'anchor': anchor, 'label': label, 'meaning': row['Meaning']})
    return entries


RU_COMMON_WORD_TERMS = {
    'Термин', 'Банк', 'Роль', 'Направление', 'Модель', 'Режим', 'Фаза', 'Пакет', 'Каталог', 'Решение', 'Сервис',
    'Продукт', 'Получатель', 'Передача', 'Предложение', 'Задача', 'Команда', 'Зависимость', 'Календарь', 'Стадия',
    'Проверка', 'Проверяющий', 'Приёмка', 'Выпуск', 'Показатель', 'Шаблон', 'Реестр', 'Запись',
    'Переход', 'Цикл', 'Сокращения', 'Мероприятие', 'Состояние', 'Реализация', 'Определение', 'Анализ',
    'Версия',
}


def load_terms(site):
    rows = site.sources.table('charter/en/documents/vocabulary.md', '| Term | Meaning')
    terms = {}
    for r in rows:
        t = r['Term'].strip()
        mean = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', r['Meaning'])
        mean = re.sub(r'[*`]', '', mean).strip()
        if len(t) >= 3 and mean:
            terms[t] = mean if len(mean) <= 300 else mean[:297].rsplit(' ', 1)[0] + '...'
    if site.language == 'ru':
        # In Russian these defined terms are also everyday words (решение, задача, направление работы, модель
        # обслуживания); a tooltip on the first such word would often explain the wrong sense, so they are not linked.
        for t in RU_COMMON_WORD_TERMS:
            terms.pop(t, None)
    site.terms = terms
    # Russian terms are written in lowercase in running text; the table cell starts with a capital.
    def alt(t):
        if re.match(r'[А-ЯЁ][а-яё]', t):
            return '[%s%s]' % (t[0], t[0].lower()) + re.escape(t[1:])
        return re.escape(t)
    site.term_re = re.compile(r'(?<![\w-])(' + '|'.join(alt(t) for t in sorted(terms, key=len, reverse=True)) + r')(?![\w-])')


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
            key = t if t in site.terms else t[:1].upper() + t[1:]
            if key in seen or len(seen) >= limit:
                return t
            seen.add(key)
            return '<a class="term" href="%s#t-%s" data-tip="%s" data-tip-title="%s">%s</a>' % (base, slug(key), esc(site.terms[key]), esc(key), t)
        out.append(site.term_re.sub(sub, part))
    return ''.join(out)


def description_language(site, p):
    source = (p.get('source') or [''])[0]
    if p['type'] == 'role' or p['id'] == 'organization/roles':
        return site.role_language
    catalog = {'workflow': 'workflows', 'guide': 'guides', 'template': 'templates'}.get(p['type'])
    if catalog:
        return site.sources.resolve('charter/en/%s/README.md' % catalog).language
    if p['type'] in ('document', 'reference') and len(p.get('source', [])) == 1 and (not p.get('source_sections') or p.get('part', '').startswith('1 of')):
        if site.doc_desc.get(h1_of(source)):
            return site.sources.resolve('charter/en/documents/document-catalog.md').language
    if p['type'] == 'legal' and p['id'] in site.msg[site.language].get('page_descriptions', {}):
        return site.language
    if source and (p.get('source_sections') or source.startswith('portal/content/')):
        return site.sources.resolve(source).language
    if p['id'] in site.msg[site.language].get('page_descriptions', {}):
        return site.language
    return 'en'


def desc_of(site, p):
    src = (p.get('source') or [None])[0]
    if p['type'] in ('document', 'reference') and len(p.get('source', [])) == 1:
        if (not p.get('source_sections')) or p.get('part', '').startswith('1 of'):
            d = site.doc_desc.get(h1_of(src))
            if d:
                return d
        if p.get('source_sections'):
            pre, ss, ch = split_sections(site.sources.text(src))
            return '; '.join(t for n, t, b in ss if n in p['source_sections'])
    if p['type'] == 'catalogue' and p.get('source_sections'):
        pre, ss, ch = split_sections(site.sources.text(src))
        return '; '.join(t for n, t, b in ss if n in p['source_sections'])
    if p['type'] == 'workflow' and src in site.wf_desc:
        return site.wf_desc[src][0]
    if p['type'] == 'guide' and src in site.gd_desc:
        return site.gd_desc[src][0]
    if p['type'] == 'template' and src in site.tpl_desc:
        return site.tpl_desc[src]['used']
    if p['type'] == 'role':
        return site.roles['om'].get(p.get('english_title', p['title']), {}).get('Does', '')
    if src and src.startswith('portal/content/en/') and p['type'] != 'legal':
        return lead_of(site.sources.resolve(src).path)
    if p['id'] == 'organization/roles':
        return site.msg[site.role_language]['roles_description']
    fixed = {
        'about/charter-outline': 'How the charter is organized on this site, where each part is, and where to start',
        'knowledge-base/guides': 'The five guides in one place: who does what, when, and what is left on record, each beside its workflow',
        'about/strategy': 'The strategy of the Bank, the Strategic Priorities, the strategic choices across every aspect of AICC, and the road of Maturity Levels',
        'about/values-and-principles': 'The values and the principles of adoption, application, work, and delivery, and what each applies to',
        'reference/vocabulary': 'The defined terms of the charter and its style',
        'reference/change-history': 'The revision history of the documents',
        'reference/records-and-systems': 'Where each record is kept, and which control it evidences',
        'organization/roles': 'The seven Roles and their pages',
        'privacy': 'What this site does, and does not do, with information about the persons who use it',
        'terms-of-use': 'The conditions under which this site is made available, and the standing of its pages',
    }
    return site.msg[site.language].get('page_descriptions', {}).get(p['id'], fixed.get(p['id'], ''))


def render_pages(site):
    diagrams = []
    for p in site.pages:
        t = p['type']
        if t == 'section' and p.get('series') and p.get('source'):
            pass
        elif p['id'] in ('reference/change-history', 'about/values-and-principles', 'about/charter-outline', 'about/strategy', 'reference/records-and-systems', 'organization/roles', 'index') or t in ('section', 'home', 'role', 'control', 'index', 'records'):
            continue
        if not p.get('source'):
            continue
        if p['id'] == 'about/charter-outline':
            body = re.sub(r'^# .*$', '', read('charter/en/README.md'), count=1, flags=re.M).strip()
            fm, change, raw = {}, '', body
            src = 'charter/en/README.md'
        else:
            body, fm, change, raw = source_text(p, site.sources.resolve(p['source'][0]))
            src = p['source'][0]
        selected = site.sources.resolve(src)
        p['content_language'] = selected.language
        p_ctx = {'source': selected.path, 'lang': site.language, 'url': site.url(p, site.language)}
        h, outline, chunks, anchors, dg = site.md.render(body, p_ctx)
        site.bodies[p['id']] = {'html': h, 'outline': outline, 'chunks': chunks, 'anchors': anchors, 'fm': fm, 'change': change, 'raw': raw, 'src': selected.path, 'language': selected.language}
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
        if p.get('series'):
            if p['series'] in seen:
                continue
            seen.add(p['series'])
        items.append(p)
    return items


def nav_title(site, p):
    # A page may carry a shorter name for the left navigation, per language.
    short = site.msg[site.language].get('nav_short', {}).get(p['id'])
    if short:
        return short
    if p.get('series'):
        return p.get('series_title') or p['title']
    if p.get('source_sections') and p.get('document') and p['id'] != 'governance/delivery-records-controls-and-measures':
        t = disp(h1_of(site.sources.resolve(p['source'][0]).path)) if p['type'] != 'catalogue' else disp(p['title'])
    else:
        t = disp(p['title'])
    return NAV_SHORT.get(t, t)


def doc_parts(site, p):
    if not p.get('document'):
        return []
    return sorted([x for x in site.pages if x.get('document') == p['document'] and x['source'][0] == p['source'][0] and x['type'] in ('document', 'catalogue', 'workflow', 'guide')],
                  key=lambda x: (x['section'] != p['section'], x['order'], x['id']))


def asset_version(name):
    """A short content hash of a site asset, appended to its address so that a browser fetches a changed file instead of a cached one."""
    path = os.path.join(PORTAL, 'site', name)
    with open(path, 'rb') as handle:
        return hashlib.sha1(handle.read()).hexdigest()[:8]


def layout(site, p, lang, main_html, outline):
    m = site.msg[lang]
    vcss = asset_version('charter.css')
    url = site.url(p, lang)
    A = site.assets(url)
    home = site.rel(url, site.url(site.by_id['index'], lang))
    other = [l for l in LANGS if l != lang][0]
    nav = ['<a href="%s"%s>%s<span>%s</span></a>' % (home, ' aria-current="page"' if p['id'] == 'index' else '', icon('map'), esc(m['home']))]
    for s in site.sections:
        sec = site.auth['sections'][s['id']]
        sp = site.by_id[s['id'] + '/index']
        href = site.rel(url, site.url(sp, lang))
        here = p.get('section') == s['id']
        cur = ' aria-current="page"' if p['id'] == sp['id'] else (' aria-current="true"' if here else '')
        nav.append('<a href="%s"%s>%s<span>%s</span></a>' % (href, cur, icon(sec['icon']), esc({'portfolio': {'en': 'Portfolio management', 'ru': 'Управление портфелем'}, 'delivery': {'en': 'Delivery model', 'ru': 'Модель реализации'}}.get(s['id'], {}).get(lang, sec['label'][lang]))))
        if here:
            sub = []
            items = nav_groups(site, s['id'])
            ids = {x['id'] for x in items}
            nested = {x['companion']: x for x in items if x['type'] == 'guide' and x.get('companion') in ids}

            def link(q, cls=''):
                qh = site.rel(url, site.url(q, lang))
                active = q['id'] == p['id'] or (q.get('document') and q.get('document') == p.get('document') and q['source'][0] == (p.get('source') or [''])[0]) or (q.get('series') and q.get('series') == p.get('series'))
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
                if q['type'] in ('template', 'regulation', 'service'):
                    continue
                if q.get('series') and q.get('series') == sp.get('series'):
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
        bc = '<div class="crumbbar%s"><div class="crumbline">%s<a class="crumb-next" href="%s" rel="next"><span>%s:</span> <strong>%s</strong> &rsaquo;</a></div></div>' % (
            ' has-ctx' if outline else '', bc, site.rel(url, site.url(nx, lang)), esc(m['next']), esc(flow_label(site, nx, lang)))
    ctx = ''
    if outline:
        links = ''.join('<a class="lv%d" href="#%s">%s</a>' % (lv, i, esc(t)) for lv, i, t in outline)
        ctx = '<aside class="o-context" aria-label="%s"><strong>%s</strong>%s</aside>' % (esc(m['on_this_page']), esc(m['on_this_page']), links)
    reading = '<div class="o-reading"><div class="o-copy">%s</div>%s</div>' % (main_html, ctx) if ctx else '<div class="o-wide">%s</div>' % main_html
    ref = p.get('ref', '')
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
<link rel="stylesheet" href="{A}/charter.css?v={vcss}">
<link rel="stylesheet" href="{workspace.asset(url, 'neighbours.css')}">
<link rel="alternate" hreflang="{other}" href="{site.rel(url, site.url(p, other))}">
{workspace.script(url, lang, 'center', m)}
</head>
<body class="charter" data-portal-section="center">
<a class="o-skip" href="#main">{esc(m['skip'])}</a>
{workspace.header(url, lang, 'center', m)}
<div class="o-frame">
  {workspace.navigation(url, lang, 'center', ''.join(nav), m)}
  <main class="o-main" id="main" tabindex="-1">
    {bc}
    {reading}
    {workspace.footer(url, lang, ref, m)}
  </main>
</div>
{workspace.feedback_dialog(lang, p['title'], ref, m)}
</body>
</html>
'''


# ---------------------------------------------------------------- page content

def substitute(site, html_text, lang):
    def widen(svg):
        for kind, label in site.msg[lang].get('diagram_types', {}).items():
            svg = svg.replace('aria-roledescription="%s"' % kind, 'aria-roledescription="%s"' % esc(label))
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
    if fm.get('source_revision'):
        items.append((m['source_revision'], fm['source_revision']))
    if fm.get('revised'):
        items.append((m['revised'], fm['revised']))
    if fm.get('status'):
        st = fm['status'].strip().lower()
        items.append((m['status'], '<span class="status status-%s">%s</span>' % (esc(re.sub(r'[^a-z]+', '-', st)), esc(m.get('status_' + st, fm['status'])))))
    if items:
        items.append((m['owner'], esc(m['owner_value'])))
        src = site.bodies.get(p['id'], {}).get('src', (p.get('source') or [''])[0])
        if src.startswith(('charter/en/', 'charter/ru/')):
            rel_path = src[len('charter/') :]
            items.append((m['source_file'], '<a class="src" href="%s%s" title="%s">%s</a> <button type="button" class="icon-copy" data-copy-text="%s" aria-label="%s" title="%s">%s</button>' % (
                CHARTER_BASE, rel_path, esc(unc(CHARTER_BASE, rel_path)), esc(os.path.basename(src)), esc(unc(CHARTER_BASE, rel_path)), esc(m['copy_path']), esc(m['copy_path']), icon('copy'))))
    if not items:
        return ''
    return '<dl class="doc-facts">%s</dl>' % ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % (esc(k), v if k in (m['status'], m['owner'], m['source_file']) else esc(v)) for k, v in items)


def series_pages(site, p):
    if not p.get('series'):
        return []
    return sorted([x for x in site.pages if x.get('series') == p['series']], key=lambda x: (x.get('series_order', 0), x['order'], x['id']))


def parts_html(site, p, lang):
    parts = series_pages(site, p) or doc_parts(site, p)
    if len(parts) < 2:
        return ''
    url = site.url(p, lang)
    links = []
    for q in parts:
        if q.get('series'):
            cur = ' aria-current="page"' if q['id'] == p['id'] else ''
            links.append('<a href="%s"%s>%s</a>' % (site.rel(url, site.url(q, lang)), cur, esc(q.get('tab') or q['title'])))
            continue
        label = q['title'].split(': ', 1)[1] if ': ' in q['title'] else (tr(site, lang, 'foundations') if q.get('part', '').startswith('1 of') else q['title'])
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
        # Legal pages stand outside the reading flow: nothing leads into them or back from them.
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
    if q['type'] == 'home':
        return site.msg[lang]['home']
    if q['type'] == 'section':
        return site.auth['sections'][q['section']]['label'][lang]
    if q['type'] == 'control':
        return q['control']['ref']
    t = disp(q['title'])
    return NAV_SHORT.get(t, t)


def prev_next(site, p, lang):
    if p['type'] in ('control', 'role', 'home') or not (p.get('section') or p['type'] == 'legal'):
        return ''
    sib = list(flow_pages(site))
    i = [x['id'] for x in sib].index(p['id']) if p['id'] in [x['id'] for x in sib] else -1
    if i < 0:
        return ''
    url = site.url(p, lang)
    m = site.msg[lang]
    out = []
    if i > 0:
        out.append('<a class="pn prev" href="%s" rel="prev"><span>%s</span>%s</a>' % (site.rel(url, site.url(sib[i - 1], lang)), esc(m['previous']), esc(flow_label(site, sib[i - 1], lang))))
    nx = next_page(site, p)
    if nx:
        out.append('<a class="pn next" href="%s" rel="next"><span>%s</span>%s</a>' % (site.rel(url, site.url(nx, lang)), esc(m['next']), esc(flow_label(site, nx, lang))))
    return '<nav class="o-pn" aria-label="%s / %s">%s</nav>' % (esc(m['previous']), esc(m['next']), ''.join(out)) if out else ''


def companion_html(site, p, lang):
    c = p.get('companion')
    if not c or c not in site.by_id or p.get('series'):
        return ''
    q = site.by_id[c]
    key = 'companion_guide' if q['type'] == 'guide' else 'companion_workflow'
    return '<p class="companion"><a href="%s">%s: %s</a></p>' % (site.rel(site.url(p, lang), site.url(q, lang)), esc(tr(site, lang, key)), esc(re.sub(r'^(?:Guide|Руководство):\s*', '', q['title'])))


def lang_note(site, lang, content_language='en', partial=False):
    if lang == content_language:
        return ''
    return '<p class="o-callout lang-note" role="note">%s</p>' % esc(tr(site, lang, 'translation_partial' if partial else 'translation_missing'))


def read_further(site, p, lang):
    """The other pages of the section, as compact cards, below the navigation of a page."""
    if not p.get('section'):
        return ''
    url = site.url(p, lang)
    m = site.msg[lang]
    mine = {x['id'] for x in doc_parts(site, p)} | {x['id'] for x in series_pages(site, p)} | {p['id']}
    items = [q for q in nav_groups(site, p['section']) if q['id'] not in mine and not (q.get('document') and q['source'][0] == (p.get('source') or [''])[0])]
    if p['type'] == 'regulation':
        items = [q for q in items if q['type'] == 'regulation' and q.get('region') == p.get('region')] or [q for q in items if q['id'] == 'reference/regulators-and-acts']
    elif p['type'] == 'template':
        items = [q for q in items if q['id'] == 'knowledge-base/templates-and-forms'] + [q for q in items if q['type'] == 'template'][:5]
    else:
        items = [q for q in items if q['type'] not in ('regulation', 'template')]
    if not items:
        return ''
    if len(items) > 6:
        # the nearest pages in the order of the section, so that a long section does not list itself in full
        order = nav_groups(site, p['section'])
        pos = {q['id']: i for i, q in enumerate(order)}
        here = pos.get(p['id'], pos.get(next((x['id'] for x in order if x.get('document') and x.get('document') == p.get('document')), ''), 0))
        items = sorted(items, key=lambda q: abs(pos.get(q['id'], 0) - here))[:6]
        items.sort(key=lambda q: pos.get(q['id'], 0))
    return '<h2 class="about-deeper">%s</h2><ul class="o-grid card-list cards-compact">%s</ul>' % (esc(m['read_further']), ''.join(card(site, q, lang, url, 'card--compact') for q in items))


def content_page(site, p, lang):
    b = site.bodies[p['id']]
    ctx = {'source': b['src'], 'lang': lang, 'url': site.url(p, lang)}
    body = site.link_xrefs(b['html'], ctx)
    if p['id'] == 'reference/vocabulary':
        entries = iter(vocabulary_entries(site, p['source'][0]))
        body = re.sub(r'<tr>\n<td>(.*?)</td>', lambda mm: '<tr id="%s"><td>%s</td>' % (next(entries)['anchor'], mm.group(1)), body)
    elif p['type'] not in ('template',):
        body = link_terms(site, body, ctx)
    body = substitute(site, body, lang)
    about_guide = p['id'] in ('about/what-we-do', 'about/how-we-work')
    if about_guide:
        body = body.replace('<p>', '<p class="o-lead">', 1)
    desc = desc_of(site, p)
    lead = '<p class="o-lead" lang="%s">%s</p>' % (description_language(site, p), esc(desc)) if desc and p['type'] != 'catalogue' and not b['src'].startswith('portal/content/') else ''
    h1 = p['title'] if p['title'] in SHORT else disp(p['title'])
    if p['type'] == 'section' and p.get('series'):
        sec = site.auth['sections'][p['section']]
        h1 = sec['label'][lang]
        lead = '<p class="o-lead">%s</p>' % esc(sec['intro'][lang])
    eyebrow = ''
    if p.get('parent') and p['parent'] in site.by_id:
        par = site.by_id[p['parent']]
        eyebrow = '<p class="o-eyebrow parent"><a href="%s">%s</a> · %s</p>' % (site.rel(ctx['url'], site.url(par, lang)), esc(par['title']), esc(page_meta(site, p, lang)))
    head = eyebrow + '<h1>%s</h1>%s%s%s%s%s' % (esc(PAGE_TITLE.get(h1, h1)), lead, facts_html(site, p, lang, b['fm']), companion_html(site, p, lang), parts_html(site, p, lang), lang_note(site, lang, b['language']))
    extra = ''
    if p['type'] == 'catalogue':
        extra = controls_catalogue(site, p, lang)
        if site.control_language != b['language']:
            extra = lang_note(site, lang, site.control_language, partial=True) + extra
    if p['type'] == 'template':
        copy_text = re.sub(r'^```yaml\n.*?```\s*', '', b['raw'], count=1, flags=re.S)
        extra += '<p class="tpl-tools"><button type="button" class="oc-button" data-copy="tpl-src">%s</button></p><script type="text/markdown" id="tpl-src">%s</script>' % (
            esc(tr(site, lang, 'copy_template')), copy_text.replace('</script', '<\\/script'))
        # the template page starts with the "when used" line from the README
        tp = site.tpl_desc.get(p['source'][0])
        if tp:
            extra = ('<dl class="o-facts"><dt>%s</dt><dd lang="en">%s</dd><dt>%s</dt><dd lang="en"><code>%s</code></dd></dl>' % (esc(tr(site, lang, 'used_when')), esc(tp['used']), esc(tr(site, lang, 'kept_in')), esc(tp['kept'].strip('`')))).replace('lang="en"', 'lang="%s"' % description_language(site, p)) + extra
    change = ''
    if b['change']:
        ch = site.md.md.render(re.sub(r'^## .*$', '', b['change'], count=1, flags=re.M).strip())
        table_label = esc(site.msg[lang].get('table_label', 'Table'))
        ch = ch.replace('<table>', '<div class="o-table-wrap" role="region" tabindex="0" aria-label="%s"><table>' % table_label).replace('</table>', '</table></div>')
        change = '<details class="oc-disclosure change"><summary>%s</summary><div>%s</div></details>' % (esc(tr(site, lang, 'change_history')), ch)
    main = '%s%s<div class="o-doc" lang="%s">%s</div>%s%s%s' % (head, extra if p['type'] == 'template' else '', b['language'], body, change, prev_next(site, p, lang), read_further(site, p, lang))
    if about_guide:
        main = main.replace('<div class="o-doc"', '<div class="o-doc about-guide"', 1)
    if p['type'] == 'catalogue':
        main = '%s<div class="o-doc" lang="%s">%s%s</div>%s%s' % (head, b['language'], extra, body, prev_next(site, p, lang), read_further(site, p, lang))
    return layout(site, p, lang, main, b['outline'])


def weight(p):
    """The weight of a page on its section page: a document leads, a workflow supports it, a guide supports a workflow."""
    if p['type'] in ('document', 'catalogue', 'service') or p['id'] in ('reference/vocabulary',):
        return 'primary'
    if p['type'] == 'guide':
        return 'support'
    return 'secondary'


def parts_label(n, lang, m):
    # Russian needs the plural form that agrees with the number: 1 часть, 2-4 части, 5+ частей.
    if lang == 'ru':
        if n % 10 == 1 and n % 100 != 11:
            return 'часть'
        if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
            return 'части'
        return 'частей'
    return m['kind_parts']


def page_meta(site, p, lang):
    m = site.msg[lang]
    kinds = {'document': 'kind_document', 'catalogue': 'kind_document', 'workflow': 'kind_workflow', 'guide': 'kind_guide', 'template': 'kind_template',
             'outline': 'kind_page', 'reference': 'kind_reference', 'records': 'kind_reference', 'index': 'kind_page', 'legal': 'kind_page', 'service': 'kind_service', 'catalog': 'kind_catalog', 'regulation': 'kind_reference'}
    k = m.get(kinds.get(p['type'], 'kind_page'), '')
    bits = [k]
    if p.get('source_sections') and p.get('document'):
        n = len([x for x in site.pages if x.get('document') == p['document'] and x['source'][0] == p['source'][0]])
        if n > 1:
            bits.append('%d %s' % (n, parts_label(n, lang, m)))
    elif p.get('series'):
        bits.append('%d %s' % (len(series_pages(site, p)), parts_label(len(series_pages(site, p)), lang, m)))
    elif p.get('words'):
        bits.append('%s %s' % (format(p['words'], ','), m['kind_words']))
    return ' · '.join(b for b in bits if b)


def section_desc(site, q):
    """A document that is split over parts is described, in its section, by the sections of the parts that this section holds."""
    if q.get('document') and q.get('source_sections'):
        same = [x for x in site.pages if x.get('document') == q['document'] and x['source'][0] == q['source'][0] and x['section'] == q['section']]
        first = [x for x in site.pages if x.get('document') == q['document'] and x['source'][0] == q['source'][0] and x.get('part', '').startswith('1 of')]
        if first and first[0]['section'] != q['section']:
            pre, ss, ch = split_sections(site.sources.text(q['source'][0]))
            nums = sorted({n for x in same for n in x['source_sections']})
            names = [t for n, t, bb in ss if n in nums]
            if names:
                return '; '.join(names)
    return desc_of(site, q)


def doc_id(site, q):
    """The identifier of the document behind a page, from its front matter, or ''."""
    src = (q.get('source') or [''])[0]
    if not canonical_path(src).startswith('charter/en/documents/'):
        return ''
    combined_view = q['type'] in ('role', 'control') or q['id'] == 'organization/roles'
    sources = site.english_sources if combined_view and q.get('content_language') == 'en' else site.sources
    fm = site.bodies.get(q['id'], {}).get('fm') or sources.resolve(src).metadata
    return fm.get('id', '')


def card(site, q, lang, url, cls, extra=''):
    d = section_desc(site, q)
    meta = page_meta(site, q, lang)
    did = doc_id(site, q)
    title = q['title'] if q.get('series') else nav_title(site, q)
    tip_title = title + (' · ' + did if did else '')
    return ('<li class="o-card linked %s" data-tip="%s" data-tip-title="%s"><p class="card-kicker">%s</p><h3><a href="%s">%s</a></h3><p class="card-desc" lang="%s">%s</p>%s</li>' % (
        cls, esc(d), esc(tip_title), esc(meta), site.rel(url, site.url(q, lang)), esc(title), description_language(site, q), esc(d), extra))


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
                extra = '<p class="card-guide"><a href="%s">%s</a></p>' % (site.rel(from_url, site.url(g, lang)), esc(m['kind_guide'] + ': ' + re.sub(r'^(?:Guide|Руководство):\s*', '', g['title'])))
            cards.append(card(site, q, lang, from_url, 'card--secondary', extra))
        out.append('<h2>%s</h2><ul class="o-grid card-list cards-secondary">%s</ul>' % (esc(m['grp_workflows']), ''.join(cards)))
    if sup:
        lis = ''.join('<li><a href="%s">%s</a><span lang="%s"> &mdash; %s</span></li>' % (site.rel(from_url, site.url(q, lang)), esc(nav_title(site, q)), description_language(site, q), esc(desc_of(site, q))) for q in sup)
        out.append('<h2>%s</h2><ul class="support-list">%s</ul>' % (esc(m['grp_guides']), lis))
    return ''.join(out)


def section_page(site, p, lang):
    sid = p['section']
    sec = site.auth['sections'][sid]
    url = site.url(p, lang)
    m = site.msg[lang]
    if sid == 'responsible-ai':
        items = nav_groups(site, sid)
        course = sorted([q for q in site.pages if q.get('section') == sid and q.get('series')], key=lambda x: x['order'])
        rules = [q for q in items if not q.get('series')]
        cards = '<h2>%s</h2><ol class="levels steps course-steps">%s</ol><ul class="o-grid card-list cards-secondary">%s</ul><h2>%s</h2><ul class="o-grid card-list cards-primary">%s</ul>' % (
            esc(m['grp_course']), ''.join('<li><span class="lv-n">%d</span><strong><a href="%s">%s</a></strong></li>' % (i, site.rel(url, site.url(q, lang)), esc(q['title'])) for i, q in enumerate(course, 1)),
            ''.join(card(site, q, lang, url, 'card--secondary') for q in course), esc(m['grp_rules']), ''.join(card(site, q, lang, url, 'card--primary') for q in rules))
        main = '<h1>%s</h1><p class="o-lead">%s</p>%s%s' % (esc(sec['label'][lang]), esc(sec['intro'][lang]), cards, prev_next(site, p, lang))
        return layout(site, p, lang, main, [])
    if sid == 'reference':
        items = nav_groups(site, sid)
        main_items = [q for q in items if q['type'] != 'regulation']
        regs = [q for q in items if q['type'] == 'regulation']
        groups = []
        for region in ('Kyrgyz Republic', 'Kazakhstan', 'Russian Federation', 'European Union', 'United States', 'Global'):
            rs = [q for q in regs if q.get('region') == region]
            if rs:
                groups.append('<li><strong>%s:</strong> %s</li>' % (esc(m.get('regions', {}).get(region, region)), ', '.join('<a href="%s">%s</a>' % (site.rel(url, site.url(q, lang)), esc(q['title'])) for q in rs)))
        cards = '<ul class="o-grid card-list cards-primary">%s</ul><h2>%s</h2><p>%s</p><ul class="support-list reg-list">%s</ul>' % (
            ''.join(card(site, q, lang, url, 'card--primary' if q['type'] in ('reference', 'document') else 'card--secondary') for q in main_items),
            esc(m['grp_regulations']), esc(m['grp_regulations_lead']), ''.join(groups))
        main = '<h1>%s</h1><p class="o-lead">%s</p>%s%s' % (esc(sec['label'][lang]), esc(sec['intro'][lang]), cards, prev_next(site, p, lang))
        return layout(site, p, lang, main, [])
    else:
        cards = cards_for(site, sid, lang, url)
    main = '<h1>%s</h1><p class="o-lead">%s</p>%s%s' % (esc(sec['label'][lang]), esc(sec['intro'][lang]), cards, prev_next(site, p, lang))
    return layout(site, p, lang, main, [])


def guides_index(site, p, lang):
    url = site.url(p, lang)
    m = site.msg[lang]
    gs = sorted([x for x in site.pages if x['type'] == 'guide'], key=lambda x: (x['section'], x['order']))
    lis = ''.join('<li><a href="%s">%s</a><span lang="en"> &mdash; %s</span> <span class="x-kind">· %s</span></li>' % (
        site.rel(url, site.url(q, lang)), esc(nav_title(site, q)), esc(desc_of(site, q)), esc(site.auth['sections'][q['section']]['label'][lang])) for q in gs)
    intro = 'The guides explain the workflows and the organization for the people who use them: who does what, when, and what is left on record. Each guide sits beside its subject; this page lists them in one place.'
    main = '<h1>%s</h1><p class="o-lead">%s</p>%s<ul class="support-list">%s</ul>' % (esc(p['title']), esc(intro), lang_note(site, lang), lis) + prev_next(site, p, lang) + read_further(site, p, lang)
    return layout(site, p, lang, main, [])


def home_page(site, p, lang):
    a = site.auth['home']
    url = site.url(p, lang)
    m = site.msg[lang]
    soi = site.sources.text('charter/en/documents/statement-of-intent.md')
    pri = [(r['num'], r['t'], r.get('Objective', '')) for r in soi_priorities(soi)]
    sp = site.by_id['about/statement-of-intent/strategic-priorities']
    sp_url = site.rel(url, site.url(sp, lang))
    pcards = ''.join('<li class="o-card linked card--secondary" data-tip="%s"><p class="o-tag">%s</p><h3><a href="%s#c-%s">%s</a></h3><p class="card-desc" lang="en">%s</p></li>' % (
        esc(o), 'PRI-%d' % (k + 1), sp_url, num.replace('.', '-'), esc(t), esc(o)) for k, (num, t, o) in enumerate(pri))
    levels = site.sources.table('charter/en/documents/statement-of-intent.md', '| Maturity Level | Name | Capability')
    rp = site.by_id['about/statement-of-intent/capability-and-maturity-roadmap']
    rp_url = site.rel(url, site.url(rp, lang))
    lcards = ''.join('<li class="level"><span class="lv-n">%s %s</span><strong lang="en">%s</strong><span lang="en">%s</span></li>' % (esc(m['level']), esc(r['Maturity Level']), esc(r['Name']), esc(r['Capability'])) for r in levels)
    scards = ''
    for s in site.sections:
        sec = site.auth['sections'][s['id']]
        sp2 = site.by_id[s['id'] + '/index']
        line = sec.get('line', {}).get(lang) or sec.get('line', {}).get('en') or sec['intro'][lang].split('. ')[0].rstrip('.') + '.'
        scards += '<li class="o-card linked card--compact" data-tip="%s" data-tip-title="%s">%s<h3><a href="%s">%s</a></h3><p class="card-desc">%s</p></li>' % (esc(sec['intro'][lang].split('. ')[0]), esc(sec['label'][lang]), icon(sec['icon']), site.rel(url, site.url(sp2, lang)), esc(sec['label'][lang]), esc(line))
    def tip_of(pid):
        q = site.by_id.get(pid) or site.by_id.get(pid + '/index')
        if q is None:
            return ''
        if q['type'] == 'section' or q['id'].endswith('/index'):
            sec = site.auth['sections'].get(q.get('section') or '', {})
            return (sec.get('line', {}).get(lang) or sec.get('line', {}).get('en') or desc_of(site, q))
        return desc_of(site, q)
    ctas = ''.join('<a class="home-cta%s" href="%s" data-tip="%s">%s</a>' % (' primary' if i == 0 else '', site.rel(url, site.url(site.by_id[c['to']] if c['to'] in site.by_id else site.by_id[c['to'] + '/index'], lang)), esc(tip_of(c['to'])), esc(c['label'][lang])) for i, c in enumerate(a['cta']))
    # A card may carry its own short tip; otherwise the tip is the description of the linked page.
    stand = ''.join('<li class="linked" data-tip="%s" data-tip-title="%s"><h3>%s</h3><p>%s</p><a href="%s">%s &rsaquo;</a></li>' % (esc(st.get('tip', {}).get(lang) or tip_of(st['to'])), esc(st['link'][lang]), esc(st['title'][lang]), esc(st['text'][lang]), site.rel(url, site.url(site.by_id[st['to']], lang)), esc(st['link'][lang])) for st in a['stand'])
    chips = ''.join('<li><a href="%s#c-%s" data-tip="%s" data-tip-title="%s">%s</a></li>' % (sp_url, num.replace('.', '-'), esc(o), esc('%s %d' % (m['strategic_priority'], k + 1)), esc(t)) for k, (num, t, o) in enumerate(pri))
    lp = site.by_id['knowledge-base/learning-paths']
    main = f'''<section class="home-hero"><p class="o-eyebrow">{esc(a['eyebrow'][lang])}</p><h1>{esc(a['title'][lang])}</h1><p class="o-lead home-lead">{esc(a['lead'][lang])}</p><p class="home-tagline">{esc(a['tagline'][lang])}</p><p class="home-ctas">{ctas}</p></section>
<section aria-label="{esc(m['home'])}"><ul class="home-stand">{stand}</ul></section>
<section aria-labelledby="h-pri" class="home-pri"><h2 id="h-pri">{esc(m['strategic_priorities'])}</h2><p class="home-pri-lead">{esc(a['priorities_lead'][lang])}</p><ol class="home-chips">{chips}</ol></section>
<section aria-labelledby="h-sec"><h2 id="h-sec">{esc(a['sections_title'][lang])}</h2><ul class="o-grid card-list cards-compact home-sections">{scards}</ul></section>
<section class="home-newhere"><p>{esc(a['newhere'][lang])} <a href="{site.rel(url, site.url(lp, lang))}">{esc(a['newhere_link'][lang])} &rsaquo;</a></p></section>'''
    source_language = site.sources.resolve('charter/en/documents/statement-of-intent.md').language
    main = main.replace('lang="en"', 'lang="%s"' % source_language)
    return layout(site, p, lang, main, [])


def plain_md(t):
    return re.sub(r'\*\*([^*]+)\*\*', r'\1', re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t))


def vp_items(doc, num, sources):
    """The items of one group of values or principles, read from the clauses of the document: (lead, text) pairs, and an introduction where the clause has one."""
    pre, ss, ch = split_sections(sources.text('charter/en/documents/%s.md' % doc))
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
                lead = re.match(r'(Integrity|Prudence|Respect for people|Добросовестность|Осмотрительность|Уважение к людям)', sent)
                items.append((lead.group(1), sent[len(lead.group(1)):].lstrip()) if lead else ('', sent))
            continue
        mm = re.match(r'^2\.1\. (.*)$', l) if doc == 'solution-lifecycle-model' else None
        if mm:
            intro = plain_md(mm.group(1))
    return items, intro


def values_page(site, p, lang):
    a = site.auth['values_page']
    m = site.msg[lang]
    url = site.url(p, lang)
    ctx = {'url': url, 'lang': lang, 'source': 'charter/en/documents/statement-of-intent.md'}
    out, outline = [], []
    for g in a['groups']:
        doc, num = g['source']
        selected = site.sources.resolve('charter/en/documents/%s.md' % doc)
        items, intro = vp_items(doc, num, site.sources)
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
        block = ('<section class="vp-group" aria-labelledby="%s"><h2 id="%s">%s</h2><p class="vp-applies">%s</p>%s<ol class="vp-list">%s</ol>'
                 '<p class="vp-source">%s: <a href="%s" lang="en">%s %s</a></p></section>') % (
            hid, hid, esc(title), esc(g['applies'][lang]), intro_html, link_terms(site, ''.join(lis), ctx), esc(m['vp_source']), href, esc(h1_of(selected.path)), num)
        source_language = selected.language
        out.append(block.replace('lang="en"', 'lang="%s"' % source_language))
        site.extra_search.setdefault(lang, []).append({'u': url + '#' + hid, 't': p['title'], 'h': title, 'x': (g['applies'][lang] + ' ' + ' '.join((l + ' ' + t) for l, t in items))[:360]})
    ms = a['mission']
    charter = site.sources.resolve('charter/en/documents/aicc-charter.md')
    mission_text = re.search(r'^2\.1\. (.+)$', charter.text, re.M).group(1)
    mission = '<section class="vp-mission" aria-labelledby="g-mission"><h2 id="g-mission">%s</h2><p lang="%s">%s</p><p class="vp-source">%s: <a href="%s" lang="%s">%s 2.1</a></p></section>' % (
        esc(ms['title'][lang]), charter.language, esc(mission_text), esc(m['vp_source']), site._target('aicc-charter', '2.1', ctx), charter.language, esc(h1_of(charter.path)))
    outline.insert(0, (2, 'g-mission', ms['title'][lang]))
    site.extra_search.setdefault(lang, []).append({'u': url + '#g-mission', 't': p['title'], 'h': ms['title'][lang], 'x': mission_text[:360]})
    main = '<h1>%s</h1><p class="o-lead">%s</p>%s%s%s' % (esc(p['title']), esc(a['intro'][lang]), lang_note(site, lang, content_language=site.combined_sources(['charter/en/documents/aicc-charter.md'] + ['charter/en/documents/%s.md' % g['source'][0] for g in a['groups']]).language, partial=True), mission, ''.join(out)) + prev_next(site, p, lang) + read_further(site, p, lang)
    return layout(site, p, lang, main, outline)


def soi_priorities(soi):
    lines = soi.split('\n')
    pri = []
    for i, l in enumerate(lines):
        mm = re.match(r'### (9\.\d+)\. (.*)', l)
        if mm:
            row = {'n': len(pri) + 1, 'num': mm.group(1), 't': mm.group(2)}
            values = [match.group(1).strip() for line in lines[i + 1:i + 5]
                      if (match := re.match(r'- \*\*.+?\.\*\* (.*)', line))]
            row.update(zip(('Objective', 'Scope', 'Intended outcome'), values))
            pri.append(row)
    return pri


def strategy_page(site, p, lang):
    a = site.auth['strategy_page']
    m = site.msg[lang]
    url = site.url(p, lang)
    ctx = {'url': url, 'lang': lang, 'source': 'charter/en/documents/statement-of-intent.md'}
    soi = site.sources.text('charter/en/documents/statement-of-intent.md')
    sp = site.by_id['about/statement-of-intent/strategic-priorities']
    sp_url = site.rel(url, site.url(sp, lang))
    rp = site.by_id['about/statement-of-intent/capability-and-maturity-roadmap']
    rp_url = site.rel(url, site.url(rp, lang))
    soi_url = site.rel(url, site.url(site.by_id['about/statement-of-intent'], lang))

    def table(label, head, rows, cls=''):
        return '<div class="o-table-wrap%s" role="region" tabindex="0" aria-label="%s"><table lang="en"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
            (' ' + cls) if cls else '', esc(label), ''.join('<th>%s</th>' % esc(h) for h in head), rows)
    out, outline = [], []

    def section(hid, title, lead, body, lead_html=False):
        outline.append((2, hid, title))
        out.append('<section aria-labelledby="%s"><h2 id="%s">%s</h2>%s%s</section>' % (hid, hid, esc(title), ('<p>%s</p>' % (lead if lead_html else esc(lead))) if lead else '', body))
        site.extra_search.setdefault(lang, []).append({'u': url + '#' + hid, 't': p['title'], 'h': title, 'x': plain(lead)[:360]})
    # 1. the strategy of the Bank
    pillars = site.sources.table('charter/en/documents/statement-of-intent.md', '| Strategic Pillar |', ('Strategic Pillar',))
    carried = a['pillars_carried']
    rows = ''.join('<tr><td><strong>%s</strong></td><td>%s</td><td lang="__AUTHORED_LANG__">%s</td></tr>' % (esc(r.get('_localized_Strategic Pillar', r['Strategic Pillar'])), esc(r['Contribution of AI adoption']), esc(carried.get(r['Strategic Pillar'], {}).get(lang, ''))) for r in pillars)
    section('st-bank', a['bank_title'][lang], a['bank_lead'][lang], table(a['bank_title'][lang], [m['st_pillar'], m['st_contribution'], m['st_carried']], rows) + '<p class="vp-source">%s: <a href="%s#s-3">Statement of Intent 3</a></p>' % (esc(m['vp_source']), soi_url))
    # 2. the Strategic Priorities
    pri = soi_priorities(soi)
    rows = ''.join('<tr><td>%d</td><td><a href="%s#c-%s"><strong>%s</strong></a></td><td>%s</td><td>%s</td></tr>' % (
        r['n'], sp_url, r['num'].replace('.', '-'), esc(r['t']), esc(r.get('Objective', '')), esc(r.get('Intended outcome', ''))) for r in pri)
    section('st-priorities', a['priorities_title'][lang], a['priorities_lead'][lang], table(a['priorities_title'][lang], ['#', m['strategic_priority'], m['objective'], m['intended_outcome']], rows) + '<p class="vp-source">%s: <a href="%s">Statement of Intent 9</a>; <a href="%s#s-8">Statement of Intent 8</a></p>' % (esc(m['vp_source']), sp_url, soi_url))
    # 3. the aspects
    rows = ''.join('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>' % (esc(r['aspect'][lang]), esc(r['choice'][lang]), esc(r['decides'][lang]), site.link_xrefs(esc(r['read'][lang]), ctx)) for r in a['aspects'])
    section('st-aspects', a['aspects_title'][lang], a['aspects_lead'][lang], table(a['aspects_title'][lang], [m['st_aspect'], m['st_choice'], m['st_decides'], m['st_read']], rows, 'st-wide').replace('<table lang="en">', '<table lang="__ASPECT_LANG__">'))
    # 4. the road
    lv = site.sources.table('charter/en/documents/statement-of-intent.md', '| Maturity Level | Name | Capability')
    rows = ''.join('<tr><td>%s</td><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>' % (esc(r['Maturity Level']), esc(r['Name']), esc(r['Capability']), esc(r['Use of AI'])) for r in lv)
    section('st-road', a['road_title'][lang], a['road_lead'][lang], table(a['road_title'][lang], [m['level'], m['name'], m['capability'], m['st_use']], rows) + '<p class="vp-source">%s: <a href="%s">Statement of Intent 11</a>; %s: <a href="%s#c-11-3">Statement of Intent 11.3</a></p>' % (esc(m['vp_source']), rp_url, esc(m['st_measures']), rp_url))
    # 5. how it is kept
    section('st-kept', a['kept_title'][lang], site.link_xrefs(esc(a['kept'][lang]), ctx), '', lead_html=True)
    main = '<h1>%s</h1><p class="o-lead">%s</p>%s%s' % (esc(p['title']), esc(a['intro'][lang]), lang_note(site, lang, content_language=site.sources.resolve('charter/en/documents/statement-of-intent.md').language, partial=True), ''.join(out)) + prev_next(site, p, lang) + read_further(site, p, lang)
    source_language = site.sources.resolve('charter/en/documents/statement-of-intent.md').language
    main = main.replace('lang="en"', 'lang="%s"' % source_language)
    main = main.replace('__ASPECT_LANG__', lang)
    main = main.replace('__AUTHORED_LANG__', lang)
    main = main.replace('>Statement of Intent ', '>' + esc(h1_of(site.sources.resolve('charter/en/documents/statement-of-intent.md').path)) + ' ')
    return layout(site, p, lang, main, outline)


def explore_page(site, p, lang):
    a = site.auth['explore_page']
    m = site.msg[lang]
    url = site.url(p, lang)
    ctx = {'url': url, 'lang': lang, 'source': 'charter/en/documents/operating-model.md'}
    outline = []
    out = []
    # the four parts
    rows = []
    for r in a['parts']:
        where = esc(r['where'][lang])
        if r.get('to'):
            q = site.by_id[r['to']]
            where = '%s: <a href="%s">%s</a>' % (where, site.rel(url, site.url(q, lang)), esc(disp(q['title'])))
        rows.append('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>' % (esc(r['part'][lang]), esc(r['answers'][lang]), where))
    out.append('<section aria-labelledby="x-parts"><h2 id="x-parts">%s</h2><p>%s</p><div class="o-table-wrap" role="region" tabindex="0" aria-label="%s"><table><thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table></div></section>' % (
        esc(a['parts_title'][lang]), esc(a['parts_lead'][lang]), esc(a['parts_title'][lang]), esc(m['x_part']), esc(m['x_answers']), esc(m['x_where']), ''.join(rows)))
    outline.append((2, 'x-parts', a['parts_title'][lang]))
    # the sections and their pages, from the sitemap
    secs = []
    for sdef in site.sections:
        sec = site.auth['sections'][sdef['id']]
        sp = site.by_id[sdef['id'] + '/index']
        items = nav_groups(site, sdef['id'])
        if sdef['id'] == 'knowledge-base':
            tpls = sorted([x for x in site.pages if x['type'] == 'template'], key=lambda x: x['order'])
            lis = ''.join('<li><a href="%s">%s</a><span lang="%s"> &mdash; %s</span></li>' % (site.rel(url, site.url(q, lang)), esc(q['title']), description_language(site, q), esc(desc_of(site, q))) for q in items if q['type'] != 'template' and q.get('series'))
            lis += '<li>%s: %s</li>' % (esc(m['grp_templates']), ', '.join('<a href="%s">%s</a>' % (site.rel(url, site.url(q, lang)), esc(q['title'])) for q in tpls))
        else:
            lis = ''.join('<li><a href="%s">%s</a><span class="x-kind"> · %s</span><span lang="%s"> &mdash; %s</span></li>' % (
                site.rel(url, site.url(q, lang)), esc(nav_title(site, q)), esc(page_meta(site, q, lang).split(' · ')[0]), description_language(site, q), esc(section_desc(site, q))) for q in items if q['type'] != 'regulation')
        hid = 'x-' + sdef['id']
        secs.append('<section class="x-sec" aria-labelledby="%s"><h3 id="%s"><a href="%s">%s</a></h3><p>%s</p><ul class="support-list">%s</ul></section>' % (
            hid, hid, site.rel(url, site.url(sp, lang)), esc(sec['label'][lang]), esc(sec['intro'][lang].split('. ')[0].rstrip('.') + '.'), lis))
        outline.append((3, hid, sec['label'][lang]))
    out.insert(1, '<section aria-labelledby="x-sections"><h2 id="x-sections">%s</h2>%s</section>' % (esc(a['sections_title'][lang]), ''.join(secs)))
    outline.insert(1, (2, 'x-sections', a['sections_title'][lang]))
    # routes
    routes = ''
    for r in site.auth['routes']:
        links = []
        for pid in r['pages']:
            q = site.by_id.get(pid) or site.by_id.get(pid + '/index')
            links.append('<li><a href="%s">%s</a></li>' % (site.rel(url, site.url(q, lang)), esc(flow_label(site, q, lang))))
        routes += '<li class="o-card route"><h3>%s</h3><p class="route-reader">%s</p><p>%s</p><ol>%s</ol></li>' % (esc(r['title'][lang]), esc(r['reader'][lang]), esc(r['purpose'][lang]), ''.join(links))
    out.append('<section aria-labelledby="x-routes"><h2 id="x-routes">%s</h2><p>%s</p><ul class="o-grid card-list routes">%s</ul></section>' % (esc(a['routes_title'][lang]), esc(a['routes_lead'][lang]), routes))
    outline.append((2, 'x-routes', a['routes_title'][lang]))
    # control of the charter
    out.append('<section aria-labelledby="x-control"><h2 id="x-control">%s</h2><p>%s</p></section>' % (esc(a['control_title'][lang]), site.link_xrefs(esc(a['control'][lang]), ctx)))
    outline.append((2, 'x-control', a['control_title'][lang]))
    for hid, t, x in (('x-parts', a['parts_title'][lang], a['parts_lead'][lang]), ('x-routes', a['routes_title'][lang], a['routes_lead'][lang]), ('x-control', a['control_title'][lang], a['control'][lang])):
        site.extra_search.setdefault(lang, []).append({'u': url + '#' + hid, 't': p['title'], 'h': t, 'x': x[:360]})
    main = '<h1>%s</h1><p class="o-lead">%s</p>%s%s' % (esc(p['title']), esc(a['intro'][lang]), lang_note(site, lang, content_language=lang if all(description_language(site, q) == lang or not desc_of(site, q) for q in site.pages) else 'en', partial=True), ''.join(out)) + prev_next(site, p, lang) + read_further(site, p, lang)
    return layout(site, p, lang, main, outline)


def about_page(site, p, lang):
    a = site.auth['about_page']
    sec = site.auth['sections']['about']
    m = site.msg[lang]
    url = site.url(p, lang)
    soi = site.sources.text('charter/en/documents/statement-of-intent.md')
    sp = site.by_id['about/statement-of-intent/strategic-priorities']
    sp_url = site.rel(url, site.url(sp, lang))
    blocks = []
    for b in a['blocks']:
        extra = ''
        if b.get('priorities'):
            pri = soi_priorities(soi)
            lv = site.sources.table('charter/en/documents/statement-of-intent.md', '| Maturity Level | Name | Capability')
            prows = ''.join('<tr><td>%d</td><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>' % (r['n'], esc(r['t']), esc(r.get('Objective', '')), esc(r.get('Intended outcome', ''))) for r in pri)
            lrows = ''.join('<tr><td>%s</td><td><strong>%s</strong></td><td>%s</td></tr>' % (esc(r['Maturity Level']), esc(r['Name']), esc(r['Capability'])) for r in lv)
            extra = ('<div class="o-table-wrap about-table" role="region" tabindex="0" aria-label="%s"><table lang="en"><thead><tr><th>#</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table></div>'
                     '<div class="o-table-wrap about-table" role="region" tabindex="0" aria-label="%s"><table lang="en"><thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table></div>') % (
                esc(m['strategic_priorities']), esc(m['strategic_priority']), esc(m['objective']), esc(m['intended_outcome']), prows,
                esc(m['maturity_levels']), esc(m['level']), esc(m['name']), esc(m['capability']), lrows)
        links = []
        for l in b['links']:
            q = site.by_id.get(l['to']) or site.by_id.get(l['to'] + '/index')
            links.append('<a href="%s">%s</a>' % (site.rel(url, site.url(q, lang)), esc(l['label'][lang])))
        blocks.append('<section class="about-block" aria-labelledby="a-%s"><h2 id="a-%s">%s</h2><div><p>%s</p>%s<p class="about-links">%s</p></div></section>' % (
            b['id'], b['id'], esc(b['title'][lang]), esc(b['text'][lang]), extra, ' '.join(links)))
        site.extra_search.setdefault(lang, []).append({'u': url + '#a-' + b['id'], 't': sec['label'][lang], 'h': b['title'][lang], 'x': b['text'][lang][:360]})
    deeper = ''.join(card(site, q, lang, url, 'card--compact') for q in nav_groups(site, 'about'))
    main = '<h1>%s</h1><p class="o-lead">%s</p>%s%s<h2 class="about-deeper" id="a-further">%s</h2><ul class="o-grid card-list cards-compact">%s</ul>' % (
        esc(sec['label'][lang]), esc(sec['intro'][lang]), ''.join(blocks), prev_next(site, p, lang), esc(a['deeper'][lang]), deeper)
    outline = [(2, 'a-' + b['id'], b['title'][lang]) for b in a['blocks']] + [(2, 'a-further', a['deeper'][lang])]
    source_language = site.sources.resolve('charter/en/documents/statement-of-intent.md').language
    main = main.replace('lang="en"', 'lang="%s"' % source_language)
    return layout(site, p, lang, main, outline)


def change_history(site, p, lang):
    rows = []
    for key in ['statement-of-intent', 'aicc-charter', 'business-model', 'operating-model', 'portfolio-management-model', 'solution-lifecycle-model', 'ai-policy', 'vocabulary', 'document-catalog']:
        path = 'charter/en/documents/%s.md' % key
        selected = site.sources.resolve(path)
        tbl = site.sources.table(path, '| Revision | Date | Change | Decision')
        page = site.file_page[path]
        for r in tbl:
            rows.append('<tr><td><a href="%s">%s</a></td><td>%s</td><td>%s</td><td lang="%s">%s</td><td>%s</td></tr>' % (
                site.rel(site.url(p, lang), site.url(page, lang)), esc(h1_of(selected.path)), esc(r['Revision']), esc(r['Date']), selected.language, esc(r['Change']), esc(r['Decision'])))
    m = site.msg[lang]
    main = '<h1>%s</h1><div class="o-table-wrap" role="region" tabindex="0" aria-label="%s"><table><thead><tr><th>Document</th><th>%s</th><th>%s</th><th>Change</th><th>Decision</th></tr></thead><tbody>%s</tbody></table></div>%s' % (
        esc(p['title']), esc(p['title']), esc(m['revision']), esc(m['revised']), ''.join(rows), prev_next(site, p, lang))
    if lang == 'ru':
        for en, ru in [('Document', 'Документ'), ('Change', 'Изменение'), ('Decision', 'Управленческое решение')]:
            main = main.replace('<th>' + en + '</th>', '<th>' + ru + '</th>')
    return layout(site, p, lang, main, [])


def records_page(site, p, lang):
    m = site.msg[lang]
    url = site.url(p, lang)
    by_tpl = {}
    for c in site.controls:
        t = re.sub(r'\s+', ' ', c['canonical_template']).strip()
        by_tpl.setdefault(t, []).append(c['ref'])
    rows = []
    for src, d in sorted(site.tpl_desc.items(), key=lambda kv: kv[1]['order']):
        page = site.file_page.get(src)
        controls = []
        for t, refs in by_tpl.items():
            if t and (t.lower() in d['canonical_name'].lower() or d['canonical_name'].lower() in t.lower()):
                controls += refs
        ctl = ', '.join('<a href="%s">%s</a>' % (site.rel(url, '/%s/center/governance/controls/%s/' % (lang, r.lower())), r) for r in sorted(set(controls)))
        rows.append('<tr><td><a href="%s">%s</a></td><td lang="en">%s</td><td lang="en"><code>%s</code></td><td>%s</td></tr>' % (
            site.rel(url, site.url(page, lang)), esc(d['name']), esc(d['used']), esc(d['kept'].strip('`')), ctl or '&ndash;'))
    template_language = site.sources.resolve('charter/en/templates/README.md').language
    rows = [row.replace('lang="en"', 'lang="%s"' % template_language) for row in rows]
    systems = [('Registry', 'Decisions, appointments, controls, backlogs, roadmap, calendar, and other evidence records, as closed and dated extracts. Kept on the corporate folder: <a href="%s" title="%s">%s</a> <button type="button" class="icon-copy" data-copy-text="%s" aria-label="%s" title="%s">%s</button>' % (
                    REGISTRY_BASE, esc(unc(REGISTRY_BASE)), esc(unc(REGISTRY_BASE)), esc(unc(REGISTRY_BASE)), esc(m['copy_path']), esc(m['copy_path']), icon('copy'))),
               ('Jira and Confluence', 'The working state of the Program Backlog, boards, and Work Items, and the working documents, from the cutover of the working state'),
               ('Service Management', 'Requests and incidents, including AI Incidents')]
    if lang == 'ru':
        systems = [
            ('Папка AICC', 'Управленческие решения, назначения, контрольные процедуры, бэклоги, дорожная карта, календарь и другие подтверждающие документы в виде неизменяемых датированных выгрузок. Хранятся на корпоративном сетевом ресурсе: ' + systems[0][1].split('Kept on the corporate folder: ', 1)[1]),
            ('Jira и Confluence', 'Рабочее состояние бэклога программы, бордов и задач, а также рабочие документы — с момента перехода рабочего состояния в эти системы'),
            ('Service Management', 'Запросы и инциденты, в том числе инциденты AI'),
        ]
    srows = ''.join('<tr><th scope="row">%s</th><td lang="%s">%s</td></tr>' % (esc(a), lang, b if i == 0 else esc(b)) for i, (a, b) in enumerate(systems))
    intro = {'en': 'This site is static. It states the rules and the forms of AICC and holds no live record. The table lists each record by its template, with the place where it is kept and the controls that it evidences.',
             'ru': 'Портал статичен: он излагает правила и формы AICC и не содержит текущих рабочих документов. В таблице рабочие документы перечислены по их шаблонам с указанием места хранения и контрольных процедур, которые они подтверждают.'}[lang]
    main = '<h1>%s</h1><p class="o-lead">%s</p><h2>Systems</h2><div class="o-table-wrap" role="region" tabindex="0" aria-label="Systems"><table><tbody>%s</tbody></table></div><h2>Records</h2><div class="o-table-wrap" role="region" tabindex="0" aria-label="Records"><table><thead><tr><th>Template</th><th>%s</th><th>%s</th><th>Controls</th></tr></thead><tbody>%s</tbody></table></div>%s' % (
        esc(p['title']), esc(intro), srows, esc(m['used_when']), esc(m['kept_in']), ''.join(rows), prev_next(site, p, lang))
    if lang == 'ru':
        for en, ru in [('Systems', 'Системы'), ('Records', 'Рабочие документы'), ('Template', 'Шаблон'), ('Controls', 'Контрольные процедуры')]:
            main = main.replace('>' + en + '<', '>' + ru + '<').replace('aria-label="' + en + '"', 'aria-label="' + ru + '"')
    return layout(site, p, lang, main, [])


def controls_catalogue(site, p, lang):
    m = site.msg[lang]
    url = site.url(p, lang)
    types = sorted({c['type'] for c in site.controls if c['type']})
    opts = ''.join('<option value="%s">%s</option>' % (esc(t), esc(t)) for t in types)
    rows = []
    for c in site.controls:
        href = site.rel(url, '/%s/center/governance/controls/%s/' % (lang, c['ref'].lower()))
        rows.append('<tr data-type="%s"><td><a href="%s">%s</a></td><td lang="en">%s</td><td lang="en">%s</td><td lang="en">%s</td><td>%s</td></tr>' % (
            esc(c['type']), href, esc(c['ref']), esc(c['title']), esc(c['owner']), esc(c['when']), esc(c['type'])))
    return ('<section class="catalogue" aria-label="%s"><div class="o-toolbar"><div class="oc-field"><label for="cf">%s</label><input id="cf" class="oc-input" type="search" data-filter="ctl"></div>'
            '<div class="oc-field"><label for="ct">%s</label><select id="ct" class="oc-input" data-filter-type="ctl"><option value="">%s</option>%s</select></div></div>'
            '<div class="o-table-wrap" role="region" tabindex="0" aria-label="%s"><table id="ctl" lang="%s"><thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table></div>'
            '<p class="o-caption">%s</p></section>') % (
        esc(p['title']), esc(m['controls_filter']), esc(m['controls_type']), esc(m['controls_all']), opts, esc(p['title']), site.control_language,
        esc(m['control_ref']), esc(m['control_title']), esc(m['control_owner']), esc(m['control_when']), esc(m['control_type']), ''.join(rows).replace('lang="en"', 'lang="%s"' % site.control_language), esc(m['control_status_note']))


def control_page(site, p, lang):
    c = p['control']
    m = site.msg[lang]
    url = site.url(p, lang)
    parent = site.by_id['governance/controls']
    facts = [('control_rule', c['rule']), ('control_owner', c['owner']), ('control_when', c['when']), ('control_evidence', c['evidence']), ('control_template', c['template']),
             ('control_objective', c['objective']), ('control_type', c['type']), ('control_test', c['test'])]
    dl = ''.join('<dt>%s</dt><dd lang="en">%s</dd>' % (esc(m[k]), site.link_xrefs(esc(v), {'source': 'charter/en/documents/operating-model.md', 'lang': lang, 'url': url})) for k, v in facts if v)
    idx = [x['ref'] for x in site.controls].index(c['ref'])
    pn = []
    if idx > 0:
        q = site.controls[idx - 1]
        pn.append('<a class="pn prev" href="%s"><span>%s</span>%s</a>' % (site.rel(url, '/%s/center/governance/controls/%s/' % (lang, q['ref'].lower())), esc(m['previous']), esc(q['ref'])))
    if idx + 1 < len(site.controls):
        q = site.controls[idx + 1]
        pn.append('<a class="pn next" href="%s"><span>%s</span>%s</a>' % (site.rel(url, '/%s/center/governance/controls/%s/' % (lang, q['ref'].lower())), esc(m['next']), esc(q['ref'])))
    main = '<h1 lang="en">%s</h1><p class="o-lead" lang="en">%s</p>%s<dl class="o-facts control-facts">%s</dl><p class="o-caption">%s</p><p><a href="%s">%s</a></p><nav class="o-pn">%s</nav>' % (
        esc(c['ref'] + ' ' + c['title']), esc(c['objective']), lang_note(site, lang, site.control_language if p['type'] == 'control' else site.role_language), dl, esc(m['control_status_note']), site.rel(url, site.url(parent, lang)), esc(parent['title']), ''.join(pn))
    return layout(site, p, lang, main.replace('lang="en"', 'lang="%s"' % (site.control_language if p['type'] == 'control' else site.role_language)), [])


def roles_index(site, p, lang):
    url = site.url(p, lang)
    out = []
    for q in sorted([x for x in site.pages if x['type'] == 'role'], key=lambda x: x['order']):
        d = site.roles['om'].get(q.get('english_title', q['title']), {}).get('Does', '')
        out.append('<li class="o-card linked card--secondary" data-tip="%s"><h3><a href="%s">%s</a></h3><p class="card-desc" lang="en">%s</p></li>' % (esc(q.get('ref', '')), site.rel(url, site.url(q, lang)), esc(q['title']), esc(d)))
    main = '<h1>%s</h1><ul class="o-grid card-list">%s</ul>%s' % (esc(p['title']), ''.join(out), lang_note(site, lang, site.control_language if p['type'] == 'control' else site.role_language))
    return layout(site, p, lang, main.replace('lang="en"', 'lang="%s"' % (site.control_language if p['type'] == 'control' else site.role_language)), [])


def role_page(site, p, lang):
    m = site.msg[lang]
    name = p.get('english_title', p['title'])
    om = site.roles['om'].get(name, {})
    prof = site.roles['prof'].get(name, {})
    cols = {'Executive Sponsor': 'SP', 'AICC Lead': 'AL', 'Solution Engineer': 'SE', 'Domain Owner': 'DO', 'Domain Expert': 'DE', 'Control Function Contact': 'CFC', 'Platform Owner': 'PO'}
    col = cols.get(name)
    raci = [(r['Activity'], r.get(col, '')) for r in site.roles['raci'] if col and r.get(col)]
    dl = ''
    for k, v in (('Purpose', prof.get('Purpose')), ('Main responsibilities', prof.get('Main responsibilities')), ('Authority', prof.get('Authority')), ('Reports in', prof.get('Reports in')), ('Typical competence', prof.get('Typical competence'))):
        if v:
            dl += '<dt>%s</dt><dd lang="en">%s</dd>' % (esc(prof.get('_labels', {}).get(k, k)), esc(v))
    rows = ''.join('<tr><td lang="en">%s</td><td>%s</td></tr>' % (esc(a), esc(r)) for a, r in raci)
    om_page = site.section_page[('charter/en/documents/operating-model.md', 4)]
    activity_label = site.roles['raci'][0]['_labels']['Activity']
    rule_title = h1_of(site.sources.resolve('charter/en/documents/operating-model.md').path)
    main = '<h1>%s</h1><p class="o-lead" lang="en">%s</p>%s<h2>%s</h2><dl class="o-facts">%s</dl><h2>%s</h2><p lang="en">%s</p><h2>%s</h2><div class="o-table-wrap" role="region" tabindex="0" aria-label="RACI"><table><thead><tr><th>%s</th><th>R / A / C / I</th></tr></thead><tbody>%s</tbody></table></div><p><a href="%s#c-4-2">%s 4.2</a></p>' % (
        esc(p['title']), esc(om.get('Does', '')), lang_note(site, lang, site.control_language if p['type'] == 'control' else site.role_language), esc(m['role_profile']), dl, esc(m['role_decides']), esc(om.get('Decides', '')), esc(m['role_raci']), esc(activity_label), rows,
        site.rel(site.url(p, lang), site.url(om_page, lang)), esc(rule_title))
    return layout(site, p, lang, main.replace('lang="en"', 'lang="%s"' % (site.control_language if p['type'] == 'control' else site.role_language)), [])


def build_page(site, p, lang):
    t = p['type']
    if t == 'home':
        return home_page(site, p, lang)
    if p['id'] == 'about/index':
        return about_page(site, p, lang)
    if t == 'section' and p.get('series'):
        return content_page(site, p, lang)
    if t == 'section':
        return section_page(site, p, lang)
    if p['id'] == 'about/values-and-principles':
        return values_page(site, p, lang)
    if p['id'] == 'about/charter-outline':
        return explore_page(site, p, lang)
    if p['id'] == 'about/strategy':
        return strategy_page(site, p, lang)
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
            if not site.bodies[p['id']]['chunks']:
                # Heading-free forms still need a searchable page entry.
                out.append({'u': u, 't': p['title'], 'h': p['title'],
                            'x': plain(site.bodies[p['id']]['html'])[:360]})
            for c in site.bodies[p['id']]['chunks']:
                txt = re.sub(r'\s+', ' ', re.sub(r'[*_`|]|\[([^\]]*)\]\([^)]*\)', lambda m: m.group(1) or ' ', c['text'])).strip()
                out.append({'u': u + '#' + c['anchor'], 't': p['title'], 'h': c['heading'], 'x': txt[:360]})
        if p['id'] == 'reference/vocabulary':
            # A section excerpt cannot index the definitions near the end of a long table.
            for entry in vocabulary_entries(site, p['source'][0]):
                out.append({'u': u + '#' + entry['anchor'], 't': p['title'], 'h': entry['label'], 'x': entry['meaning'][:360]})
        if p['id'] == 'reference/shared-terminology':
            # Grouped tables need a search entry for every term, including late rows.
            for occurrence, section in enumerate(('s-3', 's-4', 's-5', 's-6')):
                for row in site.sources.table(p['source'][0], '| Universal term | Meaning',
                                              occurrence=occurrence):
                    label = row['Universal term']
                    # The Russian edition is searched by the form its corpus writes.
                    local_name = row.get('Accepted form') or row.get('Russian-language term')
                    if local_name and local_name != label:
                        label += ' — ' + local_name
                    out.append({'u': u + '#' + section, 't': p['title'], 'h': label,
                                'x': row['Meaning'][:360]})
        if p['type'] == 'control':
            c = p['control']
            out.append({'u': u, 't': p['title'], 'h': c['ref'], 'x': ' '.join([c['objective'], c['rule'], c['owner'], c['test']])[:360]})
        if p['type'] == 'role':
            out.append({'u': u, 't': p['title'], 'h': p['title'], 'x': site.roles['om'].get(p.get('english_title', p['title']), {}).get('Does', '')[:360]})
        if p['type'] == 'section':
            sec = site.auth['sections'][p['section']]
            out.append({'u': u, 't': sec['label'][lang], 'h': sec['label'][lang], 'x': sec['intro'][lang]})
    # Generated pages without source chunks must also be discoverable by title.
    indexed = {entry['u'].split('#', 1)[0] for entry in out}
    for p in site.pages:
        u = site.url(p, lang)
        if u not in indexed:
            out.append({'u': u, 't': p['title'], 'h': p['title'], 'x': desc_of(site, p)[:360]})
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
    for name in ('neighbours.css', 'discovery.css'):
        shutil.copy(os.path.join(PORTAL, 'site', name), os.path.join(dst, name))


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
    validate_translations(ROOT)
    sites = {language: Site(args, language) for language in LANGS}
    diagrams = []
    for site in sites.values():
        add_generated_pages(site)
        assign_refs(site)
        load_terms(site)
        diagrams.extend(render_pages(site))
    diagram_code = dict(diagrams)
    svgs = render_diagrams(list(diagram_code.items()), not args.no_diagrams)
    for site in sites.values():
        site.diagram_code = diagram_code
        site.svgs = svgs
    missing = [k for k, v in svgs.items() if not v]
    if missing and not args.no_diagrams:
        raise RuntimeError('%d diagram(s) not rendered' % len(missing))
    # clean output
    for d in LANGS + ['assets']:
        shutil.rmtree(os.path.join(OUT, d), ignore_errors=True)
    os.makedirs(OUT, exist_ok=True)
    copy_assets()
    count = 0
    for lang in LANGS:
        site = sites[lang]
        for p in sorted(site.pages, key=lambda x: x['id']):
            page = build_page(site, p, lang)
            page = page.replace('@@NOLINK@@', '#')
            rel = site.url(p, lang).strip('/')
            write(os.path.join(OUT, rel, 'index.html'), page)
            count += 1
        write(os.path.join(OUT, 'assets', 'search-center-%s.json' % lang), json.dumps(search_index(site, lang), ensure_ascii=False, separators=(',', ':')))
    from neighbours import build_neighbours
    count += build_neighbours(OUT)
    import router
    count += router.build(OUT)
    write(os.path.join(OUT, 'index.html'), gateway())
    print('built %d pages, %d diagrams (%d not rendered)' % (count, len(site.svgs), len(missing)))


if __name__ == '__main__':
    main()
