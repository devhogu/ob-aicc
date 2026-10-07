# START_MODULE_CONTRACT
#   PURPOSE: Project the complete retained laboratory operating model into AI Lab.
#   SCOPE: Source extraction, paired translation, native presentation and local search.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   SOURCE - English Lab record (lab/en/lab.md)
#   TRANSLATION - Russian Lab record with the same keys, pinned to the English one
#   UI - bilingual reading controls and local section names
#   source_content - read the Lab model and its text units from the English record
#   edition - require a complete, current language edition
#   render - build native laboratory content and search destinations
#   build - package both editions and local reading assets in the common shell
# END_MODULE_MAP
"""The AI Lab section, built from its own Markdown records."""
from html import escape
import hashlib
import json
from pathlib import Path
import re
import shutil

import workspace

# The Lab is its own source context: lab/<lang>/lab.md, the Russian record pinned to the English one.
SOURCE = workspace.ROOT / 'lab/en/lab.md'
TRANSLATION = workspace.ROOT / 'lab/ru/lab.md'
UI = {
    'en': {'concept': 'Concept', 'matrix': 'Experiment workflow', 'systems': 'People and AI agents', 'maturity': 'Practice maturity',
           'guardrails_intro': 'The Lab runs under seven guardrails. The Competence Center Lead keeps them with their evidence in the Standards record, and the quarterly Steering reviews them.',
           'guardrail': 'Guardrail', 'evidence': 'Evidence', 'setup': 'Once, before the first Experiment', 'bands': 'Maturity bands',
           'capabilities': 'Capabilities', 'loop': 'Intent loop', 'guardrails': 'Guardrails',
           'stages': 'Stage', 'lanes': 'Workstream', 'whole': 'Whole workflow', 'by_stage': 'By stage',
           'empty': 'No separate activity specified', 'coverage': 'Assessment', 'not_assessed': 'Not yet assessed', 'levels': 'What each level requires',
           'concern': 'Concern', 'posture': 'Intended practice', 'selection': 'Workflow view'},
    'ru': {'concept': 'Концепция', 'matrix': 'Процесс эксперимента', 'systems': 'Люди и AI-агенты', 'maturity': 'Оценка контроля',
           'guardrails_intro': 'Лабораторная среда работает в рамках семи защитных механизмов. Руководитель Центра Компетенций ведёт их вместе с подтверждениями в реестре «Стандарты», а ежеквартальное управляющее совещание их рассматривает.',
           'guardrail': 'Защитный механизм', 'evidence': 'Подтверждение', 'setup': 'Один раз, до первого эксперимента', 'bands': 'Уровни зрелости',
           'capabilities': 'Возможности', 'loop': 'Цикл управления', 'guardrails': 'Защитные механизмы',
           'stages': 'Этап', 'lanes': 'Блок работ', 'whole': 'Весь процесс', 'by_stage': 'По этапам',
           'empty': 'Отдельная задача не указана', 'coverage': 'Оценка', 'not_assessed': 'Не оценено', 'levels': 'Что требуется для каждого уровня',
           'concern': 'Область контроля', 'posture': 'Планируемая практика', 'selection': 'Вид процесса'},
}


BANDS = {
    'en': [(0, 25, 'Not in place', 'Done case by case or not at all; no defined practice.'),
           (26, 50, 'Basic', 'A minimal practice exists, but it is informal, manual, or not applied to every Experiment.'),
           (51, 75, 'Established', 'Defined and applied to every Experiment, with evidence kept; some gaps against what production requires.'),
           (76, 100, 'Strong', 'Applied consistently, evidenced, and checked; close to what the Bank requires of production systems.')],
    'ru': [(0, 25, 'Нет практики', 'Решается в каждом случае отдельно или не выполняется; практика не определена.'),
           (26, 50, 'Базовый уровень', 'Минимальная практика есть, но она неформальна, выполняется вручную или не в каждом эксперименте.'),
           (51, 75, 'Устойчивая практика', 'Определена и применяется в каждом эксперименте, подтверждения сохраняются; есть пробелы относительно требований к промышленным системам.'),
           (76, 100, 'Высокий уровень', 'Применяется последовательно, подтверждается и проверяется; близко к требованиям Банка к промышленным системам.')],
}


