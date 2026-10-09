# START_MODULE_CONTRACT
#   PURPOSE: The reference and the knowledge base: regulators and acts, open resources, and the list of guides, each as a searchable, filterable card grid.
#   SCOPE: Reads aicc/v2/reference/*.yaml and the guide pages under content/ru/kb/guides; adds generated pages and decorates guide pages. No network.
#   DEPENDS: M-PORTAL-SOURCE, i18n
#   LINKS: C-HUB-V2
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   add_pages - add the regulation, resources and knowledge base pages; give each guide its header
#   add_maps - add the learning roadmap and one page per learning map
# END_MODULE_MAP
"""Reference and knowledge base pages built from data."""
from html import escape
from pathlib import Path

import yaml

from i18n import T, loc

SRC = Path(__file__).resolve().parents[1]
WEIGHT = {'applies': ('действует для нас', 'is-applies'), 'partners': ('касается партнёров', 'is-partners'), 'benchmark': ('ориентир', 'is-benchmark')}
CATEGORY_ORDER = ['Начало работы', 'Безопасная работа', 'Запросы к Claude', 'Claude', 'Claude Cowork', 'Автоматизация',
                  'Claude Tag', 'Для руководителей', 'Claude Code', 'Обучение']
LEVEL = {'start': 'с нуля', 'basic': 'базовый', 'advanced': 'продвинутый', 'deep': 'полное руководство'}


def category(meta, default=''):
    """A guide's category in the edition: the page's own front matter, or the Russian name of a fixed category through the table."""
    name = meta.get('category', default)
    return T(name) if name in CATEGORY_ORDER or name == 'Разное' else name


def level_label(meta):
    level = meta.get('level', '')
    return T(LEVEL[level]) if level in LEVEL else level


def load(name):
    return yaml.safe_load((SRC / 'reference' / f'{name}.yaml').read_text(encoding='utf-8')) or []


def finder(groups, count, placeholder):
    chips = '<button type="button" class="lib-chip" data-lib-group="" aria-pressed="true">' + T('Все') + '</button>' + ''.join(
        f'<button type="button" class="lib-chip" data-lib-group="{escape(g)}" aria-pressed="false">{escape(g)}</button>' for g in groups)
    return (f'<div class="lib-find"><input type="search" data-lib-search placeholder="{escape(placeholder)}" aria-label="{escape(T('Поиск'))}">'
            f'<output data-lib-count aria-live="polite">{T('Показано: {count}', count=count)}</output></div><div class="lib-chips" role="group" aria-label="{escape(T('Разделы'))}">{chips}</div>')


