# Customer & Market Intelligence

Customer & Market Intelligence encompasses the analytical layer through which the Bank understands its customer base, tracks competitive positioning, and monitors brand standing. It spans segment economics, retention dynamics, lifetime value, share-of-wallet, market share, and reputation signals — the outward-facing view that strategic and commercial decisions depend on. **GenAI compresses the cycle between raw signal and actionable insight**: aggregating voice-of-customer at scale, surfacing churn cohort patterns before attrition materializes, and synthesizing competitive intelligence from public signals into decision-ready narratives for senior leadership.

## Problems

### Customer insights {#customer-insights}

| Lens | Problem |
| --- | --- |
| insights | Segment performance, retention cohorts, churn drivers, lifetime value, and share-of-wallet are maintained in separate team dashboards. Commercial leads lack a consolidated view of the customer economics picture — how segments are evolving, which cohorts are deteriorating, and where wallet opportunity remains uncaptured. |
| enablement | Testing a new segmentation hypothesis, modeling CLV under alternative retention assumptions, or estimating the wallet-share upside in a segment requires pulling multiple analysts for multi-day exercises. Product and segment owners cannot self-serve the answer to a commercial question within a business day. |
| automation | Monthly NPS and CSAT theme reports, retention cohort packs, churn root-cause write-ups, and wallet-share dashboards are assembled manually each cycle. The recurring structure and data-pipeline inputs make these strong candidates for end-to-end automated production. |
| new-opps | With continuous intelligence on segment economics and retention dynamics, the Bank identifies cross-sell and wallet-expansion opportunities weeks ahead of the quarterly review cycle. Cohorts that are expanding wallet with competitors surface as priority targets before the window closes. |

### Market position {#market-position}

| Lens | Problem |
| --- | --- |
| insights | Market share, competitive pricing, peer product moves, and brand-reputation signals are tracked through fragmented inputs — periodic surveys, press monitoring, and analyst reports. Leadership lacks a current, integrated view of where the Bank stands in its primary markets and how brand perception is moving. |
| enablement | Competitive positioning analyses and brand-reputation assessments are commissioned as multi-week research exercises. Strategy and marketing leaders cannot quickly test positioning hypotheses or assess the reputational exposure of a planned product or pricing move. |
| automation | Quarterly competitive intelligence briefs, brand sentiment reports, and market-share commentary for board packs are assembled manually. The aggregation pattern across fixed sources makes these candidates for automated production with human editorial sign-off. |
| new-opps | Continuous brand-reputation and competitive-position monitoring enables the Bank to act on emerging market spaces and reputational vulnerabilities before they surface in public or regulatory scrutiny. A bank that reads signals earliest is positioned to move first. |

## Overview

### Customer segmentation {#customer-segmentation}

- Group: Customer insights

| Sub-group | Items |
| --- | --- |
| Segmentation models | behavioural-segmentation, value-based-segmentation, needs-based-segmentation, risk-tier-segmentation |
| Segmentation operationalization | segment-to-product-mapping, segment-migration-tracking |

### Market share & competitive positioning {#market-share-positioning}

- Group: Market position

| Sub-group | Items |
| --- | --- |
| Market position measurement | market-share-by-product, market-share-by-segment, geographic-market-share |
| Competitive intelligence | peer-product-benchmarking, competitor-strategic-moves |

### Intelligence Cycles {#intelligence-cycles}

- Group: Analytics cycles

| Section | List name | Flows |
| --- | --- | --- |
| Customer insights | Customer insights | segmentation-refresh-cycle, retention-review-cycle |
| Market position | Market position | competitive-intelligence-cycle, brand-sentiment-cycle |

### Voice of customer {#voice-of-customer}

- Group: Customer insights

| Sub-group | Items |
| --- | --- |
| Listening signals | nps-csat-surveys, complaint-data, app-store-reviews |
| Synthesis & action | theme-extraction, feedback-to-priority-translation |

### Retention & churn {#retention-churn}

- Group: Customer insights

