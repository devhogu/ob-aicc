"""Work packages for the rewording agents, and the merge of their patches (RUNBOOK.md steps 5 and 6).

view  : from the exported page JSON, write compact text views (one or more parts per page), the fix
        entries of each part, and a packing of the parts into agent batches.
merge : apply the patches written by the agents ({key: new text}) to the exported JSON, producing the
        JSON that `dc.py import` reads. A key is a node id, or `s<n>` for the n-th stage text.
"""
import argparse
import collections
import glob
import json
import os
import re

# Shown to nobody: fixed labels, counts and texts that follow the page title (synchronized after import).
HIDDEN = {'scenarios-col-label', 'card__count', 'card-link__count', 'html-title', 'breadcrumb__link', 'breadcrumb__current', 'dot'}
HANDLED = {'okr', 'lens', 'complexity', 'structure', 'count'}


def norm(text):
    return re.sub(r'\s+', ' ', text).strip().lower()


def line(key, role, text):
    return f'{key}\t{role}\t{text}'.replace('\n', ' ⏎ ') + '\n'


def blocks_of(data):
    """A page as blocks that may not be split: the page nodes by section, each card, the stages of each flow."""
    blocks, current = [], None
    for node in data['page']:
        if node['role'] in HIDDEN or not re.search(r'[A-Za-zА-Яа-я]', node['text']):
            continue
        if current is None or node['role'] in ('l3-section__title', 'card__eyebrow'):
            current = {'head': '== page ==\n' if current is None else '== page, continued ==\n', 'lines': [], 'texts': [], 'urn': '', 'order': node['id']}
            blocks.append(current)
        current['lines'].append(line(node['id'], node['role'], node['text']))
        current['texts'].append(node['text'])
    for card in data['cards']:
        block = {'head': f"== card {card['urn']} | lens {card.get('lens', '')} | complexity {card.get('complexity', '')} ==\n",
                 'lines': [], 'texts': [], 'urn': card['urn'], 'order': card['nodes'][0]['id']}
        for node in card['nodes']:
            block['lines'].append(line(node['id'], node['role'], node['text']))
            block['texts'].append(node['text'])
        blocks.append(block)
    blocks.sort(key=lambda b: b['order'])
    flows = collections.OrderedDict()
    for index, stage in enumerate(data.get('stages', [])):
        flow, position, key = stage['path'].rsplit('|', 2)
        block = flows.setdefault(flow, {'head': f'== stages of {flow} ==\n', 'lines': [], 'texts': [], 'urn': ''})
        block['lines'].append(line(f's{index}', f'stage {int(position) + 1} {key}', stage['text']))
        block['texts'].append(stage['text'])
    return blocks + list(flows.values())


