# 

source: html-alt/financial-services/en/finance-treasury/fpa/index.html


[PAGE TEXT]
Annual budget cycle
The annual budget cycle is the bank's primary mechanism for translating the strategic plan into BU-level volume, margin, cost, and capital targets. Under NBKR, NBK/ARDFM, and CBR supervisory frameworks, the approved budget feeds ICAAP and capital plan filings. The cycle runs three to four months and culminates in a board-approved budget with BU-level cascades, assumption documentation, and a CFO narrative pack.
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|S] Budget Assumption Quality Scan
urn: urn:financial-services:scenario:finance-treasury/fpa/annual-budget-cycle/budget-assumption-quality-scan
intent: Before the budget model is locked, agent identifies BU assumptions that deviate materially from trailing actuals, peer benchmarks, or approved FTP curves, and presents a ranked exception list for CFO and FP&A review.
Problem to solve: Budget assumptions submitted by BUs are reviewed by FP&A through manual cross-referencing against actuals and prior-year submissions. Outlier assumptions — aggressive deposit beta forecasts, NIM projections that conflict with the approved FTP curve — are identified inconsistently across units and only after the full submission round has closed.
Solution: Agent reads each BU submission alongside trailing-twelve-month actuals, the approved FTP curve, and the prior-year budget. It flags assumptions whose deviation from the trailing run rate or FTP anchor exceeds a defined materiality threshold, ranks them by consolidated P&L impact, and produces an exception list for FP&A to challenge before the model lock. BUs are alerted to the flagged line items, enabling targeted revision without reopening the full submission.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Automation|S] ICAAP-Budget Consistency Check
urn: urn:financial-services:scenario:finance-treasury/fpa/annual-budget-cycle/icaap-budget-consistency-check
intent: Agent validates that the approved annual budget is consistent with the capital plan assumptions submitted to NBKR, NBK/ARDFM, or CBR in the ICAAP — flagging any volume, RWA, or dividend assumption that differs between the two documents before external filing.
Problem to solve: The annual budget and the ICAAP capital plan are produced by different teams on overlapping timelines. Inconsistencies between the two — budget loan growth rates that imply a different RWA trajectory than the ICAAP projects, or dividend assumptions that differ between documents — are identified during audit committee review or, in the worst case, by the regulator after submission.
Solution: Agent cross-reads the locked budget model and the current ICAAP draft, maps shared assumptions — loan volume growth, RWA density, dividend payout, and NIM — and produces a reconciliation table identifying every cell where the documents differ. FP&A and Capital Management resolve differences before the ICAAP is submitted. The reconciliation table is retained as evidence for the audit committee and external auditor.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Automation|M] Rolling Forecast & Budget Narrative
urn: urn:financial-services:scenario:finance-treasury/fpa/annual-budget-cycle/rolling-forecast-budget-narrative
intent: Agent assembles BU-level driver assumptions into a consolidated rolling forecast model and drafts the CFO budget or reforecast narrative, ready for review on the day assumptions close. Both the quarterly reforecast and annual budget cycle are served by the same production workflow.
Problem to solve: The quarterly reforecast cycle extends over several weeks as FP&A waits for BU assumption submissions and rebuilds the consolidated model. Event-driven reforecasts between scheduled cycles are impractical at this pace, and annual budget narrative drafting is similarly bottlenecked on data assembly before CFO review can begin.
Solution: Agent ingests BU driver submissions as they arrive, validates cross-BU consistency — NIM assumptions aligned with deposit beta, volume growth aligned with credit capacity — flags gaps, and runs the consolidated model. For the annual budget cycle, it generates a board-pack narrative from approved model output and prior board submissions as style anchors. CFO reviews a complete reforecast or budget pack and edits for forward judgment.
OKR objective: A consolidated rolling forecast model — assembled from BU driver submissions as they arrive with cross-BU consistency validated — and the CFO budget or reforecast narrative are available for CFO review on the day assumptions close.
OKR KR [Adoption]: Agent-produced consolidated forecast model and narrative used for ≥4 quarterly reforecast and ≥1 annual budget cycle within year 1.
OKR KR [Acceptance]: ≥80% of consolidated forecast narratives accepted by the CFO without material structural rewrite; cross-BU NIM, deposit beta, and credit capacity consistency flags confirmed as genuine inconsistencies in ≥85% of cases.
OKR KR [Cycle]: Consolidated forecast and CFO narrative available on the day BU assumption submissions close, vs. 1–2 weeks of sequential model rebuild and drafting in the prior process.