| Sub-group | Items |
| --- | --- |
| Early warning signals | churn-cohort-analysis, at-risk-customer-identification, contact-pattern-indicators |
| Intervention design | save-program-design, intervention-efficacy-tracking |

### Customer lifetime value {#customer-lifetime-value}

- Group: Customer insights

| Sub-group | Items |
| --- | --- |
| CLV measurement | cac-ltv-payback, cohort-level-clv, clv-by-segment |
| CLV-driven decisions | acquisition-channel-prioritisation, retention-spend-allocation |

### Wallet share {#wallet-share}

- Group: Customer insights

| Sub-group | Items |
| --- | --- |
| Share measurement | primary-bank-relationship-share, product-penetration-depth, competitor-held-share-estimation |
| Share growth | cross-sell-opportunity-identification |

### Brand & reputation {#brand-reputation}

- Group: Market position

| Sub-group | Items |
| --- | --- |
| Brand sentiment monitoring | net-promoter-brand-equity-tracking, social-media-sentiment, conduct-complaint-signals |
| Reputation defense | reputational-risk-early-warning, crisis-communication-readiness |

## Scenarios

### Customer & Commercial Metrics Digest

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-commercial-metrics-digest
- Lens: Insights
- Complexity: S
- Intent: Customer and commercial KPIs — NPS, acquisition rate, attrition rate, segment performance, channel mix, pricing realization, and product penetration — are aggregated each week into a decision-focused digest for the CCO, CMO, Head of Retail, and their leadership teams. The AI agent detects anomalies against trend, links co-moving metrics to root-cause hypotheses, and surfaces the decision queue.
- Problem to solve: The Monday commercial dashboard is produced manually from BI exports each week by analyst teams. Anomalies are visible only to those who interrogate the data; co-moving metrics are not linked; decision items are buried in volume. The CCO and the Head of Retail spend the first part of each week reconstructing context before the commercial review meeting.
- Solution: The AI agent aggregates customer and commercial KPIs from source systems, detects anomalies against rolling trend, links co-moving metrics to root-cause hypotheses, and surfaces the decision queue for the customer and commercial leadership review. Commercial leadership acts on surfaced signals; the AI agent aggregates and detects.
- OKR: The CCO and commercial leadership receive a weekly customer and commercial metrics digest with anomalies flagged, co-moving metrics linked, and a decision queue surfaced — enabling the commercial review meeting to focus on decisions rather than data reconstruction.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the customer and commercial metrics digest for ≥90% of weekly commercial review cycles for ≥12 consecutive weeks within 6 months of go-live. |
| Acceptance | ≥85% of anomaly flags confirmed as actionable by the CCO or the Head of Retail; root-cause hypothesis links confirmed directionally accurate in ≥80% of instances reviewed by commercial leadership. |
| Cycle | Per-cycle commercial metrics preparation and context-reconstruction time reduced from 2–3 days of manual BI export, assembly, and pre-meeting briefing to ≤2 hours of leadership digest review. |

### Customer Contact Root-Cause Intelligence

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-contact-root-cause-intelligence
- Lens: Insights
- Complexity: S
- Intent: The AI agent classifies every customer contact across channels into granular root-cause categories, identifies avoidable contacts and repeat-contacting customers, and delivers a management dashboard that makes investment priorities visible to ops and product leadership.
- Problem to solve: The Bank logs hundreds of customer contacts each day across phone, email, chat, branch, and mobile, but tags them with coarse, channel-specific categories that don't capture the real reason for contact. Management can't answer the questions that drive priority decisions — which contacts are avoidable, which customers contact repeatedly, which products generate disproportionate volume.
- Solution: The AI agent classifies every interaction into granular root-cause categories and produces a weekly management dashboard. Batch analytics over historical data identifies avoidable-contact clusters and repeat-contacting customers, which ops and product leadership review and validate.
- OKR: Ops and product leadership receive a weekly root-cause dashboard that classifies every customer contact across channels and surfaces the primary avoidable-contact drivers and repeat-contacting customers.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the root-cause dashboard for ≥95% of weekly cycles for ≥12 consecutive weeks post go-live; dashboard reviewed by ops and product leadership in ≥3 consecutive monthly cycles. |
| Acceptance | ≥75% of flagged avoidable-contact clusters validated as actionable by ops leadership. |
| Cycle | Root-cause analysis cycle reduced from periodic manual sampling to weekly automated production. |

