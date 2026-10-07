# Capital management

Capital management is the Bank's discipline for maintaining its regulatory capital ratios — CET1, Tier 1, and Total Capital — within the bounds set by the regulator's minima, plus the Bank's own management buffers, while deploying capital efficiently across business lines. It encompasses capital position monitoring, forward capital projection, stress capital assessment (ICAAP), and all supervisory dialog on capital adequacy. **The GenAI opportunity is continuous capital instrumentation and ICAAP drafting acceleration** — translating a monthly reporting cycle into a weekly forward-looking signal and compressing ICAAP production from months to weeks.

## Problems

### Capital position & projection {#capital-position-projection}

| Lens | Problem |
| --- | --- |
| Insights & analytics | CET1 and Tier 1 ratios are reported to ALCO monthly from data assembled across Finance, Risk, and Treasury. Between cycles, the CFO and CRO lack a current forward view of the capital trajectory — emerging headroom pressure from loan growth, provisioning, or regulatory change is identified reactively after positions have moved materially. |
| Enablement | Capital scenario analysis — required for ICAAP, for supervisory dialog, and for capital action decisions — is bottlenecked on small capital modeling teams. When a rating agency or the regulator requests a sensitivity analysis on an alternative macroeconomic scenario, the response requires several weeks of model time and senior analyst capacity. |
| Automation | ICAAP narrative sections, capital ratio walk reports for ALCO, and capital plan summaries for the board are assembled manually from model outputs and prior documents in every reporting cycle. Each document has a prescribed structure — for the ICAAP, the regulator publishes format requirements — and known inputs. |
| New business opportunities | A continuously instrumented capital position enables the CFO to identify RWA optimization opportunities — segments or products where capital consumption is high relative to RAROC — in time to redirect origination before the quarter closes. Banks monitoring capital efficiency weekly rather than monthly act on the signal before the drag compounds. |

## CET1 & Tier 1 position {#cet1-tier1-position}

Current and projected CET1, Tier 1, and Total Capital ratios — maintained above regulatory minima plus management buffers. The position is reported to ALCO monthly and to the board quarterly, with daily monitoring by the CFO and Treasury against management limits. Capital deductions, RWA movements, and accumulated OCI changes all affect the ratio between reporting cycles.

### Capital Ratio Limit Proximity Alert

- URN: urn:financial-services:scenario:finance-treasury/capital-management/cet1-tier1-position/capital-ratio-limit-proximity-alert
- Lens: Optimize
- Complexity: S
- Intent: The AI agent monitors the daily distance between the current capital position and each regulatory and management buffer threshold, and issues an attributed alert when intra-period movements bring any ratio within a defined proximity band before the next monthly report is scheduled.
- Problem to solve: Between monthly reporting cycles, intra-period RWA growth, provision spikes, or accumulated OCI movements can bring the capital ratio materially closer to a buffer threshold without triggering a formal alert. The CFO and Treasury become aware of the proximity only when the monthly report is assembled — by which point the management action window is narrower.
- Solution: The AI agent reads daily capital feeds — current RWA components, CET1 deductions, accumulated OCI, and retained earnings — and computes the live distance to each buffer threshold: regulatory minimum, management buffer, and ICAAP stress capital. When any ratio moves within a defined proximity band — configurable by the CFO's office — the AI agent issues an attributed alert summarizing the current position, the remaining headroom, and the top three intra-period drivers of the movement. Treasury reviews the alert and determines the management response.
- OKR: Treasury and the CFO receive an attributed alert — current position, remaining headroom, and the top three intra-period drivers — whenever a capital ratio moves within the defined proximity band of a regulatory minimum, management buffer, or ICAAP stress capital threshold.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-computed distance to each buffer threshold refreshed on ≥95% of business days in year 1; alerts issued for all proximity-band crossings detected. |
| Acceptance | ≥85% of alerts confirmed by Treasury as accurate and warranting a management response decision; alerted ratios reconcile to the next monthly capital report within ±0.2 percentage points in ≥95% of cases. |
| Cycle | Proximity to a buffer threshold alerted on the day it arises, vs. only when the monthly report is assembled in the prior process. |

### CET1 Capital Headroom & Forward Projection

