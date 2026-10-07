# START_MODULE_CONTRACT
#   PURPOSE: Build the Discovery Catalog pages from their Markdown records.
#   SCOPE: Record reading, derived counts and titles, and the catalog page markup that the Discovery projection consumes.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   RECORDS - language roots of the catalog records (portfolio/<lang>/discovery)
#   ASSETS - catalog layout style sheets (styles/), copied into each edition
#   SCRIPT - catalog interaction script, published as assets/discovery.js
#   LABELS - interface labels of the catalog pages in each language
#   HOME_LAYOUT - placement and card style of each area on the overview page
#   STYLE_SHEETS, BODY_CLASS - layout style sheets and page class of each kind of page
#   md_escape, inline, plain - record text to and from page text
#   plural_form - plural category of a count in a language
#   record_path, page_path - map a page to its record and back
#   pages - every catalog page of an edition, in path order
#   record - read one record into its content
#   scenario_count - count the scenarios of a page, or of an area with its pages
#   STAGE_SCRIPT - stage dialog of a flow page with its stage map
#   source - render one catalog page
# END_MODULE_MAP
"""The Discovery Catalog source context: one Markdown record per catalog page, rendered into the catalog markup."""
import functools
from html import escape
import json
from pathlib import Path
import re

import workspace

ROOT = workspace.ROOT
RECORDS = {lang: ROOT / 'portfolio' / lang / 'discovery' for lang in ('en', 'ru')}
ASSETS = ROOT / 'portal/site/discovery'
SCRIPT = ROOT / 'portal/site/discovery.js'

# START_BLOCK_LABELS
# Interface labels repeat on every page and are not part of the records. Record keys (the labelled lines and
# table headers) are written in the language of the record.
LABELS = {
    'en': {
        'skip': 'Skip to main content', 'breadcrumb': 'Breadcrumb', 'root': 'service.eyebrow', 'home': 'Financial Services',
        'footer': 'GenAI-enabled Banking and Financial Services Framework · v11i',
        'problems': 'Problems', 'flow-set-problems': 'Flow-set problems', 'flow-problems': 'Flow lens problems',
        'flow-stages': 'Flow stages', 'scenarios': 'Scenarios', 'close': 'Close',
        'main': {'home': 'Framework overview', 'area': 'Concern overview', 'capability': 'Sub-concerns', 'flows': 'Flow categories'},
        'regions': {'top-band': 'Strategic layer', 'main-row': 'Value chain and capabilities', 'below-band': 'Value chain and capabilities',
                    'cap-row': 'Shared capabilities', 'data': 'Data and analytics foundation', 'peers': 'Peer frameworks'},
        'peer': 'Peer framework',
        'columns': ('Lens', 'Scenario', 'Intent', 'Complexity'),
        'sections': ('Problem to solve', 'Solution', 'OKR'),
        'dimensions': ('Adoption', 'Acceptance', 'Cycle'),
        'count': {'one': 'scenario', 'other': 'scenarios'},
        'lens': {'Insights': 'insights', 'Automation': 'automation', 'Enablement': 'enablement', 'Optimize': 'optimize', 'New opps': 'new-opps'},
        # Record keys
        'key': {'urn': 'URN', 'lens': 'Lens', 'complexity': 'Complexity', 'intent': 'Intent', 'group': 'Group', 'summary': 'Summary'},
        'heading': {'problems': 'Problems', 'overview': 'Overview', 'scenarios': 'Scenarios'},
        'table': {'problems': ('Lens', 'Problem'), 'results': ('Dimension', 'Key result'),
                  'stages': ('Key', 'Stage', 'Title', 'Description', 'Problem to solve'),
                  'groups': ('Sub-group', 'Items'), 'flows': ('Section', 'List name', 'Flows')},
    },
    'ru': {
        'skip': 'Перейти к основному содержимому', 'breadcrumb': 'Навигационная цепочка', 'root': 'service.eyebrow', 'home': 'Финансовые услуги',
        'footer': 'Фреймворк GenAI-банкинга и финансовых услуг · v11i',
        'problems': 'Проблемы', 'flow-set-problems': 'Проблемы потока', 'flow-problems': 'Проблемы потока по аспектам',
        'flow-stages': 'Этапы потока', 'scenarios': 'Сценарии', 'close': 'Закрыть',
        'main': {'home': 'Обзор фреймворка', 'area': 'Обзор раздела', 'capability': 'Подразделы', 'flows': 'Категории потоков'},
        'regions': {'top-band': 'Стратегический уровень', 'main-row': 'Цепочка создания стоимости и возможности',
                    'below-band': 'Цепочка создания стоимости и возможности', 'cap-row': 'Общие возможности',
                    'data': 'Данные и аналитика', 'peers': 'Партнёрские фреймворки'},
        'peer': 'Смежная модель',
        'columns': ('Аспект', 'Сценарий', 'Назначение', 'Сложность'),
        'sections': ('Решаемая задача', 'Решение', 'Критерии приёмки'),
        'dimensions': ('Внедрение', 'Принятие', 'Цикл'),
        'count': {'one': 'сценарий', 'few': 'сценария', 'many': 'сценариев'},
        'lens': {'Аналитика': 'insights', 'Автоматизация': 'automation', 'Поддержка': 'enablement', 'Оптимизация': 'optimize', 'Новые возможности': 'new-opps'},
        'key': {'urn': 'URN', 'lens': 'Аспект', 'complexity': 'Сложность', 'intent': 'Назначение', 'group': 'Группа', 'summary': 'Кратко'},
        'heading': {'problems': 'Проблемы', 'overview': 'Обзор', 'scenarios': 'Сценарии'},
        'table': {'problems': ('Аспект', 'Проблема'), 'results': ('Измерение', 'Ключевой результат'),
                  'stages': ('Ключ', 'Этап', 'Название', 'Описание', 'Решаемая задача'),
                  'groups': ('Подгруппа', 'Элементы'), 'flows': ('Раздел', 'Название списка', 'Потоки')},
    },
}
COMPLEXITY = ('S', 'M', 'L', 'XL')

