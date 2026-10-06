"""Russian edition of the Discovery Catalog from the current English pages.

The English and Russian pages share their markup: only texts and a few attribute values (aria-label,
lang, the language link) differ. A Russian page is therefore rebuilt from the current English page, with
the English texts replaced by Russian ones. Old Russian texts serve the translators as hints.

prepare  : align the starting English edition with the current Russian edition token by token, collect
           the dictionaries of fixed texts and attribute values, export the current English nodes, attach
           to each node the old Russian text of its counterpart, and write translation views and batches.
assemble : write the Russian pages from the current English pages and the translators' patches.
"""
import argparse
import collections
import difflib
import glob
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import dc  # noqa: E402

ATTRS = ('aria-label', 'title', 'alt', 'placeholder')
SCRIPT_LABEL = ('problem: "Problem to solve"', 'problem: "\\u0420\\u0435\\u0448\\u0430\\u0435\\u043c\\u0430\\u044f \\u0437\\u0430\\u0434\\u0430\\u0447\\u0430"')


def norm(text):
    return re.sub(r'\s+', ' ', html.unescape(text)).strip()


def pages(root):
    return sorted(os.path.relpath(p, root) for p in glob.glob(os.path.join(root, '**/index.html'), recursive=True) if '/assets/' not in p)


def attrs_of(tag):
    return dict(re.findall(r'\s([a-zA-Z-]+)="([^"]*)"', tag))


def align(en_text, ru_text):
    """Token pairs of two editions of one page; the tag sequences must agree apart from attribute values.

    Returns the two token lists and a map from each English token index to its Russian token index.
    Text tokens of whitespace only are ignored, since the editions differ there.
    """
    te, tr = dc.tokens(en_text), dc.tokens(ru_text)
    ie = [i for i, (k, v) in enumerate(te) if k != 'text' or v.strip()]
    ir = [i for i, (k, v) in enumerate(tr) if k != 'text' or v.strip()]
    def sig(t):
        kind, value = t
        return re.match(r'</?[\w!-]*', value)[0] if kind == 'tag' else 'T'
    matcher = difflib.SequenceMatcher(None, [sig(te[i]) for i in ie], [sig(tr[j]) for j in ir], autojunk=False)
    pair = {}
    for a0, b0, size in matcher.get_matching_blocks():
        for k in range(size):
            pair[ie[a0 + k]] = ir[b0 + k]
    return te, tr, pair


