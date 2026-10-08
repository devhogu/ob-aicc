# Capability Cycles

The recurring cycles that govern shared banking capabilities — KPI/SLA review, continuous improvement, investment, and vendor sourcing.

## Performance & improvement {#performance-improvement}

### Capability KPI & SLA review cycle {#capability-kpi-sla-review-cycle}

- URN: urn:financial-services:flow:shared-banking-capabilities/capability-kpi-sla-review-cycle
- Summary: Monthly and quarterly review of KPI and SLA performance across shared capabilities — scorecard assembly, breach identification, root-cause triage, and remediation planning. The cycle anchor is the time from metric collection to management action.

The capability KPI and SLA review cycle is the recurring governance process by which the Bank measures whether its shared operational capabilities — credit decisioning throughput, transaction processing exception rates, KYC completion cycle times, AML alert triage volumes, collections contact rates — are performing to the standards committed in service-level agreements and internal capability plans. The cycle runs monthly at the operational level and quarterly at senior management review, covering operational metrics that the regulator supervises alongside internally defined SLAs. Each capability has a distinct metric set, but the cycle structure is common: collect actuals, compare to targets, identify and diagnose breaches, produce a management report, and assign remediation. The bottleneck is the assembly step — metrics arrive from separate operational systems on different schedules, and cross-capability comparison is a manual consolidation exercise that delays management visibility by one to two weeks after the measurement period ends. GenAI compresses assembly and diagnosis — automating the collection of actuals across systems, flagging breaches against SLA thresholds, and producing draft root-cause commentary — so the management review can focus on remediation decisions rather than data consolidation.

| Lens | Problem |
| --- | --- |
| Analyze | KPI and SLA actuals across all shared capabilities are assembled manually once per month or quarter. Continuous visibility into intra-period performance trends — which capabilities are trending toward breach mid-cycle — is absent from the standard management information set. |
| Optimize | Cross-capability breach prioritization and remediation-plan coherence are assessed by separate capability owners without a common framework. The cumulative remediation backlog and the interaction between overlapping remediations are not visible to a single owner between formal review cycles. |
| Automate | Actuals collection, SLA threshold comparison, breach identification, and draft root-cause commentary are structured, repeating tasks performed on the same data sources each cycle. The assembly and comparison steps are high-volume and rule-bound — primary candidates for AI-driven execution with analyst review. |
| Enrich | Remediation outcomes — whether the action taken resolved the breach — are rarely linked back to the root-cause attribution that framed the remediation. The cycle builds little compounding knowledge about which root causes recur and which remediation types are effective. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| measure | Measure | Collection and consolidation of KPI and SLA actuals across capabilities | Collects performance actuals from each shared capability's operational systems — processing volumes, cycle times, exception rates, breach counts, SLA attainment — and assembles a cross-capability scorecard for the review period. The stage that opens the cycle at each measurement interval. | Performance data for shared capabilities is held in separate operational systems — credit, payments, KYC, AML, collections — each with its own data extract schedule and metric definition. Cross-capability consolidation is a manual process that consumes one to two weeks before the management scorecard is ready for review. |
| review | Review | Structured review of the scorecard against SLA thresholds and prior periods | Compares consolidated actuals against SLA thresholds, internal capability targets, and prior-period trends — surfacing which capabilities are within tolerance, which are approaching breach, and which have already breached. The stage where the performance picture becomes a management signal. | The SLA threshold comparison requires analysts to cross-reference the live scorecard against a separate SLA register maintained in a different system. Threshold changes approved mid-year are not always reflected in the comparison tool, creating mis-stated breach signals that require manual correction. |
| identify | Identify breaches | Identification and prioritization of SLA breaches and performance outliers | Isolates confirmed SLA breaches and material performance outliers from the comparison output — categorized by capability, severity, and customer or regulatory impact. The diagnostic filter that focuses remediation effort on the most consequential performance gaps. | Breach prioritization is applied by individual capability owners using their own severity criteria. Cross-capability prioritization — which breach has the highest combined customer, regulatory, and operational impact — is not systematically applied, and high-impact outliers in less-visible capabilities are deprioritized relative to noisier but lower-impact breaches in prominent capabilities. |
| plan | Plan remediation | Remediation planning for confirmed SLA breaches and performance gaps | Develops remediation plans for confirmed breaches — root-cause attribution, responsible owner, action steps, target resolution date, and next-cycle reassessment criteria. The stage that converts breach identification into an operational mandate. | Remediation plans are produced by capability owners in narrative form with variable depth. Root-cause attribution is informal, target dates are often rolled forward from prior cycles, and the link between the remediation action and the specific metric being remediated is not always explicit enough to verify at the next review cycle. |
| track | Track | Cycle-over-cycle tracking of remediation progress and SLA recovery | Monitors remediation progress against the plans agreed at the prior cycle, updates the scorecard with recovery trajectories, and flags remediations that are overdue or at risk of slippage. The closing stage that feeds the next cycle's opening scorecard. | Remediation tracking relies on self-reported progress updates from capability owners submitted before each review cycle. Late submissions and optimistic status claims surface only when the metric fails to recover at the expected rate — one cycle after the slippage has already occurred. |

#### Mid-Cycle SLA Breach Signal

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-kpi-sla-review-cycle/mid-cycle-sla-breach-signal
- Lens: Insights
- Complexity: S
- Intent: The AI agent monitors intra-period performance feeds daily and surfaces capabilities trending toward SLA breach before the formal measurement date, giving capability owners a remediation window within the cycle rather than a confirmed breach at the end of it.
- Problem to solve: SLA breach identification is a monthly or quarterly event; capabilities can trend toward breach for weeks without management visibility. Remediation that could have been applied mid-cycle is deferred until the breach is confirmed and recorded.
- Solution: The AI agent reads the same operational data feeds used for scorecard assembly on a daily cadence, applies the SLA threshold logic against trajectory rather than end-of-period actuals, and issues breach-risk alerts for capabilities where the trend indicates a threshold will be crossed before the measurement date. Capability owners receive the alert with a current-state data summary and decide on remediation within the cycle.
- OKR: Capabilities trending toward SLA breach receive a threshold-proximity alert before the formal measurement date, giving capability owners a remediation window within the cycle rather than a confirmed breach record at the end of it.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced mid-cycle SLA breach signals delivered for ≥90% of threshold-proximity events detected during daily monitoring in year 1; all capability domains covered in daily feeds. |
| Acceptance | ≥80% of mid-cycle alerts confirmed as indicating genuine breach risk by capability owners on review; remediation actions initiated within 3 business days in ≥75% of alerted cases. |
| Cycle | Breach-risk signal available to capability owners within 1 business day of threshold-proximity detection, vs. confirmed breach at the monthly measurement date in the prior process. |

