"""Cross-page consistency of terms in all patches. Prints counts; --write applies."""
import glob, json, re, sys, collections
R = [
 (r'аудиторск(ий|ого|ому|им|ом) трейл(а|у|ом|е)?\b', lambda m: 'аудиторск' + m[1] + ' след' + {'': '', 'а': 'а', 'у': 'у', 'ом': 'ом', 'е': 'е'}[m[2] or '']),
 (r'\bстюард(ы|а|у|ом|е|ов|ам|ами|ах)?\b(?: данных)?', None),
 (r'ключев(ые|ых|ым|ыми) элемент(ы|ов|ам|ами|ах) данных', lambda m: {'ые': 'критически важные', 'ых': 'критически важных', 'ым': 'критически важным', 'ыми': 'критически важными'}[m[1]] + ' элемент' + m[2] + ' данных'),
 (r'план(а|у|ом|е)? финансирования в кризисной ситуации', lambda m: 'план' + (m[1] or '') + ' экстренного фондирования'),
 (r'реестр(а|у|ом|е)? AI-систем\b', lambda m: 'реестр' + (m[1] or '') + ' AI-решений'),
]
STEWARD = {'': 'ответственный за данные', 'ы': 'ответственные за данные', 'а': 'ответственного за данные', 'у': 'ответственному за данные', 'ом': 'ответственным за данные', 'е': 'ответственном за данные', 'ов': 'ответственных за данные', 'ам': 'ответственным за данные', 'ами': 'ответственными за данные', 'ах': 'ответственных за данные'}
def steward(m):
    out = STEWARD[m[1] or '']
    return out[0].upper() + out[1:] if m[0][0].isupper() else out
count = collections.Counter()
for p in sorted(glob.glob('/tmp/ru-run/patch/*.json')):
    d = json.load(open(p)); changed = False
    for k, v in d.items():
        if not isinstance(v, str): continue
        new = v
        for pat, rep in R:
            fn = rep or steward
            new2, n = re.subn(pat, fn, new, flags=re.I if rep is None else 0)
            if n: count[pat[:30]] += n
            new = new2
        if new != v: d[k] = new; changed = True
    if changed and '--write' in sys.argv:
        json.dump(d, open(p, 'w'), ensure_ascii=False, indent=1)
print(dict(count))
