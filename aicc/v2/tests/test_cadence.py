"""PI calendar: the rules give the dates of the agreed calendar, and the page script draws the same calendar as the build."""
from datetime import date, timedelta
import json
from pathlib import Path
import shutil
import subprocess
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import cadence

SITE_JS = Path(__file__).resolve().parents[1] / 'site.js'


class Rules(unittest.TestCase):
    def test_iterations_match_the_agreed_calendar(self):
        # name, start, end, weeks
        agreed = [((2026, 10), date(2026, 9, 28), date(2026, 11, 1), 5), ((2026, 11), date(2026, 11, 2), date(2026, 11, 29), 4),
                  ((2026, 12), date(2026, 11, 30), date(2027, 1, 3), 5), ((2027, 1), date(2027, 1, 4), date(2027, 1, 31), 4),
                  ((2027, 9), date(2027, 8, 30), date(2027, 10, 3), 5)]
        for (year, month), start, end, weeks in agreed:
            it = cadence.iteration(year, month)
            self.assertEqual((it['start'], it['end'], it['weeks']), (start, end, weeks), it['name'])

    def test_iterations_tile_the_years_without_gaps(self):
        prev = cadence.iteration(2025, 1)
        for k in range(1, 72):
            it = cadence.iteration(2025 + k // 12, k % 12 + 1)
            self.assertEqual(it['start'], prev['end'] + timedelta(days=1))
            self.assertEqual(it['start'].weekday(), 0)
            self.assertIn(it['weeks'], (4, 5))
            prev = it

    def test_the_current_week_and_increment(self):
        r = cadence.rolling(date(2026, 10, 8))
        self.assertEqual(r['week_name'], '2026-PIQ4 I10W2')
        self.assertEqual([p['name'] for p in r['increments']], ['2026-PIQ4', '2027-PIQ1', '2027-PIQ2'])
        self.assertEqual(cadence.week_of(date(2027, 1, 1))[0]['name'], 'I12')  # the week of New Year belongs to December
        self.assertEqual(cadence.increment(2026, 4)['ip']['start'], date(2026, 12, 21))


@unittest.skipUnless(shutil.which('node'), 'node is not installed')
class PageScript(unittest.TestCase):
    def test_the_script_draws_what_the_build_draws(self):
        text = SITE_JS.read_text(encoding='utf-8')
        block = text[text.index('var PI = (function'):text.index('window.HubPI')]
        days = [date(2026, 9, 27) + timedelta(days=9 * k) for k in range(90)]
        rows = [{'id': 'INI-001', 'title': 'Проект <первый>', 'href': '../ini-001/', 'find': 'ini-001', 'function': 'HR', 'area': 'Услуга "А"',
                 'items': [{'id': 'FEAT-001', 'title': 'Отчёт', 'state': 'В работе', 'iteration': '2026-PIQ4 I11', 'href': '../ini-001/'},
                           {'id': 'FEAT-002', 'title': 'Форма', 'state': 'Бэклог', 'iteration': '', 'href': '../ini-001/'},
                           {'id': 'FEAT-003', 'title': 'Сверка', 'state': 'Завершено', 'iteration': '2027-PIQ1 I02', 'href': '../ini-001/'}]},
                {'id': 'INI-002', 'title': 'Второй', 'href': '../ini-002/', 'find': 'ini-002', 'function': '', 'area': '',
                 'items': [{'id': 'FEAT-004', 'title': 'Готово', 'state': 'Завершено', 'iteration': '', 'href': '../ini-002/'}]}]
        data = {'ip_weeks': cadence.DATA['ip_weeks'], 'notes': cadence.DATA['notes'], 'rows': rows}
        program = block + (f'Object.assign(PI.data, {json.dumps(data, ensure_ascii=False)});'
                           f'var days = {json.dumps([d.isoformat() for d in days])};'
                           'var out = []; days.forEach(function (s) { var p = s.split("-").map(Number), t = PI.at(p[0], p[1], p[2]);'
                           '[-1, 0, 2].forEach(function (k) { out.push(PI.calendar(t, k)); }); out.push(PI.here(t)); });'
                           'process.stdout.write(JSON.stringify(out));')
        got = json.loads(subprocess.run(['node', '-e', program], capture_output=True, text=True, check=True).stdout)
        want = [x for d in days for x in [cadence.calendar_html(d, k, rows) for k in (-1, 0, 2)] + [cadence.here_html(d)]]
        self.assertIn('FEAT-001', cadence.calendar_html(date(2026, 10, 8), 0, rows))  # planned in I11 of the current PI
        self.assertNotIn('FEAT-004', ''.join(want))  # done and never planned: shown nowhere
        for g, w in zip(got, want):
            self.assertEqual(g, w)
        self.assertEqual(len(got), len(want))


if __name__ == '__main__':
    unittest.main()
