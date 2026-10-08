# Performance measurement

Performance measurement translates the Bank's financial results into a management view — segment, product, and customer-level P&L with cost and capital allocations — and into risk-adjusted return metrics that link commercial performance to the risk budget consumed. RAROC, EVA, and return on risk-weighted assets are the measures by which the CFO assesses whether each BU creates or destroys value net of the cost of capital. Under Pillar 2 of the Basel framework and supervisory ICAAP guidance, risk-adjusted performance measures are expected to inform capital allocation and strategic planning. **The GenAI opportunity is continuous management reporting — moving from quarterly segment P&L reviews to monthly driver-attributed packs and continuous RAROC monitoring against board-set hurdles.**

## Problems

### Profit attribution {#profit-attribution}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Segment-level P&L — with cost and capital allocations — is assembled quarterly across BUs by combining finance and risk data from separate systems. The quarterly review meeting is consumed by data walkthrough, leaving limited time for the strategic discussion the segment heads and CFO need to have. Cross-segment dynamics — one BU's deposit pricing pulling from another's funding cost — are not visible in the individual-segment view. |
| Enablement | Allocation methodology disputes recur each quarter as segment heads challenge cost and capital allocation assumptions they cannot verify independently. Finance teams spend significant review-meeting bandwidth defending allocation methodology rather than discussing performance trends and management actions. |
| Automation | Monthly management accounts commentary, quarterly segment performance bridges, and CFO board preparation materials are assembled manually from P&L reports, allocation schedules, and prior-period narratives. Each document has a stable structure and known inputs; assembly is the constraint. |
| New business opportunities | Segment finance teams with a continuously attributed P&L view can identify margin erosion in time for commercial action — repricing, origination mix adjustment, or cost reduction — before the quarter closes. Teams receiving quarterly snapshots respond to the outcome; teams with monthly or weekly driver attribution manage the trajectory. |

## Segment P&L & management accounts {#segment-pl}

Segment P&L with cost and capital allocations is the primary management view the CFO and segment heads use to assess BU performance — revenue, NIM, fee income, operating costs, provisions, allocated capital cost, and net income. The management accounts narrative synthesizes segment performance into a coherent picture for the executive committee and board.

### Segment NIM Driver Analysis

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/segment-pl/segment-nim-driver-analysis
- Lens: Insights
- Complexity: S
- Intent: The AI agent decomposes each segment's net interest margin into asset yield, liability cost, FTP credit, and FTP charge components, and attributes the period-on-period NIM movement to volume, rate, and mix effects — enabling the CFO and segment heads to identify the source of NIM compression before the ALCO discussion.
- Problem to solve: Segment P&L reports the net interest margin as a single figure without driver decomposition. When a segment's NIM compresses, the CFO and segment head cannot determine from the management accounts alone whether the compression reflects a decline in asset yield, a rise in deposit cost, a change in the FTP curve, or a shift in product mix — each requiring a different management response.
- Solution: The AI agent reads the segment's asset and liability volume and rate data, the FTP credit and charge schedule, and the prior-period actuals. It decomposes the segment NIM into asset yield, liability cost, and net FTP contribution, and applies a rate-volume-mix attribution to the period-on-period NIM change. The decomposition is appended to the monthly segment P&L pack as an additional page. The CFO and segment heads use the decomposition to direct pricing, mix, or FTP curve review actions to the material driver.
- OKR: The CFO and segment heads receive, with the monthly segment P&L pack, a decomposition of each segment's NIM into asset yield, liability cost, and net FTP contribution, with the period-on-period change attributed to rate, volume, and mix.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced NIM decomposition appended to ≥10 of 12 monthly segment P&L packs in year 1; all segments covered. |
| Acceptance | ≥85% of decompositions accepted by the CFO and segment heads without material restatement; components reconcile to the reported segment NIM in ≥98% of reviewed packs. |
| Cycle | NIM driver view available with the monthly segment P&L pack, before the ALCO discussion, vs. a single NIM figure without driver decomposition in the prior process. |

