# C1: portal pages (T-003)

Scope: portal/content/{en,ru}/about, organization, governance, services, delivery; Russian term sweep also in ru/privacy.md, ru/terms-of-use.md, ru/README.md (README.md had nothing to change).

## English files changed (pins in portal/translation-source.json still need a refresh in T-004)

- about/how-we-work.md: 5.1 follows R1/R2; 6.1 "Governance and oversight" became "The Governance section" (the section label is Governance; REPORT §4).
- organization/the-place-of-aicc-in-the-bank.md: lead, 1.1 (R1, R2, R3, R4), table row "The Board Committee".
- organization/overview.md: Figure 1 labels of B and ES (topology unchanged).
- organization/the-roles.md: Executive Sponsor "Does" cell (approves the Quarterly Report, decides whether to bring it).
- organization/who-does-what.md: Informed cells of the oversight row and the Quarterly Report row.
- governance/controls-and-the-catalogue.md: assurance row restates C-07 under its R5 name.
- governance/decisions-and-escalation.md: 3.1, risk beyond appetite: "who tells the Board Committee without waiting for any report" (replaces "with a report to the Board Committee", which clashed with the new defined term).
- governance/measures-and-reporting.md: rows "AI Incidents" and "Risks accepted beyond appetite"; 3.1 (no quarterly submission required).
- governance/overview.md: lead, 1.1, Figure 1 node B label, 3.1 (industry practice).
- governance/records-evidence-and-assurance.md: Figure 1 node B label, 4.1.
- governance/the-control-loops.md: assurance row, Acts cell.
- governance/the-steerings-and-the-bodies.md: lead, Board Committee row (adds noting the AI Risk Appetite Statement, R3), quarterly row "Leaves", 3.1.
- services/oversight.md: lead, 3.1, 5.1, 8.1.
- services/areas/assurance.md and services/areas/overview.md: the Assurance lead.
- services/adoption-and-lifecycle-management.md: 1.1 and 4.1 aligned with Solution Lifecycle Model 8.1 table and 8.5: a new version of a Product comes through the Portfolio Backlog; a request for a new feature of a Solution in use enters the Program Backlog (REPORT §4).
- delivery/events-and-rituals.md: 2.1, the Executive Sponsor "may bring it to the Board Committee or the Board".
- delivery/measures-definitions-and-formulas.md: rows "First-time-right rate" and "Items returned by reason": "the Verify or the Review" became "the test in Verify or the acceptance at the Iteration Review", matching the formula column (REPORT §4). The same wording is in Solution Lifecycle Model 9 (lines 585-586), owned by T-001.

Every matching Russian page was realigned and given the new source_sha256. check_one.py reports OK for every Russian file in scope (README.md FAIL is expected: no English counterpart).

## REPORT §4 portal items outside this batch

- The "opportunities" page (responsible-ai/) and the industry body of knowledge page (reference/) are outside my areas. I did not change them.

## Russian term sweep (all Russian pages in scope)

- Initiative/Initiatives → инициатива in the right case (паспорт инициативы, «Паспорт инициативы», постоянная инициатива, структура инициатив, лимит инициатив в работе); about 100 places in 38 files. Table cells and clause starts are capitalised (Инициатива).
- Work Item: «рабочий элемент» → «задача» (organization/how-the-organization-grows, governance/decisions-and-escalation incl. figure, services/catalog-form, delivery/events-and-rituals, measures-and-tracking, the-cadence, backlogs-boards-and-kanbans, the-flow-of-value). In the-flow-of-value 1.1 the Jira mapping now reads «Feature — отдельному типу элемента Jira, а задача — подзадаче», so that «задача» does not appear twice with two meanings.
- AICC workflows: «рабочий процесс/рабочие процессы» → «workflow/workflows» in the rule sources and running text (governance, services, delivery, privacy, terms-of-use). The page title «Рабочий процесс эксперимента» became «Workflow эксперимента», and the references to it in delivery/overview and life-cycle-management changed with it.
- delivery/the-flow-of-value.md: the title «Поток создания ценности» (rejected by the map) became «Value stream», as Solution Lifecycle Model 3 does in Russian. The term is explained at its first use in the lead.

## Notes

- QUESTION delivery/experiment-workflow.md step 4: «Рабочий процесс или AI-агент создаётся» kept. Here the English "workflow" means an automated workflow being built, not an AICC workflow.
- QUESTION organization/who-does-what.md, oversight row, Informed: "Board Committee, of a major AI Incident". The Organization guide matrix (T-002) may choose other words. Align it if they differ.
- QUESTION navigation labels in portal/messages/ru.json still read «Рабочий процесс», «Рабочие процессы» (companion_workflow, kind_workflow, grp_workflows, services/engagement-workflow), and authored.json intros say «рабочий процесс». They are outside my edit scope.
- ENGLISH? charter/en/documents/solution-lifecycle-model.md 9 still says "the Verify or the Review". The portal now says it in plain words.
- During this run, check_sources.py and the unit tests failed only on other workers' in-progress files (ai-policy pin; charter/ru/templates/solution-definition.md hash). No file in this batch failed.
