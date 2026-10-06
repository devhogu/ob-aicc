# 

source: html-alt/financial-services/en/customer-channels/index.html


[PAGE TEXT]
Assisted channels
Physical branches (12)
Network design operations
Branch network planning (3)
·
Teller & frontline operations (3)
·
Cash management (3)
Branch performance
Branch performance reporting (3)
Self-service & partner
Digital channels (12)
Web mobile experience
Digital onboarding (3)
·
Digital engagement & personalisation (3)
Digital engagement operations
Digital support & servicing (3)
·
Digital adoption tracking (3)
Channel governance
Channel Cycles (17)
Performance & service
Channel performance review cycle (5)
Service-level & incident governance cycle (4)
Strategy & evolution
Channel-mix steering cycle (4)
Channel evolution cycle (4)
Assisted channels
Contact center (15)
Inbound servicing
Inbound call routing & IVR (3)
·
Agent assist & guided resolution (3)
·
Complaint & escalation handling (3)
Outbound multichannel
Contact center quality assurance (3)
·
Workforce management (3)
Self-service & partner
ATMs & self-service (12)
Network uptime
ATM uptime & incident management (3)
·
Cash replenishment optimisation (3)
Service evolution
ATM fraud & skimming detection (3)
·
Self-service channel evolution (3)
Assisted channels
Relationship management (12)
Rm productivity
RM book management (3)
·
Client interaction & meeting prep (3)
·
Relationship deepening & cross-sell (3)
Client lifecycle stewardship
Client lifecycle stewardship (3)
Self-service & partner
Partner & API channels (12)
Open banking api governance
Open banking & API governance (3)
·
API product catalogue & monetisation (3)
Partner network economics
Partner performance monitoring (3)
·
Partner network economics (3)
Scenarios
Lens
Scenario
Intent
Complexity

### CARD 1 [Optimize|S] Omnichannel Service-Recovery Orchestration
urn: urn:financial-services:scenario:customer-channels/omnichannel-service-recovery-orchestration
intent: Agent detects when a customer's unresolved service failure has generated contact across more than one channel and orchestrates a single consolidated resolution path, eliminating repeat-contact waste and redundant hand-offs. It assigns ownership to the channel best placed to resolve and drafts a resolution brief for the handling staff with full cross-channel interaction history. Repeat-contact rate by issue category, tracked across channels, is the primary outcome metric.
Problem to solve: A customer whose issue is not resolved on first contact returns through a different channel — calling after a failed digital complaint, visiting a branch after an unresolved contact center case. Each channel treats the incoming contact as new; the customer restates the full issue while the handling staff have no cross-channel history, and the bank generates avoidable cost across multiple channels for a single unresolved issue. Repeat-contact rate is not measured across channels under the current model, making the cost of repeat-contact cycles invisible to the Head of Channels.
Solution: Agent monitors unresolved case records across all channels and flags customers who have contacted more than one channel about the same outstanding issue within a defined resolution window. It generates a cross-channel repeat-contact alert with the full interaction history, assigns ownership to the channel best placed to resolve, and drafts a resolution brief for the handling staff. The repeat-contact rate by issue category, measured across channels, provides the primary metric for tracking the impact of the orchestration capability.
OKR objective: Customers with an unresolved service failure who have contacted more than one channel receive a single consolidated resolution path — with ownership assigned and a resolution brief with full cross-channel history delivered to the handling staff — eliminating repeat-contact waste.
OKR KR [Adoption]: Agent detects and orchestrates a consolidated resolution path for ≥90% of cross-channel repeat-contact cases within 4 hours of repeat-contact identification, across ≥48 consecutive weeks.
OKR KR [Acceptance]: Repeat-contact rate by issue category, measured across channels, reduced by ≥25% against the pre-deployment baseline within 12 months.
OKR KR [Cycle]: Cross-channel repeat-contact identification and resolution brief delivery cycle reduced from multi-day manual case reconciliation to ≤4 hours of automated detection and brief generation.