### Cost Allocation Quality Review

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/segment-pl/cost-allocation-quality-review
- Lens: Optimize
- Complexity: S
- Intent: The AI agent reviews the period's cost allocation model outputs — shared service cost allocations, technology cost distributions, and central function charges to segments — for movements that exceed defined materiality thresholds, and flags anomalous allocations for Finance review before the segment P&L is finalized.
- Problem to solve: Cost allocations to segments are computed by the Finance shared services team using allocation keys that are updated periodically but not validated each period for movement reasonableness. Anomalous allocations — from a mis-configured key or a one-time volume spike in a cost pool — are identified by segment finance teams when they query the management accounts, adding one to two days to the close cycle.
- Solution: The AI agent reads the current-period cost allocation outputs and the prior three-period history for each allocation pool and segment. It computes the period-on-period movement for each cost allocation and flags any allocation where the movement exceeds the defined materiality threshold — either as an absolute amount or as a percentage deviation from the trailing average. Flagged allocations are presented to the Finance shared services team for review before the segment P&L is released. The team confirms or corrects each flagged item; the AI agent does not change any allocation.
- OKR: The Finance shared services team receives a list of cost allocations whose period-on-period movement exceeds the materiality threshold — by allocation pool and segment — before the segment P&L is released.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced allocation review run for ≥10 of 12 monthly close cycles in year 1; all allocation pools and segments covered. |
| Acceptance | ≥70% of flagged allocations confirmed by the Finance shared services team as warranting review, whether confirmed or corrected; allocation queries raised by segment finance teams after release reduced by ≥50% vs. the pre-deployment baseline. |
| Cycle | Anomalous allocations identified before the segment P&L is released, vs. one to two days added to the close cycle by segment finance queries in the prior process. |

### Management Accounts Narrative

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/segment-pl/management-accounts-narrative
- Lens: Automation
- Complexity: M
- Intent: The AI agent drafts the monthly management accounts commentary from the consolidated P&L, BU submissions, and prior-period narrative, delivering a CFO-ready pack before the executive committee meeting.
- Problem to solve: The monthly management accounts commentary is assembled by Controllers and segment finance teams from BU submissions and the consolidated P&L. Draft quality varies by BU and by the analyst assigned; the CFO's review window compresses because narrative is available only after the full data pack is assembled.
- Solution: The AI agent reads the consolidated P&L, BU-level submissions, approved budget, and prior-month narrative. It generates the management accounts commentary in the house format — headline performance, segment bridges, one-time item flagging, and outlook section — with BU commentary normalized to a consistent register. The CFO reviews and adds forward judgment before distribution.
- OKR: The monthly management accounts commentary — covering headline performance, segment bridges, one-time item flagging, and the outlook section — is drafted from the consolidated P&L and BU submissions in a consistent register and available for CFO review before the executive committee meeting.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted management accounts narrative used for ≥10 of 12 monthly cycles in year 1; all prescribed commentary sections covered in each cycle. |
| Acceptance | ≥85% of management accounts narratives accepted by the CFO without material structural rewrite; BU commentary normalization confirmed as consistent in register and materiality framing in ≥90% of reviewed cycles. |
| Cycle | Management accounts narrative available for CFO review the day the data pack is assembled, vs. 1–2 days of additional drafting delay in the prior process. |

## RAROC & EVA attribution by BU {#raroc-by-bu}

RAROC and EVA attribution by BU is the quarterly performance measure that links commercial results to risk budget consumed — the return metric by which capital is allocated and pricing hurdles are set. Under Pillar 2 of the Basel framework and supervisory ICAAP guidance, capital allocation is expected to reflect risk, and RAROC is the measure the Bank uses for it. The quarterly attribution requires combining risk-weighted assets, expected loss, and P&L from Finance and Risk systems.

