# 

source: html-alt/financial-services/en/risk-control/liquidity-risk/index.html


[PAGE TEXT]
LCR & NSFR reporting
The Liquidity Coverage Ratio (LCR) measures the stock of High-Quality Liquid Assets (HQLA) relative to 30-day net cash outflows under a combined stress scenario — the regulatory minimum is 100% under Basel III and NBKR implementing regulations. The Net Stable Funding Ratio (NSFR) measures the proportion of stable funding relative to required stable funding over a one-year horizon — regulatory minimum also 100%. Both ratios are calculated daily (LCR) and monthly (NSFR) from treasury system feeds, with the narrative explaining drivers of movement, HQLA composition, and buffer headroom above the supervisory minimum.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] LCR/NSFR Daily Ratio Narrative
urn: urn:financial-services:scenario:risk-control/liquidity-risk/lcr-nsfr-reporting/lcr-nsfr-daily-ratio-narrative
intent: Agent generates the daily LCR and NSFR management narrative — ratio level, key driver movements, and regulatory threshold distance — from the overnight regulatory calculation run.
Problem to solve: Daily LCR and NSFR ratios are produced by the regulatory calculation engine, but the management commentary — which HQLA categories moved, which outflow buckets drove the ratio change, and how far the ratio sits from the regulatory minimum — is assembled manually each morning.
Solution: Agent reads the overnight regulatory calculation output, maps ratio movements to component drivers, computes threshold distance, and produces the standard management narrative. The treasury risk officer reviews and releases before the morning stand-up.
OKR objective: The treasury risk officer releases the daily LCR and NSFR management narrative — with ratio level, driver decomposition, and regulatory threshold distance — following a brief review of the agent-generated draft rather than manual morning assembly.
OKR KR [Adoption]: Agent used to generate the daily LCR/NSFR management narrative on ≥200 business days per year within 6 months of go-live; all standard narrative components (ratio level, driver movements, threshold distance) produced in every run.
OKR KR [Acceptance]: ≥90% of agent-generated narratives released by the treasury risk officer without material amendment; ratio driver mapping accuracy confirmed at ≥95% on monthly quality checks.
OKR KR [Cycle]: Daily narrative draft available to the treasury risk officer within 30 minutes of overnight calculation run completion, versus ≥90 minutes of manual commentary assembly under the prior approach.

### CARD 2 [Insights|M] LCR Component Sensitivity Analysis
urn: urn:financial-services:scenario:risk-control/liquidity-risk/lcr-nsfr-reporting/lcr-sensitivity-analysis
intent: Agent models LCR sensitivity to defined outflow and HQLA scenarios — a 10% increase in unsecured wholesale outflows, a rating downgrade triggering additional collateral calls — delivering the sensitivity table to the ALCO ahead of each meeting.
Problem to solve: ALCO discusses LCR headroom based on the current ratio without a forward-looking sensitivity view. The headroom available to absorb a specific liquidity stress — a wholesale funding withdrawal, a margin call, a collateral downgrade trigger — requires scenario analysis that is produced for ILAAP but not for routine ALCO reporting.
Solution: Agent reads the current LCR components and applies a defined set of sensitivity scenarios — outflow rate increases, HQLA haircut changes, collateral trigger outflows. It computes the resulting LCR under each scenario, ranks scenarios by impact, and delivers the sensitivity table to the ALCO secretary alongside the standard LCR report.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Insights|M] NSFR Structural Funding Analysis
urn: urn:financial-services:scenario:risk-control/liquidity-risk/lcr-nsfr-reporting/nsfr-structural-funding-analysis
intent: Agent analyses NSFR component trends — available stable funding by source and required stable funding by asset class — to identify structural funding mismatches developing before they affect the regulatory ratio.
Problem to solve: The monthly NSFR report provides the ratio and a driver narrative. Structural trends in funding composition — a gradual shift from stable retail deposits to less stable wholesale funding, or an increase in required stable funding from longer-duration lending — build over multiple months and are not visible in the single-period ratio narrative.
Solution: Agent reads 12 months of NSFR component data, decomposes available stable funding by source and required stable funding by asset class, computes component trend lines, and identifies structural mismatches developing in either the funding or asset mix. The ALCO receives the structural analysis in the quarterly ILAAP review pack.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Stress & contingency funding
Liquidity stress testing models the bank's funding survival horizon under defined stress scenarios — idiosyncratic (loss of market confidence), market-wide (systemic liquidity crunch), and combined. The Contingency Funding Plan (CFP) maps the activation sequence of emergency liquidity levers — HQLA monetization, central bank facilities, asset sales — against defined trigger conditions. Under ILAAP requirements and NBKR supervisory guidance, the CFP must demonstrate a minimum survival horizon of 30 days under the combined stress scenario. CFP triggers must be calibrated to the bank's actual funding structure and reviewed at least annually.
Lens
Scenario
Intent
Complexity

