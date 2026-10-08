# START_MODULE_CONTRACT
#   PURPOSE: The reference and the knowledge base: regulators and acts, open resources, and the list of guides, each as a searchable, filterable card grid.
#   SCOPE: Reads aicc/v2/reference/*.yaml and the guide pages under content/ru/kb/guides; adds generated pages and decorates guide pages. No network.
#   DEPENDS: M-HUB-V2-BUILD
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

SRC = Path(__file__).resolve().parents[1]
WEIGHT = {'applies': ('действует для нас', 'is-applies'), 'partners': ('касается партнёров', 'is-partners'), 'benchmark': ('ориентир', 'is-benchmark')}
LEVEL = {'start': 'с нуля', 'basic': 'базовый', 'advanced': 'продвинутый', 'deep': 'полное руководство'}


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

    # Anthropic's learning resources: every section and course, linked at its root
    links = load('anthropic')
    lgroups = list(dict.fromkeys(x['group'] for x in links))

    def outside(x):
        lang = '<span class="lib-tag is-applies">на русском</span>' if x['lang'] == 'ru' else '<span class="lib-tag is-benchmark">EN</span>'
        retold = [pages[f'kb/guides/{g}'] for g in x.get('ours', []) if f'kb/guides/{g}' in pages]
        mine = ('<p class="lib-ours"><b>Пересказ у нас:</b> ' + ', '.join(
            f'<a href="{e(rel(url_of("reference/anthropic"), url_of(g.id)))}">{e(g.title)}</a>' for g in retold) + '</p>') if retold else ''
        return (f'<article class="lib-card" data-lib-item data-group="{e(x["group"])}" data-find="{find_text(x["title"], x["what"], x["group"], x["lang"])}">'
                f'<div class="lib-card__top"><small>{e(x["group"])}</small>{lang}</div>'
                f'<h3><a href="{e(x["url"])}" target="_blank" rel="noopener">{e(x["title"])} ↗</a></h3><p>{e(x["what"])}</p>{mine}</article>')
    body = ('<p class="lede">Всё обучение от Anthropic, создателя Claude, в одном месте: сначала официальные материалы на русском, '
            'затем учебный портал Claude Academy с бесплатными курсами и практические материалы на английском. Ссылки ведут на первоисточник.</p>'
            f'<p class="pf-tip">Короткие пересказы самого полезного — на русском и с нашими примерами — в <a href="{e(rel(url_of("reference/anthropic"), url_of("kb")))}">Базе знаний</a>.</p>'
            f'<div class="lib" data-lib>{finder(lgroups, len(links), "Найти: курс, тема, продукт")}{grid(links, lgroups, outside)}</div>')
    pages['reference/anthropic'] = Page('reference/anthropic', 'Обучение Anthropic', 'reference', 25,
                                        'Claude Academy и все её курсы, официальная документация на русском и практические материалы Anthropic.', body)

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
    def maps_band():
        """The learning roadmap first: every stop as a small card with its progress."""
        mfile = SRC / 'learning' / 'maps.yaml'
        if not mfile.exists():
            return ''
        data = yaml.safe_load(mfile.read_text(encoding='utf-8'))
        order = data['roadmap']['core'] + [mid for b in data['roadmap']['branches'] for mid in b['maps']]
        names = {m['id']: m for m in data['maps']}
        cards = ''.join(
            f'<a class="kb-map" href="{e(rel(url_of(here), url_of(f"kb/maps/{mid}")))}"><small>{f"Остановка {i + 1}" if i < len(data["roadmap"]["core"]) else e(names[mid]["for"]).capitalize()}</small>'
            f'<b>{e(names[mid]["title"])}</b>'
            f'<div class="lm-progress lm-progress--mini" data-map-progress="{e(mid)}" data-total="{sum(len(lv["steps"]) for lv in names[mid]["levels"])}"><span class="lm-bar"><i></i></span><b></b></div></a>'
            for i, mid in enumerate(order))
        drawn = roadmap_svg(data, names, lambda mid: rel(url_of(here), url_of(f"kb/maps/{mid}")), lambda mm: (sum(len(lv['steps']) for lv in mm['levels']), 0))
        return (f'<section class="kb-maps" aria-label="Карты обучения"><div class="kb-maps__head"><h2>Карты обучения: от нуля до эксперта</h2>'
                f'<a href="{e(rel(url_of(here), url_of("kb/maps")))}">Вся дорожная карта →</a></div>'
                f'<figure class="rm-figure rm-figure--compact">{drawn}</figure><div class="kb-maps__grid">{cards}</div></section>')

    def featured_band():
        """The deep guides, shown first: each is a course of several parts."""
        deep = [p for p in guides if str(p.meta.get('featured', '')).lower() in ('true', 'yes', '1')]
        if not deep:
            return ''
        cards = ''.join(
            f'<a class="kb-feature" href="{e(rel(url_of(here), url_of(p.id)))}"><small>Полное руководство · {e(p.meta.get("minutes", ""))} мин</small>'
            f'<h3>{e(p.title)}</h3><p>{e(p.summary)}</p><span>Открыть →</span></a>' for p in deep)
        return f'<section class="kb-featured" aria-label="Полные руководства"><h2>Полные руководства</h2><div class="kb-featured__grid">{cards}</div></section>'

    body = ('<p class="lede">Руководства по работе с AI и с Claude: как начать, как писать запросы, как работать безопасно и как автоматизировать свою работу. '
            'Короткие пересказы лучших материалов — курсов и документации Anthropic — на русском, с примерами из нашей работы.</p>'
            '<p class="pf-tip">Пользуйтесь только теми инструментами и аккаунтами, которые одобрены в вашей организации. Если инструмента нет — '
            f'<a href="{e(rel(url_of(here), url_of("services/how-to-engage")))}">напишите нам</a>, разберёмся вместе.</p>'
            + maps_band()
            + featured_band()
            + f'<div class="lib" data-lib>{finder(cats, len(guides), "Найти руководство")}'
            f'<div class="lib-grid">{"".join(guide(p) for p in guides)}</div></div>')
    pages[here] = Page(here, 'База знаний', 'kb', 0, 'Руководства по работе с AI по категориям, с поиском.', body)

    # every guide opens with its category, level and time, and leads back to the list
    for p in guides:
        m = p.meta
        level = LEVEL.get(m.get('level', ''), m.get('level', ''))
        p.body = (f'<p class="kb-head"><a href="{e(rel(url_of(p.id), url_of(here)))}">← Все руководства</a>'
                  f'<span>{e(m.get("category", ""))}</span><span>{e(level)}</span><span>{e(m.get("minutes", ""))} мин</span></p>\n\n' + p.body)
        if m.get('source_url'):  # a retelling of an outside guide names it and links to the original
            ru = '/ru/' in m['source_url'] or '/docs/ru' in m['source_url']
            p.body += (f'\n\n<p class="kb-source">По материалам: <a href="{e(m["source_url"])}">{e(m.get("source", m["source_url"]))}</a> — '
                       + ('официальная документация Anthropic на русском. Здесь — короткая выжимка с нашими примерами.</p>\n' if ru else
                          'Anthropic, на английском. Здесь — короткий пересказ на русском с нашими примерами.</p>\n'))
        p.nav = False


