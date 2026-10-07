"""Behaviour at the catalog record -> independent neighbour page boundary."""
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import discovery
import neighbours
import workspace
from check_neighbours import Inspection


class NeighbourRendering(unittest.TestCase):
    def test_shell_keeps_five_sections_and_current_search_scope(self):
        markup = workspace.page('/ru/program/service-resolution/', 'ru', 'program', 'Проект', '<h1>Проект</h1>', '<a href="../">Реестр</a>')
        parsed = Inspection(markup)
        self.assertEqual(parsed.groups, ['center', 'discovery', 'portfolio', 'program', 'lab'])
        self.assertEqual(parsed.section, 'program')
        self.assertEqual(parsed.search, '../../../assets/search-program-ru.json')
        self.assertEqual(parsed.search_all, [f'../../../assets/search-{s}-ru.json' for s in ('center', 'discovery', 'portfolio', 'program', 'lab')])
        self.assertFalse(parsed.global_default)
        self.assertIn('Все разделы', markup)
        self.assertIn('href="../../../en/program/service-resolution/"', markup)
        self.assertIn('Версия 2.2', markup)
        self.assertEqual(parsed.feedback_buttons, 1)
        self.assertEqual(len(parsed.nav_footer_links), 2)
        self.assertEqual(len(parsed.footer_links), 3)
        self.assertNotIn('class="doc-facts"', markup)

    def test_renamed_routes_keep_their_page_references(self):
        # A reader may quote the feedback ID of a page published under its former route.
        self.assertEqual(workspace.page_key('/en/program/service-resolution/charter/'), 'projects/service-resolution/charter/index')
        self.assertEqual(workspace.page_key('/ru/portfolio/ini-004/'), 'initiatives/ini-004/index')
        self.assertEqual(workspace.page_key('/en/lab/'), 'lab/index')

    def test_router_leads_to_the_five_branches_with_counted_facts(self):
        import router
        for lang in ('en', 'ru'):
            with self.subTest(lang=lang):
                url, markup = router.router_page(lang)
                parsed = Inspection(markup)
                self.assertEqual(url, f'/{lang}/')
                self.assertEqual(parsed.section, 'router')
                self.assertEqual(parsed.doors, ['center', 'discovery', 'portfolio', 'program', 'lab'])
                self.assertTrue(parsed.global_default)
                self.assertEqual(parsed.main_links, ['center/', 'discovery/', 'portfolio/', 'program/', 'lab/'])
                counts = router.facts(lang)
                self.assertEqual(counts['discovery'], len(neighbours.scenario_index(lang)))
                self.assertEqual(counts['center'], len([p for p in (workspace.ROOT / 'charter/en').rglob('*.md') if p.name != 'README.md']))
                fact = f'{counts["lab"]} workflow tasks' if lang == 'en' else f'Задач процесса: {counts["lab"]}'
                self.assertIn(fact, markup)
                self.assertIn(f'href="../{"ru" if lang == "en" else "en"}/"', markup)

    def test_discovery_preserves_scenario_text_and_direct_search_destination(self):
        source = discovery.source(Path('shared-banking-capabilities/customer-servicing/index.html'), 'en')
        url, title, body, *_ = neighbours.discovery_page(source, Path('shared-banking-capabilities/customer-servicing/index.html'), 'en')
        self.assertEqual(Inspection(source).cards, Inspection(body).cards)
        entries = neighbours.search_entries(body, url, title)
        copilot = next(entry for entry in entries if entry['h'] == 'Frontline Service Copilot')
        self.assertEqual(copilot['u'], '/en/discovery/shared-banking-capabilities/customer-servicing/#scenario-frontline-service-copilot')
        self.assertIn('id="scenario-frontline-service-copilot"', body)
        self.assertNotIn('<main', body)

    def test_portfolio_is_record_projected_and_project_remains_a_proposal_in_both_editions(self):
        root = workspace.ROOT / 'portal/sections'
        self.assertIn('maintained Registry', (root / 'portfolio/en/register.md').read_text())
        self.assertIn('рабочих записей реестра', (root / 'portfolio/ru/register.md').read_text())
        self.assertIn('| Proposed initiative |', (root / 'program/en/index.md').read_text())
        self.assertIn('| Предлагаемая инициатива |', (root / 'program/ru/index.md').read_text())

    def test_domain_preview_stage_links_reach_preserved_flow_actions(self):
        for lang in ('en', 'ru'):
            with self.subTest(lang=lang):
                route = Path('strategic-portfolio/index.html')
                source = discovery.source(route, lang)
                body = neighbours.discovery_page(source, route, lang)[2]
                links = [urlsplit(link) for link in Inspection('<main>' + body + '</main>').main_links if '#stage-' in link]
                self.assertTrue(links)
                target = route.parent / links[0].path
                original = discovery.source(target, lang)
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
