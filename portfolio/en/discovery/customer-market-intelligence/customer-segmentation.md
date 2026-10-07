# Customer segmentation

Customer segmentation is the analytical discipline of dividing the customer base into groups with shared economics, behavior, or needs — the foundation on which product design, pricing, channel investment, and retention programs are targeted. Segment boundaries commonly reflect the concentration of banking relationships in salary-account and pension-linked retail cohorts and the SME credit-access gap. **GenAI accelerates segmentation from static annual exercises to continuous model refresh**, enabling commercial teams to act on segment shifts within weeks rather than quarters.

## Behavioral segmentation {#behavioural-segmentation}

Classification of the customer base by observed transaction patterns, channel use, and product activity — the primary basis for propensity scoring and next-best-action prioritization. Behavioral segments shift continuously as customer activity evolves, but most banks refresh them quarterly or annually. In line with supervisory expectations on customer profiling, behavioral segmentation feeds AML transaction monitoring and retail credit scoring overlays.

### Digital Behavior Cluster Analysis

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/behavioural-segmentation/digital-behaviour-cluster-analysis
- Lens: Insights
- Complexity: S
- Intent: The AI agent clusters customers by digital-channel interaction patterns monthly, producing named behavioral archetypes and their size for product and channel investment decisions.
- Problem to solve: Digital behavior data — app session frequency, feature-use patterns, self-service versus assisted-channel mix — is captured in analytics platforms but not connected to CRM segment definitions. Channel investment decisions and digital product prioritization proceed without a systematic view of which behavioral archetypes represent the largest and most commercially relevant customer groups.
- Solution: The AI agent reads app and digital-channel interaction logs, clusters customers by interaction pattern, names the top archetypes by feature-use and channel-mix profile, and sizes each cohort. Product and channel teams receive a monthly archetype report, which their leads review each quarter; segment definitions are updated to incorporate the digital-behavior dimension.
- OKR: A monthly digital-behavior archetype report — naming the top archetypes by feature-use and channel-mix profile and sizing each cohort — is available to product and channel teams for channel investment and digital product prioritization.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the archetype report for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live; clustering covers all active digital-channel customers. |
| Acceptance | ≥80% of named archetypes confirmed as commercially meaningful by product and channel leads on quarterly review; the digital-behavior dimension incorporated into segment definitions within 6 months of go-live. |
| Cycle | Digital-behavior archetype view moved from no systematic production to a monthly automated report within 5 business days of month close. |

### Transaction Pattern Anomaly Flag

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/behavioural-segmentation/transaction-pattern-anomaly-flag
- Lens: Insights
- Complexity: S
- Intent: The AI agent identifies customers whose transaction patterns have diverged materially from their segment baseline, flagging both outliers for AML review and commercial opportunities for relationship-manager follow-up.
- Problem to solve: Segment-baseline transaction patterns are used for AML monitoring thresholds but the comparison is run on static annual baselines. Customers whose patterns shift gradually but persistently — a growing cash-withdrawal pattern in a salary-account holder, or a new inbound payment source — drift outside their segment norm for months before the next annual baseline comparison picks them up.
- Solution: The AI agent computes a rolling segment baseline from the prior 90 days and flags customers whose current-week transaction pattern deviates beyond a statistical threshold. AML analysts receive a prioritized review list; commercial teams receive a separate flag for customers showing positive engagement uplift above segment norm, for relationship-manager follow-up.
- OKR: Customers whose transaction patterns diverge materially from a rolling 90-day segment baseline are flagged each week — as a prioritized review list for AML and a separate engagement-uplift flag for commercial teams.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent computes the rolling segment baseline and delivers both flag lists for ≥95% of weekly cycles for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥70% of deviations on the AML list confirmed as warranting review by AML analysts; ≥60% of engagement-uplift flags accepted for follow-up by relationship managers. |
| Cycle | Segment-baseline comparison cycle reduced from static annual baselines to a rolling 90-day baseline evaluated weekly. |

