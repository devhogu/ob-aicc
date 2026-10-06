"""Add new scenario sections to the Discovery Catalog source and keep the counts that show them.

Input: a JSON list of {"page", "section": {"id", "title", "intent"}, "cards": [...]} as in
horizon/new-scenarios.json. For each entry the section is appended to its sub-area page, the area page
gains a group linking to it, and the counts on the area page and the overview grow by the number of
cards. Idempotent: a section that already exists is left alone.
"""
import argparse
import html
import json
import re
from pathlib import Path

LENSES = {'Insights': 'insights', 'Automation': 'automation', 'Enablement': 'enablement', 'Optimize': 'optimize', 'New opps': 'new-opps'}


def esc(text):
    return html.escape(text, quote=False).replace("'", '&#39;')


def card(urn, item):
    okr = item['okr']
    results = ''.join(f'''
        <div class="okr-kr">
          <div class="okr-kr__dim">{dim}</div>
          <p>{esc(okr[key])}</p>
        </div>
        ''' for dim, key in (('Adoption', 'adoption'), ('Acceptance', 'acceptance'), ('Cycle', 'cycle')))
    return f'''
<details class="scenario-card" data-urn="{urn}">
  <summary class="scenario-card__summary">
    <span class="scenario-lens scenario-lens--{LENSES[item['lens']]}">{item['lens']}</span>
    <div class="scenario-card__title-col">
      <span class="scenario-card__chevron" aria-hidden="true">▸</span>
      <h3 class="scenario-card__title">{esc(item['title'])}</h3>
    </div>
    <div class="scenario-card__intent-col">
      <p class="scenario-card__intent">{esc(item['intent'])}</p>
    </div>
    <span
      class="scenario-complexity scenario-complexity--{item['complexity']}"
      title="Complexity"
    >{item['complexity']}</span>
  </summary>

  <div class="scenario-card__body">

    <div class="scenario-section">
      <div class="scenario-section__label">Problem to solve</div>
      <p>{esc(item['problem'])}</p>
    </div>

    <div class="scenario-section">
      <div class="scenario-section__label">Solution</div>
      <p>{esc(item['solution'])}</p>
    </div>

    <div class="scenario-section">
      <div class="scenario-section__label">OKR</div>
      <p class="okr-objective">{esc(okr['objective'])}</p>
      <div class="okr-grid">{results}
      </div>
    </div>

  </div>
</details>
'''


def section(base, entry):
    sid = entry['section']['id']
    cards = ''.join(card(f'urn:financial-services:scenario:{base}/{sid}/{item["slug"]}', item) for item in entry['cards'])
    return f'''<section class="l3-section" id="{sid}">

  <header class="l3-section__head">
    <h2 class="l3-section__title">{esc(entry['section']['title'])}</h2>
    <p class="l3-section__intent">{esc(entry['section']['intent'])}</p>
  </header>

  <div class="scenarios-column-labels l3-section__column-labels" role="row" aria-hidden="true">
    <span class="scenarios-col-label scenarios-col-label--lens">Lens</span>
    <span class="scenarios-col-label scenarios-col-label--scenario">Scenario</span>
    <span class="scenarios-col-label scenarios-col-label--intent">Intent</span>
    <span class="scenarios-col-label scenarios-col-label--complexity">Complexity</span>
  </div>

  <div class="l3-section__scenarios">
{cards}
  </div>

</section>
    '''


def grow(text, pattern, added):
    """Increase the count that follows a heading or link matched by pattern."""
    def bump(match):
        old = int(match['n'])
        return match[0].replace(f'aria-label="{old} scenarios"', f'aria-label="{old + added} scenarios"').replace(f'({old})', f'({old + added})')
    text, n = re.subn(pattern, bump, text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'count not found: {pattern}')
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True)
    parser.add_argument('--input', required=True)
    args = parser.parse_args()
    root = Path(args.root)
    for entry in json.loads(Path(args.input).read_text()):
        page = root / entry['page']
        base = Path(entry['page']).parent.as_posix()
        area, sub = base.split('/')
        sid, added = entry['section']['id'], len(entry['cards'])
        text = page.read_text()
        if f'<section class="l3-section" id="{sid}">' in text:
            print('present', base, sid)
            continue
        end = text.index('</main>')
        last = text.rindex('</section>', 0, end) + len('</section>')
        page.write_text(text[:last] + '\n    \n    ' + section(base, entry) + text[last:])

        area_page = root / area / 'index.html'
        text = area_page.read_text()
        box_end = text.index(f'<a class="card__click-target" href="{sub}/index.html"')
        box_start = text.rindex('<article class="card', 0, box_end)
        box = text[box_start:box_end]
        groups_end = box.rindex('</div>\n    \n  </div>')
        group = f'''
      <div class="sub-group">
        <div class="sub-group__label">{esc(entry['section']['title'])}</div>
        <div class="sub-group__items">
          <a class="card-link" href="{sub}/index.html#{sid}">{esc(entry['section']['title'])} <span class="card-link__count">({added})</span></a>
        </div>
      </div>
      '''
        box = box[:groups_end] + group + box[groups_end:]
        box = grow(box, r'<span class="card__count" aria-label="(?P<n>\d+) scenarios">\((?P=n)\)</span>', added)
        area_page.write_text(text[:box_start] + box + text[box_end:])

        overview = root / 'index.html'
        text = overview.read_text()
        text = grow(text, re.escape(f'href="{area}/{sub}/index.html">') + r'[^<]*<span class="card-link__count">\((?P<n>\d+)\)</span>', added)
        area_head = re.search(r'<a class="card__click-target" href="' + re.escape(area) + r'/index.html"', text).start()
        head_start = text.rindex('<article class="card', 0, area_head)
        text = text[:head_start] + grow(text[head_start:area_head], r'<span class="card__count" aria-label="(?P<n>\d+) scenarios">\((?P=n)\)</span>', added) + text[area_head:]
        overview.write_text(text)
        print('added', base, sid, added)


if __name__ == '__main__':
    main()
