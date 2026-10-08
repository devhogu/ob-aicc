# START_MODULE_CONTRACT
#   PURPOSE: The PI calendar: from any date, the current program increment, its iterations with real dates, the current iteration and week, and the next increments.
#   SCOPE: Pure date arithmetic on the calendar rules plus the known week notes in aicc/v2/calendar.json. The page script applies the same rules to today's date.
#   DEPENDS: none
#   LINKS: C-HUB-V2, M-HUB-V2-BUILD
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
    return {'name': f'I{month:02d}', 'month': month, 'year': year, 'pi': f'{year}-PIQ{(month - 1) // 3 + 1}',
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


def increment(year, quarter):
    its = [iteration(year, 3 * (quarter - 1) + k) for k in (1, 2, 3)]
    name = f'{year}-PIQ{quarter}'
    last = its[-1]
    ip_week = last['weeks'] - 1 if last['month'] == 12 and last['weeks'] == 5 else last['weeks']
    known = DATA['ip_weeks'].get(name)
    if known:
        ip_week = int(known.rsplit('W', 1)[1])
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
    return {'today': day, 'iteration': it, 'week': week, 'week_name': name, 'note': DATA['notes'].get(name, ''), 'increments': pis}


SHORT = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
LONG = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']


def esc(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def span(a, b, long=False):
    names = LONG if long else SHORT
    left = f'{a.day} {names[a.month - 1]}' + (f' {a.year}' if a.year != b.year else '')
    return f'{left} – {b.day} {names[b.month - 1]} {b.year}'


DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']


# START_CONTRACT: here_html
#   PURPOSE: Where we are in time: today, the current increment with its progress and IP week, the current iteration with its weeks.
#   INPUTS: { day: date }
#   OUTPUTS: { str - HTML of three tiles; site.js draws the same tiles for the reader's date }
#   SIDE_EFFECTS: none
# END_CONTRACT: here_html
def short(a, b):
    return f'{a.day} {SHORT[a.month - 1]} – {b.day} {SHORT[b.month - 1]}'


IP_TIP = ('Неделя инноваций и планирования. Это последняя рабочая неделя PI, отдельной итерацией она не считается: '
          'ревью и демонстрация третьей итерации, итоги PI, планирование следующего PI, время на инновации и обучение. Новую работу в эту неделю не берут.')


def ip_tip(pi):
    return f'<span class="here-tip" role="tooltip"><b>Неделя IP · {span(pi["ip"]["start"], pi["ip"]["end"])}</b>{IP_TIP}</span>'


def here_html(day):
    r = rolling(day, 1)
    pi, it, week = r['increments'][0], r['iteration'], r['week']
    monday = day - timedelta(days=day.weekday())
    pi_weeks = ((pi['end'] - pi['start']).days + 1) // 7
    pi_week = (monday - pi['start']).days // 7 + 1
    ip = pi['ip']['name']
    segs = []
    for i in pi['iterations']:
        cells = ''.join(
            f'<i{cls("is-done" if s < monday else "is-current" if s == monday else "", "is-ip" if n == ip else "")}{" tabindex=\"0\"" if n == ip else ""}>{ip_tip(pi) if n == ip else ""}</i>'
            for s, n in ((i['start'] + timedelta(weeks=w - 1), f'{i["pi"]} {i["name"]}W{w}') for w in range(1, i['weeks'] + 1)))
        segs.append(f'<li{cls("is-current" if it_key(i) == it_key(it) else "", "is-done" if i["end"] < monday else "")} style="flex:{i["weeks"]}">'
                    f'<span class="here-cells">{cells}</span><b>{i["name"]} · {i["title"]}</b><span>{short(i["start"], i["end"])}</span></li>')
    weeks = []
    for w in range(1, it['weeks'] + 1):
        s = it['start'] + timedelta(weeks=w - 1)
        n = f'{it["pi"]} {it["name"]}W{w}'
        weeks.append(f'<li><button type="button"{cls("is-done" if w < week else "is-current" if w == week else "", "is-ip" if n == ip else "", "is-picked" if w == week else "")} '
                     f'data-here-week data-range="W{w} · {span(s, s + timedelta(days=6))}{" · сейчас" if w == week else ""}" data-note="{esc(DATA["notes"].get(n, ""))}">W{w}</button></li>')
    note = r['note']
    return (f'<div class="here-tile" data-week="{monday.isoformat()}" tabindex="0"><small>Сегодня</small><strong>{day.day} {LONG[day.month - 1]} {day.year}</strong><span>{DAYS[day.weekday()]}</span></div>'
            f'<div class="here-tile" data-pi="{pi["name"]}" tabindex="0"><small>Программный инкремент · неделя {pi_week} из {pi_weeks}</small><div class="here-head"><strong>PI {pi["name"]}</strong><span>{span(pi["start"], pi["end"])}</span></div>'
            f'<ol class="here-pi">{"".join(segs)}</ol>'
            f'<span class="here-ip" tabindex="0"><i></i>Неделя IP · {span(pi["ip"]["start"], pi["ip"]["end"])}{ip_tip(pi)}</span></div>'
            f'<div class="here-tile" data-it="{it_key(it)}" tabindex="0"><small>Итерация · неделя {week} из {it["weeks"]}</small><div class="here-head"><strong>{it["name"]} · {it["title"]}</strong><span>{span(it["start"], it["end"])}</span></div>'
            f'<ol class="here-weeks">{"".join(weeks)}</ol><span class="here-range" data-here-range>W{week} · {span(monday, monday + timedelta(days=6))} · сейчас</span>'
            f'<span class="here-note" data-here-note{"" if note else " hidden"}>{esc(note)}</span></div>')


def cls(*names):
    names = [n for n in names if n]
    return f' class="{" ".join(names)}"' if names else ''


def it_key(i):
    return f'{i["year"]}-{i["month"]:02d}'


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
                   f'<b>{i["name"]}</b> {i["title"]}<small>{span(i["start"], i["end"])}</small></th>' for i in pi['iterations'])
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
           f'<strong>{it["pi"]} · {it["name"]} · неделя {week} из {it["weeks"]}</strong><span>{span(monday, monday + timedelta(days=6))}</span>{note}</div>'
           '<div class="pi-nav"><button type="button" data-pi-step="-1" aria-label="Предыдущий PI">‹</button>'
           '<button type="button" data-pi-step="0">Сегодня</button><button type="button" data-pi-step="1" aria-label="Следующий PI">›</button></div></div><div class="pi-row">']
    for pi in pis:
        total = (pi['end'] - pi['start']).days + 1
        done = max(0, min(total, (day - pi['start']).days + 1))
        pct = 100 * done // total
        state = 'идёт' if pi['name'] == it['pi'] else ('завершён' if done == total else 'впереди')
        its = ''.join(f'<li{cls("is-current" if it_key(i) == it_key(it) else "", "is-selected" if it_key(i) == it_key(sel) else "")} data-it="{it_key(i)}" tabindex="0"><b>{i["name"]}</b><em>{i["title"]}</em>'
                      f'<span>{span(i["start"], i["end"])} · {i["weeks"]} нед.</span></li>' for i in pi['iterations'])
        out.append(f'<article{cls("pi-card", "is-current" if pi["name"] == it["pi"] else "", "is-selected" if pi["name"] == shown["name"] else "")} data-pi="{pi["name"]}" tabindex="0">'
                   f'<header><strong>{pi["name"]}</strong><small>{state}</small></header><span class="pi-dates">{span(pi["start"], pi["end"])}</span>'
                   f'<div class="pi-progress" title="Пройдено {pct}%"><span style="width:{pct}%"></span></div>'
                   f'<ol class="pi-its">{its}</ol><p class="pi-ip"><b>Неделя IP</b> {span(pi["ip"]["start"], pi["ip"]["end"])}</p></article>')
    out.append('</div>')
    ip = shown['ip']['name']
    weeks = []
    for w in range(1, sel['weeks'] + 1):
        start = sel['start'] + timedelta(weeks=w - 1)
        name = f'{sel["pi"]} {sel["name"]}W{w}'
        text = DATA['notes'].get(name, '')
        weeks.append(f'<li{cls("is-current" if start == monday else "", "is-ip" if name == ip else "")} data-week="{start.isoformat()}" tabindex="0"><b>W{w}</b>'
                     f'<span>{span(start, start + timedelta(days=6))}</span>{f"<small>{esc(text.split(chr(59))[0])}</small>" if text else ""}</li>')
    out.append(f'<div class="pi-weeks"><span class="pi-weeks__label">Недели итерации {sel["name"]} ({sel["title"]}) · нажмите на неделю, итерацию или PI, чтобы открыть подробности</span><ol>{"".join(weeks)}</ol></div>'
               f'<h3 class="pi-board-title">Работа по итерациям {shown["name"]}</h3>{board_html(shown, it, sel, rows)}')
    return ''.join(out)
