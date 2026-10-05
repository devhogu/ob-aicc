# A1 core: Charter, Statement of Intent, Operating Model, Vocabulary, Document Catalog, executive summary, README

## charter/en/documents/aicc-charter.md

- ENGLISH-CHANGE 3.1: "AICC reports to the Executive Sponsor, and through the Executive Sponsor to the Board Committee." → "AICC reports to the Executive Sponsor. Through the Executive Sponsor, the Board Committee is informed of the matters that the Executive Sponsor brings to it and of the escalations of 7.2." (R1–R3)
- ENGLISH-CHANGE 5.4: "The Board Committee notes it in its report. A risk beyond it may be accepted only by the Executive Sponsor, with a report to the Board Committee." → "The Board Committee notes it and each change to it. A risk beyond it may be accepted only by the Executive Sponsor, who shall tell the Board Committee of it as 7.2 states." (R3; "its report" was ambiguous and implied a periodic report)
- ENGLISH-CHANGE 7.2: "goes to the next quarterly Steering. The Executive Sponsor approves the Quarterly Report and issues it to the Board Committee each quarter as the report to the Board Committee. … without waiting for the next report." → Quarterly Report goes to the Executive Sponsor at the next quarterly Steering, where the AI Steering Committee advises; the Executive Sponsor approves it; the Executive Sponsor may bring the Quarterly Report, findings, the AI adoption strategy and a bank-level Proposal to the Board Committee or the Board when judged useful or the Board asks, "this is not a periodic duty"; the Executive Sponsor shall tell the Board Committee of a major AI Incident and each risk beyond the appetite "without waiting for any report". (R1–R3)

## charter/en/documents/statement-of-intent.md

- ENGLISH-CHANGE 12.2: "to the AI Steering Committee each quarter, and to the Board Committee each quarter." → "to the Executive Sponsor each quarter, at the quarterly Steering, where the AI Steering Committee advises. The Executive Sponsor may bring them to the Board Committee." (R6; REPORT.md §4 conflict fixed)
- ENGLISH-CHANGE 6.1: "The Board oversees AI through regular reporting." → "The Board oversees AI through the Board Committee (7.6)." "Regular reporting" implied a periodic report to the Board, contrary to R2; R4 wording used.

## charter/en/documents/operating-model.md

- ENGLISH-CHANGE Roles table, Executive Sponsor: "approves and issues the report to the Board Committee" → "approves the Quarterly Report and decides whether to bring it to the Board Committee or the Board; tells the Board Committee of the escalations of Charter 7.2".
- ENGLISH-CHANGE 4.5: "and receives the report of the Executive Sponsor" → "It receives what the Executive Sponsor brings to it and the escalations of Charter 7.2."
- ENGLISH-CHANGE 5.4: "with a report to the Board Committee" → "who shall tell the Board Committee of it without waiting for any report (Charter 7.2)".
- ENGLISH-CHANGE 6.6: act now "approves the Quarterly Report that the AICC Lead prepares, and decides whether the Executive Sponsor brings it to the Board Committee or the Board (Charter 7.2)"; the loop returns the Quarterly Report to the direction loop; "The Quarterly Report reaches the Board Committee or the Board when the Executive Sponsor brings it there, and a risk accepted beyond the appetite always reaches the Board Committee."
- ENGLISH-CHANGE Figure 3 label: "To above<br/>report to the Board Committee" → "To above<br/>Quarterly Report where the Executive Sponsor brings it; escalations to the Board Committee" (node and edge unchanged).
- ENGLISH-CHANGE practice note after Figure 3: "accepted only with a report to the Board Committee" → "accepted only by the Executive Sponsor, who tells the Board Committee of it without waiting for any report".
- ENGLISH-CHANGE 6.10: "from the Teams to the AICC Lead, to the Steering, and to the Board Committee" → "from the Teams to the AICC Lead and to the Steering, where the Executive Sponsor receives it. It reaches the Board Committee or the Board when the Executive Sponsor brings a matter there, and always for the escalations of Charter 7.2." (R4)
- ENGLISH-CHANGE 6.11 table, Risks accepted beyond appetite, target rule: "None without a report to the Board Committee (5.4)" → "Each told to the Board Committee (5.4)".
- ENGLISH-CHANGE 7.3 (REPORT §4): "at the close of each Iteration, which the monthly Steering leaves," → "which closes with the monthly Steering,". Meaning taken from the Steering Summary template ("Registry Snapshot left: … the Iteration … that closes with this Steering").
- ENGLISH-CHANGE 7.4 (REPORT §4): "It is promoted to the corporate share, where the AICC portal links to its records." → "The main branch of the Registry is published to the corporate share, where the AICC portal links to its records." Subject taken from collaboration tooling ("Registry on the corporate share") and Vocabulary "Corporate share".
- ENGLISH-CHANGE C-07 (R5): Control "Approval of the Quarterly Report, and its submission to the Board Committee or the Board where the Executive Sponsor decides"; Owner "AICC Lead prepares; Executive Sponsor approves and decides on submission"; When "Quarterly"; Evidence "Quarterly Report with its approval block and, where made, the submission".
- ENGLISH-CHANGE C-16 When: "without waiting for the next report" → "without waiting for any report".
- ENGLISH-CHANGE C-27 Evidence: "Decision Record; the report to the Board Committee" → "Decision Record; Decision Log entry of the notice to the Board Committee" (same evidence form as C-16).
- QUESTION C-07 evidence says "approval block"; the Quarterly Report template (other batch) must name its block the same way, otherwise the control points to a block that does not exist.

