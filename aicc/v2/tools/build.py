#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Build the AI Competence Hub site (version 2) from its Russian Markdown pages, vocabulary and project cards.
#   SCOPE: Reads aicc/v2 only; writes html/aicc/v2 only. Self-contained: shares no code or file with version 1.
#   DEPENDS: markdown-it-py, PyYAML
#   LINKS: C-HUB-V2, M-HUB-V2-CHECK
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   ROOT, SRC, OUT - repository root, source folder, output folder
#   load_site - read site.json
#   load_terms - read the vocabulary
#   short_id - stable five-character page identifier
#   load_pages - read the Markdown pages and the generated pages
#   render_markdown - Markdown to HTML with term markers, page links and heading ids
#   build - write the whole site
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


def url_of(page_id, lang='ru'):
    """The file of a page below the site root; every address names its file so the site also opens from a folder."""
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
    """A vocabulary term as it appears in running text: the Russian word with the English term beside it, linked to the vocabulary."""
    entry = terms[key]
    href = rel(here, url_of('vocabulary')) + '#' + key
    return (f'<a class="term" href="{href}" title="{escape(entry["definition"], quote=True)}">'
            f'{escape(surface or entry["ru"])} <span class="term-en">({escape(entry["en"])})</span></a>')


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

    text = TERM.sub(term, text)
    text = PAGE_LINK.sub(link, text)
    text = HTML_PAGE_LINK.sub(html_link, text)
    text = ICON.sub(lambda m: icon(m[1]), text)
    md = MarkdownIt('commonmark', {'html': True}).enable('table')
    tokens = md.parse(text)
    used = set()
    page.headings = []
    for i, token in enumerate(tokens):
        if token.type == 'heading_open':
            inline = tokens[i + 1]
            explicit = re.search(r'\s*\{#([\w-]+)\}\s*$', inline.content)
            if explicit:
                inline.content = inline.content[:explicit.start()]
                if inline.children and inline.children[-1].type == 'text':
                    inline.children[-1].content = re.sub(r'\s*\{#[\w-]+\}\s*$', '', inline.children[-1].content)
            label = plain(md.renderer.renderInline(inline.children, md.options, {}))
            ident = explicit[1] if explicit else slug(label)
            n = 2
            base = ident
            while ident in used:
                ident = f'{base}-{n}'
                n += 1
            used.add(ident)
            token.attrSet('id', ident)
            if token.tag in ('h2', 'h3'):
                page.headings.append((token.tag, ident, label))
    html = md.renderer.render(tokens, md.options, {})
    return html.replace('<table>', '<div class="o-table-wrap"><table>').replace('</table>', '</table></div>')


def load_pages(site, terms):
    pages = {}
    content = SRC / 'content' / 'ru'
    for path in sorted(content.rglob('*.md')):
        relative = path.relative_to(content).with_suffix('')
        page_id = relative.as_posix()
        if page_id.endswith('/index'):
            page_id = page_id[:-len('/index')]
        meta, body = front_matter(path.read_text(encoding='utf-8'), path)
        first = page_id.split('/')[0]
        section = 'hub' if page_id == 'index' or first not in {s['id'] for s in site['sections']} else first
        pages[page_id] = Page(page_id, meta['title'], section, int(meta.get('order', 100)), meta.get('summary', ''), body,
                              source=path, nav=str(meta.get('nav', 'true')).lower() not in ('false', 'no', '0'), nav_title=meta.get('nav_title'), layout=meta.get('layout', ''))
    return pages


def add_generated(pages, site, terms):
    """Pages that are projections of data rather than Markdown: the vocabulary, and later the card views."""
    rows = ''.join(
        f'<tr id="{escape(t["id"])}"><td><strong>{escape(t["ru"])}</strong> <span class="term-en">({escape(t["en"])})</span></td>'
        f'<td>{escape(t["definition"])}</td></tr>' for t in sorted(terms.values(), key=lambda t: t['ru'].casefold()))
    m = site['messages']['ru']
    body = (f'<p class="lede">{escape(m["vocabulary_intro"])}</p><div class="o-table-wrap"><table class="vocabulary"><thead><tr>'
            f'<th>{escape(m["vocabulary_term"])}</th><th>{escape(m["vocabulary_definition"])}</th></tr></thead><tbody>{rows}</tbody></table></div>')
    pages['vocabulary'] = Page('vocabulary', 'Словарь', 'vocabulary', 0, m['vocabulary_intro'], body)
    import cards
    cards.add_pages(pages, site, terms, sys.modules[__name__])


