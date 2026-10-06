# 

source: html-alt/financial-services/en/value-streams/index.html


[PAGE TEXT]
Customer-facing value streams
Deposits & Transaction Banking
Holding and moving customer money — accounts, payments, cards, transfers. The cycle anchor is the speed and integrity of moving value while staying compliant.
Deposits & Transaction Banking covers account opening, funding, payment initiation, card issuance, domestic and cross-border transfers, dispute handling, and ongoing account servicing. Transaction volume is high and operationally routine, yet exception handling, payment investigations, and dispute management consume disproportionate capacity. The regulatory overlay — NBKR payment system rules, NBK account-status reporting, FATF AML obligations — runs alongside every transaction, and compliance friction at the edges slows resolution cycles without reducing volume.
Analyze
Payment exception rates, dispute volumes, and transaction failure patterns are tracked in isolated system reports with no cross-channel aggregation. Operations managers reconstruct the picture each week from separate extracts; root causes of recurrent failure patterns remain attributed to one-off causes.
Optimize
Dispute routing and investigation sequencing are handler-driven and not informed by case complexity or resolution probability. Payment investigation queues grow during peak periods without workload-balancing logic; cases of similar type take materially different time depending on queue assignment.
Automate
Transaction investigation triage, dispute-response drafting, and complaint acknowledgment consume frontline analyst capacity on tasks that follow consistent resolution paths. Initiation-to-resolution for straightforward disputes runs days because each case enters a shared queue regardless of complexity.
Enrich
Spend-pattern intelligence from the transaction ledger is not systematically surfaced for product or pricing decisions. Interchange optimization, cohort-level churn signals, and balance-behavior shifts remain latent in the transaction data and are not acted on until lag indicators appear.
<button
class="flow-stages__stage"
type="button"
data-stage="account-opening"
data-flow-id="urn:financial-services:flow:deposits-transaction-banking"
>
Account opening
→
<button
class="flow-stages__stage"
type="button"
data-stage="fund"
data-flow-id="urn:financial-services:flow:deposits-transaction-banking"
>
Fund
→
<button
class="flow-stages__stage"
type="button"
data-stage="transact"
data-flow-id="urn:financial-services:flow:deposits-transaction-banking"
>
Transact
→
<button
class="flow-stages__stage"
type="button"
data-stage="service"
data-flow-id="urn:financial-services:flow:deposits-transaction-banking"
>
Service
→
<button
class="flow-stages__stage"
type="button"
data-stage="retain"
data-flow-id="urn:financial-services:flow:deposits-transaction-banking"
>
Retain
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] Dispute resolution automation
urn: urn:financial-services:scenario:flow/deposits-transaction-banking/dtb-dispute-resolution-automation
intent: End-to-end agent-driven resolution of straightforward dispute cases — documentation assembly, transaction context retrieval, customer communication drafting, and regulatory-deadline tracking — with analyst review reserved for contested or high-value cases. Initiation-to-resolution cycle time compresses materially for the majority of dispute volume.
Problem to solve: Transaction investigation triage, dispute-response drafting, and complaint acknowledgment consume frontline analyst capacity on tasks that follow consistent resolution paths. Straightforward disputes enter a shared queue regardless of complexity; resolution runs days because the case sequence is not differentiated by effort required.
Solution: Agent handles the full resolution sequence for structurally simple disputes: retrieves transaction context, assembles the documentation set, drafts the customer response, and tracks chargeback or payment-scheme deadlines. Analyst approval gates the customer-facing output and any credit or reversal action.
OKR objective: Straightforward dispute cases are resolved through an agent-driven end-to-end sequence covering documentation, transaction context retrieval, customer communication, and deadline tracking, with analyst approval gating customer-facing output and any credit or reversal action.
OKR KR [Adoption]: Agent manages the full resolution sequence for ≥70% of structurally simple dispute cases within 9 months of go-live.
OKR KR [Acceptance]: ≥85% of agent-drafted customer dispute responses accepted by analysts without material amendment before dispatch.
OKR KR [Cycle]: Dispute initiation-to-resolution cycle time for agent-managed cases reduced by ≥40% compared to the manual queue baseline within 12 months.

### CARD 2 [Enablement|S] KYC adaptive document sequencing
urn: urn:financial-services:scenario:flow/deposits-transaction-banking/dtb-kyc-adaptive-sequencing
intent: Adaptive KYC document request sequencing at account opening, ordered by segment-specific completion probability to improve first-attempt completion rates and reduce the activation-delay tail. The sequence adjusts based on customer segment, channel, and the KYC tier assigned at initiation.
Problem to solve: KYC completion rates drop when document requests are static and sequenced identically across customer segments. Activation delays carry into the transact stage; operational staff chase missing items while the account sits dormant.
Solution: Agent recommends the optimal document request sequence for each applicant based on segment, channel, and KYC-tier signals, presenting the highest-completion-probability requests first. Staff review the recommended sequence before customer contact; the model retrains on completion outcomes across the portfolio.
OKR objective: KYC document request sequencing at account opening adapts to customer segment, channel, and KYC tier to present the highest-completion-probability requests first, improving first-attempt completion rates and compressing the activation-delay tail.
OKR KR [Adoption]: Agent adaptive sequencing applied to ≥85% of retail and SME account openings across relevant KYC tiers within 6 months of go-live.
OKR KR [Acceptance]: ≥80% of recommended document sequences accepted by KYC operations staff without override before customer contact.
OKR KR [Cycle]: Average KYC completion lag from application initiation to document set completion reduced by ≥25% for agent-sequenced cases within 12 months.

### CARD 3 [Insights|M] Payment exception pattern analytics
urn: urn:financial-services:scenario:flow/deposits-transaction-banking/dtb-exception-pattern-analytics
intent: Cross-channel aggregation of payment exception rates, dispute volumes, and transaction failure patterns, classified by root cause and recurrence frequency. Operations managers receive a continuous view of systemic failures — beneficiary routing gaps, format mismatches, limit-breach patterns — without weekly reconstruction from separate system extracts.
Problem to solve: Exception and dispute patterns are tracked in isolated system reports with no cross-channel aggregation. Root causes of recurrent failure patterns remain attributed to one-off causes because the cross-channel picture is never assembled at the time the pattern forms.
Solution: Agent continuously reads exception and dispute data across channels, classifies cases by root-cause category, and surfaces recurrence patterns ranked by volume and resolution cost. Operations teams act on the pattern view; individual case handling proceeds with the benefit of systemic context.
OKR objective: Payment exception rates, dispute volumes, and transaction failure patterns are aggregated cross-channel and classified by root cause, giving operations a continuous systemic-failure view for targeted process and routing remediation.
OKR KR [Adoption]: Agent exception aggregation covers ≥95% of payment channels and exception types with daily updates within 6 months of go-live.
OKR KR [Acceptance]: ≥75% of agent-identified systemic failure patterns confirmed as actionable by operations managers in weekly pattern reviews.
OKR KR [Cycle]: Time from pattern emergence to operations-ready root-cause classification reduced from weekly manual report cycle to ≤24 hours on a continuous basis.

### CARD 4 [Optimize|M] STP routing and queue optimisation
urn: urn:financial-services:scenario:flow/deposits-transaction-banking/dtb-stp-routing-intelligence
intent: Routing optimisation for payment investigation and dispute queues based on case complexity, resolution probability, and handler workload. STP rates improve as structurally similar cases are separated from genuinely complex exceptions at the point of queue entry.
Problem to solve: Dispute routing and investigation sequencing are handler-driven with no complexity or resolution-probability signal at assignment. Cases of similar type take materially different time depending on queue assignment; peak-period backlogs grow without workload-balancing logic.
Solution: Agent scores incoming cases by complexity and estimated resolution path, routes straightforward disputes to auto-resolution tracks, and assigns complex or contested cases to experienced handlers. Queue rebalancing logic triggers during peak periods, maintaining consistent cycle-time targets.
OKR objective: Payment investigation and dispute queues are routed by case complexity and resolution probability at the point of queue entry, increasing STP rates by separating structurally routine cases from genuinely complex exceptions.
OKR KR [Adoption]: Agent complexity scoring and routing logic applied to ≥90% of incoming dispute and investigation cases within 6 months of go-live.
OKR KR [Acceptance]: ≥80% of auto-resolution routing decisions confirmed as correctly classified by analyst review within the first 3 months; ongoing false-routing rate ≤5%.
OKR KR [Cycle]: Dispute queue cycle time for agent-routed auto-resolution cases reduced by ≥50% compared to the pre-routing baseline within 12 months.

### CARD 5 [New opps|M] Transaction behaviour intelligence for product and pricing
urn: urn:financial-services:scenario:flow/deposits-transaction-banking/dtb-transaction-behavior-intelligence
intent: Continuous intelligence on cohort spend shifts, CASA balance-behavior changes, and interchange optimisation opportunities derived from the transaction ledger, surfaced for product and pricing decisions. The bank acts on behavioral signals before lag indicators appear in management reporting.
Problem to solve: Spend-pattern intelligence from the transaction ledger is not systematically surfaced for product or pricing decisions. Interchange optimisation, cohort-level churn signals, and balance-behavior shifts remain latent in the transaction data and are not acted on until lag indicators appear.
Solution: Agent monitors cohort-level transaction patterns, detects meaningful shifts in CASA balance behavior and spend mix, and surfaces actionable intelligence to product and pricing teams on a continuous cadence. Outputs are calibrated to decision windows — pricing reviews, product design cycles — rather than delivered at fixed reporting intervals.
OKR objective: Cohort spend shifts, CASA balance-behavior changes, and interchange optimisation opportunities are surfaced continuously from the transaction ledger to product and pricing teams at decision-relevant cadence.
OKR KR [Adoption]: Agent transaction intelligence delivered to product and pricing teams for ≥6 of 8 defined decision windows (pricing reviews, product design cycles) in the first 12 months.
OKR KR [Acceptance]: ≥75% of agent-surfaced behavioral signals accepted by product and pricing leadership as decision-informing without material reanalysis.
OKR KR [Cycle]: Interval from behavioral pattern emergence in the transaction ledger to product-team-reviewed intelligence output reduced from lag-indicator reporting (4–6 weeks) to ≤5 business days on a continuous basis.

[PAGE TEXT]
Lending
Credit products across retail, SME, corporate, and mortgage. The cycle anchor is decision time — from application to funded — while keeping risk discipline.
Lending originates credit across retail, SME, corporate, and mortgage segments — application intake, KYC and credit assessment, decision, documentation, funding, and post-origination servicing. Decision cycle time ranges from minutes for retail unsecured to weeks for complex SME and corporate cases. The cycle's competing pressures are speed (customer expectation, competitor benchmarks) and discipline (credit quality, regulatory adherence, fraud control), and most of the improvement headroom sits in the hand-offs between intake, underwriting, credit committee, and funding teams.
Analyze
Origination cycle-time, queue depth at credit review, and exception patterns are reconstructed manually each cycle from disconnected case-management systems. Underwriters and credit-committee secretaries lack a live picture of which applications are stalled and why.
Optimize
Routing decisions (fast-track vs. full review), document-collection sequencing, and credit-committee batching are set at the policy level and rarely retuned. Each segment's optimization headroom requires multi-day modeling that competes with day-to-day origination throughput.
Automate
Document collection, status updates to customers and intermediaries, low-risk decisioning under a threshold, and post-origination notification cascades all consume frontline analyst time. Most steps are rule-driven and prescribed — the structural similarity across applications makes them ripe for end-to-end automation.
Enrich
Optimization wins in retail rarely transfer to SME or corporate; cross-segment learnings stay siloed. Trial of new lending products (new structures, new collateral types) requires multi-week setup before the first application can be processed.
<button
class="flow-stages__stage"
type="button"
data-stage="application"
data-flow-id="urn:financial-services:flow:lending"
>
Application
→
<button
class="flow-stages__stage"
type="button"
data-stage="underwriting"
data-flow-id="urn:financial-services:flow:lending"
>
Underwriting
→
<button
class="flow-stages__stage"
type="button"
data-stage="decision"
data-flow-id="urn:financial-services:flow:lending"
>
Decision
→
<button
class="flow-stages__stage"
type="button"
data-stage="documentation"
data-flow-id="urn:financial-services:flow:lending"
>
Documentation
→
<button
class="flow-stages__stage"
type="button"
data-stage="funding"
data-flow-id="urn:financial-services:flow:lending"
>
Funding
→
<button
class="flow-stages__stage"
type="button"
data-stage="servicing"
data-flow-id="urn:financial-services:flow:lending"
>
Servicing
Lens
Scenario
Intent
Complexity

### CARD 6 [Automation|S] Credit document collection and notification automation
urn: urn:financial-services:scenario:flow/lending/lending-doc-collection-automation
intent: Agent-managed document collection, customer and intermediary status notifications, and post-decision notification cascades for structurally similar retail and SME credit applications. Analyst capacity is directed toward exception handling and complex documentation requirements rather than routine follow-up.
Problem to solve: Document collection, status updates to customers and intermediaries, and post-origination notification cascades consume frontline analyst time on tasks that are rule-driven and prescribed. Structural similarity across applications makes the full sequence a candidate for end-to-end automation.
Solution: Agent orchestrates the document-collection sequence — request dispatch, receipt confirmation, and missing-item escalation — and sends structured status updates at defined origination milestones. Post-decision notifications to customer, intermediary, and downstream systems are dispatched automatically with analyst review of exceptions.
OKR objective: Document collection, customer and intermediary status notifications, and post-decision notification cascades for structurally similar retail and SME credit applications are agent-orchestrated, with analyst capacity directed toward exception handling.
OKR KR [Adoption]: Agent manages the end-to-end document collection and notification sequence for ≥80% of eligible retail and SME credit applications within 9 months of go-live.
OKR KR [Acceptance]: ≥85% of agent-dispatched post-decision notifications accepted by analysts as accurate and complete without correction before customer delivery.
OKR KR [Cycle]: Average document collection cycle time from application intake to complete documentation set reduced by ≥30% for agent-managed applications within 12 months.