#### SLA Breach Root-Cause Commentary Drafting

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-kpi-sla-review-cycle/sla-breach-root-cause-commentary
- Lens: Enablement
- Complexity: S
- Intent: The AI agent drafts root-cause commentary for each confirmed SLA breach at the identify stage, drawing on the last three cycles of scorecard history and any linked incident or remediation records, ready for capability owner review and amendment before the management report is finalized.
- Problem to solve: Root-cause attribution for breaches is drafted by capability owners under time pressure after the scorecard is available. Recurring root causes — interface latency, batch processing failure, staffing shortfall — are re-described from scratch each cycle rather than referenced against prior occurrence records.
- Solution: The AI agent retrieves the breach record, the last three cycles of metric history for the same capability, and any linked incident or prior-remediation records. It drafts the root-cause commentary in the management report template with cross-references to prior occurrences and remediation outcomes. The capability owner reviews, amends, and approves before submission.
- OKR: Root-cause commentary for each confirmed SLA breach is drafted from the last three cycles of scorecard history and linked incident and remediation records, ready for capability owner review before the management report is finalized.

| Dimension | Key result |
| --- | --- |
| Adoption | AI agent used to draft root-cause commentary for ≥90% of confirmed SLA breaches within the monthly management reporting cycle in year 1. |
| Acceptance | ≥80% of AI-drafted commentaries accepted by capability owners without material restatement; prior-occurrence cross-references validated as accurate in ≥90% of reviewed breaches. |
| Cycle | Root-cause commentary draft available within 4 hours of breach confirmation, vs. 1–2 days of capability owner drafting under reporting deadline in the prior process. |

#### Remediation Outcome Institutional Record

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-kpi-sla-review-cycle/remediation-outcome-institutional-record
- Lens: New opps
- Complexity: S
- Intent: The AI agent accumulates remediation outcomes — actual metric recovery against plan, root-cause recurrence — across cycles into a structured institutional record, enabling FP&A and capability planning to calibrate OPEX and SLA ambition from evidence rather than from first principles at each planning round.
- Problem to solve: Remediation tracking relies on self-reported progress updates; outcome evidence — whether the metric recovered, whether the root cause recurred — is not captured in a durable structured form after the cycle closes. Each new capability investment case and planning round re-creates OPEX and SLA assumptions without reference to prior remediation evidence.
- Solution: The AI agent reads the post-cycle metric actuals for each capability under active remediation and compares them to the targets committed in the remediation plan. It records the outcome — recovered, partially recovered, failed — against the root-cause attribution and the specific remediation action, building a searchable institutional library that feeds business-case and planning-cycle assumption setting; Finance validates outcome accuracy on periodic review.
- OKR: Remediation outcomes — actual metric recovery against plan and root-cause recurrence — are accumulated into a structured institutional record across cycles, enabling FP&A and capability planning to calibrate OPEX and SLA ambition from prior-cycle evidence.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-maintained remediation outcome record covers ≥85% of closed remediation cycles from the preceding 24 months within 12 months of go-live; new outcomes recorded within 10 business days of cycle close. |
| Acceptance | ≥60% of new capability investment cases and planning-cycle OPEX assumptions reference prior remediation outcome records as calibration inputs; outcome accuracy validated at ≥80% on periodic Finance review of benefit realization. |
| Cycle | Prior remediation evidence retrievable for planning assumptions within 1 hour of query, vs. no structured institutional record in the prior process. |

#### KPI/SLA Scorecard Assembly

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-kpi-sla-review-cycle/kpi-sla-scorecard-assembly-agent
- Lens: Automation
- Complexity: M
- Intent: The AI agent collects KPI and SLA actuals from operational systems across credit decisioning, payments, KYC, AML, and collections on the cycle cadence, assembles the cross-capability scorecard, and delivers it to the review team within one business day of the measurement period close. The stage that previously consumed one to two weeks of manual consolidation is reduced to an automated data pull with analyst sign-off on outliers.
- Problem to solve: Performance data for shared capabilities sits in separate operational systems, each with its own extract schedule and metric definition. Cross-capability scorecard assembly is a manual consolidation exercise; the management review meeting opens one to two weeks after the measurement period ends.
- Solution: The AI agent reads structured actuals from each operational system on the cycle cadence, maps metrics to the shared SLA register, assembles the cross-capability scorecard, and flags metrics with no matching actuals for analyst resolution. The scorecard is available for review within one business day of period close.
- OKR: KPI and SLA actuals across credit decisioning, payments, KYC, AML, and collections are collected from operational systems and assembled into a cross-capability scorecard available for management review within one business day of the measurement period close.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced KPI/SLA scorecard used for ≥10 of 12 monthly measurement cycles in year 1; all five capability domains covered in each cycle. |
| Acceptance | ≥90% of scorecard actuals confirmed accurate by analysts without requiring restatement; metrics with no matching actuals flagged for analyst resolution within 4 hours of scorecard delivery in ≥95% of cycles. |
| Cycle | Cross-capability scorecard available within 1 business day of period close, vs. 1–2 weeks of manual consolidation in the prior process. |

#### Capability Remediation Backlog Prioritization

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-kpi-sla-review-cycle/capability-remediation-backlog-prioritisation
- Lens: Optimize
- Complexity: M
- Intent: The AI agent scores the active remediation backlog across all capabilities on a combined impact index — customer, regulatory, and OPEX exposure weighted by SLA severity — and recommends a sequenced remediation queue at the plan stage, making cross-capability priority explicit for the COO.
- Problem to solve: Remediation plans are produced by individual capability owners using domain-specific severity criteria. Cross-capability prioritization — which breach has the highest combined customer, regulatory, and OPEX impact — is not systematically applied; high-impact breaches in less-visible capabilities are deprioritized relative to noisier but lower-impact breaches in prominent ones.
- Solution: The AI agent reads confirmed breaches and their associated metric, severity classification, and customer and regulatory impact flags across all capabilities. It applies a consistent impact index, ranks the remediation backlog, and produces a prioritized queue with supporting rationale for each rank position. The COO reviews the recommended sequence; capability owners retain ownership of individual remediation plans.
- OKR: The active capability remediation backlog is ranked on a consistent cross-capability impact index — weighted by customer, regulatory, and OPEX exposure and SLA severity — and a sequenced remediation queue is available for COO review at the plan stage of each quarterly review.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced remediation backlog ranking used for ≥90% of quarterly capability review cycles within year 1; ranking covers all active breaches across all capability domains. |
| Acceptance | ≥75% of COO-level remediation sequencing decisions align with the AI-produced ranking; cross-capability prioritization score validated by independent review in ≥90% of assessed cases. |
| Cycle | Cross-capability remediation queue available for COO review within 2 business days of each measurement period close, vs. 1–2 weeks of independent capability-owner submissions in the prior process. |

