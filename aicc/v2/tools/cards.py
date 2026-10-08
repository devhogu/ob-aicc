# START_MODULE_CONTRACT
#   PURPOSE: Read the project cards (YAML checked by a schema) and render the Hub views from them: the projects overview, the Funnel, the Portfolio, the Program and one page per card.
#   SCOPE: Reads aicc/v2/cards only. Produces Page objects for the builder; writes nothing itself.
#   DEPENDS: PyYAML, jsonschema, M-HUB-V2-BUILD (passed in as api)
#   LINKS: C-HUB-V2
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   STAGES, PROGRAM_COLUMNS - the states of the Portfolio and the columns of the Program board
#   load_cards - read and validate every card
#   add_pages - add the generated pages to the page set
# END_MODULE_MAP
"""Project cards and the views rendered from them."""
import json
from html import escape
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[3]
CARDS = ROOT / 'aicc' / 'v2' / 'cards'
STAGES = ['Воронка', 'Проработка', 'Готово к старту', 'В работе', 'Завершено']
OFF_FLOW = ['Отложено', 'Закрыто']
PROGRAM_COLUMNS = ['Бэклог', 'Готово к работе', 'В работе', 'На проверке', 'Завершено']
STAGE_TERM = {'Воронка': 'funnel', 'Проработка': 'shaping', 'Готово к старту': 'ready', 'В работе': 'doing', 'Завершено': 'done'}
STATUS_CLASS = {'зелёный': 'ok', 'жёлтый': 'warn', 'красный': 'bad', 'не задан': 'none'}
PROFILE_TITLE = {'initiative': 'Инициатива', 'run-rate': 'Текущая работа', 'recurring-check': 'Регулярная проверка', 'enablement': 'Обучение и внедрение'}


# START_CONTRACT: load_cards
#   PURPOSE: Read every card file, check it against the schema and the rules the schema cannot express.
#   INPUTS: { directory: Path - folder with the card files and schema.json }
#   OUTPUTS: { list - cards as dictionaries, in identifier order }
#   SIDE_EFFECTS: none
# END_CONTRACT: load_cards
def load_cards(directory=CARDS):
    schema = json.loads((directory / 'schema.json').read_text(encoding='utf-8'))
    validator = jsonschema.Draft202012Validator(schema)
    cards, seen, work_seen = [], set(), set()
    for path in sorted(directory.glob('*.yaml')):
        if path.name == 'template.yaml':
            continue
        card = yaml.safe_load(path.read_text(encoding='utf-8'))
        problems = sorted(validator.iter_errors(card), key=lambda e: list(e.path))
        if problems:
            where = '/'.join(str(p) for p in problems[0].path) or 'card'
            raise ValueError(f'{path.name}: {where}: {problems[0].message}')
        if path.stem != card['id']:
            raise ValueError(f'{path.name}: the file name must be the card id {card["id"]}')
        if card['id'] in seen:
            raise ValueError('duplicate card ' + card['id'])
        seen.add(card['id'])
        ids = {w['id'] for w in card.get('work', [])}
        if len(ids) != len(card.get('work', [])) or ids & work_seen:
            raise ValueError(f'{path.name}: work items repeat an id')
        work_seen |= ids
        for item in card.get('work', []):
            if item.get('parent') and item['parent'] not in ids:
                raise ValueError(f'{path.name}: {item["id"]} names a parent that is not on the card')
        cards.append(card)
    return cards