### Behavioral Segment Refresh

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/behavioural-segmentation/behavioural-segment-refresh
- Lens: Insights
- Complexity: M
- Intent: The AI agent recalculates behavioral segment membership from transaction and channel-use data on a fortnightly cadence, surfacing the customers who have migrated across tiers since the last cycle for commercial and compliance review.
- Problem to solve: Behavioral segments are refreshed quarterly. Customers who shift transaction patterns — salary-account holders who start using a competitor for daily spend, or dormant customers who re-engage — remain in their prior segment for up to three months. AML monitoring overlays and propensity models built on stale segment labels produce alerts and targeting errors.
- Solution: The AI agent reads transaction, channel, and product-activity logs fortnightly, recalculates behavioral segment membership for the full active base, and produces a migration report showing net moves per tier. Compliance and commercial teams review the updated segment assignments; AML monitoring and propensity models consume the refreshed labels.
- OKR: Behavioral segment membership for the full active base is recalculated fortnightly, with a migration report of net moves per tier available to compliance and commercial teams and refreshed labels feeding AML monitoring and propensity models.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent completes the fortnightly recalculation and migration report for ≥95% of scheduled cycles for ≥26 consecutive fortnights post go-live. |
| Acceptance | ≥85% of refreshed segment assignments accepted by compliance and commercial reviewers without manual correction on sampled review. |
| Cycle | Behavioral segment refresh cycle reduced from quarterly to fortnightly, cutting the maximum age of a segment label from three months to two weeks. |

## Segment-to-product mapping {#segment-to-product-mapping}

Translation of segment definitions into product eligibility, pricing tiers, and feature prioritization — the operating mechanism by which segmentation drives commercial decisions. When segment membership is refreshed faster than product mapping, the two fall out of sync and campaigns target the wrong population. In multi-product banking contexts, the mapping must cover credit, deposits, cards, insurance, and digital service tiers simultaneously.

### Segment-Product Eligibility Sync

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-to-product-mapping/segment-product-eligibility-sync
- Lens: Automation
- Complexity: S
- Intent: The AI agent validates alignment between segment-membership updates and product-eligibility assignments weekly, flagging mismatches where a customer's segment has changed but their product eligibility has not been updated.
- Problem to solve: Segment membership is refreshed on a faster cadence than product eligibility assignment. When a customer migrates from the mass-retail tier to the emerging-affluent tier, the product eligibility update that unlocks investment or premium card products is triggered only in the next manual mapping review — weeks later. Campaigns and digital journeys present the customer with out-of-date product offers.
- Solution: The AI agent reads the segment-membership snapshot and the product-eligibility register each week, identifies mismatches where segment has changed but eligibility has not updated, and produces a correction queue for the product operations team, which confirms and corrects them. Digital journeys and campaign targeting consume the refreshed eligibility data within 48 hours of the segment update.
- OKR: Mismatches between segment membership and product eligibility are identified each week and delivered as a correction queue to the product operations team, so that digital journeys and campaigns present offers matching the customer's current segment.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent runs the segment-to-eligibility comparison for ≥95% of weekly cycles for ≥48 consecutive weeks post go-live, covering all products in the eligibility register. |
| Acceptance | ≥90% of mismatches in the correction queue confirmed as genuine by the product operations team and corrected within the same weekly cycle. |
| Cycle | Eligibility update lag after a segment change reduced from weeks, pending the next manual mapping review, to ≤48 hours. |

### Segment Pricing-Tier Mapping Review

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-to-product-mapping/segment-pricing-tier-mapping-review
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes the relationship between segment membership and pricing-tier assignment across credit, deposit, and fee products, identifying where pricing tiers are out of step with segment economics for a pricing-committee review.
- Problem to solve: Pricing tiers are set at product level with reference to segment definitions, but the two are not systematically compared after initial setting. As segment membership evolves — an affluent retail cohort grows while the mass-retail cohort shrinks — the pricing tiers that were calibrated on a prior segment mix become misaligned with current segment economics, leaving margin on the table or creating over-pricing exposure in regulated retail products.
- Solution: The AI agent reads segment-membership distribution and pricing-tier assignment across credit, deposit, and fee products quarterly, computes the margin impact of pricing-tier misalignment by segment, and produces a ranked list of adjustment opportunities for the pricing committee. The pricing committee evaluates pricing-tier adjustments against segment economics rather than legacy precedent.
- OKR: The pricing committee receives a quarterly ranked list of pricing-tier adjustment opportunities across credit, deposit, and fee products, with the margin impact of misalignment computed by segment.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the pricing-tier misalignment analysis for ≥90% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live. |
| Acceptance | ≥70% of ranked adjustment opportunities accepted by the pricing committee for evaluation; margin-impact estimates confirmed as directionally accurate in ≥80% of reviewed cases. |
| Cycle | Comparison of pricing tiers against segment economics moved from a one-off check at initial tier setting to a quarterly review delivered within 2 weeks of quarter close. |