### CARD 4 [Enablement|M] Liquidity Stress Scenario Narrative
urn: urn:financial-services:scenario:risk-control/liquidity-risk/stress-contingency-funding/liquidity-stress-scenario-narrative
intent: Agent constructs the ILAAP liquidity stress narrative — survival horizon by scenario, HQLA monetization capacity, and CFP trigger mapping — from current treasury and deposit position data.
Problem to solve: Each ILAAP cycle requires the treasury risk team to assemble the liquidity stress narrative through manual modelling and drafting. The exercise covers survival horizon by scenario, runoff assumptions, HQLA monetization sequence, and CFP trigger calibration, consuming several weeks of senior analyst effort.
Solution: Agent reads current deposit positions, HQLA composition, wholesale funding maturity profile, and prior ILAAP runoff assumptions. It models survival horizon under each stress scenario, maps CFP trigger points, and drafts the liquidity stress narrative. The treasury risk team reviews assumptions and adds forward judgement before regulatory submission.
OKR objective: The treasury risk team reviews assumptions and adds forward judgement to an agent-constructed ILAAP liquidity stress narrative — covering survival horizon, HQLA monetization capacity, and CFP trigger mapping — modelled from current position data.
OKR KR [Adoption]: Agent used to construct the liquidity stress narrative for ≥1 ILAAP submission cycle within 18 months of go-live; all prescribed components (survival horizon by scenario, runoff assumptions, HQLA sequence, CFP triggers) produced by the agent from go-live.
OKR KR [Acceptance]: ≥80% of agent-constructed narrative sections accepted by the treasury risk team without structural revision; supervisory feedback items on liquidity stress narrative quality reduced by ≥30% versus prior submission.
OKR KR [Cycle]: Liquidity stress narrative draft delivered within 5 business days of current position data cut, reducing the overall ILAAP liquidity section cycle from ≥4 weeks of senior analyst effort.