### CARD 7 [Insights|M] Lending origination queue intelligence
urn: urn:financial-services:scenario:flow/lending/lending-origination-queue-intelligence
intent: Continuous view of origination cycle time, queue depth at credit review, and exception patterns across retail, SME, and corporate tracks — without manual reconstruction from disconnected case-management systems. Operations and credit leadership see which applications are stalled, at which stage, and for what reason, in real time.
Problem to solve: Origination cycle time, queue depth at credit review, and exception patterns are reconstructed manually each cycle from disconnected case-management systems. Underwriters and credit-committee secretaries lack a live picture of which applications are stalled and why.
Solution: Agent reads across origination systems, classifies queue-state and stall reasons per application, and produces a continuous dashboard of cycle-time distribution and exception patterns by segment and underwriting track. Credit operations acts on the live view; monthly reporting is generated from the same data feed.
OKR objective: Origination cycle time, queue depth at credit review, and stall reasons across retail, SME, and corporate tracks are continuously visible from aggregated case management systems, replacing manual reconstruction each cycle.
OKR KR [Adoption]: Agent origination queue dashboard covers ≥95% of active applications across all tracks with intraday updates within 6 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-produced queue intelligence views accepted by credit operations as decision-ready without manual supplementation.
OKR KR [Cycle]: Time from queue-state change to operations-visible stall classification reduced from weekly manual reconstruction to ≤4 hours on a continuous basis.

### CARD 8 [Optimize|M] Underwriting capacity and routing optimisation
urn: urn:financial-services:scenario:flow/lending/lending-underwriting-capacity-optimisation
intent: Dynamic routing of credit applications to fast-track, delegated-authority, or full-review tracks based on policy-eligible signals at intake, reducing senior-underwriter time on cases that policy already determines. Credit committee batching is reordered by urgency and completeness to maintain throughput.
Problem to solve: Routing decisions — fast-track versus full review — and credit-committee batching are set at the policy level and rarely retuned. Senior underwriters spend disproportionate time on cases that policy already approves and on applications requiring early decline; optimisation headroom requires multi-day modeling.
Solution: Agent evaluates each application at intake against current policy parameters and routes it to the appropriate review track with a confidence score. Committee scheduling logic groups applications by completeness and decision-readiness; the credit secretariat reviews and confirms routing before cases move to the next stage.
OKR objective: Credit applications are dynamically routed to fast-track, delegated-authority, or full-review tracks based on policy-eligible signals at intake, with committee batching sequenced by completeness and urgency to sustain throughput.
OKR KR [Adoption]: Agent routing recommendations applied to ≥85% of incoming credit applications within 6 months of go-live; committee scheduling logic deployed for ≥95% of weekly credit committee sessions.
OKR KR [Acceptance]: ≥80% of agent routing recommendations confirmed by credit secretariat without override before case advancement.
OKR KR [Cycle]: Average senior-underwriter time per straightforward policy-eligible case reduced by ≥35% within 12 months of go-live.

### CARD 9 [Enablement|M] Credit decision copilot for underwriters
urn: urn:financial-services:scenario:flow/lending/lending-credit-decision-copilot
intent: Structured synthesis of application data, bureau scores, collateral assessment, and policy-edge flags presented to underwriters at the point of case review. Credit committee pre-reads are assembled from the same synthesis, reducing preparation time and compressing the lag between application intake and committee-ready documentation.
Problem to solve: Underwriters and credit-committee secretaries reconstruct application context manually from separate case-management systems each cycle. Decision explainability for delegated-authority cases is limited, and policy-edge flags surface in committee rather than before it.
Solution: Agent assembles a structured case brief for each application — credit score, capacity-and-willingness summary, collateral status, policy flags, and comparable precedents — and presents it to the underwriter before review. Committee pre-reads are generated from the same structured inputs; underwriter edits the brief before it advances to committee.
OKR objective: Underwriters receive a structured case brief — credit score, capacity-and-willingness summary, collateral status, policy flags, and precedents — at the point of case review, with credit committee pre-reads assembled from the same synthesis.
OKR KR [Adoption]: Agent case brief used by underwriters for ≥85% of credit applications across retail and SME tracks within 9 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-assembled committee pre-reads accepted by credit secretariat as ready for distribution without material reconstruction.
OKR KR [Cycle]: Average preparation time from application intake to committee-ready documentation reduced by ≥40% within 12 months of go-live.

### CARD 10 [New opps|M] Cross-segment lending learning transfer
urn: urn:financial-services:scenario:flow/lending/lending-cross-segment-learning-transfer
intent: Systematic propagation of policy-edge learnings, optimisation wins, and exception patterns from retail origination to SME and corporate tracks, reducing the structural siloing that currently prevents cross-segment credit intelligence from improving origination quality across the bank.
Problem to solve: Optimisation wins in retail rarely transfer to SME or corporate; cross-segment learnings stay siloed. Servicing operations run in isolation from origination data; modification and exception patterns do not feed back into origination policy.
Solution: Agent identifies policy-edge cases, exception patterns, and performance outliers across origination segments and classifies each for cross-segment applicability. A structured learning brief is distributed to credit policy owners quarterly; changes to routing rules or documentation requirements are reviewed by credit risk before adoption.
OKR objective: Policy-edge learnings, optimisation wins, and exception patterns from retail origination are systematically propagated to SME and corporate credit policy owners, reducing structural siloing across lending segments.
OKR KR [Adoption]: Agent identifies and classifies cross-segment learnings from ≥80% of finalised exception and outlier cases for ≥4 consecutive quarterly learning brief distributions within the first year.
OKR KR [Acceptance]: ≥65% of agent-distributed cross-segment learning briefs result in credit policy owner review and a documented accept/reject decision within 30 days.
OKR KR [Cycle]: Time from exception pattern identification in one origination segment to credit-policy-reviewed learning note in applicable peer segments reduced to ≤45 days.

[PAGE TEXT]
Wealth Management
Investment, advisory, and portfolio management for affluent and institutional clients. The cycle anchor is the advisory journey from goals to allocation to ongoing rebalancing.
Wealth Management covers client onboarding, goals-based financial planning, portfolio construction, trade execution, ongoing monitoring, and periodic review and rebalancing across affluent and high-net-worth segments. The relationship manager (RM) is the cycle's rate-limiting resource — client preparation, investment committee pre-reads, and portfolio review packs each draw on RM time before the client interaction occurs. The advisory cycle compounds the bottleneck: RM capacity spent in preparation is unavailable for client coverage, constraining the book size each RM can serve at advisory quality.
Analyze
Portfolio performance attribution across asset classes, custodians, and client mandates is assembled from separate system extracts each review cycle. RM and investment committee have no continuous view of which mandates are drifting from strategic allocation or how book-level performance compares to benchmark.
Optimize
RM time allocation across client-facing and back-office preparation tasks is not tracked or rebalanced. High-effort preparation tasks — review packs, IC pre-reads, DD synthesis — consume fixed hours per client regardless of mandate complexity or review materiality.
Automate
Client review pack assembly, investment committee pre-read drafting, and post-meeting follow-up extraction are fully manual. Each of these tasks is structurally similar across clients and cycles — text synthesis from structured inputs — and absorbs disproportionate RM capacity.
Enrich
Prospect pipeline intelligence and competitor positioning are gathered informally by RMs before prospect meetings. The institutional knowledge embedded in completed portfolio reviews, client interaction histories, and investment thesis notes is not systematically reused across the advisory team.
<button
class="flow-stages__stage"
type="button"
data-stage="discover"
data-flow-id="urn:financial-services:flow:wealth-management"
>
Discover
→
<button
class="flow-stages__stage"
type="button"
data-stage="plan"
data-flow-id="urn:financial-services:flow:wealth-management"
>
Plan
→
<button
class="flow-stages__stage"
type="button"
data-stage="construct"
data-flow-id="urn:financial-services:flow:wealth-management"
>
Construct
→
<button
class="flow-stages__stage"
type="button"
data-stage="implement"
data-flow-id="urn:financial-services:flow:wealth-management"
>
Implement
→
<button
class="flow-stages__stage"
type="button"
data-stage="monitor"
data-flow-id="urn:financial-services:flow:wealth-management"
>
Monitor
→
<button
class="flow-stages__stage"
type="button"
data-stage="review"
data-flow-id="urn:financial-services:flow:wealth-management"
>
Review
Lens
Scenario
Intent
Complexity

### CARD 11 [Automation|S] Client review pack and IC pre-read automation
urn: urn:financial-services:scenario:flow/wealth-management/wm-review-pack-automation
intent: Agent assembly of client review packs, investment committee pre-reads, and post-meeting follow-up extracts from structured performance, market, and client-plan inputs. RM capacity released from preparation is directed toward client coverage and prospecting.
Problem to solve: Client review pack assembly, investment committee pre-read drafting, and post-meeting follow-up extraction are fully manual. Each task is structurally similar across clients and cycles — text synthesis from structured inputs — yet absorbs 3-5 hours of RM time per client per review cycle.
Solution: Agent assembles the review pack from performance reports, allocation data, market commentary, and the client's original plan. The RM reviews and edits the draft before client distribution; post-meeting action items are extracted from the meeting record and assigned with deadlines.
OKR objective: Client review packs, investment committee pre-reads, and post-meeting follow-up extracts are assembled by agent from structured performance, market, and client-plan inputs, with RMs reviewing and editing before client distribution.
OKR KR [Adoption]: Agent assembles the review pack for ≥85% of scheduled client reviews across the advisory book within 9 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-assembled review packs accepted by RMs as requiring editing rather than full redraft before client distribution.
OKR KR [Cycle]: RM preparation time per client review cycle reduced from 3-5 hours of manual assembly to ≤45 minutes of review and editing within 12 months of go-live.

### CARD 12 [Enablement|S] Advisory discovery and suitability capture enablement
urn: urn:financial-services:scenario:flow/wealth-management/wm-discovery-capture-enablement
intent: Structured in-meeting capture of client goals, risk tolerance, liquidity needs, and existing holdings, with the investment policy statement drafted by agent for RM review and approval post-meeting. Downstream stages — planning, construction — receive consistent, complete discovery inputs rather than reconstructed RM notes.
Problem to solve: Discovery documentation is completed post-meeting from RM notes; structured data capture is incomplete and inconsistent across advisors. Gaps surface during portfolio construction rather than at the discovery conversation, requiring the RM to re-engage the client for missing information.
Solution: Agent provides the RM with a structured discovery guide and captures responses during the meeting using a mobile-accessible interface. The investment policy statement draft is generated immediately post-meeting for RM review; the RM approves or edits before client signature and downstream system update.
OKR objective: Structured discovery data — client goals, risk tolerance, liquidity needs, and existing holdings — is captured consistently across advisory conversations, with the investment policy statement drafted by agent for RM review and approval post-meeting.
OKR KR [Adoption]: Agent discovery capture and IPS drafting used by RMs for ≥80% of new client discovery meetings within 9 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-drafted investment policy statements accepted by RMs as requiring editing rather than full redraft before client signature.
OKR KR [Cycle]: Time from discovery meeting completion to approved IPS available for downstream planning reduced from multi-day post-meeting reconstruction to ≤24 hours.

### CARD 13 [Insights|M] Wealth portfolio drift and mandate-breach monitoring
urn: urn:financial-services:scenario:flow/wealth-management/wm-portfolio-drift-monitoring
intent: Continuous monitoring of portfolio positions against mandate constraints, strategic allocation bands, and client-specific thresholds — with intraday breach detection replacing end-of-day batch reporting. The investment committee and RMs receive an alert feed calibrated to materiality rather than batch-cycle cadence.
Problem to solve: Portfolio monitoring relies on end-of-day position snapshots from custody systems. Breaches of allocation bands or mandate constraints are flagged in the following day's report; intraday events that cross client thresholds go undetected until the next batch run.
Solution: Agent reads intraday position data from custody feeds, evaluates positions against mandate and client-specific parameters, and generates a prioritised alert feed for investment operations and RMs. Alert materiality thresholds are set per mandate type; the RM reviews and approves any rebalancing action before execution.
OKR objective: Portfolio positions are monitored continuously against mandate constraints, strategic allocation bands, and client-specific thresholds with intraday breach detection, replacing end-of-day batch reporting.
OKR KR [Adoption]: Agent intraday monitoring covers ≥95% of active mandates and client portfolios with position refresh intervals of ≤30 minutes within 6 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-generated breach alerts confirmed as actionable by investment operations and RMs within the first 3 months; ongoing false-alert rate ≤5%.
OKR KR [Cycle]: Portfolio breach detection lag reduced from end-of-day batch to intraday real-time monitoring within ≤30 minutes of position event.

### CARD 14 [Optimize|M] RM time allocation and book-capacity optimisation
urn: urn:financial-services:scenario:flow/wealth-management/wm-rm-time-allocation-optimisation
intent: Rebalancing of RM time across client-facing and back-office preparation tasks based on mandate complexity and review materiality, enabling each RM to serve a larger book at advisory quality. Preparation effort is directed toward reviews with the highest complexity and commercial significance rather than distributed uniformly.
Problem to solve: RM time allocation across client-facing and back-office preparation tasks is not tracked or rebalanced. High-effort preparation tasks — review packs, IC pre-reads, DD synthesis — consume fixed hours per client regardless of mandate complexity or review materiality.
Solution: Agent tracks preparation effort per client across review cycles, identifies where high RM time consumption does not correspond to mandate complexity or AUM materiality, and recommends reallocation. The head of wealth reviews the time-allocation analysis quarterly; agent-assisted preparation covers low-complexity reviews, freeing RM hours for high-value client engagement.
OKR objective: RM preparation effort is rebalanced across the client book on the basis of mandate complexity and review materiality, enabling each RM to serve a larger book at advisory quality.
OKR KR [Adoption]: Agent time-allocation analysis reviewed by the head of wealth for ≥4 consecutive quarters within the first year; reallocation recommendations applied across ≥80% of the advisory book.
OKR KR [Acceptance]: ≥75% of agent-recommended preparation-effort reallocation decisions accepted by the head of wealth without material revision.
OKR KR [Cycle]: Average RM preparation hours per low-complexity review cycle reduced by ≥40% within 12 months of go-live, with released hours verified against time-recording data.