### Segment Feature Demand Mapping

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-to-product-mapping/segment-feature-demand-mapping
- Lens: Insights
- Complexity: M
- Intent: The AI agent maps inferred product-feature demand by segment from usage patterns and voice-of-customer data, identifying where the current feature set has demand gaps that the product roadmap has not addressed.
- Problem to solve: Product roadmap prioritization is informed by stakeholder input and NPS scores but not by a systematic mapping of feature demand to segment. Segments with high wallet-share potential but a weak voice in survey and NPS feedback — SME micro, rural retail — have their feature needs under-represented in the prioritization process, and the product roadmap concentrates development on the most vocal segments.
- Solution: The AI agent reads product-feature usage patterns, NPS verbatims, complaint themes, and app-review content, infers feature-demand signals by segment, and produces a demand-gap map showing which segments are most under-served by the current feature set. Product leadership uses the map as a quarterly roadmap input alongside stakeholder proposals.
- OKR: Product leadership receives a quarterly demand-gap map — feature-demand signals inferred by segment from usage patterns, NPS verbatims, complaint themes, and app reviews — showing which segments the current feature set under-serves.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the demand-gap map for ≥90% of scheduled quarterly roadmap cycles for ≥4 consecutive quarters post go-live, covering all defined segments. |
| Acceptance | ≥70% of identified demand gaps confirmed as valid roadmap inputs by product leadership on quarterly review. |
| Cycle | Feature-demand mapping by segment moved from no systematic production to a quarterly output available ≥1 week before each roadmap prioritization session. |

## Value-based segmentation {#value-based-segmentation}

Grouping customers by economic contribution — actual and potential — typically expressed as revenue per customer, product penetration, or risk-adjusted margin. Value tiers set the service model, relationship investment, and retention priority: a bank that cannot identify its top decile by current value misallocates relationship-manager capacity. Where high-value flows are concentrated in a small proportion of the retail salary-account base, value segmentation must account for that concentration.

### Top-Decile Revenue Concentration Report

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/value-based-segmentation/top-decile-revenue-concentration-report
- Lens: Automation
- Complexity: S
- Intent: Automated monthly report of revenue concentration in the top value tiers — top 1%, top 5%, top 10% — with trend commentary, delivered to retail and commercial leadership without manual data assembly.
- Problem to solve: Revenue concentration in the top customer tiers is tracked annually. Commercial leadership cannot see in-year changes in concentration — whether the top decile is becoming more or less concentrated — without commissioning a custom analysis. Monthly board packs carry aggregate revenue numbers but not the distribution-level view that informs service-model decisions.
- Solution: The AI agent reads customer-level revenue and margin data monthly, computes concentration metrics for the top 1%, 5%, and 10% value tiers, and produces a monthly report with trend commentary. Retail and commercial leadership receive the concentration view monthly as part of the standard management pack.
- OKR: Retail and commercial leadership receive a monthly revenue-concentration report for the top 1%, 5%, and 10% value tiers, with trend commentary, as part of the standard management pack and without manual data assembly.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the concentration report for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥85% of reports accepted by retail and commercial leadership for the management pack without supplementary analysis requests. |
| Cycle | Revenue-concentration reporting cycle reduced from annual tracking, or a custom analysis on request, to a monthly report within 5 business days of month close. |