def section_members(pages, section_id):
    return sorted((p for p in pages.values() if p.section == section_id and p.nav), key=lambda p: (p.order, p.title.casefold()))


def navigation(page, pages, site):
    groups = []
    m = site['messages']['ru']
    for section in site['sections']:
        members = section_members(pages, section['id'])
        if not members:
            continue
        first = members[0]
        current = section['id'] == page.section
        local = ''
        if current and len(members) > 1:
            # Large sections list their top pages; the pages of the area the reader is in open beside them.
            area = '/'.join(page.id.split('/')[:2])
            shown = [p for p in members if p.id.count('/') <= 1 or p.id.startswith(area + '/')]
            local = '<div class="portal-local-nav">' + ''.join(
                f'<a{" class=nav-sub" if p.id.count("/") >= 2 else ""} href="{escape(rel(page.url, p.url))}"' + (' aria-current="page"' if p is page else '') + f'>{escape(p.nav_title)}</a>'
                for p in shown) + '</div>'
        groups.append(f'<div class="portal-nav-group{" is-current" if current else ""}"><a class="portal-section-link" data-section="{section["id"]}" '
                      f'href="{escape(rel(page.url, first.url))}"' + (' aria-current="true"' if current else '') +
                      f'>{icon(section["icon"])}<span>{escape(section["label"]["ru"])}</span></a>{local}</div>')
    legal = ''.join(f'<a href="{escape(rel(page.url, pages[pid].url))}"' + (' aria-current="page"' if pages[pid] is page else '') + f'>{escape(m[key])}</a>'
                    for pid, key in (('privacy', 'privacy'), ('terms-of-use', 'terms_of_use')))
    foot = f'<div class="nav-foot"><div class="nav-legal">{legal}</div></div>'
    return (f'<aside class="o-nav"><details open><summary>{escape(m["nav_summary"])}</summary>'
            f'<nav class="portal-sections" aria-label="{escape(m["nav_label"])}">{"".join(groups)}</nav></details>{foot}</aside>')


def crumbbar(page, pages, site):
    """The line above the title: where the page sits in its section, and the next page of the section."""
    m = site['messages']['ru']
    section = next(s for s in site['sections'] if s['id'] == page.section)
    members = section_members(pages, page.section)
    root = members[0] if members else page
    parts = f'<a href="{escape(rel(page.url, root.url))}">{escape(section["label"]["ru"])}</a>'
    if page is not root:
        parts += f' / <span aria-current="page">{escape(page.nav_title)}</span>'
    following = ''
    if page in members and members.index(page) + 1 < len(members):
        nxt = members[members.index(page) + 1]
        following = (f'<a class="crumb-next" href="{escape(rel(page.url, nxt.url))}" rel="next"><span>{escape(m["next"])}</span> '
                     f'<strong>{escape(nxt.nav_title)}</strong> &rsaquo;</a>')
    return f'<div class="crumbbar"><div class="crumbline"><nav class="o-eyebrow crumbs" aria-label="{escape(m["breadcrumb"])}">{parts}</nav>{following}</div></div>'


