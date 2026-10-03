# DR-2026-062 Revision 2.0 of the documents: the corpus aligned with the intent of the AICC portal

| Field | Entry |
| --- | --- |
| Identifier | DR-2026-062 |
| Title | Revision 2.0 of the documents: the corpus aligned with the intent of the AICC portal |
| Date | 2026-10-03 |
| Type | Decision of the AICC Lead (activation of documents, Document Catalog 4) |
| Level | AICC Lead |
| Decided by | AICC Lead (Timur Alimbayev) |
| Status | Decided |

## 1. Facts

- The AICC portal, published from the charter, explained the charter with a service model, two modes of work, Packages, the service steps and the Lab, measures with definitions and target rules, governance measures, and the portal as a tool, which the documents at revision 1.0 did not carry.
- The documents are revised to carry them in their own wording, so that the AICC portal states nothing that the documents do not ground.
- Each change alters the meaning of an active document, so each takes the next whole revision (Document Catalog 4.2).
- The revision does not change the AI Risk Appetite Statement, so no decision of the Executive Sponsor is needed for it (Document Catalog 4.1).

## 2. Options

1. Leave the documents at revision 1.0 and correct the AICC portal.
2. Revise the documents to carry the intent of the AICC portal, and correct the AICC portal where it departed from them by error.

## 3. Decision

The AICC Lead takes the second option, and decides the following.

1. The Business Model, the AICC Charter, the Solution Lifecycle Model, the Portfolio Management Model, the Operating Model, the AI Policy, the Vocabulary and Style, and the Document Catalog are activated at revision 2.0.
2. The Templates changed are activated at revision 1.1: the Service Agreement, the Initiative Brief, the Outcome Report, the Solution Definition, the Acceptance Checklist, the AI Incident Review, the Steering Summary, the Quarterly Report, and the Appointments Record.
3. The Package Definition AICC-TPL-14 is activated at revision 1.0.
4. The Statement of Intent on the Adoption of Artificial Intelligence stays at revision 1.0.
5. The check with the ten questions of the Document Catalog 7.1 is recorded for each document below.

## 4. Conflicts and advice

The AICC Lead revises and activates the documents. This is an accepted limit (Business Model 7.5, Solution Lifecycle Model 7.3(d)). The Executive Sponsor and those concerned are told of the activation (Document Catalog 4.2).

## 5. Where it was decided

This Record; the Decision Log; the rows of revision 2.0 in the change logs of the eight documents.

## 6. Review

| Field | Entry |
| --- | --- |
| Funding reference | None |
| Revisit | 2026-12-07 to 2026-12-11 (the yearly Steering of December 2026) |
| Supersedes | None |

## For an activation of a document

The ten questions of the Document Catalog 7.1, with the result of each, for each document activated and for the Templates. BM is the Business Model, CH the AICC Charter, SLM the Solution Lifecycle Model, PMM the Portfolio Management Model, OM the Operating Model, AIP the AI Policy, VOC the Vocabulary and Style, DC the Document Catalog, and TPL the Templates changed and the Package Definition.

| Number | Question | BM | CH | SLM | PMM | OM | AIP | VOC | DC | TPL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Does the document have its metadata block, and does its change log end on its revision? | Met | Met | Met | Met | Met | Met | Met | Met | Met |
| 2 | Does it use the defined terms, and none of the terms that the Vocabulary marks as not used? | Met | Met | Met | Met | Met | Met | Met | Met | Met |
| 3 | Are its clauses numbered, with "shall" for each obligation? | Met | Met | Met | Met | Met | Met | Met | Met | Met |
| 4 | Does it agree with every document that is higher in precedence? | Met | Met | Met | Met | Met | Met | Met | Met | Met |
| 5 | Is every Role, Record, and Template that it names defined? | Met | Met | Met | Met | Met | Met | Met | Met | Met |
| 6 | Does each requirement have one Role that must meet it? | Met | Met | Met | Met | Met | Met | Met | Met | Met |
| 7 | Is it free of open questions, provenance, and references to files, except in its change log? | Met | Met | Met | Met | Met | Met | Met | Met | Met |
| 8 | Does every table other than a change log have an introducing clause, and does every link work? | Met | Met | Met | Met | Met | Met | Met | Met | Met |
| 9 | Is it within the size limit, and does it say nothing that another document says? | Met | Met | Met | Met | Met | Met | Met | Met | Met |
| 10 | Can a person do what it asks today, with the people and the tools that exist? | Met, once the Standing Initiatives are entered | Met | Met | Met, once the Standing Initiatives are entered | Met, except where the Control Function Contacts are not named (RI-005) | Met, except where the Control Function Contacts are not named (RI-005) | Met | Met | Met |

