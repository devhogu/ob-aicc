# 

source: html-alt/financial-services/en/customer-market-intelligence/wallet-share/index.html


[PAGE TEXT]
Primary bank relationship share
The proportion of customers for whom the bank is the primary financial-services provider — defined by salary crediting, main transaction account, or majority-wallet relationship. Primary relationship depth is the most important single indicator of wallet share: primary-bank customers have three to five times the revenue potential of secondary-bank customers. In KZ and KG markets, primary relationship is typically defined by the salary-crediting account, which concentrates competitive vulnerability at payroll-cycle moments.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] Primary Relationship Migration Monitor
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/primary-bank-relationship-share/primary-relationship-migration-monitor
intent: Automated monthly report of movements between primary and secondary relationship tiers, showing the net change in primary-bank share and the segments where migration is most active.
Problem to solve: Primary-bank share is measured annually in commissioned customer research. In-year movements — customers migrating from primary to secondary following a competitor salary-account campaign, or secondary customers upgrading after a new product offer — are not tracked. Commercial leadership cannot see whether primary-bank share is improving or declining during the year, reducing the responsiveness of the commercial programme.
Solution: Agent reads the monthly primary-bank classification output, computes net tier migration flows, and produces a month-on-month primary-relationship monitor. Commercial leadership receives the migration report monthly; the annual commissioned research becomes a validation of the in-year signal rather than the sole measurement of primary-bank share.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Insights|S] Salary-Switch Risk Alert
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/primary-bank-relationship-share/salary-switch-risk-alert
intent: Agent identifies customers showing salary-crediting disruption signals — missed or reduced salary credits, new inbound payments from a competing institution — and surfaces them as salary-switch risk for priority retention outreach ahead of the payroll-cycle moment.
Problem to solve: Salary-crediting is the most important primary-bank signal in KZ and KG retail banking. A customer who switches salary crediting to a competitor represents an immediate and material wallet-share loss. The switch decision typically happens at an HR payroll-change moment and is irreversible within the quarter. The bank currently identifies salary-switch exits after the first missed salary credit — at the point of loss, not before.
Solution: Agent monitors salary-credit patterns for all primary-bank customers weekly, flags customers showing pre-switch signals — credit amount declining over two consecutive cycles, new competitive inbound appearing alongside the salary credit — and produces a priority alert list. Relationship managers receive the salary-switch risk alert at least one payroll cycle before the likely switch date.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Insights|M] Primary-Bank Identification Model
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/primary-bank-relationship-share/primary-bank-identification-model
intent: Agent classifies the active customer base into primary-bank and secondary-bank relationships monthly, using salary-credit patterns, transaction volume share, and product depth as classification signals, and surfaces the secondary-bank cohort as the primary wallet-share growth opportunity.
Problem to solve: Primary-bank relationship status is not classified systematically. Commercial teams know that salary-crediting is the strongest primary-bank signal, but customers without salary crediting whose main transaction account is with the bank are not identified, and customers with salary crediting who have migrated their primary spend to a competitor card are not flagged. The commercial opportunity in each relationship tier is invisible without explicit classification.
Solution: Agent reads salary-credit events, transaction volume, inbound payment sources, and product-depth data monthly, classifies each active customer as primary-bank, probable-primary, secondary-bank, or transactional-only, and produces a classification report with the wallet-share opportunity sized per tier. Commercial teams prioritise secondary-bank customers with high CLV as the first wallet-share growth cohort.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Cross-sell opportunity identification
Systematic identification of customers with a high probability of accepting a specific product offer — based on their current product profile, financial behaviour, and CLV tier. Cross-sell opportunity identification is the commercial application of segmentation, CLV, and wallet-share estimation: the output is a ranked, actionable list of customer-product opportunities for commercial teams. In CIS banking markets, the highest cross-sell opportunity concentrations are in salary-account holders without a retail credit product and SME transactional-account holders without a trade-finance product.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] Cross-Sell Campaign Performance Report
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/cross-sell-opportunity-identification/cross-sell-campaign-performance-report
intent: Automated monthly report of cross-sell campaign conversion rates, product-take-up by segment, and wallet-share impact, delivered to commercial leadership without manual extraction from campaign management and CRM systems.
Problem to solve: Cross-sell campaign performance is assembled from campaign management tool exports, CRM contact records, and core banking product-opening data — three systems with different identifiers that require manual matching. The monthly performance report takes two to three analyst days to produce and arrives in the commercial review cycle late, limiting its influence on the following month's campaign design.
Solution: Agent reads campaign contact records, offer details, and product-opening events from source systems, matches by customer identifier, computes conversion rates by segment and product, and produces the standard monthly campaign performance report. Commercial leadership reviews the agent-generated output; campaign design for the following month references the performance data within one week of month close.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [New opps|M] Next-Best-Offer Prioritisation
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/cross-sell-opportunity-identification/next-best-offer-prioritisation
intent: Agent scores the customer base weekly for product-specific cross-sell propensity, producing a ranked next-best-offer list for campaign execution and relationship-manager queues.
Problem to solve: Cross-sell targeting is produced through periodic campaign planning cycles. Customers who become cross-sell eligible between campaigns — a salary-account holder who completed three consecutive months of payroll crediting — are missed until the next campaign cycle, and eligibility signals decay before they are acted on.
Solution: Agent reads product-ownership, transaction-behaviour, and eligibility-signal data weekly, scores each customer for cross-sell propensity by product, and produces a ranked next-best-offer list. Campaign teams execute against the weekly list; relationship managers receive their individual customer queue, and offer eligibility is always current.
OKR objective: A weekly ranked next-best-offer list — scored for product-specific cross-sell propensity across the active customer base — is available for campaign execution and relationship-manager queues.
OKR KR [Adoption]: Agent produces the next-best-offer ranked list for ≥95% of weekly scoring cycles for ≥48 consecutive weeks post go-live.
OKR KR [Acceptance]: ≥75% of top-ranked offers confirmed as appropriate for the targeted segment by the campaign lead on weekly review; cross-sell conversion rate tracked as primary outcome metric.
OKR KR [Cycle]: Next-best-offer scoring cycle reduced from monthly batch campaign production to weekly automated ranked output.