### CARD 15 [New opps|M] Wealth prospect and competitive intelligence enrichment
urn: urn:financial-services:scenario:flow/wealth-management/wm-prospect-intelligence-enrichment
intent: Systematic reuse of institutional knowledge from completed portfolio reviews, client interaction histories, and investment thesis notes for prospect preparation and competitive positioning across the advisory team. Prospect meetings are informed by the bank's own asset-class experience and client outcome history rather than relying on individual RM knowledge.
Problem to solve: Prospect pipeline intelligence and competitor positioning are gathered informally by individual RMs before prospect meetings. The institutional knowledge embedded in completed reviews, client histories, and investment thesis notes is not systematically reused across the advisory team.
Solution: Agent indexes completed reviews, investment thesis notes, and client outcome data, and assembles a prospect brief on request — relevant asset-class experience, comparable client profiles, and competitive positioning. The RM reviews the brief before the prospect meeting; the knowledge base is updated after each completed engagement.
OKR objective: Institutional knowledge from completed portfolio reviews, client interaction histories, and investment thesis notes is systematically indexed and assembled into prospect briefs, giving the advisory team consistent preparation across the book.
OKR KR [Adoption]: Agent prospect brief used by RMs for ≥75% of qualified prospect meetings within 9 months of go-live; knowledge base updated after ≥85% of completed engagements.
OKR KR [Acceptance]: ≥75% of agent-produced prospect briefs accepted by RMs as decision-informing without material supplementation before prospect meeting.
OKR KR [Cycle]: Time from prospect meeting request to RM-reviewed brief reduced from informal multi-day information gathering to ≤4 hours.

[PAGE TEXT]
Bancassurance (insurance distribution)
Insurance distribution through the bank's channels. The cycle anchor is the cross-sell journey at the moment of customer life events.
Bancassurance distributes insurance products — life, mortgage protection, general, and health — through the bank's branch, digital, and relationship-banking channels, typically under partnership or captive insurer arrangements. The cycle anchors on life-event triggers: a mortgage origination prompts mortgage protection, a salary increase prompts life and savings-linked products, a business loan prompts trade credit or key-man cover. Frontline staff capacity to identify the trigger, position the offer, and support the sale conversation is the primary constraint — not product breadth or customer eligibility.
Analyze
Insurance conversion rates by channel, frontline staff, and product are tracked at the total level without decomposition by trigger type, offer stage, or customer segment. The bank cannot identify which life-event triggers carry the highest conversion probability or where the offer conversation most commonly breaks down.
Optimize
Frontline staff positioning of insurance products is not supported by real-time guidance on which product to offer, what to say, or how to handle common objections. Staff rely on periodic training and printed product guides; offer quality and compliance-disclosure completeness are not measured per interaction.
Automate
Post-sale policy documentation, disclosure pack delivery, and premium setup each require separate manual steps. The sequence between sale agreement and policy binding involves handoffs across bancassurance operations, the partner insurer's platform, and the bank's payment system.
Enrich
Customer eligibility and propensity intelligence from the bank's account data are not systematically used to rank which customers to contact for which product. Cross-sell targeting is driven by product campaigns rather than behavioral signals from the customer's transactional relationship with the bank.
<button
class="flow-stages__stage"
type="button"
data-stage="identify"
data-flow-id="urn:financial-services:flow:bancassurance"
>
Identify trigger
→
<button
class="flow-stages__stage"
type="button"
data-stage="position"
data-flow-id="urn:financial-services:flow:bancassurance"
>
Position offer
→
<button
class="flow-stages__stage"
type="button"
data-stage="underwrite"
data-flow-id="urn:financial-services:flow:bancassurance"
>
Underwrite
→
<button
class="flow-stages__stage"
type="button"
data-stage="sell-onboard"
data-flow-id="urn:financial-services:flow:bancassurance"
>
Sell & onboard
→
<button
class="flow-stages__stage"
type="button"
data-stage="retain"
data-flow-id="urn:financial-services:flow:bancassurance"
>
Retain
Lens
Scenario
Intent
Complexity

### CARD 16 [Enablement|S] Insurance positioning and disclosure enablement for frontline staff
urn: urn:financial-services:scenario:flow/bancassurance/banc-frontline-positioning-enablement
intent: Real-time product positioning guidance and compliance-disclosure prompts for frontline staff at the point of a customer life-event trigger, calibrated to the specific product and customer profile. Offer quality and disclosure completeness are consistent across the channel rather than dependent on individual training recency.
Problem to solve: Frontline staff have inconsistent familiarity with insurance product features and compliance disclosure requirements. Positioning quality depends on individual training recency; customers receive offers at different depths and with variable disclosure completeness across the channel.
Solution: Agent surfaces a product-specific positioning guide and mandatory disclosure checklist to the frontline staff member at the point of the identified trigger. The guide adapts to the product being offered and the customer's profile; the staff member confirms disclosure completion before closing the offer conversation.
OKR objective: Insurance product positioning quality and compliance disclosure completeness are consistent across frontline channels, with real-time guidance calibrated to the specific product and customer profile at the point of each life-event trigger.
OKR KR [Adoption]: Agent-supplied positioning guide and disclosure checklist used by frontline staff for ≥85% of insurance offer conversations within 6 months.
OKR KR [Acceptance]: ≥90% of disclosure completion confirmations accepted by compliance review as complete and accurate without remediation.
OKR KR [Cycle]: Average time from trigger identification to offer-ready frontline presentation reduced from same-day manual retrieval to ≤2 minutes per interaction.

### CARD 17 [Automation|S] Bancassurance policy onboarding automation
urn: urn:financial-services:scenario:flow/bancassurance/banc-policy-onboarding-automation
intent: Agent-driven post-sale sequence — policy documentation generation, disclosure pack delivery, premium collection setup, and insurer platform handoff — reducing the manual steps between sale agreement and policy binding. Drop-off between sale and bound policy is reduced by eliminating the separate operational steps that currently interrupt the sequence.
Problem to solve: Post-sale policy documentation, disclosure pack delivery, and premium setup each require separate manual steps across bancassurance operations, the partner insurer's platform, and the bank's payment system. Completion rate drops between sale agreement and policy binding as handoffs accumulate.
Solution: Agent triggers the post-sale sequence on sale confirmation — generates the documentation pack, delivers disclosure materials through the customer's preferred channel, initiates premium setup, and submits the policy application to the insurer's platform. Operations reviews the status feed and intervenes on exceptions; the customer receives a single coordinated communication.
OKR objective: The post-sale policy onboarding sequence — documentation, disclosure delivery, premium setup, and insurer platform handoff — is agent-driven from sale confirmation to policy binding, with operations reviewing exceptions.
OKR KR [Adoption]: Agent manages the end-to-end post-sale sequence for ≥85% of eligible bancassurance policy sales within 6 months of go-live.
OKR KR [Acceptance]: ≥90% of agent-generated documentation packs accepted by bancassurance operations without manual rework before insurer submission.
OKR KR [Cycle]: Sale-to-bound-policy cycle time reduced by ≥40% for eligible policies within 12 months of go-live.

### CARD 18 [Insights|M] Bancassurance conversion and trigger analytics
urn: urn:financial-services:scenario:flow/bancassurance/banc-conversion-trigger-analytics
intent: Decomposition of insurance conversion rates by life-event trigger type, channel, frontline staff, and offer stage, identifying which triggers carry the highest conversion probability and where the offer conversation breaks down. Product and training investments are directed at the highest-return points in the sales funnel.
Problem to solve: Insurance conversion rates by channel, staff, and product are tracked at the total level without decomposition by trigger type, offer stage, or customer segment. The bank cannot identify which life-event triggers carry the highest conversion probability or where the offer conversation most commonly breaks down.
Solution: Agent classifies each insurance interaction by trigger type, offer stage, and outcome, assembles a conversion funnel view by segment and channel, and surfaces it to the bancassurance and frontline leadership teams. Training and script adjustments are directed at the stages with the highest observed drop-off rates.
OKR objective: Conversion analytics are decomposed by trigger type, offer stage, channel, and frontline staff, directing product investment and training to the highest-return points in the bancassurance sales funnel.
OKR KR [Adoption]: Agent classifies ≥90% of insurance interactions by trigger type and offer stage within 3 months of go-live.
OKR KR [Acceptance]: ≥80% of funnel decomposition views accepted by bancassurance and frontline leadership without material amendment.
OKR KR [Cycle]: Conversion analysis cycle time reduced from multi-week manual reconstruction to a continuously refreshed view available within 24 hours of request.

### CARD 19 [Optimize|M] Insurance offer sequencing and propensity optimisation
urn: urn:financial-services:scenario:flow/bancassurance/banc-offer-sequencing-optimisation
intent: Propensity-ranked insurance offer sequencing based on transaction and account behavioral signals from the bank's own data, replacing product-campaign-driven targeting with customer-need-driven contact prioritisation. Frontline staff and digital channels engage customers with the offer most likely to convert at the right moment in the customer's lifecycle.
Problem to solve: Customer eligibility and propensity intelligence from the bank's account data are not systematically used to rank which customers to contact for which product. Cross-sell targeting is driven by product campaigns rather than behavioral signals from the customer's transactional relationship with the bank.
Solution: Agent scores the customer base by product propensity using transaction, balance, and life-event signals, and produces a ranked contact list for frontline and digital channels. Campaign management reviews the propensity rankings before contact execution; actual conversion data retrains the propensity model on a rolling basis.
OKR objective: Insurance cross-sell contact sequencing is driven by customer propensity scores derived from transaction and account behavioral data, replacing product-campaign-based targeting.
OKR KR [Adoption]: Agent propensity rankings used for ≥80% of bancassurance contact prioritisation decisions across frontline and digital channels within 9 months.
OKR KR [Acceptance]: ≥75% of ranked contact lists accepted by campaign management without material reordering.
OKR KR [Cycle]: Time from data cut to distribution-ready propensity-ranked contact list reduced from multi-week modeling cycle to ≤48 hours on a rolling basis.

### CARD 20 [New opps|M] Policy lapse early-warning and retention
urn: urn:financial-services:scenario:flow/bancassurance/banc-lapse-early-warning
intent: Early-warning signals for policy lapse risk derived from intermediate behavioral indicators — missed premiums, life-event changes, balance-behavior shifts — enabling proactive retention contact before the customer's renewal decision is made. Lapse intervention is most effective in the window before the decision point, not after it.
Problem to solve: Policy lapse events are identified at renewal only, after the customer has already decided to discontinue. Intermediate signals — missed premiums, life-event changes, balance-behavior shifts — are not used to initiate proactive retention contact.
Solution: Agent monitors premium payment behavior, life-event signals in transaction data, and account balance trends for active policyholders, and generates a lapse-risk score updated monthly. Relationship managers and bancassurance operations receive a ranked retention contact list with the primary signal driving each customer's risk score; outreach is personalised to the identified trigger.
OKR objective: Proactive retention contact is initiated in the pre-decision window for at-risk policyholders, using behavioral and premium payment signals to identify lapse risk before the customer's renewal decision is made.
OKR KR [Adoption]: Agent lapse-risk scoring covers ≥95% of the active policyholder base on a monthly cadence within 6 months of go-live.
OKR KR [Acceptance]: ≥75% of agent-flagged high-risk retention cases confirmed as actionable by relationship managers and bancassurance operations.
OKR KR [Cycle]: Lapse-risk identification lead time extended from policy renewal date to ≥60 days prior, measured across the retained policyholder portfolio.

[PAGE TEXT]
Treasury & Funding
Bank self-funding and institutional liquidity. The cycle anchor is the funding-decision rhythm against the maturity ladder.
Treasury & Funding covers the bank's own balance-sheet funding — cash forecasting, wholesale and retail funding execution, intraday and structural liquidity management, asset-liability matching, and the reporting and narrative cycle to ALCO, the board, and regulators (NBKR, NBK, and under Basel III LCR/NSFR standards). The cycle's competing constraints are funding cost minimization and regulatory liquidity floor maintenance; most of the friction sits in forecast accuracy, intraday liquidity visibility, and the narrative production cycle that runs alongside every ALCO meeting.
Analyze
Funding cost, liquidity ratio headroom, and forecast accuracy are tracked in static reports produced for each ALCO cycle. Treasury has no continuous view of forecast error attribution, funding cost decomposition by instrument, or how regulatory ratio headroom is evolving across the inter-ALCO period.
Optimize
Funding mix decisions are made weekly against a point-in-time view of costs and ratios. Scenario analysis across instrument options — comparing cost against LCR, NSFR, and leverage impacts — is manual and takes hours; the window for acting on intraweek market opportunities is often missed.
Automate
ALCO pack assembly, regulatory return production, and the narrative explaining liquidity position changes are fully manual each cycle. The process is structurally similar across periods — pulling data from known sources, applying consistent methodology, narrating variances — and is the primary constraint on ALCO preparation quality.
Enrich
Rating agency and counterparty due diligence cycles create episodic demands on Treasury for structured narrative on funding strategy, liquidity position, and capital adequacy. These demands are handled reactively with bespoke document production each time, drawing on institutional knowledge held in individuals.
<button
class="flow-stages__stage"
type="button"
data-stage="forecast"
data-flow-id="urn:financial-services:flow:treasury-funding"
>
Forecast
→
<button
class="flow-stages__stage"
type="button"
data-stage="plan"
data-flow-id="urn:financial-services:flow:treasury-funding"
>
Plan funding
→
<button
class="flow-stages__stage"
type="button"
data-stage="execute"
data-flow-id="urn:financial-services:flow:treasury-funding"
>
Execute
→
<button
class="flow-stages__stage"
type="button"
data-stage="monitor"
data-flow-id="urn:financial-services:flow:treasury-funding"
>
Monitor
→
<button
class="flow-stages__stage"
type="button"
data-stage="report"
data-flow-id="urn:financial-services:flow:treasury-funding"
>
Report & narrate
Lens
Scenario
Intent
Complexity

