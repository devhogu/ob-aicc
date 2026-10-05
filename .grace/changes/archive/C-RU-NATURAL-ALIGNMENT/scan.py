#!/usr/bin/env python3
"""Scan the in-scope Russian sources for calque markers; write a per-file JSON report.

Usage: python3 .grace/changes/active/C-RU-NATURAL-ALIGNMENT/scan.py OUT.json
Markers: rejected forms of the translation map (by map section), Latin words in Russian prose,
and defined terms of Vocabulary and Style written with a capital letter inside a sentence.
"""
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
MAP = ROOT / 'charter/ru/translation-en-ru-map.md'
VOCAB = ROOT / 'charter/ru/documents/vocabulary.md'
# Fixed names and bodies that keep their capital letter in Russian usage.
KEEP = {'Банк', 'Совет', 'Комитет', 'Правление', 'AICC', 'SLA', 'KPI', 'WIP', 'Service', 'Портал', 'Операционный',
        'Корпоративный', 'Управляющий', 'Ежегодное', 'Минимально', 'Бизнес-модель', 'Каталог', 'Три', 'Четыре'}


def sources():
    files = [p for p in glob.glob(str(ROOT / 'charter/ru/**/*.md'), recursive=True) if not p.endswith('translation-en-ru-map.md')]
    files += glob.glob(str(ROOT / 'portal/content/ru/**/*.md'), recursive=True)
    out = {Path(p).relative_to(ROOT).as_posix(): Path(p).read_text(encoding='utf-8') for p in sorted(files)}
    authored = json.loads((ROOT / 'portal/content/authored.json').read_text(encoding='utf-8'))
    ru = []

    def walk(v):
        if isinstance(v, dict):
            if v and set(v) <= {'en', 'ru', 'ky'}:
                if isinstance(v.get('ru'), str):
                    ru.append(v['ru'])
                return
            for x in v.values():
                walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)
    walk(authored)
    out['portal/content/authored.json#ru'] = '\n'.join(ru)
    out['portal/messages/ru.json'] = '\n'.join(str(v) for v in json.loads((ROOT / 'portal/messages/ru.json').read_text(encoding='utf-8')).values())
    return out


def prose(text):
    text = re.sub(r'^```.*?^```', '', text, flags=re.S | re.M)          # front matter and diagrams
    text = re.sub(r'`[^`]*`', '', text)
    text = re.sub(r'\]\([^)]*\)', ']', text)                            # link targets
    text = re.sub(r'https?://\S+', '', text)
    return text


def rejected_forms():
    section, forms = None, []
    for line in MAP.read_text(encoding='utf-8').splitlines():
        m = re.match(r'#{2,3} (\d)', line)
        if m:
            section = m.group(1)
        if line.startswith('| ') and 'не:' in line:
            en = line.split('|')[1].strip()
            for seg in re.findall(r'не:\s*((?:«[^»]+»(?:,\s*)?)+)', line):
                for q in re.findall(r'«([^»…]+)»', seg):
                    forms.append({'section': section, 'en': en, 'form': q.strip()})
    return forms


def defined_stems():
    stems = set()
    # The baseline Vocabulary still writes terms with capitals; it fixes the term list for every scan.
    import subprocess
    text = subprocess.run(['git', 'show', 'ae1889f8:charter/ru/documents/vocabulary.md'], cwd=ROOT,
                          capture_output=True, text=True).stdout or VOCAB.read_text(encoding='utf-8')
    body = text.split('## 4.')[1].split('## Журнал')[0]
    for line in body.splitlines():
        if line.startswith('| ') and not line.startswith('| ---') and not line.startswith('| Термин'):
            for word in line.split('|')[1].strip().split():
                if re.match(r'[А-ЯЁ][а-яё-]{3,}$', word) and word not in KEEP:
                    stems.add(word[:max(4, len(word) - 2)])
    return sorted(stems)


def scan():
    forms, stems = rejected_forms(), defined_stems()
    cap = re.compile(r'(?<![.!?:|#«>\n]\s)(?<=[а-яё,;)]\s)(%s)[а-яё-]*' % '|'.join(map(re.escape, stems)))
    report = {}
    for path, raw in sources().items():
        text = prose(raw)
        rej = {}
        for f in forms:
            # Whole words; the first letter may differ in case only at a sentence start.
            form = f['form']
            first = '[%s%s]' % (form[0].upper(), form[0].lower()) if form[:1].isalpha() else re.escape(form[:1])
            n = len(re.findall(r'(?<![\w-])' + first + re.escape(form[1:]) + r'(?![\w-])', text))
            if n:
                rej['%s | %s' % (f['section'], f['form'])] = n
        latin = re.findall(r'(?<![\w@/.-])[a-z][a-z-]{3,}(?: [a-z][a-z-]{3,})*', text)
        caps = [m.group(0) for m in cap.finditer(text)]
        report[path] = {'rejected': rej, 'rejected_total': sum(rej.values()),
                        'latin': len(latin), 'latin_sample': sorted(set(latin))[:15],
                        'capitalised_terms': len(caps)}
    totals = {k: sum(r[k] for r in report.values()) for k in ('rejected_total', 'latin', 'capitalised_terms')}
    return {'totals': totals, 'files': report}


if __name__ == '__main__':
    result = scan()
    Path(sys.argv[1]).write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(json.dumps(result['totals']))
