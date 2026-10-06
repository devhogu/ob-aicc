# 

source: html-alt/financial-services/en/finance-treasury/liquidity-management/index.html


[PAGE TEXT]
Daily LCR & NSFR monitoring
Daily LCR and NSFR ratio compliance is the Treasurer's primary regulatory obligation — maintained against NBKR, NBK/ARDFM, and CBR minima and internal management thresholds. The daily report covers ratio levels, HQLA composition, inflow and outflow drivers, and the overnight movement attribution that the Treasurer reviews before markets open.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] Daily LCR / NSFR Monitoring & Commentary
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/daily-lcr-nsfr/daily-lcr-nsfr-monitoring
intent: Agent generates the daily LCR and NSFR commentary for the Treasurer — ratio movement attribution, HQLA composition note, regulatory buffer position, and ALCO-format narrative — from overnight system feeds.
Problem to solve: The daily liquidity report covering LCR, NSFR, HQLA composition, and overnight ratio movement is assembled by treasury operations from multiple systems each morning. The assembly and drafting cycle delays the Treasurer's decision window on the day's funding and investment actions.
Solution: Agent reads overnight LCR and NSFR data feeds, attributes ratio movements to inflow, outflow, and HQLA changes, and generates the daily report and accompanying ALCO-format narrative in the Treasurer's house structure. HQLA classification against LCR and NSFR regulatory eligibility rules is applied automatically to surface rebalancing requirements; the report is available at system open.
OKR objective: The daily LCR and NSFR report — covering ratio movement attribution, HQLA composition, regulatory buffer position, and ALCO-format narrative — is available to the Treasurer at system open each business day from overnight feeds.
OKR KR [Adoption]: Agent-produced daily liquidity report delivered at system open for ≥220 trading days in year 1; ALCO-format narrative included in every daily output.
OKR KR [Acceptance]: ≥90% of daily reports accepted by the Treasurer as accurate without requiring manual restatement; ratio figures reconcile to the formal monthly liquidity report in ≥98% of checked periods.
OKR KR [Cycle]: Daily liquidity report available at system open vs. 1–2 hours post-open in the prior manual assembly process.

