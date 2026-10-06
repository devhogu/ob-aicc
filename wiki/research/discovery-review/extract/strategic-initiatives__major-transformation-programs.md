# 

source: html-alt/financial-services/en/strategic-initiatives/major-transformation-programs/index.html


[PAGE TEXT]
Program design
Structural design of the program — defining scope, workstream decomposition, interdependencies with other programs and BAU operations, resource requirements, and the governance model (steering committee, working groups, escalation paths). Program design quality determines the accuracy of the business case and the risk of scope drift. Under NBKR and CBR operational risk frameworks, material transformation programs require documented design prior to board approval.
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|M] Program Scope & Dependency Map
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/program-design/program-scope-dependency-map
intent: Agent reads active program charters, technology architecture documents, and the NBKR and CBR regulatory milestone calendar, producing a scope map with cross-program dependency flags, shared-resource conflicts, and regulatory milestone alignment assessment for ExCo review. Scope conflicts and dependency risks are identified before program design is approved, at a stage when remediation is comparatively inexpensive. The map is refreshed each time a program charter or architecture document is updated.
Problem to solve: Program scope design is assembled by the PMO and functional leads from program briefs, architecture documents, and stakeholder interviews. Cross-program dependencies — programs sharing a core platform, a specialist team, or a regulatory milestone — are identified manually and incompletely. Scope conflicts typically surface during delivery, when remediation requires a scope change, additional funding, and a re-baseline of commitments to the board.
Solution: Agent reads active program charters, technology architecture documents, and the NBKR and CBR regulatory milestone calendar. It produces a scope map with cross-program dependency flags, shared-resource conflicts, and regulatory milestone alignment across all active programs. ExCo reviews the dependency map before approving program design and investment allocation; structural conflicts are resolved at design stage.
OKR objective: A scope map with cross-program dependency flags, shared-resource conflicts, and regulatory milestone alignment — produced by agent from active program charters, technology architecture documents, and the NBKR and CBR regulatory milestone calendar — is available for ExCo review before program design is approved, when remediation is comparatively inexpensive.
OKR KR [Adoption]: Agent produces and refreshes scope dependency maps for ≥95% of active programs within 5 business days of each charter or architecture document update; NBKR and CBR regulatory milestone alignment included in ≥100% of applicable jurisdictional maps.
OKR KR [Acceptance]: ≥80% of agent-identified scope conflicts and dependency risks confirmed as requiring resolution by ExCo; scope conflicts resolved at design stage (versus delivery stage) rate ≥2x the prior-year baseline.
OKR KR [Cycle]: Cross-program scope conflict identification lag reduced from delivery-stage discovery to design-stage review, providing ≥8 weeks of earlier intervention per conflict.

### CARD 2 [Automation|M] Program Design Scope Change Control Brief
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/program-design/program-design-scope-change-control
intent: Agent reads all scope change requests submitted against the program, cross-references each against the original workstream decomposition and dependency map, and produces a structured impact brief covering schedule impact, cost-to-complete revision, and interdependency ripple effects. The program director and steering committee review the impact brief before approving any scope change; scope drift is tracked cumulatively against the original program design.
Problem to solve: Scope change requests are reviewed individually for merit; their cumulative impact on the program's original design assumptions — schedule, budget, and workstream interdependencies — is not modeled at the time of each approval. Scope drift accumulates across individually reasonable approvals until the program's original business case assumptions are materially compromised. The point at which cumulative scope changes invalidate the business case is identified late.
Solution: Agent reads each scope change request alongside the accumulated change history and the original program design. It produces an impact brief showing the individual and cumulative effect on schedule, cost-to-complete, and dependency chains. The program director reviews the brief before each steering committee approval; cumulative drift is visible as a running metric.
OKR objective: Scope change approval decisions are made with a cumulative impact assessment, not only a review of the individual request.
OKR KR [Adoption]: Agent scope change impact briefs produced for ≥90% of change requests across ≥3 active programs within 12 months of go-live.
OKR KR [Acceptance]: ≥80% of impact briefs confirmed as accurate by the program director after committee review.
OKR KR [Cycle]: Programs that breach the cumulative scope drift threshold before board re-approval is triggered reduced by ≥50% vs baseline.

