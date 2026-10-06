# 

source: html-alt/financial-services/en/shared-banking-capabilities/capability-cycles/index.html


[PAGE TEXT]
Performance & improvement
Capability KPI & SLA review cycle
Monthly and quarterly review of KPI and SLA performance across shared capabilities — scorecard assembly, breach identification, root-cause triage, and remediation planning. The cycle anchor is the time from metric collection to management action.
The capability KPI and SLA review cycle is the recurring governance process by which the bank measures whether its shared operational capabilities — credit decisioning throughput, transaction processing exception rates, KYC completion cycle times, AML alert triage volumes, collections contact rates — are performing to the standards committed in service-level agreements and internal capability plans. The cycle runs monthly at the operational level and quarterly at senior management review, covering NBKR-supervised operational metrics alongside internally defined SLAs.
Each capability has a distinct metric set, but the cycle structure is common: collect actuals, compare to targets, identify and diagnose breaches, produce a management report, and assign remediation. The bottleneck is the assembly step — metrics arrive from separate operational systems on different schedules, and cross-capability comparison is a manual consolidation exercise that delays management visibility by one to two weeks after the measurement period ends.
GenAI compresses assembly and diagnosis — automating the collection of actuals across systems, flagging breaches against SLA thresholds, and producing draft root-cause commentary — so the management review can focus on remediation decisions rather than data consolidation.
Analyze
KPI and SLA actuals across all shared capabilities are assembled manually once per month or quarter. Continuous visibility into intra-period performance trends — which capabilities are trending toward breach mid-cycle — is absent from the standard management information set.
Optimize
Cross-capability breach prioritisation and remediation-plan coherence are assessed by separate capability owners without a common framework. The cumulative remediation backlog and the interaction between overlapping remediations are not visible to a single owner between formal review cycles.
Automate
Actuals collection, SLA threshold comparison, breach identification, and draft root-cause commentary are structured, repeating tasks performed on the same data sources each cycle. The assembly and comparison steps are high-volume and rule-bound — primary candidates for agent-driven execution with analyst review.
Enrich
Remediation outcomes — whether the action taken resolved the breach — are rarely linked back to the root-cause attribution that framed the remediation. The cycle builds little compounding knowledge about which root causes recur and which remediation types are effective.
<button
class="flow-stages__stage"
type="button"
data-stage="measure"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/capability-kpi-sla-review-cycle"
>
Measure
→
<button
class="flow-stages__stage"
type="button"
data-stage="review"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/capability-kpi-sla-review-cycle"
>
Review
→
<button
class="flow-stages__stage"
type="button"
data-stage="identify"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/capability-kpi-sla-review-cycle"
>
Identify breaches
→
<button
class="flow-stages__stage"
type="button"
data-stage="plan"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/capability-kpi-sla-review-cycle"
>
Plan remediation
→
<button
class="flow-stages__stage"
type="button"
data-stage="track"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/capability-kpi-sla-review-cycle"
>
Track
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|S] Mid-Cycle SLA Breach Signal
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-kpi-sla-review-cycle/mid-cycle-sla-breach-signal
intent: Agent monitors intra-period performance feeds daily and surfaces capabilities trending toward SLA breach before the formal measurement date, giving capability owners a remediation window within the cycle rather than a confirmed breach at the end of it.
Problem to solve: SLA breach identification is a monthly or quarterly event; capabilities can trend toward breach for weeks without management visibility. Remediation that could have been applied mid-cycle is deferred until the breach is confirmed and recorded.
Solution: Agent reads the same operational data feeds used for scorecard assembly on a daily cadence, applies the SLA threshold logic against trajectory rather than end-of-period actuals, and issues breach-risk alerts for capabilities where the trend indicates a threshold will be crossed before the measurement date. Capability owners receive the alert with a current-state data summary.
OKR objective: Capabilities trending toward SLA breach receive a threshold-proximity alert before the formal measurement date, giving capability owners a remediation window within the cycle rather than a confirmed breach record at the end of it.
OKR KR [Adoption]: Agent-produced mid-cycle SLA breach signals delivered for ≥90% of threshold-proximity events detected during daily monitoring in year 1; all capability domains covered in daily feeds.
OKR KR [Acceptance]: ≥80% of mid-cycle alerts confirmed as indicating genuine breach risk by capability owners on review; remediation actions initiated within 3 business days in ≥75% of alerted cases.
OKR KR [Cycle]: Breach-risk signal available to capability owners within 1 business day of threshold-proximity detection, vs. confirmed breach at the monthly measurement date in the prior process.

### CARD 2 [Enablement|S] SLA Breach Root-Cause Commentary Drafting
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-kpi-sla-review-cycle/sla-breach-root-cause-commentary
intent: Agent drafts root-cause commentary for each confirmed SLA breach at the identify stage, drawing on the last three cycles of scorecard history and any linked incident or remediation records, ready for capability owner review and amendment before the management report is finalised.
Problem to solve: Root-cause attribution for breaches is drafted by capability owners under time pressure after the scorecard is available. Recurring root causes — interface latency, batch processing failure, staffing shortfall — are re-described from scratch each cycle rather than referenced against prior occurrence records.
Solution: Agent retrieves the breach record, the last three cycles of metric history for the same capability, and any linked incident or prior-remediation records. It drafts the root-cause commentary in the management report template with cross-references to prior occurrences and remediation outcomes. The capability owner reviews, amends, and approves before submission.
OKR objective: Root-cause commentary for each confirmed SLA breach is drafted from the last three cycles of scorecard history and linked incident and remediation records, ready for capability owner review before the management report is finalised.
OKR KR [Adoption]: Agent used to draft root-cause commentary for ≥90% of confirmed SLA breaches within the monthly management reporting cycle in year 1.
OKR KR [Acceptance]: ≥80% of agent-drafted commentaries accepted by capability owners without material restatement; prior-occurrence cross-references validated as accurate in ≥90% of reviewed breaches.
OKR KR [Cycle]: Root-cause commentary draft available within 4 hours of breach confirmation, vs. 1–2 days of capability owner drafting under reporting deadline in the prior process.