### High-Value Attrition Early Warning

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/value-based-segmentation/high-value-attrition-early-warning
- Lens: Insights
- Complexity: S
- Intent: The AI agent monitors top-decile customers for early-stage disengagement signals weekly, surfacing at-risk high-value customers before they appear in the standard at-risk scoring model.
- Problem to solve: The standard at-risk scoring model is calibrated on the full active base and uses thresholds appropriate for the median customer. High-value customers, who typically have lower transaction frequency and a more concentrated product footprint, can exhibit meaningful disengagement — declining balance trend, reduced transaction frequency, unused credit facilities — without crossing the standard model's threshold for weeks.
- Solution: The AI agent applies a high-value-specific attrition signal framework to the top-decile customer list weekly, using tighter thresholds calibrated on prior high-value churn patterns. Relationship managers receive a weekly list of top-decile customers showing early-stage disengagement signals, enabling contact ahead of the standard at-risk model alert.
- OKR: Relationship managers receive a weekly list of top-decile customers showing early-stage disengagement signals, identified with high-value-specific thresholds ahead of the standard at-risk model alert.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent applies the high-value attrition signal framework to the full top-decile customer list for ≥95% of weekly cycles for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥70% of flagged customers confirmed as warranting contact by the responsible relationship manager; ≥80% of flagged customers contacted within 5 business days. |
| Cycle | Detection of high-value disengagement advanced by ≥3 weeks relative to the standard at-risk model alert. |

### Value-Tier Classification

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/value-based-segmentation/value-tier-classification
- Lens: Insights
- Complexity: M
- Intent: The AI agent calculates risk-adjusted revenue contribution per customer quarterly, classifies the base into value tiers, and produces a tier-migration report showing which customers have moved into or out of the top decile since the prior quarter.
- Problem to solve: Value-tier classification is produced annually for strategic planning and used to set relationship-manager portfolio composition targets. Customers who move into the top value decile during the year — a retail customer who starts salary crediting or an SME that draws on a credit facility — are not reclassified until the annual refresh, and relationship-manager assignment does not adjust to reflect the commercial priority shift.
- Solution: The AI agent reads revenue, product-holding, and margin data quarterly, computes risk-adjusted revenue contribution per customer, classifies the base into value tiers, and produces a migration report, which the relationship-manager teams review each quarter. Relationship-manager assignments and service-model decisions are updated to reflect the current-quarter tier classification rather than the prior-year model.
- OKR: The customer base is classified into value tiers each quarter from risk-adjusted revenue contribution, with a tier-migration report showing moves into and out of the top decile available for relationship-manager assignment and service-model decisions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the value-tier classification and migration report for ≥90% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live, covering the full customer base. |
| Acceptance | ≥80% of top-decile entries and exits confirmed as correct on quarterly review by the relationship-manager teams that receive them; relationship-manager assignment updated for ≥75% of customers entering the top decile within the following quarter. |
| Cycle | Value-tier classification cycle reduced from annual refresh to quarterly production within 3 weeks of quarter close. |

## Segment migration tracking {#segment-migration-tracking}

Systematic monitoring of customer movement across segment definitions over time — the feedback loop that validates whether retention programs and product interventions are working as intended. Migration rates are a leading indicator of segment health: rapid downward migration in a value tier signals a structural problem before it surfaces in revenue or NPS data.

### Segment Migration Tracker

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-migration-tracking/segment-migration-tracker
- Lens: Insights
- Complexity: S
- Intent: The AI agent recalculates segment membership from transaction and behavior feeds on a weekly cadence, ranking migration cohorts by commercial priority for segment heads.
- Problem to solve: Segment membership is recalculated quarterly. Customers migrating across value or behavioral tiers are identified retrospectively, after the commercial window has passed. High-value customers in early-stage downgrade are the last to be flagged.
- Solution: The AI agent reads transaction and behavior feeds weekly, recalculates segment membership, and ranks migration cohorts — high-value downgraders, emerging mid-tier, re-engaged dormant — by commercial priority. Segment heads receive a weekly migration brief with recommended action by cohort.
- OKR: Segment membership is recalculated from transaction and behavior feeds weekly, with migration cohorts ranked by commercial priority and available to segment heads at each review cycle — replacing quarterly recalculation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the weekly segment migration ranking for ≥95% of scheduled cycles for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥80% of migration cohort priorities confirmed as actionable by segment heads on monthly review. |
| Cycle | Segment migration tracking cycle reduced from quarterly recalculation to weekly automated output within 24 hours of transaction feed refresh. |

