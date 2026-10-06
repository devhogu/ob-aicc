# 

source: html-alt/financial-services/en/finance-treasury/finance-cycles/index.html


[PAGE TEXT]
Planning & balance-sheet steering
Budget & forecast cycle
Annual budget production with rolling reforecast — revenue, cost, capital, and risk metric targets set by business line, tracked quarterly against actuals, and updated through the year. The cycle anchor is the time from planning assumptions to board-approved budget.
The budget and forecast cycle produces the bank's annual financial plan — the revenue, cost, capital, and risk targets by business line and function that govern management performance through the year — and maintains a rolling reforecast that reflects the latest view of full-year outturn as the year progresses. In CIS markets, annual budget approval is required by NBKR, NBK/ARDFM, and CBR supervisory frameworks, and the approved budget feeds capital adequacy and liquidity planning submissions.
The cycle opens six to eight weeks before the financial year end. It requires coordinated inputs from every business line, Finance, Risk, Treasury, and the CEO's office, synthesised by FP&A into a coherent group financial plan. The reforecast runs quarterly: after each close, FP&A re-runs the year-to-date actuals plus a forward estimate based on pipeline, pricing, and cost signals.
The primary bottleneck is the synthesis step — reconciling the sum of business-line submissions into a group plan that meets the board-approved return-on-equity target while respecting capital and risk-appetite constraints. GenAI can compress narrative drafting, sensitivity analysis, and reforecast commentary — allowing the FP&A team to iterate across planning scenarios faster.
Analyze
The full-year financial trajectory — current actuals plus reforecast-to-year-end — is assembled quarterly after close rather than on a continuous basis. Intra-quarter signals that indicate the full-year outlook is shifting — loan volume deviation, deposit repricing, expense run-rate change — are not routinely incorporated into management projections between formal reforecast cycles.
Optimize
Budget scenario exploration is constrained by the time cost of each what-if. The FP&A team delivers two or three planning scenarios before the approval deadline; alternative capital deployment assumptions, product mix scenarios, or rate environment sensitivities that would sharpen the board discussion are not explored because each iteration consumes days of model-run time.
Automate
Budget narrative drafting, reforecast commentary, board pack assembly, and sensitivity table production are structured, recurring tasks performed on consistent frameworks each cycle. The narrative structure across years is substantially stable; GenAI can draft from model outputs with analyst review.
Enrich
Budget assumptions from prior years — which proved accurate, which proved systematically optimistic or conservative by business line — are held in prior-year model files rather than in a structured assumption library. Each planning cycle re-creates the assumption calibration exercise from scratch.
<button
class="flow-stages__stage"
type="button"
data-stage="set"
data-flow-id="urn:financial-services:flow:finance-treasury/budget-forecast-cycle"
>
Set assumptions
→
<button
class="flow-stages__stage"
type="button"
data-stage="plan"
data-flow-id="urn:financial-services:flow:finance-treasury/budget-forecast-cycle"
>
Plan
→
<button
class="flow-stages__stage"
type="button"
data-stage="build"
data-flow-id="urn:financial-services:flow:finance-treasury/budget-forecast-cycle"
>
Build
→
<button
class="flow-stages__stage"
type="button"
data-stage="approve"
data-flow-id="urn:financial-services:flow:finance-treasury/budget-forecast-cycle"
>
Approve
→
<button
class="flow-stages__stage"
type="button"
data-stage="track"
data-flow-id="urn:financial-services:flow:finance-treasury/budget-forecast-cycle"
>
Track & reforecast
Lens
Scenario
Intent
Complexity

### CARD 1 [New opps|S] Intra-Quarter NIM and FTP Signal Monitoring
urn: urn:financial-services:scenario:flow/finance-treasury/budget-forecast-cycle/intra-quarter-nim-ftp-signal-monitoring
intent: Agent monitors intra-quarter NIM and FTP signals continuously, detecting balance-sheet mix shifts, deposit repricing events, or loan origination deviations that indicate the full-year NIM trajectory is drifting from budget before the formal quarterly reforecast cycle, enabling Treasury and FP&A to act within the quarter.
Problem to solve: The full-year NIM and FTP outlook is updated quarterly through the formal reforecast cycle. Intra-quarter signals — a large-volume fixed-rate loan origination, a deposit repricing event, or a product mix shift — that indicate NIM is tracking away from budget are not routinely incorporated into management projections between formal reforecast windows.
Solution: Agent reads daily balance-sheet position and FTP rate data from the Treasury management system and compares the running NIM trajectory against the budget assumption. When the deviation from the budget NIM trajectory exceeds a defined threshold, agent produces a signal brief for the Treasurer and FP&A covering the driver decomposition — volume, rate, mix — and the implied full-year NIM revision.
OKR objective: Intra-quarter NIM and FTP deviations from budget — driven by balance-sheet mix shifts, deposit repricing, or loan origination variance — are detected continuously and a signal brief with driver decomposition and full-year NIM revision is available to Treasury and FP&A within 2 business days of threshold crossing.
OKR KR [Adoption]: Agent-produced intra-quarter NIM signal briefs delivered for ≥90% of threshold-crossing events identified during daily monitoring in year 1.
OKR KR [Acceptance]: ≥80% of signal briefs confirmed as reflecting a genuine NIM trajectory deviation by Treasury and FP&A on review; full-year NIM revision estimates in signal briefs reconcile to the next formal quarterly reforecast within ±10 basis points in ≥85% of reviewed signals.
OKR KR [Cycle]: NIM deviation signal brief available within 2 business days of threshold crossing, vs. identification only at the quarterly reforecast cycle in the prior process.

### CARD 2 [Insights|M] Budget Assumption Calibration Library
urn: urn:financial-services:scenario:flow/finance-treasury/budget-forecast-cycle/budget-assumption-calibration-library
intent: Agent builds a structured assumption calibration library from prior planning cycles — recording which assumptions proved accurate by business line, which were systematically optimistic or conservative, and the macro variables most correlated with planning error — and delivers a calibrated assumption reference pack to FP&A at the start of each planning cycle.
Problem to solve: Budget assumptions from prior years are held in model files rather than in a structured library. Each planning cycle re-creates the calibration exercise from scratch; systematic planning bias — a business line that consistently overestimates fee income or underestimates credit loss — is not documented in a form that carries forward.
Solution: Agent reads the closed prior-year budget, reforecast, and actual series for each business line and function, computes assumption accuracy by category — revenue growth, cost run-rate, credit loss, NIM — and identifies systematic bias patterns by originator. FP&A applies the calibration as a starting adjustment before business-line submissions are collected.
OKR objective: A structured assumption calibration library built from prior planning cycles — recording accuracy, systematic bias by business line, and macro-variable correlation with planning error — is available to FP&A at the start of each planning cycle as a calibrated reference pack.
OKR KR [Adoption]: Agent-produced calibration library used as a reference input for ≥90% of business-line assumption submissions at the first annual planning cycle after go-live.
OKR KR [Acceptance]: ≥75% of FP&A planning managers rate the calibration library as materially influencing their opening assumption set; systematic planning bias reduction ≥10% in calibrated dimensions vs. the prior cycle's actuals-to-budget variance.
OKR KR [Cycle]: Planning assumption calibration reference available to FP&A at cycle kick-off, vs. 2–4 weeks of manual prior-year analysis in the prior process.