# The overview page places each area in a fixed region with a fixed card style: (region, card class, heading level, large).
HOME_LAYOUT = {
    'strategic-portfolio': ('top-band', 'card', 2, True),
    'strategic-initiatives': ('top-band', 'card', 2, True),
    'value-streams': ('main-row', 'card card--flow', 2, True),
    'customer-market-intelligence': ('right-col', 'card card--teal', 3, False),
    'customer-channels': ('right-col', 'card card--teal', 3, False),
    'risk-control': ('right-col', 'card card--sage', 3, False),
    'shared-banking-capabilities': ('cap-row', 'card', 2, False),
    'finance-treasury': ('cap-row', 'card', 2, False),
    'banking-data-analytics': ('data', 'card card--data', 2, True),
}
STYLE_SHEETS = {
    'home': ('tokens.css', 'components.css', 'theme.css', 'layouts/service.css'),
    'area': ('tokens.css', 'components.css', 'theme.css', 'layouts/concern.css'),
    'capability': ('tokens.css', 'components.css', 'theme.css', 'layouts/concern.css', 'layouts/concern-l2.css'),
    'flows': ('tokens.css', 'components.css', 'theme.css', 'layouts/service.css', 'layouts/concern.css', 'layouts/flow-set.css'),
}
BODY_CLASS = {'home': '', 'area': 'page--concern', 'capability': 'page--concern page--concern-l2', 'flows': 'page--flow-set'}
# END_BLOCK_LABELS


# START_BLOCK_TEXT
def md_escape(value):
    """Plain text as record text: the characters with a meaning in a record are escaped."""
    return re.sub(r'([\\|*])', r'\\\1', value)


def _spans(value):
    for token in re.split(r'(\\[\\|*]|\*\*|\*)', value):
        if token:
            yield token


def inline(value):
    """Record text as page markup: **strong** and *emphasis*, everything else escaped."""
    out, open_tags = [], []
    for token in _spans(value):
        if token in ('**', '*'):
            tag = 'strong' if token == '**' else 'em'
            if open_tags and open_tags[-1] == tag:
                open_tags.pop()
                out.append(f'</{tag}>')
            else:
                open_tags.append(tag)
                out.append(f'<{tag}>')
        else:
            out.append(escape(token[1] if token.startswith('\\') else token, quote=False))
    if open_tags:
        raise ValueError(f'Unclosed emphasis in record text: {value}')
    return ''.join(out)


def plain(value):
    """Record text without emphasis, as an attribute value."""
    text = ''.join(token[1] if token.startswith('\\') else '' if token in ('**', '*') else token for token in _spans(value))
    return escape(text, quote=False).replace('"', '&quot;')


def plural_form(number, lang):
    if lang == 'en':
        return 'one' if number == 1 else 'other'
    if number % 10 == 1 and number % 100 != 11:
        return 'one'
    if 2 <= number % 10 <= 4 and not 12 <= number % 100 <= 14:
        return 'few'
    return 'many'
# END_BLOCK_TEXT


# START_BLOCK_RECORDS
def record_path(page):
    """The record of a catalog page: index.html, <area>/index.html, <area>/<page>/index.html."""
    parts = Path(page).parts[:-1]
    return Path('index.md') if not parts else Path(parts[0], 'index.md') if len(parts) == 1 else Path(parts[0], parts[1] + '.md')


def page_path(path):
    path = Path(path)
    if path == Path('index.md'):
        return Path('index.html')
    if path.name == 'index.md':
        return path.parent / 'index.html'
    return path.parent / path.stem / 'index.html'


@functools.cache
def pages(lang):
    """Every catalog page of an edition, in path order (the order of the pages and of the search index)."""
    return tuple(sorted(page_path(path.relative_to(RECORDS[lang])) for path in RECORDS[lang].rglob('*.md') if path.name != 'README.md'))


