# Customer lifetime value

Customer lifetime value measures the net economic contribution of a customer relationship across its projected duration — integrating acquisition cost, revenue trajectory, product penetration, retention probability, and risk-adjusted margin. CLV governs acquisition-channel investment, retention-spend allocation, and product-sequencing decisions: a bank that acquires high-CAC, low-LTV customers at scale destroys capital even while growing the book. Where relationship depth is concentrated in salary-account and payroll-linked cohorts, CLV analysis must account for that concentration. **GenAI compresses CLV from annual planning inputs to continuous decision signals** — surfacing channel-specific unit economics and cohort-level payback in hours rather than weeks.

## CAC / LTV / payback {#cac-ltv-payback}

The unit-economics triad — customer acquisition cost, lifetime value, and capital payback period — that governs whether a bank's growth investment is creating or destroying economic value. CAC is straightforward in principle but complex in practice: fully-loaded CAC must include sales, marketing, onboarding, and compliance overhead, not just paid acquisition spend. LTV extrapolation from early-cohort behavior carries model risk that must be made explicit.

### CAC/LTV Payback Monitor

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cac-ltv-payback/cac-ltv-payback-monitor
- Lens: Automation
- Complexity: S
- Intent: Automated quarterly CAC/LTV/payback report by acquisition channel, produced from finance, marketing, and cohort-model data without manual assembly, delivered to the commercial leadership team.
- Problem to solve: Unit-economics calculations require data from marketing, finance, operations, and the CLV model team. Each team produces its input on its own cycle; combining the inputs into a single report requires a coordination exercise that typically takes two to three weeks. By the time the report is available, a quarter of the next planning cycle has elapsed.
- Solution: The AI agent reads marketing spend, onboarding cost, and CLV-model outputs on a quarterly cadence, assembles the CAC/LTV/payback calculation for each acquisition channel, and produces the standard commercial report. Commercial leadership receives the unit-economics view within one week of quarter close; the coordination exercise between teams is replaced by AI-driven data assembly.
- OKR: The commercial leadership team receives the quarterly CAC/LTV/payback report by acquisition channel within one week of quarter close, assembled from finance, marketing, and cohort-model data without cross-team coordination.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the CAC/LTV/payback report for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live, covering all acquisition channels. |
| Acceptance | ≥85% of reports accepted by commercial leadership without recalculation; inputs reconciled to finance and marketing source figures in every cycle. |
| Cycle | Unit-economics report production reduced from two to three weeks of cross-team coordination to ≤1 week from quarter close. |

### Unit Economics Channel Dashboard

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cac-ltv-payback/unit-economics-channel-dashboard
- Lens: Insights
- Complexity: M
- Intent: The AI agent calculates fully-loaded CAC, LTV, and payback period by acquisition channel quarterly, producing a unit-economics dashboard that enables marketing and commercial leadership to compare channel efficiency on a consistent basis.
- Problem to solve: CAC is tracked by the marketing team as paid media cost per new account opened, without including sales, compliance onboarding, and operational overhead in the cost base. LTV is calculated by the finance team on separate assumptions. The two numbers are produced on different cycles by different teams and are never combined into a channel-level payback view. Marketing investment decisions are made on paid-only CAC, which systematically overstates digital-channel efficiency.
- Solution: The AI agent reads marketing spend, onboarding cost, sales overhead, and compliance cost allocations from finance and operations, combines them with LTV projections from the cohort model, and computes fully-loaded CAC, LTV, and payback period by channel. Marketing and commercial leadership review a consistent unit-economics dashboard each quarter; channel investment decisions reference payback rather than paid-only CAC.
- OKR: Marketing and commercial leadership review a quarterly unit-economics dashboard showing fully-loaded CAC, LTV, and payback period by acquisition channel on one consistent basis.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the dashboard for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live; fully-loaded CAC includes marketing, onboarding, sales, and compliance cost allocations for every channel. |
| Acceptance | ≥80% of channel investment decisions in quarterly planning reference payback from the dashboard; cost allocations confirmed by finance in every cycle. |
| Cycle | Channel payback view moved from not produced, with CAC and LTV calculated separately on different cycles, to a combined quarterly dashboard within 2 weeks of quarter close. |

