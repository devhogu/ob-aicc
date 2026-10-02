# Charter re-evaluation: runtime model, audit and HR expectations, evidence templates, guides

Date: 2026-10-01. Assessor: independent; did not write or change the documents. No existing file was edited.
Scope read in full: the six documents, workflows (cadence, unit-governance, service-delivery, README), five Templates, guides README, the Registry records (README, Appointments, Decision Log, Risks and Issues, Teams, AI Registry, Priorities, backlogs, boards, notes, standards), the Portfolio README, and DR-2026-009, 018, 019, 024, 025. Earlier assessments were used only to avoid repeating fixed findings.
Model assumed: the charter is static and is the rule; Jira (on premises, with Service Management) and Confluence run the live work; they are not an evidence store; the Registry keeps extracts as documents for audit and sharing.

## 1. Verdict

The corpus is coherent on names, levels, states, and deciders after DR-2026-025. Two things stop it from standing up to an auditor: (1) the evidence model is only half written (the live state versus the evidence is blurred in OM 9 and the Vocabulary, and several controls name records that do not exist), and (2) the governing authority is thin (the AICC Lead activates documents that bind the Bank; the governing body has no terms of reference; appointments have no dates, authority, or change rules). The model is also heavy for one to three people. Task A: 32 findings (2 Blocker, 15 Major, 15 Minor). Task B: 28 expectations, 15 marked GAP, 13 PARTIAL, none fully OK. Task C: 11 templates (5 existing, 6 new). Task D: two guides.

## 2. Task A: consistency findings

Severity: Blocker (cannot be defended to audit as written), Major (a control or a decision is unclear, missing, or contradicted), Minor (wording, term, or proportion).

