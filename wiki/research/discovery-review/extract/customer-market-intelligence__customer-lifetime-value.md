# 

source: html-alt/financial-services/en/customer-market-intelligence/customer-lifetime-value/index.html


[PAGE TEXT]
CAC / LTV / payback
The unit-economics triad — customer acquisition cost, lifetime value, and capital payback period — that governs whether the bank's growth investment is creating or destroying economic value. CAC is straightforward in principle but complex in practice: fully-loaded CAC must include sales, marketing, onboarding, and compliance overhead, not just paid acquisition spend. LTV extrapolation from early-cohort behaviour carries model risk that must be made explicit. Under OECD CRS and regional regulatory expectations for consumer credit, LTV assumptions underpin pricing and provisioning.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] CAC/LTV Payback Monitor
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cac-ltv-payback/cac-ltv-payback-monitor
intent: Automated quarterly CAC/LTV/payback report by acquisition channel, produced from finance, marketing, and cohort-model data without manual assembly, delivered to the commercial leadership team.
Problem to solve: Unit-economics calculations require data from marketing, finance, operations, and the CLV model team. Each team produces its input on its own cycle; combining the inputs into a single report requires a coordination exercise that typically takes two to three weeks. By the time the report is available, a quarter of the next planning cycle has elapsed.
Solution: Agent reads marketing spend, onboarding cost, and CLV-model outputs on a quarterly cadence, assembles the CAC/LTV/payback calculation for each acquisition channel, and produces the standard commercial report. Commercial leadership receives the unit-economics view within one week of quarter close; the coordination exercise between teams is replaced by agent-driven data assembly.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Insights|M] Unit Economics Channel Dashboard
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cac-ltv-payback/unit-economics-channel-dashboard
intent: Agent calculates fully-loaded CAC, LTV, and payback period by acquisition channel quarterly, producing a unit-economics dashboard that enables marketing and commercial leadership to compare channel efficiency on a consistent basis.
Problem to solve: CAC is tracked by the marketing team as paid media cost per new account opened, without including sales, compliance onboarding, and operational overhead in the denominator. LTV is calculated by the finance team on separate assumptions. The two numbers are produced on different cycles by different teams and are never combined into a channel-level payback view. Marketing investment decisions are made on paid-only CAC, which systematically overstates digital-channel efficiency.
Solution: Agent reads marketing spend, onboarding cost, sales overhead, and compliance cost allocations from finance and operations, combines them with LTV projections from the cohort model, and computes fully-loaded CAC, LTV, and payback period by channel. Marketing and commercial leadership review a consistent unit-economics dashboard each quarter; channel investment decisions reference payback rather than paid-only CAC.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Insights|M] Payback-Risk Cohort Flag
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cac-ltv-payback/payback-risk-cohort-flag
intent: Agent identifies acquisition cohorts where actual LTV trajectory is tracking below the payback-period projection used in the original investment case, and produces a flag for CFO and marketing leadership review.
Problem to solve: LTV projections underpin the investment case for each acquisition channel. Actual cohort performance against those projections is not tracked between the original investment case and the annual CLV model refresh. Cohorts that are materially underperforming their payback projection — mobile-acquired cohorts exiting at month 10 against a 24-month payback projection — are not flagged until the annual model comparison, when the investment capital has already been deployed.
Solution: Agent reads actual cohort revenue and retention outcomes quarterly, compares against the LTV projection recorded in the original investment case, and flags cohorts where actual trajectory is more than a defined percentage below projection. CFO and marketing leadership receive the flag with a current payback-period estimate versus the original projection; channel investment decisions for the following quarter account for the cohort performance gap.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Acquisition channel prioritisation
Ranking and reallocating acquisition-channel investment based on channel-specific LTV/CAC ratios — the mechanism by which CLV measurement translates into growth-budget allocation. Default last-touch attribution systematically over-credits paid channels and under-credits content and referral, inflating the apparent CAC for organic channels. Accurate channel-level CLV requires multi-touch attribution and cohort-level LTV by origination channel, maintained over the full customer lifecycle.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] Channel Attribution Model Report
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/acquisition-channel-prioritisation/channel-attribution-model-report
intent: Automated quarterly report of multi-touch channel attribution for new customer originations, replacing last-touch attribution with a distributional view that corrects the systematic over-crediting of paid search.
Problem to solve: New customer origination is attributed to the last marketing touch before account opening — typically a paid search click. Organic channels — content, referral, in-branch — that influenced the customer journey earlier receive no attribution credit. Marketing investment decisions based on last-touch attribution systematically over-invest in paid performance channels and under-invest in organic channels.
Solution: Agent reads the customer journey touch sequence for each new origination, applies a data-driven multi-touch attribution model, and distributes conversion credit across the full journey. The quarterly attribution report shows paid and organic channel contributions under multi-touch attribution; marketing investment decisions reference the distributional view rather than the last-touch metric.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Insights|M] Channel LTV/CAC Ranking
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/acquisition-channel-prioritisation/channel-ltv-cac-ranking
intent: Agent produces a ranked comparison of acquisition channels by LTV/CAC ratio and payback period quarterly, enabling marketing leadership to rebalance channel investment toward the most economically efficient origination sources.
Problem to solve: Marketing investment decisions across channels — digital performance, branch referral, partnership, and direct — are made on cost-per-acquisition metrics that do not include LTV. A partnership channel with a higher cost per new account may produce customers with twice the LTV of a digital acquisition channel; without the LTV dimension, the partnership channel appears less efficient and receives lower investment.
Solution: Agent reads channel-level CAC components and CLV-model outputs for each origination cohort, computes LTV/CAC ratios and payback periods by channel, and produces a quarterly ranking. Marketing leadership uses the channel ranking as the primary input for budget reallocation decisions; channels are evaluated on economic return rather than cost-per-acquisition alone.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Enablement|M] Acquisition Channel Mix Optimiser
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/acquisition-channel-prioritisation/acquisition-channel-mix-optimiser
intent: Agent models the channel-mix allocation that maximises aggregate LTV generated from the acquisition budget, subject to capacity and regulatory constraints, and produces a recommended mix for the next planning cycle.
Problem to solve: Acquisition budget allocation across channels is determined through planning discussions that reference prior-year spend ratios, available channel capacity, and qualitative judgement. The combination of LTV/CAC data, channel capacity constraints, and a budget constraint that would enable a formally optimised channel-mix recommendation is not assembled as a standard planning input.
Solution: Agent reads LTV/CAC ratios by channel, channel capacity constraints, and the acquisition budget envelope, runs an allocation model maximising expected aggregate LTV subject to constraints, and produces a recommended channel-mix for the planning cycle. Marketing leadership reviews the agent-generated recommendation alongside qualitative inputs; the allocation discussion starts from an economically grounded baseline.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Cohort-level CLV
CLV calculated at the cohort level — by origination vintage, acquisition channel, product bundle, and segment — rather than as a blended average. Cohort-level CLV reveals structural differences that aggregate numbers conceal: a mobile-acquisition cohort may have 40% lower LTV than a branch-originated cohort for the same product, changing the economics of the digital-channel investment case entirely. Cohort analysis requires maintaining product, payment, and activity histories per cohort over the full customer lifecycle.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] Cohort CLV Vintage Monitor
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cohort-level-clv/cohort-clv-vintage-monitor
intent: Automated quarterly report of CLV trajectory by origination vintage, showing which vintages are tracking above, on, and below projection at each tenure milestone for finance and commercial review.
Problem to solve: Origination vintage CLV tracking is conducted annually when the full cohort analysis is refreshed. Vintages from the most recent 12 to 18 months — when early-tenure trajectory divergence is most actionable — receive no interim tracking between production runs. Finance and commercial teams cannot see in the current year whether a recent digital acquisition vintage is on track to meet its payback projection.
Solution: Agent reads revenue and product-holding data for each origination vintage quarterly, computes CLV trajectory against the cohort projection, and produces the standard vintage monitor report. Finance and commercial teams review whether recent vintages are on track at each tenure milestone and flag deviating vintages for intervention ahead of the annual model refresh.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Insights|M] Cohort CLV Trajectory Report
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cohort-level-clv/cohort-clv-trajectory-report
intent: Agent calculates CLV trajectory per origination cohort quarterly, identifies cohorts deviating from projected trajectory, and produces a narrative with driver attribution for CFO and commercial-lead review.
Problem to solve: Cohort-level CLV is calculated annually for strategic planning and remains static between refreshes. Trajectory deviations — a mobile-acquisition cohort whose tenure is shortening relative to projections — surface only when they appear in aggregate churn or revenue numbers, months after the cohort signal was available.
Solution: Agent calculates CLV trajectory per cohort from billing, product, and retention data on a quarterly cadence, identifies deviating cohorts, and produces a narrative with driver attribution and recommended management action. CFO and commercial leads review the agent-generated report rather than raw cohort tables.
OKR objective: A CLV trajectory report per origination cohort — identifying cohorts deviating from projected trajectory and attributing primary drivers — is available to the CFO and commercial leadership on the quarterly scheduled cadence.
OKR KR [Adoption]: Agent produces the cohort CLV trajectory report for ≥95% of quarterly scheduled cycles for ≥4 consecutive quarters post go-live.
OKR KR [Acceptance]: ≥80% of cohort trajectory narratives confirmed as directionally accurate by commercial leadership on quarterly review.
OKR KR [Cycle]: CLV trajectory reporting cycle reduced from 4–6 weeks of manual cohort modelling and narrative assembly to ≤1 week of automated production and leadership review.

