"""Check one translated part: python3 /tmp/ru-run/scan.py <part> [...]"""
import json, os, re, sys
W = '/tmp/ru-run'
ALLOW = set('''AI IT ICT API APIs MVP KPI KPIs SLA SLAs CRM ROI SQL ETL ELT PDF SMS HR QA NPS CSAT CLV LTV CAC KYC KYB P&L FP&A M&A ESG CET1 AT1 Tier LCR NSFR HQLA RWA VaR ES PD LGD EAD IRRBB EVE NII ICAAP ILAAP IRB DV01 CS01 MTM FTP RCSA Basel BCBS IFRS ISSB TCFD FATF PCAF NGFS ISO SWIFT NIST CSF CIS MITRE ATT&CK OWASP COREP FINREP XBRL DORA PSD2 GDPR SR EBA EU MiFID CSRD Visa Mastercard Bloomberg Refinitiv MSCI Sustainalytics ISS Telegram Google Play App Store iOS Android Word Excel Capability Feature Story Epic workflow private banking run-rate data science mesh performance due diligence term sheet earn-out RAROC EVA ROE RoE NIM CDE MDM BI NLP RAG OCR CVSS SIEM CERT TLPT RTO RPO BCP UX CX IVR AHT FCR SKU DAU MAU PIN BIN XML PSI KS AUC Gini RMSE GL OPEX CAPEX CASA DPD NPL SME DCF NPV IRR SOFR EURIBOR ECB OECD BIS IMF S&P S1 S2 Scope GRI XBRL MCC TIN CRS FATCA BEPS IAS IFRIC DTA ETR MD&A CECL A/B T+1 SaaS IDB ICE EMMI FIBO DAMA DMBOK STP ACH RTGS ISO20022 CBDC FRTB SIFI CCyB CCB GRC TPRM MRM ERM KRI RCSA PMI BAU NDA SDN OFAC UN CVA DPO CDO CISO COO CTO CSO CCO IR LinkedIn Twitter X Instagram VoC CTR Pillar III IV L1 L2 L3 ML GenAI'''.split())
BAN = {
 'ИИ instead of AI': r'(?<![А-Яа-яЁё])ИИ(?![А-Яа-яЁё])',
 'regulator named': r'НБКР|ЦБ РФ|ЦБР|Банк России|НБК(?![А-Яа-я])|АРРФР|АРДФМ|АФК|AFSA|NBKR|CBR\b|Росфинмониторинг|FinCEN',
 'country or currency': r'Казахстан|Росси[ия]|Кыргыз|КЗ\b|РФ\b|СНГ|тенге|рубл|(?<![а-яёА-ЯЁ-])сом(?![а-яё])|KZT|RUB|KASE|MOEX|ЕАЭС',
 'bare агент at start (write AI-агент)': r'(?:^|[.;:]\s+)[Аа]гент(?:ы|а|у|ом)?\s',
 'ИИ-агент': r'ИИ-агент',
 'Title Case words': r'^(?:[А-ЯЁ][а-яё]+ ){2,}[А-ЯЁ][а-яё]+',
 'English quotes': r'"[^"]+"',
 'decimal point': r'\d\.\d',
 'range with hyphen': r'\d\s?-\s?\d',
 'calque на ... основе': r'на (?:ежемесячной|еженедельной|ежедневной|ежеквартальной|ежегодной|постоянной|регулярной) основе',
 'piece starts with punctuation': r'^\s*[,:;.]',
}
for part in sys.argv[1:]:
    view = open(f'{W}/view/{part}.txt').read()
    keys = {m[1]: (m[2], m[3]) for m in re.finditer(r'^(s?\d+)\t([^\t]*)\t(.*)$', view, re.M)}
    path = f'{W}/patch/{part}.json'
    if not os.path.exists(path):
        print(part, 'NO PATCH'); continue
    try:
        patch = json.load(open(path))
    except ValueError as e:
        print(part, 'INVALID JSON', e); continue
    out = []
    miss = [k for k in keys if k not in patch]
    extra = [k for k in patch if k not in keys]
    for k, (role, en) in keys.items():
        ru = patch.get(k)
        if not isinstance(ru, str) or (not ru.strip() and en.strip()):
            continue
        if en == 'service.eyebrow':
            if ru != 'service.eyebrow': out.append(f'  {k} [{role}] keep service.eyebrow as is')
            continue
        for name, pat in BAN.items():
            if name == 'Title Case words' and role not in ('title', 'l3-section__title', 'page-header__title', 'card__title'):
                continue
            for m in re.finditer(pat, ru):
                out.append(f'  {k} [{role}] {name}: …{ru[max(0, m.start() - 30):m.end() + 30]}…')
        for m in re.finditer(r"[A-Za-z][A-Za-z0-9&/'+-]*", ru):
            w = m.group(0).strip("-'/")
            if w in ALLOW or w.upper() in ALLOW or all(p in ALLOW for p in re.split(r'[/-]', w) if p):
                continue
            out.append(f'  {k} [{role}] Latin word "{w}": …{ru[max(0, m.start() - 30):m.end() + 30]}…')
        if len(en) > 60 and not (0.6 <= len(ru) / len(en) <= 1.8):
            out.append(f'  {k} [{role}] length {len(en)} → {len(ru)}')
    print(f'{part}: keys {len(keys)} | written {len(patch)} | missing {len(miss)} {miss[:6]} | unknown {len(extra)} {extra[:6]} | to check {len(out)}')
    print('\n'.join(out))
