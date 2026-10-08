# Operational Value Streams

Operational Value Streams are the Bank's primary value chain — the flows that hold and move customer money, deliver credit and wealth services, and run the cross-cutting cycles that keep the institution disciplined. **The opportunity for GenAI is to compress cycle time and surface waste continuously across these flows** — so that each routine cycle can be tuned continuously and capacity is freed for judgment-heavy work.

## Problems

| Lens | Problem |
| --- | --- |
| Waste | Banking flows accumulate non-value-add activity — hand-off waiting, reconciliations across systems, rework after exceptions. Value-add time is a fraction of elapsed time, and visibility into where the waste sits is reconstructed manually each cycle. |
| Variability | Flow load swings across day, week, and quarter — month-end peaks, batch backlogs, intermittent customer events. Capacity is sized to absorb the swings, but the swings themselves are not measured or planned for. |
| Overload | Critical judgment roles — credit committees, compliance investigators, audit leads, financial-close teams — operate at sustained over-capacity. The load on these scarce roles is known by anecdote, not measured. |
| Quality at source | Defects in banking flows surface downstream where correction costs multiply — mis-routings, mis-classifications, exception escapes carried forward through hand-offs. The flow rarely stops at the moment of error. |

## Customer and balance-sheet value streams {#customer-facing-flows}

### Deposits & Transaction Banking {#deposits-transaction-banking}

- URN: urn:financial-services:flow:deposits-transaction-banking
- Summary: Holding and moving customer money — accounts, payments, cards, transfers. The stream turns on the speed and integrity of moving value while staying compliant.

Deposits & Transaction Banking covers account opening, funding, payment initiation, card issuance, domestic and cross-border transfers, dispute handling, and ongoing account servicing. Transaction volume is high and operationally routine, yet exception handling, payment investigations, and dispute management consume disproportionate capacity. The regulatory overlay — payment-system rules, account-status reporting, AML obligations in line with the FATF Recommendations — runs alongside every transaction, and compliance friction at the edges slows resolution cycles without reducing volume.

| Lens | Problem |
| --- | --- |
| Analyze | Payment exception rates, dispute volumes, and transaction failure patterns are tracked in isolated system reports with no cross-channel aggregation. Operations managers reconstruct the picture each week from separate extracts; recurrent failure patterns remain attributed to one-off causes. |
| Optimize | Dispute routing and investigation sequencing are handler-driven and not informed by case complexity or resolution probability. Payment investigation queues grow during peak periods without workload-balancing logic; cases of similar type take materially different time depending on queue assignment. |
| Automate | Transaction investigation triage, dispute-response drafting, and complaint acknowledgment consume frontline analyst capacity on tasks that follow consistent resolution paths. Initiation-to-resolution for straightforward disputes runs days because each case enters a shared queue regardless of complexity. |
| Enrich | Spend-pattern intelligence from the transaction ledger is not systematically surfaced for product or pricing decisions. Interchange optimization, cohort-level churn signals, and balance-behavior shifts remain latent in the transaction data and are not acted on until lag indicators appear. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| account-opening | Account opening | Account opening and initial onboarding | A retail or corporate customer applies to open an account — identity verification, KYC tier assignment, product selection, and account activation. The stage sets the compliance baseline and determines transaction permissions from day one. | KYC completion rates drop when document requests are static and sequenced identically across customer segments. Activation delays carry into the transact stage; operational staff chase missing items while the account sits dormant. |
| fund | Fund | Initial funding and account activation | Customer funds the account via transfer, cash, or card linkage. The stage confirms the account is operationally live and triggers downstream system activations — card issuance, limit assignment, and mobile banking provisioning. | Funding events trigger manual provisioning sequences across card, limits, and mobile banking systems. Failures in any downstream step leave the account partially activated without a clear resolution path for the customer. |
| transact | Transact | Day-to-day payment and transfer execution | Execution of payments, transfers, card transactions, and direct debits. High-volume, time-sensitive, and subject to continuous AML screening and fraud detection at the transaction level. | Payment failures and exceptions generate investigation queues handled case-by-case. Exception patterns — failed beneficiary routing, format mismatches, limit breaches — recur without systematic feedback into the initiation controls. |
| service | Service | Dispute handling, inquiry resolution, and account maintenance | Handling of disputes, payment inquiries, chargebacks, and account-maintenance requests. The stage where the gap between customer expectation and operational reality becomes most visible. | Dispute and investigation cases arrive with inconsistent documentation; handlers reconstruct transaction context from multiple systems per case. Resolution time variance is wide and driven by which handler picks up the case. |
| retain | Retain | Retention, cross-sell, and account deepening | Identification of at-risk accounts, cross-sell eligibility, and deepening of the transaction relationship. The commercial stage where product breadth and customer engagement metrics are actively managed. | Churn signals — declining transaction activity, reduced balance, competitor inquiry — arrive too late for effective intervention. Cross-sell offers are product-push rather than derived from observed transaction behavior. |

#### Dispute resolution automation

- URN: urn:financial-services:scenario:flow/deposits-transaction-banking/dtb-dispute-resolution-automation
- Lens: Automation
- Complexity: M
- Intent: End-to-end AI-driven resolution of straightforward dispute cases — documentation assembly, transaction context retrieval, customer communication drafting, and deadline tracking — with analyst approval before dispatch and full analyst handling reserved for contested or high-value cases. Initiation-to-resolution cycle time compresses materially for the majority of dispute volume.
- Problem to solve: Transaction investigation triage, dispute-response drafting, and complaint acknowledgment consume frontline analyst capacity on tasks that follow consistent resolution paths. Straightforward disputes enter a shared queue regardless of complexity; resolution runs days because the case sequence is not differentiated by effort required.
- Solution: The AI agent handles the full resolution sequence for structurally simple disputes: retrieves transaction context, assembles the documentation set, drafts the customer response, and tracks chargeback or payment-scheme deadlines. Analyst approval gates the customer-facing output and any credit or reversal action; contested or high-value cases stay with analysts.
- OKR: Straightforward dispute cases are resolved through an AI-driven end-to-end sequence covering documentation, transaction context retrieval, customer communication, and deadline tracking, with analyst approval gating customer-facing output and any credit or reversal action.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent manages the full resolution sequence for ≥70% of structurally simple dispute cases within 9 months of go-live. |
| Acceptance | ≥85% of AI-drafted customer dispute responses accepted by analysts without material amendment before dispatch. |
| Cycle | Dispute initiation-to-resolution cycle time for AI-managed cases reduced by ≥40% compared to the manual queue baseline within 12 months. |

#### KYC adaptive document sequencing

- URN: urn:financial-services:scenario:flow/deposits-transaction-banking/dtb-kyc-adaptive-sequencing
- Lens: Enablement
- Complexity: S
- Intent: Adaptive KYC document request sequencing at account opening, ordered by segment-specific completion probability to improve first-attempt completion rates and reduce the activation-delay tail. The sequence adjusts based on customer segment, channel, and the KYC tier assigned at initiation.
- Problem to solve: KYC completion rates drop when document requests are static and sequenced identically across customer segments. Activation delays carry into the transact stage; KYC operations staff chase missing items while the account sits dormant.
- Solution: The AI agent recommends the optimal document request sequence for each applicant based on segment, channel, and KYC-tier signals, presenting the highest-completion-probability requests first. KYC operations staff review the recommended sequence before customer contact; the model retrains on completion outcomes across the portfolio.
- OKR: KYC document request sequencing at account opening adapts to customer segment, channel, and KYC tier to present the highest-completion-probability requests first, improving first-attempt completion rates and compressing the activation-delay tail.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's adaptive sequencing applied to ≥85% of retail and SME account openings across relevant KYC tiers within 6 months of go-live. |
| Acceptance | ≥80% of recommended document sequences accepted by KYC operations staff without override before customer contact. |
| Cycle | Average KYC completion lag from application initiation to document set completion reduced by ≥25% for AI-sequenced cases within 12 months. |

#### Payment exception pattern analytics

- URN: urn:financial-services:scenario:flow/deposits-transaction-banking/dtb-exception-pattern-analytics
- Lens: Insights
- Complexity: M
- Intent: Cross-channel aggregation of payment exception rates, dispute volumes, and transaction failure patterns, classified by root cause and recurrence frequency. Operations managers receive a continuous view of systemic failures — beneficiary routing gaps, format mismatches, limit-breach patterns — without weekly reconstruction from separate system extracts.
- Problem to solve: Exception and dispute patterns are tracked in isolated system reports with no cross-channel aggregation. Recurrent failure patterns remain attributed to one-off causes because the cross-channel picture is never assembled at the time the pattern forms.
- Solution: The AI agent continuously reads exception and dispute data across channels, classifies cases by root-cause category, and surfaces recurrence patterns ranked by volume and resolution cost. Operations managers confirm the patterns in weekly reviews and act on them; individual case handling proceeds with the benefit of systemic context.
- OKR: Payment exception rates, dispute volumes, and transaction failure patterns are aggregated cross-channel and classified by root cause, giving operations managers a continuous systemic-failure view for targeted process and routing remediation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's exception aggregation covers ≥95% of payment channels and exception types with daily updates within 6 months of go-live. |
| Acceptance | ≥75% of AI-identified systemic failure patterns confirmed as actionable by operations managers in weekly pattern reviews. |
| Cycle | Time from pattern emergence to operations-ready root-cause classification reduced from the weekly manual report cycle to ≤24 hours on a continuous basis. |

#### Dispute and investigation queue routing optimization

- URN: urn:financial-services:scenario:flow/deposits-transaction-banking/dtb-stp-routing-intelligence
- Lens: Optimize
- Complexity: M
- Intent: Routing optimization for payment investigation and dispute queues based on case complexity, resolution probability, and handler workload. The share of cases resolved without manual handling rises as structurally similar cases are separated from genuinely complex exceptions at the point of queue entry.
- Problem to solve: Dispute routing and investigation sequencing are handler-driven with no complexity or resolution-probability signal at assignment. Cases of similar type take materially different time depending on queue assignment; peak-period backlogs grow without workload-balancing logic.
- Solution: The AI agent scores incoming cases by complexity and estimated resolution path, routes straightforward disputes to auto-resolution tracks, and assigns complex or contested cases to experienced handlers. Analysts review auto-resolution routing decisions; queue rebalancing logic triggers during peak periods, maintaining consistent cycle-time targets.
- OKR: Payment investigation and dispute queues are routed by case complexity and resolution probability at the point of queue entry, increasing the share of cases resolved without manual handling by separating structurally routine cases from genuinely complex exceptions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's complexity scoring and routing logic applied to ≥90% of incoming dispute and investigation cases within 6 months of go-live. |
| Acceptance | ≥80% of auto-resolution routing decisions confirmed as correctly classified by analyst review within the first 3 months; ongoing false-routing rate ≤5%. |
| Cycle | Dispute queue cycle time for AI-routed auto-resolution cases reduced by ≥50% compared to the pre-routing baseline within 12 months. |

#### Transaction behavior intelligence for product and pricing

- URN: urn:financial-services:scenario:flow/deposits-transaction-banking/dtb-transaction-behavior-intelligence
- Lens: New opps
- Complexity: M
- Intent: Continuous intelligence on cohort spend shifts, CASA balance-behavior changes, and interchange optimization opportunities derived from the transaction ledger, surfaced for product and pricing decisions. The Bank acts on behavioral signals before lag indicators appear in management reporting.
- Problem to solve: Spend-pattern intelligence from the transaction ledger is not systematically surfaced for product or pricing decisions. Interchange optimization, cohort-level churn signals, and balance-behavior shifts remain latent in the transaction data and are not acted on until lag indicators appear.
- Solution: The AI agent monitors cohort-level transaction patterns, detects meaningful shifts in CASA balance behavior and spend mix, and surfaces actionable intelligence to product and pricing teams on a continuous cadence. Outputs are calibrated to decision windows — pricing reviews, product design cycles — rather than delivered at fixed reporting intervals; product and pricing leadership review them before acting.
- OKR: Cohort spend shifts, CASA balance-behavior changes, and interchange optimization opportunities are surfaced continuously from the transaction ledger to product and pricing teams at decision-relevant cadence.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's transaction intelligence delivered to product and pricing teams for ≥6 of 8 defined decision windows (pricing reviews, product design cycles) in the first 12 months. |
| Acceptance | ≥75% of AI-surfaced behavioral signals accepted by product and pricing leadership as decision-informing without material reanalysis. |
| Cycle | Interval from behavioral pattern emergence in the transaction ledger to product-team-reviewed intelligence output reduced from lag-indicator reporting (4–6 weeks) to ≤5 business days on a continuous basis. |

### Lending {#lending}

- URN: urn:financial-services:flow:lending
- Summary: Credit products across retail, SME, corporate, and mortgage. The stream turns on decision time — from application to funded — while keeping risk discipline.

Lending originates credit across retail, SME, corporate, and mortgage segments — application intake, KYC and credit assessment, decision, documentation, funding, and post-origination servicing. Decision cycle time ranges from minutes for retail unsecured to weeks for complex SME and corporate cases. The cycle's competing pressures are speed (customer expectation, competitor benchmarks) and discipline (credit quality, regulatory adherence, fraud control), and most of the improvement headroom sits in the hand-offs between intake, underwriting, credit committee, and funding teams.

| Lens | Problem |
| --- | --- |
| Analyze | Origination cycle time, queue depth at credit review, and exception patterns are reconstructed manually each cycle from disconnected case-management systems. Underwriters and credit-committee secretaries lack a live picture of which applications are stalled and why. |
| Optimize | Routing decisions (fast-track vs. full review), document-collection sequencing, and credit-committee batching are set at the policy level and rarely retuned. Each segment's optimization headroom requires multi-day modeling that competes with day-to-day origination throughput. |
| Automate | Document collection, status updates to customers and intermediaries, low-risk decisioning under a threshold, and post-decision notification cascades all consume frontline analyst time. Most steps are rule-driven and prescribed — the structural similarity across applications makes them ripe for end-to-end automation. |
| Enrich | Optimization wins in retail rarely transfer to SME or corporate; cross-segment learnings stay siloed. Trial of new lending products (new structures, new collateral types) requires multi-week setup before the first application can be processed. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| application | Application | Application for credit by the customer | Customer initiates a credit request — application capture, initial KYC, intent classification, and routing to the appropriate underwriting track. | Application intake is fragmented across channels (branch, digital, intermediary), and routing decisions are encoded in static rules that are rarely retuned. Misrouted or incomplete applications consume frontline-analyst time before they reach underwriting. |
| underwriting | Underwriting | Risk assessment of the application by the Bank | Credit assessment — risk score, capacity-and-willingness analysis, collateral assessment, and policy compliance check. The stage where most decision time accumulates. | Underwriting capacity is the principal bottleneck. Senior underwriters spend disproportionate time on cases that policy already approves and on applications that need early decline. Routing intelligence is policy-set and slow to evolve. |
| decision | Decision | Approval or decline of the credit by the Bank | Approval/decline decision — committee for material cases, delegated authority for the rest. The stage where institutional judgment crystallizes. | Credit committee throughput drops without clear root cause; the secretariat's after-the-fact analysis lags by a week. Delegated authority decisions are recorded with limited explainability, weakening the Bank's ability to learn from policy edges. |
| documentation | Documentation | Documentation and signing of the loan terms | Loan documentation — terms, security registration, regulatory disclosures, and customer signing. The administrative bottleneck after decision. | Documentation packs are assembled manually from product templates, signed offline, and tracked in case-management systems. Document collection from customers and intermediaries is the largest contributor to post-decision cycle time. |
| funding | Funding | Disbursement of credit to the customer or their counterparty | Disbursement — to customer, to vendor, or to settlement system. The stage where the decision becomes a balance-sheet position and a customer-facing event. | Funding-stage hand-offs cross treasury, operations, and customer servicing systems with different latencies. Notification cascades to customer, intermediary, and downstream systems are manually relayed; downstream systems sometimes receive stale states. |
| servicing | Servicing | Ongoing servicing of the credit relationship across its lifecycle | Ongoing servicing — repayments, modifications, collections, and exceptions. The stage where the credit relationship lives across its lifecycle. | Servicing operations run in isolation from origination data and learnings. Modifications and exceptions are case-handled with limited pattern recognition; cross-segment learnings rarely propagate back to origination policy. |

#### Credit document collection and notification automation

