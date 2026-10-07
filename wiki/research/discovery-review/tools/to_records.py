#!/usr/bin/env python3
"""One-time conversion of the Discovery Catalog pages into Markdown records.

Reads the retained pages html-alt/financial-services/{en,ru}/**/index.html and writes one record per page to
portfolio/{en,ru}/discovery/<path>.md in the format described in portfolio/en/discovery/README.md. The Russian
records carry the translation pin of their English records.

  to_records.py write    convert every page and write the records
  to_records.py verify   regenerate every page from the records (portal/tools/discovery.py) and compare it with the
                         retained page: same elements, attributes and text, whitespace aside

The pages were generated from templates that are no longer in the repository, so their markup is regular; the parser
below asserts that regularity and fails on anything it does not recognise instead of guessing. The retained pages were
removed once the records were verified (change C-SITE-BOUNDED-BRANCHES, T-003); to rerun this tool, restore
html-alt/financial-services from the history first.
"""
import hashlib
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / 'html-alt/financial-services'
sys.path.insert(0, str(ROOT / 'portal/tools'))
import discovery  # noqa: E402

LANGS = ('en', 'ru')


def text(markup):
    """Visible text of an element's content as record text: entities decoded, emphasis as Markdown, one line."""
    parts = []
    for token in re.split(r'(</?(?:strong|em)>)', markup):
        if token in ('<strong>', '</strong>'):
            parts.append('**')
        elif token in ('<em>', '</em>'):
            parts.append('*')
        elif '<' in token.replace('&lt;', ''):
            raise ValueError(f'Unexpected markup in text: {markup[:120]}')
        else:
            parts.append(discovery.md_escape(unescape(token)))
    return re.sub(r'\s*\n\s*', ' ', ''.join(parts)).strip()


def attr(markup, name):
    match = re.search(r'\b' + name + r'="([^"]*)"', markup)
    if not match:
        raise ValueError(f'Missing attribute {name}: {markup[:120]}')
    return unescape(match[1])


def one(pattern, markup, what):
    found = re.findall(pattern, markup, re.S)
    if len(found) != 1:
        raise ValueError(f'Expected one {what}, found {len(found)}')
    return found[0]


CONSTANTS = {lang: {} for lang in LANGS}


def constant(lang, key, value):
    """Interface labels repeat on every page; record them once and require them to agree with the generator."""
    seen = CONSTANTS[lang].setdefault(key, value)
    if seen != value:
        raise ValueError(f'{lang}: interface label {key} varies: {seen!r} / {value!r}')


def scenario(markup, lang):
    labels = re.findall(r'<div class="scenario-section__label">(.*?)</div>', markup)
    dims = re.findall(r'<div class="okr-kr__dim">(.*?)</div>', markup)
    constant(lang, 'sections', tuple(unescape(x) for x in labels))
    constant(lang, 'dimensions', tuple(unescape(x) for x in dims))
    constant(lang, 'complexity', attr(one(r'<span\s+class="scenario-complexity[^"]*"\s+title="[^"]*"\s*>', markup, 'complexity'), 'title'))
    lens_class, lens = one(r'<span class="scenario-lens scenario-lens--([\w-]+)">(.*?)</span>', markup, 'lens')
    constant(lang, 'lens:' + unescape(lens), lens_class)
    complexity_class, complexity = one(r'class="scenario-complexity scenario-complexity--(\w+)"\s+title="[^"]*"\s*>(\w+)</span>', markup, 'complexity value')
    if complexity_class != complexity:
        raise ValueError('Complexity class and value differ')
    paragraphs = re.findall(r'<div class="scenario-section__label">[^<]*</div>\s*<p>(.*?)</p>', markup, re.S)
    results = re.findall(r'<div class="okr-kr__dim">[^<]*</div>\s*<p>(.*?)</p>', markup, re.S)
    if len(paragraphs) != 2 or len(results) != 3:
        raise ValueError('Unexpected scenario sections')
    return {
        'urn': attr(markup, 'data-urn'),
        'title': text(one(r'<h3 class="scenario-card__title">(.*?)</h3>', markup, 'title')),
        'lens': text(lens),
        'complexity': complexity,
        'intent': text(one(r'<p class="scenario-card__intent">(.*?)</p>', markup, 'intent')),
        'problem': text(paragraphs[0]),
        'solution': text(paragraphs[1]),
        'objective': text(one(r'<p class="okr-objective">(.*?)</p>', markup, 'objective')),
        'results': [text(x) for x in results],
    }


