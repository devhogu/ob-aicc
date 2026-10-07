# Liquidity management

Liquidity management is the Bank's discipline for maintaining sufficient liquid assets and diversified funding to meet obligations under both normal and stressed conditions. The Treasurer monitors LCR and NSFR ratios daily against regulatory minima, manages the HQLA portfolio, and operates the Contingency Funding Plan. **The GenAI opportunity is continuous liquidity intelligence — automating the daily reporting cycle, compressing stress scenario analysis, and surfacing slow-burn composition trends before they breach regulatory thresholds.**

## Problems

### Cash & liquidity position {#cash-liquidity-position}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Slow-burn funding composition trends — time-deposit migration to on-demand, deposit beta acceleration, or wholesale funding concentration growth — are identified at the quarterly stress refresh cycle, not as they develop. The Treasurer's daily view covers ratio compliance but not the trajectory of the inputs driving the ratio. |
| Enablement | When HQLA moves materially overnight — from repo, deposit concentration change, or wholesale maturity — attributing the movement to its source requires the treasury operations team to cross-reference treasury, funding, and cash management systems manually. The answer arrives after the morning meeting, not before. |
| Automation | The daily liquidity report — covering LCR, NSFR, HQLA composition, deposit flows, and funding maturities — is assembled each morning from system exports by a treasury operations team. The assembly consumes two to three hours before the Treasurer's review window opens. The report's structure is prescribed and inputs are known. |
| New business opportunities | Banks with continuous deposit composition and funding maturity visibility can optimize HQLA portfolio yield and funding cost within regulatory buffers in real time. Deposits repricing ahead of maturity, short-tenor wholesale funding extending opportunistically, and HQLA rebalancing between asset classes each require a current position view to execute with precision. |

## Daily LCR & NSFR monitoring {#daily-lcr-nsfr}

Daily LCR and NSFR ratio compliance is the Treasurer's primary regulatory obligation — maintained against the regulator's minima and internal management thresholds. The daily report covers ratio levels, HQLA composition, inflow and outflow drivers, and the overnight movement attribution that the Treasurer reviews before markets open.

### Daily LCR / NSFR Monitoring & Commentary

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/daily-lcr-nsfr/daily-lcr-nsfr-monitoring
- Lens: Automation
- Complexity: S
- Intent: The AI agent generates the daily LCR and NSFR commentary for the Treasurer — ratio movement attribution, HQLA composition note, regulatory buffer position, and ALCO-format narrative — from overnight system feeds.
- Problem to solve: The daily liquidity report covering LCR, NSFR, HQLA composition, and overnight ratio movement is assembled by treasury operations from multiple systems each morning. The assembly and drafting cycle delays the Treasurer's decision window on the day's funding and investment actions.
- Solution: The AI agent reads overnight LCR and NSFR data feeds, attributes ratio movements to inflow, outflow, and HQLA changes, and generates the daily report and accompanying ALCO-format narrative in the Treasurer's house structure. HQLA classification against LCR and NSFR regulatory eligibility rules is applied automatically to surface rebalancing requirements; the report is available at system open for the Treasurer's review.
- OKR: The daily LCR and NSFR report — covering ratio movement attribution, HQLA composition, regulatory buffer position, and ALCO-format narrative — is available to the Treasurer at system open each business day from overnight feeds.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced daily liquidity report delivered at system open for ≥220 trading days in year 1; ALCO-format narrative included in every daily output. |
| Acceptance | ≥90% of daily reports accepted by the Treasurer as accurate without requiring manual restatement; ratio figures reconcile to the formal monthly liquidity report in ≥98% of checked periods. |
| Cycle | Daily liquidity report available at system open vs. 1–2 hours post-open in the prior manual assembly process. |

