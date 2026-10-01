```yaml
id: AICC-REF-02-EN
title: Document Catalog
status: active
revision: 2.10
created: 2026-09-30
revised: 2026-10-01
```

# Document Catalog

## 1. Purpose and scope

1.1. This Catalog lists the documents and states how they are labeled, kept, activated, and checked. It
is the only place for these rules.

1.2. The AICC Lead owns every document. A document is short and is changed like software: in small steps, with the change
logged.

1.3. The documents and the Records carry definitions of work, scope, methods, and architecture. They carry no figures of the Bank, no
documents of the functions, no data, and no code. A figure lives in its source system, and the Record points to it.

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

4.1. The AICC Lead activates every document and Template by setting its status to active, recording the date in the change log,
and entering the Decision in the Decision Log. The activation of a document binds the Bank. An Entity takes part by its own
recorded decision.

4.2. A change that alters the meaning of an active document takes the next whole revision number, and is activated in the same
way. A correction that does not change the meaning needs only a change log row. The AICC Lead tells those concerned of an
activation or a change that affects them.

## 5. The documents

5.1. The following table lists the documents. The status and revision of each are in its own metadata block. EN is the source
language.

| Identifier | Title | Purpose | Languages |
| --- | --- | --- | --- |
| AICC-MND-01 | Statement of Intent on the Adoption of Artificial Intelligence | The intent, values, principles, and strategy of the Group for AI | EN |
| AICC-MND-02 | AICC Charter | Mission, authority, funding, risk appetite, offer, and measures of AICC | EN |
| AICC-MND-03 | Business Model | What AICC is, whom it serves, what it offers, how it commits, and how it tracks value and capacity | EN |
| AICC-ORG-01 | Operating Model | Roles, decisions, flow of work, meetings, and Records | EN |
| AICC-POL-01 | AI Policy | Rules of use, Risk Tiers, providers, AI Incidents, and Exceptions | EN |
| AICC-REF-01 | Vocabulary and Style | Terms and style | EN |
| AICC-REF-02 | Document Catalog | This Catalog | EN |

5.2. A new document is added only when no existing document can hold its content. The documents together number no more than eight, and no document is longer than about 80 clauses. A translation states the revision of the source that it translates.

5.3. The workflows, the templates, and the guides of the charter are changed like software, with their history in the repository, and are
not activated. They state no rule of their own: the rules are in the documents.

## 6. Templates

6.1. The following Templates give the form of the Records that need one. A Template has a status and a revision but no change
log, and a copy of it carries no metadata block.

| Order of use | Template | Used for |
| --- | --- | --- |
| 1 | AICC-TPL-02 Initiative Brief | Each Initiative: its business case, as the lean business case of SAFe |
| 2 | AICC-TPL-06 Service Agreement | Each Engagement: the commitment and the working agreement |
| 3 | AICC-TPL-01 Solution Definition | Each Solution: its type, Receiver, scope, capabilities, architecture, Risk Tier, and acceptance criteria |
| 4 | AICC-TPL-03 Control Sign-Off | The decision of a Control Function Contact: a validation, a stop, a provider check, or an Exception |
| 5 | AICC-TPL-08 Decision Record | A Decision at the level of the AICC Lead or above, an activation, a delegation, an approval of output, and the cutover |
| 6 | AICC-TPL-04 Steering Summary | Each Steering, monthly or quarterly: attendance, advice, Decisions, and actions |
| 7 | AICC-TPL-07 Outcome Report | The end of each Engagement: what was delivered, the evidence, the capacity, and the acceptance |
| 8 | AICC-TPL-10 AI Incident Review | The review of each AI Incident |
| 9 | AICC-TPL-11 Registry Snapshot | The closed extract of the working state at the close of each IT and PI, and at the cutover |
| 10 | AICC-TPL-05 Quarterly Report | The Quarterly Report, and the report to the Board Committee |
| 11 | AICC-TPL-09 Assignment Map | The Roles mapped to people, the appointment log, the declarations, and the access |
| 12 | AICC-TPL-12 Proposal | A Proposal to adopt a Solution at scale, and the yearly Proposal of the AI adoption strategy |

The identifiers keep the order of creation, and the table is in the order of use.

## 7. Checks

7.1. The AICC Lead checks each document before its activation, and the documents together once a year. A second person may also
check, when the AICC Lead or the Executive Sponsor asks. The check asks the following ten questions. A failure shall be entered as
a Finding in the Risks and Issues Record with a Severity.

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

7.2. A document is ready to activate when the AICC Lead is satisfied with the answers. Missing Appointments are tracked in the
Risks and Issues Record and do not block activation.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 0.1 to 0.8 | 2026-09-30 | Drafted and revised. | none |
| 1.0 | 2026-09-30 | Rewritten for the simplified corpus of six documents and five Templates; ten checks replace the Corpus Assessment; the Artifact Standards are folded into the Operating Model. | DR-2026-009 |
| 1.1 | 2026-09-30 | Fixes from the independent check: Status and Revision columns removed, TPL category, check cadence and checker, activation announced. | DR-2026-010 |
| 2.0 | 2026-09-30 | Second fixes: activation and announcement; checks apply where required; change logs exempt from the table rule. | DR-2026-011 |
| 2.1 | 2026-09-30 | Acceptance fixes: activation order and revision, Templates, change to an active document, participation of Entities, readiness gate, size limit. | DR-2026-015 |
| 2.2 | 2026-10-01 | Activation by the AICC Lead; the Executive Sponsor and the independent check removed from activation. | DR-2026-018 |
| 2.3 | 2026-10-01 | Notes Template used for the Iteration and Program Increment events. | DR-2026-020 |
| 2.4 | 2026-10-01 | Event names use the short forms IT and IP. | DR-2026-023 |
| 2.5 | 2026-10-01 | Content rule: no bank figures, function documents, data, or code in the documents and Records. | none |
| 2.6 | 2026-10-01 | Solution Definition replaces the Use Case Card. | DR-2026-024 |
| 2.7 | 2026-10-01 | The workflows, templates, and guides are part of the charter and state no rule. | DR-2026-025 |
| 2.8 | 2026-10-01 | The Business Model is added. | DR-2026-026 |
| 2.9 | 2026-10-01 | Service Agreement and Outcome Report Templates; the Initiative Brief for every Initiative. | DR-2026-026 |
| 2.10 | 2026-10-01 | The twelve evidence Templates: Decision Record, Assignment Map, AI Incident Review, Registry Snapshot, Proposal added; Notes became the Steering Summary; listed in the order of use. | DR-2026-029 |
