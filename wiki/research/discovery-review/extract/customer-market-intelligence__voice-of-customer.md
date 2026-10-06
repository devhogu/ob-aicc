# 

source: html-alt/financial-services/en/customer-market-intelligence/voice-of-customer/index.html


[PAGE TEXT]
NPS & CSAT surveys
Net Promoter Score and Customer Satisfaction surveys — the primary structured-feedback instrument for tracking customer loyalty and transactional experience quality. Under the CBR and NBK customer-protection frameworks, NPS trend is a supervisory-monitored indicator for retail banks above a regulated asset threshold. Most banks read the score monthly and process open-text verbatims through a sample — missing the granular driver signal in 90% of the feedback received.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] CSAT Post-Interaction Monitor
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/nps-csat-surveys/csat-post-interaction-monitor
intent: Agent aggregates post-interaction CSAT scores by channel, product, and issue type daily, producing a real-time dashboard for contact-centre and branch operations leadership.
Problem to solve: Post-interaction CSAT data arrives from IVR, digital-channel, and branch surveys in separate platforms on inconsistent schedules. Operations management receives aggregated CSAT weekly at best; intraday or daily variation — a branch team showing declining scores following a process change — is visible only in retrospect.
Solution: Agent aggregates CSAT scores from all interaction channels daily, classifies by channel, product, branch location, and issue type, and produces an operations dashboard updated each morning. Operations management identifies CSAT deterioration within 24 hours of onset and can isolate the channel or process driver before it affects the weekly score.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Insights|S] NPS Cohort Trend Analysis
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/nps-csat-surveys/nps-cohort-trend-analysis
intent: Agent tracks NPS trend by customer cohort and segment across consecutive survey cycles, identifying whether score improvements or declines are broad-based or concentrated in specific groups.
Problem to solve: NPS is reported as a single overall score and by broad product category. Trend analysis does not distinguish between a general score movement and one concentrated in a specific segment or origination cohort. A declining NPS driven entirely by a specific product cohort — mobile-originated retail customers in their first six months — is indistinguishable from a broad-based decline in the aggregate number.
Solution: Agent reads NPS data with respondent segment and cohort attributes, tracks score trend by segment and origination cohort across survey cycles, and surfaces cohorts with statistically significant divergence from the overall trend. CX leadership receives cohort-level trend commentary alongside the aggregate score; product teams use the cohort signal to target improvement initiatives.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Insights|M] NPS Driver Decomposition
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/nps-csat-surveys/nps-driver-decomposition
intent: Agent processes the full NPS verbatim set from each survey cycle, identifies the top drivers of promoter and detractor scores by segment, and produces a driver-decomposition brief for the CX leadership team.
Problem to solve: NPS survey cycles produce a score and a verbatim set. The score is reported monthly; the verbatims are sampled manually by a CX analyst who reads a representative subset and produces theme commentary. The commentary captures the most frequent theme in the sample but misses the driver pattern specific to high-value segments whose verbatim volume is too low for sampling to surface reliably.
Solution: Agent processes every verbatim from each NPS cycle, applies thematic classification, and decomposes the NPS score into driver contributions by segment. CX leadership receives a driver decomposition showing which themes are inflating the detractor score for the emerging-affluent segment, for example, alongside the overall score commentary.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Theme extraction
The analytical step of converting raw, unstructured customer feedback — verbatims, complaint text, review content, call transcripts — into named, quantified themes that can be tracked over time and across channels. Theme quality determines the utility of all downstream VoC work: coarse themes produce coarse actions. Extraction at scale requires ML-assisted clustering that no manual sampling process can approximate for breadth of coverage.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] Complaint Theme Extraction
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/theme-extraction/complaint-theme-extraction
intent: Agent classifies and clusters complaint text from all channels into thematic groups weekly, producing a ranked dashboard of complaint drivers for compliance and ops review.
Problem to solve: Complaint text is classified using coarse product or channel tags at intake. The taxonomy is too broad to drive ops prioritisation, and cross-product complaint patterns that reveal systemic issues remain invisible in the category totals. Compliance reporting to NBK and CBR is produced from the same coarse classification.
Solution: Agent processes all incoming complaint text through thematic clustering, produces a weekly dashboard ranked by complaint volume, trend direction, and product, and provides the classified output for NBK and CBR regulatory reporting. Compliance uses the agent-generated classification for regulatory submissions; ops and product teams use the theme list to prioritise resolution.
OKR objective: A weekly ranked dashboard of complaint drivers — classified and clustered from all-channel complaint text — is available to compliance and ops leadership without manual categorisation effort.
OKR KR [Adoption]: Agent produces the complaint theme dashboard for ≥95% of weekly cycles for ≥48 consecutive weeks post go-live.
OKR KR [Acceptance]: ≥80% of thematic clusters confirmed as accurately categorised by the compliance lead on weekly review.
OKR KR [Cycle]: Complaint theme identification cycle reduced from monthly manual sampling and categorisation to weekly automated production within 24 hours of period close.

