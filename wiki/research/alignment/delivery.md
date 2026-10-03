# Site-to-corpus alignment: Delivery

Working record, 2026-10-03. Gap list between the 14 site pages of the Delivery section and the corpus. The corpus is normative; the site explains it. Site paths are under `portal/content/delivery/`. Proposed clauses use the corpus's own terms and avoid words it lists as "Not used" (WIP limit, capacity, sponsor, KPI, OKR).

Six decisions to take before redrafting:
- Who releases a Solution the AICC Lead built (C-02).
- Who states the value of an item (C-01); the SLM and the Operating Model disagree.
- How PI predictability is calculated (C-14): a count of objectives or a ratio of business value.
- Whether a Service can be handed over instead of only retired (C-10), and whether an Experiment can change type (C-07).
- What to call the seven Service steps and the six Experiment steps (C-08, C-09); not "states" or "Stages" without breaking Vocabulary 4.2/4.3.
- Whether the classes of service carry default targets (C-12), or targets stay with each Service Agreement.

## 1. New on the site, absent from the corpus

### 1.1 Solution Lifecycle Model

§3 Flow of value
- N-01 Tracker mapping: Initiative above Epic, Capability = Epic, Feature = issue, Work Item = sub-task (the-flow-of-value.md 1.1). Tool setup; belongs in Service delivery workflow §9 or Collaboration tooling.

§4 Backlogs and boards
- N-02 Definition of ready (backlogs-boards-and-kanbans.md 1.2). Proposed 4.2A: "A Feature is ready when it is Approved under 5.2: its acceptance criteria are stated and its Dependencies are known. This is its definition of ready."
- N-03 Definition of done (backlogs 1.2; quality-verification-and-release.md 2.4). Proposed 4.2B: "A Feature is done when it is tested (7.1), deployed with its change ticket and test reference entered (8.3), and accepted by the product owner (7.3(a))."
- N-04 Refinement keeps one to two Iterations of ready Features ahead (backlogs 1.2; events table; measures "Ready ahead"). Proposed 6.3 addition.
- N-05 "Two backlogs and four boards", with a "Read at" column (backlogs 2). Proposed: add a Program Board row and a "Read at" column to the 4.2 table.
- N-06 Limit reached: finish before start; Waiting item keeps its place and flag, days Waiting counted (backlogs 3.1). Proposed 4.2 addition.

§6 Cadence and loops
- N-07 Each event has one purpose, named participants, input, output, record; nothing else is held (events-and-rituals.md intro). Proposed 6.1A.
- N-08 Participants of each event (events table). Proposed: "Participants" column in the 6.1 table and in Cadence workflow §6.
- N-09 Retrospective ends with one or two improvements as Work Items or Features (events table, 3.1). Proposed 6.3 addition.
- N-10 Inputs: Iteration Planning takes the PI Objectives; PI Planning takes the mix of Initiatives, Dependencies, capacity (events table). Proposed: add to Cadence workflow §6 ("capacity" is T-04).
- N-11 Innovation: "pay down what the quarter left" (events table). Proposed 6.2 wording: "to learn, to try, and to pay down what the Program Increment left."
- N-12 Four habits (events 3.1). Proposed 2.2(h) extension: "Each demonstration shows working software against written acceptance criteria."
- N-13 Three loops of the work: exploration, build, release (the-loops-of-delivery.md 2.1, Fig. 4). Proposed 6.8.
- N-14 Integrate step; failure returns to the builder the same day (loops 2.1). Proposed 7.1A.
- N-15 Four feedback loops: demonstration, retrospective with Inspect and Adapt, live review, measures (loops 3.1, Fig. 5). Proposed 6.9.