- URN: urn:financial-services:scenario:finance-treasury/capital-management/cet1-tier1-position/cet1-capital-headroom-projection
- Lens: Insights
- Complexity: M
- Intent: The AI agent projects CET1, Tier 1, and Total Capital ratios across a rolling 12-month horizon, surfaces headroom against regulatory minima plus management buffers, and delivers a weekly ALCO capital update.
- Problem to solve: The capital position is reported to ALCO monthly from data assembled across Finance, Risk, and Treasury. Emerging headroom pressure — from accelerating loan growth, provisioning spikes, or regulatory change — is identified only at the next scheduled cycle, leaving ALCO without a current forward view of the capital ratio trajectory between monthly reports.
- Solution: The AI agent reads current capital feeds — RWA components, CET1 deductions, accumulated OCI — and applies approved planning model assumptions to project the ratio trajectory. It identifies which drivers are tightening headroom fastest, computes distance to each regulatory minimum and management buffer, and produces a weekly ALCO capital narrative in a consistent format. The Treasury and Finance teams review the narrative before it goes to ALCO.
- OKR: CET1, Tier 1, and Total Capital ratio trajectories over a rolling 12-month horizon are available to ALCO and the Treasurer each week, with headroom against regulatory minima and management buffers quantified and driver-attributed in a consistent format.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced weekly capital updates delivered for ≥48 of 52 weeks in year 1; projection covers all RWA components, CET1 deductions, and accumulated OCI movements. |
| Acceptance | ≥85% of weekly capital narratives accepted by the Treasury and Finance teams as current and accurate without material restatement; ratio projections reconcile to the monthly formal capital report within ±0.5 percentage points in ≥95% of weekly checks. |
| Cycle | Weekly ALCO capital narrative available each Monday morning from current feeds, vs. monthly cycle only in the prior process. |

### RWA Movement Attribution

- URN: urn:financial-services:scenario:finance-treasury/capital-management/cet1-tier1-position/rwa-movement-attribution
- Lens: Automation
- Complexity: M
- Intent: The AI agent attributes each period's RWA movement to its drivers — new origination, model parameter changes, rating migrations, regulatory definition changes, and foreign exchange — and delivers a waterfall attribution to the CFO and Treasury on the first day of reporting.
- Problem to solve: RWA movements are reported as a net period change without systematic driver attribution. When the capital ratio tightens unexpectedly, identifying whether the driver is volume growth, a model parameter change, a rating migration wave, or a regulatory definition update requires manual queries across the credit risk and capital systems — a process that takes two to four days and delays management response.
- Solution: The AI agent reads the prior and current-period RWA data extracts across credit, market, and operational risk categories. It applies the Bank's standard RWA attribution methodology — new business, parameter changes, model changes (where the Bank uses internal models), definition changes, and FX — and produces a waterfall chart with materiality-ranked drivers. The attribution is available to the CFO and Treasury on the first day of reporting. Capital Management reviews and signs off the methodology application before the output is shared with ALCO.
- OKR: The CFO and Treasury receive a waterfall attribution of each period's RWA movement — new business, parameter changes, model changes, definition changes, and FX — with materiality-ranked drivers on the first day of reporting.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced RWA attribution used for ≥10 of 12 monthly reporting cycles in year 1; credit, market, and operational risk RWA covered. |
| Acceptance | ≥85% of attributions signed off by Capital Management without material re-attribution; drivers sum to the net period RWA change in ≥98% of reviewed cycles. |
| Cycle | RWA attribution available on day 1 of the reporting window, vs. two to four days of manual queries across the credit risk and capital systems in the prior process. |

## Supervisory communications {#supervisory-communications}

Written supervisory dialog — ICAAP submission cover letters, remediation plan responses, Pillar 2 guidance acknowledgments, and replies to ad hoc supervisory data requests — requires the CFO and CRO to produce regulator-ready narrative under fixed submission deadlines. Response quality, internal consistency with prior submissions, and alignment to the regulator's stated methodology concerns all affect the supervisory relationship.

### Supervisory Observation Tracker

