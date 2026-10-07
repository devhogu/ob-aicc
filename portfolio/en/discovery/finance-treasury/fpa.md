# FP&A

Financial Planning & Analysis is the Bank's planning and decision-support engine — the function that translates strategy into annual budgets and rolling forecasts, monitors performance against plan, and answers the CFO's and ALCO's real-time analytical questions. Under supervisory requirements, planning outputs feed ICAAP submissions, capital planning reports, and strategic plan filings. **The GenAI opportunity is compressing the reforecast cycle and the variance Q&A cycle from weeks and days to hours** — enabling FP&A to operate at the speed of the business rather than the speed of the model.

## Problems

### Planning & forecasting {#planning-forecasting}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Budget and forecast accuracy is assessed at quarter-end when actuals are available, not during the planning cycle. FP&A lacks a continuous view of how emerging actuals compare to underlying assumptions — deposit beta drift, NIM compression from rate moves, or loan volume deceleration — between formal review checkpoints. |
| Enablement | Event-driven reforecasts — required after a central bank rate decision, a peer earnings surprise, or a macro shift — are bottlenecked on FP&A rebuilding the planning model manually from revised assumptions. The elapsed time from event to CFO-ready reforecast is three to five days at best; at most banks, it is two to three weeks. |
| Automation | Annual budget narratives, rolling forecast packs, and assumption-to-P&L bridges are assembled manually from model outputs and system exports each cycle. The structure of each document is prescribed; the assembly is the constraint. Each planning cycle consumes 200–400 FP&A team-hours before the CFO receives a review-ready pack. |
| New business opportunities | FP&A teams that compress planning cycle times can run more scenario iterations before the budget is locked. Banks that test fifteen demand scenarios rather than three — rate paths, competitive deposit repricing, credit loss distributions — enter the year with a more robust plan and respond to deviations faster. |

## Annual budget cycle {#annual-budget-cycle}

The annual budget cycle is the Bank's primary mechanism for translating the strategic plan into BU-level volume, margin, cost, and capital targets. The approved budget feeds the ICAAP and capital plan filings to the regulator. The cycle runs three to four months and culminates in a board-approved budget with BU-level cascades, assumption documentation, and a CFO narrative pack.

### Budget Assumption Quality Scan

- URN: urn:financial-services:scenario:finance-treasury/fpa/annual-budget-cycle/budget-assumption-quality-scan
- Lens: Insights
- Complexity: S
- Intent: Before the budget model is locked, the AI agent identifies BU assumptions that deviate materially from trailing actuals, the prior-year budget, or the approved FTP curve, and presents a ranked exception list for CFO and FP&A review.
- Problem to solve: Budget assumptions submitted by BUs are reviewed by FP&A through manual cross-referencing against actuals and prior-year submissions. Outlier assumptions — aggressive deposit beta forecasts, NIM projections that conflict with the approved FTP curve — are identified inconsistently across units and only after the full submission round has closed.
- Solution: The AI agent reads each BU submission alongside trailing-twelve-month actuals, the approved FTP curve, and the prior-year budget. It flags assumptions whose deviation from the trailing run rate or FTP anchor exceeds a defined materiality threshold, ranks them by consolidated P&L impact, and produces an exception list for FP&A to challenge before the model lock. BUs are alerted to the flagged line items, enabling targeted revision without reopening the full submission.
- OKR: FP&A and the CFO receive a ranked exception list of BU budget assumptions that deviate materially from trailing-twelve-month actuals, the prior-year budget, or the approved FTP curve — ranked by consolidated P&L impact — before the budget model is locked.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced assumption exception list used for ≥1 annual budget cycle within year 1; all BU submissions scanned before the model lock. |
| Acceptance | ≥75% of flagged assumptions confirmed by FP&A as warranting challenge; ≥80% of confirmed exceptions revised or justified by the submitting BU without reopening the full submission. |
| Cycle | Exception list available within 2 business days of each BU submission, vs. outliers identified only after the full submission round has closed in the prior process. |

### ICAAP-Budget Consistency Check

