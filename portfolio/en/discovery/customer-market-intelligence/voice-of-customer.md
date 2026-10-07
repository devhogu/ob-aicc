# Voice of customer

Voice of customer aggregates the full spectrum of customer-expressed signals — NPS and CSAT surveys, complaint text, app-store reviews, social mentions, and contact-center transcripts — into a coherent view of experience quality and friction patterns. Complaint-handling requirements call for systematic capture and resolution of complaint signals; VoC analytics is the intelligence layer that turns complaint data into operational learning. **GenAI enables the Bank to process every customer signal at scale**, producing thematic intelligence and priority rankings that a manual sampling process cannot match.

## NPS & CSAT surveys {#nps-csat-surveys}

Net Promoter Score and Customer Satisfaction surveys — the primary structured-feedback instrument for tracking customer loyalty and transactional experience quality. Most banks read the score monthly and process open-text verbatims through a sample — missing the granular driver signal in 90% of the feedback received.

### CSAT Post-Interaction Monitor

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/nps-csat-surveys/csat-post-interaction-monitor
- Lens: Automation
- Complexity: S
- Intent: The AI agent aggregates post-interaction CSAT scores by channel, product, and issue type daily, producing a dashboard refreshed each morning for contact-center and branch operations leadership.
- Problem to solve: Post-interaction CSAT data arrives from IVR, digital-channel, and branch surveys in separate platforms on inconsistent schedules. Operations management receives aggregated CSAT weekly at best; intraday or daily variation — a branch team showing declining scores following a process change — is visible only in retrospect.
- Solution: The AI agent aggregates CSAT scores from all interaction channels daily, classifies by channel, product, branch location, and issue type, and produces an operations dashboard updated each morning. Operations management identifies CSAT deterioration within 24 hours of onset and can isolate the channel or process driver before it affects the weekly score.
- OKR: Contact-center and branch operations leadership have a CSAT dashboard refreshed each morning — post-interaction scores from all channels classified by channel, product, branch location, and issue type — so that deterioration is seen within 24 hours of onset.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent aggregates CSAT scores from all interaction channels and refreshes the dashboard for ≥98% of business days from go-live. |
| Acceptance | ≥80% of CSAT deterioration signals on the dashboard confirmed as warranting investigation by operations management on weekly review. |
| Cycle | CSAT visibility cycle reduced from weekly aggregated reporting to a daily dashboard available each morning. |

### NPS Cohort Trend Analysis

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/nps-csat-surveys/nps-cohort-trend-analysis
- Lens: Insights
- Complexity: S
- Intent: The AI agent tracks NPS trend by customer cohort and segment across consecutive survey cycles, identifying whether score improvements or declines are broad-based or concentrated in specific groups.
- Problem to solve: NPS is reported as a single overall score and by broad product category. Trend analysis does not distinguish between a general score movement and one concentrated in a specific segment or origination cohort. A declining NPS driven entirely by a specific product cohort — mobile-originated retail customers in their first six months — is indistinguishable from a broad-based decline in the aggregate number.
- Solution: The AI agent reads NPS data with respondent segment and cohort attributes, tracks score trend by segment and origination cohort across survey cycles, and surfaces cohorts with statistically significant divergence from the overall trend. CX leadership receives cohort-level trend commentary alongside the aggregate score; product teams use the cohort signal to target improvement initiatives.
- OKR: CX leadership receives cohort-level NPS trend commentary alongside the aggregate score each survey cycle, showing whether score movements are broad-based or concentrated in specific segments or origination cohorts.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the cohort trend analysis for ≥95% of NPS survey cycles for ≥12 consecutive months post go-live, covering all segments and origination cohorts with respondent attributes. |
| Acceptance | ≥80% of cohorts flagged as diverging from the overall trend confirmed as meaningful by CX leadership; ≥50% of confirmed divergences taken up by product teams as improvement targets. |
| Cycle | Cohort-level NPS trend analysis moved from not produced to delivery within 3 business days of each survey cycle close. |

