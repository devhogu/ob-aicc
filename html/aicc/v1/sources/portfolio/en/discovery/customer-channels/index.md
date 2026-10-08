# Customer & Channels

Customer & Channels is the Bank's distribution layer — the physical, digital, and partner infrastructure through which it acquires, serves, and retains customers across every segment. The channel mix spans six sub-concerns: physical branches, digital channels, contact center, ATMs & self-service, relationship management, and partner & API channels. Each channel has distinct economics, its own consumer-protection obligations, and a different customer-experience profile. **The opportunity for GenAI is to instrument channel economics and customer journey quality continuously** — replacing periodic reviews with always-current cost-to-serve analytics, predictive maintenance, real-time agent assist, and personalized digital engagement that lift conversion and reduce assisted-channel cost simultaneously.

## Problems

### Assisted channels {#assisted-channels}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Branch network performance, contact-center queue patterns, and relationship manager book health are each measured within their own channel reporting cycle. Cross-channel comparisons — cost-to-serve for the same transaction type across branch and contact center, or the RM interaction frequency relative to attrition risk — require bespoke analytical work that most teams complete quarterly at best. |
| Enablement | Branch managers calibrate staffing schedules from historical averages; contact-center agents search knowledge bases manually during live calls; relationship managers prepare client briefs from memory and ad hoc CRM review. Each assisted-channel role carries an analytical burden that reduces time for customer-facing activity. |
| Automation | Branch performance packs, contact-center quality assurance scoring, and RM book management reporting are assembled manually from multiple system exports on a monthly or quarterly cadence. The recurring, structured nature of each report makes them candidates for AI-driven assembly. |
| New business opportunities | Assisted channels generate the highest-margin customer interactions — RM cross-sell conversations, complex product advice, relationship deepening — but the bandwidth of each channel is constrained by administrative overhead. Reducing that overhead releases RM and branch capacity for revenue-generating activity that the channel mix is sized to deliver. |

### Self-service & partner {#self-service-partner}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Digital onboarding funnels, ATM fleet uptime, and API consumption are each tracked in aggregate within their own platform — the analytics platform, the incident log, and the API gateway dashboard. Step-level abandonment by segment, per-machine failure risk, and revenue yield per API product require bespoke analytical work, so the Head of Digital, the Head of Self-Service, and the Head of Partner Channels act on periodic retrospectives rather than on a current signal. |
| Enablement | Digital operations, ATM operations, and partner management teams prepare their own working briefs — daily servicing status, cash carrier route priorities, partner review packs — by pulling data from separate systems before each cycle. The preparation burden delays the response to servicing degradation, cash depletion risk, and partner performance trends. |
| Automation | ATM cash load orders, outage and fraud incident notifications, digital adoption reporting, partner billing reconciliation, and, where the Bank runs an open-banking API platform, open banking compliance reporting are calculated or compiled manually from system exports. Each is a structured, data-driven task that follows the same steps every cycle, making it a candidate for AI-driven preparation with human review and release. |
| New business opportunities | Self-service and partner channels are the lowest-cost distribution surfaces, but their commercial potential is reviewed only at campaign or annual-review cadence. A next-best-action at session level, terminal estate reconfiguration modeled per location, and API catalog and partner network expansion driven by demand signals turn these channels from cost-reduction levers into sources of revenue growth. |

## Overview

### Physical branches {#physical-branches}

- Group: Assisted channels

| Sub-group | Items |
| --- | --- |
| Network design & operations | branch-network-planning, teller-frontline-operations, cash-management |
| Branch performance | branch-performance-reporting |

### Digital channels {#digital-channels}

- Group: Self-service & partner

| Sub-group | Items |
| --- | --- |
| Web & mobile experience | digital-onboarding, digital-engagement-personalisation |
| Digital servicing & adoption | digital-support-servicing, digital-adoption-tracking |

### Channel Cycles {#channel-cycles}

- Group: Channel governance

