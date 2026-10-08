# START_MODULE_CONTRACT
#   PURPOSE: The reference and the knowledge base: regulators and acts, open resources, and the list of guides, each as a searchable, filterable card grid.
#   SCOPE: Reads aicc/v2/reference/*.yaml and the guide pages under content/ru/kb/guides; adds generated pages and decorates guide pages. No network.
#   DEPENDS: M-HUB-V2-BUILD
#   LINKS: C-HUB-V2
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   add_pages - add the regulation, resources and knowledge base pages; give each guide its header
# END_MODULE_MAP
"""Reference and knowledge base pages built from data."""
from html import escape
from pathlib import Path

import yaml

SRC = Path(__file__).resolve().parents[1]
WEIGHT = {'applies': ('действует для нас', 'is-applies'), 'partners': ('касается партнёров', 'is-partners'), 'benchmark': ('ориентир', 'is-benchmark')}
LEVEL = {'start': 'с нуля', 'basic': 'базовый', 'advanced': 'продвинутый'}


def load(name):
    return yaml.safe_load((SRC / 'reference' / f'{name}.yaml').read_text(encoding='utf-8')) or []


def finder(groups, count, placeholder):
    chips = '<button type="button" class="lib-chip" data-lib-group="" aria-pressed="true">Все</button>' + ''.join(
        f'<button type="button" class="lib-chip" data-lib-group="{escape(g)}" aria-pressed="false">{escape(g)}</button>' for g in groups)
    return (f'<div class="lib-find"><input type="search" data-lib-search placeholder="{escape(placeholder)}" aria-label="Поиск">'
            f'<output data-lib-count aria-live="polite">Показано: {count}</output></div><div class="lib-chips" role="group" aria-label="Разделы">{chips}</div>')


def grid(items, groups, card):
    """Cards grouped under headings; every card carries what the search and the chips need."""
    out = []
    for g in groups:
        members = [x for x in items if x['group'] == g]
        out.append(f'<section class="lib-group" data-lib-section="{escape(g)}"><h2>{escape(g)}</h2><div class="lib-grid">{"".join(card(x) for x in members)}</div></section>')
    return ''.join(out)


def find_text(*parts):
    return escape(' '.join(p for p in parts if p).lower())