### Payback-Risk Cohort Flag

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cac-ltv-payback/payback-risk-cohort-flag
- Lens: Insights
- Complexity: M
- Intent: The AI agent identifies acquisition cohorts where actual LTV trajectory is tracking below the payback-period projection used in the original investment case, and produces a flag for CFO and marketing leadership review.
- Problem to solve: LTV projections underpin the investment case for each acquisition channel. Actual cohort performance against those projections is not tracked between the original investment case and the annual CLV model refresh. Cohorts that are materially underperforming their payback projection — mobile-acquired cohorts exiting at month 10 against a 24-month payback projection — are not flagged until the annual model comparison, when the investment capital has already been deployed.
- Solution: The AI agent reads actual cohort revenue and retention outcomes quarterly, compares against the LTV projection recorded in the original investment case, and flags cohorts where actual trajectory is more than a defined percentage below projection. CFO and marketing leadership receive the flag with a current payback-period estimate versus the original projection; channel investment decisions for the following quarter account for the cohort performance gap.
- OKR: The CFO and marketing leadership receive a quarterly flag for acquisition cohorts whose actual LTV trajectory is tracking below the projection in the original investment case, with a current payback-period estimate set against the original.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent compares actual cohort revenue and retention against projection for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live, covering all cohorts with a recorded investment case. |
| Acceptance | ≥80% of flagged cohorts confirmed as materially underperforming by the CFO's team; flagged gaps reflected in ≥75% of following-quarter channel investment decisions. |
| Cycle | Detection of payback underperformance reduced from the annual CLV model refresh to quarterly review. |

## Acquisition channel prioritization {#acquisition-channel-prioritisation}

Ranking and reallocating acquisition-channel investment based on channel-specific LTV/CAC ratios — the mechanism by which CLV measurement translates into growth-budget allocation. Default last-touch attribution systematically over-credits paid channels and under-credits content and referral, inflating the apparent CAC for organic channels. Accurate channel-level CLV requires multi-touch attribution and cohort-level LTV by origination channel, maintained over the full customer lifecycle.

### Channel Attribution Model Report

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/acquisition-channel-prioritisation/channel-attribution-model-report
- Lens: Automation
- Complexity: M
- Intent: Automated quarterly report of multi-touch channel attribution for new customer originations, replacing last-touch attribution with a distributional view that corrects the systematic over-crediting of paid search.
- Problem to solve: New customer origination is attributed to the last marketing touch before account opening — typically a paid search click. Organic channels — content, referral, in-branch — that influenced the customer journey earlier receive no attribution credit. Marketing investment decisions based on last-touch attribution systematically over-invest in paid performance channels and under-invest in organic channels.
- Solution: The AI agent reads the customer journey touch sequence for each new origination, applies a data-driven multi-touch attribution model, and distributes conversion credit across the full journey. Marketing leadership receives the quarterly attribution report, which shows paid and organic channel contributions under multi-touch attribution; marketing investment decisions reference the distributional view rather than the last-touch metric.
- OKR: Marketing leadership receives a quarterly multi-touch attribution report for new customer originations, showing paid and organic channel contributions across the full journey in place of last-touch attribution.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent applies the multi-touch attribution model to ≥95% of new originations with a recorded touch sequence and delivers the report for ≥4 consecutive quarters post go-live. |
| Acceptance | ≥80% of attribution reports accepted by marketing leadership as the reference for channel investment decisions in place of the last-touch metric. |
| Cycle | Attribution reporting moved from last-touch only to a quarterly multi-touch report within 2 weeks of quarter close. |

### Channel LTV/CAC Ranking

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/acquisition-channel-prioritisation/channel-ltv-cac-ranking
- Lens: Insights
- Complexity: M
- Intent: The AI agent produces a ranked comparison of acquisition channels by LTV/CAC ratio and payback period quarterly, enabling marketing leadership to rebalance channel investment toward the most economically efficient origination sources.
- Problem to solve: Marketing investment decisions across channels — digital performance, branch referral, partnership, and direct — are made on cost-per-acquisition metrics that do not include LTV. A partnership channel with a higher cost per new account may produce customers with twice the LTV of a digital acquisition channel; without the LTV dimension, the partnership channel appears less efficient and receives lower investment.
- Solution: The AI agent reads channel-level CAC components and CLV-model outputs for each origination cohort, computes LTV/CAC ratios and payback periods by channel, and produces a quarterly ranking. Marketing leadership uses the channel ranking as the primary input for budget reallocation decisions; channels are evaluated on economic return rather than cost-per-acquisition alone.
- OKR: Marketing leadership receives a quarterly ranking of acquisition channels by LTV/CAC ratio and payback period as the primary input for budget reallocation decisions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the channel ranking for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live, covering digital performance, branch referral, partnership, and direct channels. |
| Acceptance | ≥80% of rankings accepted by marketing leadership as the primary input to budget reallocation; ranking changes explained by underlying CAC or LTV movement in every cycle. |
| Cycle | Channel evaluation moved from cost-per-acquisition alone to a quarterly LTV/CAC ranking within 2 weeks of quarter close. |