### CARD 3 [Enablement|M] Program Design Resource Demand Forecast
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/program-design/program-design-resource-demand-forecast
intent: Agent reads the program workstream decomposition, milestone sequence, and skill-type requirements for each work package, and produces a rolling resource demand forecast by skill type across the program horizon. The program director and HR use the forecast to plan recruitment, contractor sourcing, and cross-program allocation before demand peaks arrive, rather than responding to resource gaps at execution.
Problem to solve: Program resource demand is estimated at business case stage as a total headcount and cost envelope. Within the program, resource demand peaks by skill type — integration architects, test leads, change management specialists — occur at specific points in the delivery schedule. These peaks are not forecast systematically; resource gaps emerge at execution and are filled by expensive emergency sourcing or by pulling resources from other programs.
Solution: Agent reads the workstream decomposition, milestone sequence, and skill-type annotations for each work package. It produces a rolling resource demand forecast by skill type across the program horizon, updated as milestones are completed or revised. The program director and HR use the forecast to plan sourcing with lead time.
OKR objective: Program resource demand peaks by skill type are forecast with sufficient lead time for planned sourcing rather than emergency sourcing.
OKR KR [Adoption]: Agent resource demand forecasts consumed by program directors and HR for ≥3 active programs within 12 months of go-live.
OKR KR [Acceptance]: ≥75% of forecast demand peaks confirmed as accurate within 20% by execution; emergency sourcing events reduced by ≥40%.
OKR KR [Cycle]: Average cost premium for emergency vs planned sourcing for transformation skill types reduced by ≥30% vs baseline.

[PAGE TEXT]
Milestone & dependency tracking
Real-time monitoring of program milestone completion against the delivery schedule, with dependency-aware impact assessment when milestones slip. Cross-program dependencies mean that a delay in one program can trigger cascading slippage across the portfolio. Program managers track milestones in separate tools; the consolidated cross-program view is assembled manually by the PMO and delivered to the ExCo monthly — after slippage has compounded.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] Milestone External Dependency Watch
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/milestone-dependency-tracking/milestone-external-dependency-watch
intent: Agent monitors third-party vendor delivery statuses, NBKR and CBR regulatory approval calendars, and inter-program dependency milestones, and produces a weekly external dependency watch briefing the PMO on any signal that a dependency is at risk before the contractual or agreed deadline. The PMO escalates and initiates contingency planning before the at-risk dependency affects the program critical path.
Problem to solve: External dependencies — vendor deliveries, regulatory approval timelines, and other program completion milestones that this program depends on — are monitored by individual workstream leads who report into the PMO monthly. By the time the PMO learns that an external dependency is at risk, it has already affected the program schedule. Contingency planning begins after the impact has occurred.
Solution: Agent monitors vendor contract milestones, regulatory approval calendar signals, and inter-program dependency trackers. It produces a weekly watch brief flagging any external dependency showing an at-risk signal — delayed vendor delivery confirmation, regulatory calendar slippage, or peer-program milestone revision. The PMO reviews and initiates contingency planning with lead time.
OKR objective: External program dependencies at risk are identified before they affect the program critical path.
OKR KR [Adoption]: Agent external dependency watch brief produced weekly for ≥90% of reporting cycles across ≥3 active programs within 12 months of go-live.
OKR KR [Acceptance]: ≥80% of at-risk dependency flags confirmed as materialising or requiring contingency planning by the PMO.
OKR KR [Cycle]: Schedule impacts from external dependency failures reduced by ≥35% vs baseline for programs with agent monitoring active.