def _blocks(text):
    """Headings, paragraphs, keyed lists and tables of a record, in order."""
    text = re.sub(r'\A```yaml\n.*?```\n', '', text, flags=re.S)
    lines, blocks, index = text.split('\n'), [], 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
        elif line.startswith('#'):
            match = re.fullmatch(r'(#{1,6}) (.+?)(?: \{#([\w-]+)\})?', line.rstrip())
            if not match:
                raise ValueError(f'Malformed heading: {line}')
            blocks.append(('heading', len(match[1]), match[2], match[3]))
            index += 1
        elif line.startswith('|'):
            rows = []
            while index < len(lines) and lines[index].startswith('|'):
                rows.append([cell.strip() for cell in re.split(r'(?<!\\)\|', lines[index].strip()[1:-1])])
                index += 1
            if len(rows) < 2 or not all(re.fullmatch(r':?-{3,}:?', cell) for cell in rows[1]):
                raise ValueError(f'Malformed table: {rows[0]}')
            blocks.append(('table', tuple(rows[0]), rows[2:]))
        elif line.startswith('- '):
            items = []
            while index < len(lines) and lines[index].startswith('- '):
                items.append(lines[index][2:].strip())
                index += 1
            blocks.append(('list', items))
        else:
            paragraph = []
            while index < len(lines) and lines[index].strip() and not lines[index].startswith(('#', '|', '- ')):
                paragraph.append(lines[index].strip())
                index += 1
            blocks.append(('paragraph', ' '.join(paragraph)))
    return blocks


class _Reader:
    """Sequential reading of record blocks with the record's own keys."""

    def __init__(self, path, lang):
        self.path, self.lang, self.labels = path, lang, LABELS[lang]
        self.blocks, self.index = _blocks(path.read_text()), 0

    def error(self, message):
        return ValueError(f'{self.path.relative_to(ROOT)}: {message}')

    def peek(self, kind=None, level=None):
        block = self.blocks[self.index] if self.index < len(self.blocks) else None
        if block and (kind is None or block[0] == kind) and (level is None or block[1] == level):
            return block
        return None

    def take(self, kind, level=None):
        block = self.peek(kind, level)
        if not block:
            found = self.blocks[self.index][:3] if self.index < len(self.blocks) else 'end of record'
            raise self.error(f'expected {kind}{"" if level is None else " " + "#" * level}, found {found}')
        self.index += 1
        return block

    def heading(self, level, text=None, identified=None):
        block = self.take('heading', level)
        if text is not None and block[2] != text:
            raise self.error(f'expected heading {"#" * level} {text}, found {block[2]}')
        if identified is not None and bool(block[3]) != identified:
            raise self.error(f'heading identifier {"missing" if identified else "unexpected"}: {block[2]}')
        return block[2], block[3]

    def paragraphs(self):
        found = []
        while self.peek('paragraph'):
            found.append(self.take('paragraph')[1])
        return found

    def keys(self, *names):
        items = self.take('list')[1]
        labels = [self.labels['key'][name] for name in names]
        if len(items) != len(names) or not all(item.startswith(label + ': ') for item, label in zip(items, labels)):
            raise self.error(f'expected the lines {", ".join(labels)}, found {items}')
        return [item[len(label) + 2:].strip() for item, label in zip(items, labels)]

    def table(self, name):
        _, header, rows = self.take('table')
        expected = self.labels['table'][name]
        if header != expected or any(len(row) != len(expected) for row in rows):
            raise self.error(f'expected a table | {" | ".join(expected)} |, found {header}')
        return rows

    def scenario(self, level):
        """### Title, then the labelled lines URN, lens, complexity, intent, problem, solution and objective, then the key results."""
        title, _ = self.heading(level, identified=False)
        keys = [self.labels['key'][name] for name in ('urn', 'lens', 'complexity', 'intent')] + list(self.labels['sections'])
        items = self.take('list')[1]
        if len(items) != len(keys) or not all(item.startswith(key + ': ') for item, key in zip(items, keys)):
            raise self.error(f'scenario {title}: expected the lines {", ".join(keys)}')
        urn, lens, complexity, intent, problem, solution, objective = (item[len(key) + 2:].strip() for item, key in zip(items, keys))
        if lens not in self.labels['lens'] or complexity not in COMPLEXITY or not urn.startswith('urn:financial-services:scenario:'):
            raise self.error(f'scenario {urn}: unknown lens, complexity or identity')
        results = self.table('results')
        if [row[0] for row in results] != list(self.labels['dimensions']):
            raise self.error(f'scenario {urn}: expected the key results {", ".join(self.labels["dimensions"])}')
        return {'urn': urn, 'title': title, 'lens': lens, 'complexity': complexity, 'intent': intent,
                'problem': problem, 'solution': solution, 'objective': objective, 'results': [row[1] for row in results]}

    def scenarios(self, level):
        found = []
        while self.peek('heading', level):
            found.append(self.scenario(level))
        return found

    def problems(self):
        """Problem categories (### Category {#id} with a table each), or one table without categories."""
        categories = []
        heading = self.peek('heading', 2)
        if heading and heading[2] == self.labels['heading']['problems'] and not heading[3]:
            self.heading(2)
            if self.peek('table'):
                return self.table('problems')
            while self.peek('heading', 3) and self.peek('heading', 3)[3]:
                label, identifier = self.heading(3, identified=True)
                categories.append({'id': identifier, 'label': label, 'rows': self.table('problems')})
        return categories

    def card(self):
        title, identifier = self.heading(3, identified=True)
        group, = self.keys('group')
        if self.peek('table') and self.peek('table')[1] == self.labels['table']['flows']:
            return {'id': identifier, 'title': title, 'group': group,
                    'flows': [[label, name, _ids(items)] for label, name, items in self.table('flows')]}
        return {'id': identifier, 'title': title, 'group': group, 'groups': [[label, _ids(items)] for label, items in self.table('groups')]}

    def end(self):
        if self.index != len(self.blocks):
            raise self.error(f'unexpected content: {self.blocks[self.index][:3]}')