def render_page(page, pages, site):
    m = site['messages']['ru']
    names = site['names']['ru']
    here = page.url
    root = posixpath.relpath('.', posixpath.dirname(here))
    asset = lambda name: rel(here, 'assets/' + name)
    toc = ''
    if len(page.headings) >= 4 and page.layout != 'home':
        toc = (f'<nav class="page-toc" aria-label="{escape(m["on_this_page"])}"><strong>{escape(m["on_this_page"])}</strong><ul>' +
               ''.join(f'<li class="{tag}"><a href="#{i}">{escape(label)}</a></li>' for tag, i, label in page.headings) + '</ul></nav>')
    subject = quote(m['feedback_subject'].format(id=page.ident))
    section = next(s for s in site['sections'] if s['id'] == page.section)
    if page.layout == 'home':
        # the front page carries its own title inside the hero; the page identifier sits beside it
        head, lede = '', ''
        body = f'<div class="o-wide">{page.body}</div>'
    else:
        lede = f'<p class="lede">{escape(page.summary)}</p>' if page.summary and page.id != 'vocabulary' else ''
        head = f'<div class="page-title"><h1>{escape(page.title)}</h1></div>'
        body = page.body
    return f'''<!doctype html>
<html lang="ru" data-theme="light"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark">
<title>{escape(page.title)} · {escape(names["title"])}</title>
<script>try{{var t=localStorage.getItem('hub-theme');document.documentElement.dataset.theme=t==='dark'?'dark':'light';}}catch(e){{}}</script>
{''.join(f'<link rel="stylesheet" href="{asset("ui/" + n)}">' for n in ('fonts.css', 'tokens.css', 'primitives.css', 'workspace.css'))}<link rel="stylesheet" href="{asset("site.css")}">
<script src="{asset("search-ru.js")}"></script><script src="{asset("site.js")}" defer data-root="{escape(root)}" data-t-none="{escape(m["search_none"])}" data-t-light="{escape(m["theme_to_light"])}" data-t-dark="{escape(m["theme_to_dark"])}" data-t-mail-body="{escape(m["fb_mail_body"])}"></script>
</head><body class="portal-workspace" data-portal-section="{page.section}" data-page="{escape(page.id)}">
<a class="o-skip" href="#main">{escape(m["skip"])}</a>
<header class="o-header">
  <a class="o-identity" href="{escape(rel(here, url_of("index")))}"><img src="{escape(rel(here, "assets/ui/assets/logos/hub-mark.svg"))}" width="36" height="36" alt=""><span>{escape(names["title"])}</span></a>
  <span class="header-scope">{escape(section["label"]["ru"])}</span>
  <span class="status-chip" title="{escape(m["status_chip_title"])}">{escape(m["status_chip"])}</span>
  <div class="o-search" role="search"><label class="o-sr-only" for="q">{escape(m["search_label"])}</label><input id="q" type="search" autocomplete="off" placeholder="{escape(m["search_label"])}" aria-controls="results"><div id="results" class="o-search-results" hidden></div></div>
  <div class="o-tools"><button id="theme-switch" type="button" class="theme-switch" aria-label="{escape(m["theme_to_dark"])}" title="{escape(m["theme_to_dark"])}"><span class="ts-moon">{icon("moon")}</span><span class="ts-sun">{icon("sun")}</span></button></div>
</header>
<div class="o-frame">{navigation(page, pages, site)}
<main class="o-main hub-main" id="main" tabindex="-1">
{crumbbar(page, pages, site)}
{head}{lede}{toc}
<article class="page-body">{body}</article>
<footer class="o-footer"><span class="foot-text">{escape(m["footer"])} <a class="contact" href="mailto:{site["contact"]}?subject={subject}">{escape(m["contact_us"])}</a> <a class="contact" href="{escape(rel(here, pages["privacy"].url))}">{escape(m["privacy"])}</a> <a class="contact" href="{escape(rel(here, pages["terms-of-use"].url))}">{escape(m["terms_of_use"])}</a> <a class="contact" href="{escape(rel(here, "sources/index.html"))}">{escape(m["sources_title"])}</a></span>
<button type="button" class="pagefb" data-dialog="fb" aria-haspopup="dialog"><span>{escape(m["pagefb"])}</span><span>ID: {page.ident}</span></button></footer>
</main></div>
<dialog id="fb" class="fb" aria-labelledby="fb-t" data-subject="{escape(m["feedback_subject"].format(id=page.ident))}" data-ref="{page.ident}" data-page="{escape(page.title)}">
  <form method="dialog">
    <div class="fb-head"><h2 id="fb-t">{escape(m["pagefb"])}</h2><code>ID: {page.ident}</code></div>
    <div class="fb-body"><p>{escape(m["fb_prov"])} <a data-mail href="mailto:{site["contact"]}">{escape(m["fb_word"])}</a>.</p><button class="oc-button" value="close">{escape(m["fb_close"])}</button></div>
  </form>
</dialog>
</body></html>
'''