### CARD 5 [Enablement|S] Theme Trend Alert
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/theme-extraction/theme-trend-alert
intent: Agent monitors week-on-week volume change for each active feedback theme, triggers an alert to the responsible product or ops owner when a theme grows beyond a defined velocity threshold, and pre-drafts a root-cause investigation prompt.
Problem to solve: Thematic intelligence from VoC systems is produced monthly. A theme that begins growing rapidly mid-cycle — a new fee structure generating complaints, a release bug driving app-store negative reviews — is not visible until the next monthly production run. No alert mechanism connects theme-velocity signals to the product or ops owner in near-real time.
Solution: Agent monitors weekly theme volumes, detects themes growing at more than a defined velocity threshold since the prior week, and sends a structured alert to the responsible product or ops owner with a pre-drafted root-cause investigation prompt. Owners investigate the alert-triggered theme within 48 hours rather than at the next monthly review cycle.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Insights|M] Cross-Channel VoC Synthesis
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/theme-extraction/cross-channel-voc-synthesis
intent: Agent aggregates feedback from NPS verbatims, complaint text, support notes, app reviews, and social mentions into a single ranked thematic view with source attribution and trend direction.
Problem to solve: Customer-experience teams read NPS verbatims, complaint text, support tickets, app reviews, and social mentions in separate tools with no unified view. Systemic frictions that appear across multiple channels surface only when a senior analyst manually connects signals from different teams, typically months after they began.
Solution: Agent aggregates all active feedback channels on a monthly cadence, applies unified thematic clustering across sources, and produces a ranked theme list with source attribution, volume, and trend direction. CX leadership reviews a single thematic view rather than four separate channel reports.
OKR objective: A single ranked thematic view of customer feedback — aggregated from NPS verbatims, complaint text, support notes, app reviews, and social mentions with source attribution and trend direction — is available to the CX and product teams on the scheduled reporting cadence.
OKR KR [Adoption]: Agent produces the cross-channel VoC synthesis for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live.
OKR KR [Acceptance]: ≥80% of thematic views confirmed as materially complete and accurately attributed by the CX lead on monthly review.
OKR KR [Cycle]: Cross-channel VoC synthesis cycle reduced from 2–3 weeks of manual aggregation across feedback sources to ≤2 days of automated assembly and review.