### CARD 3 [New opps|S] Remediation Outcome Institutional Record
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-kpi-sla-review-cycle/remediation-outcome-institutional-record
intent: Agent accumulates remediation outcomes — actual metric recovery against plan, root-cause recurrence — across cycles into a structured institutional record, enabling FP&A and capability planning to calibrate OPEX and SLA ambition from evidence rather than from first principles at each planning round.
Problem to solve: Remediation tracking relies on self-reported progress updates; outcome evidence — whether the metric recovered, whether the root cause recurred — is not captured in a durable structured form after the cycle closes. Each new capability investment case and planning round re-creates OPEX and SLA assumptions without reference to prior remediation evidence.
Solution: Agent reads the post-cycle metric actuals for each capability under active remediation and compares them to the targets committed in the remediation plan. It records the outcome — recovered, partially recovered, failed — against the root-cause attribution and the specific remediation action, building a searchable institutional library that feeds business-case and planning-cycle assumption setting.
OKR objective: Remediation outcomes — actual metric recovery against plan and root-cause recurrence — are accumulated into a structured institutional record across cycles, enabling FP&A and capability planning to calibrate OPEX and SLA ambition from prior-cycle evidence.
OKR KR [Adoption]: Agent-maintained remediation outcome record covers ≥85% of closed remediation cycles from the preceding 24 months within 12 months of go-live; new outcomes recorded within 10 business days of cycle close.
OKR KR [Acceptance]: ≥60% of new capability investment cases and planning-cycle OPEX assumptions reference prior remediation outcome records as calibration inputs; outcome accuracy validated at ≥80% on periodic Finance review of benefit realisation.
OKR KR [Cycle]: Prior remediation evidence retrievable for planning assumptions within 1 hour of query, vs. no structured institutional record in the prior process.

### CARD 4 [Automation|M] KPI/SLA Scorecard Assembly Agent
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-kpi-sla-review-cycle/kpi-sla-scorecard-assembly-agent
intent: Agent collects KPI and SLA actuals from operational systems across credit decisioning, payments, KYC, AML, and collections on the cycle cadence, assembles the cross-capability scorecard, and delivers it to the review team within one business day of the measurement period close. The stage that previously consumed one to two weeks of manual consolidation is reduced to an automated data pull with analyst sign-off on outliers.
Problem to solve: Performance data for shared capabilities sits in separate operational systems, each with its own extract schedule and metric definition. Cross-capability scorecard assembly is a manual consolidation exercise; the management review meeting opens one to two weeks after the measurement period ends.
Solution: Agent reads structured actuals from each operational system on the cycle cadence, maps metrics to the shared SLA register, assembles the cross-capability scorecard, and flags metrics with no matching actuals for analyst resolution. The scorecard is available for review within one business day of period close.
OKR objective: KPI and SLA actuals across credit decisioning, payments, KYC, AML, and collections are collected from operational systems and assembled into a cross-capability scorecard available for management review within one business day of the measurement period close.
OKR KR [Adoption]: Agent-produced KPI/SLA scorecard used for ≥10 of 12 monthly measurement cycles in year 1; all five capability domains covered in each cycle.
OKR KR [Acceptance]: ≥90% of scorecard actuals confirmed accurate by analysts without requiring restatement; metrics with no matching actuals flagged for analyst resolution within 4 hours of scorecard delivery in ≥95% of cycles.
OKR KR [Cycle]: Cross-capability scorecard available within 1 business day of period close, vs. 1–2 weeks of manual consolidation in the prior process.

### CARD 5 [Optimize|M] Capability Remediation Backlog Prioritisation
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-kpi-sla-review-cycle/capability-remediation-backlog-prioritisation
intent: Agent scores the active remediation backlog across all capabilities on a combined impact index — customer, regulatory, and OPEX exposure weighted by SLA severity — and recommends a sequenced remediation queue at the plan stage, making cross-capability priority explicit for the COO.
Problem to solve: Remediation plans are produced by individual capability owners using domain-specific severity criteria. Cross-capability prioritisation — which breach has the highest combined customer, regulatory, and OPEX impact — is not systematically applied; high-impact breaches in less-visible capabilities are deprioritised relative to noisier but lower-impact breaches in prominent ones.
Solution: Agent reads confirmed breaches and their associated metric, severity classification, and customer and regulatory impact flags across all capabilities. It applies a consistent impact index, ranks the remediation backlog, and produces a prioritised queue with supporting rationale for each rank position. The COO reviews the recommended sequence; capability owners retain ownership of individual remediation plans.
OKR objective: The active capability remediation backlog is ranked on a consistent cross-capability impact index — weighted by customer, regulatory, and OPEX exposure and SLA severity — and a sequenced remediation queue is available for COO review at each planning stage.
OKR KR [Adoption]: Agent-produced remediation backlog ranking used for ≥90% of quarterly capability review cycles within year 1; ranking covers all active breaches across all capability domains.
OKR KR [Acceptance]: ≥75% of COO-level remediation sequencing decisions align with the agent-produced ranking; cross-capability prioritisation score validated by independent review in ≥90% of assessed cases.
OKR KR [Cycle]: Cross-capability remediation queue available for COO review within 2 business days of each measurement period close, vs. 1–2 weeks of independent capability-owner submissions in the prior process.

