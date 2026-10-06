# 

source: html-alt/financial-services/en/finance-treasury/performance-measurement/index.html


[PAGE TEXT]
Segment P&L & management accounts
Segment P&L with cost and capital allocations is the primary management view the CFO and segment heads use to assess BU performance — revenue, NIM, fee income, operating costs, provisions, allocated capital cost, and net income. The management accounts narrative synthesizes segment performance into a coherent picture for the executive committee and board.
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|S] Segment NIM Driver Analysis
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/segment-pl/segment-nim-driver-analysis
intent: Agent decomposes each segment's net interest margin into asset yield, liability cost, FTP credit, and FTP charge components, and attributes the period-on-period NIM movement to volume, rate, and mix effects — enabling CFO and segment heads to identify the source of NIM compression before the ALCO discussion.
Problem to solve: Segment P&L reports the net interest margin as a single figure without driver decomposition. When a segment's NIM compresses, the CFO and segment head cannot determine from the management accounts alone whether the compression reflects a decline in asset yield, a rise in deposit cost, a change in the FTP curve, or a shift in product mix — each requiring a different management response.
Solution: Agent reads the segment's asset and liability volume and rate data, the FTP credit and charge schedule, and the prior-period actuals. It decomposes the segment NIM into asset yield, liability cost, and net FTP contribution, and applies a rate-volume-mix attribution to the period-on-period NIM change. The decomposition is appended to the monthly segment P&L pack as an additional page. CFO and segment heads use the decomposition to direct pricing, mix, or FTP curve review actions to the material driver.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Optimize|S] Cost Allocation Quality Review
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/segment-pl/cost-allocation-quality-review
intent: Agent reviews the period's cost allocation model outputs — shared service cost allocations, technology cost distributions, and central function charges to segments — for movements that exceed defined materiality thresholds, and flags anomalous allocations for Finance review before the segment P&L is finalised.
Problem to solve: Cost allocations to segments are computed by the Finance shared services team using allocation keys that are updated periodically but not validated each period for movement reasonableness. Anomalous allocations — from a mis-configured key or a one-time volume spike in a cost pool — are identified by segment finance teams when they query the management accounts, adding one to two days to the close cycle.
Solution: Agent reads the current-period cost allocation outputs and the prior three-period history for each allocation pool and segment. It computes the period-on-period movement for each cost allocation and flags any allocation where the movement exceeds the defined materiality threshold — either as an absolute amount or as a percentage deviation from the trailing average. Flagged allocations are presented to the Finance shared services team for review before the segment P&L is released. The team confirms or corrects each flagged item; the agent does not change any allocation.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Automation|M] Management Accounts Narrative
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/segment-pl/management-accounts-narrative
intent: Agent drafts the monthly management accounts commentary from the consolidated P&L, BU submissions, and prior-period narrative, delivering a CFO-ready pack before the executive committee meeting.
Problem to solve: The monthly management accounts commentary is assembled by Controllers and segment finance teams from BU submissions and the consolidated P&L. Draft quality varies by BU and by the analyst assigned; the CFO's review window compresses because narrative is available only after the full data pack is assembled.
Solution: Agent reads the consolidated P&L, BU-level submissions, approved budget, and prior-month narrative. It generates the management accounts commentary in the house format — headline performance, segment bridges, one-time item flagging, and outlook section — with BU commentary normalised to a consistent register. CFO reviews and adds forward judgment before distribution.
OKR objective: The monthly management accounts commentary — covering headline performance, segment bridges, one-time item flagging, and the outlook section — is drafted from the consolidated P&L and BU submissions in a consistent register and available for CFO review before the executive committee meeting.
OKR KR [Adoption]: Agent used to draft the monthly management accounts narrative for ≥10 of 12 monthly cycles in year 1; all prescribed commentary sections covered in each cycle.
OKR KR [Acceptance]: ≥85% of management accounts narratives accepted by the CFO without material structural rewrite; BU commentary normalisation confirmed as consistent in register and materiality framing in ≥90% of reviewed cycles.
OKR KR [Cycle]: Management accounts narrative available for CFO review the day the data pack is assembled, vs. 1–2 days of additional drafting delay in the prior process.