The residuals of question 10 are the ones of the baseline, and the four Standing Initiatives of the Business Model 4.9, whose Initiative Briefs the Executive Sponsor approves and the AICC Lead enters in the Portfolio Backlog. The Document Catalog 7.2 states that a missing Appointment does not block an activation.

## Dated confirmation and correction: 2026-10-03

This entry supplements DR-2026-062 under Operating Model 7.4; the original entry above is retained.

The AICC Lead confirmed reconciliation as the new baseline aligned with the site and instructed it to proceed on 2026-10-03. The instruction is recorded in the AICC-Claude project thread `thr_87vctwz64d`: “reconsile as new baseline and alingment with the site, go”. The activation status is therefore Decided; the earlier handoff request for confirmation is no longer outstanding. The published revision 2.0 baseline is identified by tag `baseline-2026-10-03-rev2`.

The subsequent instruction to fix the defects and reconcile the English version authorizes the corrections recorded in the revision 2.1 change-log rows of the Business Model, the Portfolio Management Model, the Solution Lifecycle Model, and the Vocabulary. These corrections complete the existing run-rate route, correct the units and population of expected lead time, and align the defined terms. They add no approval of a Solution, provider, data class, or Standing Initiative. The other document and template revisions activated above are unchanged.

The current source edition of the English portal is 2.1. It identifies a set of sources, not a common revision for every document. Each document and template retains its own revision and status. The exact English source files are identified in `portal/translation-source.json`.

The following findings qualify the original check and record the reconciliation:

| Finding | Correction or current position |
| --- | --- |
| Expected lead time mixed throughput per Iteration with a result in days and counted different item populations | SLM 10.3 and the portal definition use the same Feature population, observation period, and throughput per calendar day; a zero or unsuitable throughput produces no estimate |
| Run-rate Features lacked an explicit delivery parent and admission path | The models, Vocabulary, workflow, guide, and backlogs identify the Standing Initiative as parent and the Weekly Review as admission, with the existing checks and acceptance retained |
| C-08 was Open although the control had not operated | C-08 and RI-004 are recorded as a Deficiency; C-32 remains Open until its remediation due date is recorded |
| The site edition was presented as the revision of all its documents | Source edition and individual document revisions are distinguished in the footer and provenance |
| Package catalog entries lacked their Package Definitions | Twelve Definitions are linked from the catalog, with concrete source references for available material and explicit gaps for planned or in-preparation material |
| Standing Initiatives were not entered | INI-009 to INI-012 are entered as Proposed, with Initiative Briefs awaiting Executive Sponsor approval, recorded in RI-008 and DEP-015 |

Operational residuals remain: the Standing Initiative approvals and Team limits, the unissued Service Agreements and remediation due date of RI-004, the missing appointments of RI-005, and the unverified applicability of the instruments and Bank policies in RI-006. Reconciliation of the English source does not assert that these actions have been completed.

## Subsequent baseline settlement: 2026-10-03

DR-2026-063 establishes approved English source edition 2.2 and settles the four Standing Initiative approvals, initial measures, and capacity limits. RI-008 is Closed and DEP-015 is Met. The earlier descriptions of these matters above are retained as dated history; DR-2026-063 states their current disposition. The operational records continue to report the actual state of execution.
