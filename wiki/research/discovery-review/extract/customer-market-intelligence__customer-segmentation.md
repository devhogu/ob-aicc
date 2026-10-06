# 

source: html-alt/financial-services/en/customer-market-intelligence/customer-segmentation/index.html


[PAGE TEXT]
Behavioural segmentation
Classification of the customer base by observed transaction patterns, channel use, and product activity — the primary basis for propensity scoring and next-best-action prioritisation. Behavioural segments shift continuously as customer activity evolves, but most banks refresh them quarterly or annually. Under NBK and NBKR customer-profiling guidelines, behavioural segmentation feeds AML transaction monitoring and retail credit scoring overlays.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] Digital Behaviour Cluster Analysis
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/behavioural-segmentation/digital-behaviour-cluster-analysis
intent: Agent clusters customers by digital-channel interaction patterns monthly, producing named behavioural archetypes and their size for product and channel investment decisions.
Problem to solve: Digital behaviour data — app session frequency, feature-use patterns, self-service versus assisted-channel mix — is captured in analytics platforms but not connected to CRM segment definitions. Channel investment decisions and digital product prioritisation proceed without a systematic view of which behavioural archetypes represent the largest and most commercially relevant customer groups.
Solution: Agent reads app and digital-channel interaction logs, clusters customers by interaction pattern, names the top archetypes by feature-use and channel-mix profile, and sizes each cohort. Product and channel teams receive a monthly archetype report; segment definitions are updated to incorporate the digital-behaviour dimension.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Insights|S] Transaction Pattern Anomaly Flag
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/behavioural-segmentation/transaction-pattern-anomaly-flag
intent: Agent identifies customers whose transaction patterns have diverged materially from their segment baseline, flagging both outliers for AML review and commercial opportunities for relationship-manager follow-up.
Problem to solve: Segment-baseline transaction patterns are used for AML monitoring thresholds but the comparison is run on static annual baselines. Customers whose patterns shift gradually but persistently — a growing cash-withdrawal pattern in a salary-account holder, or a new inbound payment source — drift outside their segment norm without triggering the threshold review that annual baselines require.
Solution: Agent computes a rolling segment baseline from the prior 90 days and flags customers whose current-week transaction pattern deviates beyond a statistical threshold. AML receives a prioritised review list; commercial teams receive a separate flag for customers showing positive engagement uplift above segment norm.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Insights|M] Behavioural Segment Refresh
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/behavioural-segmentation/behavioural-segment-refresh
intent: Agent recalculates behavioural segment membership from transaction and channel-use data on a fortnightly cadence, surfacing the customers who have migrated across tiers since the last cycle for commercial and compliance review.
Problem to solve: Behavioural segments are refreshed quarterly. Customers who shift transaction patterns — salary-account holders who start using a competitor for daily spend, or dormant customers who re-engage — remain in their prior segment for up to three months. AML monitoring overlays and propensity models built on stale segment labels produce alerts and targeting errors.
Solution: Agent reads transaction, channel, and product-activity logs fortnightly, recalculates behavioural segment membership for the full active base, and produces a migration report showing net moves per tier. Compliance and commercial teams receive updated segment assignments; AML monitoring and propensity models consume the refreshed labels.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Segment-to-product mapping
Translation of segment definitions into product eligibility, pricing tiers, and feature prioritisation — the operating mechanism by which segmentation drives commercial decisions. When segment membership is refreshed faster than product mapping, the two fall out of sync and campaigns target the wrong population. In multi-product banking contexts, the mapping must cover credit, deposits, cards, insurance, and digital service tiers simultaneously.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] Segment-Product Eligibility Sync
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-to-product-mapping/segment-product-eligibility-sync
intent: Agent validates alignment between segment-membership updates and product-eligibility assignments weekly, flagging mismatches where a customer's segment has changed but their product eligibility has not been updated.
Problem to solve: Segment membership is refreshed on a faster cadence than product eligibility assignment. When a customer migrates from the mass-retail tier to the emerging-affluent tier, the product eligibility update that unlocks investment or premium card products is triggered only in the next manual mapping review — weeks later. Campaigns and digital journeys present the customer with out-of-date product offers.
Solution: Agent reads the segment-membership snapshot and the product-eligibility register each week, identifies mismatches where segment has changed but eligibility has not updated, and produces a correction queue for the product operations team. Digital journeys and campaign targeting consume the refreshed eligibility data within 48 hours of the segment update.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Insights|M] Segment Pricing-Tier Mapping Review
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-to-product-mapping/segment-pricing-tier-mapping-review
intent: Agent analyses the relationship between segment membership and pricing-tier assignment across credit, deposit, and fee products, identifying where pricing tiers are out of step with segment economics for a pricing-committee review.
Problem to solve: Pricing tiers are set at product level with reference to segment definitions, but the two are not systematically compared after initial setting. As segment membership evolves — an affluent retail cohort grows while the mass-retail cohort shrinks — the pricing tiers that were calibrated on a prior segment mix become misaligned with current segment economics, leaving margin on the table or creating over-pricing exposure in regulated retail products.
Solution: Agent reads segment-membership distribution and pricing-tier assignment across credit, deposit, and fee products quarterly, computes the margin impact of pricing-tier misalignment by segment, and produces a ranked list of adjustment opportunities for the pricing committee. Pricing-tier adjustments are evaluated against segment economics rather than legacy precedent.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Insights|M] Segment Feature Demand Mapping
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-to-product-mapping/segment-feature-demand-mapping
intent: Agent maps inferred product-feature demand by segment from usage patterns and VoC data, identifying where the current feature set has demand gaps that the product roadmap has not addressed.
Problem to solve: Product roadmap prioritisation is informed by stakeholder input and NPS scores but not by a systematic mapping of feature demand to segment. Segments with high wallet-share potential but low NPS expression — SME micro, rural retail — have their feature needs under-represented in the prioritisation process, and the product roadmap concentrates development on the most vocal segments.
Solution: Agent reads product-feature usage patterns, NPS verbatims, complaint themes, and app-review content, infers feature-demand signals by segment, and produces a demand-gap map showing which segments are most under-served by the current feature set. Product leadership uses the map as a quarterly roadmap input alongside stakeholder proposals.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Value-based segmentation
Grouping customers by economic contribution — actual and potential — typically expressed as revenue per customer, product penetration, or risk-adjusted margin. Value tiers set the service model, relationship investment, and retention priority: a bank that cannot identify its top-decile by current value misallocates relationship-manager capacity. In KZ and KG banking markets, value segmentation must account for the concentration of high-value flows in a small proportion of the retail salary-account base.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] Top-Decile Revenue Concentration Report
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/value-based-segmentation/top-decile-revenue-concentration-report
intent: Automated monthly report of revenue concentration in the top value tiers — top 1%, top 5%, top 10% — with trend commentary, delivered to retail and commercial leadership without manual data assembly.
Problem to solve: Revenue concentration in the top customer tiers is tracked annually. Commercial leadership cannot see in-year changes in concentration — whether the top decile is becoming more or less concentrated — without commissioning a custom analysis. Monthly board packs carry aggregate revenue numbers but not the distribution-level view that informs service-model decisions.
Solution: Agent reads customer-level revenue and margin data monthly, computes concentration metrics for the top 1%, 5%, and 10% value tiers, and produces a monthly report with trend commentary. Commercial and retail leadership receive the concentration view monthly as part of the standard management pack.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Insights|S] High-Value Attrition Early Warning
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/value-based-segmentation/high-value-attrition-early-warning
intent: Agent monitors top-decile customers for early-stage disengagement signals weekly, surfacing at-risk high-value customers before they appear in the standard at-risk scoring model.
Problem to solve: The standard at-risk scoring model is calibrated on the full active base and uses thresholds appropriate for the median customer. High-value customers, who typically have lower transaction frequency and a more concentrated product footprint, can exhibit meaningful disengagement — declining balance trend, reduced transaction frequency, unused credit facilities — without crossing the standard model's threshold for weeks.
Solution: Agent applies a high-value-specific attrition signal framework to the top-decile customer list weekly, using tighter thresholds calibrated on prior high-value churn patterns. Relationship managers receive a weekly list of top-decile customers showing early-stage disengagement signals, enabling contact ahead of the standard at-risk model alert.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Insights|M] Value-Tier Classification
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/value-based-segmentation/value-tier-classification
intent: Agent calculates risk-adjusted revenue contribution per customer quarterly, classifies the base into value tiers, and produces a tier-migration report showing which customers have moved into or out of the top decile since the prior quarter.
Problem to solve: Value-tier classification is produced annually for strategic planning and used to set relationship-manager portfolio composition targets. Customers who move into the top value decile during the year — a retail customer who starts salary crediting or an SME that draws on a credit facility — are not reclassified until the annual refresh, and relationship-manager assignment does not adjust to reflect the commercial priority shift.
Solution: Agent reads revenue, product-holding, and margin data quarterly, computes risk-adjusted revenue contribution per customer, classifies the base into value tiers, and produces a migration report. Relationship-manager assignments and service-model decisions are updated to reflect the current-quarter tier classification rather than the prior-year model.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Segment migration tracking
Systematic monitoring of customer movement across segment definitions over time — the feedback loop that validates whether retention programmes and product interventions are working as intended. Migration rates are a leading indicator of segment health: rapid downward migration in a value tier signals a structural problem before it surfaces in revenue or NPS data. OECD guidelines on fair-lending monitoring require that risk-tier migration trends are tracked and reported at the portfolio level.
Lens
Scenario
Intent
Complexity