### LCR & NSFR Driver Trend Analysis

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/daily-lcr-nsfr/lcr-nsfr-driver-trend-analysis
- Lens: Insights
- Complexity: S
- Intent: The AI agent analyzes the rolling twenty-trading-day history of LCR and NSFR movements to identify structural trends in inflow, outflow, and HQLA components — distinguishing seasonal patterns from persistent deterioration before the trend breaches a management threshold.
- Problem to solve: The daily liquidity report covers the overnight movement but does not contextualize it against the rolling trend. Persistent intra-month deterioration in a specific outflow category — such as retail deposit run-off or corporate line drawdowns — is visible in the daily report only as a sequence of individual movements that the Treasurer must manually aggregate to identify the structural direction.
- Solution: The AI agent maintains a rolling twenty-trading-day history of each LCR and NSFR component. It applies a trend decomposition to distinguish seasonal from structural movements and surfaces any component where the twenty-day direction shows persistent deterioration against the prior equivalent period. The trend analysis is appended to the daily report as a supplementary section each morning and shared with the Treasurer and the Treasury liquidity desk. Threshold-crossing trends trigger a proactive alert before the monthly ALCO cycle.
- OKR: The Treasurer receives, with each daily liquidity report, a twenty-trading-day trend analysis of LCR and NSFR components that separates seasonal movements from persistent deterioration before a management threshold is breached.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced trend analysis appended to the daily report on ≥220 trading days in year 1; all inflow, outflow, and HQLA components covered. |
| Acceptance | ≥80% of persistent-deterioration flags confirmed by the Treasurer as structural rather than seasonal; ≥90% of threshold-crossing trends alerted before the monthly ALCO cycle. |
| Cycle | Structural trend direction visible each morning, vs. manual aggregation of individual daily movements by the Treasurer in the prior process. |

### LCR Buffer Optimization Signal

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/daily-lcr-nsfr/lcr-buffer-optimisation-signal
- Lens: Optimize
- Complexity: S
- Intent: The AI agent analyzes the HQLA portfolio composition and the current LCR calculation to identify Level 1 and Level 2 rebalancing opportunities that maintain the regulatory ratio while improving portfolio yield within the regulator's eligibility constraints.
- Problem to solve: The HQLA portfolio is managed to maintain LCR compliance, but the composition between Level 1 central bank reserves, Level 1 government securities, and Level 2 assets is not systematically optimized for yield within the regulatory framework. Over-allocation to central bank reserves above the minimum required buffer suppresses yield without adding regulatory benefit; the analysis to identify rebalancing opportunities requires a manual cross-reference of the current HQLA composition against the LCR calculation.
- Solution: The AI agent reads the current HQLA portfolio composition, the daily LCR calculation inputs, and the applicable regulatory eligibility and haircut schedule. It computes the minimum required Level 1 balance for the current outflow base, identifies excess central bank reserves above that minimum, and presents a rebalancing signal — volume of excess reserves, eligible government securities that could replace them within Level 1, and the estimated yield pickup. The Treasurer reviews the signal and makes the reinvestment decision; the AI agent updates the analysis each day the excess persists.
- OKR: The Treasurer receives a rebalancing signal — the volume of central bank reserves held above the minimum required Level 1 balance, the eligible government securities that could replace them, and the estimated yield pickup — on each day the excess persists.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced rebalancing signal refreshed on ≥95% of business days on which excess reserves are identified in year 1. |
| Acceptance | ≥75% of signals rated by the Treasurer as actionable for the reinvestment decision; proposed replacement securities confirmed as eligible under the regulatory haircut schedule in 100% of reviewed signals. |
| Cycle | Rebalancing opportunity identified daily, vs. a manual cross-reference of HQLA composition against the LCR calculation in the prior process. |

## Contingency Funding Plan (CFP) {#contingency-funding-plan}

The Contingency Funding Plan is the Bank's documented playbook for managing liquidity under stress — sequencing the contingent actions available to the Treasurer from HQLA disposal through emergency borrowing facilities, with estimated execution timelines and liquidity values per action. The regulator requires the CFP to be maintained, stress-tested, and available for supervisory review.

