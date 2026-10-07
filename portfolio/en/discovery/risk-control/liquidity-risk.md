# Liquidity risk

Liquidity risk is the risk that a bank cannot meet its payment and funding obligations as they fall due without incurring unacceptable cost. Under Basel III, the Liquidity Coverage Ratio (LCR) and Net Stable Funding Ratio (NSFR) set regulatory minima; ILAAP requires a bank to demonstrate adequate liquidity under idiosyncratic, market-wide, and combined stress scenarios. Supervisory requirements commonly provide for daily LCR reporting, monthly NSFR reporting, and quarterly ILAAP updates. **The GenAI opportunity is to instrument liquidity monitoring on a continuous basis** — replacing manual daily narrative assembly with AI-generated buffer analysis and providing a real-time runoff signal between ALCO meetings.

## Problems

### Funding adequacy & runoff {#funding-adequacy-runoff}

| Lens | Problem |
| --- | --- |
| Insights & analytics | The LCR is calculated daily and the NSFR monthly from treasury system feeds, but the management narrative — buffer adequacy, HQLA composition, drivers of day-over-day movement — is assembled manually each morning. Funding concentration signals — a large depositor account declining, broker deposit share rising above ILAAP assumptions — are identified reactively when the quarterly review highlights the movement. |
| Enablement | ILAAP stress scenario modeling — constructing the funding survival horizon under idiosyncratic and combined stress scenarios — requires the treasury risk team to assemble runoff assumptions, HQLA monetization capacity, and Contingency Funding Plan trigger calibration from multiple systems before modeling can begin. The exercise takes three to four weeks of senior analyst time per ILAAP cycle. |
| Automation | Daily LCR reports, monthly NSFR submissions, and the ILAAP liquidity section each follow defined formats with known data sources. The narrative structure is consistent across cycles; the data-intensive assembly is repeatable. |
| New business opportunities | Continuous visibility into funding runoff and HQLA buffer adequacy gives the Head of Treasury an intraday signal for wholesale funding decisions. Buffer headroom above the supervisory minimum is a deployment signal for short-duration assets; buffer tightening is an early warning to adjust the funding mix before a threshold is approached. |

## LCR & NSFR reporting {#lcr-nsfr-reporting}

The Liquidity Coverage Ratio (LCR) measures the stock of High-Quality Liquid Assets (HQLA) relative to 30-day net cash outflows under a combined stress scenario — the Basel III minimum is 100%. The Net Stable Funding Ratio (NSFR) measures the proportion of stable funding relative to required stable funding over a one-year horizon — the minimum is also 100%. The LCR is calculated daily and the NSFR monthly from treasury system feeds, with the narrative explaining drivers of movement, HQLA composition, and buffer headroom above the supervisory minimum.

### LCR/NSFR Daily Ratio Narrative

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/lcr-nsfr-reporting/lcr-nsfr-daily-ratio-narrative
- Lens: Automation
- Complexity: S
- Intent: The AI agent generates the daily LCR management narrative — ratio level, key driver movements, and regulatory threshold distance — from the overnight regulatory calculation run, and adds the NSFR commentary after each monthly NSFR calculation.
- Problem to solve: The daily LCR and the monthly NSFR are produced by the regulatory calculation engine, but the management commentary — which HQLA categories moved, which outflow buckets drove the ratio change, and how far the ratio sits from the regulatory minimum — is assembled manually each morning.
- Solution: The AI agent reads the overnight regulatory calculation output, maps ratio movements to component drivers, computes threshold distance, and produces the standard management narrative, with the NSFR commentary added monthly. The treasury risk officer reviews and releases it before the morning stand-up.
- OKR: The treasury risk officer releases the daily LCR management narrative — with ratio level, driver decomposition, and regulatory threshold distance, and the NSFR commentary after each monthly calculation — following a brief review of the AI-generated draft rather than manual morning assembly.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to generate the daily LCR management narrative on ≥200 business days per year within 6 months of go-live; all standard narrative components (ratio level, driver movements, threshold distance) produced in every run. |
| Acceptance | ≥90% of AI-generated narratives released by the treasury risk officer without material amendment; ratio driver mapping accuracy confirmed at ≥95% on monthly quality checks. |
| Cycle | Daily narrative draft available to the treasury risk officer within 30 minutes of overnight calculation run completion, versus ≥90 minutes of manual commentary assembly under the prior approach. |

