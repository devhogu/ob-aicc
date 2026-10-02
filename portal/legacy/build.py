#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Render the AICC portal sources into the static site under html/aicc.
#   SCOPE: Reads portal content, messages, templates, assets and UI kit; writes the output directory completely on each run.
#   DEPENDS: none
#   LINKS: M-PORTAL-SOURCE, M-PORTAL-PROJECTION, V-M-PORTAL-SOURCE
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   ROOT - module-internal helper or constant
#   REPO - module-internal helper or constant
#   DEFAULT_OUT - module-internal helper or constant
#   LANGS - module-internal helper or constant
#   PAGE_ORDER - module-internal helper or constant
#   Site - module-internal helper or constant
#   icon - module-internal helper or constant
#   logo_svg - module-internal helper or constant
#   fill - module-internal helper or constant
#   inline - module-internal helper or constant
#   PageRenderer - module-internal helper or constant
#   page_dir - module-internal helper or constant
#   link - module-internal helper or constant
#   render_page - one page in one language with per-field fallback to the source language
#   render_gateway - site root page that leads to /ru/
#   copy_tree - module-internal helper or constant
#   build - regenerate tokens.css and the whole static site
# END_MODULE_MAP
"""Render the AICC portal into a static site.

Sources: portal/content/*.json (one file per page, per-field translations), portal/messages/*.json
(interface text), portal/templates, portal/assets, portal/ui-comps, portal/tokens.
Output: html/aicc/ (default). The output directory is replaced completely on every run.
"""
import argparse
import html
import json
import os
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tokens  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
DEFAULT_OUT = REPO / 'html' / 'aicc'
LANGS = ('ru', 'en')          # ru is primary
PAGE_ORDER = ('home', 'statement-of-intent')


class Site:
    def __init__(self):
        self.messages = {l: json.loads((ROOT / f'messages/{l}.json').read_text(encoding='utf-8')) for l in LANGS}
        self.pages = {}
        for pid in PAGE_ORDER:
            self.pages[pid] = json.loads((ROOT / f'content/{pid}.json').read_text(encoding='utf-8'))
        self.templates = {n: (ROOT / f'templates/{n}.html').read_text(encoding='utf-8') for n in ('page', 'gateway')}
        self.warnings = []


def icon(name):
    svg = (ROOT / f'ui-comps/icons/ui-{name}.svg').read_text(encoding='utf-8')
    svg = re.sub(r'\s+', ' ', svg).strip()
    return svg.replace('<svg ', '<svg class="oc-icon" aria-hidden="true" focusable="false" ', 1)


def logo_svg():
    """Inline O!Bank logo. The magenta mark keeps its artwork colour; the white wordmark follows the text colour."""
    svg = (ROOT / 'ui-comps/logos/obank-on-dark.svg').read_text(encoding='utf-8')
    svg = re.sub(r'\sstyle="[^"]*"', '', svg)
    svg = re.sub(r'<path([^>]*) fill="white"', r'<path\1 fill="currentColor"', svg)
    svg = re.sub(r'^<svg [^>]*>', '<svg class="site-logo" role="img" aria-label="O!Bank" viewBox="0 0 240 91" width="105" height="40" fill="none" xmlns="http://www.w3.org/2000/svg">', svg)
    return re.sub(r'\s+', ' ', svg).strip()


def fill(template, values):
    def sub(m):
        return values[m.group(1)]
    return re.sub(r'\{\{(\w+)\}\}', sub, template)


# ---- inline markup: **bold**, *italic*, `code`, [text](https://...) ----
def inline(text):
    out = html.escape(text, quote=False)
    out = re.sub(r'`([^`]+)`', r'<code>\1</code>', out)
    out = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', out)
    out = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'<em>\1</em>', out)
    out = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', r'<a href="\2">\1</a>', out)
    return out