def cmd_prepare(a):
    os.makedirs(a.work, exist_ok=True)
    texts, attrs = collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)
    hints = {}
    for rel in pages(a.base_en):
        te, tr, pair = align(open(os.path.join(a.base_en, rel)).read(), open(os.path.join(a.ru, rel)).read())
        for i, j in pair.items():
            (kind, ve), (_, vr) = te[i], tr[j]
            if kind == 'text':
                texts[norm(ve)][vr.strip()] += 1
            elif kind == 'tag' and ve != vr:
                ae, ar = attrs_of(ve), attrs_of(vr)
                for name in ATTRS:
                    if name in ae and ae.get(name) != ar.get(name):
                        attrs[name + '|' + ae[name]][ar.get(name, '')] += 1
        # Old Russian per base English node, for hints: walk gives the editable nodes in order.
        base_nodes = [(i, role, card) for i, role, t, card in dc.walk(open(os.path.join(a.base_en, rel)).read())]
        hints[rel] = {'nodes': [(role, card, tr[pair[i]][1].strip() if i in pair else '') for i, role, card in base_nodes]}
        stages_en = dc.STAGES_RE.search(open(os.path.join(a.base_en, rel)).read())
        stages_ru = dc.STAGES_RE.search(open(os.path.join(a.ru, rel)).read())
        if stages_en and stages_ru:
            hints[rel]['stages'] = json.loads(stages_ru.group(2))
    json.dump({'texts': {k: v.most_common(1)[0][0] for k, v in texts.items()},
               'attrs': {k: v.most_common(1)[0][0] for k, v in attrs.items()}},
              open(os.path.join(a.work, 'dictionary.json'), 'w'), ensure_ascii=False, indent=0)

    # Current English nodes with the old Russian of their counterpart.
    for name in ('json', 'view', 'patch', 'report'):
        os.makedirs(os.path.join(a.work, name), exist_ok=True)
    parts = []
    for rel in pages(a.en):
        source = open(os.path.join(a.en, rel)).read()
        nodes = [(i, role, norm(t), card) for i, role, t, card in dc.walk(source) if role not in dc.EDITABLE_SKIP]
        old = hints.get(rel, {'nodes': []})['nodes']
        old_edit = [(role, card, text) for role, card, text in old if role not in dc.EDITABLE_SKIP]
        matcher = difflib.SequenceMatcher(None, [(r, c) for _, r, _, c in nodes], [(r, c) for r, c, _ in old_edit], autojunk=False)
        hint = {}
        for i1, j1, size in matcher.get_matching_blocks():
            for k in range(size):
                hint[nodes[i1 + k][0]] = old_edit[j1 + k][2]
        stages = []
        m = dc.STAGES_RE.search(source)
        if m:
            data, old_stages = json.loads(m.group(2)), hints.get(rel, {}).get('stages', {})
            for flow, items in data.items():
                for k, item in enumerate(items):
                    for key, value in item.items():
                        if isinstance(value, str) and key not in ('slug', 'urn', 'id') and value.strip():
                            previous = old_stages.get(flow, [{}] * (k + 1))
                            stages.append({'path': f'{flow}|{k}|{key}', 'text': value,
                                           'ru_old': previous[k].get(key, '') if k < len(previous) else ''})
        page = rel.replace('/index.html', '').replace('/', '__').replace('index.html', '_root')
        record = {'file': rel, 'nodes': [{'id': i, 'role': role, 'text': text, 'card': card, 'ru_old': hint.get(i, '')} for i, role, text, card in nodes], 'stages': stages}
        json.dump(record, open(os.path.join(a.work, 'json', page + '.json'), 'w'), ensure_ascii=False, indent=0)

        # Views: blocks per card or section; parts of at most a.part_bytes.
        blocks, current = [], None
        for n in record['nodes']:
            key = n['card'] or ''
            head = f'== card {n["card"]} ==\n' if n['card'] else ('== page ==\n' if current is None else '')
            if current is None or key != current['key'] or (not key and n['role'] in ('l3-section__title', 'card__eyebrow')):
                current = {'key': key, 'text': head or '== page, continued ==\n'}
                blocks.append(current)
            current['text'] += f'{n["id"]}\t{n["role"]}\t{n["text"]}\n' + (f'\t\t(было) {n["ru_old"]}\n' if n['ru_old'] else '')
        flows = collections.OrderedDict()
        for k, s in enumerate(stages):
            flow, pos, key = s['path'].rsplit('|', 2)
            flows.setdefault(flow, f'== stages of {flow} ==\n')
            flows[flow] += f's{k}\tstage {int(pos) + 1} {key}\t{s["text"]}\n' + (f'\t\t(было) {s["ru_old"]}\n' if s['ru_old'] else '')
        blocks += [{'key': f, 'text': t} for f, t in flows.items()]
        groups, size = [[]], 0
        for b in blocks:
            weight = len(b['text'].encode())
            if groups[-1] and size + weight > a.part_bytes:
                groups.append([]); size = 0
            groups[-1].append(b); size += weight
        for i, g in enumerate(groups):
            part = f'{page}.{i + 1}'
            body = f'PAGE {rel} — part {i + 1} of {len(groups)}\n\n' + '\n'.join(b['text'] for b in g)
            open(os.path.join(a.work, 'view', part + '.txt'), 'w').write(body)
            parts.append({'part': part, 'page': page, 'bytes': len(body.encode())})
    batches, size = [[]], 0
    for p in parts:
        fresh = not batches[-1] or batches[-1][-1]['page'] != p['page']
        if batches[-1] and fresh and size + p['bytes'] > a.batch_bytes:
            batches.append([]); size = 0
        batches[-1].append(p); size += p['bytes']
    json.dump(batches, open(os.path.join(a.work, 'batches.json'), 'w'), indent=1)
    print('pages', len(pages(a.en)), '| parts', len(parts), '| batches', len(batches), '| bytes', sum(p['bytes'] for p in parts))