### LCR Component Sensitivity Analysis

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/lcr-nsfr-reporting/lcr-sensitivity-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent models LCR sensitivity to defined outflow and HQLA scenarios — a 10% increase in unsecured wholesale outflows, a rating downgrade triggering additional collateral calls — delivering the sensitivity table to the ALCO ahead of each meeting.
- Problem to solve: ALCO discusses LCR headroom based on the current ratio without a forward-looking sensitivity view. The headroom available to absorb a specific liquidity stress — a wholesale funding withdrawal, a margin call, a collateral downgrade trigger — requires scenario analysis that is produced for ILAAP but not for routine ALCO reporting.
- Solution: The AI agent reads the current LCR components and applies a defined set of sensitivity scenarios — outflow rate increases, HQLA haircut changes, collateral trigger outflows. It computes the resulting LCR under each scenario, ranks scenarios by impact, and delivers the sensitivity table to the ALCO secretary, who includes it in the meeting pack alongside the standard LCR report.
- OKR: The ALCO discusses LCR headroom with an AI-produced sensitivity table — the LCR under defined outflow, HQLA haircut, and collateral trigger scenarios, ranked by impact — delivered alongside the standard LCR report ahead of each meeting.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's sensitivity table is produced for ≥90% of ALCO meetings within 12 months of go-live; the full defined scenario set applied to the current LCR components in every run. |
| Acceptance | ≥80% of sensitivity tables accepted by the ALCO secretary for the meeting pack without recomputation; sensitivity results referenced in the ALCO headroom discussion in ≥75% of meetings. |
| Cycle | Sensitivity table delivered to the ALCO secretary ≥2 business days before each meeting, versus scenario analysis produced only for the ILAAP under the prior approach. |

### NSFR Structural Funding Analysis

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/lcr-nsfr-reporting/nsfr-structural-funding-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes NSFR component trends — available stable funding by source and required stable funding by asset class — to identify developing structural funding mismatches before they affect the regulatory ratio.
- Problem to solve: The monthly NSFR report provides the ratio and a driver narrative. Structural trends in funding composition — a gradual shift from stable retail deposits to less stable wholesale funding, or an increase in required stable funding from longer-duration lending — build over multiple months and are not visible in the single-period ratio narrative.
- Solution: The AI agent reads 12 months of NSFR component data, decomposes available stable funding by source and required stable funding by asset class, computes component trend lines, and identifies structural mismatches developing in either the funding or asset mix. The ALCO receives the structural analysis in the quarterly ILAAP review pack and decides on any funding mix action.
- OKR: The ALCO receives a quarterly structural funding analysis — 12-month trends in available stable funding by source and required stable funding by asset class — identifying mismatches before they affect the regulatory NSFR.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's structural analysis is produced for ≥4 consecutive quarterly ILAAP review packs within 18 months of go-live; available and required stable funding decomposed by source and asset class in every run. |
| Acceptance | ≥75% of structural mismatches identified by the AI agent rated as material by the ALCO on review; ≥1 funding mix action per year initiated from an AI-identified trend. |
| Cycle | Structural analysis delivered within 5 business days of quarter-end NSFR data, surfacing multi-month funding trends that the single-period monthly ratio narrative does not show. |

## Stress & contingency funding {#stress-contingency-funding}

Liquidity stress testing models the Bank's funding survival horizon under defined stress scenarios — idiosyncratic (loss of market confidence), market-wide (systemic liquidity crunch), and combined. The Contingency Funding Plan (CFP) maps the activation sequence of emergency liquidity levers — HQLA monetization, central bank facilities, asset sales — against defined trigger conditions. Under ILAAP requirements, the CFP is typically expected to demonstrate a minimum survival horizon of 30 days under the combined stress scenario. CFP triggers are calibrated to the Bank's actual funding structure and reviewed at least annually.

