# C2 — portal pages and chrome (portfolio, responsible-ai, reference, knowledge-base, authored.json, messages/ru.json, build.py)

## English changed (R1–R6)

- portfolio/the-loops-and-governance: intro (week's evidence reaches the Executive Sponsor at the yearly Steering; the Executive Sponsor may bring it to the Board Committee or the Board); table row "Portfolio review" Acts cell; Figure 3 node A label (node ID and edges kept); 4.2; 5.1.
- portfolio/roles-and-records: lead; Executive Sponsor row (approves the Quarterly Report and decides whether to bring it); Quarterly Report record row.
- portfolio/measures-and-tracking: "Portfolio review, quarterly" row, last cell.
- portfolio/overview 2.1: "show the Board" → show the Executive Sponsor, who can show it to the Board when useful.
- responsible-ai/how-the-bank-applies-it: 1.2, 6.1, 7.1 (escalations kept mandatory: the Executive Sponsor tells the Board Committee without waiting for any report); rows AICC Lead, Executive Sponsor, Board Committee.
- responsible-ai/what-responsible-ai-means: Accountability row, "reporting to the Board" → to the Executive Sponsor, who may bring it to the Board.
- reference/regulations/nbkr, financial-standard-setters-on-ai, bank-of-russia-on-ai 5.1; reference/industry-body-of-knowledge row "Reports on AI in the financial sector": "the escalations and reporting that the Executive Sponsor brings to the Board Committee".
- knowledge-base/questions-people-ask (incident and risk beyond appetite: escalation kept, "without waiting for any report"); templates-and-forms (Quarterly Report row); learning-paths (Executive Sponsor step 5).
- authored.json "en": about_page block 5 text; strategy_page aspects/11 choice and kept; services_page areas/3 text. routes/1 reader ("The Executive Sponsor and the Board Committee") left: it names readers, not a reporting duty.

## English clarity fixes (REPORT.md §4)

- portfolio/measures-definitions-and-formulas, First-time-right rate: "meet the Verify or the Review" → "pass the check or the validation".
- responsible-ai/opportunities 4.1: sixth priority now "information technology operations and service lifecycle" (Statement of Intent 9.7).
- reference/industry-body-of-knowledge intro: says only linked sources have a page; names the unlinked ones.
- Link label "Industry body of knowledge" → "Standards and frameworks" in the seven regulation pages and portfolio/overview 3.1.
- reference/regulations/iso-iec-ai-standards §6: unlinked item "Governance and oversight" → link "[Governance](../../governance/overview.md)" (Russian matched).
- authored.json: "Governance and oversight" → "Governance" (about_page link label, explore_page parts 0 and 1).
- Outside my files, not changed: delivery/overview 3.1 still links "[Industry body of knowledge]"; services/research-and-exploration, delivery/life-of-a-service and delivery/service-operations name "Industry body of knowledge" in text; services adoption-and-lifecycle page (Portfolio vs Program Backlog) belongs to another area.

## Russian

- Every Russian counterpart of a changed English page realigned and its source_sha256 refreshed (22 pages); all my-area Russian pages pass check_one.py.
- Term sweep in all Russian pages of my areas, authored.json "ru", messages/ru.json, build.py: Initiative → «инициатива» (declined; паспорт инициативы, постоянная инициатива, структура инициатив, лимит инициатив в работе; column/mode header «Инициатива»); AICC workflows → «workflow» (indeclinable; part label «Workflows»); «рабочих элементов» → «задач» (build.py systems table); «потокам создания ценности» → «value stream» with the style-sheet explanation (lean-portfolio-management, its only use in my areas). No remaining «Initiative», «рабочий процесс», «рабочий элемент» or «поток создания ценности» in my files.
- messages/ru.json: companion_workflow «Связанный workflow»; kind_workflow, services/engagement-workflow «Workflow»; grp_workflows «Workflows»; cat_initiative «Инициатива»; set-ai-risk-control «Workflow «Риски и контроль AI»» (matches the corpus title).
- build.py: change-log column 'Decision' → «Управленческое решение» («Решение» alone means Solution). Only text literals changed.
- portfolio/overview 3.1 link label «Отраслевой базе знаний» → «Стандарты и методологии»; DRIFT: the old Russian already used that title in the regulation pages, only the overview lagged.
- DRIFT strategy-and-investment 1.1: «Initiative принимается» was ambiguous; now «инициатива включается в портфель» (English "taken in").
- QUESTION: check_one/scan reports «паспорт инициативы» and «лимит инициатив» as rejected forms (translation-en-ru-map.md §3 still rejects them); the revised STYLE.md of 5 October 2026 requires them, so the map row is stale.

## For T-004 (verification)

- `python3 -m unittest discover -s portal/tests` fails two assertions I may not edit: test_localization line 484 expects tab label «Рабочий процесс» for services/engagement-workflow (now «Workflow», as instructed), and line 407 expects the unit-governance workflow part title «Рабочий процесс «Управление подразделением»…» (now «Workflow …» from the corpus, not from my files). The tests need the new labels.
- check_sources.py currently stops on unrefreshed translation-source.json pins (charter/en/documents/ai-policy.md first); pins are not mine.