§7 Verification, release, acceptance
- N-16 "A failing measure is a problem for Inspect and Adapt, not a reason to add a gate" (quality 2.4; measures-and-tracking 3.1 says "Retrospective"; the site contradicts itself). Proposed 10.1 addition.
- N-17 Security test against attacks on AI in validation (quality 2.1); in AI Policy 3.3 and the risk workflow §3 but not SLM 7.1/7.2. Proposed 7.2 cross-reference.
- N-18 The separations (roles-and-records.md 1.1). Proposed 7.5: "The person who builds does not test, check, or validate; the requester who accepts a Solution is not from AICC; the person who releases a Solution owns its results. The one accepted limit is that of 7.3(d)."

§8 Life-cycle management
- N-19 A Service the Bank should run at scale is handed to a platform team or IT function with a Proposal (life-cycle-management.md 3.1; life-of-a-service.md 3.1). Proposed 8.8; conflicts with the Service row (C-10).
- N-20 Seven steps in the life of a Service: Candidate, Admitted, Catalogued, Active, Improving, Transition planned, Migrating (life-of-a-service.md 1). Proposed 8.9 table as "service steps", not states (C-09, T-08).
- N-21 Catalogued gate: catalog entry, Service Agreement with response targets, Service Management route, first request served. Proposed 8.5 addition.
- N-22 Quarterly Steering reads the Services and decides on a transition (life-of-a-service 2.1). Proposed 8.4 addition; who decides is C-11.
- N-23 Same path for an Adopted Solution that returns to AICC for oversight (life-of-a-service 3.1). SLM 8.2 silent; add or delete as unclear.
- N-24 Experiment workflow, six steps: Define, Establish, Prepare data, Build, Validate, Decide (experiment-workflow.md 1). Proposed 8.10 table "Experiment steps" (C-08).
- N-25 Rules of the Lab (experiment-workflow.md 2.1–2.4). Proposed 8.11: (a) the Lab is an environment and holds no decision right; (b) read-only extracts under the classification of the Bank, named owner per source, no write-back; (c) personal data minimized and assessed with the Contact of data protection; (d) a cloud or external environment is a provider checked under AI Policy 4.1; (e) an Experiment ends at the close of its time-box; (f) guardrails kept as a scorecard with coverage, reviewed at the quarterly Steering as evidence of the Maturity Level.
- N-26 Build step guardrails (grounding, drift, bias, evaluation set); Validate step benchmark against the current way and its cost, correctness of data. Proposed in 8.10.
- N-27 Eight service operations practices (service-operations.md 1); corpus lacks problem management, knowledge, service level as a practice, service financial management. Proposed 8.5A.
- N-28 Meaning of each class of service: Urgent within the day; High priority within the Iteration week; Normal everything else (service-operations 2.1). Proposed 8.5B as defaults (C-12).
- N-29 Who sets the class: Solution Engineer triages, AICC Lead decides where in doubt. Proposed 8.5.
- N-30 Four service signals: service levels, incidents incl. AI Incidents, adoption, cost; read at each Iteration Review and Demo, carried into the Quarterly Report, feed the sunset rule (service-operations 3.1; measures-and-tracking 4.1). Proposed 8.4 addition.
- N-31 Service operations in light mode: one queue, one weekly session, classes as flags, practices as a checklist in the Solution Definition (service-operations 4.1). Proposed 6.6 addition; "flags" conflicts (C-13).
- N-32 Run-book template filled in the Service Agreement and Solution Definition (service-operations intro). Proposed 8.5C plus template change.

§9 Records
- N-33 Records the site lists that SLM 9.1 omits: PI Objectives with scores, change tickets and test references, AI Incident Reviews, live review notes. Proposed 9.1 addition.