### CARD 5 [Optimize|M] Milestone Slippage Early-Warning Alert
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/milestone-dependency-tracking/milestone-slippage-alert
intent: Agent reads milestone completion data across all active programs, models dependency propagation, and generates weekly slippage alerts ranked by cascade severity for PMO review. Intervention is initiated at the point when re-planning options are still open — ahead of the monthly steering committee cycle. Cross-program cascade effects are surfaced proactively rather than reconstructed after the compounding has begun.
Problem to solve: Milestone slippage is identified at the monthly program status review, by which time cross-program dependency disruption has already begun compounding. Cascade propagation — one program's delay triggering shared-resource conflicts or sequenced milestone failures across other programs — is reconstructed by the PMO after the fact. The low-cost re-planning window has typically already closed by the time the steering committee receives the picture.
Solution: Agent reads milestone completion data from the program tracker, models dependency propagation across all active programs, and generates weekly slippage alerts ranked by cascade severity. PMO reviews the alerts and initiates re-planning. The re-planning window opens ahead of the steering committee cycle rather than in response to it; cascade exposure is identified while corrective options remain available.
OKR objective: Weekly milestone slippage alerts — ranked by cascade severity across all active programs — are produced by agent from program-tracker data and dependency propagation modeling, giving the PMO a re-planning window before the monthly steering committee cycle rather than after cascade compounding has begun.
OKR KR [Adoption]: Agent produces weekly slippage alerts for ≥90% of active program portfolios for ≥48 consecutive weeks per year; cascade severity ranking and cross-program dependency propagation analysis included in ≥95% of weekly outputs.
OKR KR [Acceptance]: ≥80% of agent-surfaced high-severity cascade alerts confirmed as requiring intervention by the PMO; cascade exposure identification rate at the re-planning window ≥2x the rate identified reactively in the prior year.
OKR KR [Cycle]: Cascade slippage identification lag reduced from monthly steering committee review (post-compounding) to a weekly signal available ≥3 weeks before the steering committee cycle.

### CARD 6 [Insights|M] Milestone Critical Path Brief
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/milestone-dependency-tracking/milestone-critical-path-brief
intent: Agent reads the full program milestone schedule and dependency map and produces a weekly critical path brief identifying which current milestones sit on the critical path to the program's regulatory or commercial go-live deadline, what the float is for near-critical milestones, and which external dependencies — regulatory approvals, vendor deliveries, third-party integrations — represent the highest schedule risk. Program directors concentrate oversight on critical-path items rather than distributing attention equally across all milestones.
Problem to solve: Program milestone tracking covers all milestones equally; the PMO and steering committee do not have a dynamically maintained view of which milestones are on the critical path to the program deadline and how much float remains for near-critical tasks. Resources and senior attention are distributed by workstream seniority rather than by criticality, resulting in critical-path slippage going unaddressed while non-critical workstreams receive disproportionate attention.
Solution: Agent reads the milestone schedule and dependency map and computes the current critical path and float for each milestone. It produces a weekly brief identifying critical-path milestones, near-critical items with float below a defined threshold, and external dependencies with schedule risk. Program directors review and reallocate senior attention and resources accordingly.
OKR objective: Program oversight is concentrated on critical-path milestones rather than distributed equally across workstreams.
OKR KR [Adoption]: Agent critical path briefs consumed by program directors for ≥90% of reporting cycles across ≥3 programs within 12 months of go-live.
OKR KR [Acceptance]: ≥85% of critical path identifications confirmed as accurate by program directors and PMO.
OKR KR [Cycle]: Critical-path milestone slip rate reduced by ≥25% vs baseline for programs in scope.

[PAGE TEXT]
Business case & funding
Financial justification for the program investment — covering cost estimates by workstream, benefit realization schedule (cost savings, revenue uplift, regulatory compliance cost avoidance), risk adjustment, NPV/IRR analysis, and capital allocation implications. Board approval of major programs requires a business case that passes the CFO and risk function review. Benefit realization assumptions must be defensible under ExCo scrutiny and traceable back to the delivery workstreams that will generate them.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|M] Business Case Narrative Drafting
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/business-case-funding/business-case-narrative-drafting
intent: Agent reads program cost estimates, benefit realization schedules, risk register, and financial model outputs and generates the board-approval business case narrative in the prescribed format — financial summary, benefit attribution by workstream, risk-adjustment rationale, and board-action items. Finance and the program director edit the generated narrative for forward judgment and board-specific framing. The drafting bottleneck is removed from the approval cycle, allowing a higher throughput of programs to reach the board.
Problem to solve: Program business case narratives are drafted from scratch by senior program directors and finance business partners. Collating cost estimates, benefit schedules, risk assessments, and financial model outputs into a board-ready document requires multiple review cycles to achieve cross-section consistency, limiting how many programs can reach the board in each approval cycle. Inconsistencies between the financial model, risk adjustment, and benefit attribution sections are identified during the board review rather than before.
Solution: Agent reads cost estimates, benefit realization schedules, risk register, and financial model outputs. It generates the business case narrative in the board-approval format with a financial summary, benefit attribution by workstream, risk-adjustment rationale, and board-action items — with cross-section consistency maintained. Finance and the program director review the generated narrative, apply forward judgment, and refine for the board's framing preferences.
OKR objective: Board-approval business case narratives — financial summary, benefit attribution by workstream, risk-adjustment rationale, and board-action items — are produced by agent from validated program inputs with cross-section consistency maintained, giving finance and program directors an editing task rather than a drafting task.
OKR KR [Adoption]: Agent produces draft business case narratives for ≥95% of programs entering the board approval queue; all four required sections populated in each draft.
OKR KR [Acceptance]: ≥80% of agent-produced narratives accepted by finance and program directors as structurally complete without full redraft; cross-section consistency errors reaching board review reduced to ≤5% of submitted documents.
OKR KR [Cycle]: Per-program business case narrative production time reduced by ≥60% because drafting is replaced by structured editing.

