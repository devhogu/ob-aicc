# 

source: html-alt/financial-services/en/customer-market-intelligence/retention-churn/index.html


[PAGE TEXT]
Churn cohort analysis
Retrospective analysis of which customer cohorts have churned, at what rate, and with what pattern — the foundation for understanding which segment and product combinations have chronic retention problems. Cohort analysis by origination vintage, product bundle, and acquisition channel reveals structural retention differences that aggregate churn rates conceal. In CIS banking markets, churn cohort analysis must distinguish salary-crediting switches (high-value, swift) from product-fee-driven attrition (gradual, price-sensitive).
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] Churn Rate Automated Report
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/churn-cohort-analysis/churn-rate-automated-report
intent: Automated monthly churn-rate report by segment, product, and origination vintage — produced from core banking data without manual extraction — delivered to commercial leadership as part of the standard management pack.
Problem to solve: Monthly churn reporting requires analyst extraction from core banking and CRM systems, standardised into a consistent format, with commentary written against a template. The process takes one to two analyst days per cycle and the output structure is unchanged month to month. Late delivery of the churn report delays the commercial review meeting preparation.
Solution: Agent reads account-closure and product-exit events from core banking monthly, computes churn rates by segment, product, and origination vintage, and produces the standard management report with trend commentary. Analysts review the agent-generated output and add forward-looking commentary; the data-assembly and formatting step is eliminated.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Optimize|M] Cohort Retention and Cross-Sell Window Analysis
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/churn-cohort-analysis/cohort-retention-cross-sell-window
intent: Agent analyses product-deepening rates by cohort, segment, and tenure to identify the post-onboarding windows when cross-sell conversion probability is highest for each product category.
Problem to solve: Cross-sell campaigns are timed to product launch cycles and seasonal calendars. The windows within the customer lifecycle when each segment is most receptive to each product — inferred from cohort conversion data — are not used to sequence outreach. Off-peak contact dilutes the commercial offer without increasing reach.
Solution: Agent reads product-holding events and contact-outcome records across customer cohorts, identifying the post-onboarding windows at which conversion probability peaks by product and segment. The cross-sell programme is re-sequenced to align contact timing with conversion windows; campaign efficiency improves without increasing contact volume.
OKR objective: The post-onboarding windows of highest cross-sell conversion probability — by cohort, segment, and tenure for each product category — are available to campaign and relationship management teams from continuous cohort product-deepening analysis.
OKR KR [Adoption]: Agent refreshes the cross-sell window analysis for ≥90% of active product categories on the scheduled quarterly cadence for ≥4 consecutive quarters.
OKR KR [Acceptance]: ≥70% of recommended cross-sell windows confirmed as commercially actionable by product heads on quarterly review.
OKR KR [Cycle]: Cross-sell window identification cycle reduced from annual retrospective analysis to quarterly automated cohort output.