### CARD 2 [Insights|M] Channel Mix Cost-to-Serve Analysis
urn: urn:financial-services:scenario:customer-channels/channel-mix-cost-to-serve-analysis
intent: Agent computes cost-to-serve by transaction type across all channels — branch, contact center, ATM, digital, and partner — and models the economic impact of channel mix shifts for the Head of Channels. The output consolidates staffing, infrastructure, and third-party fee allocation into a per-channel, per-transaction-type cost view unavailable from individual channel reporting. The Head of Channels uses the monthly cross-channel economics pack to prioritise channel migration investments and benchmark the portfolio against peer institutions.
Problem to solve: Channel economics are tracked separately by each channel head, with no unified cost-to-serve view for the same transaction type across channels. The Head of Channels cannot quantify the economic impact of mix-shift programmes or compare channel unit economics without commissioning bespoke analytical work. Peer benchmarking and migration business-case construction are constrained by the absence of a consolidated cross-channel cost baseline.
Solution: Agent reads cost allocation data per channel and maps transaction types across channel event logs, computing a per-channel, per-transaction-type cost-to-serve with a confidence range. It models the economic impact of target channel mix shifts — projecting cost savings from migration of high-cost transaction types to lower-cost channels. The Head of Channels reviews the generated economics pack monthly and uses it to direct channel migration budgets.
OKR objective: A monthly cross-channel cost-to-serve pack — covering staffing, infrastructure, and third-party fee allocation by channel and transaction type — is available to the Head of Channels, enabling channel migration investment decisions from a unified cost baseline.
OKR KR [Adoption]: Agent delivers the cross-channel cost-to-serve pack for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live.
OKR KR [Acceptance]: ≥80% of cost-to-serve outputs accepted by the Head of Channels as the basis for channel migration business cases without requiring supplementary commissioned analysis.
OKR KR [Cycle]: Cost-to-serve analysis cycle reduced from 3–4 weeks of bespoke analytical work to ≤2 days of agent-assisted pack assembly.

### CARD 3 [Automation|M] Cross-Channel Complaint Intake Unification
urn: urn:financial-services:scenario:customer-channels/cross-channel-complaint-intake-unification
intent: Agent unifies complaint records across all intake channels — branch, contact center, digital, ATM dispute, and partner API — into a single regulatory complaint record, eliminating duplicate case creation when a customer contacts multiple channels about the same issue. The unified record sets the SLA timer from the earliest intake event and routes to the complaints handler with full cross-channel interaction history attached. The handler works from one consolidated file rather than reconciling independent channel records.
Problem to solve: A customer who raises the same complaint across digital, contact center, and branch generates separate case records in separate systems; the bank's regulatory complaint count is overstated and SLA timers run independently across duplicates. The complaints team cannot see that the same customer has escalated across channels, preventing coordinated resolution and creating the risk of contradictory responses to the same underlying issue. Under NBKR Resolution No. 47/4 and CBR Ordinance No. 59-I, each formal complaint requires a single dated record with an unbroken audit trail — a standard that multi-channel duplicate creation systematically undermines.
Solution: Agent reads complaint events across all channel intake systems — contact center CRM, digital submission queue, branch teller log, ATM dispute record, and partner escalation feed — and matches records to the same underlying customer issue using customer ID, issue category, and time proximity. It merges duplicates into a single regulatory complaint record, sets the SLA timer from the earliest intake event, and routes the unified record with the full cross-channel history to the complaints handler. The handler works from one consolidated file; the regulatory complaint count reflects unique issues rather than unique intake events.
OKR objective: Every multi-channel complaint event is unified into a single regulatory complaint record — with SLA timer set from the earliest intake event and full cross-channel interaction history attached — eliminating duplicate case creation and contradictory resolution risk.
OKR KR [Adoption]: Agent matches and unifies ≥95% of multi-channel complaint events involving the same customer issue within 4 hours of intake detection, across ≥48 consecutive weeks.
OKR KR [Acceptance]: ≥90% of unified records confirmed as accurately matched by the complaints handler; regulatory complaint count reconciled to unique issues on supervisory reporting extract.
OKR KR [Cycle]: Duplicate complaint identification and unification cycle reduced from end-of-day manual reconciliation to automated unification within 4 hours of multi-channel event detection.