def scenarios(markup, lang):
    cards = re.findall(r'<details class="scenario-card" data-urn="[^"]+">.*?</details>', markup, re.S)
    return [scenario(card, lang) for card in cards]


def problem_rows(markup):
    rows = re.findall(r'<tr class="problems-row">\s*<th class="problems-lens" scope="row">(.*?)</th>\s*'
                      r'<td class="problems-statement">(.*?)</td>\s*</tr>', markup, re.S)
    if len(rows) != markup.count('<tr'):
        raise ValueError('Unrecognized problem rows')
    return [[text(lens), text(statement)] for lens, statement in rows]


def problems(markup, lang):
    if '<section class="concern-problems"' not in markup:
        return []
    section = one(r'<section class="concern-problems" aria-label="([^"]*)">', markup, 'problems section')
    constant(lang, 'problems', unescape(section))
    categories = []
    for slug, label in re.findall(r'<label\s+class="problems-tab-label"\s+for="problems-tab-([^"]+)"[^>]*>(.*?)</label>', markup, re.S):
        panel = one(r'<div\s+class="problems-panel"\s+id="problems-panel-' + re.escape(slug) + r'".*?</table>', markup, 'panel ' + slug)
        aria = attr(one(r'<input[^>]*id="problems-tab-' + re.escape(slug) + r'"[^>]*>', markup, 'input ' + slug), 'aria-label')
        if aria != unescape(label.strip()):
            raise ValueError(f'Tab name differs from its label: {slug}')
        categories.append({'id': slug, 'label': text(label), 'rows': problem_rows(panel)})
    return categories


def header(markup, lang):
    constant(lang, 'breadcrumb', unescape(re.search(r'<nav class="breadcrumb" aria-label="([^"]*)">', markup)[1]))
    constant(lang, 'skip', unescape(one(r'<a class="skip-link" href="#main-content">(.*?)</a>', markup, 'skip link')))
    constant(lang, 'footer', unescape(one(r'<footer class="page-footer" role="contentinfo">(.*?)</footer>', markup, 'footer')))
    title = one(r'<h1 class="page-header__title">(.*?)</h1>', markup, 'title')
    intents = re.findall(r'<p class="page-header__intent">(.*?)</p>', markup, re.S)
    return {'title': text(title), 'intent': text(intents[0]) if intents else ''}


def item_id(href):
    """A card item names a section of a capability page (area pages) or a capability page (home page)."""
    return href.split('#', 1)[1] if '#' in href else href.split('/')[1]


def card(markup, lang):
    target = attr(one(r'<a class="card__click-target"[^>]*>', markup, 'card target'), 'href')
    number, noun = one(r'<span class="card__count" aria-label="([^"]*)">', markup, 'count').split(' ', 1)
    constant(lang, f'count:{discovery.plural_form(int(number), lang)}', noun)
    entry = {'id': target.split('/')[-2],
             'group': text(one(r'<div class="card__eyebrow">(.*?)</div>', markup, 'group')),
             'title': text(one(r'<h[23] class="card__title[^"]*">(.*?) <span class="card__count"', markup, 'card title'))}
    if 'card--flow' in markup:
        entry['flows'] = [[text(label), text(list_label), [href.split('#', 1)[1] for href in re.findall(r'<a href="([^"]+)" class="flow-item__name', items)]]
                          for label, list_label, items in re.findall(r'<div class="flow-section__label">(.*?)</div>\s*<ul class="flow-list" aria-label="([^"]*)">(.*?)</ul>', markup, re.S)]
    else:
        entry['groups'] = [[text(label), [item_id(href) for href in re.findall(r'<a class="card-link" href="([^"]+)"', items)]]
                           for label, items in re.findall(r'<div class="sub-group__label">(.*?)</div>\s*<div class="sub-group__items">(.*?)</div>', markup, re.S)]
    return entry


