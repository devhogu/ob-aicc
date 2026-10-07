---
key: "start"
eyebrow: "INI-013 (Proposed; Portfolio Funnel) · Strategic Priority 1, customer intelligence"
lede: "An employee-assist pilot for one Customer Service team. When a customer comes back about an issue that is still unresolved, the employee sees one verified view of what has happened so far, with each fact linked to its source record, and a suggested next step from an approved list. The employee checks it, decides, and acts. The assistant moves no funds, takes no regulated decision, and sends nothing to a customer."
pills: ["Expected Risk Tier 2", "The assistant reads; the employee acts", "One journey, one team", "Model runs in the Bank", "Time-box: [AICC Lead's estimate, Iterations]"]
---

# Customer Intelligence–Enabled Service Resolution

## Status and the decision sought {#start-status-and-decision}

| Item | Entry |
| --- | --- |
| Status | INI-013 (Proposed; Portfolio Funnel). The AICC Lead takes it in at the Funnel. It is linked to INI-006, Customer experience intelligence, which studies front-office inefficiency across the Bank. This Initiative builds a case-level assistant for one team. |
| Client function | Customer Service, the only Domain. Its head is the Domain Owner. The process function of the chosen journey (Payments Operations, Disputes Operations, or Onboarding/KYC) is a Dependency. It approves the action list and supplies Domain Experts. |
| Decision sought now | The AICC Lead takes the idea in and selects one journey with the Domain Owner (Discovery: Scoping). |
| Decision sought next | The Domain Owner approves the business case in the [Charter (Initiative Brief)](#charter) once the Control Function Contacts have cleared it: model risk, information security, data protection, compliance, and legal. |
| Expected Risk Tier | 2. This depends on one condition: the model is an Assistant that holds no tools. It reads context and returns structured output, and every write is the employee's action in the workspace. |
| MVP and time-box | Phase 1 is an Experiment in the Lab, on read-only extracts of past cases. It ends in an Outcome Report. Phase 2 is a Service run by AICC with a sunset rule. One team uses it as first users, after validation, the Team's final acceptance, and the Bank's change management. Time-box: [AICC Lead's estimate, Iterations]. Effort and cost: [AICC Lead's estimate, by Role and phase]. |

## Expected value {#start-expected-value}

<!-- flow -->
- **Customer** One clear explanation and a resolution or a committed next step, without having to repeat the story.
- **Service team** Less time spent rebuilding a case by hand, fewer avoidable transfers, and process failures that become visible.
- **The Bank** Reusable components and evaluation sets for the next journey. Pilot outputs serve only service resolution and the evaluation of the assistant.

## Three journey options {#start-journey-options}

One journey is chosen at Scoping by the [selection rule](#journeys).

<!-- cards -->
- [Payment Issue Resolution · Lower complexity](#journey-payment): Failed, pending, or reversed domestic payments where the payment system shows the status and an approved resolution action exists.
- [Card Dispute Progress Support · Medium](#journey-dispute): Dispute stage, evidence still needed, deadlines, and what the employee may tell the customer about progress.
- [Onboarding/KYC Progress Support · Medium–high](#journey-kyc): Where an application stands and which information may be requested, behind a strict boundary around KYC and financial-crime data.

## Pages of this project {#start-pages}

<!-- cards -->
- [Charter (Initiative Brief)](#charter): The business case for the approver: hypothesis, leading indicators, MVP, cost, risks, and decisions, plus the measurement annex.
- [Governance and roles](#governance): The AICC path step by step, who decides, the RACI, workstreams, and where risks, decisions, and changes are recorded.
- [How the pilot works](#how-it-works): The problem, what is built, the case workflow, and what the employee can do.
- [Controls and evidence](#controls): Data and model hosting, Tier 2 obligations, and the single acceptance rule.
- [Technical design](#technical-design): Architecture, information paths, the workspace, and testing.
- [Journey technical profiles](#journey-profiles): The technical differences between the three journeys.
- [IT readiness checklist](#it-readiness): What the pilot asks of IT, the Dependencies, and the readiness evidence for each step.