### RAROC Hurdle Monitoring

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/raroc-by-bu/raroc-limit-breach-early-warning
- Lens: Insights
- Complexity: S
- Intent: The AI agent monitors each BU's quarterly RAROC trajectory against the board-approved hurdle rate and projects whether the trailing-four-quarter RAROC will fall below the hurdle before the next formal capital allocation review, enabling management intervention before the breach occurs.
- Problem to solve: RAROC by BU is computed quarterly and reported to the Risk Committee and CFO at the formal quarterly attribution cycle. A BU whose RAROC is drifting toward the hurdle rate from above does not receive a formal alert until the quarterly attribution confirms the breach — at which point the management response options are narrower.
- Solution: The AI agent reads the quarterly RAROC attribution outputs for each BU and maintains a trailing-four-quarter RAROC series. It fits a trend to each BU's RAROC trajectory and projects the forward trajectory over the next two quarters. When the projection shows any BU's RAROC reaching the hurdle within the projection horizon, a forward-looking flag is issued to the CFO and relevant BU finance head with the trend attribution — identifying whether the drift reflects margin compression, RWA inflation, or provision build. Capital Management uses the flag to initiate a targeted RAROC improvement plan before the formal breach.
- OKR: The CFO and the relevant BU finance head receive a forward-looking flag, with trend attribution, when a BU's trailing-four-quarter RAROC is projected to reach the board-approved hurdle rate within the next two quarters.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-maintained RAROC trend series updated for ≥4 quarterly attribution cycles within year 1; all BUs monitored. |
| Acceptance | ≥75% of forward-looking flags confirmed by Capital Management as warranting a targeted RAROC improvement plan; trend attribution to margin compression, RWA inflation, or provision build accepted by the BU finance head in ≥85% of flags. |
| Cycle | Drift toward the hurdle flagged up to two quarters ahead, vs. a formal alert only when the quarterly attribution confirms the breach in the prior process. |

### RAROC & EVA Attribution by BU

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/raroc-by-bu/raroc-eva-attribution
- Lens: Enablement
- Complexity: M
- Intent: The AI agent computes quarterly RAROC and EVA by business unit from risk-weighted assets, expected loss allocations, and P&L feeds, and produces the attribution narrative with comparison against board-set hurdles and prior-quarter trend.
- Problem to solve: RAROC and EVA attribution by BU requires combining RWA, expected loss, and P&L from Finance and Risk systems — a cross-system assembly that Finance and Risk teams negotiate each quarter. The assembly takes one to two weeks, so the attribution reaches the CFO and segment heads well after quarter-end and without a consistent driver decomposition.
- Solution: The AI agent reads the current-period P&L, RWA by BU, expected loss allocations, and the approved cost-of-capital schedule. It computes RAROC and EVA per BU, compares each result against the board-set hurdle and prior-quarter trend, and generates the attribution narrative with driver decomposition for the CFO and segment heads. Finance and Risk review the output; capital allocation decisions remain with ALCO, and the AI agent provides the analysis.
- OKR: Quarterly RAROC and EVA by business unit — computed from risk-weighted assets, expected loss allocations, and P&L feeds, with comparison against board-set hurdles and prior-quarter trend — are available to the CFO and segment heads with driver decomposition.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced RAROC/EVA attribution used for ≥4 quarterly reporting cycles within year 1; all active business units covered in each attribution. |
| Acceptance | ≥85% of RAROC/EVA attribution outputs accepted by Finance and Risk without material restatement; RWA and expected loss inputs reconcile to source system data in ≥98% of reviewed quarters. |
| Cycle | RAROC/EVA attribution available within 3 business days of quarter-end P&L close, vs. 1–2 weeks of cross-system Finance/Risk assembly in the prior process. |

### RAROC Product Portfolio Decomposition

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/raroc-by-bu/raroc-product-portfolio-decomposition
- Lens: Automation
- Complexity: M
- Intent: The AI agent decomposes each BU's RAROC into its product-level components — by loan product, deposit product, and fee income stream — identifying which products within the BU are above and below the hurdle rate, and presenting the decomposition alongside the quarterly BU RAROC report.
- Problem to solve: RAROC is reported at the BU level, which may mask product-level return dispersion. A BU reporting a RAROC above the hurdle rate may contain product lines with returns below the hurdle that are offset by high-return products elsewhere — information that is relevant to product mix decisions, pricing hurdle calibration, and capital reallocation but is not visible in the BU aggregate.
- Solution: The AI agent reads the BU P&L at the product level, the allocated RWA by product, and the expected loss by product from the IFRS 9 model. It computes RAROC at the product level within each BU, identifies products above and below the hurdle, and presents the decomposition as an annex to the quarterly BU RAROC report. The CFO and BU heads use the decomposition to assess whether capital reallocation, product pricing adjustment, or origination constraint is warranted for below-hurdle products. Capital Management confirms the RWA allocation methodology before distribution.
- OKR: The CFO and BU heads receive, as an annex to the quarterly BU RAROC report, product-level RAROC within each BU showing which loan, deposit, and fee income products sit above and below the hurdle rate.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced product decomposition annexed to ≥4 quarterly BU RAROC reports within year 1; all BUs and material products covered. |
| Acceptance | ≥85% of decompositions confirmed by Capital Management as consistent with the RWA allocation methodology; product-level results reconcile to the BU RAROC in ≥98% of reviewed quarters. |
| Cycle | Product-level RAROC available with the quarterly BU RAROC report, vs. BU aggregate only in the prior process. |