### NPS Driver Decomposition

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/nps-csat-surveys/nps-driver-decomposition
- Lens: Insights
- Complexity: M
- Intent: The AI agent processes the full NPS verbatim set from each survey cycle, identifies the top drivers of promoter and detractor scores by segment, and produces a driver-decomposition brief for the CX leadership team.
- Problem to solve: NPS survey cycles produce a score and a verbatim set. The score is reported monthly; the verbatims are sampled manually by a CX analyst who reads a representative subset and produces theme commentary. The commentary captures the most frequent theme in the sample but misses the driver pattern specific to high-value segments whose verbatim volume is too low for sampling to surface reliably.
- Solution: The AI agent processes every verbatim from each NPS cycle, applies thematic classification, and decomposes the NPS score into driver contributions by segment. CX leadership receives a driver decomposition showing which themes are inflating the detractor score for the emerging-affluent segment, for example, alongside the overall score commentary.
- OKR: The CX leadership team receives a driver-decomposition brief after each NPS cycle — built from every verbatim rather than a sample — showing the top drivers of promoter and detractor scores by segment.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent processes 100% of verbatims and delivers the driver-decomposition brief for ≥95% of NPS survey cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥80% of identified drivers confirmed as accurate by CX leadership on review; thematic classification matches CX analyst coding in ≥85% of sampled verbatims. |
| Cycle | Verbatim analysis moved from manual reading of a representative sample to full-coverage decomposition within 5 business days of each survey cycle close. |

## Theme extraction {#theme-extraction}

The analytical step of converting raw, unstructured customer feedback — verbatims, complaint text, review content, call transcripts — into named, quantified themes that can be tracked over time and across channels. Theme quality determines the utility of all downstream VoC work: coarse themes produce coarse actions. Extraction at scale requires ML-assisted clustering that no manual sampling process can approximate for breadth of coverage.

### Complaint Theme Extraction

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/theme-extraction/complaint-theme-extraction
- Lens: Automation
- Complexity: S
- Intent: The AI agent classifies and clusters complaint text from all channels into thematic groups weekly, producing a ranked dashboard of complaint drivers for compliance and ops review.
- Problem to solve: Complaint text is classified using coarse product or channel tags at intake. The taxonomy is too broad to drive ops prioritization, and cross-product complaint patterns that reveal systemic issues remain invisible in the category totals. Compliance reporting to the regulator is produced from the same coarse classification.
- Solution: The AI agent processes all incoming complaint text through thematic clustering, produces a weekly dashboard ranked by complaint volume, trend direction, and product, and provides the classified output for regulatory complaint reporting. The compliance lead reviews the AI-generated classification each week before compliance uses it for regulatory submissions; ops and product teams use the theme list to prioritize resolution.
- OKR: A weekly ranked dashboard of complaint drivers — classified and clustered from all-channel complaint text — is available to compliance and ops leadership without manual categorization effort.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the complaint theme dashboard for ≥95% of weekly cycles for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥80% of thematic clusters confirmed as accurately categorized by the compliance lead on weekly review. |
| Cycle | Complaint theme identification cycle reduced from monthly manual sampling and categorization to weekly automated production within 24 hours of period close. |

### Theme Trend Alert

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/theme-extraction/theme-trend-alert
- Lens: Enablement
- Complexity: S
- Intent: The AI agent monitors week-on-week volume change for each active feedback theme, triggers an alert to the responsible product or ops owner when a theme grows beyond a defined velocity threshold, and pre-drafts a root-cause investigation prompt.
- Problem to solve: Thematic intelligence from VoC systems is produced monthly. A theme that begins growing rapidly mid-cycle — a new fee structure generating complaints, a release bug driving app-store negative reviews — is not visible until the next monthly production run. No alert mechanism connects theme-velocity signals to the product or ops owner in near-real time.
- Solution: The AI agent monitors weekly theme volumes, detects themes growing at more than a defined velocity threshold since the prior week, and sends a structured alert to the responsible product or ops owner with a pre-drafted root-cause investigation prompt. Owners investigate the alert-triggered theme within 48 hours rather than at the next monthly review cycle.
- OKR: The responsible product or ops owner is alerted when a feedback theme grows beyond the defined week-on-week velocity threshold, with a pre-drafted root-cause investigation prompt attached.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent evaluates all active feedback themes against the velocity threshold for ≥95% of weekly cycles for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥75% of alerts confirmed as warranting investigation by the receiving product or ops owner; investigation opened within 48 hours for ≥80% of alerts. |
| Cycle | Time from the onset of rapid theme growth to owner awareness reduced from the next monthly production run to ≤1 week, with investigation started within 48 hours of the alert. |