### CARD 21 [New opps|S] Rating agency and counterparty posture brief
urn: urn:financial-services:scenario:flow/treasury-funding/trs-rating-agency-posture-brief
intent: On-demand posture briefing for rating-agency and counterparty due diligence interactions, assembled from the bank's current funding strategy, liquidity position, and capital adequacy data. Agency-relationship leads work from a current-state brief rather than spending days on bespoke manual reconstruction for each interaction.
Problem to solve: Rating agency and counterparty due diligence cycles create episodic demands on Treasury for structured narrative on funding strategy, liquidity position, and capital adequacy. These demands are handled reactively with bespoke document production each time, drawing on institutional knowledge held in individuals.
Solution: Agent maintains a continuous treasury posture summary in structured form — funding strategy rationale, current LCR/NSFR levels, capital adequacy overview, and key sensitivity narratives — and assembles an agency-facing brief on demand. Treasury leadership reviews and approves the brief before distribution; prior briefings are retained for consistency tracking across agency interaction cycles.
OKR objective: On-demand posture briefings for rating agency and counterparty due diligence interactions are assembled from the bank's continuously maintained treasury posture summary, with Treasury leadership reviewing and approving each brief before distribution.
OKR KR [Adoption]: Agent assembles a posture brief for ≥100% of rating agency and counterparty due diligence requests within 3 hours of request for the first 12 months of go-live.
OKR KR [Acceptance]: ≥85% of agent-produced posture briefs accepted by Treasury leadership without material amendment before distribution; consistency review confirms alignment with prior briefings in ≥90% of cases.
OKR KR [Cycle]: Briefing preparation time reduced from multi-day bespoke document production to ≤3 hours from Treasury leadership review request to approved brief.

### CARD 22 [Insights|M] Treasury cash forecast accuracy attribution
urn: urn:financial-services:scenario:flow/treasury-funding/trs-forecast-accuracy-attribution
intent: Continuous attribution of cash forecast errors by source, horizon, and instrument type, giving Treasury a running view of where accuracy degrades across the 5-30 day horizon and which behavioral deposit assumptions carry the most variance. Forecast buffers are calibrated to identified error patterns rather than held at uniform levels.
Problem to solve: Funding cost, liquidity ratio headroom, and forecast accuracy are tracked in static reports produced for each ALCO cycle. Treasury has no continuous view of forecast error attribution or how regulatory ratio headroom is evolving across the inter-ALCO period.
Solution: Agent tracks each cash forecast cohort from production to realisation, attributes errors to source — behavioral deposit variance, payment system timing, wholesale maturity rollover — and produces a continuous accuracy view by horizon. Treasury uses the attribution to adjust buffer levels and refine the behavioral deposit model assumptions presented at ALCO.
OKR objective: Cash forecast errors are attributed continuously by source, horizon, and instrument type, giving Treasury a running view of where accuracy degrades across the 5-30 day horizon and which behavioral deposit assumptions carry the most variance.
OKR KR [Adoption]: Agent tracks forecast cohorts from production to realisation for ≥95% of published cash forecasts across active horizons within 6 months of go-live.
OKR KR [Acceptance]: ≥80% of agent attribution views accepted by Treasury as accurate and decision-ready for buffer calibration and behavioral deposit model adjustment at each ALCO cycle.
OKR KR [Cycle]: Interval from forecast period realisation to attribution-complete accuracy view available to Treasury reduced from the next ALCO cycle preparation to ≤3 business days.

### CARD 23 [Optimize|M] Funding mix scenario optimisation
urn: urn:financial-services:scenario:flow/treasury-funding/trs-funding-mix-scenario-optimisation
intent: Rapid scenario comparison of funding instrument mixes against LCR, NSFR, and leverage ratio targets, enabling intraweek funding decisions without multi-hour manual spreadsheet analysis. Treasury acts on intraweek market opportunities within the window they are available rather than after the window has closed.
Problem to solve: Funding mix decisions are made against a point-in-time weekly view. Scenario analysis across instrument options — comparing cost against LCR, NSFR, and leverage impacts — is manual and takes hours; the window for acting on intraweek market opportunities is often missed.
Solution: Agent runs funding-mix scenarios on demand — specifying instrument type, volume, and tenor — and returns the cost, ratio, and maturity-ladder impact within minutes. Treasury reviews the scenario output before any execution; the model is updated with live rate and ratio data from treasury systems.
OKR objective: Funding-mix scenario comparison across instrument types, volumes, and tenors — evaluated against LCR, NSFR, and leverage ratio impacts — is available to Treasury within minutes of parameter entry, enabling intraweek market opportunities to be acted on within the available window.
OKR KR [Adoption]: Agent scenario tool used for ≥80% of intraweek and ALCO-preparatory funding-mix decisions within 9 months of go-live.
OKR KR [Acceptance]: ≥80% of agent scenario outputs accepted by Treasury as analytically sound without remodeling before execution review.
OKR KR [Cycle]: Time from scenario request to cost-and-ratio-impact output reduced from hours of manual spreadsheet analysis to ≤15 minutes per scenario run.

### CARD 24 [Automation|M] ALCO pack and regulatory liquidity return automation
urn: urn:financial-services:scenario:flow/treasury-funding/trs-alco-pack-automation
intent: Agent-assembled ALCO pack, regulatory liquidity returns (NBKR Basel LCR/NSFR), and variance narrative — pulling from treasury, finance, and risk systems on the established reporting cycle with Treasury review before distribution. The CFO and ALCO chair receive a decision-quality pack without the current multi-day manual production cycle.
Problem to solve: ALCO packs and regulatory returns are assembled manually from treasury, finance, and risk systems each reporting cycle. The narrative explaining variances from plan is drafted by Treasury after the data pack is finalized; the full cycle takes days and compresses ALCO discussion time.
Solution: Agent pulls data from treasury, finance, and risk systems on the reporting calendar, assembles the ALCO pack structure, calculates LCR and NSFR ratios, and drafts the variance narrative. Treasury reviews and edits the pack; the final version is approved by the CFO or Head of Treasury before distribution to ALCO members.
OKR objective: ALCO pack, regulatory LCR/NSFR returns, and variance narrative are assembled by agent from treasury, finance, and risk systems on the established reporting calendar, with Treasury reviewing and editing before distribution to ALCO members.
OKR KR [Adoption]: Agent assembles the full ALCO pack and regulatory returns for ≥11 of 12 monthly ALCO cycles in the first year of go-live.
OKR KR [Acceptance]: ≥80% of agent-produced ALCO packs accepted by the Head of Treasury or CFO as requiring editing rather than full reconstruction before distribution.
OKR KR [Cycle]: ALCO pack production cycle from data pull to distribution-ready pack reduced by ≥3 business days compared to the manual multi-day baseline.

### CARD 25 [Enablement|M] Intraday liquidity position copilot
urn: urn:financial-services:scenario:flow/treasury-funding/trs-intraday-liquidity-copilot
intent: Near-real-time intraday liquidity position synthesis from payment system feeds and settlement data, reducing the 30-90 minute monitoring lag and giving Treasury operations anticipatory rather than reactive visibility. Contingency actions are prepared before a threshold breach rather than triggered after it is reported.
Problem to solve: Intraday liquidity monitoring draws on payment system feeds updated at intervals rather than in real time. The treasury operations team's view of the liquidity position lags by 30-90 minutes; contingency actions are reactive rather than anticipatory.
Solution: Agent aggregates intraday payment system feeds, settlement confirmations, and committed facility drawdown data into a continuously updated liquidity position view. Treasury operations reviews the dashboard in real time; agent generates an alert and recommended contingency action when the projected position approaches a regulatory or internal limit threshold.
OKR objective: Intraday liquidity position is synthesised continuously from payment system feeds and settlement confirmations, reducing the monitoring lag to near-real-time and giving Treasury operations anticipatory visibility for contingency action preparation.
OKR KR [Adoption]: Agent intraday liquidity dashboard active for ≥99% of business days with sub-15-minute position refresh intervals within 6 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-generated contingency action recommendations reviewed by Treasury operations as appropriate before threshold breach confirmation.
OKR KR [Cycle]: Intraday position monitoring lag reduced from the current 30-90 minute interval to ≤10 minutes on a continuous operating basis.

[PAGE TEXT]
FX & Cross-border
Multi-currency operations and international transfers. The cycle anchor is the FX-leg-and-settlement timing against customer-experience expectations.
FX & Cross-border covers corporate and retail FX conversion, international payment initiation, correspondent bank routing, settlement, and reconciliation. In CIS markets — Kazakhstan (NBK/NBKR), Kyrgyzstan (NBKR), and Russia (CBR) — the cycle carries additional regulatory specificity: currency control notifications, cross-border transfer reporting thresholds, and corridor-specific correspondent routing constraints. The cycle's competing pressures are price transparency (customer expectation for FX rate and fee certainty at the point of order) and settlement timing (correspondent bank chains introduce latency and status uncertainty that the originating bank cannot resolve unilaterally).
Analyze
FX exception rates, settlement failure causes, and nostro break volumes are tracked in end-of-day reports from individual systems with no cross-corridor aggregation. Operations cannot identify which correspondent bank corridors carry the highest exception rates or what settlement failure causes are systematic versus episodic.
Optimize
Correspondent bank routing decisions for CIS-corridor payments are encoded in static routing tables that are reviewed infrequently. Routing optimization — selecting the correspondent path with the lowest expected settlement failure rate and cost — is not a continuous process.
Automate
Nostro reconciliation, SWIFT exception triage, and currency-control notification preparation are manual daily tasks consuming treasury operations capacity. Each task is rule-governed and draws on structured data; the structural similarity across periods makes them candidates for end-to-end automation.
Enrich
Corporate clients with material FX exposures lack a systematic intelligence service on rate movements against their hedging thresholds. The bank's FX data — pricing history, corridor volumes, settlement timing — is not used to generate client-specific FX intelligence or early-warning alerts.
<button
class="flow-stages__stage"
type="button"
data-stage="capture"
data-flow-id="urn:financial-services:flow:fx-cross-border"
>
Capture order
→
<button
class="flow-stages__stage"
type="button"
data-stage="price"
data-flow-id="urn:financial-services:flow:fx-cross-border"
>
Price & quote
→
<button
class="flow-stages__stage"
type="button"
data-stage="execute"
data-flow-id="urn:financial-services:flow:fx-cross-border"
>
Execute
→
<button
class="flow-stages__stage"
type="button"
data-stage="settle"
data-flow-id="urn:financial-services:flow:fx-cross-border"
>
Settle
→
<button
class="flow-stages__stage"
type="button"
data-stage="reconcile"
data-flow-id="urn:financial-services:flow:fx-cross-border"
>
Reconcile
Lens
Scenario
Intent
Complexity

### CARD 26 [Enablement|S] FX purpose-code classification enablement
urn: urn:financial-services:scenario:flow/fx-cross-border/fx-purpose-code-classification-enablement
intent: Intelligent purpose-code classification at FX and cross-border payment order capture across channels, reducing misclassification-driven remediation requests before payment release under NBKR and NBK currency-control rules. The correct regulatory classification is proposed to the customer or handler at the point of order entry.
Problem to solve: Order capture across channels produces inconsistent purpose-code classification for currency-control reporting under NBKR and NBK rules. Misclassified orders generate remediation requests from operations before payment can proceed, extending settlement cycle time and consuming operations capacity.
Solution: Agent analyses the payment instruction — beneficiary type, amount, currency, and transaction description — and proposes the most likely regulatory purpose code with a confidence level. The handler or customer confirms or overrides the classification before order submission; low-confidence classifications are flagged for mandatory operations review.
OKR objective: Intelligent purpose-code classification is proposed at FX and cross-border payment order capture, reducing misclassification-driven remediation requests before payment release under NBKR and NBK currency-control rules.
OKR KR [Adoption]: Agent purpose-code classification deployed across ≥90% of FX and cross-border payment order capture channels within 6 months of go-live.
OKR KR [Acceptance]: ≥85% of agent purpose-code proposals confirmed by handlers or customers without override at order entry; operations remediation request rate reduced by ≥30% within 12 months.
OKR KR [Cycle]: Average settlement delay attributable to purpose-code remediation reduced by ≥40% for channels using agent-assisted classification within 12 months.

### CARD 27 [Insights|M] FX corridor exception and settlement failure analytics
urn: urn:financial-services:scenario:flow/fx-cross-border/fx-exception-corridor-analytics
intent: Cross-corridor aggregation of FX exception rates, settlement failure causes, and nostro break volumes — identifying which correspondent bank corridors carry systematic failure patterns and which exceptions are episodic. Operations and Treasury prioritise correspondent relationship management at the corridors with the highest systemic cost.
Problem to solve: FX exception rates, settlement failure causes, and nostro break volumes are tracked in end-of-day reports from individual systems with no cross-corridor aggregation. Operations cannot identify which correspondent bank corridors carry the highest exception rates or what settlement failure causes are systematic versus episodic.
Solution: Agent aggregates exception data across corridors and correspondent banks, classifies failure causes by type and frequency, and produces a ranked corridor-risk view updated daily. Treasury operations uses the corridor ranking to prioritise correspondent bank engagement; the view also informs routing-table review decisions.
OKR objective: FX exception rates, settlement failure causes, and nostro break volumes are aggregated cross-corridor and classified by failure type, giving operations and treasury a ranked corridor-risk view for correspondent relationship prioritisation.
OKR KR [Adoption]: Agent aggregates exception and settlement failure data across ≥95% of active correspondent corridors with daily updates within 6 months of go-live.
OKR KR [Acceptance]: ≥75% of agent-identified systemic corridor failure patterns confirmed as actionable by treasury operations for correspondent bank engagement prioritisation.
OKR KR [Cycle]: Time from corridor exception pattern emergence to treasury operations-reviewed ranked risk view reduced from end-of-day batch reports to ≤4 hours on a continuous basis.

### CARD 28 [Optimize|M] FX correspondent routing table optimisation
urn: urn:financial-services:scenario:flow/fx-cross-border/fx-correspondent-routing-optimisation
intent: Continuous optimisation of CIS-corridor correspondent routing tables based on settlement failure rates, cost, and format-compliance signals — replacing the current infrequent manual review of static routing rules. The bank routes each payment through the correspondent path with the lowest expected settlement failure rate within the available cost envelope.
Problem to solve: Correspondent bank routing decisions for CIS-corridor payments are encoded in static routing tables reviewed infrequently. Routing optimisation — selecting the correspondent path with the lowest settlement failure rate and cost — is not a continuous process.
Solution: Agent monitors settlement outcomes, format-rejection rates, and cost by correspondent path for each CIS corridor, generates an updated routing recommendation set monthly, and flags high-deterioration corridors for immediate review. Treasury operations reviews the routing recommendations before they are applied to the payment factory's configuration.
OKR objective: CIS-corridor correspondent routing tables are continuously optimised against settlement failure rates, cost, and format-compliance signals, replacing infrequent manual review of static routing rules.
OKR KR [Adoption]: Agent generates updated routing recommendation sets for ≥100% of active CIS corridors on a monthly cadence within 6 months of go-live; high-deterioration corridors flagged for immediate review within 24 hours of threshold breach.
OKR KR [Acceptance]: ≥80% of agent routing recommendations accepted by treasury operations without material override before configuration update.
OKR KR [Cycle]: Routing-table review cycle compressed from infrequent manual reviews to a continuous monthly cadence, with high-risk corridor updates processed within 48 hours.