### CFP Annual Review Narrative

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/contingency-funding-plan/cfp-annual-review-narrative
- Lens: Automation
- Complexity: S
- Intent: The AI agent drafts the annual CFP review narrative for the regulator — covering changes to the action register, revised stress outflow estimates, test exercise results, and governance attestation — from current Treasury data and the prior submission as a style anchor.
- Problem to solve: The annual CFP review narrative is a regulatory-required document prepared by Treasury with CFO and CRO sign-off. Drafting draws on test exercise results, the current action register, and the prior submission for structural consistency. The process takes one to two weeks of Treasury time and is repeated as a manual drafting exercise each year.
- Solution: The AI agent reads the current CFP action register with any changes from the prior year, the results of the most recent CFP test exercise, the current stress outflow estimates, and the prior-year approved CFP narrative as a style anchor. It generates a full draft covering the prescribed sections — governance, action register, stress estimates, test results, and attestation — and flags each change from the prior submission for explicit disclosure. Treasury reviews and edits; the AI agent handles the drafting cycle and version control.
- OKR: Treasury receives a full draft of the annual CFP review narrative — governance, action register, stress estimates, test results, and attestation — with each change from the prior submission flagged for explicit disclosure, ahead of CFO and CRO sign-off.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted CFP review narrative used for ≥1 annual CFP review within year 1; all prescribed sections covered. |
| Acceptance | ≥80% of drafted sections accepted by Treasury without material rewrite; changes from the prior submission flagged with ≥95% completeness on Treasury review. |
| Cycle | Full draft available within 3 business days of the action register, test results, and stress estimates being final, vs. one to two weeks of Treasury drafting in the prior process. |

### Contingency Funding Plan Stress Analysis

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/contingency-funding-plan/cfp-stress-analysis
- Lens: Enablement
- Complexity: M
- Intent: The AI agent runs liquidity stress scenarios against current position data and produces the CFP narrative — survival horizon, trigger conditions, and contingent action inventory — for ALCO and regulatory review.
- Problem to solve: Stress-scenario liquidity analysis for the Contingency Funding Plan is produced quarterly — and ad hoc after a market event — by cross-referencing the stress model, HQLA inventory, funding concentration data, and the documented contingent action list. Each production run is manual and the output is current only at point-in-time.
- Solution: The AI agent reads the liquidity stress model, current HQLA inventory, funding maturity profile, and contingent action list. It runs the prescribed stress scenarios, computes survival horizons per scenario, identifies assumptions that drive the most adverse outcomes, and generates the CFP narrative sections. The Treasurer checks the generated analysis and ALCO reviews it before approving the submission; the AI agent is re-run on demand following a material market event.
- OKR: The Contingency Funding Plan stress analysis — survival horizon, trigger conditions, and contingent action inventory — is produced from current position data for each prescribed scenario and available for ALCO and regulatory review on demand, including after material market events.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced CFP stress analysis used for ≥4 scheduled quarterly reviews and all ad hoc requests triggered by material market events within year 1. |
| Acceptance | ≥85% of CFP stress narratives approved by the Treasurer without material amendment to the survival horizon calculation; scenario outputs reconcile to the liquidity stress model within ±2% on periodic validation. |
| Cycle | CFP narrative available for ALCO review within 2 business days of a stress run trigger, vs. 1–2 weeks of manual assembly in the prior process. |

### CFP Stress Action Sequencing

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/contingency-funding-plan/cfp-stress-action-sequencing
- Lens: Insights
- Complexity: M
- Intent: The AI agent models the execution sequence and cumulative liquidity value of CFP contingent actions under each stress scenario — HQLA disposal, repo facility drawdown, emergency central bank borrowing — and identifies the minimum action set required to cover projected outflows within each stress horizon.
- Problem to solve: The CFP lists contingent actions with estimated liquidity values and execution timelines, but does not model the optimal sequencing of those actions under specific stress scenarios. ALCO and the Treasurer assess the adequacy of the CFP at annual review against a static stress outflow estimate, without a dynamic view of which action sequences are executable under market stress conditions.
- Solution: The AI agent reads the CFP action register with estimated liquidity values and execution timelines, and the stress scenario outflow projections by day from the current ILAAP. It models the execution sequence for each stress scenario, applying haircuts and timeline constraints to each action, and computes the cumulative liquidity coverage at each day of the stress horizon. Minimum action sets that cover projected outflows are identified for each scenario. ALCO and the Treasurer review the sequencing analysis at the annual CFP stress test review.
- OKR: ALCO and the Treasurer receive, for the annual CFP stress test review, a sequencing analysis showing cumulative liquidity coverage at each day of the stress horizon and the minimum set of contingent actions that covers projected outflows under each stress scenario.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced sequencing analysis used for ≥1 annual CFP stress test review within year 1; all ILAAP stress scenarios and CFP actions modeled. |
| Acceptance | ≥85% of minimum action sets confirmed by the Treasurer as executable under stress conditions; haircuts and execution timelines reconcile to the CFP action register in ≥98% of reviewed actions. |
| Cycle | Sequencing analysis available within 3 business days of the ILAAP outflow projections, vs. assessment against a static stress outflow estimate in the prior process. |