- URN: urn:financial-services:scenario:finance-treasury/capital-management/supervisory-communications/supervisory-observation-tracker
- Lens: Insights
- Complexity: S
- Intent: The AI agent maintains a structured register of all open supervisory observations — categorized by topic, due date, and closure status — and cross-references each new supervisory letter against open items to flag when the regulator is revisiting an unresolved concern.
- Problem to solve: Supervisory observations are tracked in a manual register maintained by the Capital Management team. When a subsequent supervisory letter addresses a topic for which an observation is already open, the link between the two is identified through manual review of prior correspondence — a process that creates risk of inconsistent or delayed responses.
- Solution: The AI agent reads each incoming supervisory letter and the current observation register. It extracts new observations, adds them to the structured register with categorization by risk type and regulatory framework, and cross-references the letter's content against open items to identify where the regulator is revisiting a prior concern. The cross-reference output is presented to the CFO and CRO with the draft response for context. Capital Management owns the register and confirms classification.
- OKR: Capital Management holds a structured register of all open supervisory observations — categorized by topic, due date, and closure status — and the CFO and CRO see, with each draft response, where a new supervisory letter revisits an open item.

| Dimension | Key result |
| --- | --- |
| Adoption | ≥95% of incoming supervisory letters processed into the register within year 1; all open observations categorized by risk type and regulatory framework. |
| Acceptance | ≥90% of extracted observations and classifications confirmed by Capital Management without correction; ≥90% of cross-references to open items rated as relevant by the CFO and CRO. |
| Cycle | New observations registered and cross-referenced within 1 business day of the letter's receipt, vs. manual review of prior correspondence in the prior process. |

### Regulatory Relationship Briefing

- URN: urn:financial-services:scenario:finance-treasury/capital-management/supervisory-communications/regulatory-relationship-briefing
- Lens: Automation
- Complexity: S
- Intent: Before scheduled supervisory meetings, the AI agent assembles a briefing covering the Bank's current capital and liquidity position, all open observations and pending responses, and the topics most likely to be raised based on the regulator's recent public guidance and inspection priorities.
- Problem to solve: Preparation for supervisory meetings draws on the Capital Management team to compile the current capital position, the open observation register, and the CFO's briefing note. The preparation cycle takes two to three days and produces a document that reflects the position at the time of assembly rather than the current state on the day of the meeting.
- Solution: The AI agent reads the current capital and liquidity position from live feeds, the open observation register, the regulator's most recent published consultation papers and inspection focus areas, and the Bank's prior meeting notes. It assembles a pre-meeting briefing covering current ratios and headroom, open observation status, recent regulator guidance relevant to the Bank's position, and a Q&A preparation section for topics likely to arise. The CFO and CRO review and edit the briefing; the AI agent refreshes ratio data on the morning of the meeting.
- OKR: The CFO and CRO receive a briefing before each scheduled supervisory meeting — current ratios and headroom, open observation status, relevant recent regulator guidance, and Q&A preparation — with ratio data refreshed on the morning of the meeting.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-assembled briefing used for ≥90% of scheduled supervisory meetings in year 1; all four briefing sections included. |
| Acceptance | ≥85% of briefings accepted by the CFO and CRO without material restructuring; ≥70% of topics raised by the regulator anticipated in the Q&A preparation section. |
| Cycle | Briefing assembled within 1 business day and current on the day of the meeting, vs. two to three days of preparation reflecting the position at the time of assembly in the prior process. |

### Supervisory Communications Drafting

- URN: urn:financial-services:scenario:finance-treasury/capital-management/supervisory-communications/supervisory-communications-drafting
- Lens: Enablement
- Complexity: M
- Intent: The AI agent drafts the Bank's written supervisory responses — ICAAP cover letters, Pillar 2 guidance acknowledgments, remediation plan responses, and replies to ad hoc data requests from the regulator — from current capital data and prior submission records.
- Problem to solve: Supervisory correspondence requires the CFO and CRO to produce regulator-ready narrative under fixed deadlines, with explicit consistency to prior submissions and direct responses to any methodology concerns the regulator has raised. Each response is treated as an isolated drafting exercise, with prior submissions referenced manually.
- Solution: The AI agent reads the incoming supervisory letter, the prior ICAAP and Pillar 2 submissions, and any open supervisory observations. It drafts a response that addresses each supervisory point directly, references the relevant prior submission passage, and maintains consistency with the Bank's established capital adequacy positions. Finance and the CRO review the draft and apply judgment on tone and regulatory relationship management before dispatch.
- OKR: Written supervisory responses — ICAAP cover letters, Pillar 2 guidance acknowledgments, remediation plan responses, and replies to ad hoc data requests from the regulator — are drafted from current capital data and prior submission records with explicit consistency to prior submissions and direct responses to each supervisory point.

