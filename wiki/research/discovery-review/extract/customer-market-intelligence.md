# 

source: html-alt/financial-services/en/customer-market-intelligence/index.html


[PAGE TEXT]
Customer insights
Customer segmentation (18)
Segmentation models
Behavioural segmentation (3)
·
Value-based segmentation (3)
·
Needs-based segmentation (3)
·
Risk-tier segmentation (3)
Segmentation operationalization
Segment-to-product mapping (3)
·
Segment migration tracking (3)
Market position
Market share & competitive positioning (15)
Market position measurement
Market share by product (3)
·
Market share by segment (3)
·
Geographic market share (3)
Competitive intelligence
Peer product benchmarking (3)
·
Competitor strategic moves (3)
Analytics cycles
Intelligence Cycles (17)
Customer insights
Segmentation refresh cycle (4)
Retention review cycle (5)
Market position
Competitive intelligence cycle (4)
Brand sentiment cycle (4)
Customer insights
Voice of customer (15)
Listening signals
NPS & CSAT surveys (3)
·
Complaint data (3)
·
App-store reviews (3)
Synthesis action
Theme extraction (3)
·
Feedback-to-priority translation (3)
Customer insights
Retention & churn (15)
Early warning signals
Churn cohort analysis (3)
·
At-risk customer identification (3)
·
Contact-pattern indicators (3)
Intervention design
Save-program design (3)
·
Intervention efficacy tracking (3)
Customer insights
Customer lifetime value (15)
Clv measurement
CAC / LTV / payback (3)
·
Cohort-level CLV (3)
·
CLV by segment (3)
Clv driven decisions
Acquisition channel prioritisation (3)
·
Retention spend allocation (3)
Customer insights
Wallet share (12)
Share measurement
Primary bank relationship share (3)
·
Product penetration depth (3)
·
Competitor-held share estimation (3)
Share growth
Cross-sell opportunity identification (3)
Market position
Brand & reputation (15)
Brand sentiment monitoring
Net promoter & brand equity tracking (3)
·
Social & media sentiment (3)
·
Conduct complaint signals (3)
Reputation defense build
Reputational risk early warning (3)
·
Crisis communication readiness (3)
Scenarios
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|S] Customer & commercial metrics digest
urn: urn:financial-services:scenario:customer-market-intelligence/customer-commercial-metrics-digest
intent: Customer and commercial KPIs — NPS, acquisition rate, attrition rate, segment performance, channel mix, pricing realisation, and product penetration — are aggregated each week into a decision-focused digest for the CCO, CMO, Head of Retail, and their leadership teams. The agent detects anomalies against trend, links co-moving metrics to root-cause hypotheses, and surfaces the decision queue.
Problem to solve: The Monday commercial dashboard is produced manually from BI exports each week by analyst teams. Anomalies are visible only to those who interrogate the data; co-moving metrics are not linked; decision items are buried in volume. CCO and Head of Retail spend the first part of each week reconstructing context before the commercial review meeting.
Solution: Agent aggregates customer and commercial KPIs from source systems, detects anomalies against rolling trend, links co-moving metrics to root-cause hypotheses, and surfaces the decision queue for the customer and commercial leadership review. Commercial leadership acts on surfaced signals; agent aggregates and detects.
OKR objective: CCO and commercial leadership receive a weekly customer and commercial metrics digest with anomalies flagged, co-moving metrics linked, and a decision queue surfaced — enabling the commercial review meeting to focus on decisions rather than data reconstruction.
OKR KR [Adoption]: Agent delivers customer and commercial metrics digest for ≥90% of weekly commercial review cycles for ≥12 consecutive weeks within 6 months of go-live.
OKR KR [Acceptance]: ≥85% of anomaly flags confirmed as actionable by CCO or Head of Retail; root-cause hypothesis links confirmed directionally accurate in ≥80% of instances reviewed by commercial leadership.
OKR KR [Cycle]: Per-cycle commercial metrics preparation and context-reconstruction time reduced from 2–3 days of manual BI export, assembly, and pre-meeting briefing to ≤2 hours of leadership digest review.