### Liquidity Stress Scenario Narrative

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/stress-contingency-funding/liquidity-stress-scenario-narrative
- Lens: Enablement
- Complexity: M
- Intent: The AI agent constructs the ILAAP liquidity stress narrative — survival horizon by scenario, HQLA monetization capacity, and CFP trigger mapping — from current treasury and deposit position data.
- Problem to solve: Each ILAAP cycle requires the treasury risk team to assemble the liquidity stress narrative through manual modeling and drafting. The exercise covers survival horizon by scenario, runoff assumptions, HQLA monetization sequence, and CFP trigger calibration, consuming several weeks of senior analyst effort.
- Solution: The AI agent reads current deposit positions, HQLA composition, wholesale funding maturity profile, and prior ILAAP runoff assumptions. It models survival horizon under each stress scenario, maps CFP trigger points, and drafts the liquidity stress narrative. The treasury risk team reviews assumptions and adds forward judgment before regulatory submission.
- OKR: The treasury risk team reviews assumptions and adds forward judgment to an AI-constructed ILAAP liquidity stress narrative — covering survival horizon, HQLA monetization capacity, and CFP trigger mapping — modeled from current position data.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to construct the liquidity stress narrative for ≥1 ILAAP submission cycle within 18 months of go-live; all prescribed components (survival horizon by scenario, runoff assumptions, HQLA sequence, CFP triggers) produced by the AI agent from go-live. |
| Acceptance | ≥80% of AI-constructed narrative sections accepted by the treasury risk team without structural revision; supervisory feedback items on liquidity stress narrative quality reduced by ≥30% versus prior submission. |
| Cycle | Liquidity stress narrative draft delivered within 5 business days of current position data cut, reducing the overall ILAAP liquidity section cycle from ≥4 weeks of senior analyst effort. |

### CFP Trigger Monitoring

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/stress-contingency-funding/cfp-trigger-monitoring
- Lens: Automation
- Complexity: M
- Intent: The AI agent monitors the Bank's defined CFP trigger indicators daily — credit rating signals, wholesale funding access metrics, deposit outflow rates, and market confidence proxies — and alerts the CRO and Head of Treasury when a trigger threshold is approached.
- Problem to solve: CFP trigger indicators are defined in the ILAAP and reviewed in the quarterly ILAAP update. Monitoring the indicators against the trigger levels between ILAAP cycles requires treasury risk staff to check multiple data sources; there is no automated alert when a trigger indicator approaches its threshold.
- Solution: The AI agent reads the CFP trigger indicator schedule, monitors each indicator on a daily basis from the relevant system feeds, and delivers an automated alert to the CRO and Head of Treasury when any indicator is within 20% of its trigger threshold. The Head of Treasury assesses the alert and decides whether to initiate the CFP pre-activation protocol.
- OKR: The CRO and Head of Treasury are alerted when any Contingency Funding Plan trigger indicator comes within 20% of its threshold, from daily monitoring by the AI agent rather than manual checks of multiple data sources between ILAAP cycles.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent monitors 100% of the CFP trigger indicator schedule daily within 3 months of go-live; monitoring run on ≥200 business days per year once live. |
| Acceptance | ≥85% of the AI agent's alerts confirmed by the Head of Treasury as accurate against the trigger indicator schedule; ≤10% false-positive rate on trigger alerts measured over rolling 90-day windows. |
| Cycle | Alert delivered to the CRO and Head of Treasury on the same business day an indicator comes within 20% of its trigger threshold, versus identification at the quarterly ILAAP update under the prior approach. |

