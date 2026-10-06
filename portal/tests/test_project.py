"""Protect actual document links, source preservation and failure detection."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import project
from check_project import Capture


class ProjectPromotion(unittest.TestCase):
    def test_charter_links_reach_real_journey_and_technical_pages(self):
        docs, owners = project.documents('en')
        charter = next(d for d in docs if d['key'] == 'charter')
        rendered = project.render(charter, docs, owners, 'en')
        self.assertIn('href="../journeys/#en-journeys"', rendered)
        self.assertIn('href="../technical-design/#en-technical-design"', rendered)
        self.assertIn('id="en-charter-hypothesis"', rendered)
        self.assertNotIn('href="#en-technical-design"', rendered)
        self.assertIn("The project's single acceptance rule is on ", rendered)

    def test_source_checker_detects_dropped_cell_and_changed_diagram_relationship(self):
        docs, owners = project.documents('en')
        case = next(d for d in docs if d['key'] == 'charter')
        rendered = project.render(case, docs, owners, 'en')
        baseline = Capture(case['body']).documents[case['id']]
        self.assertEqual(baseline['atoms'], Capture(rendered).documents[case['id']]['atoms'])
        self.assertEqual(baseline['diagrams'], Capture(rendered).documents[case['id']]['diagrams'])
        changed = rendered.replace('<td>AICC Lead</td>', '<td>Unassigned</td>', 1)
        self.assertNotEqual(baseline['atoms'], Capture(changed).documents[case['id']]['atoms'])
        changed = rendered.replace('marker-end="url(', 'marker-end="broken(', 1)
        self.assertNotEqual(baseline['diagrams'], Capture(changed).documents[case['id']]['diagrams'])

    def test_russian_sources_stay_russian_with_matching_project_routes(self):
        en, _ = project.documents('en'); ru, owners = project.documents('ru')
        self.assertEqual([d['url'].split('/service-resolution/')[1] for d in en], [d['url'].split('/service-resolution/')[1] for d in ru])
        self.assertIn('Решение клиентских обращений', ru[0]['title'])
        rendered = project.render(ru[0], ru, owners, 'ru')
        self.assertIn('href="journeys/payment-issue/#ru-journey-payment"', rendered)
        self.assertNotIn('href="journeys/payment-issue/#en-journey-payment"', rendered)


if __name__ == '__main__': unittest.main()