### Acquisition Channel Mix Optimizer

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/acquisition-channel-prioritisation/acquisition-channel-mix-optimiser
- Lens: Optimize
- Complexity: M
- Intent: The AI agent models the channel-mix allocation that maximizes aggregate LTV generated from the acquisition budget, subject to capacity and regulatory constraints, and produces a recommended mix for marketing leadership for the next planning cycle.
- Problem to solve: Acquisition budget allocation across channels is determined through planning discussions that reference prior-year spend ratios, available channel capacity, and qualitative judgment. The combination of LTV/CAC data, channel capacity constraints, and a budget constraint that would enable a formally optimized channel-mix recommendation is not assembled as a standard planning input.
- Solution: The AI agent reads LTV/CAC ratios by channel, channel capacity constraints, and the acquisition budget envelope, runs an allocation model maximizing expected aggregate LTV subject to constraints, and produces a recommended channel-mix for the planning cycle. Marketing leadership reviews the AI-generated recommendation alongside qualitative inputs; the allocation discussion starts from an economically grounded baseline.
- OKR: Marketing leadership receives a recommended channel-mix allocation for each planning cycle — maximizing expected aggregate LTV within the acquisition budget and channel capacity constraints — as the starting baseline for the allocation discussion.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the channel-mix recommendation for ≥90% of planning cycles from go-live, using current LTV/CAC ratios, channel capacity constraints, and the budget envelope. |
| Acceptance | ≥70% of recommended allocations adopted by marketing leadership with adjustment of no more than 10% of budget per channel. |
| Cycle | Channel-mix preparation moved from planning discussions based on prior-year spend ratios to a modeled recommendation available ≥1 week before the planning session. |

## Cohort-level CLV {#cohort-level-clv}

CLV calculated at the cohort level — by origination vintage, acquisition channel, product bundle, and segment — rather than as a blended average. Cohort-level CLV reveals structural differences that aggregate numbers conceal: a mobile-acquisition cohort may have 40% lower LTV than a branch-originated cohort for the same product, changing the economics of the digital-channel investment case entirely. Cohort analysis requires maintaining product, payment, and activity histories per cohort over the full customer lifecycle.

### Cohort CLV Vintage Monitor

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cohort-level-clv/cohort-clv-vintage-monitor
- Lens: Automation
- Complexity: S
- Intent: Automated quarterly report of CLV trajectory by origination vintage, showing which vintages are tracking above, on, and below projection at each tenure milestone for finance and commercial review.
- Problem to solve: Origination vintage CLV tracking is conducted annually when the full cohort analysis is refreshed. Vintages from the most recent 12 to 18 months — when early-tenure trajectory divergence is most actionable — receive no interim tracking between production runs. Finance and commercial teams cannot see in the current year whether a recent digital acquisition vintage is on track to meet its payback projection.
- Solution: The AI agent reads revenue and product-holding data for each origination vintage quarterly, computes CLV trajectory against the cohort projection, and produces the standard vintage monitor report. Finance and commercial teams review whether recent vintages are on track at each tenure milestone and flag deviating vintages for intervention ahead of the annual model refresh.
- OKR: Finance and commercial teams receive a quarterly vintage monitor showing which origination vintages are tracking above, on, or below CLV projection at each tenure milestone.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the vintage monitor for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live, covering all vintages from the most recent 18 months. |
| Acceptance | ≥80% of vintages flagged as deviating confirmed by finance and commercial teams on review; ≥75% of confirmed deviations assigned for intervention ahead of the annual model refresh. |
| Cycle | Vintage CLV tracking cycle reduced from the annual cohort analysis refresh to quarterly production within 2 weeks of quarter close. |

