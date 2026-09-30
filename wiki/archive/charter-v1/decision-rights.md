```yaml
id: AICC-ORG-03-EN
title: Decision Rights
status: draft
revision: 0.8
created: 2026-09-29
revised: 2026-09-30
```

# Decision Rights

## 1. Purpose and scope

1.1. This document allocates responsibility and accountability for each decision and activity in the adoption of AI, from
Intake to Retirement of a Use Case.

1.2. The columns of the tables are the Roles defined in the Roles and Responsibilities and not Positions. The Register of
Appointments maps Positions and Holders to those Roles.

## 2. Notation

2.1. **R** denotes responsible: the Role that does the work. **A** denotes accountable: the Role that decides, of which
there is exactly one in each row. **A/R** denotes accountable and responsible. **C** denotes consulted before the decision.
**I** denotes informed after the decision.

2.2. The codes for the Roles are: **SP** Executive Sponsor; **SC** AI Steering Committee; **BC** Board Committee; **AL**
AICC Lead; **LA** Lead Architect; **PM** Portfolio Manager; **DL** Delivery Lead; **EC** Enablement Coach; **DO** Domain
Owner; **DE** Domain Expert; **SE** AI Solution Engineer; **CFC** Control Function Contact; and **PO** Platform Owner.

2.3. Where a row involves a Control Function, CFC denotes the Control Function Contact of each Control Function within its
own remit, for the Entity and the regulatory regime concerned. Each remit decides for itself. A Control Function Contact may
raise a Risk Tier within its remit, and only the Control Function Contact of model risk may lower it.

## 3. Rules

3.1. Validation, confirmation of the Risk Tier, and the stopping of a Use Case for a control breach are decided by the
Control Function Contacts. Neither AICC nor the Domain validates its own work.

3.2. Business acceptance and the funding of a Use Case are decided by the Domain Owner.

3.3. AICC directs the AI work of AI Solution Engineers through Functional Direction. It manages their employment only where
the AI Solution Engineer is assigned to AICC.

## 4. Allocation

### 4.1. Mandate and strategy

4.1.1. The allocation of mandate and strategy is as follows.

| Activity | SP | SC | BC | AL | LA | PM | DL | EC | DO | DE | SE | CFC | PO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set the yearly strategy, the Strategic Priorities, the Investment Envelopes, and the Investment Guardrails | A | R | I | R | C | R | I | I | C | I | I | C | C |
| Review each year, at the yearly session of the AI Steering Committee, the strategy, the Investment Envelopes, the Investment Guardrails, the roadmap, the Operating Model, the progress of the Evolution Plan, the AI Risk Appetite Statement, and the Corpus | A | R | I | R | I | C | I | I | C | I | I | C | I |
| Set the AI Risk Appetite Statement | A | R | I | R | I | I | I | I | C | I | I | C | C |
| Report to the Board Committee | A | C | I | R | I | C | I | I | I | I | I | I | I |

4.1.2. The Executive Sponsor decides the Strategic Priorities, the Investment Envelopes, and the Investment Guardrails on the
recommendation of the AI Steering Committee.

### 4.2. Portfolio Flow

4.2.1. The allocation of the activities of the Portfolio Flow is as follows.

| Activity | SP | SC | BC | AL | LA | PM | DL | EC | DO | DE | SE | CFC | PO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Take in a Use Case at Intake, and check its fit, size, and routing to the Control Functions | I | I | I | A | C | R | I | C | C | C | C | C | I |
| Assess benefits, cost, and risks at Discovery, and write an Initiative Brief where required | I | I | I | C | C | R | I | I | A | C | I | C | I |
| Approve an Initiative above the threshold set by the Investment Guardrails | I | A | I | R | I | R | I | I | C | I | I | C | I |
| Retire an Initiative | I | A | I | C | I | R | I | I | C | I | I | I | I |
| Rank the backlogs by value and urgency relative to effort | I | I | I | C | C | A/R | I | I | C | C | C | I | I |
| Confirm the priorities of the Portfolio each quarter | I | A | I | R | I | R | I | I | C | I | I | C | I |
| Agree that a Domain takes part, name the Domain Expert, and fund the Use Case | I | I | I | C | I | C | I | I | A/R | I | I | I | I |
| Secure an AI Solution Engineer for a Use Case, under one of the arrangements in the Operating Model | I | I | I | A/R | I | C | I | I | C | I | I | I | I |
| Define the technical Solution and approve its design against the Standards Record | I | I | I | C | A | I | I | I | I | C | R | C | C |
| Pilot the Solution in real work | I | I | I | I | C | C | I | C | A | R | R | C | I |
| Validate the Solution against control standards | I | I | I | I | I | I | I | I | C | C | C | A/R | C |
| Accept the Solution into use and decide its rollout across the Domain | I | I | I | I | I | C | I | I | A/R | C | C | I | I |
| Decide the release of a Risk Tier 4 Use Case after validation | I | A | I | C | C | C | I | I | R | I | I | C | I |
| Scale adoption and train colleagues in the Domain | I | I | I | I | I | I | I | C | A | R | C | I | I |
| Operate and improve a live Solution, including monitoring, AI Incidents, and drift | I | I | I | C | C | I | I | I | A | C | R | C | C |
| Stop a Use Case for a control breach | I | I | I | I | I | I | I | I | I | I | I | A/R | I |
| Retire a Use Case | I | I | I | C | I | R | I | I | A | I | C | C | C |