### CARD 3 [Optimize|M] Budget Scenario and Sensitivity Engine
urn: urn:financial-services:scenario:flow/finance-treasury/budget-forecast-cycle/budget-scenario-sensitivity-engine
intent: Agent runs additional budget scenarios and sensitivity analyses on the consolidated group plan beyond the two or three the FP&A team can manually produce within the planning deadline — covering NII sensitivity to rate paths, credit loss sensitivity to GDP, and capital headroom under alternative origination mix — delivering a fuller decision range to the board.
Problem to solve: Each scenario iteration costs two to four analyst-days; the planning cycle delivers two or three scenarios before the board approval deadline. Material sensitivity space — alternative capital deployment assumptions, product mix scenarios, rate environment sensitivities — is left unexplored.
Solution: Agent holds the consolidated group plan model in parametric form and runs scenario variants by modifying specified input assumptions — rate path, GDP trajectory, origination mix, cost envelope — and re-computing NII, RWA, capital ratios, and ROE under each variant. Scenarios are available within hours of commissioning; FP&A selects the set for board presentation.
OKR objective: The board and FP&A review a broader decision range for each budget cycle, with NII sensitivity to rate paths, credit loss sensitivity to GDP, and capital headroom under alternative origination mix scenarios produced beyond the 2–3 manually feasible within the planning deadline.
OKR KR [Adoption]: Agent-produced scenario variants used in ≥80% of annual budget presentations and ≥2 mid-year reforecast cycles within year 1; ≥5 agent-produced scenarios per budget cycle beyond the manually produced set.
OKR KR [Acceptance]: ≥80% of additional scenarios rated as analytically sound by the CFO team; NII, RWA, capital ratio, and ROE outputs reconcile to the approved plan model within ±1% on standard scenarios.
OKR KR [Cycle]: Time from FP&A scenario commissioning to complete scenario output available for review reduced from 2–4 analyst-days to ≤4 hours per scenario.

### CARD 4 [Automation|M] Budget Board Pack Narrative Drafting
urn: urn:financial-services:scenario:flow/finance-treasury/budget-forecast-cycle/budget-board-pack-narrative-drafting
intent: Agent drafts the budget narrative sections of the board pack from the approved plan outputs — headline performance targets by business line, capital position, sensitivity commentary, and regulatory submission narrative for NBKR/NBK/CBR — ready for CFO review and amendment before the board presentation.
Problem to solve: Board pack narrative drafting compresses into the final weeks of the planning cycle when scenario finalisation and narrative production compete with the presentation deadline. The narrative structure is substantially stable across years; only the current-cycle content changes, yet the full production is performed manually each round.
Solution: Agent reads the approved plan outputs — business-line P&L targets, capital adequacy ratios, sensitivity results, and prior-year comparison tables — and populates the board pack narrative in the bank's standard format. It drafts the CFO commentary, sensitivity section, and regulatory submission narrative in the prescribed NBKR/NBK/CBR format. The CFO reviews, amends for judgment and forward framing, and approves before board submission.
OKR objective: The budget board pack narrative — covering headline performance targets, capital position, sensitivity commentary, and NBKR/NBK/CBR regulatory submission narrative — is available for CFO review and amendment before the board presentation, produced from approved plan outputs.
OKR KR [Adoption]: Agent used to draft the budget board pack narrative for ≥1 annual budget cycle and ≥2 major reforecast cycles within year 1.
OKR KR [Acceptance]: ≥80% of drafted board pack narrative sections accepted by the CFO without material structural amendment; regulatory submission narrative sections reviewed and approved by the Compliance team in ≥95% of submissions.
OKR KR [Cycle]: Board pack narrative drafting time reduced from 1–2 weeks of manual CFO-office production to ≤3 days of CFO review and amendment from plan output availability.

### CARD 5 [Enablement|M] Rolling Reforecast Model Compression
urn: urn:financial-services:scenario:flow/finance-treasury/budget-forecast-cycle/rolling-reforecast-model-compression
intent: Agent re-runs the reforecast model from the latest close actuals and updated pipeline signals within two business days of each quarter-end, delivering a revised full-year outlook to FP&A for review before the window for early-quarter management action closes.
Problem to solve: Quarterly reforecast requires FP&A to re-run a substantial portion of the budget model with current actuals and revised assumptions. The manual re-run takes one to two weeks after close, delaying the revised full-year outlook beyond the window where early-quarter management actions — pricing adjustments, cost actions, origination steering — are most effective.
Solution: Agent reads the closed actuals from the management accounts system and updated pipeline data from the CRM and credit origination systems, applies the reforecast methodology to each business line, and computes the revised full-year outlook with NII, cost, credit loss, capital, and ROE implications. The revised model is available for FP&A review within two business days of close.
OKR objective: The revised full-year outlook — covering NII, cost, credit loss, capital, and ROE by business line — is available for FP&A review within 2 business days of each quarter-end close, within the window where early-quarter management actions remain effective.
OKR KR [Adoption]: Agent-produced rolling reforecast available within 2 business days of quarter-end close for ≥4 quarterly cycles within year 1.
OKR KR [Acceptance]: ≥85% of agent-produced reforecast outputs accepted by FP&A as the basis for the formal reforecast cycle without requiring a separate manual model rebuild; full-year NII and capital ratio estimates reconcile to the final approved reforecast within ±3% in ≥85% of reviewed cycles.
OKR KR [Cycle]: Revised full-year outlook available within 2 business days of quarter-end close, vs. 1–2 weeks of manual model re-run in the prior process.

[PAGE TEXT]
ALM & balance-sheet steering cycle
Monthly ALCO-supported cycle to measure and steer interest rate risk in the banking book, NII sensitivity, EVE, and balance-sheet hedge positions — aligned to IRRBB / BCBS 368 and the Basel III IRRBB framework. The cycle anchor is the interval from rate or balance-sheet signal to management steering action.
The ALM and balance-sheet steering cycle is the bank's primary mechanism for managing interest rate risk in the banking book (IRRBB) — the risk that shifts in market interest rates affect the bank's net interest income (NII) and economic value of equity (EVE). Under the Basel III IRRBB framework (BCBS 368, effective 2018) and its CIS-market equivalents under NBKR and CBR guidance, banks are required to measure NII and EVE sensitivity under prescribed and internal shock scenarios, maintain IRRBB limits aligned to their risk appetite, and demonstrate effective governance through an ALCO-anchored steering process.
The cycle runs monthly, with a full IRRBB sensitivity run feeding the ALCO pack and an abbreviated weekly monitoring update between formal ALCO meetings. Balance-sheet hedging decisions — the use of interest rate swaps, cross-currency swaps, and natural offsets between assets and liabilities — are reviewed and approved within the cycle. The annual IRRBB strategy, including hedge accounting elections and the treatment of behavioural deposits under BCBS 368 Principle 4, is calibrated in the annual planning cycle and reviewed at each ALCO.
GenAI supports the cycle by drafting the ALCO rate narrative, summarising sensitivity position changes since the prior meeting, and flagging NII-at-risk and EVE positions that approach limit thresholds.
Analyze
NII and EVE sensitivity is measured monthly. Intra-month balance-sheet movements — deposit repricing events, large fixed-rate loan originations, significant hedge maturities — that alter the IRRBB position between measurements are not reflected in the continuous management picture.
Optimize
ALCO scenario exploration at each meeting is constrained by the time required to produce each rate scenario run. Alternative balance-sheet positioning strategies — different hedge tenors, different deposit pricing assumptions, different origination mix — are rarely explored with quantitative depth before the ALCO decision.
Automate
ALCO rate narrative drafting, sensitivity position change attribution, and the monthly IRRBB limit utilisation report are structured tasks that repeat on a known cycle with a consistent analytical framework and stable output format. GenAI can draft from model outputs with ALM officer review.
Enrich
Rate scenario assumptions used in prior IRRBB cycles — their accuracy relative to realised rates, and the accuracy of behavioural deposit modelling assumptions — are rarely fed back systematically into the model calibration process. BCBS 368 Principle 4 (behavioural assumption governance) requires regular backtesting, but the findings rarely loop back into the cycle's assumption setting.
<button
class="flow-stages__stage"
type="button"
data-stage="measure"
data-flow-id="urn:financial-services:flow:finance-treasury/alm-balance-sheet-steering-cycle"
>
Measure
→
<button
class="flow-stages__stage"
type="button"
data-stage="analyze"
data-flow-id="urn:financial-services:flow:finance-treasury/alm-balance-sheet-steering-cycle"
>
Analyse
→
<button
class="flow-stages__stage"
type="button"
data-stage="decide"
data-flow-id="urn:financial-services:flow:finance-treasury/alm-balance-sheet-steering-cycle"
>
Decide
→
<button
class="flow-stages__stage"
type="button"
data-stage="hedge"
data-flow-id="urn:financial-services:flow:finance-treasury/alm-balance-sheet-steering-cycle"
>
Execute hedges
→
<button
class="flow-stages__stage"
type="button"
data-stage="monitor"
data-flow-id="urn:financial-services:flow:finance-treasury/alm-balance-sheet-steering-cycle"
>
Monitor
Lens
Scenario
Intent
Complexity

