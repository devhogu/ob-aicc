"""Observable portfolio rules, source disagreements and public projection boundaries."""
from pathlib import Path
import json
import shutil
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import portfolio


class PortfolioRules(unittest.TestCase):
    def test_waiting_retains_column_and_active_capacity(self):
        rows = [{'state':'Waiting', 'stage':'MVP', 'standing':False, 'waiting_from':'Active'},
                {'state':'Active', 'stage':'Implementation', 'standing':False},
                {'state':'Active', 'standing':True}]
        self.assertEqual(portfolio.position('Waiting','MVP',waiting_from='Active',dependency='DEP-X'), 'MVP')
        self.assertEqual(portfolio.position('Waiting','Business case',waiting_from='Discovery',dependency='DEP-Y'), 'Analyzing')
        self.assertEqual(portfolio.capacity(rows,{'initiative':1})['active'],2)
        self.assertRaises(ValueError,portfolio.position,'Waiting','MVP')

    def test_done_keeps_review_and_terminal_exits_separate(self):
        for state in ('Review','Accepted','Closed'):
            self.assertEqual(portfolio.position(state), 'Done')
        for state in ('Deferred','Rejected','Pivoted','Cancelled'):
            self.assertEqual(portfolio.position(state), 'Off-flow')
        self.assertEqual(portfolio.position('Proposed'),'Funnel')
        self.assertEqual(portfolio.position('Approved'),'Portfolio Backlog')
        self.assertRaises(ValueError,portfolio.position,'Active','Scoping')

    def test_delivery_capacity_includes_review_completed_and_waiting(self):
        features = [{'State':'Active'}, {'State':'Completed'}, {'State':'Review'},
                    {'State':'Waiting','Waiting from':'Active'}, {'State':'Waiting','Waiting from':'Approved'},
                    {'State':'Approved'}, {'State':'Accepted'}]
        c = portfolio.capacity([],{'initiative':1},features)
        # A Waiting Feature keeps its column, so Waiting after Approved still occupies Ready.
        self.assertEqual(c['feature'],{'progress':4,'ready':2})
        self.assertEqual(c['active'],0)
        # A Completed Initiative stays in Implementation and keeps its place until Review.
        self.assertEqual(portfolio.capacity([{'state':'Completed','standing':False},{'state':'Review','standing':False}],{'initiative':1})['active'],1)

    def test_dates_and_scores_read_in_the_language_of_the_edition(self):
        self.assertEqual(portfolio._date('ru','2026-10-03'),'3 октября 2026 года')
        self.assertEqual(portfolio._date('en','2026-12-23'),'23 December 2026')
        self.assertEqual(portfolio._decimal('ru',3.75),'3,75')
        self.assertEqual(portfolio._decimal('en',4.0),'4')

    def test_actual_record_identities_rank_and_unknown_dates_in_both_editions(self):
        expected = ['INI-002','INI-006','INI-004','INI-003','INI-007','INI-008','INI-013','INI-009','INI-010','INI-011','INI-012']
        for lang in ('en','ru'):
            d = portfolio.project(lang=lang)
            self.assertEqual([x['id'] for x in d['items']], expected)
            self.assertEqual(d['date'],'2026-10-06')
            self.assertEqual(d['counts']['Reviewing'],6)
            self.assertEqual(d['capacity']['active'],0)
            self.assertEqual(d['capacity']['limit'],1)
            ordinary = [x for x in d['items'] if not x['standing']]
            self.assertEqual([x['rank'] for x in ordinary],[1,2,3,4,5,6,None])
            # Scored order is different; the first-100-days order must survive.
            self.assertGreater(ordinary[2]['wsjf'], ordinary[0]['wsjf'])
            self.assertTrue(all(x['stage_entered'] is None and x['approval_ref'] is None for x in ordinary[:6]))
            self.assertEqual([x['state'] for x in d['items'][7:]],['Approved']*4)
            self.assertEqual(d['features'],0)
            proposed = next(x for x in d['items'] if x['id']=='INI-013')
            self.assertEqual(proposed['column'],'Funnel')
            self.assertEqual(proposed['stage_entered'],'2026-10-06')
            self.assertIsNone(proposed['goal_confirmation'])
            self.assertIsNone(proposed['approval_ref'])
            self.assertIsNone(proposed['wsjf'])
            self.assertTrue(any(r['Value']=='' for r in d['measures']))
            self.assertEqual(len(d['milestones']),13)
            public = json.dumps(d,ensure_ascii=False)
            self.assertNotIn('Moldogazieva',public);self.assertNotIn('Молдогазиева',public)
            self.assertEqual(next(x for x in d['items'] if x['id']=='INI-004')['owner'], 'Head of the FP&A function' if lang=='en' else 'Руководитель подразделения FP&A')

    def test_record_disagreement_prevents_a_misleading_dashboard(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); shutil.copytree(portfolio.workspace.ROOT/'portfolio/en',root/'portfolio/en');shutil.copytree(portfolio.workspace.ROOT/'registry/en',root/'registry/en')
            path = root/'portfolio/en/portfolio-backlog.md'
            path.write_text(path.read_text().replace('| Discovery | Scoping |','| Approved |  |',1))
            with self.assertRaisesRegex(ValueError,'state disagreement'):
                portfolio.project(root)

    def test_changed_recorded_limits_and_snapshot_counts_are_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp);shutil.copytree(portfolio.workspace.ROOT/'portfolio/en',root/'portfolio/en');shutil.copytree(portfolio.workspace.ROOT/'registry/en',root/'registry/en')
            path = root/'portfolio/en/board.md'
            path.write_text(path.read_text().replace('Shared Active limit: 1','Shared Active limit: 2'))
            snapshot = root/'portfolio/en/dashboard.md'
            snapshot.write_text(snapshot.read_text().replace('1 shared Active','2 shared Active'))
            self.assertEqual(portfolio.project(root)['capacity']['limit'],2)
            path=root/'portfolio/en/dashboard.md'
            path.write_text(path.read_text().replace('| Items | 1 | 6 |','| Items | 1 | 5 |',1))
            with self.assertRaisesRegex(ValueError,'count disagreement'):
                portfolio.project(root)


if __name__=='__main__': unittest.main()
