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
            files[f'{lang}/index.html'] = f'''<html lang="{lang}"><head><script src="../assets/site.js" defer data-search="../assets/search-center-{lang}.json"></script></head><body><h1>AI — Банк</h1><a href="guide/?print=1#term">Guide</a><a href="../{other}/">Language</a><a href="https://example.org/">Citation</a><svg viewBox="0 0 24 24"><path d="M1 2"/></svg></body></html>'''
            files[f'{lang}/guide/index.html'] = f'''<html lang="{lang}"><head><script src="../../assets/site.js" defer data-search="../../assets/search-center-{lang}.json"></script></head><body><h1 id="term">AI</h1><a href="../">Home</a><a href="/">Entry</a><a href="#term">Term</a></body></html>'''
            files[f'assets/search-center-{lang}.json'] = json.dumps([{'u': f'/{lang}/guide/#term', 'h': 'AI', 't': 'Guide', 'x': 'AI — Банк'}])
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
        self.assertIn('src="../assets/search-center-ru.js"', page)
        self.assertIn('data-search="../assets/search-center-ru.js"', page)
        self.assertIn('/ru/guide/index.html#term', (self.output / 'assets/search-center-ru.js').read_text())
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
            path.write_text(f'<html lang="{lang}"><script src="../../assets/site.js" defer data-search="../../assets/search-discovery-{lang}.json" data-search-all="../../assets/search-center-{lang}.json ../../assets/search-discovery-{lang}.json"></script><h1 id="payment">Payment discovery</h1></html>')
            (self.source / f'assets/search-discovery-{lang}.json').write_text(json.dumps([{'u': f'/{lang}/discovery/#payment', 'h': 'Payment discovery', 't': 'Discovery', 'x': 'Scenario'}]))
        result = self.run_export()
        self.assertEqual(result.returncode, 0, result.stderr)
        page = (self.output / 'ru/discovery/index.html').read_text()
        self.assertIn('src="../../assets/search-discovery-ru.js"', page)
        self.assertIn('data-search="../../assets/search-discovery-ru.js"', page)
        self.assertNotIn('src="../../assets/search-center-ru.js"', page)
        # Global search loads every branch index as a script too.
        self.assertIn('data-search-all="../../assets/search-center-ru.js ../../assets/search-discovery-ru.js"', page)
        self.assertIn('/ru/discovery/index.html#payment', (self.output / 'assets/search-discovery-ru.js').read_text())

    def test_refuses_to_replace_an_unowned_folder(self):
        self.output.mkdir()
        (self.output / 'notes.txt').write_text('Keep this')
        result = self.run_export()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.output / 'notes.txt').read_text(), 'Keep this')


class StaticLanguageExport(PortableExport):
    def run_export(self):
        return subprocess.run([sys.executable, str(EXPORT), '--static', '--source', str(self.source), '--output', str(self.output)], capture_output=True, text=True)

    # Interactive export assertions belong to PortableExport, not this edition.
    def test_reader_links_search_unicode_and_svg_survive_relocation(self):
        before = self.tree(self.source)
        result = self.run_export()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(before, self.tree(self.source))
        for lang, other in [('en', 'ru'), ('ru', 'en')]:
            page = (self.output / lang / 'index.html').read_text()
            self.assertNotIn('<script', page)
            self.assertNotIn(f'../{other}/', page)
            self.assertIn('href="guide/index.html?print=1#term"', page)
            self.assertIn('<h1>AI — Банк</h1>', page)
            self.assertIn('<svg viewBox="0 0 24 24"><path d="M1 2"/></svg>', page)
            self.assertIn('href="https://example.org/"', page)
            self.assertIn('href="../index.html"', (self.output / lang / 'guide/index.html').read_text())
            self.assertTrue((self.output / lang / 'contents.html').is_file())
        self.assertFalse(any(p.endswith('.js') for p in self.tree(self.output)))
        first = self.tree(self.output)
        self.assertEqual(self.run_export().returncode, 0)
        self.assertEqual(first, self.tree(self.output))

    def test_neighbour_search_keeps_its_own_index_after_export(self):
        # Native topic indexes retain section-local destinations without script data.
        for lang in ('en', 'ru'):
            path = self.source / lang / 'discovery/index.html'
            path.parent.mkdir()
            path.write_text(f'<html lang="{lang}"><script src="../../assets/site.js" data-search="../../assets/search-discovery-{lang}.json"></script><h1 id="payment">Payment discovery</h1></html>')
            (self.source / f'assets/search-discovery-{lang}.json').write_text(json.dumps([{'u': f'/{lang}/discovery/#payment', 'h': 'Payment discovery', 't': 'Discovery', 'x': 'Scenario'}]))
        result = self.run_export()
        self.assertEqual(result.returncode, 0, result.stderr)
        for lang in ('en', 'ru'):
            contents = (self.output / lang / 'contents.html').read_text()
            self.assertIn('discovery/index.html#payment', contents)
            self.assertIn('guide/index.html#term', contents)

    def test_popup_content_controls_and_light_mode(self):
        for lang in ('en', 'ru'):
            path = self.source / lang / 'guide/index.html'
            text = path.read_text().replace('</body>', '')
            text = text.replace('</html>', '') + '''
<nav class="lang-switch"><a href="../../ru/">RU</a></nav>
<button id="theme-switch">Dark</button><div class="o-search"><input type="search"></div>
<div class="pf-filter"><input data-pf-search></div><section id="board" hidden><h2>Board</h2><a href="../">Home</a></section>
<details><summary>Scenario</summary><p>Actual expanded scenario</p></details>
<button class="flow-stages__stage" id="stage-flow--scan" data-flow-id="flow" data-stage="scan"><span>Scan</span></button>
<script>const FLOW_STAGES = {"flow":[{"slug":"scan","label":"Scan","title":"Scan the landscape","intent":"Unique stage intent","problem":"Unique stage problem"}]};</script>
<button onclick="bad()" data-copy="term">Copy</button><a href="javascript:bad()">Bad control</a>
<figure class="o-diagram"><button class="dz-open">Expand</button><svg viewBox="0 0 100 20"><text x="1" y="10">Diagram label</text><foreignObject x="0" y="0" width="100" height="20"><div xmlns="http://www.w3.org/1999/xhtml"><p>First<br>Second&nbsp;line</p></div></foreignObject></svg></figure>
</body></html>'''
            path.write_text(text)
        result = self.run_export()
        self.assertEqual(result.returncode, 0, result.stderr)
        for lang in ('en', 'ru'):
            page = (self.output / lang / 'guide/index.html').read_text()
            for word in ['Unique stage intent', 'Unique stage problem', 'Actual expanded scenario', 'Diagram label', 'data-theme="light"']:
                self.assertIn(word, page)
            for forbidden in ['<script', '<button', 'onclick=', 'javascript:', ' hidden', 'lang-switch', 'theme-switch', 'pf-filter']:
                self.assertNotIn(forbidden, page)
            self.assertIn('href="#stage-flow--scan"', page)
            diagrams = list((self.output / lang / 'assets/diagrams').glob('*.svg'))
            self.assertTrue(diagrams)
            from xml.etree import ElementTree
            for diagram in diagrams:
                ElementTree.parse(diagram)

    def test_refreshes_previous_interactive_export(self):
        result = subprocess.run([sys.executable, str(EXPORT), '--source', str(self.source), '--output', str(self.output)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = self.run_export()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.output / 'assets').exists())
        self.assertTrue((self.output / 'en/contents.html').exists())


if __name__ == '__main__':
    unittest.main()