- URN: urn:financial-services:scenario:flow/lending/lending-doc-collection-automation
- Lens: Automation
- Complexity: S
- Intent: AI-managed document collection, customer and intermediary status notifications, and post-decision notification cascades for structurally similar retail and SME credit applications. Analyst capacity is directed toward exception handling and complex documentation requirements rather than routine follow-up.
- Problem to solve: Document collection, status updates to customers and intermediaries, and post-decision notification cascades consume frontline analyst time on tasks that are rule-driven and prescribed. Structural similarity across applications makes the full sequence a candidate for end-to-end automation.
- Solution: The AI agent orchestrates the document-collection sequence — request dispatch, receipt confirmation, and missing-item escalation — and sends structured status updates at defined origination milestones. Post-decision notifications to customer, intermediary, and downstream systems are dispatched automatically with analyst review of exceptions.
- OKR: Document collection, customer and intermediary status notifications, and post-decision notification cascades for structurally similar retail and SME credit applications are orchestrated by the AI agent, with analyst capacity directed toward exception handling.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent manages the end-to-end document collection and notification sequence for ≥80% of eligible retail and SME credit applications within 9 months of go-live. |
| Acceptance | ≥85% of AI-prepared post-decision notifications dispatched without analyst correction; the remainder routed to analyst exception review before customer delivery. |
| Cycle | Average document collection cycle time from application intake to complete documentation set reduced by ≥30% for AI-managed applications within 12 months. |

#### Lending origination queue intelligence

- URN: urn:financial-services:scenario:flow/lending/lending-origination-queue-intelligence
- Lens: Insights
- Complexity: M
- Intent: Continuous view of origination cycle time, queue depth at credit review, and exception patterns across retail, SME, and corporate tracks — without manual reconstruction from disconnected case-management systems. Operations and credit leadership see which applications are stalled, at which stage, and for what reason, with intraday updates.
- Problem to solve: Origination cycle time, queue depth at credit review, and exception patterns are reconstructed manually each cycle from disconnected case-management systems. Underwriters and credit-committee secretaries lack a live picture of which applications are stalled and why.
- Solution: The AI agent reads across origination systems, classifies queue-state and stall reasons per application, and produces a continuous dashboard of cycle-time distribution and exception patterns by segment and underwriting track. Credit operations acts on the intraday view; monthly reporting is generated from the same data feed.
- OKR: Origination cycle time, queue depth at credit review, and stall reasons across retail, SME, and corporate tracks are continuously visible from aggregated case-management systems, replacing manual reconstruction each cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's origination queue dashboard covers ≥95% of active applications across all tracks with intraday updates within 6 months of go-live. |
| Acceptance | ≥80% of AI-produced queue intelligence views accepted by credit operations as decision-ready without manual supplementation. |
| Cycle | Time from queue-state change to operations-visible stall classification reduced from weekly manual reconstruction to ≤4 hours on a continuous basis. |

#### Underwriting capacity and routing optimization

- URN: urn:financial-services:scenario:flow/lending/lending-underwriting-capacity-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Dynamic routing of credit applications to fast-track, delegated-authority, or full-review tracks based on policy-eligible signals at intake, reducing senior-underwriter time on cases that policy already determines. Credit committee batching is reordered by urgency and completeness to maintain throughput.
- Problem to solve: Routing decisions — fast-track versus full review — and credit-committee batching are set at the policy level and rarely retuned. Senior underwriters spend disproportionate time on cases that policy already approves and on applications requiring early decline; retuning the routing rules requires multi-day modeling.
- Solution: The AI agent evaluates each application at intake against current policy parameters and routes it to the appropriate review track with a confidence score. Committee scheduling logic groups applications by completeness and decision-readiness; the credit secretariat reviews and confirms routing before cases move to the next stage.
- OKR: Credit applications are dynamically routed to fast-track, delegated-authority, or full-review tracks based on policy-eligible signals at intake, with committee batching sequenced by completeness and urgency to sustain throughput.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's routing recommendations applied to ≥85% of incoming credit applications within 6 months of go-live; committee scheduling logic deployed for ≥95% of weekly credit committee sessions. |
| Acceptance | ≥80% of the AI agent's routing recommendations confirmed by the credit secretariat without override before case advancement. |
| Cycle | Average senior-underwriter time per straightforward policy-eligible case reduced by ≥35% within 12 months of go-live. |

#### Credit decision copilot for underwriters

- URN: urn:financial-services:scenario:flow/lending/lending-credit-decision-copilot
- Lens: Enablement
- Complexity: M
- Intent: Structured synthesis of application data, bureau scores, collateral assessment, and policy-edge flags presented to underwriters at the point of case review. Credit committee pre-reads are assembled from the same synthesis, reducing preparation time and compressing the lag between application intake and committee-ready documentation.
- Problem to solve: Underwriters and credit-committee secretaries reconstruct application context manually from separate case-management systems each cycle. Decision explainability for delegated-authority cases is limited, and policy-edge flags surface in committee rather than before it.
- Solution: The AI agent assembles a structured case brief for each application — credit score, capacity-and-willingness summary, collateral status, policy flags, and comparable precedents — and presents it to the underwriter before review. Committee pre-reads are generated from the same structured inputs; the underwriter edits the brief before it advances to committee, and the credit secretariat checks the pre-read.
- OKR: Underwriters receive a structured case brief — credit score, capacity-and-willingness summary, collateral status, policy flags, and precedents — at the point of case review, with credit committee pre-reads assembled from the same synthesis.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's case brief used by underwriters for ≥85% of credit applications across retail and SME tracks within 9 months of go-live. |
| Acceptance | ≥80% of AI-assembled committee pre-reads accepted by the credit secretariat as ready for distribution without material reconstruction. |
| Cycle | Average preparation time from application intake to committee-ready documentation reduced by ≥40% within 12 months of go-live. |

#### Cross-segment lending learning transfer

- URN: urn:financial-services:scenario:flow/lending/lending-cross-segment-learning-transfer
- Lens: New opps
- Complexity: M
- Intent: Systematic propagation of policy-edge learnings, optimization wins, and exception patterns from retail origination to SME and corporate tracks, reducing the structural siloing that currently prevents cross-segment credit intelligence from improving origination quality across the Bank.
- Problem to solve: Optimization wins in retail rarely transfer to SME or corporate; cross-segment learnings stay siloed. Policy-edge cases and exception patterns found in one segment are not classified for their relevance to the others, so credit policy owners in peer segments never see them.
- Solution: The AI agent identifies policy-edge cases, exception patterns, and performance outliers across origination segments and classifies each for cross-segment applicability. A structured learning brief is distributed to credit policy owners quarterly; changes to routing rules or documentation requirements are reviewed by credit risk before adoption.
- OKR: Policy-edge learnings, optimization wins, and exception patterns from retail origination are systematically propagated to SME and corporate credit policy owners, reducing structural siloing across lending segments.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent identifies and classifies cross-segment learnings from ≥80% of finalized exception and outlier cases for ≥4 consecutive quarterly learning brief distributions within the first year. |
| Acceptance | ≥65% of AI-distributed cross-segment learning briefs result in credit policy owner review and a documented accept/reject decision within 30 days. |
| Cycle | Time from exception pattern identification in one origination segment to credit-policy-reviewed learning note in applicable peer segments reduced to ≤45 days. |

### Wealth Management {#wealth-management}

- URN: urn:financial-services:flow:wealth-management
- Summary: Investment, advisory, and portfolio management for affluent and high-net-worth clients. The stream turns on the advisory journey from goals to allocation to ongoing rebalancing.

Wealth Management covers client onboarding, goals-based financial planning, portfolio construction, trade execution, ongoing monitoring, and periodic review and rebalancing across affluent and high-net-worth segments. The relationship manager (RM) is the cycle's rate-limiting resource — client preparation, investment committee pre-reads, and portfolio review packs each draw on RM time before the client interaction occurs. The advisory cycle compounds the bottleneck: RM capacity spent in preparation is unavailable for client coverage, constraining the book size each RM can serve at advisory quality.

| Lens | Problem |
| --- | --- |
| Analyze | Portfolio performance attribution across asset classes, custodians, and client mandates is assembled from separate system extracts each review cycle. RMs and the investment committee have no continuous view of which mandates are drifting from strategic allocation or how book-level performance compares to benchmark. |
| Optimize | RM time allocation across client-facing and back-office preparation tasks is not tracked or rebalanced. High-effort preparation tasks — review packs, investment committee pre-reads, due-diligence synthesis — consume fixed hours per client regardless of mandate complexity or review materiality. |
| Automate | Client review pack assembly, investment committee pre-read drafting, and post-meeting follow-up extraction are fully manual. Each of these tasks is structurally similar across clients and cycles — text synthesis from structured inputs — and absorbs disproportionate RM capacity. |
| Enrich | Prospect pipeline intelligence and competitor positioning are gathered informally by RMs before prospect meetings. The institutional knowledge embedded in completed portfolio reviews, client interaction histories, and investment thesis notes is not systematically reused across the advisory team. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| discover | Discover | Client goals discovery and risk profiling | RM or advisor conducts the initial discovery conversation — documenting client goals, time horizon, risk tolerance, liquidity needs, and existing holdings. The stage produces the investment policy statement and determines the advisory mandate scope. | Discovery documentation is completed post-meeting from RM notes; structured data capture is incomplete and inconsistent across advisors. Subsequent stages depend on discovery quality, and gaps surface during portfolio construction rather than at the conversation. |
| plan | Plan | Financial planning and strategic asset allocation | Translation of client goals into a strategic asset allocation and financial plan. The stage determines target allocation by asset class, liability structure, tax overlay, and mandate constraints. | Financial plans are assembled manually by advisors, drawing on model portfolios, tax schedules, and client data held in separate systems. Plan quality depends on individual advisor depth; peer review is infrequent and informal. |
| construct | Construct | Portfolio construction and investment committee review | Specific security and fund selection within the approved strategic allocation. For managed mandates, the investment committee reviews and approves the recommended portfolio. The stage where institutional investment judgment is applied. | Investment committee pre-read packs are assembled by analysts from research notes, fund data, and prior meeting minutes — a process that takes days and compresses committee discussion time. Portfolio construction for new mandates draws on similar precedents held in analysts' personal files. |
| implement | Implement | Trade execution and mandate activation | Execution of the portfolio — trade orders, fund subscriptions, and cash management. The stage where the investment decision becomes a position and a custody record. | Trade execution across multiple custodians and fund administrators requires manual order routing and confirmation tracking. Partial fills and failed settlements return to the advisor queue without systematic escalation logic. |
| monitor | Monitor | Ongoing portfolio monitoring and exception flagging | Continuous monitoring of portfolio positions against mandate constraints, market events, and client-specific thresholds. Produces alerts for rebalancing triggers, limit breaches, and investment committee attention items. | Portfolio monitoring relies on end-of-day position snapshots from custody systems. Breaches of allocation bands or mandate constraints are flagged in the following day's report; intraday events that cross client thresholds go undetected until the next batch run. |
| review | Review | Periodic portfolio review, client meeting preparation, and rebalancing | Periodic review of portfolio performance and client goals alignment. The stage produces the client review pack, the rebalancing recommendation, and — for managed mandates — the investment committee update. | Client review packs are assembled manually by RMs from performance reports, market commentary, and the client's original plan. Preparation time per client is 3–5 hours; RMs with large books compress preparation quality or defer lower-tier reviews. |

#### Client review pack and IC pre-read automation

- URN: urn:financial-services:scenario:flow/wealth-management/wm-review-pack-automation
- Lens: Automation
- Complexity: S
- Intent: Assembly of client review packs, investment committee pre-reads, and post-meeting follow-up extracts by the AI agent from structured performance, market, and client-plan inputs. RM capacity released from preparation is directed toward client coverage and prospecting.
- Problem to solve: Client review pack assembly, investment committee pre-read drafting, and post-meeting follow-up extraction are fully manual. Each task is structurally similar across clients and cycles — text synthesis from structured inputs — yet absorbs 3–5 hours of RM time per client per review cycle.
- Solution: The AI agent assembles the review pack and the investment committee pre-read from performance reports, allocation data, market commentary, and the client's original plan. The RM reviews and edits the draft before client distribution; post-meeting action items are extracted from the meeting record and assigned with deadlines.
- OKR: Client review packs, investment committee pre-reads, and post-meeting follow-up extracts are assembled by the AI agent from structured performance, market, and client-plan inputs, with RMs reviewing and editing before client distribution.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent assembles the review pack for ≥85% of scheduled client reviews across the advisory book within 9 months of go-live. |
| Acceptance | ≥80% of AI-assembled review packs accepted by RMs as requiring editing rather than full redraft before client distribution. |
| Cycle | RM preparation time per client review cycle reduced from 3–5 hours of manual assembly to ≤45 minutes of review and editing within 12 months of go-live. |

#### Advisory discovery and suitability capture enablement

- URN: urn:financial-services:scenario:flow/wealth-management/wm-discovery-capture-enablement
- Lens: Enablement
- Complexity: S
- Intent: Structured in-meeting capture of client goals, risk tolerance, liquidity needs, and existing holdings, with the investment policy statement drafted by the AI agent for RM review and approval post-meeting. Downstream stages — planning, construction — receive consistent, complete discovery inputs rather than reconstructed RM notes.
- Problem to solve: Discovery documentation is completed post-meeting from RM notes; structured data capture is incomplete and inconsistent across RMs. Gaps surface during portfolio construction rather than at the discovery conversation, requiring the RM to re-engage the client for missing information.
- Solution: The AI agent provides the RM with a structured discovery guide and captures responses during the meeting using a mobile-accessible interface. The investment policy statement (IPS) draft is generated immediately post-meeting for RM review; the RM approves or edits before client signature and downstream system update.
- OKR: Structured discovery data — client goals, risk tolerance, liquidity needs, and existing holdings — is captured consistently across advisory conversations, with the investment policy statement drafted by the AI agent for RM review and approval post-meeting.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's discovery capture and IPS drafting used by RMs for ≥80% of new client discovery meetings within 9 months of go-live. |
| Acceptance | ≥80% of AI-drafted investment policy statements accepted by RMs as requiring editing rather than full redraft before client signature. |
| Cycle | Time from discovery meeting completion to approved IPS available for downstream planning reduced from multi-day post-meeting reconstruction to ≤24 hours. |

#### Wealth portfolio drift and mandate-breach monitoring

- URN: urn:financial-services:scenario:flow/wealth-management/wm-portfolio-drift-monitoring
- Lens: Insights
- Complexity: M
- Intent: Continuous monitoring of portfolio positions against mandate constraints, strategic allocation bands, and client-specific thresholds — with intraday breach detection replacing end-of-day batch reporting. Investment operations and RMs receive an alert feed calibrated to materiality rather than batch-cycle cadence.
- Problem to solve: Portfolio monitoring relies on end-of-day position snapshots from custody systems. Breaches of allocation bands or mandate constraints are flagged in the following day's report; intraday events that cross client thresholds go undetected until the next batch run.
- Solution: The AI agent reads intraday position data from custody feeds, evaluates positions against mandate and client-specific parameters, and generates a prioritized alert feed for investment operations and RMs. Alert materiality thresholds are set per mandate type; the RM reviews and approves any rebalancing action before execution.
- OKR: Portfolio positions are monitored continuously against mandate constraints, strategic allocation bands, and client-specific thresholds with intraday breach detection, replacing end-of-day batch reporting.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's intraday monitoring covers ≥95% of active mandates and client portfolios with position refresh intervals of ≤30 minutes within 6 months of go-live. |
| Acceptance | ≥80% of AI-generated breach alerts confirmed as actionable by investment operations and RMs within the first 3 months; ongoing false-alert rate ≤5%. |
| Cycle | Portfolio breach detection lag reduced from the following day's batch report to ≤30 minutes from the position event. |

#### RM time allocation and book-capacity optimization