### Cross-Channel VoC Synthesis

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/theme-extraction/cross-channel-voc-synthesis
- Lens: Insights
- Complexity: M
- Intent: The AI agent aggregates feedback from NPS verbatims, complaint text, support notes, app reviews, and social mentions into a single ranked thematic view with source attribution and trend direction.
- Problem to solve: Customer-experience teams read NPS verbatims, complaint text, support notes, app reviews, and social mentions in separate tools with no unified view. Systemic frictions that appear across multiple channels surface only when a senior analyst manually connects signals from different teams, typically months after they began.
- Solution: The AI agent aggregates all active feedback channels on a monthly cadence, applies unified thematic clustering across sources, and produces a ranked theme list with source attribution, volume, and trend direction. CX leadership reviews a single thematic view rather than five separate channel reports.
- OKR: A single ranked thematic view of customer feedback — aggregated from NPS verbatims, complaint text, support notes, app reviews, and social mentions with source attribution and trend direction — is available to the CX and product teams on the scheduled reporting cadence.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the cross-channel VoC synthesis for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥80% of thematic views confirmed as materially complete and accurately attributed by CX leadership on monthly review. |
| Cycle | Cross-channel VoC synthesis cycle reduced from 2–3 weeks of manual aggregation across feedback sources to ≤2 days of automated assembly and review. |

## Complaint data {#complaint-data}

Formally registered customer complaints — the regulated signal with mandatory capture, categorization, resolution, and reporting obligations under the regulator's complaint-handling requirements. Complaint data is the highest-signal VoC input: a complaint represents a customer who did not leave quietly. Systematic theme extraction from complaint text surfaces the operational and product failures generating regulatory exposure before they accumulate.

### Complaint Volume Trend Dashboard

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/complaint-data/complaint-volume-trend-dashboard
- Lens: Automation
- Complexity: S
- Intent: The AI agent aggregates complaint volumes by product, channel, and resolution status daily, producing a management dashboard and the data foundation for regulatory complaint-reporting submissions.
- Problem to solve: Complaint data is logged in the complaints management system but aggregated and formatted for management review manually each week. The regulatory reporting templates require complaint volumes classified by product category and resolution outcome, produced by compliance analysts from the same raw data. The aggregation effort is duplicated across management reporting and regulatory submissions.
- Solution: The AI agent reads complaint-management system data daily, aggregates volumes by product, channel, resolution status, and regulatory category, and populates both the management dashboard and the regulatory reporting template. Compliance analysts review the AI-generated regulatory output; management receives the dashboard without a weekly manual build.
- OKR: Management has a daily complaint dashboard by product, channel, and resolution status, and compliance analysts receive the regulatory reporting template populated from the same data — removing the duplicated manual aggregation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent refreshes the complaint dashboard for ≥98% of business days from go-live and populates the regulatory reporting template for 100% of reporting periods. |
| Acceptance | ≥90% of AI-populated regulatory templates accepted by compliance analysts without correction of volumes or categories. |
| Cycle | Complaint aggregation reduced from a weekly manual build, repeated for regulatory submissions, to a daily automated refresh with one source for both outputs. |