### CARD 29 [Automation|M] Nostro reconciliation and currency-control notification automation
urn: urn:financial-services:scenario:flow/fx-cross-border/fx-nostro-reconciliation-automation
intent: Agent-driven nostro reconciliation, SWIFT exception triage, and currency-control notification preparation for NBKR and NBK reporting obligations, with operations review of break dispositions. Treasury operations capacity is directed toward correspondent relationship management and exception escalation rather than daily reconciliation mechanics.
Problem to solve: Nostro reconciliation across multiple correspondent banks and currencies is performed daily from manually downloaded statements. Break identification and investigation consumes treasury operations time; cross-border reporting to NBKR and NBK draws on the same reconciliation output, extending the reporting cycle.
Solution: Agent downloads nostro statements, matches transactions against the bank's records, classifies breaks by type and age, and prepares the currency-control notification submissions for NBKR and NBK. Operations reviews the break classification and approves notification submissions; unmatched items above a materiality threshold are escalated for manual investigation.
OKR objective: Nostro reconciliation, SWIFT exception triage, and NBKR/NBK currency-control notification preparation are agent-managed, with treasury operations reviewing break dispositions and approving all regulatory notification submissions.
OKR KR [Adoption]: Agent manages the full nostro reconciliation and notification preparation sequence for ≥90% of correspondent bank statements across active currencies within 6 months of go-live.
OKR KR [Acceptance]: ≥85% of agent-prepared NBKR/NBK notification submissions accepted by treasury operations without material revision before approval.
OKR KR [Cycle]: Daily nostro reconciliation and currency-control notification preparation cycle time reduced by ≥50% compared to the manual baseline within 12 months.

### CARD 30 [New opps|M] Corporate client FX rate intelligence service
urn: urn:financial-services:scenario:flow/fx-cross-border/fx-corporate-client-rate-intelligence
intent: Corporate client FX intelligence service — rate movements against client-specific hedging thresholds, corridor settlement timing intelligence, and early-warning alerts — derived from the bank's own FX pricing and volume data. Corporate clients with material FX exposures receive systematic market intelligence as part of the banking relationship rather than transacting at market without threshold visibility.
Problem to solve: Corporate clients with material FX exposures lack a systematic intelligence service on rate movements against their hedging thresholds. The bank's FX data — pricing history, corridor volumes, settlement timing — is not used to generate client-specific FX intelligence or early-warning alerts.
Solution: Agent tracks each corporate client's stated FX thresholds and monitors intraday rate movements, generating an alert when the rate enters the client's execution range. The relationship manager reviews the alert before client contact; the service is positioned as part of the bank's corporate FX proposition rather than as a separate advisory product.
OKR objective: Corporate clients with material FX exposures receive systematic rate-movement intelligence against their hedging thresholds and settlement timing signals, derived from the bank's own FX pricing and volume data.
OKR KR [Adoption]: Agent FX intelligence service covering ≥80% of enrolled corporate clients with material FX thresholds within 9 months of go-live.
OKR KR [Acceptance]: ≥75% of agent-generated client FX alerts reviewed and forwarded by relationship managers without material amendment.
OKR KR [Cycle]: Time from intraday rate entry into client execution range to RM-reviewed alert dispatch reduced to ≤15 minutes per event.

[PAGE TEXT]
Cross-cutting flows
Customer Lifecycle
End-to-end orchestration of the customer's institutional journey — acquisition, onboarding, active service, relationship growth, and exit. The cycle anchor is per-stage time and friction across the journey.
The Customer Lifecycle spans the full institutional journey — from acquisition and onboarding through active service, relationship growth, and eventual exit. Each stage carries its own cycle time and friction profile: onboarding completion rates, time-to-first-transaction, cross-sell conversion windows, and churn lead times are the operational metrics that govern commercial outcome. The GenAI opportunity runs across the entire lifecycle — compressing onboarding friction, surfacing retention signals before the decision window closes, and giving relationship managers and servicing teams a continuous, data-grounded view of where each customer sits in the journey.
Analyze
Customer journey data spans acquisition systems, KYC platforms, account management systems, and CRM — with no continuous cross-stage view. The bank reconstructs lifecycle stage transition rates and cycle times manually per quarter; the picture of where customers drop off, churn, or stall is always retrospective.
Optimize
Onboarding sequencing, cross-sell contact timing, and retention intervention thresholds are set at the policy level and reviewed infrequently. Segment-specific optimization — which customers to contact, when, and with what — requires multi-week analytical cycles that lag the commercial window.
Automate
KYC document chase, onboarding status updates, cross-sell offer follow-up, and exit processing steps each consume frontline or operations capacity on tasks that follow defined rules. The structural similarity across customers at each stage makes these candidates for agent-driven execution with human review.
Enrich
Lifetime value intelligence — acquisition cost, product depth, tenure, and risk-adjusted margin by customer — is assembled episodically for portfolio reviews. The bank does not maintain a continuous, customer-level lifecycle value view that could anchor retention prioritization and cross-sell sequencing in real time.
<button
class="flow-stages__stage"
type="button"
data-stage="acquire"
data-flow-id="urn:financial-services:flow:customer-lifecycle"
>
Acquire
→
<button
class="flow-stages__stage"
type="button"
data-stage="onboard"
data-flow-id="urn:financial-services:flow:customer-lifecycle"
>
Onboard
→
<button
class="flow-stages__stage"
type="button"
data-stage="serve"
data-flow-id="urn:financial-services:flow:customer-lifecycle"
>
Serve
→
<button
class="flow-stages__stage"
type="button"
data-stage="grow"
data-flow-id="urn:financial-services:flow:customer-lifecycle"
>
Grow
→
<button
class="flow-stages__stage"
type="button"
data-stage="retain"
data-flow-id="urn:financial-services:flow:customer-lifecycle"
>
Retain
→
<button
class="flow-stages__stage"
type="button"
data-stage="exit"
data-flow-id="urn:financial-services:flow:customer-lifecycle"
>
Exit
Lens
Scenario
Intent
Complexity

### CARD 31 [Insights|M] Customer lifecycle cross-stage journey analytics
urn: urn:financial-services:scenario:flow/customer-lifecycle/cl-cross-stage-journey-analytics
intent: Continuous cross-stage view of lifecycle transition rates and cycle times — onboarding completion, time-to-first-transaction, cross-sell conversion windows, and churn lead times — assembled from acquisition, KYC, account management, and CRM systems without quarterly manual reconstruction. The bank identifies where customers drop off, stall, or churn in close to real time.
Problem to solve: Customer journey data spans acquisition systems, KYC platforms, account management systems, and CRM with no continuous cross-stage view. The bank reconstructs lifecycle stage transition rates and cycle times manually per quarter; the picture of where customers drop off, churn, or stall is always retrospective.
Solution: Agent reads across lifecycle systems, tracks each customer's current stage and transition timestamps, and produces a continuous dashboard of completion rates, cycle times, and stage-exit reasons by segment and channel. Marketing and operations use the live view to direct interventions at the highest-friction stages; quarterly reporting is generated from the same data feed.
OKR objective: Customer lifecycle transition rates and cycle times across onboarding, activation, cross-sell, and churn stages are continuously visible from aggregated acquisition, KYC, account management, and CRM data, replacing quarterly manual reconstruction.
OKR KR [Adoption]: Agent maintains the cross-stage lifecycle dashboard with ≥99% data completeness across all defined transition points for ≥9 consecutive months within the first year.
OKR KR [Acceptance]: ≥80% of agent-produced lifecycle analytics views accepted by marketing and operations as decision-ready without material amendment.
OKR KR [Cycle]: Time from period close to distribution-ready cross-stage lifecycle analysis reduced from multi-week manual reconstruction to ≤24 hours.

### CARD 32 [Optimize|M] Onboarding and cross-sell sequencing optimisation
urn: urn:financial-services:scenario:flow/customer-lifecycle/cl-onboarding-sequence-optimisation
intent: Segment-specific optimisation of onboarding step sequencing and cross-sell contact timing based on behavioral signals, reducing drop-off at KYC and document collection steps and improving conversion within the early-tenure cross-sell window. Contact timing is determined by readiness signals rather than fixed post-onboarding calendars.
Problem to solve: Onboarding sequencing, cross-sell contact timing, and retention intervention thresholds are set at the policy level and reviewed infrequently. Segment-specific optimisation — which customers to contact, when, and with what — requires multi-week analytical cycles that lag the commercial window.
Solution: Agent models completion probability by onboarding step and segment, identifies the sequence that maximises completion rate, and generates a cross-sell contact signal when the customer's first-use behavior indicates readiness. Marketing and servicing operations review the recommended contact list before outreach; actual outcomes retrain the sequence model continuously.
OKR objective: Onboarding step sequencing and cross-sell contact timing are continuously optimised by segment using behavioral completion signals, reducing KYC drop-off and improving conversion within the early-tenure cross-sell window.
OKR KR [Adoption]: Agent sequence optimisation deployed across ≥3 retail segments and ≥1 SME segment within 9 months of go-live; contact signals generated for ≥80% of qualifying early-tenure customers.
OKR KR [Acceptance]: ≥75% of recommended contact lists accepted by marketing and servicing operations without material reordering before outreach.
OKR KR [Cycle]: Onboarding completion rate improvement across agent-optimised segments measured at ≥10 percentage points above pre-optimisation baseline within 12 months.

### CARD 33 [Automation|M] Lifecycle stage agent execution
urn: urn:financial-services:scenario:flow/customer-lifecycle/cl-lifecycle-agent-execution
intent: Agent-driven KYC document chase, onboarding status updates, cross-sell follow-up, and exit processing steps across the customer lifecycle, with human review triggered by exception rather than routine task assignment. Frontline and operations capacity is directed toward judgment-intensive interactions rather than structured task sequences.
Problem to solve: KYC document chase, onboarding status updates, cross-sell offer follow-up, and exit processing steps each consume frontline or operations capacity on tasks that follow defined rules. The structural similarity across customers at each stage makes these candidates for agent-driven execution with human review.
Solution: Agent orchestrates the task sequence for each customer at each lifecycle stage — dispatching requests, tracking responses, escalating non-completions, and updating downstream systems — with operations reviewing exceptions and approving any action that departs from the standard path. Human intervention is triggered by exception signal rather than by routine task queue.
OKR objective: KYC document chase, onboarding status updates, cross-sell follow-up, and exit processing steps are agent-orchestrated across the customer lifecycle, with operations reviewing exceptions and approving departures from the standard path.
OKR KR [Adoption]: Agent executes the task sequence for ≥80% of eligible structured lifecycle tasks across retail and SME segments within 9 months of go-live.
OKR KR [Acceptance]: ≥85% of agent-completed lifecycle task sequences accepted by operations without escalation to manual intervention.
OKR KR [Cycle]: KYC document collection and onboarding completion cycle time reduced by ≥35% for agent-managed cases within 12 months of go-live.

### CARD 34 [Enablement|M] Customer churn signal aggregation and scoring
urn: urn:financial-services:scenario:flow/customer-lifecycle/cl-churn-signal-enrichment
intent: Aggregated churn scoring from declining balance, reduced transaction frequency, competitor inquiry signals, and product usage changes across systems, surfaced to relationship managers and servicing teams as a continuous risk feed. Retention interventions are triggered by behavioral signals in the decision window rather than by the customer's exit notification.
Problem to solve: Churn signals — declining balance, reduced transaction frequency, competitor inquiry — arrive in multiple systems with no aggregation or scoring. Relationship managers and servicing teams identify at-risk customers reactively, after the churn decision is made.
Solution: Agent aggregates churn signals across account, transaction, and CRM systems, scores each customer's at-risk probability weekly, and surfaces a ranked retention contact list to relationship managers and servicing teams. Each at-risk flag includes the primary signal and the recommended retention action; the RM reviews and approves outreach before contact.
OKR objective: Churn signals from account, transaction, and CRM systems are aggregated and scored continuously, giving relationship managers a ranked retention contact list with primary signal context in advance of the customer's exit decision.
OKR KR [Adoption]: Agent churn scoring covers ≥90% of the active retail and SME customer base on a weekly cadence within 6 months of go-live.
OKR KR [Acceptance]: ≥70% of agent-flagged at-risk customers confirmed as actionable by relationship managers before outreach.
OKR KR [Cycle]: Lead time between churn signal emergence and RM-reviewed retention contact list reduced from reactive identification post-exit to ≥4 weeks before projected churn.

### CARD 35 [New opps|M] Customer lifetime value intelligence
urn: urn:financial-services:scenario:flow/customer-lifecycle/cl-lifetime-value-intelligence
intent: Continuous customer-level lifetime value view — acquisition cost, product depth, tenure, and risk-adjusted margin — anchoring retention prioritisation and cross-sell sequencing in real time. Relationship managers and segment heads direct effort at the customers and cohorts with the highest forward CLV rather than responding to backward-looking portfolio summaries.
Problem to solve: Lifetime value intelligence — acquisition cost, product depth, tenure, and risk-adjusted margin by customer — is assembled episodically for portfolio reviews. The bank does not maintain a continuous, customer-level lifecycle value view that could anchor retention prioritisation and cross-sell sequencing in real time.
Solution: Agent calculates and maintains a current CLV estimate for each customer, updated monthly from product revenue, cost-to-serve, and risk data. Relationship managers access the CLV view through the CRM; segment heads use the cohort-level CLV distribution to set coverage and cross-sell priorities. The model's assumptions are reviewed by Finance and Retail leadership quarterly.
OKR objective: A continuously updated customer-level CLV estimate — incorporating acquisition cost, product depth, tenure, and risk-adjusted margin — anchors RM coverage prioritisation and cross-sell sequencing on a rolling basis.
OKR KR [Adoption]: Agent CLV model covers ≥95% of the active customer base with monthly updates for ≥10 consecutive months within the first year.
OKR KR [Acceptance]: ≥80% of CLV model assumptions validated by Finance and Retail leadership at quarterly review without material methodology revision.
OKR KR [Cycle]: Interval from data refresh to CLV-updated CRM view available to relationship managers reduced from episodic portfolio-review cycles to ≤5 business days on a monthly cadence.