- URN: urn:financial-services:scenario:flow/wealth-management/wm-rm-time-allocation-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Rebalancing of RM time across client-facing and back-office preparation tasks based on mandate complexity and review materiality, enabling each RM to serve a larger book at advisory quality. Preparation effort is directed toward reviews with the highest complexity and commercial significance rather than distributed uniformly.
- Problem to solve: RM time allocation across client-facing and back-office preparation tasks is not tracked or rebalanced. High-effort preparation tasks — review packs, investment committee pre-reads, due-diligence synthesis — consume fixed hours per client regardless of mandate complexity or review materiality.
- Solution: The AI agent tracks preparation effort per client across review cycles, identifies where high RM time consumption does not correspond to mandate complexity or AUM materiality, and recommends reallocation. The head of wealth reviews the time-allocation analysis quarterly; AI-assisted preparation covers low-complexity reviews, freeing RM hours for high-value client engagement.
- OKR: RM preparation effort is rebalanced across the client book on the basis of mandate complexity and review materiality, enabling each RM to serve a larger book at advisory quality.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's time-allocation analysis reviewed by the head of wealth for ≥4 consecutive quarters within the first year; reallocation recommendations applied across ≥80% of the advisory book. |
| Acceptance | ≥75% of the AI agent's preparation-effort reallocation recommendations accepted by the head of wealth without material revision. |
| Cycle | Average RM preparation hours per low-complexity review cycle reduced by ≥40% within 12 months of go-live, with released hours verified against time-recording data. |

#### Wealth prospect and competitive intelligence enrichment

- URN: urn:financial-services:scenario:flow/wealth-management/wm-prospect-intelligence-enrichment
- Lens: New opps
- Complexity: M
- Intent: Systematic reuse of institutional knowledge from completed portfolio reviews, client interaction histories, and investment thesis notes for prospect preparation and competitive positioning across the advisory team. Prospect meetings are informed by the Bank's own asset-class experience and client outcome history rather than relying on individual RM knowledge.
- Problem to solve: Prospect pipeline intelligence and competitor positioning are gathered informally by individual RMs before prospect meetings. The institutional knowledge embedded in completed reviews, client histories, and investment thesis notes is not systematically reused across the advisory team.
- Solution: The AI agent indexes completed reviews, investment thesis notes, and client outcome data, and assembles a prospect brief on request — relevant asset-class experience, anonymized comparable client profiles, and competitive positioning. The RM reviews the brief before the prospect meeting; the knowledge base is updated after each completed engagement.
- OKR: Institutional knowledge from completed portfolio reviews, client interaction histories, and investment thesis notes is systematically indexed and assembled into prospect briefs, giving the advisory team consistent preparation across the book.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's prospect brief used by RMs for ≥75% of qualified prospect meetings within 9 months of go-live; knowledge base updated after ≥85% of completed engagements. |
| Acceptance | ≥75% of AI-produced prospect briefs accepted by RMs as decision-informing without material supplementation before the prospect meeting. |
| Cycle | Time from prospect meeting request to RM-reviewed brief reduced from informal multi-day information gathering to ≤4 hours. |

### Bancassurance (insurance distribution) {#bancassurance}

- URN: urn:financial-services:flow:bancassurance
- Summary: Insurance distribution through the Bank's channels. The stream turns on the cross-sell journey at the moment of customer life events.

Bancassurance distributes insurance products — life, mortgage protection, general, and health — through the Bank's branch, digital, and relationship-banking channels, typically under partnership or captive insurer arrangements. The cycle anchors on life-event triggers: a mortgage origination prompts mortgage protection, a salary increase prompts life and savings-linked products, a business loan prompts trade credit or key-man cover. Frontline staff capacity to identify the trigger, position the offer, and support the sale conversation is the primary constraint — not product breadth or customer eligibility.

| Lens | Problem |
| --- | --- |
| Analyze | Insurance conversion rates by channel, frontline staff, and product are tracked at the total level without decomposition by trigger type, offer stage, or customer segment. The Bank cannot identify which life-event triggers carry the highest conversion probability or where the offer conversation most commonly breaks down. |
| Optimize | Customer eligibility and propensity intelligence from the Bank's account data are not systematically used to rank which customers to contact for which product. Cross-sell targeting is driven by product campaigns rather than behavioral signals from the customer's transactional relationship with the Bank. |
| Automate | Post-sale policy documentation, disclosure pack delivery, and premium setup each require separate manual steps. The sequence between sale agreement and policy binding involves hand-offs across bancassurance operations, the partner insurer's platform, and the Bank's payment system. |
| Enrich | Frontline staff positioning of insurance products is not supported by real-time guidance on which product to offer, what to say, or how to handle common objections. Staff rely on periodic training and printed product guides; offer quality and compliance-disclosure completeness are not measured per interaction. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| identify | Identify trigger | Identify customer life-event trigger and eligibility | Detection of a customer life event — mortgage funding, income change, business milestone, deposit maturity — that creates insurance eligibility or need. The stage determines which product to position and to whom. | Life-event triggers are identified reactively by frontline staff during customer contact rather than proactively from transaction and account data. High-value triggers — mortgage funding, large balance movements — pass without structured insurance positioning in the majority of customer interactions. |
| position | Position offer | Position and frame the insurance offer | Frontline staff or digital channel presents the insurance offer in the context of the customer's event. The stage defines the conversation frame, the product features most relevant to the customer's circumstances, and the compliance disclosures required. | Frontline staff have inconsistent familiarity with insurance product features and compliance disclosure requirements. Positioning quality depends on individual training recency; customers receive offers at different depths and with variable disclosure completeness. |
| underwrite | Underwrite | Insurance underwriting and eligibility confirmation | Assessment of customer eligibility under the insurer's underwriting criteria — health declarations, sum-assured limits, product restrictions. The gateway between offer and binding. | Underwriting questions are presented as static forms regardless of product or customer profile. Customers with straightforward eligibility complete the same declaration set as those near underwriting boundaries; completion rates fall with form length. |
| sell-onboard | Sell & onboard | Sale completion, documentation, and policy issuance | Policy application completion, disclosure document delivery, premium collection arrangement, and policy issuance. The stage where the sale converts to a bound insurance relationship. | Policy documentation and disclosure packs are generated from static templates and delivered separately from the sale conversation. Premium setup requires a separate operational step in most channels; completion rate drops between sale agreement and policy binding. |
| retain | Retain | Policy retention, lapse management, and cross-sell | Ongoing relationship management — renewal prompts, lapse intervention, claims support, and identification of additional coverage needs as customer circumstances evolve. | Policy lapse events are identified at renewal only, after the customer has already decided to discontinue. Intermediate signals — missed premiums, life-event changes, balance-behavior shifts — are not used to initiate proactive retention contact. |

#### Insurance positioning and disclosure enablement for frontline staff

- URN: urn:financial-services:scenario:flow/bancassurance/banc-frontline-positioning-enablement
- Lens: Enablement
- Complexity: S
- Intent: Real-time product positioning guidance and compliance-disclosure prompts for frontline staff at the point of a customer life-event trigger, calibrated to the specific product and customer profile. Offer quality and disclosure completeness are consistent across the channel rather than dependent on individual training recency.
- Problem to solve: Frontline staff have inconsistent familiarity with insurance product features and compliance disclosure requirements. Positioning quality depends on individual training recency; customers receive offers at different depths and with variable disclosure completeness across the channel.
- Solution: The AI agent surfaces a product-specific positioning guide and mandatory disclosure checklist to the frontline staff member at the point of the identified trigger. The guide adapts to the product being offered and the customer's profile; the staff member confirms disclosure completion before closing the offer conversation, and compliance review checks the confirmations.
- OKR: Insurance product positioning quality and compliance disclosure completeness are consistent across frontline channels, with real-time guidance calibrated to the specific product and customer profile at the point of each life-event trigger.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-supplied positioning guide and disclosure checklist used by frontline staff for ≥85% of insurance offer conversations within 6 months. |
| Acceptance | ≥90% of disclosure completion confirmations accepted by compliance review as complete and accurate without remediation. |
| Cycle | Average time from trigger identification to offer-ready frontline presentation reduced from same-day manual retrieval to ≤2 minutes per interaction. |

#### Bancassurance policy onboarding automation

- URN: urn:financial-services:scenario:flow/bancassurance/banc-policy-onboarding-automation
- Lens: Automation
- Complexity: M
- Intent: AI-driven post-sale sequence — policy documentation generation, disclosure pack delivery, premium collection setup, and insurer platform hand-off — reducing the manual steps between sale agreement and policy binding. Drop-off between sale and bound policy is reduced by eliminating the separate operational steps that currently interrupt the sequence.
- Problem to solve: Post-sale policy documentation, disclosure pack delivery, and premium setup each require separate manual steps across bancassurance operations, the partner insurer's platform, and the Bank's payment system. Completion rate drops between sale agreement and policy binding as hand-offs accumulate.
- Solution: The AI agent triggers the post-sale sequence on sale confirmation — generates the documentation pack, delivers disclosure materials through the customer's preferred channel, initiates premium setup, and submits the policy application to the insurer's platform. Bancassurance operations reviews the status feed and intervenes on exceptions; the customer receives a single coordinated communication.
- OKR: The post-sale policy onboarding sequence — documentation, disclosure delivery, premium setup, and insurer platform hand-off — is AI-driven from sale confirmation to policy binding, with bancassurance operations reviewing exceptions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent manages the end-to-end post-sale sequence for ≥85% of eligible bancassurance policy sales within 6 months of go-live. |
| Acceptance | ≥90% of AI-generated documentation packs accepted by bancassurance operations without manual rework before insurer submission. |
| Cycle | Sale-to-bound-policy cycle time reduced by ≥40% for eligible policies within 12 months of go-live. |

#### Bancassurance conversion and trigger analytics

- URN: urn:financial-services:scenario:flow/bancassurance/banc-conversion-trigger-analytics
- Lens: Insights
- Complexity: M
- Intent: Decomposition of insurance conversion rates by life-event trigger type, channel, frontline staff, and offer stage, identifying which triggers carry the highest conversion probability and where the offer conversation breaks down. Product and training investments are directed at the highest-return points in the sales funnel.
- Problem to solve: Insurance conversion rates by channel, staff, and product are tracked at the total level without decomposition by trigger type, offer stage, or customer segment. The Bank cannot identify which life-event triggers carry the highest conversion probability or where the offer conversation most commonly breaks down.
- Solution: The AI agent classifies each insurance interaction by trigger type, offer stage, and outcome, assembles a conversion funnel view by segment and channel, and surfaces it to the bancassurance and frontline leadership teams. Training and script adjustments are directed at the stages with the highest observed drop-off rates.
- OKR: Conversion analytics are decomposed by trigger type, offer stage, channel, and frontline staff, directing product investment and training to the highest-return points in the bancassurance sales funnel.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent classifies ≥90% of insurance interactions by trigger type and offer stage within 3 months of go-live. |
| Acceptance | ≥80% of funnel decomposition views accepted by bancassurance and frontline leadership without material amendment. |
| Cycle | Conversion analysis cycle time reduced from multi-week manual reconstruction to a continuously refreshed view available within 24 hours of request. |

#### Insurance offer sequencing and propensity optimization

- URN: urn:financial-services:scenario:flow/bancassurance/banc-offer-sequencing-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Propensity-ranked insurance offer sequencing based on transaction and account behavioral signals from the Bank's own data, replacing product-campaign-driven targeting with customer-need-driven contact prioritization. Frontline staff and digital channels engage customers with the offer most likely to convert at the right moment in the customer's lifecycle.
- Problem to solve: Customer eligibility and propensity intelligence from the Bank's account data are not systematically used to rank which customers to contact for which product. Cross-sell targeting is driven by product campaigns rather than behavioral signals from the customer's transactional relationship with the Bank.
- Solution: The AI agent scores the customer base by product propensity using transaction, balance, and life-event signals, and produces a ranked contact list for frontline and digital channels. Campaign management reviews the propensity rankings before contact execution; actual conversion data retrains the propensity model on a rolling basis.
- OKR: Insurance cross-sell contact sequencing is driven by customer propensity scores derived from transaction and account behavioral data, replacing product-campaign-based targeting.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's propensity rankings used for ≥80% of bancassurance contact prioritization decisions across frontline and digital channels within 9 months. |
| Acceptance | ≥75% of ranked contact lists accepted by campaign management without material reordering. |
| Cycle | Time from data cut to distribution-ready propensity-ranked contact list reduced from a multi-week modeling cycle to ≤48 hours on a rolling basis. |

#### Policy lapse early-warning and retention

- URN: urn:financial-services:scenario:flow/bancassurance/banc-lapse-early-warning
- Lens: New opps
- Complexity: M
- Intent: Early-warning signals for policy lapse risk derived from intermediate behavioral indicators — missed premiums, life-event changes, balance-behavior shifts — enabling proactive retention contact before the customer's renewal decision is made. Lapse intervention is most effective in the window before the decision point, not after it.
- Problem to solve: Policy lapse events are identified at renewal only, after the customer has already decided to discontinue. Intermediate signals — missed premiums, life-event changes, balance-behavior shifts — are not used to initiate proactive retention contact.
- Solution: The AI agent monitors premium payment behavior, life-event signals in transaction data, and account balance trends for active policyholders, and generates a lapse-risk score updated monthly. Relationship managers and bancassurance operations receive a ranked retention contact list with the primary signal driving each customer's risk score; outreach is personalized to the identified trigger.
- OKR: Proactive retention contact is initiated in the pre-decision window for at-risk policyholders, using behavioral and premium payment signals to identify lapse risk before the customer's renewal decision is made.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's lapse-risk scoring covers ≥95% of the active policyholder base on a monthly cadence within 6 months of go-live. |
| Acceptance | ≥75% of AI-flagged high-risk retention cases confirmed as actionable by relationship managers and bancassurance operations. |
| Cycle | Lapse-risk identification lead time extended from policy renewal date to ≥60 days prior, measured across the retained policyholder portfolio. |

### Treasury & Funding {#treasury-funding}

- URN: urn:financial-services:flow:treasury-funding
- Summary: The Bank's own funding and liquidity management. The stream turns on the funding-decision rhythm against the maturity ladder.

Treasury & Funding covers the Bank's own balance-sheet funding — cash forecasting, wholesale and retail funding execution, intraday and structural liquidity management, asset-liability matching, and the reporting and narrative cycle to ALCO, the board, and the regulator (including liquidity returns under prudential standards such as the Basel III LCR and NSFR). The cycle's competing constraints are funding cost minimization and regulatory liquidity floor maintenance; most of the friction sits in forecast accuracy, intraday liquidity visibility, and the narrative production cycle that runs alongside every ALCO meeting.

| Lens | Problem |
| --- | --- |
| Analyze | Funding cost, liquidity ratio headroom, and forecast accuracy are tracked in static reports produced for each ALCO cycle. Treasury has no continuous view of forecast error attribution, funding cost decomposition by instrument, or how regulatory ratio headroom is evolving across the inter-ALCO period. |
| Optimize | Funding mix decisions are made weekly against a point-in-time view of costs and ratios. Scenario analysis across instrument options — comparing cost against LCR, NSFR, and leverage impacts — is manual and takes hours; the window for acting on intraweek market opportunities is often missed. |
| Automate | ALCO pack assembly, regulatory return production, and the narrative explaining liquidity position changes are fully manual each cycle. The process is structurally similar across periods — pulling data from known sources, applying consistent methodology, narrating variances — and is the primary constraint on ALCO preparation quality. |
| Enrich | Rating agency and counterparty due diligence cycles create episodic demands on Treasury for structured narrative on funding strategy, liquidity position, and capital adequacy. These demands are handled reactively with bespoke document production each time, drawing on institutional knowledge held in individuals. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| forecast | Forecast | Cash and liquidity forecasting | Production of the short- and medium-term cash and liquidity forecast — covering expected outflows, asset maturities, committed facilities, and behavioral deposit assumptions. The forecast drives funding plan decisions for the coming period. | Cash forecasts are assembled from multiple treasury and operations systems with different update cadences. Forecast accuracy degrades across the 5–30 day horizon; Treasury manages forecast error through buffers that carry a cost. |
| plan | Plan funding | Funding mix planning and instrument selection | Decision on the funding mix for the period — retail deposit pricing, wholesale issuance, repo, and interbank borrowing — against the maturity ladder, cost constraints, and regulatory ratio targets. | Funding mix decisions are made by Treasury in a weekly planning session using prior-period actuals and the current forecast. Scenario analysis — cost of different instrument mixes against LCR and NSFR targets — is performed in spreadsheets and is slow to update when market conditions shift intraweek. |
| execute | Execute | Funding execution and market transactions | Execution of funding transactions — deposit rate changes, wholesale paper issuance, repo, and interbank borrowing. The stage where the funding plan becomes a balance-sheet position. | Funding execution is fragmented across dealing desk, deposit operations, and corporate treasury systems. Position reconciliation after each execution step is manual; intraday liquidity position updates lag execution by hours. |
| monitor | Monitor | Intraday liquidity monitoring and limit management | Real-time and near-real-time monitoring of intraday liquidity position, LCR and NSFR headroom, and limit utilization. The stage that detects emerging shortfalls before they reach threshold breaches. | Intraday liquidity monitoring draws on payment system feeds updated at intervals rather than in real time. The treasury operations team's view of the liquidity position lags by 30–90 minutes; contingency actions are reactive rather than anticipatory. |
| report | Report & narrate | ALCO reporting, regulatory filing, and narrative | Production of the ALCO pack, the regulatory liquidity returns (such as the Basel LCR and NSFR), and the treasury narrative for board and senior management. The stage where the period's funding decisions are explained and judged. | ALCO packs and regulatory returns are assembled manually from treasury, finance, and risk systems each reporting cycle. The narrative explaining variances from plan is drafted by Treasury after the data pack is finalized; the full cycle takes days and compresses ALCO discussion time. |

