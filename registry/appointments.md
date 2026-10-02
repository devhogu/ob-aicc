# Appointments

This is the Appointments Record, in the form of the Appointments Record Template. It maps the Roles of the charter to real people. It is the Record that names the Holders of the Roles, and it holds their names and posts, and their declarations, consents, and access, and no other personal data. Part C is append-only. One person may hold several Roles; each is in its own row. The names live here and not in the charter. A bracketed comment states what is expected in an open place.

## Part A. The map

| Role | Scope | Holder (name and post) | Deputy | Status | From | To | Appointed by | Decision reference (DR-[yyyy]-[nnn], or the number and date of the order) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Executive Sponsor | The Bank | Simen Munter, Chief Executive Officer of the Bank | [ A deputy named by the Executive Sponsor ] | Appointed | [ The date of the mandate ] | | The Board (AICC Charter 3.1) | [ The decision or order of the mandate of AICC: its number, date, and issuer ] |
| AICC Lead | AICC | Timur Alimbayev, head of AICC | [ A deputy named by the AICC Lead ] | Appointed | [ The date of the appointment ] | | Executive Sponsor | [ The decision or order of the appointment: its number, date, and issuer ] |
| Solution Engineer | AICC | Timur Alimbayev, head of AICC | [ A deputy named by the AICC Lead ] | Appointed | [ The date of the appointment ] | | [ The Executive Sponsor, because the AICC Lead may not appoint their own person to a Role (Operating Model 4.6, 5.7) ] | [ The decision reference ] |
| Platform Owner | The AI Platform | [ The person who owns the platform AICC runs on, named when a platform is in use ] | | | | | Head of technology | |
| Domain Owner | FP&A | Ademi Moldogazieva, head of the FP&A function | | Appointed | [ The date ] | | The head of the Domain, by Operating Model 4.6; the Executive Sponsor confirmed it with INI-004 | [ The decision reference ] |
| Domain Owner | Other Domains | [ The head of the function that owns the Domain, named at the start of an Engagement ] | | | | | The head of the Domain | |
| Domain Expert | Each Domain | [ The practitioner the Domain Owner names to work with the Team ] | | | | | Domain Owner | |

The Executive Sponsor names the members of the AI Steering Committee (Operating Model 4.6), the heads of the functions, when the Committee convenes. Until then the Executive Sponsor decides alone (Operating Model 6.2).

| Function | Holder | Deputy | Status | From | To | Decision reference (DR-[yyyy]-[nnn], or the number and date of the order) |
| --- | --- | --- | --- | --- | --- | --- |
| Business | [ The head of the function ] | | | | | |
| Technology | [ The head of the function ] | | | | | |
| Risk | [ The head of the function ] | | | | | |
| Compliance | [ The head of the function ] | | | | | |

The Control Function Contacts. Each Control Function names its Contact.

| Control Function | Remit | Control Function Contact | Named by | Deputy | Status | From | To | Decision reference (DR-[yyyy]-[nnn], or the number and date of the order) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model risk | Risk Tier and model validation, including language models | [ The contact named by the function ] | | [ The deputy named by the function ] | | | | |
| Compliance | Regulation, conduct, consumer protection, and anti-money-laundering rules of the Bank | [ The contact named by the function ] | | [ The deputy named by the function ] | | | | |
| Information security | Security requirements, access, and attacks specific to AI | [ The contact named by the function ] | | [ The deputy named by the function ] | | | | |
| Data protection | Lawful use of personal data, retention, cross-border transfer, sharing outside the Bank | [ The contact named by the function ] | | [ The deputy named by the function ] | | | | |
| Legal | Contracts, intellectual property, partners, and liability | [ The contact named by the function ] | | [ The deputy named by the function ] | | | | |

Internal audit gives assurance only.

| Function | Contact | Named by | Status | From | To | Decision reference (DR-[yyyy]-[nnn], or the number and date of the order) |
| --- | --- | --- | --- | --- | --- | --- |
| Internal audit, with read access to every Record | [ The named contact of internal audit ] | | | | | |