[PAGE TEXT]
Budget-to-actual variance attribution
Monthly and quarterly budget-to-actual variance attribution decomposes the gap between plan and actual P&L across revenue, cost, provision, and capital dimensions for each BU and the consolidated bank. Attribution identifies whether variances are volume-driven, margin-driven, one-time, or indicative of a structural trend — the distinction that determines whether management action is required.
Lens
Scenario
Intent
Complexity

### CARD 4 [Insights|S] In-Period Variance Flash
urn: urn:financial-services:scenario:finance-treasury/fpa/budget-to-actual-variance/in-period-variance-flash
intent: Agent generates a mid-month variance flash from available trading data — revenue run-rate, cost accruals, and provisioning estimates — giving the CFO an early directional read on material P&L deviations before close.
Problem to solve: The CFO's first quantified view of the period's P&L variance against budget is available only after close, typically three to five business days into the following month. Material variances identified at that point leave limited time for corrective action in the same period or for briefing the board in advance of formal reporting.
Solution: Agent reads available intra-month data — daily transaction revenue feeds, cost accrual estimates, and the ECL model's indicative provision — and applies the bank's standard variance attribution methodology to produce a directional flash by BU around day 20 of the month. The flash quantifies the estimated budget gap and identifies the top three variance drivers per BU, giving the CFO and segment heads a working view before close. FP&A confirms or revises the flash at close.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Automation|M] Budget-to-Actual Variance Attribution
urn: urn:financial-services:scenario:finance-treasury/fpa/budget-to-actual-variance/budget-to-actual-variance-attribution
intent: Agent decomposes the gap between plan and actual P&L across volume, rate, mix, and cost dimensions for each BU and the consolidated bank, producing a consistent attribution on the first day of reporting.
Problem to solve: Variance attribution is produced manually by each BU finance team after close, using methodologies that differ across units. The CFO receives a consolidated variance without a consistent analytical frame, and attribution quality depends on the team member assigned each cycle.
Solution: Agent reads the closed ledger actuals and the approved budget assumptions, applies the bank's standard variance attribution methodology across all P&L lines and BUs, and produces a consolidated output with materiality-ranked variances. The CFO reviews the attributed output and adds qualitative context; attribution methodology is consistent across units and available on the first day of reporting.
OKR objective: A consistent budget-to-actual variance attribution — decomposed by volume, rate, mix, and cost across every business unit and the consolidated bank — is available on the first day of reporting each period.
OKR KR [Adoption]: Agent-produced variance attribution used for ≥10 of 12 monthly reporting cycles in year 1; attribution covers all BUs and all material P&L lines.
OKR KR [Acceptance]: ≥85% of agent-produced attribution outputs accepted by BU finance leads as accurate without material restatement; methodology consistency across BUs confirmed on periodic Finance review.
OKR KR [Cycle]: Variance attribution available on day 1 of the reporting window, vs. 3–5 business days of manual BU-by-BU assembly in the prior process.

### CARD 6 [Optimize|M] Structural Variance Trend Detection
urn: urn:financial-services:scenario:finance-treasury/fpa/budget-to-actual-variance/structural-variance-trend-detection
intent: Agent classifies budget variances across successive periods into structural and transient categories, surfacing persistent margin or volume deterioration trends before they compound into a budget reforecast event.
Problem to solve: Monthly variance attribution identifies the current-period gap but does not classify whether the variance is reverting or persistent. A volume shortfall in retail lending may reflect a single timing item or the start of a structural share-of-wallet decline; the CFO and segment heads make different decisions depending on which it is, but the classification requires manual analysis across several months of attribution tables.
Solution: Agent maintains a rolling variance history by BU and P&L line. Each close cycle it classifies new variances as transient — within normal fluctuation range and partially offset in prior periods — or structural, where the same line shows a directional miss across three or more consecutive periods. Structural patterns are surfaced in a ranked flag list for the CFO and FP&A before the monthly management accounts are distributed. Segment heads whose lines carry structural flags are notified for inclusion in the ALCO discussion.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Rolling forecast
Rolling forecasts refresh the budget with current-period actuals and updated BU assumptions on a quarterly or monthly cadence. Each reforecast cycle requires cross-BU assumption submission, cross-functional consistency checking, and a consolidated model rebuild before the CFO pack is produced. The reforecast is the primary tool by which ALCO and the CFO adjust the bank's operating plan between annual budget cycles.
Lens
Scenario
Intent
Complexity

