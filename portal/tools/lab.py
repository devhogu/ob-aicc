# START_MODULE_CONTRACT
#   PURPOSE: Project the complete retained laboratory operating model into AI Lab.
#   SCOPE: Source extraction, paired translation, native presentation and local search.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   SOURCE - retained English laboratory source
#   TRANSLATION - Russian content keyed to source units
#   UI - bilingual reading controls and local section names
#   source_content - extract every authored content unit and structural assignment
#   content_hash - translation freshness identity for the extracted content
#   edition - require a complete, current language edition
#   render - build native laboratory content and search destinations
#   build - package both editions and local reading assets in the common shell
# END_MODULE_MAP
"""The predecessor is a build input, never a publication dependency."""
from html import escape
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re
import shutil

import workspace

SOURCE = workspace.ROOT / 'html-alt/cloudlab/index.html'
TRANSLATION = workspace.ROOT / 'portal/sections/lab/ru/content.json'
UI = {
    'en': {'concept': 'Concept', 'matrix': 'Validation workflow', 'systems': 'Operating model',
           'capabilities': 'Capabilities', 'loop': 'Intent loop', 'guardrails': 'Guardrails',
           'stages': 'Stage', 'lanes': 'Workstream', 'all': 'All', 'reset': 'Show complete workflow',
           'empty': 'No separate activity specified', 'coverage': 'Illustrative coverage',
           'concern': 'Concern', 'posture': 'Posture', 'selection': 'Workflow view'},
    'ru': {'concept': 'Концепция', 'matrix': 'Проверка гипотез', 'systems': 'Операционная модель',
           'capabilities': 'Возможности', 'loop': 'Цикл взаимодействия', 'guardrails': 'Ограничения и контроль',
           'stages': 'Этап', 'lanes': 'Направление работы', 'all': 'Все', 'reset': 'Показать весь процесс',
           'empty': 'Отдельная задача не указана', 'coverage': 'Иллюстративный охват',
           'concern': 'Область контроля', 'posture': 'Подход', 'selection': 'Представление процесса'},
}