def _ids(cell):
    return [item.strip() for item in cell.split(',') if item.strip()]


@functools.cache
def record(lang, page):
    """The content of a catalog page from its record."""
    page = Path(page)
    path = RECORDS[lang] / record_path(page)
    reader = _Reader(path, lang)
    title, _ = reader.heading(1)
    intent = ' '.join(reader.paragraphs())
    labels = LABELS[lang]
    content = {'title': title, 'intent': intent}
    if page == Path('index.html'):
        reader.heading(2, labels['heading']['overview'])
        content['areas'] = []
        while reader.peek('heading', 3):
            content['areas'].append(reader.card())
        content['peers_title'], _ = reader.heading(2, identified=False)
        content['peers'] = []
        while reader.peek('heading', 3):
            peer_title, _ = reader.heading(3, identified=False)
            content['peers'].append({'title': peer_title, 'text': ' '.join(reader.paragraphs())})
        content['kind'] = 'home'
    elif any(block[0] == 'list' and block[1][0].startswith(labels['key']['urn'] + ': urn:financial-services:flow:') for block in reader.blocks):
        content['kind'], content['problems'], content['categories'] = 'flows', reader.problems(), []
        while reader.peek('heading', 2):
            category_title, category_id = reader.heading(2, identified=True)
            category = {'id': category_id, 'title': category_title, 'flows': []}
            while reader.peek('heading', 3):
                flow_title, flow_id = reader.heading(3, identified=True)
                urn, summary = reader.keys('urn', 'summary')
                category['flows'].append({'id': flow_id, 'urn': urn, 'title': flow_title, 'summary': summary,
                                          'description': reader.paragraphs(), 'problems': reader.table('problems'),
                                          'stages': reader.table('stages'), 'scenarios': reader.scenarios(4)})
            content['categories'].append(category)
    elif page.parent.parent == Path('.'):
        content['kind'], content['problems'] = 'area', reader.problems()
        reader.heading(2, labels['heading']['overview'])
        content['cards'] = []
        while reader.peek('heading', 3):
            content['cards'].append(reader.card())
        reader.heading(2, labels['heading']['scenarios'])
        content['scenarios'] = reader.scenarios(3)
    else:
        content['kind'], content['problems'], content['sections'] = 'capability', reader.problems(), []
        while reader.peek('heading', 2):
            section_title, section_id = reader.heading(2, identified=True)
            content['sections'].append({'id': section_id, 'title': section_title, 'intent': ' '.join(reader.paragraphs()),
                                        'scenarios': reader.scenarios(3)})
    reader.end()
    return content


def scenario_count(lang, page):
    """Every scenario of a catalog page."""
    content = record(lang, page)
    if content['kind'] == 'capability':
        return sum(len(section['scenarios']) for section in content['sections'])
    if content['kind'] == 'flows':
        return sum(len(flow['scenarios']) for category in content['categories'] for flow in category['flows'])
    if content['kind'] == 'area':
        return len(content['scenarios']) + sum(scenario_count(lang, other) for other in pages(lang)
                                               if other.parts[0] == page.parts[0] and other != page)
    raise ValueError(f'No scenario count for {page}')
# END_BLOCK_RECORDS


# START_BLOCK_MARKUP
def _count(number, lang):
    return f'{number} {LABELS[lang]["count"][plural_form(number, lang)]}'


def _breadcrumb(page, content, lang):
    labels, depth = LABELS[lang], len(page.parts) - 1
    up = '../' * depth
    if depth == 0:
        items = [f'<span class="breadcrumb__current" aria-current="page">{escape(labels["home"])}</span>']
    else:
        items = [f'<a class="breadcrumb__link" href="{up}index.html">{labels["root"]}</a>']
        if depth == 2:
            items.append(f'<a class="breadcrumb__link" href="../index.html">{inline(record(lang, Path(page.parts[0], "index.html"))["title"])}</a>')
        items.append(f'<span class="breadcrumb__current" aria-current="page">{inline(content["title"])}</span>')
    spans = [items[0]] + ['<span class="breadcrumb__sep" aria-hidden="true">/</span>\n    ' + item for item in items[1:]]
    return (f'<nav class="breadcrumb" aria-label="{labels["breadcrumb"]}">\n'
            + ''.join(f'  <span class="breadcrumb__item">\n    {item}\n  </span>\n' for item in spans) + '</nav>')


def _header(content, lang):
    title = inline(content['title'])
    intent = f'\n  <p class="page-header__intent">{inline(content["intent"])}</p>' if content['intent'] else ''
    return ('<header class="page-header" role="banner">\n  <div class="page-header__title-row">\n    <div>\n'
            f'      <h1 class="page-header__title">{title}</h1>\n    </div>\n  </div>{intent}\n</header>')


def _problem_rows(rows, indent):
    pad = ' ' * indent
    return ''.join(f'{pad}<tr class="problems-row">\n{pad}  <th class="problems-lens" scope="row">{inline(lens)}</th>\n'
                   f'{pad}  <td class="problems-statement">{inline(statement)}</td>\n{pad}</tr>\n' for lens, statement in rows)