### CARD 3 [Insights|M] Churn Driver Attribution by Cohort
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/churn-cohort-analysis/churn-driver-attribution-by-cohort
intent: Agent attributes churn events by cohort to primary driver categories — price sensitivity, service failure, digital-competitor acquisition, salary-crediting switch — and produces a quarterly attribution report for commercial and retention strategy.
Problem to solve: Churn is tracked as a rate by segment. Why customers from specific cohorts exit — the driver rather than the rate — is understood only from exit surveys, which capture a voluntary sample of departing customers with inherent selection bias. Cohorts with high churn rates from service-failure drivers and cohorts churning due to competitor price actions require different retention responses, but the current reporting does not distinguish them.
Solution: Agent reads churn events with pre-exit behavioural signals, contact history, and where available exit-survey data, attributes each cohort's churn to primary driver categories using a classification model, and produces a quarterly attribution report. Commercial and retention teams design cohort-specific interventions based on driver attribution rather than rate alone.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Save-program design
The structured process of designing retention interventions — by cohort, trigger signal, channel, offer type, and timing — that constitute the bank's proactive churn-prevention programme. Save-programme ROI is determined by which customers are contacted, with which offer, through which channel, and at what point in the at-risk trajectory. In CIS retail banking, save-programmes typically combine a fee-waiver or rate offer with a personal outreach from a relationship manager — a combination that is effective only for high-value customers and counterproductive for lower-value cohorts.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] Save-Programme Contact Scheduler
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/save-program-design/save-programme-contact-scheduler
intent: Agent generates a weekly save-programme contact schedule from the current at-risk list, assigning each customer to the recommended intervention type, channel, and timing based on cohort brief and relationship-manager capacity constraints.
Problem to solve: Save-programme contact scheduling is performed manually by the retention operations team, who take the at-risk list, apply the cohort brief, and allocate customers to relationship managers and outreach channels while managing capacity constraints. The scheduling process takes one to two working days per week and produces a static list that is out of date by mid-week as new at-risk customers enter the scoring cycle.
Solution: Agent reads the weekly at-risk list, cohort intervention briefs, relationship-manager capacity data, and channel-capacity constraints, and generates an optimised contact schedule. Relationship managers receive their weekly queue automatically; retention operations reviews and approves the schedule rather than building it. The schedule updates when new at-risk customers enter mid-week.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Enablement|M] Save-Programme Cohort Brief
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/save-program-design/save-program-cohort-brief
intent: Agent generates a cohort-level intervention brief for each at-risk cluster, specifying recommended offer type, channel, timing, and expected save rate based on prior-cycle efficacy data.
Problem to solve: Save-programme interventions are designed once per cycle applying a standard offer set to all at-risk customers regardless of churn driver or cohort profile. Fee-waiver offers go to customers who would have stayed anyway; relationship-manager calls are allocated to price-sensitive cohorts better served by a self-service offer.
Solution: Agent reads cohort profiles, driver attribution from the at-risk model, and prior-cycle save-programme outcome data, then produces a cohort brief specifying recommended intervention type, channel, timing, and expected save rate per at-risk cluster. The save-programme team reviews and executes against cohort-specific recommendations.
OKR objective: A cohort-level intervention brief — specifying recommended offer type, channel, timing, and expected save rate from prior-cycle efficacy data — is available to the retention team at the start of each save programme cycle.
OKR KR [Adoption]: Agent generates a cohort intervention brief for ≥95% of at-risk clusters identified in each scoring cycle for ≥48 consecutive cycles post go-live.
OKR KR [Acceptance]: ≥80% of cohort intervention briefs confirmed as sufficient for programme execution by the retention team lead without supplementary manual design work.
OKR KR [Cycle]: Save programme cohort brief preparation cycle reduced from 5–7 days of manual cohort analysis and brief drafting to ≤24 hours of automated production.

### CARD 6 [Insights|M] Save-Offer Effectiveness Insights
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/save-program-design/save-offer-effectiveness-insights
intent: Agent analyses the outcomes of the prior three save-programme cycles to identify which offer types, delivery channels, and contact timings produced the highest save rates by churn driver and cohort, and produces a design brief for the next cycle.
Problem to solve: Save-programme design relies on accumulated experience and practitioner judgment. Which offer produced the best save rate for salary-switch churn in the SME segment in the last quarter, relative to the cost of the offer, is not available as a systematic analytical input. The programme is adjusted through informal observation rather than structured outcome analysis.
Solution: Agent reads save-programme contact records, offer details, cost data, and 90-day retention outcomes from the prior three cycles. It identifies offer-channel-timing combinations with above-average save rates by churn driver and cohort, and produces a design brief specifying the recommended combination set for the next programme cycle. The brief replaces informal programme calibration with an evidence base.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
At-risk customer identification
Forward-looking identification of currently-active customers displaying the behavioural precursors to churn — the operational output that enables proactive save-programme targeting. At-risk scoring depends on multi-signal aggregation: no single signal (usage decline, support-ticket spike, payment failure) is sufficient; the combination determines risk level. Banks that can score their entire active base weekly rather than sample quarterly contact the right customers before the exit decision is made.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] Segment-Specific At-Risk Profiling
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/at-risk-customer-identification/segment-specific-at-risk-profiling
intent: Agent applies segment-specific at-risk thresholds to the weekly at-risk scoring output, producing separate prioritised lists for the SME, retail mass, and emerging-affluent segments calibrated to each segment's churn-signal profile.
Problem to solve: The at-risk model produces a single ranked list calibrated on the full active base. Segments with different behavioural profiles — SME customers, whose primary churn signal is credit-facility utilisation decline rather than transaction-frequency drop — receive the same scoring threshold as retail customers. SME at-risk customers are systematically under-flagged in the unified model output.
Solution: Agent reads the weekly at-risk score output and applies segment-specific thresholds calibrated on historical churn patterns per segment. The SME relationship team, the retail mass save-programme team, and the affluent relationship team each receive a segment-specific at-risk list with thresholds appropriate for their customer profile. No customers are missed due to cross-segment threshold miscalibration.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Insights|M] At-Risk Scoring and Triage
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/at-risk-customer-identification/at-risk-scoring-and-triage
intent: Agent scores the full active customer base for churn probability weekly, surfacing a prioritised at-risk list for save-programme and relationship-manager action.
Problem to solve: At-risk identification relies on relationship managers recognising disengagement signals in their own books, supplemented by occasional analytics-team cohort studies. The multi-signal pattern that precedes churn — usage decline, support escalation, reduced transaction frequency, failed direct debit — is not assembled systematically across the full base before the customer exits.
Solution: Agent reads usage, support, payment, and digital-activity signals weekly for every active customer, scores churn probability using the multi-signal pattern, and produces a triage list ranked by risk score and segment priority. Save-programme teams and relationship managers work from the agent-generated list rather than reactive referrals.
OKR objective: A weekly at-risk score covering the full active customer base is available to the save programme and relationship managers, giving retention teams a prioritised intervention queue calibrated to current churn probability.
OKR KR [Adoption]: Agent produces the ranked at-risk list for ≥95% of weekly scoring cycles for ≥48 consecutive weeks within 12 months of go-live.
OKR KR [Acceptance]: ≥75% of top-decile at-risk flags confirmed as requiring intervention by the retention team lead on weekly review.
OKR KR [Cycle]: At-risk identification cycle reduced from monthly batch scoring to weekly automated production within 90 days of go-live.