### CARD 5 [Automation|M] CFP Trigger Monitoring
urn: urn:financial-services:scenario:risk-control/liquidity-risk/stress-contingency-funding/cfp-trigger-monitoring
intent: Agent monitors the bank's defined CFP trigger indicators daily — credit rating signals, wholesale funding access metrics, deposit outflow rates, and market confidence proxies — and alerts the CRO and Head of Treasury when a trigger threshold is approached.
Problem to solve: CFP trigger indicators are defined in the ILAAP and reviewed in the quarterly ILAAP update. Monitoring the indicators against the trigger levels between ILAAP cycles requires treasury risk staff to check multiple data sources; there is no automated alert when a trigger indicator approaches its threshold.
Solution: Agent reads the CFP trigger indicator schedule, monitors each indicator on a daily basis from the relevant system feeds, and delivers an automated alert to the CRO and Head of Treasury when any indicator is within 20% of its trigger threshold. The Head of Treasury initiates the CFP pre-activation protocol.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Insights|M] Survival Horizon Scenario Refresh
urn: urn:financial-services:scenario:risk-control/liquidity-risk/stress-contingency-funding/survival-horizon-scenario-refresh
intent: Agent refreshes the ILAAP survival horizon estimate quarterly using current deposit, HQLA, and wholesale funding data, giving the ALCO a current-position survival estimate rather than the prior ILAAP submission figure.
Problem to solve: The survival horizon estimate presented to the ALCO reflects the ILAAP submission, which may be six to twelve months old. The current survival horizon under each stress scenario changes with the balance sheet composition; management is making liquidity risk decisions against a stale estimate.
Solution: Agent reads current deposit balances by behavioural segment, HQLA composition, and wholesale funding maturity profile. It applies the ILAAP stress scenario runoff and outflow assumptions to the current position and computes the updated survival horizon under idiosyncratic, market-wide, and combined scenarios. The ALCO receives the refreshed estimate at each quarterly meeting alongside the prior ILAAP submission figure.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Intraday liquidity monitoring
Intraday liquidity is the bank's capacity to meet payment and settlement obligations throughout the business day — across RTGS, correspondent banking, and securities settlement systems. Under BCBS 248 and CBR intraday liquidity guidelines, banks must monitor peak intraday liquidity usage, available intraday liquidity facilities, and the timing of significant payment outflows. Intraday liquidity stress — where a large counterparty fails to deliver expected inflows — can create settlement delays that cascade through the payment system. Monitoring intraday liquidity positions requires real-time feeds from payment and settlement systems.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] Settlement Counterparty Behaviour Monitor
urn: urn:financial-services:scenario:risk-control/liquidity-risk/intraday-liquidity-monitoring/settlement-counterparty-behaviour-monitor
intent: Agent monitors intraday payment timing from the bank's material settlement counterparties, flags counterparties whose inflow timing has shifted relative to historical patterns, and alerts treasury operations to potential settlement stress.
Problem to solve: Settlement stress typically manifests as a counterparty that normally delivers funds by 11:00 failing to deliver, creating a liquidity gap the treasury team must manage. The current monitoring requires treasury operations staff to check counterparty inflow status manually during the business day rather than receiving an automated alert when the timing deviation exceeds the threshold.
Solution: Agent reads real-time payment system data, tracks inflow timing per material counterparty against their rolling 20-day median timing, and delivers an alert to treasury operations when a counterparty's expected inflow is delayed beyond the defined threshold. The treasury operations team initiates the contingency protocol before the intraday position deteriorates.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Insights|M] Intraday Liquidity Position Watch
urn: urn:financial-services:scenario:risk-control/liquidity-risk/intraday-liquidity-monitoring/intraday-liquidity-position-watch
intent: Agent monitors intraday payment flows and liquidity usage continuously, flagging settlement pressure and peak intraday usage events for the Head of Treasury.
Problem to solve: Intraday liquidity monitoring requires treasury operations staff to track payment flows, correspondent bank positions, and RTGS usage throughout the business day from multiple system screens. Settlement pressure events — large counterparty inflow delays, unexpected outflow spikes — are identified when a team member checks the system rather than by an automated alert.
Solution: Agent reads real-time payment system feeds, correspondent account positions, and RTGS capacity utilization. It monitors peak intraday usage relative to available facilities, flags counterparty inflow delays above threshold, and delivers a structured morning position report with intraday event alerts to the Head of Treasury.
OKR objective: The Head of Treasury manages intraday liquidity from a structured morning position report and continuous intraday event alerts generated by agent monitoring of payment flows, correspondent positions, and RTGS capacity.
OKR KR [Adoption]: Agent intraday liquidity monitoring running continuously on ≥200 business days per year within 6 months of go-live; morning position report delivered to the Head of Treasury before the daily open for ≥200 business days per year.
OKR KR [Acceptance]: ≥85% of agent-generated settlement pressure alerts rated as accurate by the Head of Treasury; ≤10% false-positive rate on intraday event alerts measured over rolling 90-day windows.
OKR KR [Cycle]: Intraday event alert delivered within 5 minutes of threshold breach, versus identification latency of ≥15 minutes under the prior manual monitoring approach.

