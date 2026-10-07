# Strategic & reputational risk

Strategic risk is the risk of loss from business decisions that prove incorrect in the face of competitive, regulatory, or macroeconomic change — the category that encompasses business model obsolescence, failed acquisitions, and market-exit decisions. Reputational risk is the risk of damage to a bank's standing with customers, counterparties, regulators, and investors from adverse events or perceptions. Both categories lack the precise measurement frameworks that govern credit or market risk; they are assessed through scenario analysis, signal monitoring, and management judgment. **The GenAI opportunity is to aggregate the signal volume** — peer earnings, regulatory communications, media monitoring, customer sentiment — that exceeds manual review capacity and deliver a structured picture (daily for reputational signals, monthly to semi-annual for regulatory, peer, and competitive signals) for the CRO and Board Risk Committee.

## Problems

### Strategic-decision risk {#strategic-decision-risk}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Strategic risk scenarios — business model stress from fintech competition, central bank digital currency adoption impacts, regulatory capital changes — are assessed annually as part of the ICAAP strategic risk section. Between cycles, the board and CRO lack a current signal on which strategic risks are materializing faster than the annual scenario assumed, or which new strategic risks have emerged from the external environment. |
| Enablement | Board-level strategy reviews, M&A target assessment, and new-market entry decisions each require an integrated view of competitive positioning, regulatory landscape, and macroeconomic environment. Assembling that view from multiple research and intelligence sources before a board session is a multi-week research exercise. |
| Automation | Strategic risk reporting for the board — emerging strategic risk register, peer comparison on strategic KPIs, scenario update — is assembled manually from research, market data, and peer disclosures on a quarterly or annual cycle. |
| New business opportunities | A continuously refreshed strategic risk signal — monthly and quarterly scans of peer earnings commentary, regulatory speeches, and competitor product announcements — gives the CEO and board a forward-looking input to strategy adaptation that annual review cycles cannot provide. Banks that adapt their strategic positioning quarterly rather than annually respond to competitive and regulatory shifts before peers whose cycle is longer. |

## Strategic-decision risk analysis {#strategic-decision-risk-analysis}

Strategic-decision risk analysis quantifies the risk embedded in major strategic choices — new market entry, product line extension, acquisition, or business model transformation — by assessing the range of outcomes under competitive, regulatory, and macroeconomic scenarios. Inputs include competitor positioning, regulatory signals, customer segment economics, and macroeconomic forecasts. The analysis is the primary input to board-level strategy reviews and ICAAP strategic risk sections. Strategy teams conducting this analysis face a data-assembly challenge: the relevant signals are distributed across research subscriptions, regulatory publications, peer disclosures, and internal performance data.

### Strategic-Decision Risk Analysis

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/strategic-decision-risk-analysis/strategic-decision-risk-analysis
- Lens: Enablement
- Complexity: M
- Intent: The AI agent evaluates major strategic proposals — new market entry, product launch, acquisition — against the Bank's risk appetite, regulatory standing, and reputational track record, producing a structured risk opinion for the CRO.
- Problem to solve: Strategic proposals reach the CRO for risk review with variable levels of risk framing. Alignment to risk appetite, regulatory constraint mapping, and reputational precedent analysis are prepared by the proposing business unit and reviewed by risk in a compressed timeframe before Board or EXCO submission.
- Solution: The AI agent reads the strategic proposal and maps it against the Bank's risk appetite statement, regulatory operating permissions, prior regulatory findings, and reputational signal history. It produces a structured CRO risk opinion covering risk-appetite alignment, regulatory constraints, reputational exposure, and flagged conditions. General Counsel checks the regulatory constraints, and the CRO reviews and adds judgment before submission to the Board or EXCO.
- OKR: The CRO presents a structured risk opinion — covering risk-appetite alignment, regulatory constraints, reputational exposure, and flagged conditions — on major strategic proposals, drafted by the AI agent from the proposal, the risk appetite statement, regulatory permissions, and reputational signal history.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to produce the CRO risk opinion draft for ≥80% of major strategic proposals reaching the Board or EXCO within 12 months of go-live; all four risk opinion dimensions (risk-appetite alignment, regulatory constraints, reputational exposure, flagged conditions) covered in every run. |
| Acceptance | ≥75% of AI-drafted risk opinions accepted by the CRO with only judgment additions before Board or EXCO submission; regulatory constraint accuracy confirmed at ≥90% on review by General Counsel. |
| Cycle | Risk opinion draft delivered within 2 business days of proposal submission, versus ≥5 days of manual preparation in a compressed pre-Board window under the prior approach. |