class _Node:
    def __init__(self, tag='', attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    def text(self):
        return ' '.join(' '.join(c.text() if isinstance(c, _Node) else c for c in self.children).split())

    def find(self, *, cls=None, tag=None):
        result = []
        for child in self.children:
            if isinstance(child, _Node):
                if (cls is None or cls in child.attrs.get('class', '').split()) and (tag is None or child.tag == tag):
                    result.append(child)
                result.extend(child.find(cls=cls, tag=tag))
        return result

    def one(self, cls):
        found = self.find(cls=cls)
        if len(found) != 1:
            raise ValueError(f'Expected one source {cls}, found {len(found)}')
        return found[0]


class _Source(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.root = _Node()
        self.stack = [self.root]
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        node = _Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(_Node(tag, attrs))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, text):
        self.stack[-1].children.append(text)


def source_content(source=SOURCE):
    """Extract the source model; keys identify content, not translated wording."""
    root = _Source(Path(source).read_text()).root
    units = {}

    def unit(key, node):
        value = node.text() if isinstance(node, _Node) else node
        if key in units or not value:
            raise ValueError(f'Invalid source unit: {key}')
        units[key] = value
        return key

    model = {'units': units, 'stages': [], 'lanes': [], 'cells': [], 'systems': [], 'capabilities': [], 'loop': [], 'guardrails': []}
    model['subtitle'] = unit('subtitle', root.one('page-header__title').text().split('·', 1)[1].strip())
    model['intro'] = unit('intro', root.one('page-header__intent'))
    for stage in root.find(cls='cl-chev'):
        step = stage.attrs['data-step']
        model['stages'].append({'id': step, 'name': unit(f'stage-{step}', stage.one('cl-chev-name'))})
    for lane in root.find(cls='cl-lane-label'):
        identifier = lane.attrs['data-lane']
        model['lanes'].append({'id': identifier, 'name': unit(f'lane-{identifier}', lane.one('cl-lane-label__name'))})
    for cell in root.find(cls='cl-cell'):
        lane, step = cell.attrs['data-lane'], cell.attrs['data-step']
        tasks = []
        for index, card in enumerate(cell.find(cls='cl-card'), 1):
            identifier = f'task-{lane.lower()}-{step}-{index}'
            tasks.append({'id': identifier, 'name': unit(identifier + '-name', card.one('cl-name')),
                          'desc': unit(identifier + '-desc', card.one('cl-desc'))})
        model['cells'].append({'lane': lane, 'stage': step, 'tasks': tasks})
    model['systems_title'] = unit('systems-title', root.one('cl-page-subhead'))
    model['systems_intro'] = unit('systems-intro', root.one('cl-page-subhead-intent'))
    model['systems_connection'] = unit('systems-connection', root.one('cl-spine__label'))
    for index, system in enumerate(root.find(cls='cl-system'), 1):
        prefix = f'system-{index}'
        duties = []
        for number, duty in enumerate(system.one('cl-duties').find(tag='li'), 1):
            title = duty.find(tag='strong')[0]
            spans = [c for c in duty.children if isinstance(c, _Node) and c.tag == 'span']
            description = ' '.join(c.text() if isinstance(c, _Node) else c for c in spans[-1].children if c is not title)
            identifier = f'{prefix}-duty-{number}'
            duties.append({'id': identifier, 'number': unit(identifier + '-number', duty.one('cl-duties__num')),
                           'name': unit(identifier + '-name', title), 'desc': unit(identifier + '-desc', ' '.join(description.split()))})
        model['systems'].append({'id': prefix, 'label': unit(prefix + '-label', system.one('cl-system__label')),
                                'name': unit(prefix + '-name', system.one('cl-system__name')),
                                'role': unit(prefix + '-role', system.one('cl-system__role')), 'duties': duties})
    implication = root.one('cl-implication')
    model['implication_label'] = unit('implication-label', implication.one('cl-implication__tag'))
    model['implication'] = unit('implication', implication.find(tag='p')[0])
    for kind, source_cls, name_cls, desc_cls in (
        ('capabilities', 'cl-cap', 'cl-cap__name', 'cl-cap__desc'),
        ('loop', 'cl-loop-step', 'cl-loop-step__name', 'cl-loop-step__desc')):
        section = root.one('cloud-lab-section--' + ('capabilities' if kind == 'capabilities' else 'loop'))
        model[kind + '_title'] = unit(kind + '-title', section.one('cl-block-title'))
        model[kind + '_intro'] = unit(kind + '-intro', section.one('cl-block-intent'))
        for index, item in enumerate(section.find(cls=source_cls), 1):
            identifier = f'{kind}-{index}'
            model[kind].append({'id': identifier, 'name': unit(identifier + '-name', item.one(name_cls)),
                                'desc': unit(identifier + '-desc', item.one(desc_cls))})
    model['guardrails_title'] = unit('guardrails-title', root.one('cl-govtable-title'))
    model['guardrails_intro'] = unit('guardrails-intro', root.one('cl-govtable-intent'))
    group = None
    for row in root.one('cl-govtable').find(tag='tr'):
        if 'cl-govtable__category-row' in row.attrs.get('class', '').split():
            number = len(model['guardrails']) + 1
            group = {'id': f'guardrails-{number}', 'name': unit(f'guardrails-{number}-name', row), 'concerns': []}
            model['guardrails'].append(group)
        else:
            name = row.one('cl-govtable__concern-name')
            identifier = f'{group["id"]}-{len(group["concerns"]) + 1}'
            group['concerns'].append({'id': identifier, 'name': unit(identifier + '-name', name),
                                      'desc': unit(identifier + '-desc', row.one('cl-govtable__posture')),
                                      'coverage': int(re.search(r'--coverage:\s*(\d+)%', name.attrs['style'])[1])})
    return model


def content_hash(units):
    return hashlib.sha256(json.dumps(units, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def edition(model, lang):
    if lang == 'en':
        return model['units']
    translation = json.loads(TRANSLATION.read_text())
    if translation['source_hash'] != content_hash(model['units']):
        raise ValueError('AI Lab Russian translation requires source reconciliation')
    if set(translation['text']) != set(model['units']) or not all(translation['text'].values()):
        raise ValueError('AI Lab Russian translation must cover exactly all source units')
    return translation['text']


def render(model, lang):
    words, ui = edition(model, lang), UI[lang]
    url = f'/{lang}/lab/'
    entries = []

    def text(key, tag='span', attrs=''):
        return f'<{tag} data-lab-unit="{key}" {attrs}>{escape(words[key])}</{tag}>'

    def index(identifier, title, description):
        entries.append({'u': url + '#' + identifier, 't': 'AI Lab', 'h': words[title], 'x': words[description]})

    def heading(identifier, title, intro):
        index(identifier, title, intro)
        return text(title, 'h2', f'id="{identifier}"') + text(intro, 'p', 'class="lab-section-intro"')

    body = f'<article class="lab-content"><header class="lab-header"><span class="neighbour-status">{ui["concept"]}</span><h1>AI Lab</h1>'
    body += text(model['subtitle'], 'p', 'class="lab-subtitle"') + text(model['intro'], 'p', 'class="lab-intro"') + '</header>'
    body += f'<section class="lab-section" aria-labelledby="workflow"><h2 id="workflow">{ui["matrix"]}</h2>'
    body += '<div class="lab-controls" hidden>'
    for kind, items in (('stage', model['stages']), ('lane', model['lanes'])):
        label = ui['stages' if kind == 'stage' else 'lanes']
        body += f'<fieldset><legend>{label}</legend><div class="lab-options"><button type="button" data-lab-{kind}="all" aria-pressed="true">{ui["all"]}</button>'
        for item in items:
            body += f'<button type="button" data-lab-{kind}="{item["id"]}" aria-pressed="false">{escape(words[item["name"]])}</button>'
        body += '</div></fieldset>'
    body += f'<button type="button" class="lab-reset" data-lab-reset>{ui["reset"]}</button><p class="lab-selection o-sr-only" aria-live="polite"></p></div>'
    body += f'<div class="lab-matrix-wrap" role="region" tabindex="0" aria-label="{ui["matrix"]}"><div class="lab-matrix">'
    for row, lane in enumerate(model['lanes'], 2):
        body += text(lane['name'], 'div', f'class="lab-lane" data-lane="{lane["id"]}" style="grid-column:1;grid-row:{row}"')
    for column, stage in enumerate(model['stages'], 2):
        step = stage['id']
        index('stage-' + step, stage['name'], model['intro'])
        body += f'<h3 id="stage-{step}" class="lab-stage" data-stage="{step}" style="grid-column:{column};grid-row:1"><span class="lab-number">{step}</span>{text(stage["name"])}</h3>'
        for row, lane in enumerate(model['lanes'], 2):
            cell = next(c for c in model['cells'] if c['stage'] == step and c['lane'] == lane['id'])
            body += f'<div class="lab-cell" data-stage="{step}" data-lane="{lane["id"]}" style="grid-column:{column};grid-row:{row}">'
            body += f'<div class="lab-cell-label">{escape(words[lane["name"]])}</div>'
            for task in cell['tasks']:
                index(task['id'], task['name'], task['desc'])
                body += f'<article class="lab-task lab-card" id="{task["id"]}">{text(task["name"], "h4")}{text(task["desc"], "p")}</article>'
            if not cell['tasks']:
                body += f'<span class="lab-empty">{ui["empty"]}</span>'
            body += '</div>'
    body += '</div></div></section><section class="lab-section" aria-labelledby="systems">'
    body += heading('systems', model['systems_title'], model['systems_intro']) + '<div class="lab-systems">'
    for system in model['systems']:
        body += f'<article class="lab-system lab-card" id="{system["id"]}"><header>{text(system["label"], "p", "class=lab-eyebrow")}{text(system["name"], "h3")}{text(system["role"], "p")}</header><ol class="lab-duties">'
        for duty in system['duties']:
            index(duty['id'], duty['name'], duty['desc'])
            body += f'<li id="{duty["id"]}">{text(duty["number"], "span", "class=lab-duty-number")}<div>{text(duty["name"], "h4")}{text(duty["desc"], "p")}</div></li>'
        body += '</ol></article>'
    body += '</div><a class="lab-systems-connection" href="#intent-loop"><span aria-hidden="true">↔</span>' + text(model['systems_connection']) + '</a>'
    body += '<aside class="lab-implication">' + text(model['implication_label'], 'h3') + text(model['implication'], 'p') + '</aside></section>'
    for kind, identifier in (('capabilities', 'capabilities'), ('loop', 'intent-loop')):
        body += f'<section class="lab-section" aria-labelledby="{identifier}">' + heading(identifier, model[kind + '_title'], model[kind + '_intro'])
        body += f'<div class="lab-{kind}">'
        for number, item in enumerate(model[kind], 1):
            index(item['id'], item['name'], item['desc'])
            body += f'<article class="lab-card lab-{kind}-card" id="{item["id"]}"><header><span class="lab-number">{number}</span>{text(item["name"], "h3")}</header>{text(item["desc"], "p")}</article>'
        body += '</div></section>'
    body += '<section class="lab-section" aria-labelledby="guardrails">' + heading('guardrails', model['guardrails_title'], model['guardrails_intro'])
    body += f'<p class="lab-coverage-label">{ui["coverage"]}</p><div class="lab-guardrails">'
    for group in model['guardrails']:
        body += f'<article class="lab-card lab-guardrail-group" id="{group["id"]}">{text(group["name"], "h3")}<table><thead><tr><th scope="col">{ui["concern"]}</th><th scope="col">{ui["posture"]}</th><th scope="col">{ui["coverage"]}</th></tr></thead><tbody>'
        for concern in group['concerns']:
            index(concern['id'], concern['name'], concern['desc'])
            body += f'<tr id="{concern["id"]}">{text(concern["name"], "th", "scope=row")}{text(concern["desc"], "td")}<td><span class="lab-coverage" style="--coverage:{concern["coverage"]}%"><span>{concern["coverage"]}%</span></span></td></tr>'
        body += '</tbody></table></article>'
    body += '</div></section></article>'
    return body, entries


def build(output):
    model = source_content()
    for lang in ('en', 'ru'):
        url = f'/{lang}/lab/'
        body, entries = render(model, lang)
        ui = UI[lang]
        labels = [('workflow', ui['matrix']), ('systems', ui['systems']), ('capabilities', ui['capabilities']), ('intent-loop', ui['loop']), ('guardrails', ui['guardrails'])]
        nav = f'<a href="{workspace.relative(url, url)}" aria-current="page">AI Lab</a>' + ''.join(f'<a href="#{identifier}">{escape(label)}</a>' for identifier, label in labels)
        head = f'<link rel="stylesheet" href="{workspace.asset(url, "lab.css")}"><script defer src="{workspace.asset(url, "lab.js")}"></script>'
        page = workspace.page(url, lang, 'lab', 'AI Lab', body, nav, body_class='lab-workspace')
        # The local skin follows the shared stylesheet cascade.
        page = page.replace('</head>', head + '\n</head>', 1)
        target = Path(output) / lang / 'lab/index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page)
        entries.insert(0, {'u': url, 't': 'AI Lab', 'h': 'AI Lab', 'x': edition(model, lang)[model['intro']]})
        (Path(output) / f'assets/search-lab-{lang}.json').write_text(json.dumps(entries, ensure_ascii=False, separators=(',', ':')))
    for name in ('lab.css', 'lab.js'):
        shutil.copyfile(workspace.ROOT / 'portal/site' / name, Path(output) / 'assets' / name)
    return 2
