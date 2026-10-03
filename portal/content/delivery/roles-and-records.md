# Roles and records

Delivery is carried by a small number of Roles, each with a defined part, and it leaves records that let the Steering, the Control Functions, and the auditor see every acceptance, every check, and every release. This part states both, and where each step of the life of a Solution is controlled.

## 1. The roles in delivery

| Role | What it does in delivery |
| --- | --- |
| Solution Engineer | Designs, builds, verifies, and deploys the Solution with the Domain Expert; defines the architecture and the Solution Definition; builds the MVP; raises the change and deploys through the processes of the Bank; operates a Service that AICC runs; removes access and handles data at retirement |
| Domain Expert | The partner from the function who works with the Solution Engineer: the need, the cases, the evaluation set, the acceptance criteria in the words of the business |
| Product owner | Accepts each Feature and each Capability against its criteria at the Iteration Review and Demo; the AICC Lead while the Team has up to three people, later a person named in the Appointments Record |
| AICC Lead | Ranks the Program Backlog; keeps the Program Board and the Dashboard; sets the limit on the Active Initiatives; gives the final acceptance of the Team; decides whether a change needs a new check or validation; prepares the monthly Steering and writes the Quarterly Report |
| Domain Owner | Owns the outcome; names and trains the first users; judges and accepts the working Solution as the requester; reviews each live Solution at the Iteration Review and Demo; releases a Solution of Risk Tier 1 and 2 beyond its first users; approves its retirement |
| Checker | A person other than the builder who checks a Solution of Risk Tier 1 before its first real users |
| Control Function Contacts | Take part when a Solution of Risk Tier 2 or 3 is defined and in its validation; sign the Acceptance Checklist within their remit; may stop |
| Platform Owner | Provides the environments, the logging, the monitoring, and the traces on which the validation relies; operates the AI Platform of the Bank outside AICC |
| Executive Sponsor | Confirms the Roadmap and the PI Objectives at the quarterly Steering; releases a Risk Tier 3 Solution and a Solution that the AICC Lead built; accepts an item across Domains, enabling work, or an Experiment without a Domain; issues the Quarterly Report |

1.1. The separations that matter: the person who builds is not the person who tests; the person who checks or validates is not the builder; the person who accepts the Solution as the requester is not from AICC; and the person who releases is the one who owns the results. A small unit keeps them by role, and records the one limit it accepts while it is small.

## 2. The records

| Record | What it holds | Where |
| --- | --- | --- |
| Program Backlog and Iteration Backlogs | The Capabilities and the Features with their state, Stage, rank, criteria, Dependencies, acceptances | The Registry; the tracker |
| Program Board | The Features by Iteration, their state, their Dependencies and status, the Milestones | The Registry |
| Roadmap | The three horizons and the Milestones | The Registry |
| Dashboard | The state of the Program Increment, the flow, the Dependencies at risk, the risks, the Measures | The Registry |
| Calendar | The dates of the events, the blocked and gray days | The Registry |
| PI Objectives | The objectives of each Program Increment with their business value planned and scored | The Registry |
| Solution Definition | The Solution: need, scope, architecture and data, Risk Tier, acceptance criteria, check or validation, release block, life after delivery, live review notes | The Portfolio |
| Control Sign-Off | The decision of a Control Function Contact at a clearance or a validation | The Registry |
| Acceptance Checklist | The signed items of each party before release beyond the first users | The Registry |
| Change ticket and test reference | For each deployment, in the Feature and, for the first, in the release block | The change management of the Bank; the tracker |
| AI Incident Review | The review of an AI Incident | The Registry |
| Registry Snapshot | The closed extract at the close of each Iteration and Program Increment | The Registry |

## 3. Where each step is controlled

| Step | Decides | Evidence |
| --- | --- | --- |
| A Feature enters and is ranked | AICC Lead | Program Backlog |
| A Feature is selected | The Team at Iteration Planning | Iteration Backlog |
| A Feature is tested | A person other than the builder | The test result referenced in the Feature |
| A Solution is checked or validated | Checker, or Control Function Contacts | AI Registry entry; Control Sign-Off |
| A Feature is deployed | Change management of the Bank | Change ticket and test reference |
| A Feature is accepted | Product owner | The acceptance in the backlog |
| A Solution receives the Team's final acceptance | AICC Lead | Release block of the Solution Definition |
| A Solution is accepted by the requester | Domain Owner, or Executive Sponsor | Release block; Outcome Report |
| A Solution is released beyond its first users | Domain Owner, or Executive Sponsor | Acceptance Checklist; Decision Record for Risk Tier 3 |
| A live Solution is reviewed | Domain Owner, or Executive Sponsor | Live review note in the Solution Definition |
| A change is made | AICC Lead on the need for a new check; the releaser for a significant change | Decision Log; Feature; change ticket |
| A Solution is retired | Domain Owner, or Executive Sponsor | Solution Definition; AI Registry |

3.1. The controls that the Solution Lifecycle Model carries are listed in the Operating Model 8 and their status is kept in the Control Matrix of the Registry; the page Records and systems states where each record is kept.

## 4. Rule source

Solution Lifecycle Model 3.5, 7, 8, and 9; Operating Model 4 and 7; the templates of the Knowledge base.