### Voice-of-Customer / NPS Verbatim Synthesis

- URN: urn:financial-services:scenario:customer-market-intelligence/voice-of-customer-nps-verbatim-synthesis
- Lens: Insights
- Complexity: S
- Intent: NPS verbatims and survey free-text collected across digital, branch, contact-center, and relationship channels are classified into a stable theme taxonomy each cycle. The AI agent detects emerging themes, links theme volume to operational changes, and produces a CX dashboard for the Head of CX and product and channel owners.
- Problem to solve: The Bank collects NPS verbatims and survey free-text every month across its channels. Theme-coding is manual — conducted by in-house CX analysts — with a monthly thematic refresh, inconsistent inter-coder classification, and no systematic linkage between theme volume and operational changes such as product releases, fee changes, or channel outages.
- Solution: The AI agent classifies verbatims against a stable theme taxonomy, detects emerging themes not yet in the taxonomy, and links theme volume shifts to operational changes in the period. Output is a CX dashboard for the Head of CX and product and channel owners. CX analysts review emerging-theme detections and apply judgment on taxonomy updates; the AI agent classifies and detects.
- OKR: The Head of CX and product and channel owners receive a consistently classified CX dashboard each cycle — with emerging themes surfaced and theme volume linked to operational changes — enabling action on CX signals within the same cycle they arise.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent classifies verbatims and delivers the CX dashboard for ≥90% of monthly CX review cycles for ≥6 consecutive months within 9 months of go-live; classification covers all active channels (digital, branch, contact-center, relationship). |
| Acceptance | Inter-cycle theme classification consistency ≥90% on stable taxonomy themes; emerging-theme detections confirmed as genuinely novel by the Head of CX in ≥80% of instances; operational-change linkage confirmed directionally accurate in ≥80% of flagged instances. |
| Cycle | CX thematic analysis cycle reduced from a monthly manual coding process with 3–4 week lag to a weekly AI-led classification with ≤48-hour lag from verbatim collection to CX dashboard availability. |

### Peer-Bank Competitive Intelligence

- URN: urn:financial-services:scenario:customer-market-intelligence/peer-bank-competitive-intelligence
- Lens: Insights
- Complexity: S
- Intent: A continuous peer-bank intelligence view is maintained across earnings calls (where peers hold them), Pillar 3 and regulatory filings, published deposit and loan rate boards, branch and ATM footprint changes, and announced product launches. The AI agent synthesizes peer earnings calls into a comparable-narrative format, tracks pricing moves across peer rate boards, flags regulatory-filing changes, and surfaces footprint and product-launch signals. Strategy and Pricing teams act on signals; the AI agent maintains the continuous view.
- Problem to solve: Peer intelligence is fragmented across Strategy, Treasury, Product, and Pricing teams. Weekly pricing surveys are maintained in spreadsheets. Peer earnings synthesis consumes 15–25 hours per analyst per quarter. Changes in peer Pillar 3 disclosures, regulatory filings, and published financial statements are tracked inconsistently; footprint and product-launch signals surface ad hoc.
- Solution: The AI agent maintains a continuous peer-bank intelligence view, synthesizing peer earnings calls into a comparable-narrative format each quarter, tracking deposit and loan rate board moves on a weekly cadence, flagging material changes in peer regulatory filings, and surfacing footprint and product-launch signals as they appear. Strategy and Pricing teams act on surfaced signals; the AI agent maintains the continuous view.
- OKR: Strategy and Pricing teams have a continuously maintained peer-bank intelligence view — with earnings synthesis, pricing moves, regulatory-filing changes, and footprint and product signals surfaced — replacing fragmented spreadsheet tracking and ad hoc analyst synthesis.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers peer earnings synthesis within 5 business days of each peer's quarterly earnings release for ≥90% of peers in the coverage set; weekly pricing-board tracking maintained for ≥12 consecutive weeks within 6 months of go-live. |
| Acceptance | ≥85% of peer earnings synthesis accepted by the Strategy team without material amendment; pricing-move flags confirmed accurate against published rate boards in ≥95% of instances reviewed. |
| Cycle | Per-quarter peer earnings synthesis effort reduced from 15–25 hours per analyst to ≤2 hours of Strategy team review per peer coverage set; weekly pricing survey cycle reduced from manual spreadsheet maintenance to ≤1 hour of Pricing team review. |

