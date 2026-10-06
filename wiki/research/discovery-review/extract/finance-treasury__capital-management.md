# 

source: html-alt/financial-services/en/finance-treasury/capital-management/index.html


[PAGE TEXT]
CET1 & Tier 1 position
Current and projected CET1, Tier 1, and Total Capital ratios — maintained within NBKR, NBK/ARDFM, and CBR regulatory minima plus management buffers. The position is reported to ALCO monthly and to the board quarterly, with daily monitoring by the CFO and Treasury against management limits. Capital deductions, RWA movements, and AOCI changes all affect the ratio between reporting cycles.
Lens
Scenario
Intent
Complexity

### CARD 1 [Optimize|S] Capital Ratio Limit Proximity Alert
urn: urn:financial-services:scenario:finance-treasury/capital-management/cet1-tier1-position/capital-ratio-limit-proximity-alert
intent: Agent monitors the daily distance between the current capital position and each regulatory and management buffer threshold, and issues an attributed alert when intra-period movements bring any ratio within a defined proximity band before the next monthly report is scheduled.
Problem to solve: Between monthly reporting cycles, intra-period RWA growth, provision spikes, or AOCI movements can bring the capital ratio materially closer to a buffer threshold without triggering a formal alert. The CFO and Treasury become aware of the proximity only when the monthly report is assembled — by which point the management action window is narrower.
Solution: Agent reads daily capital feeds — current RWA components, CET1 deductions, AOCI, and retained earnings — and computes the live distance to each buffer threshold: regulatory minimum, management buffer, and ICAAP stress capital. When any ratio moves within a defined proximity band — configurable by the CFO's office — the agent issues an attributed alert summarising the current position, the remaining headroom, and the top three intra-period drivers of the movement. Treasury reviews the alert and determines management response.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Insights|M] CET1 Capital Headroom & Forward Projection
urn: urn:financial-services:scenario:finance-treasury/capital-management/cet1-tier1-position/cet1-capital-headroom-projection
intent: Agent projects CET1, Tier 1, and Total Capital ratios across a rolling 12-month horizon, surfaces headroom against NBKR, NBK/ARDFM, and CBR regulatory minima plus management buffers, and delivers a weekly ALCO capital update.
Problem to solve: The capital position is reported to ALCO monthly from data assembled across Finance, Risk, and Treasury. Emerging headroom pressure — from accelerating loan growth, provisioning spikes, or regulatory change — is identified only at the next scheduled cycle, leaving ALCO without a current forward view of the capital ratio trajectory between monthly reports.
Solution: Agent reads current capital feeds — RWA components, CET1 deductions, AOCI — and applies approved planning model assumptions to project the ratio trajectory. It identifies which drivers are tightening headroom fastest, computes distance to each regulatory minimum and management buffer, and produces a weekly ALCO capital narrative in a consistent format.
OKR objective: CET1, Tier 1, and Total Capital ratio trajectories over a rolling 12-month horizon are available to ALCO and the Treasurer each week, with headroom against NBKR, NBK/ARDFM, and CBR regulatory minima and management buffers quantified and driver-attributed in a consistent format.
OKR KR [Adoption]: Agent-produced weekly capital updates delivered for ≥48 of 52 weeks in year 1; projection covers all RWA components, CET1 deductions, and AOCI movements.
OKR KR [Acceptance]: ≥85% of weekly capital narratives accepted by the Treasury and Finance teams as current and accurate without material restatement; ratio projections reconcile to the monthly formal capital report within ±0.5 percentage points in ≥95% of weekly checks.
OKR KR [Cycle]: Weekly ALCO capital narrative available each Monday morning from current feeds, vs. monthly cycle only in the prior process.

### CARD 3 [Automation|M] RWA Movement Attribution
urn: urn:financial-services:scenario:finance-treasury/capital-management/cet1-tier1-position/rwa-movement-attribution
intent: Agent attributes each period's RWA movement to its drivers — new origination, model parameter changes, rating migrations, regulatory definition changes, and foreign exchange — and delivers a waterfall attribution to the CFO and Treasury on the first day of reporting.
Problem to solve: RWA movements are reported as a net period change without systematic driver attribution. When the capital ratio tightens unexpectedly, identifying whether the driver is volume growth, a model parameter change, a rating migration wave, or a regulatory definition update requires manual queries across the credit risk and capital systems — a process that takes two to four days and delays management response.
Solution: Agent reads the prior and current-period RWA data extracts across credit, market, and operational risk categories. It applies the bank's standard RWA attribution methodology — new business, parameter changes, model changes, definition changes, and FX — and produces a waterfall chart with materiality-ranked drivers. The attribution is available to the CFO and Treasury on the first day of reporting. Capital Management reviews and signs off the methodology application before the output is shared with ALCO.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Supervisory communications
Written supervisory dialog — ICAAP submission cover letters, remediation plan responses, Pillar 2 guidance acknowledgments, and ad hoc data requests from NBKR, NBK/ARDFM, or CBR — requires the CFO and CRO to produce regulator-ready narrative under fixed submission deadlines. Response quality, internal consistency with prior submissions, and alignment to the regulator's stated methodology concerns all affect the supervisory relationship.
Lens
Scenario
Intent
Complexity