## HQLA portfolio & investment management {#investment-portfolio}

The HQLA portfolio holds the securities and central bank reserves that constitute the Bank's liquid asset buffer under LCR and NSFR. Portfolio composition — between Level 1 assets (central bank reserves, government securities) and Level 2 assets — determines both the quality of the liquidity buffer and the yield the Bank earns on its surplus liquidity. Reinvestment decisions require cross-referencing portfolio yield, duration, market rates, and regulatory eligibility.

### HQLA Portfolio Yield & Duration Dashboard

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/investment-portfolio/hqla-portfolio-yield-duration-dashboard
- Lens: Insights
- Complexity: S
- Intent: The AI agent produces a daily HQLA portfolio dashboard covering current yield, duration, and spread-to-benchmark by asset class and regulatory tier, and flags positions where duration drift or credit spread widening has moved the portfolio outside its approved investment mandate.
- Problem to solve: The HQLA portfolio is monitored against LCR and NSFR eligibility but not systematically against the yield and duration parameters of the investment mandate. Duration drift from maturing instruments and mark-to-market spread movements are visible in the portfolio system but not surfaced in a daily management view that links portfolio composition to both regulatory eligibility and mandate compliance.
- Solution: The AI agent reads the portfolio position file and current market data feeds. It computes current weighted-average yield, duration, and spread-to-benchmark by Level 1 and Level 2 asset class, applies the Bank's investment mandate parameters, and flags any position or aggregate exposure that sits outside the mandate range. The dashboard is available to the Treasurer each morning alongside the daily LCR report. Mandate breaches trigger an immediate alert for remediation review; the Treasurer confirms or escalates each flag.
- OKR: The Treasurer receives a daily HQLA portfolio dashboard — yield, duration, and spread-to-benchmark by Level 1 and Level 2 asset class — with positions outside the approved investment mandate flagged, alongside the daily LCR report.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced dashboard available each morning on ≥220 trading days in year 1; all HQLA asset classes covered. |
| Acceptance | ≥90% of mandate flags confirmed or escalated by the Treasurer as genuine; yield and duration figures reconcile to the portfolio system in ≥98% of sampled positions. |
| Cycle | Duration drift and spread movements against the mandate visible each morning, vs. no daily management view linking composition to mandate compliance in the prior process. |

### HQLA Reinvestment Decision Support

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/investment-portfolio/hqla-reinvestment-decision-support
- Lens: Automation
- Complexity: S
- Intent: When an HQLA instrument matures or a reinvestment window opens, the AI agent presents the Treasurer with a ranked set of eligible replacement instruments — government bonds, central bank facilities, and qualifying Level 2 securities — scored by yield, LCR haircut, duration fit, and regulatory eligibility under the regulator's rules.
- Problem to solve: HQLA reinvestment decisions are made by the Treasurer from a manual scan of available instruments against the regulatory eligibility schedule and the current portfolio gap. The analysis takes two to four hours per decision and is made without a consistent scoring framework that weighs yield against haircut cost and duration fit simultaneously.
- Solution: The AI agent reads the maturing instrument details, the current portfolio composition, and the applicable regulatory eligibility and haircut schedule. It screens the universe of eligible instruments available in the market that day and scores each by yield-to-maturity, LCR haircut-adjusted return, duration fit to the portfolio target, and regulatory tier. The ranked shortlist and scoring rationale are presented to the Treasurer for the reinvestment decision. The Treasurer selects the instrument; the AI agent does not execute any transaction.
- OKR: The Treasurer receives, when an HQLA instrument matures or a reinvestment window opens, a ranked shortlist of eligible replacement instruments scored by yield-to-maturity, LCR haircut-adjusted return, duration fit, and regulatory tier, with the scoring rationale.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced shortlist used for ≥90% of HQLA reinvestment decisions in year 1. |
| Acceptance | Treasurer selects from the top three ranked instruments in ≥80% of decisions; eligibility and haircut classification confirmed correct in 100% of reviewed shortlists. |
| Cycle | Ranked shortlist available within 30 minutes of the reinvestment trigger, vs. two to four hours of manual scanning per decision in the prior process. |

