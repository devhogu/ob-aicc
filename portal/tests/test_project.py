"""Protect actual document links, source preservation and failure detection."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import project
from check_project import Capture


class ProjectPromotion(unittest.TestCase):
    def test_business_case_links_reach_real_candidate_and_blueprint_pages(self):
        docs, owners = project.documents('en')
        case = next(d for d in docs if d['key'] == 'business-use-case')
        rendered = project.render(case, docs, owners, 'en')
        self.assertIn('href="../payment-issue/#en-payment-charter"', rendered)
        self.assertIn('href="../technical-blueprint/#en-technical-blueprint"', rendered)
        self.assertIn('id="en-business-use-case-delivery-action-workflow"', rendered)
        self.assertNotIn('href="#en-payment-charter"', rendered)
        self.assertIn('The use case recommends from this approved list. It does not invent process steps.', rendered)

    def test_source_checker_detects_dropped_cell_and_changed_diagram_relationship(self):
        docs, owners = project.documents('en')
        case = next(d for d in docs if d['key'] == 'business-use-case')
        rendered = project.render(case, docs, owners, 'en')
        baseline = Capture(case['body']).documents[case['id']]
        self.assertEqual(baseline['atoms'], Capture(rendered).documents[case['id']]['atoms'])
        self.assertEqual(baseline['diagrams'], Capture(rendered).documents[case['id']]['diagrams'])
        changed = rendered.replace('<td>Service Operations Manager</td>', '<td>Unassigned</td>', 1)
        self.assertNotEqual(baseline['atoms'], Capture(changed).documents[case['id']]['atoms'])
        changed = rendered.replace('marker-end="url(', 'marker-end="broken(', 1)
        self.assertNotEqual(baseline['diagrams'], Capture(changed).documents[case['id']]['diagrams'])

    def test_russian_sources_stay_russian_with_matching_project_routes(self):
        en, _ = project.documents('en'); ru, owners = project.documents('ru')
        self.assertEqual([d['url'].split('/service-resolution/')[1] for d in en], [d['url'].split('/service-resolution/')[1] for d in ru])
        self.assertIn('Разрешение вопросов клиентского обслуживания', ru[0]['title'])
        rendered = project.render(ru[0], ru, owners, 'ru')
        self.assertIn('href="payment-issue/#ru-payment-charter"', rendered)
        self.assertNotIn('href="payment-issue/#en-payment-charter"', rendered)


if __name__ == '__main__': unittest.main()