### CARD 9 [Insights|M] Intraday Peak Usage Trend Analysis
urn: urn:financial-services:scenario:risk-control/liquidity-risk/intraday-liquidity-monitoring/intraday-peak-usage-trend-analysis
intent: Agent analyses rolling 90-day intraday liquidity usage data to identify trend in peak usage relative to available facilities, seasonal patterns, and counterparty-specific inflow timing shifts, for the BCBS 248 intraday reporting and ALCO liquidity review.
Problem to solve: BCBS 248 requires banks to monitor and report intraday peak usage trends. Trend analysis across the 90-day reporting window requires aggregating daily peak usage records, computing percentile distributions, and identifying shifts in usage patterns — a manual analysis exercise not routinely performed outside the quarterly BCBS 248 reporting cycle.
Solution: Agent reads 90 days of intraday usage records, computes peak usage trends and percentile distributions, identifies seasonal patterns and counterparty-specific inflow timing shifts, and produces the BCBS 248 intraday liquidity report. The Head of Treasury reviews and submits.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Funding runoff & concentration
Funding runoff risk is the risk that liability providers — retail depositors, wholesale funders, institutional counterparties — withdraw funding faster than the bank can replace it under stress conditions. Concentration in the funding base amplifies runoff risk: a small number of large depositors or a concentrated wholesale funding maturity cliff can produce correlated outflows that HQLA cannot absorb. ILAAP behavioural assumptions calibrate retail deposit runoff rates; wholesale funding concentration triggers enhanced monitoring under NBKR liquidity risk guidelines.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|S] Wholesale Funding Maturity Cliff Watch
urn: urn:financial-services:scenario:risk-control/liquidity-risk/funding-runoff-concentration/wholesale-funding-maturity-cliff-watch
intent: Agent reads the wholesale funding maturity ladder daily, identifies upcoming maturity concentrations within the 30-day LCR stress window and 90-day horizon, and delivers an early-warning alert to the Head of Treasury.
Problem to solve: Wholesale funding maturity concentrations are visible in the LCR maturity ladder but are not monitored on a rolling forward-looking basis outside the daily LCR calculation. A material maturity cliff forming within a 30-day window may be visible in the data two weeks before it occurs but goes unalerted until the daily LCR report surfaces it.
Solution: Agent reads the wholesale funding maturity ladder, computes net maturity flow by day and week over the rolling 90-day horizon, and flags concentration points where gross maturities exceed the defined threshold relative to available refinancing capacity. The Head of Treasury receives the alert three weeks before the concentration date.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Insights|M] Funding Runoff & Concentration Watch
urn: urn:financial-services:scenario:risk-control/liquidity-risk/funding-runoff-concentration/funding-runoff-concentration-watch
intent: Agent monitors daily deposit flows for runoff signals and funding concentration patterns, flagging deviations from ILAAP behavioural assumptions for the CRO and ALCO.
Problem to solve: Funding concentration risk accumulates between quarterly ILAAP reviews. Large depositor account movements, wholesale funding share increases, and retail behavioural runoff deviations from ILAAP assumptions are identified when the quarterly review surfaces the movement rather than as signals develop.
Solution: Agent monitors daily deposit flows by counterparty, channel, and product type against ILAAP behavioural assumptions. It surfaces concentration signals and runoff deviations, delivering a weekly funding-risk digest to the ALCO secretary and CRO.
OKR objective: The ALCO and CRO receive a weekly funding-risk digest with agent-identified deposit runoff deviations and funding concentration signals referenced to ILAAP behavioural assumptions.
OKR KR [Adoption]: Agent monitoring daily deposit flows against ILAAP behavioural assumptions within 3 months of go-live; weekly digest delivered to ALCO secretary and CRO for ≥45 consecutive weeks in year 1.
OKR KR [Acceptance]: ≥75% of agent-flagged runoff deviations and concentration signals rated as material by the ALCO on review; ≤10% false-positive rate on weekly flags measured over rolling 90-day windows.
OKR KR [Cycle]: Weekly funding-risk digest delivered within 1 business day of each monitoring cycle close, versus a quarterly identification cadence under the prior ILAAP review approach.

### CARD 12 [Insights|M] ILAAP Behavioural Assumption Drift Monitor
urn: urn:financial-services:scenario:risk-control/liquidity-risk/funding-runoff-concentration/ilaap-behavioural-assumption-drift
intent: Agent compares actual deposit runoff rates by customer segment and product against ILAAP behavioural assumptions on a monthly basis, flagging segments where observed behaviour has deviated from the assumption used in the stress model.
Problem to solve: ILAAP behavioural assumptions for retail deposit runoff are calibrated at the annual ILAAP review. Actual retail and SME deposit behaviour during the year — driven by rate competition, customer mix changes, and digital account switching — may diverge from the calibrated assumption without the treasury risk team receiving a systematic signal.
Solution: Agent reads monthly deposit flow data by segment and product, computes actual runoff rates, and compares each segment against the current ILAAP assumption. It flags segments where the deviation exceeds the materiality threshold and delivers a monthly behavioural drift report to the treasury risk officer for ILAAP recalibration consideration.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