### CARD 6 [Insights|S] Intra-Month IRRBB Position Signal
urn: urn:financial-services:scenario:flow/finance-treasury/alm-balance-sheet-steering-cycle/intra-month-irrbb-position-signal
intent: Agent monitors intra-month balance-sheet movements for IRRBB-material events — large fixed-rate loan originations, material deposit repricing, hedge maturities — and produces a signal brief for the ALM team when a movement materially alters the bank's NII-at-risk or EVE position between monthly ALCO meetings.
Problem to solve: NII and EVE sensitivity is measured monthly. Intra-month balance-sheet movements that alter the IRRBB position between measurements are not reflected in the continuous management picture; ALCO may approve a steering decision based on a position that has shifted materially since the last measurement date.
Solution: Agent reads daily balance-sheet position changes from the Treasury management system and applies the BCBS 368 sensitivity logic to the incremental position. When a cumulative intra-month movement exceeds a defined NII-at-risk or EVE threshold, agent produces a signal brief for the ALM team with the position change estimate and the implied limit headroom revision.
OKR objective: Intra-month balance-sheet movements that materially alter the bank's NII-at-risk or EVE position between monthly ALCO measurements trigger a signal brief for the ALM team within 1 business day of the threshold being crossed.
OKR KR [Adoption]: Agent-produced intra-month IRRBB signal briefs delivered for ≥90% of threshold-crossing events identified during daily balance-sheet monitoring in year 1.
OKR KR [Acceptance]: ≥85% of signal briefs confirmed as reflecting a material IRRBB position change by the ALM team on review; NII-at-risk and EVE estimates in signal briefs reconcile to the next monthly formal sensitivity run within ±3%.
OKR KR [Cycle]: IRRBB signal brief available within 1 business day of threshold-crossing event, vs. identification only at next monthly ALCO meeting in the prior process.

### CARD 7 [Enablement|S] FTP Rate Curve and Attribution Brief
urn: urn:financial-services:scenario:flow/finance-treasury/alm-balance-sheet-steering-cycle/ftp-rate-curve-attribution-brief
intent: Agent produces the monthly FTP rate curve commentary and business-line FTP attribution brief from the Treasury management system outputs, making the NIM contribution by funding source and business line transparent to Finance and ALCO without manual reconstruction by the ALM team.
Problem to solve: The FTP rate curve and its attribution to business-line NIM are reconstructed manually each month from Treasury model outputs. The attribution brief is typically available late in the ALCO pack production window, limiting time for business-line finance teams to review their FTP allocation before the ALCO meeting.
Solution: Agent reads the monthly FTP rate curve from the Treasury management system, attributes the NIM contribution by business line and funding source category, and produces the attribution brief in the standard format. Business-line finance teams receive the brief three days before ALCO, giving them time to review their allocation and raise queries through the ALM team before the meeting.
OKR objective: The monthly FTP rate curve commentary and business-line NIM attribution brief are produced from Treasury management system outputs and delivered to Finance and ALCO three business days before the ALCO meeting.
OKR KR [Adoption]: Agent-produced FTP attribution brief delivered for ≥11 of 12 monthly ALCO cycles in year 1; all material business lines and funding source categories covered in each brief.
OKR KR [Acceptance]: ≥85% of FTP attribution briefs accepted by the ALM team without material restatement; NIM attribution by business line reconciles to the Treasury management system in ≥98% of reviewed months.
OKR KR [Cycle]: FTP attribution brief available 3 business days before ALCO, vs. 1 business day or less under compressed manual production in the prior process.

### CARD 8 [Automation|M] ALCO IRRBB Pack Narrative Drafting
urn: urn:financial-services:scenario:flow/finance-treasury/alm-balance-sheet-steering-cycle/alco-irrbb-pack-narrative-drafting
intent: Agent drafts the ALCO pack's rate narrative and IRRBB sensitivity section from the ALM model outputs — NII-at-risk and EVE positions under BCBS 368 six-shock scenarios, position change attribution since prior ALCO, and limit utilisation status — ready for ALM officer review the day after the sensitivity run completes.
Problem to solve: ALCO pack preparation compresses into a two-day window between the monthly sensitivity run and the ALCO meeting. The rate narrative and sensitivity attribution are drafted manually; the time pressure limits the analytical depth of the attribution and the quality of the steering discussion.
Solution: Agent reads the ALM model output files — NII-at-risk and EVE by shock scenario, position change decomposition, hedge notional and mark-to-market — and drafts the ALCO pack sections covering the current IRRBB position, position change attribution since prior ALCO, limit utilisation against risk appetite, and recommended steering options. The ALM officer reviews the draft, confirms the attribution decomposition, and approves before ALCO distribution.
OKR objective: The ALCO IRRBB pack narrative and sensitivity attribution section are available for ALM officer review the day after the monthly sensitivity run completes, with position change decomposition and limit utilisation covered in every cycle.
OKR KR [Adoption]: Agent used to draft the ALCO IRRBB narrative for ≥11 of 12 monthly cycles in year 1.
OKR KR [Acceptance]: ≥85% of drafted ALCO IRRBB narratives accepted by ALM officers without material amendment to the attribution decomposition; limit utilisation figures reconcile to the ALM model output in ≥98% of reviewed cycles.
OKR KR [Cycle]: ALCO IRRBB narrative available for ALM officer review within 24 hours of sensitivity run completion, vs. 2 days in the prior manual process.

### CARD 9 [Optimize|M] ALCO Balance-Sheet Positioning Scenario Analysis
urn: urn:financial-services:scenario:flow/finance-treasury/alm-balance-sheet-steering-cycle/alco-balance-sheet-positioning-scenarios
intent: Agent models alternative balance-sheet positioning strategies at the ALCO decide stage — different hedge tenors, deposit pricing assumptions, and origination mix — producing quantified NII and EVE outcomes for each option so ALCO can make the steering decision on the basis of a full scenario comparison rather than a single recommended position.
Problem to solve: ALCO scenario exploration is constrained by the time required to produce each rate scenario run. Alternative strategies — different hedge tenors, modified deposit pricing assumptions, alternative fixed-to-floating origination ratios — are rarely explored with quantitative depth before the ALCO decision.
Solution: Agent holds the current ALM model in parametric form and runs the ALCO-specified positioning alternatives against the BCBS 368 shock set. It produces a structured scenario comparison showing NII-at-risk, EVE, and carry cost of hedging for each alternative. ALCO reviews the comparison at the meeting and selects the approved positioning strategy.
OKR objective: ALCO enters each balance-sheet steering decision with a quantified comparison of alternative positioning strategies — covering different hedge tenors, deposit pricing assumptions, and origination mix — against the full BCBS 368 shock set.
OKR KR [Adoption]: Agent-generated positioning scenario comparisons used for ≥90% of ALCO balance-sheet steering decisions within 12 months of go-live.
OKR KR [Acceptance]: ≥80% of ALCO-reviewed scenario comparisons accepted as analytically sufficient for the steering decision without requiring a further manual run; NII-at-risk and EVE outputs validated against ALM model benchmarks within ±2%.
OKR KR [Cycle]: Time from ALCO scenario commissioning to complete multi-option comparison available for review reduced from 2–3 days to ≤4 hours.

