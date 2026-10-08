"""Protect the real Kanban consumers and production/fixture boundary."""
from html.parser import HTMLParser
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import delivery
import portfolio


class Cards(HTMLParser):
    def __init__(self,text):
        super().__init__();self.cards=[];self.templates=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'data-kb-open' in a:self.cards.append(a)
        if 'data-kb-detail' in a:self.templates.append(a['data-kb-detail'])


class SharedKanban(unittest.TestCase):
    def test_actual_portfolio_has_native_compact_cards_and_matching_details(self):
        for lang in ('en','ru'):
            text=portfolio.render(portfolio.project(lang=lang),f'/{lang}/portfolio/')
            parsed=Cards(text)
            self.assertEqual(len(parsed.cards),18) # 7 board + 7 review + 4 Standing
            self.assertEqual(len(parsed.templates),11)
            self.assertEqual(set(c['data-kb-open'] for c in parsed.cards),set(parsed.templates))
            self.assertTrue(all(c['href'].startswith('ini-') for c in parsed.cards))
            self.assertNotIn('<dialog',text)
            self.assertNotIn('DR-2026-',text)
            self.assertIn('service-resolution/',text)

    def test_production_delivery_has_no_demo_cards_but_keeps_intake_documents(self):
        for lang in ('en','ru'):
            text=delivery.render(delivery.project(lang=lang),f'/{lang}/program/')
            self.assertEqual(Cards(text).cards,[])
            self.assertIn('INI-013',text)
            self.assertIn('data-dl-panel',text)
            self.assertIn('kb-table',text)
            self.assertNotIn('Preview A',text)

    def test_nonempty_waiting_delivery_uses_same_summary_path_with_real_goal(self):
        data=delivery.project();parent=next(i for i in data['portfolio']['items'] if i['id']=='INI-009')
        row={'Identifier':'FEAT-001','kind':'Feature','title':'Verified case history','initiative':'INI-009','State':'Waiting','status':'Waiting','column':'Active','Lane':'Normal','stage_label':'Develop','rank':1,'approval':'2026-10-06','accepted':'','criteria':'Given a permitted case, show source-linked history','dependencies':['DEP-014'],'Waiting Dependency':'DEP-014','Parent: Capability or Standing Initiative':'INI-009'}
        data['items']=[row];data['counts']['Active']=1
        text=delivery.render(data,'/en/program/');parsed=Cards(text)
        self.assertEqual(parsed.cards[0]['href'],'items/feat-001/')
        self.assertEqual(parsed.templates,['FEAT-001'])
        self.assertIn(parent['outcome'],text)
        self.assertIn('DEP-014',text)
        self.assertIn('Next decision',text)
        self.assertIn(row['criteria'],text)


if __name__=='__main__':unittest.main()