### CARD 2 [Insights|S] LCR & NSFR Driver Trend Analysis
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/daily-lcr-nsfr/lcr-nsfr-driver-trend-analysis
intent: Agent analyses the rolling twenty-trading-day history of LCR and NSFR movements to identify structural trends in inflow, outflow, and HQLA components — distinguishing seasonal patterns from persistent deterioration before the trend breaches a management threshold.
Problem to solve: The daily liquidity report covers the overnight movement but does not contextualise it against the rolling trend. Persistent intra-month deterioration in a specific outflow category — such as retail deposit run-off or corporate line drawdowns — is visible in the daily report only as a sequence of individual movements that the Treasurer must manually aggregate to identify the structural direction.
Solution: Agent maintains a rolling twenty-trading-day history of each LCR and NSFR component. It applies a trend decomposition to distinguish seasonal from structural movements and surfaces any component where the twenty-day direction shows persistent deterioration against the prior equivalent period. The trend analysis is appended to the daily report as a supplementary section each morning and shared with the Treasurer and ALCO liquidity desk. Threshold-crossing trends trigger a proactive alert before the monthly ALCO cycle.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Optimize|S] LCR Buffer Optimisation Signal
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/daily-lcr-nsfr/lcr-buffer-optimisation-signal
intent: Agent analyses the HQLA portfolio composition and the current LCR calculation to identify Level 1 and Level 2 rebalancing opportunities that maintain the regulatory ratio while improving portfolio yield within NBKR, NBK/ARDFM, or CBR eligibility constraints.
Problem to solve: The HQLA portfolio is managed to maintain LCR compliance, but the composition between Level 1 central bank reserves, Level 1 government securities, and Level 2 assets is not systematically optimised for yield within the regulatory framework. Over-allocation to central bank reserves above the minimum required buffer suppresses yield without adding regulatory benefit; the analysis to identify rebalancing opportunities requires a manual cross-reference of the current HQLA composition against the LCR calculation.
Solution: Agent reads the current HQLA portfolio composition, the daily LCR calculation inputs, and the regulatory eligibility and haircut schedule for the relevant jurisdiction. It computes the minimum required Level 1 balance for the current outflow base, identifies excess central bank reserves above that minimum, and presents a rebalancing signal — volume of excess reserves, eligible government securities that could replace them within Level 1, and the estimated yield pickup. The Treasurer reviews the signal and makes the reinvestment decision; the agent updates the analysis each day the excess persists.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Contingency Funding Plan (CFP)
The Contingency Funding Plan is the bank's documented playbook for managing liquidity under stress — sequencing the contingent actions available to the Treasurer from HQLA disposal through emergency borrowing facilities, with estimated execution timelines and liquidity values per action. NBKR, NBK/ARDFM, and CBR require the CFP to be maintained, stress-tested, and available for supervisory review.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] CFP Annual Review Narrative
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/contingency-funding-plan/cfp-annual-review-narrative
intent: Agent drafts the annual CFP review narrative for NBKR, NBK/ARDFM, or CBR — covering changes to the action register, revised stress outflow estimates, test exercise results, and governance attestation — from current Treasury data and the prior submission as a style anchor.
Problem to solve: The annual CFP review narrative is a regulatory-required document prepared by Treasury with CFO and CRO sign-off. Drafting draws on test exercise results, the current action register, and the prior submission for structural consistency. The process takes one to two weeks of Treasury time and is treated as a standalone drafting exercise each year without reuse of prior-year structure.
Solution: Agent reads the current CFP action register with any changes from the prior year, the results of the most recent CFP test exercise, the current stress outflow estimates, and the prior-year approved CFP narrative as a style anchor. It generates a full draft covering the prescribed sections — governance, action register, stress estimates, test results, and attestation — and flags each change from the prior submission for explicit disclosure. Treasury reviews and edits; the agent handles the drafting cycle and version control.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Enablement|M] Contingency Funding Plan Stress Analysis
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/contingency-funding-plan/cfp-stress-analysis
intent: Agent runs liquidity stress scenarios against current position data and produces the CFP narrative — survival horizon, trigger conditions, and contingent action inventory — for ALCO and regulatory review.
Problem to solve: Stress-scenario liquidity analysis for the Contingency Funding Plan is produced quarterly — and ad hoc after a market event — by cross-referencing the stress model, HQLA inventory, funding concentration data, and the documented contingent action list. Each production run is manual and the output is current only at point-in-time.
Solution: Agent reads the liquidity stress model, current HQLA inventory, funding maturity profile, and contingent action list. It runs the prescribed stress scenarios, computes survival horizons per scenario, identifies assumptions that drive the most adverse outcomes, and generates the CFP narrative sections. ALCO reviews the generated analysis before approving the submission; the agent is re-run on demand following a material market event.
OKR objective: The Contingency Funding Plan stress analysis — survival horizon, trigger conditions, and contingent action inventory — is produced from current position data for each prescribed scenario and available for ALCO and regulatory review on demand, including after material market events.
OKR KR [Adoption]: Agent-produced CFP stress analysis used for ≥4 scheduled quarterly reviews and all ad hoc requests triggered by material market events within year 1.
OKR KR [Acceptance]: ≥85% of CFP stress narratives approved by the Treasurer without material amendment to the survival horizon calculation; scenario outputs reconcile to the liquidity stress model within ±2% on periodic validation.
OKR KR [Cycle]: CFP narrative available for ALCO review within 2 business days of a stress run trigger, vs. 1–2 weeks of manual assembly in the prior process.

### CARD 6 [Insights|M] CFP Stress Action Sequencing
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/contingency-funding-plan/cfp-stress-action-sequencing
intent: Agent models the execution sequence and cumulative liquidity value of CFP contingent actions under each stress scenario — HQLA disposal, repo facility drawdown, emergency central bank borrowing — and identifies the minimum action set required to cover projected outflows within each stress horizon.
Problem to solve: The CFP lists contingent actions with estimated liquidity values and execution timelines, but does not model the optimal sequencing of those actions under specific stress scenarios. ALCO and the Treasurer assess the adequacy of the CFP at annual review against a static stress outflow estimate, without a dynamic view of which action sequences are executable under market stress conditions.
Solution: Agent reads the CFP action register with estimated liquidity values and execution timelines, and the stress scenario outflow projections by day from the current ILAAP. It models the execution sequence for each stress scenario, applying haircuts and timeline constraints to each action, and computes the cumulative liquidity coverage at each day of the stress horizon. Minimum action sets that cover projected outflows are identified for each scenario. ALCO reviews the sequencing analysis at the annual CFP stress test review.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
HQLA portfolio & investment management
The HQLA portfolio holds the securities and central bank reserves that constitute the bank's liquid asset buffer under LCR and NSFR. Portfolio composition — between Level 1 assets (central bank reserves, government securities) and Level 2 assets — determines both the quality of the liquidity buffer and the yield the bank earns on its surplus liquidity. Reinvestment decisions require cross-referencing portfolio yield, duration, market rates, and regulatory eligibility.
Lens
Scenario
Intent
Complexity