### Continuous improvement cycle {#continuous-improvement-cycle}

- URN: urn:financial-services:flow:shared-banking-capabilities/continuous-improvement-cycle
- Summary: Structured identification, prioritization, and implementation of operational improvements across shared capabilities. The cycle anchor is the time from improvement identification to production deployment and measured benefit realization.

The continuous improvement cycle is the process by which the Bank systematically identifies, evaluates, and deploys operational improvements across shared capabilities — reducing unit cost, improving throughput, lowering exception rates, and enhancing customer outcomes in credit decisioning, transaction processing, KYC, financial crime, and servicing. It operates as a rolling quarterly cycle with a structured intake, prioritization against a business-case framework, and post-implementation measurement. The principal bottleneck is the gap between improvement identification — typically surfaced through post-incident reviews, SLA breach remediations, or frontline operational feedback — and the point at which an improvement reaches the prioritization committee with a complete business case. Most improvements stall at the business-case assembly stage for two to four quarters before receiving a prioritization decision. GenAI shortens the business-case assembly step and accelerates post-implementation measurement — producing draft cases from structured operational data and comparing pre/post metrics automatically once a change has been deployed.

| Lens | Problem |
| --- | --- |
| Analyze | The improvement pipeline — intake queue size, prioritization backlog, implementation progress, and realization status — is not tracked in a consolidated form. The Head of Shared Capabilities cannot see the full improvement lifecycle at any point in the cycle without manual assembly from multiple project and operational sources. |
| Optimize | Prioritization scoring is applied within each capability domain independently. Cross-capability prioritization — an improvement in transaction processing that unlocks capacity in AML alert triage — requires cross-domain analysis that capability-specific prioritization committees are not structured to perform. |
| Automate | Business-case modeling, post-implementation metric comparison, and the production of the quarterly prioritization pack are structured analytical tasks that repeat each cycle with the same framework applied to updated operational data. |
| Enrich | Completed improvements and their realized benefit outcomes are rarely documented in a form that informs future improvement identification. The Bank does not maintain a searchable library of past interventions, their root causes, and their outcomes that could accelerate business-case assembly for similar future improvements. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| identify | Identify | Identification of improvement opportunities from operational signals | Aggregates improvement opportunities from multiple sources — SLA breach remediations, post-incident reviews, frontline feedback, benchmarking exercises, and strategic capability reviews — into a structured intake. The stage that populates the improvement pipeline each cycle. | Improvement opportunities from different sources arrive in different formats and channels. SLA breach remediations produce structured plans; frontline feedback arrives informally through team leads; benchmarking findings are documented in project reports. No single intake mechanism captures all sources, and improvements identified in one channel are invisible to the prioritization process in another. |
| prioritize | Prioritize | Prioritization of improvement candidates against business-case criteria | Evaluates improvement candidates against a common business-case framework — impact on key metrics, cost and effort to implement, dependency on other changes, and risk — and ranks them for the quarterly prioritization committee. The governance gate that determines which improvements enter the implementation queue. | Business cases for improvement candidates are prepared by capability owners with variable analytical rigor. Quantifying the metric impact of a proposed improvement requires access to operational data that capability owners do not always have direct access to; cases often rely on directional estimates rather than modeled projections, making comparisons across candidates inconsistent. |
| implement | Implement | Structured implementation of approved improvement initiatives | Executes approved improvements through the capability's change management process — design, testing, deployment, training, and controlled rollout. The stage where a prioritized improvement becomes an operational change. | Implementation of capability improvements competes with business-as-usual change demand in the same technology and operations teams. Approved improvements are frequently delayed when higher-urgency fixes or regulatory change demands consume available change capacity. The improvement backlog grows faster than it is cleared. |
| measure | Measure benefit | Post-implementation measurement of benefit realization against the business case | Measures the operational impact of implemented improvements against business-case targets — metric movement, cost change, exception-rate reduction — over the defined realization window. The stage that closes the improvement cycle and validates the investment decision. | Post-implementation measurement is the most consistently skipped stage in the improvement cycle. Responsibility sits with the capability owner who championed the improvement, but by the time the realization window has elapsed the same team is absorbed in the next implementation cycle. Formal realization evidence is produced for a minority of completed improvements. |
| sustain | Sustain | Embedding of improvements into standard operating procedures and monitoring | Embeds implemented improvements into the capability's standard operating model — updated procedures, revised SLA thresholds, new KPI baselines — so that gains are sustained and not eroded by subsequent change. The closing stage that anchors the new operating level as the baseline for the next cycle. | Improvements that are successfully implemented often erode within two to four quarters when the operational team reverts to prior working practices under pressure. Updated procedures are documented but not enforced; new KPI baselines are set but not linked to the SLA review cycle. The next cycle measures against the old baseline, masking the erosion. |

#### Improvement Business Case Drafting

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/continuous-improvement-cycle/improvement-business-case-drafting
- Lens: Enablement
- Complexity: S
- Intent: The AI agent drafts the business case for each improvement candidate from the structured operational data available in the improvement register and the Bank's operational systems, compressing the time from improvement identification to prioritization-ready case from two to four quarters to two to three weeks.
- Problem to solve: Improvement candidates stall at the business-case assembly stage for two to four quarters because quantifying the metric impact requires access to operational data that capability owners do not directly control. Cases rely on directional estimates; cross-candidate comparisons are inconsistent.
- Solution: The AI agent reads the improvement register entry, the relevant operational metric history, and any linked incident or SLA breach records. It drafts the business case in the Bank's standard template — current-state metric baseline, estimated post-improvement target, cost and effort estimate, risk assessment, and dependency flags. The capability owner reviews the draft, confirms assumptions, and submits to the prioritization committee.
- OKR: The business case for each improvement candidate — covering current-state metric baseline, estimated post-improvement target, cost and effort estimate, risk assessment, and dependency flags — is available for capability owner review within 2–3 weeks of improvement identification, vs. 2–4 quarters in the prior process.

| Dimension | Key result |
| --- | --- |
| Adoption | AI agent used to draft ≥80% of improvement business cases submitted to the prioritization committee within year 1. |
| Acceptance | ≥80% of AI-drafted business cases accepted by capability owners without material restatement of the metric baseline or benefit estimate; cross-candidate comparison consistency verified on periodic Finance review. |
| Cycle | Business case available for capability owner review within 2–3 weeks of improvement identification, vs. 2–4 quarters of stalled assembly in the prior process. |