### Strategic Risk Appetite Alignment Check

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/strategic-decision-risk-analysis/strategic-risk-appetite-alignment-check
- Lens: Enablement
- Complexity: M
- Intent: The AI agent reads a strategic proposal and maps each material risk dimension against the Bank's current Risk Appetite Statement, producing a structured alignment assessment for the CRO before EXCO submission.
- Problem to solve: Strategic proposals are reviewed for risk appetite alignment by the CRO in a compressed pre-EXCO window. The alignment assessment requires cross-referencing the proposal against the risk appetite framework (RAF) across capital, liquidity, credit, operational, and reputational risk dimensions — a structured task that is currently performed through the CRO's judgment without a systematic mapping tool.
- Solution: The AI agent reads the strategic proposal and the current Risk Appetite Statement. It maps each proposed action to the relevant RAF metric and dimension, identifies dimensions where the proposal would consume material headroom or push the Bank toward an appetite boundary, and assembles the structured alignment assessment. The CRO reviews and adds forward-looking judgment before EXCO submission.
- OKR: The CRO adds forward-looking judgment to an AI-assembled risk appetite alignment assessment — each proposed action mapped to the relevant RAF metric and dimension, with material headroom consumption flagged — before EXCO submission.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's alignment assessment produced for ≥80% of strategic proposals submitted to EXCO within 12 months of go-live; all five RAF dimensions (capital, liquidity, credit, operational, reputational) mapped in every assessment. |
| Acceptance | ≥75% of alignment assessments accepted by the CRO with only judgment additions; RAF metric mapping confirmed as accurate in ≥90% of cases on review. |
| Cycle | Alignment assessment delivered within 2 business days of proposal receipt, versus an unstructured review in the compressed pre-EXCO window. |

### Market Entry Regulatory Constraint Mapping

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/strategic-decision-risk-analysis/market-entry-regulatory-constraint-mapping
- Lens: Insights
- Complexity: M
- Intent: The AI agent maps a proposed new market or product entry against the regulatory requirements of the target jurisdiction — licensing, capital, AML, consumer protection — producing a constraint summary for the strategy and legal teams.
- Problem to solve: New market and product entry decisions require a regulatory constraint mapping exercise conducted by the legal and compliance functions. The initial mapping — covering licensing requirements, capital implications, local AML regime requirements, and consumer protection obligations — is assembled manually from regulatory databases and legal research, consuming legal function capacity before the business case is approved.
- Solution: The AI agent reads the target jurisdiction's regulatory framework publications and the Bank's regulatory monitoring database, and extracts licensing requirements, capital treatment, AML obligations, and consumer protection thresholds for the proposed market or product. It produces a constraint summary covering each regulatory dimension with source citations. The strategy team uses the summary to frame the business case; the legal team validates it before formal commitment.
- OKR: The strategy team frames the business case from an AI-produced regulatory constraint summary — licensing, capital treatment, AML obligations, and consumer protection thresholds for the target market or product, with source citations — which the legal team validates before formal commitment.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's constraint summary produced for ≥80% of new market and product entry proposals within 12 months of go-live; all four regulatory dimensions covered with source citations in every summary. |
| Acceptance | ≥80% of constraint statements confirmed as accurate by the legal team on validation; ≥75% of summaries used by the strategy team in the business case without material rework. |
| Cycle | Constraint summary delivered within 5 business days of the proposal request, versus weeks of manual legal research before the business case is approved. |

## Reputational signal monitoring {#reputational-signal-monitoring}

Reputational signal monitoring aggregates adverse and positive signals from media coverage, social media sentiment, customer complaint trends, regulatory enforcement actions, and ESG rating agency commentary to produce a continuous picture of the Bank's reputational standing. Early detection of an emerging adverse narrative — when it is still confined to specialist media or social media before mainstream coverage — enables a more measured and effective response than one initiated after mass coverage. Supervisors commonly assess reputational risk qualitatively in the supervisory review process; boards are expected to demonstrate active monitoring.