### CARD 8 [Insights|M] Business Case Assumption Benchmarking Brief
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/business-case-funding/business-case-assumption-benchmarking
intent: Agent reads each submitted program business case and benchmarks its key assumptions — cost of capital, benefit realization timeline, cost-to-complete by workstream type, and risk adjustment — against comparable completed programs in the bank's institutional record and industry benchmarks for equivalent transformation types. The CFO and Strategy team receive a benchmarking brief before ExCo review, identifying where assumptions diverge materially from precedent and require sponsor justification.
Problem to solve: Business case assumptions are challenged qualitatively by the CFO and strategy function in ExCo review. Without a systematic benchmark against comparable programs, aggressive assumptions on benefit realization timelines or cost-to-complete optimism pass without challenge because the reviewer lacks a reference point. Programs with the most optimistic assumptions are approved; they subsequently underdeliver against business case and require re-funding or scope reduction.
Solution: Agent reads each submitted business case and compares key assumptions against the bank's completed program record and available industry benchmarks for comparable transformation types. It produces a benchmarking brief identifying which assumptions diverge materially from precedent, the magnitude of deviation, and comparable program outcomes where available. The CFO reviews the brief before ExCo challenge.
OKR objective: Business case assumption challenges at ExCo are anchored to quantified benchmarks rather than qualitative judgment.
OKR KR [Adoption]: Agent benchmarking briefs produced for ≥90% of business case submissions in ≥2 consecutive annual planning cycles within 18 months.
OKR KR [Acceptance]: ≥75% of material assumption deviations flagged by the agent confirmed as requiring justification by the CFO.
OKR KR [Cycle]: Business case resubmission rate due to assumption quality concerns reduced by ≥30% vs baseline in cycles after go-live.

### CARD 9 [Enablement|M] Business Case Funding Decision Brief
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/business-case-funding/business-case-funding-decision-brief
intent: Agent reads the submitted business case, the benchmarking brief, and the ExCo challenge session notes to produce a funding decision brief that synthesises the investment case, the risk-adjusted scenario range, and the conditions precedent recommended before the next funding tranche is released. The CFO and ExCo use the brief to record a structured funding decision with explicit conditions; funding approvals carry accountability markers rather than open commitments.
Problem to solve: Program funding decisions at ExCo are recorded as approvals or deferrals without a structured narrative of the conditions under which the approval was granted. Conditions precedent discussed in the session — assumptions that must be validated before the next tranche, governance requirements, or scope confirmations — are captured informally in minutes rather than as binding conditions attached to the funding commitment. Programs draw on approved funding envelopes even when the conditions discussed in approval have not been met.
Solution: Agent reads the business case, benchmarking brief, and challenge session notes and produces a funding decision brief with the approved investment case, risk-adjusted scenario range, and explicit conditions precedent for each subsequent tranche. The CFO and ExCo sign off on the conditions brief; conditions are tracked against each funding draw-down.
OKR objective: Program funding approvals carry explicit, tracked conditions precedent rather than open commitments.
OKR KR [Adoption]: Agent funding decision briefs produced for ≥90% of major program approvals within 2 annual cycles of go-live.
OKR KR [Acceptance]: ≥80% of conditions precedent identified by the agent confirmed as appropriate by the CFO.
OKR KR [Cycle]: Programs drawing on approved envelopes before conditions precedent are met reduced to zero within 18 months of go-live.