### Repeat-Contact & Poor-Outcome Correlation Analysis

- URN: urn:financial-services:scenario:customer-market-intelligence/repeat-contact-poor-outcome-correlation-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent links customer interactions across channels into issue chains by topic and temporal proximity, measures final outcomes per chain — account closure, escalation, complaint — and quantifies the handling cost attributable to repeat-contact patterns for customer-experience and ops teams.
- Problem to solve: When a customer's issue isn't fully resolved on the first contact, they call back — often through different channels under different ticket IDs. The repeat-contact chain is invisible to the Bank, because the linkage lives in the customer's experience, not in the data. Customer-experience and ops teams can't see which repeat patterns end in account closure or formal complaint.
- Solution: The AI agent reads 12 months of customer interactions across all channels and links them by customer, topic, and temporal proximity, identifying chains that are really one issue handled poorly. It combines per-interaction classification, customer-level journey linking, and outcome correlation to identify the top repeat-contact patterns driving account closure and formal complaints. Ops leadership reviews the output monthly; channel owners confirm the systemic patterns.
- OKR: Customer-experience and ops teams receive a monthly view of the top repeat-contact patterns that end in account closure, escalation, or formal complaint, with the handling cost attributable to each pattern.

| Dimension | Key result |
| --- | --- |
| Adoption | Repeat-contact analysis deployed across ≥2 channels; reviewed by ops leadership monthly. |
| Acceptance | ≥70% of high-risk chain patterns confirmed as systemic by channel owners on review. |
| Cycle | Repeat-contact pattern identification reduced from quarterly retrospective to monthly automated output. |

### Customer Health Score and Retention Prioritization

- URN: urn:financial-services:scenario:customer-market-intelligence/customer-health-score-synthesis
- Lens: Optimize
- Complexity: L
- Intent: The AI agent synthesizes behavioral, product, and service signals into a continuous customer health score, ranking the portfolio for retention contact by urgency.
- Problem to solve: Retention prioritization depends on relationship manager judgment over their book. Customers at the highest churn risk are not always those receiving the most attention; high-value customers in early-stage decline can go uncontacted until the signal becomes a confirmed exit.
- Solution: The AI agent reads transaction activity, product depth, service contact recency, and balance trend for each customer and produces a health score updated weekly. Relationship managers and the retention team use the ranked output to prioritize contact; the highest-risk high-value customers receive outreach ahead of the decision window.
- OKR: Every customer in the managed portfolio carries a weekly-updated health score synthesized from behavioral, product, and service signals, giving relationship managers and the retention team a continuously ranked basis for prioritizing contact.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's health score covers the full managed customer base and is refreshed weekly for ≥48 consecutive weeks within 12 months of go-live; relationship managers confirm using the ranked output for ≥80% of retention contact decisions. |
| Acceptance | Churn rate among customers receiving score-triggered proactive retention contact at least 25% lower than the prior reactive baseline; health score predictive accuracy (AUC ≥0.72) confirmed on a 6-month holdout cohort. |
| Cycle | First retention contact for highest-risk high-value customers advanced from post-exit-notification to ≥6 weeks before confirmed churn for ≥80% of the top-risk score decile. |
