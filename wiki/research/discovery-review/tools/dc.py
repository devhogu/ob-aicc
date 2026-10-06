#!/usr/bin/env python3
"""Discovery Catalog content tool: structured fixes, text export/import, verification.

The catalog source is html-alt/financial-services/<lang>/**/index.html. Text is edited through a JSON view of the
text nodes so that markup, identifiers and classes cannot be changed by an edit.

  dc.py structured --root R --fixmap DIR     apply OKR, lens and complexity entries of the fix maps to the HTML
  dc.py export     --root R --out DIR        write one JSON per page with every text node of the body (without the footer), <title> and the stage map
  dc.py import     --root R --in DIR         write edited JSON texts back into the HTML
  dc.py verify     --root R [--baseline B]   check structure, completeness and wording invariants
"""
import argparse, collections, glob, html, json, os, re, sys

LENS = {'Insights': 'insights', 'Automation': 'automation', 'Enablement': 'enablement', 'Optimize': 'optimize', 'New opps': 'new-opps'}
CARD_RE = re.compile(r'(<details[^>]*class="[^"]*scenario-card[^"]*"[^>]*data-urn="([^"]*)"[^>]*>)(.*?)(</details>)', re.S)
OPAQUE_RE = re.compile(r'(<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->)', re.S)
STAGES_RE = re.compile(r'(const FLOW_STAGES = )(\{.*?\})(;\s*\n)', re.S)


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def norm(t):
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()


def pages(root):
    return sorted(glob.glob(os.path.join(root, '**', '*.html'), recursive=True))


def okr_markup(o):
    krs = ''.join('\n        <div class="okr-kr">\n          <div class="okr-kr__dim">%s</div>\n          <p>%s</p>\n        </div>\n        ' % (d, esc(o[k]))
                  for d, k in (('Adoption', 'adoption'), ('Acceptance', 'acceptance'), ('Cycle', 'cycle')))
    return '\n      <div class="scenario-section__label">OKR</div>\n      \n      <p class="okr-objective">%s</p>\n      \n      <div class="okr-grid">\n        %s\n      </div>\n    ' % (esc(o['objective']), krs)


def cmd_structured(a):
    entries = []
    for f in sorted(glob.glob(os.path.join(a.fixmap, '*.jsonl'))):
        entries += [json.loads(l) for l in open(f) if l.strip()]
    by_file = collections.defaultdict(list)
    for e in entries:
        if e.get('field') in ('okr', 'lens', 'complexity'):
            by_file[e['file']].append(e)
    done = collections.Counter(); failed = []
    for file, es in by_file.items():
        rel = file.split('/en/', 1)[1] if '/en/' in file else file
        path = os.path.join(a.root, rel)
        if not os.path.exists(path):
            failed += [(e['id'], 'no file') for e in es]; continue
        s = open(path).read()
        for e in es:
            cards = [(m.start(), m.end(), m.group(2), m.group(0)) for m in CARD_RE.finditer(s)]
            target = [c for c in cards if e.get('urn') and c[2] == e['urn']]
            if not target:
                key = norm(e.get('locator') or '')
                def title_of(c):
                    t = re.search(r'class="scenario-card__title"[^>]*>(.*?)</h3>', c[3], re.S)
                    return norm(re.sub(r'<[^>]+>', '', t.group(1))) if t else ''
                target = [c for c in cards if key and (title_of(c) == key or title_of(c) in key)]
            if len(target) != 1:
                failed.append((e['id'], 'card not found or ambiguous (%d)' % len(target))); continue
            st, en, urn, card = target[0]
            new = card
            if e['field'] == 'okr':
                o = e['proposed']
                sec = re.search(r'(<div class="scenario-section">)(\s*<div class="scenario-section__label">OKR</div>.*?)(</div>\s*</div>\s*</details>)', card, re.S)
                if not sec or not isinstance(o, dict):
                    failed.append((e['id'], 'okr section not found')); continue
                new = card[:sec.start(2)] + okr_markup(o) + '</div>\n    \n\n  </div>\n</details>'
            elif e['field'] == 'lens':
                if e['proposed'] not in LENS:
                    failed.append((e['id'], 'unknown lens %r' % e['proposed'])); continue
                new, n = re.subn(r'<span class="scenario-lens scenario-lens--[a-z-]+">[^<]*</span>',
                                 '<span class="scenario-lens scenario-lens--%s">%s</span>' % (LENS[e['proposed']], e['proposed']), card, count=1)
                if not n: failed.append((e['id'], 'lens span not found')); continue
            else:
                v = e['proposed'].strip()
                if v not in ('S', 'M', 'L', 'XL'):
                    failed.append((e['id'], 'unknown complexity %r' % v)); continue
                new, n = re.subn(r'(class="scenario-complexity scenario-complexity--)(?:S|M|L|XL)("[^>]*>)\s*(?:S|M|L|XL)\s*(</span>)', r'\g<1>%s\g<2>%s\g<3>' % (v, v), card, count=1, flags=re.S)
                if not n: failed.append((e['id'], 'complexity span not found')); continue
            s = s[:st] + new + s[en:]
            done[e['field']] += 1
        open(path, 'w').write(s)
    print('applied', dict(done)); print('failed', len(failed))
    for x in failed: print('  ', x)


