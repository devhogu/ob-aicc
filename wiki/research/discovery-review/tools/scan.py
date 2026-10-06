"""Self-check of one part: apply patch/<part>.json to view/<part>.txt and list what still needs attention.
Usage: python3 /tmp/dc-run/scan.py <part> [<part> ...]"""
import json, os, re, sys
W = '/tmp/dc-run'
HARD = {
 'regulator named': r'\bNBKR\b|\bCBR\b|\bNBK\b|\bARDFM\b|\bAFSA\b|\bAFMRK\b|Bank of Russia|National Bank of (?:Kazakhstan|the Kyrgyz|Kyrgyz)|Central Bank of',
 'FIU / foreign officer': r'\bFinCEN\b|Rosfinmonitoring|\bBSA\b|\bMLRO\b|\bCFPB\b|\bOCC\b|\bFCA\b|\bPRA\b|Consumer Duty|money.transmitter',
 'country / region': r'Kazakh\w*|\bRussian?\b|Kyrgyz\w*|\bCIS\b|Uzbek\w*|Tajik\w*|Central Asia\w*|three jurisdictions|\bKZ\b|\bRU\b|\bKG\b|Eurasian|\bEAEU\b',
 'currency / market': r'\bKZT\b|\bRUB\b|\bKGS\b|\btenge\b|\brubles?\b|\broubles?\b|\bsom\b|\bKASE\b|\bMOEX\b|\bTONIA\b|\bMOSPRIME\b|\bRUONIA\b|KazPost|Rosstat|Elcart|\bMir\b',
 'numbered act': r'\b(?:Resolution|Ordinance|Regulation|Instruction|Directive|Law|Form|Decree)\s+(?:No\.?\s*)?\d[\w/.-]*|\bNo\.\s*\d',
 '>=100%': r'≥\s*100\s*%',
 'placeholder / note': r'service\.eyebrow|\bTODO\b|\bTBD\b|complexity is retained|lorem',
 'the bank (lower case)': r'\b[Tt]he bank\b',
 'British spelling': r"\b\w{3,}is(?:e|es|ed|ing|ation|ations|er|ers)\b|\banalys(?:e|ed|ing)\b|\b\w*(?:behaviour|colour|favour|labour|honour)\w*|\bcentres?\b|\bprogrammes?\b|\bjudgement\w*|\bmodell(?:ing|ed)\b|\blabell(?:ing|ed)\b|\bcancell(?:ing|ed)\b|\btravell\w+|\bfulfil\b|\benrol\b|\bcatalogues?\b|\bcheques?\b|\bdefence\b|\boffence\b|\bageing\b|\bwhilst\b|\bamongst\b|\bper cent\b|\bgrey\b|\bpractis(?:e|es|ed|ing)\b|\blicence\w*|\bfulfilment\b|\benrolment\b|\bartefacts?\b|\bsceptic\w*|\bcounsell\w+|\bsignall\w+|\bchannell\w+|\bfuell\w+|\btotall(?:ing|ed)\b|\bskilful\b|\bdialogue\b(?=XXX)",
 'bare agent as the AI': r"(?<![Aa]I )(?<![\w-])[Aa]gents?\b(?!-assist| assist| desktop)",
 'range without en dash': r'\b\d+(?:\.\d+)?\s?-\s?\d+(?:\.\d+)?\s?(?:%|percent|hours?|days?|weeks?|months?|minutes?|bps|basis)',
 'markup or entity in text': r'</?[a-z]+[ >]|&amp;|&#\d+;|&nbsp;',
}
SOFT = {
 'foreign regime (drop, or name the subject; at most one "such as …")': r'\bCOREP\b|\bFINREP\b|\bEBA\b|\bDORA\b|SR 11-7|\bMiFID\b|\bPSD2\b|\bGDPR\b|\bSREP\b|\bECB\b|\bSEC\b|\bFDIC\b|\bCCAR\b|Dodd.Frank|\bFed\b|Federal Reserve|\bEU\b|\bUK\b|\bU\.?S\.?\b(?! dollar)',
 'analyses (fine as a plural noun; the verb is analyzes)': r'\banalyses\b',
 'US GAAP term (write accumulated OCI)': r'\bAOCI\b',
 'scale-dependent practice (condition once per card)': r'\bIRB\b|\bAMA\b|\bAT1\b|covered bond|sell-side|private banking|open.banking|earnings call|internal.models',
}
OK_ISE = set('''precise precisely exercise exercises exercised exercising otherwise expertise promise promises promised promising premise premises premised enterprise enterprises franchise franchises franchised franchising rise rises rising arise arises arising raise raises raised raising noise concise advise advises advised advising adviser advisers supervise supervises supervised supervising revise revises revised revising compromise compromises compromised compromising surprise surprises surprised surprising comprise comprises comprised comprising likewise merchandise merchandising disguise disguised devise devises devised devising praise demise appraise appraises appraised appraising appraiser appraisers liaise liaises liaised liaising improvise improvised improvisation advertise advertises advertised advertising advertiser advertisers surmise treatise poise poised bruise cruise paradise apprise apprised reprise televised wise unwise clockwise stepwise pairwise piecewise coursewise noisy noised raiser raisers fundraiser fundraisers riser risers miser cheerleadersX disease diseases diseased increase decrease release lease please tease cease phrase paraphrase purchase erase chase base case cases based basing bases promiser franchiser franchisers franchisee exerciser advised guise disguises expertises concisely precision'''.split())
HUMAN = r'(?:contact-center|call-center|branch|human|live|service|servicing|sales|collections?|field|transfer|settlement|paying|fiscal|tax|escalation|handling|individual|frontline|front-line|onboarding|per|each|by|productive|senior|junior|experienced|new|available|assigned|same|another|next|specialist|tier-\d|care|support|desk|recovery|recoveries|insurance|real-estate|registrar|custody|correspondent|sub|third-party|payment|merchant|cash|banking|bank|retail|mobile|agency) $'
def main():
    for part in sys.argv[1:]:
        view = open(f'{W}/view/{part}.txt').read()
        lines = {m[1]: (m[2], m[3]) for m in re.finditer(r'^(s?\d+)\t([^\t]*)\t(.*)$', view, re.M)}
        ppath = f'{W}/patch/{part}.json'
        if not os.path.exists(ppath): print(part, 'NO PATCH FILE'); continue
        try: patch = json.load(open(ppath))
        except ValueError as e: print(part, 'PATCH IS NOT VALID JSON:', e); continue
        unknown = [k for k in patch if k not in lines]
        hard = soft = 0; out = []
        for key, (role, old) in lines.items():
            new = patch.get(key, old)
            if not isinstance(new, str) or not new.strip(): out.append(f'  {key} [{role}] EMPTY OR NOT A STRING'); hard += 1; continue
            for name, pat in HARD.items():
                for m in re.finditer(pat, new):
                    hit = m.group(0)
                    if name == 'British spelling' and hit.lower() in OK_ISE: continue
                    if name == 'bare agent as the AI':
                        before = new[max(0, m.start() - 22):m.start()]
                        if re.search(HUMAN, before, re.I): continue
                    out.append(f'  {key} [{role}] {name}: …{new[max(0, m.start() - 45):m.end() + 35]}…'); hard += 1
            for name, pat in SOFT.items():
                for m in re.finditer(pat, new):
                    out.append(f'  {key} [{role}] review — {name}: …{new[max(0, m.start() - 45):m.end() + 35]}…'); soft += 1
            if key in patch and len(old) > 80 and not role.startswith('okr') and not (0.65 <= len(new) / len(old) <= 1.4):
                out.append(f'  {key} [{role}] length changed {len(old)} → {len(new)} characters'); soft += 1
        print(f'{part}: lines {len(lines)} | patched {len(patch)} | unknown keys {len(unknown)} {unknown[:8]} | must fix {hard} | to review {soft}')
        print('\n'.join(out))
        rpath = f'{W}/report/{part}.json'
        if not os.path.exists(rpath): print('  NO REPORT FILE'); continue
        try:
            rep = json.load(open(rpath)); want = {e['id'] for e in json.load(open(f'{W}/fix/{part}.json'))}
            miss = sorted(want - set(rep.get('fixes', {})))
            if miss: print('  report lacks fix ids:', miss)
        except ValueError as e: print('  REPORT IS NOT VALID JSON:', e)
main()
