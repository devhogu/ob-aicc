#!/usr/bin/env python3
"""Prove the published lab retains the predecessor and complete paired content."""
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

import lab

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'html/aicc/v1'
SOURCE_BLOCKS = {'page-header__intent', 'cl-chev-name', 'cl-lane-label__name', 'cl-card',
                 'cl-page-subhead', 'cl-page-subhead-intent', 'cl-system__label', 'cl-system__name',
                 'cl-system__role', 'cl-spine__label', 'cl-implication', 'cl-block-title',
                 'cl-block-intent', 'cl-cap', 'cl-loop-step', 'cl-govtable-title',
                 'cl-govtable-intent', 'cl-govtable__category-row', 'cl-govtable__concern-row'}


class Capture(HTMLParser):
    """Independently capture source blocks and output units from actual markup."""
    def __init__(self, markup):
        super().__init__()
        self.active, self.blocks, self.units, self.ids, self.cells, self.values = [], [], {}, [], {}, []
        self.classes, self.resources = Counter(), []
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        self.classes.update(classes)
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if 'lab-cell' in classes:
            self.cells[(attrs['data-lane'], attrs['data-stage'])] = []
            self.cell = (attrs['data-lane'], attrs['data-stage'])
        if 'lab-task' in classes:
            self.cells[self.cell].append(attrs['id'])
        if 'lab-coverage' in classes:
            self.values.append(int(re.search(r'--coverage:(\d+)%', attrs['style'])[1]))
        for name in ('src', 'href'):
            if name in attrs:
                self.resources.append(attrs[name])
        tracked = SOURCE_BLOCKS.intersection(classes)
        # A duty includes the source number, title and description in one block.
        if tag == 'li':
            tracked.add('duty')
        if tracked or 'data-lab-unit' in attrs:
            self.active.append({'tag': tag, 'depth': 0, 'key': attrs.get('data-lab-unit'), 'parts': []})
        for item in self.active:
            if tag not in {'br', 'hr', 'img', 'input', 'meta', 'link'}:
                item['depth'] += 1

    def handle_endtag(self, tag):
        for item in self.active[:]:
            item['depth'] -= 1
            if item['depth'] == 0:
                value = ' '.join(' '.join(item['parts']).split())
                if item['key']:
                    self.units[item['key']] = value
                else:
                    self.blocks.append(value)
                self.active.remove(item)

    def handle_data(self, text):
        for item in self.active:
            item['parts'].append(text)


def check(output=OUTPUT):
    errors, counts = [], {}
    model = lab.source_content()
    # Every text cell of the English record, read independently of the projection model.
    source_cells = []
    for line in lab.SOURCE.read_text().splitlines():
        cells = [c.strip().replace('\\|', '|') for c in re.split(r'(?<!\\)\|', line.strip())[1:-1]] if line.startswith('|') else []
        for cell in cells[1:]:
            if cell and not set(cell) <= {'-'} and not re.fullmatch(r'[A-E]|\d{1,3}|system-\d+|guardrails-\d+|(Workstream|Stage|Task|Description|Text|Label|Name|Role|System|Number|Duty|Step|Area|Concern|Intended practice|Assessed coverage|Level \d)', cell):
                source_cells.append(cell)
    expected_cells = {(c['lane'], c['stage']): [task['id'] for task in c['tasks']] for c in model['cells']}
    expected_values = [c['coverage'] for group in model['guardrails'] for c in group['concerns'] if c['coverage'] is not None]
    for lang in ('en', 'ru'):
        route = Path(output) / lang / 'lab/index.html'
        if not route.exists():
            errors.append(f'{lang}: AI Lab page missing')
            continue
        markup = route.read_text()
        parsed = Capture(markup)
        if parsed.units != lab.edition(model, lang):
            errors.append(f'{lang}: published source units or translation incomplete/changed')
        if parsed.cells != expected_cells or parsed.values != expected_values:
            errors.append(f'{lang}: matrix assignments or scorecard values changed')
        # Expected structure follows the source model and the Standards record, not fixed numbers.
        concerns = sum(len(group['concerns']) for group in model['guardrails'])
        for name, number in {'lab-task': sum(len(tasks) for tasks in expected_cells.values()), 'lab-cell': len(model['cells']),
                             'lab-stage': len(model['stages']), 'lab-lane': len(model['lanes']),
                             'lab-system': len(model['systems']), 'lab-capabilities-card': len(model['capabilities']),
                             'lab-loop-card': len(model['loop']), 'lab-guardrail-group': len(model['guardrails']),
                             'lab-coverage': len(expected_values), 'lab-tip': concerns, 'lab-band': len(lab.BANDS[lang])}.items():
            if parsed.classes[name] != number:
                errors.append(f'{lang}: expected {number} {name}, got {parsed.classes[name]}')
        if markup.count('class="lab-guardrail-id"') != len(lab.corpus_guardrails(lang)):
            errors.append(f'{lang}: Lab guardrails differ from the Standards record')
        if len(parsed.ids) != len(set(parsed.ids)):
            errors.append(f'{lang}: duplicate Lab fragment identifiers')
        if 'html-alt/' in markup or 'fonts.googleapis.com' in markup:
            errors.append(f'{lang}: Lab depends on a retired source or external fonts')
        if lang == 'en':
            visible = ' '.join(parsed.units.values())
            for cell in source_cells:
                if cell not in visible:
                    errors.append(f'en: source record content absent: {cell[:80]}')
        entries = json.loads((Path(output) / f'assets/search-lab-{lang}.json').read_text())
        for entry in entries:
            destination = urlsplit(entry['u'])
            if destination.path != f'/{lang}/lab/' or (destination.fragment and destination.fragment not in parsed.ids):
                errors.append(f'{lang}: invalid Lab search destination {entry["u"]}')
        searchable = {urlsplit(entry['u']).fragment for entry in entries}
        if not set(task for tasks in expected_cells.values() for task in tasks).issubset(searchable):
            errors.append(f'{lang}: not every matrix task is searchable')
        if f'>{lab.UI[lang]["coverage"]}<' not in markup:
            errors.append(f'{lang}: assessment column not labelled')
        counts[lang + '_lab_content_units'] = len(parsed.units)
        counts[lang + '_lab_search_entries'] = len(entries)
    for lang in ('en', 'ru'):
        for route in (Path(output) / lang).rglob('index.html'):
            if route.parent == Path(output) / lang:
                continue  # the language entry only forwards to the Center
            text = route.read_text()
            label = re.search(r'<a\b[^>]*data-section="lab"[^>]*>.*?<span>(.*?)</span>\s*</a>', text, re.S)
            if not label or label[1] != 'AI Lab':
                errors.append(f'{route}: global Lab label is not AI Lab')
    return errors, counts


if __name__ == '__main__':
    errors, counts = check()
    print(json.dumps({'counts': counts, 'errors': errors}, ensure_ascii=False, indent=2))
    raise SystemExit(bool(errors))