### HQLA Stress Scenario Adequacy Check

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/investment-portfolio/hqla-stress-scenario-adequacy-check
- Lens: Optimize
- Complexity: M
- Intent: The AI agent applies the Bank's LCR and ILAAP stress scenario outflow assumptions to the current HQLA portfolio — applying regulatory haircuts and sale-execution constraints — and reports whether the portfolio provides adequate liquidity coverage at each day of each stress horizon.
- Problem to solve: The HQLA portfolio is sized against the LCR minimum on a daily basis but is not regularly assessed against the multi-week stress horizons in the ILAAP. A portfolio that passes LCR on day one may prove insufficient after 10 or 20 days if the composition relies on Level 2 assets subject to daily sale volume constraints or market-liquidity haircuts under stress.
- Solution: The AI agent reads the current portfolio composition, the ILAAP stress scenario outflow profiles by day across 30- and 90-day horizons, and the regulatory haircut and daily sale volume limits applicable to each asset class. It computes the projected net liquidity position at each day under each stress scenario, identifies the day and scenario where the net position first approaches or breaches zero, and produces a portfolio adequacy report for the Treasurer and ALCO. Results inform the next quarterly portfolio composition review.
- OKR: The Treasurer and ALCO receive a portfolio adequacy report showing the projected net liquidity position at each day of the 30- and 90-day ILAAP stress horizons, and the day and scenario where it first approaches or breaches zero, ahead of each quarterly portfolio composition review.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced adequacy report used for ≥4 quarterly portfolio composition reviews within year 1; all ILAAP stress scenarios covered. |
| Acceptance | ≥85% of adequacy reports accepted by the Treasurer without material recalculation; haircuts and daily sale volume limits applied correctly in ≥98% of reviewed asset classes. |
| Cycle | Multi-week stress adequacy assessed each quarter within 2 business days of the portfolio position date, vs. sizing against the daily LCR minimum only in the prior process. |

## Funding strategy & wholesale mix {#funding-strategy}

The funding strategy covers the Bank's mix of retail deposits, corporate deposits, wholesale term funding, and central bank facilities — and the pricing, tenor, and diversification decisions that minimize funding cost within LCR, NSFR, and concentration limits. The Treasurer presents a quarterly funding strategy memo to ALCO with recommendations on deposit pricing, wholesale issuance, and contingent facility utilization.

### Deposit Concentration Risk Insight

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/funding-strategy/deposit-concentration-risk-insight
- Lens: Insights
- Complexity: S
- Intent: The AI agent monitors the retail and corporate deposit book for single-counterparty, sector, and geographic concentration against the Bank's approved funding concentration limits, and surfaces emerging concentrations before they breach the threshold reported to ALCO.
- Problem to solve: Deposit concentration analysis is a component of the quarterly funding strategy memo but is not monitored continuously between ALCO cycles. A single large corporate deposit that grows to represent a material share of the funding base, or a geographic concentration in a market exhibiting credit stress, may not be visible to the Treasurer until the quarterly memo is assembled.
- Solution: The AI agent reads the current deposit register at the single-counterparty, sector, and geography level and computes concentration ratios against the Bank's approved limits. It produces a weekly concentration dashboard for the Treasurer identifying the top twenty depositors by balance, the top five sector concentrations, and any balance movement that has brought a concentration measure within 10% of the approved limit. Limit proximity alerts are issued immediately when the threshold is crossed, for the Treasurer to confirm. ALCO reviews the concentration analysis at each quarterly funding strategy session.
- OKR: The Treasurer receives a weekly deposit concentration dashboard — the top twenty depositors, the top five sector concentrations, and any measure within 10% of its approved limit — with an immediate alert when a limit proximity threshold is crossed.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced concentration dashboard delivered for ≥48 of 52 weeks in year 1; single-counterparty, sector, and geographic measures covered. |
| Acceptance | ≥85% of limit proximity alerts confirmed by the Treasurer as accurate; concentration ratios reconcile to the deposit register in ≥98% of sampled measures. |
| Cycle | Emerging concentrations visible weekly, vs. only when the quarterly funding strategy memo is assembled in the prior process. |