### CARD 6 [Insights|M] Propensity Model Cross-Sell Insights
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/cross-sell-opportunity-identification/propensity-model-cross-sell-insights
intent: Agent analyses the product-acceptance and product-decline patterns from the prior six months to identify the propensity signals most predictive of cross-sell conversion, and produces a model-insight brief for the data science and commercial teams.
Problem to solve: Cross-sell propensity models are built and validated at initial deployment. The signals that were predictive at build time may decay as customer behaviour evolves — a signal that predicted credit card acceptance at salary crediting three years ago may be less predictive now that the digital-channel onboarding journey has changed. Model-insight reviews are conducted only at the annual model rebuild and do not reflect in-year signal drift.
Solution: Agent reads product-acceptance and decline outcomes from the prior six months, analyses which propensity signals at the point of offer are most correlated with acceptance in the current customer base, and produces a model-insight brief showing signal importance rankings and the direction of any drift from the model's original calibration. The data science team uses the brief to prioritise the next model-refresh cycle.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Product penetration depth
The number of active product categories held per customer, and the distribution of that depth across the customer base — the structural measure of wallet share within the bank's own product set. Deep penetration (three or more product categories per customer) is the strongest predictor of retention and CLV. Under-penetrated customers — holding only a salary account or a single credit product — represent the highest wallet-share upside for cross-sell programmes. Product penetration analysis by segment reveals which combinations have the highest retention and revenue effects.
Lens
Scenario
Intent
Complexity

### CARD 7 [Insights|S] Penetration Gap Analysis
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/product-penetration-depth/penetration-gap-analysis
intent: Agent maps the product-penetration distribution across segments weekly, identifying the highest-upside cross-sell gaps by product pair and the retention correlation by penetration depth tier.
Problem to solve: Product penetration depth is reported quarterly as an aggregate statistic — average products per customer by segment. The distribution underneath — how many customers hold only one product, which product combinations correlate with retention — is not surfaced, and cross-sell programme design defaults to the same standard offer set regardless of the penetration pattern.
Solution: Agent reads product-ownership data from CRM and core banking weekly, produces a penetration-gap analysis showing the proportion of customers at each depth level per segment, the top cross-sell gaps by product pair, and the retention correlation by depth tier. Commercial and product teams use the output to prioritise cross-sell campaigns.
OKR objective: A weekly product-penetration distribution map — identifying the highest-upside cross-sell gaps by product pair and retention correlation by penetration depth tier — is available to segment heads and the commercial leadership.
OKR KR [Adoption]: Agent produces the penetration gap analysis for ≥95% of scheduled weekly cycles for ≥48 consecutive weeks post go-live.
OKR KR [Acceptance]: ≥75% of identified cross-sell gaps confirmed as priority targets by segment heads on monthly review; cross-sell penetration rate per product pair tracked as primary outcome metric.
OKR KR [Cycle]: Penetration gap analysis cycle reduced from quarterly manual cohort analysis to weekly automated production within 24 hours of segment data refresh.

