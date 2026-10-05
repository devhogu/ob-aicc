"""Behaviour at the retained source -> independent neighbour page boundary."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import neighbours
import workspace
from check_neighbours import Inspection


class NeighbourRendering(unittest.TestCase):
    def test_shell_keeps_five_sections_and_current_search_scope(self):
        markup = workspace.page('/ru/projects/service-resolution/', 'ru', 'projects', 'Проект', '<h1>Проект</h1>', '<a href="../">Реестр</a>')
        parsed = Inspection(markup)
        self.assertEqual(parsed.groups, ['aicc', 'discovery', 'initiatives', 'projects', 'lab'])
        self.assertEqual(parsed.section, 'projects')
        self.assertEqual(parsed.search, '../../../assets/search-projects-ru.json')
        self.assertIn('href="../../../en/projects/service-resolution/"', markup)
        self.assertNotIn('Version 2.2', markup)

    def test_discovery_preserves_scenario_text_and_direct_search_destination(self):
        source = neighbours.finance_renderer().discovery_source(Path('shared-banking-capabilities/customer-servicing/index.html'), 'en')
        url, title, body, *_ = neighbours.discovery_page(source, Path('shared-banking-capabilities/customer-servicing/index.html'), 'en')
        self.assertEqual(Inspection(source).cards, Inspection(body).cards)
        entries = neighbours.search_entries(body, url, title)
        copilot = next(entry for entry in entries if entry['h'] == 'Frontline Service Copilot')
        self.assertEqual(copilot['u'], '/en/discovery/shared-banking-capabilities/customer-servicing/#scenario-frontline-service-copilot')
        self.assertIn('id="scenario-frontline-service-copilot"', body)
        self.assertNotIn('<main', body)

    def test_portfolio_is_empty_and_project_remains_a_proposal_in_both_editions(self):
        root = workspace.ROOT / 'portal/sections'
        self.assertIn('No initiatives have been selected', (root / 'initiatives/en/register.md').read_text())
        self.assertIn('не отобрано ни одной инициативы', (root / 'initiatives/ru/register.md').read_text())
        self.assertIn('**Status: proposal.**', (root / 'projects/en/service-resolution.md').read_text())
        self.assertIn('**Статус: предложение.**', (root / 'projects/ru/service-resolution.md').read_text())


if __name__ == '__main__':
    unittest.main()