| Dimension | Key result |
| --- | --- |
| Adoption | AI agent used to draft ≥80% of written supervisory responses to the regulator within year 1. |
| Acceptance | ≥85% of AI-drafted responses accepted by Finance and the CRO without material structural rewrite; prior submission passage references confirmed as accurate in ≥97% of reviewed responses. |
| Cycle | Supervisory response draft available for Finance review within 3 business days of the incoming letter, vs. 5–10 days of manual drafting and prior-submission cross-reference in the prior process. |

## ICAAP & stress capital {#icaap-stress-capital}

The Internal Capital Adequacy Assessment Process is the board-approved document submitted annually to the regulator that demonstrates the Bank's capital adequacy under base and stress scenarios. It covers Pillar 1 capital requirements, Pillar 2 add-ons, stress testing results, capital planning, and governance. Each submission requires several months of multi-team production and carries regulatory consequence if material errors are found.

### ICAAP Prior-Submission Delta Analysis

- URN: urn:financial-services:scenario:finance-treasury/capital-management/icaap-stress-capital/icaap-prior-submission-delta
- Lens: Automation
- Complexity: S
- Intent: The AI agent cross-reads the draft ICAAP submission and the prior-year approved submission to identify all material changes in methodology, assumptions, capital ratios, and scenario results, producing a tracked-change summary for CFO and CRO review before filing.
- Problem to solve: ICAAP submissions are reviewed internally for quality but without a systematic comparison to the prior approved submission. Material changes in methodology or scenario results that require proactive disclosure to the regulator — and that affect the supervisory relationship if the regulator finds them first — are tracked manually by the team that authored the relevant section.
- Solution: The AI agent reads the current draft and prior-year approved ICAAP document. It produces a structured delta summary covering changes in Pillar 1 and Pillar 2 methodology, scenario design and parameter changes, capital ratio trajectory, stress results, and governance narrative. Changes are ranked by materiality and flagged for CFO and CRO sign-off before filing. The delta summary is retained as evidence of proactive disclosure review.
- OKR: The CFO and CRO receive a materiality-ranked delta summary of all changes between the draft ICAAP and the prior-year approved submission — methodology, scenario design, capital ratio trajectory, stress results, and governance narrative — for sign-off before filing.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced delta summary used for ≥1 annual ICAAP submission cycle within year 1; all ICAAP sections compared. |
| Acceptance | ≥90% of changes ranked as material confirmed by the CFO and CRO; no material methodology or scenario change first identified by the regulator after filing. |
| Cycle | Delta summary available within 2 business days of each ICAAP draft, vs. changes tracked manually by the authoring teams in the prior process. |

### Stress Scenario Sensitivity Ranking

- URN: urn:financial-services:scenario:finance-treasury/capital-management/icaap-stress-capital/stress-scenario-sensitivity-ranking
- Lens: Insights
- Complexity: M
- Intent: The AI agent ranks the ICAAP stress scenarios by their capital consumption impact, decomposes each scenario's capital charge into its credit, market, operational risk, and Pillar 2 components, and identifies which BU portfolios drive the largest stress capital requirement.
- Problem to solve: ICAAP stress scenario outputs are presented as a set of ratio movements without a comparative sensitivity ranking. The CFO and Risk Committee cannot readily identify which scenario consumes the most capital, which risk type drives the stress, or which BU portfolios account for the majority of the stress charge — the distinctions that inform buffer sizing and management overlay decisions.
- Solution: The AI agent reads the stress scenario outputs from the capital model across all ICAAP scenarios and risk types. It ranks scenarios by total stressed capital consumption, decomposes each scenario's charge into credit, market, operational, and Pillar 2 components, and maps the largest credit stress charges to BU portfolios by product type and geography. The ranked output is presented alongside the narrative assessment to the Risk Committee and CFO. Capital Management validates methodology alignment before distribution.
- OKR: The Risk Committee and CFO receive the ICAAP stress scenarios ranked by total stressed capital consumption, with each scenario's charge decomposed by risk type and the largest credit stress charges mapped to BU portfolios.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced scenario ranking used for ≥1 annual ICAAP cycle within year 1; all ICAAP scenarios and risk types covered. |
| Acceptance | ≥85% of rankings and decompositions validated by Capital Management without material restatement; component charges reconcile to the capital model outputs in ≥98% of reviewed scenarios. |
| Cycle | Ranked output available within 3 business days of the stress model run, vs. ratio movements presented without comparative ranking in the prior process. |