[PAGE TEXT]
Continuous improvement cycle
Structured identification, prioritisation, and implementation of operational improvements across shared capabilities. The cycle anchor is the time from improvement identification to production deployment and measured benefit realisation.
The continuous improvement cycle is the process by which the bank systematically identifies, evaluates, and deploys operational improvements across shared capabilities — reducing unit cost, improving throughput, lowering exception rates, and enhancing customer outcomes in credit decisioning, transaction processing, KYC, financial crime, and servicing. It operates as a rolling quarterly cycle with a structured intake, prioritisation against a business-case framework, and post-implementation measurement.
The principal bottleneck is the gap between improvement identification — typically surfaced through post-incident reviews, SLA breach remediations, or frontline operational feedback — and the point at which an improvement reaches the prioritisation committee with a complete business case. Most improvements stall at the business-case assembly stage for two to four quarters before receiving a prioritisation decision.
GenAI shortens the business-case assembly step and accelerates post-implementation measurement — producing draft cases from structured operational data and comparing pre/post metrics automatically once a change has been deployed.
Analyze
The improvement pipeline — intake queue size, prioritisation backlog, implementation progress, and realisation status — is not tracked in a consolidated form. The head of shared capabilities cannot see the full improvement lifecycle at any point in the cycle without manual assembly from multiple project and operational sources.
Optimize
Prioritisation scoring is applied within each capability domain independently. Cross-capability prioritisation — an improvement in transaction processing that unlocks capacity in AML alert triage — requires cross-domain analysis that capability-specific prioritisation committees are not structured to perform.
Automate
Business-case modelling, post-implementation metric comparison, and the production of the quarterly prioritisation pack are structured analytical tasks that repeat each cycle with the same framework applied to updated operational data.
Enrich
Completed improvements and their realised benefit outcomes are rarely documented in a form that informs future improvement identification. The bank does not maintain a searchable library of past interventions, their root causes, and their outcomes that could accelerate business-case assembly for similar future improvements.
<button
class="flow-stages__stage"
type="button"
data-stage="identify"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/continuous-improvement-cycle"
>
Identify
→
<button
class="flow-stages__stage"
type="button"
data-stage="prioritize"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/continuous-improvement-cycle"
>
Prioritise
→
<button
class="flow-stages__stage"
type="button"
data-stage="implement"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/continuous-improvement-cycle"
>
Implement
→
<button
class="flow-stages__stage"
type="button"
data-stage="measure"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/continuous-improvement-cycle"
>
Measure benefit
→
<button
class="flow-stages__stage"
type="button"
data-stage="sustain"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/continuous-improvement-cycle"
>
Sustain
Lens
Scenario
Intent
Complexity

### CARD 6 [Enablement|S] Improvement Business Case Drafting
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/continuous-improvement-cycle/improvement-business-case-drafting
intent: Agent drafts the business case for each improvement candidate from the structured operational data available in the improvement register and the bank's operational systems, compressing the time from improvement identification to prioritisation-ready case from two to four quarters to two to three weeks.
Problem to solve: Improvement candidates stall at the business-case assembly stage for two to four quarters because quantifying the metric impact requires access to operational data that capability owners do not directly control. Cases rely on directional estimates; cross-candidate comparisons are inconsistent.
Solution: Agent reads the improvement register entry, the relevant operational metric history, and any linked incident or SLA breach records. It drafts the business case in the bank's standard template — current-state metric baseline, estimated post-improvement target, cost and effort estimate, risk assessment, and dependency flags. The capability owner reviews the draft, confirms assumptions, and submits to the prioritisation committee.
OKR objective: The business case for each improvement candidate — covering current-state metric baseline, estimated post-improvement target, cost and effort estimate, risk assessment, and dependency flags — is available for capability owner review within 2–3 weeks of improvement identification, vs. 2–4 quarters in the prior process.
OKR KR [Adoption]: Agent used to draft ≥80% of improvement business cases submitted to the prioritisation committee within year 1.
OKR KR [Acceptance]: ≥80% of agent-drafted business cases accepted by capability owners without material restatement of the metric baseline or benefit estimate; cross-candidate comparison consistency verified on periodic Finance review.
OKR KR [Cycle]: Business case available for capability owner review within 2–3 weeks of improvement registration, vs. 2–4 quarters of stalled assembly in the prior process.

### CARD 7 [Insights|S] Improvement Post-Implementation Benefit Measurement
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/continuous-improvement-cycle/improvement-post-implementation-benefit-measurement
intent: Agent compares pre- and post-implementation metric actuals for each deployed improvement at the measurement stage, produces a structured realisation report against business-case targets, and flags improvements where benefit is not materialising on the expected trajectory for capability owner investigation.
Problem to solve: Post-implementation benefit measurement is the most consistently skipped stage in the improvement cycle. Formal realisation evidence is produced for a minority of completed improvements because the implementing team is absorbed in the next cycle by the time the realisation window elapses.
Solution: Agent reads pre-implementation metric baselines from the improvement register and post-implementation actuals from the operational system at defined measurement intervals — 30, 60, and 90 days. It produces a structured realisation report for each improvement and flags cases where actual benefit delivery falls below the business-case target threshold, triggering a capability owner investigation task.
OKR objective: Pre- and post-implementation metric actuals are compared at 30-, 60-, and 90-day intervals for each deployed improvement, with a structured realisation report produced against business-case targets and below-trajectory benefits flagged for capability owner investigation.
OKR KR [Adoption]: Agent-produced benefit measurement reports delivered for ≥85% of completed improvements at all three measurement intervals within year 1.
OKR KR [Acceptance]: ≥80% of realisation reports confirmed as accurate by capability owners on review; below-trajectory flags triggering capability owner investigation in ≥90% of confirmed underperformance cases.
OKR KR [Cycle]: Measurement report available within 5 business days of each measurement interval, vs. no systematic post-implementation measurement in the prior process.