| Section | List name | Flows |
| --- | --- | --- |
| Performance & service | Performance & service | channel-performance-review-cycle, service-level-incident-cycle |
| Strategy & evolution | Strategy & evolution | channel-mix-steering-cycle, channel-evolution-cycle |

### Contact center {#contact-center}

- Group: Assisted channels

| Sub-group | Items |
| --- | --- |
| Inbound servicing | inbound-call-routing-ivr, agent-assist-guided-resolution, complaint-escalation-handling |
| Quality & workforce | contact-center-quality-assurance, workforce-management |

### ATMs & self-service {#atms-self-service}

- Group: Self-service & partner

| Sub-group | Items |
| --- | --- |
| Network uptime | atm-uptime-incident-management, cash-replenishment-optimisation |
| Fraud control & service evolution | atm-fraud-skimming-detection, self-service-channel-evolution |

### Relationship management {#relationship-management}

- Group: Assisted channels

| Sub-group | Items |
| --- | --- |
| RM productivity | rm-book-management, client-interaction-meeting-prep, relationship-deepening-cross-sell |
| Client lifecycle stewardship | client-lifecycle-stewardship |

### Partner & API channels {#partner-api-channels}

- Group: Self-service & partner

| Sub-group | Items |
| --- | --- |
| Open banking & API governance | open-banking-api-governance, api-product-catalogue-monetisation |
| Partner network economics | partner-performance-monitoring, partner-network-economics |

## Scenarios

### Omnichannel Service-Recovery Orchestration

- URN: urn:financial-services:scenario:customer-channels/omnichannel-service-recovery-orchestration
- Lens: Optimize
- Complexity: M
- Intent: The AI agent detects when a customer's unresolved service failure has generated contact across more than one channel and orchestrates a single consolidated resolution path, eliminating repeat-contact waste and redundant hand-offs. It assigns ownership to the channel best placed to resolve and drafts a resolution brief for the handling staff with full cross-channel interaction history. Repeat-contact rate by issue category, tracked across channels, is the primary outcome metric.
- Problem to solve: A customer whose issue is not resolved on first contact returns through a different channel — calling after a failed digital complaint, visiting a branch after an unresolved contact-center case. Each channel treats the incoming contact as new; the customer restates the full issue while the handling staff have no cross-channel history, and the Bank generates avoidable cost across multiple channels for a single unresolved issue. Repeat-contact rate is not measured across channels under the current model, making the cost of repeat-contact cycles invisible to the Head of Channels.
- Solution: The AI agent monitors unresolved case records across all channels and flags customers who have contacted more than one channel about the same outstanding issue within a defined resolution window. It generates a cross-channel repeat-contact alert with the full interaction history, assigns ownership to the channel best placed to resolve, and drafts a resolution brief for the handling staff. The repeat-contact rate by issue category, measured across channels, provides the primary metric for tracking the impact of the orchestration capability.
- OKR: Customers with an unresolved service failure who have contacted more than one channel receive a single consolidated resolution path — with ownership assigned and a resolution brief with full cross-channel history delivered to the handling staff — eliminating repeat-contact waste.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent detects and orchestrates a consolidated resolution path for ≥90% of cross-channel repeat-contact cases within 4 hours of repeat-contact identification, across ≥48 consecutive weeks. |
| Acceptance | Repeat-contact rate by issue category, measured across channels, reduced by ≥25% against the pre-deployment baseline within 12 months. |
| Cycle | Cross-channel repeat-contact identification and resolution brief delivery cycle reduced from multi-day manual case reconciliation to ≤4 hours of automated detection and brief generation. |

### Channel Mix Cost-to-Serve Analysis