#### Improvement Post-Implementation Benefit Measurement

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/continuous-improvement-cycle/improvement-post-implementation-benefit-measurement
- Lens: Insights
- Complexity: S
- Intent: The AI agent compares pre- and post-implementation metric actuals for each deployed improvement at the measurement stage, produces a structured realization report against business-case targets, and flags improvements where benefit is not materializing on the expected trajectory for capability owner investigation.
- Problem to solve: Post-implementation benefit measurement is the most consistently skipped stage in the improvement cycle. Formal realization evidence is produced for a minority of completed improvements because the implementing team is absorbed in the next cycle by the time the realization window elapses.
- Solution: The AI agent reads pre-implementation metric baselines from the improvement register and post-implementation actuals from the operational system at defined measurement intervals — 30, 60, and 90 days. It produces a structured realization report for each improvement and flags cases where actual benefit delivery falls below the business-case target threshold, triggering a capability owner investigation task.
- OKR: Pre- and post-implementation metric actuals are compared at 30-, 60-, and 90-day intervals for each deployed improvement, with a structured realization report produced against business-case targets and below-trajectory benefits flagged for capability owner investigation.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced benefit measurement reports delivered for ≥85% of completed improvements at all three measurement intervals within year 1. |
| Acceptance | ≥80% of realization reports confirmed as accurate by capability owners on review; below-trajectory flags triggering capability owner investigation in ≥90% of confirmed underperformance cases. |
| Cycle | Measurement report available within 5 business days of each measurement interval, vs. no systematic post-implementation measurement in the prior process. |

#### Improvement Institutional Knowledge Base

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/continuous-improvement-cycle/improvement-knowledge-base-accumulation
- Lens: New opps
- Complexity: S
- Intent: The AI agent accumulates completed improvement records — root cause, intervention type, realized benefit, and recurrence status — into a searchable institutional library that accelerates business-case assembly for similar future improvements and informs root-cause elimination at a systemic level.
- Problem to solve: Completed improvements and their outcomes are not documented in a searchable form. The Bank has no library of past interventions, root causes, and outcomes that could reduce business-case assembly burden or support a root-cause elimination program.
- Solution: The AI agent reads each completed improvement record — intake evidence, root-cause attribution, approved business case, implementation outcome, and benefit realization result — and writes a structured entry into the institutional improvement knowledge base indexed by capability domain, root-cause category, intervention type, and benefit range. Future intake processing references the knowledge base to identify analogous prior improvements and reuse validated business-case assumptions.
- OKR: Completed improvement records — root cause, intervention type, realized benefit, and recurrence status — are accumulated into a searchable institutional library indexed by capability domain, root-cause category, intervention type, and benefit range, available for business-case assembly and root-cause elimination.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-maintained knowledge base covers ≥85% of completed improvements from the preceding 24 months within 12 months of go-live; new entries added within 10 business days of improvement closure. |
| Acceptance | ≥60% of new business cases reference prior knowledge-base entries as assumption anchors; validated business-case assumptions reused from the library confirmed as accurate within ±20% on benefit realization in ≥75% of cases. |
| Cycle | Prior improvement records retrievable for business-case assembly within 1 hour of query, vs. no searchable institutional library in the prior process. |

#### Improvement Opportunity Intake Channel Unification

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/continuous-improvement-cycle/improvement-intake-channel-unification
- Lens: Automation
- Complexity: M
- Intent: The AI agent reads improvement signals from all intake channels — SLA breach remediations, post-incident reviews, frontline feedback logs, benchmarking reports, and strategic reviews — and normalizes them into a structured improvement register with a common classification, estimated impact range, and originating evidence reference.
- Problem to solve: Improvement opportunities arrive through separate channels in different formats; improvements surfaced through one channel are invisible to the prioritization process of another. The prioritization committee works from an incomplete picture of the opportunity set.
- Solution: The AI agent reads all intake channels on a weekly cadence and normalizes each item into the common improvement register schema, merging duplicate signals raised through more than one channel. It applies an initial impact classification based on the affected capability and the metric referenced in the originating evidence. The prioritization committee works from a complete, classified register.
- OKR: Improvement signals from all intake channels — SLA breach remediations, post-incident reviews, frontline feedback logs, benchmarking reports, and strategic reviews — are normalized into a single structured improvement register with a common classification, estimated impact range, and originating evidence reference.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-normalized improvement register covers ≥90% of active intake channels within 12 months of go-live; all improvement signals processed into the shared register within 5 business days of source event. |
| Acceptance | ≥80% of cross-channel improvement entries rated as correctly classified and impact-estimated by the prioritization committee; duplicate detection accuracy ≥90% on periodic register audit. |
| Cycle | Improvement signal normalization completed within 5 business days of source event, vs. channel-specific queues with no unified view in the prior process. |

#### Cross-Capability Improvement Prioritization

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/continuous-improvement-cycle/cross-capability-improvement-prioritisation
- Lens: Optimize
- Complexity: M
- Intent: The AI agent scores improvement candidates across all capability domains on a common business-case framework — weighted metric impact, cost-to-implement estimate, cross-capability dependency, and risk — and surfaces cross-domain improvement opportunities that individual capability prioritization committees are not structured to identify.
- Problem to solve: Prioritization scoring is applied within each capability domain by separate committees. Cross-capability improvements — an enhancement to transaction processing that unlocks AML alert queue capacity — require cross-domain analysis that domain-specific committees do not perform.
- Solution: The AI agent applies the Bank's standard improvement prioritization model to all candidates, scoring each on weighted metric impact, cost and effort, change complexity, and cross-capability dependency. It flags candidates where the primary benefit accrues to a different domain than the implementing capability and presents the full cross-capability ranked queue alongside the domain-specific view to the quarterly prioritization committee.
- OKR: Improvement candidates across all capability domains are scored on a common business-case framework and a cross-domain ranked queue — including candidates where the primary benefit accrues to a different domain than the implementing capability — is available for the quarterly prioritization committee.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced cross-capability improvement ranking used for ≥3 of 4 quarterly prioritization cycles in year 1; all active capability domains covered in each scoring run. |
| Acceptance | ≥75% of cross-capability improvement candidates flagged by the AI agent are rated as genuinely cross-domain by the prioritization committee; scoring methodology consistency verified on periodic Finance review. |
| Cycle | Cross-capability improvement ranking available within 5 business days of each quarterly prioritization intake close, vs. 3–4 weeks of sequential domain-committee review in the prior process. |

## Investment & sourcing {#investment-sourcing}

### Capability investment cycle {#capability-investment-cycle}

- URN: urn:financial-services:flow:shared-banking-capabilities/capability-investment-cycle
- Summary: Annual and periodic investment planning for shared capability upgrades, replacements, and new builds — business-case development, approval, delivery, and benefit tracking. The cycle anchor is the time from strategic gap identification to approved investment mandate.

