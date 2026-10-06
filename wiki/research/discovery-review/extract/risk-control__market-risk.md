# 

source: html-alt/financial-services/en/risk-control/market-risk/index.html


[PAGE TEXT]
VaR & expected shortfall
Value-at-Risk (VaR) and Expected Shortfall (ES) are the primary statistical measures of potential market loss at a given confidence level and horizon. Under Basel III IMA, regulated banks compute daily 99th-percentile VaR and 97.5th-percentile ES across the trading book; backtesting against actual P&L is a regulatory requirement with defined exception thresholds. VaR by risk factor and desk provides the granular view used in limit monitoring; aggregate ES provides the board-level capital adequacy signal.
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|M] VaR & Expected Shortfall Narrative
urn: urn:financial-services:scenario:risk-control/market-risk/var-expected-shortfall/var-expected-shortfall-narrative
intent: Agent drafts the daily VaR and expected shortfall commentary — decomposing drivers by desk, risk factor, and portfolio — for the Market Risk Committee pack.
Problem to solve: Daily VaR and ES figures are produced by the risk engine, but the driver commentary — which desks, risk factors, or position changes drove the move — is assembled manually. The commentary step adds analyst hours to a same-day reporting cycle under which timeliness is a supervisory expectation.
Solution: Agent reads the risk engine decomposition, maps VaR and ES movements to desk contributions and factor sensitivities, and drafts the narrative commentary in the committee's standard format. The market risk analyst reviews, adds judgement on unusual patterns, and releases the pack.
OKR objective: The market risk analyst reviews and releases the daily VaR and expected shortfall commentary — decomposing movements by desk, risk factor, and portfolio in the committee's standard format — drafted by the agent from the risk engine decomposition.
OKR KR [Adoption]: Agent used to draft daily VaR and ES narrative commentary on ≥200 business days per year within 6 months of go-live; desk contribution and factor sensitivity decomposition included in every draft from go-live.
OKR KR [Acceptance]: ≥90% of agent-drafted commentaries released by the market risk analyst with only minor additions before committee distribution; driver attribution accuracy confirmed at ≥95% on monthly quality checks.
OKR KR [Cycle]: Daily VaR and ES commentary draft available within 30 minutes of risk engine output publication, versus ≥90 minutes of manual assembly under the prior approach.

