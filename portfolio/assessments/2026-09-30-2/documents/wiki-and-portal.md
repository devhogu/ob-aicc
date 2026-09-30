# Document assessment report: Wiki pages and published portal copy

## 1. Header

| Field | Entry |
| --- | --- |
| Document | Wiki pages and published portal copy, wiki/ ; portal/content/ ; html/aicc/ (n/a) |
| Assessment | 2026-09-30, second Assessment (folder 2026-09-30-2) |
| Assessor | Independent assessor, not the author; the Delivery Lead Role has no Holder |
| Author | AICC Lead (owner of every document, Document Catalog 1.2) |
| Readiness Level | R3 (formal: see the corpus report, section 3) |
| Previous Readiness Level | not assessed at a level |

## 2. Scores

Scores follow Corpus Assessment 7.1 from the failed items; severities are those of 6.2.

| Criterion | Score (0 to 3) | Failed items | Evidence |
| --- | --- | --- | --- |
| D-1 Intent fit | 3 | none | none |
| D-2 Structure fit | 3 | none | none |
| D-3 Completeness | 3 | none | none |
| D-4 Vocabulary and style | 3 | D-4.5 | D-4.5 (Minor): "organisational" in wiki/README.md (British spelling). |
| D-5 Internal consistency | 3 | none | none |
| D-6 Cross-document consistency | 3 | none | none |
| D-7 Traceability | 3 | D-7.3 | D-7.3 (Minor): Seven documents have no lineage page (F-026). |
| D-8 Operability | 3 | D-8.5 | D-8.5 (Minor): Nothing checks the wiki against the charter; the stale pages show that none is run (F-020, F-067). |
| D-9 Proportionality | 3 | D-9.4 | D-9.4 (Minor): Research volume of about 3,600 lines, of which about 2,200 are function pages, for a corpus of 25 documents. |
| D-10 Currency and governance | 2 | D-10.3, D-10.4, D-10.5 | D-10.3 (Major): Superseded material remains: open-decisions.md, overview.md, scaffolding-basis.md "Document classes", README "approved" (F-020, F-067).; D-10.4 (Major): The published Statement of Intent (html/aicc, portal/content) is not the charter text (F-004).; D-10.5 (Minor): Open items pages are out of date: no item 2, decided items left open, old counts (F-067). |

## 3. Strengths

- Lineage pages exist for the Statement of Intent, the Operating Model, the responsible AI alignment, and the scaffolding of Forums, decisions, Records, and Templates (scaffolding-basis.md is new and current for those).
- The wiki states that it is explanatory only and that approved material is in the charter folder.
- The portal builds idempotently and has a check script (portal/tools/check.py).

## 4. Findings

| Finding | Category | Severity | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- |
| F-004 (continues) | drift | Major | The published page (portal/content/statement-of-intent.json; html/aicc/en and html/aicc/ru statement-of-intent) is still the v0.1 text imported at wiki revision add2031: title "AICC Statement of Intent", six principles, four commitments, first person ("We move the bank"), no Maturity Roadmap, no governance section. The charter text is revision 0.6 with thirteen sections and seven Strategic Priorities. The JSON records a source path (wiki/statement-of-intent.md) that no longer exists. The Russian page shows the English text with a notice. | Regenerate the page from the charter text once the Statement of Intent is activated. Until then replace the page by a notice that the Statement is in draft, or remove it. Add the comparison to the quarterly mechanical run. | AICC Lead | 5 |
| F-020 (continues) | legacy | Major | wiki/open-decisions.md lists stack, tooling, and deployment choices that have been taken (static generator build.py, check.py, the deployment repository, and aicc-deploy). wiki/overview.md describes the portal only and points to .grace files. Neither page was refreshed. wiki/README.md describes open-decisions as "choices still to be made by the first spec", and refers to "approved organisational documents" (legacy word, British spelling). wiki/charter-completeness-audit.md is superseded and kept "only so that earlier links resolve". | Archive the two pages or bring them to the present state; correct the README text. | AICC Lead | 1 |
| F-026 (continues) | gap | Minor | The wiki page research/operating-model/scaffolding-basis.md now records the basis of the Forums, Decision Management, Portfolio Management, Service Catalog, and Registers. No wiki page records the basis of the Vocabulary and Style, Corpus Assessment, Register of Appointments, Document Catalog (the one row on "Document classes" is superseded), Reporting, Data Classification Policy, or the allocation of the Decision Rights. wiki/decision-rights-open-items.md holds open questions only. | Add one short lineage page for the listed documents, or record that a document has none by design. | AICC Lead | 1 |
| F-030 (continues) | gap | Minor | No Russian version of any document exists. The portal is Russian-first and its Russian page shows English text. The Catalog states the rule (2.4, source field) and no translation exists to test it. | Produce the Russian text of the Statement of Intent after its activation, with the source field. | AICC Lead | 5 |
| F-067 (new) | drift | Minor | Lineage and open items pages carry superseded facts. agile-mapping.md says the Operating Model has 3 work levels, 4 cadences, 31 RACI rows, and ten principles (now 4 levels, 6 cadences in 14.1 to 14.6, 43 rows, 7 principles); decision-rights-open-items.md says "35 activities", "first draft", and lists the recording rule as open (decided in Decision Management 3.1); operating-model-open-items.md has no item 2, lists the rules that the charter now states (items 23, 24) as open, and its "Decided" list repeats the old counts; scaffolding-basis.md has a row on "Document classes". No check compares the wiki with the charter. | Bring the counts to the charter or delete the counts from the wiki; remove decided items. | AICC Lead | 1 |
| F-073 (new) | overcomplexity | Minor | The detail exceeds the risk that it controls while the portfolio holds no item: five blocks by Entity, Domain, and regime in the Register of Appointments; a 16-field Decision Record and four-step escalation; 13 identifier families and fifteen folders; a requirements matrix of 11 rows by four Risk Tiers; an excluded-terms column for 75 terms; 81 checklist items; about 3,600 lines of wiki research for 25 documents. | Keep the core (one Decision Record form of nine fields, three identifier families, two Risk Tier checks) and mark the rest dormant until a first Use Case passes the Stage concerned. | AICC Lead | 4 |

## 5. Recommendations

1. (Wave 1, P2) Archive the two pages or bring them to the present state; correct the README text. Closes F-020; raises D-4.5, D-10.3, D-10.5.
2. (Wave 1, P3) Add one short lineage page for the listed documents, or record that a document has none by design. Closes F-026; raises D-7.3.
3. (Wave 1, P3) Bring the counts to the charter or delete the counts from the wiki; remove decided items. Closes F-067; raises D-8.5, D-10.3, D-10.5.
4. (Wave 4, P3) Keep the core (one Decision Record form of nine fields, three identifier families, two Risk Tier checks) and mark the rest dormant until a first Use Case passes the Stage concerned. Closes F-073; raises D-9.4.
5. (Wave 5, P2) Regenerate the page from the charter text once the Statement of Intent is activated. Until then replace the page by a notice that the Statement is in draft, or remove it. Add the comparison to the quarterly mechanical run. Closes F-004; raises D-10.4.
6. (Wave 5, P3) Produce the Russian text of the Statement of Intent after its activation, with the source field. Closes F-030; raises corpus criteria.

## 6. Result

The group reaches R3 on the scores (7.3): D-1 to D-5 score 3, D-6 to D-10 score at least 2, and no Blocker finding is open. It has no activation. It is not accepted under 9.1 because Major findings are open (F-004, F-020).