def add_pages(pages, site, terms, api):
    cards = load_cards()
    rel, Page, term = api.rel, api.Page, api.term_html
    ids = {c['id']: 'projects/' + c['id'].lower() for c in cards}

    def link(here, page_id):
        return escape(rel(api.url_of(here), api.url_of(page_id)))

    def tile(here, card):
        status = card['live']['status']
        owner = card['people']['business_owner'].get('holder') or ''
        meta = ' · '.join(x for x in (card.get('function'), card.get('class_of_service')) if x)
        owner_html = f'<span class="tile-owner">{escape(owner)}</span>' if owner else ''
        return (f'<li class="tile"><a href="{link(here, ids[card["id"]])}"><span class="tile-id">{escape(card["id"])}</span> '
                f'<strong>{escape(card["title"])}</strong></a>'
                f'<span class="tile-meta">{escape(meta)}</span>'
                f'{owner_html}'
                f'<span class="dot {STATUS_CLASS[status]}" title="Состояние: {escape(status)}"></span></li>')

    def column(here, title, items, tile_html, term_id=None, note=''):
        head = term(terms, term_id, title, api.url_of(here)) if term_id else escape(title)
        body = ''.join(tile_html(i) for i in items) or '<li class="tile-empty">Пока ничего</li>'
        return f'<section class="column"><h3>{head} <span class="count">{len(items)}</span></h3>{note}<ul class="tiles">{body}</ul></section>'

    by_stage = {s: [c for c in cards if c['stage'] == s] for s in STAGES + OFF_FLOW}

    # the overview
    here = 'projects'
    counts = ''.join(f'<li><strong>{len(by_stage[s])}</strong> {escape(s)}</li>' for s in STAGES)
    body = (
        f'<p class="lede">Все проекты Хаба в одном месте. Каждый проект ведёт своя карточка, сайт показывает её как есть.</p>'
        f'<ul class="stats">{counts}</ul>'
        f'<h2>Виды</h2><ul class="cards">'
        f'<li><strong><a href="{link(here, "projects/portfolio")}">Портфель</a></strong> канбан от воронки до завершения, по функциям и направлениям</li>'
        f'<li><strong><a href="{link(here, "projects/program")}">Программа</a></strong> возможности и функции на доске</li>'
        f'<li><strong><a href="{link(here, "projects/new")}">Завести карточку</a></strong> как принести идею или проект</li></ul>'
        f'<h2>Как это работает</h2>'
        f'<p>У каждого проекта есть карточка: один файл, в котором записано, что делаем, зачем, кто отвечает и на каком мы этапе. Карточку ведёт руководитель проекта. Пока карточка актуальна, сайт показывает проект правильно. Это всё, что нужно для отчётности.</p>')
    pages[here] = Page(here, 'Проекты', 'projects', 0, 'Портфель и программа в виде карточек.', body)

    # the live boards: one interactive workspace per level, in the manner of the kit's Kanban
    wip = site.get('wip_limits', {})
    pf_gates = {'Воронка': 'Взять в проработку — менеджер продукта', 'Проработка': 'Условия записаны: критерий выхода, объём вложений, порог остановки',
                'Готово к старту': 'Решение о старте — бизнес-владелец и менеджер продукта',
                'В работе': f'WIP-лимит {wip.get("portfolio", 1)} · продолжать ли — бизнес-владелец', 'Завершено': 'Результат подтверждает бизнес-владелец'}
    pf_en = {'Воронка': 'Funnel', 'Проработка': 'Shaping', 'Готово к старту': 'Ready', 'В работе': 'Doing', 'Завершено': 'Done'}
    pg_gates = {'Бэклог': 'Порядок — менеджер продукта и форум решений по программе', 'Готово к работе': 'Понятны результат и критерии приёмки',
                'В работе': f'WIP-лимит {wip.get("program", 1)}', 'На проверке': 'Приёмка Feature — менеджер продукта', 'Завершено': 'Принято и отмечено на карточке'}
    pg_en = {'Бэклог': 'Backlog', 'Готово к работе': 'Ready', 'В работе': 'Active', 'На проверке': 'Review', 'Завершено': 'Done'}
    e = escape

    def options(values, label):
        return f'<option value="">{e(label)}</option>' + ''.join(f'<option value="{e(v)}">{e(v)}</option>' for v in values)

    def filters(here, items, kind):
        functions = sorted({c.get('function') for c in cards if c.get('function')})
        areas = sorted({c.get('area') for c in cards if c.get('area')})
        return (f'<div class="pf-filter" role="search"><label>Найти<input type="search" data-kb-search placeholder="идентификатор, название, функция"></label>'
                f'<label>Функция<select data-kb-filter="function">{options(functions, "Все функции")}</select></label>'
                f'<label>Услуга<select data-kb-filter="area">{options(areas, "Все услуги")}</select></label>'
                f'<output data-kb-count aria-live="polite">Показано: {len(items)}</output></div>')

    def card_attrs(card):
        find = ' '.join(x for x in (card['id'], card['title'], card.get('function', ''), card.get('area', ''), card['summary']) if x).lower()
        return f'data-find="{e(find)}" data-function="{e(card.get("function", ""))}" data-area="{e(card.get("area", ""))}"'

    def kb_card(here, card, ident, title, kind, state, foot_left, foot_right, find_attrs):
        return (f'<a class="kb-card" data-kb-open="{e(ident)}" href="{link(here, ids[card["id"]])}" title="{e(title)}" {find_attrs}>'
                f'<div class="kb-meta"><span>{e(ident)}</span><span>{e(kind)}</span></div><h3>{e(title)}</h3>'
                f'<div class="kb-state">{e(state)}</div><div class="kb-foot"><span>{e(foot_left)}</span><span>{e(foot_right)}</span></div></a>')

    def detail_template(here, card, ident=None, extra=''):
        status = card['live']['status']
        facts = ''.join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in (
            ('Состояние', card['stage']), ('Статус', status), ('Класс', card.get('class_of_service', '—')), ('Функция', card.get('function') or '—')))
        o = card['outcome']
        return (f'<template data-kb-detail="{e(ident or card["id"])}"><header><span class="pf-meta">{e(card["id"])} · {e(PROFILE_TITLE[card["profile"]])}</span>'
                f'<h2>{e(card["title"])}</h2><p>{e(card["summary"])}</p></header><dl class="pf-facts">{facts}</dl>{extra}'
                f'<div class="kb-detail-main"><section class="pf-section"><h3>Задача</h3><p>{e(o["problem"])}</p></section>'
                f'<section class="pf-section"><h3>Ожидаемый результат</h3><p>{e(o["intended_outcome"])}</p></section></div>'
                f'<p class="pf-notice"><strong>Следующий шаг.</strong> {e(card["live"].get("next_step") or "—")}</p></template>')

    def column(title, en, count, caption, cards_html):
        return (f'<section class="kb-column"><div class="kb-column-head"><div><h3>{e(title)}<span class="kb-step-en" lang="en">{e(en)}</span></h3>'
                f'<span class="kb-count">{count}</span></div><small>{e(caption)}</small></div>'
                f'<div class="kb-stack">{cards_html or "<span class=kb-empty>Пока ничего</span>"}</div></section>')

    def panel():
        return ('<section class="kb-detail" data-kb-panel hidden><div class="kb-detail-actions"><span data-kb-identity></span>'
                '<div><a data-kb-full>Полная карточка →</a><button type="button" data-kb-close>Закрыть ×</button></div></div><div class="kb-detail-body"></div></section>')

    def stats(items):
        return '<div class="pf-stats">' + ''.join(f'<div><strong>{e(str(v))}</strong><span>{e(k)}</span></div>' for k, v in items) + '</div>'

    # the Portfolio
    here = 'projects/portfolio'
    cols = []
    for s in STAGES:
        html = ''.join(kb_card(here, c, c['id'], c['title'], PROFILE_TITLE[c['profile']], c['live'].get('next_step') or c['stage'],
                               c.get('function') or '—', c.get('class_of_service') or '', card_attrs(c)) for c in by_stage[s])
        cols.append(column(s, pf_en[s], len(by_stage[s]), pf_gates[s], html))
    templates = ''.join(detail_template(here, c) for c in cards)
    off = by_stage['Отложено'] + by_stage['Закрыто']
    register = ''.join(f'<tr data-kb-row {card_attrs(c)}><td><a href="{link(here, ids[c["id"]])}">{e(c["id"])}</a></td><td>{e(c["title"])}</td><td>{e(c["stage"])}</td>'
                       f'<td>{e(c.get("function") or "—")}</td><td>{e(c.get("area") or "—")}</td><td>{e(c.get("class_of_service") or "—")}</td></tr>' for c in cards)
    run_rate = sum(1 for c in cards if c['profile'] == 'run-rate')
    body = (f'<article class="hub-board" data-kanban-workspace>'
            f'<p class="lede">Все идеи, инициативы и текущая работа на одном канбане — от воронки до завершения. Нажмите на карточку, чтобы увидеть её здесь же; полная карточка открывается по ссылке.</p>'
            + stats([('В воронке', len(by_stage['Воронка'])), ('В проработке', len(by_stage['Проработка'])),
                     ('В работе, в пределах лимита', f'{len(by_stage["В работе"])} / {wip.get("portfolio", 1)}'), ('Текущая работа', run_rate)])
            + filters(here, cards, 'portfolio')
            + f'<div class="kb-scroll"><div class="kb-board" style="grid-template-columns:repeat(5,minmax(170px,1fr));min-width:900px">{"".join(cols)}</div></div>'
            + panel() + templates
            + (('<h2>Отложено и закрыто</h2><ul class="tiles wide">' + ''.join(tile(here, c) for c in off) + '</ul>') if off else '')
            + f'<h2>Реестр</h2><div class="o-table-wrap"><table class="hub-register"><thead><tr><th>Карточка</th><th>Название</th><th>Состояние</th><th>Функция</th><th>Услуга</th><th>Класс</th></tr></thead><tbody>{register}</tbody></table></div>'
            + '</article>')
    pages[here] = Page(here, 'Портфель', 'projects', 20, 'Канбан портфеля от воронки до завершения, с поиском и фильтрами.', body)

    # the Program
    here = 'projects/program'
    work = [(c, w) for c in cards for w in c.get('work', [])]
    cols = []
    for s in PROGRAM_COLUMNS:
        html = ''.join(kb_card(here, c, w['id'], w['title'], 'Capability' if w['type'] == 'capability' else 'Feature', f'{c["id"]} · {c["title"]}',
                               c.get('function') or '—', ('Jira ' + w['jira']) if w.get('jira') else '', card_attrs(c))
                       for c, w in work if w['state'] == s)
        cols.append(column(s, pg_en[s], sum(1 for _, w in work if w['state'] == s), pg_gates[s], html))
    templates = ''.join(detail_template(here, c, w['id'], f'<p class="pf-notice"><strong>{e(w["id"])}</strong> · {"Capability" if w["type"] == "capability" else "Feature"} · {e(w["title"])} · {e(w["state"])}</p>') for c, w in work)
    body = (f'<article class="hub-board" data-kanban-workspace>'
            f'<p class="lede">Capabilities и Features всех начатых инициатив и текущей работы на одной доске. Строки берутся из карточек, подробности каждой Feature — в Jira.</p>'
            + stats([('В бэклоге', sum(1 for _, w in work if w['state'] == 'Бэклог')), ('Готово к работе', sum(1 for _, w in work if w['state'] == 'Готово к работе')),
                     ('В работе, в пределах лимита', f'{sum(1 for _, w in work if w["state"] == "В работе")} / {wip.get("program", 1)}'), ('Принято', sum(1 for _, w in work if w['state'] == 'Завершено'))])
            + filters(here, [c for c, _ in work], 'program')
            + f'<div class="kb-scroll"><div class="kb-board" style="grid-template-columns:repeat(5,minmax(170px,1fr));min-width:900px">{"".join(cols)}</div></div>'
            + panel() + templates + '</article>')
    pages[here] = Page(here, 'Программа', 'projects', 30, 'Доска программы: Capabilities и Features всех инициатив, с поиском и фильтрами.', body)

    # how to bring a card
    here = 'projects/new'
    template = (CARDS / 'template.yaml').read_text(encoding='utf-8')
    body = (f'<p class="lede">Заведите карточку, и ваш проект появится на сайте.</p>'
            f'<ol><li>Скопируйте шаблон ниже в файл <code>cards/ИДЕНТИФИКАТОР.yaml</code>.</li>'
            f'<li>Заполните обязательные поля: идентификатор, название, суть, профиль, состояние, позиции людей, задача и ожидаемый результат, текущее состояние.</li>'
            f'<li>Для идеи поставьте состояние «Воронка». Остальное можно добавить позже.</li>'
            f'<li>Обновляйте карточку по мере работы. Сайт при следующей сборке покажет изменения.</li></ol>'
            f'<p>Карточка проверяется схемой: сборка остановится и скажет, что поправить. Файл схемы — <code>cards/schema.json</code>, оба файла лежат в <a href="{escape(rel(api.url_of(here), "sources/index.html"))}">исходных файлах</a>.</p>'
            f'<h2>Шаблон</h2><pre><code>{escape(template)}</code></pre>')
    pages[here] = Page(here, 'Завести карточку', 'projects', 40, 'Как принести идею или проект.', body)

    # one page per card
    for card in cards:
        pages[ids[card['id']]] = render_card(card, ids[card['id']], pages, terms, api, ids)
        pages[ids[card['id']]].nav = False