### Cohort CLV Trajectory Report

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cohort-level-clv/cohort-clv-trajectory-report
- Lens: Insights
- Complexity: M
- Intent: The AI agent calculates CLV trajectory per origination cohort quarterly, identifies cohorts deviating from projected trajectory, and produces a narrative with driver attribution for review by the CFO and commercial leadership.
- Problem to solve: Cohort-level CLV is calculated annually for strategic planning and remains static between refreshes. Trajectory deviations — a mobile-acquisition cohort whose tenure is shortening relative to projections — surface only when they appear in aggregate churn or revenue numbers, months after the cohort signal was available.
- Solution: The AI agent calculates CLV trajectory per cohort from revenue, product, and retention data on a quarterly cadence, identifies deviating cohorts, and produces a narrative with driver attribution and recommended management action. The CFO and commercial leadership review the AI-generated report rather than raw cohort tables.
- OKR: A CLV trajectory report per origination cohort — identifying cohorts deviating from projected trajectory and attributing primary drivers — is available to the CFO and commercial leadership on the quarterly scheduled cadence.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the cohort CLV trajectory report for ≥95% of quarterly scheduled cycles for ≥4 consecutive quarters post go-live. |
| Acceptance | ≥80% of cohort trajectory narratives confirmed as directionally accurate by commercial leadership on quarterly review. |
| Cycle | CLV trajectory reporting cycle reduced from 4–6 weeks of manual cohort modeling and narrative assembly to ≤1 week of automated production and leadership review. |

### Channel-Vintage CLV Comparison

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/cohort-level-clv/channel-vintage-clv-comparison
- Lens: Insights
- Complexity: M
- Intent: The AI agent compares CLV trajectories for customers originated through different channels within the same vintage, identifying structural CLV differences between digital, branch, and direct-sales acquisition for investment-case validation.
- Problem to solve: CLV analysis is conducted at segment or product level; origination channel is treated as an attribute rather than a primary analysis dimension. Whether mobile-originated customers within the retail mass segment generate higher or lower 24-month CLV than branch-originated customers from the same vintage is not available as a standard output, despite being the most important variable in the digital investment case.
- Solution: The AI agent reads CLV trajectory data with origination-channel attribution, computes CLV comparisons for digital, branch, and direct-sales origin cohorts within equivalent segment and vintage groups, and produces a channel-vintage comparison report. Digital investment cases reference the AI-generated channel CLV comparison; branch-network rationalization decisions use the same output.
- OKR: A channel-vintage comparison report — CLV trajectories for digital, branch, and direct-sales origin cohorts within equivalent segment and vintage groups — is available as the standard reference for digital investment cases and branch-network rationalization decisions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the comparison report for ≥90% of scheduled refresh cycles for ≥4 consecutive quarters post go-live, covering all three origination channels. |
| Acceptance | ≥80% of digital investment cases and branch-network rationalization proposals submitted in the period reference the comparison; computed channel differences confirmed on sampled review. |
| Cycle | Channel-level CLV comparison moved from not available as a standard output to a report refreshed within 3 weeks of each CLV trajectory update. |

## Retention spend allocation {#retention-spend-allocation}

Allocating retention investment — save-program offers, loyalty-program costs, relationship-manager time — across cohorts based on CLV impact rather than uniform spend per at-risk customer. A retention intervention on a high-CLV customer generates more economic value per unit of spend than the same intervention on a low-CLV customer. Without CLV as the prioritization input, retention spend defaults to the loudest or most recent at-risk signal rather than the highest-value one.