### CARD 7 [Insights|S] HQLA Portfolio Yield & Duration Dashboard
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/investment-portfolio/hqla-portfolio-yield-duration-dashboard
intent: Agent produces a daily HQLA portfolio dashboard covering current yield, duration, and spread-to-benchmark by asset class and regulatory tier, and flags positions where duration drift or credit spread widening has moved the portfolio outside its approved investment mandate.
Problem to solve: The HQLA portfolio is monitored against LCR and NSFR eligibility but not systematically against the yield and duration parameters of the investment mandate. Duration drift from maturing instruments and mark-to-market spread movements are visible in the portfolio system but not surfaced in a daily management view that links portfolio composition to both regulatory eligibility and mandate compliance.
Solution: Agent reads the portfolio position file and current market data feeds. It computes current weighted-average yield, duration, and spread-to-benchmark by Level 1 and Level 2 asset class, applies the bank's investment mandate parameters, and flags any position or aggregate exposure that sits outside the mandate range. The dashboard is available to the Treasurer each morning alongside the daily LCR report. Mandate breaches trigger an immediate alert for remediation review; the Treasurer confirms or escalates each flag.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Automation|S] HQLA Reinvestment Decision Support
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/investment-portfolio/hqla-reinvestment-decision-support
intent: When a HQLA instrument matures or a reinvestment window opens, agent presents the Treasurer with a ranked set of eligible replacement instruments — government bonds, central bank facilities, and qualifying Level 2 securities — scored by yield, LCR haircut, duration fit, and regulatory eligibility under NBKR, NBK/ARDFM, or CBR rules.
Problem to solve: HQLA reinvestment decisions are made by the Treasurer from a manual scan of available instruments against the regulatory eligibility schedule and the current portfolio gap. The analysis takes two to four hours per decision and is made without a consistent scoring framework that weighs yield against haircut cost and duration fit simultaneously.
Solution: Agent reads the maturing instrument details, the current portfolio composition, and the regulatory eligibility and haircut schedule for the relevant jurisdiction. It screens the universe of eligible instruments available in the market that day and scores each by yield-to-maturity, LCR haircut-adjusted return, duration fit to the portfolio target, and regulatory tier. The ranked shortlist and scoring rationale are presented to the Treasurer for the reinvestment decision. The Treasurer selects the instrument; the agent does not execute any transaction.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Optimize|M] HQLA Stress Scenario Adequacy Check
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/investment-portfolio/hqla-stress-scenario-adequacy-check
intent: Agent applies the bank's LCR and ILAAP stress scenario outflow assumptions to the current HQLA portfolio — applying regulatory haircuts and sale-execution constraints — and reports whether the portfolio provides adequate liquidity coverage across each stress horizon without breaching NSFR or concentration limits.
Problem to solve: The HQLA portfolio is sized against the LCR minimum on a daily basis but is not regularly assessed against the multi-week stress horizons in the ILAAP. A portfolio that passes LCR on day one may prove insufficient after 10 or 20 days if the composition relies on Level 2 assets subject to daily sale volume constraints or market-liquidity haircuts under stress.
Solution: Agent reads the current portfolio composition, the ILAAP stress scenario outflow profiles by day across 30 and 90-day horizons, and the regulatory haircut and daily sale volume limits applicable to each asset class. It computes the projected net liquidity position at each day under each stress scenario, identifies the day and scenario where the net position first approaches or breaches zero, and produces a portfolio adequacy report for the Treasurer and ALCO risk committee. Results inform the next quarterly portfolio composition review.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Funding strategy & wholesale mix
The funding strategy covers the bank's mix of retail deposits, corporate deposits, wholesale term funding, and central bank facilities — and the pricing, tenor, and diversification decisions that minimize funding cost within LCR, NSFR, and concentration limits. The Treasurer presents a quarterly funding strategy memo to ALCO with recommendations on deposit pricing, wholesale issuance, and contingent facility utilization.
Lens
Scenario
Intent
Complexity

