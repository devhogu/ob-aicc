---
key: "journey-dispute"
label: "Card Dispute Progress Support"
section: "Journey options"
---

## Card Dispute Progress Support {#journey-dispute-card-dispute-progress-support}

Journey option for the INI-013 (Proposed; Portfolio Funnel). If selected at Scoping, it becomes the journey annex to the Initiative Brief (see [Journey options and selection](#journeys)). This page holds only what is specific to the journey; the common content is on the [Initiative Brief](#charter), [Governance and roles](#governance) and [Controls and evidence](#controls) pages, and the technical profile on [Journey technical profiles](#journey-profiles).

**Intent:** fewer avoidable status contacts and less uncertainty for the customer during a card dispute, because the servicing employee sees the dispute stage, the actions completed, the evidence still outstanding, the communications already sent and the approved next step, each linked to its source record. **Scope of the decision requested:** one dispute type and one servicing queue.

### Scope and exclusions {#journey-dispute-scope-and-exclusions}

| Matter | Treatment in the pilot | Reason |
| --- | --- | --- |
| One dispute type, named at Scoping; one servicing queue | Included | Small enough to measure |
| Dispute stage and milestones; prior contacts and communications; evidence requested and received (type and status only) | Included | The history the employee rebuilds by hand today; the employee needs to know what is missing, not what a document says |
| Deadlines and escalation conditions | Included only as the dispute system or an approved rule gives them | The assistant shows a deadline; it does not calculate or change one |
| Source of the dispute stage | Included only if the dispute system has a read interface or an approved extract, with stage dates (to confirm at Scoping) | Stages without a recorded source stay with specialists |
| Adjudication, eligibility and reimbursement | Excluded; Disputes Operations | They decide the customer's entitlement |
| Fraud determination | Excluded; existing fraud process | Own investigation and decision authority |
| Setting or changing a legal or card-scheme deadline | Excluded; Disputes Operations | A wrong deadline can cost the customer a right |
| Legal interpretation | Excluded; legal or the dispute specialist | Outside an employee-assist pilot |

### Process function and what it approves {#journey-dispute-process-function-and-what-it-approves}

| Item | For this journey |
| --- | --- |
| Process function (Dependency) | Disputes Operations: a Dependency of the Initiative, not a second Domain, unless it claims part of the benefit. Its specialists act as Domain Experts when the Domain Owner names them |
| What it approves | The dispute stages in scope and the explanation of each; the evidence each stage needs; the action list (the next steps the assistant may propose per stage); when a case goes to a specialist; what counts as a status contact and as a repeated evidence request; the reading of the historical cases in the Evaluation set; the dispute-servicing procedure and evidence guidance with their effective dates, of which it is the knowledge-source owner noted in the AI Registry |
| First users | The Customer Service team that handles card dispute contacts |
| Control remits this journey adds | Compliance and legal confirm which card-scheme rules and legal deadlines apply, and which notices the customer must receive |

### Baseline measures {#journey-dispute-baseline-measures}

Each baseline is a reference to its source, usually a management information (MI) report, taken in Discovery: Business case by the source owner; formulas and the comparison design are in the measurement annex on the [Initiative Brief](#charter) page.

| Measure | Use | Source reference |
| --- | --- | --- |
| Repeat contacts about the same eligible open dispute | Leading indicator: repeat contact | [MI report: contacts per open dispute, by dispute type] |
| Status-investigation effort per eligible contact | Leading indicator: handling effort | [Workforce report or case timestamps; timestamps to confirm] |
| Avoidable status contacts: contacts asking for progress when the stage has not changed since the last contact | Journey indicator (Brief section 2) | [MI report: status contacts per open dispute, matched to stage dates] |
| Repeated, incomplete or incorrect evidence requests | Supporting measure | [Quality review of dispute cases] |
| Reopened or re-routed dispute-service cases | Supporting measure | [Case system: reopen and transfer records] |
| Dispute-service complaints and escalations | Control limit | [Complaints record] |

### Quality and control-limit criteria {#journey-dispute-quality-and-control-limit-criteria}

The journey values of the one acceptance rule on [Controls and evidence](#controls).

| Criterion | For this journey |
| --- | --- |
| State quality | At least 95% of sampled readings of stage, evidence, owner, deadline and next step correct in the Evaluation set, across the languages of the records (Russian, Kyrgyz, mixed). A proposed floor, confirmed with Disputes Operations after the baseline; it may be raised, not lowered |
| Critical errors | A wrong stage or deadline shown; a request for evidence already received; any statement on the likely outcome of the dispute. None found in the Evaluation set; any one found blocks first use until corrected and retested |
| Traceability | Every dispute fact, deadline, evidence status and prior action shown links to its source record |
| Zero-tolerance events | A legal or card-scheme deadline missed because of the assistant; a customer's dispute right lost; dispute details disclosed to a person not entitled to them |
| Monitored limits | Complaints and escalations do not get worse than the baseline by more than the agreed tolerance |

### Stop conditions {#journey-dispute-stop-conditions}

- The dispute stage or deadlines cannot be shown reliably from the dispute system.
- Customers' dispute rights could be impaired.
- Disputes Operations cannot approve an action list and evidence list for the stages in scope.
- A control limit above cannot be held.

### Expected volume {#journey-dispute-expected-volume}

Does one team see enough open disputes of the chosen type, within the observation period, for a claim on status contacts? The figure is [MI report: open disputes and status contacts per month for the chosen dispute type in the pilot queue]. For one team it is likely too low. The customer outcome is then directional evidence (an indication, not proof), and the decision after the MVP rests on investigation effort, evidence-request quality and the quality of stage and deadline readings, which a smaller sample can show. Rare stages and deadline boundaries may need every available historical case in the Evaluation set. A higher-volume dispute type or a longer observation period is chosen at Scoping, not after the result.