### CARD 10 [New opps|M] BCBS 368 Behavioural Assumption Backtesting
urn: urn:financial-services:scenario:flow/finance-treasury/alm-balance-sheet-steering-cycle/bcbs368-behavioural-assumption-backtesting
intent: Agent backtests the behavioural deposit and repricing assumptions used in the IRRBB model against realised deposit behaviour on a monthly basis, producing a structured accuracy report against BCBS 368 Principle 4 requirements and flagging assumptions that have drifted beyond tolerance for model recalibration.
Problem to solve: Behavioural deposit assumptions under BCBS 368 Principle 4 are calibrated annually but not backtested continuously. NBKR and CBR supervisors increasingly challenge ILAAP submissions that rely on stale behavioural assumptions; model risk from assumption drift accumulates without a continuous governance process.
Solution: Agent reads actual deposit balance and rate data from the core banking system on a monthly basis and compares it against the behavioural assumptions embedded in the ALM model. It produces a structured accuracy report by assumption category — stability ratio, repricing beta, conditional prepayment rate — and flags assumptions that exceed the tolerance threshold for the model risk team as recalibration candidates ahead of the next ILAAP cycle.
OKR objective: IRRBB behavioural deposit and repricing assumptions are backtested against realised balance-sheet behaviour on a monthly basis, with a structured accuracy report produced each cycle and assumptions exceeding tolerance flagged for model recalibration ahead of each ILAAP submission.
OKR KR [Adoption]: Agent-produced backtesting reports covering all material BCBS 368 behavioural assumption categories delivered for ≥11 of 12 monthly cycles within year 1.
OKR KR [Acceptance]: ≥90% of model risk committee recalibration decisions on flagged assumptions supported by agent-produced backtesting evidence; accuracy reports reconcile to ALM model assumption values in ≥98% of reviewed cycles.
OKR KR [Cycle]: Monthly assumption backtesting cycle completed within 3 business days of balance-sheet data availability, vs. annual calibration only in the prior process.

[PAGE TEXT]
Liquidity steering cycle (LCR & ILAAP)
Daily LCR and NSFR monitoring with a monthly ALCO-supported liquidity steering cycle — HQLA adequacy, funding maturity profile, and ILAAP submission. The cycle anchor is the interval from liquidity signal to funding or HQLA positioning action.
The liquidity steering cycle governs the bank's compliance with and active management of liquidity requirements under the Basel III Liquidity Coverage Ratio (LCR) and Net Stable Funding Ratio (NSFR) standards, and the Internal Liquidity Adequacy Assessment Process (ILAAP) submitted to supervisors. In Kazakhstan and the Kyrgyz Republic, NBKR and NBK/ARDFM maintain their own liquidity ratios and reporting requirements alongside — or adapted from — Basel III; CBR in Russia implements LCR and NSFR under the Bank of Russia's own calibration. ILAAP equivalent assessments are required under each CIS supervisor's stress-testing framework.
The cycle operates on three cadences: daily LCR and NSFR calculation for internal management and regulatory reporting; monthly ALCO-anchored liquidity steering review covering HQLA adequacy, funding maturity profile, deposit concentration risk, and survival horizon under internal stress scenarios; and annual ILAAP/equivalent submission incorporating stressed liquidity projections and the Contingency Funding Plan. The annual ILAAP must demonstrate that the bank holds a liquidity buffer sufficient to survive the bank's own internally defined stress scenarios.
GenAI supports the narrative drafting for monthly ALCO liquidity packs, the ILAAP document production, and exception triage across the daily monitoring output.
Analyze
LCR and NSFR are calculated daily, but the forward-looking liquidity picture — survival horizon under stress, funding maturity cliff analysis, deposit concentration trend — is assembled monthly for ALCO. Management lacks a continuous-form view of liquidity adequacy margin between formal committee reviews.
Optimize
ILAAP stress scenario design and the monthly operational stress scenarios operate on separate assumptions and run on separate cadences. Aligning the operational monthly cycle with the annual ILAAP design would reduce the duplication of stress modelling effort and improve the ILAAP's credibility with NBKR/NBK/CBR supervisors.
Automate
Daily LCR/NSFR exception commentary, monthly ALCO liquidity narrative, ILAAP document sections, and Contingency Funding Plan updates are structured narrative tasks with consistent frameworks that repeat on known cycles. BCBS 368 and ILAAP disclosure sections follow prescribed formats amenable to agent-assisted drafting.
Enrich
Behavioural assumptions for demand deposits, credit line drawdown rates, and contingent outflows are calibrated annually from historical data but are rarely backtested continuously against realised behaviour within the year. ILAAP submissions that rely on stale behavioural assumptions accumulate model risk that NBKR/NBK/CBR supervisors increasingly challenge.
<button
class="flow-stages__stage"
type="button"
data-stage="forecast"
data-flow-id="urn:financial-services:flow:finance-treasury/liquidity-steering-cycle"
>
Forecast
→
<button
class="flow-stages__stage"
type="button"
data-stage="stress"
data-flow-id="urn:financial-services:flow:finance-treasury/liquidity-steering-cycle"
>
Stress
→
<button
class="flow-stages__stage"
type="button"
data-stage="plan"
data-flow-id="urn:financial-services:flow:finance-treasury/liquidity-steering-cycle"
>
Plan
→
<button
class="flow-stages__stage"
type="button"
data-stage="report"
data-flow-id="urn:financial-services:flow:finance-treasury/liquidity-steering-cycle"
>
Report
→
<button
class="flow-stages__stage"
type="button"
data-stage="adjust"
data-flow-id="urn:financial-services:flow:finance-treasury/liquidity-steering-cycle"
>
Adjust
Lens
Scenario
Intent
Complexity

### CARD 11 [Automation|S] Daily LCR/NSFR Submission Exception Commentary
urn: urn:financial-services:scenario:flow/finance-treasury/liquidity-steering-cycle/daily-lcr-nsfr-exception-commentary
intent: Agent drafts the exception commentary for daily LCR and NSFR submissions — identifying the driver of each ratio movement, the HQLA composition change, and any inflow/outflow category that moved materially — ready for Treasury review before the submission is dispatched to NBKR/NBK/CBR.
Problem to solve: Daily LCR and NSFR exception commentary is drafted manually by Treasury analysts before each submission. On days with material ratio movements, the commentary production consumes one to two analyst hours under the submission deadline, leaving limited time for quality review before the explanation is dispatched to the supervisor.
Solution: Agent reads the daily LCR and NSFR calculation outputs, identifies the categories with material movements since the prior day, and drafts the exception commentary in the format prescribed by NBKR/NBK/CBR for each submission. The Treasury analyst reviews the draft, confirms the driver identification, and approves before submission. Exception commentary time compresses from one to two analyst hours to a fifteen-minute review cycle.
OKR objective: Exception commentary for daily LCR and NSFR submissions — identifying each ratio movement driver, HQLA composition change, and material inflow/outflow category — is available for Treasury review within 30 minutes of daily calculation output in the format prescribed by NBKR/NBK/CBR.
OKR KR [Adoption]: Agent used to draft daily LCR/NSFR exception commentary for ≥95% of submission days in year 1.
OKR KR [Acceptance]: ≥90% of agent-drafted commentaries accepted by Treasury analysts without material amendment before submission dispatch; driver identification accuracy confirmed by supervisory query analysis at ≤5% query rate.
OKR KR [Cycle]: Exception commentary production time reduced from 1–2 analyst hours to ≤15 minutes of Treasury review per submission day.

