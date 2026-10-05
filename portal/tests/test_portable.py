"""Exercise the export CLI through files a reader will open, including failed refreshes."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

EXPORT = Path(__file__).resolve().parents[1] / 'tools/export_portable.py'


class PortableExport(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / 'source'
        self.output = Path(self.temp.name) / 'output'
        files = {
            'index.html': '<html><head><meta http-equiv="refresh" content="0; url=en/"></head><body><a href="en/">EN</a><a href="ru/">RU</a></body></html>',
            'assets/site.js': '// web script',
        }
        for lang in ('en', 'ru'):
            other = 'ru' if lang == 'en' else 'en'
            files[f'{lang}/index.html'] = f'''<html lang="{lang}"><head><script src="../assets/site.js" defer data-search="../assets/search-{lang}.json"></script></head><body><h1>AI — Банк</h1><a href="guide/?print=1#term">Guide</a><a href="../{other}/">Language</a><a href="https://example.org/">Citation</a><svg viewBox="0 0 24 24"><path d="M1 2"/></svg></body></html>'''
            files[f'{lang}/guide/index.html'] = f'''<html lang="{lang}"><head><script src="../../assets/site.js" defer data-search="../../assets/search-{lang}.json"></script></head><body><h1 id="term">AI</h1><a href="../">Home</a><a href="/">Entry</a><a href="#term">Term</a></body></html>'''
            files[f'assets/search-{lang}.json'] = json.dumps([{'u': f'/{lang}/guide/#term', 'h': 'AI', 't': 'Guide', 'x': 'AI — Банк'}])
        for path, text in files.items():
            target = self.source / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)

    def run_export(self):
        return subprocess.run([sys.executable, str(EXPORT), '--source', str(self.source), '--output', str(self.output)], capture_output=True, text=True)

    def tree(self, path):
        return {p.relative_to(path).as_posix(): p.read_bytes() for p in path.rglob('*') if p.is_file()}

    def test_reader_links_search_unicode_and_svg_survive_relocation(self):
        before = self.tree(self.source)
        result = self.run_export()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(before, self.tree(self.source))
        page = (self.output / 'ru/index.html').read_text()
        self.assertIn('href="guide/index.html?print=1#term"', page)
        self.assertIn('href="../en/index.html"', page)
        self.assertIn('href="https://example.org/"', page)
        self.assertIn('<h1>AI — Банк</h1>', page)
        self.assertIn('<svg viewBox="0 0 24 24"><path d="M1 2"/></svg>', page)
        self.assertIn('src="../assets/search-ru.js"', page)
        self.assertIn('data-search="../assets/search-ru.js"', page)
        self.assertIn('/ru/guide/index.html#term', (self.output / 'assets/search-ru.js').read_text())
        self.assertIn('href="../../index.html"', (self.output / 'ru/guide/index.html').read_text())
        entry = (self.output / 'aicc.html').read_text()
        self.assertNotIn('http-equiv="refresh"', entry)
        self.assertIn('href="ru/index.html"', entry)
        first = self.tree(self.output)
        self.assertEqual(self.run_export().returncode, 0)
        self.assertEqual(first, self.tree(self.output))

    def test_broken_anchor_does_not_replace_a_working_export(self):
        self.assertEqual(self.run_export().returncode, 0)
        before = self.tree(self.output)
        page = self.source / 'ru/index.html'
        page.write_text(page.read_text().replace('#term', '#missing'))
        result = self.run_export()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('missing anchor', result.stderr)
        self.assertEqual(before, self.tree(self.output))

    def test_neighbour_search_keeps_its_own_index_after_export(self):
        for lang in ('en', 'ru'):
            path = self.source / lang / 'discovery/index.html'
            path.parent.mkdir()
            path.write_text(f'<html lang="{lang}"><script src="../../assets/site.js" defer data-search="../../assets/search-discovery-{lang}.json"></script><h1 id="payment">Payment discovery</h1></html>')
            (self.source / f'assets/search-discovery-{lang}.json').write_text(json.dumps([{'u': f'/{lang}/discovery/#payment', 'h': 'Payment discovery', 't': 'Discovery', 'x': 'Scenario'}]))
        result = self.run_export()
        self.assertEqual(result.returncode, 0, result.stderr)
        page = (self.output / 'ru/discovery/index.html').read_text()
        self.assertIn('src="../../assets/search-discovery-ru.js"', page)
        self.assertIn('data-search="../../assets/search-discovery-ru.js"', page)
        self.assertNotIn('src="../../assets/search-ru.js"', page)
        self.assertIn('/ru/discovery/index.html#payment', (self.output / 'assets/search-discovery-ru.js').read_text())

    def test_refuses_to_replace_an_unowned_folder(self):
        self.output.mkdir()
        (self.output / 'notes.txt').write_text('Keep this')
        result = self.run_export()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.output / 'notes.txt').read_text(), 'Keep this')


if __name__ == '__main__':
    unittest.main()