### Wholesale Funding Maturity Ladder

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/funding-strategy/wholesale-funding-maturity-ladder
- Lens: Automation
- Complexity: S
- Intent: The AI agent generates the forward wholesale funding maturity ladder — by instrument, counterparty, and tenor bucket — from current funding register data, identifies refinancing concentrations in the 90-day and 12-month buckets, and presents the ladder to the Treasurer each week, ahead of the quarterly ALCO funding strategy session.
- Problem to solve: The wholesale funding maturity profile is assembled from the funding register for each ALCO cycle, a process that requires data extraction across term deposits, repo agreements, medium-term notes, and, where the Bank issues them, covered bonds. Refinancing concentrations in near-term tenor buckets — where several instruments mature in the same two-week window — are identified during the assembly process rather than as a proactive signal that drives pre-emptive action.
- Solution: The AI agent reads the funding register across all wholesale instrument categories and constructs a daily maturity ladder by 7-day, 30-day, 90-day, 180-day, and 12-month tenor buckets. It identifies windows where refinancing concentration in any 14-day period exceeds a defined threshold relative to the HQLA buffer and presents the ladder and concentration flags to the Treasurer each week. ALCO reviews the ladder at the quarterly funding strategy session; the Treasurer uses the weekly output to plan pre-emptive issuance timing.
- OKR: The Treasurer receives a weekly forward wholesale funding maturity ladder — by instrument, counterparty, and tenor bucket — with refinancing concentrations in any 14-day window flagged against the HQLA buffer.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced maturity ladder delivered for ≥48 of 52 weeks in year 1 and reviewed at ≥4 quarterly ALCO funding strategy sessions; all wholesale instrument categories covered. |
| Acceptance | ≥90% of ladders accepted by the Treasurer without correction; maturities reconcile to the funding register in ≥98% of sampled instruments. |
| Cycle | Refinancing concentrations flagged weekly, vs. identified only during assembly for each ALCO cycle in the prior process. |

### Funding Strategy Scenario Analysis

- URN: urn:financial-services:scenario:finance-treasury/liquidity-management/funding-strategy/funding-strategy-scenario-analysis
- Lens: Optimize
- Complexity: M
- Intent: The AI agent models the cost and regulatory-ratio impact of alternative funding mixes against the current cash forecast and market conditions, ranking options for the Treasury funding committee.
- Problem to solve: Funding mix scenario analysis is produced by Treasury analysts ahead of the weekly funding committee decision. The analysis window is constrained by the manual data update and ratio calculation cycle, limiting the range of scenarios the committee can consider within the available decision time.
- Solution: The AI agent reads the current cash forecast, market rates, deposit repricing data, and regulatory ratio headroom, and produces a ranked comparison of funding mix options — cost, LCR impact, NSFR impact, concentration risk, and maturity profile — for the funding committee. The committee reviews the comparison and selects the funding mix; scenario breadth expands without extending the decision window.
- OKR: The Treasury funding committee reviews a ranked comparison of funding mix alternatives — covering cost, LCR impact, NSFR impact, concentration risk, and maturity profile — produced from current cash forecast, market rates, and regulatory ratio headroom before each weekly decision.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced funding strategy scenario comparison used for ≥40 of 52 weekly funding committee meetings in year 1. |
| Acceptance | ≥80% of funding committee decisions cite the AI-produced scenario comparison as the primary analytical input; ratio calculations reconcile to Treasury management system outputs within ±0.5 percentage points in ≥97% of reviewed weeks. |
| Cycle | Funding mix scenario comparison available for committee review within 2 hours of data refresh, vs. 4–8 hours of manual analyst assembly in the prior process. |