### Executive Mention & Media Monitor

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/reputational-signal-monitoring/executive-mention-media-monitor
- Lens: Automation
- Complexity: S
- Intent: The AI agent monitors news and social media for named executive mentions and references to the Bank's brand, classifies them by sentiment and topic, alerts the Head of Communications to high-severity adverse signals as they are detected, and delivers a daily brief with all adverse signals flagged for same-day review.
- Problem to solve: Executive mentions in media and on social platforms require the communications team to monitor multiple channels throughout the business day. An adverse mention — executive conduct comment, analyst criticism, or social media amplification of a customer complaint — may circulate for hours before reaching the communications team's attention under the current review cadence.
- Solution: The AI agent reads media monitoring feeds and social platform data continuously, classifies mentions by sentiment and topic for each named executive and the Bank's brand, and alerts the Head of Communications to high-severity adverse signals as they are detected. A daily brief lists all adverse signals flagged by severity, which the Head of Communications reviews the same day.
- OKR: The Head of Communications is alerted to high-severity adverse executive and brand mentions as they are detected and reviews all adverse mentions on the day they appear, from an AI-produced daily brief that classifies news and social media mentions by sentiment and topic and flags adverse signals by severity.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's monitoring covers all named executives and the Bank's brand across the defined media and social feeds within 3 months of go-live; daily brief delivered on ≥95% of business days once live. |
| Acceptance | ≥80% of adverse flags confirmed by the Head of Communications as warranting same-day review; sentiment and topic classification accuracy confirmed at ≥85% on monthly sample review. |
| Cycle | High-severity adverse mentions reach the Head of Communications as they are detected and all others on the day they appear, versus circulating for hours undetected under the manual review cadence. |

### ESG Rating Agency Signal Monitor

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/reputational-signal-monitoring/esg-rating-agency-signal-monitor
- Lens: Insights
- Complexity: S
- Intent: Where the Bank holds ESG ratings, the AI agent monitors rating agency publications — MSCI, Sustainalytics, ISS — for the Bank's ESG score updates, controversy flags, and peer ESG rating movements, delivering a quarterly signal digest to the Head of Investor Relations and CRO.
- Problem to solve: ESG rating changes affect the Bank's eligibility for ESG-benchmarked institutional investor mandates. ESG agency publications are monitored by the sustainability team but are not systematically cross-referenced with investor relations and CRO risk functions; a rating downgrade or controversy flag identified in the sustainability team's routine review may not reach investor relations or the CRO before investor inquiries arrive.
- Solution: The AI agent reads ESG rating agency publications for the Bank and the peer set, and identifies score updates, controversy flag additions, and methodology changes. It cross-references score movements against the Bank's ESG target commitments and delivers the quarterly signal digest to the Head of Investor Relations and CRO.
- OKR: The Head of Investor Relations and CRO receive a quarterly AI-produced digest of ESG rating agency signals — the Bank's score updates, controversy flags, methodology changes, and peer rating movements, cross-referenced against the Bank's ESG target commitments — ahead of investor inquiries.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's signal digest delivered for ≥4 consecutive quarters within 15 months of go-live; all monitored rating agencies and the full defined peer set covered in every digest. |
| Acceptance | ≥80% of digests rated as complete and relevant by the Head of Investor Relations; 100% of score changes and controversy flags affecting the Bank captured in the digest for the quarter in which they were published. |
| Cycle | Digest delivered within 5 business days of quarter-end, so that rating changes reach investor relations and the CRO before investor inquiries arrive rather than after. |

