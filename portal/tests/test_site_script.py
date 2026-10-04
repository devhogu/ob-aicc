"""Run site-script interaction regressions with Node's built-in test runner."""
from pathlib import Path
import subprocess
import unittest


class SiteScript(unittest.TestCase):
    def test_search_uses_the_current_query_after_delayed_loading(self):
        result = subprocess.run(
            ['node', '--test', str(Path(__file__).with_name('search.test.cjs'))],
            capture_output=True, text=True, timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
