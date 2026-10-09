# START_MODULE_CONTRACT
#   PURPOSE: The PI calendar: from any date, the current program increment, its iterations with real dates, the current iteration and week, and the next increments.
#   SCOPE: Pure date arithmetic on the calendar rules plus the known week notes in aicc/v2/calendar.json. The page script applies the same rules to today's date.
#   DEPENDS: none
#   LINKS: C-HUB-V2, M-PORTAL-SOURCE
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   iteration - the iteration of a year and month: start Monday, end Sunday, weeks
#   week_of - the iteration and week that contain a date
#   increment - a program increment: its three iterations and its IP week
#   rolling - the current increment and the next ones
# END_MODULE_MAP
"""PI calendar rules: an iteration is a calendar month; a week (Monday to Sunday) belongs to the month that holds its Thursday;
a program increment is a quarter of three iterations; the IP week is the last week of the third iteration, the fourth in a five-week I12."""
from datetime import date, timedelta
import json
from pathlib import Path

DATA = json.loads((Path(__file__).resolve().parents[1] / 'calendar.json').read_text(encoding='utf-8'))
MONTHS = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']


def first_monday(year, month):
    """Monday of the week whose Thursday is the first Thursday of the month."""
    day = date(year, month, 1)
    thursday = day + timedelta(days=(3 - day.weekday()) % 7)
    return thursday - timedelta(days=3)