### CARD 12 [Insights|M] Continuous Liquidity Position Monitoring
urn: urn:financial-services:scenario:flow/finance-treasury/liquidity-steering-cycle/continuous-liquidity-position-monitoring
intent: Agent maintains a continuous-form liquidity position view — LCR, NSFR, HQLA buffer, survival horizon under the operational stress scenario, and funding maturity cliff — updated daily from Treasury position data, giving ALCO and the Treasurer a current-state picture between monthly formal reviews.
Problem to solve: Daily LCR and NSFR are calculated but the forward-looking liquidity picture — survival horizon, funding maturity cliff, deposit concentration trend — is assembled monthly for ALCO. Compound deterioration signals that individually do not breach daily thresholds can accumulate to a material position change before the monthly pack is produced.
Solution: Agent reads daily balance-sheet position, HQLA composition, and funding maturity data from the Treasury management system. It computes LCR, NSFR, survival horizon under the operational stress scenario, and deposit concentration index on a daily basis and maintains a continuous dashboard narrative updated each business day. The Treasurer reviews the narrative each morning; material movements trigger an immediate brief with the driver decomposition.
OKR objective: A continuous-form liquidity position view — LCR, NSFR, HQLA buffer, survival horizon, and funding maturity cliff — updated daily from Treasury position data, is available to ALCO and the Treasurer between monthly formal reviews.
OKR KR [Adoption]: Agent-maintained daily liquidity position dashboard available each business day for ≥220 trading days in year 1; all prescribed metrics covered in each daily update.
OKR KR [Acceptance]: ≥90% of daily liquidity narratives confirmed accurate by the Treasurer without requiring correction; daily metric values reconcile to the monthly formal liquidity report within prescribed tolerance in ≥97% of checked periods.
OKR KR [Cycle]: Daily liquidity position available each morning from overnight feeds, vs. formal monthly cycle only in the prior process; intra-period deterioration visibility increased from 30-day lag to ≤1 business day.

### CARD 13 [Optimize|M] ILAAP and Operational Stress Scenario Alignment
urn: urn:financial-services:scenario:flow/finance-treasury/liquidity-steering-cycle/ilaap-operational-stress-scenario-alignment
intent: Agent aligns the operational monthly liquidity stress scenarios with the annual ILAAP stress design, producing a mapping of shared assumptions and scenario parameters so that monthly stress run outputs can be directly extracted into the ILAAP submission rather than requiring a separate full re-run.
Problem to solve: Monthly operational stress scenarios and the annual ILAAP stress scenarios operate on separate assumptions and cadences. The gap between the two means the ILAAP submission requires a time-consuming separate stress modelling exercise, duplicating effort and introducing the risk of inconsistency between the ILAAP position and the running operational liquidity management view.
Solution: Agent reads the ILAAP stress scenario specifications and the operational monthly stress scenario parameters and produces a structured mapping of shared and divergent assumptions. For parameters that are compatible, it generates a standard transformation rule so that the monthly stress run output maps directly to the corresponding ILAAP input cell. For parameters that genuinely differ, it produces a documented reconciliation explanation for inclusion in the ILAAP methodology note.
OKR objective: A structured mapping of shared and divergent parameters between the monthly operational liquidity stress scenarios and the annual ILAAP stress design is maintained, with transformation rules enabling monthly stress run outputs to populate ILAAP input cells directly and reconciliation explanations documented for genuinely divergent parameters.
OKR KR [Adoption]: Agent-produced ILAAP scenario alignment mapping used for ≥1 annual ILAAP submission cycle within year 1; all material stress scenario parameters covered in the mapping.
OKR KR [Acceptance]: ≥80% of ILAAP input cells populated directly from monthly stress run outputs using agent-produced transformation rules, without requiring a separate full ILAAP re-run; reconciliation explanations accepted by the model risk team in ≥90% of genuinely divergent parameter cases.
OKR KR [Cycle]: Time required for ILAAP stress modelling reduced by ≥50% through direct monthly-to-ILAAP parameter mapping vs. full independent re-run in the prior process.

### CARD 14 [Enablement|M] ALCO Liquidity Pack Narrative Drafting
urn: urn:financial-services:scenario:flow/finance-treasury/liquidity-steering-cycle/alco-liquidity-pack-narrative-drafting
intent: Agent drafts the monthly ALCO liquidity pack narrative from the liquidity model outputs — stress scenario results, survival horizon analysis, HQLA composition, funding maturity profile, and deposit concentration metrics — ready for Treasurer review the day after the model run completes.
Problem to solve: Monthly ALCO liquidity narrative is drafted manually from model outputs each month, consuming one to two Treasury analyst days on a structure that changes only at the margins between meetings. The draft is often available only one business day before the ALCO meeting.
Solution: Agent reads the monthly liquidity model outputs — LCR, NSFR, survival horizon under each stress scenario, HQLA buffer composition, funding maturity ladder, and deposit concentration index — and drafts the ALCO liquidity pack sections in the bank's standard format. It highlights position changes since the prior meeting and flags any metric approaching a risk-appetite limit. The Treasurer reviews and approves the draft, adding forward-looking judgment on funding strategy.
OKR objective: The monthly ALCO liquidity pack narrative is available for Treasurer review the day after the liquidity model run completes, covering LCR, NSFR, survival horizon, HQLA buffer, funding maturity, and deposit concentration for every cycle.
OKR KR [Adoption]: Agent used to draft the ALCO liquidity pack narrative for ≥11 of 12 monthly cycles in year 1.
OKR KR [Acceptance]: ≥85% of agent-drafted liquidity narratives accepted by the Treasurer without material amendment; position change flags and risk-appetite proximity alerts verified as accurate in ≥95% of reviewed cycles.
OKR KR [Cycle]: ALCO liquidity pack narrative available for Treasurer review within 24 hours of model run, vs. 1–2 analyst-days in the prior manual process.

### CARD 15 [New opps|M] ILAAP Behavioural Assumption Continuous Backtesting
urn: urn:financial-services:scenario:flow/finance-treasury/liquidity-steering-cycle/ilaap-behavioural-assumption-backtesting
intent: Agent backtests ILAAP behavioural assumptions — demand deposit stability, credit line drawdown rates, contingent outflow rates — against realised balance-sheet behaviour on a monthly basis, producing a structured accuracy report that feeds ILAAP assumption governance and supervisory credibility under NBKR/NBK/CBR challenge.
Problem to solve: ILAAP behavioural assumptions are calibrated annually from historical data but are not backtested continuously within the year. NBKR, NBK, and CBR supervisors increasingly challenge ILAAP submissions where behavioural assumptions appear stale relative to realised depositor and counterparty behaviour.
Solution: Agent reads monthly balance-sheet data from the core banking and Treasury systems and compares demand deposit stability ratios, credit line utilisation rates, and contingent outflow actuals against the ILAAP model assumptions. It produces a structured monthly accuracy report by assumption category with deviation measurement and cumulative drift since the last calibration. Assumptions that breach the tolerance threshold are escalated to the model risk team as recalibration candidates, and the accuracy report is retained as supervisory evidence of ILAAP assumption governance.
OKR objective: ILAAP behavioural assumptions — demand deposit stability, credit line drawdown rates, contingent outflow rates — are backtested against realised balance-sheet behaviour on a monthly basis, with structured accuracy reports retained as supervisory evidence of ILAAP assumption governance.
OKR KR [Adoption]: Agent-produced ILAAP behavioural assumption backtesting reports delivered for ≥11 of 12 monthly cycles in year 1; all material assumption categories covered in each cycle.
OKR KR [Acceptance]: ≥90% of model risk committee recalibration decisions on flagged assumptions supported by agent-produced backtesting evidence; monthly accuracy reports cited in ≥1 ILAAP supervisory submission per year as governance evidence.
OKR KR [Cycle]: Monthly backtesting report available within 3 business days of balance-sheet data close, vs. annual calibration review only in the prior process.