def band(value, lang):
    return next(item for item in BANDS[lang] if item[0] <= value <= item[1])


def corpus_guardrails(lang):
    """The guardrails of the Lab as the Standards record of the Registry keeps them."""
    rows = []
    for line in (workspace.ROOT / 'registry' / lang / 'standards.md').read_text().splitlines():
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if cells and re.fullmatch(r'LAB-\d{3}', cells[0]):
            rows.append({'id': cells[0], 'text': cells[1], 'evidence': cells[2]})
    if not rows:
        raise ValueError(f'No Lab guardrails in the {lang} Standards record')
    return rows


def _records(path):
    """Tables of a Lab record by section: {section heading: [row dicts by column]} with the column order kept."""
    sections, current, header = {}, None, None
    for line in Path(path).read_text().splitlines():
        if line.startswith('## '):
            current, header = line[3:].strip(), None
            sections[current] = []
        elif current and line.startswith('|'):
            cells = [c.strip().replace('\\|', '|') for c in re.split(r'(?<!\\)\|', line.strip())[1:-1]]
            if header is None:
                header = cells
            elif not all(set(c) <= {'-'} for c in cells):
                sections[current].append(cells)
    return list(sections.values())


def _units(path):
    """Every text unit of a Lab record, keyed as the model keys it."""
    page, stages, lanes, tasks, systems, duties, loop, areas, concerns = _records(path)
    units = {}
    def put(key, value):
        if key in units or not value:
            raise ValueError(f'Invalid Lab source unit: {key}')
        units[key] = value
    for key, text in page: put(key, text)
    for key, text in stages + lanes: put(key, text)
    for key, _lane, _stage, name, desc in tasks: put(key + '-name', name); put(key + '-desc', desc)
    for key, label, name, role in systems: put(key + '-label', label); put(key + '-name', name); put(key + '-role', role)
    for key, _system, number, name, desc in duties: put(key + '-number', number); put(key + '-name', name); put(key + '-desc', desc)
    for key, name, desc in loop: put(key + '-name', name); put(key + '-desc', desc)
    for key, name in areas: put(key + '-name', name)
    for key, _area, name, desc, _coverage, *levels in concerns:
        put(key + '-name', name); put(key + '-desc', desc)
        for band, text in zip(('2', '3', '4'), levels):
            if text: put(f'{key}-criteria-{band}', text)
    return units


def source_content(source=SOURCE):
    """The Lab model from its English record; keys identify content, not translated wording."""
    page, stages, lanes, tasks, systems, duties, loop, areas, concerns = _records(source)
    model = {'units': _units(source), 'stages': [], 'lanes': [], 'cells': [], 'systems': [], 'capabilities': [], 'loop': [], 'guardrails': []}
    for field in ('subtitle', 'intro', 'systems-title', 'systems-intro', 'systems-connection', 'implication-label', 'implication',
                  'loop-title', 'loop-intro', 'guardrails-title', 'guardrails-intro'):
        model[field.replace('-', '_')] = field
    model['stages'] = [{'id': key.split('-', 1)[1], 'name': key} for key, _ in stages]
    model['lanes'] = [{'id': key.split('-', 1)[1], 'name': key} for key, _ in lanes]
    # Every workstream meets every stage; a cell without a task stays visible as empty.
    for lane in model['lanes']:
        for stage in model['stages']:
            cell = [{'id': k, 'name': k + '-name', 'desc': k + '-desc'} for k, l, st, *_ in tasks if l == lane['id'] and st == stage['id']]
            model['cells'].append({'lane': lane['id'], 'stage': stage['id'], 'tasks': cell})
    for key, *_ in systems:
        model['systems'].append({'id': key, 'label': key + '-label', 'name': key + '-name', 'role': key + '-role',
                                 'duties': [{'id': d, 'number': d + '-number', 'name': d + '-name', 'desc': d + '-desc'} for d, owner, *_ in duties if owner == key]})
    model['loop'] = [{'id': key, 'name': key + '-name', 'desc': key + '-desc'} for key, *_ in loop]
    for key, _ in areas:
        group = {'id': key, 'name': key + '-name', 'concerns': []}
        for c, area, _n, _d, coverage, *levels in concerns:
            if area == key:
                group['concerns'].append({'id': c, 'name': c + '-name', 'desc': c + '-desc', 'coverage': int(coverage) if coverage else None,
                                          'criteria': [(band, f'{c}-criteria-{band}') for band, text in zip(('2', '3', '4'), levels) if text]})
        model['guardrails'].append(group)
    return model