### CARD 4 [Insights|S] Supervisory Observation Tracker
urn: urn:financial-services:scenario:finance-treasury/capital-management/supervisory-communications/supervisory-observation-tracker
intent: Agent maintains a structured register of all open supervisory observations from NBKR, NBK/ARDFM, and CBR — categorised by topic, due date, and closure status — and cross-references each new supervisory letter against open items to flag when a regulator is revisiting an unresolved concern.
Problem to solve: Supervisory observations from NBKR, NBK/ARDFM, and CBR are tracked in a manual register maintained by the Capital Management team. When a subsequent supervisory letter addresses a topic for which an observation is already open, the link between the two is identified through manual review of prior correspondence — a process that creates risk of inconsistent or delayed responses.
Solution: Agent reads each incoming supervisory letter and the current observation register. It extracts new observations, adds them to the structured register with categorisation by risk type and regulatory framework, and cross-references the letter's content against open items to identify where the regulator is revisiting a prior concern. The cross-reference output is presented to the CFO and CRO with the draft response for context. Capital Management maintains the register and confirms classification.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Automation|S] Regulatory Relationship Briefing
urn: urn:financial-services:scenario:finance-treasury/capital-management/supervisory-communications/regulatory-relationship-briefing
intent: Before scheduled supervisory meetings with NBKR, NBK/ARDFM, or CBR, agent assembles a briefing covering the bank's current capital and liquidity position, all open observations and pending responses, and the topics most likely to be raised based on the regulator's recent public guidance and inspection priorities.
Problem to solve: Preparation for supervisory meetings draws on the Capital Management team to compile the current capital position, the open observation register, and the CFO's briefing note. The preparation cycle takes two to three days and produces a document that reflects the position at the time of assembly rather than the current state on the day of the meeting.
Solution: Agent reads the current capital and liquidity position from live feeds, the open observation register, the regulator's most recent published consultation papers and inspection focus areas, and the bank's prior meeting notes. It assembles a pre-meeting briefing covering current ratios and headroom, open observation status, recent regulator guidance relevant to the bank's position, and a Q&A preparation section for topics likely to arise. The CFO and CRO review and edit the briefing; the agent refreshes ratio data on the morning of the meeting.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Enablement|M] Supervisory Communications Drafting
urn: urn:financial-services:scenario:finance-treasury/capital-management/supervisory-communications/supervisory-communications-drafting
intent: Agent drafts the bank's written supervisory responses — ICAAP cover letters, Pillar 2 guidance acknowledgments, remediation plan responses, and ad hoc data requests from NBKR, NBK/ARDFM, and CBR — from current capital data and prior submission records.
Problem to solve: Supervisory correspondence requires the CFO and CRO to produce regulator-ready narrative under fixed deadlines, with explicit consistency to prior submissions and direct responses to any methodology concerns the regulator has raised. Each response is treated as an isolated drafting exercise, with prior submissions referenced manually.
Solution: Agent reads the incoming supervisory letter, the prior ICAAP and Pillar 2 submissions, and any open regulator observations. It drafts a response that addresses each supervisory point directly, references the relevant prior submission passage, and maintains consistency with the bank's established capital adequacy positions. Finance reviews and applies judgment on tone and regulatory relationship management before dispatch.
OKR objective: Written supervisory responses — ICAAP cover letters, Pillar 2 guidance acknowledgments, remediation plan responses, and ad hoc data requests from NBKR, NBK/ARDFM, and CBR — are drafted from current capital data and prior submission records with explicit consistency to prior submissions and direct responses to each supervisory point.
OKR KR [Adoption]: Agent used to draft ≥80% of written supervisory responses to NBKR, NBK/ARDFM, and CBR within year 1.
OKR KR [Acceptance]: ≥85% of agent-drafted responses accepted by Finance and the CRO without material structural rewrite; prior submission passage references confirmed as accurate in ≥97% of reviewed responses.
OKR KR [Cycle]: Supervisory response draft available for Finance review within 3 business days of the incoming letter, vs. 5–10 days of manual drafting and prior-submission cross-reference in the prior process.