### CARD 9 [Insights|M] Channel-Vintage CLV Comparison
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cohort-level-clv/channel-vintage-clv-comparison
intent: Agent compares CLV trajectories for customers originated through different channels within the same vintage, identifying structural CLV differences between digital, branch, and direct-sales acquisition for investment-case validation.
Problem to solve: CLV analysis is conducted at segment or product level; origination channel is treated as an attribute rather than a primary analysis dimension. Whether mobile-originated customers within the retail mass segment generate higher or lower 24-month CLV than branch-originated customers from the same vintage is not available as a standard output, despite being the most important variable in the digital investment case.
Solution: Agent reads CLV trajectory data with origination-channel attribution, computes CLV comparisons for digital, branch, and direct-sales origin cohorts within equivalent segment and vintage groups, and produces a channel-vintage comparison report. Digital investment cases reference the agent-generated channel CLV comparison; branch-network rationalisation decisions use the same output.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Retention spend allocation
Allocating retention investment — save-programme offers, loyalty programme costs, relationship-manager time — across cohorts based on CLV impact rather than uniform spend per at-risk customer. A retention intervention on a high-CLV customer generates more economic value per pound spent than the same intervention on a low-CLV customer. Without CLV as the prioritisation input, retention spend defaults to the loudest or most recent at-risk signal rather than the highest-value one.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|S] Retention Spend ROI Tracking
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/retention-spend-allocation/retention-spend-roi-tracking
intent: Automated quarterly report of retention spend ROI by cohort — actual CLV saved versus intervention cost — delivered to finance and commercial leadership without manual calculation.
Problem to solve: Retention spend is tracked as a budget line; the CLV value it preserves is not measured against the cost. Finance reviews retention spend as a cost item and commercial leadership reviews save rate as a performance metric, but neither team has a combined view of retention ROI — CLV preserved per unit of retention spend — that would validate or challenge the current budget level.
Solution: Agent reads save-programme costs — offer cost, relationship-manager time, channel cost — and CLV data for retained customers by cohort, computes retention ROI per cohort quarterly, and produces the finance and commercial report. The retention budget discussion in quarterly planning is grounded in CLV-preserved-per-pound evidence rather than cost trend alone.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Enablement|M] CLV-Weighted Retention Prioritisation
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/retention-spend-allocation/clv-weighted-retention-prioritisation
intent: Agent ranks the at-risk customer list by CLV-weighted save value, producing a prioritised intervention queue where high-CLV at-risk customers are contacted ahead of lower-value customers with the same churn probability.
Problem to solve: At-risk lists are ranked by churn probability without weighting for the CLV at stake. Relationship managers and save-programme teams allocate equal intervention resources to a low-CLV customer and a high-CLV customer with the same churn probability, misallocating the most expensive save-programme interventions.
Solution: Agent reads the at-risk probability score alongside the CLV estimate for each customer, produces a CLV-weighted save-value ranking, and delivers a prioritised intervention queue. High-CLV at-risk customers receive contact priority; the save-programme team executes against the agent-generated queue rather than the unweighted risk list.
OKR objective: The at-risk customer list is ranked by CLV-weighted save value on each retention cycle, directing save programme and RM contact to the customers where revenue retention is highest relative to intervention cost.
OKR KR [Adoption]: Agent produces a CLV-weighted ranked intervention queue for ≥95% of weekly retention cycles for ≥48 consecutive weeks post go-live.
OKR KR [Acceptance]: ≥75% of top-quintile CLV-weighted intervention recommendations confirmed as priority contacts by the retention team lead on weekly review.
OKR KR [Cycle]: At-risk list prioritisation cycle reduced from manual analyst ranking to weekly automated CLV-weighted output within 4 hours of scoring completion.