[PAGE TEXT]
Complaint data
Formally registered customer complaints — the regulated signal with mandatory capture, categorisation, resolution, and reporting obligations under NBK complaint-handling standards (Kazakhstan Financial Sector Regulatory Agency requirements) and CBR Ordinance No. 3854-U. Complaint data is the highest-signal VoC input: a complaint represents a customer who did not leave quietly. Systematic theme extraction from complaint text surfaces the operational and product failures generating regulatory exposure before they accumulate.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] Complaint Volume Trend Dashboard
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/complaint-data/complaint-volume-trend-dashboard
intent: Agent aggregates complaint volumes by product, channel, and resolution status daily, producing a management dashboard and the data foundation for NBK and CBR regulatory complaint-reporting submissions.
Problem to solve: Complaint data is logged in the complaints management system but aggregated and formatted for management review manually each week. The NBK and CBR regulatory reporting templates require complaint volumes classified by product category and resolution outcome, produced by compliance analysts from the same raw data. The aggregation effort is duplicated across management reporting and regulatory submissions.
Solution: Agent reads complaint-management system data daily, aggregates volumes by product, channel, resolution status, and regulatory category, and populates both the management dashboard and the regulatory reporting template. Compliance analysts review the agent-generated regulatory output; management receives the dashboard without a weekly manual build.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Insights|S] High-Risk Complaint Escalation Flag
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/complaint-data/high-risk-complaint-escalation-flag
intent: Agent reviews incoming complaints daily, flags those with regulatory escalation risk — language patterns indicating likely regulator referral, high-value customer status, or repeat-complaint history — for same-day compliance review.
Problem to solve: Complaints with regulatory escalation potential — those likely to be referred to NBK or CBR if not resolved promptly — are identified through a manual triage step performed by the compliance team. The triage is conducted on a weekly batch basis; complaints with high escalation risk sit unidentified in the queue for up to five working days before receiving compliance attention.
Solution: Agent reads all incoming complaints daily, scores each for regulatory escalation risk using complaint-language patterns, customer value tier, and complaint history, and flags high-risk complaints for same-day compliance review. Compliance triage shifts from weekly batch to daily targeted review of agent-flagged cases.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Insights|M] Complaint Driver Insights
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/complaint-data/complaint-driver-insights
intent: Agent applies thematic classification to complaint text weekly, identifies the top complaint drivers by product and customer segment, and produces a driver-insight report for ops and product leadership.
Problem to solve: Complaint categories assigned at intake use a taxonomy optimised for regulatory reporting — broad product categories and a fixed resolution-type list — rather than for operational insight. The thematic content of complaint text — which specific product features, processes, or staff interactions generate the most complaints — is not extracted systematically, and ops teams respond to volume signals rather than root-cause patterns.
Solution: Agent processes complaint text through thematic classification weekly, identifies the top drivers by product and segment beyond the regulatory intake taxonomy, and produces a driver-insight report for ops and product leadership. Ops improvement initiatives are targeted at the highest-volume complaint drivers identified in agent-generated themes.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Feedback-to-priority translation
The governance step of translating validated VoC themes into backlog items, ops improvement initiatives, or regulatory responses — closing the loop between signal and action. Without this step, VoC analytics produces insight but not change. The challenge is that theme volume exceeds the bank's capacity to act; prioritisation must weigh complaint-regulatory exposure, customer volume affected, revenue impact, and fix complexity. Banks operating under CBR and NBK conduct-supervision regimes carry a supervisory reporting obligation that makes complaint theme prioritisation a compliance input as well as a commercial one.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|S] VoC Action Outcome Tracking
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/feedback-to-priority-translation/voc-action-outcome-tracking
intent: Agent tracks the status of VoC-initiated actions against the backlog and ops improvement queue monthly, reporting which theme-driven actions have been completed and measuring their impact on the originating theme volume.
Problem to solve: VoC governance meetings assign actions — backlog items, ops process changes, training interventions — but there is no systematic tracking of whether those actions are completed or whether they reduce the complaint or feedback volume that prompted them. The feedback loop from action to impact is not closed, and recurring themes are re-raised in successive governance meetings without resolution history.
Solution: Agent reads the action log from VoC governance meetings, tracks completion status against the backlog and ops improvement queue, and measures theme-volume change in the four to six weeks following action implementation. Monthly action-outcome reports show which VoC-initiated interventions reduced theme volume and which had no measurable effect, building an evidence base for future prioritisation.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Enablement|M] VoC-to-Backlog Priority Mapping
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/feedback-to-priority-translation/voc-to-backlog-priority-mapping
intent: Agent maps validated VoC themes to product backlog items and ops work queues, scoring each by customer volume affected, regulatory exposure, and estimated fix complexity for the CX governance committee.
Problem to solve: Monthly VoC review meetings produce a theme list but no automatic connection to the product backlog or ops improvement queue. Each theme requires manual assessment for regulatory exposure, customer volume, and fix complexity before prioritisation — a two-to-three-week coordination exercise across CX, product, ops, and compliance.
Solution: Agent reads validated VoC themes, maps each to open backlog items or ops initiatives, scores by regulatory-exposure level, customer-volume affected, and estimated fix complexity, and delivers a ranked prioritisation list before the governance meeting. Product and ops leads review the agent-generated ranking rather than assembling it in the meeting.
OKR objective: Validated VoC themes are mapped to product backlog items and ops work queues — scored by customer volume affected, regulatory exposure, and estimated fix complexity — and available to the CX governance committee on the scheduled review cadence.
OKR KR [Adoption]: Agent produces the VoC-to-backlog priority mapping for ≥95% of scheduled monthly CX governance review cycles for ≥12 consecutive months post go-live.
OKR KR [Acceptance]: ≥75% of priority mappings confirmed as actionable and correctly linked to backlog items by the CX governance committee on review.
OKR KR [Cycle]: VoC theme-to-backlog mapping cycle reduced from 2–3 weeks of manual theme validation and backlog cross-reference work to ≤3 days of automated mapping and committee review.