### CARD 2 [Automation|M] VaR Model Backtesting Pack
urn: urn:financial-services:scenario:risk-control/market-risk/var-expected-shortfall/var-model-backtesting-pack
intent: Agent maintains the rolling 250-day backtesting record, generates the monthly backtesting report in Basel III traffic-light format, and drafts any required supervisory notification when the exception threshold is crossed.
Problem to solve: The Basel III backtesting framework requires a rolling 250-day actual P&L vs VaR comparison maintained in a format that identifies the traffic-light zone and supports immediate supervisory notification. The monthly backtesting report is assembled manually from the daily comparison records; supervisory notification drafts are prepared from scratch when exception counts breach the threshold.
Solution: Agent maintains the rolling daily P&L vs VaR comparison, computes the exception count in the 250-day window, applies the traffic-light classification, generates the monthly report, and drafts the supervisory notification where the amber or red threshold is crossed. The Market Risk Officer reviews and submits.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Enablement|M] Stressed VaR Scenario Narrative
urn: urn:financial-services:scenario:risk-control/market-risk/var-expected-shortfall/stressed-var-scenario-narrative
intent: Agent drafts the stressed VaR scenario selection rationale and comparative narrative — justifying the chosen stress period, comparing stressed VaR to current VaR by risk factor, and mapping capital implications — for the Market Risk Committee quarterly pack.
Problem to solve: Stressed VaR requires selecting a one-year stress period relevant to the bank's current portfolio. Justifying the stress period selection, comparing the stressed and current VaR by risk factor, and explaining capital implications requires a narrative that is drafted manually each quarter, consuming the market risk team's time before the committee pack is finalised.
Solution: Agent reads the current portfolio risk-factor profile, historical stress period performance data, and prior stressed VaR narratives. It evaluates the stress period's relevance to the current portfolio and drafts the selection rationale and comparative narrative in the committee's standard format. The market risk team reviews and approves before submission.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
P&L attribution & backtesting
P&L attribution explains the daily profit or loss of each trading desk in terms of changes in underlying risk factors — decomposing performance into rate, FX, spread, and volatility drivers. Backtesting compares actual P&L against the VaR estimate to test model accuracy; under Basel III IMA, five or more exceptions in 250 trading days trigger a regulatory capital add-on and supervisory review (the 'traffic light' framework). Both attribution and backtesting documentation are regulatory requirements and must be produced daily. Reconciling attributed P&L to the official finance P&L adds a further data-quality step to each cycle.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] Backtesting Exception Documentation Pack
urn: urn:financial-services:scenario:risk-control/market-risk/pl-attribution-backtesting/backtesting-exception-pack
intent: Agent generates the regulatory backtesting exception documentation when actual P&L exceeds the VaR estimate, pre-populating the root-cause template and Basel III traffic-light status for the Market Risk Committee and supervisor.
Problem to solve: Each VaR backtesting exception requires a documented root-cause analysis filed with the Market Risk Committee and, where the exception count triggers the Basel III traffic-light threshold, with the supervisor. Assembling the documentation — exception count in the rolling 250-day window, root-cause classification, and supervisor notification draft — is performed manually after the exception is identified.
Solution: Agent detects exceptions from the daily P&L vs VaR comparison, updates the rolling 250-day exception counter, classifies the root cause from the P&L attribution data, and generates the exception documentation pack including supervisor notification draft if the traffic-light threshold is crossed. The Market Risk Officer reviews and files.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Automation|M] P&L Attribution Daily Narrative
urn: urn:financial-services:scenario:risk-control/market-risk/pl-attribution-backtesting/pl-attribution-daily-narrative
intent: Agent generates the daily P&L attribution narrative — decomposing desk P&L into rate, FX, spread, and volatility drivers — and reconciles attributed P&L to the official finance P&L for the Market Risk Committee.
Problem to solve: Daily P&L attribution requires the market risk team to decompose desk performance into risk-factor contributions and reconcile to the official finance P&L. Both steps are performed manually; the reconciliation adds an additional data-quality check before the committee pack can be finalised.
Solution: Agent reads the risk system factor sensitivities and daily market data moves, computes risk-factor P&L attributions by desk, maps to the official finance P&L, and flags reconciliation breaks above threshold. The market risk analyst reviews breaks and releases the narrative for the committee pack.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Insights|M] P&L Attribution Pattern Analysis
urn: urn:financial-services:scenario:risk-control/market-risk/pl-attribution-backtesting/pl-attribution-pattern-analysis
intent: Agent analyses rolling 90-day P&L attribution patterns to identify systematic model misspecification — risk factors consistently over- or under-attributed — and delivers a quarterly signal to the market risk model validation team.
Problem to solve: Daily P&L attribution is reviewed for the current day but not analysed for systematic patterns across the quarter. Recurring attribution misses — a specific risk factor consistently under-attributed on one desk — indicate model misspecification that should trigger validation review but are not visible without time-series aggregation.
Solution: Agent reads 90 days of P&L attribution records, computes residual attribution error by risk factor and desk, identifies factors with systematic directional bias, and delivers a quarterly signal report to the market risk validation function for investigation.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Sensitivity & Greeks monitoring
Sensitivity analysis quantifies the change in portfolio value for a unit movement in a risk factor — interest rate delta, FX gamma, equity vega — enabling the market risk team to monitor the portfolio's directional and convexity exposure to each factor. Greeks monitoring for options-containing books tracks delta, gamma, vega, theta, and rho at desk and aggregate level. Limit frameworks for sensitivities are set alongside VaR limits; a sensitivity near-breach in a specific factor signals concentrated risk-factor exposure before it translates into a VaR breach.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] Greeks Daily Position Report
urn: urn:financial-services:scenario:risk-control/market-risk/sensitivity-greeks-monitoring/greeks-daily-position-report
intent: Agent compiles the daily Greeks and sensitivity position report — delta, gamma, vega, theta, rho by desk and risk factor — against defined sensitivity limits for the Market Risk Committee morning pack.
Problem to solve: Options-containing desks require daily reporting of delta, gamma, vega, theta, and rho positions relative to sensitivity limits. Compiling these from the risk system into the committee's standard tabular format and flagging near-limit positions is performed manually each morning, adding a production step to a same-day reporting cycle.
Solution: Agent reads the overnight Greeks output from the risk system, applies the limit framework per desk and risk factor, computes utilisation percentages, and generates the daily sensitivity report with near-limit flags. The market risk analyst reviews the output before the morning pack is distributed.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Automation|S] Sensitivity Limit Breach Escalation Pack
urn: urn:financial-services:scenario:risk-control/market-risk/sensitivity-greeks-monitoring/sensitivity-limit-breach-escalation
intent: Agent generates the escalation pack when a desk crosses a sensitivity limit — pulling the position detail, breach history, and a pre-drafted trader notification — within the escalation window required by the limits policy.
Problem to solve: A sensitivity limit breach triggers an escalation sequence: the desk head is notified, the Market Risk Officer documents the breach, and a management action is agreed. Assembling the escalation documentation — position detail, limit comparison, breach history, and notification draft — delays the start of the escalation window.
Solution: Agent detects the breach from the daily position report, retrieves the desk position detail, breach count in the rolling period, and prior breach documentation, and generates the escalation pack including the trader notification draft. The Market Risk Officer reviews and sends within the policy window.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Insights|M] Sensitivity Risk-Factor Concentration Analysis
urn: urn:financial-services:scenario:risk-control/market-risk/sensitivity-greeks-monitoring/sensitivity-risk-factor-concentration
intent: Agent analyses aggregate sensitivity positions across all desks to identify concentrated risk-factor exposures — where multiple desks hold correlated directional positions — for the CRO's weekly risk review.
Problem to solve: Desk-level sensitivity limits control individual desk exposures, but correlated directional positions across multiple desks in the same risk factor — interest rate delta concentrated in rates and credit desks simultaneously — represent an aggregate exposure that desk-level monitoring does not capture.
Solution: Agent reads all desk sensitivity positions, aggregates by risk factor, computes directional correlation across desks, and identifies risk factors where aggregate exposure across multiple desks warrants the CRO's attention beyond individual desk limit status. The CRO receives a weekly risk-factor concentration view alongside the standard desk-level report.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Market risk limits utilization
The market risk limits framework sets position constraints at desk, product, and aggregate trading-book level — covering VaR, sensitivity, stop-loss, and concentration limits. Monitoring compliance with the limits framework is a daily obligation; breaches must be escalated within defined timeframes and reported to supervisors. Limit utilization reporting for the Market Risk Committee is typically produced weekly, with breaches and near-misses documented separately. Under BCBS 239 risk data aggregation standards, the bank must be able to produce consolidated limit utilization data across the trading book on demand.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|M] Market Risk Limits Utilization Report
urn: urn:financial-services:scenario:risk-control/market-risk/market-risk-limits-utilization/market-risk-limits-utilization-report
intent: Agent compiles the weekly market risk limits utilization report across all desks and limit types, highlighting near-breaches and breach documentation for the Market Risk Committee.
Problem to solve: The weekly limits utilization report spans VaR, sensitivity, stop-loss, and concentration limits across all desks. Assembling utilization percentages, flagging near-limit positions, and documenting actual breaches with escalation history consumes analyst time before the committee pack is ready.
Solution: Agent reads daily limit utilization feeds across all limit types and desks, computes weekly utilization summaries, flags near-limit positions above the committee threshold, and generates breach documentation where applicable. The Market Risk Committee receives the assembled pack the day before the meeting.
OKR objective: The Market Risk Committee receives the weekly limits utilization report — spanning VaR, sensitivity, stop-loss, and concentration limits across all desks — assembled by the agent with near-breach flags and breach documentation current as of the day before the meeting.
OKR KR [Adoption]: Agent used to compile the weekly market risk limits utilization report for ≥48 consecutive weeks within 12 months of go-live; all limit types (VaR, sensitivity, stop-loss, concentration) covered across all desks from go-live.
OKR KR [Acceptance]: ≥90% of agent-compiled reports accepted by the Market Risk Committee secretary without manual supplementation; breach documentation completeness confirmed at ≥95% of confirmed breach events on quarterly quality review.
OKR KR [Cycle]: Full limits utilization pack available to the committee secretary by close of business the day before the weekly meeting, versus same-day manual assembly that compressed committee review time.