### CARD 10 [Insights|S] Deposit Concentration Risk Insight
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/funding-strategy/deposit-concentration-risk-insight
intent: Agent monitors the retail and corporate deposit book for single-counterparty, sector, and geographic concentration against the bank's approved funding concentration limits, and surfaces emerging concentrations before they breach the threshold reported to ALCO.
Problem to solve: Deposit concentration analysis is a component of the quarterly funding strategy memo but is not monitored continuously between ALCO cycles. A single large corporate deposit that grows to represent a material share of the funding base, or a geographic concentration in a market exhibiting credit stress, may not be visible to the Treasurer until the quarterly memo is assembled.
Solution: Agent reads the current deposit register at the single-counterparty, sector, and geography level and computes concentration ratios against the bank's approved limits. It produces a weekly concentration dashboard for the Treasurer identifying the top twenty depositors by balance, the top five sector concentrations, and any balance movement that has brought a concentration measure within 10% of the approved limit. Limit proximity alerts are issued immediately when the threshold is crossed. ALCO reviews the concentration analysis at each quarterly funding strategy session.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Automation|S] Wholesale Funding Maturity Ladder
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/funding-strategy/wholesale-funding-maturity-ladder
intent: Agent generates the forward wholesale funding maturity ladder — by instrument, counterparty, and tenor bucket — from current funding register data, identifies refinancing concentrations in the 90-day and 12-month buckets, and presents the ladder to the Treasurer before each ALCO funding strategy discussion.
Problem to solve: The wholesale funding maturity profile is assembled from the funding register for each ALCO cycle, a process that requires data extraction across term deposits, repo agreements, medium-term notes, and covered bonds. Refinancing concentrations in near-term tenor buckets — where several instruments mature in the same two-week window — are identified during the assembly process rather than as a proactive signal that drives pre-emptive action.
Solution: Agent reads the funding register across all wholesale instrument categories and constructs a daily maturity ladder by 7-day, 30-day, 90-day, 180-day, and 12-month tenor buckets. It identifies windows where refinancing concentration in any 14-day period exceeds a defined threshold relative to the HQLA buffer and presents the ladder and concentration flags to the Treasurer each week. ALCO reviews the ladder at the quarterly funding strategy session; the Treasurer uses the weekly output to plan pre-emptive issuance timing.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Optimize|M] Funding Strategy Scenario Analysis
urn: urn:financial-services:scenario:finance-treasury/liquidity-management/funding-strategy/funding-strategy-scenario-analysis
intent: Agent models the cost and regulatory-ratio impact of alternative funding mixes against the current cash forecast and market conditions, ranking options for the Treasury funding committee.
Problem to solve: Funding mix scenario analysis is produced by Treasury analysts ahead of the weekly funding committee decision. The analysis window is constrained by the manual data update and ratio calculation cycle, limiting the range of scenarios the committee can consider within the available decision time.
Solution: Agent reads the current cash forecast, market rates, deposit repricing data, and regulatory ratio headroom, and produces a ranked comparison of funding mix options — cost, LCR impact, NSFR impact, concentration risk, and maturity profile — for the funding committee. Treasury reviews and selects; scenario breadth expands without extending the decision window.
OKR objective: The Treasury funding committee reviews a ranked comparison of funding mix alternatives — covering cost, LCR impact, NSFR impact, concentration risk, and maturity profile — produced from current cash forecast, market rates, and regulatory ratio headroom before each weekly decision.
OKR KR [Adoption]: Agent-produced funding strategy scenario comparison used for ≥40 of 52 weekly funding committee meetings in year 1.
OKR KR [Acceptance]: ≥80% of funding committee decisions cite the agent-produced scenario comparison as the primary analytical input; ratio calculations reconcile to Treasury management system outputs within ±0.5 percentage points in ≥97% of reviewed weeks.
OKR KR [Cycle]: Funding mix scenario comparison available for committee review within 2 hours of data refresh, vs. 4–8 hours of manual analyst assembly in the prior process.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