def tokens(s):
    """Split into opaque blocks, tags and text; text tokens are the only editable ones."""
    out = []
    for part in OPAQUE_RE.split(s):
        if OPAQUE_RE.fullmatch(part or ''):
            out.append(('opaque', part))
        else:
            for t in re.split(r'(<[^>]+>)', part):
                if t:
                    out.append(('tag' if t.startswith('<') and t.endswith('>') else 'text', t))
    return out


def walk(s):
    """Yield (index, kind, token, context) where context describes where a text node sits."""
    toks = tokens(s)
    stack = []; in_main = False; in_title = False; card = None; label = None; dim = None
    for i, (kind, t) in enumerate(toks):
        if kind == 'tag':
            m = re.match(r'<(/?)([a-zA-Z0-9]+)([^>]*)>', t)
            if not m: continue
            close, name, attrs = m.group(1), m.group(2).lower(), m.group(3)
            # The editable region is the body down to the footer: page header, problem rows and the main content.
            if name == 'body' and not close: in_main = True
            if name == 'footer' and not close: in_main = False
            if name == 'title': in_title = not close
            if name in ('br', 'img', 'hr', 'input', 'meta', 'link') or attrs.rstrip().endswith('/'): continue
            if close:
                while stack:
                    top = stack.pop()
                    if top[0] == name:
                        if name == 'details' and top[2]: card = None; label = None
                        break
            else:
                cls = (re.search(r'class="([^"]*)"', attrs) or [0, ''])[1]
                urn = (re.search(r'data-urn="([^"]*)"', attrs) or [0, ''])[1] if 'scenario-card' in cls else ''
                if urn: card = urn; label = None; dim = None
                stack.append((name, cls, urn))
        elif kind == 'text' and t.strip() and (in_main or in_title):
            cls = next((c for n, c, u in reversed(stack) if c), '')
            parent = stack[-1][0] if stack else ''
            role = cls.split()[0] if cls else parent
            if in_title and not in_main: role = 'html-title'
            if role == 'scenario-section__label': label = norm(t)
            if role == 'okr-kr__dim': dim = norm(t)
            if card:
                if role == 'scenario-section' or (parent == 'p' and cls.startswith('scenario-section')):
                    role = {'Problem to solve': 'problem', 'Solution': 'solution'}.get(label, 'section-text')
                elif role == 'okr-kr': role = 'okr-' + (dim or 'kr').lower()
                elif role == 'okr-objective': role = 'okr-objective'
                elif role == 'scenario-card__title': role = 'title'
                elif role == 'scenario-card__intent': role = 'intent'
            yield i, role, t, card
    return


EDITABLE_SKIP = {'scenario-section__label', 'okr-kr__dim', 'scenario-lens', 'scenario-complexity', 'scenario-card__chevron', 'skip-link', 'breadcrumb__sep'}


def cmd_export(a):
    os.makedirs(a.out, exist_ok=True); total = 0
    for path in pages(a.root):
        rel = os.path.relpath(path, a.root); s = open(path).read()
        page, cards = [], collections.OrderedDict()
        for i, role, t, card in walk(s):
            if role in EDITABLE_SKIP: 
                if card and role in ('scenario-lens', 'scenario-complexity'):
                    cards.setdefault(card, {'urn': card, 'nodes': []})[role.split('-')[1]] = norm(t)
                continue
            node = {'id': i, 'role': role, 'text': norm(t)}
            if card: cards.setdefault(card, {'urn': card, 'nodes': []})['nodes'].append(node)
            else: page.append(node)
            total += 1
        stages = []
        m = STAGES_RE.search(s)
        if m:
            data = json.loads(m.group(2))
            for flow, lst in data.items():
                for k, st in enumerate(lst):
                    for key, val in st.items():
                        if isinstance(val, str) and key not in ('slug', 'urn', 'id') and val.strip():
                            stages.append({'path': '%s|%d|%s' % (flow, k, key), 'text': val}); total += 1
        name = rel.replace('/index.html', '').replace('/', '__').replace('index.html', '_root')
        json.dump({'file': rel, 'page': page, 'cards': list(cards.values()), 'stages': stages},
                  open(os.path.join(a.out, name + '.json'), 'w'), ensure_ascii=False, indent=1)
    print('exported', len(pages(a.root)), 'pages,', total, 'text nodes')


