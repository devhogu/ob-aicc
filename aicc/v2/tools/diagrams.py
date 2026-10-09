# START_MODULE_CONTRACT
#   PURPOSE: Draw the Mermaid flows of the Hub pages to SVG, once per theme, cached, and give each a figure with a zoom button.
#   SCOPE: Reads ```mermaid blocks handed over by the builder; writes only its cache.
#   DEPENDS: node, the Mermaid and Puppeteer packages, a Chromium (the same environment as the repository's other diagrams)
#   LINKS: C-HUB-V2, M-PORTAL-SOURCE
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   GATE - label prefix that marks a control point
#   prepare - wrap long labels and give control points their class
#   render - draw every diagram in both themes; cached by content
# END_MODULE_MAP
"""Mermaid diagrams for the Hub site."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
CACHE = ROOT / 'portal' / '.cache' / 'mermaid-hub'
NPX = Path(os.environ.get('MMDC_NPX', os.path.expanduser('~/.npm/_npx/668c188756b835f3/node_modules')))
CHROME = os.environ.get('MMDC_CHROME', os.path.expanduser('~/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'))
LIBS = ROOT / 'portal' / '.tools' / 'pw-syslibs'
FONT = ROOT / 'aicc' / 'v2' / 'ui' / 'assets' / 'fonts' / 'golos-text' / 'GolosText-variable.woff2'
GATE = 'Точка контроля: '


def wrap(text, width=28):
    out = []
    for seg in text.split('<br/>'):
        line = ''
        for word in seg.split(' '):
            if line and len(line) + 1 + len(word) > width:
                out.append(line)
                line = word
            else:
                line = (line + ' ' + word).strip()
        out.append(line)
    return '<br/>'.join(out)


# START_CONTRACT: prepare
#   PURPOSE: Wrap node labels and mark control points: a node whose label starts with GATE gets the class gate (pink), and the prefix is dropped.
#   INPUTS: { code: str - Mermaid source }
#   OUTPUTS: { str - Mermaid source ready to draw }
#   SIDE_EFFECTS: none
# END_CONTRACT: prepare
def prepare(code):
    if not code.lstrip().startswith(('flowchart', 'graph')):
        return code
    gates = []

    def gate(m):
        gates.append(m[1])
        return f'{m[1]}["{m[2][:1].upper() + m[2][1:]}"]'
    code = re.sub(r'(\b[A-Za-z][A-Za-z0-9_]*)\["' + re.escape(GATE) + r'([^"]*)"\]', gate, code)
    lines = [l if l.lstrip().startswith('subgraph ') else re.sub(r'"([^"]*)"', lambda m: '"%s"' % wrap(m[1]), l) for l in code.split('\n')]
    code = '\n'.join(lines)
    if gates:
        code = code.rstrip('\n') + '\n  class %s gate\n' % ','.join(gates)
    return code


def key_of(code):
    return hashlib.sha256(code.encode('utf-8')).hexdigest()[:16]


# START_CONTRACT: render
#   PURPOSE: Draw each diagram in the light and the dark theme, reusing the cache; a diagram that cannot be drawn is reported and left out.
#   INPUTS: { codes: list - Mermaid sources }
#   OUTPUTS: { dict - key to {'light','dark'} SVG, or None when it could not be drawn }
#   SIDE_EFFECTS: Writes SVG files to the cache.
# END_CONTRACT: render
def render(codes):
    CACHE.mkdir(parents=True, exist_ok=True)
    jobs, keys = [], []
    for code in codes:
        prepared = prepare(code)
        key = key_of(prepared)
        keys.append(key)
        if not all((CACHE / f'{key}-{t}.svg').exists() for t in ('light', 'dark')):
            jobs.append({'key': key, 'code': prepared})
    if jobs:
        env = dict(os.environ)
        env['LD_LIBRARY_PATH'] = str(LIBS / 'usr' / 'lib' / 'x86_64-linux-gnu') + ':' + env.get('LD_LIBRARY_PATH', '')
        env['FONTCONFIG_PATH'] = str(LIBS / 'etc' / 'fonts')
        env['FONTCONFIG_FILE'] = str(LIBS / 'etc' / 'fonts' / 'portal.conf')
        payload = json.dumps({'jobs': jobs, 'font': str(FONT), 'mermaid': str(NPX / 'mermaid' / 'dist' / 'mermaid.min.js'),
                              'puppeteer': str(NPX / 'puppeteer'), 'chrome': CHROME})
        result = subprocess.run(['node', str(Path(__file__).with_name('render-mermaid.js'))], input=payload, capture_output=True, text=True, timeout=900, env=env)
        if result.stderr.strip():
            print(result.stderr.strip()[:1500], file=sys.stderr)
        drawn = json.loads(result.stdout) if result.stdout.strip() else {}
        for key, svgs in drawn.items():
            if 'light' in svgs and 'dark' in svgs:
                for theme in ('light', 'dark'):
                    (CACHE / f'{key}-{theme}.svg').write_text(svgs[theme], encoding='utf-8')
    out = {}
    for key in keys:
        paths = [CACHE / f'{key}-{t}.svg' for t in ('light', 'dark')]
        out[key] = {'light': paths[0].read_text(encoding='utf-8'), 'dark': paths[1].read_text(encoding='utf-8')} if all(p.exists() for p in paths) else None
    return out