The capability investment cycle governs the Bank's decisions on major investment in shared operational capabilities — platform upgrades, technology replacements, process automation programs, and capability expansions that fall above the operational improvement threshold and require capital allocation through the annual planning or mid-year investment approval process. Supervisory requirements commonly provide that significant technology and outsourcing investments are notified to the regulator or pre-approved; the cycle must accommodate regulatory notification timelines alongside internal governance. The cycle's primary constraint is the quality and speed of business-case production. Investment cases for capability upgrades require cross-function input — IT architecture, operations, finance, risk, compliance, legal — assembled under the annual planning deadline. Cases that miss the annual planning window are deferred to the next cycle, imposing a twelve-month penalty that compounds the operational cost of running on a degraded capability. GenAI can compress the business-case assembly stage — synthesizing cross-function inputs, modeling benefit scenarios, and producing the investment case document — so that cases arrive at the investment committee with full supporting analysis rather than directional estimates.

| Lens | Problem |
| --- | --- |
| Analyze | The capability investment portfolio — cases in preparation, cases in approval, programs in delivery, and benefits in realization — is not tracked in a consolidated view. The Head of Shared Capabilities and the CTO cannot see pipeline coverage, approval lag, delivery variance, and benefit realization gap simultaneously. |
| Optimize | Investment case benefit modeling is the weakest stage in the cycle. Cases use directional estimates because the data assembly required for rigorous modeling consumes more time than the planning deadline allows. Alternative investment options — build vs buy, phased vs full-scope, vendor A vs vendor B — are rarely explored with equal analytical depth before the approval decision. |
| Automate | Investment case document production, cross-function input synthesis, regulatory notification checklist preparation, and post-deployment benefit tracking reports are structured tasks that repeat for each investment across a consistent framework. The assembly burden is the primary cycle constraint. |
| Enrich | Completed investment programs — their actual vs planned cost, delivery timelines, and realized benefits — are rarely documented in a structured form that informs the next investment cycle's assumptions. Each new investment case is built from first principles, repeating the estimation effort that prior program outcomes could have informed. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| plan | Plan | Strategic capability gap assessment and investment scope definition | Identifies strategic gaps in the capability portfolio — where current capabilities will fall short of the Bank's three-year plan, regulatory requirements, or competitive benchmarks — and defines the investment scope for the annual planning cycle. The stage that opens the investment pipeline. | Capability gap assessments are conducted by individual capability owners in preparation for the annual planning cycle. Cross-capability gap prioritization — whether the most material gap is in credit decisioning, transaction processing, or financial crime — requires a consolidated assessment that the planning process rarely produces before the investment submission deadline. |
| approve | Approve | Investment committee review and capital allocation approval | Presents investment cases to the relevant governance forum — technology investment committee, management board, or board of directors — for capital allocation approval, supported by full business-case documentation including regulatory notification requirements. The governance gate for the investment cycle. | Investment cases arrive at the committee with variable analytical depth. Cases developed under tight annual planning deadlines often lack quantified benefit modeling, realistic delivery timelines, or documented regulatory notification obligations. Committee discussions are consumed by case clarification rather than investment decision-making. |
| build | Build | Program initiation and capability delivery | Initiates and delivers the approved investment through a structured program — requirements definition, vendor selection where applicable, build or configuration, testing, and staged deployment. The delivery stage that converts the approved investment into a new or enhanced operating capability. | Capability investment programs frequently encounter scope creep, integration complexity with legacy systems, and resource conflicts with concurrent change programs. Budget and timeline variance is identified late when milestone reviews surface accumulated slippage rather than early when steering intervention could redirect the program. |
| deploy | Deploy | Capability deployment and transition to operations | Deploys the new or enhanced capability into production — cutover planning, parallel running, operational readiness sign-off, and hypercare period management. The stage where the delivered capability transitions from program to operational ownership. | Cutover plans are typically developed late in the program and compress significantly when downstream delivery milestones slip. Operational readiness assessments are completed under deadline pressure rather than as a gate with sufficient lead time. |
| sustain | Sustain | Post-deployment benefit realization and capability performance tracking | Tracks the deployed capability's performance against the approved investment case over the defined realization horizon — measuring whether the committed benefits have been achieved and initiating remediation where the capability underperforms against plan. The closing stage of the investment cycle. | Benefit realization tracking for capability investments is rarely maintained for the full realization horizon stated in the business case. Program closure triggers a handover to operations that does not include a formal benefit tracking mandate; realization evidence is absent from subsequent investment cases that rely on the same benefit logic. |

#### Program Delivery Variance Monitoring

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-investment-cycle/programme-delivery-variance-monitoring
- Lens: Enablement
- Complexity: S
- Intent: The AI agent reads program milestone data across active capability investment programs, surfaces delivery variance against plan at milestone level rather than at quarterly gate review, and produces a weekly steering brief for the CTO covering slippage risk, budget variance, and interdependency impacts.
- Problem to solve: Budget and timeline variance on capability investment programs is identified late, when milestone reviews surface accumulated slippage rather than when steering intervention could redirect the program. Intra-quarter slippage across interdependent programs is invisible to the CTO between formal review events.
- Solution: The AI agent reads milestone completion status, budget consumption, and resource allocation data from the program management system on a weekly cadence. It flags milestones at slippage risk based on completion trajectory and identifies dependencies where a slipping milestone affects downstream delivery. The CTO receives a weekly steering brief with recommended intervention points.
- OKR: Delivery variance against plan at milestone level — covering slippage risk, budget variance, and interdependency impacts across all active capability investment programs — is surfaced to the CTO in a weekly steering brief rather than at quarterly gate reviews.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced weekly program steering brief delivered for ≥48 of 52 weeks in year 1; all active capability investment programs covered. |
| Acceptance | ≥80% of slippage risk flags confirmed as genuine by the CTO on review; recommended intervention points acted on within 5 business days in ≥70% of flagged cases. |
| Cycle | Program variance signal available to the CTO weekly, vs. quarterly gate review only in the prior process; intra-quarter slippage detection latency reduced from 3 months to ≤7 days. |