### CARD 8 [Automation|S] Product Penetration Milestone Alert
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/product-penetration-depth/product-penetration-milestone-alert
intent: Agent monitors product-penetration depth across the customer base weekly, alerts relationship managers and campaign teams when a customer crosses a depth milestone — reaching a second or third active product — for timely follow-on offer sequencing.
Problem to solve: Product-penetration milestones — the moment a customer moves from one to two or from two to three active products — are strong signals for follow-on offer sequencing: retention rates and CLV increase materially at each additional product. These milestones are not monitored in real time; campaign targeting is based on the penetration-depth snapshot from the last campaign cycle, missing the window immediately after the milestone crossing.
Solution: Agent reads product-holding events weekly, identifies customers crossing penetration-depth milestones in the prior seven days, and alerts relationship managers and campaign teams with the customer's current product set and the highest-propensity next-product recommendation. Offers are sequenced within the optimal post-milestone window rather than at the next campaign cycle.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Insights|M] Product Combination Retention Analysis
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/product-penetration-depth/product-combination-retention-analysis
intent: Agent analyses historical retention rates by product combination, identifying which two- and three-product combinations produce the strongest retention and CLV, and produces a combination-ranking brief for product and commercial strategy.
Problem to solve: Cross-sell strategy targets individual product additions without a systematic view of which product combinations produce the strongest retention outcomes. Whether a salary-account plus credit-card combination retains customers materially better than salary-account plus personal loan — and by how much — is not available as a standard analytical input. Product prioritisation decisions do not differentiate by retention impact.
Solution: Agent reads product-holding history alongside 12-month retention outcomes, computes retention rates and CLV averages by product combination, ranks the top two- and three-product combinations by retention differential above the single-product baseline, and produces the combination-ranking brief. Product and commercial strategy uses the ranking to sequence cross-sell programme priorities toward the highest-retention combinations.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Competitor-held share estimation
Inference of the proportion of a customer's financial wallet held by competing institutions — inferred from transaction flow patterns, declined-competitor-offer data, and external market-share benchmarks. Competitor-held share is not directly observable but can be estimated from outbound payment flows, salary-credit channel patterns, and credit-bureau product-ownership data. Under NBKR and CBR reporting frameworks, banks with significant retail deposit books are expected to monitor primary-bank attrition as part of their funding-risk assessment.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|S] Competitor Share Movement Monitor
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/competitor-held-share-estimation/competitor-share-movement-monitor
intent: Automated monthly report of changes in estimated competitor-held share by segment, surfacing segments where competitors are gaining wallet share for commercial and strategy leadership review.
Problem to solve: Competitor-held share estimates are produced for cross-sell targeting but not tracked as a monthly trend by segment. Whether a specific competitor is gaining wallet share in the SME core segment — inferred from increasing outbound payment flows to that institution — is not visible until the annual market-share commissioned research confirms it months later.
Solution: Agent reads the monthly competitor-share inference output, computes segment-level estimates of competitor-held share and their month-on-month direction, and produces a competitor-share movement report. Commercial and strategy leadership review the monthly signal; segments showing competitor wallet-share gains receive prioritised commercial response in the following month's programme.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Enablement|S] High Competitor-Share Customer Targeting Brief
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/competitor-held-share-estimation/high-share-customer-targeting-brief
intent: Agent identifies the top-decile customers by estimated competitor-held share within each CLV tier and produces a targeting brief for relationship managers, specifying the most probable competitor-held product category and the recommended initial offer.
Problem to solve: Competitor-held share estimates exist at the portfolio level but are not used to generate individual customer targeting priorities for relationship managers. A relationship manager with a book of 200 customers cannot determine which 20 have the highest competitor-held share opportunity without running a custom query; they default to contacting the customers they know best rather than the highest-opportunity ones.
Solution: Agent reads the per-customer competitor-held share estimates and CLV tier assignments, identifies the top-decile by competitor-held share within each CLV tier, and produces a monthly targeting brief for relationship managers showing each customer's estimated competitor-held product category and the recommended first conversation offer. Relationship managers prioritise contact based on the agent-generated brief.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Insights|M] Competitor Share Inference Model
urn: urn:financial-services:scenario:customer-market-intelligence/wallet-share/competitor-held-share-estimation/competitor-share-inference-model
intent: Agent infers each customer's estimated competitor-held wallet share from outbound payment flows, salary-credit channel patterns, and credit-bureau product-ownership signals, producing a ranked opportunity list for commercial targeting.
Problem to solve: The proportion of a customer's financial wallet held by competitors is not directly observable. Commercial teams operate on the assumption that secondary-bank customers have competitor-held share but cannot quantify it per customer. Without a per-customer estimate, cross-sell prioritisation cannot distinguish a customer with 60% competitor-held share from one with 15%, even though the commercial opportunity is four times larger.
Solution: Agent reads outbound payment destinations, salary-credit source patterns, bureau product-ownership flags where available, and account-balance trend data to construct a per-customer competitor-held share estimate. Customers are ranked by estimated competitor-held share within their CLV tier, producing a cross-sell priority list ordered by wallet-share opportunity. Commercial teams focus contact capacity on the highest-opportunity cohort.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