#### Rating agency and counterparty posture brief

- URN: urn:financial-services:scenario:flow/treasury-funding/trs-rating-agency-posture-brief
- Lens: New opps
- Complexity: S
- Intent: On-demand posture briefing for rating-agency and counterparty due diligence interactions, assembled from the Bank's current funding strategy, liquidity position, and capital adequacy data. Agency-relationship leads work from a current-state brief rather than spending days on bespoke manual reconstruction for each interaction.
- Problem to solve: Rating agency and counterparty due diligence cycles create episodic demands on Treasury for structured narrative on funding strategy, liquidity position, and capital adequacy. These demands are handled reactively with bespoke document production each time, drawing on institutional knowledge held in individuals.
- Solution: The AI agent maintains a continuous treasury posture summary in structured form — funding strategy rationale, current LCR/NSFR levels, capital adequacy overview, and key sensitivity narratives — and assembles an agency-facing brief on demand. Treasury leadership reviews and approves the brief before distribution; prior briefings are retained for consistency tracking across agency interaction cycles.
- OKR: On-demand posture briefings for rating agency and counterparty due diligence interactions are assembled from the Bank's continuously maintained treasury posture summary, with Treasury leadership reviewing and approving each brief before distribution.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent assembles a posture brief for 100% of rating agency and counterparty due diligence requests within 3 hours of request during the first 12 months after go-live. |
| Acceptance | ≥85% of AI-produced posture briefs accepted by Treasury leadership without material amendment before distribution; consistency review confirms alignment with prior briefings in ≥90% of cases. |
| Cycle | Briefing preparation time reduced from multi-day bespoke document production to ≤3 hours from request to a brief ready for Treasury leadership review. |

#### Treasury cash forecast accuracy attribution

- URN: urn:financial-services:scenario:flow/treasury-funding/trs-forecast-accuracy-attribution
- Lens: Insights
- Complexity: M
- Intent: Continuous attribution of cash forecast errors by source, horizon, and instrument type, giving Treasury a running view of where accuracy degrades across the 5–30 day horizon and which behavioral deposit assumptions carry the most variance. Forecast buffers are calibrated to identified error patterns rather than held at uniform levels.
- Problem to solve: Cash forecasts are assembled from multiple treasury and operations systems with different update cadences, and accuracy degrades across the 5–30 day horizon. Treasury has no continuous view of where forecast error comes from, so it manages the error through uniform buffers that carry a cost.
- Solution: The AI agent tracks each cash forecast cohort from production to realization, attributes errors to source — behavioral deposit variance, payment system timing, wholesale maturity rollover — and produces a continuous accuracy view by horizon. Treasury uses the attribution to adjust buffer levels and refine the behavioral deposit model assumptions presented at ALCO.
- OKR: Cash forecast errors are attributed continuously by source, horizon, and instrument type, giving Treasury a running view of where accuracy degrades across the 5–30 day horizon and which behavioral deposit assumptions carry the most variance.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent tracks forecast cohorts from production to realization for ≥95% of published cash forecasts across active horizons within 6 months of go-live. |
| Acceptance | ≥80% of the AI agent's attribution views accepted by Treasury as accurate and decision-ready for buffer calibration and behavioral deposit model adjustment at each ALCO cycle. |
| Cycle | Interval from forecast period realization to attribution-complete accuracy view available to Treasury reduced from the next ALCO cycle preparation to ≤3 business days. |

#### Funding mix scenario optimization

- URN: urn:financial-services:scenario:flow/treasury-funding/trs-funding-mix-scenario-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Rapid scenario comparison of funding instrument mixes against LCR, NSFR, and leverage ratio targets, enabling intraweek funding decisions without multi-hour manual spreadsheet analysis. Treasury acts on intraweek market opportunities within the window they are available rather than after the window has closed.
- Problem to solve: Funding mix decisions are made against a point-in-time weekly view. Scenario analysis across instrument options — comparing cost against LCR, NSFR, and leverage impacts — is manual and takes hours; the window for acting on intraweek market opportunities is often missed.
- Solution: The AI agent runs funding-mix scenarios on demand — specifying instrument type, volume, and tenor — and returns the cost, ratio, and maturity-ladder impact within minutes. Treasury reviews the scenario output before any execution; the model is updated with live rate and ratio data from treasury systems.
- OKR: Funding-mix scenario comparison across instrument types, volumes, and tenors — evaluated against LCR, NSFR, and leverage ratio impacts — is available to Treasury within minutes of parameter entry, enabling intraweek market opportunities to be acted on within the available window.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's scenario tool used for ≥80% of intraweek and ALCO-preparatory funding-mix decisions within 9 months of go-live. |
| Acceptance | ≥80% of the AI agent's scenario outputs accepted by Treasury as analytically sound without remodeling before execution review. |
| Cycle | Time from scenario request to cost-and-ratio-impact output reduced from hours of manual spreadsheet analysis to ≤15 minutes per scenario run. |

#### ALCO pack and regulatory liquidity return automation

- URN: urn:financial-services:scenario:flow/treasury-funding/trs-alco-pack-automation
- Lens: Automation
- Complexity: M
- Intent: AI-assembled ALCO pack, regulatory liquidity returns (such as the Basel III LCR and NSFR), and variance narrative — pulling from treasury, finance, and risk systems on the established reporting cycle with Treasury review before distribution. The CFO and ALCO chair receive a decision-quality pack without the current multi-day manual production cycle.
- Problem to solve: ALCO packs and regulatory returns are assembled manually from treasury, finance, and risk systems each reporting cycle. The narrative explaining variances from plan is drafted by Treasury after the data pack is finalized; the full cycle takes days and compresses ALCO discussion time.
- Solution: The AI agent pulls data from treasury, finance, and risk systems on the reporting calendar, assembles the ALCO pack structure, takes the LCR and NSFR ratios from the approved regulatory calculation, and drafts the variance narrative. Treasury reviews and edits the pack; the final version is approved by the CFO or Head of Treasury before distribution to ALCO members.
- OKR: ALCO pack, regulatory LCR/NSFR returns, and variance narrative are assembled by the AI agent from treasury, finance, and risk systems on the established reporting calendar, with Treasury reviewing and editing before distribution to ALCO members.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent assembles the full ALCO pack and regulatory returns for ≥11 of 12 monthly ALCO cycles in the first year of go-live. |
| Acceptance | ≥80% of AI-produced ALCO packs accepted by the Head of Treasury or CFO as requiring editing rather than full reconstruction before distribution. |
| Cycle | ALCO pack production cycle from data pull to distribution-ready pack reduced by ≥3 business days compared to the manual multi-day baseline. |

#### Intraday liquidity position copilot

- URN: urn:financial-services:scenario:flow/treasury-funding/trs-intraday-liquidity-copilot
- Lens: Enablement
- Complexity: M
- Intent: Near-real-time intraday liquidity position synthesis from payment system feeds and settlement data, reducing the 30–90 minute monitoring lag and giving treasury operations anticipatory rather than reactive visibility. Contingency actions are prepared before a threshold breach rather than triggered after it is reported.
- Problem to solve: Intraday liquidity monitoring draws on payment system feeds updated at intervals rather than in real time. The treasury operations team's view of the liquidity position lags by 30–90 minutes; contingency actions are reactive rather than anticipatory.
- Solution: The AI agent aggregates intraday payment system feeds, settlement confirmations, and committed facility drawdown data into a continuously updated liquidity position view. Treasury operations reviews the dashboard in real time; the AI agent generates an alert and recommended contingency action when the projected position approaches a regulatory or internal limit threshold.
- OKR: Intraday liquidity position is synthesized continuously from payment system feeds and settlement confirmations, reducing the monitoring lag to near-real-time and giving treasury operations anticipatory visibility for contingency action preparation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's intraday liquidity dashboard active for ≥99% of business days with position refresh intervals of ≤10 minutes within 6 months of go-live. |
| Acceptance | ≥80% of AI-generated contingency action recommendations judged appropriate by treasury operations on review, ahead of any threshold breach. |
| Cycle | Intraday position monitoring lag reduced from the current 30–90 minute interval to ≤10 minutes on a continuous operating basis. |

### FX & Cross-border {#fx-cross-border}

- URN: urn:financial-services:flow:fx-cross-border
- Summary: Multi-currency operations and international transfers. The stream turns on the timing of FX conversion and settlement against what customers expect.

FX & Cross-border covers corporate and retail FX conversion, international payment initiation, correspondent bank routing, settlement, and reconciliation. In markets with currency controls, the cycle carries additional regulatory specificity: currency-control notifications, cross-border transfer reporting thresholds, and corridor-specific correspondent routing constraints. The cycle's competing pressures are price transparency (customer expectation for FX rate and fee certainty at the point of order) and settlement timing (correspondent bank chains introduce latency and status uncertainty that the originating bank cannot resolve unilaterally).

| Lens | Problem |
| --- | --- |
| Analyze | FX exception rates, settlement failure causes, and nostro break volumes are tracked in end-of-day reports from individual systems with no cross-corridor aggregation. Operations cannot identify which correspondent bank corridors carry the highest exception rates or what settlement failure causes are systematic versus episodic. |
| Optimize | Correspondent bank routing decisions for cross-border payments are encoded in static routing tables that are reviewed infrequently. Routing optimization — selecting the correspondent path with the lowest expected settlement failure rate and cost — is not a continuous process. |
| Automate | Nostro reconciliation, SWIFT exception triage, and currency-control notification preparation are manual daily tasks consuming treasury operations capacity. Each task is rule-governed and draws on structured data; the structural similarity across periods makes them candidates for end-to-end automation. |
| Enrich | Corporate clients with material FX exposures lack a systematic intelligence service on rate movements against their hedging thresholds. The Bank's FX data — pricing history, corridor volumes, settlement timing — is not used to generate client-specific FX intelligence or early-warning alerts. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| capture | Capture order | Customer order capture and pre-flight checks | Customer initiates an FX or cross-border payment order — amount, currency pair, beneficiary, value date, and purpose code for regulatory reporting. Pre-flight checks confirm beneficiary validity, AML screening, and currency-control reporting obligations. | Order capture across channels (branch, digital, corporate banking portal) produces inconsistent purpose-code classification for currency-control reporting to the regulator. Misclassified orders generate remediation requests from operations before payment can proceed. |
| price | Price & quote | FX pricing and customer quote | Rate calculation and quote delivery to the customer — spot or forward rate, spread, and fee components. The stage where the Bank's FX economics and the customer's price expectation intersect. | Corporate clients with recurring FX needs receive indicative rates through relationship managers without a structured rate-monitoring or alert mechanism. Clients execute at market rather than at pre-agreed thresholds because the Bank does not surface rate-trigger intelligence proactively. |
| execute | Execute | FX execution and payment instruction release | Execution of the FX conversion and release of the payment instruction to the correspondent bank chain. For corporate clients, the execution may involve a forward leg or a multi-currency sweep. | Payment instruction release to correspondent banks follows manual SWIFT messaging for non-straight-through-processing corridors. Payments in some regional corridors carry format-specific requirements that are not fully encoded in the payment factory's routing rules, generating manual intervention before release. |
| settle | Settle | Settlement through correspondent bank chain | Settlement of the payment through the correspondent chain — tracking of SWIFT status messages, identification of held or rejected payments, and escalation of exceptions to the relevant correspondent bank. | Settlement status tracking across multiple correspondent banks relies on SWIFT MT199/MT299 messaging that arrives asynchronously and is monitored by operations manually. Held or rejected payments in the correspondent chain are identified with a lag; customer-facing status updates are delayed. |
| reconcile | Reconcile | Nostro reconciliation and reporting | Reconciliation of the Bank's nostro accounts against correspondent bank statements — identification of breaks, unmatched items, and currency position errors. The operational close of the payment and the compliance input for currency-control reporting. | Nostro reconciliation across multiple correspondent banks and currencies is performed daily from manually downloaded statements. Break identification and investigation consumes treasury operations time; cross-border reporting to the regulator draws on the same reconciliation output, extending the reporting cycle. |

#### FX purpose-code classification enablement

- URN: urn:financial-services:scenario:flow/fx-cross-border/fx-purpose-code-classification-enablement
- Lens: Enablement
- Complexity: S
- Intent: Intelligent purpose-code classification at FX and cross-border payment order capture across channels, reducing misclassification-driven remediation requests before payment release under currency-control rules. The correct regulatory classification is proposed to the customer or handler at the point of order entry.
- Problem to solve: Order capture across channels produces inconsistent purpose-code classification for currency-control reporting. Misclassified orders generate remediation requests from operations before payment can proceed, extending settlement cycle time and consuming operations capacity.
- Solution: The AI agent analyzes the payment instruction — beneficiary type, amount, currency, and transaction description — and proposes the most likely regulatory purpose code with a confidence level. The handler or customer confirms or overrides the classification before order submission; low-confidence classifications are flagged for mandatory operations review.
- OKR: Intelligent purpose-code classification is proposed at FX and cross-border payment order capture, reducing misclassification-driven remediation requests before payment release under currency-control rules.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's purpose-code classification deployed across ≥90% of FX and cross-border payment order capture channels within 6 months of go-live. |
| Acceptance | ≥85% of the AI agent's purpose-code proposals confirmed by handlers or customers without override at order entry; operations remediation request rate reduced by ≥30% within 12 months. |
| Cycle | Average settlement delay attributable to purpose-code remediation reduced by ≥40% for channels using AI-assisted classification within 12 months. |

#### FX corridor exception and settlement failure analytics

- URN: urn:financial-services:scenario:flow/fx-cross-border/fx-exception-corridor-analytics
- Lens: Insights
- Complexity: M
- Intent: Cross-corridor aggregation of FX exception rates, settlement failure causes, and nostro break volumes — identifying which correspondent bank corridors carry systematic failure patterns and which exceptions are episodic. Operations and Treasury prioritize correspondent relationship management at the corridors with the highest systemic cost.
- Problem to solve: FX exception rates, settlement failure causes, and nostro break volumes are tracked in end-of-day reports from individual systems with no cross-corridor aggregation. Operations cannot identify which correspondent bank corridors carry the highest exception rates or what settlement failure causes are systematic versus episodic.
- Solution: The AI agent aggregates exception data across corridors and correspondent banks, classifies failure causes by type and frequency, and produces a ranked corridor-risk view updated daily. Treasury operations uses the corridor ranking to prioritize correspondent bank engagement; the view also informs routing-table review decisions.
- OKR: FX exception rates, settlement failure causes, and nostro break volumes are aggregated cross-corridor and classified by failure type, giving operations and Treasury a ranked corridor-risk view for correspondent relationship prioritization.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent aggregates exception and settlement failure data across ≥95% of active correspondent corridors with daily updates within 6 months of go-live. |
| Acceptance | ≥75% of AI-identified systemic corridor failure patterns confirmed as actionable by treasury operations for correspondent bank engagement prioritization. |
| Cycle | Time from corridor exception pattern emergence to a treasury-operations-reviewed ranked risk view reduced from ad hoc manual assembly across separate end-of-day reports to ≤1 business day on the daily refresh. |

#### FX correspondent routing table optimization