def cmd_view(args):
    for name in ('view', 'fix', 'patch', 'report'):
        os.makedirs(os.path.join(args.out, name), exist_ok=True)
    parts, unplaced = [], 0
    for path in sorted(glob.glob(os.path.join(args.json, '*.json'))):
        page = os.path.basename(path)[:-5]
        data = json.load(open(path))
        groups, size = [[]], 0
        for block in blocks_of(data):
            weight = len(block['head']) + sum(len(l.encode()) for l in block['lines'])
            if groups[-1] and size + weight > args.part_bytes:
                groups.append([]); size = 0
            groups[-1].append(block); size += weight
        fix_path = os.path.join(args.fixes, page + '.json')
        entries = [e for e in (json.load(open(fix_path)) if os.path.exists(fix_path) else [])
                   if e['field'] not in HANDLED and not (e['field'] == 'problem_row' and not e.get('current'))]
        placed = collections.defaultdict(list)
        for entry in entries:
            target = [i for i, g in enumerate(groups) if entry.get('urn') and any(b['urn'] == entry['urn'] for b in g)]
            if not target:
                probe = norm(entry.get('current') or '')[:50]
                target = [i for i, g in enumerate(groups) if probe and any(probe in norm(t) for b in g for t in b['texts'])]
            if not target:
                target = list(range(len(groups))); unplaced += 1
            for i in target[:1] if len(target) < len(groups) or len(groups) == 1 else target:
                placed[i].append(entry)
        for i, group in enumerate(groups):
            part = f'{page}.{i + 1}'
            text = (f"PAGE {data['file']} — part {i + 1} of {len(groups)}\n"
                    'Each line: key <tab> role <tab> text. Patch keys are the keys of this file.\n\n'
                    + ''.join(b['head'] + ''.join(b['lines']) + '\n' for b in group))
            open(os.path.join(args.out, 'view', part + '.txt'), 'w').write(text)
            json.dump(placed[i], open(os.path.join(args.out, 'fix', part + '.json'), 'w'), ensure_ascii=False, indent=1)
            parts.append({'part': part, 'page': page, 'bytes': len(text.encode()), 'fixes': len(placed[i])})
    batches, size = [[]], 0
    for part in parts:
        last = batches[-1][-1]['page'] if batches[-1] else None
        page_bytes = sum(p['bytes'] for p in parts if p['page'] == part['page'])
        fresh = part['page'] != last
        if batches[-1] and ((fresh and size + min(page_bytes, args.batch_bytes) > args.batch_bytes) or size + part['bytes'] > args.batch_bytes):
            batches.append([]); size = 0
        batches[-1].append(part); size += part['bytes']
    json.dump(batches, open(os.path.join(args.out, 'batches.json'), 'w'), indent=1)
    print('parts', len(parts), '| batches', len(batches), '| bytes', sum(p['bytes'] for p in parts),
          '| fix entries', sum(p['fixes'] for p in parts), '| given to every part', unplaced)
    for i, batch in enumerate(batches):
        print(f'  {i + 1:2d}', sum(p['bytes'] for p in batch) // 1024, 'KB', ' '.join(p['part'] for p in batch))


def cmd_merge(args):
    os.makedirs(args.out, exist_ok=True)
    changed, problems, missing = 0, [], []
    for path in sorted(glob.glob(os.path.join(args.json, '*.json'))):
        page = os.path.basename(path)[:-5]
        data = json.load(open(path))
        nodes = {str(n['id']): n for n in data['page'] + [n for c in data['cards'] for n in c['nodes']]}
        nodes.update({f's{i}': s for i, s in enumerate(data.get('stages', []))})
        expected = len(glob.glob(os.path.join(args.work, 'view', page + '.*.txt')))
        found = sorted(glob.glob(os.path.join(args.work, 'patch', page + '.*.json')))
        if len(found) != expected:
            missing.append(f'{page}: {len(found)} of {expected} patches')
        for patch_path in found:
            try:
                patch = json.load(open(patch_path))
            except ValueError as error:
                problems.append(f'{os.path.basename(patch_path)}: {error}'); continue
            view = open(os.path.join(args.work, 'view', os.path.basename(patch_path)[:-5] + '.txt')).read()
            allowed = set(re.findall(r'^(s?\d+)\t', view, re.M))
            for key, text in patch.items():
                if key not in nodes or key not in allowed:
                    problems.append(f'{os.path.basename(patch_path)}: unknown key {key}'); continue
                if not isinstance(text, str) or not text.strip() or '<' in text and re.search(r'</?[a-z]+[ >]', text):
                    problems.append(f'{os.path.basename(patch_path)}: bad text for {key}'); continue
                text = re.sub(r'\s+', ' ', text.replace('⏎', ' ')).strip()
                if nodes[key]['text'] != text:
                    nodes[key]['text'] = text; changed += 1
        json.dump(data, open(os.path.join(args.out, page + '.json'), 'w'), ensure_ascii=False, indent=1)
    print('texts changed', changed, '| missing', len(missing), '| problems', len(problems))
    for item in missing + problems:
        print('  ', item)


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='cmd', required=True)
    view = sub.add_parser('view')
    view.add_argument('--json', required=True); view.add_argument('--fixes', required=True); view.add_argument('--out', required=True)
    view.add_argument('--part-bytes', type=int, default=46000); view.add_argument('--batch-bytes', type=int, default=135000)
    merge = sub.add_parser('merge')
    merge.add_argument('--json', required=True); merge.add_argument('--work', required=True); merge.add_argument('--out', required=True)
    args = parser.parse_args()
    {'view': cmd_view, 'merge': cmd_merge}[args.cmd](args)


if __name__ == '__main__':
    main()
