# Report — 5 October 2026 round

Branch `claude/ru-alignment`. Covers C-BOARD-REPORTING-CLARITY and C-RU-TERMS-AND-RECORDS. The first round is in `C-RU-NATURAL-ALIGNMENT/REPORT.md`.

## 1. Board reporting (English, then Russian)

The rule now reads, in every English source and its Russian counterpart:

- AICC reports to the Executive Sponsor. Operational and tactical reporting (Steerings, measures, the Quarterly Report) goes to the Executive Sponsor at the quarterly Steering, where the AI Steering Committee advises.
- The Executive Sponsor **may** bring the Quarterly Report, findings, the AI adoption strategy and bank-level Proposals to the Board Committee or the Board, when useful or when the Board asks. No periodic submission is required.
- **Mandatory, unchanged:** the Executive Sponsor tells the Board Committee, without waiting for any report, of a major AI Incident and of each risk accepted beyond the AI Risk Appetite Statement; the Board Committee notes the Statement. These are now called notices, to keep them apart from the optional report.
- Control **C-07** keeps its ID: "Approval of the Quarterly Report, and its submission to the Board Committee or the Board where the Executive Sponsor decides". The Quarterly Report template has an approval block with an optional "submitted to" line. The defined term "Report to the Board Committee" now means a report the Executive Sponsor decides to submit.
- Statement of Intent 12.2 no longer conflicts with the Charter; 6.1 no longer implies regular reporting to the Board.

Files: 73 English sources (charter documents, guides, workflows, templates, portal pages, `authored.json`, two Registry records), each with its Russian counterpart.

## 2. English clarity fixes

All items of the first report's section 4 are fixed, among them: Operating Model 7.3 and 7.4, Document Catalog 5.3, Portfolio Management Model 4.3, Solution Lifecycle Model 4.1, 6.6 and Figure 11, engagement guide §7, C-31 ("no active AI Registry entry"), service delivery Figure 1, Appointments Record, Proposal ("the Domain Owners concerned"), Solution Definition §4, "the check or the validation", the sixth Strategic Priority's full title, the standards page intro and every "Industry body of knowledge" link label, "Governance and oversight", and the adoption page's backlog route. The terminology now states that workflow and value stream keep their Latin names in all language versions.

## 3. Revised Russian terms

Applied across the Russian charter, portal, interface text, Registry and Portfolio:

| Term | Russian |
| --- | --- |
| Initiative, Initiative Brief, Standing Initiative, Mix of Initiatives | инициатива, паспорт инициативы, постоянная инициатива, структура инициатив |
| Work Item | задача (the Jira type Task stays «Task») |
| Workflow | workflow (part «Workflows»; indeclinable, masculine) |
| Value stream | value stream, explained at first use in each document |

Translation map is at version 0.4 with these rows; the style sheet is revised.

## 4. Registry and Portfolio (Russian)

All 57 Russian files (42 Registry, 15 Portfolio) compared with English and rewritten; identifiers, dates, decisions, states and fields unchanged. **33 drifts corrected**, among them Feature and Capability translated instead of kept Latin, Inspect and Adapt translated, «надзор» for oversight, a package kit misread as a workflow kit, mixed decision statuses, a Kanban column labelled with a state name, and category and priority names that differed from the corpus.

## 5. Revisit candidates

1. **"The flow of value"** (Solution Lifecycle Model §3, 3.4, Figure 2; Catalog 5.1; README 2.5) is plain English, but Russian now uses «value stream» there too. A plain «поток ценности» would follow the English more literally.
2. **Generic "work items"** in the terminology: «элемент работы», kept apart from the AICC term «задача».
3. **Jira mapping line**: «Feature — карточке Jira (issue), задача — подзадаче (sub-task)», to avoid «задача» meaning two things.
4. **Escalation wording**: the unit governance sequence diagram keeps "without waiting for the next report"; elsewhere it is "without waiting for any report".
5. **Appointments Record**: "the heads" read as the AI Steering Committee members.
6. **Registry**: "Chief Executive Officer" → «председатель Правления Банка»; ISO dates kept in prose because the build compares them with English; "source edition" → «издание источников»; "baseline" → «базовая версия».
7. **Change-log column** "Decision" is now «Управленческое решение» in the portal table header.
8. **Russian Vocabulary 3.3** names how to write workflow and value stream, slightly beyond the English clause.
9. Experiment workflow step 4 keeps «рабочий процесс» where it means an automation being built, not an AICC workflow.

Per-batch notes with alternatives: `C-BOARD-REPORTING-CLARITY/notes/*` (7 drifts, 17 questions), `C-RU-TERMS-AND-RECORDS/notes/*` (33 drifts, 22 questions).

## 6. Verification

Source check (217 English pins, all refreshed where English changed), 22 unit tests, scaffolding check, full build (460 pages, 197 diagrams), repeatable build and site check pass. The first round's `protected-files.sha256` no longer matches, as intended: this round changed English.