#### Capability Investment Benefit Realization Tracking

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-investment-cycle/capability-investment-benefit-realisation
- Lens: New opps
- Complexity: S
- Intent: The AI agent tracks post-deployment benefit realization for each capability investment against the committed business-case targets over the defined realization horizon, producing a quarterly realization report that accumulates institutional evidence on which benefit categories and investment types reliably deliver committed returns.
- Problem to solve: Benefit realization tracking for capability investments lapses after program closure; the handover to operations does not include a formal tracking mandate. Subsequent investment cases rely on benefit assumptions that prior program outcomes could have calibrated, but that evidence is not structured or accessible.
- Solution: The AI agent reads the operational KPI actuals for each deployed capability against the business-case baseline at quarterly intervals for the committed realization horizon. It produces a realization report by benefit category — OPEX reduction, throughput improvement, exception-rate reduction — for the investment sponsor to confirm, and accumulates a benefit realization library available to the next investment planning cycle.
- OKR: Post-deployment benefit realization for each capability investment is tracked quarterly against committed business-case targets over the defined realization horizon, with an accumulating institutional evidence base available for the next investment planning cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced realization reports covering ≥85% of deployed capability investments with committed realization horizons within year 1; quarterly cadence maintained for all tracked investments. |
| Acceptance | ≥80% of investment sponsors confirm the realization report accurately reflects operational metric performance; prior-cycle realization evidence cited in ≥50% of new investment case benefit assumptions within year 2. |
| Cycle | Realization report for each tracked investment available within 5 business days of each quarter-end, vs. no systematic tracking in the prior process. |

#### Capability Gap Assessment Synthesis

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-investment-cycle/capability-gap-assessment-synthesis
- Lens: Insights
- Complexity: M
- Intent: The AI agent synthesizes cross-capability gap evidence from SLA breach history, benchmarking data, regulatory findings, and strategic plan targets into a ranked capability gap register at the start of the annual planning cycle, giving the CTO and Head of Shared Capabilities a prioritized investment pipeline before individual business-case production begins.
- Problem to solve: Capability gap assessments are produced by individual capability owners independently. Cross-capability gap prioritization — whether the most material shortfall is in credit decisioning throughput, KYC cycle time, or transaction processing exception rates — is not consolidated before the investment submission deadline.
- Solution: The AI agent reads SLA breach history, prior-year benchmark reports, regulatory observation logs, and the three-year strategic plan targets for each capability. It synthesizes a cross-capability gap register ranked by a composite gap score covering OPEX impact, customer outcome risk, and regulatory exposure. The CTO and Head of Shared Capabilities use the register to align on investment priorities before individual business cases are commissioned.
- OKR: A cross-capability gap register — ranked by composite OPEX impact, customer outcome risk, and regulatory exposure — is available to the CTO and Head of Shared Capabilities before individual business-case production begins each annual planning cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced capability gap register used as the primary investment prioritization input for ≥1 annual planning cycle within year 1; register covers ≥90% of capability domains. |
| Acceptance | ≥75% of CTO-level investment priority decisions cite the gap register as a primary input; gap register completeness verified against source evidence (SLA breach history, regulatory findings, benchmarking) in ≥90% of entries. |
| Cycle | Cross-capability gap register available for CTO review at planning cycle kick-off, vs. 4–6 weeks of independent capability-owner submissions in the prior process. |

#### Capability Investment Case Document Assembly

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-investment-cycle/capability-investment-case-assembly
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles the investment case document for a capability upgrade from structured inputs provided by capability, IT, Finance, Risk, and Compliance owners — producing a fully populated case including cost-benefit analysis, delivery timeline, regulatory notification checklist, and risk assessment — ready for committee review.
- Problem to solve: Investment cases for capability upgrades require cross-function inputs assembled under the annual planning deadline. Cases that arrive at the investment committee with incomplete benefit modeling or undocumented regulatory notification obligations consume committee time in clarification rather than decision-making.
- Solution: The AI agent receives structured inputs from each contributing function through a common case template and assembles the investment case in the prescribed format. It flags missing inputs, applies the standard cost-benefit model, and produces the regulatory notification checklist under current outsourcing requirements. The sponsor reviews the assembled case before committee submission.
- OKR: Investment cases for capability upgrades are assembled with complete cost-benefit analysis, delivery timeline, regulatory notification checklist, and risk assessment ready for committee review, with cross-function input gaps flagged before committee submission.

| Dimension | Key result |
| --- | --- |
| Adoption | AI agent used to assemble ≥80% of capability investment cases submitted for committee approval within year 1. |
| Acceptance | ≥85% of assembled cases accepted for decision at first committee review without being returned for supplementary analysis; regulatory notification checklist completeness confirmed by Compliance in ≥95% of reviewed cases. |
| Cycle | Investment case assembly time from sponsor brief to committee-ready document reduced from 6–10 weeks of cross-function coordination to ≤2 weeks. |

#### Build-Buy-Partner Scenario Modeling

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/capability-investment-cycle/build-buy-partner-scenario-modelling
- Lens: Optimize
- Complexity: M
- Intent: The AI agent models build, buy, and partner options for a capability investment at the approval stage, producing a structured comparison of ten-year OPEX and CAPEX, delivery risk, vendor concentration exposure, and regulatory notification burden for each option.
- Problem to solve: Build-vs-buy-vs-partner options for capability investments are rarely explored with equal analytical depth before the approval decision. Time constraints in the annual planning cycle mean the committee typically reviews a single recommended option with directional sensitivity rather than a quantified comparison across alternatives.
- Solution: The AI agent applies the Bank's standard investment scenario model to each option, modeling ten-year total cost of ownership under the Bank's cost of capital assumptions, delivery risk discount, and vendor concentration exposure under outsourcing concentration limits. The committee selects the approved option on the basis of the full quantified comparison.
- OKR: Investment committees review a quantified 10-year OPEX/CAPEX, delivery risk, vendor concentration, and regulatory notification comparison across build, buy, and partner options for every material capability investment decision.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced build-buy-partner scenario comparison used for ≥80% of capability investment cases submitted for committee approval within year 1. |
| Acceptance | In ≥75% of cases the investment committee rates the scenario comparison as sufficient to select the approved option without commissioning a further manual analysis; model outputs reconcile to the Bank's standard cost-of-capital assumptions in ≥98% of reviewed cases. |
| Cycle | Build-buy-partner scenario comparison available within 5 business days of investment case commissioning, vs. 3–6 weeks of manual analysis in the prior process. |

### Vendor & sourcing review cycle {#vendor-sourcing-review-cycle}

- URN: urn:financial-services:flow:shared-banking-capabilities/vendor-sourcing-review-cycle
- Summary: Periodic review of vendor performance, contract terms, and sourcing strategy across critical shared-capability suppliers — aligned to the regulator's outsourcing requirements. The cycle anchor is the time from performance signal to contract or sourcing action.