def grid(items, groups, card):
    """Cards grouped under headings; every card carries what the search and the chips need."""
    out = []
    for g in groups:
        members = [x for x in items if loc(x, 'group') == g]
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
    groups = list(dict.fromkeys(loc(a, 'group') for a in acts))

    def act(a):
        label, cls = WEIGHT[a['weight']]
        label = T(label)
        title, kind, what, for_us, group = (loc(a, f) for f in ('title', 'kind', 'what', 'for_us', 'group'))
        return (f'<article class="lib-card" data-lib-item data-group="{e(group)}" data-find="{find_text(title, kind, what, for_us, group)}">'
                f'<div class="lib-card__top"><small>{e(kind)}</small><span class="lib-tag {cls}">{e(label)}</span></div>'
                f'<h3>{e(title)}</h3><p>{e(what)}</p><p class="lib-for"><b>{T('Для нас.')}</b> {e(for_us)}</p></article>')
    body = (f'<p class="lede">{T("Кто и что регулирует AI и данные — у нас, в регионе и в мире. Коротко: что это за документ и что он значит для нас. "
                                 "Это ориентир для разговора, а не юридическое заключение; за точным текстом обращайтесь к первоисточнику и юристам.")}</p>'
            f'<p class="lib-legend"><span class="lib-tag is-applies">{T("действует для нас")}</span> {T("требования, которые применяются напрямую")} · '
            f'<span class="lib-tag is-partners">{T("касается партнёров")}</span> {T("важно при выборе поставщиков и партнёров")} · '
            f'<span class="lib-tag is-benchmark">{T("ориентир")}</span> {T("куда движутся регулирование и практика")}</p>'
            f'<div class="lib" data-lib>{finder(groups, len(acts), T("Найти: закон, регулятор, тема"))}{grid(acts, groups, act)}</div>')
    pages['reference/regulation'] = Page('reference/regulation', T('Регуляторы и нормативные акты'), 'reference', 10,
                                         T('Кто регулирует AI и данные у нас, в регионе и в мире, и что это значит для нас.'), body)

    # open resources
    res = load('resources')
    rgroups = list(dict.fromkeys(loc(r, 'group') for r in res))

    def resource(r):
        title, what, for_us, group = (loc(r, f) for f in ('title', 'what', 'for_us', 'group'))
        return (f'<article class="lib-card" data-lib-item data-group="{e(group)}" data-find="{find_text(title, what, for_us, group)}">'
                f'<div class="lib-card__top"><small>{e(group)}</small></div><h3>{e(title)}</h3><p>{e(what)}</p>'
                f'<p class="lib-for"><b>{T("Зачем.")}</b> {e(for_us)}</p></article>')
    body = (f'<p class="lede">{T("Открытые источники, которые стоит знать: где учиться, где следить за отраслью, что читают регуляторы финансового сектора "
                                 "и где искать сведения об атаках и инцидентах. Внешние сервисы — только для чтения: рабочие данные туда не отправляем.")}</p>'
            f'<div class="lib" data-lib>{finder(rgroups, len(res), T("Найти: курс, доклад, тема"))}{grid(res, rgroups, resource)}</div>')
    pages['reference/resources'] = Page('reference/resources', T('Ресурсы для обучения и исследований'), 'reference', 20,
                                        T('Где учиться, где следить за отраслью и где искать сведения об атаках и инцидентах.'), body)

    # Anthropic's learning resources: every section and course, linked at its root
    links = load('anthropic')
    lgroups = list(dict.fromkeys(loc(x, 'group') for x in links))

    def outside(x):
        lang = f'<span class="lib-tag is-applies">{T("на русском")}</span>' if x['lang'] == 'ru' else '<span class="lib-tag is-benchmark">EN</span>'
        retold = [pages[f'kb/guides/{g}'] for g in x.get('ours', []) if f'kb/guides/{g}' in pages]
        mine = (f'<p class="lib-ours"><b>{T("Пересказ у нас:")}</b> ' + ', '.join(
            f'<a href="{e(rel(url_of("reference/anthropic"), url_of(g.id)))}">{e(g.title)}</a>' for g in retold) + '</p>') if retold else ''
        title, what, group = (loc(x, f) for f in ('title', 'what', 'group'))
        return (f'<article class="lib-card" data-lib-item data-group="{e(group)}" data-find="{find_text(title, what, group, x["lang"])}">'
                f'<div class="lib-card__top"><small>{e(group)}</small>{lang}</div>'
                f'<h3><a href="{e(x["url"])}" target="_blank" rel="noopener">{e(title)} ↗</a></h3><p>{e(what)}</p>{mine}</article>')
    body = (f'<p class="lede">{T("Всё обучение от Anthropic, создателя Claude, в одном месте: сначала официальные материалы на русском, "
                                 "затем учебный портал Claude Academy с бесплатными курсами и практические материалы на английском. Ссылки ведут на первоисточник.")}</p>'
            f'<p class="pf-tip">{T("Короткие пересказы самого полезного — на русском и с нашими примерами — в {link}.", link=f'<a href="{e(rel(url_of("reference/anthropic"), url_of("kb")))}">{T("Базе знаний")}</a>')}</p>'
            f'<div class="lib" data-lib>{finder(lgroups, len(links), T("Найти: курс, тема, продукт"))}{grid(links, lgroups, outside)}</div>')
    pages['reference/anthropic'] = Page('reference/anthropic', T('Обучение Anthropic'), 'reference', 25,
                                        T('Claude Academy и все её курсы, официальная документация на русском и практические материалы Anthropic.'), body)

    # the knowledge base: guides by category
    # categories in the order a newcomer needs them, the same as the learning roadmap; within one, the guide's order
    # the order holds the Russian names; a category is compared in the edition's words, so English front matter sorts the same
    rank = {T(c): n for n, c in enumerate(CATEGORY_ORDER)}
    guides = sorted((p for pid, p in pages.items() if pid.startswith('kb/guides/')),
                    key=lambda p: (rank.get(category(p.meta), len(rank)), p.order, p.title.casefold()))
    cats = list(dict.fromkeys(category(p.meta, 'Разное') for p in guides))
    here = 'kb'

    def guide(p):
        m = p.meta
        level = level_label(m)
        return (f'<a class="lib-card lib-card--link" href="{e(rel(url_of(here), url_of(p.id)))}" data-lib-item data-group="{e(category(m))}" '
                f'data-find="{find_text(p.title, p.summary, category(m), m.get("tags", ""))}">'
                f'<div class="lib-card__top"><small>{e(category(m))}</small><span class="lib-time">{T("{n} мин · {level}", n=e(m.get("minutes", "")), level=e(level))}</span></div>'
                f'<h3>{e(p.title)}</h3><p>{e(p.summary)}</p></a>')
    def maps_band():
        """The learning roadmap first: every stop as a small card with its progress."""
        mfile = SRC / 'learning' / 'maps.yaml'
        if not mfile.exists():
            return ''
        data = yaml.safe_load(mfile.read_text(encoding='utf-8'))
        order = data['roadmap']['core'] + [mid for b in data['roadmap']['branches'] for mid in b['maps']]
        names = {m['id']: m for m in data['maps']}
        cards = ''.join(
            f'<a class="kb-map" href="{e(rel(url_of(here), url_of(f"kb/maps/{mid}")))}"><small>{T("Остановка {n}", n=i + 1) if i < len(data["roadmap"]["core"]) else e(loc(names[mid], "for")).capitalize()}</small>'
            f'<b>{e(loc(names[mid], "title"))}</b>'
            f'<div class="lm-progress lm-progress--mini" data-map-progress="{e(mid)}" data-total="{sum(len(lv["steps"]) for lv in names[mid]["levels"])}"><span class="lm-bar"><i></i></span><b></b></div></a>'
            for i, mid in enumerate(order))
        drawn = roadmap_svg(data, names, lambda mid: rel(url_of(here), url_of(f"kb/maps/{mid}")), lambda mm: (sum(len(lv['steps']) for lv in mm['levels']), 0))
        return (f'<section class="kb-maps" aria-label="{e(T("Карты обучения"))}"><div class="kb-maps__head"><h2>{T("Карты обучения: от нуля до эксперта")}</h2>'
                f'<a href="{e(rel(url_of(here), url_of("kb/maps")))}">{T("Вся дорожная карта →")}</a></div>'
                f'<figure class="rm-figure rm-figure--compact">{drawn}</figure><div class="kb-maps__grid">{cards}</div></section>')

    def featured_band():
        """The deep guides, shown first: each is a course of several parts."""
        deep = [p for p in guides if str(p.meta.get('featured', '')).lower() in ('true', 'yes', '1')]
        if not deep:
            return ''
        cards = ''.join(
            f'<a class="kb-feature" href="{e(rel(url_of(here), url_of(p.id)))}"><small>{T("Полное руководство · {n} мин", n=e(p.meta.get("minutes", "")))}</small>'
            f'<h3>{e(p.title)}</h3><p>{e(p.summary)}</p><span>{T("Открыть →")}</span></a>' for p in deep)
        return f'<section class="kb-featured" aria-label="{e(T("Полные руководства"))}"><h2>{T("Полные руководства")}</h2><div class="kb-featured__grid">{cards}</div></section>'

    body = (f'<p class="lede">{T("Руководства по работе с AI и с Claude: как начать, как писать запросы, как работать безопасно и как автоматизировать свою работу. "
                                 "Короткие пересказы лучших материалов — курсов и документации Anthropic — на русском, с примерами из нашей работы.")}</p>'
            f'<p class="pf-tip">{T("Пользуйтесь только теми инструментами и аккаунтами, которые одобрены в вашей организации. Если инструмента нет — {link}, разберёмся вместе.", link=f'<a href="{e(rel(url_of(here), url_of("services/how-to-engage")))}">{T("напишите нам")}</a>')}</p>'
            + maps_band()
            + featured_band()
            + f'<div class="lib" data-lib>{finder(cats, len(guides), T("Найти руководство"))}'
            f'<div class="lib-grid">{"".join(guide(p) for p in guides)}</div></div>')
    pages[here] = Page(here, T('База знаний'), 'kb', 0, T('Руководства по работе с AI по категориям, с поиском.'), body)

    # every guide opens with its category, level and time, and leads back to the list
    for p in guides:
        m = p.meta
        level = level_label(m)
        p.body = (f'<p class="kb-head"><a href="{e(rel(url_of(p.id), url_of(here)))}">{T("← Все руководства")}</a>'
                  f'<span>{e(category(m))}</span><span>{e(level)}</span><span>{T("{n} мин", n=e(m.get("minutes", "")))}</span></p>\n\n' + p.body)
        if m.get('source_url'):  # a retelling of an outside guide names it and links to the original
            ru = '/ru/' in m['source_url'] or '/docs/ru' in m['source_url']
            p.body += ('\n\n<!--course-end-->' if p.layout == 'course' else '') + (f'\n\n<p class="kb-source">{T("По материалам:")} <a href="{e(m["source_url"])}">{e(m.get("source", m["source_url"]))}</a> — '
                       + (T('официальная документация Anthropic на русском. Здесь — короткая выжимка с нашими примерами.') + '</p>\n' if ru else
                          T('Anthropic, на английском. Здесь — короткий пересказ на русском с нашими примерами.') + '</p>\n'))
        p.nav = False


