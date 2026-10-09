"""The parity tool notices what breaks a translated edition: changed anchors, components, progress keys, tables, links into the Russian edition, and Russian words left on the page."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import parity  # noqa: E402

PAGE = '''<html><body><header><a class="lang-switch" href="../ru/x/index.html">RU</a></header><main>
<h1>{h1}</h1><h2 id="start">{h2}</h2><div class="lm-walk" data-walk="maps"><a class="lm-dot" data-dot-step="maps|guide#">1</a></div>
<table><tr><th>a</th><th>b</th></tr><tr><td>1</td><td>2</td></tr></table>
<p>{p} <span lang="ru">Закон</span></p><a href="{link}">x</a></main></body></html>'''


def sig(**kw):
    values = dict(h1='Title', h2='Part', p='Text', link='../y/index.html')
    values.update(kw)
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as fh:
        fh.write(PAGE.format(**values))
    return parity.signature(fh.name)


class Parity(unittest.TestCase):
    def test_same_structure_passes(self):
        self.assertEqual(parity.compare(sig(h1='Заголовок', h2='Часть', p='Текст'), sig(), 'x/index.html', 'en'), [])

    def test_changed_anchor_fails(self):
        other = sig()
        other.ids = ['begin']
        self.assertTrue(parity.compare(sig(), other, 'x/index.html', 'en'))

    def test_changed_progress_key_fails(self):
        other = sig()
        other.keyed = [k.replace('guide#', 'guide#part') for k in other.keyed]
        self.assertTrue(any('keyed' in e for e in parity.compare(sig(), other, 'x/index.html', 'en')))

    def test_changed_table_fails(self):
        other = sig()
        other.tables = [(2, 3)]
        self.assertTrue(any('table' in e for e in parity.compare(sig(), other, 'x/index.html', 'en')))

    def test_link_into_russian_edition_fails(self):
        errors = parity.compare(sig(), sig(link='../../ru/y/index.html'), 'x/index.html', 'en')
        self.assertTrue(any('Russian edition' in e for e in errors))

    def test_russian_words_found_but_marked_originals_and_switch_skipped(self):
        self.assertEqual(parity.cyrillic(sig()), [])
        self.assertEqual(parity.cyrillic(sig(p='Text with слово')), ['слово'])

    def test_vocabulary_order_may_differ(self):
        ru, other = sig(), sig()
        ru.ids, other.ids = ['a', 'b'], ['b', 'a']
        self.assertTrue(parity.compare(ru, other, 'x/index.html', 'en'))
        self.assertEqual(parity.compare(ru, other, 'x/index.html', 'en', ordered=False), [])

    def test_english_fields_do_not_change_the_russian_hash(self):
        ru = {'title': 'Заголовок', 'items': [{'what': 'Текст'}]}
        both = {'title': 'Заголовок', 'title_en': 'Title', 'items': [{'what': 'Текст', 'what_en': 'Text'}]}
        self.assertEqual(parity.russian_part(both), ru)


if __name__ == '__main__':
    unittest.main()
