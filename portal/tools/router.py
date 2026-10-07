# START_MODULE_CONTRACT
#   PURPOSE: Render the language routers that lead to the five branches, and the site's one 404 page.
#   SCOPE: One door per branch with its navigation icon, purpose and one fact counted from the branch's own sources at build time.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   PURPOSE - the one-line purpose of each branch, per language
#   FACTS - the wording of each branch's live fact, per language
#   TITLE - the accessible name of the list of doors
#   facts - count each branch's fact from its sources and builders
#   number - group the digits of a count for the language
#   door - render one branch door
#   router_page - render the router of one language on the shared shell
#   not_found - render the self-contained bilingual 404 page
#   build - write both routers and the 404 page
# END_MODULE_MAP
"""The router at /{lang}/: the five branches and nothing else."""
from html import escape
from pathlib import Path

import workspace

PURPOSE = {
    'center': {'en': 'The charter, operating models, knowledge base and templates of the AI Competence Center.',
               'ru': 'Устав, операционные модели, база знаний и шаблоны Центра компетенций по AI.'},
    'discovery': {'en': 'Scenarios in which AI can help the Bank, by area and capability.',
                  'ru': 'Сценарии применения AI в Банке по направлениям и областям.'},
    'portfolio': {'en': 'The Initiatives of AICC on the Portfolio Kanban, from the Funnel to Done.',
                  'ru': 'Инициативы AICC на канбане портфеля — от воронки до завершения.'},
    'program': {'en': 'Delivery: the Program Kanban and the documents of each project.',
                'ru': 'Реализация: канбан программы и документы каждого проекта.'},
    'lab': {'en': 'The on-premises AI Lab: how an Experiment runs and how it is controlled.',
            'ru': 'AI Lab в контуре Банка: как проводится эксперимент и как он контролируется.'},
}
# English wording takes (singular, plural); Russian wording puts the count after a label.
FACTS = {
    'center': {'en': ('document and template', 'documents and templates'), 'ru': 'Документов и шаблонов'},
    'discovery': {'en': ('scenario', 'scenarios'), 'ru': 'Сценариев'},
    'portfolio': {'en': ('initiative', 'initiatives'), 'ru': 'Инициатив'},
    'program': {'en': ('project', 'projects'), 'ru': 'Проектов'},
    'lab': {'en': ('workflow task', 'workflow tasks'), 'ru': 'Задач процесса'},
}
TITLE = {'en': 'Sections of AICC', 'ru': 'Разделы AICC'}


def facts(lang):
    """Each branch's fact, counted from the same sources and builders that publish the branch."""
    import discovery
    import lab
    import portfolio
    corpus = [path for path in (workspace.ROOT / 'charter/en').rglob('*.md') if path.name != 'README.md']
    area_pages = [page for page in discovery.pages(lang) if len(page.parts) == 2 and page.name == 'index.html']
    data = portfolio.project(lang=lang)
    model = lab.source_content()
    return {
        'center': len(corpus),
        'discovery': sum(discovery.scenario_count(lang, page) for page in area_pages),
        'portfolio': sum(1 for item in data['items'] if not item['standing']),
        'program': len({item['project_key'] for item in data['items'] if item.get('project_key')}),
        'lab': sum(len(cell['tasks']) for cell in model['cells']),
    }


def number(value, lang):
    return f'{value:,}'.replace(',', ',' if lang == 'en' else ' ')


def door(url, lang, section, count):
    wording = FACTS[section['id']][lang]
    if lang == 'en':
        fact = f'{number(count, lang)} {wording[0] if count == 1 else wording[1]}'
    else:
        fact = f'{wording}: {number(count, lang)}'
    href = workspace.relative(url, workspace.route(lang, section['id']))
    return (f'<li><a class="router-door" data-door="{section["id"]}" href="{href}">{workspace.icon(section["icon"])}'
            f'<h2>{escape(section["label"][lang])}</h2><p>{escape(PURPOSE[section["id"]][lang])}</p>'
            f'<span class="router-fact">{escape(fact)}</span></a></li>')


def router_page(lang):
    url = workspace.route(lang, workspace.ROUTER)
    counts = facts(lang)
    doors = ''.join(door(url, lang, section, counts[section['id']]) for section in workspace.SECTIONS)
    body = (f'<article class="router"><h1 class="o-sr-only">{escape(workspace.messages(lang)["site_name"])}</h1>'
            f'<ul class="router-doors" aria-label="{escape(TITLE[lang])}">{doors}</ul></article>')
    return url, workspace.page(url, lang, workspace.ROUTER, workspace.messages(lang)['site_name'], body, '', body_class='router-workspace')


def not_found():
    """Served for any missing path at any depth, so it carries its own styles and links from the site root."""
    return '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark"><meta name="robots" content="noindex">
<title>Page not found · Страница не найдена · AICC</title>
<style>
:root{--brand:#F0047F;--canvas:#F4F4F6;--surface:#FFFFFF;--text:#202025;--muted:#625D67;--link:#B80061;--border:#DCD6DE}
@media(prefers-color-scheme:dark){:root{--canvas:#101012;--surface:#18181B;--text:#F5F5F7;--muted:#B9B3BC;--link:#FF85C1;--border:#464149}}
*{box-sizing:border-box}body{margin:0;min-height:100vh;background:var(--canvas);color:var(--text);font:400 16px/1.5 "Golos Text",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
header{padding:14px 22px;background:linear-gradient(100deg,#460020,#111014 65%);color:#fff;border-bottom:2px solid var(--brand);font-weight:600}
main{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;max-width:880px;margin:48px auto;padding:0 16px}
section{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:28px}
h1{font-size:28px;line-height:1.22;margin:0 0 12px}p{color:var(--muted);margin:0 0 18px}a{color:var(--link);font-weight:500;text-underline-offset:3px}
a:focus-visible{outline:3px solid var(--brand);outline-offset:3px}
</style></head>
<body><header>AI Competence Center · Центр компетенций по AI</header>
<main id="main">
<section lang="en"><h1>Page not found</h1><p>The address does not lead to a page of this site. The site was reorganized into five sections; start again from the section list.</p><a href="/aicc/en/" hreflang="en">Go to the sections of AICC</a></section>
<section lang="ru"><h2 style="font-size:28px;line-height:1.22;margin:0 0 12px">Страница не найдена</h2><p>По этому адресу на сайте нет страницы. Сайт разделён на пять разделов; начните с их списка.</p><a href="/aicc/ru/" hreflang="ru">Перейти к разделам AICC</a></section>
</main>
<script>/* the site may also be served from the domain root */ if (location.pathname.indexOf('/aicc/') !== 0) document.querySelectorAll('a[href^="/aicc/"]').forEach(function (a) { a.setAttribute('href', a.getAttribute('href').slice(5)); });</script>
</body></html>
'''


def build(output):
    output = Path(output)
    for lang in ('en', 'ru'):
        url, page = router_page(lang)
        target = output / url.lstrip('/') / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page)
    (output / '404.html').write_text(not_found())
    return 2