### Reputational Signal Monitoring

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/reputational-signal-monitoring/reputational-signal-monitoring
- Lens: Insights
- Complexity: M
- Intent: The AI agent monitors media, social channels, and regulatory publication feeds for reputational signals relevant to the Bank — executive mentions, product complaints, sector peer events, and regulatory commentary — and delivers a daily brief to the Head of Communications and CRO.
- Problem to solve: Reputational signal monitoring relies on media monitoring subscriptions reviewed by communications staff. Cross-channel synthesis — linking a social media complaint cluster to a product issue already visible in the internal complaint register — requires manual correlation and is typically identified in the weekly communications review rather than as the signal emerges.
- Solution: The AI agent reads media monitoring feeds, social channel APIs, regulatory publication feeds, and the internal complaint register. It identifies signal clusters, cross-references external and internal sources, and produces a daily brief ranked by reputational severity for the Head of Communications and CRO.
- OKR: The Head of Communications and CRO manage reputational risk from a daily AI-produced brief — with cross-channel signal clusters ranked by severity — rather than from weekly manual synthesis of media monitoring subscriptions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's reputational signal monitoring runs across media, social, regulatory, and internal complaint register feeds within 6 months of go-live; daily brief delivered to the Head of Communications and CRO for ≥200 business days per year once live. |
| Acceptance | ≥75% of daily signal clusters rated as material or higher by the Head of Communications; cross-channel correlation accuracy (external signal linked to corresponding internal complaint cluster) confirmed at ≥80% on monthly quality review. |
| Cycle | Daily brief delivered before the start of business each morning, versus ≥5 business days of latency from signal emergence to identification under the prior weekly synthesis approach. |

## Competitive & industry signals {#competitive-industry-signals}

Competitive intelligence monitors the strategic moves of peer banks and non-bank competitors — product launches, pricing changes, M&A activity, technology investments, and market exits — to inform the Bank's own strategic positioning and risk assessment. Industry signals cover structural shifts — open banking adoption, digital currency development, regulatory framework evolution — that affect the competitive environment over a longer horizon. Both inputs are relevant to the strategic risk section of ICAAP and to board strategy reviews. The signal volume from peer banks, fintech competitors, and regulatory bodies in the Bank's market requires systematic aggregation.

### Peer Earnings & Strategy Signal Digest

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/competitive-industry-signals/peer-earnings-signal-digest
- Lens: Insights
- Complexity: M
- Intent: The AI agent reads peer bank earnings releases, investor day transcripts, and regulatory filings each quarter and produces a structured signal digest — product moves, capital actions, technology investments, and strategic guidance — for the Chief Strategy Officer and CRO.
- Problem to solve: Peer bank signals are distributed across earnings releases, investor presentations, and regulatory filings published across a concentrated earnings window. Strategy and risk teams review a subset of peer disclosures manually; a systematic cross-peer comparison is produced at most annually for board strategy sessions.
- Solution: The AI agent reads earnings releases, investor day transcripts, and annual report and regulatory disclosure filings for a defined peer set. It extracts product launch announcements, pricing signals, capital allocation priorities, technology investment commentary, and market exit decisions, and assembles the quarterly digest for the Chief Strategy Officer and CRO, with signal clusters ranked by strategic relevance to the Bank.
- OKR: The Chief Strategy Officer and CRO receive a quarterly AI-produced peer signal digest — product moves, pricing signals, capital actions, technology investments, and market exits across the defined peer set, ranked by strategic relevance — rather than a manual review of a subset of peer disclosures.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's peer digest delivered for ≥4 consecutive quarters within 15 months of go-live; 100% of the defined peer set covered in every digest. |
| Acceptance | ≥75% of signal clusters rated as strategically relevant by the Chief Strategy Officer; extracted signals confirmed as accurate against source disclosures in ≥90% of sampled items. |
| Cycle | Quarterly digest delivered within 10 business days of the close of the peer reporting window, versus a cross-peer comparison produced at most annually for board strategy sessions. |