§10 Measures
- N-34 Four families: flow, quality, health of what is live, value (measures-and-tracking intro). Proposed 10.1A.
- N-35 What each loop reads, Day to PI (measures-and-tracking 1): per-person limit; first-time pass, items by lane, Dependencies at risk; Completed to Accepted, override rate; throughput of the quarter, lead time, trends. Proposed 10.2A table.
- N-36 Conventions: calendar days; median and 85th percentile (measures-definitions 1.1). Proposed 10.1 addition.
- N-37 Formula, Source, Read at, Target rule for every measure (measures-definitions 2–5). Proposed: extend the 10.3 table.
- N-38 Measures named in 10.2 but undefined, which the site defines: Items by lane; Ready ahead; Items returned by reason; Defects after the check; Acceptance Checklist items not met; Completed to Accepted; Requests within target; Incidents (repeats as a share); Lead time of a change; Retirements complete; Features accepted against selected. Proposed: add to 10.3.
- N-39 Measures absent from the SLM: Expected lead time (WIP / throughput); Flow efficiency; Deployment frequency; Lead time for a change (deployed minus Active); Adoption; Run cost; Key results progress ((current − baseline)/(target − baseline)). Proposed: add to 10.3 by Decision Record.
- N-40 New target rules (measures-definitions): WIP item older than the 85th percentile of its column is raised; Urgent is rare; every Waiting item names its Dependency and owner; Completed to Accepted within the Iteration; override rate very high and very low are signals; run cost: sunset rule when it exceeds the benefit; PI predictability read as a band; steady gap in Features accepted against selected shows over-selection; key results two to four per Initiative (belongs in PMM 6.1). Proposed 10.3 Target rule column.
- N-41 Defects after the check feed the reassessment of the Risk Tier (measures-definitions 3). Proposed 10.3, cross-referenced to AI Policy 3.3.
- N-42 Measure governance: AICC Lead owns each definition; added or changed by a Decision at the monthly Steering; a measure not read for two quarters is removed (measures-definitions 6.1). Proposed 10.5.

### 1.2 Cadence workflow and guide
- N-43 Participants column, "one or two improvements" output, inputs of N-08/N-09/N-10 in Cadence workflow §6 (no "Who" column today).
- N-44 Light mode weekly session also handles requests and problems (service-operations 4.1). Cadence §9 row note.
- N-45 Quarterly Steering "Takes in" the four signals of each Service (life-of-a-service 2.1).

### 1.3 Service delivery workflow and guide
- N-46 Figure for the exploration, build, release loops in workflow §5.
- N-47 Guide §4 Decisions: transition of a Service to a receiving team; outcome of an Experiment; class of a request.
- N-48 Guide §6 Situations: "A Service should run at scale"; "An Experiment proves its case"; "Incidents or requests repeat".
- N-49 Six Experiment steps and seven Service steps in workflow §6, as Figure 7 detail.

### 1.4 Collaboration tooling
- N-50 Tracker mapping (N-01) in the Jira row.
- N-51 "the live portal of AICC will present them [the measures]" (measures-and-tracking 6.1); tooling says the AICC portal is static and gives progress to the Operating portal. State which portal presents the measures.
- N-52 The Lab environment (isolated workspace, access by role, logging) absent from the tools table.

### 1.5 AI risk and control workflow
- N-53 Lab data rules (N-25 (b)–(d)) missing from §8 Situations.
- N-54 "In operation" table (§4) has no trigger for defects after the check → Risk Tier reassessment (N-41).
- N-55 Lab guardrails scorecard as evidence for the Maturity Level (N-25(f)) absent from the corpus.

### 1.6 Templates
- N-56 Solution Definition §7: Service step and catalog entry reference; Service Agreement reference and response targets by class; light-mode practices checklist; known errors and user guide references; handover to a receiving team; signal columns in the live-review table; Experiment fields (hypothesis and leading indicators, environment record, data extracts, evaluation set, benchmark, Lab guardrails).
- N-57 Outcome Report: for an Experiment, results against leading indicators, benchmark against the current way and cost, correctness of the data, demonstration, decision; §4 median and 85th percentile.
- N-58 AI Incident Review: repeat-incident flag, problem-management Feature reference.
- N-59 Acceptance Checklist: "Items Not met: [count]"; for a Service, "Catalog entry and Service Management route ready".

## 2. Contradictions