def _problems(categories, lang):
    """Problem categories as radio tabs; the selected tab shows its panel."""
    if not categories:
        return ''
    rules = ''.join(
        f'  #problems-tab-{c["id"]}:checked ~ .problems-tab-bar label[for="problems-tab-{c["id"]}"] {{\n'
        '    color: var(--ink-accent);\n    border-bottom-color: var(--ink-accent);\n    background: var(--paper-blue-soft);\n    font-weight: 600;\n  }\n'
        f'  #problems-tab-{c["id"]}:checked ~ .problems-panel[data-tab="{c["id"]}"] {{\n    display: block;\n  }}\n' for c in categories)
    inputs = ''.join(f'  <input type="radio" class="problems-tab-input" name="problems-tabs" id="problems-tab-{c["id"]}" value="{c["id"]}"'
                     f'{" checked" if index == 0 else ""} aria-label="{plain(c["label"])}">\n' for index, c in enumerate(categories))
    tabs = ''.join(f'    <label class="problems-tab-label" for="problems-tab-{c["id"]}" role="tab" aria-controls="problems-panel-{c["id"]}">'
                   f'{inline(c["label"])}</label>\n' for c in categories)
    panels = ''.join(f'  <div class="problems-panel" id="problems-panel-{c["id"]}" data-tab="{c["id"]}" role="tabpanel" aria-labelledby="problems-tab-{c["id"]}">\n'
                     f'    <table class="problems-table">\n      <tbody>\n{_problem_rows(c["rows"], 8)}      </tbody>\n    </table>\n  </div>\n' for c in categories)
    return (f'<style>\n{rules}</style>\n<section class="concern-problems" aria-label="{LABELS[lang]["problems"]}">\n{inputs}'
            f'  <div class="problems-tab-bar" role="tablist">\n{tabs}  </div>\n  <hr class="problems-divider">\n{panels}</section>\n')


def _columns(lang, extra=''):
    names = ('lens', 'scenario', 'intent', 'complexity')
    spans = ''.join(f'    <span class="scenarios-col-label scenarios-col-label--{name}">{label}</span>\n' for name, label in zip(names, LABELS[lang]['columns']))
    return f'  <div class="scenarios-column-labels{extra}" role="row" aria-hidden="true">\n{spans}  </div>\n'


def _scenario(item, lang):
    labels = LABELS[lang]
    results = ''.join(f'        <div class="okr-kr">\n          <div class="okr-kr__dim">{dimension}</div>\n          <p>{inline(text)}</p>\n        </div>\n'
                      for dimension, text in zip(labels['dimensions'], item['results']))
    problem, solution, okr = labels['sections']
    return (f'<details class="scenario-card" data-urn="{plain(item["urn"])}">\n'
            '  <summary class="scenario-card__summary">\n'
            f'    <span class="scenario-lens scenario-lens--{labels["lens"][item["lens"]]}">{inline(item["lens"])}</span>\n'
            '    <div class="scenario-card__title-col">\n      <span class="scenario-card__chevron" aria-hidden="true">▸</span>\n'
            f'      <h3 class="scenario-card__title">{inline(item["title"])}</h3>\n    </div>\n'
            f'    <div class="scenario-card__intent-col">\n      <p class="scenario-card__intent">{inline(item["intent"])}</p>\n    </div>\n'
            f'    <span class="scenario-complexity scenario-complexity--{item["complexity"]}" title="{labels["columns"][3]}">{item["complexity"]}</span>\n'
            '  </summary>\n  <div class="scenario-card__body">\n'
            f'    <div class="scenario-section">\n      <div class="scenario-section__label">{problem}</div>\n      <p>{inline(item["problem"])}</p>\n    </div>\n'
            f'    <div class="scenario-section">\n      <div class="scenario-section__label">{solution}</div>\n      <p>{inline(item["solution"])}</p>\n    </div>\n'
            f'    <div class="scenario-section">\n      <div class="scenario-section__label">{okr}</div>\n'
            f'      <p class="okr-objective">{inline(item["objective"])}</p>\n      <div class="okr-grid">\n{results}      </div>\n    </div>\n'
            '  </div>\n</details>\n')


def _scenarios(items, lang):
    return ''.join(_scenario(item, lang) for item in items)


def _capability_main(content, lang):
    sections = ''.join(
        f'<section class="l3-section" id="{section["id"]}">\n  <header class="l3-section__head">\n'
        f'    <h2 class="l3-section__title">{inline(section["title"])}</h2>\n    <p class="l3-section__intent">{inline(section["intent"])}</p>\n  </header>\n'
        f'{_columns(lang, " l3-section__column-labels")}  <div class="l3-section__scenarios">\n{_scenarios(section["scenarios"], lang)}  </div>\n</section>\n'
        for section in content['sections'])
    return f'<main id="main-content" class="l3-sections" aria-label="{LABELS[lang]["main"]["capability"]}">\n{sections}</main>\n'