def area_page(markup, lang):
    page = {'kind': 'area', **header(markup, lang), 'problems': problems(markup, lang)}
    main = one(r'<main id="main-content" aria-label="([^"]*)">', markup, 'main')
    constant(lang, 'main:area', unescape(main))
    page['cards'] = [card(x, lang) for x in re.findall(r'<article class="card[^"]*">.*?</article>', markup, re.S)]
    section = markup.split('</main>', 1)[1]
    constant(lang, 'scenarios', unescape(one(r'<section class="concern-scenarios" aria-label="([^"]*)">', section, 'scenarios')))
    constant(lang, 'scenarios-eyebrow', unescape(one(r'<div class="scenarios-eyebrow">(.*?)</div>', section, 'eyebrow')))
    constant(lang, 'scenarios-heading', unescape(one(r'<h2 class="scenarios-heading">(.*?)</h2>', section, 'heading')))
    page['scenarios'] = scenarios(section, lang)
    return page


def capability_page(markup, lang):
    page = {'kind': 'capability', **header(markup, lang), 'problems': problems(markup, lang)}
    constant(lang, 'main:capability', attr(one(r'<main id="main-content" class="l3-sections"[^>]*>', markup, 'main'), 'aria-label'))
    page['sections'] = []
    for slug, body in re.findall(r'<section class="l3-section" id="([^"]+)">(.*?)</section>', markup, re.S):
        page['sections'].append({'id': slug, 'title': text(one(r'<h2 class="l3-section__title">(.*?)</h2>', body, 'section title')),
                                 'intent': text(one(r'<p class="l3-section__intent">(.*?)</p>', body, 'section intent')),
                                 'scenarios': scenarios(body, lang)})
    return page


def flows_page(markup, lang):
    page = {'kind': 'flows', **header(markup, lang), 'problems': []}
    flow_set = re.search(r'<section class="flow-problems" aria-label="([^"]*)">(.*?)</section>', markup, re.S)
    if flow_set:
        constant(lang, 'flow-set-problems', unescape(flow_set[1]))
        page['problems'] = problem_rows(flow_set[2])
    constant(lang, 'main:flows', attr(one(r'<main id="main-content" class="flow-categories"[^>]*>', markup, 'main'), 'aria-label'))
    stages = json.loads(one(r'const FLOW_STAGES = (\{.*?\});\n', markup, 'stage map'))
    constant(lang, 'close', unescape(one(r'<button class="modal__close" type="button" aria-label="([^"]*)">', markup, 'close')))
    constant(lang, 'stage-problem', json.loads(one(r'problem: ("[^"]*"),', markup, 'stage label')))
    page['categories'] = []
    for slug, body in re.findall(r'<section class="flow-category" id="([^"]+)">(.*?)(?=<section class="flow-category"|</main>)', markup, re.S):
        category = {'id': slug, 'title': text(one(r'<h2 class="flow-category__title">(.*?)</h2>', body, 'category')), 'flows': []}
        for flow_id, detail in re.findall(r'<details class="flow-detail" id="([^"]+)">(.*?)(?=<details class="flow-detail"|$)', body, re.S):
            urns = set(re.findall(r'data-flow-id="([^"]+)"', detail))
            if len(urns) != 1:
                raise ValueError(f'Flow without one identity: {flow_id}')
            urn = urns.pop()
            buttons = re.findall(r'data-stage="([^"]+)"[^>]*>\s*<span class="flow-stages__stage-label">(.*?)</span>', detail, re.S)
            constant(lang, 'flow-problems', attr(one(r'<section class="flow-detail__problems"[^>]*>', detail, 'flow problems'), 'aria-label'))
            constant(lang, 'flow-stages', attr(one(r'<nav class="flow-stages"[^>]*>', detail, 'stages'), 'aria-label'))
            constant(lang, 'scenarios', attr(one(r'<section class="concern-scenarios"[^>]*>', detail, 'scenarios'), 'aria-label'))
            stage_rows = [[discovery.md_escape(re.sub(r'\s*\n\s*', ' ', s[key]).strip()) for key in ('slug', 'label', 'title', 'intent', 'problem')] for s in stages.pop(urn)]
            if [(s[0], s[1]) for s in stage_rows] != [(slug, text(label)) for slug, label in buttons]:
                raise ValueError(f'Stage buttons differ from the stage map: {flow_id}')
            category['flows'].append({
                'id': flow_id, 'urn': urn,
                'title': text(one(r'<h3 class="flow-detail__title">(.*?)</h3>', detail, 'flow title')),
                'summary': text(one(r'<p class="flow-detail__intent">(.*?)</p>', detail, 'flow intent')),
                'description': [text(x) for x in re.findall(r'<p class="flow-detail__intent-full">(.*?)</p>', detail, re.S)],
                'problems': problem_rows(one(r'<section class="flow-detail__problems"[^>]*>(.*?)</section>', detail, 'flow problems')),
                'stages': stage_rows,
                'scenarios': scenarios(detail, lang)})
        page['categories'].append(category)
    if stages:
        raise ValueError(f'Stage map entries without a flow: {sorted(stages)}')
    return page