- URN: urn:financial-services:scenario:flow/fx-cross-border/fx-correspondent-routing-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Monthly, signal-driven optimization of correspondent routing tables for cross-border corridors based on settlement failure rates, cost, and format-compliance signals — replacing the current infrequent manual review of static routing rules. The Bank routes each payment through the correspondent path with the lowest expected settlement failure rate within the available cost envelope.
- Problem to solve: Correspondent bank routing decisions for cross-border payments are encoded in static routing tables reviewed infrequently. Routing optimization — selecting the correspondent path with the lowest settlement failure rate and cost — is not a continuous process.
- Solution: The AI agent monitors settlement outcomes, format-rejection rates, and cost by correspondent path for each corridor, generates an updated routing recommendation set monthly, and flags high-deterioration corridors for immediate review. Treasury operations reviews the routing recommendations before they are applied to the payment factory's configuration.
- OKR: Correspondent routing tables for cross-border corridors are reviewed monthly, and on deterioration signals, against settlement failure rates, cost, and format-compliance signals, replacing infrequent manual review of static routing rules.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent generates updated routing recommendation sets for 100% of active corridors on a monthly cadence within 6 months of go-live; high-deterioration corridors flagged for immediate review within 24 hours of threshold breach. |
| Acceptance | ≥80% of the AI agent's routing recommendations accepted by treasury operations without material override before configuration update. |
| Cycle | Routing-table review cycle shortened from infrequent manual reviews to a monthly cadence, with high-risk corridor updates processed within 48 hours. |

#### Nostro reconciliation and currency-control notification automation

- URN: urn:financial-services:scenario:flow/fx-cross-border/fx-nostro-reconciliation-automation
- Lens: Automation
- Complexity: M
- Intent: AI-driven nostro reconciliation, SWIFT exception triage, and currency-control notification preparation for regulatory reporting obligations, with treasury operations review of break dispositions. Treasury operations capacity is directed toward correspondent relationship management and exception escalation rather than daily reconciliation mechanics.
- Problem to solve: Nostro reconciliation across multiple correspondent banks and currencies is performed daily from manually downloaded statements. Break identification and investigation consumes treasury operations time; cross-border reporting to the regulator draws on the same reconciliation output, extending the reporting cycle.
- Solution: The AI agent downloads nostro statements, matches transactions against the Bank's records, classifies breaks by type and age, triages SWIFT exception messages against the open breaks, and prepares the currency-control notification submissions. Treasury operations reviews the break classification and approves notification submissions; unmatched items above a materiality threshold are escalated for manual investigation.
- OKR: Nostro reconciliation, SWIFT exception triage, and currency-control notification preparation are AI-managed, with treasury operations reviewing break dispositions and approving all regulatory notification submissions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent manages the full nostro reconciliation and notification preparation sequence for ≥90% of correspondent bank statements across active currencies within 6 months of go-live. |
| Acceptance | ≥85% of AI-prepared currency-control notification submissions accepted by treasury operations without material revision before approval. |
| Cycle | Daily nostro reconciliation and currency-control notification preparation cycle time reduced by ≥50% compared to the manual baseline within 12 months. |

#### Corporate client FX rate intelligence service

- URN: urn:financial-services:scenario:flow/fx-cross-border/fx-corporate-client-rate-intelligence
- Lens: New opps
- Complexity: M
- Intent: Corporate client FX intelligence service — rate movements against client-specific hedging thresholds, corridor settlement timing intelligence, and early-warning alerts — derived from the Bank's own FX pricing and volume data. Corporate clients with material FX exposures receive systematic market intelligence as part of the banking relationship rather than transacting at market without threshold visibility.
- Problem to solve: Corporate clients with material FX exposures lack a systematic intelligence service on rate movements against their hedging thresholds. The Bank's FX data — pricing history, corridor volumes, settlement timing — is not used to generate client-specific FX intelligence or early-warning alerts.
- Solution: The AI agent tracks each corporate client's stated FX thresholds and monitors intraday rate movements, generating an alert — with the expected settlement timing for the client's corridors — when the rate enters the client's execution range. The relationship manager reviews the alert before client contact; the service is positioned as part of the Bank's corporate FX proposition rather than as a separate advisory product.
- OKR: Corporate clients with material FX exposures receive systematic rate-movement intelligence against their hedging thresholds and settlement timing signals, derived from the Bank's own FX pricing and volume data.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's FX intelligence service covers ≥80% of enrolled corporate clients with material FX thresholds within 9 months of go-live. |
| Acceptance | ≥75% of AI-generated client FX alerts reviewed and forwarded by relationship managers without material amendment. |
| Cycle | Time from intraday rate entry into client execution range to RM-reviewed alert dispatch reduced to ≤15 minutes per event. |

## Cross-cutting flows {#cross-cutting-flows}

### Customer Lifecycle {#customer-lifecycle}

- URN: urn:financial-services:flow:customer-lifecycle
- Summary: End-to-end orchestration of the customer's journey with the Bank — acquisition, onboarding, active service, relationship growth, retention, and exit. The stream turns on per-stage time and friction across the journey.

The Customer Lifecycle spans the customer's full journey with the Bank — from acquisition and onboarding through active service, relationship growth, and retention to eventual exit. Each stage carries its own cycle time and friction profile: onboarding completion rates, time-to-first-transaction, cross-sell conversion windows, and churn lead times are the operational metrics that govern commercial outcome. The GenAI opportunity runs across the entire lifecycle — compressing onboarding friction, surfacing retention signals before the decision window closes, and giving relationship managers and servicing teams a continuous, data-grounded view of where each customer sits in the journey.

| Lens | Problem |
| --- | --- |
| Analyze | Customer journey data spans acquisition systems, KYC platforms, account management systems, and CRM — with no continuous cross-stage view. The Bank reconstructs lifecycle stage transition rates and cycle times manually per quarter; the picture of where customers drop off, churn, or stall is always retrospective. |
| Optimize | Onboarding sequencing, cross-sell contact timing, and retention intervention thresholds are set at the policy level and reviewed infrequently. Segment-specific optimization — which customers to contact, when, and with what — requires multi-week analytical cycles that lag the commercial window. |
| Automate | KYC document chase, onboarding status updates, cross-sell offer follow-up, and exit processing steps each consume frontline or operations capacity on tasks that follow defined rules. The structural similarity across customers at each stage makes these candidates for AI-driven execution with human review. |
| Enrich | Lifetime value intelligence — acquisition cost, product depth, tenure, and risk-adjusted margin by customer — is assembled episodically for portfolio reviews. The Bank does not maintain a continuous, customer-level lifetime value view that could anchor retention prioritization and cross-sell sequencing in real time. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| acquire | Acquire | Customer acquisition and initial engagement | The Bank identifies and engages prospective customers through direct, digital, branch, and intermediary channels. The stage covers lead generation, initial qualification, and the transition of a prospect to an applicant. Acquisition economics — cost per acquired customer by channel and segment — set the commercial baseline for the lifecycle. | Acquisition channel performance is measured at the volume level without attribution to downstream lifecycle quality. High-volume low-cost channels may deliver customers with short tenures; the Bank has no systematic view of acquisition channel quality until churn occurs downstream. |
| onboard | Onboard | Customer onboarding — KYC, account activation, and first use | KYC completion, account activation, initial product setup, and the customer's first meaningful engagement with the Bank. Onboarding quality determines the customer's activation rate and the speed at which the relationship generates revenue. | Onboarding drop-off occurs at document collection and KYC verification steps where customer effort peaks. Drop-off rates vary by segment and channel; the Bank cannot identify at which step most customers abandon without manual case-level review. |
| serve | Serve | Day-to-day servicing and transactional engagement | Ongoing servicing of the customer relationship — transaction processing, inquiry handling, complaint resolution, and account maintenance. The stage where service quality is experienced daily and where operational friction is most visible to the customer. | Servicing contacts arrive without structured context; handlers reconstruct the customer's recent history per interaction. Resolution quality and handling time vary with the complexity of the contact and the experience of the assigned handler. |
| grow | Grow | Relationship deepening and cross-sell | Identification and capture of additional product and service relationships — credit, insurance, investment, and cash management — within the existing customer base. The growth stage determines wallet share and lifetime value expansion beyond the initial product. | Cross-sell conversations are initiated from product campaign calendars rather than from behavioral signals in the customer's transactional data. Relationship managers and frontline staff lack real-time signals identifying which customers have active cross-sell propensity. |
| retain | Retain | Retention and churn prevention | Detection and management of at-risk customer relationships before the customer's decision to exit is made. Retention interventions are most effective when triggered early against behavioral signals; they are least effective when triggered by the customer's exit notification. | Churn signals — declining balance, reduced transaction frequency, competitor inquiry — arrive in multiple systems with no aggregation or scoring. Relationship managers and servicing teams identify at-risk customers reactively, after the churn decision is made. |
| exit | Exit | Customer exit, account closure, and offboarding | Managed closure of the customer relationship — account closure, balance transfer, regulatory reporting, and data retention. The exit stage carries compliance obligations and an opportunity to understand the causes of attrition for future cycle improvement. | Exit reasons are captured informally through exit surveys or handler notes with no structured classification. The institutional learning from exit data — which products, segments, or service failures generate most exits — is not systematically fed back into acquisition or retention strategy. |

#### Customer lifecycle cross-stage journey analytics

- URN: urn:financial-services:scenario:flow/customer-lifecycle/cl-cross-stage-journey-analytics
- Lens: Insights
- Complexity: M
- Intent: Continuous cross-stage view of lifecycle transition rates and cycle times — onboarding completion, time-to-first-transaction, cross-sell conversion windows, and churn lead times — assembled from acquisition, KYC, account management, and CRM systems without quarterly manual reconstruction. The Bank identifies where customers drop off, stall, or churn in close to real time.
- Problem to solve: Customer journey data spans acquisition systems, KYC platforms, account management systems, and CRM with no continuous cross-stage view. The Bank reconstructs lifecycle stage transition rates and cycle times manually per quarter; the picture of where customers drop off, churn, or stall is always retrospective.
- Solution: The AI agent reads across lifecycle systems, tracks each customer's current stage and transition timestamps, and produces a continuous dashboard of completion rates, cycle times, and stage-exit reasons by segment and channel. Marketing and operations use the live view to direct interventions at the highest-friction stages; quarterly reporting is generated from the same data feed.
- OKR: Customer lifecycle transition rates and cycle times across onboarding, activation, cross-sell, and churn stages are continuously visible from aggregated acquisition, KYC, account management, and CRM data, replacing quarterly manual reconstruction.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent maintains the cross-stage lifecycle dashboard with ≥99% data completeness across all defined transition points for ≥9 consecutive months within the first year. |
| Acceptance | ≥80% of AI-produced lifecycle analytics views accepted by marketing and operations as decision-ready without material amendment. |
| Cycle | Time from period close to distribution-ready cross-stage lifecycle analysis reduced from multi-week manual reconstruction to ≤24 hours. |

#### Onboarding and cross-sell sequencing optimization

- URN: urn:financial-services:scenario:flow/customer-lifecycle/cl-onboarding-sequence-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Segment-specific optimization of onboarding step sequencing and cross-sell contact timing based on behavioral signals, reducing drop-off at KYC and document collection steps and improving conversion within the early-tenure cross-sell window. Contact timing is determined by readiness signals rather than fixed post-onboarding calendars.
- Problem to solve: Onboarding sequencing and cross-sell contact timing are set at the policy level and reviewed infrequently. Segment-specific optimization — which customers to contact, when, and with what — requires multi-week analytical cycles that lag the commercial window.
- Solution: The AI agent models completion probability by onboarding step and segment, identifies the sequence that maximizes completion rate, and generates a cross-sell contact signal when the customer's first-use behavior indicates readiness. Marketing and servicing operations review the recommended contact list before outreach; actual outcomes retrain the sequence model weekly.
- OKR: Onboarding step sequencing and cross-sell contact timing are optimized by segment on a weekly model refresh using behavioral completion signals, reducing KYC drop-off and improving conversion within the early-tenure cross-sell window.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's sequence optimization deployed across ≥3 retail segments and ≥1 SME segment within 9 months of go-live; contact signals generated for ≥80% of qualifying early-tenure customers. |
| Acceptance | ≥75% of recommended contact lists accepted by marketing and servicing operations without material reordering before outreach. |
| Cycle | Segment-level retuning of onboarding sequence and contact timing shortened from multi-week analytical cycles to a weekly model refresh; onboarding completion in AI-optimized segments ≥10 percentage points above the pre-optimization baseline within 12 months. |

#### Lifecycle task orchestration automation

- URN: urn:financial-services:scenario:flow/customer-lifecycle/cl-lifecycle-agent-execution
- Lens: Automation
- Complexity: L
- Intent: AI-driven KYC document chase, onboarding status updates, cross-sell follow-up, and exit processing steps across the customer lifecycle, with human review triggered by exception rather than routine task assignment. Frontline and operations capacity is directed toward judgment-intensive interactions rather than structured task sequences.
- Problem to solve: KYC document chase, onboarding status updates, cross-sell offer follow-up, and exit processing steps each consume frontline or operations capacity on tasks that follow defined rules. The structural similarity across customers at each stage makes these candidates for AI-driven execution with human review.
- Solution: The AI agent orchestrates the task sequence for each customer at each lifecycle stage — dispatching requests, tracking responses, escalating non-completions, and updating downstream systems — with operations reviewing exceptions and approving any action that departs from the standard path. Human intervention is triggered by exception signal rather than by routine task queue.
- OKR: KYC document chase, onboarding status updates, cross-sell follow-up, and exit processing steps are orchestrated by the AI agent across the customer lifecycle, with operations reviewing exceptions and approving departures from the standard path.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent executes the task sequence for ≥80% of eligible structured lifecycle tasks across retail and SME segments within 9 months of go-live. |
| Acceptance | ≥85% of AI-completed lifecycle task sequences accepted by operations without escalation to manual intervention. |
| Cycle | KYC document collection and onboarding completion cycle time reduced by ≥35% for AI-managed cases within 12 months of go-live. |

#### Customer churn signal aggregation and scoring

- URN: urn:financial-services:scenario:flow/customer-lifecycle/cl-churn-signal-enrichment
- Lens: Enablement
- Complexity: M
- Intent: Aggregated churn scoring from declining balance, reduced transaction frequency, competitor inquiry signals, and product usage changes across systems, surfaced to relationship managers and servicing teams as a continuous risk feed. Retention interventions are triggered by behavioral signals in the decision window rather than by the customer's exit notification.
- Problem to solve: Churn signals — declining balance, reduced transaction frequency, competitor inquiry — arrive in multiple systems with no aggregation or scoring. Relationship managers and servicing teams identify at-risk customers reactively, after the churn decision is made.
- Solution: The AI agent aggregates churn signals across account, transaction, and CRM systems, scores each customer's at-risk probability weekly, and surfaces a ranked retention contact list to relationship managers and servicing teams. Each at-risk flag includes the primary signal and the recommended retention action; the RM reviews and approves outreach before contact.
- OKR: Churn signals from account, transaction, and CRM systems are aggregated and scored weekly, giving relationship managers a ranked retention contact list with primary signal context in advance of the customer's exit decision.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's churn scoring covers ≥90% of the active retail and SME customer base on a weekly cadence within 6 months of go-live. |
| Acceptance | ≥70% of AI-flagged at-risk customers confirmed as actionable by relationship managers before outreach. |
| Cycle | At-risk customers reach the RM-reviewed retention contact list ≥4 weeks before projected churn, against reactive identification after the exit decision today. |

#### Customer lifetime value intelligence

- URN: urn:financial-services:scenario:flow/customer-lifecycle/cl-lifetime-value-intelligence
- Lens: New opps
- Complexity: M
- Intent: Continuous customer-level lifetime value (CLV) view — acquisition cost, product depth, tenure, and risk-adjusted margin — anchoring retention prioritization and cross-sell sequencing on a monthly refresh. Relationship managers and segment heads direct effort at the customers and cohorts with the highest forward CLV rather than responding to backward-looking portfolio summaries.
- Problem to solve: Lifetime value intelligence — acquisition cost, product depth, tenure, and risk-adjusted margin by customer — is assembled episodically for portfolio reviews. The Bank does not maintain a continuous, customer-level lifetime value view that could anchor retention prioritization and cross-sell sequencing.
- Solution: The AI agent calculates and maintains a current CLV estimate for each customer, updated monthly from product revenue, cost-to-serve, and risk data. Relationship managers access the CLV view through the CRM; segment heads use the cohort-level CLV distribution to set coverage and cross-sell priorities. The model's assumptions are reviewed by Finance and Retail leadership quarterly.
- OKR: A customer-level CLV estimate updated monthly — incorporating acquisition cost, product depth, tenure, and risk-adjusted margin — anchors RM coverage prioritization and cross-sell sequencing on a rolling basis.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's CLV model covers ≥95% of the active customer base with monthly updates for ≥10 consecutive months within the first year. |
| Acceptance | ≥80% of CLV model assumptions validated by Finance and Retail leadership at quarterly review without material methodology revision. |
| Cycle | Interval from data refresh to CLV-updated CRM view available to relationship managers reduced from episodic portfolio-review cycles to ≤5 business days on a monthly cadence. |

