# Shape review of the charter, registry, and portfolio

Date: 2026-10-01. Reviewer: independent; did not write the documents. No existing file was edited.
Read in full: the seven documents, the four workflows and README, the seven templates, charter/README, guides/README, registry/README and the main records, the Portfolio README, DR-2026-026, and the prior re-evaluation (2026-10-01-2). Findings already in that re-evaluation (R-01 to R-32) are not repeated unless the new additions changed them; they are cited as "R-nn".
Abbreviations: OM = Operating Model, BM = Business Model, SoI = Statement of Intent, SA = Service Agreement, OR = Outcome Report, SD = Solution Definition, IB = Initiative Brief, UG = unit-governance, SDW = service-delivery.

## 0. Verdict in brief

The shape is sound in its idea (outside-in commitment, SAFe loops, rules in documents, state in the Registry) but it grew by addition. The consulting layer (BM, Engagement, SA, OR, Agreement Log) was laid over the SAFe layer (levels, 13 states, 20 Stages, 13 events, 22 Records) without a join: the Engagement is not a level, a state, or a Record owner in the OM, and its relation to Initiative and Solution is not stated. About 27,000 words must be held; a new joiner can read about 15,000 in an hour. The load is right for a unit of ten, not for one to three. The fix is mostly moving, merging, and labeling, not rewriting.

## 1. The story: Business Model, Operating Model, workflows, templates, registry

### 1.1 The path as it reads today

BM (936 words, clear and short) > OM (5,410 words) > workflows (Engagement, Service delivery, Cadence, Unit governance; 6,800 words) > templates > registry. The BM is a good first page. The path breaks at seven places.