### High-Risk Complaint Escalation Flag

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/complaint-data/high-risk-complaint-escalation-flag
- Lens: Insights
- Complexity: S
- Intent: The AI agent reviews incoming complaints daily, flags those with regulatory escalation risk — language patterns indicating likely regulator referral, high-value customer status, or repeat-complaint history — for same-day compliance review.
- Problem to solve: Complaints with regulatory escalation potential — those likely to be referred to the regulator if not resolved promptly — are identified through a manual triage step performed by the compliance team. The triage is conducted on a weekly batch basis; complaints with high escalation risk sit unidentified in the queue for up to five working days before receiving compliance attention.
- Solution: The AI agent reads all incoming complaints daily, scores each for regulatory escalation risk using complaint-language patterns, customer value tier, and complaint history, and flags high-risk complaints for same-day compliance review. Compliance triage shifts from weekly batch to daily targeted review of AI-flagged cases.
- OKR: Complaints with regulatory escalation risk are flagged for compliance review on the day they are received, scored on complaint-language patterns, customer value tier, and complaint history.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent scores 100% of incoming complaints and delivers the high-risk flag list for ≥98% of business days from go-live. |
| Acceptance | ≥75% of flagged complaints confirmed as high escalation risk by the compliance team; ≤5% of complaints later referred to the regulator not previously flagged. |
| Cycle | Time to compliance attention for high-risk complaints reduced from up to five working days under weekly batch triage to the same business day. |

### Complaint Driver Insights

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/complaint-data/complaint-driver-insights
- Lens: Insights
- Complexity: M
- Intent: The AI agent applies thematic classification to complaint text weekly, identifies the top complaint drivers by product and customer segment, and produces a driver-insight report for ops and product leadership.
- Problem to solve: Complaint categories assigned at intake use a taxonomy optimized for regulatory reporting — broad product categories and a fixed resolution-type list — rather than for operational insight. The thematic content of complaint text — which specific product features, processes, or staff interactions generate the most complaints — is not extracted systematically, and ops teams respond to volume signals rather than root-cause patterns.
- Solution: The AI agent processes complaint text through thematic classification weekly, identifies the top drivers by product and segment beyond the regulatory intake taxonomy, and produces a driver-insight report for ops and product leadership. Ops improvement initiatives are targeted at the highest-volume complaint drivers identified in AI-generated themes.
- OKR: Ops and product leadership receive a weekly driver-insight report naming the top complaint drivers by product and customer segment, extracted from complaint text beyond the regulatory intake taxonomy.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the driver-insight report for ≥95% of weekly cycles for ≥48 consecutive weeks post go-live, covering all registered complaints. |
| Acceptance | ≥80% of top-ranked drivers confirmed as accurate root-cause patterns by ops and product leadership on monthly review; ≥1 ops improvement initiative per quarter opened against a ranked driver. |
| Cycle | Complaint driver identification moved from volume signals in intake categories to a weekly driver report within 2 business days of week close. |

## Feedback-to-priority translation {#feedback-to-priority-translation}

The governance step of translating validated VoC themes into backlog items, ops improvement initiatives, or regulatory responses — closing the loop between signal and action. Without this step, VoC analytics produces insight but not change. The challenge is that theme volume exceeds a bank's capacity to act; prioritization must weigh complaint-regulatory exposure, customer volume affected, revenue impact, and fix complexity. Where conduct supervision carries a reporting obligation on complaints, complaint-theme prioritization is a compliance input as well as a commercial one.

### VoC Action Outcome Tracking

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/feedback-to-priority-translation/voc-action-outcome-tracking
- Lens: Automation
- Complexity: S
- Intent: The AI agent tracks the status of VoC-initiated actions against the backlog and ops improvement queue monthly, reporting which theme-driven actions have been completed and measuring their impact on the originating theme volume.
- Problem to solve: VoC governance meetings assign actions — backlog items, ops process changes, training interventions — but there is no systematic tracking of whether those actions are completed or whether they reduce the complaint or feedback volume that prompted them. The feedback loop from action to impact is not closed, and recurring themes are re-raised in successive governance meetings without resolution history.
- Solution: The AI agent reads the action log from VoC governance meetings, tracks completion status against the backlog and ops improvement queue, and measures theme-volume change in the four to six weeks following action implementation. Monthly action-outcome reports, checked by the action owners, show which VoC-initiated interventions reduced theme volume and which had no measurable effect, building an evidence base for future prioritization.
- OKR: The VoC governance meeting receives a monthly action-outcome report showing which theme-driven actions were completed and whether each reduced the volume of the theme that prompted it.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent tracks 100% of actions in the VoC governance action log and delivers the action-outcome report for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥80% of reported completion statuses and theme-volume effects confirmed as accurate by action owners on review. |
| Cycle | Action-to-impact feedback moved from not tracked to a monthly report, with theme-volume change measured four to six weeks after each action is implemented. |