## Budget-to-actual variance & attribution {#budget-variance-attribution}

Monthly budget-to-actual variance attribution by segment decomposes the gap between plan and actual across revenue, cost, and provision dimensions, identifying whether variances are volume-driven, margin-driven, or one-time. The attribution is the basis for CFO and segment head action decisions during the month — not just a retrospective record of what happened.

### Budget Variance Action Tracker

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/budget-variance-attribution/budget-variance-action-tracker
- Lens: Automation
- Complexity: S
- Intent: The AI agent maintains a structured tracker of management actions committed in response to material budget variances — action owner, target period, expected P&L impact, and resolution status — and updates the CFO on action completion rates at each monthly review.
- Problem to solve: Management actions committed in response to budget variances are recorded in meeting minutes and tracked informally by BU finance teams. The CFO has no systematic view of which actions from prior periods have been completed, which remain open, and whether the expected P&L recovery has been achieved — the information needed to distinguish performance recovery from continuing deterioration.
- Solution: The AI agent reads the minutes of each monthly performance review and the budget variance attribution output. It extracts committed actions, assigns owner and target period from the discussion, and appends them to the structured action tracker. Each month it cross-references the tracker against the current attribution output to determine whether the expected P&L recovery is visible in the actuals. The CFO reviews the tracker update — showing open actions, actions closed with evidence of impact, and actions closed without measurable impact — at each monthly performance session.
- OKR: The CFO receives, at each monthly performance session, a tracker of management actions committed in response to material budget variances — owner, target period, expected P&L impact, and status — showing which closed actions delivered a measurable recovery.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-maintained action tracker updated for ≥10 of 12 monthly performance reviews in year 1; all actions recorded in the review minutes captured. |
| Acceptance | ≥90% of extracted actions confirmed at the monthly performance session without correction of owner or target period; the tracker's assessment of P&L recovery accepted by the CFO for ≥85% of closed actions. |
| Cycle | Action status and recovery evidence available at each monthly performance session, vs. informal tracking in meeting minutes by BU finance teams in the prior process. |

### Segment P&L Forward Run-Rate Signal

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/budget-variance-attribution/segment-pl-forward-run-rate
- Lens: Optimize
- Complexity: S
- Intent: The AI agent combines the current period's attributed P&L variance with the segment's own forward trading signals — pipeline volumes, deposit book repricing schedule, and cost accrual run rate — to produce a forward run-rate estimate for each segment at mid-month.
- Problem to solve: Segment performance reviews are retrospective — the attributed variance for the closed period is available but no forward signal is produced until the quarterly reforecast. Segment heads and the CFO manage the remainder of the current period without a quantified view of whether the forward run rate implies the budget gap will widen or close.
- Solution: The AI agent reads the current-period attributed variance, the segment's pipeline and origination data, deposit repricing notices, and cost accrual estimates. It applies the prior-period attribution methodology to the forward drivers and produces a mid-month run-rate estimate per segment — showing the estimated full-period outturn relative to budget and the assumptions driving the estimate. FP&A reviews the output and confirms or adjusts the run-rate assumptions before distribution to segment heads. The signal is produced around day 15 of each month.
- OKR: Segment heads and the CFO receive, around day 15 of each month, a forward run-rate estimate per segment — the estimated full-period outturn relative to budget and the assumptions driving it — reviewed by FP&A before distribution.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced run-rate signal delivered for ≥10 of 12 months in year 1; all segments covered. |
| Acceptance | ≥85% of run-rate estimates released by FP&A without material adjustment of the assumptions; estimated outturn within ±10% of the closed-period result in ≥80% of segment-months. |
| Cycle | Forward run-rate view available around day 15 of each month, vs. no forward signal until the quarterly reforecast in the prior process. |