### Retention Spend ROI Tracking

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/retention-spend-allocation/retention-spend-roi-tracking
- Lens: Automation
- Complexity: S
- Intent: Automated quarterly report of retention spend ROI by cohort — actual CLV saved versus intervention cost — delivered to finance and commercial leadership without manual calculation.
- Problem to solve: Retention spend is tracked as a budget line; the CLV value it preserves is not measured against the cost. Finance reviews retention spend as a cost item and commercial leadership reviews save rate as a performance metric, but neither team has a combined view of retention ROI — CLV preserved per unit of retention spend — that would validate or challenge the current budget level.
- Solution: The AI agent reads save-program costs — offer cost, relationship-manager time, channel cost — and CLV data for retained customers by cohort, computes retention ROI per cohort quarterly, and produces the finance and commercial report. The retention budget discussion in quarterly planning is grounded in evidence of CLV preserved per unit of spend rather than cost trend alone.
- OKR: Finance and commercial leadership receive a quarterly report of retention ROI by cohort — CLV preserved against offer cost, relationship-manager time, and channel cost — as the shared basis for the retention budget discussion.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the retention ROI report for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live, covering all cohorts with save-program spend. |
| Acceptance | ≥80% of reports accepted by finance without recalculation; the report referenced in 100% of quarterly retention budget discussions. |
| Cycle | Retention ROI measurement moved from not calculated, with spend and save rate reviewed separately, to a quarterly report within 2 weeks of quarter close. |

### CLV-Weighted Retention Prioritization

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/retention-spend-allocation/clv-weighted-retention-prioritisation
- Lens: Enablement
- Complexity: M
- Intent: The AI agent ranks the at-risk customer list by CLV-weighted save value, producing a prioritized intervention queue where high-CLV at-risk customers are contacted ahead of lower-value customers with the same churn probability.
- Problem to solve: At-risk lists are ranked by churn probability without weighting for the CLV at stake. Relationship managers and save-program teams allocate equal intervention resources to a low-CLV customer and a high-CLV customer with the same churn probability, misallocating the most expensive save-program interventions.
- Solution: The AI agent reads the at-risk probability score alongside the CLV estimate for each customer, produces a CLV-weighted save-value ranking, and delivers a prioritized intervention queue in which high-CLV at-risk customers receive contact priority. The retention team lead confirms the priority contacts on weekly review; the save-program team executes against the AI-generated queue rather than the unweighted risk list.
- OKR: The at-risk customer list is ranked by CLV-weighted save value on each retention cycle, directing save-program and relationship-manager contact to the customers where revenue retention is highest relative to intervention cost.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces a CLV-weighted ranked intervention queue for ≥95% of weekly retention cycles for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥75% of top-quintile CLV-weighted intervention recommendations confirmed as priority contacts by the retention team lead on weekly review. |
| Cycle | At-risk list prioritization cycle reduced from manual analyst ranking to weekly automated CLV-weighted output within 4 hours of scoring completion. |

### CLV-Driven Retention Budget Allocation

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/retention-spend-allocation/clv-retention-budget-allocation
- Lens: Optimize
- Complexity: M
- Intent: The AI agent models the retention-spend allocation that maximizes expected CLV saved across the at-risk cohort given a fixed budget, and produces a recommended allocation for commercial leadership approval.
- Problem to solve: Retention budgets are allocated across customer segments based on historic spend ratios and segment size, not on the CLV at stake and the expected save rate per unit of spend. Equal per-customer spend across a high-CLV and a low-CLV at-risk cohort of the same size produces materially different economic returns, but the allocation process does not model this difference.
- Solution: The AI agent reads the current at-risk list with CLV estimates, expected save rates by intervention type from prior-cycle efficacy data, and the available retention budget, and runs an allocation optimization that maximizes expected CLV saved subject to the budget constraint. Commercial leadership reviews and approves the recommended allocation; the retention operations team executes against it.
- OKR: Commercial leadership receives a recommended retention-budget allocation that maximizes expected CLV saved across the at-risk cohort within the available budget, for approval and execution by retention operations.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the allocation recommendation for ≥90% of retention budget cycles from go-live, using current at-risk CLV estimates and prior-cycle save rates by intervention type. |
| Acceptance | ≥75% of recommended allocations approved by commercial leadership with minor amendment or none. |
| Cycle | Retention budget allocation moved from historic spend ratios and segment size to a modeled recommendation available ≥1 week before each budget decision. |

## CLV by segment {#clv-by-segment}

Customer lifetime value disaggregated by segment — retail mass, emerging affluent, SME micro, SME core — enabling relative comparison of segment economics and informing where relationship investment generates the highest return. Segment CLV differences drive service-model decisions: the economics of dedicated relationship management versus digital self-service are answerable only from segment-level CLV data. Where revenue is concentrated in the SME and high-income retail cohorts, segment CLV analysis must account for that concentration.