### Survival Horizon Scenario Refresh

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/stress-contingency-funding/survival-horizon-scenario-refresh
- Lens: Insights
- Complexity: M
- Intent: The AI agent refreshes the ILAAP survival horizon estimate quarterly using current deposit, HQLA, and wholesale funding data, giving the ALCO a current-position survival estimate rather than the prior ILAAP submission figure.
- Problem to solve: The survival horizon estimate presented to the ALCO reflects the ILAAP submission, which may be six to twelve months old. The current survival horizon under each stress scenario changes with the balance sheet composition; management is making liquidity risk decisions against a stale estimate.
- Solution: The AI agent reads current deposit balances by behavioral segment, HQLA composition, and wholesale funding maturity profile. It applies the ILAAP stress scenario runoff and outflow assumptions to the current position and computes the updated survival horizon under idiosyncratic, market-wide, and combined scenarios. The ALCO receives the refreshed estimate at each quarterly meeting alongside the prior ILAAP submission figure.
- OKR: The ALCO takes liquidity risk decisions against a survival horizon refreshed each quarter from current deposit, HQLA, and wholesale funding data — under idiosyncratic, market-wide, and combined scenarios — presented alongside the prior ILAAP submission figure.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's survival horizon refresh is produced for ≥4 consecutive quarterly ALCO meetings within 18 months of go-live; ILAAP runoff and outflow assumptions applied to the current position under all three stress scenarios in every run. |
| Acceptance | ≥85% of refreshed estimates accepted by the ALCO without recomputation by the treasury risk team; the refreshed survival horizon cited in ALCO liquidity decisions in ≥3 of 4 quarterly meetings. |
| Cycle | Refreshed estimate delivered within 5 business days of quarter-end position data, versus an ILAAP submission figure six to twelve months old under the prior approach. |

## Intraday liquidity monitoring {#intraday-liquidity-monitoring}

Intraday liquidity is a bank's capacity to meet payment and settlement obligations throughout the business day — across RTGS, correspondent banking, and securities settlement systems. In line with BCBS 248, banks monitor peak intraday liquidity usage, available intraday liquidity facilities, and the timing of significant payment outflows. Intraday liquidity stress — where a large counterparty fails to deliver expected inflows — can create settlement delays that cascade through the payment system. Monitoring intraday liquidity positions requires real-time feeds from payment and settlement systems.

### Settlement Counterparty Behavior Monitor

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/intraday-liquidity-monitoring/settlement-counterparty-behaviour-monitor
- Lens: Automation
- Complexity: S
- Intent: The AI agent monitors intraday payment timing from the Bank's material settlement counterparties, flags counterparties whose inflow timing has shifted relative to historical patterns, and alerts treasury operations to potential settlement stress.
- Problem to solve: Settlement stress typically manifests as a counterparty that normally delivers funds by 11:00 failing to deliver, creating a liquidity gap that treasury operations must manage. Monitoring typically requires treasury operations staff to check counterparty inflow status manually during the business day rather than receiving an automated alert when the timing deviation exceeds the threshold.
- Solution: The AI agent reads real-time payment system data, tracks inflow timing per material counterparty against their rolling 20-day median timing, and delivers an alert to treasury operations when a counterparty's expected inflow is delayed beyond the defined threshold. The treasury operations team initiates the contingency protocol before the intraday position deteriorates.
- OKR: Treasury operations is alerted when a material settlement counterparty's expected inflow is delayed beyond its historical timing pattern, and initiates the contingency protocol before the intraday position deteriorates.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent tracks inflow timing for 100% of material settlement counterparties against their rolling 20-day median within 3 months of go-live; monitoring active on ≥200 business days per year once live. |
| Acceptance | ≥85% of the AI agent's delay alerts confirmed by treasury operations as genuine timing deviations; ≤10% false-positive rate on counterparty alerts measured over rolling 90-day windows. |
| Cycle | Alert delivered to treasury operations within 5 minutes of a counterparty's inflow passing the delay threshold, versus identification only when staff check inflow status manually during the business day. |