[PAGE TEXT]
Risk Management Cycle
Enterprise risk discipline across credit, market, operational, and strategic domains — identification, assessment, mitigation, monitoring, and reporting. The cycle anchor is the cadence at which emerging risks reach decision-makers.
The Risk Management Cycle is the institution's primary discipline for maintaining risk appetite alignment across credit, market, operational, and strategic risk domains. Each stage — from identification of emerging signals to assessment, mitigation action, ongoing monitoring, and reporting to the board and regulators — carries its own latency. Under NBKR, NBK, and ARDFM frameworks in CIS markets, the reporting cycle is externally timed; the internal discipline governs how fast emerging risks travel from detection to decision and action. The GenAI opportunity is to compress the identification-to-decision pathway and to ensure that risk monitoring is continuous rather than batch-driven.
Analyze
Emerging risks surface across credit, market, operational, and strategic domains in separate monitoring silos. Risk teams produce consolidated views manually for each governance cycle; the interval between the emergence of a risk signal and its appearance in a decision-ready format is measured in days to weeks.
Optimize
Risk mitigation action sequencing and control prioritization are set through annual risk appetite reviews and updated in response to material events. Continuous optimization — reranking mitigations based on observed control effectiveness and evolving exposure — is not a routine process.
Automate
Risk narrative production for ALCO, board risk committee, and regulatory submissions consumes risk team capacity on tasks that draw on structured data and established methodology. Each reporting cycle repeats the same data-pull, synthesis, and narrative sequence with manual effort.
Enrich
Stress-test results and risk assessment outputs are produced for regulatory and governance cycles but are not systematically used to enrich forward-looking business decisions. Credit pricing, product design, and limit-setting rarely draw directly on the most recent stress-test or emerging-risk assessment output.
<button
class="flow-stages__stage"
type="button"
data-stage="identify"
data-flow-id="urn:financial-services:flow:risk-management-cycle"
>
Identify
→
<button
class="flow-stages__stage"
type="button"
data-stage="assess"
data-flow-id="urn:financial-services:flow:risk-management-cycle"
>
Assess
→
<button
class="flow-stages__stage"
type="button"
data-stage="mitigate"
data-flow-id="urn:financial-services:flow:risk-management-cycle"
>
Mitigate
→
<button
class="flow-stages__stage"
type="button"
data-stage="monitor"
data-flow-id="urn:financial-services:flow:risk-management-cycle"
>
Monitor
→
<button
class="flow-stages__stage"
type="button"
data-stage="report"
data-flow-id="urn:financial-services:flow:risk-management-cycle"
>
Report
Lens
Scenario
Intent
Complexity

### CARD 36 [Insights|M] Emerging risk signal synthesis
urn: urn:financial-services:scenario:flow/risk-management-cycle/rmc-emerging-risk-signal-synthesis
intent: Cross-domain aggregation of credit, market, operational, and strategic risk signals into a continuous identification feed, compressing the interval between signal emergence and decision-ready format from days to hours. The CRO and risk committee receive an emerging-risk brief calibrated to materiality rather than governance-cycle cadence.
Problem to solve: Emerging risks surface across credit, market, operational, and strategic domains in separate monitoring silos. Risk teams produce consolidated views manually for each governance cycle; the interval between the emergence of a risk signal and its appearance in a decision-ready format is measured in days to weeks.
Solution: Agent monitors risk signals across domain-specific systems and external feeds, classifies each signal by risk type and materiality, and assembles a continuous emerging-risk brief for CRO review. Signals that cross materiality thresholds trigger an immediate alert with a recommended escalation path; the full risk identification view is refreshed daily for governance distribution.
OKR objective: Emerging risk signals across credit, market, operational, and strategic domains are aggregated and classified continuously, compressing the interval from signal emergence to decision-ready governance brief from days to hours.
OKR KR [Adoption]: Agent maintains the continuous emerging-risk brief with daily updates across all four domain-specific monitoring feeds for ≥350 days within the first year.
OKR KR [Acceptance]: ≥80% of agent-produced emerging-risk briefs accepted by the CRO as governance-ready without material revision at each distribution cycle.
OKR KR [Cycle]: Interval from risk signal emergence to CRO-reviewed decision-ready format reduced from the manual governance-cycle lag (days to weeks) to ≤24 hours for signals crossing materiality thresholds.

### CARD 37 [Optimize|M] Risk control effectiveness and mitigation prioritisation
urn: urn:financial-services:scenario:flow/risk-management-cycle/rmc-control-effectiveness-optimisation
intent: Continuous reranking of mitigation actions and control priorities based on observed control effectiveness and evolving risk exposure, replacing the annual risk appetite review as the primary driver of mitigation sequencing. The risk function directs remediation effort at the controls with the highest current marginal impact.
Problem to solve: Risk mitigation action sequencing and control prioritisation are set through annual risk appetite reviews and updated in response to material events. Continuous optimisation — reranking mitigations based on observed control effectiveness and evolving exposure — is not a routine process.
Solution: Agent tracks the effectiveness of each active mitigation action against the risk it was designed to address, identifies controls that have not reduced the measured risk as expected, and generates a reranked mitigation priority list for CRO review. The reranking is presented at each ALCO cycle as an input to the risk committee's agenda.
OKR objective: Mitigation action sequencing and control prioritisation are reranked on a continuous basis against observed control effectiveness and evolving exposure, with the CRO reviewing the updated priority list at each ALCO cycle.
OKR KR [Adoption]: Agent reranked mitigation priority list presented at ≥90% of ALCO cycles for ≥4 consecutive quarters within the first year.
OKR KR [Acceptance]: ≥75% of agent-identified underperforming controls confirmed by the CRO as meriting remediation reprioritisation at ALCO review.
OKR KR [Cycle]: Interval from control effectiveness signal emergence to CRO-reviewed reprioritisation recommendation reduced from the annual risk appetite review cycle to ≤1 ALCO cycle.

### CARD 38 [Automation|M] Risk narrative and regulatory reporting automation
urn: urn:financial-services:scenario:flow/risk-management-cycle/rmc-risk-narrative-automation
intent: Agent-assembled risk narratives for ALCO, board risk committee, and regulatory submissions — pulling from structured risk data and established methodology with risk team review before governance distribution. Risk team capacity is directed toward substantive risk analysis rather than report production.
Problem to solve: Risk narrative production for ALCO, board risk committee, and regulatory submissions consumes risk team capacity on tasks that draw on structured data and established methodology. Each reporting cycle repeats the same data-pull, synthesis, and narrative sequence with manual effort.
Solution: Agent pulls risk metric data from domain systems, synthesises it using the bank's established reporting framework, and drafts the narrative sections for each governance report. The CRO and senior risk team members review and edit the draft before distribution; the agent maintains version history for regulatory traceability.
OKR objective: Risk narratives for ALCO, board risk committee, and regulatory submissions are assembled by agent from structured risk data using the bank's established reporting framework, with the CRO and senior risk team reviewing and editing before governance distribution.
OKR KR [Adoption]: Agent produces the full risk narrative draft for ≥90% of scheduled ALCO, board risk committee, and regulatory reporting cycles within 12 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-drafted risk narratives accepted by the CRO team as requiring editing rather than full redraft before governance distribution.
OKR KR [Cycle]: Risk narrative production cycle from data pull to draft-ready-for-CRO-review reduced by ≥3 business days compared to the fully manual production baseline.

### CARD 39 [Enablement|M] Stress test and risk assessment decision enrichment
urn: urn:financial-services:scenario:flow/risk-management-cycle/rmc-stress-test-enrichment-copilot
intent: Structured presentation of stress-test results and emerging risk assessments to credit pricing, product design, and limit-setting teams at the point of decision, ensuring forward-looking risk intelligence is systematically embedded in business choices rather than held within the risk function.
Problem to solve: Stress-test results and risk assessment outputs are produced for regulatory and governance cycles but are not systematically used to enrich forward-looking business decisions. Credit pricing, product design, and limit-setting rarely draw directly on the most recent stress-test or emerging-risk assessment output.
Solution: Agent identifies business decisions currently in process — credit limit reviews, new product approvals, pricing changes — and surfaces the most relevant stress-test or risk assessment output with a structured impact narrative. Business unit leads review the risk enrichment as part of the decision dossier; the risk function is notified when enrichment is reviewed but not acted upon.
OKR objective: Stress-test results and emerging risk assessments are systematically surfaced to credit pricing, product design, and limit-setting teams at the point of decision, embedding forward-looking risk intelligence in business choices.
OKR KR [Adoption]: Agent identifies and enriches ≥80% of qualifying business decisions in process — credit limit reviews, new product approvals, pricing changes — with the most relevant stress-test or risk assessment output within 6 months of go-live.
OKR KR [Acceptance]: ≥75% of agent-produced risk enrichment dossiers reviewed by business unit leads as decision-informing without material supplementation.
OKR KR [Cycle]: Time from business decision trigger to risk-function-reviewed enrichment narrative available to decision makers reduced to ≤24 hours per qualifying event.

### CARD 40 [New opps|L] Cross-domain aggregate risk event view
urn: urn:financial-services:scenario:flow/risk-management-cycle/rmc-aggregate-risk-view
intent: Integrated cross-risk-type assessment for events that span credit, market, and operational boundaries — a single aggregate view of a counterparty failure, macro shock, or geopolitical event that the current siloed risk framework cannot produce. The CRO and board risk committee receive a complete exposure picture rather than three sequential sub-domain analyses.
Problem to solve: Credit, market, and operational risks are assessed in separate frameworks. A single event that crosses risk types — a counterparty failure that generates both credit and operational exposure — may not be assessed in its aggregate form within the governance cycle.
Solution: Agent maintains a cross-domain event registry and, when a qualifying event is identified, assembles an aggregate exposure assessment across credit, market, and operational risk dimensions simultaneously. The CRO reviews the aggregate assessment within 24 hours of event identification; the board risk committee receives it at the next governance cycle or sooner if the exposure exceeds appetite thresholds.
OKR objective: Cross-domain aggregate exposure assessments spanning credit, market, and operational risk are assembled simultaneously for qualifying events, giving the CRO and board risk committee a complete exposure picture within the governance cycle.
OKR KR [Adoption]: Agent assembles cross-domain aggregate assessment for ≥90% of qualifying events meeting defined threshold criteria within 24 hours of event identification.
OKR KR [Acceptance]: ≥80% of agent aggregate exposure assessments accepted by the CRO as analytically complete without material supplementation before board risk committee distribution.
OKR KR [Cycle]: Time from qualifying cross-domain event identification to CRO-reviewed aggregate exposure assessment reduced to ≤24 hours.

[PAGE TEXT]
Compliance & Financial Crime Cycle
AML, sanctions, counter-terrorism financing, and conduct obligations across the institution — alert detection, investigation, action, and regulatory reporting. The cycle anchor is the speed and accuracy of moving from alert to disposition.
The Compliance & Financial Crime Cycle governs the bank's obligations under AML, sanctions, counter-terrorism financing, and conduct frameworks — detecting suspicious activity, investigating to a disposition, actioning through blocking or reporting, and submitting regulatory filings. In CIS markets, the FATF-aligned frameworks of NBKR (Kyrgyzstan), NBK and ARDFM (Kazakhstan), and CBR (Russia) impose specific STR/SAR submission windows, correspondent banking KYC obligations, and PEP and sanctions screening standards. The cycle's primary constraint is alert throughput — the ratio of alerts generated by transaction monitoring to investigators available to reach a disposition — and its primary quality measure is accuracy: false positives waste capacity; false negatives create regulatory and reputational exposure.
Analyze
Alert volumes, false-positive rates, and investigation throughput are tracked at the system level in reports produced for each governance cycle. The financial crime operations team has no continuous view of which transaction monitoring rules generate the highest false-positive burden, which customer segments produce the most actionable alerts, or where investigation time is concentrated.
Optimize
Alert triage sequencing and investigator case assignment are driven by queue order rather than case complexity or filing probability. High-probability cases that warrant faster investigation are not differentiated from low-probability alerts at the point of assignment; investigator capacity is not matched to case complexity.
Automate
Case dossier assembly, adverse media search, SAR narrative drafting, and STR submission formatting each consume investigator capacity on tasks with defined structure and clear inputs. These tasks are strong candidates for agent execution with investigator review and approval before any regulatory action.
Enrich
Typology intelligence — the patterns of suspicious activity that financial intelligence units and FATF have identified as indicative of ML/TF — is available in public guidance but is not systematically applied to tune transaction monitoring rules or to enrich investigator decision-making at the case level.
<button
class="flow-stages__stage"
type="button"
data-stage="detect"
data-flow-id="urn:financial-services:flow:compliance-financial-crime-cycle"
>
Detect
→
<button
class="flow-stages__stage"
type="button"
data-stage="investigate"
data-flow-id="urn:financial-services:flow:compliance-financial-crime-cycle"
>
Investigate
→
<button
class="flow-stages__stage"
type="button"
data-stage="action"
data-flow-id="urn:financial-services:flow:compliance-financial-crime-cycle"
>
Action
→
<button
class="flow-stages__stage"
type="button"
data-stage="report"
data-flow-id="urn:financial-services:flow:compliance-financial-crime-cycle"
>
Report
Lens
Scenario
Intent
Complexity

