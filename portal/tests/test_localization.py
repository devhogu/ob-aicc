"""Behavioral checks for the language source -> rendered page boundary."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.insert(0, str(TOOLS))
import build
from localization import Sources, canonical_path


def translation(path, source, body, extra='', status='reviewed'):
    metadata = build.front_matter(source)
    original_body = re.sub(r'^```yaml\n.*?```\s*', '', body, count=1, flags=re.S)
    fields = ''
    if metadata.get('id'):
        fields += 'id: ' + metadata['id'].replace('-EN', '-RU') + '\n'
        fields += 'status: ' + metadata['status'] + '\nrevision: ' + metadata['revision'] + '\n'
        fields += 'source_revision: ' + metadata['revision'] + '\n'
    return ('```yaml\n' + fields + f'source: {path}\nsource_sha256: {hashlib.sha256(source.encode()).hexdigest()}\n'
            + f'translation_status: {status}\n' + extra + '```\n\n' + original_body)


class SourceSelection(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = 'charter/en/documents/example.md'
        self.en = '```yaml\nid: AICC-REF-01-EN\nstatus: active\nrevision: 2.1\n```\n\n# Example\n\n## 1. Scope\n\n1.1. Approved rule.\n'
        p = self.root / self.path
        p.parent.mkdir(parents=True)
        p.write_text(self.en)
        self.ru = self.root / 'charter/ru/documents/example.md'
        self.ru.parent.mkdir(parents=True)

    def select(self):
        return Sources(self.root, 'ru').resolve(self.path)

    def test_missing_and_draft_translation_keep_english_identity(self):
        self.assertEqual(self.select().language, 'en')
        self.ru.write_text(translation(self.path, self.en, self.en.replace('Approved rule.', 'Черновик.'), status='draft'))
        selected = self.select()
        self.assertEqual(selected.text, self.en)
        self.assertEqual(selected.path, self.path)
        self.assertEqual(selected.metadata['id'], 'AICC-REF-01-EN')

    def test_reviewed_translation_selects_real_language_and_metadata(self):
        self.ru.write_text(translation(self.path, self.en, self.en.replace('Approved rule.', 'Утверждённое правило.')))
        selected = self.select()
        self.assertEqual(selected.language, 'ru')
        self.assertEqual(selected.metadata['id'], 'AICC-REF-01-RU')
        self.assertIn('Утверждённое правило.', selected.text)
        self.assertEqual(canonical_path(selected.path), self.path)

    def test_english_edit_invalidates_reviewed_translation(self):
        self.ru.write_text(translation(self.path, self.en, self.en))
        (self.root / self.path).write_text(self.en + '\nNew obligation.\n')
        with self.assertRaisesRegex(ValueError, 'source_sha256'):
            self.select()

    def test_wrong_identity_and_clause_drift_are_rejected(self):
        valid = translation(self.path, self.en, self.en)
        self.ru.write_text(valid.replace('id: AICC-REF-01-RU', 'id: AICC-REF-02-RU'))
        with self.assertRaisesRegex(ValueError, 'id does not match'):
            self.select()
        self.ru.write_text(valid.replace('1.1.', '1.2.'))
        with self.assertRaisesRegex(ValueError, 'numbered sections or clauses'):
            self.select()

    def test_translated_table_headers_retain_canonical_lookup_keys(self):
        self.en += '\n| Role | Does |\n| --- | --- |\n| Owner | Approves |\n'
        (self.root / self.path).write_text(self.en)
        self.ru.write_text(translation(self.path, self.en, self.en.replace('| Role | Does |', '| Роль | Обязанности |').replace('| Owner | Approves |', '| Владелец | Утверждает |')))
        rows = Sources(self.root, 'ru').table(self.path, '| Role | Does', ('Role',))
        self.assertEqual(rows[0]['Role'], 'Owner')
        self.assertEqual(rows[0]['_localized_Role'], 'Владелец')
        self.assertEqual(rows[0]['Does'], 'Утверждает')
        self.ru.write_text(self.ru.read_text().replace('| Владелец | Утверждает |', '| Владелец | Утверждает | Extra |'))
        with self.assertRaisesRegex(ValueError, 'table structure'):
            self.select()

    def test_record_date_cannot_be_changed_by_a_translation(self):
        path = 'registry/en/decision-log.md'
        source = '# Decisions\n\nDR-2026-063, 2026-10-03.\n'
        p = self.root / path; p.parent.mkdir(parents=True); p.write_text(source)
        target = self.root / 'registry/ru/decision-log.md'; target.parent.mkdir(parents=True)
        target.write_text(translation(path, source, source.replace('2026-10-03', '2026-10-04')))
        with self.assertRaisesRegex(ValueError, 'record identifiers or dates'):
            Sources(self.root, 'ru').resolve(path)


class PortalRendering(unittest.TestCase):
    def test_reviewed_text_links_search_diagrams_and_missing_fallback(self):
        # Exercise the real renderer with the actual sitemap and a temporary corpus.
        repository = Path(build.ROOT)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for rel in ['charter/en', 'portal/content/en']:
                shutil.copytree(repository / rel, root / rel)
            path = 'portal/content/en/delivery/overview.md'
            en_text = (root / path).read_text()
            ru_text = re.sub(r'^1\.1\..*$', '1.1. Проверка русской поставки.', en_text, count=1, flags=re.M)
            ru_text = ru_text.replace('Capability<br/>from the Portfolio', 'Возможность<br/>from the Portfolio')
            target = root / 'portal/content/ru/delivery/overview.md'; target.parent.mkdir(parents=True)
            target.write_text(translation(path, en_text, ru_text))
            # Also exercise a governed document, including its identity and source revision.
            doc = 'charter/en/documents/business-model.md'
            source_doc = (root / doc).read_text()
            doc_target = root / 'charter/ru/documents/business-model.md'; doc_target.parent.mkdir(parents=True)
            doc_target.write_text(translation(doc, source_doc, source_doc.replace('# Business Model', '# Бизнес-модель', 1)))
            soi_path = 'charter/en/documents/statement-of-intent.md'
            soi = (root / soi_path).read_text()
            (root / 'charter/ru/documents/statement-of-intent.md').write_text(translation(soi_path, soi, soi.replace('Customer intelligence', 'Аналитика клиентов').replace('**Objective.**', '**Цель.**').replace('**Intended outcome.**', '**Ожидаемый результат.**')))
            om_path = 'charter/en/documents/operating-model.md'
            om = (root / om_path).read_text()
            (root / 'charter/ru/documents/operating-model.md').write_text(translation(om_path, om, om.replace('Review of the documents', 'Проверка документов')))
            guide_path = 'charter/en/guides/unit-governance-guide.md'
            guide = (root / guide_path).read_text()
            guide_target = root / 'charter/ru/guides/unit-governance-guide.md'; guide_target.parent.mkdir(parents=True)
            guide_target.write_text(translation(guide_path, guide, guide.replace('| Control |', '| Контроль |')))
            templates_path = 'charter/en/templates/README.md'
            templates = (root / templates_path).read_text()
            templates_target = root / 'charter/ru/templates/README.md'; templates_target.parent.mkdir(parents=True)
            templates_target.write_text(translation(templates_path, templates, templates.replace('Decision Record', 'Запись о решении')))
            with patch.object(build, 'ROOT', str(root)):
                ru = build.Site(argparse.Namespace(no_diagrams=True), 'ru')
                build.add_generated_pages(ru); build.assign_refs(ru); build.load_terms(ru)
                diagrams = build.render_pages(ru)
                ru.diagram_code = dict(diagrams)
                ru.svgs = {key: {'light': '<svg></svg>', 'dark': '<svg></svg>'} for key, _ in diagrams}
                page = ru.by_id['delivery/index']
                rendered = build.build_page(ru, page, 'ru')
                self.assertIn('Проверка русской поставки.', rendered)
                self.assertIn('<div class="o-doc" lang="ru">', rendered)
                self.assertNotIn('class="o-callout lang-note"', rendered)
                self.assertIn('hreflang="en"', rendered)
                self.assertTrue(any('Возможность' in code for _, code in diagrams))
                records = [r for r in build.search_index(ru, 'ru') if r['u'].startswith('/ru/delivery/#')]
                self.assertTrue(any('Проверка русской поставки' in r['x'] for r in records))
                href = ru.map_link('../reference/industry-body-of-knowledge.md', {'source': str(target.relative_to(root)), 'lang': 'ru', 'url': '/ru/delivery/'})
                self.assertEqual(href, '../reference/industry-body-of-knowledge/')
                doc_page = ru.by_id['services/business-model']
                doc_html = build.build_page(ru, doc_page, 'ru')
                self.assertIn('AICC-MND-03-RU', doc_html)
                self.assertIn('Версия английского оригинала', doc_html)
                self.assertIn('charter/ru/documents/business-model.md', doc_html)
                control_html = build.build_page(ru, ru.by_id['governance/controls/c-04'], 'ru')
                self.assertIn('Проверка документов', control_html)
                self.assertNotIn('class="o-callout lang-note"', control_html)
                self.assertIn('<dd lang="ru">', control_html)
                home = build.build_page(ru, ru.by_id['index'], 'ru')
                self.assertIn('Аналитика клиентов', home)
                strategy = build.build_page(ru, ru.by_id['about/strategy'], 'ru')
                self.assertIn('Аналитика клиентов', strategy)
                about = build.build_page(ru, ru.by_id['about/index'], 'ru')
                self.assertIn('Аналитика клиентов', about)
                self.assertIn('<table lang="ru">', about)
                records_html = build.build_page(ru, ru.by_id['reference/records-and-systems'], 'ru')
                self.assertEqual(len(ru.tpl_desc), 14)
                decision_row = next(row for row in records_html.split('</tr>') if 'Запись о решении' in row)
                self.assertIn('/governance/controls/c-04/', decision_row)
                context = {'source': 'charter/ru/documents/business-model.md', 'lang': 'ru', 'url': '/ru/services/business-model/'}
                self.assertIn('class="xref"', ru.link_xrefs('Бизнес-модель 4.8', context))
                fallback_page = ru.by_id['reference/vocabulary']
                fallback = build.build_page(ru, fallback_page, 'ru')
                self.assertIn('class="o-callout lang-note"', fallback)
                self.assertIn('<div class="o-doc" lang="en">', fallback)
                self.assertIn('AICC-REF-01-EN', fallback)
                en = build.Site(argparse.Namespace(no_diagrams=True), 'en')
                build.add_generated_pages(en); build.assign_refs(en); build.load_terms(en); build.render_pages(en)
                self.assertNotIn('Проверка русской поставки', en.bodies['delivery/index']['html'])
                self.assertEqual(en.by_id['delivery/index']['ref'], ru.by_id['delivery/index']['ref'])


if __name__ == '__main__':
    unittest.main()
