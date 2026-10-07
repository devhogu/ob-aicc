"""Content preservation and fail-closed translation at the actual build boundary."""
import copy
import json
import re
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
        for lang, expected_name in (('en', 'Requirements & acceptance'), ('ru', 'Требования и приёмка')):
            body, search = lab.render(model, lang)
            parsed = Capture(body)
            self.assertEqual(parsed.units['task-a-2-2-name'], expected_name)
            self.assertEqual(parsed.units['task-a-2-1-desc'], 'Fix the number of Iterations and the date of the review' if lang == 'en' else 'Зафиксировать число итераций и дату рассмотрения результата')
            self.assertEqual(parsed.cells['A', '2'], ['task-a-2-1', 'task-a-2-2'])
            self.assertEqual(parsed.cells['E', '1'], [])
            self.assertIn(f'/{lang}/lab/#task-a-2-2', [entry['u'] for entry in search])
            self.assertEqual(parsed.values, [])
            self.assertEqual(len(parsed.units), len(lab.source_content()["units"]))
            self.assertNotIn('html-alt/', body)

    def test_incomplete_or_stale_russian_record_cannot_publish(self):
        model = lab.source_content()
        original = lab.TRANSLATION.read_text()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'lab.md'
            for kind in ('missing', 'stale'):
                if kind == 'missing':
                    text = '\n'.join(l for l in original.splitlines() if not l.startswith('| task-a-2-2 |'))
                else:
                    text = re.sub(r'source_sha256: [0-9a-f]+', 'source_sha256: ' + '0' * 64, original)
                path.write_text(text)
                with patch.object(lab, 'TRANSLATION', path), self.assertRaises(ValueError):
                    lab.render(model, 'ru')


if __name__ == '__main__':
    unittest.main()