### Regulatory & Industry Horizon Scanning

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/competitive-industry-signals/regulatory-horizon-scanning
- Lens: Insights
- Complexity: M
- Intent: The AI agent monitors regulatory consultation papers, Basel Committee publications, and industry body reports, extracting strategic risk implications for the Bank's business model and delivering a monthly briefing to the CRO and Board Risk Committee secretary.
- Problem to solve: The volume of publications from the regulator, the Basel Committee, and industry bodies generates more material than the risk team can systematically review. Strategic risk implications — a Basel IV implementation timeline that changes capital requirements, an update to operational-resilience requirements that affects the vendor strategy — can be missed in the volume of concurrent publications.
- Solution: The AI agent monitors defined regulatory and industry publication feeds, classifies each item by strategic risk category, and delivers a monthly structured briefing covering the top items with strategic risk implication summaries. The CRO and Board Risk Committee secretary use the briefing to prepare the strategic risk section of the quarterly board report.
- OKR: The CRO and Board Risk Committee secretary prepare the strategic risk section of the quarterly board report from a monthly AI-produced briefing that classifies regulatory and industry publications by strategic risk category and summarizes the implications of the top items.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's monthly briefing delivered for ≥10 consecutive months in year 1; 100% of the defined regulatory and industry publication feeds monitored in every run. |
| Acceptance | ≥75% of top items rated as strategically relevant by the CRO; ≥80% of briefings used in preparing the quarterly board report without material supplementation. |
| Cycle | Briefing delivered within 3 business days of month-end, versus publications reviewed as capacity allowed, with strategic implications missed in the volume. |

### Competitive Position Benchmark

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/competitive-industry-signals/competitive-position-benchmark
- Lens: Insights
- Complexity: M
- Intent: The AI agent assembles a semi-annual competitive position benchmark — market share, pricing, digital product parity, and capital ratios — against the Bank's defined peer set, for the ICAAP strategic risk section and board strategy review.
- Problem to solve: ICAAP strategic risk analysis requires a competitive position assessment. Assembling a multi-dimensional benchmark across market share, product parity, pricing, and capital strength from public sources and industry data for a defined peer set is performed manually once per year, using data that may already be several months stale at the time of ICAAP submission.
- Solution: The AI agent reads public filings, industry association data, and regulatory disclosures for the peer set, constructs the multi-dimensional benchmark table, and delivers the semi-annual competitive position report. The strategy team reviews data currency and adds qualitative interpretation before ICAAP submission.
- OKR: The strategy team adds qualitative interpretation to an AI-assembled semi-annual competitive position benchmark — market share, pricing, digital product parity, and capital ratios against the defined peer set — for the ICAAP strategic risk section and board strategy review.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's benchmark produced for ≥2 consecutive semi-annual cycles within 18 months of go-live; all four benchmark dimensions covered for 100% of the defined peer set. |
| Acceptance | ≥85% of benchmark data points accepted by the strategy team as current and accurate on review; benchmark used in the ICAAP strategic risk section without material rework. |
| Cycle | Benchmark delivered within 10 business days of each semi-annual data cut, versus a once-a-year manual exercise with data several months stale at ICAAP submission. |

## Crisis response & narrative {#crisis-response-narrative}

Crisis response covers the governance, communication, and operational actions the Bank takes when a material adverse event — a cyber incident, a regulatory enforcement action, an executive conduct matter, or a large credit loss announcement — becomes public. Pre-crisis preparation maps plausible adverse scenarios to stakeholder-specific narrative frameworks; the response at crisis onset activates the prepared materials and adapts them in real time. The Board, regulators, institutional investors, retail customers, and staff each require different messaging calibrated to the appropriate level of disclosure and tone. In crisis conditions, the time available to assemble coherent stakeholder-specific messaging is often shorter than the time needed to prepare it.

### Post-Crisis Narrative Review

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/crisis-response-narrative/post-crisis-narrative-review
- Lens: Insights
- Complexity: S
- Intent: The AI agent reviews the communications record of a resolved crisis — stakeholder messages, timeline, media coverage — and produces a narrative effectiveness assessment for the Head of Communications to inform future scenario framework updates.
- Problem to solve: Post-crisis lessons learned for communications effectiveness are captured informally. Whether stakeholder messages were timely, consistent across audiences, and aligned with regulatory disclosure requirements is assessed in retrospect through management discussion rather than systematic review.
- Solution: The AI agent reads the outbound communications record, media coverage, and regulatory notification timeline for the resolved crisis. It assesses message consistency across stakeholder audiences, timing against regulatory notification windows, and sentiment trajectory in media coverage, and produces a structured review for the Head of Communications. The findings the Head of Communications accepts feed the next update cycle of the crisis scenario framework.
- OKR: The Head of Communications updates the crisis scenario framework from an AI-produced structured review of each resolved crisis — message consistency across stakeholder audiences, timing against regulatory notification windows, and media sentiment trajectory — rather than from informal lessons learned.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's narrative review produced for 100% of resolved crisis events within 12 months of go-live; all three assessment dimensions covered in every review. |
| Acceptance | ≥80% of review findings accepted by the Head of Communications as accurate; ≥1 crisis scenario framework update per reviewed crisis attributable to the review findings. |
| Cycle | Structured review delivered within 10 business days of crisis resolution, versus retrospective assessment through management discussion with no defined timeline. |