### CARD 8 [New opps|S] Improvement Institutional Knowledge Base
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/continuous-improvement-cycle/improvement-knowledge-base-accumulation
intent: Agent accumulates completed improvement records — root cause, intervention type, realised benefit, and recurrence status — into a searchable institutional library that accelerates business-case assembly for similar future improvements and informs root-cause elimination at a systemic level.
Problem to solve: Completed improvements and their outcomes are not documented in a searchable form. The bank has no library of past interventions, root causes, and outcomes that could reduce business-case assembly burden or support a root-cause elimination programme.
Solution: Agent reads each completed improvement record — intake evidence, root-cause attribution, approved business case, implementation outcome, and benefit realisation result — and writes a structured entry into the institutional improvement knowledge base indexed by capability domain, root-cause category, intervention type, and benefit range. Future intake processing references the knowledge base to identify analogous prior improvements and reuse validated business-case assumptions.
OKR objective: Completed improvement records — root cause, intervention type, realised benefit, and recurrence status — are accumulated into a searchable institutional library indexed by capability domain, root-cause category, intervention type, and benefit range, available for business-case assembly and root-cause elimination.
OKR KR [Adoption]: Agent-maintained knowledge base covers ≥85% of completed improvements from the preceding 24 months within 12 months of go-live; new entries added within 10 business days of improvement closure.
OKR KR [Acceptance]: ≥60% of new business cases reference prior knowledge-base entries as assumption anchors; validated business-case assumptions reused from the library confirmed as accurate within ±20% on benefit realisation in ≥75% of cases.
OKR KR [Cycle]: Prior improvement records retrievable for business-case assembly within 1 hour of query, vs. no searchable institutional library in the prior process.

### CARD 9 [Automation|M] Improvement Opportunity Intake Channel Unification
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/continuous-improvement-cycle/improvement-intake-channel-unification
intent: Agent reads improvement signals from all intake channels — SLA breach remediations, post-incident reviews, frontline feedback logs, benchmarking reports, and strategic reviews — and normalises them into a structured improvement register with a common classification, estimated impact range, and originating evidence reference.
Problem to solve: Improvement opportunities arrive through separate channels in different formats; improvements surfaced through one channel are invisible to the prioritisation process of another. The prioritisation committee works from an incomplete picture of the opportunity set.
Solution: Agent reads all intake channels on a weekly cadence and normalises each item into the common improvement register schema. It applies an initial impact classification based on the affected capability and the metric referenced in the originating evidence. The prioritisation committee works from a complete, classified register.
OKR objective: Improvement signals from all intake channels — SLA breach remediations, post-incident reviews, frontline feedback logs, benchmarking reports, and strategic reviews — are normalised into a single structured improvement register with a common classification, estimated impact range, and originating evidence reference.
OKR KR [Adoption]: Agent-normalised improvement register covers ≥90% of active intake channels within 12 months of go-live; all improvement signals processed into the shared register within 5 business days of source event.
OKR KR [Acceptance]: ≥80% of cross-channel improvement entries rated as correctly classified and impact-estimated by the prioritisation committee; duplicate detection accuracy ≥90% on periodic register audit.
OKR KR [Cycle]: Improvement signal normalisation completed within 5 business days of source event, vs. channel-specific queues with no unified view in the prior process.

### CARD 10 [Optimize|M] Cross-Capability Improvement Prioritisation
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/continuous-improvement-cycle/cross-capability-improvement-prioritisation
intent: Agent scores improvement candidates across all capability domains on a common business-case framework — weighted metric impact, cost-to-implement estimate, cross-capability dependency, and risk — and surfaces cross-domain improvement opportunities that individual capability prioritisation committees are not structured to identify.
Problem to solve: Prioritisation scoring is applied within each capability domain by separate committees. Cross-capability improvements — an enhancement to transaction processing that unlocks AML alert queue capacity — require cross-domain analysis that domain-specific committees do not perform.
Solution: Agent applies the bank's standard improvement prioritisation model to all candidates, scoring each on weighted metric impact, cost and effort, change complexity, and cross-capability dependency. It flags candidates where the primary benefit accrues to a different domain than the implementing capability and presents the full cross-capability ranked queue alongside the domain-specific view.
OKR objective: Improvement candidates across all capability domains are scored on a common business-case framework and a cross-domain ranked queue — including candidates where the primary benefit accrues to a different domain than the implementing capability — is available for the investment committee.
OKR KR [Adoption]: Agent-produced cross-capability improvement ranking used for ≥80% of annual investment prioritisation cycles within year 1; all active capability domains covered in each scoring run.
OKR KR [Acceptance]: ≥75% of cross-capability improvement candidates flagged by the agent are rated as genuinely cross-domain by the investment committee; scoring methodology consistency verified on periodic Finance review.
OKR KR [Cycle]: Cross-capability improvement ranking available within 5 business days of the annual prioritisation intake close, vs. 3–4 weeks of sequential domain-committee review in the prior process.