| ID | Sev | Evidence | Finding | Fix |
| --- | --- | --- | --- | --- |
| R-01 | Blocker | Document Catalog 4.1; SoI 13.5; Charter 3.1, 5.4; AI Policy 2.1; DR-2026-018 | The AICC Lead owns every document and activates all of them, and activation "binds the Bank". The AI Policy obliges all employees and the Charter holds the risk appetite, yet no one above the unit approves them. The source of the Executive Sponsor's mandate is not recorded. The Board Committee only "notes" an appetite that the Lead owns. | Record the mandate (decision or order reference) in the Charter and Appointments, and make the SoI, Charter, and AI Policy effective on the Executive Sponsor's recorded approval; or state that they bind AICC and the Entities that take part. |
| R-02 | Blocker | OM 9.1, 9.2; Vocabulary "Record"; unit-governance 8 | No single rule says what is live where. OM 9.2 puts live-state items (Backlogs, Kanban, Dashboard, Teams, Calendar, Dependency Map) and evidence records in one table "as files". "Until Jira and Confluence run the work" has no criterion, date, or Decision. Nowhere does it say that Jira and Confluence are not an evidence store. | Split 9.2 into Working state (Registry now, Jira and Confluence after a dated cutover Decision) and Evidence records (always the Registry, as extracts), and state that Jira and Confluence are not evidence. |
| R-03 | Major | SoI 10.4; Document Catalog 6.1; Initiative Brief template header vs OM 6.2, Charter 4.2, DR-025 item 7 | SoI, Catalog, and the template say a brief is for an Initiative "above a Guardrail"; OM, Charter, and DR-025 say every Initiative has a brief. | Align the three to "every Initiative has a brief; above a Guardrail it also needs the Executive Sponsor's approval". |
| R-04 | Major | OM 4.6; registry/appointments.md; RI-001 | The Executive Sponsor and AICC Lead rows have no From date, authority, or decision reference. The 60-day clock for missing Appointments ends 2026-11-30. RI-001 (formal appointment) was closed by DR-018, which appoints no one. There is no rule on change, relief, acting marker, or leaver. | Add to 4.6: every appointment, acting designation, change, and relief is entered within five working days with date and decision reference; enter the two appointments now. |
| R-05 | Major | SoI 13.5; AI Policy 2.4, 7.1; Appointments | SoI 13.5 lists participating Entities "in the Appointments Record"; Policy 2.4 puts the Sponsor's delegate there; Policy 7.1 needs an "acting" mark. The Record has no such table or column. | Add the tables and the column (see the Assignment Map in section 4). |
| R-06 | Major | OM 9.2; Document Catalog 6.1; unit-governance 5; registry/README | Control Sign-Off has a Template but no Record or folder. Unit-governance 5 names evidence that OM 9.2 does not define: Board report, Incident record, Exception record, Record of the approval, Deliverable record, Document check, PI snapshot. Assessments and decisions/ are in the folder but not in 9.2. | List the evidence Records in 9.2, one per control, with the event that produces each (section 4). |
| R-07 | Major | workflows/README last paragraph; unit-governance 8; service-delivery 9 | The workflows say in the present tense that the loop "runs in Jira and Confluence", while OM 9.1 and DR-025 say the Registry is live until cutover. Service-delivery 9 says the business states are "in the charter and the Registry", but its own table puts state and Stage in Jira fields. | Say "will run in Jira and Confluence after the cutover of OM 9.1"; say the business state is a Jira field and the Registry holds its extract. |
| R-08 | Major | Vocabulary: Record, Dashboard, Calendar, Cadence, Registry; 3.4 "wiki" | "Record" is "a file", which fits neither a Jira-held working state nor an evidence extract. Cadence is called a Record yet is an unapproved charter workflow. "Wiki" now collides with Confluence and the repository's wiki/ folder. | Define Record as an evidence extract or the working state, remove Cadence from the Records, and name Confluence in 3.4. |
| R-09 | Major | service-delivery 9; OM 6.1, 6.5 | The Solution carries the Risk Tier, check, release, and AI Registry entry, but has only a Confluence page and a label, with no Jira workflow or approval step. "Needs the edition of Jira that has [the Initiative level]" is stale for the latest on-premises edition. | Model Initiative and Solution as levels above Epic, each with its own approval transition and the five statuses. |
| R-10 | Major | Document Catalog 7.1, 4.1; Vocabulary "Check"; OM 4.4(a) | The AICC Lead checks the documents that the Lead wrote and activates, though a Check is "by a person other than the one who built it". A passed check leaves no record; only failures become Findings. | Require a Document Review Record (pass or fail) and a yearly check by a person the Executive Sponsor names. |
| R-11 | Major | OM 4.5, 5.3, 7.2, 7.4 | The AI Steering Committee has no terms of reference: members, absence rule, cadence, how advice and dissent are recorded. 5.3 says the Sponsor decides "after asking the Committee"; 7.2 says alone while unformed; 7.4 asks only risk and compliance. | Add one clause: membership in the Assignment Map, advice and dissent in the Steering Summary, and a stated rule for absence. |
| R-12 | Major | OM 4.2, 6.9; AI Policy 2.4; DR-019 | The Executive Sponsor (the CEO) accepts all enabling work of AICC and approves every published AI output. Delegation exists only for outputs (2.4) and a deputy (4.6). A decider gap and a single point of stoppage. | Add a general, scoped, dated delegation by the Executive Sponsor in the Assignment Map. |
| R-13 | Major | OM 6.5 Initiative row; portfolio-backlog.md | The Domain Owner approves an Initiative, but INI-003, 006, and 008 span Domains and have no Domain Owner named. 6.9 fixes acceptance only. | For an Initiative that spans Domains the Executive Sponsor approves, or the brief names a lead Domain Owner. |
| R-14 | Major | OM 4.2, 4.4(d), 4.6, 6.5 | The AICC Lead assigns the Risk Tier, builds, approves the use of own Solutions, decides Exceptions to AICC requirements, and is Domain Owner of AICC work, so approves the business case of INI-001. Only validation is barred. | Add a compensating control: Steering samples the Lead's Decision Log lines each month, and the Checker confirms the Risk Tier for every tier, not only Tier 1. |
| R-15 | Major | AI Policy 2.1, 5.3, 6.1; Charter 6.2 | Incident, Exception, approval, and request intake are described as "entered in the Risks and Issues Record" or "asks the AICC Lead". Jira Service Management, with approvals and audit trail, is not mentioned in any document. | Keep the rules tool-neutral and state that intake, incidents, Exceptions, and approvals run in Service Management, with an extract to the Registry. |
| R-16 | Major | OM 9.1; RI-005; Appointments | "The history is not rewritten" is not a control: no protected branch, backup, or signing is required; repository visibility is unconfirmed; Appointments hold personal names; "forever" conflicts with "the period the retention rules require". | Add a rule: protected main branch, restricted visibility, retention period by record type, minimum personal data. |
| R-17 | Major | OM 3.1(g), 6.3, 6.4, 7.1; all workflows | Heavy for one to three people: 13 states plus Stages, 13 events (the IP week has five in five days, retrospective and refinement for one person), three backlogs, two Kanbans, Dependency Map, Dashboard, Calendar, Cadence, and 21 hand-kept Records. Review is a separate state for one product owner. | Add a one-person mode: one weekly session, retrospective merged into the IT Review, refinement not an event, Review and Accepted collapsed, Dashboard generated from Jira. |
| R-18 | Minor | Document Catalog 3.1, 4.1, 4.2; change logs OM 5.3, 5.4, Charter 1.0, Catalog 2.5, Vocabulary 3.3 | Revisions that change meaning (for example the content rule of Catalog 2.5) are logged "none", though 4.1 and 4.2 require a Decision Log entry for an activation. | Each activation row cites a Decision, or the rule says which changes need none. |
| R-19 | Minor | OM 7.1, 7.3; cadence 4 | PI Planning (Thursday) sets the Roadmap before the quarterly Steering (Friday) confirms priorities and funding; OM 7.3 says the Steering sets the Roadmap. | Say the PI Planning proposes and the Steering confirms, or move the Steering before it. |
| R-20 | Minor | SoI 11.1; OM 6.10 | The timing of Maturity Levels is "set in the roadmap of the Portfolio", but the Roadmap shows three months. | Point to the target dates in the Priorities Record. |
| R-21 | Minor | Charter 7.1, 7.2; SoI 12.2; Vocabulary "Measure", "PI Objective"; priorities.md | "Share of PI Objectives achieved" conflicts with a PI Objective that is "not a commitment". Measures lack baseline, owner, and source. SoI 12.2 says Board Committee "at regular intervals"; Charter says each quarter. | Use "value scored"; require owner, source, and the Registry Snapshot as source; align 12.2 to quarterly. |
| R-22 | Minor | Solution Definition template line 12; OM 6.4, 6.5, 6.9 | The template says the Domain Owner "accepts" the definition; OM says approves. "Backlog" is used alone, a term Vocabulary forbids. | Say "approves"; name the backlog of the level. |
| R-23 | Minor | OM 2.3, 4.3, 6.4, 7.1; workflows | Terms used but not defined: keeper (of a backlog), snapshot, review week (only in cadence.md), product owner (a function of the Domain Owner or Sponsor), first-line (while "second line" is Not used). | Define or drop them in the Vocabulary. |
| R-24 | Minor | Vocabulary "Adoption"; Charter 6.1(a); SoI 9.4 | The defined term Adoption (a Solution others deliver) collides with the ordinary use "adoption engagement" and "Adoption within Domains". | Rename the defined term "Adopted Solution". |
| R-25 | Minor | OM 6.4, 6.7 | A Solution is Active until retirement and then needs Completed, Review, Accepted, Closed; "the Team pulls it" does not fit an Initiative or Solution. | Add the end-of-life rows for Initiative and Solution. |
| R-26 | Minor | OM 4.4(f); unit-governance 5 | Audit has "read access to every Record"; Jira, Confluence, and Service Management are not named. | Extend read access to the working tools, read-only. |
| R-27 | Minor | AI Policy 3.5, 5.5 | The incident review is by "the people involved" with no single Role. | Name the AICC Lead as owner. |
| R-28 | Minor | Appointments (Domain Owner "by position"); Vocabulary 3.6 | Appointing "by position" mixes post and person; a leaver changes the Holder silently. | Appoint a person, with the post as an attribute. |
| R-29 | Minor | notes/2026-09-steering.md; DR-2026-012 | An evidence record has no exact date ("to be entered"; DR-012 dated "2026-09"). | Enter the date, or mark it reconstructed. |
| R-30 | Minor | Charter 4.1, 4.2; OM 4.2, 6.5 | Domain Owners fund Solutions from Envelopes that the Sponsor sets; Guardrails are unset (RI-012). Only Charter 4.2 says the Sponsor approves any commitment until then. | Cross-refer in OM 6.5. |
| R-31 | Minor | unit-governance 2 (yearly row) | The yearly "strategy proposal" is not in OM 7.3. | Add it to 7.3 or remove it. |
| R-32 | Minor | cadence 9; Vocabulary 4.1 | The Cadence keeps its own glossary (Loop, Control, Review week, Event) that duplicates the Vocabulary. | One source: the Vocabulary. |