### CARD 2 [Insights|S] Customer Contact Root-Cause Intelligence
urn: urn:financial-services:scenario:customer-market-intelligence/customer-contact-root-cause-intelligence
intent: Classifies every customer contact across channels into granular root-cause categories, identifies avoidable contacts and repeat-contacting customers, and delivers a management dashboard that makes investment priorities visible.
Problem to solve: The bank logs hundreds of customer contacts each day across phone, email, chat, branch, and mobile, but tags them with coarse, channel-specific categories that don't capture the real reason for contact. Management can't answer the questions that drive priority decisions — which contacts are avoidable, which customers contact repeatedly, which products generate disproportionate volume.
Solution: AI processes every interaction and produces a management dashboard — turning thousands of cases into management insight. Batch analytics over historical data identifies avoidable-contact clusters and repeat-contacting customers.
OKR objective: Surface the primary avoidable-contact drivers to ops and product leadership on a weekly cadence.
OKR KR [Adoption]: Root-cause dashboard reviewed by ops and product leads in ≥3 consecutive monthly cycles.
OKR KR [Acceptance]: ≥75% of flagged avoidable-contact clusters validated as actionable by ops leadership.
OKR KR [Cycle]: Root-cause analysis cycle reduced from periodic manual sampling to weekly automated production.

### CARD 3 [Insights|S] Voice-of-customer / NPS verbatim synthesis
urn: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer-nps-verbatim-synthesis
intent: NPS verbatims and survey free-text collected across digital, branch, contact-centre, and relationship channels are classified into a stable theme taxonomy each cycle. The agent detects emerging themes, links theme volume to operational changes, and produces a CX dashboard for the Head of CX and product and channel owners.
Problem to solve: Banks collect thousands of NPS verbatims and survey free-text per month. Theme-coding is manual — conducted by offshore teams or in-house CX analysts — with a monthly thematic refresh, inconsistent inter-coder classification, and no systematic linkage between theme volume and operational changes such as product releases, fee changes, or channel outages.
Solution: Agent classifies verbatims against a stable theme taxonomy, detects emerging themes not yet in the taxonomy, and links theme volume shifts to operational changes in the period. Output is a CX dashboard for the Head of CX and product and channel owners. CX analysts review emerging-theme detections and apply judgement on taxonomy updates; agent classifies and detects.
OKR objective: The Head of CX and product and channel owners receive a consistently classified CX dashboard each cycle — with emerging themes surfaced and theme volume linked to operational changes — enabling action on CX signals within the same cycle they arise.
OKR KR [Adoption]: Agent classifies verbatims and delivers CX dashboard for ≥90% of monthly CX review cycles for ≥6 consecutive months within 9 months of go-live; classification covers all active channels (digital, branch, contact-centre, relationship).
OKR KR [Acceptance]: Inter-cycle theme classification consistency ≥90% on stable taxonomy themes; emerging-theme detections confirmed as genuinely novel by Head of CX in ≥80% of instances; operational-change linkage confirmed directionally accurate in ≥80% of flagged instances.
OKR KR [Cycle]: CX thematic analysis cycle reduced from a monthly manual coding process with 3–4 week lag to a weekly agent-led classification with ≤48-hour lag from verbatim collection to CX dashboard availability.

