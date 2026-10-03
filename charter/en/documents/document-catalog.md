```yaml
id: AICC-REF-02-EN
title: Document Catalog
status: active
revision: 2.1
created: 2026-10-02
revised: 2026-10-03
```

# Document Catalog

## 1. Purpose and scope

1.1. This Catalog lists the documents and states how they are labeled, kept, activated, and checked. It is the only place for these rules.

1.2. The AICC Lead owns every document. A document is short and is changed like software: in small steps, with the change logged.

1.3. The documents and the Records carry definitions of work, scope, methods, and architecture. They carry no figures of the Bank, no documents of the functions, no data, and no code. A figure lives in its source system, and the Record points to it.

## 2. Labeling

2.1. Each document has the identifier AICC-CAT-nn-LL: the category, a two-digit number, and the language (EN, RU, or KY). A translation keeps the identifier and changes the language.

2.2. The categories are MND (mandate), ORG (organization and way of working), POL (policy), REF (reference), and TPL (Template).

## 3. Metadata, status, revision, and change log

3.1. Each document shall begin with a block of six fields: id, title, status, revision, created, and revised. It shall end with a change log: one row for each change, starting at the baseline, with the revision, the date, the change, and the Decision Log entry or "none". The revision of the document is that of the last row.

3.2. The status is draft, active, or deprecated. A draft is being written. An active document is in force. A deprecated document is kept for history.

3.3. The revision is x.y. It rises by 0.1 at each change and to the next whole number when the meaning of the document changes. A row may cover several revisions made while the document was a draft.

## 4. Activation

4.1. The AICC Lead activates every document and Template by setting its status to active, recording the date in the change log (for a Template, in the Decision Log entry, because a Template has no change log), and entering the Decision in the Decision Log. The activation of a document binds the Bank. Where a change concerns the AI Risk Appetite Statement, the Executive Sponsor decides it and the AICC Lead activates the change on that decision.

4.2. A change that alters the meaning of an active document takes the next whole revision number, and is activated in the same way. A correction that does not change the meaning needs only a change log row. The AICC Lead tells those concerned of an activation or a change that affects them.

## 5. The documents

5.1. The following table lists the documents. The status and revision of each are in its own metadata block. The Languages column records the available language versions.

| Identifier | Title | Purpose | Languages |
| --- | --- | --- | --- |
| AICC-MND-01 | Statement of Intent on the Adoption of Artificial Intelligence | The intent, values, principles, and strategy of the Bank for AI | EN |
| AICC-MND-02 | AICC Charter | Mission, authority, funding, risk appetite, offer, and measures of AICC | EN |
| AICC-MND-03 | Business Model | What AICC is, whom it serves, what it offers in its service areas, how it takes in work in its two modes, how it commits, and how it tracks value and flow | EN |
| AICC-ORG-01 | Operating Model | AICC as a unit of the Bank: Roles, Decisions, the five control loops, Records, controls, and the governance measures | EN |
| AICC-ORG-02 | Portfolio Management Model | How AICC decides which business initiatives to take in, fund, continue, defer, or reject: the strategic inputs, the four portfolio loops, the portfolio Kanban, the business case, and the MVP | EN |
| AICC-ORG-03 | Solution Lifecycle Model | How AICC delivers: the principles, the flow of value, the backlogs and the Program Board, the states, the cadence and its loops, verification and release, the life cycle with the service steps and the Lab, and the measures | EN |
| AICC-POL-01 | AI Policy | Rules of use, Risk Tiers, providers, AI Incidents, and Exceptions | EN |
| AICC-REF-01 | Vocabulary and Style | Terms and style | EN |
| AICC-REF-02 | Document Catalog | This Catalog | EN |

5.2. A new document is added only when no existing document can hold its content. The documents together number no more than nine, and no document is longer than about 80 clauses. A translation states the revision of the source that it translates.

5.3. The workflows and the guides of the charter are changed like software, with their history in the repository, and are not activated. A Template is activated as 4.1 states. They state no rule of their own: the rules are in the documents.

5.4. The pages that the AICC portal adds to explain the charter, such as the courses, the learning paths, the knowledge base, the references, and the service catalog, state no rule, and each states its edition. The AICC Lead shall keep them, with the Control Function Contacts of compliance and legal for a page on law, and shall remove a page that no longer serves a reader. A page in another language states the revision of the source that it explains. A page that states the form of a catalog, a Measure, or a Package gives the form only, and each instance is in the Registry or the Portfolio.