## charter/en/documents/vocabulary.md

- ENGLISH-CHANGE Quarterly Report: "which goes to the quarterly Steering and is drafted …" → "which goes to the Executive Sponsor at the quarterly Steering and is drafted … . The Executive Sponsor approves it and may bring it to the Board Committee or the Board".
- ENGLISH-CHANGE Report to the Board Committee: "The Quarterly Report as the Executive Sponsor approves and issues it to the Board Committee" → "A report, usually the Quarterly Report, that the Executive Sponsor decides to submit to the Board Committee or the Board" (R5).

## charter/en/documents/document-catalog.md

- ENGLISH-CHANGE 5.3 (REPORT §4): "They state no rule of their own" → "The workflows, the guides, and the Templates state no rule of their own". The old Russian already read it this way.

## charter/en/executive-summary.md

- ENGLISH-CHANGE §6: "The Executive Sponsor reports each quarter to the Board Committee." → "AICC reports to the Executive Sponsor. The Executive Sponsor may bring the Quarterly Report, findings, and Proposals at the scale of the Bank to the Board Committee or the Board, and tells the Board Committee of a major AI Incident and of a risk accepted beyond the appetite without waiting for any report."

## charter/en/README.md

- Not changed. Rows 5.12 ("The quarterly report and the report to the Board Committee") and the Executive Sponsor / Board Committee reading route stay true under the R5 definition. The Russian README got term updates only, and its source_sha256 did not change.

## Russian counterparts (all seven)

- source_sha256 refreshed for aicc-charter, statement-of-intent, operating-model, vocabulary, document-catalog, executive-summary; the changed sentences were rewritten to match the new English.
- Applied the revised terms in all seven: «инициатива» (incl. «паспорт инициативы», «постоянная инициатива», «структура инициатив», «лимит инициатив в работе»), «задача» for Work Item, «workflow»/«workflows» for the AICC workflows (part heading and README structure «Workflows»), «value stream» with the explanation at its first use (Document Catalog table 5.1, README row 2.5; in Vocabulary the definition row itself explains it).
- DRIFT ru Operating Model 7.3: old «по итогам ежемесячного управляющего совещания» (snapshot taken after the Steering) did not match the unclear English; now both say the Iteration closes with the monthly Steering.
- DRIFT ru Operating Model 7.4: old «Реестр размещается…» already guessed the subject. Now it says the main branch of the Registry is published, matching the new English.
- QUESTION Vocabulary 3.3 (ru only): this clause listed Initiative among the Latin work-item names. I removed it and named only Capability, Feature, Story, Task, Spike, Bug and Epic, and I added one sentence: «Латинские термины workflow и value stream пишутся со строчной буквы и не склоняются.» Remove the sentence if the Russian style clauses must not go beyond the English.
- QUESTION Vocabulary «Пакет», interpretation: "distinct from a work item's state" is a generic item state, not the Work Item term. I wrote «отличный от состояния элемента», not «состояния задачи».
- QUESTION Vocabulary «Задача»: the definition reads «Работа команды в составе Feature», because «Задача команды» would define the term with itself. Readers may confuse «задача» with the Jira type «Task», which stays Latin.
- QUESTION Document Catalog 5.1 and README 2.5: the English says "the flow of value", but the old Russian «поток создания ценности» was replaced by «value stream» as instructed. If the Solution Lifecycle Model §3 heading keeps «Поток создания ценности», these two cells should follow it.
- QUESTION scan: `check_one.py` passes, but scan.py still flags «паспорт инициативы», «постоянная инициатива» and «лимит инициатив» as rejected forms. These come from translation-en-ru-map.md row 201, which predates the 5 October decision. The map needs updating (not in my files).