- URN: urn:financial-services:scenario:customer-channels/channel-mix-cost-to-serve-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent computes cost-to-serve by transaction type across all channels — branch, contact center, ATM, digital, and partner — and models the economic impact of channel mix shifts for the Head of Channels. The output consolidates staffing, infrastructure, and third-party fee allocation into a per-channel, per-transaction-type cost view unavailable from individual channel reporting. The Head of Channels uses the monthly cross-channel economics pack to prioritize channel migration investments and benchmark the portfolio against peer institutions.
- Problem to solve: Channel economics are tracked separately by each channel head, with no unified cost-to-serve view for the same transaction type across channels. The Head of Channels cannot quantify the economic impact of mix-shift programs or compare channel unit economics without commissioning bespoke analytical work. Peer benchmarking and migration business-case construction are constrained by the absence of a consolidated cross-channel cost baseline.
- Solution: The AI agent reads cost allocation data per channel and maps transaction types across channel event logs, computing a per-channel, per-transaction-type cost-to-serve with a confidence range. It models the economic impact of target channel mix shifts — projecting cost savings from migration of high-cost transaction types to lower-cost channels. The Head of Channels reviews the generated economics pack monthly and uses it to direct channel migration budgets.
- OKR: A monthly cross-channel cost-to-serve pack — covering staffing, infrastructure, and third-party fee allocation by channel and transaction type — is available to the Head of Channels, enabling channel migration investment decisions from a unified cost baseline.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the cross-channel cost-to-serve pack for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥80% of cost-to-serve outputs accepted by the Head of Channels as the basis for channel migration business cases without requiring supplementary commissioned analysis. |
| Cycle | Cost-to-serve analysis cycle reduced from 3–4 weeks of bespoke analytical work to ≤2 days of AI-assisted pack assembly. |

### Cross-Channel Complaint Intake Unification

- URN: urn:financial-services:scenario:customer-channels/cross-channel-complaint-intake-unification
- Lens: Automation
- Complexity: M
- Intent: The AI agent unifies complaint records across all intake channels — branch, contact center, digital, ATM dispute, and partner API — into a single regulatory complaint record, eliminating duplicate case creation when a customer contacts multiple channels about the same issue. The unified record sets the SLA timer from the earliest intake event and routes to the complaint handler with full cross-channel interaction history attached. The handler works from one consolidated file rather than reconciling independent channel records.
- Problem to solve: A customer who raises the same complaint across digital, contact center, and branch generates separate case records in separate systems; the Bank's regulatory complaint count is overstated and SLA timers run independently across duplicates. The complaints team cannot see that the same customer has escalated across channels, preventing coordinated resolution and creating the risk of contradictory responses to the same underlying issue. Consumer-protection requirements commonly call for a single dated record of each formal complaint with an unbroken audit trail — a standard that multi-channel duplicate creation systematically undermines.
- Solution: The AI agent reads complaint events across all channel intake systems — contact-center CRM, digital submission queue, branch teller log, ATM dispute record, and partner escalation feed — and matches records to the same underlying customer issue using customer ID, issue category, and time proximity. It merges duplicates into a single regulatory complaint record, sets the SLA timer from the earliest intake event, and routes the unified record with the full cross-channel history to the complaint handler. The handler works from one consolidated file; the regulatory complaint count reflects unique issues rather than unique intake events.
- OKR: Every multi-channel complaint event is unified into a single regulatory complaint record — with SLA timer set from the earliest intake event and full cross-channel interaction history attached for the complaint handler — eliminating duplicate case creation and contradictory resolution risk.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent matches and unifies ≥95% of multi-channel complaint events involving the same customer issue within 4 hours of intake detection, across ≥48 consecutive weeks. |
| Acceptance | ≥90% of unified records confirmed as accurately matched by the complaint handler; regulatory complaint count reconciled to unique issues on the supervisory reporting extract. |
| Cycle | Duplicate complaint identification and unification cycle reduced from end-of-day manual reconciliation to automated unification within 4 hours of multi-channel event detection. |

### Channel Frontline Coaching Synthesis