[PAGE TEXT]
ICAAP & stress capital
The Internal Capital Adequacy Assessment Process is the board-approved document submitted annually to NBKR, NBK/ARDFM, or CBR that demonstrates the bank's capital adequacy under base and stress scenarios. It covers Pillar 1 capital requirements, Pillar 2 add-ons, stress testing results, capital planning, and governance. Each submission requires several months of multi-team production and carries regulatory consequence if material errors are found.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] ICAAP Prior-Submission Delta Analysis
urn: urn:financial-services:scenario:finance-treasury/capital-management/icaap-stress-capital/icaap-prior-submission-delta
intent: Agent cross-reads the draft ICAAP submission and the prior-year approved submission to identify all material changes in methodology, assumptions, capital ratios, and scenario results, producing a tracked-change summary for CFO and regulator review before filing.
Problem to solve: ICAAP submissions are reviewed internally for quality but without a systematic comparison to the prior approved submission. Material changes in methodology or scenario results that require proactive disclosure to NBKR, NBK/ARDFM, or CBR — and that affect the supervisory relationship if identified first by the regulator — are tracked manually by the team that authored the relevant section.
Solution: Agent reads the current draft and prior-year approved ICAAP document. It produces a structured delta summary covering changes in Pillar 1 and Pillar 2 methodology, scenario design and parameter changes, capital ratio trajectory, stress results, and governance narrative. Changes are ranked by materiality and flagged for CFO and Chief Risk Officer sign-off before filing. The delta summary is retained as evidence of proactive disclosure review.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Insights|M] Stress Scenario Sensitivity Ranking
urn: urn:financial-services:scenario:finance-treasury/capital-management/icaap-stress-capital/stress-scenario-sensitivity-ranking
intent: Agent ranks the ICAAP stress scenarios by their capital consumption impact, decomposes each scenario's capital charge into its credit, market, and operational risk components, and identifies which BU portfolios drive the largest stress capital requirement.
Problem to solve: ICAAP stress scenario outputs are presented as a set of ratio movements without a comparative sensitivity ranking. The CFO and Risk Committee cannot readily identify which scenario consumes the most capital, which risk type drives the stress, or which BU portfolios account for the majority of the stress charge — the distinctions that inform buffer sizing and management overlay decisions.
Solution: Agent reads the stress scenario outputs from the capital model across all ICAAP scenarios and risk types. It ranks scenarios by total stressed capital consumption, decomposes each scenario's charge into credit, market, operational, and Pillar 2 components, and maps the largest credit stress charges to BU portfolios by product type and geography. The ranked output is presented alongside the narrative assessment to the Risk Committee and CFO. Capital Management validates methodology alignment before distribution.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Automation|L] ICAAP Narrative Drafting
urn: urn:financial-services:scenario:finance-treasury/capital-management/icaap-stress-capital/icaap-narrative-drafting
intent: Agent drafts the ICAAP narrative from capital model outputs, stress results, and the prior submission, substantially reducing CFO and CRO drafting time across the annual production window. The generated document follows the regulator-prescribed structure and directly addresses prior-year supervisory observations.
Problem to solve: The annual ICAAP submission to NBKR, NBK/ARDFM, or CBR is a 60–120 page document requiring the CFO and CRO to synthesize capital model outputs, stress scenario results, business plan assumptions, and governance narrative into a regulator-ready format. The production window spans six to eight weeks and draws on Finance, Risk, and Treasury simultaneously.
Solution: Agent reads capital model outputs, stress test results, business plan data, the prior ICAAP submission, and regulator feedback letters. It generates ICAAP sections in the prescribed structure — capital adequacy assessment, stress testing, Pillar 2 add-ons, and management overlays — and flags prior-year regulator observations for explicit response in the current draft. Finance and Risk review and edit; the agent handles the drafting cycle.
OKR objective: The ICAAP submission draft — structured per regulator prescription and explicitly addressing prior-year supervisory observations — is available for Finance and Risk review within 3 weeks of the data package being finalised, substantially reducing CFO and CRO drafting time across the annual production window.
OKR KR [Adoption]: Agent used to draft ≥80% of ICAAP section content for ≥1 annual submission cycle within year 1 across NBKR, NBK/ARDFM, or CBR perimeters as applicable.
OKR KR [Acceptance]: ≥80% of drafted ICAAP sections accepted by Finance and Risk without material structural rewrite; prior-year supervisory observations addressed directly in ≥95% of cases confirmed by the Compliance team.
OKR KR [Cycle]: ICAAP draft available for Finance and Risk review within 3 weeks of data package finalisation, vs. 6–8 weeks of manual drafting across the production window in the prior process.