### Intraday Liquidity Position Watch

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/intraday-liquidity-monitoring/intraday-liquidity-position-watch
- Lens: Insights
- Complexity: M
- Intent: The AI agent monitors intraday payment flows and liquidity usage continuously, flagging settlement pressure and peak intraday usage events for the Head of Treasury.
- Problem to solve: Intraday liquidity monitoring requires treasury operations staff to track payment flows, correspondent bank positions, and RTGS usage throughout the business day from multiple system screens. Settlement pressure events — large counterparty inflow delays, unexpected outflow spikes — are identified when a team member checks the system rather than by an automated alert.
- Solution: The AI agent reads real-time payment system feeds, correspondent account positions, and RTGS capacity utilization. It monitors peak intraday usage relative to available facilities, flags counterparty inflow delays above threshold, and delivers a structured morning position report with intraday event alerts to the Head of Treasury, who manages the intraday position from them.
- OKR: The Head of Treasury manages intraday liquidity from a structured morning position report and continuous intraday event alerts generated by the AI agent's monitoring of payment flows, correspondent positions, and RTGS capacity.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's intraday liquidity monitoring runs continuously on ≥200 business days per year within 6 months of go-live; morning position report delivered to the Head of Treasury before the daily open for ≥200 business days per year. |
| Acceptance | ≥85% of AI-generated settlement pressure alerts rated as accurate by the Head of Treasury; ≤10% false-positive rate on intraday event alerts measured over rolling 90-day windows. |
| Cycle | Intraday event alert delivered within 5 minutes of threshold breach, versus identification latency of ≥15 minutes under the prior manual monitoring approach. |

### Intraday Peak Usage Trend Analysis

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/intraday-liquidity-monitoring/intraday-peak-usage-trend-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes rolling 90-day intraday liquidity usage data to identify the trend in peak usage relative to available facilities, seasonal patterns, and counterparty-specific inflow timing shifts, for the BCBS 248 intraday reporting and the ALCO liquidity review.
- Problem to solve: Under BCBS 248, banks monitor and report intraday peak usage trends. Trend analysis across the 90-day reporting window requires aggregating daily peak usage records, computing percentile distributions, and identifying shifts in usage patterns — a manual analysis exercise not routinely performed outside the quarterly BCBS 248 reporting cycle.
- Solution: The AI agent reads 90 days of intraday usage records, computes peak usage trends and percentile distributions, identifies seasonal patterns and counterparty-specific inflow timing shifts, and produces the BCBS 248 intraday liquidity report. The Head of Treasury reviews and submits it.
- OKR: The Head of Treasury reviews and submits the BCBS 248 intraday liquidity report from an AI-produced analysis of rolling 90-day usage — peak usage trends, percentile distributions, seasonal patterns, and counterparty inflow timing shifts — which also informs the ALCO liquidity review.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to produce the intraday usage trend analysis for ≥4 consecutive quarterly reporting cycles within 18 months of go-live; 90 days of daily peak usage records analyzed in every run. |
| Acceptance | ≥85% of AI-produced reports submitted by the Head of Treasury without material amendment; usage pattern shifts identified by the AI agent rated as material by the ALCO in ≥70% of cases. |
| Cycle | Report draft delivered within 3 business days of the close of the 90-day reporting window, versus ≥1 week of manual aggregation in each quarterly reporting cycle under the prior approach. |

## Funding runoff & concentration {#funding-runoff-concentration}

Funding runoff risk is the risk that liability providers — retail depositors, wholesale funders, institutional counterparties — withdraw funding faster than a bank can replace it under stress conditions. Concentration in the funding base amplifies runoff risk: a small number of large depositors or a concentrated wholesale funding maturity cliff can produce correlated outflows that HQLA cannot absorb. ILAAP behavioral assumptions calibrate retail deposit runoff rates; wholesale funding concentration triggers enhanced monitoring under liquidity-risk requirements.

### Wholesale Funding Maturity Cliff Watch

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/funding-runoff-concentration/wholesale-funding-maturity-cliff-watch
- Lens: Automation
- Complexity: S
- Intent: The AI agent reads the wholesale funding maturity ladder daily, identifies upcoming maturity concentrations within the 30-day LCR stress window and 90-day horizon, and delivers an early-warning alert to the Head of Treasury.
- Problem to solve: Wholesale funding maturity concentrations are visible in the LCR maturity ladder but are not monitored on a rolling forward-looking basis outside the daily LCR calculation. A material maturity cliff forming within a 30-day window may be visible in the data weeks before it occurs but goes unalerted until the daily LCR report surfaces it.
- Solution: The AI agent reads the wholesale funding maturity ladder, computes net maturity flow by day and week over the rolling 90-day horizon, and flags concentration points where gross maturities exceed the defined threshold relative to available refinancing capacity. The Head of Treasury receives the alert at least three weeks before the concentration date, with time to arrange refinancing.
- OKR: The Head of Treasury receives an early-warning alert for every wholesale funding maturity concentration forming within the rolling 90-day horizon, with time to arrange refinancing before it enters the 30-day LCR stress window.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent reads the wholesale funding maturity ladder daily on ≥200 business days per year within 3 months of go-live; net maturity flow computed by day and week over the rolling 90-day horizon in every run. |
| Acceptance | ≥85% of AI-flagged concentration points confirmed as material by the Head of Treasury; no maturity concentration above the defined threshold first identified through the daily LCR report. |
| Cycle | Alert delivered to the Head of Treasury at least three weeks before the concentration date, versus surfacing in the daily LCR report once the maturity is already inside the 30-day window. |

