"""Project cards: the schema refuses what it must, and the views follow the cards."""
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import cards

CARDS = Path(__file__).resolve().parents[1] / 'cards'
GOOD = (CARDS / 'INI-014.yaml').read_text(encoding='utf-8')


class Loading(unittest.TestCase):
    def folder(self, **files):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        shutil.copyfile(CARDS / 'schema.json', root / 'schema.json')
        for name, text in files.items():
            (root / name).write_text(text, encoding='utf-8')
        return root

    def test_the_real_cards_are_valid(self):
        loaded = cards.load_cards()
        self.assertTrue(loaded)
        self.assertEqual(len({c['id'] for c in loaded}), len(loaded))

    def test_a_valid_card_loads(self):
        self.assertEqual(cards.load_cards(self.folder(**{'INI-014.yaml': GOOD}))[0]['id'], 'INI-014')

    def test_unknown_stage_unknown_field_and_missing_field_are_refused(self):
        with self.assertRaisesRegex(ValueError, 'stage'):
            cards.load_cards(self.folder(**{'INI-014.yaml': GOOD.replace('stage: Воронка', 'stage: Одобрено')}))
        with self.assertRaisesRegex(ValueError, 'additional|Additional'):
            cards.load_cards(self.folder(**{'INI-014.yaml': GOOD + 'secret: 1\n'}))
        with self.assertRaisesRegex(ValueError, 'folks|required|people'):
            cards.load_cards(self.folder(**{'INI-014.yaml': GOOD.replace('people:', 'folks:')}))

    def test_the_file_name_must_be_the_card_id(self):
        with self.assertRaisesRegex(ValueError, 'file name'):
            cards.load_cards(self.folder(**{'INI-099.yaml': GOOD}))

    def test_a_function_must_name_a_parent_that_is_on_the_card(self):
        with self.assertRaisesRegex(ValueError, 'parent'):
            cards.load_cards(self.folder(**{'INI-014.yaml': GOOD.replace('parent: CAP-001', 'parent: CAP-099', 1)}))

    def test_work_item_ids_are_unique_across_cards(self):
        other = GOOD.replace('id: INI-014', 'id: INI-016')
        with self.assertRaisesRegex(ValueError, 'repeat'):
            cards.load_cards(self.folder(**{'INI-014.yaml': GOOD, 'INI-016.yaml': other}))


if __name__ == '__main__':
    unittest.main()