## 3. Task B: what internal audit and HR would expect

This is general practice (IIA standards, the three lines model, COSO, usual committee governance, HR organization controls). It is not a Bank requirement. It must be validated with the Bank's internal audit and HR before it is used as a standard.
Marks: OK (rule and record exist), PARTIAL (rule or record is thin), GAP (no rule or no record).

| # | Expectation | Rule in the charter | Record in the Registry | Mark |
| --- | --- | --- | --- | --- |
| B-01 | Mandate or terms of reference, approved above the unit | Charter 2.1, 3.1; OM 1; Catalog 4.1 (self-activation) | DR-2026-018 only; mandate source missing | GAP |
| B-02 | Delegation of authority and decision rights, with financial limits | OM 4.2, 5.2, 5.3; 4.6 (deputy, over two weeks); Charter 4.2 | Decision Log; deputy column blank; Guardrails unset (RI-012) | GAP |
| B-03 | Role profiles and RACI | OM 4.2 (does, decides) | None | GAP |
| B-04 | Organization chart, reporting line, place in the Bank's staffing structure | OM 2.1, 6.1 only | Teams; Appointments | GAP |
| B-05 | Appointments, changes, and leavers log with dates (joiners, movers, leavers) | OM 4.6 (appointment, 60 days) | Appointments From and To columns, blank; no change or leaver rule | GAP |
| B-06 | Conflict-of-interest declarations and register | OM 5.7 (declare at the decision) | None; no annual declaration | GAP |
| B-07 | Minutes and decisions of the steering committee | OM 7.2, 5.6; Notes Template | notes/2026-09-steering.md; no terms of reference, attendance by Role, or date | PARTIAL |
| B-08 | Decision register | OM 5.6 | Decision Log, decisions/; the Sponsor's decisions are evidenced by the Lead's note, no approval channel | PARTIAL |
| B-09 | Risk register with method | OM 9.2; Policy 5; Catalog 7.1 | Risks and Issues; Severity only, no rating method or link to the Bank's enterprise risk register | PARTIAL |
| B-10 | Issue and incident register, with incident review and notification record | Policy 5.1 to 5.5 | One line in Risks and Issues; no review record | GAP |
| B-11 | Exception register | Policy 6.1; SoI 6.7 | Risks and Issues type Exception; no approver evidence or compensating control | PARTIAL |
| B-12 | Policy and document control, review cycle | Catalog 3, 4, 7; OM 7.3; SoI 13.3 | Change logs, Decision Log; author is approver; no review-due date, owner, or pass record | PARTIAL |
| B-13 | Training and competence records | SoI 10.1; Policy 2.1, 3.5; Charter 6.1(e) | None | GAP |
| B-14 | Budget and funding approval trace | Charter 4.1, 4.2 | Priorities (pointers, empty); Initiative Brief; no finance reference in a Decision | GAP |
| B-15 | Performance and KPI reporting to the board committee | Charter 7.1, 7.2; SoI 12; Quarterly Report Template | reports/ empty; Board Committee unnamed (RI-010); baselines blank | PARTIAL |
| B-16 | Third-party and vendor records | Policy 4.1; SoI 10.5 | AI Registry column only; the check itself has no form (Control Sign-Off is per Solution) | GAP |
| B-17 | AI inventory | Policy 2.1, 3.3; OM 9.2 | AI Registry (empty; due 90 days after 2026-10-01) | PARTIAL |
| B-18 | Segregation of duties evidence | OM 4.4; Policy 3.3; SoI 7.3 | Appointments (Checker); Control Sign-Off has no home; role combinations not reviewed | PARTIAL |
| B-19 | Access to the tools, and periodic access review | PLT-004, PLT-006 (AI Platform only) | None for Jira, Confluence, Service Management, or the repository | GAP |
| B-20 | Audit access and follow-up of findings | OM 4.4(f), 9.1; SoI 12.4; Catalog 7.1 | Risks and Issues type Finding; audit contact blank; access limited to Records | PARTIAL |
| B-21 | Record retention and integrity | OM 9.1; Catalog 1.3 | No retention schedule, integrity control, or "Jira is not evidence" rule; RI-005 open | GAP |
| B-22 | Evidence of validation, release, and acceptance | OM 6.6, 6.9; Policy 3.3, 3.4 | Solution Definition; Control Sign-Off (no home); acceptance only "noted in the backlog" | PARTIAL |
| B-23 | Key-person and continuity cover | OM 4.6 (deputy) | Appointments deputy column blank (RI-009) | PARTIAL |
| B-24 | HR: appointment instrument (who, by what authority, from when) | OM 4.6 | Appointments has no decision reference column | GAP |
| B-25 | HR: multiple Roles per person, time allocation, line-manager consent | OM 4.1 (several Roles allowed); Policy 7.1 (head's consent for acting) | Teams capacity blank | PARTIAL |
| B-26 | HR: approval of published AI output with record per edition | Policy 2.4; DR-014 | Held in SOL-001 (RI-015); no template | PARTIAL |
| B-27 | HR: role-based objectives tied to appraisal | None | None | GAP |
| B-28 | HR and data protection: personal data in Registry kept minimal and retained by schedule | Catalog 1.3 (no data of the Bank) | Appointments holds names | GAP |

## 4. Task C: Registry evidence templates

Principle: Jira and Confluence hold the work, its discussion, and its history while it is live. The Registry holds one dated, closed extract at each event, so an auditor can read it without the tools and after the tools change. The extract states what was decided, by whom, when, on which facts, and where the live item is (the Jira key or page). It copies no discussion.
Each Template keeps the current rules: no figures of the Bank, no data, no code. Records that today are hand-kept tables (backlogs, boards, Dependency Map, Dashboard, Teams, Calendar) become Working state; the Registry Snapshot (TPL-10) keeps their closed extract. Total: 11 Templates, 5 existing and 6 new.

| ID | Name | Status | Event that produces it | Audit and HR purpose | Key fields | Stays only in Jira or Confluence |
| --- | --- | --- | --- | --- | --- | --- |
| TPL-01 | Solution Definition | Keep; add an approvals table (Risk Tier assigned by and on; approved by and on; release by and on) | Solution defined; any approval or release | Scope, Risk Tier, release, and approval of each Solution | As now, plus the approvals table and Jira key | Drafts, comments, page versions |
| TPL-02 | Initiative Brief | Keep; change to "every Initiative"; decision and acceptance block points to TPL-06 and TPL-08 | Initiative business case | Business case and funding trace | As now, plus funding reference (system and number, no figure) | Working edits |
| TPL-03 | Control Sign-Off | Change and merge: covers validation, stop, provider check, and Exception | A Control Function validates, stops, checks a provider, or grants an Exception | Independent control; segregation of duties; third-party record | Type; subject (SOL or provider); Control Function and Contact; result; evidence reviewed (references); valid until; conditions; limits of use; compensating control and expiry for an Exception | Evidence files, test results, messages |
| TPL-04 | Steering Summary | Change: replaces Notes; variant for monthly and quarterly | Monthly and quarterly Steering | Committee minutes, advice, and decisions | See below | Agenda page, discussion, action tracking |
| TPL-05 | Quarterly Report | Keep; add an issuance block | PI Review and Demo; issue to the Board Committee | KPI reporting to the Board | As now, plus approved by, date issued, sent to, version, each figure's source and date | Working figures, drafts |
| TPL-06 | Decision Record | New; the Decision Log stays as the one-line index | A Decision at AICC Lead level or above, an activation, a delegation, a Group Arrangement, an Exception to an AICC requirement, a cutover | Decision register with evidence of the decision | See below | Discussion, approval workflow steps |
| TPL-07 | Assignment Map | New | Any appointment, acting designation, deputy, change, relief, or leaver; each PI close | Delegation, role profiles, appointments, joiners-movers-leavers, conflicts, access | See below | Tool permission groups and user accounts |
| TPL-08 | Delivery and Acceptance Extract | New; replaces "noted in the backlog" | IT Review and Demo (items); PI close (Epics, Solutions); Handoff | Evidence that a deliverable was delivered, checked, and accepted by the right person | See below | Acceptance criteria text, work items, comments, attachments |
| TPL-09 | AI Incident Review | New | Containment of an AI Incident; review within ten working days (Policy 5.5) | Incident register detail; notification decisions; lessons | RI id; Severity; dates (occurred, detected, reported, contained, reviewed); Solution; description without data; classified by; notification decisions of compliance and data protection, with reference; cause; actions, owners, dates | Ticket, logs, communications, attachments (restricted) |
| TPL-10 | Registry Snapshot | New | Close of each IT and each PI; cutover | State of the work at a date, since Jira is not evidence | Date; scope; source query; exported by; items by state and Stage; changes since the last snapshot, each with its Decision; reconciliation to the last snapshot; files exported (backlogs, boards, Dependencies, Dashboard measures) | Live items, history, sprints |
| TPL-11 | Proposal | New | An Experiment ends in a Proposal; the yearly strategy Proposal | Proposals and their decisions | Id; origin (SOL or strategy); what is proposed; evidence; options; recommendation; who decides; decision reference and date | Working material |

### 4.1 Steering Summary (TPL-04)

Fields: type (monthly or quarterly); date and week (for example 2026-PIQ4 IT10W4); chair; present and absent, by Role and name; inputs (Snapshot or Quarterly Report reference); matters considered (progress, risks, blockers, acceptances); advice given by each function, with any dissent; Decisions, each with its Decision Record and who decided; Risks, Exceptions, and AI Incidents reviewed (RI ids); conflicts declared (none, or by whom); actions (who, by when, Jira key); sample of the AICC Lead's Decisions reviewed (R-14); date approved by the chair.

### 4.2 Decision Record (TPL-06)

Fields: DR id; date; type; level (OM 5.3); decided by (Role and name); facts; options considered (one line each); decision; effect and scope (Entity, Domain, Solution); conflicts declared; advice taken (who); evidence of the decision (channel and reference, for example the Jira approval key or the signed message; the Sponsor's decisions must carry it); funding reference (system and number, no figure); revisit date; supersedes; status. An activation uses the same record, with the ten questions of Catalog 7.1 and the result (this is the Document Review Record of R-10).

### 4.3 Assignment Map (TPL-07)

One document with five parts. Part C is append-only; Parts A and B derive from it; each change makes a new dated copy in the Registry, and the history is the repository.

| Part | Content | Key fields |
| --- | --- | --- |
| A. Map (current) | Each Role and scope mapped to a person | Role; scope (Entity, Domain, Solution, or AICC); Holder (name, HR reference of the post, no other personal data); deputy; status (Appointed, Acting, Relieved); from; to; appointed by (Role); appointment reference |
| B. RACI | The charter's activities by Role: Responsible, Accountable, Consulted, Informed; one A for each activity | Activity; clause of the charter; one column per Role (7 Roles, plus the AI Steering Committee and internal audit); Holders resolve through Part A. The Role-only RACI itself belongs in the charter guide (Task D) and the Map only references it |
| C. Appointment log | One line for each event | Log id (AP-nnn); date entered; event (Appointed, Acting, Relieved, Changed, Deputy named, Confirmed, Left); Role; scope; person; previous Holder; effective from and to; decided by; Decision Record; role acceptance and conflict declaration received (date); tool access granted or removed (date and ticket) |
| D. Declarations and competence | Per Holder | Conflict-of-interest declaration (date, outcome, yearly); training required for the Role and date completed (Policy 2.1, 3.5); line-manager consent and time allocation (HR) |
| E. Tools and access | By Role, not by person | Jira, Confluence, Service Management, and repository permission group; date of the last access review; who reviewed it |

The Map absorbs the present Appointments Record (including the checker, heads of function, participating Entities, and the Sponsor's delegate) and the Teams Record (members and capacity).

### 4.4 Delivery and Acceptance Extract (TPL-08)

One file for each IT (items) and one for each PI (Epics, Solutions, Handoffs). A row for each item: item id (INI, SOL, EP, FT) and Jira key; title; deliverable and where it is (page or artifact, with version or date); acceptance criteria (summary or reference); result (Accepted, Returned, Cancelled); accepted by (Role and name) and date; evidence of the acceptance (Jira approval key or message reference); check or validation reference (Control Sign-Off id); release reference. The product owner is the one who accepts (OM 6.9); the AICC Lead enters it.

### 4.5 Disposition of the other present Records

| Present Record | Becomes |
| --- | --- |
| Decision Log | Stays: the index of Decision Records |
| Risks and Issues, AI Registry, Priorities, Standards | Stay as working tables; their closed state is in the Snapshot; each AI Incident also has TPL-09 |
| Notes (TPL-04) | Replaced by the Steering Summary; other events keep notes in Confluence |
| Appointments, Teams | Merged into the Assignment Map |
| Portfolio Backlog, Program Backlog, Boards, Dependency Map, Dashboard, Calendar, Roadmap | Working state (Jira after the cutover); extracts in the Snapshot |
| Reports | Quarterly Report, issued copies only |
| Assessments | Kept; each assessment is an evidence record of the Document Review (TPL-06 type) |

## 5. Task D: outline of the guides

Each guide states no rule (Catalog 5.3). Every chapter ends with "Rule source", a list of the clauses it explains, and its examples use Roles only. The portal publishes them from the charter.

### Guide 1: The agile workflows (SAFe and Kanban at AICC)

1. Intent and principles: why a SAFe-inspired lab with Kanban; the principles of OM 3.1; what AICC deliberately does not adopt; the one-person mode.
2. The model on one page: levels, backlogs, boards, loops, and Roles in one figure.
3. The levels: Strategic Priority, Initiative, Solution, Epic, Feature, Work Item; for each, its meaning, owner, backlog, entry, and exit.
4. States and Stages: the thirteen states, the transition table, the Stages of each level, Waiting and the flags; how a state maps to Jira.
5. From need to Solution: funnel, scoping, business case, Solution Definition, Risk Tier, Epics and Features.
6. Execution in a Program Increment: backlogs, IT Planning, definition of ready and done, Verify, Deploy, Release, acceptance, splitting a Feature.
7. After delivery: Service, Product, Experiment, Adopted Solution, and Handoff.
8. Cadence and events: day, week, IT, PI, and the IP week; for each event the intent, inputs, outputs, and the rules for moved or missed events; the dated calendar.
9. Flow control: Limits on Work in Progress, lanes and classes of service, Dependencies, flow measures.
10. Controls inside the flow: the Risk Tier, check or validation, release, and acceptance gates, and who decides each.
11. Running it in Jira, Confluence, and Service Management: issue types and levels, statuses, fields, boards, dashboards, approvals, and what is extracted to the Registry and when.
12. Playbooks: start an Initiative; define a Solution; run an IT; close a PI; handle an AI Incident; end an Experiment.
13. Quick reference: SAFe-to-AICC map, glossary extract, one-page cards for each event.

### Guide 2: The organization of AICC (the PMO body of knowledge)

1. Mandate and place in the Bank: mission, authority and limits, the three lines, relation to the Control Functions and internal audit.
2. Roles and responsibilities: the seven Roles, role profiles, the RACI, Hats, deputies, separation of duties and permitted Role combinations in a small unit.
3. Governance bodies: the Executive Sponsor, the AI Steering Committee, the Board Committee; purpose, membership, cadence, inputs and outputs, and how each records its work.
4. Decision rights and delegation: the Decision levels, escalation, delegation, conflicts of interest, the Decision Record.
5. Planning, funding, and portfolio: priorities, Envelopes, Guardrails, business cases, the Roadmap, the yearly wheel.
6. Risk, control, and assurance: Risk Tiers, validation, Exceptions, AI Incidents, provider checks, internal audit and supervisory interface.
7. Reporting: the Quarterly Report, the Board Committee report, Measures and Maturity Levels, and where each figure comes from.
8. Records and evidence: what Jira and Confluence hold, what the Registry holds, the Templates, naming, who keeps each, when, retention, integrity, and access.
9. People: appointments and the Assignment Map, joiners, movers, and leavers, competence and training, access to the tools.
10. Document control: the life of a document, activation, review, change log, translation.
11. Engaging a Domain: intake, first Solution, onboarding of the Domain Owner and Domain Expert.
12. Audit and HR reference: the matrix of Task B (expectation, rule, record), kept current, and the questions an auditor asks with the Record that answers each.

Appendices to both: the index of Templates with an example filled in; the change history of the guide; the contact of the keeper of each Record.

## 6. Recommended order of work

1. Decide R-01 and R-02 first; they set the shape of everything else.
2. Add the evidence Records and TPL-06, TPL-07, TPL-08, and TPL-10 (they close R-04, R-05, R-06, B-03, B-05, B-24).
3. Fill the Appointments (R-04), name the Board Committee, and set the Guardrails (RI-010, RI-012) so B-02 and B-14 close.
4. Add the one-person mode (R-17) before the first IT of the Program Increment runs in full.
5. Validate Task B with the Bank's internal audit and HR before it becomes a standard.