The vendor and sourcing review cycle governs the Bank's oversight of third-party suppliers providing services to shared capabilities — core banking platform vendors, payment processing providers, KYC and AML software suppliers, credit bureau data providers, and managed service operators. Outsourcing requirements commonly impose formal obligations on vendor due diligence, contract terms, concentration limits, and exit planning. International guidance such as the EBA guidelines on outsourcing arrangements serves as a reference for third-party risk management. The cycle operates on a tiered cadence: critical and material vendors are reviewed quarterly; non-critical vendors annually. Each review covers operational performance against SLAs, financial health of the vendor, regulatory compliance of the outsourced function, concentration risk, and contractual adequacy. The governance framework must evidence continuous oversight to the regulator. GenAI compresses the vendor performance narrative assembly, financial health monitoring, and contract adequacy analysis — enabling the sourcing team to maintain continuous oversight of a large vendor portfolio without proportional analyst headcount.

| Lens | Problem |
| --- | --- |
| Analyze | Vendor performance, financial health, and risk signals are assessed on fixed review cycles rather than continuously. A vendor's SLA degradation trajectory between quarterly reviews, or a financial distress signal appearing in public filings between annual reviews, is not systematically surfaced to the sourcing team. |
| Optimize | Sourcing strategy decisions — which capabilities to insource, which to consolidate to a single vendor, which to multi-source — are made at contract renewal with incomplete market intelligence. Concentration risk analysis across the vendor portfolio requires manual aggregation that is rarely current enough to inform active sourcing decisions. |
| Automate | Vendor performance report assembly, contract adequacy review against current outsourcing requirements, financial health summary production, and due diligence pack assembly for new vendor onboarding are structured tasks with defined frameworks that repeat for each vendor each cycle. |
| Enrich | Vendor review findings, incident histories, and regulatory observations accumulate in individual contract files rather than in a consolidated vendor knowledge base. The sourcing team does not have access to a searchable record of prior findings across the portfolio that would improve the efficiency and quality of each new review. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| evaluate | Evaluate | Vendor performance assessment against SLAs and risk criteria | Assesses each vendor against operational SLAs, information security standards, regulatory compliance requirements, financial stability indicators, and concentration risk thresholds — producing a performance and risk rating for each relationship. The diagnostic stage that opens each vendor review cycle. | Vendor performance data is held in separate contract management, SLA monitoring, and information security systems. The sourcing team assembles the performance picture manually for each review, drawing from SLA reports, vendor-submitted attestations, and periodic security assessments. The assembly consumes the majority of the review window, leaving limited time for analytical judgment on the rating. |
| negotiate | Negotiate | Contract negotiation or renegotiation triggered by performance or cycle events | Initiates contract renegotiation where performance-based contractual rights are triggered, where market benchmarking identifies pricing or terms divergence, or where regulatory changes require contract amendments — aligned to outsourcing contract requirements. | Contract renegotiation is reactive — triggered by expiry or breach rather than by continuous market benchmarking. The sourcing team typically enters renegotiation without a current market comparison, limiting leverage. Regulatory changes that require contract amendments are identified only when Compliance reviews the new regulation, not through continuous monitoring. |
| onboard | Onboard | Structured onboarding of new vendors with regulatory and risk due diligence | Executes the onboarding process for new vendors providing services to shared capabilities — due diligence, regulatory notification where outsourcing rules require it, contract execution, and operational readiness validation. The stage that brings a new vendor into the Bank's approved supplier framework. | Vendor onboarding for critical functions commonly requires regulatory notification or approval under outsourcing rules, which typically adds four to twelve weeks to the onboarding timeline. Onboarding timelines are consistently underestimated during vendor selection because the regulatory notification step is not built into the standard onboarding plan. |
| monitor | Monitor | Continuous operational and risk monitoring of active vendor relationships | Maintains continuous monitoring of active vendors between formal review cycles — SLA tracking, information security posture assessment, financial health signals, and incident reporting — to surface material deterioration before the next scheduled review. The stage that underpins outsourcing compliance between formal review events. | Between formal review cycles, vendor monitoring relies on monthly SLA reports self-submitted by vendors and annual security assessments triggered by calendar rather than by risk signal. Material vendor deterioration — a security incident at a critical payment provider, or a financial distress signal at a core banking vendor — can go undetected until the next formal review. |
| renew | Renew or exit | Contract renewal decision or managed exit from the vendor relationship | Makes the renewal or exit decision at contract expiry — supported by the full review cycle evidence, a market benchmarking assessment, and a documented exit plan compliant with outsourcing exit requirements. The governance gate that closes one cycle and opens the next. | Exit plans are commonly required under outsourcing rules for material outsourcing arrangements but are typically generic and untested. When a genuine exit is required — due to vendor failure, regulatory sanction, or strategic sourcing change — the exit plan does not provide sufficient operational detail to execute without significant disruption. |

