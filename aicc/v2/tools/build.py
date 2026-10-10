#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Build the AI Competence Hub site (version 2) in each of its languages from its Markdown pages, vocabulary and project cards; Russian is the source and English its translation.
#   SCOPE: Reads aicc/v2 only; writes html/aicc/v2 only (ru/, en/, assets/, sources/). Self-contained: shares no code or file with version 1.
#   DEPENDS: markdown-it-py, PyYAML
#   LINKS: C-HUB-V2, M-PORTAL-PROJECTION
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   ROOT, SRC, OUT - repository root, source folder, output folder
#   load_site - read site.json
#   load_terms - read the vocabulary
#   short_id - stable five-character page identifier
#   load_pages - read the Markdown pages and the generated pages
#   render_markdown - Markdown to HTML with term markers, page links and heading ids
#   build_edition - write one edition
#   build - write the whole site, one edition per language
#   messages - the site messages of the edition being built
# END_MODULE_MAP
"""Build html/aicc/v2: python3 aicc/v2/tools/build.py"""
import hashlib
import json
import os
from html import escape
from pathlib import Path
import posixpath
import re
import shutil
import sys
from urllib.parse import quote

import yaml
from markdown_it import MarkdownIt

sys.path.insert(0, str(Path(__file__).resolve().parent))
import i18n  # noqa: E402
from i18n import T, loc  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / 'aicc' / 'v2'
OUT = Path(os.environ.get('AICC_V2_OUT') or ROOT / 'html' / 'aicc' / 'v2')  # a writer may build into a private folder
LENIENT = bool(os.environ.get('AICC_V2_LENIENT'))  # writers: links to pages another writer has not finished yet do not stop the build
ALPHABET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
TERM = re.compile(r'\[\[([a-z0-9-]+)(?:\|([^\]]+))?\]\]')
PAGE_LINK = re.compile(r'\]\(page:([a-z0-9/_-]+)(#[^)]*)?\)')
HTML_PAGE_LINK = re.compile(r'href="page:([a-z0-9/_-]+)(#[^"]*)?"')
ICON = re.compile(r'\{\{icon:([a-z0-9-]+)\}\}')


def load_site():
    return json.loads((SRC / 'site.json').read_text(encoding='utf-8'))


def load_terms():
    terms = []
    for path in sorted((SRC / 'vocabulary').glob('*.yaml')):
        terms.extend(yaml.safe_load(path.read_text(encoding='utf-8')) or [])
    seen = {}
    for term in terms:
        for key in ('id', 'ru', 'en', 'definition'):
            if not term.get(key):
                raise ValueError(f'vocabulary term without {key}: {term}')
        if term['id'] in seen:
            if LENIENT:
                continue  # writers may define the same term at the same time; the assembled site refuses it
            raise ValueError('duplicate vocabulary id ' + term['id'])
        seen[term['id']] = term
    return seen


# START_CONTRACT: short_id
#   PURPOSE: A stable five-character identifier of a page, derived from its key; readers quote it when they write about the page.
#   INPUTS: { key: str - page key; taken: set - identifiers already in use }
#   OUTPUTS: { str - identifier unique among taken }
#   SIDE_EFFECTS: Adds the identifier to taken.
# END_CONTRACT: short_id
def short_id(key, taken):
    digest = hashlib.sha1(key.encode('utf-8')).digest()
    n = 0
    while True:
        chunk = int.from_bytes(hashlib.sha1(digest + bytes([n])).digest()[:8], 'big')
        out = ''
        for _ in range(5):
            out += ALPHABET[chunk % 32]
            chunk //= 32
        if out not in taken:
            taken.add(out)
            return out
        n += 1


def slug(text):
    text = re.sub(r'<[^>]+>', '', text).lower()
    return re.sub(r'[^\w]+', '-', text, flags=re.UNICODE).strip('-_') or 'section'


def plain(html):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html.replace('</p>', ' '))).strip()


def url_of(page_id, lang=None):
    """The file of a page below the site root, in the edition being built unless a language is given; every address names its file so the site also opens from a folder."""
    lang = lang or i18n.lang()
    if page_id == 'index':
        return f'{lang}/index.html'
    return f'{lang}/{page_id}/index.html'


def rel(source, target):
    return posixpath.relpath(target, posixpath.dirname(source)) if posixpath.dirname(source) else target


def icon(name):
    path = SRC / 'ui' / 'icons' / f'ui-{name}.svg'
    return path.read_text(encoding='utf-8').replace('<svg ', '<svg class="o-icon" aria-hidden="true" ', 1).strip()