LEVEL_COLORS = ['#9aa3b2', '#5b6bd6', '#d6006f', '#7a3db8']
BRANCH_COLORS = ['#5b6bd6', '#0f7c80', '#d98a00']


def wrap(text, width):
    """Split a label into lines of about `width` characters for SVG text."""
    lines, line = [], ''
    for word in text.split():
        if line and len(line) + 1 + len(word) > width:
            lines.append(line)
            line = word
        else:
            line = f'{line} {word}'.strip()
    return lines + [line] if line else lines


def svg_text(x, y, text, width, cls, anchor='middle', up=False):
    lines = wrap(text, width)
    if up:
        y -= (len(lines) - 1) * 16
    spans = ''.join(f'<tspan x="{x}" dy="{0 if i == 0 else 16}">{escape(l)}</tspan>' for i, l in enumerate(lines))
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{spans}</text>'


# START_CONTRACT: roadmap_svg
#   PURPOSE: The roadmap as a metro line: a start, the core maps as stations in order, then a fork into one track per role, each ending at an expert flag.
#   INPUTS: { data: dict - maps.yaml; maps: dict - id -> map; link: callable(map_id) -> href; totals: callable(map) -> (steps, minutes) }
#   OUTPUTS: { str - inline SVG; progress rings are filled by site.js from the reader's ticks }
#   SIDE_EFFECTS: none
# END_CONTRACT: roadmap_svg
def roadmap_svg(data, maps, link, totals):
    core, branches = data['roadmap']['core'], data['roadmap']['branches']
    W = 1180
    spread = 140
    H = 210 + spread * max(1, len(branches) - 1)
    mid = H // 2
    x0, step = 60, 150
    xs = [x0 + 120 + i * step for i in range(len(core))]
    fork = xs[-1] + 110
    ys = [round(mid + (k - (len(branches) - 1) / 2) * spread) for k in range(len(branches))]
    out = [f'<svg class="rm-svg" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(T('Дорожная карта обучения'))}">',
           f'<path class="rm-track" stroke="#d6006f" d="M{x0},{mid} L{xs[0]},{mid}"/>']
    # the core line, one segment per stop: it turns green once the map behind it is done (site.js, data-seg)
    ends = xs[1:] + [fork]
    for map_id, a, b in zip(core, xs, ends):
        out.append(f'<path class="rm-track rm-seg" data-seg="{escape(map_id)}" data-total="{totals(maps[map_id])[0]}" stroke="#d6006f" d="M{a},{mid} L{b},{mid}"/>')
    for k, y in enumerate(ys):
        out.append(f'<path class="rm-track rm-track--branch rm-track--b{k}" stroke="{BRANCH_COLORS[k % len(BRANCH_COLORS)]}" d="M{fork},{mid} C{fork + 70},{mid} {fork + 50},{y} {fork + 120},{y} L{W - 70},{y}"/>')
    out.append(f'<g class="rm-start"><circle cx="{x0}" cy="{mid}" r="22"/><text x="{x0}" y="{mid + 4}" text-anchor="middle">{T('Старт')}</text></g>')
    for i, (map_id, x) in enumerate(zip(core, xs)):
        m = maps[map_id]
        count, minutes = totals(m)
        up = i % 2 == 0
        out.append(f'<a href="{escape(link(map_id))}" class="rm-node"><title>{T("{title} — {n} шагов", title=escape(loc(m, "title")), n=count)}</title>'
                   f'<circle class="rm-ring-bg" cx="{x}" cy="{mid}" r="34"/><circle class="rm-ring" data-ring="{escape(map_id)}" data-total="{count}" cx="{x}" cy="{mid}" r="34" transform="rotate(-90 {x} {mid})"/>'
                   f'<circle class="rm-station" cx="{x}" cy="{mid}" r="26"/><text class="rm-num" x="{x}" y="{mid + 6}" text-anchor="middle">{i + 1}</text>'
                   + svg_text(x, mid - 50 if up else mid + 60, loc(m, 'title'), 18, 'rm-label', up=up) + '</a>')
    out.append(f'<circle class="rm-forkdot" cx="{fork}" cy="{mid}" r="9"/>')
    for k, (b, y) in enumerate(zip(branches, ys)):
        for j, map_id in enumerate(b['maps']):
            m = maps[map_id]
            count, _ = totals(m)
            x = fork + 230 + j * 150
            out.append(f'<a href="{escape(link(map_id))}" class="rm-node rm-node--branch rm-node--b{k}"><title>{T("{title} — {n} шагов", title=escape(loc(m, "title")), n=count)}</title>'
                       f'<circle class="rm-ring-bg" cx="{x}" cy="{y}" r="30"/><circle class="rm-ring" data-ring="{escape(map_id)}" data-total="{count}" cx="{x}" cy="{y}" r="30" transform="rotate(-90 {x} {y})"/>'
                       f'<circle class="rm-station" cx="{x}" cy="{y}" r="22"/>'
                       + svg_text(x, y - 44, loc(b, 'title'), 20, 'rm-branch-title', up=True)
                       + svg_text(x, y + 52, loc(m, 'title'), 18, 'rm-label') + '</a>')
        gx = W - 70
        out.append(f'<g class="rm-goal"><path d="M{gx},{y + 4} l0,-30 l24,8 l-24,8"/><text x="{gx}" y="{y + 26}" text-anchor="middle">{T('Эксперт')}</text></g>')
    out.append('</svg>')
    return ''.join(out)