### CARD 41 [Enablement|S] Financial crime typology enrichment copilot
urn: urn:financial-services:scenario:flow/compliance-financial-crime-cycle/cfc-typology-enrichment-copilot
intent: Investigator-facing typology intelligence drawn from FATF guidance, FIU publications, and internal case history, surfaced at the case level when the alert pattern matches a known ML/TF typology. Investigator decision quality improves at the disposition stage, particularly for complex or novel case types.
Problem to solve: Typology intelligence — the patterns of suspicious activity identified by financial intelligence units and FATF as indicative of ML/TF — is available in public guidance but is not systematically applied to tune transaction monitoring rules or to enrich investigator decision-making at the case level.
Solution: Agent classifies each incoming alert against a structured typology library drawn from FATF mutual evaluation findings, FIU red-flag indicators, and internal SAR history, and surfaces the most relevant typology match alongside the case dossier. The investigator reviews the typology context as part of the disposition decision; the typology library is updated quarterly by the financial crime intelligence function.
OKR objective: Investigator decision quality at alert disposition is systematically supported by FATF-aligned typology intelligence matched to each case's alert pattern, drawn from a maintained typology library.
OKR KR [Adoption]: Agent typology classification applied to ≥90% of incoming alerts for ≥6 months within the first year of go-live.
OKR KR [Acceptance]: ≥75% of typology match suggestions rated by investigators as relevant to their disposition decision in quarterly quality reviews.
OKR KR [Cycle]: Average investigator time at the disposition stage for complex or novel case types reduced by ≥25% compared to pre-typology-enrichment baseline within 12 months.

### CARD 42 [Insights|M] AML alert throughput and false-positive analytics
urn: urn:financial-services:scenario:flow/compliance-financial-crime-cycle/cfc-alert-throughput-analytics
intent: Continuous decomposition of alert volumes, false-positive rates by transaction monitoring rule, and investigation throughput by customer segment — giving financial crime operations a live view of where investigator capacity is concentrated and where rule tuning will have the highest return. AML program efficiency and regulatory defensibility improve together.
Problem to solve: Alert volumes, false-positive rates, and investigation throughput are tracked at the system level in reports produced for each governance cycle. The financial crime operations team has no continuous view of which transaction monitoring rules generate the highest false-positive burden or where investigation time is concentrated.
Solution: Agent monitors the case management system continuously, classifies each alert disposition against its generating rule, and assembles a rule-level false-positive and throughput dashboard updated daily. Financial crime operations and the AML model governance team use the view to prioritise rule tuning; changes to transaction monitoring rule parameters are reviewed by the MLRO before implementation.
OKR objective: AML alert volumes, false-positive rates, and investigation throughput are visible at the transaction monitoring rule level on a continuous basis, enabling targeted rule tuning and defensible AML program governance.
OKR KR [Adoption]: Agent rule-level false-positive and throughput dashboard in active use by financial crime operations and the AML model governance team for ≥95% of governance cycles within 6 months.
OKR KR [Acceptance]: ≥80% of agent-surfaced rule-tuning recommendations accepted by the MLRO as analytically sound prior to parameter change review.
OKR KR [Cycle]: Interval from rule-level alert pattern emergence to MLRO-reviewed governance briefing reduced from quarterly report cycle to ≤5 business days.

### CARD 43 [Optimize|M] Financial crime case triage and assignment optimisation
urn: urn:financial-services:scenario:flow/compliance-financial-crime-cycle/cfc-case-complexity-triage-optimisation
intent: Alert triage sequencing that differentiates cases by SAR-filing probability and investigation complexity at the point of assignment, matching investigator experience to case complexity rather than processing alerts by queue order. High-probability cases reach experienced investigators faster; investigator capacity is not diluted across low-probability alerts.
Problem to solve: Alert triage sequencing and investigator case assignment are driven by queue order rather than case complexity or SAR-filing probability. High-probability cases are not differentiated from low-probability alerts at assignment; investigator capacity is not matched to case complexity.
Solution: Agent scores each alert at triage for estimated SAR-filing probability and case complexity, assigns cases to investigator tiers accordingly, and surfaces the complexity rationale alongside the case dossier. The financial crime operations manager reviews the triage logic weekly; scoring model performance is validated against actual SAR-filing outcomes on a quarterly basis.
OKR objective: Alert triage sequences cases by SAR-filing probability and investigation complexity, ensuring experienced investigators are assigned high-probability cases rather than processing alerts by queue order.
OKR KR [Adoption]: Agent complexity scoring and tiered assignment applied to ≥90% of incoming alerts within 6 months of go-live.
OKR KR [Acceptance]: ≥80% of agent triage assignments validated as appropriately matched to investigator tier upon quarterly scoring model review.
OKR KR [Cycle]: Average time from alert generation to experienced-investigator assignment for high-SAR-probability cases reduced by ≥30% within 12 months.

### CARD 44 [Automation|M] Financial crime investigation pack and SAR draft automation
urn: urn:financial-services:scenario:flow/compliance-financial-crime-cycle/cfc-investigation-pack-automation
intent: Agent assembly of case dossiers — transaction history, KYC documents, beneficial ownership records, adverse media search, and SAR narrative draft — with investigator review and approval before any regulatory filing or account action. Investigator time is directed toward substantive analysis and disposition judgment rather than evidence gathering.
Problem to solve: Case dossier assembly, adverse media search, SAR narrative drafting, and STR submission formatting each consume investigator capacity on tasks with defined structure and clear inputs. Investigators spend more time on evidence gathering than on substantive analysis.
Solution: Agent assembles the case dossier from case management, KYC, and transaction systems, conducts structured adverse media and sanctions screening, and drafts the SAR narrative. The investigator reviews the full dossier, edits the SAR narrative, and approves the submission; the agent tracks STR/SAR submission windows against FATF-aligned regulatory deadlines.
OKR objective: Case dossier assembly, adverse media search, and SAR narrative drafting are agent-managed, with investigator capacity directed toward substantive disposition analysis and approval of all regulatory filings.
OKR KR [Adoption]: Agent assembles the full case dossier and SAR narrative draft for ≥85% of assigned investigations within 6 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-drafted SAR narratives accepted by investigators as substantively complete, requiring editing rather than full redraft before approval.
OKR KR [Cycle]: Time from alert assignment to investigation-pack-ready status reduced from 2–4 hours of manual assembly to ≤30 minutes per case.

### CARD 45 [New opps|M] Continuous AML program health monitoring
urn: urn:financial-services:scenario:flow/compliance-financial-crime-cycle/cfc-aml-program-health-continuous
intent: Continuous AML program health view — alert volumes, false-positive rates, investigation throughput, STR filing trends, and time-to-disposition by segment — updated in real time from case management data and surfaced to MLRO and senior management without waiting for the periodic report cycle. Regulatory examinations are met with a current-state view, not a retrospective reconstruction.
Problem to solve: Management and board reporting on AML program health is compiled manually from case management system extracts each reporting cycle. The picture of AML program effectiveness is always retrospective and produced at the cadence of the reporting cycle rather than continuously.
Solution: Agent reads from the case management system continuously, maintains a structured AML program health view across the five key program metrics, and produces the management and board report from the same live data on demand. The MLRO reviews the report before board distribution; the live dashboard is accessible to financial crime operations leadership at all times.
OKR objective: AML program health across alert volumes, false-positive rates, investigation throughput, STR filing trends, and time-to-disposition is continuously available to the MLRO and senior management, independent of the periodic report cycle.
OKR KR [Adoption]: Agent maintains the AML program health view with daily updates across all five key program metrics for ≥52 consecutive weeks within 12 months of go-live.
OKR KR [Acceptance]: ≥85% of on-demand management and board reports generated from the live dashboard accepted by the MLRO without material amendment.
OKR KR [Cycle]: AML program health reporting cycle compressed from multi-day manual extraction and compilation to board-ready output available within 2 hours of request.

[PAGE TEXT]
Internal Audit Cycle
Independent assurance over the bank's controls, risk management, and governance frameworks — risk-based audit planning, execution, reporting, and remediation tracking. The cycle anchor is audit coverage rate against the institutional risk surface.
The Internal Audit Cycle provides the board and senior management with independent assurance on the effectiveness of the bank's controls, risk management, and governance. The IIA standards and regulatory expectations from NBKR, NBK, and ARDFM define the audit universe, planning methodology, and reporting obligations. The cycle's primary constraint is audit coverage — the ability to maintain adequate assurance across an expanding risk surface with a fixed audit team. Each stage from plan to remediation verification carries its own lead time; findings that are identified but not remediated within the agreed timeline accumulate as open items and attract regulatory scrutiny.
Analyze
Audit finding data — by business unit, control type, root-cause category, and recurrence rate — is held in the audit management system but not routinely analyzed for systematic patterns. The audit committee and senior management receive finding summaries per report cycle but not a continuous view of which control domains are generating recurring issues.
Optimize
Audit planning allocates team capacity annually against a static risk ranking. High-risk business units that generate frequent repeat findings — indicating control environments that have not sustainably improved — do not automatically attract higher audit frequency in the planning cycle; replanning requires a manual review of the prior period's finding data.
Automate
Working paper documentation, evidence indexing, finding draft preparation, and remediation status update chasing consume audit team time on structured tasks with well-defined inputs. These tasks compete with the judgment-intensive analytical work that generates the assurance value; shifting them to agent execution preserves auditor capacity for substantive testing.
Enrich
The audit function's intelligence on control weaknesses, root-cause patterns, and remediation effectiveness is not systematically shared across business lines. A control weakness identified in retail banking may have a structural equivalent in SME or corporate banking; the institutional learning from audit findings rarely propagates to business units that have not yet been audited on the same control domain.
<button
class="flow-stages__stage"
type="button"
data-stage="plan"
data-flow-id="urn:financial-services:flow:internal-audit-cycle"
>
Plan
→
<button
class="flow-stages__stage"
type="button"
data-stage="execute"
data-flow-id="urn:financial-services:flow:internal-audit-cycle"
>
Execute
→
<button
class="flow-stages__stage"
type="button"
data-stage="report"
data-flow-id="urn:financial-services:flow:internal-audit-cycle"
>
Report
→
<button
class="flow-stages__stage"
type="button"
data-stage="remediate"
data-flow-id="urn:financial-services:flow:internal-audit-cycle"
>
Remediate
Lens
Scenario
Intent
Complexity

### CARD 46 [Automation|S] Audit fieldwork documentation and evidence automation
urn: urn:financial-services:scenario:flow/internal-audit-cycle/iac-fieldwork-documentation-automation
intent: Agent-managed working paper documentation, evidence indexing, finding draft preparation, and remediation status update chasing — preserving auditor capacity for substantive testing and judgment-intensive control analysis. The time savings on documentation tasks translates directly into broader audit coverage within the approved budget.
Problem to solve: Working paper documentation, evidence indexing, finding draft preparation, and remediation status update chasing consume audit team time alongside substantive testing. These structured tasks compete with the judgment-intensive analytical work that generates assurance value.
Solution: Agent manages the documentation workflow throughout fieldwork — indexing evidence to control objectives, drafting initial findings from test results, and chasing overdue remediation status updates from management. Audit staff review and approve each finding draft before it advances; the agent maintains a complete audit trail for regulatory review.
OKR objective: Working paper documentation, evidence indexing, finding draft preparation, and remediation status chasing are agent-managed throughout fieldwork, preserving auditor capacity for substantive testing and control analysis.
OKR KR [Adoption]: Agent manages documentation workflow for ≥85% of audit fieldwork assignments within 9 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-drafted initial findings accepted by audit staff as substantively complete, requiring editing rather than full redraft before advancement.
OKR KR [Cycle]: Proportion of audit team time spent on documentation tasks reduced by ≥30% per engagement within 12 months of go-live, measured against pre-implementation time-recording data.

### CARD 47 [Enablement|S] Audit finding remediation tracking enablement
urn: urn:financial-services:scenario:flow/internal-audit-cycle/iac-remediation-tracking-enablement
intent: Continuous remediation status tracking with automated follow-up prompts and overdue-action escalation, replacing periodic manual status reviews with a live open-finding visibility mechanism. Regulators reviewing open-item ageing receive a current-state view rather than a point-in-time extract produced at the previous governance cycle.
Problem to solve: Remediation tracking depends on management's voluntary status updates in the audit issue tracking system, supplemented by periodic auditor follow-up. Overdue actions and partial remediations are identified at the next status review date rather than on a continuous basis; open findings accumulate without a continuous visibility mechanism.
Solution: Agent monitors remediation commitments against agreed due dates, sends structured follow-up prompts to action owners at defined intervals before expiry, and escalates overdue actions to senior management and the Chief Audit Executive. The audit committee receives a continuous open-item dashboard; the agent generates the remediation status section of each board report from the live tracking data.
OKR objective: Remediation commitment status is tracked continuously with automated follow-up prompts and overdue-action escalation to senior management and the Chief Audit Executive, replacing periodic manual status reviews with a live open-finding visibility mechanism.
OKR KR [Adoption]: Agent remediation tracking covers ≥95% of open audit findings with due dates across all business units within 6 months of go-live.
OKR KR [Acceptance]: ≥75% of agent-generated remediation status sections in board reports accepted by the audit committee without material amendment.
OKR KR [Cycle]: Average overdue-action identification lag reduced from next periodic status review (typically 30–60 days) to ≤24 hours of due-date expiry.

### CARD 48 [Insights|M] Audit finding pattern intelligence
urn: urn:financial-services:scenario:flow/internal-audit-cycle/iac-finding-pattern-intelligence
intent: Continuous analysis of audit finding data by business unit, control type, root-cause category, and recurrence rate, giving the audit committee a live view of which control domains generate repeat issues rather than a per-cycle finding summary. Control environment trends are visible between governance cycles, not only at them.
Problem to solve: Audit finding data is held in the audit management system but not routinely analysed for systematic patterns. The audit committee and senior management receive finding summaries per report cycle but not a continuous view of which control domains are generating recurring issues.
Solution: Agent analyses the audit management system's finding records continuously, classifies each finding by control domain, root-cause category, and recurrence status, and produces a trend view updated after each audit report is finalised. The audit committee chair receives the pattern view at each meeting alongside the cycle's individual audit reports; the Chief Audit Executive uses the trend analysis in annual planning.
OKR objective: Audit finding data is analysed continuously by control domain, root-cause category, and recurrence rate, giving the audit committee a live trend view of control environment health between governance cycles.
OKR KR [Adoption]: Agent maintains the finding pattern trend view with updates after each finalised audit report for ≥100% of reports issued within the year.
OKR KR [Acceptance]: ≥80% of agent-produced audit committee trend analyses accepted by the Chief Audit Executive without material revision before committee distribution.
OKR KR [Cycle]: Interval from finding finalisation to audit committee-reviewed pattern view reduced from the next per-cycle summary report to ≤5 business days.