### Risk Management Cycle {#risk-management-cycle}

- URN: urn:financial-services:flow:risk-management-cycle
- Summary: Enterprise risk discipline across credit, market, operational, and strategic domains — identification, assessment, mitigation, monitoring, and reporting. The stream turns on the cadence at which emerging risks reach decision-makers.

The Risk Management Cycle is the institution's primary discipline for maintaining risk appetite alignment across credit, market, operational, and strategic risk domains. Each stage — from identification of emerging signals to assessment, mitigation action, ongoing monitoring, and reporting to the board and the regulator — carries its own latency. The reporting cycle is externally timed by supervisory requirements; the internal discipline governs how fast emerging risks travel from detection to decision and action. The GenAI opportunity is to compress the identification-to-decision pathway and to ensure that risk monitoring is continuous rather than batch-driven.

| Lens | Problem |
| --- | --- |
| Analyze | Emerging risks surface across credit, market, operational, and strategic domains in separate monitoring silos. Risk teams produce consolidated views manually for each governance cycle; the interval between the emergence of a risk signal and its appearance in a decision-ready format is measured in days to weeks. |
| Optimize | Risk mitigation action sequencing and control prioritization are set through annual risk appetite reviews and updated in response to material events. Continuous optimization — reranking mitigations based on observed control effectiveness and evolving exposure — is not a routine process. |
| Automate | Risk narrative production for ALCO, board risk committee, and regulatory submissions consumes risk team capacity on tasks that draw on structured data and established methodology. Each reporting cycle repeats the same data-pull, synthesis, and narrative sequence with manual effort. |
| Enrich | Stress-test results and risk assessment outputs are produced for regulatory and governance cycles but are not systematically used to enrich forward-looking business decisions. Credit pricing, product design, and limit-setting rarely draw directly on the most recent stress-test or emerging-risk assessment output. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| identify | Identify | Emerging risk identification from internal and external signals | Detection of emerging risk — credit concentration growth, market volatility signals, operational incident patterns, regulatory developments, and counterparty stress — before the risk crystallizes into a loss or limit breach. The stage determines which risks enter the formal risk management cycle. | Risk identification draws on a mix of system-generated alerts, periodic risk team scans, and management-level ad hoc signals. Emerging risks surfaced through informal channels — internal incident reports, news, industry contacts — do not enter the formal risk register until a human champion escalates them. |
| assess | Assess | Risk quantification and appetite alignment | Quantification of identified risks — probability, severity, time horizon, and correlation with existing positions — and comparison against the Bank's risk appetite statement and limit framework. The stage produces the risk assessment that informs mitigation and monitoring decisions. | Risk assessments are produced by risk teams using models and expert judgment, but the synthesis across risk types is manual. Credit, market, and operational risks are assessed in separate frameworks; a single event that crosses risk types — a counterparty failure that generates both credit and operational exposure — may not be assessed in its aggregate form. |
| mitigate | Mitigate | Mitigation action and control implementation | Design and implementation of mitigation actions — limit reductions, hedging, control enhancements, provisioning, and process changes — aligned to the assessed risk and the board-approved risk appetite. The stage where the risk decision becomes an operational change. | Mitigation actions are assigned to business owners with follow-up tracked through manual status updates in risk management systems. Control effectiveness is assessed retrospectively; actions that have not reduced the risk as expected surface only at the next assessment cycle. |
| monitor | Monitor | Continuous risk monitoring and limit utilization | Ongoing tracking of risk positions, limit utilization, control effectiveness, and key risk indicators (KRIs) against appetite thresholds. The stage produces the continuous signal flow that feeds into formal reporting cycles and triggers ad hoc escalation when thresholds are breached. | KRI dashboards are updated on daily or weekly batch cycles from source systems. The window between a threshold breach and the notification reaching the relevant risk owner depends on the monitoring batch frequency; intraday limit breaches in market risk may not surface until end-of-day reports. |
| report | Report | Risk reporting to senior management, board, and regulators | Production of risk reports for senior management, the board risk committee, and the regulator. The reporting stage translates the monitoring output into structured narratives that support governance decisions and satisfy regulatory disclosure requirements. | Risk reports are assembled from multiple source systems by risk teams, with narrative drafted manually after the data is compiled. Report preparation for ALCO, board risk committee, and regulatory submissions runs in parallel cycles with overlapping data draws; the narrative quality depends on the analyst's access to the relevant history. |

#### Emerging risk signal synthesis

- URN: urn:financial-services:scenario:flow/risk-management-cycle/rmc-emerging-risk-signal-synthesis
- Lens: Insights
- Complexity: M
- Intent: Cross-domain aggregation of credit, market, operational, and strategic risk signals into a continuous identification feed, compressing the interval between signal emergence and decision-ready format from days to hours. The CRO and risk committee receive an emerging-risk brief calibrated to materiality rather than governance-cycle cadence.
- Problem to solve: Emerging risks surface across credit, market, operational, and strategic domains in separate monitoring silos. Risk teams produce consolidated views manually for each governance cycle; the interval between the emergence of a risk signal and its appearance in a decision-ready format is measured in days to weeks.
- Solution: The AI agent monitors risk signals across domain-specific systems and external feeds, classifies each signal by risk type and materiality, and assembles a continuous emerging-risk brief for CRO review. Signals that cross materiality thresholds trigger an immediate alert with a recommended escalation path; the full risk identification view is refreshed daily for governance distribution.
- OKR: Emerging risk signals across credit, market, operational, and strategic domains are aggregated and classified continuously, compressing the interval from signal emergence to decision-ready governance brief from days to hours.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent maintains the continuous emerging-risk brief with daily updates across all four domain-specific monitoring feeds for ≥350 days within the first year. |
| Acceptance | ≥80% of AI-produced emerging-risk briefs accepted by the CRO as governance-ready without material revision at each distribution cycle. |
| Cycle | Interval from risk signal emergence to CRO-reviewed decision-ready format reduced from the manual governance-cycle lag (days to weeks) to ≤24 hours for signals crossing materiality thresholds. |

#### Risk control effectiveness and mitigation prioritization

- URN: urn:financial-services:scenario:flow/risk-management-cycle/rmc-control-effectiveness-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Continuous reranking of mitigation actions and control priorities based on observed control effectiveness and evolving risk exposure, supplementing the annual risk appetite review as the driver of mitigation sequencing. The risk function directs remediation effort at the controls with the highest current marginal impact.
- Problem to solve: Risk mitigation action sequencing and control prioritization are set through annual risk appetite reviews and updated in response to material events. Continuous optimization — reranking mitigations based on observed control effectiveness and evolving exposure — is not a routine process.
- Solution: The AI agent tracks the effectiveness of each active mitigation action against the risk it was designed to address, identifies controls that have not reduced the measured risk as expected, and generates a reranked mitigation priority list for CRO review. The reranking is presented at each risk committee cycle as an input to the committee's agenda.
- OKR: Mitigation action sequencing and control prioritization are reranked on a continuous basis against observed control effectiveness and evolving exposure, with the CRO reviewing the updated priority list at each risk committee cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's reranked mitigation priority list presented at ≥90% of risk committee cycles for ≥4 consecutive quarters within the first year. |
| Acceptance | ≥75% of AI-identified underperforming controls confirmed by the CRO as meriting remediation reprioritization at risk committee review. |
| Cycle | Interval from control effectiveness signal emergence to CRO-reviewed reprioritization recommendation reduced from the annual risk appetite review cycle to ≤1 risk committee cycle. |

#### Risk narrative and regulatory reporting automation

- URN: urn:financial-services:scenario:flow/risk-management-cycle/rmc-risk-narrative-automation
- Lens: Automation
- Complexity: M
- Intent: AI-assembled risk narratives for ALCO, board risk committee, and regulatory submissions — pulling from structured risk data and established methodology with risk team review before governance distribution. Risk team capacity is directed toward substantive risk analysis rather than report production.
- Problem to solve: Risk narrative production for ALCO, board risk committee, and regulatory submissions consumes risk team capacity on tasks that draw on structured data and established methodology. Each reporting cycle repeats the same data-pull, synthesis, and narrative sequence with manual effort.
- Solution: The AI agent pulls risk metric data from domain systems, synthesizes it using the Bank's established reporting framework, and drafts the narrative sections for each governance report. The CRO and senior risk team members review and edit the draft before distribution; the AI agent maintains version history for regulatory traceability.
- OKR: Risk narratives for ALCO, board risk committee, and regulatory submissions are assembled by the AI agent from structured risk data using the Bank's established reporting framework, with the CRO and senior risk team reviewing and editing before governance distribution.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the full risk narrative draft for ≥90% of scheduled ALCO, board risk committee, and regulatory reporting cycles within 12 months of go-live. |
| Acceptance | ≥80% of AI-drafted risk narratives accepted by the CRO and senior risk team as requiring editing rather than full redraft before governance distribution. |
| Cycle | Risk narrative production cycle from data pull to draft-ready-for-CRO-review reduced by ≥3 business days compared to the fully manual production baseline. |

#### Stress test and risk assessment decision enrichment

- URN: urn:financial-services:scenario:flow/risk-management-cycle/rmc-stress-test-enrichment-copilot
- Lens: Enablement
- Complexity: M
- Intent: Structured presentation of stress-test results and emerging risk assessments to credit pricing, product design, and limit-setting teams at the point of decision, ensuring forward-looking risk intelligence is systematically embedded in business choices rather than held within the risk function.
- Problem to solve: Stress-test results and risk assessment outputs are produced for regulatory and governance cycles but are not systematically used to enrich forward-looking business decisions. Credit pricing, product design, and limit-setting rarely draw directly on the most recent stress-test or emerging-risk assessment output.
- Solution: The AI agent identifies business decisions currently in process — credit limit reviews, new product approvals, pricing changes — and surfaces the most relevant stress-test or risk assessment output with a structured impact narrative. Business unit leads review the risk enrichment as part of the decision dossier; the risk function is notified when enrichment is reviewed but not acted upon.
- OKR: Stress-test results and emerging risk assessments are systematically surfaced to credit pricing, product design, and limit-setting teams at the point of decision, embedding forward-looking risk intelligence in business choices.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent identifies and enriches ≥80% of qualifying business decisions in process — credit limit reviews, new product approvals, pricing changes — with the most relevant stress-test or risk assessment output within 6 months of go-live. |
| Acceptance | ≥75% of AI-produced risk enrichment dossiers rated by business unit leads as decision-informing without material supplementation. |
| Cycle | Time from business decision trigger to enrichment narrative available to decision-makers reduced to ≤24 hours per qualifying event. |

#### Cross-domain aggregate risk event view

- URN: urn:financial-services:scenario:flow/risk-management-cycle/rmc-aggregate-risk-view
- Lens: New opps
- Complexity: L
- Intent: Integrated cross-risk-type assessment for events that span credit, market, and operational boundaries — a single aggregate view of a counterparty failure, macro shock, or geopolitical event that the current siloed risk framework cannot produce. The CRO and board risk committee receive a complete exposure picture rather than three sequential sub-domain analyses.
- Problem to solve: Credit, market, and operational risks are assessed in separate frameworks. A single event that crosses risk types — a counterparty failure that generates both credit and operational exposure — may not be assessed in its aggregate form within the governance cycle.
- Solution: The AI agent maintains a cross-domain event registry and, when a qualifying event is identified, assembles an aggregate exposure assessment across credit, market, and operational risk dimensions simultaneously. The CRO reviews the aggregate assessment within 24 hours of event identification; the board risk committee receives it at the next governance cycle or sooner if the exposure exceeds appetite thresholds.
- OKR: Cross-domain aggregate exposure assessments spanning credit, market, and operational risk are assembled simultaneously for qualifying events, giving the CRO and board risk committee a complete exposure picture within the governance cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent assembles a cross-domain aggregate assessment for ≥90% of qualifying events meeting defined threshold criteria within 24 hours of event identification. |
| Acceptance | ≥80% of the AI agent's aggregate exposure assessments accepted by the CRO as analytically complete without material supplementation before board risk committee distribution. |
| Cycle | Time from qualifying cross-domain event identification to CRO-reviewed aggregate exposure assessment reduced to ≤24 hours. |

### Compliance & Financial Crime Cycle {#compliance-financial-crime-cycle}

- URN: urn:financial-services:flow:compliance-financial-crime-cycle
- Summary: AML, sanctions, counter-terrorism financing, and conduct obligations across the institution — alert detection, investigation, action, and regulatory reporting. The stream turns on the speed and accuracy of moving from alert to disposition.

The Compliance & Financial Crime Cycle governs the Bank's obligations under AML, sanctions, counter-terrorism financing, and conduct frameworks — detecting suspicious activity, investigating to a disposition, actioning through blocking or reporting, and submitting regulatory filings. National frameworks aligned with the FATF Recommendations set suspicious transaction report (STR) submission windows, correspondent banking KYC obligations, and PEP and sanctions screening standards. The cycle's primary constraint is alert throughput — the ratio of alerts generated by transaction monitoring to investigators available to reach a disposition — and its primary quality measure is accuracy: false positives waste capacity; false negatives create regulatory and reputational exposure.

| Lens | Problem |
| --- | --- |
| Analyze | Alert volumes, false-positive rates, and investigation throughput are tracked at the system level in reports produced for each governance cycle. The financial crime operations team has no continuous view of which transaction monitoring rules generate the highest false-positive burden, which customer segments produce the most actionable alerts, or where investigation time is concentrated. |
| Optimize | Alert triage sequencing and investigator case assignment are driven by queue order rather than case complexity or filing probability. High-probability cases that warrant faster investigation are not differentiated from low-probability alerts at the point of assignment; investigator capacity is not matched to case complexity. |
| Automate | Case dossier assembly, adverse media search, STR narrative drafting, and STR submission formatting each consume investigator capacity on tasks with defined structure and clear inputs. These tasks are strong candidates for execution by an AI agent, with investigator review and approval before any regulatory action. |
| Enrich | Typology intelligence — the patterns of suspicious activity that financial intelligence units and FATF have identified as indicative of ML/TF — is available in public guidance but is not systematically applied to tune transaction monitoring rules or to enrich investigator decision-making at the case level. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| detect | Detect | Transaction monitoring, screening, and alert generation | Automated detection of potentially suspicious activity through transaction monitoring rules, sanctions screening, PEP checks, and behavioral analytics. The stage generates the alert queue that investigators must process to a disposition within regulatory timeframes. | Transaction monitoring systems generate alert volumes dominated by false positives — rule-based triggers that fire on benign activity patterns. High false-positive rates consume investigator capacity on cases that will not produce filings, while the overall alert queue continues to grow with each new monitoring rule added. |
| investigate | Investigate | Alert triage, case investigation, and evidence assembly | Alert triage and case investigation — reviewing the transaction and customer context, assembling the evidence set, and reaching a disposition (dismiss, escalate, file). The quality and speed of investigation determine the Bank's STR filing accuracy and its regulatory compliance posture. | Investigators reconstruct customer and transaction context from multiple systems for each alert. Case dossier assembly — pulling transaction history, KYC documents, beneficial ownership records, and adverse media — is manual and time-consuming; investigators spend more time on evidence gathering than on substantive analysis. |
| action | Act | Disposition — blocking, filing, and enhanced monitoring | Execution of the investigation's disposition — account restriction, transaction blocking, placement on enhanced monitoring, or drafting and approval of the STR for filing. The stage turns the investigation's conclusion into a regulatory-quality output. | STR drafting following an investigation is a manual authoring task dependent on investigator skill and template discipline. Draft quality varies across investigators; STR narratives on similar fact patterns can differ materially in completeness and regulatory-disclosure precision. |
| report | Report | Regulatory filing, management reporting, and governance | STR submission to the financial intelligence unit, management reporting on AML program health, and board-level governance reporting. The stage closes the operational cycle and feeds into the Bank's regulatory relationship. | Management and board reporting on AML program health — alert volumes, investigation rates, STR filing trends, and false-positive rates — is compiled manually from case management system extracts each reporting cycle. The picture of AML program effectiveness is always retrospective and produced at the cadence of the reporting cycle rather than continuously. |