- URN: urn:financial-services:scenario:finance-treasury/fpa/annual-budget-cycle/icaap-budget-consistency-check
- Lens: Automation
- Complexity: S
- Intent: The AI agent validates that the approved annual budget is consistent with the capital plan assumptions submitted to the regulator in the ICAAP — flagging any volume, RWA, or dividend assumption that differs between the two documents before external filing.
- Problem to solve: The annual budget and the ICAAP capital plan are produced by different teams on overlapping timelines. Inconsistencies between the two — budget loan growth rates that imply a different RWA trajectory than the ICAAP projects, or dividend assumptions that differ between documents — are identified during audit committee review or, in the worst case, by the regulator after submission.
- Solution: The AI agent cross-reads the locked budget model and the current ICAAP draft, maps shared assumptions — loan volume growth, RWA density, dividend payout, and NIM — and produces a reconciliation table identifying every cell where the documents differ. FP&A and Capital Management resolve differences before the ICAAP is submitted. The reconciliation table is retained as evidence for the audit committee and external auditor.
- OKR: FP&A and Capital Management receive a reconciliation table of every shared assumption — loan volume growth, RWA density, dividend payout, and NIM — that differs between the locked budget model and the ICAAP draft, and resolve the differences before the ICAAP is submitted.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced budget-to-ICAAP reconciliation table used for ≥1 annual ICAAP submission cycle within year 1; all shared volume, RWA, dividend, and NIM assumptions mapped. |
| Acceptance | ≥90% of differences listed in the reconciliation table confirmed as genuine by FP&A and Capital Management; all confirmed differences resolved before submission, with the table retained as evidence for the audit committee and external auditor. |
| Cycle | Reconciliation table available within 2 business days of the budget model lock, vs. inconsistencies identified at audit committee review or by the regulator after submission in the prior process. |

### Rolling Forecast & Budget Narrative

- URN: urn:financial-services:scenario:finance-treasury/fpa/annual-budget-cycle/rolling-forecast-budget-narrative
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles BU-level driver assumptions into a consolidated rolling forecast model and drafts the CFO budget or reforecast narrative, ready for review on the day assumptions close. Both the quarterly reforecast and annual budget cycle are served by the same production workflow.
- Problem to solve: The quarterly reforecast cycle extends over several weeks as FP&A waits for BU assumption submissions and rebuilds the consolidated model. Event-driven reforecasts between scheduled cycles are impractical at this pace, and annual budget narrative drafting is similarly bottlenecked on data assembly before CFO review can begin.
- Solution: The AI agent ingests BU driver submissions as they arrive, validates cross-BU consistency — NIM assumptions aligned with deposit beta, volume growth aligned with credit capacity — flags gaps, and runs the consolidated model. For the annual budget cycle, it generates a board-pack narrative from approved model output and prior board submissions as style anchors. The CFO reviews a complete reforecast or budget pack and edits for forward judgment.
- OKR: A consolidated rolling forecast model — assembled from BU driver submissions as they arrive with cross-BU consistency validated — and the CFO budget or reforecast narrative are available for CFO review on the day assumptions close.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced consolidated forecast model and narrative used for ≥4 quarterly reforecast and ≥1 annual budget cycle within year 1. |
| Acceptance | ≥80% of consolidated forecast narratives accepted by the CFO without material structural rewrite; cross-BU NIM, deposit beta, and credit capacity consistency flags confirmed as genuine inconsistencies in ≥85% of cases. |
| Cycle | Consolidated forecast and CFO narrative available on the day BU assumption submissions close, vs. 1–2 weeks of sequential model rebuild and drafting in the prior process. |

## Budget-to-actual variance attribution {#budget-to-actual-variance}

Monthly and quarterly budget-to-actual variance attribution decomposes the gap between plan and actual P&L across revenue, cost, provision, and capital dimensions for each BU and the Bank as a whole. Attribution identifies whether variances are volume-driven, margin-driven, one-time, or indicative of a structural trend — the distinction that determines whether management action is required.

### In-Period Variance Flash