def cmd_assemble(a):
    d = json.load(open(os.path.join(a.work, 'dictionary.json')))
    texts, attrs = d['texts'], d['attrs']
    missing_text, missing_attr, missing_patch = collections.Counter(), collections.Counter(), []
    written = 0
    only = set(a.pages.split(',')) if a.pages else None
    for rel in pages(a.en):
        page = rel.replace('/index.html', '').replace('/', '__').replace('index.html', '_root')
        if only and page not in only:
            continue
        record = json.load(open(os.path.join(a.work, 'json', page + '.json')))
        patch = {}
        for p in sorted(glob.glob(os.path.join(a.work, 'patch', page + '.*.json'))):
            patch.update(json.load(open(p)))
        source = open(os.path.join(a.en, rel)).read()
        toks = dc.tokens(source)
        editable = {n['id'] for n in record['nodes']}
        for n in record['nodes']:
            ru = patch.get(str(n['id']))
            if ru is None:
                missing_patch.append(f'{page}:{n["id"]}')
                continue
            kind, old = toks[n['id']]
            lead, trail = re.match(r'\s*', old).group(0), re.search(r'\s*$', old).group(0)
            toks[n['id']] = (kind, lead + dc.esc(ru.strip()) + trail)
        for i, (kind, value) in enumerate(toks):
            if kind == 'text' and value.strip() and i not in editable:
                ru = texts.get(norm(value))
                if ru is None:
                    if re.search(r'[A-Za-z]{2}', value):
                        missing_text[norm(value)] += 1
                    continue
                lead, trail = re.match(r'\s*', value).group(0), re.search(r'\s*$', value).group(0)
                toks[i] = (kind, lead + ru + trail)
            elif kind == 'tag':
                def swap(m):
                    name, val = m.group(1), m.group(2)
                    ru = attrs.get(name + '|' + val)
                    if ru is None:
                        if re.search(r'[A-Za-z]{3}', val) and name == 'aria-label':
                            missing_attr[val] += 1
                        return m.group(0)
                    return f' {name}="{ru}"'
                value = re.sub(r'\s(' + '|'.join(ATTRS) + r')="([^"]*)"', swap, value)
                value = value.replace('<html lang="en"', '<html lang="ru"')
                toks[i] = (kind, value)
        out = ''.join(t for _, t in toks)
        out = re.sub(r'href="([^"]*?)\.\./ru/([^"]*)" hreflang="ru"', r'href="\1../en/\2" hreflang="en"', out)
        out = out.replace(*SCRIPT_LABEL)
        m = dc.STAGES_RE.search(out)
        if m and record['stages']:
            data = json.loads(m.group(2))
            for k, s in enumerate(record['stages']):
                flow, pos, key = s['path'].rsplit('|', 2)
                ru = patch.get(f's{k}')
                if ru is None:
                    missing_patch.append(f'{page}:s{k}')
                    continue
                data[flow][int(pos)][key] = ru.strip()
            out = out[:m.start(2)] + json.dumps(data, ensure_ascii=False) + out[m.end(2):]
        target = os.path.join(a.out, rel)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        open(target, 'w').write(out)
        written += 1
    sync(a.en, a.out, [rel for rel in pages(a.en) if not only or rel.replace('/index.html', '').replace('/', '__').replace('index.html', '_root') in only])
    print('written', written, '| missing translations', len(missing_patch), '| fixed texts without Russian', len(missing_text), '| aria-labels without Russian', len(missing_attr))
    for x in missing_patch[:10]:
        print('   patch', x)
    for x, n in missing_text.most_common(30):
        print('   text', n, x[:100])
    for x, n in missing_attr.most_common(30):
        print('   attr', n, x[:100])


def titles(text):
    """Page title and section or flow titles by anchor, as plain text."""
    def plain(markup):
        return norm(re.sub(r'<[^>]+>', '', markup))
    head = re.search(r'<h1 class="page-header__title">(.*?)</h1>', text, re.S)
    found = {'': plain(head[1]) if head else ''}
    for m in re.finditer(r'<section class="l3-section" id="([^"]+)">.*?<h2 class="l3-section__title">(.*?)</h2>', text, re.S):
        found[m[1]] = plain(m[2])
    for m in re.finditer(r'<details class="flow-detail" id="([^"]+)">.*?<(h[23])[^>]*class="flow-detail__title[^"]*"[^>]*>(.*?)</\2>', text, re.S):
        found[m[1]] = plain(m[3])
    return found