[PAGE TEXT]
Reporting & close
Financial close cycle
Month-end and year-end financial close — journal cut-off, reconciliations, adjusting entries, consolidation, and production of the management accounts pack. The cycle anchor is the time from cut-off to final management accounts sign-off.
The financial close cycle produces the bank's periodic financial statements — management accounts monthly and statutory accounts annually — through a structured sequence of cut-off, reconciliation, adjustment, consolidation, and reporting steps. Under IFRS as adopted in Kazakhstan, Kyrgyzstan, and Russia, the bank's annual statutory accounts must comply with IFRS 9 (financial instruments), IFRS 16 (leases), and IAS 32/39 (financial instruments) at a minimum; the monthly management close feeds directly into the regulatory reporting cycle.
The cycle runs for 7-12 business days after each month end, compressing the assembly of a complete financial picture from 15-30 source systems into a single agreed set of accounts. The bottleneck is the reconciliation and exception-clearing stage — where GL-to-sub-ledger differences, inter-entity mismatches, and late-arriving journal entries accumulate into a concentrated period of manual resolution under close deadline pressure.
GenAI can accelerate the exception triage and close narrative stages — identifying root causes of reconciliation exceptions from prior patterns, drafting management commentary, and tracking close task status — freeing the Controllers team for judgement-intensive adjusting entries.
Analyze
Close performance — exception volumes, late-submission counts, reconciliation duration by entity and sub-ledger — is reviewed informally at team level but not tracked systematically across close cycles. The Controllers team cannot measure which reconciliation steps are trending longer or which exception types are recurring without manual extraction from close task logs.
Optimize
The sequence of reconciliation tasks within the close cycle is managed by a close task tracker but is not dynamically prioritised. When a critical-path reconciliation is delayed, the re-sequencing of downstream tasks to minimise total close duration is performed by the close manager manually without analytical support.
Automate
Management accounts commentary, reconciliation exception triage commentary, and close task status reporting are structured, recurring production tasks. The narrative structure is stable across periods; only the current-period variance content changes. GenAI can draft from closed accounts data with Finance review.
Enrich
Recurring reconciliation exception types — the same GL-to-sub-ledger mismatch arising from the same system interface limitation each month — are resolved individually each close cycle without a root-cause fix being escalated through the systems improvement process. Close cycle exception history is not mined for systemic patterns.
<button
class="flow-stages__stage"
type="button"
data-stage="cutoff"
data-flow-id="urn:financial-services:flow:finance-treasury/financial-close-cycle"
>
Cut-off
→
<button
class="flow-stages__stage"
type="button"
data-stage="reconcile"
data-flow-id="urn:financial-services:flow:finance-treasury/financial-close-cycle"
>
Reconcile
→
<button
class="flow-stages__stage"
type="button"
data-stage="adjust"
data-flow-id="urn:financial-services:flow:finance-treasury/financial-close-cycle"
>
Adjust
→
<button
class="flow-stages__stage"
type="button"
data-stage="close"
data-flow-id="urn:financial-services:flow:finance-treasury/financial-close-cycle"
>
Close
→
<button
class="flow-stages__stage"
type="button"
data-stage="report"
data-flow-id="urn:financial-services:flow:finance-treasury/financial-close-cycle"
>
Report
Lens
Scenario
Intent
Complexity

### CARD 16 [Enablement|S] IFRS 9 ECL Provision Commentary Drafting
urn: urn:financial-services:scenario:flow/finance-treasury/financial-close-cycle/ifrs9-ecl-provision-commentary-drafting
intent: Agent drafts the IFRS 9 ECL provision commentary for the management accounts close from the credit risk model outputs — PD, LGD, EAD by stage, staging migration matrix, macro overlay rationale — ready for Finance and Risk joint review before the adjusting entry is posted.
Problem to solve: ECL provision calculations arrive late in the close window; the gap between the credit risk model run cadence and the Finance close cut-off compresses the time available for quality review. Senior Finance and Risk input is applied under deadline pressure.
Solution: Agent reads the credit risk model outputs for the period — staging analysis, provision movement by portfolio, macro overlay assumptions — and drafts the IFRS 9 ECL commentary in the format prescribed for the management accounts and the IFRS 9 disclosure note. It flags material movements against prior period and against the budget provision. The joint Finance and Risk review team focuses on the provision quantum and staging judgment, not on narrative production.
OKR objective: The IFRS 9 ECL provision commentary for the management accounts close — covering PD, LGD, EAD by stage, staging migration, macro overlay rationale, and material movements against prior period and budget provision — is available for Finance and Risk joint review before the adjusting entry is posted.
OKR KR [Adoption]: Agent used to draft the IFRS 9 ECL commentary for ≥10 of 12 monthly close cycles in year 1.
OKR KR [Acceptance]: ≥85% of agent-drafted ECL commentaries accepted by the Finance and Risk joint review team without material amendment; provision figures and staging analysis reconcile to the credit risk model outputs in ≥98% of reviewed cycles.
OKR KR [Cycle]: IFRS 9 ECL commentary available for joint review within 4 hours of credit risk model output availability, vs. 1–2 days of manual drafting under deadline pressure in the prior process.

### CARD 17 [Insights|S] Close Performance Trend Analytics
urn: urn:financial-services:scenario:flow/finance-treasury/financial-close-cycle/close-performance-trend-analytics
intent: Agent tracks close performance metrics — exception volumes by type, reconciliation duration by entity and sub-ledger, late journal counts, and sign-off timeline — across cycles, surfacing deterioration trends and systemic exception patterns to the Financial Controller for structural remediation rather than cycle-by-cycle resolution.
Problem to solve: Close performance is reviewed informally at team level and is not tracked systematically across cycles. The Controllers team cannot readily identify which reconciliation steps are trending longer or which exception types are recurring systemically without manual extraction from close task logs.
Solution: Agent reads close task completion times, exception queue volumes and resolution durations, and late journal counts from the close management system at each period-end. It maintains a rolling close performance database, identifies trend deterioration by step and entity, and flags systemic exception patterns for the Financial Controller's structural investigation queue.
OKR objective: Close performance metrics — exception volumes, reconciliation durations, late journal counts, and sign-off timelines — are tracked across cycles with deterioration trends and systemic patterns surfaced to the Financial Controller for structural remediation.
OKR KR [Adoption]: Agent-produced close performance trend report used for ≥10 of 12 monthly cycles in year 1; all material close steps and entities covered in each report.
OKR KR [Acceptance]: ≥75% of trend deterioration signals rated as actionable by the Financial Controller; systemic exception patterns confirmed on independent log review in ≥80% of flagged cases.
OKR KR [Cycle]: Close performance trend report available within 3 business days of each period-end close, vs. no systematic cross-cycle tracking in the prior process.

### CARD 18 [Automation|M] Close Reconciliation Exception Triage
urn: urn:financial-services:scenario:flow/finance-treasury/financial-close-cycle/close-reconciliation-exception-triage
intent: Agent classifies each reconciliation exception in the GL-to-sub-ledger queue by root-cause category — interface timing, posting error, system mapping defect, manual journal gap — matches it against the prior-period exception pattern library, and produces a triage pack for the Controllers team with a recommended resolution path for each item.
Problem to solve: GL-to-sub-ledger reconciliation exceptions are resolved individually each cycle. Recurring exceptions — the same mismatch arising from the same system interface limitation each month — are investigated from scratch rather than resolved by applying the established fix from the prior cycle.
Solution: Agent reads the exception queue from the reconciliation system, applies a root-cause classification model trained on prior-cycle exception records, and matches each new exception to the closest prior-period instance. For exceptions with an established resolution path, the agent produces a recommended resolution with prior-period source evidence; for novel exceptions, it provides a structured investigation brief. The triage pack is available within four hours of the exception queue being generated.
OKR objective: Each GL-to-sub-ledger reconciliation exception is classified by root-cause category, matched against the prior-period pattern library, and provided with a recommended resolution path before the Controllers team begins investigation.
OKR KR [Adoption]: Agent-produced triage pack used for ≥90% of reconciliation exceptions in the monthly close within year 1.
OKR KR [Acceptance]: ≥80% of resolution recommendations accepted by Controllers without material alteration; root-cause classification accuracy confirmed at ≥90% on periodic QA review against final resolution records.
OKR KR [Cycle]: Triage pack available within 4 hours of exception queue generation, vs. same-day or next-day manual investigation start in the prior process.