[PAGE TEXT]
Investment & sourcing
Capability investment cycle
Annual and periodic investment planning for shared capability upgrades, replacements, and new builds — business-case development, approval, delivery, and benefit tracking. The cycle anchor is the time from strategic gap identification to approved investment mandate.
The capability investment cycle governs the bank's decisions on major investment in shared operational capabilities — platform upgrades, technology replacements, process automation programmes, and capability expansions that fall above the operational improvement threshold and require capital allocation through the annual planning or mid-year investment approval process. Under NBKR and NBK/ARDFM supervisory frameworks, significant technology and outsourcing investments must be notified or pre-approved; the cycle must accommodate regulatory notification timelines alongside internal governance.
The cycle's primary constraint is the quality and speed of business-case production. Investment cases for capability upgrades require cross-function input — IT architecture, operations, finance, risk, compliance, legal — assembled under the annual planning deadline. Cases that miss the annual planning window are deferred to the next cycle, imposing a twelve-month penalty that compounds the operational cost of running on a degraded capability.
GenAI can compress the business-case assembly stage — synthesising cross-function inputs, modelling benefit scenarios, and producing the investment case document — so that cases arrive at the investment committee with full supporting analysis rather than directional estimates.
Analyze
The capability investment portfolio — cases in preparation, cases in approval, programmes in delivery, and benefits in realisation — is not tracked in a consolidated view. The head of shared capabilities and CTO cannot see pipeline coverage, approval lag, delivery variance, and benefit realisation gap simultaneously.
Optimize
Investment case benefit modelling is the weakest stage in the cycle. Cases use directional estimates because the data assembly required for rigorous modelling consumes more time than the planning deadline allows. Alternative investment options — build vs buy, phased vs full-scope, vendor A vs vendor B — are rarely explored with equal analytical depth before the approval decision.
Automate
Investment case document production, cross-function input synthesis, regulatory notification checklist preparation, and post-deployment benefit tracking reports are structured tasks that repeat for each investment across a consistent framework. The assembly burden is the primary cycle constraint.
Enrich
Completed investment programmes — their actual vs planned cost, delivery timelines, and realised benefits — are rarely documented in a structured form that informs the next investment cycle's assumptions. Each new investment case is built from first principles, repeating the estimation effort that prior programme outcomes could have informed.
<button
class="flow-stages__stage"
type="button"
data-stage="plan"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/capability-investment-cycle"
>
Plan
→
<button
class="flow-stages__stage"
type="button"
data-stage="approve"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/capability-investment-cycle"
>
Approve
→
<button
class="flow-stages__stage"
type="button"
data-stage="build"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/capability-investment-cycle"
>
Build
→
<button
class="flow-stages__stage"
type="button"
data-stage="deploy"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/capability-investment-cycle"
>
Deploy
→
<button
class="flow-stages__stage"
type="button"
data-stage="sustain"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/capability-investment-cycle"
>
Sustain
Lens
Scenario
Intent
Complexity

### CARD 11 [Enablement|S] Programme Delivery Variance Monitoring
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-investment-cycle/programme-delivery-variance-monitoring
intent: Agent reads programme milestone data across active capability investment programmes, surfaces delivery variance against plan at milestone level rather than at quarterly gate review, and produces a weekly steering brief for the CTO covering slippage risk, budget variance, and interdependency impacts.
Problem to solve: Budget and timeline variance on capability investment programmes is identified late, when milestone reviews surface accumulated slippage rather than when steering intervention could redirect the programme. Intra-quarter slippage across interdependent programmes is invisible to the CTO between formal review events.
Solution: Agent reads milestone completion status, budget consumption, and resource allocation data from the programme management system on a weekly cadence. It flags milestones at slippage risk based on completion trajectory and identifies dependencies where a slipping milestone affects downstream delivery. The CTO receives a weekly steering brief with recommended intervention points.
OKR objective: Delivery variance against plan at milestone level — covering slippage risk, budget variance, and interdependency impacts across all active capability investment programmes — is surfaced to the CTO in a weekly steering brief rather than at quarterly gate reviews.
OKR KR [Adoption]: Agent-produced weekly programme steering brief delivered for ≥48 of 52 weeks in year 1; all active capability investment programmes covered.
OKR KR [Acceptance]: ≥80% of slippage risk flags confirmed as genuine by the CTO on review; recommended intervention points acted on within 5 business days in ≥70% of flagged cases.
OKR KR [Cycle]: Programme variance signal available to the CTO weekly, vs. quarterly gate review only in the prior process; intra-quarter slippage detection latency reduced from 3 months to ≤7 days.

### CARD 12 [New opps|S] Capability Investment Benefit Realisation Tracking
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-investment-cycle/capability-investment-benefit-realisation
intent: Agent tracks post-deployment benefit realisation for each capability investment against the committed business-case targets over the defined realisation horizon, producing a quarterly realisation report that accumulates institutional evidence on which benefit categories and investment types reliably deliver committed returns.
Problem to solve: Benefit realisation tracking for capability investments lapses after programme closure; the handover to operations does not include a formal tracking mandate. Subsequent investment cases rely on benefit assumptions that prior programme outcomes could have calibrated, but that evidence is not structured or accessible.
Solution: Agent reads the operational KPI actuals for each deployed capability against the business-case baseline at quarterly intervals for the committed realisation horizon. It produces a realisation report by benefit category — OPEX reduction, throughput improvement, exception-rate reduction — and accumulates a benefit realisation library available to the next investment planning cycle.
OKR objective: Post-deployment benefit realisation for each capability investment is tracked quarterly against committed business-case targets over the defined realisation horizon, with an accumulating institutional evidence base available for the next investment planning cycle.
OKR KR [Adoption]: Agent-produced realisation reports covering ≥85% of deployed capability investments with committed realisation horizons within year 1; quarterly cadence maintained for all tracked investments.
OKR KR [Acceptance]: ≥80% of investment sponsors confirm the realisation report accurately reflects operational metric performance; prior-cycle realisation evidence cited in ≥50% of new investment case benefit assumptions within year 2.
OKR KR [Cycle]: Realisation report for each tracked investment available within 5 business days of each quarter-end, vs. no systematic tracking in the prior process.