### CARD 9 [Insights|M] Early-Warning Signal Calibration
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/at-risk-customer-identification/early-warning-signal-calibration
intent: Agent analyses historical churn events to identify the combination of behavioural signals that preceded exit at each lead time — 2 weeks, 4 weeks, 8 weeks — and produces a signal-calibration report for the at-risk model team.
Problem to solve: The at-risk model uses a fixed signal set selected at initial build. The relative predictive weight of signals changes as the customer base evolves — digital adoption increases, new product features alter usage patterns — but the model signal calibration is not reviewed until the next full model rebuild cycle, which occurs annually. The model accumulates silent decay between rebuilds.
Solution: Agent reads confirmed churn events from the prior 12 months, traces the behavioural signal pattern in the weeks preceding each exit, and produces a signal-calibration report showing which signals carry the strongest lead-time predictive value at 2, 4, and 8 weeks before churn. The model team uses the agent-generated calibration report as the primary input to the next recalibration cycle.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Intervention efficacy tracking
Systematic measurement of which save-programme interventions worked — for which cohorts, in which channels, at which points in the at-risk trajectory — so that future intervention design is informed by accumulated evidence rather than intuition. Efficacy tracking is the feedback loop that makes the save programme a learning system. Without it, the same ineffective interventions are repeated each cycle while effective ones are not scaled. OECD consumer-finance guidelines recommend systematic outcome tracking for retention programmes affecting credit products.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|S] Save-Programme Efficacy Report
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/intervention-efficacy-tracking/save-program-efficacy-report
intent: Automated monthly report of save-programme outcomes by cohort, intervention type, and channel, with agent-generated narrative identifying which interventions are working and which should be retired.
Problem to solve: Save-programme outcomes are tracked informally — contacts made and customers retained — without systematic breakdown by intervention type, cohort, or channel. Whether a fee waiver outperformed a relationship-manager call for a specific churn cluster is answerable only through a retrospective custom analysis.
Solution: Agent reads save-programme contact logs, offer details, and 90-day post-contact retention outcomes; produces a monthly efficacy report by intervention type, cohort, and channel; and flags which interventions are above or below expected save rate. CX leadership reviews the agent-generated narrative and adjusts the programme based on accumulated evidence.
OKR objective: A monthly save-programme efficacy report — covering outcomes by cohort, intervention type, and channel with narrative identifying which interventions should be continued or retired — is available to the retention team on the scheduled delivery date without manual assembly.
OKR KR [Adoption]: Agent delivers the save-programme efficacy report for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live.
OKR KR [Acceptance]: ≥80% of efficacy reports accepted by the retention lead as the basis for the next cycle's offer mix calibration without requiring supplementary manual analysis.
OKR KR [Cycle]: Efficacy report production cycle reduced from 5–7 days of manual outcome aggregation and commentary drafting to ≤24 hours of automated assembly.