def render_card(card, page_id, pages, terms, api, ids):
    rel, Page, term = api.rel, api.Page, api.term_html
    here = api.url_of(page_id)
    e = escape
    status = card['live']['status']
    profile = card['profile']
    people = ''.join(
        f'<tr><td>{e(label)}</td><td>{e(card["people"][key]["position"])}</td><td>{e(card["people"][key].get("holder") or "—")}</td></tr>'
        for key, label in (('business_owner', 'Бизнес-владелец'), ('product_manager', 'Менеджер продукта'), ('project_manager', 'Руководитель проекта')))
    outcome = card['outcome']
    out_rows = ''.join(f'<tr><td>{e(label)}</td><td>{e(outcome[key])}</td></tr>' for key, label in
                       (('problem', 'Задача'), ('intended_outcome', 'Ожидаемый результат'), ('measure', 'Чем измерим'), ('baseline', 'Как сейчас'), ('target', 'Как хотим')) if outcome.get(key))
    constraints = card.get('constraints') or {}
    con_rows = ''.join(f'<tr><td>{e(label)}</td><td>{e(constraints[key])}</td></tr>' for key, label in
                       (('appetite', 'Допустимый объём вложений'), ('review_point', 'Контрольная точка'), ('exit_criterion', 'Критерий выхода'), ('stop_threshold', 'Порог остановки')) if constraints.get(key))
    checklist = card.get('checklist') or []
    mark = {'сделано': '✔', 'не начато': '○', 'не нужно': '—'}
    check = ''.join(f'<li class="check {"done" if c["state"] == "сделано" else ""}"><span aria-hidden="true">{mark[c["state"]]}</span> {e(c["item"])}'
                    + (f' <em>{e(c["note"])}</em>' if c.get('note') else '') + f' <span class="check-state">{e(c["state"])}</span></li>' for c in checklist)
    live = card['live']
    risks = ''.join(f'<li>{e(r)}</li>' for r in live.get('risks', [])) or '<li>—</li>'
    deps = ''.join(f'<li>{e(r)}</li>' for r in live.get('dependencies', [])) or '<li>—</li>'
    work = ''.join(
        f'<tr><td>{e(w["id"])}</td><td>{"возможность" if w["type"] == "capability" else "функция"}</td><td>{e(w["title"])}</td><td>{e(w["state"])}</td><td>{e(w.get("jira") or "—")}</td></tr>'
        for w in card.get('work', []))
    decisions = ''.join(f'<tr><td>{e(d["what"])}</td><td>{e(d.get("who") or "—")}</td><td>{e(d.get("when") or "—")}</td></tr>' for d in card.get('decisions', []))
    closure = card.get('closure') or {}
    links = card.get('links') or {}
    profile_page = 'process/profiles'
    meta = ' · '.join(dict.fromkeys(x for x in (PROFILE_TITLE[profile], (card.get('class_of_service') or '').capitalize(), card.get('function')) if x))
    body = (
        f'<p class="card-meta"><span class="stage">{e(card["stage"])}</span> <span class="dot {STATUS_CLASS[status]}"></span> Состояние: {e(status)} · {e(meta)}</p>'
        f'<p>Как устроена работа такого вида: <a href="{e(rel(here, api.url_of(profile_page)))}#{profile}">профиль «{e(PROFILE_TITLE[profile])}»</a>.</p>'
        f'<h2>Люди</h2><div class="o-table-wrap"><table><thead><tr><th>Роль</th><th>Позиция</th><th>Кто</th></tr></thead><tbody>{people}</tbody></table></div>'
        f'<h2>Задача и результат</h2><div class="o-table-wrap"><table><tbody>{out_rows}</tbody></table></div>'
        + (f'<h2>Условия</h2><div class="o-table-wrap"><table><tbody>{con_rows}</tbody></table></div>' if con_rows else '')
        + (f'<h2>Памятка по практике</h2><ul class="checklist">{check}</ul>' if check else '')
        + f'<h2>Сейчас</h2><p><strong>Следующий шаг.</strong> {e(live.get("next_step") or "—")}</p><div class="two"><div><h3>Главные риски</h3><ul>{risks}</ul></div><div><h3>Зависимости</h3><ul>{deps}</ul></div></div>'
        + (f'<h2>Работа</h2><div class="o-table-wrap"><table><thead><tr><th>Ключ</th><th>Вид</th><th>Название</th><th>Состояние</th><th>Jira</th></tr></thead><tbody>{work}</tbody></table></div>' if work else '')
        + (f'<h2>Журнал решений</h2><div class="o-table-wrap"><table><thead><tr><th>Что решили</th><th>Кто</th><th>Когда</th></tr></thead><tbody>{decisions}</tbody></table></div>' if decisions else '')
        + (f'<h2>Итог</h2><p><strong>Результат.</strong> {e(closure.get("result") or "—")}</p><p><strong>Чему научились.</strong> {e(closure.get("lessons") or "—")}</p>' if closure.get('result') or closure.get('lessons') else '')
        + (f'<h2>Ссылки</h2><ul>' + ''.join(f'<li>{e(k)}: {e(v)}</li>' for k, v in links.items() if v) + '</ul>' if any(links.values()) else ''))
    page = Page(page_id, f'{card["id"]}: {card["title"]}', 'projects', 100, card['summary'], body)
    return page