| # | Break | Evidence |
| --- | --- | --- |
| S1 | The BM cannot be read alone, and it does not hand over to the OM. It uses Domain Owner, Domain Expert, Initiative, Solution, Adoption, IT, Proposal before any definition; BM 1.2 says it does not restate the OM, so every term is a forward reference. | BM 3.1, 4.1, 4.3, 2.3 |
| S2 | The Engagement is the BM's central object but is absent from the OM level table (6.1), the state table (6.4), and the Role table (4.2) except "issue of a Service Agreement". OM 8.1 is the only bridge and it is one sentence. The reader leaves BM with "Engagement" and enters OM with "Initiative" and no sentence that equates them. | OM 6.1, 8.1; BM 4.1 |
| S3 | Cardinality of Engagement, Initiative, SA, Solution is not stated. SA has one "Initiative" field and the Agreement Log one "Function and Domain Owner" cell, but INI-003, 006, 008 span several functions; INI-001 and INI-002 have no client function; an Experiment has "no consumer". Who is the client of an enabling Initiative? | SA Part A; agreement-log.md; portfolio-backlog.md; OM 6.7 |
| S4 | The SA "phases covered" include the study, but the SA is issued after the study (the business case is approved first). The commitment therefore never covers the first phase, which is where capacity is spent. | BM 4.1, 5.2; engagement.md section 2 table row 3 |
| S5 | Order of the workflows hides the story. The README lists Engagement, Unit governance, Service delivery, Cadence. The Engagement workflow uses IT, Review, Waiting, Dependency before the Cadence defines them, and Unit governance (the auditor's page) interrupts the delivery story. | workflows/README.md; engagement.md section 3 |
| S6 | Templates are numbered by history, not by flow: SD is 01, IB is 02, SA is 06, OR is 07. The story order is IB, SA, SD, Control Sign-Off, Notes, OR, Quarterly Report. | document-catalog.md 6.1 |
| S7 | No worked example. The Registry has seven INI folders with only a brief each, one Solution Definition (SOL-001), an empty Agreement Log, no SA, no OR. The new model has not been applied to any live Initiative, and no rule says how running Initiatives transition. A newcomer cannot follow one Engagement end to end. | registry/initiatives/*; agreement-log.md |

Entry-page failures: charter/README still lists six documents and omits the BM; guides/README says "being built", so there is no map of "when is which record produced"; registry/initiatives/README still says "Initiative above an Investment Guardrail" (R-03, now contradicts Charter 4.2 and OM 6.2).

### 1.2 What a newcomer finds confusing

1. Three descriptions of what AICC is, which differ: BM 2.1 "internal consulting and innovation lab"; Charter 2.1 "governance framework, a program office, and a capability to build and run"; OM 2.1 "a small team of engineers that provides the governance framework and the program office"; SoI 7.4 "governance framework and program office". OM 2 and BM 2 carry the same heading with different content.
2. The client has four names: client contact, Domain Owner, product owner, function (BM 3.1, OM 4.2, 6.1). All are one person in practice.
3. Three flows for one thing: Engagement steps (Contact, Study, SA, Delivery, OR, Support), SA phases (study, proof, delivery, support), and Stages (20). They do not map one to one, and "phase (alone)" is a term the Vocabulary forbids (BM 4.1, SA template, Agreement Log header use it).
4. Three state vocabularies for something that ends: SA states (Issued, Reviewed, Redirected, Ended; engagement.md Figure 2), the 13 item states, and the Agreement Log "State" column, which names no vocabulary.
5. "Review" has seven meanings: a state, Weekly Review, IT Review and Demo, PI Review and Demo, review week, SA "review at each IT", and the document check.

## 2. Ownership matrix

Marks: DUP = stated in more than one place; DIFF = two places differ; NONE = nobody owns it. "Owner" is the single document that should hold the rule; the others should point to it or be cut.

| # | Topic | Owner (should be) | Also stated in | Mark and note |
| --- | --- | --- | --- | --- |
| 1 | Mandate and authority | AICC Charter 3 | OM 2, 4.6; SoI 7.4; Catalog 4.1 ("binds the Bank") | DUP. NONE for the source: no instrument above the unit (R-01 still open) |
| 2 | What AICC is | Business Model 2 | Charter 2.1; OM 2.1; SoI 7.4; Vocabulary "AICC" | DIFF (see 1.2.1). OM 2.1 and Charter 2.1 should shrink to one line and point to BM 2 |
| 3 | What AICC offers | Business Model 4 | Charter 6.1 (pointer, fine); engagement.md 4; SDW 1, 6; OM 6.7; Vocabulary (Service, Product, Experiment) | DUP and DIFF. engagement.md 4 lets a Product have "agreed response targets"; OM 6.7 and Vocabulary say a Product is supported "on demand". Support level chooses the type there, and the SD type chooses the life here |
| 4 | How it commits | Business Model 5 plus SA template | engagement.md 3 (SA life); OM 4.2, 8.1; UG 5 | DUP and DIFF. BM 5.3 "the function commits to nothing" vs OM 4.2 (Domain Owner funds, names the expert, accepts, owns results); BM 5.2 lists the SA fields again, as the template does |
| 5 | Roles and decisions | OM 4, 5 | SDW 8 (decision table); UG 4, 5, 6; AI Policy 2.1, 3.2, 6.1; Charter 3.1, 4.2; Vocabulary "Accepted" row | DUP. SDW 8 and UG 6 copy OM 4.2 and 4.4. A rule in the Vocabulary row for Accepted ("The Domain Owner approves... and accepts") |
| 6 | Levels and backlogs | OM 6.1 to 6.3 | SDW 2; Vocabulary; Registry README; OM 9.2 | DUP (four tables of the same levels). Engagement is not in the level table (S2) |
| 7 | States and Stages | OM 6.4, 6.5 | Vocabulary 4.2, 4.3; SDW Figure 2 (35 arrows) and 9; engagement.md Figure 2 | DUP and DIFF. Waiting is a state in OM 6.4 but a flag in OM 6.4 closing note and SDW 9. "Accepted to Closed" has no condition. Failed Assumption "puts the work in Waiting" but Waiting means a Dependency |
| 8 | Cadence and events | Cadence workflow for the flow; OM 7 for the obligation that the events exist | OM 7.1 (13 events with intent); cadence.md 9.2 (the same 13 with intent); Vocabulary "Event"; cadence.md 9.1 glossary | DUP three times (R-32). Plus rules inside the workflow (cadence.md 7, 8) |
| 9 | Risk Tiers and controls | AI Policy 3 (requirements); OM 6.6 (when, who releases) | UG 5 (control list), UG 6; SDW 5, 8; SD template section 4; Control Sign-Off | DUP. The auditor's control list lives only in a workflow that "states no rule" and names records that do not exist (R-06) |
| 10 | AI rules | AI Policy | SoI 5, 6; Charter 5 (appetite); templates | Acceptable. Charter 5 holding the appetite is a known exception (DR-2026-003) |
| 11 | Funding and value | Charter 4, 7 | BM 6; SoI 10.4, 12.3; OM 6.2, 6.5; Quarterly Report | DUP and DIFF. BM 6.2 says the Envelopes fund AICC and AICC does not charge; Charter 4.1 and OM 4.2 say Domain Owners fund Solutions from the Envelope. Two measure lists: Charter 7.1 and BM 6.1/6.2. No method for "benefit that the function confirms" |
| 12 | Records and evidence | OM 9 (rule) plus Registry README (index) | Vocabulary "Record"; Catalog 1.3; Charter 7.2; "Where it runs" in all four workflows; UG 5 | DUP and NONE. OM 9.2 duplicates the Registry README; the evidence model (live versus evidence, Jira is not an evidence store) is still unwritten (R-02) |
| 13 | Document control | Document Catalog | UG 7 and Figure 4 (restates 3 and 4); SoI 13.3, 13.5; OM 7.3 | DUP. Catalog 5.2 limit of eight documents is already used by seven plus planned guides |
| 14 | Jira and Confluence runtime | Nobody. Proposed: one guide, plus one rule in OM 9 for the cutover | OM 9.1; workflows/README; SDW 9 (mapping tables); engagement.md 6; UG 8 | NONE. Present tense "runs in Jira" in four places, while OM 9.1 says Registry is live (R-07). Platform design (editions, issue types) is in a workflow |
| 15 | Support and incidents | Nobody for services. AI Policy 5 owns the AI Incident only | BM 4.2; engagement.md 4; OM 6.7; SDW 6 last paragraph | NONE. "At agreed response targets", "full service", the lane Incident, and Service Management have no owner, no rule, and no record. AI Incident and the lane "Incident" are different things with one name |
| 16 | Adoption oversight | OM 6.8 | BM 2.3; SDW 7; Portfolio README (adoptions/ folder, empty); Vocabulary | DUP and DIFF. Adoption has its own six states (OM 6.8) that are not the 13; no Record, no template; the word collides with SoI 9.4 "Adoption within Domains" |
| 17 | Strategy proposals | Business Model 2.3 states; OM 6.8 decides | UG 2 (yearly row); Vocabulary "Proposal"; OM 6.7 (Experiment ends in Proposal) | NONE for form, record, and receiving body ("the Bank decides"). Not in OM 7.3 (R-31). Vocabulary says the Registry holds "the proposals" but the Registry README has no such Record |
| 18 | Training and competence | SoI 10.1 (intent); AI Policy 2.1 | Charter 6.1 (stale reference) | NONE for records (B-13 in the prior review) |
| 19 | Capacity of AICC | Business Model 6 | Teams record (capacity blank); RI-017; Limits on WIP in OM 6.3 | NONE. The SA commits days per IT; no rule caps the sum against the people available; WIP limits apply to states, lanes, Domains, not to Engagements |

## 3. Proportion

### 3.1 What the reader must hold now

| Kind | Count | Where |
| --- | --- | --- |
| Documents / workflows / templates / guides | 7 / 4 / 7 / 2 planned | Catalog 5.1, 6.1 |
| Roles, plus bodies that are not Roles | 7, plus Hats, AI Steering Committee, Board Committee, 5 Control Functions, internal audit | OM 4 |
| Levels | 6 (plus Engagement outside the table) | OM 6.1 |
| Backlogs, boards, lanes | 3, 2, 3 | OM 6.2, 6.3 |
| States / Stages | 13 / 20 distinct (Retire counted once) | OM 6.4, 6.5, 6.7 |
| Other lifecycles | 4 (SA states, Engagement steps, document states, Adoption states) | engagement.md, Catalog 3.2, OM 6.8 |
| Events | 13 in 4 loops (plus Hats, plus the IP week order) | OM 7.1 |
| Records | 22 rows in OM 9.2; 21 in Registry README (the two lists differ) | OM 9.2 |
| Defined terms | 96, plus 13 states and 11 Stage rows | Vocabulary 4.1 to 4.3 |
| Identifier schemes | 15 (PRI, INI, SOL, EP, FT, DEP, MS, DR, RI, ARC, PLT, AGR, OUT, AICC-xxx, IT/PI) | Registry README, templates |
| Roles of a single person | One person is AICC Lead, AICC Engineer, Domain Owner of AICC work, and Checker's appointer (Appointments, OM 4.6) | Appointments |

### 3.2 Too much for one to three people

The work is real and the people are few: RI-017 already records one person leading six goals. Eight places carry weight without adding control.

1. Events: 13. A Daily Stand-up, Weekly Planning, Weekly Review, Backlog Refinement, IT Review, Retrospective, monthly Steering, PI Review, Inspect and Adapt for a team of one meet the same person. The IP week holds five events in five days (cadence.md 4).
2. States: 13 plus the Waiting that is already a flag in Jira. Completed to Review to Accepted to Closed is four steps for one act (the product owner says yes).
3. Stages: 20, of which Epic and Feature stages (Analysis, Explore, Design, Develop, Verify, Deploy) restate what a Jira workflow or a checklist already does. The only Stage that carries control is Verify (OM 6.6), and it is a rule, not a Stage.
4. Levels and backlogs: the Work Item is a Jira sub-task and need not be a charter level; the IT Backlog is a selection from the Program Backlog, not a third list.
5. Records: seven are working state that Jira will own (two backlogs, boards, Roadmap, Calendar, Dependency Map, Dashboard, Teams, PI folder). Writing them by hand as "Records" is the largest ongoing cost and none is evidence.
6. Templates and the Agreement chain: four documents restate the same outcome targets and acceptance (IB section 2, SA Part A, SD section 5, OR section 3), plus Quarterly Report. For one Engagement that is five writings of the same intent.
7. Terms: about 15 are unused or only repeated (see 3.3).
8. Lifecycles for one thing: Engagement steps, SA states, 13 states.

### 3.3 Cut and merge list (keeps the intent, does not redo the work)

| # | Change | Size | Effect |
| --- | --- | --- | --- |
| P1 | Add one clause to OM 7.1: "AICC runs a light mode while its Team has up to three people": one Weekly Review (planning and review, Mondays or Fridays), IT Planning, IT Review (retrospective and monthly Steering held in it), PI Review (Inspect and Adapt inside it), PI Planning, quarterly Steering. Daily Stand-up and Backlog Refinement are optional. Six events, not 13. | small | The events stay; the obligation shrinks. Keep the table; mark the optional ones |
| P2 | States: make Waiting a flag in OM 6.4 (as SDW 9 and the suspension rule already treat it); fold Completed into Review and Accepted into Closed (acceptance is a field, who and when); make Pivoted a resolution of Cancelled. Result: 9 states (Proposed, Discovery, Approved, Active, Deferred, Review, Closed, Rejected, Cancelled). Jira already has five. | medium | Removes the null transition Accepted to Closed and the Assumption versus Dependency problem |
| P3 | Stages only where a gate or a type exists: Initiative (Scoping, Business case), Solution (Definition, Delivery, then the type Stages). Epic and Feature have none; Verify stays as the rule in OM 6.6. 20 to about 13. | medium | Vocabulary 4.3 shrinks by a third |
| P4 | Levels: five in the charter (drop Work Item to "Jira sub-task, not a charter level"). Say Epic and Feature may be one level until a second Team exists. | small | Backlogs: two lists (Portfolio, Program) and the IT selection as a marked subset |
| P5 | Merge Agreement Log into the Portfolio Backlog (add columns: client function, phases, support level, SA, OR). Make Engagement an Initiative with a client function ("Engagement is an Initiative that has a client function"). Add: an enabling Initiative has the Executive Sponsor as client. | small | Removes a Record, a log, and the cardinality gap (S3). If one Initiative spans functions, one SA per function, listed in the brief |
| P6 | Split OM 9.2 into "Working state" (Priorities, backlogs, boards, Roadmap, Calendar, Dependency Map, Dashboard, Teams, PI) and "Evidence records" (Decision Log, Appointments, Risks and Issues, AI Registry, Standards, Reports, Notes, Agreement/Portfolio extract, Initiatives, Assessments). Move the table itself into the Registry README and leave one clause in OM 9. | medium | Fixes R-02 and removes the duplicate index |
| P7 | Templates: IB keeps the case; SA Part A states commitment only and points to the IB for scope, outcome targets, and risks; SD section 5 is acceptance criteria only; OR section 3 points to the SA targets. Renumber templates in story order (a mapping table in the Catalog, ids unchanged). | medium | One statement of the target, referenced three times |
| P8 | Vocabulary: remove or move Hat, Community of Practice, Reusable asset, Stakeholder (merge into "notified"), Blocked day and gray day (to the Calendar), Short forms, Event (row), Cadence glossary (cadence.md 9.1 deleted, Vocabulary is the one source). About 15 fewer terms. | small | |
| P9 | One lifecycle for the SA: the SA has no states; it is "issued", "changed" (changes table), and "ended by the OR". Delete engagement.md Figure 2 and the Agreement Log "State" column (use the Initiative state). | small | Removes a third state vocabulary |
| P10 | Workflows: keep four but order them Engagement, Service delivery, Cadence, Unit governance; delete the duplicated tables SDW 8 and UG 6 (they point to OM 4.2 and 4.4). | small | About 500 words fewer |

### 3.4 Too thin

1. Intake and capacity of the Engagement: no criteria to take a Contact in, no capacity ceiling against the people available, no WIP limit on Engagements (item 19 in the matrix). For a consulting unit of one person this is the core control, and it is absent.
2. Support and run of a Service: nothing beyond the words (item 15). Either state "AICC runs no Service until it has a second Engineer and a Service Management queue" or write one page.
3. Benefit confirmation: the function "claims and confirms" with no confirmer, method, or baseline (BM 6.1; Charter 7.1).
4. Strategy Proposals and Adoption oversight: the mission side of the lab has no form and no Record (items 16, 17).
5. Transition: how running Initiatives get an SA (INI-001 to INI-008) and whether work already accepted needs an OR.
6. Entry and guides: no one-page "AICC on a page", no reading map, no worked example; guides are planned but both are named only in the README.
7. Client feedback at the OR: a consulting unit that never asks the client how it went has no quality loop. One optional line in the OR is enough.

## 4. Layering and wording

### 4.1 Rules hidden in workflows (they say they state none: Catalog 5.3, Vocabulary 2.1, README)

| Where and what the rule says | Move to |
| --- | --- |
| cadence.md 7 (four numbered rules): move to the day before, never after; a missed event is not held later; the Weekly Review may be in writing; nothing is approved | OM 7 as one clause, or Calendar record header |
| cadence.md 8: the dated calendar "is built at the PI Planning for the next two quarters" | OM 7.1 (obligation) or delete (it is "not built yet") |
| engagement.md 3: the SA "is changed in a note when scope is redirected"; either side may redirect only at an IT boundary; a failed Assumption puts the work in Waiting | BM 5.3, 5.4 (already partly there); delete "Waiting" |
| engagement.md 4: support level to Solution type mapping | BM 4.2/4.3, once, and fix the Product difference |
| UG 5: the control list with owners, timing, and evidence | A document: OM new section "Controls" (or the Catalog) as the auditor's matrix; UG keeps only the picture |
| UG 6: separation table | Delete; OM 4.4 owns it |
| SDW 9: "Jira stays clean", five statuses, mapping, "acceptance with who and when in a field" | Guide (runtime); the field is a Record rule for OM 9 |
| SDW 5: "A Feature does not become approved until its Dependencies are known" | Already OM 6.4/6.5; delete |

### 4.2 Flow detail in documents

OM 7.1 event table (13 rows with intent) belongs in cadence.md; OM keeps one clause listing what must exist. OM 6.3 and 6.6 narrate flow (selection at IT Planning, split of a Feature). OM 9.2 is an index. Vocabulary 4.3 is a flow table (Stages), and the Vocabulary "Accepted" and "Event" rows carry a rule and a list. Catalog 7.1 is a ten-question procedure that belongs in a guide or a template ("Document Check"). BM 5.2 lists the SA fields that the template already lists.

### 4.3 Templates that duplicate documents

SA and OR template headers restate BM 5.1 and 5.5. SD section 4 restates AI Policy 3.2. Control Sign-Off section 1 restates AI Policy 3.3. Quarterly Report header states who approves (Charter 7.2). Fix by one line each: "Rule: BM 5". Nothing else changes.

### 4.4 Pairs a reader will mix up, with a one-line distinction

| Pair | Distinction |
| --- | --- |
| Business Model, Operating Model, AICC Charter | BM: what we promise to clients and how. Charter: the mandate, money, and appetite given to us from above. OM: how we run inside, who decides, and what we record |
| Engagement, Initiative, Solution | An Engagement is an Initiative that has a client function. An Initiative is the funded business program and its case. A Solution is the thing built, with a Risk Tier |
| Service Agreement, Initiative Brief, Solution Definition | Brief: why we invest. Agreement: what we promise the function and how we work together. Definition: what the thing is, how risky, who owns it |
| Outcome Report, Quarterly Report | OR closes one Engagement for the client. The Quarterly Report reports the portfolio to the Sponsor and the Board |
| Initiative, Epic, Feature, Work Item vs Jira | Initiative, Epic, and Feature are Jira issue types; Work Item is the sub-task; a Solution is a Confluence page, not an issue (SDW 9, R-09) |
| State, Stage, phase | State is the position in the life; Stage is a named step inside Discovery or Active; "phase" is not a term (use Stage, or "phase" only as an alias in the SA, mapped once) |
| Service (type), Service Agreement, Service Management, full service | Service is one offering type; the others share the word and mean a commitment, a tool, and a support level. Rename "full service" to "AICC runs it" |
| Product owner, Domain Owner, client contact | One person; Domain Owner is the Role, the others are the same Role seen in a delivery or client light. Retire "client contact" or define it |
| Handoff, Handover | Handoff is an Experiment's transfer to a Receiver; Handover is a Product's delivery to a consumer. Merge to "Handover" |
| Proposal, Proposed | A Proposal is a request to the Bank to adopt; Proposed is the first state of an item |
| Adoption, Adoption within Domains | "Adoption" is the term for a Solution others deliver; the Strategic Priority uses the ordinary word. Rename the term "Adopted Solution" (R-24) |
| Registry, AI Registry | Registry is the folder of Records; AI Registry is one Record in it. Rename the second "AI Inventory" if possible; at least avoid "Registry" alone |
| Record, document, Template, Report | Record holds state or evidence; document holds a rule; Template is a form; Report is a Record issued to someone |
| AI Incident, lane Incident, Incident record | AI Incident is the policy event (AI Policy 5). The lane is a class of service. Call the lane "Urgent" |
| Review (seven senses) | Name the event "IT Review", "PI Review", "Weekly Review"; call the state "In review"; call the SA check "SA check at the IT" |
| Cadence, Calendar, Roadmap | Cadence is the template flow, Calendar the dates, Roadmap the intent of the next three months. Only Calendar is a Record |
| Check, Validation, Sign-off, Acceptance, Release | Check is by a person other than the builder; Validation by a Control Function; Acceptance by the product owner against criteria; Release lets the Solution leave its first users |

## 5. Audit and commercial view

### 5.1 What now answers the auditor

| Question | Answer in the charter today | Quality |
| --- | --- | --- |
| What does AICC commit to? | BM 4, 5; SA template; Agreement Log | Good at the outline. Not yet applied: no SA exists for any running Initiative (S7) |
| How is it controlled? | OM 4, 5, 6.6; AI Policy 3 to 6; UG 5 | Good rules. The control matrix is in a workflow and names records that do not exist (R-06) |
| Where is the evidence? | OM 9, Registry README, engagement.md 6 | Weak. The same sentence appears in three places with three different folder rules: the Initiative folder (OM 9.2), the Agreement Log (BM 5.5), and "above a guardrail" (initiatives/README) |
| Who may do what? | OM 4.2, 5.3 | Good. The authority above the unit is missing (R-01) |

### 5.2 Still missing at the level of the shape (not wording)

1. A mandate instrument above the unit, and an appointment instrument (R-01, R-04). Without it the SA, "binds the Bank", and activation by the author rest on nothing.
2. One control matrix in a document: control, rule clause, owner, frequency, evidence record, Registry location. The seven records named in UG 5 but undefined (Board report, Incident record, Exception record, Deliverable record, Document check, PI snapshot, Record of the approval) need either a home or a template (R-06).
3. The evidence model: live state versus evidence, the cutover date and criterion, "Jira and Confluence are not an evidence store", retention, and integrity (R-02, R-16, R-21). Stated once, in the OM, with an extract template (the "Registry Snapshot" in the prior review).
4. Controls that the new commercial layer needs and does not have: (a) a check that every closed Engagement has an OR and every OR is accepted; (b) a capacity reconciliation (days committed against used, by whom, how often); (c) a rule for who confirms the benefit and from which source; (d) segregation: the AICC Lead issues the SA, delivers, and writes the OR; the OR has no reviewer other than the product owner. For one person this may be accepted, but it should be an accepted limit entered as a risk, not an omission.
5. A cost view of AICC itself: BM 6.2 says the Envelopes remain the funding of AICC, and capacity is in days, but no cost of AICC (people, platform) is tracked or referenced, and no budget owner for AICC is named. Auditors ask this first of a unit that "does not charge".
6. An Engagement-level risk and quality loop: key-person risk (RI-009, RI-017) is in Risks and Issues but not linked to commitments; no client feedback; no incident path for a running Service.
7. Carried from the re-evaluation, unchanged by DR-2026-026: no terms of reference for the AI Steering Committee (R-11), no delegation by the Executive Sponsor (R-12), no conflict declarations register (B-06), no access review of the tools (B-19), personal names in Appointments with no retention rule (B-28), blank dates in Appointments (R-04).
8. The Guide to the Registry (which record, which event, who keeps it) does not exist. It is the auditor's index and should be built before the Russian version.

## 6. Verdict and reshape plan

### 6.1 Verdict

The shape works for a unit of ten and is unproven for one to three. The consulting layer is right in idea (commitment, outcome, evidence) and wrongly joined: the Engagement has no place in the OM, and four documents state the same target. The corpus passes on names and deciders after DR-2026-025, but it does not yet let an auditor trace one Engagement from request to outcome to evidence, and it does not tell a newcomer where to start. None of the 11 changes below redoes accepted work; most move, merge, or mark text.

### 6.2 Changes in order of value

| Order | Change | Size | Why first |
| --- | --- | --- | --- |
| 1 | Join the Engagement to the OM: one clause "An Engagement is an Initiative that has a client function"; one SA per client function; enabling Initiatives have the Executive Sponsor as client; add the SA and OR to the OM 4.2 and 6.9 and the phases-to-Stage map in the Vocabulary; cut Figure 2 and the Agreement Log "State" (P5, P9) | small | Closes S2, S3, S4 and the three-vocabulary problem at once |
| 2 | Write the evidence model once in OM 9 and split 9.2 into working state and evidence records; move the table to the Registry README; state that Jira and Confluence are not an evidence store; fix "Where it runs" in all four workflows to the future tense with the cutover rule (P6; R-02, R-07) | medium | The auditor's first test, and fixes five duplications |
| 3 | Add a "light mode while the Team has up to three people" clause (P1) and cut the states to nine, Waiting as a flag (P2), Stages to Initiative and Solution only (P3), Work Item out of the charter levels (P4) | medium | Makes the model runnable by one to three people without removing anything for later |
| 4 | Move the control list from UG 5 into a document section "Controls" (OM or Catalog), with owner, clause, record, and Registry location; define the seven missing records or point each to an existing one (R-06) | medium | The one table an auditor will test |
| 5 | Add the mandate and appointment instrument: a decision or order reference in Charter 3.1 and in Appointments (From, authority, decision), and a delegation line for the Executive Sponsor (R-01, R-04, R-12) | small | Without it everything rests on self-activation |
| 6 | One statement of each target: IB owns the case and targets; SA Part A states commitment and points; SD section 5 is acceptance criteria; OR points to the SA (P7). Renumber templates in story order by a mapping table | medium | Cuts four writings to one; keeps all forms |
| 7 | Commercial controls: a capacity ceiling for Engagements against the people available, a rule that no Engagement starts above it, a benefit confirmer and source, an OR completeness check at the quarterly Steering, and a cost reference for AICC itself (matrix items 11, 19; section 5.2 items 4, 5) | medium | The consulting model is a promise; without a ceiling a one-person unit over-promises (RI-017) |
| 8 | De-duplicate: delete OM 7.1 event table in favour of cadence.md 9.2 (keep one list of events and intents, in cadence.md), delete SDW 8 and UG 6, delete UG 7, shrink OM 2.1 and Charter 2.1 to point to BM 2, move cadence.md 7 and 8 rules into OM 7 (matrix items 2, 5, 8, 13; section 4.1) | medium | About 1,200 words fewer and one source for each rule |
| 9 | Fix the word collisions with one pass: Handoff/Handover, Registry/AI Registry, lane Incident, "full service", "phase", Adoption, "client contact", Review senses; remove 15 terms from the Vocabulary (P8; section 4.4) | small | Cheap; removes the commonest confusions |
| 10 | Build the entry: charter/README with the reading path (BM, OM sections 1, 4, 6, workflows in the order Engagement, Service delivery, Cadence, Unit governance, then templates, then Registry); a one-page "AICC on a page"; one worked trace of INI-004 and SOL-001 (SA, brief, SD, Registry rows) as the first guide; update initiatives/README to "every Initiative" | medium | Gives the newcomer the hour; the worked example makes the new layer testable |
| 11 | Close the gaps that have no owner: support and run of a Service (one page, or state that AICC runs none yet), strategy Proposal form and Record, Adoption record, transition rule for running Initiatives (SA for INI-001 to INI-008, or an exemption note in DR-2026-026) | large | Turns the commercial and mission sides from outline into controlled flows; do after 1 to 10 |

Items 1, 5, 9 and the entry page can be done in one sitting. Items 2 to 4 are the structure; 6 to 8 are the trim. Do the Russian version after 10, because it freezes the vocabulary.