### CARD 12 [Insights|M] CLV-Driven Retention Budget Allocation
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/retention-spend-allocation/clv-retention-budget-allocation
intent: Agent models the retention-spend allocation that maximises expected CLV saved across the at-risk cohort given a fixed budget, and produces a recommended allocation for commercial leadership approval.
Problem to solve: Retention budgets are allocated across customer segments based on historic spend ratios and segment size, not on the CLV at stake and the expected save rate per pound spent. Equal per-customer spend across a high-CLV and a low-CLV at-risk cohort of the same size produces materially different economic returns, but the allocation process does not model this difference.
Solution: Agent reads the current at-risk list with CLV estimates, expected save rates by intervention type from prior-cycle efficacy data, and the available retention budget, and runs an allocation optimisation that maximises expected CLV saved subject to the budget constraint. Commercial leadership reviews and approves the recommended allocation; the retention operations team executes against it.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
CLV by segment
Customer lifetime value disaggregated by segment — retail mass, emerging affluent, SME micro, SME core — enabling relative comparison of segment economics and informing where relationship investment generates the highest return. Segment CLV differences drive service-model decisions: the economics of dedicated relationship management versus digital self-service are answerable only from segment-level CLV data. In KZ and KG banking markets, segment CLV analysis must account for the disproportionate revenue concentration in the SME and high-income retail cohorts.
Lens
Scenario
Intent
Complexity

