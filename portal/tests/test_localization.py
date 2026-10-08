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

    def test_local_terminology_names_keep_definitions_and_repeated_tables_aligned(self):
        path = 'charter/en/shared-technology-terminology.md'
        en = ('| Universal term | Meaning | Application |\n| --- | --- | --- |\n'
              '| business case | Investment justification | Fixed form. |\n\n'
              '| Universal term | Meaning | Application |\n| --- | --- | --- |\n'
              '| workflow | Flow of work | Fixed form. |\n')
        ru = ('| EN | RU | Принятая форма | Определение |\n'
              '| --- | --- | --- | --- |\n'
              '| business case | бизнес-обоснование | бизнес-кейс | Обоснование инвестиции |\n\n'
              '| EN | RU | Принятая форма | Определение |\n'
              '| --- | --- | --- | --- |\n'
              '| workflow | рабочий процесс | Workflow | Поток работы |\n')
        (self.root / path).write_text(en)
        target = self.root / path.replace('/en/', '/ru/')
        target.write_text(translation(path, en, ru))
        sources = Sources(self.root, 'ru')
        first = sources.table(path, '| Universal term | Meaning')[0]
        second = sources.table(path, '| Universal term | Meaning', occurrence=1)[0]
        self.assertEqual(first['Universal term'], 'business case')
        self.assertEqual(first['Russian-language term'], 'бизнес-обоснование')
        self.assertEqual(first['Accepted form'], 'бизнес-кейс')
        self.assertEqual(first['Meaning'], 'Обоснование инвестиции')
        self.assertNotIn('Application', first)
        self.assertEqual(first['_labels']['Russian-language term'], 'RU')
        self.assertEqual(first['_labels']['Accepted form'], 'Принятая форма')
        self.assertEqual(second['Universal term'], 'workflow')
        self.assertEqual(second['Meaning'], 'Поток работы')
        self.assertNotIn('Russian-language term', Sources(self.root, 'en').table(path, '| Universal term')[0])
        malformed = [
            ru.replace('| RU | Принятая форма |', '| Принятая форма | RU |'),
            ru.replace('| бизнес-обоснование |', '| |'),
            ru.replace('| business case |', '| business plan |'),
            ru.replace('| Поток работы |', '| Поток работы | лишняя графа |'),
            ru.replace('| workflow | рабочий процесс | Workflow | Поток работы |\n', ''),
        ]
        for body in malformed:
            with self.subTest(body=body):
                target.write_text(translation(path, en, body))
                with self.assertRaisesRegex(ValueError, 'table structure'):
                    Sources(self.root, 'ru').resolve(path)
        # The extra column is not a general exemption for arbitrary documents.
        (self.root / self.path).write_text(en)
        self.ru.write_text(translation(self.path, en, ru))
        with self.assertRaisesRegex(ValueError, 'table structure'):
            self.select()


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
            templates_target.write_text(translation(templates_path, templates, templates.replace('Decision Record', 'Протокол решения')))
            catalog_path = 'charter/en/documents/document-catalog.md'
            catalog = (root / catalog_path).read_text()
            (root / 'charter/ru/documents/document-catalog.md').write_text(translation(catalog_path, catalog, catalog.replace('Operating Model', 'Операционная модель').replace('Document Catalog', 'Каталог документов')))
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
                records = [r for r in build.search_index(ru, 'ru') if r['u'].startswith('/ru/center/delivery/#')]
                self.assertTrue(any('Проверка русской поставки' in r['x'] for r in records))
                href = ru.map_link('../reference/industry-body-of-knowledge.md', {'source': str(target.relative_to(root)), 'lang': 'ru', 'url': '/ru/center/delivery/'})
                self.assertEqual(href, '../reference/industry-body-of-knowledge/')
                doc_page = ru.by_id['services/business-model']
                doc_html = build.build_page(ru, doc_page, 'ru')
                self.assertIn('AICC-MND-03-RU', doc_html)
                self.assertIn('Версия исходного документа', doc_html)
                self.assertIn('>Проект</span>', doc_html)
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
                decision_row = next(row for row in records_html.split('</tr>') if 'Протокол решения' in row)
                self.assertIn('/governance/controls/c-04/', decision_row)
                context = {'source': 'charter/ru/documents/business-model.md', 'lang': 'ru', 'url': '/ru/center/services/business-model/'}
                self.assertIn('class="xref"', ru.link_xrefs('Бизнес-модель 4.8', context))
                self.assertIn('class="xref"', ru.link_xrefs('Операционной модели 8.5', context))
                self.assertIn('#c-5-4', ru.link_xrefs('Каталоге документов 5.4', context))
                reference = ru.link_xrefs('Операционная модель, раздел 4', context)
                self.assertIn('href="../../organization/operating-model/roles/#s-4"', reference)
                self.assertIn('>Операционная модель, раздел 4</a>', reference)
                self.assertEqual(reference.count('<a '), 1)
                self.assertIn('#c-5-4', ru.link_xrefs('Каталог документов, пункт 5.4', context))
                reverse = ru.link_xrefs('в соответствии с разделом 4 Операционной модели', context)
                self.assertIn('href="../../organization/operating-model/roles/#s-4"', reverse)
                self.assertIn('>разделом 4 Операционной модели</a>', reverse)
                self.assertEqual(reverse.count('<a '), 1)
                self.assertIn('#c-5-4', ru.link_xrefs('(п. 5.4 Каталога документов)', context))
                self.assertIn('#c-5-4', ru.link_xrefs('согласно пункту 5.4 Каталога документов', context))
                listed = ru.link_xrefs('пункты 4.4, 4.5 и 4.10 Операционной модели', context)
                self.assertIn('>пункты 4.4, 4.5 и 4.10 Операционной модели</a>', listed)
                self.assertEqual(listed.count('<a '), 1)
                fallback_page = ru.by_id['reference/vocabulary']
                fallback = build.build_page(ru, fallback_page, 'ru')
                self.assertIn('class="o-callout lang-note"', fallback)
                self.assertIn('<div class="o-doc" lang="en">', fallback)
                self.assertIn('AICC-REF-01-EN', fallback)
                self.assertEqual(build.doc_id(ru, ru.by_id['organization/roles']), 'AICC-ORG-01-EN')
                en = build.Site(argparse.Namespace(no_diagrams=True), 'en')
                build.add_generated_pages(en); build.assign_refs(en); build.load_terms(en); build.render_pages(en)
                self.assertNotIn('Проверка русской поставки', en.bodies['delivery/index']['html'])
                self.assertEqual(en.by_id['delivery/index']['ref'], ru.by_id['delivery/index']['ref'])