# START_CONTRACT: add_pages
#   PURPOSE: Add the reference pages built from data and the knowledge base index; put a header with category, level and time on every guide.
#   INPUTS: { pages: dict; site: dict; api: module - build helpers (Page, rel, url_of) }
#   OUTPUTS: { None }
#   SIDE_EFFECTS: Adds pages and edits guide page bodies in place.
# END_CONTRACT: add_pages
def add_pages(pages, site, api):
    Page, rel, url_of = api.Page, api.rel, api.url_of
    e = escape

    # regulators and acts
    acts = load('acts')
    groups = list(dict.fromkeys(a['group'] for a in acts))

    def act(a):
        label, cls = WEIGHT[a['weight']]
        return (f'<article class="lib-card" data-lib-item data-group="{e(a["group"])}" data-find="{find_text(a["title"], a["kind"], a["what"], a["for_us"], a["group"])}">'
                f'<div class="lib-card__top"><small>{e(a["kind"])}</small><span class="lib-tag {cls}">{e(label)}</span></div>'
                f'<h3>{e(a["title"])}</h3><p>{e(a["what"])}</p><p class="lib-for"><b>Для нас.</b> {e(a["for_us"])}</p></article>')
    body = ('<p class="lede">Кто и что регулирует AI и данные — у нас, в регионе и в мире. Коротко: что это за документ и что он значит для нас. '
            'Это ориентир для разговора, а не юридическое заключение; за точным текстом обращайтесь к первоисточнику и юристам.</p>'
            '<p class="lib-legend"><span class="lib-tag is-applies">действует для нас</span> требования, которые применяются напрямую · '
            '<span class="lib-tag is-partners">касается партнёров</span> важно при выборе поставщиков и партнёров · '
            '<span class="lib-tag is-benchmark">ориентир</span> куда движутся регулирование и практика</p>'
            f'<div class="lib" data-lib>{finder(groups, len(acts), "Найти: закон, регулятор, тема")}{grid(acts, groups, act)}</div>')
    pages['reference/regulation'] = Page('reference/regulation', 'Регуляторы и нормативные акты', 'reference', 10,
                                         'Кто регулирует AI и данные у нас, в регионе и в мире, и что это значит для нас.', body)

    # open resources
    res = load('resources')
    rgroups = list(dict.fromkeys(r['group'] for r in res))

    def resource(r):
        return (f'<article class="lib-card" data-lib-item data-group="{e(r["group"])}" data-find="{find_text(r["title"], r["what"], r["for_us"], r["group"])}">'
                f'<div class="lib-card__top"><small>{e(r["group"])}</small></div><h3>{e(r["title"])}</h3><p>{e(r["what"])}</p>'
                f'<p class="lib-for"><b>Зачем.</b> {e(r["for_us"])}</p></article>')
    body = ('<p class="lede">Открытые источники, которые стоит знать: где учиться, где следить за отраслью, что читают регуляторы финансового сектора '
            'и где искать сведения об атаках и инцидентах. Внешние сервисы — только для чтения: рабочие данные туда не отправляем.</p>'
            f'<div class="lib" data-lib>{finder(rgroups, len(res), "Найти: курс, доклад, тема")}{grid(res, rgroups, resource)}</div>')
    pages['reference/resources'] = Page('reference/resources', 'Ресурсы для обучения и исследований', 'reference', 20,
                                        'Где учиться, где следить за отраслью и где искать сведения об атаках и инцидентах.', body)

    # the knowledge base: guides by category
    guides = sorted((p for pid, p in pages.items() if pid.startswith('kb/guides/')), key=lambda p: (p.order, p.title.casefold()))
    cats = list(dict.fromkeys(p.meta.get('category', 'Разное') for p in guides))
    here = 'kb'

    def guide(p):
        m = p.meta
        level = LEVEL.get(m.get('level', ''), m.get('level', ''))
        return (f'<a class="lib-card lib-card--link" href="{e(rel(url_of(here), url_of(p.id)))}" data-lib-item data-group="{e(m.get("category", ""))}" '
                f'data-find="{find_text(p.title, p.summary, m.get("category"), m.get("tags", ""))}">'
                f'<div class="lib-card__top"><small>{e(m.get("category", ""))}</small><span class="lib-time">{e(m.get("minutes", ""))} мин · {e(level)}</span></div>'
                f'<h3>{e(p.title)}</h3><p>{e(p.summary)}</p></a>')
    body = ('<p class="lede">Руководства по работе с AI: как начать, как поставить задачу, как работать безопасно и как автоматизировать свою работу. '
            'Короткие и практичные; новые появляются по мере того, как мы осваиваем инструменты.</p>'
            '<p class="pf-tip">Пользуйтесь только теми инструментами и аккаунтами, которые одобрены в вашей организации. Если инструмента нет — '
            f'<a href="{e(rel(url_of(here), url_of("services/how-to-engage")))}">напишите нам</a>, разберёмся вместе.</p>'
            f'<div class="lib" data-lib>{finder(cats, len(guides), "Найти руководство")}'
            f'<div class="lib-grid">{"".join(guide(p) for p in guides)}</div></div>')
    pages[here] = Page(here, 'База знаний', 'kb', 0, 'Руководства по работе с AI по категориям, с поиском.', body)

    # every guide opens with its category, level and time, and leads back to the list
    for p in guides:
        m = p.meta
        level = LEVEL.get(m.get('level', ''), m.get('level', ''))
        p.body = (f'<p class="kb-head"><a href="{e(rel(url_of(p.id), url_of(here)))}">← Все руководства</a>'
                  f'<span>{e(m.get("category", ""))}</span><span>{e(level)}</span><span>{e(m.get("minutes", ""))} мин</span></p>\n\n' + p.body)
        p.nav = False
