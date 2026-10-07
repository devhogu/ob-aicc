---
key: "journey-payment"
label: "Payment Issue Resolution"
section: "Journey options"
---

## Payment Issue Resolution {#journey-payment-payment-issue-resolution}

Journey option for the INI-013 (Proposed; Portfolio Funnel). If selected at Scoping, it becomes the Charter: journey annex to the Initiative Brief (see [Journey options and selection](#journeys)). This page holds only what is specific to the journey; the common content is on the [Charter](#charter), [Governance and roles](#governance) and [Controls and evidence](#controls) pages, and the technical profile on [Journey technical profiles](#journey-profiles).

**Intent:** fewer repeat contacts about failed, pending or reversed payments, because the servicing employee sees one account of the payment state, the prior service history, the responsible owner and the approved next step, each linked to its source record. **Scope of the decision requested:** one domestic retail-payment type and one servicing queue.

### Scope and exclusions {#journey-payment-scope-and-exclusions}

| Matter | Treatment in the pilot | Reason |
| --- | --- | --- |
| One domestic retail-payment type, named at Scoping; one servicing queue | Included | Small enough to measure |
| Failed, pending and reversed states that the payment system records and for which an approved resolution step exists; related contacts, cases, investigation status and prior communications | Included | The history the employee rebuilds by hand today |
| Source of the payment state | Included only if the payment system has a read interface or an approved extract for the chosen type (to confirm at Scoping) | The state is never inferred from contact notes |
| Unrecognized payments, suspected fraud | Excluded; existing fraud process | Own investigation, customer rights and decision authority |
| Disputes and chargebacks | Excluded; existing dispute process | Card-scheme rules, legal deadlines and adjudication |
| Sanctions and anti-money-laundering holds | Excluded; compliance | Confidential regulated assessment |
| Cross-border and correspondent payments, including inbound remittances | Excluded for the first pilot, once contact volumes by payment type are checked at Scoping | Status may depend on other institutions; inbound remittances may be the largest category, so the exclusion is confirmed, not assumed |
| Reimbursement and compensation decisions | Excluded; existing decision owners | They decide the customer's entitlement |
| Moving, reversing or correcting funds | Excluded; the employee's existing transaction controls | The assistant holds no tools |

### Process function and what it approves {#journey-payment-process-function-and-what-it-approves}

| Item | For this journey |
| --- | --- |
| Process function (Dependency) | Payments Operations: a Dependency of the Initiative, not a second Domain, unless it claims part of the benefit. Its specialists act as Domain Experts when the Domain Owner names them |
| What it approves | The payment states in scope and the explanation of each; the action list (the next steps the assistant may propose per state); what counts as resolved and as a repeat contact for the same payment event; the reading of the historical cases in the Evaluation set; the payment-servicing procedure, of which it is the knowledge-source owner noted in the AI Registry |
| First users | The Customer Service team that handles contacts about the chosen payment type |
| Control remits this journey adds | None beyond the common list; compliance confirms which rules on payment information to customers apply |

### Baseline measures {#journey-payment-baseline-measures}

Each baseline is a reference to its source, usually a management information (MI) report, taken in Discovery: Business case by the source owner; formulas and the comparison design are in the measurement annex on the [Charter](#charter) page.

| Measure | Use | Source reference |
| --- | --- | --- |
| Repeat contacts for the same eligible payment event | Leading indicator: repeat contact | [MI report: repeat contacts per payment event, by payment type] |
| Investigation or handling effort per eligible case | Leading indicator: handling effort | [Workforce report or case timestamps; timestamps to confirm] |
| Time from first contact to confirmed resolution | Journey indicator (Brief section 2) | [Case system: contact and resolution dates; to confirm] |
| Transfers to Payments Operations | Supporting measure | [Case system: transfers per case] |
| Payment-service complaints and reopened cases | Control limit | [Complaints record and case system] |

### Quality and control-limit criteria {#journey-payment-quality-and-control-limit-criteria}

The journey values of the one acceptance rule on [Controls and evidence](#controls).

| Criterion | For this journey |
| --- | --- |
| State quality | At least 95% of sampled readings of payment state and next step correct in the Evaluation set, across the languages of the records (Russian, Kyrgyz, mixed). A proposed floor, confirmed with Payments Operations after the baseline; it may be raised, not lowered |
| Critical errors | A state shown that contradicts the payment system; a sign of fraud or dispute missed, so the case was not routed; a statement that funds will be returned without a recorded reversal. None found in the Evaluation set; any one found blocks first use until corrected and retested |
| Traceability | Every payment fact, status and prior action shown links to its source record |
| Zero-tolerance events | A fraud, dispute or sanctions case handled in the pilot instead of its own process; payment details disclosed to a person not entitled to them |
| Monitored limits | Complaints and reopened cases do not get worse than the baseline by more than the agreed tolerance |

### Stop conditions {#journey-payment-stop-conditions}

- The payment state of the chosen type cannot be established reliably from the payment system.
- Payments Operations cannot approve an action list for the states in scope.
- The workspace adds material effort for the employee compared with the existing process.
- A control limit above cannot be held.

### Expected volume {#journey-payment-expected-volume}

Does one team see enough eligible contacts of the chosen payment type, within the observation period, for a claim on repeat contact? The figure is [MI report: monthly eligible contacts for the chosen payment type in the pilot queue]. Of the three journeys this is the most likely to reach the sample that the measurement annex calculates; if it does, the repeat-contact indicator carries a target. If it does not, the customer outcome is directional evidence (an indication, not proof), and the decision after the MVP rests on effort, state quality and correct next step, which a smaller sample can show. A higher-volume payment type or a longer observation period is chosen at Scoping, not after the result.