def edition(model, lang):
    """The text units of one language; the Russian record must be current with the English one and cover every unit."""
    if lang == 'en':
        return model['units']
    text = TRANSLATION.read_text()
    pin = re.search(r'^source_sha256: ([0-9a-f]{64})$', text, re.M)
    if not pin or pin[1] != hashlib.sha256(SOURCE.read_bytes()).hexdigest():
        raise ValueError('AI Lab Russian record requires reconciliation with the English record')
    units = _units(TRANSLATION)
    if list(units) != list(model['units']):
        raise ValueError('AI Lab Russian record must cover exactly the English units, in the same order')
    return units


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
    body += f'<section class="lab-section" aria-labelledby="guardrails"><h2 id="guardrails">{ui["guardrails"]}</h2><p class="lab-section-intro">{escape(ui["guardrails_intro"])}</p><ol class="lab-guardrail-list">'
    for item in corpus_guardrails(lang):
        entries.append({'u': url + '#' + item['id'].lower(), 't': 'AI Lab', 'h': item['text'], 'x': item['evidence']})
        body += f'<li class="lab-card" id="{item["id"].lower()}"><span class="lab-guardrail-id">{item["id"]}</span><p>{escape(item["text"])}</p><p class="lab-guardrail-evidence"><span>{ui["evidence"]}:</span> {escape(item["evidence"])}</p></li>'
    body += '</ol></section>'
    body += f'<section class="lab-section" aria-labelledby="workflow"><h2 id="workflow">{ui["matrix"]}</h2>'
    body += '<div class="lab-controls" hidden>'

    def count_text(count):
        if lang == 'en':
            noun = 'task' if count == 1 else 'tasks'
        else:
            noun = 'задач' if 11 <= count % 100 <= 14 else 'задача' if count % 10 == 1 else 'задачи' if 2 <= count % 10 <= 4 else 'задач'
        return f'{count} {noun}'

    total = count_text(sum(len(cell['tasks']) for cell in model['cells']))
    body += f'<nav class="lab-stage-nav" aria-label="{ui["stages"]}">'
    for stage in model['stages']:
        step = stage['id']
        count = count_text(sum(len(cell['tasks']) for cell in model['cells'] if cell['stage'] == step))
        setup = step == '0'
        marker = workspace.icon('layers') if setup else step
        note = f'<span class="lab-step-note">{ui["setup"]}</span>' if setup else ''
        body += f'<button type="button" class="lab-step{" lab-step--setup" if setup else ""}" data-lab-stage="{step}" data-lab-count="{count}" aria-pressed="false" aria-controls="lab-workflow-matrix"><span class="lab-step-number" aria-hidden="true">{marker}</span><span class="lab-step-label">{escape(words[stage["name"]])}{note}</span><span class="lab-step-count">{count}</span></button>'
    body += f'</nav><div class="lab-view-bar"><div class="lab-view-options" role="group" aria-label="{ui["selection"]}"><button type="button" data-lab-view="all" data-lab-reset data-lab-count="{total}" aria-pressed="true" aria-controls="lab-workflow-matrix">{ui["whole"]}</button><button type="button" data-lab-view="stage" aria-pressed="false" aria-controls="lab-workflow-matrix">{ui["by_stage"]}</button></div><span class="lab-visible-count">{total}</span></div><p class="lab-selection o-sr-only" aria-live="polite"></p></div>'
    body += f'<div id="lab-workflow-matrix" class="lab-matrix-wrap" role="region" tabindex="0" aria-label="{ui["matrix"]}"><div class="lab-matrix" style="--lab-stages:{len(model["stages"])}">'
    for row, lane in enumerate(model['lanes'], 2):
        body += text(lane['name'], 'div', f'class="lab-lane" data-lane="{lane["id"]}" style="grid-column:1;grid-row:{row}"')
    for column, stage in enumerate(model['stages'], 2):
        step = stage['id']
        index('stage-' + step, stage['name'], model['intro'])
        if step == '0':
            # One-time preparation precedes the repeated Experiment steps.
            body += f'<h3 id="stage-{step}" class="lab-stage lab-stage--setup" data-stage="{step}" style="grid-column:{column};grid-row:1">{text(stage["name"])}<span class="lab-stage-note">{ui["setup"]}</span></h3>'
        else:
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
        if not model[kind]:
            continue
        body += f'<section class="lab-section" aria-labelledby="{identifier}">' + heading(identifier, model[kind + '_title'], model[kind + '_intro'])
        body += f'<div class="lab-{kind}">'
        for number, item in enumerate(model[kind], 1):
            index(item['id'], item['name'], item['desc'])
            body += f'<article class="lab-card lab-{kind}-card" id="{item["id"]}"><header><span class="lab-number">{number}</span>{text(item["name"], "h3")}</header>{text(item["desc"], "p")}</article>'
        body += '</div></section>'
    body += '<section class="lab-section" aria-labelledby="maturity">' + heading('maturity', model['guardrails_title'], model['guardrails_intro'])
    body += f'<dl class="lab-bands" aria-label="{ui["bands"]}">' + ''.join(
        f'<div class="lab-band lab-band--{n}"><dt>{low}–{high}% · {escape(name)}</dt><dd>{escape(meaning)}</dd></div>'
        for n, (low, high, name, meaning) in enumerate(BANDS[lang], 1)) + '</dl>'
    body += f'<p class="lab-coverage-label">{ui["coverage"]}</p><div class="lab-guardrails">'
    for group in model['guardrails']:
        body += f'<article class="lab-card lab-guardrail-group" id="{group["id"]}">{text(group["name"], "h3")}<table><thead><tr><th scope="col">{ui["concern"]}</th><th scope="col">{ui["posture"]}</th><th scope="col">{ui["coverage"]}</th></tr></thead><tbody>'
        for concern in group['concerns']:
            index(concern['id'], concern['name'], concern['desc'])
            tip = f'tip-{concern["id"]}'
            levels = ''.join(f'<li><strong>{BANDS[lang][int(level) - 1][0]}–{BANDS[lang][int(level) - 1][1]}% · {escape(BANDS[lang][int(level) - 1][2])}:</strong> {text(key)}</li>'
                             for level, key in concern['criteria'])
            if concern['coverage'] is None:
                status = f'<span class="lab-assessment" tabindex="0" aria-describedby="{tip}">{ui["not_assessed"]}</span>'
                head = f'<strong>{ui["not_assessed"]}</strong>'
            else:
                low, high, name, meaning = band(concern['coverage'], lang)
                status = f'<span class="lab-coverage" tabindex="0" aria-describedby="{tip}" style="--coverage:{concern["coverage"]}%"><span>{concern["coverage"]}%</span></span>'
                head = f'<strong>{low}–{high}% · {escape(name)}</strong><span class="lab-tip-band">{escape(meaning)}</span>'
            body += (f'<tr id="{concern["id"]}">{text(concern["name"], "th", "scope=row")}{text(concern["desc"], "td")}'
                     f'<td class="lab-coverage-cell">{status}<span class="lab-tip" role="tooltip" id="{tip}">{head}'
                     f'<span class="lab-tip-band">{ui["levels"]}</span><ul class="lab-tip-levels">{levels}</ul></span></td></tr>')
        body += '</tbody></table></article>'
    body += '</div></section></article>'
    return body, entries


def build(output):
    model = source_content()
    for lang in ('en', 'ru'):
        url = f'/{lang}/lab/'
        body, entries = render(model, lang)
        ui = UI[lang]
        labels = [('guardrails', ui['guardrails']), ('workflow', ui['matrix']), ('systems', ui['systems'])]
        labels += [('capabilities', ui['capabilities'])] if model['capabilities'] else []
        labels += [('intent-loop', ui['loop'])] if model['loop'] else []
        labels += [('maturity', ui['maturity'])]
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