# START_CONTRACT: map_svg
#   PURPOSE: One map as a track: start, the steps of each level on a segment in the level's colour, a milestone flag at every checkpoint, an expert flag at the end.
#   INPUTS: { map_id: str; m: dict - the map; infos: list - per level, per step (title, kind 'guide'|'course', key) }
#   OUTPUTS: { str - inline SVG; site.js marks done steps and the next one }
#   SIDE_EFFECTS: none
# END_CONTRACT: map_svg
def map_svg(map_id, m, infos, levels):
    points = sum(len(lv) for lv in infos) + len(infos)
    W, y = 1120, 110
    x0, x1 = 60, W - 110
    gap = (x1 - x0) / (points + 1)
    out = [f'<svg class="lm-svg" viewBox="0 0 {W} 210" role="img" aria-label="{escape(T('Путь по карте'))}">']
    x = x0 + gap
    segs, nodes, n = [], [], 0
    for i, steps in enumerate(infos):
        start = x - gap
        for title, kind, key in steps:
            n += 1
            label = T('Шаг {n}. {title}', n=n, title=title)
            shape = (f'<rect class="lm-node-shape" x="{x - 13:.1f}" y="{y - 13}" width="26" height="26" rx="4" transform="rotate(45 {x:.1f} {y})"/>' if kind == 'course'
                     else f'<circle class="lm-node-shape" cx="{x:.1f}" cy="{y}" r="15"/>')
            nodes.append(f'<a href="#step-{n}" class="lm-node lm-node--l{i + 1}" data-node-step="{escape(map_id)}|{escape(key)}"><title>{escape(label)}</title>{shape}'
                         f'<text x="{x:.1f}" y="{y + 5}" text-anchor="middle">{n}</text></a>')
            x += gap
        segs.append(f'<path class="lm-seg" stroke="{LEVEL_COLORS[i]}" d="M{start:.1f},{y} L{x:.1f},{y}"/>')
        segs.append(svg_text(round((start + x) / 2), y - 46, T('Уровень {n} · {level}', n=i + 1, level=levels[i]), 26, f'lm-svg-level lm-svg-level--{i + 1}'))
        nodes.append(f'<a href="#level-{i + 1}" class="lm-flag"><title>{T("Контрольная точка уровня {n}: {checkpoint}", n=i + 1, checkpoint=escape(loc(m["levels"][i], "checkpoint")))}</title>'
                     f'<path d="M{x:.1f},{y + 22} L{x:.1f},{y - 30} l20,7 l-20,7" stroke="{LEVEL_COLORS[i]}" fill="{LEVEL_COLORS[i]}"/></a>')
        x += gap
    out.append(f'<path class="lm-seg lm-seg--start" d="M{x0},{y} L{x0 + gap:.1f},{y}"/>')
    out.extend(segs)
    out.append(f'<circle class="lm-start" cx="{x0}" cy="{y}" r="9"/><text class="lm-svg-small" x="{x0}" y="{y + 34}" text-anchor="middle">{T('старт')}</text>')
    out.extend(nodes)
    out.append(f'<g class="lm-goal"><circle cx="{x1 + 50}" cy="{y}" r="22"/><text x="{x1 + 50}" y="{y + 5}" text-anchor="middle">★</text>'
               f'<text class="lm-svg-small" x="{x1 + 50}" y="{y + 44}" text-anchor="middle">{T('эксперт')}</text></g>')
    out.append(f'<g class="lm-legend"><circle cx="70" cy="190" r="7"/><text x="84" y="194">{T('руководство Хаба')}</text>'
               f'<rect x="224" y="183" width="12" height="12" rx="2" transform="rotate(45 230 189)"/><text x="244" y="194">{T('курс или документация')}</text>'
               f'<path d="M420,196 L420,182 l12,4 l-12,4" stroke="#5b6bd6" fill="#5b6bd6"/><text x="440" y="194">{T('контрольная точка')}</text></g>')
    out.append('</svg>')
    return ''.join(out)