- URN: urn:financial-services:scenario:customer-channels/channel-frontline-coaching-synthesis
- Lens: Enablement
- Complexity: M
- Intent: The AI agent synthesizes frontline performance signals from branch teller interactions, contact-center QA scores, ATM-assisted service events, and RM interaction outcomes into a unified coaching brief for the Head of Channels. The brief ranks channels and sub-channels by degrading metrics and produces a prioritized coaching agenda for the Head of Channels to direct to each channel head. The output is generated on a monthly cadence from operational data already produced by each channel team.
- Problem to solve: Frontline performance across channels is monitored separately — branch regional managers review branch metrics, the contact-center operations team reviews QA scores, and RM team heads review book activity. The Head of Channels has no cross-channel view of where frontline quality is degrading, which channels carry the highest complaint-to-interaction ratio, or where coaching investment would produce the greatest customer experience improvement across the full service estate. Without a synthesized view, coaching investment is directed by individual channel heads rather than by a portfolio-wide quality signal.
- Solution: The AI agent reads branch teller transaction and complaint data, contact-center QA scores and first-contact resolution (FCR) rates, ATM dispute-to-transaction ratios, and RM interaction quality indicators from CRM. It produces a monthly cross-channel frontline quality brief ranked by channel and sub-channel, with the top degrading metrics and a prioritized coaching agenda for the Head of Channels to direct to each channel head. Channel heads receive targeted coaching agendas; frontline quality improvement is tracked against the baseline complaint-to-interaction ratio and FCR rate per channel.
- OKR: A monthly cross-channel frontline quality brief — ranking channels by degrading metrics and producing a prioritized coaching agenda — is available to the Head of Channels from unified analysis of branch, contact center, ATM, and RM performance signals.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the cross-channel coaching brief for ≥95% of monthly cycles for ≥12 consecutive months from go-live. |
| Acceptance | ≥80% of coaching agenda items confirmed as actionable by the Head of Channels on monthly review; FCR rate and complaint-to-interaction ratio tracked as primary outcome metrics. |
| Cycle | Cross-channel frontline quality synthesis cycle reduced from 5–7 days of manual extraction across channel reporting systems to ≤24 hours of AI-assisted assembly. |

### Cross-Channel Segment Gap Intelligence

- URN: urn:financial-services:scenario:customer-channels/cross-channel-segment-gap-intelligence
- Lens: New opps
- Complexity: M
- Intent: The AI agent maps each customer segment's actual channel usage against the Bank's intended channel coverage model to surface segments that are underserved — transacting through a costly channel where a digital or self-service alternative exists, or outside the Bank's channel reach — for the CCO and Head of Channels. The quarterly segment-channel gap brief includes prioritized investment recommendations and estimated revenue and cost impact per identified gap. The output provides the first cross-channel investment prioritization input based on segment-level coverage rather than aggregate volume and cost metrics.
- Problem to solve: Channel investment decisions are based on aggregate volume and cost data; the Bank cannot identify which customer segments are trapped in high-cost channels because a lower-cost alternative is unavailable or not adopted. Without a segment-level channel coverage view, investment priorities are set on cost metrics alone rather than on where channel gaps are suppressing revenue or generating avoidable cost by segment. Segments the Bank is failing to reach through any channel are invisible in the current reporting model, creating blind spots in growth and retention planning.
- Solution: The AI agent reads segment profiles, product holdings, and channel usage patterns across branch transactions, digital logins, contact-center call reasons, ATM usage, and RM interaction records. It computes a channel coverage map per segment — showing which channels each segment uses, which it avoids, and where digital or self-service alternatives are available but not adopted. The CCO and Head of Channels receive a quarterly segment-channel gap brief with prioritized investment recommendations and estimated revenue and cost impact per gap.
- OKR: A quarterly segment-channel gap brief — mapping each segment's actual channel usage against the intended coverage model and providing prioritized investment recommendations with estimated revenue and cost impact — is available to the CCO and Head of Channels.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the segment-channel gap brief for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live. |
| Acceptance | ≥75% of investment recommendations confirmed as actionable by the Head of Channels without requiring supplementary segment-level analysis. |
| Cycle | Segment-channel gap analysis cycle reduced from annually commissioned analytical work to quarterly automated delivery within 1 week of data refresh. |