### VoC-to-Backlog Priority Mapping

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/feedback-to-priority-translation/voc-to-backlog-priority-mapping
- Lens: Enablement
- Complexity: M
- Intent: The AI agent maps validated VoC themes to product backlog items and ops work queues, scoring each by customer volume affected, regulatory exposure, and estimated fix complexity for the CX governance committee.
- Problem to solve: Monthly VoC review meetings produce a theme list but no automatic connection to the product backlog or ops improvement queue. Each theme requires manual assessment for regulatory exposure, customer volume, and fix complexity before prioritization — a two-to-three-week coordination exercise across CX, product, ops, and compliance.
- Solution: The AI agent reads validated VoC themes, maps each to open backlog items or ops initiatives, scores by regulatory-exposure level, customer-volume affected, and estimated fix complexity, and delivers a ranked prioritization list before the governance meeting. Product and ops leads review the AI-generated ranking rather than assembling it in the meeting.
- OKR: Validated VoC themes are mapped to product backlog items and ops work queues — scored by customer volume affected, regulatory exposure, and estimated fix complexity — and available to the CX governance committee on the scheduled review cadence.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the VoC-to-backlog priority mapping for ≥95% of scheduled monthly CX governance review cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥75% of priority mappings confirmed as actionable and correctly linked to backlog items by the CX governance committee on review. |
| Cycle | VoC theme-to-backlog mapping cycle reduced from 2–3 weeks of manual theme validation and backlog cross-reference work to ≤3 days of automated mapping and committee review. |

### Regulatory Exposure Theme Scoring

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/feedback-to-priority-translation/regulatory-exposure-theme-scoring
- Lens: Insights
- Complexity: M
- Intent: The AI agent scores each VoC theme for regulatory exposure under consumer-protection requirements, producing a tiered classification that separates conduct-supervised themes requiring formal response from those that are commercial-priority only.
- Problem to solve: VoC themes are reviewed in a single governance meeting where commercial priority and regulatory exposure are assessed informally and simultaneously. Compliance representatives in the meeting identify themes with regulatory obligations — complaint-handling deadlines, mandatory regulatory reporting — but the assessment is unstructured and depends on the institutional knowledge in the room.
- Solution: The AI agent reads the validated theme list and applies a regulatory-exposure scoring framework calibrated against the applicable complaint-handling requirements. Each theme receives a regulatory-exposure tier — mandatory response, advisory, commercial-only — and a suggested response timeline. The governance meeting receives pre-classified themes; compliance reviews the AI-assigned regulatory tiers before the meeting.
- OKR: Each validated VoC theme carries a regulatory-exposure tier — mandatory response, advisory, or commercial-only — and a suggested response timeline before the governance meeting, reviewed by compliance.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent scores 100% of validated themes for ≥95% of governance meeting cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥85% of AI-assigned regulatory tiers confirmed by compliance without reclassification. |
| Cycle | Regulatory-exposure assessment of themes moved from informal discussion in the governance meeting to pre-classified tiers available ≥2 business days before the meeting. |

## App-store reviews {#app-store-reviews}

Customer-published ratings and text reviews on the iOS App Store and Google Play — a continuous, unfiltered signal of digital-banking experience quality available in near-real time. App-store scores influence new-customer acquisition. Most banks track the aggregate star rating but do not systematically extract themes from review text, leaving the detailed product signal in the reviews unmined.