### 4.3. Way of working and cadence

4.3.1. The allocation of the way of working and the cadence is as follows.

| Activity | SP | SC | BC | AL | LA | PM | DL | EC | DO | DE | SE | CFC | PO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set the Stage policies, the Limits on Work in Progress, and the way of working | I | I | I | A | C | C | R | I | C | I | C | C | I |
| Keep the Portfolio Backlog, the Portfolio Roadmap, the Service Portfolio, the Decision Register, and the Benefits Register | I | I | I | C | C | A/R | C | I | C | I | I | I | I |
| Keep the Delivery Backlog, the Program Roadmap, the Roster, and the Risk and Issue Register | I | I | I | I | C | C | A/R | I | C | C | C | I | I |
| Keep the AI Incident Register and the Exception Register | I | I | I | A/R | C | I | I | I | I | I | C | C | I |
| Prepare and issue the Quarterly Report | I | I | I | A/R | C | R | R | I | I | I | I | C | C |
| Conduct the Quarterly Planning and Review Event, the Replenishment, and the Delivery Review | I | I | I | C | C | C | A/R | C | C | C | C | C | C |
| Track benefits and flow, score the value achieved with the Domain Owners, and report | I | I | I | A | I | R | R | C | C | C | C | I | I |

### 4.4. Standards, AI Platform, and enablement

4.4.1. The allocation of standards, the AI Platform, and enablement is as follows.

| Activity | SP | SC | BC | AL | LA | PM | DL | EC | DO | DE | SE | CFC | PO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set the architecture of Solutions, the technical standards, and the technical guardrails, and state in the Standards Record the requirements that the use of AI places on the AI Platform | I | C | I | C | A/R | C | C | C | I | I | C | C | C |
| Decide the Templates | I | I | I | A | C | C | C | R | C | I | I | C | I |
| Direct the AI work of AI Solution Engineers under Functional Direction | I | I | I | A | C | C | R | I | C | I | I | I | I |
| Provide and operate the AI Platform | I | I | I | C | C | I | I | I | I | I | C | C | A/R |
| Train and coach Domain Experts and AI Solution Engineers, conduct the Communities of Practice, and maintain training material and the portal | I | I | I | C | C | I | I | A/R | I | C | C | I | I |

### 4.5. Control and assurance

4.5.1. The allocation of control and assurance is as follows.

| Activity | SP | SC | BC | AL | LA | PM | DL | EC | DO | DE | SE | CFC | PO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Advise on control requirements and confirm the Risk Tier within each Control Function remit | I | I | I | I | C | C | I | I | C | C | C | A/R | I |
| Provide independent assurance over the Portfolio and AICC | I | I | I | I | I | I | I | I | I | I | I | A/R | I |
| Report an AI Incident to the regulator, providers, or customers where required | I | I | I | C | I | I | I | I | C | I | C | A/R | C |

### 4.6. People

4.6.1. The allocation of the activities concerning people and documents is as follows.

| Activity | SP | SC | BC | AL | LA | PM | DL | EC | DO | DE | SE | CFC | PO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Appoint the AICC Lead | A/R | C | I | I | I | I | I | I | I | I | I | I | I |
| Appoint Domain Experts and standing AI Solution Engineers for a Domain | I | I | I | C | I | I | I | C | A/R | I | I | I | I |
| Own and maintain the documents of the charter folder | I | I | I | A/R | C | C | C | C | I | I | I | I | I |
| Activate a document that the Document Catalog assigns to the Executive Sponsor | A | C | C | R | I | C | I | I | C | I | I | C | I |
| Activate a document that the Document Catalog assigns to the AICC Lead | I | I | I | A/R | C | C | C | C | I | I | I | I | I |
| Assess the documents of the charter folder and the corpus in accordance with the Corpus Assessment; the Portfolio Manager assesses the documents that the Delivery Lead wrote | I | I | I | C | I | R | A/R | I | I | I | I | C | I |
| Accept the readiness of the corpus | A | I | I | R | I | C | C | I | I | I | I | C | I |
| Decide a Group Arrangement | A | C | I | R | I | C | I | I | C | I | I | C | C |
| Grant an Exception to a control requirement | I | I | I | C | I | I | I | I | C | I | C | A/R | I |
| Grant an Exception to a requirement set by AICC | I | I | I | A/R | C | C | I | I | C | I | I | C | I |
| Keep the Register of Appointments | I | I | I | A | I | R | I | I | C | I | I | C | C |

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 0.4 | 2026-09-30 | Drafted. | none |
| 0.5 | 2026-09-30 | Document approval rows replaced by two activation rows; ownership row shortened. | none |
| 0.6 | 2026-09-30 | Iteration 2 of INI-001: F-072. | none |
| 0.7 | 2026-09-30 | Iteration 2 of INI-001: F-052. | none |
| 0.8 | 2026-09-30 | Iteration 3 of INI-001: F-009, F-011, F-041, F-042, F-050, F-051, F-056, F-065. | DR-2026-001, DR-2026-002, DR-2026-004 |
