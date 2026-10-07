# START_MODULE_CONTRACT
#   PURPOSE: Render the common presentation and navigation of independent portal sections.
#   SCOPE: Shared header, navigation, footer, page feedback, local assets and relative links; no content relationships.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   ROOT - repository root for shared assets
#   SECTIONS - bilingual branch identities and route prefixes
#   ROUTER - the language router that leads to the five branches
#   REFERENCE_PREFIX - former routes whose page references renamed branches keep
#   SEARCH_TEXT - search labels of a branch, the router and the global scope
#   route - the site-absolute route of a branch page
#   search_index - the search index of a branch
#   CONTACT - shared portal feedback contact
#   relative - resolve a site target relative to a page
#   messages - load cached language-specific UI strings
#   icon - load a local presentation icon
#   section_label - select a section's language label
#   asset - resolve a versioned presentation asset
#   header - render branding, branch or global search, language and theme controls
#   short_id - assign stable page references without changing existing AICC references
#   page_key - the stable reference key of a page, kept across route changes
#   legal_pages - shared language-specific legal destinations
#   navigation_footer - render legal links and the site version below navigation
#   navigation - render global groups and the active section's local navigation
#   footer - render the common site footer and page feedback trigger
#   feedback_dialog - render the shared page feedback dialog
#   styles - load the shared visual shell
#   script - bind interactions to the branch search index and to every branch index for global search
#   page - render an independent branch page (or the router) without charter metadata
# END_MODULE_MAP
"""The common roof. Section renderers own their bodies, search and metadata."""
from functools import lru_cache
from html import escape
import hashlib
import json
from pathlib import Path
import posixpath
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
SECTIONS = json.loads((ROOT / 'portal/sections/navigation.json').read_text())
# The language router at /{lang}/ belongs to no branch; it carries the shared shell and global search.
ROUTER = 'router'
# Feedback references are quoted by readers. Branch routes renamed by the bounded-branch layout keep the
# reference of their former route, so a quoted ID still names the same page.
REFERENCE_PREFIX = {'portfolio/': 'initiatives/', 'program/': 'projects/'}
SEARCH_TEXT = {
    'branch': {'en': 'Search this section', 'ru': 'Поиск в разделе'},
    'router': {'en': 'Search the Competence Center', 'ru': 'Поиск по сайту Центра Компетенций'},
    'all': {'en': 'All sections', 'ru': 'Все разделы'},
}
CONTACT = {'name': 'Timur Alimbayev', 'email': 'talimbayev@obank.kg'}


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
    if section == ROUTER:
        return messages(lang)['site_short']
    return next(s['label'][lang] for s in SECTIONS if s['id'] == section)


def route(lang, section, rest=''):
    """The site-absolute route of a page of a branch, e.g. route('en', 'program', 'items/x/')."""
    if section == ROUTER:
        return f'/{lang}/' + rest
    return f'/{lang}/' + next(s['path'] for s in SECTIONS if s['id'] == section) + rest


def search_index(lang, section):
    return f'/assets/search-{section}-{lang}.json'


def asset(url, name):
    path = ROOT / 'portal/site' / name
    version = hashlib.sha256(path.read_bytes()).hexdigest()[:8]
    return relative(url, '/assets/' + name) + '?v=' + version


def header(url, lang, section, m=None):
    m = m or messages(lang)
    label = section_label(section, lang)
    search = m['search_label'] if section == 'center' else SEARCH_TEXT['router' if section == ROUTER else 'branch'][lang]
    switches = []
    for language in ('en', 'ru'):
        target = url.replace('/' + lang + '/', '/' + language + '/', 1)
        current = ' aria-current="true"' if language == lang else ''
        switches.append(f'<a lang="{language}" hreflang="{language}" href="{escape(relative(url, target))}"{current}>{language.upper()}</a>')
    scope = m['header_scope'] if section == 'center' else label
    scope = '' if section == ROUTER else f'<span class="header-scope">{escape(scope)}</span>'
    # Global search is a scope of the same box; it is on by default on the router.
    checked = ' checked' if section == ROUTER else ''
    every = f'<label class="search-scope"><input id="q-all" type="checkbox"{checked}><span>{escape(SEARCH_TEXT["all"][lang])}</span></label>'
    return f'''<header class="o-header">
  <a class="o-identity" href="{relative(url, '/' + lang + '/')}"><img src="{relative(url, '/assets/ui/assets/logos/o-mark.svg')}" width="34" height="38" alt=""><span>{escape(m['site_name'])}</span></a>
  {scope}
  <div class="o-search" role="search"><label class="o-sr-only" for="q">{escape(search)}</label><input id="q" type="search" autocomplete="off" placeholder="{escape(search)}" aria-controls="results">{every}<div id="results" class="o-search-results" hidden></div></div>
  <div class="o-tools"><nav class="lang-switch" aria-label="{escape(m['language_label'])}">{''.join(switches)}</nav><button id="theme-switch" type="button" class="theme-switch" aria-label="{escape(m['theme_to_dark'])}" title="{escape(m['theme_to_dark'])}"><span class="ts-moon">{icon('moon')}</span><span class="ts-sun">{icon('sun')}</span></button></div>
</header>'''