[PAGE TEXT]
Dividend, AT1 & Tier 2 capital actions
Dividend policy, share buybacks, and AT1/Tier 2 issuance are capital distribution and optimisation decisions that require ALCO and board approval, and in some jurisdictions prior supervisory notification under NBKR, NBK/ARDFM, and CBR frameworks. Each decision requires a capital headroom analysis, pro forma ratio impact, and a board narrative justifying the action relative to the capital plan.
Lens
Scenario
Intent
Complexity

### CARD 10 [New opps|S] AT1 & Tier 2 Market Window Assessment
urn: urn:financial-services:scenario:finance-treasury/capital-management/capital-actions/at1-tier2-market-window-assessment
intent: Agent synthesises current AT1 and Tier 2 market pricing, peer issuance activity, and the bank's forward capital plan to advise the CFO and Treasurer on whether current market conditions support issuance at an all-in cost within the bank's approved pricing mandate.
Problem to solve: AT1 and Tier 2 issuance decisions require the CFO and Treasurer to judge market timing — spread levels, peer transaction pricing, and investor demand signals — alongside the bank's internal capital need. That market intelligence is assembled manually from broker notes and data terminals on an ad hoc basis, without a structured synthesis against the bank's capital plan and pricing hurdle.
Solution: Agent reads current AT1 and Tier 2 secondary spread data, recent peer issuance pricing and deal sizes, and the bank's forward capital plan including projected buffer headroom. It assesses whether current all-in issuance cost falls within the bank's approved pricing mandate and presents a market window assessment covering spread level, peer pricing context, and indicative issuance economics at the bank's target size. The Treasurer and CFO use the assessment as primary briefing material before instructing syndicate banks. Agent does not execute any market transaction.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Insights|M] Capital Action Headroom Analysis
urn: urn:financial-services:scenario:finance-treasury/capital-management/capital-actions/capital-action-headroom-analysis
intent: Agent computes the post-action CET1, Tier 1, and Total Capital ratio impact of a proposed dividend, buyback, or AT1/Tier 2 call or issuance, stress-tests the post-action position under the ICAAP stress scenarios, and presents a headroom analysis to ALCO and the board before approval.
Problem to solve: Capital distribution proposals — dividend declarations, share buybacks, and AT1 or Tier 2 calls — are assessed manually by the Capital Management team against current and projected ratios. The stress-tested headroom analysis required for ALCO and board approval is produced independently for each action, without a standardised framework that cross-references the stress capital requirement from the current ICAAP.
Solution: Agent reads the current capital position, the approved ICAAP stress scenario results, and the proposed capital action parameters. It computes the pro forma CET1, Tier 1, and Total Capital ratios post-action, applies the ICAAP stress scenarios to the post-action position, and quantifies remaining headroom against regulatory minima, management buffers, and Pillar 2 guidance. The output is structured for ALCO presentation and board pack inclusion. Capital Management reviews and confirms the methodology before distribution to governance.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Automation|M] Dividend Policy Scenario Modelling
urn: urn:financial-services:scenario:finance-treasury/capital-management/capital-actions/dividend-policy-scenario-modelling
intent: Agent models the capital ratio trajectory under multiple dividend payout scenarios — progressive, flat, and cut — across a three-year planning horizon, incorporating the approved ICAAP stress results and NBKR, NBK/ARDFM, or CBR supervisory expectations, to support the annual dividend policy review.
Problem to solve: The annual dividend policy review requires the CFO and board to assess distributable earnings against the capital plan across multiple payout scenarios. This analysis is built manually in a spreadsheet model by the Capital Management team, incorporating planning assumptions and stress outputs. Each scenario requires a full model rebuild, and the review cycle does not always complete before the board's target decision date.
Solution: Agent reads the current capital position, the approved three-year capital plan, the ICAAP stress scenario outputs, and the current year's distributable earnings estimate. It runs the three standard dividend payout scenarios — progressive policy, flat payout, and payout cut — computing the CET1 trajectory under each scenario across three years and the distance to regulatory minima and management buffers in each. The scenario pack is formatted for board presentation, with the ICAAP stress overlay applied to each payout scenario. Capital Management reviews the output and adds the board's qualitative context before distribution.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