LEVEL_COLORS = ['#9aa3b2', '#5b6bd6', '#d6006f', '#2e9e5b']


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
    out = [f'<svg class="rm-svg" viewBox="0 0 {W} {H}" role="img" aria-label="Дорожная карта обучения">',
           '<defs><linearGradient id="rm-grad" x1="0" x2="1"><stop offset="0" stop-color="#d6006f"/><stop offset="1" stop-color="#5b6bd6"/></linearGradient></defs>',
           f'<path class="rm-track" d="M{x0},{mid} L{fork},{mid}"/>']
    for k, y in enumerate(ys):
        out.append(f'<path class="rm-track rm-track--branch rm-track--b{k}" d="M{fork},{mid} C{fork + 70},{mid} {fork + 50},{y} {fork + 120},{y} L{W - 70},{y}"/>')
    out.append(f'<g class="rm-start"><circle cx="{x0}" cy="{mid}" r="22"/><text x="{x0}" y="{mid + 4}" text-anchor="middle">Старт</text></g>')
    for i, (map_id, x) in enumerate(zip(core, xs)):
        m = maps[map_id]
        count, minutes = totals(m)
        up = i % 2 == 0
        out.append(f'<a href="{escape(link(map_id))}" class="rm-node"><title>{escape(m["title"])} — {count} шагов</title>'
                   f'<circle class="rm-ring-bg" cx="{x}" cy="{mid}" r="34"/><circle class="rm-ring" data-ring="{escape(map_id)}" data-total="{count}" cx="{x}" cy="{mid}" r="34" transform="rotate(-90 {x} {mid})"/>'
                   f'<circle class="rm-station" cx="{x}" cy="{mid}" r="26"/><text class="rm-num" x="{x}" y="{mid + 6}" text-anchor="middle">{i + 1}</text>'
                   + svg_text(x, mid - 50 if up else mid + 60, m['title'], 18, 'rm-label', up=up) + '</a>')
    out.append(f'<circle class="rm-forkdot" cx="{fork}" cy="{mid}" r="9"/>')
    for k, (b, y) in enumerate(zip(branches, ys)):
        for j, map_id in enumerate(b['maps']):
            m = maps[map_id]
            count, _ = totals(m)
            x = fork + 230 + j * 150
            out.append(f'<a href="{escape(link(map_id))}" class="rm-node rm-node--branch rm-node--b{k}"><title>{escape(m["title"])} — {count} шагов</title>'
                       f'<circle class="rm-ring-bg" cx="{x}" cy="{y}" r="30"/><circle class="rm-ring" data-ring="{escape(map_id)}" data-total="{count}" cx="{x}" cy="{y}" r="30" transform="rotate(-90 {x} {y})"/>'
                       f'<circle class="rm-station" cx="{x}" cy="{y}" r="22"/>'
                       + svg_text(x, y - 44, b['title'], 20, 'rm-branch-title', up=True)
                       + svg_text(x, y + 52, m['title'], 18, 'rm-label') + '</a>')
        gx = W - 70
        out.append(f'<g class="rm-goal"><path d="M{gx},{y + 4} l0,-30 l24,8 l-24,8"/><text x="{gx}" y="{y + 26}" text-anchor="middle">Эксперт</text></g>')
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
    out = [f'<svg class="lm-svg" viewBox="0 0 {W} 210" role="img" aria-label="Путь по карте">']
    x = x0 + gap
    segs, nodes, n = [], [], 0
    for i, steps in enumerate(infos):
        start = x - gap
        for title, kind, key in steps:
            n += 1
            label = f'Шаг {n}. {title}'
            shape = (f'<rect class="lm-node-shape" x="{x - 13:.1f}" y="{y - 13}" width="26" height="26" rx="4" transform="rotate(45 {x:.1f} {y})"/>' if kind == 'course'
                     else f'<circle class="lm-node-shape" cx="{x:.1f}" cy="{y}" r="15"/>')
            nodes.append(f'<a href="#step-{n}" class="lm-node lm-node--l{i + 1}" data-node-step="{escape(map_id)}|{escape(key)}"><title>{escape(label)}</title>{shape}'
                         f'<text x="{x:.1f}" y="{y + 5}" text-anchor="middle">{n}</text></a>')
            x += gap
        segs.append(f'<path class="lm-seg" stroke="{LEVEL_COLORS[i]}" d="M{start:.1f},{y} L{x:.1f},{y}"/>')
        segs.append(svg_text(round((start + x) / 2), y - 46, f'Уровень {i + 1} · {levels[i]}', 26, f'lm-svg-level lm-svg-level--{i + 1}'))
        nodes.append(f'<a href="#level-{i + 1}" class="lm-flag"><title>Контрольная точка уровня {i + 1}: {escape(m["levels"][i]["checkpoint"])}</title>'
                     f'<path d="M{x:.1f},{y + 22} L{x:.1f},{y - 30} l20,7 l-20,7" stroke="{LEVEL_COLORS[i]}" fill="{LEVEL_COLORS[i]}"/></a>')
        x += gap
    out.append(f'<path class="lm-seg lm-seg--start" d="M{x0},{y} L{x0 + gap:.1f},{y}"/>')
    out.extend(segs)
    out.append(f'<circle class="lm-start" cx="{x0}" cy="{y}" r="9"/><text class="lm-svg-small" x="{x0}" y="{y + 34}" text-anchor="middle">старт</text>')
    out.extend(nodes)
    out.append(f'<g class="lm-goal"><circle cx="{x1 + 50}" cy="{y}" r="22"/><text x="{x1 + 50}" y="{y + 5}" text-anchor="middle">★</text>'
               f'<text class="lm-svg-small" x="{x1 + 50}" y="{y + 44}" text-anchor="middle">эксперт</text></g>')
    out.append(f'<g class="lm-legend"><circle cx="70" cy="190" r="7"/><text x="84" y="194">руководство Хаба</text>'
               f'<rect x="224" y="183" width="12" height="12" rx="2" transform="rotate(45 230 189)"/><text x="244" y="194">курс или документация</text>'
               f'<path d="M420,196 L420,182 l12,4 l-12,4" stroke="#5b6bd6" fill="#5b6bd6"/><text x="440" y="194">контрольная точка</text></g>')
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
    levels = data['levels']

    def step_info(step, here):
        """Title, address, label, minutes and stable key of a step."""
        if step.get('guide'):
            page = pages[f'kb/guides/{step["guide"]}']
            anchor = step.get('anchor')
            href = rel(url_of(here), url_of(page.id)) + (f'#{anchor}' if anchor else '')
            minutes = int(step.get('minutes') or (10 if anchor else page.meta.get('minutes', 5)))
            label = 'часть руководства' if anchor else 'руководство'
            return step.get('title') or page.title, href, label, minutes, f'{step["guide"]}#{anchor or ""}', False
        if step.get('page'):
            page = pages[step['page']]
            return step.get('title') or page.title, rel(url_of(here), url_of(page.id)), 'раздел Хаба', int(step.get('minutes', 20)), step['page'], False
        label = 'курс на русском' if step.get('lang') == 'ru' else 'курс, EN'
        return step['title'], step['url'], label, int(step.get('minutes', 30)), step['url'], True

    def totals(m, here):
        steps = [s for lv in m['levels'] for s in lv['steps']]
        minutes = sum(step_info(s, here)[3] for s in steps)
        return len(steps), minutes

    def hours(minutes):
        return f'около {max(1, round(minutes / 60))} ч' if minutes >= 90 else f'около {minutes} мин'

    def progress(map_id, total):
        return (f'<div class="lm-progress" data-map-progress="{e(map_id)}" data-total="{total}" aria-live="polite">'
                f'<span class="lm-bar"><i></i></span><b>0 из {total}</b></div>')

    order = data['roadmap']['core'] + [mid for b in data['roadmap']['branches'] for mid in b['maps']]
    for n, map_id in enumerate(order):
        m = maps[map_id]
        here = f'kb/maps/{map_id}'
        count, minutes = totals(m, here)
        infos = [[(lambda s: (s[0], 'course' if s[5] else 'guide', s[4]))(step_info(st, here)) for st in lv['steps']] for lv in m['levels']]
        out = [f'<p class="lede">{e(m["goal"])}</p>',
               f'<div class="lm-head"><span><b>Для кого:</b> {e(m["for"])}</span><span><b>Шагов:</b> {count} · {hours(minutes)}</span>{progress(map_id, count)}</div>',
               f'<figure class="lm-figure">{map_svg(map_id, m, infos, levels)}<figcaption>Наведите на шаг — увидите, что это; нажмите — перейдёте к нему. Пройденные шаги отмечаются зелёным, следующий — пульсирует.</figcaption></figure>']
        number = 0
        for i, lv in enumerate(m['levels']):
            items = []
            for step in lv['steps']:
                number += 1
                title, href, label, mins, key, outside = step_info(step, here)
                link = (f'<a href="{e(href)}" target="_blank" rel="noopener">{e(title)} ↗</a>' if outside else f'<a href="{e(href)}">{e(title)}</a>')
                practice = f'<p class="lm-practice"><b>Попробуйте:</b> {e(step["practice"])}</p>' if step.get('practice') else ''
                items.append(f'<li class="lm-step" id="step-{number}" data-step="{e(map_id)}|{e(key)}"><span class="lm-num">{number}</span><button type="button" class="lm-check" data-step-toggle aria-pressed="false" title="Отметить пройденным"><span class="o-sr-only">Отметить пройденным</span></button>'
                             f'<div class="lm-body"><div class="lm-title">{link}<span class="lm-tag">{e(label)} · {mins} мин</span></div>'
                             f'<p>{e(step["outcome"])}</p>{practice}</div></li>')
            out.append(f'<section class="lm-level lm-level--{i + 1}"><header><span class="lm-badge">Уровень {i + 1}</span><h2 id="level-{i + 1}">{e(levels[i])}</h2></header>'
                       f'<ol class="lm-steps">{"".join(items)}</ol><p class="lm-checkpoint"><b>Контрольная точка.</b> {e(lv["checkpoint"])}</p></section>')
        nxt = order[n + 1] if n + 1 < len(order) else None
        out.append(f'<nav class="lm-next"><a href="{e(rel(url_of(here), url_of("kb/maps")))}">← Вся дорожная карта</a>'
                   + (f'<a href="{e(rel(url_of(here), url_of(f"kb/maps/{nxt}")))}">Следующая карта: {e(maps[nxt]["title"])} →</a>' if nxt else '') + '</nav>')
        page = Page(here, f'Карта обучения: {m["title"]}', 'kb', 10 + n, f'{m["title"]} — от новичка до эксперта: {m["goal"]}', ''.join(out))
        page.nav = False
        pages[here] = page

    # the roadmap: the core stops in order, then the branches
    here = 'kb/maps'

    def stop(map_id, number):
        m = maps[map_id]
        count, minutes = totals(m, here)
        return (f'<a class="rm-card" href="{e(rel(url_of(here), url_of(f"kb/maps/{map_id}")))}"><small>{f"Остановка {number} · " if number else ""}{e(m["for"])}</small>'
                f'<h3>{e(m["title"])}</h3><p>{e(m["goal"])}</p><span class="rm-meta">4 уровня · {count} шагов · {hours(minutes)}</span>{progress(map_id, count)}</a>')
    core = ''.join(f'<li class="rm-stop"><span class="rm-dot">{i + 1}</span>{stop(mid, i + 1)}</li>' for i, mid in enumerate(data['roadmap']['core']))
    branches = ''.join(f'<div class="rm-branch"><h3>{e(b["title"])}</h3>{"".join(stop(mid, None) for mid in b["maps"])}</div>' for b in data['roadmap']['branches'])
    body = (f'<p class="lede">{e(data["roadmap"]["lede"])}</p>'
            '<p class="pf-tip">Отмечайте пройденные шаги на картах — прогресс сохраняется в вашем браузере и виден здесь. '
            '<button type="button" class="lm-reset" data-learn-reset>Сбросить прогресс</button></p>'
            f'<figure class="rm-figure">{roadmap_svg(data, maps, lambda mid: rel(url_of(here), url_of(f"kb/maps/{mid}")), lambda mm: totals(mm, here))}'
            '<figcaption>Начните со старта и двигайтесь по станциям. После четвёртой — выберите специализацию. Кольцо вокруг станции заполняется по мере прохождения карты.</figcaption></figure>'
            f'<h2 class="rm-h">Остановки по порядку</h2><ol class="rm-line">{core}</ol><div class="rm-fork"><span>Специализации — по вашей роли</span></div><div class="rm-branches">{branches}</div>'
            f'<p>Отдельные руководства и поиск по ним — в <a href="{e(rel(url_of(here), url_of("kb")))}">Базе знаний</a>.</p>')
    page = Page(here, data['roadmap']['title'], 'kb', 1, data['roadmap']['lede'], body)
    page.nav_title = 'Карты обучения'
    pages[here] = page