### CARD 4 [Enablement|M] Channel Frontline Coaching Synthesis
urn: urn:financial-services:scenario:customer-channels/channel-frontline-coaching-synthesis
intent: Agent synthesises frontline performance signals from branch teller interactions, contact center QA scores, ATM-assisted service events, and RM interaction outcomes into a unified coaching brief for the Head of Channels. The brief ranks channels and sub-channels by degrading metrics and produces a prioritised coaching agenda for the Head of Channels to direct to each channel head. The output is generated on a monthly cadence from operational data already produced by each channel team.
Problem to solve: Frontline performance across channels is monitored separately — branch regional managers review branch metrics, the contact center operations team reviews QA scores, and RM team heads review book activity. The Head of Channels has no cross-channel view of where frontline quality is degrading, which channels carry the highest complaint-to-interaction ratio, or where coaching investment would produce the greatest customer experience improvement across the full service estate. Without a synthesised view, coaching investment is directed by individual channel heads rather than by a portfolio-wide quality signal.
Solution: Agent reads branch teller transaction and complaint data, contact center QA scores and FCR rates, ATM dispute-to-transaction ratios, and RM interaction quality indicators from CRM. It produces a monthly cross-channel frontline quality brief ranked by channel and sub-channel, with the top degrading metrics and a prioritised coaching agenda for the Head of Channels to direct to each channel head. Channel heads receive targeted coaching agendas; frontline quality improvement is tracked against the baseline complaint-to-interaction ratio and FCR rate per channel.
OKR objective: A monthly cross-channel frontline quality brief — ranking channels by degrading metrics and producing a prioritised coaching agenda — is available to the Head of Channels from unified analysis of branch, contact center, ATM, and RM performance signals.
OKR KR [Adoption]: Agent delivers the cross-channel coaching brief for ≥95% of monthly cycles for ≥12 consecutive months from go-live.
OKR KR [Acceptance]: ≥80% of coaching agenda items confirmed as actionable by the Head of Channels on monthly review; FCR rate and complaint-to-interaction ratio tracked as primary outcome metrics.
OKR KR [Cycle]: Cross-channel frontline quality synthesis cycle reduced from 5–7 days of manual extraction across channel reporting systems to ≤24 hours of agent-assisted assembly.

### CARD 5 [New opps|M] Cross-Channel Segment Gap Intelligence
urn: urn:financial-services:scenario:customer-channels/cross-channel-segment-gap-intelligence
intent: Agent maps each customer segment's actual channel usage against the bank's intended channel coverage model to surface segments that are underserved — transacting through a costly channel where a digital or self-service alternative exists, or outside the bank's channel reach — for the CCO and Head of Channels. The quarterly segment-channel gap brief includes prioritised investment recommendations and estimated revenue and cost impact per identified gap. The output provides the first cross-channel investment prioritisation input based on segment-level coverage rather than aggregate volume and cost metrics.
Problem to solve: Channel investment decisions are based on aggregate volume and cost data; the bank cannot identify which customer segments are trapped in high-cost channels because a lower-cost alternative is unavailable or not adopted. Without a segment-level channel coverage view, investment priorities are set on cost metrics alone rather than on where channel gaps are suppressing revenue or generating avoidable cost by segment. Segments the bank is failing to reach through any channel are invisible in the current reporting model, creating blind spots in growth and retention planning.
Solution: Agent reads segment profiles, product holdings, and channel usage patterns across branch transactions, digital logins, contact center call reasons, ATM usage, and RM interaction records. It computes a channel coverage map per segment — showing which channels each segment uses, which it avoids, and where digital or self-service alternatives are available but not adopted. The Head of Channels receives a quarterly segment-channel gap brief with prioritised investment recommendations and estimated revenue and cost impact per gap.
OKR objective: A quarterly segment-channel gap brief — mapping each segment's actual channel usage against the intended coverage model and providing prioritised investment recommendations with estimated revenue and cost impact — is available to the CCO and Head of Channels.
OKR KR [Adoption]: Agent delivers the segment-channel gap brief for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live.
OKR KR [Acceptance]: ≥75% of investment recommendations confirmed as actionable by the Head of Channels without requiring supplementary segment-level analysis.
OKR KR [Cycle]: Segment-channel gap analysis cycle reduced from annually commissioned analytical work to quarterly automated delivery within 1 week of data refresh.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
