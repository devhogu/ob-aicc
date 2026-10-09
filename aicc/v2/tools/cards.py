# START_MODULE_CONTRACT
#   PURPOSE: Read the project cards (YAML checked by a schema) and render the live views from them: the overview, the Portfolio (kanban, backlog, run-rate, register), the Program (kanban with lanes, backlog, intake), the control points and one page per card.
#   SCOPE: Reads aicc/v2/cards only. Produces Page objects for the builder; writes nothing itself.
#   DEPENDS: PyYAML, jsonschema, i18n, M-PORTAL-SOURCE (passed in as api)
#   LINKS: C-HUB-V2
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   STAGES, PROGRAM_COLUMNS - the states of the Portfolio and the columns of the Program board
#   load_cards - read and validate every card
#   NEXT_POINT - the next control point of each state: what is decided, by whom, on what
#   add_pages - add the generated pages to the page set
#   render_card - one card as a page
# END_MODULE_MAP
"""Project cards and the views rendered from them."""
from datetime import date
import json
from html import escape
from pathlib import Path

import jsonschema
import yaml

import cadence
import i18n
from i18n import T, P, loc

ROOT = Path(__file__).resolve().parents[3]
CARDS = ROOT / 'aicc' / 'v2' / 'cards'
STAGES = ['Воронка', 'Проработка', 'Готово к старту', 'В работе', 'Завершено']
OFF_FLOW = ['Отложено', 'Закрыто']
PROGRAM_COLUMNS = ['Бэклог', 'Готово к работе', 'В работе', 'На проверке', 'Завершено']
STAGE_TERM = {'Воронка': 'funnel', 'Проработка': 'shaping', 'Готово к старту': 'ready', 'В работе': 'doing', 'Завершено': 'done'}
STATUS_CLASS = {'зелёный': 'ok', 'жёлтый': 'warn', 'красный': 'bad', 'не задан': 'none'}
LANES = ['срочная работа', 'инициатива', 'текущая работа']
LANE_EN = {'срочная работа': 'Urgent', 'инициатива': 'Initiative', 'текущая работа': 'Run-rate'}
NEXT_POINT = {
    'Воронка': ('Взять в проработку', 'менеджер продукта', 'На карточке записаны задача, кому станет легче и как поймём, что получилось.'),
    'Проработка': ('Готово к старту', 'менеджер продукта с бизнес-владельцем', 'Записаны ожидаемый результат, критерий выхода, допустимый объём вложений и порог остановки.'),
    'Готово к старту': ('Решение о старте', 'бизнес-владелец и менеджер продукта', 'Есть место по WIP-лимиту; бизнес-кейс и условия на карточке.'),
    'В работе': ('Продолжить, изменить курс или остановить', 'бизнес-владелец', 'Достигнут критерий выхода или порог остановки, записанные до старта.'),
    'Завершено': ('Подтверждение результата', 'бизнес-владелец', 'Результат и уроки записаны на карточке.'),
    'Отложено': ('Вернуться в воронку', 'менеджер продукта', 'Наступили условия возвращения, записанные на карточке.'),
    'Закрыто': ('—', '—', 'Причина закрытия записана на карточке.'),
}
RUN_RATE_NEXT = {'Воронка': ('Взять в работу', 'менеджер продукта', 'Есть место по WIP-лимиту; запрос записан строкой на постоянной карточке.')}
TAB_HINT = {'portfolio': 'где каждый проект', 'program': 'что делается сейчас', 'plan': 'что по итерациям',
            'backlog': 'что дальше', 'decisions': 'кто что решает', 'register': 'все карточки'}
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
    e = escape
    wip = site.get('wip_limits', {})
    day = date.fromisoformat(site['as_of_date'])
    by_stage = {s: [c for c in cards if c['stage'] == s] for s in STAGES + OFF_FLOW}
    work = [(c, w) for c in cards for w in c.get('work', [])]

    def link(here, page_id):
        return e(rel(api.url_of(here), api.url_of(page_id)))

    def next_point(card):
        if card['profile'] == 'run-rate' and card['stage'] in RUN_RATE_NEXT:
            return tuple(T(x) for x in RUN_RATE_NEXT[card['stage']])
        return tuple(T(x) for x in NEXT_POINT[card['stage']])

    def V(value):
        """A value of a fixed vocabulary (state, class of service, status) in the edition language."""
        return T(value) if value else value

    def rank_key(card):
        return (card.get('rank') or 10 ** 6, card['id'])

    def flow(target, title, steps):
        """A row of states with their counts; a limit shows as count / limit."""
        cells = ''.join(f'<li class="{"is-busy" if n else ""}{" is-limited" if lim is not None else ""}"><strong>{n}{f"<em>/{lim}</em>" if lim is not None else ""}</strong><span>{e(s)}</span></li>'
                        for s, n, lim in steps)
        return f'<a class="here-tile here-flow" href="#{target}"><small>{e(title)}</small><ol>{cells}</ol></a>'

    def options(values, label):
        return f'<option value="">{e(label)}</option>' + ''.join(f'<option value="{e(v)}">{e(v)}</option>' for v in values)

    def filters(count):
        functions = sorted({loc(c, 'function') for c in cards if c.get('function')})
        areas = sorted({loc(c, 'area') for c in cards if c.get('area')})
        return (f'<div class="pf-filter" role="search" data-kb-filterbar><label><span class="pf-filter__label">{e(T("Найти"))}</span><input type="search" data-kb-search placeholder="{e(T("Найти: идентификатор, название, функция"))}"></label>'
                f'<label><span class="pf-filter__label">{e(T("Функция"))}</span><select data-kb-filter="function">{options(functions, T("Все функции"))}</select></label>'
                f'<label><span class="pf-filter__label">{e(T("Услуга"))}</span><select data-kb-filter="area">{options(areas, T("Все услуги"))}</select></label>'
                f'<output data-kb-count aria-live="polite">{e(T("Показано: {n}", n=count))}</output></div>')

    def card_attrs(card):
        find = ' '.join(x for x in (card['id'], loc(card, 'title'), loc(card, 'function') or '', loc(card, 'area') or '', loc(card, 'summary')) if x).lower()
        return f'data-find="{e(find)}" data-function="{e(loc(card, "function") or "")}" data-area="{e(loc(card, "area") or "")}"'

    def kb_card(here, card, ident, title, kind, state, foot_left, foot_right):
        return (f'<a class="kb-card" data-kb-open="{e(ident)}" href="{link(here, ids[card["id"]])}" title="{e(title)}" {card_attrs(card)}>'
                f'<div class="kb-meta"><span>{e(ident)}</span><span>{e(kind)}</span></div><h3>{e(title)}</h3>'
                f'<div class="kb-state">{e(state)}</div><div class="kb-foot"><span>{e(foot_left)}</span><span>{e(foot_right)}</span></div></a>')

    def detail_template(card, ident=None, extra=''):
        point, who, _ = next_point(card)
        facts = ''.join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in (
            (T('Состояние'), T(card['stage'])), (T('Следующая точка контроля'), point), (T('Кто решает'), who), (T('Функция'), loc(card, 'function') or '—')))
        o = card['outcome']
        return (f'<template data-kb-detail="{e(ident or card["id"])}"><header><span class="pf-meta">{e(card["id"])} · {e(T(PROFILE_TITLE[card["profile"]]))}</span>'
                f'<h2>{e(loc(card, "title"))}</h2><p>{e(loc(card, "summary"))}</p></header><dl class="pf-facts">{facts}</dl>{extra}'
                f'<div class="kb-detail-main"><section class="pf-section"><h3>{e(T("Задача"))}</h3><p>{e(loc(o, "problem"))}</p></section>'
                f'<section class="pf-section"><h3>{e(T("Ожидаемый результат"))}</h3><p>{e(loc(o, "intended_outcome"))}</p></section></div>'
                f'<p class="pf-notice"><strong>{e(T("Следующий шаг."))}</strong> {e(loc(card["live"], "next_step") or "—")}</p></template>')

    def gloss(en):
        """The English name beside a Russian column name; in English it would only repeat the name."""
        return f'<span class="kb-step-en" lang="en">{e(en)}</span>' if i18n.lang() == i18n.SOURCE else ''

    def column(title, en, count, caption, cards_html):
        return (f'<section class="kb-column" data-kb-column><div class="kb-column-head" role="button" tabindex="0" aria-label="{e(T("Показать колонку «{title}»", title=title))}"><div><h3>{e(title)}{gloss(en)}</h3>'
                f'<span class="kb-count">{count}</span></div><small>{e(caption)}</small></div>'
                f'<div class="kb-stack">{cards_html or "<span class=kb-empty>" + e(T("Пока ничего")) + "</span>"}</div></section>')

    def panel():
        return ('<section class="kb-detail" data-kb-panel hidden><div class="kb-detail-actions"><span data-kb-identity></span>'
                f'<div><a data-kb-full>{e(T("Полная карточка →"))}</a><button type="button" data-kb-close>{e(T("Закрыть ×"))}</button></div></div><div class="kb-detail-body"></div></section>')

    def tabs(items):
        heads = ''.join(f'<button type="button" role="tab" data-tab="{k}"{" aria-selected=true" if i == 0 else ""}><span>{e(label)}</span><small>{e(T(TAB_HINT[k]))}</small></button>' for i, (k, label, _) in enumerate(items))
        panels = ''.join(f'<section class="tab-panel" id="{k}" data-tab-panel="{k}" aria-label="{e(label)}"><h2 class="tab-title">{e(label)}</h2>{html}</section>' for k, label, html in items)
        return f'<div data-tabs><div class="pf-tabs" role="tablist">{heads}</div>{panels}</div>'

    def table(head, rows):
        return '<div class="o-table-wrap reg-scroll"><table class="hub-register"><thead><tr>' + ''.join(f'<th>{e(T(h))}</th>' for h in head) + f'</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'

    pf_en = {'Воронка': 'Funnel', 'Проработка': 'Shaping', 'Готово к старту': 'Ready', 'В работе': 'Doing', 'Завершено': 'Done'}
    pf_gate = {s: f'{T(NEXT_POINT[s][0])} — {T(NEXT_POINT[s][1])}' for s in STAGES}
    pf_gate['В работе'] = T('WIP-лимит {n} · {point} — бизнес-владелец', n=wip.get('portfolio', 1), point=T(NEXT_POINT['В работе'][0]).lower())
    pg_en = {'Бэклог': 'Backlog', 'Готово к работе': 'Ready', 'В работе': 'Doing', 'На проверке': 'Review', 'Завершено': 'Done'}
    pg_gate = {'Бэклог': T('Порядок — менеджер продукта; между проектами — форум решений по программе'), 'Готово к работе': T('Понятны результат и критерии приёмки · лимит {n}', n=wip.get('program_ready', 2)),
               'В работе': T('WIP-лимит {n}', n=wip.get('program', 1)), 'На проверке': T('Приёмка Feature — менеджер продукта'), 'Завершено': T('Принято и отмечено на карточке')}

    # ---- the one page: every view of the cards, each answering one question
    here = 'projects'
    lane_of = lambda c, w: w.get('class_of_service') or c.get('class_of_service') or 'инициатива'

    def tip(text, live=''):
        return f'<p class="pf-tip"{live}>{e(text)}</p>'

    PROJECTS = ('проект', 'проекта', 'проектов')
    IN_STAGE = {'Воронка': 'в воронке', 'Проработка': 'в проработке', 'Готово к старту': 'готовы к старту', 'В работе': 'в работе',
                'Завершено': 'завершены', 'Отложено': 'отложены', 'Закрыто': 'закрыты'}
    IN_STATE = {'Бэклог': 'в бэклоге', 'Готово к работе': 'готовы к работе', 'В работе': 'в работе', 'На проверке': 'на проверке', 'Завершено': 'завершены'}

    def counts(groups, names):
        return ', '.join(f'{len(groups[s])} {T(names[s])}' for s in names if groups.get(s))

    def nearest(items):
        """The most common next control point among open cards: (point, who, how many)."""
        tally = {}
        for c in items:
            point, who, _ = next_point(c)
            tally.setdefault((point, who), []).append(c)
        return sorted(((p, w, len(v)) for (p, w), v in tally.items()), key=lambda x: -x[2])

    # status lines: what can be read off the cards right now
    open_now = [c for c in cards if c['stage'] not in ('Завершено', 'Закрыто', 'Отложено')]
    n_work, lim = len(by_stage['В работе']), wip.get('portfolio', 1)
    top = nearest(open_now)
    pf_status = (T('{n} {noun}: {counts}.', n=len(cards), noun=P(len(cards), PROJECTS), counts=counts(by_stage, IN_STAGE)) + ' '
                 + T('В работе {n} из {lim} — {verdict}', n=n_work, lim=lim, verdict=T('есть место для старта.') if n_work < lim else T('лимит занят, следующий старт ждёт места.'))
                 + (' ' + T('Ближайшее решение у {n} {noun} — «{point}», решает {who}.', n=top[0][2], noun=P(top[0][2], PROJECTS), point=top[0][0].lower(), who=top[0][1]) if top else ''))
    by_state = {s: [w for _, w in work if w['state'] == s] for s in PROGRAM_COLUMNS}
    feats = lambda s: sum(1 for _, w in work if w['state'] == s and w['type'] == 'feature')
    urgent = sum(1 for c, w in work if (w.get('class_of_service') or c.get('class_of_service')) == 'срочная работа' and w['state'] != 'Завершено')
    pg_status = (T('{n} Capabilities и Features: {counts}.', n=len(work), counts=counts(by_state, IN_STATE)) + ' '
                 + T('Features в работе {doing} из {lim}, готовы к работе {ready} из {ready_lim}.', doing=feats('В работе'), lim=wip.get('program', 1), ready=feats('Готово к работе'), ready_lim=wip.get('program_ready', 2))
                 + ' ' + (T('Срочная работа: {n}.', n=urgent) if urgent else T('Срочной работы нет.'))
                 if work else T('Capabilities и Features пока нет: они появляются после решения о старте.'))
    reg_status = T('{n} {noun}: {counts}.', n=len(cards), noun=P(len(cards), ('карточка', 'карточки', 'карточек')),
                   counts=', '.join(f'{n} — {title.lower()}' for title, n in sorted({T(PROFILE_TITLE[c["profile"]]): sum(1 for x in cards if x["profile"] == c["profile"]) for c in cards}.items(), key=lambda x: -x[1])))

    # where each project is
    cols = ''.join(column(T(s), pf_en[s], len(by_stage[s]), pf_gate[s],
                          ''.join(kb_card(here, c, c['id'], loc(c, 'title'), T(PROFILE_TITLE[c['profile']]), loc(c['live'], 'next_step') or T(c['stage']),
                                          loc(c, 'function') or '—', loc(c, 'area') or V(c.get('class_of_service')) or '') for c in sorted(by_stage[s], key=rank_key)))
                   for s in STAGES)
    portfolio = (tip(pf_status)
                 + f'<div class="kb-scroll"><div class="kb-board kb-accordion" data-kb-accordion>{cols}</div></div>')
    off = by_stage['Отложено'] + by_stage['Закрыто']
    if off:
        portfolio += f'<h3>{e(T("Отложено и закрыто"))}</h3><div class="kb-scroll"><div class="kb-board" style="grid-template-columns:repeat(4,minmax(170px,1fr))">' + ''.join(
            kb_card(here, c, c['id'], loc(c, 'title'), T(PROFILE_TITLE[c['profile']]), T(c['stage']), loc(c, 'function') or '—', '') for c in off) + '</div></div>'

    # what is being built now
    def wcard(c, w):
        return kb_card(here, c, w['id'], loc(w, 'title'), 'Capability' if w['type'] == 'capability' else 'Feature', f'{c["id"]} · {loc(c, "title")}', loc(c, 'function') or '—', ('Jira ' + w['jira']) if w.get('jira') else (w.get('iteration') or '').replace(' I', ' i'))
    head_cells = ''.join(f'<th><div class="kb-column-head"><div><h3>{e(T(s))}{gloss(pg_en[s])}</h3><span class="kb-count">{sum(1 for _, w in work if w["state"] == s)}</span></div><small>{e(pg_gate[s])}</small></div></th>' for s in PROGRAM_COLUMNS)
    lane_rows = ''.join(f'<tr><th scope="row">{e(l.capitalize()) + gloss(LANE_EN[l]) if i18n.lang() == i18n.SOURCE else e(LANE_EN[l])}</th>' + ''.join(
        '<td><div class="kb-stack">' + (''.join(wcard(c, w) for c, w in work if w['state'] == s and lane_of(c, w) == l) or '<span class="kb-empty">—</span>') + '</div></td>' for s in PROGRAM_COLUMNS) + '</tr>' for l in LANES)
    program = (tip(pg_status)
               + f'<div class="kb-scroll"><table class="kb-table"><thead><tr><th></th>{head_cells}</tr></thead><tbody>{lane_rows}</tbody></table></div>')

    # when: the PI calendar with the work placed in iterations
    plan_rows = [{'id': c['id'], 'title': loc(c, 'title'), 'href': rel(api.url_of(here), api.url_of(ids[c['id']])),
                  'find': ' '.join(x for x in (c['id'], loc(c, 'title'), loc(c, 'function') or '', loc(c, 'area') or '', loc(c, 'summary')) if x).lower(),
                  'function': loc(c, 'function') or '', 'area': loc(c, 'area') or '',
                  'items': [{'id': w['id'], 'title': loc(w, 'title'), 'state': w['state'], 'iteration': w.get('iteration', ''),
                             'href': rel(api.url_of(here), api.url_of(ids[c['id']]))} for w in c.get('work', [])]}
                 for c in sorted(cards, key=rank_key) if c.get('work')]
    cal_data = {k: cadence.DATA[k] for k in ('days', 'year_end_from', 'seasons')} | {'rows': plan_rows}
    plan = (tip(cadence.plan_status(day, plan_rows), ' data-pi-status')
            + f'<section class="pi-cal" data-pi-calendar="{e(json.dumps(cal_data, ensure_ascii=False))}">{cadence.calendar_html(day, 0, plan_rows)}</section>')

    # what comes next
    backlog = sorted([c for c in cards if c['stage'] in ('Воронка', 'Проработка', 'Готово к старту') and c['profile'] != 'run-rate'], key=lambda c: (-STAGES.index(c['stage']),) + rank_key(c))
    backlog_rows = [f'<tr {card_attrs(c)} data-kb-row><td>{e(str(c["rank"])) if c.get("rank") else e(T("без места"))}</td><td><a href="{link(here, ids[c["id"]])}">{e(c["id"])}</a></td><td>{e(loc(c, "title"))}</td>'
                    f'<td>{e(T(c["stage"]))}</td><td>{e(loc(c, "function") or "—")}</td></tr>' for c in backlog]
    pb_rows = [f'<tr {card_attrs(c)} data-kb-row><td>{e(w["id"])}</td><td>{"Capability" if w["type"] == "capability" else "Feature"}</td><td>{e(loc(w, "title"))}</td><td>{e(T(w["state"]))}</td>'
               f'<td>{e((w.get("iteration") or "—").replace(" I", " i"))}</td><td><a href="{link(here, ids[c["id"]])}">{e(c["id"])}</a></td></tr>' for c, w in work if w['state'] != 'Завершено']
    open_work = [w for _, w in work if w['state'] != 'Завершено']
    bl_status = (T('Не начато {n} {noun} и {m} Capabilities и Features.', n=len(backlog), noun=P(len(backlog), PROJECTS), m=len(open_work))
                 + (' ' + T('Первым в очереди — {id} «{title}».', id=backlog[0]['id'], title=loc(backlog[0], 'title')) if backlog else ''))
    backlog_html = (tip(bl_status)
                    + f'<h3>{e(T("Проекты, ещё не начатые"))}</h3>' + table(['Место', 'Карточка', 'Название', 'Состояние', 'Функция'], backlog_rows)
                    + f'<h3>{e(T("Capabilities и Features, ещё не принятые"))}</h3>' + table(['Ключ', 'Вид', 'Название', 'Состояние', 'Итерация', 'Карточка'], pb_rows))

    # who decides what next
    open_cards = sorted([c for c in cards if c['stage'] not in ('Завершено', 'Закрыто')], key=lambda c: (STAGES.index(c['stage']) if c['stage'] in STAGES else 9,) + rank_key(c))
    point_rows = [f'<tr {card_attrs(c)} data-kb-row><td><a href="{link(here, ids[c["id"]])}">{e(c["id"])}</a></td><td>{e(loc(c, "title"))}</td><td>{e(T(c["stage"]))}</td>'
                  f'<td><strong>{e(next_point(c)[0])}</strong></td><td>{e(next_point(c)[1])}</td></tr>' for c in open_cards]
    log = [(c, d) for c in cards for d in c.get('decisions', [])]
    log_html = (table(['Карточка', 'Что решили', 'Кто', 'Когда'], [f'<tr {card_attrs(c)} data-kb-row><td><a href="{link(here, ids[c["id"]])}">{e(c["id"])}</a></td><td>{e(loc(d, "what"))}</td><td>{e(loc(d, "who") or "—")}</td><td>{e(d.get("when") or "—")}</td></tr>' for c, d in log])
                if log else f'<p class="pf-notice">{e(T("Решений пока не записано: все проекты ещё в начале пути."))}</p>')
    groups = nearest(open_cards)
    one = len({who for _, who, _ in groups}) == 1
    waiting = {'n': len(open_cards), 'noun': P(len(open_cards), PROJECTS)}
    dec_status = ((T('Решения ждут {n} {noun}, все решает {who}: {points}.', who=groups[0][1], points=', '.join(T('«{point}» — {n}', point=pt.lower(), n=n) for pt, _, n in groups), **waiting) if one
                   else T('Решения ждут {n} {noun}: {points}.', points='; '.join(T('«{point}» — {n}, решает {who}', point=pt.lower(), n=n, who=who) for pt, who, n in groups), **waiting)) + ' '
                  + (T('Принято решений: {n}.', n=len(log)) if log else T('Принятых решений пока нет.')))
    decisions = (tip(dec_status)
                 + table(['Карточка', 'Название', 'Состояние', 'Следующая точка контроля', 'Кто решает'], point_rows) + f'<h3>{e(T("Журнал решений"))}</h3>' + log_html)

    # everything in one list
    reg_rows = [f'<tr {card_attrs(c)} data-kb-row><td><a href="{link(here, ids[c["id"]])}">{e(c["id"])}</a></td><td>{e(loc(c, "title"))}</td><td>{e(T(PROFILE_TITLE[c["profile"]]))}</td><td>{e(T(c["stage"]))}</td>'
                f'<td>{e(loc(c, "function") or "—")}</td><td>{e(loc(c, "area") or "—")}</td></tr>' for c in cards]
    register = tip(reg_status) + table(['Карточка', 'Название', 'Профиль', 'Состояние', 'Функция', 'Услуга'], reg_rows)

    here_strip = (f'<section class="here" aria-label="{e(T("Где мы сейчас"))}">'
                  f'<div class="here-time" data-pi-here>{cadence.here_html(day)}</div><div class="here-place">'
                  + flow('portfolio', T('Портфель · проектов: {n}', n=len(cards)), [(T(s), len(by_stage[s]), wip.get('portfolio', 1) if s == 'В работе' else None) for s in STAGES])
                  + flow('program', T('Программа · Capabilities и Features: {n}', n=len(work)), [(T(s), sum(1 for _, w in work if w['state'] == s),
                                                                                          {'Готово к работе': wip.get('program_ready', 2), 'В работе': wip.get('program', 1)}.get(s)) for s in PROGRAM_COLUMNS])
                  + f'</div><p class="here-asof">{T("Карточки — по состоянию на {date}; дата, PI и итерация считаются от сегодняшнего дня.", date=e(loc(site, "as_of") or ""))}</p></section>')
    body = ('<article class="hub-board" data-kanban-workspace>' + here_strip
            + filters(len(cards))
            + tabs([('portfolio', T('Портфель'), portfolio), ('program', T('Программа'), program), ('plan', T('План PI'), plan),
                    ('backlog', T('Бэклог'), backlog_html), ('decisions', T('Решения'), decisions), ('register', T('Реестр'), register)])
            + panel() + ''.join(detail_template(c) for c in cards)
            + ''.join(detail_template(c, w['id'], f'<p class="pf-notice"><strong>{e(w["id"])}</strong> · {"Capability" if w["type"] == "capability" else "Feature"} · {e(loc(w, "title"))} · {e(T(w["state"]))}</p>') for c, w in work)
            + '</article>')
    pages[here] = Page(here, T('Проекты'), 'projects', 0, T('Все проекты на одной странице: портфель, программа, план PI по итерациям, бэклог, решения и реестр.'), body)

    # ---- how to bring a card
    here = 'projects/new'
    template = (CARDS / 'template.yaml').read_text(encoding='utf-8')
    body = (f'<p class="lede">{T("Заведите карточку, и ваш проект появится во всех видах раздела.")}</p>'
            f'<ol><li>{T("Скопируйте шаблон ниже в файл <code>cards/ИДЕНТИФИКАТОР.yaml</code>.")}</li>'
            f'<li>{T("Заполните обязательные поля: идентификатор, название, суть, профиль, состояние, позиции людей, задачу и ожидаемый результат, текущее состояние.")}</li>'
            f'<li>{T("Для идеи поставьте состояние «Воронка». Остальное можно добавить позже.")}</li>'
            f'<li>{T("Обновляйте карточку по мере работы: при следующей сборке все виды покажут изменения.")}</li></ol>'
            f'<p>{T("Карточка проверяется схемой: сборка остановится и подскажет, что поправить. Схема — <code>cards/schema.json</code>.")}</p>'
            f'<h2>{T("Шаблон")}</h2><pre><code>{e(template)}</code></pre>')
    pages[here] = Page(here, T('Завести карточку'), 'projects', 40, T('Как принести идею или проект.'), body)
    pages[here].nav = False

    # ---- one page per card
    for card in cards:
        pages[ids[card['id']]] = render_card(card, ids[card['id']], pages, terms, api, ids, next_point(card))
        pages[ids[card['id']]].nav = False