[PAGE TEXT]
RAROC & EVA attribution by BU
RAROC and EVA attribution by BU is the quarterly performance measure that links commercial results to risk budget consumed — the return metric by which capital is allocated and pricing hurdles are set. Under Basel II Pillar 2 and regional ICAAP guidance, RAROC must inform capital allocation decisions. The quarterly attribution requires combining risk-weighted assets, expected loss, and P&L from Finance and Risk systems.
Lens
Scenario
Intent
Complexity

### CARD 4 [Insights|S] RAROC Hurdle Monitoring
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/raroc-by-bu/raroc-limit-breach-early-warning
intent: Agent monitors each BU's quarterly RAROC trajectory against the board-approved hurdle rate and projects whether the trailing-four-quarter RAROC will fall below the hurdle before the next formal capital allocation review, enabling management intervention before the breach occurs.
Problem to solve: RAROC by BU is computed quarterly and reported to the Risk Committee and CFO at the formal quarterly attribution cycle. A BU whose RAROC is drifting toward the hurdle rate from above does not receive a formal alert until the quarterly attribution confirms the breach — at which point the management response options are narrower.
Solution: Agent reads the quarterly RAROC attribution outputs for each BU and maintains a trailing-four-quarter RAROC series. It fits a trend to each BU's RAROC trajectory and projects the forward trajectory over the next two quarters. When the projection shows any BU's RAROC reaching the hurdle within the projection horizon, a forward-looking flag is issued to the CFO and relevant BU finance head with the trend attribution — identifying whether the drift reflects margin compression, RWA inflation, or provision build. Capital Management uses the flag to initiate a targeted RAROC improvement plan before the formal breach.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Enablement|M] RAROC & EVA Attribution by BU
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/raroc-by-bu/raroc-eva-attribution
intent: Agent computes quarterly RAROC and EVA by business unit from risk-weighted assets, expected loss allocations, and P&L feeds, and produces the attribution narrative with comparison against board-set hurdles and prior-quarter trend.
Problem to solve: RAROC and EVA attribution by BU requires combining RWA, expected loss, and P&L from Finance and Risk systems — a cross-system assembly that Finance and Risk teams negotiate each quarter. The attribution is produced once per quarter, limiting the CFO's ability to identify return deterioration within the quarter before the formal cycle.
Solution: Agent reads the current-period P&L, RWA by BU, expected loss allocations, and the approved cost-of-capital schedule. It computes RAROC and EVA per BU, compares each result against the board-set hurdle and prior-quarter trend, and generates the attribution narrative with driver decomposition for the CFO and segment heads. Capital allocation decisions remain with ALCO; the agent provides the analysis.
OKR objective: Quarterly RAROC and EVA by business unit — computed from risk-weighted assets, expected loss allocations, and P&L feeds, with comparison against board-set hurdles and prior-quarter trend — are available to the CFO and segment heads with driver decomposition.
OKR KR [Adoption]: Agent-produced RAROC/EVA attribution used for ≥4 quarterly reporting cycles within year 1; all active business units covered in each attribution.
OKR KR [Acceptance]: ≥85% of RAROC/EVA attribution outputs accepted by Finance and Risk without material restatement; RWA and expected loss inputs reconcile to source system data in ≥98% of reviewed quarters.
OKR KR [Cycle]: RAROC/EVA attribution available within 3 business days of quarter-end P&L close, vs. 1–2 weeks of cross-system Finance/Risk assembly in the prior process.