### CARD 19 [Optimize|M] Close Critical-Path Re-Sequencing
urn: urn:financial-services:scenario:flow/finance-treasury/financial-close-cycle/close-critical-path-resequencing
intent: Agent monitors the close task tracker in real time, identifies critical-path dependencies at slippage risk, and produces a re-sequenced close plan when a delay threatens the sign-off deadline — reducing the manual re-scheduling burden on the close manager during the most time-pressured period of the cycle.
Problem to solve: Close task sequencing is managed by a tracker but is not dynamically prioritised. When a critical-path reconciliation is delayed, the close manager manually re-sequences downstream tasks; the elapsed time between the delay signal and the revised plan compresses the resolution window.
Solution: Agent reads the close task tracker on a continuous basis, maintains a dependency map of the close sequence, and detects when a task's completion trajectory threatens a downstream critical-path milestone. It produces a revised close sequence with updated completion time estimates and flags tasks where acceleration or parallel execution could recover the sign-off target. The close manager reviews and approves the revised plan.
OKR objective: When a critical-path close task threatens the sign-off deadline, a re-sequenced close plan identifying acceleration and parallel-execution options is available for close manager review within 2 hours of the slippage signal.
OKR KR [Adoption]: Agent-produced re-sequenced close plans used for ≥80% of detected critical-path slippage events within year 1; dependency map covers all material close tasks.
OKR KR [Acceptance]: ≥75% of agent-produced re-sequencing plans adopted by close managers without material alteration; close sign-off deadlines met in ≥90% of cycles in which a re-sequencing event occurred.
OKR KR [Cycle]: Revised close sequence available for close manager review within 2 hours of a critical-path delay signal, vs. 4–8 hours of manual re-scheduling in the prior process.

### CARD 20 [Automation|M] Management Accounts Commentary Production
urn: urn:financial-services:scenario:flow/finance-treasury/financial-close-cycle/management-accounts-commentary-production
intent: Agent drafts the management accounts commentary pack from the closed accounts — income statement and balance sheet variance narrative, capital metrics commentary, and business-line performance summaries — in the standard pack format, ready for CFO office review on the first day of the reporting window.
Problem to solve: Management accounts commentary is drafted manually by the CFO office each period from the closed accounts and prior-period comparisons. The narrative structure is largely consistent across periods; only the current-period variances change, yet the full production consumes two to four analyst-days.
Solution: Agent reads the closed management accounts and the prior-period comparisons, identifies the material variances by business line and income category, and drafts the commentary sections in the bank's standard pack format. It flags variances that exceed the materiality threshold for senior review and marks sections where forward-looking judgment is required from the CFO.
OKR objective: The management accounts commentary pack — income statement and balance sheet variance narrative, capital metrics commentary, and business-line performance summaries — is available for CFO office review in the standard format on the first day of the reporting window.
OKR KR [Adoption]: Agent used to draft management accounts commentary for ≥10 of 12 monthly reporting cycles in year 1; all prescribed pack sections covered in each cycle.
OKR KR [Acceptance]: ≥85% of agent-drafted commentary packs accepted by the CFO office without material structural amendment; material variances flagged by the agent confirmed as requiring senior review in ≥90% of cases.
OKR KR [Cycle]: Management accounts commentary available on day 1 of the reporting window, vs. 2–4 analyst-days of manual drafting from the closed accounts in the prior process.

[PAGE TEXT]
Regulatory reporting cycle
Monthly and quarterly supervisory financial reporting to NBKR, NBK/ARDFM, and CBR — including COREP/FINREP equivalents, IFRS statutory accounts, and ad hoc data requests. The cycle anchor is the time from close to validated, submitted regulatory return.
The regulatory reporting cycle produces the bank's periodic financial and prudential submissions to supervisors — NBKR in the Kyrgyz Republic, NBK/ARDFM in Kazakhstan, and CBR in Russia. Each supervisor publishes its own prescribed reporting forms, submission calendar, and data quality validation rules, which the bank's Regulatory Reporting team must satisfy independently for each regulatory perimeter. For cross-border banking groups operating under Basel III, COREP capital returns and FINREP financial reporting align to EBA taxonomy; CIS supervisors have equivalent forms calibrated to local regulatory standards.
The cycle runs continuously: monthly returns cover capital adequacy ratios, liquidity positions, and balance-sheet composition; quarterly returns add stress-test inputs, large-exposure schedules, and asset quality classifications. The bank must demonstrate BCBS 239 risk data aggregation capability to supervisors; data lineage from source system to submitted figure must be documentable on request. Annual returns include IFRS-compliant statutory accounts and the ICAAP/ILAAP submissions.
GenAI can accelerate the data validation commentary, explanatory note drafting for regulatory submissions, and the triage of automated validation rule failures that currently consume the majority of the reporting team's time before each submission deadline.
Analyze
Regulatory submission quality — validation failure rates, exception volumes, post-submission query frequencies — is monitored informally by the reporting team but not tracked in a structured form across submission cycles. The head of regulatory reporting cannot produce a trend analysis of data quality improvement across supervisors without manual extraction from submission records.
Optimize
The validation exception queue is resolved sequentially by the reporting team each cycle, with priority set by exception severity and submission deadline proximity. Systematic patterns — the same source system consistently generating the same exception type — are identified informally rather than through a structured root-cause framework that could eliminate recurring exceptions at source.
Automate
Explanatory note drafting for validation exceptions, post-submission reconciliation commentary, supervisory query response packs, and the standard narrative sections of regulatory returns (management commentary, methodology disclosures) are structured, recurring writing tasks with consistent frameworks. BCBS 239 lineage documentation follows a traceable path from source to report field that an agent can traverse systematically.
Enrich
Supervisory queries from prior submission cycles — which data points were challenged, which explanations were accepted, which methodology clarifications were requested — are held in individual query files rather than in a structured knowledge base. The reporting team repeats the investigation and drafting effort for similar queries across cycles without a shared institutional response library.
<button
class="flow-stages__stage"
type="button"
data-stage="aggregate"
data-flow-id="urn:financial-services:flow:finance-treasury/regulatory-reporting-cycle"
>
Aggregate
→
<button
class="flow-stages__stage"
type="button"
data-stage="validate"
data-flow-id="urn:financial-services:flow:finance-treasury/regulatory-reporting-cycle"
>
Validate
→
<button
class="flow-stages__stage"
type="button"
data-stage="submit"
data-flow-id="urn:financial-services:flow:finance-treasury/regulatory-reporting-cycle"
>
Submit
→
<button
class="flow-stages__stage"
type="button"
data-stage="reconcile"
data-flow-id="urn:financial-services:flow:finance-treasury/regulatory-reporting-cycle"
>
Reconcile
→
<button
class="flow-stages__stage"
type="button"
data-stage="audit"
data-flow-id="urn:financial-services:flow:finance-treasury/regulatory-reporting-cycle"
>
Audit & respond
Lens
Scenario
Intent
Complexity

### CARD 21 [Optimize|S] Regulatory Submission Pre-Dispatch Quality Gate
urn: urn:financial-services:scenario:flow/finance-treasury/regulatory-reporting-cycle/regulatory-submission-pre-dispatch-quality-gate
intent: Agent applies a pre-submission quality gate across all return cells before the submission package is dispatched — checking cross-form consistency, COREP/FINREP reconciliation to management accounts, and prior-period plausibility benchmarks — and delivers a signed quality assurance log for the Head of Regulatory Reporting before submission.
Problem to solve: Post-submission supervisory queries from NBKR, NBK/ARDFM, and CBR frequently arise from cross-form inconsistencies or management-to-regulatory figure mismatches present in the submission. The quality check before submission is performed manually and incompletely under deadline pressure; the same mismatch types recur across cycles.
Solution: Agent reads the completed return across all forms, applies cross-form arithmetic consistency checks, reconciles COREP capital figures to the management capital reporting, and benchmarks material cells against the prior-period submission plus a plausibility range derived from balance-sheet movement between periods. It produces a quality assurance log — pass, warning, or fail — for each check category. The Head of Regulatory Reporting resolves all fail items before submission is authorised.
OKR objective: All COREP/FINREP return cells are checked for cross-form consistency, management-to-regulatory figure reconciliation, and prior-period plausibility before submission dispatch, with a signed quality assurance log delivered to the Head of Regulatory Reporting.
OKR KR [Adoption]: Agent-produced pre-dispatch quality gate applied to ≥100% of quarterly COREP/FINREP submission packages within year 1.
OKR KR [Acceptance]: ≥90% of fail items in the quality assurance log remediated by the reporting team before submission authorisation; post-submission supervisory query rate on consistency or reconciliation grounds reduced by ≥40% vs. pre-deployment baseline.
OKR KR [Cycle]: Quality assurance log available for Head of Regulatory Reporting review within 4 hours of completed return population, vs. manual spot-check of variable coverage under deadline pressure in the prior process.