### Cohort Migration Report

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-migration-tracking/cohort-migration-report
- Lens: Automation
- Complexity: S
- Intent: Automated monthly report of segment-to-segment migration flows, with trend commentary and anomaly flags, delivered to segment heads without manual assembly.
- Problem to solve: Monthly migration reports are produced through multi-step data extraction and manual formatting, consuming one to two analyst days and often arriving late relative to the planning cycle they are meant to inform. The recurring structure — migration matrix, top-movers by direction, trend commentary — is unchanged month to month but rebuilt from scratch each time.
- Solution: The AI agent reads segment-membership snapshots from the CRM and the data warehouse, produces the migration matrix, top-mover lists, and trend commentary automatically each month, and delivers the report to segment heads. Analyst effort shifts to reviewing the output and adding forward-looking interpretation.
- OKR: A monthly segment-to-segment migration flow report with trend commentary and anomaly flags is available to segment heads on the scheduled delivery date without manual assembly.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the cohort migration report for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥80% of migration reports accepted by segment heads as the basis for segment review without supplementary data requests. |
| Cycle | Migration report production cycle reduced from one to two analyst days of manual data extraction and formatting to ≤24 hours of automated assembly. |

### Segment Migration Financial Impact

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-migration-tracking/segment-migration-financial-impact
- Lens: Insights
- Complexity: M
- Intent: The AI agent quantifies the revenue and margin impact of segment migration flows each quarter, translating customer-count migration matrices into their P&L consequence for commercial leadership planning.
- Problem to solve: Segment migration reporting tracks customer-count flows but not their financial significance. A migration matrix showing 200 customers moving from emerging-affluent to mass-retail is not actionable without the revenue and margin context: those 200 customers may represent 8% of the retail margin base. Commercial leadership cannot prioritize retention and re-engagement programs without knowing which migration flows have the greatest financial consequence.
- Solution: The AI agent reads segment-migration data alongside per-customer revenue and margin records, computes the financial impact of each migration flow — revenue at risk from downward migration, incremental revenue from upward migration — and produces a quarterly financial-impact brief. Commercial leadership directs retention and growth investment to the highest-impact migration flows.
- OKR: Commercial leadership receives a quarterly financial-impact brief that translates segment-migration flows into revenue at risk from downward migration and incremental revenue from upward migration.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the financial-impact brief for ≥90% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live, covering all migration flows in the matrix. |
| Acceptance | ≥80% of briefs accepted by commercial leadership as the basis for retention and growth investment prioritization; impact estimates reconciled to per-customer revenue and margin records within ±10%. |
| Cycle | Financial quantification of migration flows moved from not produced to a quarterly brief within 2 weeks of quarter close. |

## Needs-based segmentation {#needs-based-segmentation}

Clustering customers by financial-need profile — savings behavior, credit appetite, investment intent, protection gaps — independent of current product ownership. Needs-based segments identify where a bank's product set matches declared or inferred customer intent and where gaps create opportunity or attrition risk. Where survey response rates are low, needs-based segmentation is harder to build; inference from transaction patterns and digital behavior becomes the primary source.

### Needs-Product Coverage Gap Report

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/needs-based-segmentation/needs-product-coverage-gap-report
- Lens: New opps
- Complexity: S
- Intent: The AI agent maps each inferred needs-based segment to the Bank's current product set, identifying segments whose primary financial need is not addressed by any available product and sizing the addressable revenue gap.
- Problem to solve: Needs-based segment definitions identify customer groups by financial-need profile but are not systematically mapped to the Bank's product eligibility and feature set. A needs segment classified as protection-gap — customers with no insurance product and significant savings balance — may not be covered by any current product in the Bank's retail offer, creating an opportunity that remains unquantified and unactioned.
- Solution: The AI agent reads inferred needs-based segment definitions and the Bank's product eligibility register, maps each segment's primary need to the current product set, and identifies coverage gaps where no product addresses the primary need. For each gap, the AI agent sizes the addressable revenue opportunity based on segment size and estimated per-customer value. Product leadership uses the coverage-gap report as a quarterly input to the product development pipeline.
- OKR: Product leadership receives a quarterly coverage-gap report mapping each inferred needs-based segment to the current product set, identifying primary needs that no product addresses and sizing the addressable revenue of each gap.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the coverage-gap report for ≥90% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live, covering all needs-based segments. |
| Acceptance | ≥70% of identified coverage gaps confirmed as valid by product leadership; ≥1 gap per year taken into the product development pipeline. |
| Cycle | Needs-to-product coverage mapping moved from not performed to a quarterly report available before each product pipeline review. |