#### Vendor Onboarding Regulatory Notification Timeline Planning

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/vendor-sourcing-review-cycle/vendor-onboarding-regulatory-timeline-planning
- Lens: Optimize
- Complexity: S
- Intent: The AI agent generates a vendor-specific onboarding timeline at the start of each new vendor engagement, incorporating the regulatory notification lead time that outsourcing rules require, so that notification obligations are built into the onboarding plan rather than discovered mid-process.
- Problem to solve: Vendor onboarding timelines for critical functions are consistently underestimated because the regulatory notification step under outsourcing rules — which typically adds four to twelve weeks — is not built into the standard onboarding plan. Programs are delayed and launch dates slip when the notification obligation is discovered mid-process.
- Solution: The AI agent reads the vendor's proposed service scope and classification under the Bank's outsourcing register and applies the regulatory notification requirements for that function under current outsourcing rules. It generates a complete onboarding timeline with regulatory notification milestones, due diligence checkpoint dates, and contract execution sequencing built in. The program manager receives the timeline at the start of the onboarding engagement.
- OKR: A vendor-specific onboarding timeline — with regulatory notification milestones, due diligence checkpoint dates, and contract execution sequencing built in — is generated for the program manager at the start of each new vendor engagement.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced onboarding timeline used for ≥90% of new critical and material vendor engagements within year 1; regulatory notification lead times included for all classified outsourcing functions. |
| Acceptance | ≥85% of onboarding programs that follow the AI-produced timeline meet their planned go-live date without a regulatory notification-driven delay; timeline accuracy (notification lead time vs. the regulator's actual processing time) confirmed within ±1 week in ≥85% of completed engagements. |
| Cycle | Onboarding timeline with regulatory milestones available within 2 business days of new vendor engagement initiation, vs. notification obligation discovered mid-process in the prior process. |

#### Vendor Performance Review Pack Assembly

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/vendor-sourcing-review-cycle/vendor-performance-pack-assembly
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles the vendor performance review pack for each critical and material vendor by collecting actuals from SLA monitoring systems, information security assessment outputs, financial health indicators, and regulatory compliance signals, delivering a pre-populated review pack to the sourcing team one week before the scheduled review date.
- Problem to solve: The sourcing team assembles the vendor performance picture manually for each review, drawing from SLA reports, vendor-submitted attestations, and security assessments held in separate systems. The assembly consumes the majority of the review window, leaving limited time for analytical judgment on the performance rating.
- Solution: The AI agent reads structured SLA actuals from the contract management system, extracts financial health signals from public filings and credit rating feeds, checks information security posture from the most recent assessment record, and maps the vendor's outsourced function against current outsourcing compliance requirements. The assembled pack is delivered to the sourcing team one week before the review date; analyst effort concentrates on the rating judgment and sourcing recommendation.
- OKR: The vendor performance review pack for each critical and material vendor — covering SLA actuals, financial health indicators, information security posture, and outsourcing compliance signals — is delivered to the sourcing team one week before the scheduled review date.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced vendor performance packs used for ≥90% of scheduled critical and material vendor review events within year 1. |
| Acceptance | ≥85% of assembled packs accepted by the sourcing team as complete and sufficient for the performance rating judgment without requiring supplementary data gathering; SLA actual figures reconcile to the contract management system in ≥98% of reviewed packs. |
| Cycle | Vendor performance pack available one week before the review date, vs. sourcing team manual assembly consuming the majority of the review window in the prior process. |

#### Continuous Vendor Risk Monitoring

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/vendor-sourcing-review-cycle/continuous-vendor-risk-monitoring
- Lens: Insights
- Complexity: M
- Intent: The AI agent monitors active vendor relationships continuously between formal review cycles — tracking SLA trajectory, public financial health signals, and information security event feeds — and surfaces material deterioration to the sourcing team within 48 hours of a threshold signal rather than at the next scheduled quarterly review.
- Problem to solve: Between formal review cycles, vendor monitoring relies on monthly SLA self-reports and annual security assessments triggered by calendar rather than by risk signal. Material deterioration — a financial distress signal at a core banking vendor or a security incident at a critical payment provider — can go undetected until the next formal review.
- Solution: The AI agent reads vendor SLA actuals on a daily cadence, monitors public financial news and credit rating change feeds, and checks information security event notifications from the Bank's threat intelligence subscriptions. When a signal crosses a pre-defined threshold, the sourcing team receives an alert with the signal source and current contract and regulatory context within 48 hours.
- OKR: Material deterioration in active vendor SLA trajectory, financial health, or information security posture is surfaced to the sourcing team within 48 hours of a threshold signal rather than at the next scheduled quarterly review.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-monitored vendor coverage reaches ≥90% of critical and material vendors within 12 months of go-live; monitoring cadence maintained daily for SLA and financial signals. |
| Acceptance | ≥80% of threshold alerts rated as accurate and material by sourcing team on review; false positive rate (alerts not confirmed as material) ≤20% across the monitored portfolio. |
| Cycle | Vendor deterioration signal available to the sourcing team within 48 hours of threshold crossing, vs. quarterly formal review cycle in the prior process. |

#### Vendor Contract Regulatory Adequacy Review

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/vendor-sourcing-review-cycle/vendor-contract-regulatory-adequacy-review
- Lens: Enablement
- Complexity: M
- Intent: The AI agent reviews the active contract for each vendor undergoing renegotiation against current outsourcing requirements, identifies specific clauses that require amendment to meet current regulatory standards, and produces a redline summary for the sourcing and legal teams before negotiation opens.
- Problem to solve: Changes to outsourcing regulations or guidelines that require contract amendments are identified only when Compliance reviews the new regulation, not through continuous contract monitoring against a current regulatory baseline. The renegotiation team enters negotiation without a current regulatory gap assessment.
- Solution: The AI agent maintains a current mapping of outsourcing requirements, and of reference guidance such as the EBA outsourcing guidelines, against the Bank's standard outsourcing contract provisions. At the start of each renegotiation, the AI agent reads the active contract and flags clauses that diverge from current regulatory requirements — covering audit rights, exit planning, sub-outsourcing consent, data residency, and concentration risk disclosure. The sourcing and legal teams receive a redline summary before the opening negotiation position is set; Compliance confirms the flagged gaps.
- OKR: The active contract for each vendor entering renegotiation is reviewed against current outsourcing requirements before negotiation opens, with specific clauses requiring amendment identified and a redline summary delivered to the sourcing and legal teams.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced regulatory adequacy review used for ≥90% of critical and material vendor renegotiations within year 1. |
| Acceptance | ≥85% of clause amendment flags confirmed as genuine regulatory gaps by Compliance on review; no renegotiation proceeds to signature with a known regulatory adequacy gap remaining open in the 12 months post go-live. |
| Cycle | Regulatory adequacy redline summary available to the sourcing team 5 business days before the opening negotiation session, vs. regulatory gap identification mid-negotiation or at next supervisory review in the prior process. |

#### Sourcing Concentration Risk Analysis at Renewal

- URN: urn:financial-services:scenario:flow/shared-banking-capabilities/vendor-sourcing-review-cycle/sourcing-concentration-risk-renewal-analysis
- Lens: New opps
- Complexity: M
- Intent: The AI agent produces a sourcing concentration risk analysis across the full vendor portfolio at each renewal decision point, quantifying single-vendor concentration by capability domain and the cumulative regulatory notification exposure under outsourcing concentration limits, to inform the renewal, multi-sourcing, or insourcing decision.
- Problem to solve: Sourcing strategy decisions at renewal are made without a current portfolio-wide concentration risk view. The Bank may renew a relationship that pushes it above a concentration threshold only discoverable in the next supervisory review.
- Solution: The AI agent reads the full vendor register, maps each vendor's scope to the relevant capability domain and outsourcing classification, and calculates current concentration exposure by domain, technology platform, and geography. It overlays the applicable concentration limits and flags any renewal that would breach or approach a threshold. The sourcing team receives the concentration analysis alongside the renewal recommendation before the committee decision; Compliance reviews the threshold flags.
- OKR: A sourcing concentration risk analysis — quantifying single-vendor concentration by capability domain and cumulative regulatory notification exposure under outsourcing concentration limits — is produced at each vendor renewal decision point before the committee makes its renewal, multi-sourcing, or insourcing decision.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced concentration risk analysis used for ≥90% of critical and material vendor renewal decisions within year 1. |
| Acceptance | ≥80% of threshold proximity flags confirmed as approaching or breaching the limits on Compliance review; no renewal decision results in an undetected concentration breach in the 12 months post go-live. |
| Cycle | Concentration risk analysis available for committee review 5 business days before the renewal decision date, vs. no portfolio-wide concentration view at renewal in the prior process. |