def sync(en_root, ru_root, rels):
    """Labels that repeat a title in English repeat the Russian title; tab names and page titles follow."""
    en_titles = {rel: titles(open(os.path.join(en_root, rel)).read()) for rel in pages(en_root)}
    ru_titles = {rel: titles(open(os.path.join(ru_root, rel)).read()) for rel in pages(ru_root)}
    changed = 0
    for rel in rels:
        en, ru = open(os.path.join(en_root, rel)).read(), open(os.path.join(ru_root, rel)).read()
        te, tr = dc.tokens(en), dc.tokens(ru)
        if len(te) != len(tr):
            print('   sync skipped (structure):', rel); continue

        def target(href):
            path, _, anchor = href.partition('#')
            trel = os.path.normpath(os.path.join(os.path.dirname(rel), path)) if path else rel
            return trel, anchor
        article_target = None
        for k, (kind, value) in enumerate(te):
            if kind != 'tag':
                continue
            if value.startswith('<article'):
                for j in range(k, len(te)):
                    if te[j][0] == 'tag' and te[j][1].startswith('</article'):
                        break
                    m = re.match(r'<a class="card__click-target" href="([^"]+)"', te[j][1])
                    if m:
                        article_target = target(m[1]); break
                else:
                    article_target = None
            m = re.match(r'<a\b[^>]*class="[^"]*(?:card-link|breadcrumb__link)[^"]*"[^>]*href="([^"]+)"|<a\b[^>]*href="([^"]+)"[^>]*class="[^"]*card-link', value)
            if m:
                where = target(m[1] or m[2])
            elif re.match(r'<h[23] class="card__title', value) and article_target:
                where = article_target
            else:
                continue
            if k + 1 >= len(te) or te[k + 1][0] != 'text':
                continue
            trel, anchor = where
            en_title, ru_title = en_titles.get(trel, {}).get(anchor), ru_titles.get(trel, {}).get(anchor)
            if en_title and ru_title and norm(te[k + 1][1]).lower() == en_title.lower() and norm(tr[k + 1][1]) != ru_title:
                old = tr[k + 1][1]
                lead, trail = re.match(r'\s*', old).group(0), re.search(r'\s*$', old).group(0)
                tr[k + 1] = ('text', lead + dc.esc(ru_title) + trail)
                changed += 1
        out = ''.join(t for _, t in tr)
        own = ru_titles[rel]['']
        if own:
            out = re.sub(r'(<title>).*?(</title>)', lambda m: m[1] + dc.esc(own) + m[2], out, count=1, flags=re.S)
            out = re.sub(r'(<span class="breadcrumb__current"[^>]*>).*?(</span>)', lambda m: m[1] + dc.esc(own) + m[2], out, count=1, flags=re.S)
        stages = dc.STAGES_RE.search(out)
        if stages:
            # Diagram buttons repeat the label of their stage.
            data = json.loads(stages.group(2))
            def button(m):
                flow = re.search(r'data-flow-id="([^"]+)"', m[1]); slug = re.search(r'data-stage="([^"]+)"', m[1])
                if flow and slug:
                    for item in data.get(flow[1], []):
                        if item.get('slug') == slug[1] and item.get('label'):
                            return m[0][:m.start(3) - m.start(0)] + dc.esc(item['label']) + m[0][m.end(3) - m.start(0):]
                return m[0]
            out = re.sub(r'<button\b([^>]*)>(\s*<span class="flow-stages__stage-label">)(.*?)</span>', button, out, flags=re.S)
        def plural(n):
            n = int(n)
            if n % 10 == 1 and n % 100 != 11:
                return f'{n} сценарий'
            if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
                return f'{n} сценария'
            return f'{n} сценариев'
        out = re.sub(r'aria-label="(\d+) scenarios?"', lambda m: f'aria-label="{plural(m[1])}"', out)

        def box(m):
            article = m[0]
            head = re.search(r'<h[23] class="card__title[^"]*">(.*?)(?:<span class="card__count"|</h[23]>)', article, re.S)
            if head:
                name = norm(re.sub(r'<[^>]+>', '', head[1]))
                article = re.sub(r'(<a class="card__click-target"[^>]*aria-label=")[^"]*(")', lambda x: x[1] + name.replace('&', '&amp;').replace('"', '&quot;') + x[2], article, count=1)
            return article
        out = re.sub(r'<article class="card[^"]*"[^>]*>.*?</article>', box, out, flags=re.S)
        labels = {m[1]: m[2].strip() for m in re.finditer(r'<label\s+class="problems-tab-label"\s+for="([^"]+)"[^>]*>(.*?)</label>', out, re.S)}
        out = re.sub(r'(<input\s+type="radio"\s+class="problems-tab-input"\s+name="problems-tabs"\s+id="([^"]+)".*?aria-label=")([^"]*)(")',
                     lambda m: m[1] + labels.get(m[2], m[3]) + m[4], out, flags=re.S)
        open(os.path.join(ru_root, rel), 'w').write(out)
    print('labels synchronized', changed)


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('prepare')
    s.add_argument('--en', required=True); s.add_argument('--base-en', required=True); s.add_argument('--ru', required=True); s.add_argument('--work', required=True)
    s.add_argument('--part-bytes', type=int, default=60000); s.add_argument('--batch-bytes', type=int, default=150000)
    s = sub.add_parser('assemble')
    s.add_argument('--en', required=True); s.add_argument('--work', required=True); s.add_argument('--out', required=True); s.add_argument('--pages')
    a = p.parse_args()
    {'prepare': cmd_prepare, 'assemble': cmd_assemble}[a.cmd](a)


if __name__ == '__main__':
    main()