class Page:
    def __init__(self, page_id, title, section, order, summary, body, source=None, nav=True, nav_title=None, layout=''):
        self.id, self.title, self.section, self.order = page_id, title, section, order
        self.nav_title, self.layout = nav_title or title, layout
        self.meta = {}
        self.related = []
        self.summary, self.body, self.source, self.nav = summary, body, source, nav
        self.ident = ''
        self.headings = []

    @property
    def url(self):
        return url_of(self.id)


def front_matter(text, path):
    match = re.match(r'---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise ValueError(f'{path}: front matter is missing')
    meta = {}
    for line in match[1].split('\n'):
        pair = re.match(r'([\w-]+):\s*(.*)$', line)
        if not pair:
            raise ValueError(f'{path}: cannot read the front matter line {line!r}')
        value = pair[2].strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in '"\'':
            value = value[1:-1]
        meta[pair[1]] = value
    return meta, text[match.end():]


def term_html(terms, key, surface, here):
    """A vocabulary term as it appears in running text, linked to the vocabulary: in Russian the word with the English term beside it, in English the plain term."""
    entry = terms[key]
    href = rel(here, url_of('reference/vocabulary')) + '#' + key
    if i18n.lang() != i18n.SOURCE:
        return f'<a class="term" href="{href}" title="{escape(loc(entry, "definition"), quote=True)}">{escape(surface or loc(entry, "term") or entry["en"])}</a>'
    return (f'<a class="term" href="{href}" title="{escape(entry["definition"], quote=True)}">'
            f'{escape(surface or entry["ru"])}' + ('' if (surface or entry['ru']).lower().startswith(entry['en'].lower()) else f' <span class="term-en">({escape(entry["en"])})</span>') + '</a>')


# START_CONTRACT: render_markdown
#   PURPOSE: Render one page body; expands [[term|surface]] markers with the English term, resolves page: links, gives headings identifiers.
#   INPUTS: { text: str - Markdown; page: Page - the page being rendered; terms: dict; pages: dict - page id to Page; site: dict }
#   OUTPUTS: { str - HTML; the page's headings list is filled }
#   SIDE_EFFECTS: Sets page.headings.
# END_CONTRACT: render_markdown
def render_markdown(text, page, terms, pages, site):
    here = page.url

    def term(match):
        if match[1] not in terms:
            raise ValueError(f'{page.id}: unknown term [[{match[1]}]]')
        return term_html(terms, match[1], match[2], here)

    def link(match):
        target = match[1]
        if target not in pages:
            if LENIENT:
                return '](#)'
            raise ValueError(f'{page.id}: link to unknown page {target}')
        return '](' + rel(here, pages[target].url) + (match[2] or '') + ')'

    def html_link(match):
        if match[1] not in pages:
            if LENIENT:
                return 'href="#"'
            raise ValueError(f'{page.id}: link to unknown page {match[1]}')
        return 'href="' + rel(here, pages[match[1]].url) + (match[2] or '') + '"'

    figures = []

    def mermaid(match):
        caption = re.search(r'^%%\s*caption:\s*(.+)$', match[1], re.M)
        code = re.sub(r'^%%.*\n?', '', match[1], flags=re.M)
        figures.append((code, caption[1].strip() if caption else ''))
        return f'\n\n@@FIGURE{len(figures) - 1}@@\n\n'
    text = re.sub(r'^```mermaid\n(.*?)^```\s*$', mermaid, text, flags=re.S | re.M)
    text = TERM.sub(term, text)
    text = PAGE_LINK.sub(link, text)
    text = HTML_PAGE_LINK.sub(html_link, text)
    text = ICON.sub(lambda m: icon(m[1]), text)
    md = MarkdownIt('commonmark', {'html': True}).enable('table')
    tokens = md.parse(text)
    used = set()
    page.headings = []
    hint = HEADING_IDS.get(page.id) if i18n.lang() != i18n.SOURCE else None  # a translation keeps the Russian page's anchors
    order = []
    for i, token in enumerate(tokens):
        if token.type == 'heading_open':
            inline = tokens[i + 1]
            explicit = re.search(r'\s*\{#([\w-]+)\}\s*$', inline.content)
            if explicit:
                inline.content = inline.content[:explicit.start()]
                if inline.children and inline.children[-1].type == 'text':
                    inline.children[-1].content = re.sub(r'\s*\{#[\w-]+\}\s*$', '', inline.children[-1].content)
            label = plain(md.renderer.renderInline(inline.children, md.options, {}))
            ident = explicit[1] if explicit else (hint[len(order)] if hint and len(order) < len(hint) else slug(label))
            n = 2
            base = ident
            while ident in used:
                ident = f'{base}-{n}'
                n += 1
            used.add(ident)
            order.append(ident)
            token.attrSet('id', ident)
            if token.tag in ('h2', 'h3'):
                page.headings.append((token.tag, ident, label))
    html = md.renderer.render(tokens, md.options, {})
    if i18n.lang() == i18n.SOURCE:
        HEADING_IDS[page.id] = order
    if figures:
        import diagrams
        drawn = diagrams.render([code for code, _ in figures])
        for n, (code, caption) in enumerate(figures):
            svgs = drawn[diagrams.key_of(diagrams.prepare(code))]
            if svgs is None:
                raise ValueError(f'{page.id}: a diagram could not be drawn')
            cap = f'<figcaption>{escape(caption)}</figcaption>' if caption else ''
            figure = (f'<figure class="o-diagram" role="group" aria-label="{escape(caption or page.title)}"><button type="button" class="dz-open" aria-label="{escape(T('Открыть крупно'))}">{icon("maximize")}</button>'
                      f'<div class="mm mm-light">{svgs["light"]}</div><div class="mm mm-dark">{svgs["dark"]}</div>{cap}</figure>')
            html = re.sub(r'<p>@@FIGURE' + str(n) + r'@@</p>', lambda _: figure, html)
    # headings written as HTML blocks count too, in the order they appear
    page.headings = [(m[1], m[2], plain(m[3])) for m in re.finditer(r'<(h2|h3)\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</\1>', html, re.S)]
    return html.replace('<table>', '<div class="o-table-wrap"><table>').replace('</table>', '</table></div>')


HEADING_IDS = {}  # page id -> the anchors of the Russian page's headings, in order


def load_pages(site, terms):
    """The pages of the edition: every Russian page, with its translation's text where one exists (otherwise the Russian text, marked as a fallback)."""
    pages = {}
    content = SRC / 'content' / i18n.SOURCE
    edition = SRC / 'content' / i18n.lang()
    for path in sorted(content.rglob('*.md')):
        relative = path.relative_to(content).with_suffix('')
        page_id = relative.as_posix()
        if page_id.endswith('/index'):
            page_id = page_id[:-len('/index')]
        own = edition / path.relative_to(content)
        fallback = i18n.lang() != i18n.SOURCE and not own.exists()
        if i18n.lang() != i18n.SOURCE and own.exists():
            path = own
        meta, body = front_matter(path.read_text(encoding='utf-8'), path)
        first = page_id.split('/')[0]
        section = 'hub' if page_id == 'index' or first not in {s['id'] for s in site['sections']} else first
        pages[page_id] = Page(page_id, meta['title'], section, int(meta.get('order', 100)), meta.get('summary', ''), body,
                              source=path, nav=str(meta.get('nav', 'true')).lower() not in ('false', 'no', '0'), nav_title=meta.get('nav_title'), layout=meta.get('layout', ''))
        pages[page_id].related = [x.strip() for x in meta.get('related', '').split(',') if x.strip()]
        pages[page_id].meta = meta
        pages[page_id].fallback = fallback
    if i18n.lang() != i18n.SOURCE and edition.exists():
        orphans = [p for p in edition.rglob('*.md') if not (content / p.relative_to(edition)).exists()]
        if orphans:
            raise ValueError(f'translations without a Russian page: {orphans}')
    return pages


def load_catalog(pages):
    """The scenario catalog, carried over verbatim as HTML fragments with their own styles."""
    base = SRC / 'catalog' / 'pages'
    if not base.exists():
        return
    own = SRC / 'catalog' / f'pages-{i18n.lang()}'
    if i18n.lang() != i18n.SOURCE and own.exists():
        base = own
    home = (base / 'index.html').read_text(encoding='utf-8')
    order = {}
    for n, href in enumerate(re.findall(r'href="([^"#]+)', home)):
        order.setdefault(('catalog/' + href.replace('/index.html', '')).rstrip('/'), n + 1)
    for path in sorted(list(base.rglob('index.html')) + list(base.glob('_moved/*.html'))):
        text = path.read_text(encoding='utf-8')
        meta = json.loads(re.match(r'<!--page (.*?) -->\n', text)[1])
        body = text[text.index('-->\n') + 4:]
        section = meta.get('section', 'catalog')
        page = Page(meta['id'], meta['title'], section, meta.get('order') or (0 if meta['id'] == 'catalog' else order.get(meta['id'], 9999)), meta['summary'], body, layout='raw',
                    nav_title=T('Обзор') if meta['id'] == 'catalog' else None)
        page.styles = meta['styles']
        page.fallback = i18n.lang() != i18n.SOURCE and base.name == 'pages'
        pages[meta['id']] = page


def add_generated(pages, site, terms):
    """Pages that are projections of data rather than Markdown: the vocabulary, the project views, the reference and the knowledge base."""
    if i18n.lang() == i18n.SOURCE:
        rows = ''.join(
            f'<tr id="{escape(t["id"])}"><td><strong>{escape(t["ru"])}</strong> <span class="term-en">({escape(t["en"])})</span></td>'
            f'<td>{escape(t["definition"])}</td></tr>' for t in sorted(terms.values(), key=lambda t: t['ru'].casefold()))
    else:  # the English vocabulary: the English term and its definition only
        word = lambda t: loc(t, 'term') or t['en']
        rows = ''.join(
            f'<tr id="{escape(t["id"])}"><td><strong>{escape(word(t))}</strong></td><td>{escape(loc(t, "definition"))}</td></tr>'
            for t in sorted(terms.values(), key=lambda t: word(t).casefold()))
    m = messages(site)
    body = (f'<p class="lede">{escape(m["vocabulary_intro"])}</p><div class="o-table-wrap"><table class="vocabulary"><thead><tr>'
            f'<th>{escape(m["vocabulary_term"])}</th><th>{escape(m["vocabulary_definition"])}</th></tr></thead><tbody>{rows}</tbody></table></div>')
    pages['reference/vocabulary'] = Page('reference/vocabulary', T('Словарь'), 'reference', 30, m['vocabulary_intro'], body)
    import cards
    import library
    library.add_pages(pages, site, sys.modules[__name__])
    library.add_maps(pages, sys.modules[__name__])
    cards.add_pages(pages, site, terms, sys.modules[__name__])


def messages(site):
    """The site messages of the edition, the Russian ones standing in for any the edition lacks."""
    return {**site['messages'][i18n.SOURCE], **site['messages'].get(i18n.lang(), {})}


def label_of(section):
    return section['label'].get(i18n.lang()) or section['label'][i18n.SOURCE]


def section_members(pages, section_id):
    return sorted((p for p in pages.values() if p.section == section_id and p.nav), key=lambda p: (p.order, p.title.casefold()))


def navigation(page, pages, site):
    groups = []
    m = messages(site)
    for section in site['sections']:
        members = section_members(pages, section['id'])
        if not members:
            continue
        first = members[0]
        current = section['id'] == page.section
        local = ''
        if current and len(members) > 1:
            # Large sections list their top pages; the pages of the area the reader is in open beside them.
            area = '/'.join(page.id.split('/')[:2]) if page.id.count('/') >= 1 else None
            if section['id'] == 'catalog':
                shown = [p for p in members if p.id.count('/') <= 1]  # the catalog lists its areas, as it always did
            else:
                shown = [p for p in members if p.id.count('/') <= 1 or (area and p.id.startswith(area + '/'))]
            local = '<div class="portal-local-nav">' + ''.join(
                f'<a{" class=nav-sub" if p.id.count("/") >= 2 else ""} href="{escape(rel(page.url, p.url))}"' + (' aria-current="page"' if p is page else '') + f'>{escape(p.nav_title)}</a>'
                for p in shown) + '</div>'
        groups.append(f'<div class="portal-nav-group{" is-current" if current else ""}"><a class="portal-section-link" data-section="{section["id"]}" '
                      f'href="{escape(rel(page.url, first.url))}"' + (' aria-current="true"' if current else '') +
                      f'>{icon(section["icon"])}<span>{escape(label_of(section))}</span></a>{local}</div>')
    return (f'<aside class="o-nav"><details open><summary>{escape(m["nav_summary"])}</summary>'
            f'<nav class="portal-sections" aria-label="{escape(m["nav_label"])}">{"".join(groups)}</nav></details></aside>')


def crumbbar(page, pages, site, has_ctx=False):
    """The line above the title: where the page sits in its section, and the next page of the section."""
    m = messages(site)
    section = next(s for s in site['sections'] if s['id'] == page.section)
    members = section_members(pages, page.section)
    root = members[0] if members else page
    parts = f'<a href="{escape(rel(page.url, root.url))}">{escape(label_of(section))}</a>'
    if page is not root:
        parts += f' / <span aria-current="page">{escape(page.nav_title)}</span>'
    following = ''
    if page in members and members.index(page) + 1 < len(members):
        nxt = members[members.index(page) + 1]
        following = (f'<a class="crumb-next" href="{escape(rel(page.url, nxt.url))}" rel="next"><span>{escape(m["next"])}</span> '
                     f'<strong>{escape(nxt.nav_title)}</strong> &rsaquo;</a>')
    return f'<div class="crumbbar{" has-ctx" if has_ctx else ""}"><div class="crumbline"><nav class="o-eyebrow crumbs" aria-label="{escape(m["breadcrumb"])}">{parts}</nav>{following}</div></div>'


def page_end(page, pages, site):
    """The end of a reading page, as on the overview pages of the kit: back and next within the section, then related pages in boxes."""
    m = messages(site)
    members = section_members(pages, page.section)
    out = ''
    if page in members:
        i = members.index(page)
        prev = members[i - 1] if i > 0 else None
        nxt = members[i + 1] if i + 1 < len(members) else None
        links = ''
        if prev:
            links += f'<a class="pn prev" href="{escape(rel(page.url, prev.url))}" rel="prev"><span>{escape(m["back"])}</span>{escape(prev.nav_title)}</a>'
        if nxt:
            links += f'<a class="pn next" href="{escape(rel(page.url, nxt.url))}" rel="next"><span>{escape(m["next_word"])}</span>{escape(nxt.nav_title)}</a>'
        if links:
            out += f'<nav class="o-pn" aria-label="{escape(m["back"])} / {escape(m["next_word"])}">{links}</nav>'
    related = []
    for pid in page.related:
        if pid not in pages:
            if LENIENT:
                continue
            raise ValueError(f'{page.id}: related page {pid} does not exist')
        related.append(pages[pid])
    if related:
        labels = {s['id']: label_of(s) for s in site['sections']}
        cards = ''.join(
            f'<li class="o-card linked card--compact" data-tip="{escape(r.summary)}" data-tip-title="{escape(r.title)}">'
            f'<p class="card-kicker">{escape(labels[r.section])}</p><h3><a href="{escape(rel(page.url, r.url))}">{escape(r.title)}</a></h3>'
            f'<p class="card-desc">{escape(r.summary)}</p></li>' for r in related)
        out += f'<h2 class="about-deeper">{escape(m["read_further"])}</h2><ul class="o-grid card-list cards-compact read-further">{cards}</ul>'
    return out


# START_CONTRACT: course
#   PURPOSE: Turn a page into a short course: the text before the first section stays as the introduction, each section becomes a tab, and each tab ends with a step to the next.
#   INPUTS: { body: str - rendered page HTML with <h2 id> sections }
#   OUTPUTS: { str - HTML; without the script every section stays visible in order }
#   SIDE_EFFECTS: none
# END_CONTRACT: course
def course(body):
    # what follows the course-end mark (the learning-map step bar, the source) sits below the tabs
    body, _, tail = body.partition('<!--course-end-->')
    parts = re.split(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    intro, sections = parts[0], [(parts[i], parts[i + 1], parts[i + 2]) for i in range(1, len(parts), 3)]
    heads = ''.join(f'<button type="button" role="tab" data-tab="{key}"{" aria-selected=true" if n == 0 else ""}><b>{n + 1}</b><span>{title}</span></button>'
                    for n, (key, title, _) in enumerate(sections))
    panels = ''.join(
        f'<section class="tab-panel" id="{key}" data-tab-panel="{key}"><h2 class="tab-title">{n + 1}. {title}</h2>{html}'
        + (f'<p class="course-next"><a href="#{sections[n + 1][0]}">{T('Дальше:')} {sections[n + 1][1]} →</a></p>' if n + 1 < len(sections) else '')
        + '</section>' for n, (key, title, html) in enumerate(sections))
    return f'{intro}<div class="course" data-tabs><div class="course-tabs" role="tablist">{heads}</div>{panels}</div>{tail}'


def stamp(name):
    """A version mark for a stylesheet or script taken from its content, so a browser never keeps a stale copy after a change."""
    source = SRC / name
    if not source.is_file():
        return ''
    if name not in STAMPS:
        STAMPS[name] = '?v=' + hashlib.sha1(source.read_bytes()).hexdigest()[:10]
    return STAMPS[name]


STAMPS = {}


def render_page(page, pages, site):
    m = messages(site)
    names = site['names'].get(i18n.lang()) or site['names'][i18n.SOURCE]
    here = page.url
    root = posixpath.relpath('.', posixpath.dirname(here))
    asset = lambda name: rel(here, 'assets/' + name) + stamp(name)
    context = ''
    if len(page.headings) >= 2 and page.layout not in ('home', 'course'):
        context = (f'<aside class="o-context" aria-label="{escape(m["on_this_page"])}"><strong>{escape(m["on_this_page"])}</strong>' +
                   ''.join(f'<a class="lv{2 if tag == "h2" else 3}" href="#{i}">{escape(label)}</a>' for tag, i, label in page.headings) + '</aside>')
    subject = quote(m['feedback_subject'].format(id=page.ident))
    section = next(s for s in site['sections'] if s['id'] == page.section)
    extra_head = ''
    if page.layout == 'raw':
        styles = ['tokens.css', 'components.css', 'theme.css'] + [s for s in page.styles if s.startswith('layouts/')]
        extra_head = (''.join(f'<link rel="stylesheet" href="{escape(rel(here, i18n.lang() + "/catalog/assets/styles/" + s))}">' for s in styles) +
                      f'<link rel="stylesheet" href="{escape(asset("discovery.css"))}"><script defer src="{escape(asset("discovery.js"))}"></script>')
    if page.layout == 'raw':
        body = page.body
    elif page.layout == 'course':
        body = (f'<div class="o-reading o-single"><div class="o-copy"><h1>{escape(page.title)}</h1><article class="page-body o-doc">{course(page.body)}</article>{page_end(page, pages, site)}</div></div>')
    elif page.layout == 'home':
        # the front page carries its own title inside the hero; the page identifier sits beside it
        body = f'<div class="o-wide">{page.body}</div>'
    else:
        single = '' if context else ' o-single'
        body = (f'<div class="o-reading{single}"><div class="o-copy"><h1>{escape(page.title)}</h1><article class="page-body o-doc">{page.body}</article>{page_end(page, pages, site)}</div>{context}</div>')
    return f'''<!doctype html>
<html lang="{i18n.lang()}" data-theme="light"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark">
<title>{escape(page.title)} · {escape(names["title"])}</title>
<script>try{{var t=localStorage.getItem('hub-theme');document.documentElement.dataset.theme=t==='dark'?'dark':'light';}}catch(e){{}}</script>
{extra_head}{''.join(f'<link rel="stylesheet" href="{asset("ui/" + n)}">' for n in ('fonts.css', 'tokens.css', 'primitives.css', 'workspace.css'))}<link rel="stylesheet" href="{asset("site.css")}">
<script src="{asset("search-" + i18n.lang() + ".js")}"></script>{edition_script(asset)}<script src="{asset("site.js")}" defer data-root="{escape(root)}" data-t-none="{escape(m["search_none"])}" data-t-light="{escape(m["theme_to_light"])}" data-t-dark="{escape(m["theme_to_dark"])}" data-t-mail-body="{escape(m["fb_mail_body"])}"></script>
</head><body class="portal-workspace" data-portal-section="{page.section}" data-page="{escape(page.id)}">
<a class="o-skip" href="#main">{escape(m["skip"])}</a>
<header class="o-header">
  <a class="o-identity" href="{escape(rel(here, url_of("index")))}"><img src="{escape(rel(here, "assets/ui/assets/logos/hub-mark.svg"))}" width="36" height="36" alt=""><span>{escape(names["title"])}</span></a>
  <span class="header-scope">{escape(label_of(section))}</span>
  <div class="o-search" role="search"><label class="o-sr-only" for="q">{escape(m["search_label"])}</label><input id="q" type="search" autocomplete="off" placeholder="{escape(m["search_label"])}" aria-controls="results"><div id="results" class="o-search-results" hidden></div></div>
  <div class="o-tools">{language_switch(page, site)}<button id="theme-switch" type="button" class="theme-switch" aria-label="{escape(m["theme_to_dark"])}" title="{escape(m["theme_to_dark"])}"><span class="ts-moon">{icon("moon")}</span><span class="ts-sun">{icon("sun")}</span></button></div>
</header>
<div class="o-frame">{navigation(page, pages, site)}
<main class="o-main hub-main" id="main" tabindex="-1">
{'' if page.layout == 'raw' else crumbbar(page, pages, site, bool(context))}
{body}
</main>
<footer class="o-footbar">
<nav class="fb-left" aria-label="{escape(m["legal_label"])}"><a href="{escape(rel(here, pages["privacy"].url))}"{' aria-current="page"' if page.id == "privacy" else ""}>{escape(m["privacy"])}</a><a href="{escape(rel(here, pages["terms-of-use"].url))}"{' aria-current="page"' if page.id == "terms-of-use" else ""}>{escape(m["terms_of_use"])}</a></nav>
<div class="fb-right"><span class="foot-text">{escape(m["footer"])} <a class="contact" href="mailto:{site["contact"]}?subject={subject}">{escape(m["contact_us"])}</a></span>
<button type="button" class="pagefb" data-dialog="fb" aria-haspopup="dialog"><span>{escape(m["pagefb"])}</span><span>ID: {page.ident}</span></button></div>
</footer>
</div>
<dialog id="fb" class="fb" aria-labelledby="fb-t" data-subject="{escape(m["feedback_subject"].format(id=page.ident))}" data-ref="{page.ident}" data-page="{escape(page.title)}">
  <form method="dialog">
    <div class="fb-head"><h2 id="fb-t">{escape(m["pagefb"])}</h2><code>ID: {page.ident}</code></div>
    <div class="fb-body"><p>{escape(m["fb_prov"])} <a data-mail href="mailto:{site["contact"]}">{escape(m["fb_word"])}</a>.</p><button class="oc-button" value="close">{escape(m["fb_close"])}</button></div>
  </form>
</dialog>
</body></html>
'''


def edition_script(asset):
    """The page script's words in the edition's language (none for Russian, the script's own language)."""
    return '' if i18n.lang() == i18n.SOURCE else f'<script src="{asset("i18n-" + i18n.lang() + ".js")}"></script>'


def language_switch(page, site):
    """A link to the same page in each other edition; the page script carries the reader's place (#part) along."""
    out = ''
    for other in site['languages']:
        if other == i18n.lang():
            continue
        name = site.get('language_names', {}).get(other, {'short': other.upper(), 'name': other})
        out += (f'<a class="lang-switch" href="{escape(rel(page.url, url_of(page.id, other)))}" hreflang="{other}" lang="{other}" '
                f'data-lang-switch title="{escape(name["name"])}" aria-label="{escape(name["name"])}">{escape(name["short"])}</a>')
    return out


def search_entries(page):
    entries = [{'u': page.url, 't': next_label(page), 'h': page.title, 'x': plain(page.body)[:360]}]
    if page.layout == 'raw':
        # every scenario of the catalog is found by its title and intent, and the result opens it
        for m in re.finditer(r'<details class="scenario-card"[^>]*\bid="([^"]+)".*?<h3[^>]*>(.*?)</h3>.*?(?:<p class="scenario-card__intent">(.*?)</p>|</summary>)', page.body, re.S):
            entries.append({'u': page.url + '#' + m[1], 't': page.title, 'h': plain(m[2]), 'x': plain(m[3] or '')[:240]})
        return entries
    for tag, ident, label in page.headings:
        entries.append({'u': page.url + '#' + ident, 't': page.title, 'h': label, 'x': ''})
    return entries


def next_label(page):
    """The name of the page's section in the edition's language, shown under a search result."""
    section = SECTIONS.get(page.section)
    return label_of(section) if section else page.section


SECTIONS = {s['id']: s for s in json.loads((SRC / 'site.json').read_text(encoding='utf-8'))['sections']}


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def publish_sources(site):
    """The source files of this version, so it can be read without the repository; one listing page per edition."""
    base = OUT / 'sources'
    listing = []
    for folder in ('content', 'vocabulary', 'cards', 'reference', 'learning', 'i18n'):
        for path in sorted((SRC / folder).rglob('*')):
            if path.is_file() and path.suffix in ('.md', '.yaml', '.yml', '.json'):
                target = base / path.relative_to(SRC)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
                listing.append(path.relative_to(SRC).as_posix())
    items = ''.join(f'<li><a href="{escape(quote(item))}">{escape(item)}</a></li>' for item in listing)
    for language in site['languages']:
        i18n.use(language)
        m = messages(site)
        name = 'index.html' if language == i18n.SOURCE else f'index-{language}.html'
        write(base / name, f'<!doctype html><html lang="{language}"><head><meta charset="utf-8"><title>{escape(m["sources_title"])}</title></head>'
              f'<body style="font:16px/1.5 system-ui,sans-serif;max-width:60rem;margin:2rem auto;padding:0 1rem"><h1>{escape(m["sources_title"])}</h1>'
              f'<p>{escape(m["sources_intro"])} <a href="../{language}/index.html">{escape(m["back_to_site"])}</a></p><ul>{items}</ul></body></html>\n')
    i18n.use(i18n.SOURCE)
    return len(listing) + 1


# START_CONTRACT: build_edition
#   PURPOSE: Write one edition (the language set by i18n.use): its pages, its search index, its catalog assets and, for a translation, the page script's words.
#   INPUTS: { site: dict; terms: dict }
#   OUTPUTS: { dict - page id to Page }
#   SIDE_EFFECTS: Writes html/aicc/v2/<lang>/ and assets/search-<lang>.js (and assets/i18n-<lang>.js).
# END_CONTRACT: build_edition
def build_edition(site, terms):
    language = i18n.lang()
    pages = load_pages(site, terms)
    load_catalog(pages)
    add_generated(pages, site, terms)
    taken = set()
    for page_id in sorted(pages):
        pages[page_id].ident = short_id(page_id, taken)
    for page in pages.values():
        if page.source is not None and page.layout != 'raw':
            page.body = render_markdown(page.body, page, terms, pages, site)
        else:
            page.headings = []
    for page in pages.values():
        write(OUT / page.url, render_page(page, pages, site))
    entries = [e for page in sorted(pages.values(), key=lambda p: p.id) for e in search_entries(page)]
    write(OUT / 'assets' / f'search-{language}.js', 'window.AICC_SEARCH_INDEX=' + json.dumps(entries, ensure_ascii=False, separators=(',', ':')) + ';\n')
    if (SRC / 'catalog').exists():
        shutil.copytree(SRC / 'catalog' / 'assets', OUT / language / 'catalog' / 'assets')
    if language != i18n.SOURCE:
        write(OUT / 'assets' / f'i18n-{language}.js', 'window.HUB_I18N=' + json.dumps(i18n.table(), ensure_ascii=False, separators=(',', ':'), sort_keys=True) + ';\n')
    return pages


# START_CONTRACT: build
#   PURPOSE: Write the whole site: every edition, the shared assets, the language entry and the source files.
#   INPUTS: { }
#   OUTPUTS: { dict - counts }
#   SIDE_EFFECTS: Replaces html/aicc/v2.
# END_CONTRACT: build
def build():
    site = load_site()
    terms = load_terms()
    shutil.rmtree(OUT, ignore_errors=True)
    editions = {}
    for language in site['languages']:
        i18n.use(language)
        editions[language] = build_edition(site, terms)
    i18n.use(i18n.SOURCE)
    pages = editions[i18n.SOURCE]
    shutil.copytree(SRC / 'ui', OUT / 'assets' / 'ui', ignore=shutil.ignore_patterns('icons'))
    shutil.copy(SRC / 'site.css', OUT / 'assets' / 'site.css')
    shutil.copy(SRC / 'site.js', OUT / 'assets' / 'site.js')
    if (SRC / 'catalog').exists():
        shutil.copy(SRC / 'catalog' / 'discovery.css', OUT / 'assets' / 'discovery.css')
        shutil.copy(SRC / 'catalog' / 'discovery.js', OUT / 'assets' / 'discovery.js')
    write(OUT / 'index.html', '<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=ru/index.html">'
          '<script>location.replace("ru/index.html"+location.hash)</script>'  # straight to the Russian edition, no flash of an entry page
          f'<title>{escape(site["names"]["ru"]["title"])}</title></head><body><main><h1><a href="ru/index.html">{escape(site["names"]["ru"]["title"])}</a></h1></main></body></html>\n')
    sources = publish_sources(site)
    ids = {p.id: p.ident for p in pages.values()}
    write(OUT / 'assets' / 'page-ids.json', json.dumps(ids, ensure_ascii=False, indent=1, sort_keys=True) + '\n')
    fallbacks = {lang: sorted(p.id for p in eds.values() if getattr(p, 'fallback', False)) for lang, eds in editions.items() if lang != i18n.SOURCE}
    return {'pages': len(pages), 'terms': len(terms), 'sources': sources, 'editions': len(editions),
            'fallbacks': {k: len(v) for k, v in fallbacks.items()}, 'missing': len(i18n.missing())}


if __name__ == '__main__':
    counts = build()
    print('built v2: %(pages)d pages, %(terms)d terms, %(sources)d source files' % counts)
    if counts['editions'] > 1:
        print('editions: %d; pages on the Russian text: %s; strings without a translation: %d' % (counts['editions'], counts['fallbacks'], counts['missing']))