class PageRenderer:
    def __init__(self, site, page, lang):
        self.site, self.page, self.lang = site, page, lang
        self.missing = []          # field paths rendered from the source language

    def field(self, value, path):
        """Return (text, language) for a per-language field, falling back to the source language."""
        if self.lang in value:
            return value[self.lang], self.lang
        src = self.page['source_language']
        self.missing.append(path)
        return value[src], src

    def attr(self, lang):
        return '' if lang == self.lang else f' lang="{lang}"'

    def text_html(self, value, path):
        text, lang = self.field(value, path)
        return inline(text), self.attr(lang)

    def block(self, i, b, href_to):
        t = b['type']
        p = f'blocks[{i}]'
        if t in ('h2', 'h3', 'p', 'lead'):
            content, la = self.text_html(b['text'], p + '.text')
            if t == 'lead':
                return f'<p class="oc-lede"{la}>{content}</p>'
            return f'<{t}{la}>{content}</{t}>'
        if t in ('ul', 'ol'):
            items = []
            for j, item in enumerate(b['items']):
                content, la = self.text_html(item, f'{p}.items[{j}]')
                items.append(f'<li{la}>{content}</li>')
            return f'<{t}>\n' + '\n'.join(items) + f'\n</{t}>'
        if t == 'table':
            head = ''
            for j, h in enumerate(b['header']):
                content, la = self.text_html(h, f'{p}.header[{j}]')
                head += f'<th scope="col"{la}>{content}</th>'
            rows = []
            for r, row in enumerate(b['rows']):
                cells = ''
                for c, cell in enumerate(row):
                    content, la = self.text_html(cell, f'{p}.rows[{r}][{c}]')
                    cells += f'<td{la}>{content}</td>'
                rows.append(f'<tr>{cells}</tr>')
            return ('<div class="oc-tablewrap" tabindex="0" role="region" aria-label="' +
                    html.escape(self.title_text(), quote=True) + '">\n<table class="oc-table">\n<thead><tr>' + head +
                    '</tr></thead>\n<tbody>\n' + '\n'.join(rows) + '\n</tbody>\n</table>\n</div>')
        if t == 'cards':
            cards = []
            for j, item in enumerate(b['items']):
                k, kl = self.text_html(item['kicker'], f'{p}.items[{j}].kicker')
                ti, tl = self.text_html(item['title'], f'{p}.items[{j}].title')
                n, nl = self.text_html(item['note'], f'{p}.items[{j}].note')
                cards.append(f'<a class="oc-card" href="{href_to(item["page"])}">'
                             f'<span class="oc-card__kicker"{kl}>{k}</span><h3{tl}>{ti}</h3>'
                             f'<p class="oc-card__note"{nl}>{n}</p></a>')
            return '<div class="oc-cardgrid">\n' + '\n'.join(cards) + '\n</div>'
        raise ValueError(f'unknown block type {t!r}')

    def title_text(self):
        title = self.page['title']
        return title.get(self.lang, title[self.page['source_language']])


def page_dir(pid, lang):
    return Path(lang) / ('' if pid == 'home' else pid)


def link(from_dir, to_dir):
    rel = os.path.relpath(to_dir, from_dir)
    rel = '' if rel == '.' else rel.replace(os.sep, '/') + '/'
    return rel + 'index.html'