- URN: urn:financial-services:scenario:finance-treasury/fpa/budget-to-actual-variance/in-period-variance-flash
- Lens: Insights
- Complexity: S
- Intent: The AI agent generates an in-period variance flash around day 20 of the month from available intra-month data — revenue run-rate, cost accruals, and provisioning estimates — giving the CFO an early directional read on material P&L deviations before close.
- Problem to solve: The CFO's first quantified view of the period's P&L variance against budget is available only after close, typically three to five business days into the following month. Material variances identified at that point leave limited time for corrective action in the same period or for briefing the board in advance of formal reporting.
- Solution: The AI agent reads available intra-month data — daily transaction revenue feeds, cost accrual estimates, and the ECL model's indicative provision — and applies the Bank's standard variance attribution methodology to produce a directional flash by BU around day 20 of the month. The flash quantifies the estimated budget gap and identifies the top three variance drivers per BU, giving the CFO and segment heads a working view before close. FP&A confirms or revises the flash at close.
- OKR: The CFO and segment heads receive a directional variance flash by BU around day 20 of each month — the estimated budget gap and the top three variance drivers per BU — as a working view before close.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced variance flash delivered for ≥10 of 12 months in year 1; all BUs covered in each flash. |
| Acceptance | Direction of the estimated budget gap confirmed by FP&A at close for ≥85% of BU flashes; ≥75% of the top three drivers named per BU match the drivers in the closed attribution. |
| Cycle | First quantified view of the period's variance available around day 20 of the month, vs. three to five business days into the following month in the prior process. |

### Budget-to-Actual Variance Attribution

- URN: urn:financial-services:scenario:finance-treasury/fpa/budget-to-actual-variance/budget-to-actual-variance-attribution
- Lens: Automation
- Complexity: M
- Intent: The AI agent decomposes the gap between plan and actual P&L across volume, rate, mix, and cost dimensions for each BU and the Bank as a whole, producing a consistent attribution on the first day of reporting.
- Problem to solve: Variance attribution is produced manually by each BU finance team after close, using methodologies that differ across units. The CFO receives a consolidated variance without a consistent analytical frame, and attribution quality depends on the team member assigned each cycle.
- Solution: The AI agent reads the closed ledger actuals and the approved budget assumptions, applies the Bank's standard variance attribution methodology across all P&L lines and BUs, and produces a consolidated output with materiality-ranked variances. BU finance leads confirm the attribution for their units, and the CFO reviews the attributed output and adds qualitative context; attribution methodology is consistent across units and available on the first day of reporting.
- OKR: A consistent budget-to-actual variance attribution — decomposed by volume, rate, mix, and cost across every business unit and the Bank as a whole — is available on the first day of reporting each period.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced variance attribution used for ≥10 of 12 monthly reporting cycles in year 1; attribution covers all BUs and all material P&L lines. |
| Acceptance | ≥85% of AI-produced attribution outputs accepted by BU finance leads as accurate without material restatement; methodology consistency across BUs confirmed on periodic Finance review. |
| Cycle | Variance attribution available on day 1 of the reporting window, vs. 3–5 business days of manual BU-by-BU assembly in the prior process. |

### Structural Variance Trend Detection

- URN: urn:financial-services:scenario:finance-treasury/fpa/budget-to-actual-variance/structural-variance-trend-detection
- Lens: Optimize
- Complexity: M
- Intent: The AI agent classifies budget variances across successive periods into structural and transient categories, surfacing persistent margin or volume deterioration trends before they compound into a budget reforecast event.
- Problem to solve: Monthly variance attribution identifies the current-period gap but does not classify whether the variance is reverting or persistent. A volume shortfall in retail lending may reflect a single timing item or the start of a structural share-of-wallet decline; the CFO and segment heads make different decisions depending on which it is, but the classification requires manual analysis across several months of attribution tables.
- Solution: The AI agent maintains a rolling variance history by BU and P&L line. Each close cycle it classifies new variances as transient — within normal fluctuation range and partially offset in prior periods — or structural, where the same line shows a directional miss across three or more consecutive periods. Structural patterns are surfaced in a ranked flag list for the CFO and FP&A before the monthly management accounts are distributed. Segment heads whose lines carry structural flags are notified for inclusion in the ALCO discussion.
- OKR: The CFO and FP&A receive a ranked list of structural variance patterns — P&L lines with a directional miss across three or more consecutive periods — by BU before the monthly management accounts are distributed.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced structural variance flag list delivered for ≥10 of 12 monthly close cycles in year 1; rolling variance history maintained for all BUs and material P&L lines. |
| Acceptance | ≥75% of structural flags confirmed by FP&A as persistent rather than transient; ≥80% of confirmed flags taken by the segment heads concerned into the ALCO discussion. |
| Cycle | Structural or transient classification available at each monthly close, vs. manual analysis across several months of attribution tables in the prior process. |

