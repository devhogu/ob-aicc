# START_MODULE_CONTRACT
#   PURPOSE: Render the language routers that lead to the five branches.
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
#   build - write both routers
# END_MODULE_MAP
"""The router at /{lang}/: the five branches and nothing else."""
from html import escape
from pathlib import Path

import workspace

PURPOSE = {
    'center': {'en': 'The charter, operating models, knowledge base and templates of the AI Competence Center.',
               'ru': 'Устав, операционные модели, база знаний и шаблоны Центра Компетенций по AI.'},
    'discovery': {'en': 'Scenarios in which AI can help the Bank, by area and capability.',
                  'ru': 'Сценарии применения AI в Банке по направлениям и областям.'},
    'portfolio': {'en': 'The Initiatives of the Competence Center on the Portfolio Kanban, from the Funnel to Done.',
                  'ru': 'Инициативы Центра Компетенций на канбане портфеля — от воронки до завершения.'},
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
TITLE = {'en': 'Sections of the Competence Center', 'ru': 'Разделы Центра Компетенций'}


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


def build(output):
    output = Path(output)
    for lang in ('en', 'ru'):
        url, page = router_page(lang)
        target = output / url.lstrip('/') / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page)
    return 2