def _card(card, href, count, items, css, level, large, lang):
    """An overview card: group, title with its scenario count, linked items, and the whole card as a link."""
    size = ' card__title--lg' if large else ''
    return (f'<article class="{css}">\n  <div class="card__head">\n    <div class="card__eyebrow">{inline(card["group"])}</div>\n'
            f'    <h{level} class="card__title{size}">{inline(card["title"])} <span class="card__count" aria-label="{_count(count, lang)}">({count})</span></h{level}>\n'
            f'  </div>\n  <div class="card__body">\n{items}  </div>\n'
            f'  <a class="card__click-target" href="{href}" tabindex="0" aria-label="{plain(card["title"])}"></a>\n</article>\n')


def _groups(groups):
    """Sub-groups of linked items: [(label, [(href, title, count)])]."""
    body = ''.join(
        f'      <div class="sub-group">\n        <div class="sub-group__label">{inline(label)}</div>\n        <div class="sub-group__items">\n'
        + '\n          <span class="dot" aria-hidden="true">·</span>\n'.join(
            f'          <a class="card-link" href="{href}">{inline(title)} <span class="card-link__count">({count})</span></a>' for href, title, count in links)
        + '\n        </div>\n      </div>\n' for label, links in groups)
    return f'    <div class="sub-groups sub-groups--row">\n{body}    </div>\n'


def _flow_sections(sections):
    """Flow sections of a workflow card: [(label, list name, [(href, title, count)])]."""
    body = ''.join(
        f'      <div class="flow-section">\n        <div class="flow-section__label">{inline(label)}</div>\n'
        f'        <ul class="flow-list" aria-label="{plain(name)}">\n'
        + ''.join(f'          <li class="flow-item">\n            <a href="{href}" class="flow-item__name card-link">{inline(title)} <span class="card-link__count">({count})</span></a>\n          </li>\n'
                  for href, title, count in links)
        + '        </ul>\n      </div>\n' for label, name, links in sections)
    return f'    <div class="flow-sections">\n{body}    </div>\n'


def _flow_links(lang, page, prefix, sections):
    """Workflow card sections with each flow's title and scenario count from the flow record."""
    flows = {flow['id']: flow for category in record(lang, page)['categories'] for flow in category['flows']}
    try:
        return [(label, name, [(f'{prefix}#{identifier}', flows[identifier]['title'], len(flows[identifier]['scenarios'])) for identifier in items])
                for label, name, items in sections]
    except KeyError as missing:
        raise ValueError(f'{lang}/{page}: no flow {missing}') from None


def _checked_title(lang, card, page):
    title = record(lang, page)['title']
    if card['title'] != title:
        raise ValueError(f'{lang}: card "{card["title"]}" differs from the title of {page}: "{title}"')


def _area_main(page, content, lang):
    """Capability cards and the workflow card of an area: two in the top band, the workflow card with two more, then the rest."""
    area = page.parts[0]
    rendered = []
    for card in content['cards']:
        target = Path(area, card['id'], 'index.html')
        _checked_title(lang, card, target)
        href = f'{card["id"]}/index.html'
        if 'flows' in card:
            items = _flow_sections(_flow_links(lang, target, href, card['flows']))
        else:
            sections = {section['id']: section for section in record(lang, target)['sections']}
            missing = [identifier for _, items in card['groups'] for identifier in items if identifier not in sections]
            if missing:
                raise ValueError(f'{lang}/{area}: no section {missing} in {card["id"]}')
            items = _groups([(label, [(f'{href}#{identifier}', sections[identifier]['title'], len(sections[identifier]['scenarios'])) for identifier in ids])
                             for label, ids in card['groups']])
        rendered.append((card, href, scenario_count(lang, target), items))
    flow_cards = [index for index, (card, *_) in enumerate(rendered) if 'flows' in card]
    if flow_cards != [2]:
        raise ValueError(f'{lang}/{area}: the workflow card is the third card of the overview')

    def cards(selected, level, large, css='card'):
        return ''.join(_card(card, href, count, items, css, level, large, lang) for card, href, count, items in selected)
    regions = LABELS[lang]['regions']
    return (f'<main id="main-content" aria-label="{LABELS[lang]["main"]["area"]}">\n<div class="bp-grid">\n'
            f'<div class="top-band" role="region" aria-label="{regions["top-band"]}">\n{cards(rendered[:2], 2, True)}</div>\n'
            f'<div class="main-row" role="region" aria-label="{regions["main-row"]}">\n{cards(rendered[2:3], 2, True, "card card--flow")}'
            f'<div class="right-col">\n{cards(rendered[3:5], 3, False)}</div>\n</div>\n'
            f'<div class="below-band" role="region" aria-label="{regions["below-band"]}">\n{cards(rendered[5:], 3, False)}</div>\n'
            '</div>\n</main>\n')


def _area_scenarios(content, lang):
    label = LABELS[lang]['scenarios']
    return (f'<section class="concern-scenarios" aria-label="{label}">\n  <div class="scenarios-header-row">\n'
            f'    <div class="scenarios-eyebrow">{label}</div>\n    <h2 class="scenarios-heading">{label}</h2>\n  </div>\n'
            f'{_columns(lang)}{_scenarios(content["scenarios"], lang)}</section>\n')