### Crisis Scenario Narrative Framework

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/crisis-response-narrative/crisis-scenario-narrative-framework
- Lens: Enablement
- Complexity: M
- Intent: The AI agent maps the Bank's plausible adverse scenarios — cyber incident, large credit loss, regulatory enforcement, executive conduct — to pre-drafted stakeholder-specific narrative frameworks, so the communications and risk teams have ready material at crisis onset.
- Problem to solve: In a crisis, the time available to assemble coherent stakeholder messaging for regulators, institutional investors, retail customers, and staff is shorter than the time required to draft from first principles. Pre-crisis preparation is typically limited to generic response templates not calibrated to the Bank's specific risk profile or regulatory standing.
- Solution: The AI agent reads the Bank's ICAAP stress scenarios, regulatory standing, material risk register, and prior crisis events. It generates scenario-specific narrative frameworks for each plausible adverse scenario, tailored to each stakeholder audience — regulator, investor, retail customer, staff — with modular components the communications team can activate and adapt at crisis onset. The CRO and Head of Communications review and approve the framework before filing in the crisis response library.
- OKR: The communications and risk teams hold, in the crisis response library, AI-generated narrative frameworks for each plausible adverse scenario — tailored to regulator, investor, retail customer, and staff audiences — reviewed and approved by the CRO and Head of Communications before a crisis occurs.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-generated frameworks covering all four adverse scenario types (cyber incident, large credit loss, regulatory enforcement, executive conduct) filed in the crisis response library within 12 months of go-live; all four stakeholder audiences covered in every framework. |
| Acceptance | ≥75% of frameworks approved by the CRO and Head of Communications with only minor amendment; frameworks rated as deployable without major revision in ≥75% of crisis exercises or live activations. |
| Cycle | Scenario framework regenerated within 5 business days of each update to the ICAAP stress scenarios or material risk register, versus generic response templates not calibrated to the Bank's risk profile. |

### Crisis Response Draft Generation

- URN: urn:financial-services:scenario:risk-control/strategic-reputational-risk/crisis-response-narrative/crisis-response-draft-generation
- Lens: Automation
- Complexity: M
- Intent: The AI agent generates stakeholder-specific crisis response drafts at crisis onset — regulator notification, investor statement, customer communication, and staff briefing — from the activated scenario framework and current event facts.
- Problem to solve: At crisis onset, communications and risk teams must produce stakeholder-specific messaging under severe time pressure with incomplete information. Drafting from a blank page under these conditions produces inconsistent tone, omits required regulatory disclosures, and consumes senior leadership attention that should be on incident management.
- Solution: The AI agent reads the activated crisis scenario framework, the current known facts of the incident, and regulatory notification requirements for the incident type. It generates drafts for each stakeholder audience — regulatory notification, investor statement, customer communication, and staff briefing — with disclosure fields clearly flagged for factual completion by the incident management team. The Head of Communications and General Counsel review before release.
- OKR: The Head of Communications and General Counsel review AI-generated crisis response drafts — regulator notification, investor statement, customer communication, and staff briefing, with fields needing factual completion flagged — rather than drafting from a blank page at crisis onset.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to generate stakeholder drafts in 100% of crisis activations and crisis exercises within 12 months of go-live; all four stakeholder drafts produced in every run. |
| Acceptance | ≥75% of drafts released by the Head of Communications and General Counsel with only factual completion and minor amendment; required regulatory disclosure elements present in 100% of regulator notification drafts. |
| Cycle | Full draft set available within 1 hour of scenario framework activation, versus several hours of drafting from a blank page by senior leadership under the prior approach. |