### ICAAP Narrative Drafting

- URN: urn:financial-services:scenario:finance-treasury/capital-management/icaap-stress-capital/icaap-narrative-drafting
- Lens: Automation
- Complexity: L
- Intent: The AI agent drafts the ICAAP narrative from capital model outputs, stress results, and the prior submission, substantially reducing CFO and CRO drafting time across the annual production window. The generated document follows the regulator-prescribed structure and directly addresses prior-year supervisory observations.
- Problem to solve: The annual ICAAP submission to the regulator is a 60–120 page document requiring the CFO and CRO to synthesize capital model outputs, stress scenario results, business plan assumptions, and governance narrative into a regulator-ready format. The production window spans six to eight weeks and draws on Finance, Risk, and Treasury simultaneously.
- Solution: The AI agent reads capital model outputs, stress test results, business plan data, the prior ICAAP submission, and regulator feedback letters. It generates ICAAP sections in the prescribed structure — capital adequacy assessment, stress testing, Pillar 2 add-ons, and management overlays — and flags prior-year supervisory observations for explicit response in the current draft. Finance and Risk review and edit; the AI agent handles the drafting cycle.
- OKR: The ICAAP submission draft — structured per regulator prescription and explicitly addressing prior-year supervisory observations — is available for Finance and Risk review within 3 weeks of the data package being finalized, substantially reducing CFO and CRO drafting time across the annual production window.

| Dimension | Key result |
| --- | --- |
| Adoption | AI agent used to draft ≥80% of ICAAP section content for ≥1 annual submission cycle within year 1. |
| Acceptance | ≥80% of drafted ICAAP sections accepted by Finance and Risk without material structural rewrite; prior-year supervisory observations addressed directly in ≥95% of cases confirmed by Finance and Risk reviewers. |
| Cycle | ICAAP draft available for Finance and Risk review within 3 weeks of data package finalization, vs. 6–8 weeks of manual drafting across the production window in the prior process. |

## Dividend, AT1 & Tier 2 capital actions {#capital-actions}

Dividend policy, share buybacks, and, where the Bank issues such instruments, AT1/Tier 2 issuance are capital distribution and optimization decisions that require ALCO and board approval and, where the regulator requires it, prior supervisory notification. Each decision requires a capital headroom analysis, pro forma ratio impact, and a board narrative justifying the action relative to the capital plan.

### AT1 & Tier 2 Market Window Assessment

- URN: urn:financial-services:scenario:finance-treasury/capital-management/capital-actions/at1-tier2-market-window-assessment
- Lens: New opps
- Complexity: S
- Intent: Where the Bank issues AT1 or Tier 2 instruments, the AI agent synthesizes current market pricing for these instruments, peer issuance activity, and the Bank's forward capital plan to advise the CFO and Treasurer on whether current market conditions support issuance at an all-in cost within the Bank's approved pricing mandate.
- Problem to solve: Where the Bank issues AT1 or Tier 2 instruments, issuance decisions require the CFO and Treasurer to judge market timing — spread levels, peer transaction pricing, and investor demand signals — alongside the Bank's internal capital need. That market intelligence is assembled manually from broker notes and data terminals on an ad hoc basis, without a structured synthesis against the Bank's capital plan and pricing hurdle.
- Solution: The AI agent reads current AT1 and Tier 2 secondary spread data, recent peer issuance pricing and deal sizes, and the Bank's forward capital plan including projected buffer headroom. It assesses whether current all-in issuance cost falls within the Bank's approved pricing mandate and presents a market window assessment covering spread level, peer pricing context, and indicative issuance economics at the Bank's target size. The Treasurer and CFO use the assessment as primary briefing material before instructing syndicate banks. The AI agent does not execute any market transaction.
- OKR: The CFO and Treasurer receive a market window assessment — AT1 and Tier 2 spread levels, peer pricing context, and indicative issuance economics at the Bank's target size — showing whether the all-in cost falls within the approved pricing mandate.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced market window assessment used for ≥90% of AT1 and Tier 2 issuance decisions considered in year 1; spread, peer issuance, and capital plan inputs covered in each assessment. |
| Acceptance | ≥80% of assessments rated by the Treasurer and CFO as sufficient primary briefing material before instructing syndicate banks; indicative all-in cost within ±25 basis points of subsequent syndicate indications in ≥80% of cases. |
| Cycle | Assessment available within 1 business day of request, vs. ad hoc manual assembly from broker notes and data terminals in the prior process. |