### Segment Performance Variance Attribution

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/budget-variance-attribution/performance-variance-attribution-daily
- Lens: Insights
- Complexity: M
- Intent: The AI agent decomposes the monthly budget-to-actual variance for each segment into volume, rate, mix, fee income, cost, and provision components, ranks variances by consolidated P&L impact, and delivers an attributed performance pack to the CFO and segment heads on the first day of reporting.
- Problem to solve: Segment performance variance analysis is produced by each BU finance team in formats that vary across units. The CFO receives a consolidated variance figure without a consistent driver decomposition, and identifying whether a segment's shortfall reflects a volume miss, a margin compression, or a provisioning spike requires manual queries back to each BU team — extending the time to management action by two to three days.
- Solution: The AI agent reads the closed management accounts and approved budget for each segment. It applies a standardized decomposition — separating volume-driven, rate-driven, mix, fee income, cost, and provision variances for each segment — and produces a consolidated pack with variances ranked by absolute P&L impact. The pack is available to the CFO and segment heads on day one of reporting. Each segment head reviews the attributed output and adds qualitative context; the CFO uses the ranked view to direct the management response.
- OKR: The CFO and segment heads receive, on the first day of reporting, a consolidated performance pack that decomposes each segment's monthly budget-to-actual variance into volume, rate, mix, fee income, cost, and provision components ranked by absolute P&L impact.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced performance pack used for ≥10 of 12 monthly reporting cycles in year 1; all segments covered. |
| Acceptance | ≥85% of attributed outputs accepted by segment heads without material restatement; segment variances reconcile to the closed management accounts in ≥98% of reviewed cycles. |
| Cycle | Attributed performance pack available on day 1 of the reporting window, vs. two to three days of manual queries back to each BU team in the prior process. |

## Lending portfolio attribution & IFRS 9 provisioning {#lending-default-attribution}

Lending portfolio performance attribution — vintage cohort default rates, driver decomposition by channel, scorecard, and geography, and provision sensitivity analysis under IFRS 9 — is the primary analytical tool for the CFO and CRO to assess credit performance and estimate provision requirements. The quarterly provision cycle requires 200–400 team-hours across Finance, Risk, and Credit Modeling.

### Lending Portfolio Performance Attribution

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/lending-default-attribution/lending-portfolio-performance-attribution
- Lens: Insights
- Complexity: M
- Intent: The AI agent tracks cumulative default rates by vintage cohort, decomposes performance variance across channel, scorecard, geography, and product, and pre-computes IFRS 9 provision sensitivities under base, stress, and severe scenarios.
- Problem to solve: The quarterly IFRS 9 provision cycle requires Finance, Risk, and Credit Modeling to reconcile cohort-vintage default data, attribute performance variance across origination dimensions, and stress provision estimates through several rounds of iteration. Attribution frequently remains at cohort level without decomposing channel mix, scorecard drift, or geography as contributing factors.
- Solution: The AI agent reads the loan tape, origination attributes, and IFRS 9 model parameters. It computes cumulative default rates by vintage cohort, decomposes performance variance across channel, scorecard, geography, and product, and produces provision sensitivity estimates under base, stress, and severe scenarios with macro overlay assumptions made explicit. Credit Modeling checks the attribution output before the CFO and Risk Committee review it; provision methodology decisions remain with Credit Modeling.
- OKR: Cumulative default rates by vintage cohort, performance variance decomposed across channel, scorecard, geography, and product, and IFRS 9 provision sensitivities under base, stress, and severe scenarios are available for Finance, Risk, and Credit Modeling review each quarter-end.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced portfolio performance attribution used for ≥4 quarterly IFRS 9 provision cycles within year 1; all prescribed attribution dimensions covered. |
| Acceptance | ≥85% of attribution outputs accepted by Credit Modeling as sufficient for provision committee review without supplementary manual analysis; provision sensitivity estimates reconcile to the credit risk model within ±5% on periodic validation. |
| Cycle | Portfolio attribution and provision sensitivity estimates available within 3 business days of the quarterly data close, vs. 2–3 weeks of cross-team iteration in the prior process. |