### Needs-Cluster Inference

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/needs-based-segmentation/needs-cluster-inference
- Lens: New opps
- Complexity: M
- Intent: The AI agent infers latent financial-need clusters from transaction patterns and digital behavior, surfacing the top unmet-need segments for product and marketing prioritization.
- Problem to solve: Needs-based segmentation often depends on survey data with low response rates or on commissioned research that becomes stale on arrival. The inferred-needs signal available in transaction and digital-behavior logs goes largely unused, and product teams design for the average customer rather than identified need profiles.
- Solution: The AI agent clusters customers by inferred financial-need profile using transaction patterns, digital-touchpoint sequences, and product-ownership gaps. The top clusters are named and sized; each quarter the product and marketing leads receive a ranked list of unmet-need segments with illustrative profiles and addressable revenue estimates.
- OKR: Latent financial-need clusters inferred from transaction patterns and digital behavior are available to the product and marketing leads on the quarterly scheduled cadence, surfacing the top unmet-need segments for prioritization.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the needs-cluster inference output for ≥90% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live. |
| Acceptance | ≥70% of identified unmet-need clusters confirmed as commercially actionable by the product and marketing leads on quarterly review. |
| Cycle | Needs-cluster inference cycle reduced from annual research commissioning to quarterly automated production within 1 week of transaction data refresh. |

### Needs Segment Transaction Inference

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/needs-based-segmentation/needs-segment-transaction-inference
- Lens: Insights
- Complexity: M
- Intent: The AI agent infers financial-need profiles from transaction patterns and digital-behavior signals monthly, classifying the customer base into needs-based segments for product and pricing prioritization without reliance on survey data.
- Problem to solve: Needs-based segmentation often depends on survey data with low response rates. Transaction and digital-behavior signals — inbound payment sources, savings balance trajectories, credit utilization patterns, and insurance premium payments — contain the same need signals at full population coverage, but are not used systematically to construct needs-based segments between commissioned research cycles.
- Solution: The AI agent reads transaction patterns, digital-touchpoint sequences, and product-ownership records monthly, applies a needs-inference model to classify customers into financial-need profiles — savings-intent, credit-active, protection-gap, investment-oriented — and produces a segment-size and composition report. Product and marketing teams use the inference-based segments as the standing needs view between commissioned research cycles.
- OKR: The customer base is classified into needs-based segments each month from transaction patterns and digital-behavior signals, giving product and marketing teams a standing needs view between commissioned research cycles.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent runs the needs-inference classification and delivers the segment-size and composition report for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live, covering the full active base. |
| Acceptance | ≥75% of inferred segment profiles confirmed as consistent with the most recent commissioned research by product and marketing leads on quarterly review. |
| Cycle | Needs-based segment refresh cycle reduced from commissioned-research intervals to monthly production within 1 week of month close. |

## Risk-tier segmentation {#risk-tier-segmentation}

Segmenting the customer base by credit risk, fraud propensity, or conduct-risk profile — the analytical layer that governs credit appetite, limit-setting, and compliance monitoring at the individual and segment level. Under prudential requirements for consumer credit, risk tiers underpin the PD/LGD parameters used in provisioning and pricing. As the portfolio composition shifts with new originations, risk tiers must be refreshed to avoid silent drift in the aggregate risk profile.