### CARD 49 [Optimize|M] Risk-ranked dynamic audit planning
urn: urn:financial-services:scenario:flow/internal-audit-cycle/iac-risk-ranked-audit-planning
intent: Dynamic audit schedule reallocation that increases coverage frequency for business units with high repeat-finding rates and incorporates mid-year risk changes into the coverage plan without waiting for the annual review. Audit team capacity is directed at the highest-risk parts of the institution on a rolling basis rather than a fixed annual allocation.
Problem to solve: Audit planning allocates team capacity annually against a static risk ranking. Business units that grow in risk between annual reviews may carry an outdated risk rating when the next audit is scheduled; high repeat-finding rates do not automatically increase audit frequency in the current planning cycle.
Solution: Agent recalculates the audit universe risk ranking quarterly using the most recent finding data, regulatory feedback, and business unit risk profile changes, and generates a schedule adjustment recommendation for the Chief Audit Executive. The audit committee approves material schedule changes; minor resequencing within the approved coverage commitments is managed by the Chief Audit Executive.
OKR objective: Audit coverage frequency and schedule allocation are dynamically adjusted on a quarterly basis using current finding data, regulatory feedback, and business unit risk profile changes, rather than being fixed at annual planning.
OKR KR [Adoption]: Agent generates quarterly audit universe risk reranking and schedule adjustment recommendations for ≥4 consecutive quarters within the first 12 months.
OKR KR [Acceptance]: ≥75% of agent schedule adjustment recommendations accepted by the Chief Audit Executive for implementation without material revision.
OKR KR [Cycle]: Lag between material business unit risk profile change and reflected adjustment in the approved audit coverage schedule reduced from the next annual planning cycle to ≤1 quarter.

### CARD 50 [New opps|M] Cross-entity audit control learning propagation
urn: urn:financial-services:scenario:flow/internal-audit-cycle/iac-cross-entity-control-learning
intent: Systematic propagation of audit finding intelligence across business lines — a control weakness identified in retail banking flagged to SME and corporate banking teams before their next audit cycle — reducing the institutional lag between a finding's identification in one entity and its preventive application in others.
Problem to solve: The audit function's intelligence on control weaknesses, root-cause patterns, and remediation effectiveness is not systematically shared across business lines. A control weakness identified in retail banking may have a structural equivalent in SME or corporate banking; the institutional learning rarely propagates to business units that have not yet been audited on the same control domain.
Solution: Agent classifies each finalised audit finding by control domain and structural applicability, identifies business units with similar control profiles that have not yet been audited on the relevant domain, and distributes a structured control learning note. Business unit control owners review the note and confirm whether the weakness applies; the Chief Audit Executive uses confirmed applicabilities to inform the next planning cycle.
OKR objective: Audit finding intelligence is systematically propagated across business lines by control domain, ensuring that a weakness identified in one entity informs preventive review in structurally similar business units before their next audit cycle.
OKR KR [Adoption]: Agent distributes structured control learning notes for ≥80% of finalised audit findings with identified cross-entity applicability within 3 months of finding finalisation.
OKR KR [Acceptance]: ≥70% of agent-distributed control learning notes confirmed as relevant by the receiving business unit control owners.
OKR KR [Cycle]: Propagation lag from finding finalisation in one business unit to reviewed control learning note in applicable peer entities reduced from the next annual planning cycle to ≤30 days.

[PAGE TEXT]
Financial Control & Performance Cycle
Bank-wide planning, close, and performance discipline — budget and rolling-forecast setting, financial close, management and regulatory reporting, and forward-looking adjustment. The cycle anchor is the financial-close cadence and the speed of forward-looking adjustment.
The Financial Control & Performance Cycle spans the bank's planning, close, and reporting disciplines — from annual and rolling budget setting through P&L execution, financial close, management and regulatory reporting, and the adjustment cycle that keeps the forward view current. Under NBKR, NBK, and ARDFM regulatory frameworks, periodic reporting to supervisors carries prescribed formats and submission windows; internally, the board and ALCO require a narrative view of performance against plan that the CFO function must produce each period. The cycle's primary constraint is the financial-close timeline — the elapsed time from period end to a reliable, decision-quality P&L — and the secondary constraint is the speed at which the forward view (reforecast) is updated when actuals deviate from plan.
Analyze
Variance between actual and budgeted performance is analyzed manually by finance teams after close, with each sub-team covering its own P&L line. The CFO and business unit CFOs receive the variance narrative at the point of the management pack distribution; the cycle-time between actuals and decision-ready variance analysis is measured in days.
Optimize
Budget submission and reforecast sequencing across business units is driven by the finance calendar and managed through email and spreadsheet tracking. Assumptions that are challenged or revised late in the consolidation cycle extend the overall timeline without a clear view of which submission is the constraint.
Automate
Monthly close narrative, management pack production, regulatory return formatting, and MD&A drafting are manual tasks that consume senior finance capacity on well-structured synthesis work. The structure of these tasks — pulling from known data sources, applying standard methodology, narrating variance — makes them strong candidates for agent-assisted production.
Enrich
Reforecast assumptions are updated by business units based on their own forward visibility. Cross-unit signals — a credit portfolio trend that implies a revenue headwind, an operational cost trajectory that will require provision adjustment — are not systematically surfaced to the reforecast process before they appear in the actuals.
<button
class="flow-stages__stage"
type="button"
data-stage="plan"
data-flow-id="urn:financial-services:flow:financial-control-cycle"
>
Plan
→
<button
class="flow-stages__stage"
type="button"
data-stage="execute"
data-flow-id="urn:financial-services:flow:financial-control-cycle"
>
Execute
→
<button
class="flow-stages__stage"
type="button"
data-stage="measure"
data-flow-id="urn:financial-services:flow:financial-control-cycle"
>
Measure
→
<button
class="flow-stages__stage"
type="button"
data-stage="report"
data-flow-id="urn:financial-services:flow:financial-control-cycle"
>
Report
→
<button
class="flow-stages__stage"
type="button"
data-stage="adjust"
data-flow-id="urn:financial-services:flow:financial-control-cycle"
>
Adjust
Lens
Scenario
Intent
Complexity

### CARD 51 [Insights|M] Financial variance attribution analytics
urn: urn:financial-services:scenario:flow/financial-control-cycle/fcc-variance-attribution-analytics
intent: Automated variance attribution between actual and budgeted P&L by revenue, cost, and credit-loss line across business units, reducing the interval from period close to decision-ready variance analysis from days to hours. The CFO and business unit CFOs review the attributed view rather than directing finance teams to reconstruct it.
Problem to solve: Variance between actual and budgeted performance is analysed manually by finance teams after close, with each sub-team covering its own P&L line. The CFO and business unit CFOs receive the variance narrative at the point of management pack distribution; the cycle-time between actuals and decision-ready variance analysis is measured in days.
Solution: Agent pulls actual and budget data from the closed ledger, attributes variances to price, volume, mix, and one-off effects for each P&L line, and presents the attribution to the CFO team for review. Finance leadership reviews and edits the attribution narrative before management pack distribution; the attribution methodology is maintained and version-controlled by the financial control team.
OKR objective: Variance between actual and budgeted P&L is attributed automatically by revenue, cost, and credit-loss line across business units, reducing the interval from period close to decision-ready variance analysis from days to hours.
OKR KR [Adoption]: Agent variance attribution covers ≥95% of P&L lines and all business units for ≥11 of 12 monthly close cycles in the first year.
OKR KR [Acceptance]: ≥80% of agent-produced variance attribution narratives accepted by the CFO and business unit CFOs without material reattribution before management pack distribution.
OKR KR [Cycle]: Close-to-decision-ready variance analysis interval reduced from multi-day manual cycle to ≤4 hours from ledger sign-off.

### CARD 52 [Optimize|M] Budget and reforecast consolidation optimisation
urn: urn:financial-services:scenario:flow/financial-control-cycle/fcc-budget-consolidation-optimisation
intent: Constraint-path identification in the budget submission and reforecast consolidation sequence — flagging which business unit submissions are holding the cycle — reducing the multi-week assumption-revision loop that extends the planning timeline without improving plan quality. Finance leadership acts on the constraint view to unblock the consolidation.
Problem to solve: Budget submission and reforecast sequencing across business units is driven by the finance calendar and managed through email and spreadsheet tracking. Assumptions that are challenged or revised late in the consolidation cycle extend the overall timeline without a clear view of which submission is the constraint.
Solution: Agent tracks submission status, outstanding challenge items, and assumption revision rounds across business units throughout the consolidation cycle, identifies the submissions on the critical path, and surfaces the constraint view to the CFO team. The CFO uses the constraint identification to direct follow-up effort; the agent updates the critical path view in real time as submissions are received and challenges are resolved.
OKR objective: Critical-path submissions in the budget and reforecast consolidation cycle are identified continuously, giving the CFO team a constraint view to direct assumption-challenge effort and unblock the consolidation sequence.
OKR KR [Adoption]: Agent submission tracking and critical-path identification deployed across ≥90% of business unit submissions for each consolidation cycle within 6 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-identified critical-path constraints confirmed as the actual consolidation bottleneck by the CFO team for each cycle.
OKR KR [Cycle]: Budget consolidation elapsed time from submission deadline to CFO-approved consolidated plan reduced by ≥20% within the first full planning cycle after go-live.

### CARD 53 [Automation|M] Financial close narrative and management pack automation
urn: urn:financial-services:scenario:flow/financial-control-cycle/fcc-close-narrative-automation
intent: Agent-assembled monthly close narrative, management account pack, regulatory return, and MD&A variance commentary — pulling from the closed ledger on the established finance calendar with CFO-team review before distribution. Senior finance capacity is directed toward interpretation and decision support rather than report production mechanics.
Problem to solve: Monthly close narrative, management pack production, regulatory return formatting, and MD&A drafting are manual tasks that consume senior finance capacity on well-structured synthesis work. The structure of these tasks — pulling from known data sources, applying standard methodology, narrating variance — makes them strong candidates for agent-assisted production.
Solution: Agent pulls from the closed ledger after sign-off, assembles the management account tables, drafts the revenue, cost, and credit-loss variance narratives, formats the regulatory return, and produces the MD&A draft. The CFO team reviews and edits the full pack before board or ALCO distribution; the agent maintains a version trail for each period's production cycle.
OKR objective: Monthly close narrative, management account pack, regulatory return, and MD&A variance commentary are assembled by agent from the closed ledger on the finance calendar, with the CFO team reviewing and editing before board or ALCO distribution.
OKR KR [Adoption]: Agent assembles the full close reporting package for ≥11 of 12 monthly close cycles in the first year of go-live.
OKR KR [Acceptance]: ≥80% of agent-produced management packs accepted by the CFO team with editing rather than full redraft before distribution.
OKR KR [Cycle]: Close-to-distribution cycle time for the management account pack reduced by ≥3 business days compared to the fully manual production baseline.

### CARD 54 [Enablement|M] Reforecast cross-unit forward signal enrichment
urn: urn:financial-services:scenario:flow/financial-control-cycle/fcc-reforecast-cross-signal-enrichment
intent: Cross-unit forward signals — a credit portfolio trend implying a revenue headwind, a cost trajectory that requires provision adjustment, an operational loss run-rate that will exceed budget — surfaced to the reforecast process before they appear in the actuals, enabling earlier assumption updates and reducing the gap between the forecast and the eventual outcome.
Problem to solve: Reforecast assumptions are updated by business units based on their own forward visibility. Cross-unit signals that imply assumption changes — credit portfolio trends, operational cost trajectories — are not systematically surfaced to the reforecast process before they appear in the actuals.
Solution: Agent monitors leading indicators across business units and the credit, cost, and operational data feeds, identifies signals that are inconsistent with the current reforecast assumptions, and surfaces them to the CFO team with a structured impact narrative. The CFO team reviews the flagged signals and decides whether to initiate a reforecast assumption change; business unit CFOs are notified of signals affecting their submissions.
OKR objective: Cross-unit forward signals — credit portfolio trends, cost trajectories, and operational loss run-rates that are inconsistent with current reforecast assumptions — are surfaced to the CFO team before they appear in the actuals.
OKR KR [Adoption]: Agent monitors leading indicator feeds across ≥4 business units and flags cross-unit assumption conflicts for ≥10 of 12 months in the first year.
OKR KR [Acceptance]: ≥75% of agent-surfaced cross-unit signals assessed by the CFO team as meriting a reforecast assumption review.
OKR KR [Cycle]: Lead time between cross-unit signal emergence and CFO-team-reviewed impact narrative reduced from actuals-driven identification (4–6 weeks lag) to ≤5 business days on a continuous basis.

### CARD 55 [New opps|L] IFRS 9 provision intelligence and planning integration
urn: urn:financial-services:scenario:flow/financial-control-cycle/fcc-ifrs9-provision-intelligence
intent: Continuous IFRS 9 ECL intelligence integrated with the planning and reforecast cycle — credit-loss assumptions updated in real time as the portfolio's staging distribution shifts, rather than waiting for the next formal provision review. The CFO and Finance team have an IFRS 9-consistent forward P&L view between provision review cycles.
Problem to solve: IFRS 9 ECL provision outputs are produced for governance and regulatory cycles but are not integrated into the rolling reforecast and planning process in real time. Credit-loss assumptions in the forward plan lag the portfolio's actual staging distribution, creating provision surprises at the formal review.
Solution: Agent monitors the credit portfolio's staging migration data continuously, recalculates the ECL forward projection using the approved IFRS 9 model, and updates the CFO team's provision assumption view between formal review cycles. The Chief Accounting Officer and Credit Risk validate the updated projection before it is incorporated into the reforecast; material staging movements above a defined threshold trigger an immediate alert.
OKR objective: IFRS 9 ECL projections are updated continuously as the credit portfolio's staging distribution shifts, giving the CFO and Finance team a provision-consistent forward P&L view between formal provision review cycles.
OKR KR [Adoption]: Agent ECL forward projection updated within 48 hours of material staging migration events for ≥95% of qualifying portfolio movements throughout the year.
OKR KR [Acceptance]: ≥85% of agent ECL projection updates validated by the Chief Accounting Officer and Credit Risk as methodologically consistent with the approved IFRS 9 model without material revision.
OKR KR [Cycle]: Interval from material staging migration to CFO-team-reviewed forward provision impact reduced from the next formal provision review cycle to ≤3 business days.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
×