[PAGE TEXT]
Benefit realization
Measurement of the financial and strategic benefits being delivered against the business case commitment — covering cost savings realization, revenue uplift tracking, regulatory compliance cost avoidance, and strategic capability indicators. Benefit realization is the primary accountability metric for major programs and is tracked by the board throughout the program lifecycle. The gap between promised and realized benefits is the most common source of post-program executive scrutiny and investor concern.
Lens
Scenario
Intent
Complexity

### CARD 10 [Insights|M] Benefit Realization Trajectory Monitoring
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/benefit-realization/benefit-realization-trajectory-monitoring
intent: Agent reads financial actuals, operational KPIs, and the original benefit realization schedule for each program, and produces a monthly trajectory brief showing whether each benefit stream is on track, running behind, or running ahead of the business case commitment — with a revised end-state projection under current trajectory. The board and ExCo track benefit delivery against commitment for every major program with the same rigor applied to budget delivery.
Problem to solve: Benefit realization is assessed quarterly by program leads who self-report against the business case schedule. Without a cross-reference to financial actuals and operational KPIs, self-assessment has an optimism bias. Trajectory divergence — where the realization rate implies a final shortfall even if current actuals are positive — is not computed. The board identifies benefit shortfalls at program completion rather than early enough to intervene.
Solution: Agent reads financial actuals and operational KPIs for each program and cross-references against the business case benefit realization schedule. It produces a monthly trajectory brief with a per-benefit-stream status, the implied end-state projection under current realization rate, and early-warning flags where the trajectory implies a material shortfall. The board receives the brief as a standing agenda item.
OKR objective: The board tracks benefit realization trajectory for each major program monthly rather than at completion.
OKR KR [Adoption]: Agent trajectory briefs produced monthly for ≥90% of active major programs within 12 months of go-live.
OKR KR [Acceptance]: ≥80% of trajectory flags confirmed as directionally accurate by program sponsors and CFO.
OKR KR [Cycle]: Average elapsed time from benefit shortfall trajectory emergence to board awareness reduced from ≥2 quarters to ≤1 reporting cycle.

### CARD 11 [Automation|M] Benefit Realization Attribution Pack
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/benefit-realization/benefit-realization-attribution-pack
intent: Agent reads the benefit realization schedule, financial actuals by benefit category, and program delivery milestones, and produces a quarterly attribution pack mapping each realized and unrealized benefit to its corresponding delivery milestone. Program sponsors present the attribution pack to ExCo rather than a narrative assembled from memory; benefit claims are traceable to specific deliverables rather than asserted at portfolio level.
Problem to solve: Post-program benefit reporting is presented as aggregate cost savings and revenue uplift against the business case commitment. Attribution of realized benefits to the specific deliverables that generated them — technology capability delivered, process eliminated, headcount redeployed — is not produced systematically. When realized benefits fall short, the root cause cannot be traced to a specific delivery failure without a multi-week investigation.
Solution: Agent reads the benefit realization schedule, financial actuals, and program milestone completion data. It produces a quarterly attribution pack mapping each benefit category's realization to the milestones that should have generated it, with variance attribution to specific delivery gaps. Program sponsors review and present to ExCo; benefit accountability is traceable by workstream.
OKR objective: Program benefit realization is traceable by deliverable, not just reported as an aggregate variance.
OKR KR [Adoption]: Agent attribution packs produced quarterly for ≥90% of active programs within 12 months of go-live.
OKR KR [Acceptance]: ≥80% of benefit attributions confirmed as accurate by program sponsors and CFO.
OKR KR [Cycle]: Time to root-cause analysis for benefit shortfall variance reduced from 2–3 weeks to ≤3 business days.

