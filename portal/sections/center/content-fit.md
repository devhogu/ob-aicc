# Content fit: the scaffolding against the charter

An evaluation of the scaffold against the content that it has to carry. It measures the content, states where the scaffold fits and where it does not, and proposes a placement of every part of the charter. The proposal was adopted, and the scaffold was rebuilt on it. This page keeps the reasoning.

## 1. The content profile

The charter holds about 90,000 words. Its size is uneven, and the unevenness decides how the pages should be cut.

| Item | Words | Sections | Largest section |
| --- | --- | --- | --- |
| Solution Lifecycle Model | 9,831 | 10 | 8 Life-cycle management, 1,805 |
| Operating Model | 7,133 | 8 | 6 The control loops, 1,999 |
| Vocabulary | 4,674 | 4 | 4 Defined terms, 4,363 (a table) |
| Portfolio Management Model | 4,376 | 9 | 4 The portfolio loops, 1,309 |
| Statement of Intent | 3,217 | 13 | 11 Maturity Roadmap, 855 |
| AI Policy | 2,155 | 6 | 3 Risk Tiers, 911 |
| Document Catalog | 1,519 | 7 | none above 500 |
| Business Model | 1,381 | 7 | none above 400 |
| AICC Charter | 900 | 7 | none above 200 |
| Workflows (6) | 697 to 3,399 each | n/a | Service delivery, 3,399 |
| Guides (5) | 1,459 to 3,199 each | n/a | Organization, 3,199 |
| Templates (13) | 200 to 893 each | n/a | Solution Definition, 893 |

The reading evidence recommends keeping a page to a length that a reader can take in, and splitting very long pages (NN/g; the Material for MkDocs guidance). The working range for this site is 600 to 1,800 words a page. Six items exceed it by a wide margin.

## 2. Where the scaffold fits

| Content | Placement in the scaffold | Verdict |
| --- | --- | --- |
| Statement of Intent, AICC Charter | About AICC | Fits |
| Business Model | What AICC does | Fits, but alone in its section |
| AI Policy and the AI risk and control workflow | Responsible AI | Fits |
| Unit governance workflow | Governance and oversight | Fits |
| The 13 templates | Library | Fits |
| Vocabulary, Document Catalog, change history, Records and systems | Reference | Fits |
| Reading routes | Home and the charter in outline | Fits |

## 3. Where the scaffold does not fit

1. **Long documents as single pages.** The Solution Lifecycle Model is 9,831 words on one page, and the Operating Model is 7,133. A reader cannot take in a page of that length, and the outline becomes the navigation. The sections are 1,000 to 2,000 words, which is the right size for a page.
2. **The Operating Model serves three sections, and one page with anchors is awkward.** Its Roles and Decisions belong to Organization, its control loops, records, and controls belong to Governance and oversight, and its first three sections describe AICC in brief. Anchors on a single 7,000-word page are a poor way to share a document among sections.
3. **What AICC does has one page.** A section with a single page is thin. The Engagement workflow and the Engagement guide describe how a function engages AICC, which is the offer made concrete, and they sit in How AICC works.
4. **The guides are separated from their subjects.** Each guide explains one workflow or one area: the Engagement guide explains the engagement, the Service delivery guide explains the stream, the Cadence guide explains the cadence, the Unit governance guide explains the controls, and the Organization guide explains the Roles. In the Library a reader must leave the subject to read the guide.
5. **The strategy and the roadmap are buried.** The portal exists to present the strategy, the statement of intent, the roadmap, and the knowledge base (the requirements of the portal). Strategic Priorities (549 words) and the Maturity Roadmap (855 words) are sections 9 and 11 of a 3,217-word document, and the home page has no way to feature them.
6. **"What AICC is" is stated four times** (Statement of Intent 2, AICC Charter 2, Business Model 2, Operating Model 2), and the scaffold names no lead statement.
7. **Responsible AI lacks two of its parts.** The AI Risk Appetite Statement is AICC Charter 5, and the gates before use are Solution Lifecycle Model 7. Both belong to a reader who studies how AICC uses AI.
8. **Measures and records of the method are placed with the method.** Solution Lifecycle Model 9 (records and controls) and 10 (measures) are about assurance and performance, and they belong with Governance and oversight.

## 4. Proposed rule for documents

A document with more than 3,000 words is presented as a landing page and one page for each group of its top-level sections. The groups are made so that a page holds 600 to 1,800 words, short sections are grouped, and no section is divided. Every section belongs to exactly one page, and the clause numbers and the permanent links do not change. The sitemap assigns each page to a site section, so that one document can serve more than one section without a second copy. A document with 3,000 words or fewer stays on one page.

The canonical-page rule of the scaffold then reads: every document section, and every workflow, guide, and template, has exactly one canonical page.

## 5. Proposed placement of the long documents

**Statement of Intent** (four pages, in About AICC)

| Page | Sections | Words |
| --- | --- | --- |
| Intent and strategy | 1 to 8: purpose, summary, alignment, values, principles, governance, areas of application | 1,319 |
| Strategic Priorities | 9 | 549 |
| Capability and maturity roadmap | 10, 11 | 1,051 |
| Performance and commitments | 12, 13 | 223 |