### CARD 10 [Insights|S] Segment Migration Tracker
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-migration-tracking/segment-migration-tracker
intent: Agent recalculates segment membership from transaction and behaviour feeds on a weekly cadence, ranking migration cohorts by commercial priority for segment heads.
Problem to solve: Segment membership is recalculated quarterly. Customers migrating across value or behavioural tiers are identified retrospectively, after the commercial window has passed. High-value customers in early-stage downgrade are the last to be flagged.
Solution: Agent reads transaction and behaviour feeds weekly, recalculates segment membership, and ranks migration cohorts — high-value downgraders, emerging mid-tier, re-engaged dormant — by commercial priority. Segment heads receive a weekly migration brief with recommended action by cohort.
OKR objective: Segment membership is recalculated from transaction and behaviour feeds weekly, with migration cohorts ranked by commercial priority and available to segment heads at each review cycle — replacing monthly batch recalculation.
OKR KR [Adoption]: Agent produces the weekly segment migration ranking for ≥95% of scheduled cycles for ≥48 consecutive weeks post go-live.
OKR KR [Acceptance]: ≥80% of migration cohort priorities confirmed as actionable by segment heads on monthly review.
OKR KR [Cycle]: Segment migration tracking cycle reduced from monthly batch recalculation to weekly automated output within 24 hours of transaction feed refresh.