### Segment CLV Automated Refresh

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/clv-by-segment/segment-clv-automated-refresh
- Lens: Automation
- Complexity: S
- Intent: Automated quarterly refresh of CLV by segment, produced from core banking, CRM, and revenue data without manual extraction, with trend commentary delivered to the commercial planning team.
- Problem to solve: The CLV-by-segment calculation requires revenue, margin, product-holding, retention, and churn data drawn from four or five source systems. Finance and analytics teams coordinate the extraction, standardization, and calculation manually, taking three to four weeks per refresh. The segment CLV numbers arrive in the commercial planning cycle late, reducing their influence on decisions already in progress.
- Solution: The AI agent reads source data from core banking, CRM, and finance systems on a quarterly cadence, applies the standard CLV calculation by segment, and produces the refresh report with trend commentary within one week of quarter close. The commercial planning team receives current-quarter segment CLV as an input to cycle planning rather than a retrospective confirmation.
- OKR: The commercial planning team receives the quarterly CLV-by-segment refresh with trend commentary within one week of quarter close, in time to inform planning decisions rather than confirm them.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the segment CLV refresh for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live. |
| Acceptance | ≥85% of refresh reports accepted by the commercial planning team without recalculation; segment CLV figures reconciled to source revenue and margin data in every cycle. |
| Cycle | Segment CLV refresh reduced from three to four weeks of manual extraction and calculation to ≤1 week from quarter close. |

### Segment CLV Comparison Report

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/clv-by-segment/segment-clv-comparison-report
- Lens: Insights
- Complexity: M
- Intent: The AI agent calculates and compares CLV by segment — retail mass, emerging affluent, SME micro, SME core — quarterly, producing a ranked segment-economics view for commercial and strategic leadership to inform service-model investment decisions.
- Problem to solve: Segment-level CLV is calculated annually for strategic planning and remains static between refreshes. Commercial teams making service-model and relationship-investment decisions during the year work from the prior-year CLV estimate, which may reflect a substantially different segment composition, product mix, or retention-rate environment than the current one.
- Solution: The AI agent reads per-customer revenue, margin, product-holding, and retention data quarterly, computes CLV by segment using a consistent methodology, and produces a ranked segment-economics comparison. Commercial and strategic leadership use the quarterly CLV view for service-model decisions; the annual planning CLV becomes a confirmation of the quarterly signal rather than the sole input.
- OKR: Commercial and strategic leadership receive a quarterly ranked comparison of CLV by segment — retail mass, emerging affluent, SME micro, SME core — calculated on a consistent methodology, for service-model investment decisions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the segment-economics comparison for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live, covering all four segments. |
| Acceptance | ≥80% of comparison reports accepted by commercial and strategic leadership as the reference for service-model decisions made in the quarter. |
| Cycle | Segment CLV comparison cycle reduced from annual calculation to quarterly production within 2 weeks of quarter close. |

### Segment CLV Driver Attribution

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-lifetime-value/clv-by-segment/segment-clv-roi-attribution
- Lens: Insights
- Complexity: M
- Intent: The AI agent attributes CLV improvement or decline by segment to the principal drivers — retention-rate change, product-penetration depth, margin-per-product movement — and produces a driver-attribution brief for commercial leadership.
- Problem to solve: Segment CLV changes between refreshes are reported as a number movement without driver attribution. A 12% CLV improvement in the SME core segment could reflect improved retention, higher product penetration per customer, or a margin expansion in the credit product. Without attribution, commercial teams cannot determine which intervention generated the CLV improvement or which driver needs addressing when CLV declines.
- Solution: The AI agent decomposes CLV movement by segment into its principal drivers — retention-rate contribution, penetration-depth contribution, margin-per-product contribution — and produces a quarterly attribution brief alongside the standard CLV refresh. Commercial leadership directs investment to the drivers that generated CLV improvement and targets the drivers contributing to CLV decline.
- OKR: Commercial leadership receives a quarterly driver-attribution brief alongside the CLV refresh, decomposing each segment's CLV movement into retention-rate, penetration-depth, and margin-per-product contributions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the attribution brief for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live, covering every segment in the CLV refresh. |
| Acceptance | ≥80% of driver attributions confirmed as directionally accurate by commercial leadership on quarterly review. |
| Cycle | Segment CLV change moved from a number reported without attribution to a driver brief delivered with each quarterly refresh. |