### CARD 12 [Enablement|M] Benefit Realization Business Case Refresh
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/benefit-realization/benefit-realization-business-case-refresh
intent: Agent reads cumulative realization actuals, the program's remaining delivery schedule, and updated market assumptions, and produces an annual business case refresh showing the revised NPV and IRR under current trajectory. The CFO and program sponsor use the refresh to determine whether continued investment is warranted, whether scope should be reduced, or whether the program should be restructured. The continue-vs-restructure decision is made on current financial terms, not the original approval case.
Problem to solve: Major programs are approved against a business case that is not refreshed during delivery. As market conditions shift, delivery delays accumulate, and early benefit streams under-deliver, the NPV of the remaining investment may have moved materially negative — but the program continues because no one has recalculated the case for continued investment. The decision to continue, restructure, or stop is made on the original approved case rather than the current financial reality.
Solution: Agent reads realization actuals, the remaining delivery schedule, and current market assumptions. It produces an annual business case refresh with revised NPV, IRR, and the range of outcomes under alternative completion scenarios. The CFO and program sponsor use the refresh as the basis for the annual continue-vs-restructure decision.
OKR objective: The financial case for continuing each major program is refreshed annually against current actuals and market assumptions.
OKR KR [Adoption]: Agent business case refreshes produced annually for ≥90% of active major programs within 2 annual cycles of go-live.
OKR KR [Acceptance]: ≥80% of refreshed NPV calculations accepted by the CFO without material revision to methodology.
OKR KR [Cycle]: Programs continuing beyond the point at which a refresh would have triggered restructuring reduced by ≥50% vs baseline.

[PAGE TEXT]
Steering governance
Ongoing oversight of the program through the steering committee — meeting cadence, escalation paths, issue and risk management, and milestone gate reviews. Steering governance consumes significant senior leader time each cycle: preparing materials, conducting reviews, and following up on actions. Under NBKR operational resilience guidelines, major transformation programs must maintain documented steering oversight with board visibility into material risk escalations.
Lens
Scenario
Intent
Complexity

### CARD 13 [Insights|S] Steering Committee Pre-Read Synthesis
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/steering-governance/steering-committee-pre-read-synthesis
intent: Agent reads workstream status reports, risk register updates, and issue logs submitted for each steering committee cycle and produces a synthesised pre-read brief: top three risks requiring steering decision, milestone status across all workstreams in a standard format, and unresolved issues from the previous cycle. Steering committee members receive a pre-read they can consume in 15 minutes rather than assembling across disparate workstream reports; session time concentrates on decisions rather than status review.
Problem to solve: Steering committee pre-reads are assembled by the PMO from workstream status reports of inconsistent format and quality. Members receive a thick pack that requires 45 to 60 minutes of reading to extract the decisions required and the program's current risk posture. Session time is consumed by status review, leaving insufficient time for substantive governance discussion on escalations and strategic course corrections.
Solution: Agent reads all submitted workstream materials and produces a structured pre-read brief highlighting the top risks requiring steering decision, milestone status in a consistent format, and outstanding issues. PMO reviews and supplements with forward agenda framing. Committee members consume the brief in 15 minutes; the session opens with decisions rather than status reporting.
OKR objective: Steering committee session time concentrates on governance decisions rather than status review.
OKR KR [Adoption]: Agent pre-read briefs used for ≥90% of steering cycles across ≥3 active programs within 12 months of go-live.
OKR KR [Acceptance]: ≥80% of pre-reads rated as sufficient by steering committee members; session decision throughput improves by ≥25%.
OKR KR [Cycle]: Average steering committee session time spent on status review vs decision items inverted from 70/30 to ≤40/60 within 18 months.