### CARD 11 [Automation|S] Cohort Migration Report
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-migration-tracking/cohort-migration-report
intent: Automated monthly report of segment-to-segment migration flows, with trend commentary and anomaly flags, delivered to segment heads without manual assembly.
Problem to solve: Monthly migration reports are produced through multi-step data extraction and manual formatting, consuming one to two analyst days and often arriving late relative to the planning cycle they are meant to inform. The recurring structure — migration matrix, top-movers by direction, trend commentary — is unchanged month to month but rebuilt from scratch each time.
Solution: Agent reads segment-membership snapshots from CRM and data warehouse, produces the migration matrix, top-mover lists, and trend commentary automatically each month, and delivers the report to segment heads. Analyst effort shifts to reviewing the output and adding forward-looking interpretation.
OKR objective: A monthly segment-to-segment migration flow report with trend commentary and anomaly flags is available to segment heads on the scheduled delivery date without manual assembly.
OKR KR [Adoption]: Agent delivers the cohort migration report for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live.
OKR KR [Acceptance]: ≥80% of migration reports accepted by segment heads as the basis for segment review without supplementary data requests.
OKR KR [Cycle]: Migration report production cycle reduced from 5–7 days of manual data extraction and commentary drafting to ≤24 hours of automated assembly.

### CARD 12 [Enablement|M] Segment Migration Financial Impact
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/segment-migration-tracking/segment-migration-financial-impact
intent: Agent quantifies the revenue and margin impact of segment migration flows each quarter, translating customer-count migration matrices into their P&L consequence for commercial leadership planning.
Problem to solve: Segment migration reporting tracks customer-count flows but not their financial significance. A migration matrix showing 200 customers moving from emerging-affluent to mass-retail is not actionable without the revenue and margin context: those 200 customers may represent 8% of the retail margin base. Commercial leaders cannot prioritise retention and re-engagement programmes without knowing which migration flows have the greatest financial consequence.
Solution: Agent reads segment-migration data alongside per-customer revenue and margin records, computes the financial impact of each migration flow — revenue at risk from downward migration, incremental revenue from upward migration — and produces a quarterly financial-impact brief. Commercial leadership directs retention and growth investment to the highest-impact migration flows.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Needs-based segmentation
Clustering customers by financial-need profile — savings behaviour, credit appetite, investment intent, protection gaps — independent of current product ownership. Needs-based segments identify where the bank's product set matches declared or inferred customer intent and where gaps create opportunity or attrition risk. In CIS banking markets, needs-based segmentation is complicated by low survey response rates; inference from transaction patterns and digital behaviour is the primary source.
Lens
Scenario
Intent
Complexity