### Capital Action Headroom Analysis

- URN: urn:financial-services:scenario:finance-treasury/capital-management/capital-actions/capital-action-headroom-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent computes the post-action CET1, Tier 1, and Total Capital ratio impact of a proposed dividend, buyback, or (where the Bank issues such instruments) AT1/Tier 2 call or issuance, stress-tests the post-action position under the ICAAP stress scenarios, and presents a headroom analysis to ALCO and the board before approval.
- Problem to solve: Capital distribution proposals — dividend declarations, share buybacks, and, where the Bank has such instruments, AT1 or Tier 2 calls — are assessed manually by the Capital Management team against current and projected ratios. The stress-tested headroom analysis required for ALCO and board approval is produced independently for each action, without a standardized framework that cross-references the stress capital requirement from the current ICAAP.
- Solution: The AI agent reads the current capital position, the approved ICAAP stress scenario results, and the proposed capital action parameters. It computes the pro forma CET1, Tier 1, and Total Capital ratios post-action, applies the ICAAP stress scenarios to the post-action position, and quantifies remaining headroom against regulatory minima, management buffers, and Pillar 2 guidance. The output is structured for ALCO presentation and board pack inclusion. Capital Management reviews and confirms the methodology before distribution to governance.
- OKR: ALCO and the board receive, before approving a proposed dividend, buyback, or AT1/Tier 2 call or issuance, a headroom analysis of pro forma CET1, Tier 1, and Total Capital ratios stress-tested under the ICAAP scenarios.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced headroom analysis used for ≥90% of capital action proposals presented to ALCO and the board in year 1. |
| Acceptance | ≥85% of analyses confirmed by Capital Management without methodology correction; pro forma ratios reconcile to the current capital position and ICAAP stress results in ≥98% of reviewed analyses. |
| Cycle | Headroom analysis available within 2 business days of the proposed action parameters, vs. an independent manual analysis for each action in the prior process. |

### Dividend Policy Scenario Modeling

- URN: urn:financial-services:scenario:finance-treasury/capital-management/capital-actions/dividend-policy-scenario-modelling
- Lens: Automation
- Complexity: M
- Intent: The AI agent models the capital ratio trajectory under multiple dividend payout scenarios — progressive, flat, and cut — across a three-year planning horizon, incorporating the approved ICAAP stress results and supervisory expectations, to support the annual dividend policy review.
- Problem to solve: The annual dividend policy review requires the CFO and board to assess distributable earnings against the capital plan across multiple payout scenarios. This analysis is built manually in a spreadsheet model by the Capital Management team, incorporating planning assumptions and stress outputs. Each scenario requires a full model rebuild, and the review cycle does not always complete before the board's target decision date.
- Solution: The AI agent reads the current capital position, the approved three-year capital plan, the ICAAP stress scenario outputs, and the current year's distributable earnings estimate. It runs the three standard dividend payout scenarios — progressive policy, flat payout, and payout cut — computing the CET1 trajectory under each scenario across three years and the distance to regulatory minima and management buffers in each. The scenario pack is formatted for board presentation, with the ICAAP stress overlay applied to each payout scenario. Capital Management reviews the output and adds qualitative context for the board before distribution.
- OKR: The CFO and board receive, for the annual dividend policy review, a scenario pack showing the three-year CET1 trajectory and distance to regulatory minima and management buffers under progressive, flat, and cut payout scenarios with the ICAAP stress overlay.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced dividend scenario pack used for ≥1 annual dividend policy review within year 1; all three standard payout scenarios modeled. |
| Acceptance | ≥85% of scenario packs accepted by Capital Management without material re-modeling; CET1 trajectories reconcile to the approved three-year capital plan in ≥98% of reviewed cells. |
| Cycle | Scenario pack available within 2 business days of the distributable earnings estimate and before the board's target decision date, vs. a full spreadsheet model rebuild per scenario in the prior process. |