## Rolling forecast {#rolling-forecast}

Rolling forecasts refresh the budget with current-period actuals and updated BU assumptions on a quarterly or monthly cadence. Each reforecast cycle requires cross-BU assumption submission, cross-functional consistency checking, and a consolidated model rebuild before the CFO pack is produced. The reforecast is the primary tool by which ALCO and the CFO adjust the Bank's operating plan between annual budget cycles.

### Reforecast Sensitivity Pre-Submission

- URN: urn:financial-services:scenario:finance-treasury/fpa/rolling-forecast/reforecast-sensitivity-pre-submission
- Lens: Optimize
- Complexity: S
- Intent: Before BU submissions close, the AI agent identifies which unit assumptions are most at variance with current trading conditions and quantifies the consolidated P&L impact under each sensitivity. Reforecast conversations are thereby directed to the material items before the CFO cycle begins.
- Problem to solve: Reforecast submissions are collected without a prior view of which BU assumptions are most likely to require revision. FP&A's first consolidated picture of the revised forward outlook is available only after all units have submitted, leaving no time to redirect the highest-sensitivity items before the CFO cycle begins.
- Solution: The AI agent reads current period actuals, prior-cycle BU assumptions, and available trading indicators. It produces a pre-submission sensitivity ranking — which assumptions across BUs are most at variance with current trajectory and what the consolidated P&L spread would be per unit revision. FP&A focuses the pre-submission reforecast calls on the highest-sensitivity assumptions.
- OKR: FP&A receives, before business unit submissions close, a sensitivity ranking that quantifies the consolidated P&L impact of each material BU assumption at variance with current trading conditions, so that reforecast conversations go to the highest-sensitivity items first.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced pre-submission sensitivity ranking used for ≥4 quarterly reforecast cycles and ≥1 annual budget cycle within year 1. |
| Acceptance | ≥75% of high-sensitivity BU assumptions identified in the AI-produced ranking confirmed as requiring revision in the final submitted reforecast; consolidated P&L sensitivity estimates reconcile to the final reforecast model within ±5% in ≥85% of reviewed cycles. |
| Cycle | Pre-submission sensitivity ranking available 5 business days before the BU submission deadline, vs. no pre-submission consolidated view in the prior process. |

### Event-Driven Reforecast Trigger

- URN: urn:financial-services:scenario:finance-treasury/fpa/rolling-forecast/event-driven-reforecast-trigger
- Lens: New opps
- Complexity: S
- Intent: The AI agent monitors external and internal triggers — central bank rate decisions, credit rating downgrades, macro data releases, and material loan book movements — and proposes an off-cycle reforecast when the consolidated P&L impact of a trigger event exceeds a defined materiality threshold.
- Problem to solve: Event-driven reforecasts between scheduled quarterly cycles are initiated ad hoc when the CFO or ALCO judges that an external event materially changes the forward P&L outlook. The judgment is made without a quantified estimate of the consolidated impact, and the reforecast is frequently initiated after the event has already propagated into actuals rather than when forward guidance can still be adjusted.
- Solution: The AI agent reads central bank rate decision feeds, credit rating agency alerts, macro data releases, and the Bank's own daily trading activity. For each material event it estimates the first-order P&L impact using the current reforecast model — NII impact of a rate move, provision impact of a rating migration — and presents the estimate to FP&A with a recommendation on whether the consolidated impact exceeds the materiality threshold for an off-cycle reforecast. FP&A and the CFO confirm the decision; the AI agent prepares the BU communication if a reforecast is triggered.
- OKR: FP&A and the CFO receive a first-order P&L impact estimate and an off-cycle reforecast recommendation for each material trigger event — central bank rate decision, credit rating downgrade, macro data release, or loan book movement — while forward guidance can still be adjusted.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced impact estimates delivered for ≥90% of material trigger events in year 1; all four trigger categories monitored. |
| Acceptance | ≥80% of reforecast recommendations confirmed by FP&A and the CFO; first-order impact estimates fall within ±15% of the subsequent reforecast figure in ≥80% of triggered reforecasts. |
| Cycle | Impact estimate and recommendation available within 1 business day of the trigger event, vs. ad hoc initiation after the event has propagated into actuals in the prior process. |