### CARD 14 [Automation|S] Steering Governance Longitudinal Record
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/steering-governance/steering-governance-longitudinal-record
intent: Agent reads steering committee meeting records across the program lifecycle and maintains a continuously updated longitudinal record covering every decision made, every risk escalation and its resolution, and the evolution of milestone commitments from baseline. Program directors, auditors, and NBKR/CBR examiners can retrieve a complete governance record without manual assembly; regulatory examination responses are produced from a maintained record rather than reconstructed from archived minutes.
Problem to solve: Program governance records are held in meeting minutes and action logs across the program lifecycle. When a regulatory examiner or internal auditor requests a history of steering committee decisions on a specific risk or milestone, the PMO assembles the record manually from archived documents. The reconstruction is incomplete where minutes are inconsistent and time-consuming under examination deadline pressure.
Solution: Agent reads each steering committee meeting record and adds decisions, risk escalations, and milestone revisions to a structured longitudinal record. The record is searchable by topic, date, and decision type. Program directors access it for continuity; auditors and examiners retrieve it directly; no manual reconstruction is required.
OKR objective: A complete, searchable longitudinal governance record is maintained throughout the program lifecycle without manual assembly.
OKR KR [Adoption]: Agent-maintained longitudinal records active for ≥3 programs within 12 months of go-live.
OKR KR [Acceptance]: ≥90% of governance record queries by auditors and program directors resolved without manual document retrieval.
OKR KR [Cycle]: Regulatory examination response time for governance history requests reduced from days to ≤4 hours of record retrieval and review.

### CARD 15 [Enablement|M] Steering Governance Pack Drafting
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/steering-governance/steering-governance-pack-drafting
intent: Agent reads current program progress, budget actuals vs plan, risk register, dependency status, and benefit case status, and assembles the steering committee pack with a structured recommendation framing for the gate or periodic review decision. Program manager and finance partner review the assembled pack and apply judgment on recommendation language and escalation. Inconsistencies between the budget, risk, and benefit views are flagged before the pack reaches the committee rather than identified during the review.
Problem to solve: Steering committee packs require the program manager and finance partner to collate milestone progress, budget actuals, risk updates, and benefit status from multiple systems ahead of each cycle. The collation takes several days per pack. Inconsistencies between the budget, risk, and benefit sections slip through to the steering committee paper and are identified during the review, consuming committee time on reconciliation.
Solution: Agent reads the program tracker, budget actuals, risk log, and benefit tracking source for each program due at the steering committee. It assembles the pack with a structured go/no-go or baseline-reset recommendation framing, with cross-section consistency checks flagged for reviewer attention. Program manager and finance partner edit the recommendation framing and apply forward judgment before submission.
OKR objective: The steering committee pack — RAG status, financial burn, milestone achievement, risk register, benefit case status, and go/no-go recommendation framing — is assembled by agent from program tracker, budget actuals, risk log, and benefit tracking sources, with cross-section consistency checks flagged before the pack reaches the committee.
OKR KR [Adoption]: Agent drafts steering committee packs for ≥95% of scheduled governance cycles; cross-section consistency checks completed and go/no-go recommendation framing included in ≥90% of produced packs.
OKR KR [Acceptance]: ≥80% of agent-produced packs accepted by program managers and finance partners as the committee submission basis without full redraft; cross-section inconsistencies identified at the committee review reduced by ≥70% from prior-year baseline.
OKR KR [Cycle]: Steering committee pack collation cycle reduced from several days of multi-system manual assembly to ≤1 business day of agent aggregation and program manager review.

[PAGE TEXT]
Change management
The organizational and behavioral dimension of program delivery — stakeholder engagement, training and capability build, communication planning, and adoption measurement. Change management readiness is a leading indicator of post-go-live benefit realization; programs that underinvest in change management consistently underdeliver against business cases. Measuring change readiness and adoption across large, distributed organizations requires synthesizing survey data, training completion rates, and behavioral adoption signals from operational systems.
Lens
Scenario
Intent
Complexity

