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
        f'<li><strong><a href="{link(here, "projects/funnel")}">Воронка</a></strong> все идеи, которые ждут разбора</li>'
        f'<li><strong><a href="{link(here, "projects/portfolio")}">Портфель</a></strong> инициативы по состояниям, функциям и направлениям</li>'
        f'<li><strong><a href="{link(here, "projects/program")}">Программа</a></strong> возможности и функции на доске</li>'
        f'<li><strong><a href="{link(here, "projects/new")}">Завести карточку</a></strong> как принести идею или проект</li></ul>'
        f'<h2>Как это работает</h2>'
        f'<p>У каждого проекта есть карточка: один файл, в котором записано, что делаем, зачем, кто отвечает и на каком мы этапе. Карточку ведёт руководитель проекта. Пока карточка актуальна, сайт показывает проект правильно. Это всё, что нужно для отчётности.</p>')
    pages[here] = Page(here, 'Проекты', 'projects', 0, 'Воронка, портфель и программа в виде карточек.', body)

    # the Funnel
    here = 'projects/funnel'
    funnel = ''.join(tile(here, c) for c in by_stage['Воронка']) or '<li class="tile-empty">Пока ничего</li>'
    deferred = ''.join(tile(here, c) for c in by_stage['Отложено'])
    body = (f'<p class="lede">Все идеи, которые ждут разбора. Принести свою можно в любой момент: <a href="{link(here, "projects/new")}">заведите карточку</a>.</p>'
            f'<ul class="tiles wide">{funnel}</ul>' + (f'<h2>Отложено</h2><ul class="tiles wide">{deferred}</ul>' if deferred else ''))
    pages[here] = Page(here, 'Воронка', 'projects', 10, 'Идеи, которые ждут разбора.', body)

    # the Portfolio
    here = 'projects/portfolio'
    board = ''.join(column(here, s, by_stage[s], lambda c, h=here: tile(h, c), STAGE_TERM[s]) for s in STAGES)
    rows = lambda key: sorted({c.get(key) or '—' for c in cards})
    def grouped(key, label):
        out = []
        for value in rows(key):
            members = [c for c in cards if (c.get(key) or '—') == value]
            out.append(f'<h3>{escape(value)}</h3><ul class="tiles wide">' + ''.join(tile(here, c) for c in members) + '</ul>')
        return f'<h2>{escape(label)}</h2>' + ''.join(out)
    closed = ''.join(tile(here, c) for c in by_stage['Закрыто'])
    body = (f'<p class="lede">Все инициативы и повторяющиеся работы по состояниям. Работа начинается, когда есть место: действует {term(terms, "wip-limit", "лимит работ в процессе", api.url_of(here))}.</p>'
            f'<div class="board">{board}</div>' + grouped('function', 'По функциям') + grouped('area', 'По направлениям') +
            (f'<h2>Закрыто</h2><ul class="tiles wide">{closed}</ul>' if closed else ''))
    pages[here] = Page(here, 'Портфель', 'projects', 20, 'Инициативы по состояниям, функциям и направлениям.', body)

    # the Program
    here = 'projects/program'
    work = [(c, w) for c in cards for w in c.get('work', [])]
    def work_tile(pair):
        c, w = pair
        kind = 'возможность' if w['type'] == 'capability' else 'функция'
        jira = f' · Jira {escape(w["jira"])}' if w.get('jira') else ''
        return (f'<li class="tile"><span class="tile-id">{escape(w["id"])}</span> <strong>{escape(w["title"])}</strong>'
                f'<span class="tile-meta">{kind} · <a href="{link(here, ids[c["id"]])}">{escape(c["id"])}</a>{jira}</span></li>')
    columns = ''.join(column(here, s, [p for p in work if p[1]['state'] == s], work_tile) for s in PROGRAM_COLUMNS)
    body = (f'<p class="lede">Возможности и функции всех проектов на одной доске. Строки берутся из карточек, а подробности каждой функции живут в Jira.</p>'
            f'<div class="board">{columns}</div>')
    pages[here] = Page(here, 'Программа', 'projects', 30, 'Возможности и функции на доске.', body)

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
    profile_page = 'process/profiles/' + profile
    meta = ' · '.join(dict.fromkeys(x for x in (PROFILE_TITLE[profile], (card.get('class_of_service') or '').capitalize(), card.get('function')) if x))
    body = (
        f'<p class="card-meta"><span class="stage">{e(card["stage"])}</span> <span class="dot {STATUS_CLASS[status]}"></span> Состояние: {e(status)} · {e(meta)}</p>'
        f'<p>Как устроена работа такого вида: <a href="{e(rel(here, api.url_of(profile_page)))}">профиль «{e(PROFILE_TITLE[profile])}»</a>.</p>'
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