### CARD 13 [Enablement|S] Needs-Product Coverage Gap Report
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/needs-based-segmentation/needs-product-coverage-gap-report
intent: Agent maps each inferred needs-based segment to the bank's current product set, identifying segments whose primary financial need is not addressed by any available product and sizing the addressable revenue gap.
Problem to solve: Needs-based segment definitions identify customer groups by financial-need profile but are not systematically mapped to the bank's product eligibility and feature set. A needs segment classified as protection-gap — customers with no insurance product and significant savings balance — may not be covered by any current product in the bank's retail offer, creating an opportunity that remains unquantified and unactioned.
Solution: Agent reads inferred needs-based segment definitions and the bank's product eligibility register, maps each segment's primary need to the current product set, and identifies coverage gaps where no product addresses the primary need. For each gap, the agent sizes the addressable revenue opportunity based on segment size and estimated per-customer value. Product leadership uses the coverage-gap report as a quarterly input to the product development pipeline.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 14 [New opps|M] Needs-Cluster Inference
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/needs-based-segmentation/needs-cluster-inference
intent: Agent infers latent financial-need clusters from transaction patterns and digital behaviour, surfacing the top unmet-need segments for product and marketing prioritisation.
Problem to solve: Needs-based segmentation in CIS markets depends on survey data with low response rates or commissioned research that becomes stale on arrival. The inferred-needs signal available in transaction and digital-behaviour logs goes largely unused, and product teams design for the average customer rather than identified need profiles.
Solution: Agent clusters customers by inferred financial-need profile using transaction patterns, digital-touchpoint sequences, and product-ownership gaps. The top clusters are named and sized; the product team receives a ranked list of unmet-need segments with illustrative profiles and addressable revenue estimates.
OKR objective: Latent financial-need clusters inferred from transaction patterns and digital behaviour are available to product and marketing leadership on the quarterly scheduled cadence, surfacing the top unmet-need segments for prioritisation.
OKR KR [Adoption]: Agent produces the needs-cluster inference output for ≥90% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live.
OKR KR [Acceptance]: ≥70% of identified unmet-need clusters confirmed as commercially actionable by the product and marketing leads on quarterly review.
OKR KR [Cycle]: Needs-cluster inference cycle reduced from annual research commissioning to quarterly automated production within 1 week of transaction data refresh.