### CARD 13 [Insights|M] Capability Gap Assessment Synthesis
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-investment-cycle/capability-gap-assessment-synthesis
intent: Agent synthesises cross-capability gap evidence from SLA breach history, benchmarking data, regulatory findings, and strategic plan targets into a ranked capability gap register at the start of the annual planning cycle, giving the CTO and Head of Shared Capabilities a prioritised investment pipeline before individual business-case production begins.
Problem to solve: Capability gap assessments are produced by individual capability owners independently. Cross-capability gap prioritisation — whether the most material shortfall is in credit decisioning throughput, KYC cycle time, or transaction processing exception rates — is not consolidated before the investment submission deadline.
Solution: Agent reads SLA breach history, prior-year benchmark reports, regulatory observation logs, and the three-year strategic plan targets for each capability. It synthesises a cross-capability gap register ranked by a composite gap score covering OPEX impact, customer outcome risk, and regulatory exposure. The CTO and Head of Shared Capabilities use the register to align on investment priorities before individual business cases are commissioned.
OKR objective: A cross-capability gap register — ranked by composite OPEX impact, customer outcome risk, and regulatory exposure — is available to the CTO and Head of Shared Capabilities before individual business-case production begins each annual planning cycle.
OKR KR [Adoption]: Agent-produced capability gap register used as the primary investment prioritisation input for ≥1 annual planning cycle within year 1; register covers ≥90% of capability domains.
OKR KR [Acceptance]: ≥75% of CTO-level investment priority decisions cite the gap register as a primary input; gap register completeness verified against source evidence (SLA breach history, regulatory findings, benchmarking) in ≥90% of entries.
OKR KR [Cycle]: Cross-capability gap register available for CTO review at planning cycle kick-off, vs. 4–6 weeks of independent capability-owner submissions in the prior process.

### CARD 14 [Automation|M] Capability Investment Case Document Assembly
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-investment-cycle/capability-investment-case-assembly
intent: Agent assembles the investment case document for a capability upgrade from structured inputs provided by capability, IT, Finance, Risk, and Compliance owners — producing a fully populated case including cost-benefit analysis, delivery timeline, regulatory notification checklist, and risk assessment — ready for committee review.
Problem to solve: Investment cases for capability upgrades require cross-function inputs assembled under the annual planning deadline. Cases that arrive at the investment committee with incomplete benefit modelling or undocumented regulatory notification obligations consume committee time in clarification rather than decision-making.
Solution: Agent receives structured inputs from each contributing function through a common case template and assembles the investment case in the prescribed format. It flags missing inputs, applies the standard cost-benefit model, and produces the regulatory notification checklist under current NBK/NBKR outsourcing rules. The sponsor reviews the assembled case before committee submission.
OKR objective: Investment cases for capability upgrades are assembled with complete cost-benefit analysis, delivery timeline, regulatory notification checklist, and risk assessment ready for committee review, with cross-function input gaps flagged before committee submission.
OKR KR [Adoption]: Agent used to assemble ≥80% of capability investment cases submitted for committee approval within year 1.
OKR KR [Acceptance]: ≥85% of assembled cases approved at first committee review without being returned for supplementary analysis; regulatory notification checklist completeness confirmed by Compliance in ≥95% of reviewed cases.
OKR KR [Cycle]: Investment case assembly time from sponsor brief to committee-ready document reduced from 6–10 weeks of cross-function coordination to ≤2 weeks.

### CARD 15 [Optimize|M] Build-Buy-Partner Scenario Modelling
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-investment-cycle/build-buy-partner-scenario-modelling
intent: Agent models build, buy, and partner options for a capability investment at the approval stage, producing a structured comparison of ten-year OPEX and CAPEX, delivery risk, vendor concentration exposure, and regulatory notification burden for each option.
Problem to solve: Build-vs-buy-vs-partner options for capability investments are rarely explored with equal analytical depth before the approval decision. Time constraints in the annual planning cycle mean the committee typically reviews a single recommended option with directional sensitivity rather than a quantified comparison across alternatives.
Solution: Agent applies the bank's standard investment scenario model to each option, modelling ten-year total cost of ownership under the bank's cost of capital assumptions, delivery risk discount, and vendor concentration exposure under NBK/NBKR outsourcing concentration limits. The committee selects the approved option on the basis of the full quantified comparison.
OKR objective: Investment committees review a quantified 10-year OPEX/CAPEX, delivery risk, vendor concentration, and regulatory notification comparison across build, buy, and partner options for every material capability investment decision.
OKR KR [Adoption]: Agent-produced build-buy-partner scenario comparison used for ≥80% of capability investment cases submitted for committee approval within year 1.
OKR KR [Acceptance]: ≥75% of investment committees rate the scenario comparison as sufficient to select the approved option without commissioning a further manual analysis; model outputs reconcile to the bank's standard cost-of-capital assumptions in ≥98% of reviewed cases.
OKR KR [Cycle]: Build-buy-partner scenario comparison available within 5 business days of investment case commissioning, vs. 3–6 weeks of manual analysis in the prior process.