### CARD 11 [Insights|S] Intervention Efficacy Trend Report
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/intervention-efficacy-tracking/intervention-efficacy-trend-report
intent: Agent tracks the save rate trend for each intervention type across consecutive programme cycles, surfacing whether a previously effective intervention type is decaying in performance and requires redesign.
Problem to solve: Save-programme interventions are reviewed for efficacy in the current cycle but not trended across cycles. An intervention that produced a 55% save rate in Q1 and is now delivering 38% in Q3 is declining materially, but without a trend view the Q3 number looks adequate in isolation and the intervention is not queued for redesign.
Solution: Agent reads efficacy outcomes from consecutive programme cycles, computes trend direction and statistical significance for each intervention type, and flags intervention types with declining save-rate trends for design review. The programme team uses the trend report alongside the current-cycle efficacy output to distinguish genuinely effective interventions from those in decline.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Insights|M] Intervention ROI by Cohort
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/intervention-efficacy-tracking/intervention-roi-by-cohort
intent: Agent calculates the net ROI of each save-programme intervention type by cohort — saved revenue minus offer cost and relationship-manager time — and produces a ranked ROI table for programme investment decisions.
Problem to solve: Save-programme efficacy is measured as save rate: the proportion of contacted at-risk customers who remained active 90 days after contact. Save rate does not account for offer cost or the value of the customer saved. A 60% save rate on a fee-waiver offer for a low-CLV cohort may produce negative ROI; a 30% save rate on a rate offer for a high-CLV cohort may generate substantial value. The programme is optimised for save rate rather than economic return.
Solution: Agent reads save-programme outcomes alongside offer costs, relationship-manager time allocation, and CLV data for contacted customers, computes net ROI per intervention type per cohort, and produces a ranked ROI table. The programme team allocates the next-cycle intervention budget to positive-ROI cohort-offer combinations and retires negative-ROI ones.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Contact-pattern indicators
Monitoring customer contact patterns — rising contact frequency, unresolved multi-contact chains, channel-switching after failed service interactions — as leading indicators of churn risk. A customer who contacts the bank three times in a month about the same issue and receives no resolution is materially more likely to churn than the contact-frequency number alone suggests. Under CBR and NBK conduct-supervision frameworks, systematic tracking of unresolved-contact chains is a component of complaint-monitoring obligations.
Lens
Scenario
Intent
Complexity

### CARD 13 [Insights|S] Channel-Switching Churn Signal
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/contact-pattern-indicators/channel-switching-churn-signal
intent: Agent identifies customers who switch to an assisted channel — phone, branch — after a failed digital-channel interaction, flagging the pattern as a composite churn precursor for retention prioritisation.
Problem to solve: Channel-switching after digital failure is a known churn precursor: a customer who cannot complete a task in the mobile app and subsequently calls the contact centre is materially more likely to exit than a customer who calls without prior digital failure. This pattern is not detected systematically because digital-failure events and subsequent contact-centre contacts are logged in separate systems with no cross-system linkage.
Solution: Agent reads mobile-app error and incomplete-journey events alongside contact-centre contact logs, links events by customer and temporal proximity, and identifies the channel-switch pattern. Customers matching the pattern are added to the retention at-risk queue with a higher churn-precursor weight than usage-decline signals alone.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 14 [Automation|S] Contact Frequency Trend Monitor
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/contact-pattern-indicators/contact-frequency-trend-monitor
intent: Agent tracks weekly contact frequency per customer against a personalised baseline, flagging customers whose contact rate has risen significantly for service-quality review and retention alert.
Problem to solve: Contact-centre management tracks aggregate contact volume per week. Individual customer-level contact frequency trends are not monitored. A customer whose contact rate triples in a four-week window — typically indicating a persistent unresolved issue — appears only as a marginal increment in the aggregate weekly contact count and receives no special attention.
Solution: Agent reads customer-level contact logs weekly, computes contact frequency relative to each customer's own baseline over the prior 90 days, and flags customers showing a material acceleration. The service-quality team reviews flagged customers and escalates where the accelerated contact indicates an unresolved issue; the at-risk model receives the elevated contact-frequency signal as a churn precursor input.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 15 [Insights|M] Multi-Contact Chain Detection
urn: urn:financial-services:scenario:customer-market-intelligence/retention-churn/contact-pattern-indicators/multi-contact-chain-detection
intent: Agent links customer contacts across channels by topic and time proximity weekly, identifies unresolved multi-contact chains, and surfaces customers with repeat unresolved issues for prioritised intervention before they reach formal complaint or churn.
Problem to solve: Customer contacts are logged per interaction across phone, chat, email, and branch channels with individual ticket IDs. A customer who calls three times about the same unresolved issue appears as three separate contacts in the system. The unresolved chain — the most reliable precursor to formal complaint or churn — is invisible in the ticket-level data.
Solution: Agent reads all customer interaction logs, links contacts by customer, topic, and temporal proximity, identifies chains of two or more interactions on the same unresolved issue, and produces a weekly prioritised list of customers with open multi-contact chains. Customer-experience and operations teams triage the list before formal complaints or exit behaviours materialise.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