def home_page(markup, lang):
    page = {'kind': 'home', **header(markup, lang)}
    constant(lang, 'home-crumb', unescape(one(r'<span class="breadcrumb__current" aria-current="page">(.*?)</span>', markup, 'home crumb')))
    constant(lang, 'main:home', unescape(one(r'<main id="main-content" aria-label="([^"]*)">', markup, 'main')))
    constant(lang, 'regions', tuple(unescape(label) for label in re.findall(r'<div (?:class="[\w-]+" )?role="region" aria-label="([^"]*)">', markup)))
    page['areas'] = [card(x, lang) for x in re.findall(r'<article class="card(?! card--peer)[^"]*">.*?</article>', markup, re.S)]
    page['peers_title'] = text(one(r'<div class="peer-label" role="heading" aria-level="2">(.*?)</div>', markup, 'peer label'))
    page['peers'] = []
    for peer in re.findall(r'<article class="card card--peer">.*?</article>', markup, re.S):
        constant(lang, 'peer-group', unescape(one(r'<div class="card__eyebrow">(.*?)</div>', peer, 'peer group')))
        page['peers'].append({'title': text(one(r'<span class="card-link card-link--deferred">(.*?)</span>', peer, 'peer title')),
                              'text': text(one(r'<p class="card__pointer">(.*?)</p>', peer, 'peer text'))})
    return page


def parse(markup, relative, lang):
    """The record content of one retained page."""
    body = re.search(r'<body[^>]*>', markup)[0]
    if relative == 'index.html':
        return home_page(markup, lang)
    if 'page--flow-set' in body:
        return flows_page(markup, lang)
    if 'page--concern-l2' in body:
        return capability_page(markup, lang)
    if 'page--concern' in body:
        return area_page(markup, lang)
    raise ValueError(f'Unknown page family: {relative}')


def table(header, rows):
    lines = ['| ' + ' | '.join(header) + ' |', '| ' + ' | '.join('---' for _ in header) + ' |']
    return '\n'.join(lines + ['| ' + ' | '.join(row) + ' |' for row in rows])


def paragraph(value):
    if not value or value.startswith(('#', '|', '- ')):
        raise ValueError(f'Text cannot stand as a record paragraph: {value[:80]}')
    return value


def scenario_md(item, level, lang):
    labels = discovery.LABELS[lang]
    keys = [labels['key'][name] for name in ('urn', 'lens', 'complexity', 'intent')] + list(labels['sections'])
    values = [item['urn'], item['lens'], item['complexity'], item['intent'], item['problem'], item['solution'], item['objective']]
    return ['#' * level + ' ' + item['title'], '\n'.join(f'- {key}: {value}' for key, value in zip(keys, values)),
            table(labels['table']['results'], [[dimension, value] for dimension, value in zip(labels['dimensions'], item['results'])])]


def problems_md(categories, lang):
    labels = discovery.LABELS[lang]
    if not categories:
        return []
    out = ['## ' + labels['heading']['problems']]
    if isinstance(categories[0], dict):
        for category in categories:
            out += [f'### {category["label"]} {{#{category["id"]}}}', table(labels['table']['problems'], category['rows'])]
    else:
        out.append(table(labels['table']['problems'], categories))
    return out


def card_md(card, lang):
    labels = discovery.LABELS[lang]
    out = [f'### {card["title"]} {{#{card["id"]}}}', f'- {labels["key"]["group"]}: {card["group"]}']
    if 'flows' in card:
        out.append(table(labels['table']['flows'], [[label, name, ', '.join(ids)] for label, name, ids in card['flows']]))
    else:
        out.append(table(labels['table']['groups'], [[label, ', '.join(ids)] for label, ids in card['groups']]))
    return out