def render_page(site, pid, lang):
    page = site.pages[pid]
    msg = site.messages[lang]
    here = page_dir(pid, lang)
    depth = len(here.parts)
    root = '../' * depth
    rd = PageRenderer(site, page, lang)

    def href_to(target):
        return link(here, page_dir(target, lang))

    body_blocks = [rd.block(i, b, href_to) for i, b in enumerate(page['blocks'])]
    title_val = page['title']
    if lang in title_val:
        title_text, title_lang = title_val[lang], lang
    else:
        title_text, title_lang = title_val[page['source_language']], page['source_language']
        rd.missing.append('title')
    h1 = f'<h1{rd.attr(title_lang)}>{inline(title_text)}</h1>'
    parts = []
    if rd.missing:
        parts.append(f'<p class="oc-notice" role="note">{html.escape(msg["translation_missing"])}</p>')
        site.warnings.append(f'{pid}/{lang}: {len(rd.missing)} field(s) shown in {page["source_language"]}: '
                             + ', '.join(rd.missing[:4]) + (' ...' if len(rd.missing) > 4 else ''))
    if 'eyebrow' in page:
        eb, ebl = rd.text_html(page['eyebrow'], 'eyebrow')
        parts.append(f'<p class="oc-eyebrow"{ebl}>{eb}</p>')
    parts.append(h1)
    parts.extend(body_blocks)
    if 'source' in page:
        note = msg['source_language_note'].format(language=msg['source_language_' + page['source_language']],
                                                  revision=page['source_revision'])
        parts.append(f'<p class="oc-source-note">{html.escape(note)}</p>')

    nav = []
    for other in PAGE_ORDER:
        cur = ' aria-current="page"' if other == pid else ''
        label = msg[site.pages[other]['nav']]
        nav.append(f'    <a href="{href_to(other)}"{cur}>{html.escape(label)}</a>')
    lang_links = []
    for l in LANGS:
        name = site.messages[l]['language_name_' + l]
        cur = ' aria-current="true"' if l == lang else ''
        lang_links.append(f'    <a href="{link(here, page_dir(pid, l))}" lang="{l}" hreflang="{l}" data-lang="{l}"{cur}>{html.escape(name)}</a>')

    values = {
        'lang': lang, 'root': root, 'home_href': href_to('home'),
        'title': html.escape(title_text, quote=False), 'portal_name': html.escape(msg['portal_name']),
        'portal_short': html.escape(msg['portal_short']), 'skip': html.escape(msg['skip']),
        'nav_label': html.escape(msg['nav_label']), 'menu_open': html.escape(msg['menu_open']),
        'menu_close': html.escape(msg['menu_close']), 'theme_to_dark': html.escape(msg['theme_to_dark']),
        'theme_to_light': html.escape(msg['theme_to_light']), 'language_label': html.escape(msg['language_label']),
        'footer': html.escape(msg['footer']), 'nav': '\n'.join(nav), 'lang_links': '\n'.join(lang_links),
        'badge_draft': html.escape(msg['badge_draft']), 'sidebar_eyebrow': html.escape(msg['sidebar_eyebrow']),
        'logo': logo_svg(),
        'icon_menu': icon('menu'), 'icon_sun': icon('sun'), 'icon_moon': icon('moon'),
        'body': '\n'.join(parts),
    }
    return fill(site.templates['page'], values)


def render_gateway(site):
    msg = site.messages['ru']
    return fill(site.templates['gateway'], {k: html.escape(msg[k]) for k in ('gateway_title', 'gateway_link')})


def copy_tree(src, dst):
    for path in sorted(src.rglob('*')):
        if path.is_file():
            target = dst / path.relative_to(src)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(path.read_bytes())


def build(out=DEFAULT_OUT, quiet=False):
    results = tokens.write_tokens()
    failed = [r for r in results if not r['pass']]
    if failed:
        raise SystemExit(f'contrast check failed: {failed}')
    site = Site()
    if out.exists():
        shutil.rmtree(out)
    (out / 'assets/tokens').mkdir(parents=True)
    (out / 'assets/tokens/tokens.css').write_bytes((ROOT / 'tokens/tokens.css').read_bytes())
    (out / 'assets/aicc.css').write_bytes((ROOT / 'assets/aicc.css').read_bytes())
    (out / 'assets/site.js').write_bytes((ROOT / 'assets/site.js').read_bytes())
    copy_tree(ROOT / 'ui-comps', out / 'assets/ui-comps')
    (out / 'index.html').write_text(render_gateway(site), encoding='utf-8')
    for lang in LANGS:
        for pid in PAGE_ORDER:
            target = out / page_dir(pid, lang) / 'index.html'
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(render_page(site, pid, lang), encoding='utf-8')
    if not quiet:
        for w in site.warnings:
            print('warning:', w)
        print(f'built {out} ({sum(1 for p in out.rglob("*") if p.is_file())} files)')
    return site


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path, default=DEFAULT_OUT)
    build(ap.parse_args().out.resolve())