class RussianCorpusProjection(unittest.TestCase):
    def test_business_case_search_distinguishes_the_concept_from_the_stage(self):
        for language, concept, stage, label in (
            ('en', 'justification for an investment', 'Preparing and approving', 'business case'),
            ('ru', 'Обоснование инвестиции', 'Подготовка и одобрение', 'бизнес-кейс'),
        ):
            with self.subTest(language=language):
                site = build.Site(argparse.Namespace(no_diagrams=True), language)
                build.add_generated_pages(site); build.assign_refs(site); build.load_terms(site); build.render_pages(site)
                page = site.by_id['reference/vocabulary']
                rendered = build.build_page(site, page, language)
                hits = [row for row in build.search_index(site, language)
                        if '/reference/vocabulary/#' in row['u']
                        and row['h'].lower().startswith(label)]
                self.assertEqual(len(hits), 2)
                self.assertEqual(len({row['u'] for row in hits}), 2)
                self.assertEqual(len({row['h'] for row in hits}), 2)
                for meaning in (concept, stage):
                    hit = next(row for row in hits if meaning in row['x'])
                    anchor = hit['u'].split('#')[1]
                    self.assertEqual(rendered.count('id="' + anchor + '"'), 1)
                    target = re.search(r'<tr id="' + re.escape(anchor) + r'">(.*?)</tr>', rendered, re.S)
                    self.assertIn(meaning, target.group(1))

    def test_page_titles_feedback_tables_and_card_ids_follow_the_selected_language(self):
        for language, home_title, about_title, table_label, suffix in (
            ('ru', 'Центр Компетенций по AI', 'О Центре Компетенций', 'Таблица', 'RU'),
            ('en', 'Welcome to the AI Competence Center', 'About the Competence Center', 'Table', 'EN'),
        ):
            with self.subTest(language=language):
                site = build.Site(argparse.Namespace(no_diagrams=True), language)
                build.add_generated_pages(site); build.assign_refs(site); build.load_terms(site); build.render_pages(site)
                for page_id, title in [('index', home_title), ('about/index', about_title)]:
                    rendered = build.build_page(site, site.by_id[page_id], language)
                    self.assertEqual(re.search(r'<title>(.*?)</title>', rendered)[1], title + ' · ' + {'en': 'Competence Center', 'ru': 'Центр Компетенций'}[language])
                    self.assertEqual(re.search(r'data-page="([^"]*)"', rendered)[1], title)
                hits = [e for e in build.search_index(site, language) if e['u'] == '/' + language + '/center/']
                self.assertEqual([e['t'] for e in hits], [home_title])
                catalog = build.build_page(site, site.by_id['reference/document-catalog'], language)
                for fragment in (catalog.split('<div class="o-doc"', 1)[1].split('<details', 1)[0],
                                 catalog.split('<details class="oc-disclosure change">', 1)[1]):
                    self.assertIn('aria-label="' + table_label + '"', fragment)
                    if language == 'ru':
                        self.assertNotIn('aria-label="Table"', fragment)
                for page_id, identifier in [('organization/roles', 'AICC-ORG-01-'),
                                            ('reference/records-and-systems', 'AICC-ORG-01-'),
                                            ('reference/change-history', 'AICC-REF-02-')]:
                    card = build.card(site, site.by_id[page_id], language, '/' + language + '/', '')
                    self.assertIn(identifier + suffix, card)

    def test_diagram_accessibility_is_localized_without_changing_ids_or_cached_svg(self):
        site = build.Site(argparse.Namespace(no_diagrams=True), 'ru')
        for kind, label in [('flowchart-v2', 'Блок-схема'), ('stateDiagram', 'Диаграмма состояний'),
                            ('sequence', 'Диаграмма последовательности')]:
            with self.subTest(kind=kind):
                svg = '<svg aria-roledescription="' + kind + '"><g id="Active"><text>В работе</text></g></svg>'
                site.svgs = {'abcdef123456': {'light': svg, 'dark': svg}}
                placeholder = '@@MM:abcdef123456:Рисунок 1@@'
                rendered = build.substitute(site, placeholder, 'ru')
                self.assertEqual(rendered.count('aria-roledescription="' + label + '"'), 2)
                self.assertEqual(rendered.count('id="Active"'), 2)
                self.assertEqual(site.svgs['abcdef123456']['light'], svg)
                english = build.substitute(site, placeholder, 'en')
                self.assertEqual(english.count('aria-roledescription="' + kind + '"'), 2)

    def test_reader_can_find_generated_reference_pages_by_their_titles(self):
        for language, records_title, history_title in (
            ('ru', 'Учётная система', 'История изменений'),
            ('en', 'Records and systems', 'Change history'),
        ):
            with self.subTest(language=language):
                site = build.Site(argparse.Namespace(no_diagrams=True), language)
                build.add_generated_pages(site); build.assign_refs(site); build.load_terms(site); build.render_pages(site)
                index = build.search_index(site, language)
                for title, route in ((records_title, 'records-and-systems'), (history_title, 'change-history')):
                    hits = [entry for entry in index if entry['h'] == title]
                    self.assertEqual([entry['u'] for entry in hits], ['/' + language + '/center/reference/' + route + '/'])

    def test_mandate_projections_follow_the_selected_corpus(self):
        site = build.Site(argparse.Namespace(no_diagrams=True), 'ru')
        build.add_generated_pages(site); build.assign_refs(site); build.load_terms(site); build.render_pages(site)
        statement = site.by_id['about/statement-of-intent']
        self.assertEqual(statement['title'], 'Заявление о намерениях по внедрению AI')
        self.assertEqual(build.nav_title(site, statement), 'Заявление о намерениях')
        values = build.build_page(site, site.by_id['about/values-and-principles'], 'ru')
        self.assertIn('Миссия Центра Компетенций — сделать AI', values)
        self.assertIn('<strong>Добросовестность</strong>', values)
        self.assertIn('Положение о Центре Компетенций по AI 2.1</a>', values)
        self.assertIn('Заявление о намерениях по внедрению AI 4</a>', values)
        self.assertIn('lang="ru"', values.split('id="g-work"', 1)[1].split('</section>', 1)[0])
        # Delivery principles follow the reviewed lifecycle model.
        self.assertIn('lang="ru"', values.split('id="g-delivery"', 1)[1].split('</section>', 1)[0])
        self.assertNotIn('class="o-callout lang-note"', values)
        for page_id in ('index', 'about/index', 'about/strategy'):
            html = build.build_page(site, site.by_id[page_id], 'ru')
            self.assertIn('Клиентская аналитика', html)
            self.assertIn('Разработка программного обеспечения', html)
        charter = build.build_page(site, site.by_id['about/aicc-charter'], 'ru')
        self.assertIn('AICC-MND-02-RU', charter)
        self.assertNotIn('class="o-callout lang-note"', charter)
        strategy = build.build_page(site, site.by_id['about/strategy'], 'ru')
        self.assertIn('<td lang="ru">Экспертные знания на рабочем месте;', strategy)
        self.assertNotIn('class="o-callout lang-note"', strategy)
        self.assertNotIn('&#x27;en&#x27;:', strategy)
        english = build.Site(argparse.Namespace(no_diagrams=True), 'en')
        build.add_generated_pages(english); build.assign_refs(english); build.load_terms(english); build.render_pages(english)
        english_strategy = build.build_page(english, english.by_id['about/strategy'], 'en')
        self.assertIn('<td lang="en">Expertise at the point of work;', english_strategy)
        self.assertNotIn('Экспертные знания на месте выполнения работы;', english_strategy)

    def test_russian_operating_diagrams_and_control_profiles_follow_the_corpus(self):
        site = build.Site(argparse.Namespace(no_diagrams=True), 'ru')
        build.add_generated_pages(site); build.assign_refs(site); build.load_terms(site)
        diagrams = build.render_pages(site)
        site.diagram_code = dict(diagrams)
        site.svgs = {key: {'light': '<svg></svg>', 'dark': '<svg></svg>'} for key, _ in diagrams}
        decisions = build.build_page(site, site.by_id['organization/operating-model/decisions'], 'ru')
        self.assertIn('aria-label="Рисунок 1: движение управленческого решения."', decisions)
        self.assertIn('<figcaption>Рисунок 1: движение управленческого решения.</figcaption>', decisions)
        controls = build.build_page(site, site.by_id['governance/controls'], 'ru')
        self.assertIn('AICC-ORG-01-RU', controls)
        self.assertIn('Операционная модель: Контрольные процедуры', controls)
        self.assertNotIn('class="o-callout lang-note"', controls)
        self.assertIn('<table id="ctl" lang="ru">', controls)
        tabs = build.parts_html(site, site.by_id['governance/controls'], 'ru')
        self.assertIn('Общие положения', tabs)
        self.assertIn('Циклы управления', tabs)
        self.assertIn('Рабочие и подтверждающие документы', tabs)
        self.assertEqual(build.nav_title(site, site.by_id['governance/control-loops']), 'Операционная модель')
        profile = build.build_page(site, site.by_id['governance/controls/c-04'], 'ru')
        self.assertNotIn('class="o-callout lang-note"', profile)
        self.assertIn('Документы согласованы между собой и действуют', profile)
        self.assertIn('Изучить отчёт о пересмотре', profile)
        # Multi-source indexes retain their own identity when one input is translated.
        self.assertEqual(site.by_id['organization/roles']['title'], 'Роли')
        self.assertEqual(site.by_id['reference/records-and-systems']['title'], 'Учётная система')
        records = build.build_page(site, site.by_id['reference/records-and-systems'], 'ru')
        self.assertIn('<h2>Системы</h2>', records)
        self.assertIn('<th>Контрольные процедуры</th>', records)
        self.assertNotIn('Decisions, appointments, controls, backlogs', records)

    def test_russian_role_and_guide_pages_keep_their_responsibilities_and_navigation(self):
        site = build.Site(argparse.Namespace(no_diagrams=True), 'ru')
        build.add_generated_pages(site); build.assign_refs(site); build.load_terms(site); build.render_pages(site)
        role = build.build_page(site, site.by_id['organization/roles/aicc-lead'], 'ru')
        self.assertIn('<h1>Руководитель Центра Компетенций</h1>', role)
        self.assertIn('Руководит Центром Компетенций как ведущий инженер и архитектор', role)
        self.assertIn('<th>Деятельность</th>', role)
        self.assertIn('Операционная модель 4.2</a>', role)
        self.assertIn('Присвоить категорию риска и сообщить её владельцу направления', role)
        self.assertNotIn('class="o-callout lang-note"', role)
        self.assertNotIn('<dd lang="en">', role)
        guide = site.by_id['organization/organization-guide']
        tabs = build.parts_html(site, guide, 'ru')
        self.assertIn('Распределение ответственности', tabs)
        self.assertNotIn('Who is responsible for what', tabs)
        self.assertEqual(site.by_id['governance/unit-governance-workflow/events-and-sequences']['title'],
                         'Workflow «Контроль работы подразделения»: События и последовательности')
        rendered = build.build_page(site, guide, 'ru')
        self.assertIn('<p class="o-lead" lang="ru">Роли, профили, матрица RACI и кадровый учёт</p>', rendered)

    def test_reader_can_find_a_late_glossary_term_and_open_its_definition(self):
        site = build.Site(argparse.Namespace(no_diagrams=True), 'ru')
        build.add_generated_pages(site); build.assign_refs(site); build.load_terms(site); build.render_pages(site)
        page = site.by_id['reference/vocabulary']
        html = build.build_page(site, page, 'ru')
        hits = [row for row in build.search_index(site, 'ru') if row['h'] == 'Степень серьёзности']
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]['u'], '/ru/center/reference/vocabulary/#t-степень-серьёзности')
        self.assertIn('id="t-степень-серьёзности"', html)
        self.assertIn('AICC-REF-01-RU', html)
        self.assertIn('<div class="o-doc" lang="ru">', html)
        self.assertIn('<p class="o-lead" lang="ru">Определения, толкование и стиль документов</p>', html)
        self.assertNotIn('class="o-callout lang-note"', html)

    def test_shared_terminology_table_entries_remain_searchable(self):
        for language in ('en', 'ru'):
            site = build.Site(argparse.Namespace(no_diagrams=True), language)
            build.add_generated_pages(site); build.assign_refs(site); build.load_terms(site); build.render_pages(site)
            page = site.by_id['reference/shared-terminology']
            html = build.build_page(site, page, language)
            self.assertEqual(site.bodies[page['id']]['language'], language)
            self.assertEqual(site.bodies[page['id']]['src'],
                             f'charter/{language}/shared-technology-terminology.md')
            self.assertNotIn('class="o-callout lang-note"', html)
            self.assertNotIn('Russian explanation', html)
            if language == 'en':
                self.assertNotRegex(site.bodies[page['id']]['raw'], '[А-Яа-яЁё]')
                self.assertEqual(html.count('<th>Universal term</th>'), 4)
                self.assertNotIn('Russian-language term</th>', html)
            else:
                self.assertEqual(html.count('<th>EN</th>'), 4)
                self.assertEqual(html.count('<th>RU</th>'), 4)
                self.assertEqual(html.count('<th>Принятая форма</th>'), 4)
                self.assertIn('<th>Определение</th>', html)
            entries = [row for row in build.search_index(site, language)
                       if '/reference/shared-terminology/' in row['u']]
            for term, section in [('KPI', 's-3'), ('workflow', 's-4'), ('WSJF', 's-4'),
                                  ('Finite State Machine / FSM', 's-5'), ('tool gateway', 's-5'),
                                  ('Amazon CloudWatch / CloudWatch', 's-6')]:
                with self.subTest(language=language, term=term):
                    hits = [entry for entry in entries if entry['h'] == term
                            or entry['h'].startswith(term + ' — ')]
                    self.assertEqual(len(hits), 1)
                    self.assertEqual(hits[0]['u'], f'/{language}/center/reference/shared-terminology/#{section}')
                    self.assertIn(f'id="{section}"', html)
                    self.assertIn(term, html)
                    self.assertTrue(hits[0]['x'])
                    if term == 'Finite State Machine / FSM':
                        self.assertIn('Конечный автомат' if language == 'ru' else 'A behavioral model',
                                      hits[0]['x'])
            if language == 'ru':
                hits = [e for e in entries if e['h'] == 'business case — бизнес-кейс']
                self.assertEqual(len(hits), 1)
                self.assertTrue(hits[0]['u'].endswith('#s-3'))
                self.assertIn('Обоснование инвестиции', hits[0]['x'])

    def test_translated_template_can_be_copied_and_outline_identifies_its_language(self):
        site = build.Site(argparse.Namespace(no_diagrams=True), 'ru')
        build.add_generated_pages(site); build.assign_refs(site); build.load_terms(site); build.render_pages(site)
        template = build.build_page(site, site.by_id['knowledge-base/acceptance-checklist'], 'ru')
        copied = re.search(r'<script type="text/markdown" id="tpl-src">(.*?)</script>', template, re.S)[1]
        self.assertTrue(copied.startswith('# Контрольный лист приёмки'))
        self.assertIn('При наличии невыполненного пункта выпуск не допускается', copied)
        self.assertNotIn('```yaml', copied)
        self.assertIn('AICC-TPL-13-RU', template)
        self.assertNotIn('class="o-callout lang-note"', template)
        outline = build.build_page(site, site.by_id['about/charter-outline'], 'ru')
        description = 'Мероприятия циклов по неделям, итерациям и PI, без дат'
        self.assertIn('<span lang="ru"> &mdash; ' + description, outline)
        # All authored explanations now come from reviewed Russian sources.
        self.assertNotIn('<span lang="en"> &mdash; ', outline)
        self.assertNotIn('class="o-callout lang-note"', outline)
        tabs = build.parts_html(site, site.by_id['services/engagement-workflow'], 'ru')
        self.assertIn('>Workflow</a>', tabs)
        self.assertIn('>Руководство</a>', tabs)
        self.assertNotIn('Engagement workflow', tabs)
        en = build.Site(argparse.Namespace(no_diagrams=True), 'en')
        build.add_generated_pages(en); build.assign_refs(en); build.load_terms(en); build.render_pages(en)
        original = build.build_page(en, en.by_id['knowledge-base/acceptance-checklist'], 'en')
        original_copy = re.search(r'<script type="text/markdown" id="tpl-src">(.*?)</script>', original, re.S)[1]
        self.assertTrue(original_copy.startswith('# Acceptance Checklist'))
        self.assertNotIn('```yaml', original_copy)

    def test_reader_can_find_a_template_without_section_headings(self):
        for language, title in [('ru', 'Заключение контрольной функции'), ('en', 'Control Sign-Off')]:
            site = build.Site(argparse.Namespace(no_diagrams=True), language)
            build.add_generated_pages(site); build.assign_refs(site); build.load_terms(site); build.render_pages(site)
            hits = [row for row in build.search_index(site, language)
                    if row['u'] == '/' + language + '/center/knowledge-base/control-sign-off/']
            self.assertEqual(len(hits), 1, language)
            self.assertEqual(hits[0]['t'], title)
            self.assertTrue(hits[0]['x'])


if __name__ == '__main__':
    unittest.main()
