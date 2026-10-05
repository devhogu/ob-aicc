# Control Matrix

The Control Matrix keeps the state of every control of the Operating Model 8, by its reference: the latest evidence and the status. The rule, the owner, and the timing of a control are in the Operating Model 8, and its objective, type, and test are in the Unit governance guide. This Record is a living record. The AICC Lead updates it at each monthly Steering and at each Registry Snapshot, and a change of status is entered with its date. A control that is Open has an item in the Risks and Issues Record with an owner and a due date (Operating Model 8.2).

## 1. Status

The statuses have the meanings of the Operating Model 8.5, and the gap is stated in the entry.

| Status | Meaning |
| --- | --- |
| Operating | The control operated when it was due or triggered, and its evidence record is in the Registry and cited here |
| Open | The control is due, and its evidence is missing or incomplete; the gap is stated, and the Risks and Issues Record holds an item for it with an owner and a due date |
| Deficiency | The control did not operate, or its evidence shows a failure, or it was Open and was not corrected by its due date; it is entered as a deficiency in the Risks and Issues Record, and reviewed monthly until it is closed |
| No occurrence yet | The event that triggers the control has not happened; a nil statement says so |
| Not yet due | The first date of the control has not come |

## 2. The state of the controls

| Ref | Control | Latest evidence | Where kept | Status |
| --- | --- | --- | --- | --- |
| C-01 | The mandate of the Executive Sponsor, the appointment of the AICC Lead, and the naming of the AI Steering Committee | Appointments Record (AP-001 to AP-004); DR-2026-061; Steering Summary of 2026-09-02 (`steering/2026-09-02-first.md`) | Appointments Record Part A and C (`appointments.md`), with the decision reference | Operating: the appointments of 2026-09-02 are entered (DR-2026-061; Steering Summary 2026-09-02); the order of the Board that names the Executive Sponsor is not recorded; the AI Steering Committee is not formed, and the Executive Sponsor decides alone (Operating Model 4.5, 6.2); the missing appointments are made by 2026-12-01 (Operating Model 4.8; RI-005) |
| C-02 | Priorities, funding, and guardrails | DR-2026-061; Priorities Record (`priorities.md`); Steering Summary of 2026-09-02 (`steering/2026-09-02-first.md`) | Priorities (`priorities.md`); Decision Record | Operating: the Strategic Priorities were set on 2026-09-02 (DR-2026-061); no Envelope or Guardrail is set because no budget proposal was made; the yearly Steering of December 2026 sets them for the next year (Operating Model 6.5) |
| C-03 | The yearly review of the risk appetite and the policy | - | Decision Record (`decisions/`) | Not yet due: at the yearly Steering of December 2026 |
| C-04 | Review of the documents | DR-2026-062 and its dated corrections; DR-2026-063 approved baseline settlement; revision 2.1 correction rows in the affected documents | Decision Record of the check (`decisions/`) | Operating: the charter review is settled and the English baseline approved under DR-2026-063; operational actions remain in their own records |
| C-05 | Monthly review of progress, risks, and blockers, with a sample of the AICC Lead's Decisions | - | Steering Summary (`steering/`) | Not yet due: at the monthly Steering of the Iteration Review week of I10 (2026-10-26 to 2026-10-30) |
| C-06 | Results, risk check with the review of each Risk Tier 3 Solution, and Maturity Level | - | Quarterly Report, with the review of each Risk Tier 3 Solution (`reports/`); Registry Snapshot (`snapshots/`) | Not yet due: at the quarterly Steering of 2026-12-23 (IP week of 2026-PIQ4) |
| C-07 | Approval of the Quarterly Report, and its submission to the Board Committee or the Board where the Executive Sponsor decides | - | Quarterly Report with its approval block, and the submission where made (`reports/`) | Not yet due: at the quarterly Steering of 2026-12-23 (IP week of 2026-PIQ4) |
| C-08 | Service Agreement for an Engagement | RI-004; status corrected 2026-10-03 under Operating Model 8.5 | Service Agreement (`initiatives/INI-nnn/`); Portfolio Backlog | Deficiency (2026-10-03): the studies of INI-002, INI-003, INI-004, INI-006, INI-007, and INI-008 run, and no Service Agreement is issued (RI-004); the preventive control did not operate |
| C-09 | Approval of the business case, and the decision after the MVP | - | Initiative Brief complete in its six sections, with the clearances of the Control Function Contacts; Decision Record; Decision Log entry | No occurrence yet: no business case is submitted for approval |
| C-10 | Outcome Report, acceptance, and confirmation of the benefit | - | Note of the acceptance in the backlog; the release block of the Solution Definition; Outcome Report (`initiatives/INI-nnn/`) | No occurrence yet: no Feature, Solution, or Engagement is accepted |
| C-11 | Benefit confirmed | - | Quarterly Report section 4 | Not yet due: at the quarterly Steering of 2026-12-23 (IP week of 2026-PIQ4) |
| C-12 | Risk Tier assignment | - | Solution Definition (`portfolio/en/solutions/`); AI Registry entry | No occurrence yet: SOL-001 is Proposed and no Solution is defined |
| C-13 | Check or validation before the first deployment | - | AI Registry entry for the check; Control Sign-Off (`sign-offs/`) | No occurrence yet |
| C-14 | Release | - | Release block of the Solution Definition; Acceptance Checklist (`checklists/`); Decision Record | No occurrence yet |
| C-15 | Approval of the use of a Solution for a data class, and training before first use | - | AI Registry, with who approved the use and when, and the completion of the training noted by the AICC Lead | Not yet due: the uses already in place are listed in the AI Registry within 90 days of the activation on 2026-10-02 (AI Policy 2.1), by 2026-12-31; no use is approved for a data class |
| C-16 | An AI Incident, and the notice of a major one to the Board Committee | Nil statement in `risks-and-issues.md` | Risks and Issues; AI Incident Review (`incident-reviews/`); the ticket in Service Management, by reference; Decision Log entry of the notice to the Board Committee | No occurrence yet |
| C-17 | An Exception, a suspension, and a stop | - | Control Sign-Off for an Exception or a stop, or Decision Record for the AICC Lead; Decision Log entry for a suspension and its lifting; Risks and Issues | No occurrence yet |
| C-18 | Check of a provider | - | Control Sign-Off (`sign-offs/`) | No occurrence yet |
| C-19 | Sharing of data or decisions outside the Bank | - | Decision Record | No occurrence yet |
| C-20 | A Proposal to adopt a Solution at scale, the yearly Proposal of the AI adoption strategy, and the quarterly review of the Adopted Solutions | - | Proposal (`proposals/`); Decision Record; Quarterly Report | Not yet due: the yearly Proposal is at the yearly Steering of December 2026; no Solution is ready to be adopted |
| C-21 | Output published to investors, lenders, regulators, or the Board | - | Decision Record of the approval | No occurrence yet: no output is issued |
| C-22 | Separation of duties and independence | Appointments Record Part A, B, and C; RI-001 | Appointments Record Part A and B; the Acceptance Checklist or the release block | Operating: no appointer appoints themselves (Operating Model 4.6); the Roles that one person holds are accepted limits with compensating controls (RI-001, RI-003) |
| C-23 | Intake of Engagements and the limit on work in progress | - | Service Agreement; Portfolio Backlog | Not yet due: no Initiative is Active and no Service Agreement is issued, and the AICC Lead sets the limit on the Active Initiatives, within the mix, before an Initiative is pulled to its MVP (Portfolio Management Model 5.4); initial portfolio and Team limits are now recorded in the Kanban boards under DR-2026-063 |
| C-24 | Completeness of the Outcome Reports | - | Steering Summary | Not yet due: at the quarterly Steering of 2026-12-23 (IP week of 2026-PIQ4) |
| C-25 | Access of internal audit | - | Appointments Record Part E | Not yet due: the contact of internal audit is not named (RI-005), and is entered in Part E within 60 days of the activation on 2026-10-02 (Operating Model 4.8), by 2026-12-01 |
| C-26 | Access review of the Registry, the tools, and production | - | Steering Summary | Not yet due: at the quarterly Steering of 2026-12-23 (IP week of 2026-PIQ4) |
| C-27 | Acceptance of a risk beyond the appetite | - | Decision Record (`decisions/`); the report to the Board Committee | No occurrence yet |
| C-28 | Reassessment of the Risk Tier and expiry of a validation | - | AI Registry; Control Sign-Off (`sign-offs/`) | No occurrence yet: no date of a reassessment or a validation is in the AI Registry |
| C-29 | Review of live Solutions | - | Solution Definition (`portfolio/en/solutions/`) | No occurrence yet: no Solution is live |
| C-30 | Deployment to production, and change to a released Solution | - | The Feature with its change ticket and test reference; Solution Definition; Decision Log | No occurrence yet |
| C-31 | Retirement of a Solution | - | Solution Definition; AI Registry | No occurrence yet |
| C-32 | Deficiencies and findings | RI-004, reclassified 2026-10-03 | Risks and Issues; Steering Summary | Open: the C-08 deficiency is recorded with its owner; its remediation due date still needs to be set, and the monthly review is due at the I10 Steering |

## 3. Populations for sampling

| Population | Where | Items to date |
| --- | --- | --- |
| Decisions | `decision-log.md` | 4 entries (DR-2026-060 to DR-2026-063); read the status and any dated correction of each |
| Initiatives | `portfolio-backlog.md` | 10: six in Discovery and four Approved Standing Initiatives (DR-2026-063) |
| Solution Definitions | `portfolio/en/solutions/` | 1 (SOL-001, Proposed) |
| Steering Summaries | `steering/` | 1 (2026-09-02, first) |
| Acceptance Checklists | `checklists/` | 0 |
| Control Sign-Offs | `sign-offs/` | 0 |
| AI Incident Reviews | `incident-reviews/` | 0 |
| Exceptions | `risks-and-issues.md` | 0 |
| Registry Snapshots | `snapshots/` | 0 |
| Service Agreements | `initiatives/` | 0 |
| Outcome Reports | `initiatives/` | 0 |
| Appointments | `appointments.md` Part C | 5 entries (AP-001 to AP-005) |
| AI uses in the AI Registry | `ai-registry.md` | 1 (AICC drafting assistant; tolerated existing use, not approved) |