### CARD 6 [Automation|M] RAROC Product Portfolio Decomposition
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/raroc-by-bu/raroc-product-portfolio-decomposition
intent: Agent decomposes each BU's RAROC into its product-level components — by loan product, deposit product, and fee income stream — identifying which products within the BU are above and below the hurdle rate, and presenting the decomposition alongside the quarterly BU RAROC report.
Problem to solve: RAROC is reported at the BU level, which may mask product-level return dispersion. A BU reporting a RAROC above the hurdle rate may contain product lines with returns below the hurdle that are offset by high-return products elsewhere — information that is relevant to product mix decisions, pricing hurdle calibration, and capital reallocation but is not visible in the BU aggregate.
Solution: Agent reads the BU P&L at the product level, the allocated RWA by product, and the expected loss by product from the IFRS 9 model. It computes RAROC at the product level within each BU, identifies products above and below the hurdle, and presents the decomposition as an annex to the quarterly BU RAROC report. CFO and BU heads use the decomposition to assess whether capital reallocation, product pricing adjustment, or origination constraint is warranted for below-hurdle products. Capital Management confirms the RWA allocation methodology before distribution.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Budget-to-actual variance & attribution
Monthly budget-to-actual variance attribution by segment decomposes the gap between plan and actual across revenue, cost, and provision dimensions, identifying whether variances are volume-driven, margin-driven, or one-time. The attribution is the basis for CFO and segment head action decisions during the month — not just a retrospective record of what happened.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] Budget Variance Action Tracker
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/budget-variance-attribution/budget-variance-action-tracker
intent: Agent maintains a structured tracker of management actions committed in response to material budget variances — action owner, target period, expected P&L impact, and resolution status — and updates the CFO on action completion rates at each monthly review.
Problem to solve: Management actions committed in response to budget variances are recorded in meeting minutes and tracked informally by BU finance teams. The CFO has no systematic view of which actions from prior periods have been completed, which remain open, and whether the expected P&L recovery has been achieved — the information needed to distinguish performance recovery from continuing deterioration.
Solution: Agent reads the minutes of each monthly performance review and the budget variance attribution output. It extracts committed actions, assigns owner and target period from the discussion, and appends them to the structured action tracker. Each month it cross-references the tracker against the current attribution output to determine whether the expected P&L recovery is visible in the actuals. The CFO reviews the tracker update — showing open actions, actions closed with evidence of impact, and actions closed without measurable impact — at each monthly performance session.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Optimize|S] Segment P&L Forward Run-Rate Signal
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/budget-variance-attribution/segment-pl-forward-run-rate
intent: Agent combines the current period's attributed P&L variance with the segment's own forward trading signals — pipeline volumes, deposit book repricing schedule, and cost accrual run rate — to produce a forward run-rate estimate for each segment at mid-month.
Problem to solve: Segment performance reviews are retrospective — the attributed variance for the closed period is available but no forward signal is produced until the quarterly reforecast. Segment heads and the CFO manage the remainder of the current period without a quantified view of whether the forward run rate implies the budget gap will widen or close.
Solution: Agent reads the current-period attributed variance, the segment's pipeline and origination data, deposit repricing notices, and cost accrual estimates. It applies the prior-period attribution methodology to the forward drivers and produces a mid-month run-rate estimate per segment — showing the estimated full-period outturn relative to budget and the assumptions driving the estimate. FP&A reviews the output and confirms or adjusts the run-rate assumptions before distribution to segment heads. The signal is produced around day 15 of each month.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Insights|M] Segment Performance Variance Attribution
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/budget-variance-attribution/performance-variance-attribution-daily
intent: Agent decomposes the monthly budget-to-actual variance for each segment into volume, NIM, fee income, cost, and provision components, ranks variances by consolidated P&L impact, and delivers an attributed performance pack to the CFO and segment heads on the first day of reporting.
Problem to solve: Segment performance variance analysis is produced by each BU finance team in formats that vary across units. The CFO receives a consolidated variance figure without a consistent driver decomposition, and identifying whether a segment's shortfall reflects a volume miss, a margin compression, or a provisioning spike requires manual queries back to each BU team — extending the time to management action by two to three days.
Solution: Agent reads the closed management accounts and approved budget for each segment. It applies a standardised decomposition — separating volume-driven, rate-driven, mix, fee income, cost, and provision variances for each segment — and produces a consolidated pack with variances ranked by absolute P&L impact. The pack is available to the CFO and segment heads on day one of reporting. Each segment lead reviews the attributed output and adds qualitative context; the CFO uses the ranked view to direct the management response.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Lending portfolio attribution & CECL / IFRS 9
Lending portfolio performance attribution — vintage cohort default rates, driver decomposition by channel, scorecard, and geography, and provision sensitivity analysis under CECL or IFRS 9 — is the primary analytical tool for the CFO and CRO to assess credit performance and estimate provision requirements. The quarterly provision cycle requires 200–400 team-hours across Finance, Risk, and Credit Modeling.
Lens
Scenario
Intent
Complexity