[PAGE TEXT]
Vendor & sourcing review cycle
Periodic review of vendor performance, contract terms, and sourcing strategy across critical shared-capability suppliers — aligned to NBKR and NBK outsourcing rules and EBA outsourcing guidelines. The cycle anchor is the time from performance signal to contract or sourcing action.
The vendor and sourcing review cycle governs the bank's oversight of third-party suppliers providing services to shared capabilities — core banking platform vendors, payment processing providers, KYC and AML software suppliers, credit bureau data providers, and managed service operators. In Kazakhstan and the Kyrgyz Republic, NBK and NBKR outsourcing regulations impose formal obligations on vendor due diligence, contract terms, concentration limits, and exit planning. Internationally, EBA guidelines on outsourcing arrangements (EBA/GL/2019/02) set the standard for third-party risk management applicable to cross-border engagements.
The cycle operates on a tiered cadence: critical and material vendors are reviewed quarterly; non-critical vendors annually. Each review covers operational performance against SLAs, financial health of the vendor, regulatory compliance of the outsourced function, concentration risk, and contractual adequacy. The governance framework must evidence continuous oversight to NBKR/NBK inspectors and, where applicable, to EBA-aligned supervisors.
GenAI compresses the vendor performance narrative assembly, financial health monitoring, and contract adequacy analysis — enabling the sourcing team to maintain continuous oversight of a large vendor portfolio without proportional analyst headcount.
Analyze
Vendor performance, financial health, and risk signals are assessed on fixed review cycles rather than continuously. A vendor's SLA degradation trajectory between quarterly reviews, or a financial distress signal appearing in public filings between annual reviews, is not systematically surfaced to the sourcing team.
Optimize
Sourcing strategy decisions — which capabilities to insource, which to consolidate to a single vendor, which to multi-source — are made at contract renewal with incomplete market intelligence. Concentration risk analysis across the vendor portfolio requires manual aggregation that is rarely current enough to inform active sourcing decisions.
Automate
Vendor performance report assembly, contract adequacy review against current NBK/NBKR and EBA requirements, financial health summary production, and due diligence pack assembly for new vendor onboarding are structured tasks with defined frameworks that repeat for each vendor each cycle.
Enrich
Vendor review findings, incident histories, and regulatory observations accumulate in individual contract files rather than in a consolidated vendor knowledge base. The sourcing team does not have access to a searchable record of prior findings across the portfolio that would improve the efficiency and quality of each new review.
<button
class="flow-stages__stage"
type="button"
data-stage="evaluate"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/vendor-sourcing-review-cycle"
>
Evaluate
→
<button
class="flow-stages__stage"
type="button"
data-stage="negotiate"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/vendor-sourcing-review-cycle"
>
Negotiate
→
<button
class="flow-stages__stage"
type="button"
data-stage="onboard"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/vendor-sourcing-review-cycle"
>
Onboard
→
<button
class="flow-stages__stage"
type="button"
data-stage="monitor"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/vendor-sourcing-review-cycle"
>
Monitor
→
<button
class="flow-stages__stage"
type="button"
data-stage="renew"
data-flow-id="urn:financial-services:flow:shared-banking-capabilities/vendor-sourcing-review-cycle"
>
Renew or exit
Lens
Scenario
Intent
Complexity

### CARD 16 [Optimize|S] Vendor Onboarding Regulatory Notification Timeline Planning
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/vendor-sourcing-review-cycle/vendor-onboarding-regulatory-timeline-planning
intent: Agent generates a vendor-specific onboarding timeline at the start of each new vendor engagement, incorporating the regulatory notification lead time required by NBK and NBKR outsourcing rules, so that notification obligations are built into the onboarding plan rather than discovered mid-process.
Problem to solve: Vendor onboarding timelines for critical functions under NBK and NBKR outsourcing rules are consistently underestimated because the regulatory notification step — which adds four to twelve weeks — is not built into the standard onboarding plan. Programmes are delayed and launch dates slip when the notification obligation is discovered mid-process.
Solution: Agent reads the vendor's proposed service scope and classification under the bank's outsourcing register and applies the regulatory notification requirements for that function under current NBK/NBKR rules. It generates a complete onboarding timeline with regulatory notification milestones, due diligence checkpoint dates, and contract execution sequencing built in. The programme manager receives the timeline at the start of the onboarding engagement.
OKR objective: A vendor-specific onboarding timeline — with NBK/NBKR regulatory notification milestones, due diligence checkpoint dates, and contract execution sequencing built in — is generated for the programme manager at the start of each new vendor engagement.
OKR KR [Adoption]: Agent-produced onboarding timeline used for ≥90% of new critical and material vendor engagements within year 1; regulatory notification lead times included for all classified outsourcing functions.
OKR KR [Acceptance]: ≥85% of onboarding programmes that follow the agent-produced timeline meet their planned go-live date without a regulatory notification-driven delay; timeline accuracy (notification lead time vs. actual NBKR/NBK processing time) confirmed within ±1 week in ≥85% of completed engagements.
OKR KR [Cycle]: Onboarding timeline with regulatory milestones available within 2 business days of new vendor engagement initiation, vs. notification obligation discovered mid-process in the prior process.

### CARD 17 [Automation|M] Vendor Performance Review Pack Assembly
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/vendor-sourcing-review-cycle/vendor-performance-pack-assembly
intent: Agent assembles the vendor performance review pack for each critical and material vendor by collecting actuals from SLA monitoring systems, information security assessment outputs, financial health indicators, and regulatory compliance signals, delivering a pre-populated review pack to the sourcing team one week before the scheduled review date.
Problem to solve: The sourcing team assembles the vendor performance picture manually for each review, drawing from SLA reports, vendor-submitted attestations, and security assessments held in separate systems. The assembly consumes the majority of the review window, leaving limited time for analytical judgement on the performance rating.
Solution: Agent reads structured SLA actuals from the contract management system, extracts financial health signals from public filings and credit rating feeds, checks information security posture from the most recent assessment record, and maps the vendor's outsourced function against current NBK/NBKR outsourcing compliance requirements. The assembled pack is delivered to the sourcing team one week before the review date; analyst effort concentrates on the rating judgement and sourcing recommendation.
OKR objective: The vendor performance review pack for each critical and material vendor — covering SLA actuals, financial health indicators, information security posture, and NBK/NBKR outsourcing compliance signals — is delivered to the sourcing team one week before the scheduled review date.
OKR KR [Adoption]: Agent-produced vendor performance packs used for ≥90% of scheduled critical and material vendor review events within year 1.
OKR KR [Acceptance]: ≥85% of assembled packs accepted by the sourcing team as complete and sufficient for the performance rating judgment without requiring supplementary data gathering; SLA actual figures reconcile to the contract management system in ≥98% of reviewed packs.
OKR KR [Cycle]: Vendor performance pack available one week before the review date, vs. sourcing team manual assembly consuming the majority of the review window in the prior process.