### CARD 12 [Insights|M] Regulatory Exposure Theme Scoring
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/feedback-to-priority-translation/regulatory-exposure-theme-scoring
intent: Agent scores each VoC theme for regulatory exposure under NBK and CBR consumer-protection frameworks, producing a tiered classification that separates conduct-supervised themes requiring formal response from those that are commercial-priority only.
Problem to solve: VoC themes are reviewed in a single governance meeting where commercial priority and regulatory exposure are assessed informally and simultaneously. Compliance representatives in the meeting identify themes with regulatory obligations — complaint-handling deadlines, mandatory CBR or NBK reporting — but the assessment is unstructured and depends on the institutional knowledge in the room.
Solution: Agent reads the validated theme list and applies a regulatory-exposure scoring framework calibrated against NBK complaint-handling standards and CBR Ordinance No. 3854-U requirements. Each theme receives a regulatory-exposure tier — mandatory response, advisory, commercial-only — and a suggested response timeline. The governance meeting receives pre-classified themes; compliance reviews the agent-assigned regulatory tiers before the meeting.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
App-store reviews
Customer-published ratings and text reviews on the iOS App Store and Google Play — a continuous, unfiltered signal of digital-banking experience quality available in near-real time. App-store scores influence new-customer acquisition and are increasingly monitored by technology-focused banking supervisors. Most banks track the aggregate star rating but do not systematically extract themes from review text, leaving the detailed product signal in the reviews unmined.
Lens
Scenario
Intent
Complexity

### CARD 13 [Insights|S] App-Store Review Theme Monitor
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/app-store-reviews/app-store-review-theme-monitor
intent: Agent processes all new iOS and Android app-store reviews weekly, classifies them into product and experience themes, and surfaces emerging negative-theme clusters to the digital product team before they accumulate into a sustained rating decline.
Problem to solve: App-store review monitoring is conducted through aggregate star-rating tracking. Review text is read selectively by product managers when a rating drop is visible. Emerging negative themes — a bug introduced in a recent release, a new authentication friction — accumulate for two to three weeks before the star-rating impact triggers manual review, by which point the theme has already affected acquisition conversion.
Solution: Agent processes all new app-store reviews weekly, applies thematic classification, and flags clusters with rising volume or sharply negative sentiment. Digital product teams receive a weekly theme brief; emerging negative clusters are surfaced within one review cycle of onset, enabling rapid prioritisation ahead of the rating impact.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 14 [Automation|S] App Rating Benchmark Report
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/app-store-reviews/app-rating-benchmark-report
intent: Agent aggregates the bank's app-store ratings and review volume monthly alongside peer-bank app ratings, producing a competitive benchmark report for digital leadership without manual data collection.
Problem to solve: App-store rating comparisons against the peer set are conducted manually when needed for strategy presentations. The bank's own rating history is available in the developer console; peer ratings require manual lookup. No regular benchmark exists, and digital leadership does not have a systematic view of whether the bank's app-store position is improving or declining relative to competitors.
Solution: Agent collects the bank's and peer-set app-store ratings and review volumes monthly from public store data, computes relative position and trend direction, and produces a competitive benchmark report. Digital leadership reviews the monthly benchmark; product investment decisions reference the competitive app-store position alongside internal usage metrics.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 15 [Enablement|S] App Review to Backlog Signal
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/app-store-reviews/app-review-to-backlog-signal
intent: Agent maps top app-store review themes to open backlog items monthly, flagging where review-volume evidence should accelerate existing items and where persistent review themes have no backlog representation.
Problem to solve: App-store review themes and the product backlog are managed independently. Product managers occasionally reference review themes in backlog discussions but there is no systematic mapping. Review themes that surface a recurring friction — a login step that is consistently mentioned as cumbersome — may have a backlog item that could be accelerated, or may have no backlog item at all.
Solution: Agent reads the monthly review-theme output and compares themes against open backlog items, producing a mapping that shows which themes have existing backlog representation and which are unaddressed. Product managers use the mapping in backlog grooming; review-volume data adds a customer-signal weighting to backlog prioritisation alongside engineering complexity and business-value estimates.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
