"""Content preservation and fail-closed translation at the actual build boundary."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import lab
from check_lab import Capture


class LabProjection(unittest.TestCase):
    def test_source_tasks_and_postures_reach_both_edition_destinations(self):
        model = lab.source_content()
        for lang, expected_name in (('en', 'Define IAM and Policies'), ('ru', 'Определить IAM и политики')):
            body, search = lab.render(model, lang)
            parsed = Capture(body)
            self.assertEqual(parsed.units['task-a-2-2-name'], expected_name)
            self.assertEqual(parsed.units['task-a-2-1-desc'], 'AWS approvals; vendor onboarding sign-off' if lang == 'en' else 'Согласования AWS; одобрение подключения поставщика')
            self.assertEqual(parsed.cells['A', '2'], ['task-a-2-1', 'task-a-2-2'])
            self.assertEqual(parsed.cells['E', '2'], [])
            self.assertIn(f'/{lang}/lab/#task-a-2-2', [entry['u'] for entry in search])
            self.assertEqual(parsed.values, [50, 75, 20, 40, 80, 90, 85, 30, 70, 65, 25, 45, 80, 75, 85, 65, 55, 75, 60, 50])
            self.assertEqual(len(parsed.units), 209)
            self.assertNotIn('html-alt/', body)

    def test_incomplete_or_stale_russian_source_cannot_publish(self):
        model = lab.source_content()
        original = json.loads(lab.TRANSLATION.read_text())
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'translation.json'
            for kind in ('missing', 'stale'):
                data = copy.deepcopy(original)
                if kind == 'missing': del data['text']['task-a-2-2-name']
                else: data['source_hash'] = 'obsolete'
                path.write_text(json.dumps(data))
                with patch.object(lab, 'TRANSLATION', path), self.assertRaises(ValueError):
                    lab.render(model, 'ru')


if __name__ == '__main__':
    unittest.main()