### CARD 7 [Optimize|S] Reforecast Sensitivity Pre-Submission
urn: urn:financial-services:scenario:finance-treasury/fpa/rolling-forecast/reforecast-sensitivity-pre-submission
intent: Before BU submissions close, agent identifies which unit assumptions are most at variance with current trading conditions and quantifies the consolidated P&L impact under each sensitivity. Reforecast conversations are thereby directed to the material items before the CFO cycle begins.
Problem to solve: Reforecast submissions are collected without a prior view of which BU assumptions are most likely to require revision. FP&A's first consolidated picture of the revised forward outlook is available only after all units have submitted, leaving no time to redirect the highest-sensitivity items before the CFO cycle begins.
Solution: Agent reads current period actuals, prior-cycle BU assumptions, and available trading indicators. It produces a pre-submission sensitivity ranking — which assumptions across BUs are most at variance with current trajectory and what the consolidated P&L spread would be per unit revision. FP&A focuses the pre-submission reforecast calls on the highest-sensitivity assumptions.
OKR objective: Before business unit submissions close, the consolidated P&L impact under each material BU assumption variance from current trading conditions is quantified and a pre-submission sensitivity ranking is available to FP&A for directing reforecast conversations to the highest-sensitivity items.
OKR KR [Adoption]: Agent-produced pre-submission sensitivity ranking used for ≥4 quarterly reforecast cycles and ≥1 annual budget cycle within year 1.
OKR KR [Acceptance]: ≥75% of high-sensitivity BU assumptions identified in the agent-produced ranking confirmed as requiring revision in the final submitted reforecast; consolidated P&L sensitivity estimates reconcile to the final reforecast model within ±5% in ≥85% of reviewed cycles.
OKR KR [Cycle]: Pre-submission sensitivity ranking available 5 business days before the BU submission deadline, vs. no pre-submission consolidated view in the prior process.

### CARD 8 [New opps|S] Event-Driven Reforecast Trigger
urn: urn:financial-services:scenario:finance-treasury/fpa/rolling-forecast/event-driven-reforecast-trigger
intent: Agent monitors external and internal triggers — central bank rate decisions, credit rating downgrades, macro data releases, and material loan book movements — and proposes an off-cycle reforecast when the consolidated P&L impact of a trigger event exceeds a defined materiality threshold.
Problem to solve: Event-driven reforecasts between scheduled quarterly cycles are initiated ad hoc when the CFO or ALCO judges that an external event materially changes the forward P&L outlook. The judgment is made without a quantified estimate of the consolidated impact, and the reforecast is frequently initiated after the event has already propagated into actuals rather than when forward guidance can still be adjusted.
Solution: Agent reads central bank rate decision feeds, credit rating agency alerts, macro data releases, and the bank's own daily trading activity. For each material event it estimates the first-order P&L impact using the current reforecast model — NII impact of a rate move, provision impact of a rating migration — and presents the estimate to FP&A with a recommendation on whether the consolidated impact exceeds the materiality threshold for an off-cycle reforecast. FP&A and the CFO confirm the decision; the agent prepares the BU communication if a reforecast is triggered.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Insights|M] Rolling Forecast Driver Insights
urn: urn:financial-services:scenario:finance-treasury/fpa/rolling-forecast/rolling-forecast-driver-insights
intent: Agent analyses completed reforecast cycles to identify which BU-level assumptions have the highest forecast error rate, surfacing persistent calibration biases in volume, margin, or cost assumptions that distort the consolidated model cycle after cycle.
Problem to solve: Each reforecast cycle is treated as an independent production event. BU assumption accuracy is reviewed informally but no systematic record of assumption error by unit and driver is maintained. FP&A cannot distinguish BUs whose assumptions are structurally optimistic from units that forecast accurately, and the consolidated model carries a systematic bias that is visible only in retrospect at year-end.
Solution: Agent maintains a rolling assumption accuracy register — actual vs. submitted assumption for every BU and material driver across completed reforecast cycles. After each close it updates the register with the resolved actuals, computes per-BU and per-driver mean absolute error and bias direction, and produces a calibration heat map for FP&A. BUs with persistent bias patterns are flagged for assumption-quality conversation before the next submission cycle opens. FP&A retains judgment on any model overlay.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
CFO & ALCO Q&A support
CFO and ALCO analytical questions — cross-period comparisons, multi-driver decompositions, scenario sensitivities — arise in real time during board meetings, ALCO sessions, and investor calls. These questions require cross-system data assembly and multi-source synthesis that currently takes hours or days to produce outside of prepared meeting materials.
Lens
Scenario
Intent
Complexity

