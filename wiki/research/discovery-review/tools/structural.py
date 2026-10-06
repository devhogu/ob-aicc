"""Structural fixes of the Discovery Catalog source (English), step 3 of RUNBOOK.md.

Applies the entries of fixmap/_structural.json that change markup rather than text:
the overview totals and cycles boxes, the drafted problem rows, the paragraph split of
the finance cycle descriptions and the two misplaced cards. Idempotent: a second run
changes nothing. Section-order entries are not applied (decision D8).
"""
import argparse
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
LENSES = ['Insights & analytics', 'Enablement', 'Automation', 'New business opportunities']
TOTALS = {
    'Strategic Banking Portfolio': 135, 'Strategic Initiatives & Transformation': 130,
    'Customer & Market Intelligence': 128, 'Customer & Channels': 97, 'Risk & Control': 164,
    'Shared Banking Capabilities': 132, 'Finance & Treasury': 126, 'Banking Data & Analytics': 134,
}
CYCLES = {
    'Strategic Banking Portfolio': ('Strategic governance', 'strategic-portfolio/steering-cycles', 'Steering Cycles', 19),
    'Strategic Initiatives & Transformation': ('Change cycles', 'strategic-initiatives/change-cycles', 'Change Cycles', 17),
    'Customer & Market Intelligence': ('Analytics cycles', 'customer-market-intelligence/intelligence-cycles', 'Intelligence Cycles', 17),
    'Customer & Channels': ('Channel governance', 'customer-channels/channel-cycles', 'Channel Cycles', 17),
    'Risk & Control': ('Risk governance', 'risk-control/risk-cycles', 'Risk Cycles', 25),
    'Shared Banking Capabilities': ('Capability governance', 'shared-banking-capabilities/capability-cycles', 'Capability Cycles', 20),
    'Finance & Treasury': ('Finance governance', 'finance-treasury/finance-cycles', 'Finance Cycles', 25),
    'Banking Data & Analytics': ('Data governance', 'banking-data-analytics/data-cycles', 'Data Cycles', 20),
}
STYLE_NOTE = '''  /*
    Per-page tab selectors — emitted at render time from concern-problems.html.j2
    using this L1's actual category tags. concern.css carries no hardcoded slugs.
    Pattern: checked radio siblings the tab-bar label → active style; siblings the
    matching panel → display:block. One rule pair per category.
  */
  '''


def esc(text):
    return html.escape(text, quote=False).replace("'", '&#39;')


def slug(label):
    return re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')


def rule(tab):
    return f'''
  #problems-tab-{tab}:checked ~ .problems-tab-bar label[for="problems-tab-{tab}"] {{
    color: var(--ink-accent);
    border-bottom-color: var(--ink-accent);
    background: var(--paper-blue-soft);
    font-weight: 600;
  }}
  #problems-tab-{tab}:checked ~ .problems-panel[data-tab="{tab}"] {{
    display: block;
  }}
  '''


def radio(tab, label, checked):
    return f'''
  <input
    type="radio"
    class="problems-tab-input"
    name="problems-tabs"
    id="problems-tab-{tab}"
    value="{tab}"
    {'checked' if checked else ''}
    aria-label="{esc(label)}"
  >
  '''


def tab_label(tab, label):
    return f'''
    <label
      class="problems-tab-label"
      for="problems-tab-{tab}"
      role="tab"
      aria-controls="problems-panel-{tab}"
    >{esc(label)}</label>
    '''


def panel(tab, rows):
    body = ''.join(f'''
        <tr class="problems-row">
          <th class="problems-lens" scope="row">{esc(lens)}</th>
          <td class="problems-statement">{esc(rows[lens])}</td>
        </tr>
        ''' for lens in LENSES)
    return f'''
  <div
    class="problems-panel"
    id="problems-panel-{tab}"
    data-tab="{tab}"
    role="tabpanel"
    aria-labelledby="problems-tab-{tab}"
  >
    <table class="problems-table">
      <tbody>
        {body}
      </tbody>
    </table>
  </div>
  '''


def block(tab, label, rows):
    return ('<style>\n' + STYLE_NOTE + rule(tab) + '\n</style>\n\n\n'
            '<section class="concern-problems" aria-label="Problems">\n\n  \n  '
            + radio(tab, label, True) + '\n\n  \n  <div class="problems-tab-bar" role="tablist">\n    '
            + tab_label(tab, label) + '\n  </div>\n\n  <hr class="problems-divider">\n\n  \n  '
            + panel(tab, rows) + '\n\n</section>\n  ')


def add_tab(text, tab, label, rows, first):
    """Add one tab to an existing problems block."""
    if f'id="problems-tab-{tab}"' in text:
        return text, False
    text = text.replace('\n</style>', rule(tab) + '\n</style>', 1) if not first else text.replace(STYLE_NOTE, STYLE_NOTE + rule(tab), 1)
    start = text.index('<section class="concern-problems"')
    end = text.index('</section>', start)
    section = text[start:end]
    if first:
        section = re.sub(r'(\n    )checked(\n)', r'\1\2', section, count=1)
        section = section.replace('\n  <input', radio(tab, label, True) + '\n  <input', 1)
        section = section.replace('<div class="problems-tab-bar" role="tablist">\n    ', '<div class="problems-tab-bar" role="tablist">\n    ' + tab_label(tab, label), 1)
        section = section.replace('\n  <div\n    class="problems-panel"', panel(tab, rows) + '\n  <div\n    class="problems-panel"', 1)
    else:
        bar = section.index('<div class="problems-tab-bar"')
        section = section[:bar].rstrip() + '\n  ' + radio(tab, label, False) + '\n\n  \n  ' + section[bar:]
        section = section.replace('\n  </div>\n\n  <hr class="problems-divider">', tab_label(tab, label) + '\n  </div>\n\n  <hr class="problems-divider">', 1)
        section = section.rstrip() + '\n  ' + panel(tab, rows) + '\n\n'
    return text[:start] + section + text[end:], True