def _stages(flow, lang):
    buttons = []
    for index, (slug, label, *_) in enumerate(flow['stages']):
        arrow = '\n    <span class="flow-stages__arrow" aria-hidden="true">→</span>' if index < len(flow['stages']) - 1 else ''
        buttons.append(f'  <button class="flow-stages__stage" type="button" data-stage="{slug}" data-flow-id="{plain(flow["urn"])}">\n'
                       f'    <span class="flow-stages__stage-label">{inline(label)}</span>{arrow}\n  </button>\n')
    return f'<nav class="flow-stages" aria-label="{LABELS[lang]["flow-stages"]}">\n{"".join(buttons)}</nav>\n'


def _flow(flow, lang):
    description = ''.join(f'    <p class="flow-detail__intent-full">{inline(text)}</p>\n' for text in flow['description'])
    return (f'<details class="flow-detail" id="{flow["id"]}">\n  <summary class="flow-detail__summary">\n'
            f'    <div class="flow-detail__title-col">\n      <h3 class="flow-detail__title">{inline(flow["title"])}</h3>\n    </div>\n'
            f'    <p class="flow-detail__intent">{inline(flow["summary"])}</p>\n  </summary>\n  <div class="flow-detail__body">\n{description}'
            f'    <section class="flow-detail__problems" aria-label="{LABELS[lang]["flow-problems"]}">\n      <table class="problems-table">\n        <tbody>\n'
            f'{_problem_rows(flow["problems"], 10)}        </tbody>\n      </table>\n    </section>\n{_stages(flow, lang)}'
            f'<section class="concern-scenarios" aria-label="{LABELS[lang]["scenarios"]}">\n{_columns(lang)}{_scenarios(flow["scenarios"], lang)}</section>\n'
            '  </div>\n</details>\n')


def _flows_main(content, lang):
    problems = ''
    if content['problems']:
        problems = (f'<section class="flow-problems" aria-label="{LABELS[lang]["flow-set-problems"]}">\n  <table class="problems-table">\n    <tbody>\n'
                    f'{_problem_rows(content["problems"], 6)}    </tbody>\n  </table>\n</section>\n')
    categories = ''.join(
        f'<section class="flow-category" id="{category["id"]}">\n  <h2 class="flow-category__title">{inline(category["title"])}</h2>\n'
        f'  <div class="flow-category__table">\n{"".join(_flow(flow, lang) for flow in category["flows"])}  </div>\n</section>\n'
        for category in content['categories'])
    return problems + f'<main id="main-content" class="flow-categories" aria-label="{LABELS[lang]["main"]["flows"]}">\n{categories}</main>\n'


# The stage dialog of a flow page with the page's stage map, as the former catalog pages carried it.
STAGE_SCRIPT = '''<div class="modal" id="stageModal" role="dialog" aria-modal="true" aria-hidden="true">
  <div class="modal__panel">
    <button class="modal__close" type="button" aria-label="{close}">×</button>
    <div class="modal__content"></div>
  </div>
</div>

<script>
(function () {{
  // Per-flow stage map, embedded by the composer at render time.
  // Keyed by flow URN → list of stage objects.
  const FLOW_STAGES = {stages};
  const STAGE_LABELS = {{
    problem: {problem},
  }};

  const modalEl   = document.getElementById('stageModal');
  const contentEl = modalEl.querySelector('.modal__content');
  const closeBtn  = modalEl.querySelector('.modal__close');

  function openModal()  {{ modalEl.classList.add('is-open');    modalEl.setAttribute('aria-hidden', 'false'); }}
  function closeModal() {{ modalEl.classList.remove('is-open'); modalEl.setAttribute('aria-hidden', 'true');  }}

  closeBtn.addEventListener('click', closeModal);
  modalEl.addEventListener('click', (e) => {{ if (e.target === modalEl) closeModal(); }});
  document.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape' && modalEl.classList.contains('is-open')) closeModal();
  }});

  function escapeHtml(s) {{
    return String(s).replace(/[&<>"']/g, (c) => (
      {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]
    ));
  }}

  // Auto-open the <details> for a flow when arrived via #fragment
  // (e.g. linked from L1 page flow-card or top-page value-streams card —
  // clicking an individual flow name navigates here with #<flow-slug>).
  function openDetailsFromHash() {{
    const id = window.location.hash.slice(1);
    if (!id) return;
    const target = document.getElementById(id);
    if (target && target.tagName === 'DETAILS') {{
      target.open = true;
      // Defer scroll so the layout reflows after open.
      setTimeout(() => target.scrollIntoView({{ behavior: 'smooth', block: 'start' }}), 50);
    }}
  }}
  openDetailsFromHash();
  window.addEventListener('hashchange', openDetailsFromHash);

  document.querySelectorAll('.flow-stages__stage').forEach((btn) => {{
    btn.addEventListener('click', (e) => {{
      e.preventDefault();
      const stageSlug = btn.dataset.stage;
      const flowUrn   = btn.dataset.flowId;
      const stages    = FLOW_STAGES[flowUrn] || [];
      const stage     = stages.find((s) => s.slug === stageSlug) || {{}};
      contentEl.innerHTML = `
        <div class="modal__eyebrow">${{escapeHtml(stage.label || stageSlug)}}</div>
        <h3 class="modal__title">${{escapeHtml(stage.title || stage.label || stageSlug)}}</h3>
        ${{stage.intent  ? `<p class="modal__intent">${{escapeHtml(stage.intent)}}</p>` : ''}}
        ${{stage.problem ? `
          <div class="modal__problem">
            <div class="modal__problem-label">${{escapeHtml(STAGE_LABELS.problem)}}</div>
            <p>${{escapeHtml(stage.problem)}}</p>
          </div>` : ''}}
      `;
      openModal();
    }});
  }});
}})();
</script>
'''