### CARD 16 [New opps|S] Change Readiness Assessment
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/change-management/change-readiness-assessment
intent: Agent reads stakeholder engagement scores, training completion rates by function, and behavioral adoption signals from pilot deployments, and produces a change readiness assessment ahead of each major go-live — with gap identification by stakeholder group and prioritized intervention recommendations. Steering committee acts on readiness gaps with lead time for corrective action before the go-live schedule is fixed. The bank is positioned to pursue more ambitious transformation scope because readiness risk is identified and managed, not absorbed post-launch.
Problem to solve: Change readiness is assessed through stakeholder surveys and training completion reports assembled manually by the change management team. The consolidated view reaches the steering committee two to three weeks after the underlying data is collected — typically after the go-live schedule has been confirmed. Readiness gaps that surface at this stage require expensive schedule delays or post-launch recovery programs to remediate.
Solution: Agent reads stakeholder engagement scores, training completion data by function, and behavioral adoption signals from pilot deployments. It generates a change readiness assessment with gap identification by stakeholder group and prioritized intervention recommendations. Steering committee reviews the assessment with sufficient lead time ahead of the go-live milestone and authorizes targeted remediation where gaps are identified.
OKR objective: Change readiness assessments — with gap identification by stakeholder group and prioritized intervention recommendations — are available to the steering committee from agent-produced synthesis of engagement scores, training completion, and behavioral adoption signals in advance of each major go-live milestone.
OKR KR [Adoption]: Agent produces a change readiness assessment for ≥100% of programs with a confirmed go-live milestone; assessments delivered ≥3 weeks before the scheduled go-live date.
OKR KR [Acceptance]: ≥80% of stakeholder group gap identifications confirmed as actionable by program directors and change leads without material revision; assessment delivered with sufficient lead time for remediation in ≥90% of go-lives.
OKR KR [Cycle]: Readiness assessment delivery time reduced from 2–3 weeks post-data-collection to ≤3 business days from data availability.

### CARD 17 [Automation|S] Change Impact Stakeholder Brief
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/change-management/change-impact-stakeholder-brief
intent: Agent reads the program design documents and change log and produces a change impact brief for each major stakeholder group — covering what changes for their role, what stays the same, what new capability they gain, and what the timeline is for each change. The communications team uses the briefs as the basis for stakeholder engagement materials; the change impact analysis that typically takes two weeks per stakeholder group is produced as a starting point within a working session.
Problem to solve: Change impact analysis for major transformation programs is performed by business analysts who interview workstream leads and document the implications for each affected role and business unit. The process takes two weeks per major stakeholder group and must be repeated as scope evolves. Communications and training materials are built on the change impact analysis, so delays cascade into later program phases.
Solution: Agent reads the program design documents and accumulated change log and generates a structured change impact brief for each stakeholder group — role changes, process changes, system changes, and timeline. The business analysts review and validate the brief against workstream leads; the research and documentation phase is replaced by a structured validation exercise.
OKR objective: Change impact briefs for each major stakeholder group are available for review within days of a major scope finalisation, not weeks.
OKR KR [Adoption]: Agent change impact briefs produced for ≥90% of major stakeholder groups across ≥3 programs within 12 months of go-live.
OKR KR [Acceptance]: ≥80% of briefs accepted by business analysts and communications team with ≤20% revision.
OKR KR [Cycle]: Change impact analysis elapsed time per stakeholder group reduced from 2 weeks to ≤3 business days for programs in scope.

### CARD 18 [Insights|M] Change Readiness Continuous Signal Brief
urn: urn:financial-services:scenario:strategic-initiatives/major-transformation-programs/change-management/change-readiness-continuous-signal
intent: Agent reads training completion rates, pulse survey results, help-desk query volumes by topic, and system adoption metrics from the program's operational deployment, and produces a fortnightly change readiness signal brief by business unit and role cohort. The change management lead uses the brief to identify adoption blockers and direct targeted intervention before go-live; post-go-live, the brief tracks adoption trajectory against the business case assumptions.
Problem to solve: Change readiness is assessed through periodic surveys and training completion reports. Between surveys, adoption signals from system usage data and help-desk queries are not synthesised into a readiness view. Low adoption rates are typically identified at the post-go-live benefit review rather than during preparation, when intervention options are greatest.
Solution: Agent reads training completion data, pulse survey results, help-desk query volumes, and system adoption metrics across all affected cohorts. It produces a fortnightly readiness signal brief by business unit and role, with cohorts flagged for targeted intervention. The change management lead reviews and directs resources before go-live and tracks adoption trajectory post-go-live.
OKR objective: Change readiness is monitored continuously by cohort throughout the program, not only at survey points.
OKR KR [Adoption]: Agent readiness signal brief produced fortnightly for ≥90% of program cycles across ≥3 programs within 12 months of go-live.
OKR KR [Acceptance]: ≥80% of cohort-level readiness flags confirmed as accurate by change management lead and business unit heads.
OKR KR [Cycle]: Go-live adoption rate within 90 days — measured against business case assumption — improves by ≥20% for programs with continuous readiness monitoring vs baseline.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