### Risk-Tier Monitoring Report

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/risk-tier-segmentation/risk-tier-segmentation-monitoring-report
- Lens: Automation
- Complexity: S
- Intent: Automated monthly report of risk-tier distribution, migration flows, and PD trend by tier, produced from core banking and bureau data without manual extraction for review by the credit risk committee.
- Problem to solve: The credit risk committee receives risk-tier distribution and PD trend data assembled by the analytics team from multiple source extracts, taking two to three analyst days per reporting cycle. The standard structure — tier distribution, net migration matrix, PD trend per tier — is unchanged each month but rebuilt manually, delaying the credit risk committee pack.
- Solution: The AI agent reads core banking portfolio data and bureau updates, computes tier distribution and net migration matrix, tracks PD trend per tier, and produces the standard monthly report for the credit risk committee. Credit risk analysts review the output and add forward-looking commentary; the data-assembly effort is eliminated.
- OKR: The credit risk committee receives the standard monthly risk-tier report — tier distribution, net migration matrix, and PD trend per tier — produced from core banking and bureau data without manual extraction.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the risk-tier monitoring report for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥90% of reports accepted by credit risk analysts for the committee pack without data correction; figures reconciled to core banking portfolio totals in every cycle. |
| Cycle | Report assembly reduced from two to three analyst days per cycle to ≤2 hours of analyst review and commentary. |

### Portfolio Risk-Tier Refresh

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/risk-tier-segmentation/portfolio-risk-tier-refresh
- Lens: Insights
- Complexity: M
- Intent: The AI agent refreshes risk-tier classifications across the full retail and SME portfolio monthly, surfacing tier migration patterns and the segments with the greatest concentration risk drift for credit and pricing review.
- Problem to solve: Risk-tier assignments are recalculated at origination and at annual credit review. Between reviews, the portfolio accumulates drift — customers whose risk profile has deteriorated or improved remain in their prior tier, and limit-setting and pricing decisions that depend on tier membership are based on outdated classifications. Concentration risk in the highest-risk tier is visible only when the annual refresh completes.
- Solution: The AI agent reads payment behavior, bureau updates where available, and account-activity signals monthly, recalculates risk-tier membership for the full retail and SME book, and produces a drift report showing net tier movements and concentration changes. Credit risk and pricing teams review the refreshed tier distribution before the next pricing or limit-setting cycle.
- OKR: Risk-tier membership for the full retail and SME book is recalculated monthly, with a drift report of net tier movements and concentration changes available to credit risk and pricing teams before each pricing or limit-setting cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent completes the monthly risk-tier recalculation and drift report for ≥95% of scheduled cycles for ≥12 consecutive months post go-live, covering the full retail and SME portfolio. |
| Acceptance | ≥85% of tier movements in the drift report confirmed as valid by credit risk on sampled review; refreshed tiers used in ≥90% of pricing and limit-setting cycles. |
| Cycle | Risk-tier refresh cycle reduced from origination and annual credit review to monthly recalculation. |

### Fraud Propensity Tier Overlay

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/risk-tier-segmentation/fraud-propensity-tier-overlay
- Lens: Insights
- Complexity: M
- Intent: The AI agent overlays a fraud-propensity score on the risk-tier classification, identifying customers where credit risk tier and fraud propensity are misaligned and where the combined risk profile warrants limit review.
- Problem to solve: Credit risk tier and fraud propensity are managed by separate models and separate teams. A customer can be in the lowest credit risk tier — prime, low PD — while exhibiting elevated fraud-propensity signals. The Bank's limit-setting and authentication treatment does not account for this combination, leaving a gap in the aggregate risk view.
- Solution: The AI agent reads credit risk tier assignments and fraud-propensity model scores, flags customers where the two signals diverge materially, and produces a combined-risk review list ranked by the gap size. Limits and authentication treatment for flagged customers are reviewed by the credit and fraud risk functions jointly.
- OKR: The credit and fraud risk functions receive a combined-risk review list — customers whose credit risk tier and fraud-propensity score diverge materially, ranked by gap size — as the basis for joint review of limits and authentication treatment.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the combined-risk review list for ≥95% of scheduled refresh cycles for ≥12 consecutive months post go-live, covering all customers with both a risk tier and a fraud-propensity score. |
| Acceptance | ≥70% of flagged customers confirmed as warranting limit or authentication review by the credit and fraud risk functions on joint review. |
| Cycle | Combined credit-and-fraud risk view moved from not produced, with the two models managed separately, to a ranked review list within 5 business days of each model refresh. |