# START_CONTRACT: add_maps
#   PURPOSE: The learning roadmap and its maps: each map takes one area from zero to hero in four levels of steps (our guides or outside courses), with a checkpoint per level and progress kept in the reader's browser.
#   INPUTS: { pages: dict; api: module - build helpers (Page, rel, url_of) }
#   OUTPUTS: { None }
#   SIDE_EFFECTS: Adds pages kb/maps and kb/maps/<id>.
# END_CONTRACT: add_maps
def add_maps(pages, api):
    Page, rel, url_of = api.Page, api.rel, api.url_of
    e = escape
    data = yaml.safe_load((SRC / 'learning' / 'maps.yaml').read_text(encoding='utf-8'))
    maps = {m['id']: m for m in data['maps']}
    levels = loc(data, 'levels')

    def step_info(step, here):
        """Title, address, label, minutes and stable key of a step."""
        if step.get('guide'):
            page = pages[f'kb/guides/{step["guide"]}']
            anchor = step.get('anchor')
            href = rel(url_of(here), url_of(page.id)) + (f'#{anchor}' if anchor else '')
            minutes = int(step.get('minutes') or (10 if anchor else page.meta.get('minutes', 5)))
            label = T('часть руководства') if anchor else T('руководство')
            return loc(step, 'title') or page.title, href, label, minutes, f'{step["guide"]}#{anchor or ""}', False
        if step.get('page'):
            page = pages[step['page']]
            return loc(step, 'title') or page.title, rel(url_of(here), url_of(page.id)), T('раздел Хаба'), int(step.get('minutes', 20)), step['page'], False
        url = step['url']
        kind = T('курс') if '/courses/' in url else (T('практикум') if 'github.com' in url else T('документация'))
        label = T('{kind} на русском', kind=kind) if step.get('lang') == 'ru' else T('{kind}, EN', kind=kind)
        return loc(step, 'title'), step['url'], label, int(step.get('minutes', 30)), step['url'], True

    def totals(m, here):
        steps = [s for lv in m['levels'] for s in lv['steps']]
        minutes = sum(step_info(s, here)[3] for s in steps)
        return len(steps), minutes

    def hours(minutes):
        return T('около {n} ч', n=max(1, round(minutes / 60))) if minutes >= 90 else T('около {n} мин', n=minutes)

    def progress(map_id, total):
        return (f'<div class="lm-progress" data-map-progress="{e(map_id)}" data-total="{total}" aria-live="polite">'
                f'<span class="lm-bar"><i></i></span><b>{T('0 из {total}', total=total)}</b></div>')

    order = data['roadmap']['core'] + [mid for b in data['roadmap']['branches'] for mid in b['maps']]
    core = data['roadmap']['core']

    def place_of(map_id):
        """Where a map sits on the roadmap, in words."""
        if map_id in core:
            return T('Остановка {n} из {total}', n=core.index(map_id) + 1, total=len(core))
        return T('Специализация · {branch}', branch=next(loc(b, 'title') for b in data['roadmap']['branches'] if map_id in b['maps']).lower())

    def after(map_id, here):
        """Where the road goes after a map: the next stop, the choice of a specialisation, or back to the roadmap."""
        to = lambda pid: rel(url_of(here), url_of(pid))
        if map_id in core[:-1]:
            nxt = core[core.index(map_id) + 1]
            return to(f'kb/maps/{nxt}'), T('Следующая карта'), loc(maps[nxt], 'title'), nxt
        if map_id == core[-1]:
            return to('kb/maps'), T('Дальше по дорожной карте'), T('Выберите специализацию'), ''
        return to('kb/maps'), T('Маршрут пройден'), T('Вернуться к дорожной карте'), ''

    def before(map_id, here):
        to = lambda pid: rel(url_of(here), url_of(pid))
        if map_id in core[1:]:
            prv = core[core.index(map_id) - 1]
            return to(f'kb/maps/{prv}'), T('Предыдущая карта'), loc(maps[prv], 'title'), prv
        if map_id == core[0]:
            return to('kb/maps'), T('Дорожная карта'), T('Весь маршрут обучения'), ''
        return to(f'kb/maps/{core[-1]}'), T('Предыдущая карта'), loc(maps[core[-1]], 'title'), core[-1]

    def move(cls, href, small, title, map_id=''):
        mark = f' data-map="{e(map_id)}"' if map_id else ''
        return f'<a class="{cls}" href="{e(href)}"{mark}><small>{e(small)}</small><span>{e(title)}</span></a>'

    def map_moves(map_id, here, top):
        """The bar on a map page: back along the roadmap, where this map sits, onward; at the top also a button to the first step still to do."""
        prev, nxt = before(map_id, here), after(map_id, here)
        go = (f'<a class="lm-walk__go" data-walk-continue href="#step-1">{T("Начать с шага 1 →")}</a>' if top else '')
        here_mark = f' data-walk-here="{e(map_id)}"' if top else ''
        return (f'<nav class="lm-walk lm-walk--map{" lm-walk--top" if top else " lm-walk--bottom"}"{here_mark} aria-label="{e(T("Карта на дорожной карте"))}">'
                f'<div class="lm-walk__head"><a class="lm-walk__map" href="{e(rel(url_of(here), url_of("kb/maps")))}">{T("Дорожная карта")}</a>'
                f'<span class="lm-walk__pos">{e(place_of(map_id))}</span>{go}</div>'
                f'<div class="lm-walk__moves">{move("lm-walk__prev", prev[0], "← " + prev[1], prev[2], prev[3])}{move("lm-walk__next", nxt[0], nxt[1] + " →", nxt[2], nxt[3])}</div></nav>')

    for n, map_id in enumerate(order):
        m = maps[map_id]
        here = f'kb/maps/{map_id}'
        count, minutes = totals(m, here)
        infos = [[(lambda s: (s[0], 'course' if s[5] else 'guide', s[4]))(step_info(st, here)) for st in lv['steps']] for lv in m['levels']]
        out = [f'<p class="lede">{e(loc(m, "goal"))}</p>',
               f'<div class="lm-head"><span><b>{T("Для кого:")}</b> {e(loc(m, "for"))}</span><span><b>{T("Шагов:")}</b> {count} · {hours(minutes)}</span>{progress(map_id, count)}</div>',
               f'<figure class="lm-figure">{map_svg(map_id, m, infos, levels)}<figcaption>{T("Наведите на шаг — увидите, что это; нажмите — перейдёте к нему. Пройденные шаги отмечаются зелёным, следующий — пульсирует.")}</figcaption></figure>']
        number = 0
        for i, lv in enumerate(m['levels']):
            items = []
            for step in lv['steps']:
                number += 1
                title, href, label, mins, key, outside = step_info(step, here)
                link = (f'<a href="{e(href)}" target="_blank" rel="noopener">{e(title)} ↗</a>' if outside else f'<a href="{e(href)}" data-map="{e(map_id)}">{e(title)}</a>')
                practice = f'<p class="lm-practice"><b>{T("Попробуйте:")}</b> {e(loc(step, "practice"))}</p>' if step.get('practice') else ''
                items.append(f'<li class="lm-step" id="step-{number}" data-step="{e(map_id)}|{e(key)}"><span class="lm-num">{number}</span><button type="button" class="lm-check" data-step-toggle aria-pressed="false" title="{e(T("Отметить пройденным"))}"><span class="o-sr-only">{T("Отметить пройденным")}</span></button>'
                             f'<div class="lm-body"><div class="lm-title">{link}<span class="lm-tag">{T("{label} · {n} мин", label=e(label), n=mins)}</span></div>'
                             f'<p>{e(loc(step, "outcome"))}</p>{practice}</div></li>')
            out.append(f'<section class="lm-level lm-level--{i + 1}"><header><span class="lm-badge">{T("Уровень {n}", n=i + 1)}</span><h2 id="level-{i + 1}">{e(levels[i])}</h2></header>'
                       f'<ol class="lm-steps">{"".join(items)}</ol><p class="lm-checkpoint"><b>{T("Контрольная точка.")}</b> {e(loc(lv, "checkpoint"))}</p></section>')
        out.insert(1, map_moves(map_id, here, top=True))
        out.append(map_moves(map_id, here, top=False))
        page = Page(here, T('Карта обучения: {title}', title=loc(m, 'title')), 'kb', 10 + n, T('{title} — от новичка до эксперта: {goal}', title=loc(m, 'title'), goal=loc(m, 'goal')), ''.join(out))
        page.nav = False
        pages[here] = page

    walk_steps(pages, api, maps, levels, order, step_info, before, after, move)

    # the roadmap: the core stops in order, then the branches
    here = 'kb/maps'

    def stop(map_id, number):
        m = maps[map_id]
        count, minutes = totals(m, here)
        return (f'<a class="rm-card" href="{e(rel(url_of(here), url_of(f"kb/maps/{map_id}")))}"><small>{T("Остановка {n} · ", n=number) if number else ""}{e(loc(m, "for"))}</small>'
                f'<h3>{e(loc(m, "title"))}</h3><p>{e(loc(m, "goal"))}</p><span class="rm-meta">{T("4 уровня · {n} шагов · {time}", n=count, time=hours(minutes))}</span>{progress(map_id, count)}</a>')
    stops = ''.join(f'<li class="rm-stop"><span class="rm-dot">{i + 1}</span>{stop(mid, i + 1)}</li>' for i, mid in enumerate(data['roadmap']['core']))
    branches = ''.join(f'<div class="rm-branch"><h3>{e(loc(b, "title"))}</h3>{"".join(stop(mid, None) for mid in b["maps"])}</div>' for b in data['roadmap']['branches'])
    first = data['roadmap']['core'][0]
    start = (f'<nav class="lm-walk lm-walk--map lm-walk--top" aria-label="{e(T("Начало маршрута"))}"><div class="lm-walk__head">'
             f'<span class="lm-walk__pos">{T("{n} остановки для всех, затем специализация по роли", n=len(data["roadmap"]["core"]))}</span>'
             f'<a class="lm-walk__go" data-road-continue href="{e(rel(url_of(here), url_of(f"kb/maps/{first}")))}">{T("Начать: остановка 1 — {title} →", title=e(loc(maps[first], "title")))}</a></div></nav>')
    body = (f'<p class="lede">{e(loc(data["roadmap"], "lede"))}</p>' + start +
            f'<p class="pf-tip">{T("Отмечайте пройденные шаги на картах — прогресс сохраняется в вашем браузере и виден здесь.")} '
            f'<button type="button" class="lm-reset" data-learn-reset>{T("Сбросить прогресс")}</button></p>'
            f'<figure class="rm-figure">{roadmap_svg(data, maps, lambda mid: rel(url_of(here), url_of(f"kb/maps/{mid}")), lambda mm: totals(mm, here))}'
            f'<figcaption>{T("Начните со старта и двигайтесь по станциям. После четвёртой — выберите специализацию. Кольцо вокруг станции заполняется по мере прохождения карты.")}</figcaption></figure>'
            f'<h2 class="rm-h">{T("Остановки по порядку")}</h2><ol class="rm-line">{stops}</ol><div class="rm-fork"><span>{T("Специализации — по вашей роли")}</span></div><div class="rm-branches" id="rm-branches">{branches}</div>'
            f'<p>{T("Отдельные руководства и поиск по ним — в {link}.", link=f'<a href="{e(rel(url_of(here), url_of("kb")))}">{T("Базе знаний")}</a>')}</p>')
    page = Page(here, loc(data['roadmap'], 'title'), 'kb', 1, loc(data['roadmap'], 'lede'), body)
    page.nav_title = T('Карты обучения')
    pages[here] = page