### CARD 13 [Automation|S] Segment CLV Automated Refresh
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/clv-by-segment/segment-clv-automated-refresh
intent: Automated quarterly refresh of CLV by segment, produced from core banking, CRM, and billing data without manual extraction, with trend commentary delivered to the commercial planning team.
Problem to solve: The CLV-by-segment calculation requires revenue, margin, product-holding, retention, and churn data drawn from four or five source systems. Finance and analytics teams coordinate the extraction, standardisation, and calculation manually, taking three to four weeks from quarter close. The segment CLV numbers arrive in the commercial planning cycle late, reducing their influence on decisions already in progress.
Solution: Agent reads source data from core banking, CRM, and billing systems on a quarterly cadence, applies the standard CLV calculation by segment, and produces the refresh report within one week of quarter close. The commercial planning team receives current-quarter segment CLV as an input to cycle planning rather than a retrospective confirmation.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 14 [Insights|M] Segment CLV Comparison Report
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/clv-by-segment/segment-clv-comparison-report
intent: Agent calculates and compares CLV by segment — retail mass, emerging affluent, SME micro, SME core — quarterly, producing a ranked segment-economics view for commercial and strategic leadership to inform service-model investment decisions.
Problem to solve: Segment-level CLV is calculated annually for strategic planning and remains static between refreshes. Commercial teams making service-model and relationship-investment decisions during the year work from the prior-year CLV estimate, which may reflect a substantially different segment composition, product mix, or retention-rate environment than the current one.
Solution: Agent reads per-customer revenue, margin, product-holding, and retention data quarterly, computes CLV by segment using a consistent methodology, and produces a ranked segment-economics comparison. Commercial and strategic leadership use the quarterly CLV view for service-model decisions; the annual planning CLV becomes a confirmation of the quarterly signal rather than the sole input.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 15 [Insights|M] Segment CLV ROI Attribution
urn: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/clv-by-segment/segment-clv-roi-attribution
intent: Agent attributes CLV improvement or decline by segment to the principal drivers — retention-rate change, product-penetration depth, margin-per-product movement — and produces a driver-attribution brief for commercial leadership.
Problem to solve: Segment CLV changes between refreshes are reported as a number movement without driver attribution. A 12% CLV improvement in the SME core segment could reflect improved retention, higher product penetration per customer, or a margin expansion in the credit product. Without attribution, commercial teams cannot determine which intervention generated the CLV improvement or which driver needs addressing when CLV declines.
Solution: Agent decomposes CLV movement by segment into its principal drivers — retention-rate contribution, penetration-depth contribution, margin-per-product contribution — and produces a quarterly attribution brief alongside the standard CLV refresh. Commercial leadership directs investment to the drivers that generated CLV improvement and targets the drivers contributing to CLV decline.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