def markdown(page, lang):
    """The record of one page."""
    labels = discovery.LABELS[lang]
    out = ['# ' + page['title']]
    if page['intent']:
        out.append(paragraph(page['intent']))
    kind = page['kind']
    if kind == 'home':
        out.append('## ' + labels['heading']['overview'])
        for card in page['areas']:
            out += card_md(card, lang)
        out.append('## ' + page['peers_title'])
        for peer in page['peers']:
            out += ['### ' + peer['title'], paragraph(peer['text'])]
    elif kind == 'area':
        out += problems_md(page['problems'], lang)
        out.append('## ' + labels['heading']['overview'])
        for card in page['cards']:
            out += card_md(card, lang)
        out.append('## ' + labels['heading']['scenarios'])
        for item in page['scenarios']:
            out += scenario_md(item, 3, lang)
    elif kind == 'capability':
        out += problems_md(page['problems'], lang)
        for section in page['sections']:
            out += [f'## {section["title"]} {{#{section["id"]}}}', paragraph(section['intent'])]
            for item in section['scenarios']:
                out += scenario_md(item, 3, lang)
    else:
        out += problems_md(page['problems'], lang)
        for category in page['categories']:
            out.append(f'## {category["title"]} {{#{category["id"]}}}')
            for flow in category['flows']:
                out += [f'### {flow["title"]} {{#{flow["id"]}}}',
                        f'- {labels["key"]["urn"]}: {flow["urn"]}\n- {labels["key"]["summary"]}: {flow["summary"]}']
                out += [paragraph(text) for text in flow['description']]
                out += [table(labels['table']['problems'], flow['problems']), table(labels['table']['stages'], flow['stages'])]
                for item in flow['scenarios']:
                    out += scenario_md(item, 4, lang)
    return '\n\n'.join(out) + '\n'


def localized(relative, lang):
    """The retained page with the Russian child-page breadcrumb taken from its section (the retained publishing correction)."""
    markup = (SOURCE / lang / relative).read_text()
    parts = Path(relative).parts
    if lang != 'ru' or len(parts) != 3:
        return markup
    section = (SOURCE / 'ru' / parts[0] / 'index.html').read_text()
    title = re.search(r'<span class="breadcrumb__current" aria-current="page">([^<]+)</span>', section)[1]
    parent = r'(<a class="breadcrumb__link" href="../index.html">)([^<]+)(</a>)'
    if len(re.findall(parent, markup)) != 1:
        raise ValueError(f'Missing parent breadcrumb: {relative}')
    return re.sub(parent, lambda match: match[1] + title + match[3], markup, count=1)


def write():
    pins = {}
    for lang in LANGS:
        target = discovery.RECORDS[lang]
        for old in target.rglob('*.md'):
            if old.name != 'README.md':
                old.unlink()
        for path in sorted((SOURCE / lang).rglob('index.html')):
            relative = path.relative_to(SOURCE / lang).as_posix()
            record = discovery.record_path(relative)
            text = markdown(parse(localized(relative, lang), relative, lang), lang)
            if lang == 'en':
                pins[record] = hashlib.sha256(text.encode()).hexdigest()
            else:
                text = ('```yaml\n'
                        f'source: portfolio/en/discovery/{record.as_posix()}\n'
                        f'source_sha256: {pins[record]}\n'
                        'translation_status: reviewed\n'
                        '```\n\n') + text
            (target / record).parent.mkdir(parents=True, exist_ok=True)
            (target / record).write_text(text)
    for lang in LANGS:
        constants = CONSTANTS[lang]
        labels = discovery.LABELS[lang]
        expected = {'breadcrumb': labels['breadcrumb'], 'skip': labels['skip'], 'footer': labels['footer'], 'problems': labels['problems'],
                    'sections': labels['sections'], 'dimensions': labels['dimensions'], 'complexity': labels['columns'][3],
                    'scenarios': labels['scenarios'], 'close': labels['close'], 'stage-problem': labels['sections'][0],
                    'flow-problems': labels['flow-problems'], 'flow-stages': labels['flow-stages'], 'flow-set-problems': labels['flow-set-problems'],
                    'scenarios-eyebrow': labels['scenarios'], 'scenarios-heading': labels['scenarios'], 'home-crumb': labels['home'],
                    'peer-group': labels['peer'], 'regions': tuple(labels['regions'][name] for name in ('top-band', 'main-row', 'cap-row', 'data', 'peers')),
                    **{'main:' + key: value for key, value in labels['main'].items()},
                    **{'lens:' + key: value for key, value in labels['lens'].items()},
                    **{'count:' + key: value for key, value in labels['count'].items() if 'count:' + key in constants}}
        for key, value in expected.items():
            if constants.get(key) != value:
                raise ValueError(f'{lang}: interface label {key} is {constants.get(key)!r} in the pages, {value!r} in the generator')
    print(f'Wrote {len(pins)} records per language.')