#### Financial crime typology enrichment copilot

- URN: urn:financial-services:scenario:flow/compliance-financial-crime-cycle/cfc-typology-enrichment-copilot
- Lens: Enablement
- Complexity: S
- Intent: Investigator-facing typology intelligence drawn from FATF guidance, financial intelligence unit (FIU) publications, and internal case history, surfaced at the case level when the alert pattern matches a known ML/TF typology. Investigator decision quality improves at the disposition stage, particularly for complex or novel case types.
- Problem to solve: Typology intelligence — the patterns of suspicious activity identified by financial intelligence units and FATF as indicative of ML/TF — is available in public guidance but is not systematically applied to tune transaction monitoring rules or to enrich investigator decision-making at the case level.
- Solution: The AI agent classifies each incoming alert against a structured typology library drawn from FATF mutual evaluation findings, FIU red-flag indicators, and internal STR history, and surfaces the most relevant typology match alongside the case dossier. The investigator reviews the typology context as part of the disposition decision; the typology library is updated quarterly by the financial crime intelligence function.
- OKR: Investigator decision quality at alert disposition is systematically supported by FATF-aligned typology intelligence matched to each case's alert pattern, drawn from a maintained typology library.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's typology classification applied to ≥90% of incoming alerts for ≥6 months within the first year of go-live. |
| Acceptance | ≥75% of typology match suggestions rated by investigators as relevant to their disposition decision in quarterly quality reviews. |
| Cycle | Average investigator time at the disposition stage for complex or novel case types reduced by ≥25% compared to pre-typology-enrichment baseline within 12 months. |

#### AML alert throughput and false-positive analytics

- URN: urn:financial-services:scenario:flow/compliance-financial-crime-cycle/cfc-alert-throughput-analytics
- Lens: Insights
- Complexity: M
- Intent: Continuous decomposition of alert volumes, false-positive rates by transaction monitoring rule, and investigation throughput by customer segment — giving financial crime operations a daily view of where investigator capacity is concentrated and where rule tuning will have the highest return. AML program efficiency and regulatory defensibility improve together.
- Problem to solve: Alert volumes, false-positive rates, and investigation throughput are tracked at the system level in reports produced for each governance cycle. The financial crime operations team has no continuous view of which transaction monitoring rules generate the highest false-positive burden or where investigation time is concentrated.
- Solution: The AI agent monitors the case management system continuously, classifies each alert disposition against its generating rule, and assembles a rule-level false-positive and throughput dashboard updated daily. Financial crime operations and the AML model governance team use the view to prioritize rule tuning; changes to transaction monitoring rule parameters are reviewed by the AML compliance officer before implementation.
- OKR: AML alert volumes, false-positive rates, and investigation throughput are visible at the transaction monitoring rule level on a continuous basis, enabling targeted rule tuning and defensible AML program governance.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's rule-level false-positive and throughput dashboard in active use by financial crime operations and the AML model governance team for ≥95% of governance cycles within 6 months. |
| Acceptance | ≥80% of rule-tuning priorities drawn from the AI agent's rule-level view accepted by the AML compliance officer as analytically sound prior to parameter change review. |
| Cycle | Interval from rule-level alert pattern emergence to a governance briefing reviewed by the AML compliance officer reduced from the quarterly report cycle to ≤5 business days. |

#### Financial crime case triage and assignment optimization

- URN: urn:financial-services:scenario:flow/compliance-financial-crime-cycle/cfc-case-complexity-triage-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Alert triage sequencing that differentiates cases by STR-filing probability and investigation complexity at the point of assignment, matching investigator experience to case complexity rather than processing alerts by queue order. High-probability cases reach experienced investigators faster; investigator capacity is not diluted across low-probability alerts.
- Problem to solve: Alert triage sequencing and investigator case assignment are driven by queue order rather than case complexity or STR-filing probability. High-probability cases are not differentiated from low-probability alerts at assignment; investigator capacity is not matched to case complexity.
- Solution: The AI agent scores each alert at triage for estimated STR-filing probability and case complexity, assigns cases to investigator tiers accordingly, and surfaces the complexity rationale alongside the case dossier. The financial crime operations manager reviews the triage logic weekly; scoring model performance is validated against actual STR-filing outcomes on a quarterly basis.
- OKR: Alert triage sequences cases by STR-filing probability and investigation complexity, ensuring experienced investigators are assigned high-probability cases rather than processing alerts by queue order.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's complexity scoring and tiered assignment applied to ≥90% of incoming alerts within 6 months of go-live. |
| Acceptance | ≥80% of the AI agent's triage assignments validated as appropriately matched to investigator tier upon quarterly scoring model review. |
| Cycle | Average time from alert generation to experienced-investigator assignment for high-STR-probability cases reduced by ≥30% within 12 months. |

#### Financial crime investigation pack and STR draft automation

- URN: urn:financial-services:scenario:flow/compliance-financial-crime-cycle/cfc-investigation-pack-automation
- Lens: Automation
- Complexity: M
- Intent: Assembly of case dossiers by the AI agent — transaction history, KYC documents, beneficial ownership records, adverse media search, and STR narrative draft — with investigator review and approval before any regulatory filing or account action. Investigator time is directed toward substantive analysis and disposition judgment rather than evidence gathering.
- Problem to solve: Case dossier assembly, adverse media search, STR narrative drafting, and STR submission formatting each consume investigator capacity on tasks with defined structure and clear inputs. Investigators spend more time on evidence gathering than on substantive analysis.
- Solution: The AI agent assembles the case dossier from case management, KYC, and transaction systems, conducts structured adverse media and sanctions screening, and drafts the STR narrative. The investigator reviews the full dossier, edits the STR narrative, and approves the submission; the AI agent tracks STR submission windows against the statutory filing deadlines.
- OKR: Case dossier assembly, adverse media search, and STR narrative drafting are AI-managed, with investigator capacity directed toward substantive disposition analysis and approval of all regulatory filings.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent assembles the full case dossier and STR narrative draft for ≥85% of assigned investigations within 6 months of go-live. |
| Acceptance | ≥80% of AI-drafted STR narratives accepted by investigators as substantively complete, requiring editing rather than full redraft before approval. |
| Cycle | Time from alert assignment to investigation-pack-ready status reduced from 2–4 hours of manual assembly to ≤30 minutes per case. |

#### Continuous AML program health monitoring

- URN: urn:financial-services:scenario:flow/compliance-financial-crime-cycle/cfc-aml-program-health-continuous
- Lens: New opps
- Complexity: M
- Intent: Continuous AML program health view — alert volumes, false-positive rates, investigation throughput, STR filing trends, and time-to-disposition by segment — updated daily from case management data and surfaced to the AML compliance officer and senior management without waiting for the periodic report cycle. Regulatory examinations are met with a current-state view, not a retrospective reconstruction.
- Problem to solve: Management and board reporting on AML program health is compiled manually from case management system extracts each reporting cycle. The picture of AML program effectiveness is always retrospective and produced at the cadence of the reporting cycle rather than continuously.
- Solution: The AI agent reads from the case management system continuously, maintains a structured AML program health view across the five key program metrics, and produces the management and board report from the same data on demand. The AML compliance officer reviews the report before board distribution; the dashboard is accessible to financial crime operations leadership at all times.
- OKR: AML program health across alert volumes, false-positive rates, investigation throughput, STR filing trends, and time-to-disposition is continuously available to the AML compliance officer and senior management, independent of the periodic report cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent maintains the AML program health view with daily updates across all five key program metrics for ≥52 consecutive weeks within 12 months of go-live. |
| Acceptance | ≥85% of on-demand management and board reports generated from the dashboard accepted by the AML compliance officer without material amendment. |
| Cycle | AML program health reporting cycle compressed from multi-day manual extraction and compilation to board-ready output available within 2 hours of request. |

### Internal Audit Cycle {#internal-audit-cycle}

- URN: urn:financial-services:flow:internal-audit-cycle
- Summary: Independent assurance over the Bank's controls, risk management, and governance frameworks — risk-based audit planning, execution, reporting, and remediation tracking. The stream turns on audit coverage rate against the institutional risk surface.

The Internal Audit Cycle provides the board and senior management with independent assurance on the effectiveness of the Bank's controls, risk management, and governance. The IIA standards and supervisory expectations define the audit universe, planning methodology, and reporting obligations. The cycle's primary constraint is audit coverage — the ability to maintain adequate assurance across an expanding risk surface with a fixed audit team. Each stage from plan to remediation verification carries its own lead time; findings that are identified but not remediated within the agreed timeline accumulate as open items and attract regulatory scrutiny.

| Lens | Problem |
| --- | --- |
| Analyze | Audit finding data — by business unit, control type, root-cause category, and recurrence rate — is held in the audit management system but not routinely analyzed for systematic patterns. The audit committee and senior management receive finding summaries per report cycle but not a continuous view of which control domains are generating recurring issues. |
| Optimize | Audit planning allocates team capacity annually against a static risk ranking. High-risk business units that generate frequent repeat findings — indicating control environments that have not sustainably improved — do not automatically attract higher audit frequency in the planning cycle; replanning requires a manual review of the prior period's finding data. |
| Automate | Working paper documentation, evidence indexing, finding draft preparation, and remediation status update chasing consume audit team time on structured tasks with well-defined inputs. These tasks compete with the judgment-intensive analytical work that generates the assurance value; shifting them to an AI agent preserves auditor capacity for substantive testing. |
| Enrich | The audit function's intelligence on control weaknesses, root-cause patterns, and remediation effectiveness is not systematically shared across business lines. A control weakness identified in retail banking may have a structural equivalent in SME or corporate banking; the institutional learning from audit findings rarely propagates to business units that have not yet been audited on the same control domain. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| plan | Plan | Audit planning — universe definition, risk ranking, and schedule | Annual and rolling audit planning — defining the audit universe, ranking business units and processes by risk, and constructing the audit schedule. The planning stage allocates the audit team's capacity against the institutional risk surface and sets the coverage commitments that the board audit committee approves. | Audit universe risk rankings are updated annually using a structured risk-rating methodology applied to the prior year's data. The ranking reflects the risk profile at the point of the assessment; business units that grow in risk between annual reviews may carry an outdated risk rating when the next audit is scheduled. |
| execute | Execute | Audit execution — fieldwork, testing, and finding identification | Fieldwork — control testing, transaction sampling, interview, and document review — producing the set of findings and observations that the audit report will communicate. The execution stage is where the auditor's professional judgment is most intensively applied. | Fieldwork documentation and evidence organization are manual tasks consuming audit team time alongside substantive testing. Working paper preparation, evidence indexing, and finding drafting each draw on senior auditor time that could be directed at the analytical and judgment-intensive elements of the engagement. |
| report | Report | Audit report production, rating, and management response | Production of the formal audit report — findings, root-cause analysis, risk ratings, and recommendations — followed by management response and agreement on remediation commitments. The report is the governance artifact that the board audit committee reviews and on which regulatory supervisors assess the audit function's effectiveness. | Audit report drafting is a sequential process: findings drafted by fieldwork auditors, reviewed by the audit manager, revised in response to management challenges, and finalized by the Chief Audit Executive. Each revision cycle adds days to the report production timeline; the quality of root-cause analysis in the report reflects the depth of the initial finding draft. |
| remediate | Remediate | Findings remediation, verification, and closure | Tracking and verification of management's remediation actions against agreed finding commitments. The stage closes the audit cycle by confirming that control weaknesses identified in the report have been addressed to the auditor's satisfaction and within the agreed timeline. | Remediation tracking depends on management's voluntary status updates in the audit issue tracking system, supplemented by periodic auditor follow-up. Overdue actions and partial remediations are identified at the next status review date rather than on a continuous basis; open findings accumulate without a continuous visibility mechanism. |

#### Audit fieldwork documentation and evidence automation

- URN: urn:financial-services:scenario:flow/internal-audit-cycle/iac-fieldwork-documentation-automation
- Lens: Automation
- Complexity: S
- Intent: AI-managed working paper documentation, evidence indexing, and finding draft preparation — preserving auditor capacity for substantive testing and judgment-intensive control analysis. The time saved on documentation tasks translates directly into broader audit coverage within the approved budget.
- Problem to solve: Working paper documentation, evidence indexing, and finding draft preparation consume audit team time alongside substantive testing. These structured tasks compete with the judgment-intensive analytical work that generates assurance value.
- Solution: The AI agent manages the documentation workflow throughout fieldwork — indexing evidence to control objectives and drafting initial findings from test results. Audit staff review and approve each finding draft before it advances; the AI agent maintains a complete audit trail for regulatory review.
- OKR: Working paper documentation, evidence indexing, and finding draft preparation are AI-managed throughout fieldwork, preserving auditor capacity for substantive testing and control analysis.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent manages the documentation workflow for ≥85% of audit fieldwork assignments within 9 months of go-live. |
| Acceptance | ≥80% of AI-drafted initial findings accepted by audit staff as substantively complete, requiring editing rather than full redraft before advancement. |
| Cycle | Proportion of audit team time spent on documentation tasks reduced by ≥30% per engagement within 12 months of go-live, measured against pre-implementation time-recording data. |

#### Audit finding remediation tracking enablement

- URN: urn:financial-services:scenario:flow/internal-audit-cycle/iac-remediation-tracking-enablement
- Lens: Enablement
- Complexity: S
- Intent: Continuous remediation status tracking with automated follow-up prompts and overdue-action escalation, replacing periodic manual status reviews with a live open-finding visibility mechanism. Regulators reviewing open-item aging receive a current-state view rather than a point-in-time extract produced at the previous governance cycle.
- Problem to solve: Remediation tracking depends on management's voluntary status updates in the audit issue tracking system, supplemented by periodic auditor follow-up. Overdue actions and partial remediations are identified at the next status review date rather than on a continuous basis; open findings accumulate without a continuous visibility mechanism.
- Solution: The AI agent monitors remediation commitments against agreed due dates, sends structured follow-up prompts to action owners at defined intervals before expiry, and escalates overdue actions to senior management and the Chief Audit Executive. The audit committee receives a continuous open-item dashboard; the AI agent generates the remediation status section of each board report from the live tracking data.
- OKR: Remediation commitment status is tracked continuously with automated follow-up prompts and overdue-action escalation to senior management and the Chief Audit Executive, replacing periodic manual status reviews with a live open-finding visibility mechanism.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's remediation tracking covers ≥95% of open audit findings with due dates across all business units within 6 months of go-live. |
| Acceptance | ≥75% of AI-generated remediation status sections in board reports accepted by the Chief Audit Executive without material amendment before audit committee distribution. |
| Cycle | Average overdue-action identification lag reduced from next periodic status review (typically 30–60 days) to ≤24 hours of due-date expiry. |

#### Audit finding pattern intelligence

- URN: urn:financial-services:scenario:flow/internal-audit-cycle/iac-finding-pattern-intelligence
- Lens: Insights
- Complexity: M
- Intent: Continuous analysis of audit finding data by business unit, control type, root-cause category, and recurrence rate, giving the audit committee a live view of which control domains generate repeat issues rather than a per-cycle finding summary. Control environment trends are visible between governance cycles, not only at them.
- Problem to solve: Audit finding data is held in the audit management system but not routinely analyzed for systematic patterns. The audit committee and senior management receive finding summaries per report cycle but not a continuous view of which control domains are generating recurring issues.
- Solution: The AI agent analyzes the audit management system's finding records continuously, classifies each finding by control domain, root-cause category, and recurrence status, and produces a trend view updated after each audit report is finalized. The Chief Audit Executive reviews the pattern view before the audit committee chair receives it at each meeting alongside the cycle's individual audit reports, and uses the trend analysis in annual planning.
- OKR: Audit finding data is analyzed continuously by control domain, root-cause category, and recurrence rate, giving the audit committee a live trend view of control environment health between governance cycles.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent maintains the finding pattern trend view with updates after each finalized audit report for 100% of reports issued within the year. |
| Acceptance | ≥80% of AI-produced audit committee trend analyses accepted by the Chief Audit Executive without material revision before committee distribution. |
| Cycle | Interval from finding finalization to a Chief Audit Executive-reviewed pattern view reduced from the next per-cycle summary report to ≤5 business days. |