### Funding Runoff & Concentration Watch

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/funding-runoff-concentration/funding-runoff-concentration-watch
- Lens: Insights
- Complexity: M
- Intent: The AI agent monitors daily deposit flows for runoff signals and funding concentration patterns, flagging deviations from ILAAP behavioral assumptions for the CRO and ALCO.
- Problem to solve: Funding concentration risk accumulates between quarterly ILAAP reviews. Large depositor account movements, wholesale funding share increases, and retail behavioral runoff deviations from ILAAP assumptions are identified when the quarterly review surfaces the movement rather than as signals develop.
- Solution: The AI agent monitors daily deposit flows by counterparty, channel, and product type against ILAAP behavioral assumptions. It surfaces concentration signals and runoff deviations, delivering a weekly funding-risk digest to the ALCO secretary and CRO.
- OKR: The ALCO and CRO receive a weekly funding-risk digest with AI-identified deposit runoff deviations and funding concentration signals referenced to ILAAP behavioral assumptions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent monitors daily deposit flows against ILAAP behavioral assumptions within 3 months of go-live; weekly digest delivered to the ALCO secretary and CRO for ≥45 consecutive weeks in year 1. |
| Acceptance | ≥75% of AI-flagged runoff deviations and concentration signals rated as material by the ALCO on review; ≤10% false-positive rate on weekly flags measured over rolling 90-day windows. |
| Cycle | Weekly funding-risk digest delivered within 1 business day of each monitoring cycle close, versus a quarterly identification cadence under the prior ILAAP review approach. |

### ILAAP Behavioral Assumption Drift Monitor

- URN: urn:financial-services:scenario:risk-control/liquidity-risk/funding-runoff-concentration/ilaap-behavioural-assumption-drift
- Lens: Insights
- Complexity: M
- Intent: The AI agent compares actual deposit runoff rates by customer segment and product against ILAAP behavioral assumptions on a monthly basis, flagging segments where observed behavior has deviated from the assumption used in the stress model.
- Problem to solve: ILAAP behavioral assumptions for retail deposit runoff are calibrated at the annual ILAAP review. Actual retail and SME deposit behavior during the year — driven by rate competition, customer mix changes, and digital account switching — may diverge from the calibrated assumption without the treasury risk team receiving a systematic signal.
- Solution: The AI agent reads monthly deposit flow data by segment and product, computes actual runoff rates, and compares each segment against the current ILAAP assumption. It flags segments where the deviation exceeds the materiality threshold and delivers a monthly behavioral drift report to the treasury risk officer for ILAAP recalibration consideration.
- OKR: The treasury risk officer receives a monthly behavioral drift report comparing actual deposit runoff by customer segment and product with the ILAAP assumption, so recalibration is considered when behavior diverges rather than at the next annual review.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's drift comparison runs on monthly deposit flow data for 100% of segments and products within 6 months of go-live; monthly report delivered to the treasury risk officer for ≥10 consecutive months in year 1. |
| Acceptance | ≥75% of segments flagged above the materiality threshold confirmed by the treasury risk officer as genuine deviations; ≥1 ILAAP behavioral assumption recalibrated per year from an AI-flagged deviation. |
| Cycle | Monthly drift report delivered within 3 business days of month-end deposit data, versus assumptions reviewed only at the annual ILAAP calibration under the prior approach. |