def short_id(key, taken=None, length=5):
    """Hash a stable page key using the established AICC reference alphabet."""
    taken = set() if taken is None else taken
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


def page_key(url):
    """The reference key of a branch page: its route below the language, under its former route where renamed."""
    path = url.split('/', 2)[2]
    for new, old in REFERENCE_PREFIX.items():
        if path.startswith(new):
            path = old + path[len(new):]
    return path.rstrip('/') + '/index'


def legal_pages(lang, m=None):
    m = m or messages(lang)
    return [(route(lang, 'center', 'privacy/'), m['privacy']), (route(lang, 'center', 'terms-of-use/'), m['terms_of_use'])]


def navigation_footer(url, lang, m=None):
    m = m or messages(lang)
    links = ''.join(f'<a href="{relative(url, target)}"' + (' aria-current="page"' if target == url else '') + f'>{escape(label)}</a>' for target, label in legal_pages(lang, m))
    return f'<div class="nav-foot"><div class="nav-legal">{links}</div><p class="o-caption">{escape(m["baseline"])}</p></div>'


def navigation(url, lang, active, local_nav, m=None):
    m = m or messages(lang)
    groups = []
    for section in SECTIONS:
        selected = section['id'] == active
        current = ' aria-current="true"' if selected else ''
        children = f'<div class="portal-local-nav">{local_nav}</div>' if selected else ''
        target = '/' + lang + '/' + section['path']
        groups.append(f'''<div class="portal-nav-group{' is-current' if selected else ''}">
<a class="portal-section-link" data-section="{section['id']}" href="{relative(url, target)}"{current}>{icon(section['icon'])}<span>{escape(section['label'][lang])}</span></a>{children}</div>''')
    return f'''<aside class="o-nav"><details open><summary>{escape(m['nav_summary'])}</summary><nav class="portal-sections" aria-label="{escape(m['nav_label'])}">{''.join(groups)}</nav></details>{navigation_footer(url, lang, m)}</aside>'''


def footer(url, lang, ref, m=None):
    m = m or messages(lang)
    subject = m['fb_subject'].replace('{ref}', ref)
    links = ''.join(f' <a class="contact" href="{relative(url, target)}">{escape(label)}</a>' for target, label in legal_pages(lang, m))
    return f'''<footer class="o-footer">
      <span class="foot-text">{escape(m['footer'])} <a class="contact" href="mailto:{CONTACT['email']}?subject={quote(subject)}">{escape(m['contact_us'])}</a>{links}</span>
      <button type="button" class="pagefb" data-dialog="fb" aria-haspopup="dialog"><span>{escape(m['pagefb'])}</span><span>ID: {escape(ref)}</span></button>
    </footer>'''


def feedback_dialog(lang, title, ref, m=None):
    m = m or messages(lang)
    subject = m['fb_subject'].replace('{ref}', ref)
    return f'''<dialog id="fb" class="fb" aria-labelledby="fb-t" data-subject="{escape(subject)}" data-ref="{escape(ref)}" data-page="{escape(title)}">
  <form method="dialog">
    <div class="fb-head"><h2 id="fb-t">{escape(m['pagefb'])}</h2><code>ID: {escape(ref)}</code><button type="button" class="fb-copy" data-copy-text="{escape(ref)}">{escape(m['fb_copy'])}</button></div>
    <div class="fb-body"><p>{escape(m['fb_prov'])} <a data-mail href="mailto:{CONTACT['email']}">{escape(m['fb_word'])}</a>.</p><button class="oc-button" value="close">{escape(m['fb_close'])}</button></div>
  </form>
</dialog>'''


def styles(url):
    ui = ''.join(f'<link rel="stylesheet" href="{relative(url, "/assets/ui/" + name)}">\n' for name in ('fonts.css', 'tokens.css', 'primitives.css', 'workspace.css'))
    return ui + ''.join(f'<link rel="stylesheet" href="{asset(url, name)}">\n' for name in ('charter.css', 'neighbours.css'))


def script(url, lang, section, m=None):
    m = m or messages(lang)
    # The router searches the whole site by default; its own index is the Center's.
    index = search_index(lang, 'center' if section == ROUTER else section)
    every = ' '.join(relative(url, search_index(lang, s['id'])) for s in SECTIONS)
    names = '|'.join(s['label'][lang] for s in SECTIONS)
    return f'''<script src="{asset(url, 'site.js')}" defer data-search="{relative(url, index)}" data-search-all="{escape(every)}" data-search-names="{escape(names)}" data-t-none="{escape(m['search_none'])}" data-t-light="{escape(m['theme_to_light'])}" data-t-dark="{escape(m['theme_to_dark'])}" data-t-copied="{escape(m['copied'])}" data-t-mail-body="{escape(m['fb_mail_body'])}" data-t-dz-close="{escape(m['dz_close'])}"></script>'''


def page(url, lang, section, title, body, local_nav, *, extra_head='', body_class=''):
    m = messages(lang)
    other = 'ru' if lang == 'en' else 'en'
    ref = short_id(page_key(url))
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
{footer(url, lang, ref, m)}</main></div>
{feedback_dialog(lang, title, ref, m)}
</body></html>'''