The last page is short, and it is joined to Capability and maturity roadmap if the review prefers three pages.

**Operating Model** (six pages in three sections)

| Page | Sections | Words | Site section |
| --- | --- | --- | --- |
| Foundations | 1 to 3 | 377 | Organization |
| Roles | 4 | 1,516 | Organization |
| Decisions | 5 | 742 | Organization |
| The control loops | 6 | 1,999 | Governance and oversight |
| Records and evidence | 7 | 517 | Governance and oversight |
| Controls and the control catalogue | 8 | 1,926 | Governance and oversight |

Section 2 of the Operating Model (What AICC is) is linked from About AICC as "also stated in".

**Portfolio Management Model** (five pages, in How AICC works)

| Page | Sections | Words |
| --- | --- | --- |
| Foundations | 1 to 3 | 597 |
| The portfolio loops | 4 | 1,309 |
| The portfolio Kanban | 5 | 1,074 |
| The business case and the MVP | 6, 7 | 984 |
| Levels, review, measures, and records | 8, 9 | 353 |

**Solution Lifecycle Model** (eight pages in How AICC works, one in Governance and oversight)

| Page | Sections | Words | Site section |
| --- | --- | --- | --- |
| Foundations | 1, 2 | 414 | How AICC works |
| The flow of value | 3 | 1,358 | How AICC works |
| Backlogs and boards | 4 | 1,051 | How AICC works |
| States and Stages | 5 | 1,163 | How AICC works |
| The cadence | 6 | 1,325 | How AICC works |
| Verification, release, and acceptance | 7 | 1,255 | How AICC works, linked from Responsible AI |
| Life-cycle management | 8 | 1,805 | How AICC works |
| Records, controls, and measures | 9, 10 | 1,400 | Governance and oversight |

**Single-page documents:** AI Policy (2,155), Document Catalog (1,519), Business Model (1,381), AICC Charter (900). The Vocabulary stays one page with a term index, because its content is one table.

## 6. Proposed composition of the sections

| Section | Pages |
| --- | --- |
| About AICC | Statement of Intent (4 pages), AICC Charter, the charter in outline. Links "also stated in": Business Model 2, Operating Model 2 |
| What AICC does | Business Model, Engagement workflow, Engagement guide |
| How AICC works | Portfolio Management Model (5), Solution Lifecycle Model (7), Service delivery workflow and guide, Cadence workflow and guide, Collaboration tooling workflow |
| Organization | Operating Model foundations, Roles, Decisions, Organization guide |
| Responsible AI | AI Policy, AI risk and control workflow. Links: AICC Charter 5 (the AI Risk Appetite Statement), Solution Lifecycle Model 7 (the gates) |
| Governance and oversight | The control loops, Records and evidence, Controls and the control catalogue, Solution Lifecycle Model 9 and 10, Unit governance workflow and guide |
| Library | The 13 templates and their index |
| Reference | Vocabulary, Document Catalog, change history, Records and systems |

The guides sit beside their subjects, and the Library keeps the cross-cutting forms. The page count is about 65, plus 32 generated control pages.

## 7. Further placements

1. **Home.** The home page features the intent, the Strategic Priorities, the Maturity Roadmap, the map of AICC, and the reading routes. The Strategic Priorities and the Maturity Roadmap are the strategy and the roadmap of the portal requirements.
2. **Role pages (optional).** The seven Roles are described in tables (Operating Model 4.2, the Organization guide 3). One generated page for each Role, with its purpose, responsibilities, authority, reporting line, and RACI row, would give a reader a direct answer to "who is this". No content is written.
3. **Lead statement of AICC.** The home page and About AICC take the Summary of intent (Statement of Intent 2) and the Mission (AICC Charter 2) as the lead statement. Business Model 2 and Operating Model 2 are reached by "also stated in".
4. **Workflow and guide pairs.** A workflow page links to its guide as "Companion guide", and a guide links back as "Workflow".
5. **Templates.** A workflow or a guide lists the templates that it uses, and each template page lists the workflows that use it.

## 8. Effect on the scaffold

| File | Change |
| --- | --- |
| sitemap.json | A page may carry a list of document sections; the pages of a split document are added; the guides move to their sections |
| pages/ | One outline file for each new page; the outline of a split page lists its sections with their words |
| check.py | The canonical-page rule moves to the section level of a split document |
| site-structure.md | The sitemap, the inventory, the page types (a document landing page is added), and the open points are updated |
| reading-routes.md | The sequences use the new page identifiers |
| README.md | The rules and the counts are updated |

## 9. Decisions requested

1. Adopt the rule of section 4: split a document above 3,000 words into pages of 600 to 1,800 words, in the groups of section 5.
2. Move the Engagement workflow and guide to What AICC does.
3. Place each guide beside its subject, and leave the templates in the Library.
4. Feature the Strategic Priorities and the Maturity Roadmap on the home page.
5. Add the generated Role pages, or leave them out of the first version.
