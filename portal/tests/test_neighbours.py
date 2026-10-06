"""Behaviour at the retained source -> independent neighbour page boundary."""
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import urlsplit

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
        self.assertIn('Версия 2.2', markup)
        self.assertEqual(parsed.feedback_buttons, 1)
        self.assertEqual(len(parsed.nav_footer_links), 2)
        self.assertEqual(len(parsed.footer_links), 3)
        self.assertNotIn('class="doc-facts"', markup)

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
        self.assertIn('| Proposed initiative |', (root / 'projects/en/index.md').read_text())
        self.assertIn('| Предлагаемая инициатива |', (root / 'projects/ru/index.md').read_text())

    def test_domain_preview_stage_links_reach_preserved_flow_actions(self):
        renderer = neighbours.finance_renderer()
        for lang in ('en', 'ru'):
            with self.subTest(lang=lang):
                route = Path('strategic-portfolio/index.html')
                source = renderer.discovery_source(route, lang)
                body = neighbours.discovery_page(source, route, lang)[2]
                links = [urlsplit(link) for link in Inspection('<main>' + body + '</main>').main_links if '#stage-' in link]
                self.assertTrue(links)
                target = route.parent / links[0].path
                original = renderer.discovery_source(target, lang)
                projected = neighbours.discovery_page(original, target, lang)[2]
                def identities(text):
                    buttons = re.findall(r'<button\b[^>]*data-flow-id="[^"]+"[^>]*>', text)
                    return [(re.search(r'data-flow-id="([^"]+)"', button)[1],
                             re.search(r'data-stage="([^"]+)"', button)[1]) for button in buttons]
                self.assertTrue(identities(original))
                self.assertEqual(identities(original), identities(projected))
                self.assertTrue(all(link.fragment in Inspection(projected).ids for link in links))


if __name__ == '__main__':
    unittest.main()
