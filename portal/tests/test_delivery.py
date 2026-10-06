"""Delivery admission and visible state, derived from the governing lifecycle rules."""
from pathlib import Path
import sys
import shutil
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import delivery
import portfolio


class ProgramDelivery(unittest.TestCase):
    def setUp(self):
        self.standing={'id':'INI-009','standing':True,'state':'Approved','approval_ref':'DR-2026-063'}
        self.ordinary={'id':'INI-013','standing':False,'state':'Proposed','approval_ref':None,'continuation_ref':None}

    def feature(self,identifier='FEAT-001',state='Proposed',**fields):
        return {'Identifier':identifier,'Feature':'Verified case history','Parent: Capability or Standing Initiative':'INI-009',
                'Lane':'Normal','State':state,'Stage':'','Rank':'','Acceptance criteria and Dependencies':'Given a permitted case, when opened, then show source-linked history; DEP-016',
                'Data-use approval reference':'No AI data use in this fixture','Approved by and date':'2026-10-06',
                'Accepted by and date':'','Waiting from':'','Waiting Dependency':'',**fields}

    def test_proposal_is_portfolio_intake_not_a_delivery_admission(self):
        for lang in ('en','ru'):
            data=delivery.project(lang=lang)
            self.assertEqual(data['items'],[])
            self.assertEqual(data['counts'],{'Backlog':0,'Ready':0,'Active':0,'Review':0,'Done':0})
            proposal=next(i for i in data['portfolio']['items'] if i['id']=='INI-013')
            self.assertEqual((proposal['state'],proposal['column'],proposal['project_key']),('Proposed','Funnel','service-resolution'))
            self.assertIsNone(proposal['approval_ref']);self.assertIsNone(proposal['rank'])
            funnel = next(r for r in data['portfolio']['measures'] if r['Flow Measure'].startswith(('Funnel:', 'Фаннел:')))
            self.assertIn('1 ',funnel['Value'])
            self.assertIn('2026-10-06',funnel['Value'])
            self.assertEqual(data['portfolio']['capacity']['feature'],{'progress':0,'ready':0})

    def test_model_mapping_distinguishes_completed_review_and_acceptance(self):
        expected={'Proposed':'Backlog','Discovery':'Backlog','Deferred':'Backlog','Approved':'Ready','Active':'Active','Completed':'Active','Review':'Review','Accepted':'Done','Closed':'Done','Rejected':'Off-flow','Pivoted':'Off-flow'}
        for state,column in expected.items():self.assertEqual(delivery.position(state),column)
        self.assertEqual(delivery.position('Waiting','Approved','DEP-016'),'Ready')
        self.assertEqual(delivery.position('Waiting','Review','DEP-016'),'Review')
        self.assertRaises(ValueError,delivery.position,'Waiting','Active','')

    def test_ordinary_work_cannot_bypass_the_mvp_continue_decision(self):
        cap={'Identifier':'CAP-001','Capability':'Resolve payment issues','Initiative':'INI-013','Solution':'SOL-002','Lane':'Normal','State':'Proposed','Stage':'','Rank':''}
        with self.assertRaisesRegex(ValueError,'continue decision'):delivery.validate([cap],[],[self.ordinary],{})
        parent={**self.ordinary,'continuation_ref':'DR-2026-070','state':'Active'}
        items=delivery.validate([cap],[],[parent],{})
        self.assertEqual(items[0]['column'],'Backlog')
        wrong=self.feature(**{'Parent: Capability or Standing Initiative':'INI-013'})
        with self.assertRaisesRegex(ValueError,'parent must'):delivery.validate([], [wrong],[parent],{'DEP-016':{}})

    def test_runrate_uses_approved_standing_parent_and_each_admission(self):
        bad={**self.standing,'approval_ref':None}
        with self.assertRaisesRegex(ValueError,'Standing Brief'):delivery.validate([],[self.feature()],[bad],{'DEP-016':{}})
        missing=self.feature(state='Approved',**{'Approved by and date':''})
        with self.assertRaisesRegex(ValueError,'admission record'):delivery.validate([],[missing],[self.standing],{'DEP-016':{}})
        rows=delivery.validate([],[self.feature(state='Approved')],[self.standing],{'DEP-016':{}})
        self.assertEqual((rows[0]['column'],rows[0]['initiative']),('Ready','INI-009'))

    def test_waiting_after_start_keeps_shared_capacity_and_known_dependency(self):
        rows=[self.feature('FEAT-001','Completed'),self.feature('FEAT-002','Review'),
              self.feature('FEAT-003','Waiting',**{'Waiting from':'Active','Waiting Dependency':'DEP-016','Stage':'Develop'}),
              self.feature('FEAT-004','Waiting',**{'Waiting from':'Approved','Waiting Dependency':'DEP-016'})]
        items=delivery.validate([],rows,[self.standing],{'DEP-016':{}})
        self.assertEqual([r['column'] for r in items],['Active','Review','Active','Ready'])
        self.assertEqual(portfolio.capacity([],{'initiative':1},rows)['feature']['progress'],3)
        with self.assertRaisesRegex(ValueError,'Unknown Program Dependency'):delivery.validate([],rows,[self.standing],{})

    def test_nonempty_maintained_record_reaches_its_real_board_card(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);shutil.copytree(delivery.workspace.ROOT/'registry/en',root/'registry/en')
            path=root/'registry/en/program-backlog.md';text=path.read_text()
            row=self.feature();row['Rank']='1';row['Acceptance criteria and Dependencies']=row['Acceptance criteria and Dependencies'].replace('DEP-016','DEP-014')
            header=next(line for line in text.splitlines() if line.startswith('| Rank | Identifier | Feature'))
            fields=[x.strip() for x in header.strip('|').split('|')]
            # Insert after the empty Feature table separator, as a real maintained row.
            index=text.index(header);end=text.index('\n',text.index('\n',index)+1)
            text=text[:end]+'\n| '+' | '.join(str(row.get(k,'')) for k in fields)+' |'+text[end:]
            path.write_text(text)
            path=root/'registry/en/dashboard.md';path.write_text(path.read_text().replace('| Items | 0 | 0 | 0 | 0 | 0 | 0 |','| Items | 1 | 0 | 0 | 0 | 0 | 0 |'))
            path=root/'registry/en/board.md';path.write_text(path.read_text().replace('| Normal | | | | | |','| Normal | FEAT-001 | | | | |'))
            data=delivery.project(root)
            self.assertEqual(data['counts']['Backlog'],1)
            self.assertEqual(data['items'][0]['initiative'],'INI-009')
            markup=delivery.render(data,'/en/projects/')
            self.assertIn('href="items/feat-001/"',markup)
            self.assertIn('Verified case history',markup)
            path=root/'registry/en/dashboard.md';path.write_text(path.read_text().replace('| Items | 1 | 0 | 0 | 0 | 0 | 0 |','| Items | 2 | 0 | 0 | 0 | 0 | 0 |'))
            with self.assertRaisesRegex(ValueError,'count disagreement'):delivery.project(root)

    def test_accepted_requires_evidence_and_active_requires_valid_stage(self):
        with self.assertRaisesRegex(ValueError,'acceptance record'):delivery.validate([],[self.feature(state='Accepted')],[self.standing],{'DEP-016':{}})
        with self.assertRaisesRegex(ValueError,'Active Stage'):delivery.validate([],[self.feature(state='Active',Stage='Scoping')],[self.standing],{'DEP-016':{}})
        row=self.feature(state='Accepted',**{'Accepted by and date':'2026-10-07'})
        self.assertEqual(delivery.validate([],[row],[self.standing],{'DEP-016':{}})[0]['column'],'Done')


if __name__=='__main__':unittest.main()