### CARD 15 [Insights|M] Needs Segment Transaction Inference
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/needs-based-segmentation/needs-segment-transaction-inference
intent: Agent infers financial-need profiles from transaction patterns and digital-behaviour signals monthly, classifying the customer base into needs-based segments for product and pricing prioritisation without reliance on survey data.
Problem to solve: Needs-based segmentation in CIS markets depends on survey data with low response rates. Transaction and digital-behaviour signals — inbound payment sources, savings balance trajectories, credit utilisation patterns, and insurance premium payments — contain the same need signals at full population coverage, but are not used systematically to construct needs-based segments between commissioned research cycles.
Solution: Agent reads transaction patterns, digital-touchpoint sequences, and product-ownership records monthly, applies a needs-inference model to classify customers into financial-need profiles — savings-intent, credit-active, protection-gap, investment-oriented — and produces a segment-size and composition report. Product and marketing teams use the inference-based segments as the standing needs view between commissioned research cycles.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Risk-tier segmentation
Segmenting the customer base by credit risk, fraud propensity, or conduct-risk profile — the analytical layer that governs credit appetite, limit-setting, and compliance monitoring at the individual and segment level. Under NBKR and NBK/ARDFM consumer-credit regulations, risk tiers underpin the PD/LGD parameters used in provisioning and pricing. As the portfolio composition shifts with new originations, risk tiers must be refreshed to avoid silent drift in the aggregate risk profile.
Lens
Scenario
Intent
Complexity

### CARD 16 [Automation|S] Risk-Tier Monitoring Report
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/risk-tier-segmentation/risk-tier-segmentation-monitoring-report
intent: Automated monthly report of risk-tier distribution, migration flows, and PD trend by tier, produced from core banking and bureau data without manual extraction for credit-risk committee review.
Problem to solve: The credit risk committee receives risk-tier distribution and PD trend data assembled by the analytics team from multiple source extracts, taking two to three analyst days per reporting cycle. The standard structure — tier distribution, net migration matrix, PD trend per tier — is unchanged each month but rebuilt manually, delaying the credit risk committee pack.
Solution: Agent reads core banking portfolio data, computes tier distribution and net migration matrix, tracks PD trend per tier, and produces the standard monthly credit-risk committee report. Credit risk analysts review the output and add forward-looking commentary; the data-assembly effort is eliminated.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 17 [Insights|M] Portfolio Risk-Tier Refresh
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/risk-tier-segmentation/portfolio-risk-tier-refresh
intent: Agent refreshes risk-tier classifications across the full retail and SME portfolio monthly, surfacing tier migration patterns and the segments with the greatest concentration risk drift for credit and pricing review.
Problem to solve: Risk-tier assignments are recalculated at origination and at annual credit review. Between reviews, the portfolio accumulates drift — customers whose risk profile has deteriorated or improved remain in their prior tier, and limit-setting and pricing decisions that depend on tier membership are based on outdated classifications. Concentration risk in the highest-risk tier is visible only when the annual refresh completes.
Solution: Agent reads payment behaviour, bureau updates where available, and account-activity signals monthly, recalculates risk-tier membership for the full retail and SME book, and produces a drift report showing net tier movements and concentration changes. Credit risk and pricing teams review the refreshed tier distribution before the next pricing or limit-setting cycle.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 18 [Insights|M] Fraud Propensity Tier Overlay
urn: urn:financial-services:scenario:customer-market-intelligence/customer-segmentation/risk-tier-segmentation/fraud-propensity-tier-overlay
intent: Agent overlays a fraud-propensity score on the risk-tier classification, identifying customers where credit risk tier and fraud propensity are misaligned and where the combined risk profile warrants limit review.
Problem to solve: Credit risk tier and fraud propensity are managed by separate models and separate teams. A customer can be in the lowest credit risk tier — prime, low PD — while exhibiting elevated fraud-propensity signals. The bank's limit-setting and authentication treatment does not account for this combination, leaving a gap in the aggregate risk view.
Solution: Agent reads credit risk tier assignments and fraud-propensity model scores, flags customers where the two signals diverge materially, and produces a combined-risk review list ranked by the gap size. Limits and authentication treatment for flagged customers are reviewed by the credit and fraud risk functions jointly.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