BLOCK = {'html', 'head', 'body', 'div', 'p', 'h1', 'h2', 'h3', 'h4', 'section', 'header', 'footer', 'main', 'nav', 'article', 'details',
         'summary', 'table', 'tbody', 'tr', 'th', 'td', 'ul', 'li', 'hr', 'style', 'script', 'input', 'label', 'button', 'title', 'meta', 'link'}


class Tokens(HTMLParser):
    """Elements with their ordered attributes and the text between them. Whitespace counts only where it separates
    inline content (a space between two links shows); runs collapse, and it is dropped next to block boundaries.
    Style sheets are compared without comments."""

    def __init__(self, markup):
        super().__init__(convert_charrefs=True)
        self.items, self.raw = [], None
        self.feed(markup)
        self.close()
        self.tokens = self.normalized()

    def handle_starttag(self, tag, attrs):
        self.items.append(('<', tag, tuple((name, ' '.join((value or '').split())) for name, value in attrs)))
        self.raw = tag if tag in ('style', 'script') else None

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        self.items.append(('>', tag))
        self.raw = None

    def handle_data(self, data):
        if self.raw == 'style':
            data = re.sub(r'/\*.*?\*/', '', data, flags=re.S)
        data = re.sub(r'\s+', ' ', data)
        if self.items and self.items[-1][0] == 'text':
            self.items[-1] = ('text', re.sub(' +', ' ', self.items[-1][1] + data))
        elif data:
            self.items.append(('text', data))

    def normalized(self):
        out = []
        for index, item in enumerate(self.items):
            if item[0] != 'text':
                out.append(item)
                continue
            value = item[1]
            before = self.items[index - 1] if index else None
            after = self.items[index + 1] if index + 1 < len(self.items) else None
            if before is None or before[1] in BLOCK:
                value = value.lstrip()
            if after is None or after[1] in BLOCK:
                value = value.rstrip()
            if value:
                out.append(('text', value))
        return out


def body(markup):
    """What the Discovery projection takes from a page: the body without the language switch, and the style sheets."""
    inner = re.search(r'<body[^>]*>(.*?)</body>', markup, re.S)[1]
    inner = re.sub(r'<nav\b[^>]*>.*?</nav>', lambda m: '' if 'hreflang=' in m[0] else m[0], inner, flags=re.S)
    sheets = re.findall(r'<link rel="stylesheet" href="([^"]+)">', markup)
    return re.search(r'<body[^>]*>', markup)[0], sheets, Tokens(inner).tokens


def verify():
    import difflib
    differing = 0
    for lang in LANGS:
        for path in sorted((SOURCE / lang).rglob('index.html')):
            relative = path.relative_to(SOURCE / lang)
            before, after = body(localized(relative.as_posix(), lang)), body(discovery.source(relative, lang))
            if before != after:
                differing += 1
                print(f'{lang}/{relative}: differs')
                if before[:2] != after[:2]:
                    print('  body or style sheets:', before[:2], after[:2])
                for line in list(difflib.unified_diff([repr(t) for t in before[2]], [repr(t) for t in after[2]], lineterm='', n=1))[:12]:
                    print('  ' + line[:220])
    if [discovery.page_path(discovery.record_path(p)) for p in discovery.pages('en')] != list(discovery.pages('en')):
        raise ValueError('Record paths do not map back to their pages')
    print(f'{differing} pages differ' if differing else 'Every page has the same elements, attributes and text as the retained page.')
    return differing


if __name__ == '__main__':
    command = sys.argv[1] if len(sys.argv) > 1 else ''
    if command == 'write':
        write()
    elif command == 'verify':
        sys.exit(1 if verify() else 0)
    else:
        sys.exit(__doc__)