### CARD 11 [Insights|M] Market Risk Limit Breach Pattern Analysis
urn: urn:financial-services:scenario:risk-control/market-risk/market-risk-limits-utilization/market-risk-limit-breach-pattern-analysis
intent: Agent analyses rolling 12-month limit breach history by desk, limit type, and market condition, identifying structural limit calibration issues and presenting a signal to the Market Risk Committee for limit review.
Problem to solve: Individual limit breaches are documented and escalated per event. Patterns in breach history — a specific desk breaching the same limit type under a defined market condition, or repeated near-breaches that suggest a limit set below normal operating requirements — require time-series analysis not produced routinely by the weekly utilisation report.
Solution: Agent reads 12 months of limit utilisation and breach records, computes breach frequency and near-breach distribution by desk and limit type, cross-references against market conditions at the time of each breach, and identifies structural patterns. The Market Risk Committee receives the quarterly breach pattern analysis alongside the standard utilisation report.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Enablement|M] Limits Framework Calibration Review Support
urn: urn:financial-services:scenario:risk-control/market-risk/market-risk-limits-utilization/limits-framework-calibration-review
intent: Agent analyses the relationship between current limits and the bank's risk appetite, comparing utilisation distributions and capital consumption to identify limits that appear miscalibrated relative to the bank's capital allocation and strategy, as input for the annual limits review.
Problem to solve: The annual limits review is informed by the prior year's utilisation experience but does not systematically compare limits against capital allocation or business strategy. Limits set in a prior year's market environment may be too restrictive or too permissive relative to the current strategy and capital position.
Solution: Agent reads the full year's limit utilisation distributions by desk and limit type, the current capital allocation by desk, and the annual business plan. It identifies limits with very low median utilisation relative to risk appetite capacity and limits where frequent near-breaches suggest under-calibration, and assembles the analysis document for the annual limits review.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