- C-01 Who states the value. Site: "the AICC Lead ranks it, the Domain Owners state the value" (backlogs 1.1). SLM 3.5, 4.1: the product owner. The site matches the Operating Model roles table; the corpus disagrees with itself.
- C-02 Who releases a Solution the AICC Lead built. Site: "Executive Sponsor for Tier 3 or where the AICC Lead built it" (quality Fig. 1, 2.3; roles table). SLM 7.1 and risk workflow §8: the Executive Sponsor "where the AICC Lead is the Domain Owner".
- C-03 Business acceptance when the AICC Lead is the Domain Owner: the site lists the Executive Sponsor only for across Domains, enabling work, or an Experiment without a Domain (quality Fig. 1; loops 2.2). Workflows add "where the AICC Lead is the Domain Owner".
- C-04 Week length. Site: Monday to Friday (the-cadence.md). Calendar rule 1: Monday to Sunday.
- C-05 Done vs completed. Site: done when verified, deployed, accepted (backlogs 1.2). SLM 5.2: "To be completed: It is deployed"; Completed precedes Review and Accepted.
- C-06 Experiment outcomes. Site: promote, hand over, shelve. SLM 8.1: accepted with its lessons and closed, a Proposal, or rejected.
- C-07 Experiment changes type. Site: becomes a Product or a Service through the decision after the MVP, by the approver of the business case (experiment 2.3). SLM 8.1: one offering type; only Product → Service through a business case; the decision after the MVP is an Initiative decision (PMM 7.2).
- C-08 "Stages" of an Experiment. Site: six stages. Vocabulary 4.3: Trial, Proposal, Handover.
- C-09 "States" of a Service. Site: seven states incl. Active. Vocabulary 4.2: 13 states; SLM 5.1 the only source of the moves.
- C-10 End of a Service. Site: handed to a platform team or IT function. SLM 8.1 Service End: Retired or cancelled.
- C-11 Who decides a Service transition: the quarterly Steering (site 2.1) vs the Domain Owner / Executive Sponsor (site table, SLM 8.7).
- C-12 Targets by class. Site: Urgent within the day, High priority within the Iteration week. SLM 10.4 "[Set per class]"; SLM 8.5 and BM 4.2 put targets in the Service Agreement.
- C-13 Classes of service as flags (site, light mode) vs lanes (SLM 4.2, Vocabulary); SLM 6.6 light mode has only Waiting as a flag.
- C-14 PI predictability. Site: business value achieved / planned. SLM 10.3: share of PI Objectives achieved.
- C-15 Adoption. Site: users or cases served / intended, %. SLM 10.4 "Use": users each week, trend.
- C-16 False "Charter" status in measures-definitions: 85th-percentile age rule, Run cost, Key results with formula and "two to four", Waiting naming its "owner", "Urgent is rare"; Ready ahead "Charter, in part".
- C-17 Acceptance Checklist measure read at Release (site) vs Iteration Review and Demo (SLM 10.2).
- C-18 At-risk Dependency raised at once (site) vs to the monthly Steering (SLM 4.3).
- C-19 Quarterly Report timing: written after the quarterly Steering (site; Cadence guide §4) vs goes to it (Vocabulary; Cadence workflow §6). Corpus disagrees with itself.
- C-20 Who trains the first users: Domain Owner (site) vs AICC Lead sets the training (risk workflow §3; AI Policy 2.1, 3.5).
- C-21 Re-check of a significant change: overview Fig. 1 "significant changes re-checked" vs SLM 8.6 the AICC Lead decides.
- C-22 Order of acceptance in the release loop: site Fig. 4 omits the product owner's acceptance (SLM 7.3(a)).
- C-23 Daily Stand-up input: the Team board (site) vs the Iteration Backlog (Cadence §6).

## 3. Terms (Vocabulary)