### Rolling Forecast Driver Insights

- URN: urn:financial-services:scenario:finance-treasury/fpa/rolling-forecast/rolling-forecast-driver-insights
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes completed reforecast cycles to identify which BU-level assumptions have the highest forecast error rate, surfacing persistent calibration biases in volume, margin, or cost assumptions that distort the consolidated model cycle after cycle.
- Problem to solve: Each reforecast cycle is treated as an independent production event. BU assumption accuracy is reviewed informally but no systematic record of assumption error by unit and driver is maintained. FP&A cannot distinguish BUs whose assumptions are structurally optimistic from units that forecast accurately, and the consolidated model carries a systematic bias that is visible only in retrospect at year-end.
- Solution: The AI agent maintains a rolling assumption accuracy register — actual vs. submitted assumption for every BU and material driver across completed reforecast cycles. After each close it updates the register with the resolved actuals, computes per-BU and per-driver mean absolute error and bias direction, and produces a calibration heat map for FP&A. BUs with persistent bias patterns are flagged for assumption-quality conversation before the next submission cycle opens. FP&A retains judgment on any model overlay.
- OKR: FP&A holds a rolling assumption accuracy register and calibration heat map — mean absolute error and bias direction for every BU and material driver — updated after each close and used to flag BUs with persistent bias before the next submission cycle opens.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-maintained accuracy register updated after ≥4 quarterly reforecast cycles within year 1; all BUs and material volume, margin, and cost drivers covered. |
| Acceptance | ≥80% of persistent-bias flags confirmed by FP&A as warranting an assumption-quality conversation with the BU; register entries reconcile to resolved actuals in ≥98% of sampled cells. |
| Cycle | Calibration heat map available within 5 business days of each close, vs. informal review with systematic bias visible only at year-end in the prior process. |

## CFO & ALCO Q&A support {#cfo-alco-qa-support}

CFO and ALCO analytical questions — cross-period comparisons, multi-driver decompositions, scenario sensitivities — arise in real time during board meetings, ALCO sessions, and, where the Bank holds them, investor calls. These questions require cross-system data assembly and multi-source synthesis that currently takes hours or days to produce outside of prepared meeting materials. The same support extends to the ALCO meeting itself: the pre-meeting briefing that gives principals a current-state view, and the decision log that carries actions from one session to the next.

### CFO Scenario Sandbox

- URN: urn:financial-services:scenario:finance-treasury/fpa/cfo-alco-qa-support/cfo-scenario-sandbox
- Lens: New opps
- Complexity: M
- Intent: Conversational interface through which the CFO and ALCO principals query the financial model on demand — cross-period comparisons, multi-driver decompositions, and scenario sensitivities — without queuing a request to the FP&A team.
- Problem to solve: CFO and ALCO analytical questions arise in real time during board sessions and, where the Bank holds them, investor calls, requiring cross-system data assembly and multi-source synthesis that FP&A currently turns around over hours or days. The analytical dependency constrains the CFO's ability to explore scenarios outside the prepared meeting materials.
- Solution: The AI agent maintains a continuously updated parametric view of the Bank's P&L and balance sheet from current data feeds. The CFO queries it conversationally — cross-period NIM decompositions, deposit-beta sensitivities, rate-scenario impacts — and receives an attributed answer within the session. FP&A validates material outputs; the AI agent enables exploratory reasoning that precedes formal model runs.
- OKR: The CFO and ALCO principals query the financial model conversationally on demand — cross-period comparisons, multi-driver decompositions, and scenario sensitivities — within the session, without queuing a request to the FP&A team.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-powered CFO scenario sandbox used for ≥8 board, investor, or ALCO sessions in year 1; ≥3 types of analytical query (decomposition, scenario, cross-period) used in each active session. |
| Acceptance | ≥80% of in-session scenario outputs rated as analytically sound by the CFO without requiring FP&A re-derivation; model output errors on sanity checks ≤3%. |
| Cycle | Time from scenario question to quantified answer reduced from 1–2 days of FP&A queue time to ≤15 minutes within the session. |