# START_CONTRACT: iteration
#   PURPOSE: The iteration of a year and month.
#   INPUTS: { year: int; month: int 1..12 }
#   OUTPUTS: { dict - name (I10), pi, start (Monday), end (Sunday), weeks }
#   SIDE_EFFECTS: none
# END_CONTRACT: iteration
def iteration(year, month):
    start = first_monday(year, month)
    nxt = first_monday(year + (month == 12), month % 12 + 1)
    end = nxt - timedelta(days=1)
    return {'name': f'I{month:02d}', 'label': f'i{month:02d}', 'month': month, 'year': year, 'pi': f'{year}-PIQ{(month - 1) // 3 + 1}',
            'start': start, 'end': end, 'weeks': (nxt - start).days // 7, 'title': MONTHS[month - 1]}


# START_CONTRACT: week_of
#   PURPOSE: The iteration and the week number that contain a date.
#   INPUTS: { day: date }
#   OUTPUTS: { (dict, int) - the iteration and the week number from 1 }
#   SIDE_EFFECTS: none
# END_CONTRACT: week_of
def week_of(day):
    monday = day - timedelta(days=day.weekday())
    thursday = monday + timedelta(days=3)
    it = iteration(thursday.year, thursday.month)
    return it, (monday - it['start']).days // 7 + 1


# START_CONTRACT: day_kind
#   PURPOSE: What kind of day a date is for planning: 'off' (non-working), 'away' (people likely absent), 'short' (shortened) or '' (ordinary).
#   INPUTS: { day: date }
#   OUTPUTS: { str }
#   SIDE_EFFECTS: none
# END_CONTRACT: day_kind
def day_kind(day):
    kind = DATA['days'].get(day.isoformat())
    if kind:
        return kind
    month, first = DATA['year_end_from']
    return 'away' if day.weekday() < 5 and day.month == month and day.day >= first else ''


def lost_days(monday):
    """Working days of the week that are off or with people likely absent."""
    return sum(1 for k in range(5) if day_kind(monday + timedelta(days=k)) in ('off', 'away'))


def increment(year, quarter):
    its = [iteration(year, 3 * (quarter - 1) + k) for k in (1, 2, 3)]
    name = f'{year}-PIQ{quarter}'
    last = its[-1]
    ip_week = last['weeks']
    while ip_week > 1 and lost_days(last['start'] + timedelta(weeks=ip_week - 1)) > 2:
        ip_week -= 1  # Planning moves to the week before until enough people are there
    ip_start = last['start'] + timedelta(weeks=ip_week - 1)
    return {'name': name, 'iterations': its, 'start': its[0]['start'], 'end': last['end'],
            'ip': {'name': f'{name} {last["name"]}W{ip_week}', 'start': ip_start, 'end': ip_start + timedelta(days=4)}}


# START_CONTRACT: rolling
#   PURPOSE: The current increment and the following ones, with the current iteration and week.
#   INPUTS: { day: date; count: int - increments to show }
#   OUTPUTS: { dict - today, iteration, week, week_name, note, increments }
#   SIDE_EFFECTS: none
# END_CONTRACT: rolling
def rolling(day, count=3):
    it, week = week_of(day)
    year, quarter = it['year'], (it['month'] - 1) // 3 + 1
    pis = []
    for _ in range(count):
        pis.append(increment(year, quarter))
        year, quarter = (year + 1, 1) if quarter == 4 else (year, quarter + 1)
    name = f'{it["pi"]} {it["name"]}W{week}'
    return {'today': day, 'iteration': it, 'week': week, 'week_name': name, 'note': week_note(it['start'] + timedelta(weeks=week - 1)), 'increments': pis}


SHORT = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
LONG = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']


def esc(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def span(a, b, long=False):
    names = LONG if long else SHORT
    left = f'{a.day} {names[a.month - 1]}' + (f' {a.year}' if a.year != b.year else '')
    return f'{left} – {b.day} {names[b.month - 1]} {b.year}'


# START_CONTRACT: week_note
#   PURPOSE: A short note on a week's working days that are off, with likely absences or shortened, and on a season.
#   INPUTS: { monday: date }
#   OUTPUTS: { str - empty for an ordinary week }
#   SIDE_EFFECTS: none
# END_CONTRACT: week_note
def week_note(monday):
    groups = {'off': [], 'away': [], 'short': []}
    for k in range(5):
        d = monday + timedelta(days=k)
        kind = day_kind(d)
        if kind:
            groups[kind].append(f'{d.day} {SHORT[d.month - 1]}')
    parts = [f'{label}: {"вся неделя" if len(groups[key]) == 5 else ", ".join(groups[key])}'
             for key, label in (('off', 'нерабочие'), ('away', 'вероятны отсутствия'), ('short', 'сокращённый день')) if groups[key]]
    friday = (monday + timedelta(days=4)).isoformat()
    parts += [s['text'] for s in DATA['seasons'] if s['from'] <= friday and monday.isoformat() <= s['to']]
    return '; '.join(parts)


DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']


def short(a, b):
    if a.month == b.month:
        return f'{a.day}–{b.day} {SHORT[b.month - 1]}'
    return f'{a.day} {SHORT[a.month - 1]} – {b.day} {SHORT[b.month - 1]}'


TAG = {'ip': 'Planning', 'review': 'Review'}


def week_kind(i, w, ip):
    """'ip' for the Planning week of the increment, 'review' for the last week of its first and second iterations."""
    if f'{i["pi"]} {i["name"]}W{w}' == ip:
        return 'ip'
    return 'review' if w == i['weeks'] and i['month'] % 3 else ''



def quiet(s, kind):
    """An ordinary week in which most working days are off or people are away."""
    return not kind and lost_days(s) > 2


def wtext(prefix, s, kind):
    return f'{prefix} · {week_range(s, kind)}' + (f' · {TAG[kind]}' if kind else '') + (' · вероятны отсутствия' if quiet(s, kind) else '')


def week_range(s, kind):
    """A week's dates without the year; the Planning week counts its working days."""
    return short(s, s + timedelta(days=4 if kind == 'ip' else 6))


# START_CONTRACT: here_html
#   PURPOSE: Where we are in time: today; the current increment with its iterations, weeks and key weeks to pick; the current iteration with its weeks to pick.
#   INPUTS: { day: date }
#   OUTPUTS: { str - HTML of three tiles; site.js draws the same tiles for the reader's date }
#   SIDE_EFFECTS: none
# END_CONTRACT: here_html
def here_html(day):
    r = rolling(day, 1)
    pi, it, week = r['increments'][0], r['iteration'], r['week']
    monday = day - timedelta(days=day.weekday())
    pi_weeks = ((pi['end'] - pi['start']).days + 1) // 7
    pi_week = (monday - pi['start']).days // 7 + 1
    ip = pi['ip']['name']

    def pick(text, now):
        return esc(text + (' · сейчас' if now else ''))

    segs = []
    for i in pi['iterations']:
        cells = []
        for w in range(1, i['weeks'] + 1):
            s = i['start'] + timedelta(weeks=w - 1)
            k = week_kind(i, w, ip)
            text = wtext(f'{i["label"]} W{w}', s, k)
            cells.append(f'<button type="button"{cls("is-done" if s < monday else "is-current" if s == monday else "", f"is-{k}" if k else "", "is-quiet" if quiet(s, k) else "", "is-picked" if s == monday else "")} '
                         f'data-here-week data-range="{pick(text, s == monday)}" aria-label="{i["label"]} W{w}"></button>')
        segs.append(f'<li{cls("is-current" if it_key(i) == it_key(it) else "", "is-done" if i["end"] < monday else "", "is-picked" if it_key(i) == it_key(it) else "")} data-here-it="{it_key(i)}" style="flex:{i["weeks"]}">'
                    f'<span class="here-cells">{"".join(cells)}</span>'
                    f'<button type="button" class="here-it" data-here-week data-range="{i["label"]} · {short(i["start"], i["end"])} · {i["weeks"]} нед."><b>{i["label"]} · {i["title"]}</b><span>{short(i["start"], i["end"])}</span></button>'
                    '</li>')
    weeks = []
    for w in range(1, it['weeks'] + 1):
        s = it['start'] + timedelta(weeks=w - 1)
        k = week_kind(it, w, ip)
        weeks.append(f'<li><button type="button"{cls("is-done" if w < week else "is-current" if w == week else "", f"is-{k}" if k else "", "is-quiet" if quiet(s, k) else "", "is-picked" if w == week else "")} '
                     f'data-here-week data-range="{pick(wtext(f"W{w}", s, k), w == week)}">{TAG.get(k, f"W{w}")}</button></li>')
    now = week_kind(it, week, ip)
    return (f'<div class="here-tile" data-week="{monday.isoformat()}" tabindex="0"><small>Сегодня</small><strong>{day.day} {LONG[day.month - 1]} {day.year}</strong><span>{DAYS[day.weekday()]}</span></div>'
            f'<div class="here-tile" data-pi="{pi["name"]}" tabindex="0"><small>Программный инкремент · неделя {pi_week} из {pi_weeks}</small><div class="here-head"><strong>PI {pi["name"]}</strong><span>{span(pi["start"], pi["end"])}</span></div>'
            f'<ol class="here-pi">{"".join(segs)}</ol>'
            f'<span class="here-range" data-here-range>{pick(wtext(f"{it['label']} W{week}", monday, now), True)}</span>'
            f'</div>'
            f'<div class="here-tile" data-it="{it_key(it)}" tabindex="0"><small>Итерация · неделя {week} из {it["weeks"]}</small><div class="here-head"><strong>{it["label"]} · {it["title"]}</strong><span>{span(it["start"], it["end"])}</span></div>'
            f'<ol class="here-weeks">{"".join(weeks)}</ol><span class="here-range" data-here-range>{pick(wtext(f"W{week}", monday, now), True)}</span></div>')


def cls(*names):
    names = [n for n in names if n]
    return f' class="{" ".join(names)}"' if names else ''


def it_key(i):
    return f'{i["year"]}-{i["month"]:02d}'


def plural(n, forms):
    """Russian noun form for a count: (one, few, many)."""
    k = n % 100
    return forms[2] if 11 <= k <= 14 else forms[0] if n % 10 == 1 else forms[1] if 2 <= n % 10 <= 4 else forms[2]


# START_CONTRACT: plan_status
#   PURPOSE: One line on where the plan stands today: the PI, iteration and week, the work in this iteration and without one, the next Review and Planning.
#   INPUTS: { day: date; rows: list - see board_html }
#   OUTPUTS: { str - plain text; site.js writes the same line for the reader's date }
#   SIDE_EFFECTS: none
# END_CONTRACT: plan_status
def plan_status(day, rows):
    it, week = week_of(day)
    monday = day - timedelta(days=day.weekday())
    here = f'{it["pi"]} {it["name"]}'
    items = [x for r in rows for x in r['items'] if x['state'] != 'Завершено']
    planned = sum(1 for x in items if x.get('iteration') == here)
    loose = sum(1 for x in items if not x.get('iteration'))
    nxt = {}
    for k in range(30):
        s = monday + timedelta(weeks=k)
        i, w = week_of(s)
        kind = week_kind(i, w, increment(i['year'], (i['month'] - 1) // 3 + 1)['ip']['name'])
        if kind and kind not in nxt:
            nxt[kind] = week_range(s, kind) + (' (эта неделя)' if k == 0 else '')
    return (f'Сейчас {it["pi"]}, итерация {it["label"]} ({it["title"]}), неделя {week} из {it["weeks"]}. '
            f'В этой итерации {planned} {plural(planned, ("работа", "работы", "работ"))}, без итерации — {loose}. '
            f'Ближайшая Review — {nxt.get("review", "—")}, Planning — {nxt.get("ip", "—")}.')


def item_html(item):
    return (f'<a class="pi-item pi-item--{STATE_CLASS.get(item["state"], "backlog")}" href="{esc(item["href"])}" data-item="{esc(item["id"])}" title="{esc(item["title"])} · {esc(item["state"])}">'
            f'<b>{esc(item["id"])}</b><span>{esc(item["title"])}</span></a>')


STATE_CLASS = {'Бэклог': 'backlog', 'Готово к работе': 'ready', 'В работе': 'doing', 'На проверке': 'review', 'Завершено': 'done'}


# START_CONTRACT: board_html
#   PURPOSE: The work of each project placed in the iterations of one increment, with what is not yet planned.
#   INPUTS: { pi: dict - the increment shown; it: dict - today's iteration; sel: dict - the selected iteration; rows: list - {id, title, href, find, function, area, items: [{id, title, state, iteration, href}]} }
#   OUTPUTS: { str - HTML table }
#   SIDE_EFFECTS: none
# END_CONTRACT: board_html
def board_html(pi, it, sel, rows):
    names = [f'{pi["name"]} {i["name"]}' for i in pi['iterations']]
    head = ''.join(f'<th{cls("is-current" if it_key(i) == it_key(it) else "", "is-selected" if it_key(i) == it_key(sel) else "")} data-it="{it_key(i)}" tabindex="0">'
                   f'<b>{i["label"]}</b> {i["title"]}<small>{span(i["start"], i["end"])}</small></th>' for i in pi['iterations'])
    body = []
    for row in rows:
        cells = [[x for x in row['items'] if x.get('iteration') == n] for n in names]
        loose = [x for x in row['items'] if not x.get('iteration') and x['state'] != 'Завершено']
        if not any(cells) and not loose:
            continue
        body.append(f'<tr data-kb-row data-find="{esc(row["find"])}" data-function="{esc(row["function"])}" data-area="{esc(row["area"])}">'
                    f'<th scope="row"><a href="{esc(row["href"])}">{esc(row["id"])}</a><span>{esc(row["title"])}</span></th>'
                    + ''.join(f'<td{cls("is-selected" if it_key(i) == it_key(sel) else "")}>{"".join(item_html(x) for x in c)}</td>' for i, c in zip(pi['iterations'], cells))
                    + f'<td class="pi-loose">{"".join(item_html(x) for x in loose)}</td></tr>')
    if not body:
        body.append('<tr><td colspan="5" class="pi-empty">В этом PI работы не запланировано.</td></tr>')
    return (f'<div class="o-table-wrap pi-board-wrap"><table class="pi-board"><thead><tr><th>Проект</th>{head}<th>Не запланировано</th></tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div>')


# START_CONTRACT: calendar_html
#   PURPOSE: The PI calendar as of a date: the current week, three increments from a shift with their iterations and IP weeks, the weeks of the selected iteration, and the work of the first increment by iteration.
#   INPUTS: { day: date; shift: int - increments to move the three-increment window; rows: list - see board_html }
#   OUTPUTS: { str - HTML; site.js renders the same markup for the reader's own date with the same rules, and moves the selection on click }
#   SIDE_EFFECTS: none
# END_CONTRACT: calendar_html
def calendar_html(day, shift=0, rows=()):
    r = rolling(day, 1)
    it, week = r['iteration'], r['week']
    year, quarter = it['year'], (it['month'] - 1) // 3 + 1
    q = year * 4 + quarter - 1 + shift
    pis = [increment((q + k) // 4, (q + k) % 4 + 1) for k in range(3)]
    shown = pis[0]
    sel = it if it['pi'] == shown['name'] else shown['iterations'][0]
    monday = it['start'] + timedelta(weeks=week - 1)
    note = f'<span class="pi-note">{esc(r["note"])}</span>' if r['note'] else ''
    out = [f'<div class="pi-bar"><div class="pi-now" data-week="{monday.isoformat()}" tabindex="0"><span class="pi-now__label">Сейчас</span>'
           f'<strong>{it["pi"]} · {it["label"]} · неделя {week} из {it["weeks"]}</strong><span>{span(monday, monday + timedelta(days=6))}</span>{note}</div>'
           '<div class="pi-nav"><button type="button" data-pi-step="-1" aria-label="Предыдущий PI">‹</button>'
           '<button type="button" data-pi-step="0">Сегодня</button><button type="button" data-pi-step="1" aria-label="Следующий PI">›</button></div></div><div class="pi-row">']
    for pi in pis:
        total = (pi['end'] - pi['start']).days + 1
        done = max(0, min(total, (day - pi['start']).days + 1))
        pct = 100 * done // total
        state = 'идёт' if pi['name'] == it['pi'] else ('завершён' if done == total else 'впереди')
        its = ''.join(f'<li{cls("is-current" if it_key(i) == it_key(it) else "", "is-selected" if it_key(i) == it_key(sel) else "")} data-it="{it_key(i)}" tabindex="0"><b>{i["label"]}</b><em>{i["title"]}</em>'
                      f'<span>{span(i["start"], i["end"])} · {i["weeks"]} нед.</span></li>' for i in pi['iterations'])
        out.append(f'<article{cls("pi-card", "is-current" if pi["name"] == it["pi"] else "", "is-selected" if pi["name"] == shown["name"] else "")} data-pi="{pi["name"]}" tabindex="0">'
                   f'<header><strong>{pi["name"]}</strong><small>{state}</small></header><span class="pi-dates">{span(pi["start"], pi["end"])}</span>'
                   f'<div class="pi-progress" title="Пройдено {pct}%"><span style="width:{pct}%"></span></div>'
                   f'<ol class="pi-its">{its}</ol><p class="pi-ip"><b>Planning</b> {span(pi["ip"]["start"], pi["ip"]["end"])}</p></article>')
    out.append('</div>')
    ip = shown['ip']['name']
    weeks = []
    for w in range(1, sel['weeks'] + 1):
        start = sel['start'] + timedelta(weeks=w - 1)
        name = f'{sel["pi"]} {sel["name"]}W{w}'
        text = week_note(start)
        weeks.append(f'<li{cls("is-current" if start == monday else "", "is-ip" if name == ip else "", "is-review" if week_kind(sel, w, ip) == "review" else "")} data-week="{start.isoformat()}" tabindex="0"><b>W{w}</b>'
                     f'<span>{span(start, start + timedelta(days=6))}</span>{f"<small>{esc(text.split(chr(59))[0])}</small>" if text else ""}</li>')
    out.append(f'<div class="pi-weeks"><span class="pi-weeks__label">Недели итерации {sel["label"]} ({sel["title"]})</span><ol>{"".join(weeks)}</ol></div>'
               f'<h3 class="pi-board-title">Работа по итерациям {shown["name"]}</h3>{board_html(shown, it, sel, rows)}')
    return ''.join(out)
