---
key: "governance"
label: "Governance and roles"
section: "Governance"
---

## Governance and roles {#governance-governance-and-roles}

This page shows the project's governance (who decides, who does the work, and how the work is controlled) as the AICC flows carry it. A reader used to a project charter will find each familiar element under its usual label, next to the AICC term. The page explains and does not commit anyone: the commitments are in the [Charter (Initiative Brief)](#charter) and the Service Agreement. The project uses the existing AICC events and records and adds none of its own.

### The AICC path, step by step {#governance-path}

The first column keeps the project's own steps. The other columns show where each step sits in the Portfolio Kanban and the Solution Lifecycle Model, who decides it, the record it leaves, and the event where it happens. While AICC runs in light mode, the monthly Steering is held within the Iteration Review and Demo.

| Project step | AICC step | Decided by | Record | Event |
| --- | --- | --- | --- | --- |
| Idea and journey shortlist | Funnel (Proposed) | The AICC Lead takes it in, defers it, or rejects it | Portfolio Backlog entry; Decision Log line | Weekly Review |
| Journey selection, ownership, baseline from existing figures | Reviewing (Discovery: Scoping), then Analyzing (Discovery: Business case) | The AICC Lead with the Domain Owner | Initiative Brief and journey annex; Service Agreement for the study phase | Weekly Review; Service Agreement check-in at each Iteration |
| Charter approval | Approval of the business case, after clearance by the Control Function Contacts | Domain Owner; each Contact clears within its remit | Initiative Brief; Control Sign-Offs; Decision Record; Service Agreement amended | Monthly Steering |
| Mobilization | Ranked in the Portfolio Backlog and pulled into the MVP | AICC Lead | Portfolio Backlog rank; Decision Log line | Monthly Steering; PI Planning |
| Historical validation (reconstruct past cases, check accuracy) | Phase 1 of the MVP: an Experiment in the Lab on read-only extracts, ending in an Outcome Report | The AICC Lead runs it, and the Domain Owner reviews it. While the AICC Lead builds, the Executive Sponsor approves the Solution Definition, assigns the Risk Tier, and approves the use of the data class | Solution Definition (Experiment); AI Registry entry; Outcome Report | Iteration Planning; Iteration Review and Demo |
| Readiness for live use | Validation by the Control Function Contacts, the Team's final acceptance, and the Bank's change management | The Contacts; the AICC Lead; change management | Control Sign-Offs; release block (Team final acceptance, change ticket, test reference); [IT readiness checklist](#it-readiness) | Iteration Review and Demo; monthly Steering |
| Controlled live use by one team | Phase 2 of the MVP: the first Solution, a Service run by AICC with a sunset rule, deployed to its first users | The Domain Owner reviews live use and gives the business acceptance | Solution Definition (Service); release block (business acceptance) | Iteration Review and Demo |
| Pilot acceptance and the scale decision | Decision after the MVP: continue, pivot, defer, or reject, or return with a stated extension | Domain Owner | Decision Record; Decision Log; Brief section 6 | Monthly or quarterly Steering |
| Scale and continuing ownership | Release beyond the first users with the Acceptance Checklist, or a Proposal and a Handover to an IT function as Receiver | The Domain Owner releases; the Domain Owner and the Executive Sponsor decide the Proposal; the Receiver accepts the Handover | Acceptance Checklist; Proposal; Decision Record; Handover row of the Solution Definition | Quarterly Steering |

The item can leave the path at any step. It is Deferred with a reason and a date, or Rejected on the merits. It is Cancelled for an error, a duplicate, or a stop by a Control Function. While a named Dependency outside AICC blocks it, it is Waiting. Either side may end or redirect the Engagement at the end of an Iteration. Once live, the AICC Lead or any Control Function Contact may suspend the Solution. [How the pilot works](#how-it-works) shows the stages of exposure in more detail.

### Role map {#governance-role-map}

| Project label | AICC Role or record | What changes |
| --- | --- | --- |
| Business sponsor, Sponsor, Service Owner, Benefit Owner | Domain Owner: the Head of Customer Service | One Role in place of four labels. The Domain Owner approves the business case, the Solution Definition, and the use of the data class (the Executive Sponsor approves the last two while the AICC Lead builds). The Domain Owner also accepts, releases, decides after the MVP, and confirms the benefit. "Sponsor" alone is no longer used, because Executive Sponsor is a separate AICC Role |
| (none) | Executive Sponsor | Decides only where the corpus requires it: while the AICC Lead builds, as above; when a guardrail is exceeded; for the Investment Envelope; and on a Proposal |
| Journey Process Owner, co-sponsor | The process-function head (Bank role), owner of a Dependency | Approves the action list, the outcome definitions, and the interpretation of past cases. These approvals become acceptance criteria in the Solution Definition. Supplies Domain Experts, whom the Domain Owner names. Becomes a second Domain Owner only if the function claims part of the benefit |
| Project coordination | AICC Lead; day-to-day coordination may be a Hat | The AICC Lead is accountable for the Initiative, the Brief (with the Domain Owner), the Service Agreement, and the records. A member of the AICC team, for example a partner from Customer Service, may wear the coordination Hat, named in Part B of the Service Agreement. A Hat decides nothing |
| Technology/Data Delivery Lead, AI and data engineers | Solution Engineer (the AICC Lead, while AICC has one member) | Designs, builds, deploys, and runs the Solution. Takes no part in testing, validation, or business acceptance of what they built |
| Service Quality and Measurement Lead, Measurement Owner | The source owner of the figures (Bank role), plus a tester named by the AICC Lead | The source owner provides the baselines and the figures that the decision after the MVP rests on, and holds no approval. Testing is done by an engineer of the IT function or the Domain who did not build the work |
| Service Operations Manager | Bank role; usually also a Domain Expert | Runs the team that is the first users, delivers training, and keeps the manual route open. May switch the team to the manual route at any time and tells the AICC Lead the same day. Has no power to suspend the Solution |
| Required control approvals (privacy, security, conduct, compliance, risk) | Control Function Contacts: model risk, information security, data protection, compliance, legal | All five are required, both at clearance and at validation. Conduct and, for Onboarding/KYC, financial crime are part of compliance. Each decides within its remit, and its decision is final for that remit |
| Technology leadership, enterprise architecture, platform teams | Platform Owner, named by the head of technology | Provides the AI Platform: in-Bank model hosting, the AI gateway, logging, and monitoring. Promoting pilot components to the AI Platform is a Proposal, not a separate decision |
| IT operations and service management | IT function: a Dependency now, and the Receiver at Handover | Signs its items of the Acceptance Checklist at release |

### Who does what (RACI) {#governance-raci}

The matrix uses the AICC Roles and three Bank roles. It follows section 4 of the Organization guide. R does the work. A answers for the activity and decides it, and each row has one A. C is consulted before, and I is informed after. While AICC has one member, the AICC Lead is also the Solution Engineer, and the rules of separation then apply to that person: no builder appears as R or A on testing, validation, or acceptance.

| Activity | Domain Owner | Executive Sponsor | AICC Lead | Solution Engineer | Domain Expert | Control Function Contacts | Platform Owner | Process-function head | Service Operations Manager | Source owner of the figures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Take the idea in and scope it, selecting the journey | C | I | A |  | C |  |  | C |  | C |
| Complete the Initiative Brief, with baseline references | A |  | R |  | C | C |  | C |  | R |
| Clear the business case, each within its remit | I |  | R |  |  | A |  |  |  |  |
| Approve the business case | A | C | R |  | C | C |  | C |  |  |
| Rank and pull the Initiative into the MVP | C | I | A |  |  |  |  |  |  |  |
| Approve the action list and outcome definitions, and label past cases into the Evaluation set | C |  | C | I | R |  |  | A | C |  |
| Approve the Solution Definition (Experiment, then Service), the Risk Tier, and the use of the data class | C ¹ | A ¹ | C | R | C | C |  | C |  |  |
| Design and build the assistant, with each Feature tested by a person other than its builder | C |  | I | A | R | C | C |  |  |  |
| Validate the Solution (Tier 2), including the provider check | I |  | C | C |  | A | C |  |  |  |
| Give the Team's final acceptance, then deploy through the Bank's change management | I |  | A | R |  |  | C |  |  |  |
| Train the first users and run the team, with the manual route open | A |  | C |  | R |  |  |  | R |  |
| Review live use and the monitoring at each Iteration Review and Demo | A |  | I | R |  |  | C |  | C |  |
| Suspend the Solution (a Contact may also suspend within its remit) | I | I | A | R |  | C |  |  | C |  |
| Give the business acceptance of the Solution with its first users | A |  | C |  | C |  |  | C | C |  |
| Decide after the MVP | A | I | R | C | C |  |  | C |  | R |
| Release beyond the first users, with the Acceptance Checklist | A |  | R | R |  | R | R |  |  |  |

¹ While the AICC Lead builds, the Executive Sponsor approves the Solution Definition and the use of the data class and assigns the Risk Tier. When someone else builds, the Domain Owner approves the Solution Definition and the use of the data class, and the AICC Lead assigns the Risk Tier.

### Workstreams {#governance-workstreams}

AICC has no workstream level: the work is the Features of the Experiment and then of the Service, in the one Program Backlog. The four project workstreams remain as a view. Each Feature carries its workstream as a label, and Part B of the Service Agreement names who works on each.

| Workstream | Who supplies or accepts | Artifacts, delivered as Features |
| --- | --- | --- |
| Customer journey and process | Process-function head (approves); Domain Experts (supply) | Current and target process map, action list, exception map, outcome definitions |
| Data and intelligence | Solution Engineer (builds); a tester who did not build | Source map, data contract, context assembly, assistant, quality report; the Evaluation set, labeled by the Domain Experts |
| Service experience and adoption | Domain Owner and Domain Experts; the Service Operations Manager runs the team | Workspace, role guidance, training, support and fallback runbook |
| Controls and measurement | Control Function Contacts (validation); source owner of the figures (measurement) | Measurement annex, metric definitions, Control Sign-Offs, monitoring view, Outcome Report |

### Governance forum and reporting {#governance-events}

The project has no forum of its own. Its decisions and reviews happen at the AICC events, and the process-function head and the Service Operations Manager are invited to the Iteration Review and Demo.

| Event | What this project brings |
| --- | --- |
| Weekly Planning and Weekly Review (one session in light mode) | Progress, open Dependencies, and items Waiting on a Dependency; the Dashboard |
| Service Agreement check-in, at each Iteration, with the Domain Owner and the Domain Expert | Changes of scope within the intent, the Assumptions, and the availability of the business team |
| Iteration Planning | The Features of the month, with their acceptance criteria and Dependencies |
| Iteration Review and Demo | Acceptance of Features; progress against the leading indicators; once live, the Domain Owner's review of the monitoring and the alert levels |
| Monthly Steering | Gate decisions that are due (approval of the business case, the decision after the MVP), the Investment Envelope, the month's control events (Risk Tier, validation, deployment, suspension, AI Incident), and Dependencies at risk |
| PI Planning | The Program Board and the Milestones; the Domain Owner scores the business value of the PI Objective |
| Quarterly Steering | Whether to continue the Active Initiative, the Proposal, the review of Adopted Solutions, and the benefit in the Quarterly Report |

Reporting runs from the Weekly Review to the Dashboard, the Steering Summary, and the Quarterly Report. A matter is escalated only on the conditions of Operating Model 5.2: it affects another Domain or reaches outside the Bank, is hard to reverse, exceeds a guardrail, or carries risk beyond the AI Risk Appetite Statement. A disagreement with a Control Function goes to the head of that function. Part B of the Service Agreement names who escalates to whom.

### Where the project records live {#governance-records}

| Familiar record | Where it lives in AICC |
| --- | --- |
| Risk, assumption, issue, and dependency log | Four existing records, each referenced by identifier from section 5 of the Brief. Risks and issues go in the Risks and Issues Record (RI-[nnn], with owner, severity, and due date); assumptions in the Service Agreement; dependencies on the Program Board (DEP-[nnn], with owner, Iteration needed, and status); decisions in the Decision Log |
| Decision log | The Decision Log: one line for each decision at the AICC Lead's level or above, and for any decision others will need to find. Approval of the business case and the decision after the MVP also get a Decision Record. A Team decision is noted in the work item. A Control Function's interpretation is a Control Sign-Off |
| Change control | Before approval, the Brief is edited directly. After approval, a change in scope is an amendment of the Brief with a Decision Record, and reordering within the intent goes in the Changes table of the Service Agreement. A change of model, provider, data class, autonomy, or any Risk Tier attribute of the Solution is a significant change: the AICC Lead decides whether a new validation is needed and records it in the Decision Log, and the Domain Owner releases it. Adding users beyond the first users is a release decision |
| Project plan and backlog | The Program Backlog, with the Program Board and the Roadmap Milestones for the gates |
| Approval evidence | Control Sign-Offs, the AI Registry entry, the release block of the Solution Definition, and the Acceptance Checklist |
| The Bank's project intake form | The Initiative Brief and the Service Agreement. If the Bank's own intake must also run, it is one Dependency on the IT function |
| Readiness gates A, D, C, O, and Q | Evidence that the AICC deciders read, listed step by step in the [IT readiness checklist](#it-readiness). They are not approvals of their own |

### Coordination checklist {#governance-coordination-checklist}

The initiation duties of project coordination, and the record or gate that carries each. The AICC Lead answers for them; the coordination Hat may do the work.

| Duty | Carried by |
| --- | --- |
| Record the journey, team, scope, exclusions, and owners | Brief header and section 3; the journey annex; the Appointments Record for names |
| Set the baseline, metric definitions, evidence sizes, and sources | Brief section 2 and the [measurement annex](#charter-annex) |
| Give each control limit a source, owner, tolerance, review frequency, and alert level before live use | Conditions of use and alert levels in the Solution Definition (see [Controls and evidence](#controls)) |
| Confirm the participants and their capacity | Part B of the Service Agreement, and its Assumptions |
| Turn the plan into an integrated plan and a dependency map | Program Backlog, Program Board, and Roadmap Milestones |
| Keep the backlog, logs, change control, and approval evidence | The records in the table above |
| Set up the forum, reporting path, escalation route, and cadence | The AICC events and reporting path above |
| Coordinate readiness of past cases, employees, controls, and live use; training, fallback, support, and monitoring before live use | IT readiness checklist; Control Sign-Offs; release block; training noted in the AI Registry |
| Prepare the evidence and recommendation for the next step | The facts in the Decision Record for the decision after the MVP; the Outcome Report |
| Confirm continuing ownership | The Receiver named in the Solution Definition before it is approved; the Proposal and the Handover |

### After the pilot {#governance-after-the-pilot}

| What the pilot leaves | Continuing owner |
| --- | --- |
| The service-resolution workflow and the customer outcome | Domain Owner |
| Action list, journey interpretation, and the backlog of upstream process improvements | Process-function head, recorded as owner of the knowledge source in the AI Registry |
| Source data and interfaces | The existing owners of the source systems |
| The assistant and the workspace | AICC while it runs as a Service; after a Proposal and a Handover, the Receiver, an IT function of the Bank |
| Evaluation set and quality thresholds | Kept with the Domain: Domain Experts and the process function |
| Daily operation of the team, guidance, and fallback | Service Operations Manager |
| Monitoring of the live Solution | Domain Owner (live review); Platform Owner (logs); Control Function Contacts (reassessment) |

The reusable components are the interaction timeline, the model of states and blockers, the workspace pattern, retrieval of approved knowledge, the correction and outcome feedback, and the audit path. They are described in a Package Definition, and the evaluation sets come with them. Customer data does not. Another journey enters the Funnel as a new need, where the catalog check finds the Package.
