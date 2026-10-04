"""Exercise the site checker's distinction between citations and resource loads."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


CHECKER = Path(__file__).resolve().parents[1] / 'tools' / 'check.py'


class SiteCheck(unittest.TestCase):
    def run_check(self, body):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checker = root / 'portal' / 'tools' / 'check.py'
            checker.parent.mkdir(parents=True)
            shutil.copyfile(CHECKER, checker)
            site = root / 'html' / 'aicc'
            for lang in ('en', 'ru'):
                page = site / lang / 'index.html'
                page.parent.mkdir(parents=True)
                page.write_text(
                    f'<!doctype html><html lang="{lang}"><body>'
                    '<a class="o-skip" href="#main">Skip</a>'
                    '<a hreflang="en" href="../en/">EN</a>'
                    '<a hreflang="ru" href="../ru/">RU</a>'
                    f'<main id="main"><h1>Reference</h1>{body}</main>'
                    '</body></html>', encoding='utf-8',
                )
            assets = site / 'assets'
            assets.mkdir()
            for lang in ('en', 'ru'):
                (assets / f'search-{lang}.json').write_text('[]', encoding='utf-8')
            return subprocess.run(
                [sys.executable, str(checker)], capture_output=True,
                text=True, timeout=15,
            )

    def test_external_source_citations_are_allowed(self):
        result = self.run_check('<a href="https://example.org/reference">Source</a>')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_remote_resources_are_rejected(self):
        for resource in (
            '<script src="https://example.org/script.js"></script>',
            '<img src="https://example.org/image.png" alt="Example">',
            '<link rel="stylesheet" href="https://example.org/style.css">',
            '<iframe src="https://example.org/embed"></iframe>',
            '<img src="//example.org/image.png" alt="Example">',
        ):
            with self.subTest(resource=resource):
                result = self.run_check(resource)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn('request to another host', result.stdout)


if __name__ == '__main__':
    unittest.main()