### Provision Sensitivity Scenario Analysis

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/lending-default-attribution/provision-sensitivity-scenario-analysis
- Lens: Automation
- Complexity: M
- Intent: The AI agent runs multiple economic scenario overlays on the IFRS 9 ECL model to compute the P&L range of provision outcomes under base, adverse, and severe scenarios, and presents the scenario-weighted provision estimate and sensitivity range to the CFO and audit committee before each quarter-end close, with the scenario methodology documentation packaged for the external auditors.
- Problem to solve: Under IFRS 9, the ECL provision incorporates forward-looking economic scenarios weighted by probability. The scenario overlay is applied manually to the base ECL model output, and the range of provision outcomes under the approved scenario set is not systematically available to the CFO before the close cycle. The external auditor's substantive testing targets the scenario weighting methodology, and late changes to the overlay create audit timeline risk.
- Solution: The AI agent reads the base ECL model output, the approved economic scenario inputs and probability weights, and the portfolio segmentation. It applies each economic scenario overlay to the ECL model inputs and computes the provision outcome per scenario and per portfolio segment. The scenario-weighted consolidated provision estimate and the full sensitivity range — from base to severe — are presented to the CFO and audit committee for review before the close cycle begins. External auditors receive the scenario methodology documentation in the same package.
- OKR: The CFO and audit committee receive, before each quarter-end close cycle begins, the scenario-weighted ECL provision estimate and the sensitivity range from base to severe by portfolio segment, with the scenario methodology documentation packaged for the external auditors.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced provision sensitivity package used for ≥4 quarter-end closes within year 1; all approved economic scenarios and portfolio segments covered. |
| Acceptance | ≥85% of packages accepted by the CFO without a manual re-run of the overlay; scenario-weighted estimates reconcile to the base ECL model output and approved probability weights in ≥98% of reviewed quarters. |
| Cycle | Provision range available before the close cycle begins, vs. a manual overlay with late changes during close in the prior process. |

### Vintage Cohort Default Tracking

- URN: urn:financial-services:scenario:finance-treasury/performance-measurement/lending-default-attribution/vintage-cohort-default-tracking
- Lens: Optimize
- Complexity: M
- Intent: The AI agent tracks default and stage migration rates by vintage cohort, product, and origination channel on a monthly basis, and identifies cohorts whose default trajectory diverges from the IFRS 9 model's expected pattern — an early signal for provisioning model recalibration.
- Problem to solve: IFRS 9 staging decisions rely on the ECL model's forward-looking default probability estimates. When the actual default trajectory of a recently originated cohort diverges materially from the model's expectation, the divergence is identified in the model's annual backtesting cycle rather than in the close period when the cohort exits its expected performance window. Early identification would allow model recalibration or management overlay before the provision impact is booked.
- Solution: The AI agent reads the monthly loan performance data and maps each disbursement to its vintage cohort, product, and channel. It tracks the cumulative default and Stage 2 migration rate for each cohort against the IFRS 9 model's expected trajectory for that cohort type, and flags cohorts where actual performance deviates from expectation by more than the defined tolerance. The flagged cohorts are presented to Credit Modeling and the CFO with the estimated provision impact of a model recalibration. Credit Modeling determines whether a management overlay or model update is warranted.
- OKR: Credit Modeling and the CFO receive a monthly list of vintage cohorts whose cumulative default or Stage 2 migration rate deviates from the IFRS 9 model's expected trajectory by more than the defined tolerance, with the estimated provision impact of a model recalibration.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced cohort tracking delivered for ≥10 of 12 months in year 1; all vintage cohorts, products, and origination channels covered. |
| Acceptance | ≥75% of flagged cohorts confirmed by Credit Modeling as warranting a management overlay or model update decision; cohort rates reconcile to the loan performance data in ≥98% of sampled cohorts. |
| Cycle | Cohort divergence identified monthly, vs. at the model's annual backtesting cycle in the prior process. |