def render_card(card, page_id, pages, terms, api, ids, point=None):
    rel, Page, term = api.rel, api.Page, api.term_html
    here = api.url_of(page_id)
    e = escape
    status = card['live']['status']
    profile = card['profile']
    people = ''.join(
        f'<tr><td>{e(T(label))}</td><td>{e(loc(card["people"][key], "position"))}</td><td>{e(card["people"][key].get("holder") or "—")}</td></tr>'
        for key, label in (('business_owner', 'Бизнес-владелец'), ('product_manager', 'Менеджер продукта'), ('project_manager', 'Руководитель проекта')))
    outcome = card['outcome']
    out_rows = ''.join(f'<tr><td>{e(T(label))}</td><td>{e(loc(outcome, key))}</td></tr>' for key, label in
                       (('problem', 'Задача'), ('intended_outcome', 'Ожидаемый результат'), ('measure', 'Чем измерим'), ('baseline', 'Как сейчас'), ('target', 'Как хотим')) if outcome.get(key))
    constraints = card.get('constraints') or {}
    con_rows = ''.join(f'<tr><td>{e(T(label))}</td><td>{e(loc(constraints, key))}</td></tr>' for key, label in
                       (('appetite', 'Допустимый объём вложений'), ('review_point', 'Контрольная точка'), ('exit_criterion', 'Критерий выхода'), ('stop_threshold', 'Порог остановки')) if constraints.get(key))
    checklist = card.get('checklist') or []
    mark = {'сделано': '✔', 'не начато': '○', 'не нужно': '—'}
    check = ''.join(f'<li class="check {"done" if c["state"] == "сделано" else ""}"><span aria-hidden="true">{mark[c["state"]]}</span> {e(loc(c, "item"))}'
                    + (f' — <em>{e(loc(c, "note"))}</em>' if c.get('note') else '') + f' <span class="check-state">{e(T(c["state"]))}</span></li>' for c in checklist)
    live = card['live']
    risks = ''.join(f'<li>{e(r)}</li>' for r in loc(live, 'risks') or []) or '<li>—</li>'
    deps = ''.join(f'<li>{e(r)}</li>' for r in loc(live, 'dependencies') or []) or '<li>—</li>'
    work = ''.join(
        f'<tr><td>{e(w["id"])}</td><td>{"Capability" if w["type"] == "capability" else "Feature"}</td><td>{e(loc(w, "title"))}</td><td>{e(T(w["state"]))}</td><td>{e(w.get("jira") or "—")}</td></tr>'
        for w in card.get('work', []))
    decisions = ''.join(f'<tr><td>{e(loc(d, "what"))}</td><td>{e(loc(d, "who") or "—")}</td><td>{e(d.get("when") or "—")}</td></tr>' for d in card.get('decisions', []))
    closure = card.get('closure') or {}
    links = card.get('links') or {}
    profile_page = 'process/profiles'
    meta = ' · '.join(dict.fromkeys(x for x in (T(PROFILE_TITLE[profile]), (T(card['class_of_service']) if card.get('class_of_service') else '').capitalize(), loc(card, 'function')) if x))
    point_name, point_who, point_basis = point or ('—', '—', '')
    back = e(rel(here, api.url_of('projects')))
    owner = card['people']['business_owner']
    facts = ''.join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in (
        (T('Состояние'), T(card['stage'])), (T('Профиль'), T(PROFILE_TITLE[profile])), (T('Класс обслуживания'), T(card['class_of_service']) if card.get('class_of_service') else '—'),
        (T('Бизнес-владелец'), owner.get('holder') or loc(owner, 'position')), (T('Функция'), loc(card, 'function') or '—'), (T('Услуга'), loc(card, 'area') or '—'),
        (T('Место в бэклоге'), str(card['rank']) if card.get('rank') else T('без места')), (T('Статус'), T(status))))
    exit_rule = point_basis + (' ' + T('Критерий выхода на карточке: {criterion}', criterion=loc(constraints, 'exit_criterion')) if card['stage'] == 'В работе' and constraints.get('exit_criterion') else '')
    profile_link = T('Как устроена работа такого вида: <a href="{href}">профиль «{profile}»</a>.',
                     href=e(rel(here, api.url_of(profile_page))) + '#' + profile, profile=e(T(PROFILE_TITLE[profile])))
    body = (
        f'<p class="card-back"><a href="{back}">{T("← К проектам")}</a></p>'
        f'<dl class="pf-facts card-facts">{facts}</dl>'
        f'<section class="card-point"><h2>{T("Следующая точка контроля")}</h2><dl class="pf-facts"><div><dt>{T("Точка контроля")}</dt><dd><strong>{e(point_name)}</strong></dd></div>'
        f'<div><dt>{T("Кто решает")}</dt><dd>{e(point_who)}</dd></div></dl><p><strong>{T("На что опирается.")}</strong> {e(exit_rule)}</p>'
        f'<p class="pf-muted">{profile_link}</p></section>'
        f'<h2>{T("Люди")}</h2><div class="o-table-wrap"><table><thead><tr><th>{T("Роль")}</th><th>{T("Позиция")}</th><th>{T("Кто")}</th></tr></thead><tbody>{people}</tbody></table></div>'
        f'<h2>{T("Задача и результат")}</h2><div class="o-table-wrap"><table><tbody>{out_rows}</tbody></table></div>'
        + (f'<h2>{T("Условия")}</h2><div class="o-table-wrap"><table><tbody>{con_rows}</tbody></table></div>' if con_rows else '')
        + (f'<h2>{T("Памятка по практике")}</h2><ul class="checklist">{check}</ul>' if check else '')
        + f'<h2>{T("Сейчас")}</h2><p><strong>{T("Следующий шаг.")}</strong> {e(loc(live, "next_step") or "—")}</p><div class="two"><div><h3>{T("Главные риски")}</h3><ul>{risks}</ul></div><div><h3>{T("Зависимости")}</h3><ul>{deps}</ul></div></div>'
        + (f'<h2>{T("Работа")}</h2><div class="o-table-wrap"><table><thead><tr><th>{T("Ключ")}</th><th>{T("Вид")}</th><th>{T("Название")}</th><th>{T("Состояние")}</th><th>Jira</th></tr></thead><tbody>{work}</tbody></table></div>' if work else '')
        + (f'<h2>{T("Журнал решений")}</h2><div class="o-table-wrap"><table><thead><tr><th>{T("Что решили")}</th><th>{T("Кто")}</th><th>{T("Когда")}</th></tr></thead><tbody>{decisions}</tbody></table></div>' if decisions else f'<h2>{T("Журнал решений")}</h2><p class="pf-muted">{T("Решений пока не записано.")}</p>')
        + (f'<h2>{T("Итог")}</h2><p><strong>{T("Результат.")}</strong> {e(loc(closure, "result") or "—")}</p><p><strong>{T("Чему научились.")}</strong> {e(loc(closure, "lessons") or "—")}</p>' if closure.get('result') or closure.get('lessons') else '')
        + (f'<h2>{T("Ссылки")}</h2><ul>' + ''.join(f'<li>{e(k)}: {e(v)}</li>' for k, v in links.items() if v) + '</ul>' if any(links.values()) else ''))
    page = Page(page_id, f'{card["id"]}: {loc(card, "title")}', 'projects', 100, loc(card, 'summary'), body)
    return page