def _stage_script(content, lang):
    stages = {flow['urn']: [dict(zip(('slug', 'label', 'title', 'intent', 'problem'), (_unescape_cell(cell) for cell in row))) for row in flow['stages']]
              for category in content['categories'] for flow in category['flows']}
    return STAGE_SCRIPT.format(close=LABELS[lang]['close'], stages=json.dumps(stages, ensure_ascii=False).replace('</', '<\\/'),
                               problem=json.dumps(LABELS[lang]['sections'][0]))


def _unescape_cell(value):
    return re.sub(r'\\([\\|*])', r'\1', value)


def _home_main(content, lang):
    """The overview: each area in its fixed region, then the peer frameworks."""
    regions = {name: [] for name in ('top-band', 'main-row', 'right-col', 'cap-row', 'data')}
    if [card['id'] for card in content['areas']] != list(HOME_LAYOUT):
        raise ValueError(f'{lang}: the overview lists the areas {list(HOME_LAYOUT)}')
    for card in content['areas']:
        region, css, level, large = HOME_LAYOUT[card['id']]
        target = Path(card['id'], 'index.html')
        _checked_title(lang, card, target)
        href = f'{card["id"]}/index.html'
        if 'flows' in card:
            items = _flow_sections(_flow_links(lang, target, href, card['flows']))
        else:
            items = _groups([(label, [(f'{card["id"]}/{identifier}/index.html', record(lang, Path(card['id'], identifier, 'index.html'))['title'],
                                       scenario_count(lang, Path(card['id'], identifier, 'index.html'))) for identifier in ids])
                             for label, ids in card['groups']])
        regions[region].append(_card(card, href, scenario_count(lang, target), items, css, level, large, lang))
    labels = LABELS[lang]['regions']
    peers = ''.join(f'<article class="card card--peer">\n  <div class="card__head">\n    <div class="card__eyebrow">{LABELS[lang]["peer"]}</div>\n'
                    f'    <h2 class="card__title"><span class="card-link card-link--deferred">{inline(peer["title"])}</span></h2>\n  </div>\n'
                    f'  <div class="card__body">\n    <p class="card__pointer">{inline(peer["text"])}</p>\n  </div>\n</article>\n' for peer in content['peers'])
    return (f'<main id="main-content" aria-label="{LABELS[lang]["main"]["home"]}">\n<div class="bp-grid">\n'
            f'<div class="top-band" role="region" aria-label="{labels["top-band"]}">\n{"".join(regions["top-band"])}</div>\n'
            f'<div class="main-row" role="region" aria-label="{labels["main-row"]}">\n{"".join(regions["main-row"])}'
            f'<div class="right-col">\n{"".join(regions["right-col"])}</div>\n</div>\n'
            f'<div class="cap-row" role="region" aria-label="{labels["cap-row"]}">\n{"".join(regions["cap-row"])}</div>\n'
            f'<div role="region" aria-label="{labels["data"]}">\n{"".join(regions["data"])}</div>\n'
            f'<div role="region" aria-label="{labels["peers"]}">\n<div class="peer-label" role="heading" aria-level="2">{inline(content["peers_title"])}</div>\n'
            f'<div class="peer-row">\n{peers}</div>\n</div>\n</div>\n</main>\n')


@functools.cache
def source(page, lang):
    """The catalog page as a complete document, in the markup that the Discovery projection (neighbours.py) reads."""
    page = Path(page)
    if page not in pages(lang):
        raise ValueError(f'No catalog page {lang}/{page}')
    content = record(lang, page)
    kind = content['kind']
    up = '../' * (len(page.parts) - 1)
    sheets = ''.join(f'<link rel="stylesheet" href="{up}assets/styles/{name}">\n' for name in STYLE_SHEETS[kind])
    if kind == 'home':
        main = _home_main(content, lang)
    elif kind == 'area':
        main = _problems(content['problems'], lang) + _area_main(page, content, lang) + _area_scenarios(content, lang)
    elif kind == 'capability':
        main = _problems(content['problems'], lang) + _capability_main(content, lang)
    else:
        main = _flows_main(content, lang)
    script = _stage_script(content, lang) if kind == 'flows' else ''
    body_class = f' class="{BODY_CLASS[kind]}"' if BODY_CLASS[kind] else ''
    labels = LABELS[lang]
    return (f'<!DOCTYPE html>\n<html lang="{lang}">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            f'<title>{plain(content["title"])}</title>\n{sheets}</head>\n<body{body_class}>\n'
            f'<a class="skip-link" href="#main-content">{labels["skip"]}</a>\n<div class="page">\n'
            '<div style="display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap;">\n'
            f'{_breadcrumb(page, content, lang)}\n</div>\n{_header(content, lang)}\n{main}'
            f'<footer class="page-footer" role="contentinfo">{labels["footer"]}</footer>\n</div>\n{script}</body>\n</html>\n')
# END_BLOCK_MARKUP