def cmd_import(a):
    changed = 0; problems = []
    for jf in sorted(glob.glob(os.path.join(getattr(a, 'in'), '*.json'))):
        d = json.load(open(jf)); path = os.path.join(a.root, d['file']); s = open(path).read()
        toks = tokens(s)
        nodes = d['page'] + [n for c in d['cards'] for n in c['nodes']]
        expected = {i for i, role, t, card in walk(s) if role not in EDITABLE_SKIP}
        got = {n['id'] for n in nodes}
        if expected != got:
            problems.append((d['file'], 'node ids differ: missing %s extra %s' % (sorted(expected - got)[:5], sorted(got - expected)[:5]))); continue
        for n in nodes:
            kind, old = toks[n['id']]
            if norm(old) != n['text'].strip():
                lead = re.match(r'\s*', old).group(0); trail = re.search(r'\s*$', old).group(0)
                toks[n['id']] = (kind, lead + esc(n['text'].strip()) + trail); changed += 1
        out = ''.join(t for k, t in toks)
        m = STAGES_RE.search(out)
        if m and d.get('stages'):
            data = json.loads(m.group(2))
            for st in d['stages']:
                flow, k, key = st['path'].rsplit('|', 2)
                if data[flow][int(k)][key] != st['text']:
                    data[flow][int(k)][key] = st['text']; changed += 1
            out = out[:m.start(2)] + json.dumps(data, ensure_ascii=False) + out[m.end(2):]
        open(path, 'w').write(out)
    print('texts changed', changed, '| problems', len(problems))
    for p in problems: print('  ', p)
    return 1 if problems else 0


FORBIDDEN = {
    'CBR / Bank of Russia': r'\bCBR\b|Bank of Russia', 'NBK (Kazakhstan)': r'\bNBK\b', 'ARDFM': r'\bARDFM\b', 'NBKR': r'\bNBKR\b',
    'Kazakhstan / Russia': r'Kazakhstan|\bRussia\b|\bRussian\b', 'KZT / RUB / KASE / MOEX': r'\bKZT\b|\bRUB\b|\bKASE\b|\bMOEX\b',
    'US/UK bodies': r'\bFinCEN\b|\bBSA officer\b|\bCFPB\b|\bOCC\b|\bFCA\b|Consumer Duty|Rosfinmonitoring',
    '>=100%': r'≥\s*100\s*%', 'placeholder': r'service\.eyebrow', 'British -isation': r'\b\w+isation\b', 'bare Agent actor': r'(?<!AI )\bAgent (?:reads|drafts|analyses|analyzes|generates|monitors|produces|compiles|scores|delivers|assembles|flags|tracks)',
    'the bank (lower case)': r'\bthe bank\b',
}


def cmd_verify(a):
    cards = 0; empty = 0; shape = collections.Counter(); urns = []; hits = collections.Counter(); bad = []
    for path in pages(a.root):
        s = open(path).read()
        m_ = re.sub(r'<script\b.*?</script>', '', s, flags=re.S)
        if m_.count('<details') != m_.count('</details>') or m_.count('<div') != m_.count('</div>'):
            bad.append((os.path.relpath(path, a.root), 'unbalanced tags'))
        for m in CARD_RE.finditer(s):
            cards += 1; urns.append(m.group(2)); c = m.group(0)
            o, k = c.count('class="okr-objective"'), c.count('class="okr-kr"')
            shape[(o, k)] += 1; empty += (o == 0)
            for f in ('scenario-card__title', 'scenario-card__intent'):
                t = re.search(r'class="%s"[^>]*>(.*?)</(?:h3|p)>' % f, c, re.S)
                if not t or not norm(re.sub(r'<[^>]+>', '', t.group(1))): bad.append((m.group(2), 'empty ' + f))
        vis = html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<style.*?</style>', '', s, flags=re.S)))
        for name, pat in FORBIDDEN.items(): hits[name] += len(re.findall(pat, vis))
    print('pages', len(pages(a.root)), '| cards', cards, '| unique urns', len(set(urns)), '| empty OKR', empty, '| OKR shapes', dict(shape))
    if a.baseline:
        base = [m.group(2) for p in pages(a.baseline) for m in CARD_RE.finditer(open(p).read())]
        print('urns vs baseline: missing', len(set(base) - set(urns)), 'added', len(set(urns) - set(base)), '| order same:', base == urns)
    print('wording scan:'); [print('   %-28s %d' % kv) for kv in hits.items()]
    print('structural problems', len(bad)); [print('  ', b) for b in bad[:20]]


def main():
    p = argparse.ArgumentParser(); sub = p.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('structured'); s.add_argument('--root', required=True); s.add_argument('--fixmap', required=True)
    s = sub.add_parser('export'); s.add_argument('--root', required=True); s.add_argument('--out', required=True)
    s = sub.add_parser('import'); s.add_argument('--root', required=True); s.add_argument('--in', required=True)
    s = sub.add_parser('verify'); s.add_argument('--root', required=True); s.add_argument('--baseline')
    a = p.parse_args()
    sys.exit({'structured': cmd_structured, 'export': cmd_export, 'import': cmd_import, 'verify': cmd_verify}[a.cmd](a) or 0)


if __name__ == '__main__':
    main()
