"""Every entry of the regulation page has its own page in each edition, and every such page belongs to an entry."""
import unittest
from pathlib import Path

import yaml

V2 = Path(__file__).resolve().parents[1]


class RegulationPages(unittest.TestCase):
    def test_each_entry_has_its_page_and_each_page_its_entry(self):
        ids = {a['id'] for a in yaml.safe_load((V2 / 'reference' / 'acts.yaml').read_text(encoding='utf-8'))}
        for lang in ('ru', 'en'):
            folder = V2 / 'content' / lang / 'reference' / 'regulation'
            pages = {p.stem for p in folder.glob('*.md')} if folder.exists() else set()
            self.assertEqual(sorted(ids - pages), [], f'{lang}: entries without a page')
            self.assertEqual(sorted(pages - ids), [], f'{lang}: pages without an entry')

    def test_each_page_has_the_six_parts(self):
        for lang in ('ru', 'en'):
            for page in sorted((V2 / 'content' / lang / 'reference' / 'regulation').glob('*.md')):
                text = page.read_text(encoding='utf-8')
                for anchor in ('short', 'practice', 'ideas', 'details', 'read', 'related'):
                    self.assertIn('{#' + anchor + '}', text, f'{lang}/{page.stem}: part {anchor} missing')


if __name__ == '__main__':
    unittest.main()
