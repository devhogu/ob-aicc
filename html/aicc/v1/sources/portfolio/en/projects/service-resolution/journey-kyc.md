---
key: "journey-kyc"
label: "Onboarding/KYC Progress Support"
section: "Journey options"
---

## Onboarding/KYC Progress Support {#journey-kyc-onboarding-kyc-progress-support}

Journey option for the INI-013 (Proposed; Portfolio Funnel). If selected at Scoping, it becomes the journey annex to the Initiative Brief (see [Journey options and selection](#journeys)). This page holds only what is specific to the journey; the common content is on the [Initiative Brief](#charter), [Governance and roles](#governance) and [Controls and evidence](#controls) pages, and the technical profile on [Journey technical profiles](#journey-profiles).

**Intent:** stalled onboarding and know-your-customer (KYC) cases move forward, because the servicing employee sees one accurate account of the service state, the information the customer still has to provide, the responsible queue and the approved next step, without reading, exposing or inferring restricted financial-crime information. **Scope of the decision requested:** one customer segment, one onboarding path and one support queue.

### Scope and exclusions {#journey-kyc-scope-and-exclusions}

| Matter | Treatment in the pilot | Reason |
| --- | --- | --- |
| One customer segment and one onboarding path, named at Scoping; one support queue | Included | Small enough to measure |
| Service metadata: case state, completion status of required checks, document type and receipt status, approved customer-facing reason code, responsible queue, prior communications | Included | What the employee needs to explain the stall and ask once for what is missing |
| Source of the metadata | Included only through an approved view that carries the allowed fields and nothing else (to confirm at Scoping). Without it the journey stays in historical evaluation, with no first users | The boundary below must hold by design, not by instruction to the model |
| Information boundary | The assistant explains only an established service state and the next step that Onboarding/KYC permits | It does not infer or expose the reason for a regulated assessment |
| Contents and images of identity documents; analysts' free text | Excluded; no data path to the assistant | Not needed to explain the state; personal and restricted content |
| Customer risk scores, screening matches, suspicious-activity reports, other financial-crime information | Excluded; no data path to the assistant | Restricted information; disclosing or inferring it could harm the customer and breach the Bank's obligations |
| KYC and anti-money-laundering decisions, risk-rating changes, approval or rejection of the application | Excluded; Onboarding/KYC and compliance | Regulated decisions with their own authority |
| Skipping or shortening a required check | Excluded | The pilot does not change what the Bank requires of the customer |

### Process function and what it approves {#journey-kyc-process-function-and-what-it-approves}

| Item | For this journey |
| --- | --- |
| Process function (Dependency) | Onboarding/KYC: a Dependency of the Initiative, not a second Domain, unless it claims part of the benefit. Its specialists act as Domain Experts when the Domain Owner names them |
| What it approves | The service states in scope and the explanation of each; the allowed fields of the metadata view; the customer-facing reason codes and their wording; the action list (the information requests and next steps the assistant may propose); what counts as a stall and as a valid next step; the reading of the historical cases in the Evaluation set; the customer-facing onboarding procedure, kept apart from internal KYC policy, of which it is the knowledge-source owner noted in the AI Registry |
| First users | The onboarding support team, if it sits in Customer Service. If it sits in the onboarding function, the rule for a second Domain applies (see [Governance and roles](#governance)) |
| Control remits this journey adds | Compliance, for its financial-crime remit, accepts the information boundary and the allowed fields before it clears the business case. Compliance may raise the Risk Tier in this context; expected Risk Tier 2 holds only with the boundary in place |

### Baseline measures {#journey-kyc-baseline-measures}

Each baseline is a reference to its source, usually a management information (MI) report, taken in Discovery: Business case by the source owner; formulas and the comparison design are in the measurement annex on the [Initiative Brief](#charter) page.

| Measure | Use | Source reference |
| --- | --- | --- |
| Repeat contacts per eligible stalled case | Leading indicator: repeat contact | [MI report: contacts per stalled application, by segment and path] |
| Handling effort per eligible case | Leading indicator: handling effort | [Workforce report or case timestamps; timestamps to confirm] |
| Repeated or conflicting information requests | Journey indicator (Brief section 2) | [Quality review of onboarding cases] |
| Time from a stall to a valid next step | Supporting measure | [Onboarding system timestamps; whether stalls are timestamped is to confirm] |
| Handoffs between support, KYC and product teams | Supporting measure | [Onboarding or case system: transfers per application] |
| Abandoned applications, complaints and reopened cases | Control limit | [Onboarding system and complaints record] |

### Quality and control-limit criteria {#journey-kyc-quality-and-control-limit-criteria}

The journey values of the one acceptance rule on [Controls and evidence](#controls).

| Criterion | For this journey |
| --- | --- |
| State quality | At least 95% of sampled readings of stage, outstanding information, queue and next step correct in the Evaluation set, across the languages of the records (Russian, Kyrgyz, mixed). A proposed floor, confirmed with Onboarding/KYC after the baseline; it may be raised, not lowered |
| Critical errors | A restricted field or reason shown or implied; a request for information the process does not permit; a status that implies approval or rejection. None found in the Evaluation set; any one found blocks first use until corrected and retested |
| Boundary tests | Tests show that excluded fields and content have no path into the assistant's context, its records or its output, including attempts to inject them through free text |
| Traceability | Every check status, document status, queue, reason code and prior request shown links to its source record |
| Zero-tolerance events | A KYC or anti-money-laundering check skipped or altered; restricted information disclosed; different treatment of customer groups found by the bias and error test |
| Monitored limits | Abandoned applications, complaints and reopened cases do not get worse than the baseline by more than the agreed tolerance, overall and, where permitted, by customer group |

### Stop conditions {#journey-kyc-stop-conditions}

- A required check could be bypassed through the pilot.
- Restricted information could be disclosed or inferred.
- The service state cannot be shown reliably from the approved metadata view.
- Customers could receive inconsistent treatment.

### Expected volume {#journey-kyc-expected-volume}

Does one team see enough stalled applications on the chosen segment and path, within the observation period, for a claim on repeat contact? The figure is [MI report: stalled applications per month for the chosen segment and onboarding path]. It depends on the path and may be low. If it does not reach the sample that the measurement annex calculates, the customer outcome is directional evidence (an indication, not proof), and the decision after the MVP rests on repeated information requests, time to a valid next step and state quality, which a smaller sample can show. A comparison by customer group needs more cases than the overall claim; where the volume does not allow it, the bias and error test relies on the Evaluation set. A higher-volume path or a longer observation period is chosen at Scoping, not after the result.