T-01 definition of ready; T-02 definition of done; T-03 class of service (no meaning per class); T-04 capacity (Not used; site uses it); T-05 sponsor (Not used; site uses it); T-06 key results / OKR (corpus: Leading indicator; OKR Not used); T-07 Stage (six Experiment "stages", C-08); T-08 state (seven Service "states", C-09; Candidate, Admitted, Catalogued, Improving, Transition planned, Migrating undefined); T-09 Lab (corpus: AICC is "the internal consulting and innovation lab"; site: an environment); T-10 platform team; T-11 receiving team / owner vs Receiver; T-12 Iteration week; T-13 Knowledge base (corpus: Supporting knowledge folder); T-14 catalog / catalog entry; T-15 Lead time for a change vs Lead time of a change (different start points); T-16 first-time pass vs First-time-right rate; T-17 override rate vs Human override and correction rate; T-18 practice names (request handling, incident handling, problem management, change enablement, service level, service financial management, supplier management; Incident undefined apart from AI Incident); T-19 Lab records and guardrail terms (Experiment entry, environment record, data extract record, evaluation set, build notes, scorecard, failure protocol, promotion pathway); T-20 Loop stretched (exploration, build, release, feedback loops; continuous delivery pipeline); T-21 Adoption as a service signal; T-22 signal / four signals / health signals; T-23 Experiments (lower-case) vs the offering type; T-24 Week (Calendar Monday–Sunday vs site Monday–Friday); T-25 Roadmap: Vocabulary "the Record of the three months" vs SLM 4.4 "three horizons" (corpus fault); T-26 run-book, release on demand, integrate; T-27 business value and confidence scales (1–10, 1–5) exist only in `registry/pi/2026-PIQ4/objectives.md`.

## 4. Registry impact

- R-01 `registry/program-backlog.md` Features: dates Approved/Active/Completed/Deployed/Accepted; days Waiting and Dependency owner; change ticket and test reference; first-time pass at test and acceptance, returned with reason; Iteration selected. The "Business acceptor" column conflicts with acceptance by the product owner (SLM 7.3(a)).
- R-02 Capabilities table: Approved and Accepted dates.
- R-03 `registry/pi/2026-PIQ4/I10–I12.md`: "Selected at Iteration Planning", "Accepted first time", "Returned (reason)"; Retrospective improvements table; Iteration measures block.
- R-04 `objectives.md`: totals for business value planned/achieved and PI predictability % (depends on C-14).
- R-05 `ip-week.md`: Inspect and Adapt improvement items; PI measures block; Innovation outputs.
- R-06 `registry/board.md`: Limit rows per Domain (SLM 4.2 requires them; none exist); age of the oldest item per column; lanes → flags if C-13 adopted.
- R-07 `registry/dashboard.md`: median and P85 columns; rows for expected lead time, flow efficiency, deployment frequency, lead time for a change, items returned, defects after the check, Features accepted against selected, Ready ahead, PI predictability; a "Live Solutions" section (availability/service levels, incidents and repeats, time to restore, requests within target, adoption, override rate, run cost).
- R-08 `registry/dependencies.md`: "Needed by", "Met on", "Owner" columns.
- R-09 `registry/ai-registry.md`: Service step, catalog entry reference, Service Agreement reference, Lab environment reference, defects after the check, Receiver after transition.
- R-10 New: Experiment register (Lab).
- R-11 New: Lab guardrails scorecard.
- R-12 New or Solution Definition section: Service operations record (run-book) per Service.
- R-13 New: Service catalog in the Portfolio.
- R-14 New: Measures register (measure, definition, formula, source, read at, target rule, owner, status, Decision Log ref, last read).
- R-15 `registry/teams.md`: product owner and Domain Expert columns.
- R-16 Quarterly Report: four signals per Service, PI predictability, Lab scorecard, Service transitions decided.
- R-17 `registry/calendar.md`: no change unless C-04 goes the other way.

## Count

| Class | Items |
| --- | --- |
| New on the site (N-01–N-59) | 59: SLM 42, Cadence 3, Service delivery 4, Collaboration tooling 3, AI risk and control 3, Templates 4 |
| Contradictions (C-01–C-23) | 23 |
| Terms (T-01–T-27) | 27 |
| Registry impact (R-01–R-17) | 17: 9 existing records, 5 new records, 1 report, 1 teams record, 1 no change |
| Total | 126 |