### CARD 4 [Insights|S] Peer-bank competitive intelligence
urn: urn:financial-services:scenario:customer-market-intelligence/peer-bank-competitive-intelligence
intent: A continuous peer-bank intelligence view is maintained across earnings calls, Pillar 3 and regulatory filings, published deposit and loan rate boards, branch and ATM footprint changes, and announced product launches. The agent synthesises peer earnings calls into a comparable-narrative format, tracks pricing moves across peer rate boards, flags regulatory-filing changes, and surfaces footprint and product-launch signals. Strategy and Pricing teams act on signals; agent maintains the continuous view.
Problem to solve: Peer intelligence is fragmented across Strategy, Treasury, Product, and Pricing teams. Weekly pricing surveys are maintained in spreadsheets. Peer earnings synthesis consumes 15–25 hours per analyst per quarter. Pillar 3, Call Report, FFIEC, and EBA disclosure changes are tracked inconsistently; footprint and product-launch signals surface ad hoc.
Solution: Agent maintains a continuous peer-bank intelligence view, synthesising peer earnings calls into a comparable-narrative format each quarter, tracking deposit and loan rate board moves on a weekly cadence, flagging material changes in peer regulatory filings, and surfacing footprint and product-launch signals as they appear. Strategy and Pricing teams act on surfaced signals; agent maintains the continuous view.
OKR objective: Strategy and Pricing teams have a continuously maintained peer-bank intelligence view — with earnings synthesis, pricing moves, regulatory-filing changes, and footprint and product signals surfaced — replacing fragmented spreadsheet tracking and ad hoc analyst synthesis.
OKR KR [Adoption]: Agent delivers peer earnings synthesis within 5 business days of each peer's quarterly earnings release for ≥90% of peers in the coverage set; weekly pricing-board tracking maintained for ≥12 consecutive weeks within 6 months of go-live.
OKR KR [Acceptance]: ≥85% of peer earnings synthesis accepted by Strategy team without material amendment; pricing-move flags confirmed accurate against published rate boards in ≥95% of instances reviewed.
OKR KR [Cycle]: Per-quarter peer earnings synthesis effort reduced from 15–25 hours per analyst to ≤2 hours of Strategy team review per peer coverage set; weekly pricing survey cycle reduced from manual spreadsheet maintenance to ≤1 hour of Pricing team review.

### CARD 5 [Insights|M] Repeat-Contact & Poor-Outcome Correlation Analysis
urn: urn:financial-services:scenario:customer-market-intelligence/repeat-contact-poor-outcome-correlation-analysis
intent: Links customer interactions across channels into issue chains by topic and temporal proximity, measures final outcomes per chain — account closure, escalation, complaint — and quantifies the handling cost attributable to repeat-contact patterns.
Problem to solve: When a customer's issue isn't fully resolved on the first contact they call back — often through different channels under different ticket IDs — but the repeat-contact chain is invisible to the bank, because the linkage lives in the customer's experience, not in the data. Customer-experience and ops teams can't see which repeat patterns end in account closure or formal complaint.
Solution: Take 12 months of customer interactions across all channels. AI links interactions by customer, topic, and temporal proximity, identifying chains that are really one issue handled poorly. Combines per-interaction classification, customer-level journey linking, and outcome correlation to identify top repeat-contact patterns driving account closure and formal complaints.
OKR objective: Identify the top repeat-contact patterns driving account closure and formal complaints.
OKR KR [Adoption]: Repeat-contact analysis deployed across ≥2 channels; reviewed by ops leadership monthly.
OKR KR [Acceptance]: ≥70% of high-risk chain patterns confirmed as systemic by channel owners on review.
OKR KR [Cycle]: Repeat-contact pattern identification reduced from quarterly retrospective to monthly automated output.

### CARD 6 [Optimize|L] Customer health score and retention prioritization
urn: urn:financial-services:scenario:customer-market-intelligence/customer-health-score-synthesis
intent: Agent synthesizes behavioral, product, and service signals into a continuous customer health score, ranking the portfolio for retention contact by urgency.
Problem to solve: Retention prioritization depends on relationship manager judgment over their book. Customers at the highest churn risk are not always those receiving the most attention; high-value customers in early-stage decline can go uncontacted until the signal becomes a confirmed exit.
Solution: Agent reads transaction activity, product depth, service contact recency, and balance trend for each customer and produces a health score updated weekly. Relationship managers and the retention team use the ranked output to prioritize contact; the highest-risk high-value customers receive outreach ahead of the decision window.
OKR objective: Every customer in the managed portfolio carries a weekly-updated health score synthesized from behavioral, product, and service signals, giving relationship managers and the retention team a continuously ranked basis for prioritizing contact.
OKR KR [Adoption]: Agent health score covers the full managed customer base and is refreshed weekly for ≥48 consecutive weeks within 12 months of go-live; relationship managers confirm using the ranked output for ≥80% of retention contact decisions.
OKR KR [Acceptance]: Churn rate among customers receiving score-triggered proactive retention contact at least 25% lower than the prior reactive baseline; health score predictive accuracy (AUC ≥0.72) confirmed on a 6-month holdout cohort.
OKR KR [Cycle]: First retention contact for highest-risk high-value customers advanced from post-exit-notification to ≥6 weeks before confirmed churn for ≥80% of the top-risk score decile.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
