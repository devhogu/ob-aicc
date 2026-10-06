# Brief: Russian edition of the Discovery Catalog

The O!Bank AI Competence Center publishes the Discovery Catalog in English and Russian: 76 pages and 1,110 scenarios in which AI could help a bank. The English edition has just been corrected and reworded, and it is now the source of meaning. The Russian edition was a clumsy, literal translation of the old English text. It named foreign regulators (НБКР, ЦБ РФ, НБК/АРРФР), left English words in sentences, and lacked the new content. You write the Russian text of part of the catalog anew, from the English. Readers are managers of a bank in Kyrgyzstan who read Russian at work. The text must read as if a Russian-speaking banking professional wrote it: formal business register, clear, natural, never a word-for-word rendering.

## Your files

For each part named in your task (for example `risk-control__credit-risk.1`):

- Read `/tmp/ru-run/view/<part>.txt`. Each text line is `key <tab> role <tab> English text`. Where an old Russian rendering exists, the next line is `<tab><tab>(было) old Russian`. Blocks are headed `== page ==`, `== card <urn> ==` and `== stages of <flow> ==`.
- Write `/tmp/ru-run/patch/<part>.json`: one JSON object holding **every key of the part**, `{"<key>": "<Russian text>", …}`. Write plain text: no HTML, no entities.
- Write `/tmp/ru-run/report/<part>.json`: `{"part": "<part>", "notes": ["…"]}`, with only the points that need a person's decision.

Write only these files. Do not edit the repository and do not run git.

## How to write each line

1. **Meaning comes from the English line.** Render all of it and add nothing. The old Russian is only a hint for terms and phrasing. Discard whatever it says that the English does not: regulator names, countries, currencies, acts, assertions. Where the old Russian reads well and matches the English, you may keep it.
2. **Write natural Russian.** Restructure sentences freely; split a long English sentence where Russian reads better. Prefer verbs to chains of nouns («Банк ежемесячно пересчитывает…», not «осуществление ежемесячного пересчёта»). Avoid calques: «на ежемесячной основе» → «ежемесячно»; «в разрезе» only where natural; no «данный» for "this". Keep each line about as long as the English, and keep every figure, target, role and cadence.
3. **Several consecutive lines with the same role form one paragraph** that the page prints with the middle piece in bold or italics, with a space between pieces. Keep the split, and make the pieces read on as one sentence. A piece never starts with a comma, colon or full stop; where English starts the next piece with a dash, start with «— ».
4. **Titles in sentence case**: «Мониторинг окон размещения инструментов первого уровня», not Title Case. Navigation labels (`card-link`, `card__title`, `sub-group__label`, `problems-tab-label`, `flow-item__name`) are short and match the section or page they name.
5. `stage N label` lines are the short names on a diagram (one or two words). `title`, `intent` and `problem` lines of stages are ordinary text.

## Terms

The AICC translation map rules: `/devops/obank/aicc/charter/ru/translation-en-ru-map.md`, sections 3 and 4. Before you write an English term that may be in it, search for it (for example `grep -i "| due diligence" …`). A «не: …» form in a row is an error in the situation that row describes. The settled forms used most often in this catalog:

| English | Russian |
| --- | --- |
| the AI agent, an AI agent | AI-агент (always so; a bare «агент» may follow only within the same sentence) |
| a human agent (contact-center, collections) | оператор контакт-центра; сотрудник по взысканию (never «агент») |
| the Bank (the institution) / a bank, banks | Банк (capital letter) / банк, банки |
| the regulator, the supervisor | регулятор; надзорный орган where the Bank reports, notifies or discloses to it (see the map) |
| the financial intelligence unit | подразделение финансовой разведки |
| local currency | национальная валюта |
| AI, IT, ICT | AI, IT, ICT (Latin; never «ИИ») |
| CFO, CRO, CEO | финансовый директор, директор по рискам, председатель Правления |
| ALCO, ExCo, Steering Committee | комитет по управлению активами и пассивами (КУАП); Правление; управляющий комитет |
| relationship manager (RM), PMO, ATM | клиентский менеджер, проектный офис, банкомат |
| STR, SAR | сообщение о подозрительной операции (сделке) |
| AML/CFT, PEP, CDD, EDD | ПОД/ФТ; публичное должностное лицо (ПДЛ); надлежащая проверка клиента; углублённая проверка клиента |
| IFRS 9, ECL | МСФО (IFRS) 9; ожидаемые кредитные убытки (ОКУ) |
| Tier 1, Tier 2 (capital) | капитал первого уровня, второго уровня (in lists with CET1 and AT1 the abbreviations may stay) |
| governance | by object: система управления и контроля; корпоративное управление; управление данными; управление применением AI |
| sandbox | зона контролируемого тестирования |
| OKR (objective and key results) | критерии приёмки; the three results are «Внедрение», «Принятие», «Цикл» |
| lenses | Аналитика, Автоматизация, Поддержка, Оптимизация, Новые возможности |
| Discovery Catalog | Каталог сценариев для применения AI (short: Каталог сценариев) |
| Regulatory Horizon | Регуляторные требования |
| value streams (page name) | Операционные потоки; Клиентские потоки |
| audit trail | аудиторский след |
| data steward; data lineage; golden record; CDE; master data | ответственный за данные; происхождение данных; золотая запись; критически важные элементы данных (CDE); основные данные (master and reference data: нормативно-справочные данные) |
| core banking system | автоматизированная банковская система (АБС) |
| a capability (one area of the map) | область; блок (never «направление», which the corpus reserves for a Domain of the Bank) |
| contingency funding plan | план экстренного фондирования |
| Pillar 1, 2, 3 (Basel) | Компонент 1, 2, 3; «(Pillar 2)» after the first use on a page |
| Lens (column label) | Аспект |

**Latin script stays only for:** AI, IT, ICT and other protected terms; common abbreviations (API, KPI, SLA, CRM, MVP, ROI, KYC, P&L, FP&A, M&A, ESG, NPS, CSAT); Basel and risk metrics (CET1, AT1, LCR, NSFR, HQLA, RWA, VaR, PD, LGD, EAD, IRRBB, ICAAP, ILAAP); names of international standards and bodies (Basel III, BCBS 239, ISSB, TCFD, FATF, ISO 20022, SWIFT, NIST CSF); and brand names. Every other English word is rendered in Russian. Expand an abbreviation at its first use on a card where the reader may not know it («внутренняя процедура оценки достаточности капитала (ICAAP)»).

**Formatting:** decimal comma («1,5»); thousands with a space («1 110»); ranges with an en dash and no spaces («1–3%», «4–8 часов»); «≥95%», «≤5 рабочих дней»; quotation marks «…»; cadences in words («ежеквартально», «еженедельно»); a deadline in the form the map sets («не позднее пяти рабочих дней с даты …»).

## Check before you finish

After writing the patch of a part, run `python3 /tmp/ru-run/scan.py <part>`. It lists missing keys, leftover English words, banned forms and formatting slips. Fix them, except a Latin word that the list above allows. Rerun until it is clean.

Your final message: the parts done, and any point that needs the owner's decision. Keep it under 120 words.
