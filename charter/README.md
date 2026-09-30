```yaml
id: AICC-REF-02-EN
title: Document Catalog
status: draft
revision: 2.1
created: 2026-09-30
revised: 2026-09-30
```

# Document Catalog

## 1. Purpose and scope

1.1. This Catalog lists the documents of the documents and states how they are labeled, kept, activated, and checked. It
is the only place for these rules.

1.2. The AICC Lead owns every document. A document is short and is changed like software: in small steps, with the change
logged.

## 2. Labeling

2.1. Each document has the identifier AICC-CAT-nn-LL: the category, a two-digit number, and the language (EN, RU, or KY). A
translation keeps the identifier and changes the language.

2.2. The categories are MND (mandate), ORG (organization and way of working), POL (policy), REF (reference), and TPL (Template).

## 3. Metadata, status, revision, and change log

3.1. Each document shall begin with a block of six fields: id, title, status, revision, created, and revised. It shall end with a
change log: one row for each change, with the revision, the date, the change, and the Decision Log entry or "none".

3.2. The status is draft, active, or deprecated. A draft is being written. An active document is in force. A deprecated
document is kept for history.

3.3. The revision is x.y. It rises by 0.1 at each change and to the next whole number when the meaning of the document changes. A
row may cover several revisions made while the document was a draft.

## 4. Activation

4.1. A document becomes active when the Role that activates it sets the status to active and the next whole revision number,
records the date in the change log, and enters the Decision in the Decision Log. The AICC Lead activates a document that does not
bind persons outside AICC, and does so first for the Vocabulary and Style and this Catalog. The Executive Sponsor activates a
document that does, which are the Statement of Intent, the AICC Charter, the Operating Model, and the AI Policy. The AICC Lead
activates a Template by setting its status and its revised date. The activation of a document binds the Bank. An Entity takes part
by its own recorded decision.

4.2. The first activation of a document needs the checks of section 7. A later change that alters the meaning takes the next whole
revision number and is a new draft revision that does not replace the active text until it is activated, with a Decision Log
entry. A correction that does not change the meaning needs only a change log row. The activator announces to all employees the
activation of a document that binds persons outside AICC.

## 5. The documents

5.1. The following table lists the documents. The status and revision of each are in its own metadata block. EN is the source
language.

| Identifier | Title | Purpose | Languages |
| --- | --- | --- | --- |
| AICC-MND-01 | Statement of Intent on the Adoption of Artificial Intelligence | The intent, values, principles, and strategy of the Group for AI | EN |
| AICC-MND-02 | AICC Charter | Mission, authority, funding, risk appetite, offer, and measures of AICC | EN |
| AICC-ORG-01 | Operating Model | Roles, decisions, flow of work, meetings, and Records | EN |
| AICC-POL-01 | AI Policy | Rules of use, Risk Tiers, providers, AI Incidents, and Exceptions | EN |
| AICC-REF-01 | Vocabulary and Style | Terms and style | EN |
| AICC-REF-02 | Document Catalog | This Catalog | EN |

5.2. A new document is added only when no existing document can hold its content. The documents together number no more than eight, and no document is longer than about 80 clauses. A translation states the revision of the source that it translates.

## 6. Templates

6.1. The following Templates give the form of the Records that need one. A Template has a status and a revision but no change
log, and a copy of it carries no metadata block.

| Template | Used for |
| --- | --- |
| AICC-TPL-01 Use Case Card | Each Use Case, with its Risk Tier and the effect on affected persons |
| AICC-TPL-02 Initiative Brief | Each Initiative above an Investment Guardrail |
| AICC-TPL-03 Control Sign-Off | The validation or the stop of a Control Function Contact |
| AICC-TPL-04 Notes | The Sync and Demo, the Quarterly Review, and the Steering |
| AICC-TPL-05 Quarterly Report | The Quarterly Report |

## 7. Checks

7.1. A document shall be checked before its activation when its meaning changes, and the documents together once a year, by a person
other than the author whom the Executive Sponsor names. The check asks the following ten questions. A failure shall be entered as a Finding in the Risks and Issues Record with a Severity. One line may cover the Findings of one report.

| Number | Question |
| --- | --- |
| 1 | Does the document have its metadata block, and does its change log end on its revision? |
| 2 | Does it use the defined terms, and none of the terms that the Vocabulary marks as not used? |
| 3 | Are its clauses numbered, with "shall" for each obligation? |
| 4 | Does it agree with every document that is higher in precedence? |
| 5 | Is every Role, Record, and Template that it names defined? |
| 6 | Does each requirement have one Role that must meet it? |
| 7 | Is it free of open questions, lineage, and references to files, except in its change log? |
| 8 | Does every table other than a change log have an introducing clause, and does every link work? |
| 9 | Is it within the size limit, and does it say nothing that another document says? |
| 10 | Can a person do what it asks today, with the people and the tools that exist? |

7.2. The documents are ready when every document to be activated has no open Finding of Severity Blocker or Major from the check.
Missing Appointments are tracked in the Risks and Issues Record and do not block activation.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 0.1 to 0.8 | 2026-09-30 | Drafted and revised. | none |
| 1.0 | 2026-09-30 | Rewritten for the simplified corpus of six documents and five Templates; ten checks replace the Corpus Assessment; the Artifact Standards are folded into the Operating Model. | DR-2026-009 |
| 1.1 | 2026-09-30 | Fixes from the independent check: Status and Revision columns removed, TPL category, check cadence and checker, activation announced. | DR-2026-010 |
| 2.0 | 2026-09-30 | Second fixes: activation and announcement; checks apply where required; change logs exempt from the table rule. | DR-2026-011 |
| 2.1 | 2026-09-30 | Acceptance fixes: activation order and revision, Templates, change to an active document, participation of Entities, readiness gate, size limit. | DR-2026-015 |