### CARD 10 [New opps|S] CFO Scenario Sandbox
urn: urn:financial-services:scenario:finance-treasury/fpa/cfo-alco-qa-support/cfo-scenario-sandbox
intent: Conversational interface through which the CFO and ALCO principals query the financial model on demand — cross-period comparisons, multi-driver decompositions, and scenario sensitivities — without queuing a request to the FP&A team.
Problem to solve: CFO and ALCO analytical questions arise in real time during board sessions and investor calls, requiring cross-system data assembly and multi-source synthesis that FP&A currently turns around over hours or days. The analytical dependency constrains the CFO's ability to explore scenarios outside the prepared meeting materials.
Solution: Agent maintains a continuously updated parametric view of the bank's P&L and balance sheet from current data feeds. The CFO queries it conversationally — cross-period NIM decompositions, deposit-beta sensitivities, rate-scenario impacts — and receives an attributed answer within the session. FP&A validates material outputs; the agent enables exploratory reasoning that precedes formal model runs.
OKR objective: The CFO and ALCO principals query the financial model conversationally on demand — cross-period comparisons, multi-driver decompositions, and scenario sensitivities — within the session, without queuing a request to the FP&A team.
OKR KR [Adoption]: Agent-powered CFO scenario sandbox used for ≥8 board, investor, or ALCO sessions in year 1; ≥3 types of analytical query (decomposition, scenario, cross-period) used in each active session.
OKR KR [Acceptance]: ≥80% of in-session scenario outputs rated as analytically sound by the CFO without requiring FP&A re-derivation; model output errors on sanity checks ≤3%.
OKR KR [Cycle]: Time from scenario question to quantified answer reduced from 1–2 days of FP&A queue time to ≤15 minutes within the session.

### CARD 11 [Automation|S] ALCO Pre-Meeting Briefing Pack
urn: urn:financial-services:scenario:finance-treasury/fpa/cfo-alco-qa-support/alco-pre-meeting-briefing-pack
intent: Agent assembles the ALCO pre-meeting briefing — rate environment summary, NII and EVE sensitivity update, capital and liquidity position, and open action items from the prior session — from current data feeds and presents it to the CFO and Treasurer the evening before the meeting.
Problem to solve: Pre-meeting ALCO briefing materials are assembled by Treasury and FP&A in the days before the session, drawing on reports from multiple systems. Late-arriving data — end-of-day rate moves, final liquidity ratios — cannot be incorporated before materials are distributed, and ALCO principals enter the meeting without a single current-state summary.
Solution: Agent reads end-of-day rate feeds, the most recent NII and EVE scenario outputs, the current capital and LCR/NSFR position, and the prior ALCO action-item register. It assembles a pre-meeting briefing in the bank's standard ALCO format — rate environment, IRRBB position, liquidity position, capital headroom, open actions — and distributes it to the CFO and Treasurer by 7pm the day before the session. ALCO principals enter each session with a current-state view.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Insights|S] Post-ALCO Decision & Action Log
urn: urn:financial-services:scenario:finance-treasury/fpa/cfo-alco-qa-support/post-alco-decision-log
intent: Agent transcribes ALCO meeting minutes, extracts decisions and action items with owners and deadlines, and produces a structured decision log that is cross-referenced against prior-session actions to identify unresolved items at the next meeting.
Problem to solve: ALCO decisions and action items are recorded in meeting minutes that are written and circulated manually after each session. Open actions from prior sessions are tracked in a separate register that is not consistently referenced when the next agenda is prepared, and recurring unresolved items accumulate without systematic escalation.
Solution: Agent reads the ALCO meeting recording or draft minutes, extracts each decision and action item, assigns owner and deadline from the discussion, and appends entries to the structured decision log. Before each subsequent ALCO, agent cross-references the log against items due for that session and flags unresolved items for inclusion in the agenda. The CFO's office reviews and confirms the log before distribution; the agent does not determine materiality or escalation.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