### App-Store Review Theme Monitor

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/app-store-reviews/app-store-review-theme-monitor
- Lens: Insights
- Complexity: S
- Intent: The AI agent processes all new iOS and Android app-store reviews weekly, classifies them into product and experience themes, and surfaces emerging negative-theme clusters to the digital product team before they accumulate into a sustained rating decline.
- Problem to solve: App-store review monitoring is conducted through aggregate star-rating tracking. Review text is read selectively by product managers when a rating drop is visible. Emerging negative themes — a bug introduced in a recent release, a new authentication friction — accumulate for two to three weeks before the star-rating impact triggers manual review, by which point the theme has already affected acquisition conversion.
- Solution: The AI agent processes all new app-store reviews weekly, applies thematic classification, and flags clusters with rising volume or sharply negative sentiment. Digital product teams receive a weekly theme brief; emerging negative clusters are surfaced within one review cycle of onset, enabling rapid prioritization ahead of the rating impact.
- OKR: The digital product team receives a weekly theme brief built from all new iOS and Android app-store reviews, with emerging negative-theme clusters surfaced before they accumulate into a sustained rating decline.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent processes 100% of new app-store reviews and delivers the theme brief for ≥95% of weekly cycles for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥75% of flagged emerging negative clusters confirmed as genuine product or experience issues by the digital product team. |
| Cycle | Detection of emerging negative review themes reduced from two to three weeks, when the star rating moves, to within one weekly review cycle of onset. |

### App Rating Benchmark Report

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/app-store-reviews/app-rating-benchmark-report
- Lens: Automation
- Complexity: S
- Intent: The AI agent aggregates the Bank's app-store ratings and review volume monthly alongside peer-bank app ratings, producing a competitive benchmark report for digital leadership without manual data collection.
- Problem to solve: App-store rating comparisons against the peer set are conducted manually when needed for strategy presentations. The Bank's own rating history is available in the developer console; peer ratings require manual lookup. No regular benchmark exists, and digital leadership does not have a systematic view of whether the Bank's app-store position is improving or declining relative to competitors.
- Solution: The AI agent collects the Bank's and peer-set app-store ratings and review volumes monthly from public store data, computes relative position and trend direction, and produces a competitive benchmark report. Digital leadership reviews the monthly benchmark; product investment decisions reference the competitive app-store position alongside internal usage metrics.
- OKR: Digital leadership receives a monthly competitive benchmark of the Bank's app-store ratings and review volumes against the peer set, with relative position and trend direction, without manual data collection.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the benchmark report for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live, covering the full defined peer set on both stores. |
| Acceptance | ≥85% of benchmark reports accepted by digital leadership without correction; ratings confirmed accurate against public store data in ≥95% of sampled checks. |
| Cycle | App-rating benchmarking moved from manual lookup when needed for strategy presentations to a monthly report within 3 business days of month end. |

### App Review to Backlog Signal

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer/app-store-reviews/app-review-to-backlog-signal
- Lens: Enablement
- Complexity: S
- Intent: The AI agent maps top app-store review themes to open backlog items monthly, flagging where review-volume evidence should accelerate existing items and where persistent review themes have no backlog representation.
- Problem to solve: App-store review themes and the product backlog are managed independently. Product managers occasionally reference review themes in backlog discussions but there is no systematic mapping. Review themes that surface a recurring friction — a login step that is consistently mentioned as cumbersome — may have a backlog item that could be accelerated, or may have no backlog item at all.
- Solution: The AI agent reads the monthly review-theme output and compares themes against open backlog items, producing a mapping that shows which themes have existing backlog representation and which are unaddressed. Product managers use the mapping in backlog grooming; review-volume data adds a customer-signal weighting to backlog prioritization alongside engineering complexity and business-value estimates.
- OKR: Product managers receive a monthly mapping of top app-store review themes to open backlog items, showing where review volume supports accelerating an item and which persistent themes have no backlog item.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the theme-to-backlog mapping for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥80% of theme-to-item links confirmed as correct by product managers in backlog grooming; ≥60% of unaddressed themes result in a new backlog item or a recorded decision not to act. |
| Cycle | Review-theme-to-backlog mapping moved from occasional reference in backlog discussions to a monthly mapping available before backlog grooming. |