def heading_spans(body):
    """Every Markdown heading outside code fences: (level, anchor, end of the heading line, start of the line)."""
    out, pos, fence = [], 0, False
    for line in body.splitlines(keepends=True):
        stripped = line.strip()
        if stripped.startswith('```'):
            fence = not fence
        elif not fence and stripped.startswith('#'):
            level = len(stripped) - len(stripped.lstrip('#'))
            anchor = stripped.rsplit('{#', 1)[1].rstrip('}').strip() if stripped.endswith('}') and '{#' in stripped else ''
            out.append((level, anchor, pos + len(line), pos))
        pos += len(line)
    return out


# START_CONTRACT: walk_steps
#   PURPOSE: Put a step bar at the top and bottom of every map step that lives on our site: the map, the step's place in it, a dot per step, and back/next along the map; the bottom bar also says what the step teaches and lets the reader tick it off.
#   INPUTS: { pages: dict; api: module; maps: dict; levels: list; order: list - maps in roadmap order; step_info, before, after, move: helpers from add_maps }
#   OUTPUTS: { None }
#   SIDE_EFFECTS: Edits the bodies of guide pages and of pages used as steps. A whole page gets bars under its header and at its end; a part of a page (anchor) at the top and bottom of that part. Where several maps share a spot, the first bar shows and site.js picks the reader's map.
# END_CONTRACT: walk_steps
def walk_steps(pages, api, maps, levels, order, step_info, before, after, move):
    rel, url_of = api.rel, api.url_of
    e = escape
    inserts = {}  # page id -> [(position, sequence, html)]
    seq = 0

    for map_id in order:
        m = maps[map_id]
        steps = [(i, st) for i, lv in enumerate(m['levels']) for st in lv['steps']]
        total = len(steps)
        map_page = f'kb/maps/{map_id}'

        def target(k, host):
            """Address, title and kind of step k as seen from the host page; an outside course is reached through its card on the map."""
            info = step_info(steps[k][1], host)
            if info[5]:
                return rel(url_of(host), url_of(map_page)) + f'#step-{k + 1}', info[0], T('{label} Anthropic', label=info[2])
            return info[1], info[0], info[2]

        for k, (lvl, st) in enumerate(steps):
            if not (st.get('guide') or st.get('page')):
                continue
            host = f'kb/guides/{st["guide"]}' if st.get('guide') else st['page']
            page = pages[host]
            key = step_info(st, host)[4]
            title = target(k, host)[1]
            dots = ''.join(
                f'<li{" class=\"lm-dot-gap\"" if j and steps[j][0] != steps[j - 1][0] else ""}><a class="lm-dot lm-dot--l{steps[j][0] + 1}{" is-here" if j == k else ""}" href="{e(target(j, host)[0])}" data-map="{e(map_id)}" '
                f'data-dot-step="{e(map_id)}|{e(step_info(steps[j][1], host)[4])}" title="{T("Шаг {n}. {title}", n=j + 1, title=e(target(j, host)[1]))}"'
                f'{" aria-current=\"step\"" if j == k else ""}>{j + 1}</a></li>' for j in range(total))
            to_map = rel(url_of(host), url_of(map_page))
            if k:
                href, ptitle, kind = target(k - 1, host)
                prev = move('lm-walk__prev', href, T('← Назад · шаг {n} · {kind}', n=k, kind=kind), ptitle, map_id)
            else:
                prev = move('lm-walk__prev', to_map, T('← К началу карты'), loc(m, 'title'), map_id)
            if k + 1 < total:
                href, ntitle, kind = target(k + 1, host)
                nxt = move('lm-walk__next', href, T('Далее · шаг {n} · {kind} →', n=k + 2, kind=kind), ntitle, map_id)
            else:
                href, small, ntitle, nid = after(map_id, host)
                nxt = move('lm-walk__next', href, T('Карта пройдена · {next} →', next=small), ntitle, nid)
            outcome = loc(st, 'outcome')
            head = (f'<div class="lm-walk__head"><a class="lm-walk__map" href="{e(to_map)}#step-{k + 1}" data-map="{e(map_id)}">{T("Карта обучения: {title}", title=f"<b>{e(loc(m, 'title'))}</b>")}</a>'
                    f'<span class="lm-walk__pos">{T("Шаг {n} из {total} · уровень {k}, {level}", n=f"<b>{k + 1}</b>", total=total, k=lvl + 1, level=e(levels[lvl].lower()))}</span></div>'
                    f'<ol class="lm-walk__dots" aria-label="{e(T("Шаги карты"))}">{dots}</ol>')
            practice = f'<p><b>{T("Попробуйте:")}</b> {e(loc(st, "practice"))}</p>' if st.get('practice') else ''
            done = (f'<div class="lm-walk__done" data-step="{e(map_id)}|{e(key)}"><div><p><b>{T("После этого шага вы сможете:")}</b> {e(outcome[:1].lower() + outcome[1:])}</p>{practice}</div>'
                    f'<button type="button" class="lm-walk__check" data-step-toggle aria-pressed="false"><span class="is-off">{T("Отметить шаг пройденным")}</span><span class="is-on">{T("Шаг пройден ✓")}</span></button></div>')
            label = f'aria-label="{T("Шаг {n} из {total} по карте «{title}»", n=k + 1, total=total, title=e(loc(m, "title")))}"'
            top = f'<nav class="lm-walk lm-walk--top lm-walk--l{lvl + 1}" data-walk="{e(map_id)}" {label}>{head}<div class="lm-walk__moves">{prev}{nxt}</div></nav>'
            bottom = f'<nav class="lm-walk lm-walk--bottom lm-walk--l{lvl + 1}" data-walk="{e(map_id)}" {label}>{head}{done}<div class="lm-walk__moves">{prev}{nxt}</div></nav>'

            body = page.body
            if page.layout == 'course' and '<!--course-end-->' not in body:
                body = page.body = body + '\n\n<!--course-end-->\n'
            mark = body.find('<!--course-end-->')
            source = body.find('<p class="kb-source">')
            limit = mark if mark >= 0 else (source if source >= 0 else len(body))  # the end of the reading
            end = mark + len('<!--course-end-->') if mark >= 0 else limit        # a whole-page bar: below the tabs
            anchor = st.get('anchor')
            if anchor:
                spans = heading_spans(body)
                found = [x for x in spans if x[1] == anchor]
                if not found:
                    raise SystemExit(f'map {map_id}: no heading {{#{anchor}}} in {host}')
                level, _, top_at, _ = found[0]
                bottom_at = min([x[3] for x in spans if x[3] > top_at and x[0] <= level] + [limit])
            else:
                top_at = body.find('\n\n') + 2 if body.startswith('<p class="kb-head">') else 0
                bottom_at = end
            for at, html in ((top_at, top), (bottom_at, bottom)):
                seq += 1
                inserts.setdefault(host, []).append((at, seq, html))

    for host, items in inserts.items():
        out, shown = pages[host].body, set()
        final = []
        for at, q, html in sorted(items):  # a second bar on the same spot waits for site.js to pick the reader's map
            final.append((at, html.replace('<nav ', '<nav hidden ', 1) if at in shown else html))
            shown.add(at)
        for at, html in reversed(final):
            out = out[:at] + '\n\n' + html + '\n\n' + out[at:]
        pages[host].body = out