def search_entries(page):
    entries = [{'u': page.url, 't': next_label(page), 'h': page.title, 'x': plain(page.body)[:360]}]
    for tag, ident, label in page.headings:
        entries.append({'u': page.url + '#' + ident, 't': page.title, 'h': label, 'x': ''})
    return entries


def next_label(page):
    return page.section


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def publish_sources(site):
    """The source files of this version, so it can be read without the repository."""
    base = OUT / 'sources'
    listing = []
    for folder in ('content', 'vocabulary', 'cards'):
        for path in sorted((SRC / folder).rglob('*')):
            if path.is_file() and path.suffix in ('.md', '.yaml', '.yml', '.json'):
                target = base / path.relative_to(SRC)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
                listing.append(path.relative_to(SRC).as_posix())
    m = site['messages']['ru']
    items = ''.join(f'<li><a href="{escape(quote(item))}">{escape(item)}</a></li>' for item in listing)
    write(base / 'index.html', f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>{escape(m["sources_title"])}</title></head>'
          f'<body style="font:16px/1.5 system-ui,sans-serif;max-width:60rem;margin:2rem auto;padding:0 1rem"><h1>{escape(m["sources_title"])}</h1>'
          f'<p>{escape(m["sources_intro"])} <a href="../ru/index.html">{escape(m["back_to_site"])}</a></p><ul>{items}</ul></body></html>\n')
    return len(listing) + 1


# START_CONTRACT: build
#   PURPOSE: Write the whole site: pages, search index, assets, the language entry and the source files.
#   INPUTS: { }
#   OUTPUTS: { dict - counts }
#   SIDE_EFFECTS: Replaces html/aicc/v2.
# END_CONTRACT: build
def build():
    site = load_site()
    terms = load_terms()
    pages = load_pages(site, terms)
    add_generated(pages, site, terms)
    taken = set()
    for page_id in sorted(pages):
        pages[page_id].ident = short_id(page_id, taken)
    for page in pages.values():
        if page.source is not None:
            page.body = render_markdown(page.body, page, terms, pages, site)
        else:
            page.headings = []
    shutil.rmtree(OUT, ignore_errors=True)
    for page in pages.values():
        write(OUT / page.url, render_page(page, pages, site))
    entries = [e for page in sorted(pages.values(), key=lambda p: p.id) for e in search_entries(page)]
    write(OUT / 'assets' / 'search-ru.js', 'window.AICC_SEARCH_INDEX=' + json.dumps(entries, ensure_ascii=False, separators=(',', ':')) + ';\n')
    shutil.copytree(SRC / 'ui', OUT / 'assets' / 'ui', ignore=shutil.ignore_patterns('icons'))
    shutil.copy(SRC / 'site.css', OUT / 'assets' / 'site.css')
    shutil.copy(SRC / 'site.js', OUT / 'assets' / 'site.js')
    write(OUT / 'index.html', '<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=ru/index.html">'
          f'<title>{escape(site["names"]["ru"]["title"])}</title></head><body><main><h1><a href="ru/index.html">{escape(site["names"]["ru"]["title"])}</a></h1></main></body></html>\n')
    sources = publish_sources(site)
    ids = {p.id: p.ident for p in pages.values()}
    write(OUT / 'assets' / 'page-ids.json', json.dumps(ids, ensure_ascii=False, indent=1, sort_keys=True) + '\n')
    return {'pages': len(pages), 'terms': len(terms), 'sources': sources}


if __name__ == '__main__':
    counts = build()
    print('built v2: %(pages)d pages, %(terms)d terms, %(sources)d source files' % counts)