### CARD 10 [Insights|M] Lending Portfolio Performance Attribution
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/lending-default-attribution/lending-portfolio-performance-attribution
intent: Agent tracks cumulative default rates by vintage cohort, decomposes performance variance across channel, scorecard, geography, and product, and pre-computes IFRS 9 provision sensitivities under base and stress scenarios.
Problem to solve: The quarterly IFRS 9 provision cycle requires Finance, Risk, and Credit Modelling to reconcile cohort-vintage default data, attribute performance variance across origination dimensions, and stress provision estimates through several rounds of iteration. Attribution frequently remains at cohort level without decomposing channel mix, scorecard drift, or geography as contributing factors.
Solution: Agent reads the loan tape, origination attributes, and IFRS 9 model parameters. It computes cumulative default rates by vintage cohort, decomposes performance variance across channel, scorecard, geography, and product, and produces provision sensitivity estimates under base, stress, and severe scenarios with macro overlay assumptions made explicit. CFO and Risk Committee review the attribution output; provision methodology decisions remain with the credit modeling team.
OKR objective: Cumulative default rates by vintage cohort, performance variance decomposed across channel, scorecard, geography, and product, and IFRS 9 provision sensitivities under base and stress scenarios are available for Finance, Risk, and Credit Modelling review each quarter-end.
OKR KR [Adoption]: Agent-produced portfolio performance attribution used for ≥4 quarterly IFRS 9 provision cycles within year 1; all prescribed attribution dimensions covered.
OKR KR [Acceptance]: ≥85% of attribution outputs accepted by the Credit Modelling team as sufficient for provision committee review without supplementary manual analysis; provision sensitivity estimates reconcile to the credit risk model within ±5% on periodic validation.
OKR KR [Cycle]: Portfolio attribution and provision sensitivity estimates available within 3 business days of the quarterly data close, vs. 2–3 weeks of cross-team iteration in the prior process.

### CARD 11 [Automation|M] Provision Sensitivity Scenario Analysis
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/lending-default-attribution/provision-sensitivity-scenario-analysis
intent: Agent runs multiple economic scenario overlays on the IFRS 9 ECL model to compute the P&L range of provision outcomes under base, adverse, and severe scenarios, and presents the scenario-weighted provision estimate and sensitivity range to the CFO and external auditor before each quarter-end close.
Problem to solve: IFRS 9 requires the ECL provision to incorporate forward-looking economic scenarios weighted by probability. The scenario overlay is applied manually to the base ECL model output, and the range of provision outcomes under the approved scenario set is not systematically available to the CFO before the close cycle. The external auditor's substantive testing targets the scenario weighting methodology, and late changes to the overlay create audit timeline risk.
Solution: Agent reads the base ECL model output, the approved economic scenario inputs and probability weights, and the portfolio segmentation. It applies each economic scenario overlay to the ECL model inputs and computes the provision outcome per scenario and per portfolio segment. The scenario-weighted consolidated provision estimate and the full sensitivity range — from base to severe — are presented to the CFO and audit committee before the close cycle begins. External auditors receive the scenario methodology documentation in the same package.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Optimize|M] Vintage Cohort Default Tracking
urn: urn:financial-services:scenario:finance-treasury/performance-measurement/lending-default-attribution/vintage-cohort-default-tracking
intent: Agent tracks default and stage migration rates by vintage cohort, product, and origination channel on a monthly basis, and identifies cohorts whose default trajectory diverges from the IFRS 9 model's expected pattern — an early signal for provisioning model recalibration.
Problem to solve: IFRS 9 staging decisions rely on the ECL model's forward-looking default probability estimates. When the actual default trajectory of a recently originated cohort diverges materially from the model's expectation, the divergence is identified in the model's annual backtesting cycle rather than in the close period when the cohort exits its expected performance window. Early identification would allow model recalibration or management overlay before the provision impact is booked.
Solution: Agent reads the monthly loan performance data and maps each disbursement to its vintage cohort, product, and channel. It tracks the cumulative default and stage 2 migration rate for each cohort against the IFRS 9 model's expected trajectory for that cohort type, and flags cohorts where actual performance deviates from expectation by more than the defined tolerance. The flagged cohorts are presented to Credit Modeling and the CFO with the estimated provision impact of a model recalibration. Credit Modeling determines whether a management overlay or model update is warranted.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