**Checkers.** The Checker of a Risk Tier 1 Solution, whom the AICC Lead names, is entered for each Solution (Operating Model 4.4(e)).

| Solution | Name | Named by | Date | Decision reference (DR-[yyyy]-[nnn], or the number and date of the order) |
| --- | --- | --- | --- | --- |
| [ SOL-nnn: a person who did not build the Solution ] | [ name and post ] | AICC Lead | [ date ] | [ decision reference ] |

**Product owners.** While the Team has up to three people the AICC Lead is its product owner (Solution Lifecycle Model 7.3), and no entry is needed. When the AICC Lead names another person for a Team, the person is entered here.

| Team | Name | Named by | Date | Decision reference (DR-[yyyy]-[nnn], or the number and date of the order) |
| --- | --- | --- | --- | --- |
| [ Team, when another person than the AICC Lead is named ] | [ name and post ] | AICC Lead | [ date ] | [ decision reference ] |

## Part B. The responsibilities

The RACI of the charter is in the Organization guide. Role combinations that the rules of separation forbid are accepted limits, and each is listed in the Risks and Issues with its compensating control.

| Accepted limit | Risks and Issues | Compensating control |
| --- | --- | --- |
| The AICC Lead issues the Service Agreement, delivers, and writes the Outcome Report | RI-023 | The Domain Owner, or the Executive Sponsor for enabling work, accepts the Outcome Report, and the Steering samples the Decisions of the AICC Lead each month |
| The AICC Lead accepts the Features and the Capabilities, and gives the final acceptance of the Team, for a Solution that the AICC Lead built | RI-033 | The test by a person other than the builder, the check or the validation by another person, the acceptance of the Domain Owner, the release decision, and the monthly sample of the Decisions of the AICC Lead by the Executive Sponsor |
| [ Another combination, if one is accepted: the Roles, the reason, and the compensating control ] | | |

## Part C. The appointment log

| Entry | Date entered | Event | Role | Person | Effective from and to | Decided by | Decision reference (DR-[yyyy]-[nnn], or the number and date of the order) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AP-001 | [ The date entered, within five working days of the event ] | Confirmed | [ Each Role in Part A, one entry for each ] | | | | [ The decision reference ] |

## Part D. Declarations and competence

| Holder | Role accepted (date) | Conflict declaration (date, outcome) | Training required and completed | Line manager's consent and time allocation |
| --- | --- | --- | --- | --- |
| Timur Alimbayev | [ The date ] | [ The date and the outcome ] | [ The training that the Roles need, set by the AICC Lead ] | Not applicable: the Holder is the head of AICC |
| [ Every other Holder in Part A, once named ] | | | | [ Where the Holder stays in their own line: the consent of the line manager and the time allocation ] |

## Part E. Tools and access

| Role | Jira, Confluence, and Service Management group | Repository permission | Access granted or removed (date) | Last access review (date and reviewer) |
| --- | --- | --- | --- | --- |
| AICC Lead and Solution Engineer | [ The group, entered when the tool is deployed ] | [ The permission ] | [ The date ] | [ The date and the reviewer ] |
| Internal audit | [ Read-only access to Jira, Confluence, and Service Management ] | Read | [ The date ] | [ The date and the reviewer ] |

| Tool | Keeper (Role and name) | From | To |
| --- | --- | --- | --- |
| Jira, Confluence, Service Management | [ The Role that keeps each tool, named when the tool is deployed ] | | |
| The Registry repository | AICC Lead | | |
| The portals | [ The Role that keeps each portal ] | | |

## Delegations of the Executive Sponsor

In writing, for a stated scope and period. A delegation of more than two weeks is also entered in the Decision Log (Operating Model 4.7).

| Scope | Delegate | From | To | Decision reference (DR-[yyyy]-[nnn], or the number and date of the order) |
| --- | --- | --- | --- | --- |
| [ A delegation, if one is made: its scope, delegate, period, and decision reference ] | | | | |