### ALCO Pre-Meeting Briefing Pack

- URN: urn:financial-services:scenario:finance-treasury/fpa/cfo-alco-qa-support/alco-pre-meeting-briefing-pack
- Lens: Automation
- Complexity: S
- Intent: The AI agent assembles the ALCO pre-meeting briefing — rate environment summary, NII and EVE sensitivity update, capital and liquidity position, and open action items from the prior session — from current data feeds and presents it to the CFO and Treasurer the evening before the meeting.
- Problem to solve: Pre-meeting ALCO briefing materials are assembled by Treasury and FP&A in the days before the session, drawing on reports from multiple systems. Late-arriving data — end-of-day rate moves, final liquidity ratios — cannot be incorporated before materials are distributed, and ALCO principals enter the meeting without a single current-state summary.
- Solution: The AI agent reads end-of-day rate feeds, the most recent NII and EVE scenario outputs, the current capital and LCR/NSFR position, and the prior ALCO action-item register. It assembles a pre-meeting briefing in the Bank's standard ALCO format — rate environment, IRRBB position, liquidity position, capital headroom, open actions — and distributes it to the CFO and Treasurer by 7pm the day before the session. ALCO principals enter each session with a current-state view.
- OKR: The CFO and Treasurer receive the ALCO pre-meeting briefing — rate environment, IRRBB position, liquidity position, capital headroom, and open actions — in the standard ALCO format by 7pm on the day before each session, built from end-of-day data.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced pre-meeting briefing distributed for ≥90% of ALCO sessions in year 1; all five standard sections included in each briefing. |
| Acceptance | ≥85% of briefings accepted by the CFO and Treasurer without material correction; rate, liquidity, and capital figures reconcile to end-of-day source data in ≥98% of reviewed briefings. |
| Cycle | Briefing reflects end-of-day data on the evening before the session, vs. materials assembled over several days that cannot incorporate late-arriving data in the prior process. |

### Post-ALCO Decision & Action Log

- URN: urn:financial-services:scenario:finance-treasury/fpa/cfo-alco-qa-support/post-alco-decision-log
- Lens: Insights
- Complexity: S
- Intent: The AI agent reads the ALCO meeting recording or draft minutes, extracts decisions and action items with owners and deadlines, and produces a structured decision log that is cross-referenced against prior-session actions to identify unresolved items at the next meeting.
- Problem to solve: ALCO decisions and action items are recorded in meeting minutes that are written and circulated manually after each session. Open actions from prior sessions are tracked in a separate register that is not consistently referenced when the next agenda is prepared, and recurring unresolved items accumulate without systematic escalation.
- Solution: The AI agent reads the ALCO meeting recording or draft minutes, extracts each decision and action item, assigns owner and deadline from the discussion, and appends entries to the structured decision log. Before each subsequent ALCO, the AI agent cross-references the log against items due for that session and flags unresolved items for inclusion in the agenda. The CFO's office reviews and confirms the log before distribution; the AI agent does not determine materiality or escalation.
- OKR: The CFO's office holds a structured ALCO decision log — each decision and action item with owner and deadline — in which unresolved items from prior sessions are flagged for the agenda before each subsequent ALCO.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced decision log entries created for ≥90% of ALCO sessions in year 1; open items cross-referenced before every subsequent session. |
| Acceptance | ≥90% of extracted decisions and action items confirmed by the CFO's office without correction of owner or deadline; ≥95% of unresolved items due for a session flagged for its agenda. |
| Cycle | Draft decision log available for CFO's office review within 1 business day of the session, vs. manually written minutes and a separate, inconsistently referenced action register in the prior process. |
