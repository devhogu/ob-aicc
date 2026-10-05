# START_MODULE_CONTRACT
#   PURPOSE: Render the common presentation and navigation of independent portal sections.
#   SCOPE: Shared header, section navigation, local assets and relative links; no content relationships.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   ROOT - repository root for shared assets
#   SECTIONS - bilingual section identities and route prefixes
#   relative - resolve a site target relative to a page
#   messages - load cached language-specific UI strings
#   icon - load a local presentation icon
#   section_label - select a section's language label
#   asset - resolve a versioned presentation asset
#   header - render branding, scoped search, language and theme controls
#   navigation - render global groups and the active section's local navigation
#   styles - load the shared visual shell
#   script - bind interactions to the section's search index
#   page - render an independent section page without charter metadata
# END_MODULE_MAP
"""The common roof. Section renderers own their bodies, search and metadata."""
from functools import lru_cache
from html import escape
import hashlib
import json
from pathlib import Path
import posixpath

ROOT = Path(__file__).resolve().parents[2]
SECTIONS = json.loads((ROOT / 'portal/sections/navigation.json').read_text())


def relative(url, target):
    result = posixpath.relpath(target, url)
    return result + '/' if target.endswith('/') and not result.endswith('/') else result


@lru_cache(maxsize=None)
def messages(lang):
    return json.loads((ROOT / f'portal/messages/{lang}.json').read_text())


@lru_cache(maxsize=None)
def icon(name):
    source = (ROOT / f'portal/ui-comps/icons/ui-{name}.svg').read_text()
    return source.replace('<svg ', '<svg class="o-icon" aria-hidden="true" ', 1)


def section_label(section, lang):
    return next(s['label'][lang] for s in SECTIONS if s['id'] == section)


def asset(url, name):
    path = ROOT / 'portal/site' / name
    version = hashlib.sha256(path.read_bytes()).hexdigest()[:8]
    return relative(url, '/assets/' + name) + '?v=' + version


def header(url, lang, section, m=None):
    m = m or messages(lang)
    label = section_label(section, lang)
    search = m['search_label'] if section == 'aicc' else ({'en': 'Search this section', 'ru': 'Поиск в разделе'}[lang])
    switches = []
    for language in ('en', 'ru'):
        target = url.replace('/' + lang + '/', '/' + language + '/', 1)
        current = ' aria-current="true"' if language == lang else ''
        switches.append(f'<a lang="{language}" hreflang="{language}" href="{escape(relative(url, target))}"{current}>{language.upper()}</a>')
    scope = m['header_scope'] if section == 'aicc' else label
    return f'''<header class="o-header">
  <a class="o-identity" href="{relative(url, '/' + lang + '/')}"><img src="{relative(url, '/assets/ui/assets/logos/o-mark.svg')}" width="34" height="38" alt=""><span>{escape(m['site_name'])}</span></a>
  <span class="header-scope">{escape(scope)}</span>
  <div class="o-search" role="search"><label class="o-sr-only" for="q">{escape(search)}</label><input id="q" type="search" autocomplete="off" placeholder="{escape(search)}" aria-controls="results"><div id="results" class="o-search-results" hidden></div></div>
  <div class="o-tools"><nav class="lang-switch" aria-label="{escape(m['language_label'])}">{''.join(switches)}</nav><button id="theme-switch" type="button" class="theme-switch" aria-label="{escape(m['theme_to_dark'])}" title="{escape(m['theme_to_dark'])}"><span class="ts-moon">{icon('moon')}</span><span class="ts-sun">{icon('sun')}</span></button></div>
</header>'''


def navigation(url, lang, active, local_nav, tail='', m=None):
    m = m or messages(lang)
    groups = []
    for section in SECTIONS:
        selected = section['id'] == active
        current = ' aria-current="true"' if selected else ''
        children = f'<div class="portal-local-nav">{local_nav}</div>' if selected else ''
        target = '/' + lang + '/' + section['path']
        groups.append(f'''<div class="portal-nav-group{' is-current' if selected else ''}">
<a class="portal-section-link" data-section="{section['id']}" href="{relative(url, target)}"{current}>{icon(section['icon'])}<span>{escape(section['label'][lang])}</span></a>{children}</div>''')
    return f'''<aside class="o-nav"><details open><summary>{escape(m['nav_summary'])}</summary><nav class="portal-sections" aria-label="{escape(m['nav_label'])}">{''.join(groups)}</nav></details>{tail}</aside>'''


def styles(url):
    ui = ''.join(f'<link rel="stylesheet" href="{relative(url, "/assets/ui/" + name)}">\n' for name in ('fonts.css', 'tokens.css', 'primitives.css', 'workspace.css'))
    return ui + ''.join(f'<link rel="stylesheet" href="{asset(url, name)}">\n' for name in ('charter.css', 'neighbours.css'))


def script(url, lang, section):
    m = messages(lang)
    index = f'/assets/search-{section}-{lang}.json'
    return f'''<script src="{asset(url, 'site.js')}" defer data-search="{relative(url, index)}" data-t-none="{escape(m['search_none'])}" data-t-light="{escape(m['theme_to_light'])}" data-t-dark="{escape(m['theme_to_dark'])}" data-t-dz-close="{escape(m['dz_close'])}"></script>'''


def page(url, lang, section, title, body, local_nav, *, extra_head='', body_class=''):
    m = messages(lang)
    other = 'ru' if lang == 'en' else 'en'
    return f'''<!doctype html>
<html lang="{lang}" data-theme="light"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark">
<title>{escape(title)} · {escape(section_label(section, lang))}</title>
<script>try{{var t=localStorage.getItem('aicc-theme');document.documentElement.dataset.theme=t==='dark'?'dark':'light';}}catch(e){{}}</script>
{extra_head}
{styles(url)}
<link rel="alternate" hreflang="{other}" href="{relative(url, url.replace('/' + lang + '/', '/' + other + '/', 1))}">
{script(url, lang, section)}
</head><body class="portal-workspace {escape(body_class)}" data-portal-section="{section}">
<a class="o-skip" href="#main">{escape(m['skip'])}</a>
{header(url, lang, section)}
<div class="o-frame">{navigation(url, lang, section, local_nav)}
<main class="o-main neighbour-main" id="main" tabindex="-1">{body}
<footer class="o-footer">{escape(section_label(section, lang))} · O!Bank</footer></main></div>
</body></html>'''
