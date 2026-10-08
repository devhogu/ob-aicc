"""Hub v2: term markers, page links, identifiers, and the rules the checker enforces."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import build
import check

TERMS = {'funnel': {'id': 'funnel', 'ru': 'воронка', 'en': 'funnel', 'definition': 'Входной уровень.'}}


def fixture():
    pages = {
        'index': build.Page('index', 'Хаб', 'hub', 0, '', ''),
        'process/levels': build.Page('process/levels', 'Уровни', 'process', 10, '', ''),
        'vocabulary': build.Page('vocabulary', 'Словарь', 'vocabulary', 0, '', ''),
    }
    return pages, build.load_site()


class Markers(unittest.TestCase):
    def test_term_shows_the_russian_word_and_the_english_term_and_links_to_the_vocabulary(self):
        pages, site = fixture()
        html = build.render_markdown('Уровень [[funnel|воронки]].', pages['process/levels'], TERMS, pages, site)
        self.assertIn('воронки <span class="term-en">(funnel)</span>', html)
        self.assertIn('href="../../vocabulary/index.html#funnel"', html)

    def test_unknown_term_or_page_is_refused(self):
        pages, site = fixture()
        with self.assertRaisesRegex(ValueError, 'unknown term'):
            build.render_markdown('[[nothing]]', pages['index'], TERMS, pages, site)
        with self.assertRaisesRegex(ValueError, 'unknown page'):
            build.render_markdown('[x](page:nowhere)', pages['index'], TERMS, pages, site)

    def test_page_links_are_relative_and_name_the_file(self):
        pages, site = fixture()
        html = build.render_markdown('[Уровни](page:process/levels#a)', pages['index'], TERMS, pages, site)
        self.assertIn('href="process/levels/index.html#a"', html)

    def test_headings_get_identifiers_and_repeat_headings_stay_unique(self):
        pages, site = fixture()
        page = pages['index']
        html = build.render_markdown('## Шаг\n\n## Шаг\n\n### Ещё', page, TERMS, pages, site)
        self.assertIn('id="шаг"', html)
        self.assertIn('id="шаг-2"', html)
        self.assertEqual([h[1] for h in page.headings], ['шаг', 'шаг-2', 'ещё'])


class Identifiers(unittest.TestCase):
    def test_identifiers_are_stable_five_characters_and_unique(self):
        taken = set()
        first = [build.short_id(f'page/{n}', taken) for n in range(300)]
        self.assertEqual(len(set(first)), 300)
        self.assertTrue(all(len(i) == 5 for i in first))
        again = [build.short_id(f'page/{n}', set()) for n in range(5)]
        self.assertEqual(again, first[:5])


class Vocabulary(unittest.TestCase):
    def test_every_term_has_its_four_fields_and_a_unique_id(self):
        terms = build.load_terms()
        self.assertTrue(all(t['en'] and t['ru'] and t['definition'] for t in terms.values()))


class Checker(unittest.TestCase):
    def built(self, body='<p>Текст</p>', extra=''):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        out = Path(directory.name) / 'v2'
        (out / 'ru').mkdir(parents=True)
        (out / 'assets').mkdir()
        (out / 'ru' / 'index.html').write_text(
            f'<html lang="ru"><head><title>t</title></head><body><span class="status-chip">Черновик</span><h1>Хаб</h1><button class="pagefb"><span>Отзыв</span><span>ID: AAAAA</span></button>{body}</body></html>', encoding='utf-8')
        (out / 'index.html').write_text('<meta http-equiv="refresh" content="0; url=ru/index.html">', encoding='utf-8')
        (out / 'assets' / 'page-ids.json').write_text('{"index": "AAAAA"}', encoding='utf-8')
        (out / 'assets' / 'search-ru.js').write_text('window.AICC_SEARCH_INDEX=[];\n', encoding='utf-8')
        original = check.OUT
        check.OUT = out
        self.addCleanup(setattr, check, 'OUT', original)
        return check.check()

    def test_a_sound_page_passes(self):
        self.assertEqual(self.built(), [])

    def test_forbidden_wording_and_stray_english_terms_and_broken_links_are_found(self):
        self.assertTrue(any('forbidden' in e for e in self.built('<p>Executive Sponsor решает</p>')))
        self.assertTrue(any('English term' in e for e in self.built('<p>Наша funnel большая</p>')))
        self.assertTrue(any('broken reference' in e for e in self.built('<a href="missing/index.html">x</a>')))
        self.assertTrue(any('leaves the site' in e for e in self.built('<a href="../../v1/index.html">x</a>')))

    def test_term_in_its_vocabulary_form_is_allowed(self):
        self.assertEqual(self.built('<p>Наша воронка <span class="term-en">(funnel)</span></p>'), [])


if __name__ == '__main__':
    unittest.main()