## 6. Templates

6.1. The following Templates give the form of the Records that need one. A Template has a status and a revision but no change log, and a copy of it carries no metadata block.

| Order of use | Template | Used for |
| --- | --- | --- |
| 1 | AICC-TPL-02 Initiative Brief | Each Initiative: its lean business case |
| 2 | AICC-TPL-06 Service Agreement | Each Engagement: the commitment and the working agreement |
| 3 | AICC-TPL-01 Solution Definition | Each Solution: its type, Receiver, scope, capabilities, architecture, Risk Tier, and acceptance criteria |
| 4 | AICC-TPL-13 Acceptance Checklist | Each Solution handed to a Domain as ready for use at scale: the signed answers of the Domain, the Control Functions, and the IT function |
| 5 | AICC-TPL-03 Control Sign-Off | The decision of a Control Function Contact: a validation, a clearance of a business case, a stop, a provider check, or an Exception |
| 6 | AICC-TPL-08 Decision Record | A Decision of the Executive Sponsor that is hard to reverse, a Decision that the Operating Model 8 names as evidenced by a Decision Record, such as a Data Sharing Arrangement, an Exception of the AICC Lead, and an approval of output, and the cutover |
| 7 | AICC-TPL-04 Steering Summary | Each Steering, monthly, quarterly, or yearly: attendance, advice, Decisions, and actions |
| 8 | AICC-TPL-07 Outcome Report | The end of each Engagement: what was delivered, the evidence, and the acceptance |
| 9 | AICC-TPL-14 Package Definition | Each Package: its kind, owner, status, what a function needs to re-deploy it, and the Risk Tier of its uses |
| 10 | AICC-TPL-10 AI Incident Review | The review of each AI Incident |
| 11 | AICC-TPL-11 Registry Snapshot | The closed extract of the working state at the close of each Iteration and PI, and at the cutover |
| 12 | AICC-TPL-05 Quarterly Report | The Quarterly Report, and the report to the Board Committee |
| 13 | AICC-TPL-09 Appointments Record | The Roles mapped to people, the appointment log, the declarations, and the access |
| 14 | AICC-TPL-12 Proposal | A Proposal to adopt a Solution at scale, and the yearly Proposal of the AI adoption strategy |

The table is in the order of use, and the identifiers do not follow that order. The index of the Templates carries the same order and the place where each Record is kept.

## 7. Checks

7.1. The AICC Lead checks each document before its activation, and the documents together once a year, in time for the yearly Steering of December, which reviews them (Operating Model 6.5). A second person may also check, when the AICC Lead or the Executive Sponsor asks. The check asks the following ten questions. A failure shall be entered as a Finding in the Risks and Issues Record with a Severity.

| Number | Question |
| --- | --- |
| 1 | Does the document have its metadata block, and does its change log end on its revision? |
| 2 | Does it use the defined terms, and none of the terms that the Vocabulary marks as not used? |
| 3 | Are its clauses numbered, with "shall" for each obligation? |
| 4 | Does it agree with every document that is higher in precedence? |
| 5 | Is every Role, Record, and Template that it names defined? |
| 6 | Does each requirement have one Role that must meet it? |
| 7 | Is it free of open questions, provenance, and references to files, except in its change log? |
| 8 | Does every table other than a change log have an introducing clause, and does every link work? |
| 9 | Is it within the size limit, and does it say nothing that another document says? |
| 10 | Can a person do what it asks today, with the people and the tools that exist? |

7.2. A document is ready to activate when the AICC Lead is satisfied with the answers. Missing Appointments are tracked in the Risks and Issues Record and do not block activation.

7.3. The check of 7.1 is the control C-04 of the Operating Model 8.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 1.0 | 2026-10-02 | Baseline. | DR-2026-060 |
| 2.0 | 2026-10-03 | Added the Package Definition AICC-TPL-14 to the Templates, the rules for the pages that the AICC portal adds to explain the charter, and the service areas, the modes, the governance measures, the service steps, and the Lab to the purposes of the documents. | DR-2026-062 |
| 2.1 | 2026-10-03 | Clarified that the Languages column records availability; removed the fixed source-language designation. | none |
