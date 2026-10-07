"""Exercise the site checker: citations against resource loads, the bounded-branch layout, links and search results."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


CHECKER = Path(__file__).resolve().parents[1] / 'tools' / 'check.py'
BRANCHES = ('center', 'discovery', 'portfolio', 'program', 'lab')
NOT_FOUND = '<!doctype html><html lang="en"><body><a href="/aicc/en/">EN</a><a href="/aicc/ru/">RU</a></body></html>'


def page(lang, depth, body):
    up = '../' * depth
    return (f'<!doctype html><html lang="{lang}"><body>'
            '<a class="o-skip" href="#main">Skip</a>'
            f'<a hreflang="en" href="{up}en/">EN</a>'
            f'<a hreflang="ru" href="{up}ru/">RU</a>'
            f'<main id="main"><h1 id="top">Reference</h1>{body}</main>'
            '</body></html>')


class SiteCheck(unittest.TestCase):
    def run_check(self, body='', *, extra=None, not_found=NOT_FOUND, search=None):
        """A minimal complete site; body goes into both routers, extra maps site paths to page bodies."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checker = root / 'portal' / 'tools' / 'check.py'
            checker.parent.mkdir(parents=True)
            shutil.copyfile(CHECKER, checker)
            site = root / 'html' / 'aicc'
            pages = {f'{lang}/': body for lang in ('en', 'ru')}
            pages.update({f'{lang}/{branch}/': '' for lang in ('en', 'ru') for branch in BRANCHES})
            pages.update(extra or {})
            for route, content in pages.items():
                target = site / route / 'index.html'
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(page(route.split('/')[0], route.count('/'), content), encoding='utf-8')
            (site / 'index.html').write_text('<!doctype html><html lang="en"><body><a href="en/">English</a></body></html>', encoding='utf-8')
            (site / '404.html').write_text(not_found, encoding='utf-8')
            assets = site / 'assets'
            assets.mkdir()
            for lang in ('en', 'ru'):
                for branch in BRANCHES:
                    entries = (search or {}).get(f'{branch}-{lang}', [])
                    (assets / f'search-{branch}-{lang}.json').write_text(json.dumps(entries), encoding='utf-8')
            return subprocess.run(
                [sys.executable, str(checker)], capture_output=True,
                text=True, timeout=15,
            )

    def test_complete_layout_passes(self):
        result = self.run_check('<a href="center/">Center</a>',
                                search={'center-en': [{'u': '/en/center/#top', 't': 'C', 'h': 'C', 'x': ''}]})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

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

    def test_broken_internal_links_and_indexes_are_rejected(self):
        for body, message in (
            ('<a href="initiatives/">Old route</a>', 'broken link initiatives/'),
            ('<a href="center/#nowhere">Anchor</a>', 'missing anchor center/#nowhere'),
            ('<script src="../assets/site.js" data-search="../assets/search-center-en.json" data-search-all="../assets/search-projects-en.json"></script>', 'broken link ../assets/site.js'),
            ('<script data-search-all="../assets/search-projects-en.json"></script>', 'broken link ../assets/search-projects-en.json'),
            ('<a href="/en/center/">Root link</a>', 'site-absolute link /en/center/'),
        ):
            with self.subTest(body=body):
                result = self.run_check(body)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(message, result.stdout)

    def test_legacy_routes_are_rejected(self):
        result = self.run_check(extra={'en/projects/': '', 'ru/projects/': ''})
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('expected exactly the router and the branches', result.stdout)

    def test_not_found_page_is_self_contained(self):
        for markup, message in (
            (NOT_FOUND.replace('<body>', '<head><link rel="stylesheet" href="assets/ui/tokens.css"></head><body>'), 'self-contained'),
            (NOT_FOUND.replace('/aicc/ru/', 'ru/'), 'must link exactly the routers'),
        ):
            with self.subTest(markup=markup):
                result = self.run_check(not_found=markup)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(message, result.stdout)

    def test_search_results_must_resolve_inside_their_branch(self):
        for entry, message in (
            ({'u': '/en/projects/', 't': 'P', 'h': 'P', 'x': ''}, 'result outside its branch'),
            ({'u': '/en/center/missing/', 't': 'P', 'h': 'P', 'x': ''}, 'broken result'),
            ({'u': '/en/center/#nowhere', 't': 'P', 'h': 'P', 'x': ''}, 'missing result anchor'),
        ):
            with self.subTest(entry=entry):
                result = self.run_check(search={'center-en': [entry]})
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(message, result.stdout)


if __name__ == '__main__':
    unittest.main()