### CARD 22 [Insights|S] Regulatory Reporting Quality Trend Analytics
urn: urn:financial-services:scenario:flow/finance-treasury/regulatory-reporting-cycle/regulatory-reporting-quality-trend-analytics
intent: Agent tracks regulatory submission quality metrics across cycles — validation failure rates by source system and form, post-submission query frequencies by supervisor and data category, and exception resolution time — producing a structured quality trend report for the Head of Regulatory Reporting to drive systemic data quality improvement.
Problem to solve: Regulatory submission quality is monitored informally. The Head of Regulatory Reporting cannot produce a trend analysis of validation failure rates, query frequencies, or exception types across submission cycles without manual extraction from submission records across three supervisor perimeters.
Solution: Agent reads the validation exception logs, supervisor query records, and submission metadata from each NBKR, NBK/ARDFM, and CBR cycle. It maintains a rolling quality metrics database and produces a quarterly trend report by supervisor, form, source system, and exception category. The report identifies which source systems and data categories generate disproportionate exception volumes, providing an evidence base to prioritise data quality remediation with source system owners.
OKR objective: Regulatory submission quality metrics — validation failure rates by source system and form, post-submission query frequencies by supervisor and data category, and exception resolution time — are tracked across cycles and a structured quarterly trend report is produced for the Head of Regulatory Reporting to direct systemic data quality improvement.
OKR KR [Adoption]: Agent-produced quality trend report delivered for ≥4 quarterly cycles in year 1; all three supervisor perimeters (NBKR, NBK/ARDFM, CBR) and all material reporting forms covered.
OKR KR [Acceptance]: ≥75% of source system and data category improvement priorities identified in the trend report confirmed as the highest-impact items by the Head of Regulatory Reporting; quality metric deterioration signals validated against submission records in ≥90% of flagged cases.
OKR KR [Cycle]: Quarterly quality trend report available within 5 business days of the last submission in the quarter, vs. no systematic cross-cycle quality tracking in the prior process.

### CARD 23 [Automation|M] Regulatory Validation Exception Triage
urn: urn:financial-services:scenario:flow/finance-treasury/regulatory-reporting-cycle/regulatory-validation-exception-triage
intent: Agent classifies validation exception queue items by root-cause category — source system data quality, mapping defect, regulatory taxonomy change, calculation methodology difference — matches recurring exceptions against a prior-submission knowledge base, and delivers a triage pack with recommended resolution paths to the regulatory reporting team at the start of each submission window.
Problem to solve: Automated validation rule failures generate exception queues that the reporting team resolves manually each cycle. Recurring exceptions — the same source system generating the same data quality fault each submission — are investigated individually rather than resolved by applying the established fix.
Solution: Agent reads the validation exception queue from the submission platform, classifies each item against a root-cause taxonomy, and matches it against the prior-submission exception knowledge base. For recurring items with an established resolution path, agent produces a pre-approved resolution recommendation with supporting lineage evidence; for novel exceptions, it provides a structured investigation brief.
OKR objective: Regulatory validation exception queue items are classified by root-cause category, matched against the prior-submission knowledge base, and provided with recommended resolution paths at the start of each submission window, before the reporting team begins investigation.
OKR KR [Adoption]: Agent-produced validation exception triage pack used for ≥100% of COREP/FINREP, NBKR, and CBR submission windows in year 1; all exception types and root-cause categories covered.
OKR KR [Acceptance]: ≥80% of pre-approved resolution recommendations for recurring exceptions accepted by the reporting team without supplementary investigation; root-cause classification accuracy ≥85% on periodic audit against final resolution records.
OKR KR [Cycle]: Triage pack with resolution recommendations available within 4 hours of exception queue generation, vs. 1–3 days of manual investigation start in the prior process.

### CARD 24 [Enablement|M] BCBS 239 Data Lineage Documentation Maintenance
urn: urn:financial-services:scenario:flow/finance-treasury/regulatory-reporting-cycle/bcbs239-lineage-documentation-maintenance
intent: Agent traverses the data lineage path from source system to submitted regulatory figure for each material reporting cell, produces a structured lineage map in the BCBS 239 prescribed format, and maintains it as a continuously updated artefact available for supervisory examination without manual reconstruction.
Problem to solve: Lineage documentation is maintained manually and may not reflect the most recent production pipeline configuration. Reconstructing lineage for a supervisory query requires the reporting team to trace the path manually, consuming days when examination requests arrive under compressed timeframes.
Solution: Agent reads the regulatory reporting pipeline configuration — source system extracts, transformation rules, mapping tables, and consolidation logic — and maintains a structured lineage map for each material COREP/FINREP reporting cell. The map is updated automatically when pipeline configuration changes are committed. When a supervisory query requests lineage for a specific cell, agent produces the documented lineage path in the prescribed format within one business day.
OKR objective: Data lineage from source system to submitted regulatory figure is maintained as a continuously updated structured artefact for each material COREP/FINREP reporting cell, available for supervisory examination without manual reconstruction.
OKR KR [Adoption]: Agent-maintained lineage maps cover ≥90% of material COREP/FINREP reporting cells within 12 months of go-live; maps updated within 5 business days of each production pipeline configuration change.
OKR KR [Acceptance]: ≥90% of supervisory lineage queries answered from agent-maintained documentation without requiring manual reconstruction; lineage accuracy confirmed in ≥95% of sampled cells on periodic QA review.
OKR KR [Cycle]: Supervisory lineage response time reduced from days of manual tracing to ≤1 business day per queried reporting cell.

### CARD 25 [New opps|M] Supervisory Query Response Knowledge Base
urn: urn:financial-services:scenario:flow/finance-treasury/regulatory-reporting-cycle/supervisory-query-response-knowledge-base
intent: Agent accumulates supervisory query records — the data point challenged, the explanation provided, the methodology accepted, and the resolution outcome — into a searchable knowledge base across submission cycles and supervisors, so the reporting team can retrieve and reuse established responses when similar queries recur rather than reconstructing each investigation from source.
Problem to solve: Supervisory queries are held in individual query files rather than in a structured knowledge base. The reporting team repeats the investigation and drafting effort for similar queries across cycles and across NBKR, NBK/ARDFM, and CBR submissions without access to a shared institutional response library.
Solution: Agent reads resolved supervisory query records — query text, data point referenced, lineage evidence provided, narrative explanation, and supervisor acceptance status — and writes structured entries into the knowledge base indexed by supervisor, reporting form, data category, and query type. When a new query arrives, agent retrieves the closest prior instances with resolution narratives and lineage templates for the reporting team to review, adapt, and approve before submission to the supervisor.
OKR objective: Supervisory query records — challenged data point, explanation provided, methodology accepted, and resolution outcome — are accumulated into a searchable knowledge base across submission cycles and all three supervisor perimeters, enabling the reporting team to retrieve established responses when similar queries recur.
OKR KR [Adoption]: Agent-maintained supervisory query knowledge base covers ≥85% of resolved queries from the preceding 3 submission years within 12 months of go-live; new entries added within 5 business days of query resolution.
OKR KR [Acceptance]: ≥60% of new supervisory queries resolved by the reporting team using prior knowledge-base entries without requiring a full re-investigation; response quality confirmed by supervisor acceptance in ≥90% of cases where a knowledge-base entry was the primary input.
OKR KR [Cycle]: Prior resolution evidence retrievable for a new supervisory query within 1 hour, vs. 1–2 days of manual file search and re-investigation in the prior process.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
×