### CARD 18 [Insights|M] Continuous Vendor Risk Monitoring
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/vendor-sourcing-review-cycle/continuous-vendor-risk-monitoring
intent: Agent monitors active vendor relationships continuously between formal review cycles — tracking SLA trajectory, public financial health signals, and information security event feeds — and surfaces material deterioration to the sourcing team within 48 hours of a threshold signal rather than at the next scheduled quarterly review.
Problem to solve: Between formal review cycles, vendor monitoring relies on monthly SLA self-reports and annual security assessments triggered by calendar rather than by risk signal. Material deterioration — a financial distress signal at a core banking vendor or a security incident at a critical payment provider — can remain below the monitoring threshold until the next formal review.
Solution: Agent reads vendor SLA actuals on a daily cadence, monitors public financial news and credit rating change feeds, and checks information security event notifications from the bank's threat intelligence subscriptions. When a signal crosses a pre-defined threshold, the sourcing team receives an alert with the signal source and current contract and regulatory context within 48 hours.
OKR objective: Material deterioration in active vendor SLA trajectory, financial health, or information security posture is surfaced to the sourcing team within 48 hours of a threshold signal rather than at the next scheduled quarterly review.
OKR KR [Adoption]: Agent-monitored vendor coverage reaches ≥90% of critical and material vendors within 12 months of go-live; monitoring cadence maintained daily for SLA and financial signals.
OKR KR [Acceptance]: ≥80% of threshold alerts rated as accurate and material by sourcing team on review; false positive rate (alerts not confirmed as material) ≤15% across the monitored portfolio.
OKR KR [Cycle]: Vendor deterioration signal available to the sourcing team within 48 hours of threshold crossing, vs. quarterly formal review cycle in the prior process.

### CARD 19 [Enablement|M] Vendor Contract Regulatory Adequacy Review
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/vendor-sourcing-review-cycle/vendor-contract-regulatory-adequacy-review
intent: Agent reviews the active contract for each vendor undergoing renegotiation against current NBK/NBKR outsourcing requirements and EBA guidelines, identifies specific clauses that require amendment to meet current regulatory standards, and produces a redline summary for the sourcing and legal teams before negotiation opens.
Problem to solve: Changes to NBK/NBKR outsourcing regulations or EBA guidelines that require contract amendments are identified only when the Compliance team reviews the new regulation, not through continuous contract monitoring against a current regulatory baseline. The renegotiation team enters negotiation without a current regulatory gap assessment.
Solution: Agent maintains a current mapping of NBK/NBKR outsourcing requirements and EBA outsourcing guidelines against the bank's standard outsourcing contract provisions. At the start of each renegotiation, agent reads the active contract and flags clauses that diverge from current regulatory requirements — covering audit rights, exit planning, sub-outsourcing consent, data residency, and concentration risk disclosure. The sourcing team receives a redline summary before the opening negotiation position is set.
OKR objective: The active contract for each vendor entering renegotiation is reviewed against current NBK/NBKR outsourcing requirements and EBA guidelines before negotiation opens, with specific clauses requiring amendment identified and a redline summary delivered to the sourcing and legal teams.
OKR KR [Adoption]: Agent-produced regulatory adequacy review used for ≥90% of critical and material vendor renegotiations within year 1.
OKR KR [Acceptance]: ≥85% of clause amendment flags confirmed as genuine regulatory gaps by Compliance on review; no renegotiation proceeds to signature with a known regulatory adequacy gap remaining open in the 12 months post go-live.
OKR KR [Cycle]: Regulatory adequacy redline summary available to the sourcing team 5 business days before the opening negotiation session, vs. regulatory gap identification mid-negotiation or at next supervisory review in the prior process.

### CARD 20 [New opps|M] Sourcing Concentration Risk Analysis at Renewal
urn: urn:financial-services:scenario:flow/shared-banking-capabilities/vendor-sourcing-review-cycle/sourcing-concentration-risk-renewal-analysis
intent: Agent produces a sourcing concentration risk analysis across the full vendor portfolio at each renewal decision point, quantifying single-vendor concentration by capability domain and the cumulative regulatory notification exposure under NBK/NBKR outsourcing concentration limits, to inform the renewal, multi-sourcing, or insourcing decision.
Problem to solve: Sourcing strategy decisions at renewal are made without a current portfolio-wide concentration risk view. The bank may renew a relationship that pushes it above a concentration threshold only discoverable in the next supervisory review.
Solution: Agent reads the full vendor register, maps each vendor's scope to the relevant capability domain and outsourcing classification, and calculates current concentration exposure by domain, technology platform, and geography. It overlays the NBK/NBKR concentration limits and flags any renewal that would breach or approach a threshold. The sourcing team receives the concentration analysis alongside the renewal recommendation before the committee decision.
OKR objective: A sourcing concentration risk analysis — quantifying single-vendor concentration by capability domain and cumulative regulatory notification exposure under NBK/NBKR outsourcing concentration limits — is produced at each vendor renewal decision point before the committee makes its renewal, multi-sourcing, or insourcing decision.
OKR KR [Adoption]: Agent-produced concentration risk analysis used for ≥90% of critical and material vendor renewal decisions within year 1.
OKR KR [Acceptance]: ≥80% of threshold proximity flags confirmed as approaching or breaching NBK/NBKR limits on Compliance review; no renewal decision results in an undetected concentration breach in the 12 months post go-live.
OKR KR [Cycle]: Concentration risk analysis available for committee review 5 business days before the renewal decision date, vs. no portfolio-wide concentration view at renewal in the prior process.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
×