#### Risk-ranked dynamic audit planning

- URN: urn:financial-services:scenario:flow/internal-audit-cycle/iac-risk-ranked-audit-planning
- Lens: Optimize
- Complexity: M
- Intent: Dynamic audit schedule reallocation that increases coverage frequency for business units with high repeat-finding rates and incorporates mid-year risk changes into the coverage plan without waiting for the annual review. Audit team capacity is directed at the highest-risk parts of the institution on a rolling basis rather than a fixed annual allocation.
- Problem to solve: Audit planning allocates team capacity annually against a static risk ranking. Business units that grow in risk between annual reviews may carry an outdated risk rating when the next audit is scheduled; high repeat-finding rates do not automatically increase audit frequency in the current planning cycle.
- Solution: The AI agent recalculates the audit universe risk ranking quarterly using the most recent finding data, regulatory feedback, and business unit risk profile changes, and generates a schedule adjustment recommendation for the Chief Audit Executive. The audit committee approves material schedule changes; minor resequencing within the approved coverage commitments is managed by the Chief Audit Executive.
- OKR: Audit coverage frequency and schedule allocation are dynamically adjusted on a quarterly basis using current finding data, regulatory feedback, and business unit risk profile changes, rather than being fixed at annual planning.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent generates quarterly audit universe risk reranking and schedule adjustment recommendations for ≥4 consecutive quarters within the first 12 months. |
| Acceptance | ≥75% of the AI agent's schedule adjustment recommendations accepted by the Chief Audit Executive for implementation without material revision. |
| Cycle | Lag between material business unit risk profile change and reflected adjustment in the approved audit coverage schedule reduced from the next annual planning cycle to ≤1 quarter. |

#### Cross-business-line audit control learning propagation

- URN: urn:financial-services:scenario:flow/internal-audit-cycle/iac-cross-entity-control-learning
- Lens: New opps
- Complexity: M
- Intent: Systematic propagation of audit finding intelligence across business lines — a control weakness identified in retail banking flagged to SME and corporate banking teams before their next audit cycle — reducing the institutional lag between a finding's identification in one business line and its preventive application in others.
- Problem to solve: The audit function's intelligence on control weaknesses, root-cause patterns, and remediation effectiveness is not systematically shared across business lines. A control weakness identified in retail banking may have a structural equivalent in SME or corporate banking; the institutional learning rarely propagates to business units that have not yet been audited on the same control domain.
- Solution: The AI agent classifies each finalized audit finding by control domain and structural applicability, identifies business units with similar control profiles that have not yet been audited on the relevant domain, and distributes a structured control learning note. Business unit control owners review the note and confirm whether the weakness applies; the Chief Audit Executive uses confirmed applicabilities to inform the next planning cycle.
- OKR: Audit finding intelligence is systematically propagated across business lines by control domain, ensuring that a weakness identified in one business line informs preventive review in structurally similar business units before their next audit cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent distributes structured control learning notes for ≥80% of finalized audit findings with identified cross-business-line applicability within 3 months of finding finalization. |
| Acceptance | ≥70% of AI-distributed control learning notes confirmed as relevant by the receiving business unit control owners. |
| Cycle | Propagation lag from finding finalization in one business unit to reviewed control learning note in applicable peer business units reduced from the next annual planning cycle to ≤30 days. |

### Financial Control & Performance Cycle {#financial-control-cycle}

- URN: urn:financial-services:flow:financial-control-cycle
- Summary: Bank-wide planning, close, and performance discipline — budget and rolling-forecast setting, financial close, management and regulatory reporting, and forward-looking adjustment. The stream turns on the financial-close cadence and the speed of forward-looking adjustment.

The Financial Control & Performance Cycle spans the Bank's planning, close, and reporting disciplines — from annual and rolling budget setting through P&L execution, financial close, management and regulatory reporting, and the adjustment cycle that keeps the forward view current. Periodic reporting to the regulator carries prescribed formats and submission windows; internally, the board and ALCO require a narrative view of performance against plan that the CFO function must produce each period. The cycle's primary constraint is the financial-close timeline — the elapsed time from period end to a reliable, decision-quality P&L — and the secondary constraint is the speed at which the forward view (reforecast) is updated when actuals deviate from plan.

| Lens | Problem |
| --- | --- |
| Analyze | Variance between actual and budgeted performance is analyzed manually by finance teams after close, with each sub-team covering its own P&L line. The CFO and business unit CFOs receive the variance narrative at the point of the management pack distribution; the cycle time between actuals and decision-ready variance analysis is measured in days. |
| Optimize | Budget submission and reforecast sequencing across business units is driven by the finance calendar and managed through email and spreadsheet tracking. Assumptions that are challenged or revised late in the consolidation cycle extend the overall timeline without a clear view of which submission is the constraint. |
| Automate | Monthly close narrative, management pack production, regulatory return formatting, and MD&A drafting are manual tasks that consume senior finance capacity on well-structured synthesis work. The structure of these tasks — pulling from known data sources, applying standard methodology, narrating variance — makes them strong candidates for AI-assisted production. |
| Enrich | Reforecast assumptions are updated by business units based on their own forward visibility. Cross-unit signals — a credit portfolio trend that implies a revenue headwind, an operational cost trajectory that will require provision adjustment — are not systematically surfaced to the reforecast process before they appear in the actuals. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| plan | Plan | Annual budget and rolling forecast | Annual budget setting and rolling forecast production — covering revenue, cost, credit loss, and capital. The planning stage produces the financial targets and assumptions against which in-period performance is measured and the forward view is continuously calibrated. | Budget consolidation across business units is a sequential manual process — each unit submits, finance consolidates, iterates with units on challenged assumptions, and finalizes. The process takes weeks; late submissions and assumption challenges extend the cycle and compress the time available for strategic-level review of the consolidated plan. |
| execute | Execute | In-period financial execution and ledger management | In-period execution — revenue recognition, cost allocation, provision booking, and intercompany elimination. The execution stage maintains the accuracy of the general ledger through the period and produces the data that the financial close will formalize. | Manual journal entries, intercompany reconciliation, and cost allocation calculations are the primary sources of close-period error. Entries posted outside the normal workflow — adjustments, corrections, and late accruals — introduce variance that is identified during close review rather than at the point of posting. |
| measure | Close | Financial close and period-end measurement | Period-end close — reconciliation, provision finalization, ledger sign-off, and production of the trial balance. The close stage is the control gate where the period's financial data is validated and signed off before it enters reporting and regulatory submission. | Financial close is the most time-pressured phase of the cycle, with multiple reconciliations, provision reviews, and sign-off sequences running in parallel. Bottlenecks in one work stream — intercompany reconciliation, credit-loss provision finalization — cascade into the overall close timeline and delay the reporting stage. |
| report | Report | Management reporting, regulatory submission, and investor disclosure | Production of the management accounts, board and ALCO packs, regulatory financial returns (prudential reporting), and investor disclosures. The reporting stage translates the closed ledger into decision-ready narratives for internal governance and external regulatory audiences. | Management account packs are produced by finance teams from the closed ledger, with narrative variance analysis drafted manually after the data tables are finalized. Variance narratives for revenue, cost, and credit loss lines are drafted in parallel by different sub-teams; the CFO's consolidated view is assembled sequentially, compressing the time available for review before board or ALCO distribution. |
| adjust | Adjust | Reforecast, corrective action, and forward-view update | Reforecast and corrective action following the period's performance review — updating the forward view of revenue, cost, and capital, and adjusting business unit targets and resource allocation where actuals have diverged materially from plan. The adjustment stage closes the planning-to-performance feedback loop. | Reforecast cycles require business units to resubmit assumptions and finance to re-consolidate, following the same sequencing as the original budget process. The reforecast cycle takes weeks; by the time the updated forward view is finalized, the next period's actuals are already being recorded and may have moved further from the revised forecast. |

#### Financial variance attribution analytics

- URN: urn:financial-services:scenario:flow/financial-control-cycle/fcc-variance-attribution-analytics
- Lens: Insights
- Complexity: M
- Intent: Automated variance attribution between actual and budgeted P&L by revenue, cost, and credit-loss line across business units, reducing the interval from period close to decision-ready variance analysis from days to hours. The CFO and business unit CFOs review the attributed view rather than directing finance teams to reconstruct it.
- Problem to solve: Variance between actual and budgeted performance is analyzed manually by finance teams after close, with each sub-team covering its own P&L line. The CFO and business unit CFOs receive the variance narrative at the point of management pack distribution; the cycle time between actuals and decision-ready variance analysis is measured in days.
- Solution: The AI agent pulls actual and budget data from the closed ledger, attributes variances to price, volume, mix, and one-off effects for each P&L line, and presents the attribution to the CFO team for review. The CFO and business unit CFOs review and edit the attribution narrative before management pack distribution; the attribution methodology is maintained and version-controlled by the financial control team.
- OKR: Variance between actual and budgeted P&L is attributed automatically by revenue, cost, and credit-loss line across business units, reducing the interval from period close to decision-ready variance analysis from days to hours.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's variance attribution covers ≥95% of P&L lines and all business units for ≥11 of 12 monthly close cycles in the first year. |
| Acceptance | ≥80% of AI-produced variance attribution narratives accepted by the CFO and business unit CFOs without material reattribution before management pack distribution. |
| Cycle | Close-to-decision-ready variance analysis interval reduced from the multi-day manual cycle to ≤4 hours from ledger sign-off. |

#### Budget and reforecast consolidation optimization

- URN: urn:financial-services:scenario:flow/financial-control-cycle/fcc-budget-consolidation-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Constraint-path identification in the budget submission and reforecast consolidation sequence — flagging which business unit submissions are holding the cycle — reducing the multi-week assumption-revision loop that extends the planning timeline without improving plan quality. The CFO team acts on the constraint view to unblock the consolidation.
- Problem to solve: Budget submission and reforecast sequencing across business units is driven by the finance calendar and managed through email and spreadsheet tracking. Assumptions that are challenged or revised late in the consolidation cycle extend the overall timeline without a clear view of which submission is the constraint.
- Solution: The AI agent tracks submission status, outstanding challenge items, and assumption revision rounds across business units throughout the consolidation cycle, identifies the submissions on the critical path, and surfaces the constraint view to the CFO team. The CFO uses the constraint identification to direct follow-up effort; the AI agent updates the critical path view in real time as submissions are received and challenges are resolved.
- OKR: Critical-path submissions in the budget and reforecast consolidation cycle are identified continuously, giving the CFO team a constraint view to direct assumption-challenge effort and unblock the consolidation sequence.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's submission tracking and critical-path identification deployed across ≥90% of business unit submissions for each consolidation cycle within 6 months of go-live. |
| Acceptance | ≥80% of AI-identified critical-path constraints confirmed as the actual consolidation bottleneck by the CFO team for each cycle. |
| Cycle | Budget consolidation elapsed time from submission deadline to CFO-approved consolidated plan reduced by ≥20% within the first full planning cycle after go-live. |

#### Financial close narrative and management pack automation

- URN: urn:financial-services:scenario:flow/financial-control-cycle/fcc-close-narrative-automation
- Lens: Automation
- Complexity: M
- Intent: AI-assembled monthly close narrative, management account pack, regulatory return, and MD&A variance commentary — pulling from the closed ledger on the established finance calendar with CFO-team review before distribution. Senior finance capacity is directed toward interpretation and decision support rather than report production mechanics.
- Problem to solve: Monthly close narrative, management pack production, regulatory return formatting, and MD&A drafting are manual tasks that consume senior finance capacity on well-structured synthesis work. The structure of these tasks — pulling from known data sources, applying standard methodology, narrating variance — makes them strong candidates for AI-assisted production.
- Solution: The AI agent pulls from the closed ledger after sign-off, assembles the management account tables, drafts the revenue, cost, and credit-loss variance narratives, formats the regulatory return, and produces the MD&A draft. The CFO team reviews and edits the full pack before board or ALCO distribution; the AI agent maintains a version trail for each period's production cycle.
- OKR: Monthly close narrative, management account pack, regulatory return, and MD&A variance commentary are assembled by the AI agent from the closed ledger on the finance calendar, with the CFO team reviewing and editing before board or ALCO distribution.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent assembles the full close reporting package for ≥11 of 12 monthly close cycles in the first year of go-live. |
| Acceptance | ≥80% of AI-produced management packs accepted by the CFO team with editing rather than full redraft before distribution. |
| Cycle | Close-to-distribution cycle time for the management account pack reduced by ≥3 business days compared to the fully manual production baseline. |

#### Reforecast cross-unit forward signal enrichment

- URN: urn:financial-services:scenario:flow/financial-control-cycle/fcc-reforecast-cross-signal-enrichment
- Lens: Enablement
- Complexity: M
- Intent: Cross-unit forward signals are surfaced to the reforecast process before they appear in the actuals — a credit portfolio trend implying a revenue headwind, a cost trajectory that requires provision adjustment, an operational loss run-rate that will exceed budget. Assumptions are updated earlier, and the gap between the forecast and the eventual outcome narrows.
- Problem to solve: Reforecast assumptions are updated by business units based on their own forward visibility. Cross-unit signals that imply assumption changes — credit portfolio trends, operational cost trajectories — are not systematically surfaced to the reforecast process before they appear in the actuals.
- Solution: The AI agent monitors leading indicators across business units and the credit, cost, and operational data feeds, identifies signals that are inconsistent with the current reforecast assumptions, and surfaces them to the CFO team with a structured impact narrative. The CFO team reviews the flagged signals and decides whether to initiate a reforecast assumption change; business unit CFOs are notified of signals affecting their submissions.
- OKR: Cross-unit forward signals — credit portfolio trends, cost trajectories, and operational loss run-rates that are inconsistent with current reforecast assumptions — are surfaced to the CFO team before they appear in the actuals.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent monitors leading indicator feeds across ≥4 business units and flags cross-unit assumption conflicts for ≥10 of 12 months in the first year. |
| Acceptance | ≥75% of AI-surfaced cross-unit signals assessed by the CFO team as meriting a reforecast assumption review. |
| Cycle | Lead time between cross-unit signal emergence and CFO-team-reviewed impact narrative reduced from actuals-driven identification (4–6 weeks lag) to ≤5 business days on a continuous basis. |

#### IFRS 9 provision intelligence and planning integration

- URN: urn:financial-services:scenario:flow/financial-control-cycle/fcc-ifrs9-provision-intelligence
- Lens: New opps
- Complexity: L
- Intent: Continuous IFRS 9 ECL intelligence integrated with the planning and reforecast cycle — credit-loss assumptions updated within days as the portfolio's staging distribution shifts, rather than waiting for the next formal provision review. The CFO and Finance team have an IFRS 9-consistent forward P&L view between provision review cycles.
- Problem to solve: IFRS 9 ECL provision outputs are produced for governance and regulatory cycles but are not integrated into the rolling reforecast and planning process between those cycles. Credit-loss assumptions in the forward plan lag the portfolio's actual staging distribution, creating provision surprises at the formal review.
- Solution: The AI agent monitors the credit portfolio's staging migration data continuously, recalculates the ECL forward projection using the approved IFRS 9 model, and updates the CFO team's provision assumption view between formal review cycles. The Chief Accounting Officer and Credit Risk validate the updated projection before it is incorporated into the reforecast; material staging movements above a defined threshold trigger an immediate alert.
- OKR: IFRS 9 ECL projections are updated continuously as the credit portfolio's staging distribution shifts, giving the CFO and Finance team a provision-consistent forward P&L view between formal provision review cycles.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's ECL forward projection is updated within 48 hours of material staging migration events for ≥95% of qualifying portfolio movements throughout the year. |
| Acceptance | ≥85% of the AI agent's ECL projection updates validated by the Chief Accounting Officer and Credit Risk as methodologically consistent with the approved IFRS 9 model without material revision. |
| Cycle | Interval from material staging migration to CFO-team-reviewed forward provision impact reduced from the next formal provision review cycle to ≤3 business days. |