def overview(text):
    done = 0
    for name, total in TOTALS.items():
        pattern = re.compile(r'(<h[23] class="card__title[^"]*">' + re.escape(esc(name)) + r' <span class="card__count" aria-label=")\d+( scenarios">\()\d+(\)</span>)')
        text, n = pattern.subn(lambda m: f'{m[1]}{total}{m[2]}{total}{m[3]}', text, count=1)
        if n != 1:
            raise SystemExit(f'overview heading not found: {name}')
        label, path, link, count = CYCLES[name]
        href = f'{path}/index.html'
        if f'href="{href}"' in text:
            continue
        head = pattern.search(text).start()
        end = text.index('</article>', head)
        article = text[head:end]
        last = article.rindex('<div class="sub-group">')
        close = article.index('        </div>\n      </div>\n', last) + len('        </div>\n      </div>\n')
        group = f'''
      <div class="sub-group">
        <div class="sub-group__label">{esc(label)}</div>
        <div class="sub-group__items">

          <a class="card-link" href="{href}">{esc(link)} <span class="card-link__count">({count})</span></a>


        </div>
      </div>
'''
        text = text[:head] + article[:close] + group + article[close:] + text[end:]
        done += 1
    return text, done


def split_paragraphs(text):
    def repl(match):
        parts = [p.strip() for p in match[1].split('\n') if p.strip()]
        return '\n    '.join(f'<p class="flow-detail__intent-full">{p}</p>' for p in parts)
    return re.subn(r'<p class="flow-detail__intent-full">([^<]*\n[^<]*?)</p>', repl, text)


def swap_cards(text, first, second):
    def card(urn):
        start = text.index(f'<details class="scenario-card" data-urn="{urn}"')
        return start, text.index('</details>', start) + len('</details>')
    (a0, a1), (b0, b1) = sorted([card(first), card(second)])
    return text[:a0] + text[b0:b1] + text[a1:b0] + text[a0:a1] + text[b1:]


def section_of(text, urn):
    start = text.index(f'data-urn="{urn}"')
    return re.findall(r'<section class="l3-section" id="([^"]+)"', text[:start])[-1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True)
    parser.add_argument('--fixmap', default=str(HERE.parent / 'fixmap'))
    args = parser.parse_args()
    root = Path(args.root)
    entries = json.loads((Path(args.fixmap) / '_structural.json').read_text())
    report = {}

    path = root / 'index.html'
    text, added = overview(path.read_text())
    path.write_text(text)
    report['overview totals'] = len(TOTALS)
    report['cycles boxes added'] = added

    rows = {}
    for entry in entries:
        if entry['field'] != 'problem_row':
            continue
        relative = entry['file'].split('/en/', 1)[1]
        tab = re.search(r"tab ['\"]([^'\"]+)['\"]", entry['locator'])[1]
        lens = re.search(r"row ['\"]([^'\"]+)['\"]", entry['locator'])[1]
        rows.setdefault((relative, tab), {})[lens] = entry['proposed']
    report['problem tabs added'] = 0
    for (relative, label), by_lens in rows.items():
        if set(by_lens) != set(LENSES):
            raise SystemExit(f'incomplete problem rows: {relative} {label}')
        path = root / relative
        text = path.read_text()
        tab = slug(label)
        if '<section class="concern-problems"' in text:
            # The tab order follows the order of the groups on the area page.
            text, changed = add_tab(text, tab, label, by_lens, first=relative == 'risk-control/index.html')
        elif f'id="problems-tab-{tab}"' in text:
            changed = False
        else:
            anchor = text.index('<main id="main-content"')
            header = text.rindex('</header>', 0, anchor) + len('</header>')
            text = text[:header] + '\n\n  \n  \n  \n\n' + block(tab, label, by_lens) + '\n\n  \n  ' + text[anchor:]
            changed = True
        path.write_text(text)
        report['problem tabs added'] += changed

    path = root / 'finance-treasury/finance-cycles/index.html'
    text, report['cycle descriptions split'] = split_paragraphs(path.read_text())
    path.write_text(text)

    path = root / 'strategic-initiatives/innovation-portfolio/index.html'
    text = path.read_text()
    base = 'urn:financial-services:scenario:strategic-initiatives/innovation-portfolio/'
    results, sample = base + 'mvp-design-hypothesis-testing/mvp-test-results-interpretation-brief', base + 'experiment-analytics/experiment-sample-design-optimisation'
    report['cards moved'] = 0
    if section_of(text, results) == 'mvp-design-hypothesis-testing':
        text = swap_cards(text, results, sample)
        path.write_text(text)
        report['cards moved'] = 2
    if (section_of(text, results), section_of(text, sample)) != ('experiment-analytics', 'mvp-design-hypothesis-testing'):
        raise SystemExit('card move failed')
    print(report)


if __name__ == '__main__':
    main()
