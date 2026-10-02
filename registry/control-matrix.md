# Control Matrix

The Control Matrix keeps the state of every control of the Operating Model 8, by its reference: the latest evidence and the status. The rule, the owner, and the timing of a control are in the Operating Model 8, and its objective, type, and test are in the Unit governance guide. This Record is a living record. The AICC Lead updates it at each monthly Steering and at each Registry Snapshot, and a change of status is entered with its date. A control that is Open has an item in the Risks and Issues Record with an owner and a due date (Operating Model 8.2).

## 1. Status

| Status | Meaning |
| --- | --- |
| Operating | The control has operated, and the latest evidence is cited |
| Open | The control is due or in force, and its evidence is missing or incomplete; the gap is stated, and the Risks and Issues Record holds an item for it |
| Deficiency | An Open control that is not corrected; it is entered as a Deficiency in the Risks and Issues Record, and reviewed monthly until it is closed |
| No occurrence yet | The event that triggers the control has not happened; a nil statement says so |
| Not yet due | The control is periodic, and its first occurrence has not been reached |

## 2. The state of the controls

| Ref | Control | Latest evidence | Where kept | Status |
| --- | --- | --- | --- | --- |
| C-01 | The mandate of the Executive Sponsor, the appointment of the AICC Lead, and the naming of the AI Steering Committee | None | Appointments Record Part A and C (`appointments.md`), with the decision reference | Open: the references are not entered (RI-021), and the AI Steering Committee is not formed (RI-008) |
| C-02 | Priorities, funding, and guardrails | None | Priorities (`priorities.md`); Decision Record | Open: the Guardrails, the Envelopes, and the mix of Initiatives are not set (RI-012) |
| C-03 | The yearly review of the risk appetite and the policy | DR-2026-018 (activation; the appetite part revised by DR-2026-055) | Decision Record (`decisions/`) | Not yet due: the first yearly review is at the yearly Steering of December 2026 (DR-2026-057), and the Executive Sponsor has not yet decided the AI Risk Appetite Statement (RI-032) |
| C-04 | Review of the documents | DR-2026-055 (consistency review of the pack, 2026-10-02); DR-2026-053 (the ten questions for three documents) | Decision Record of the check (`decisions/`); assessments | Open: the result of the ten questions for the six other documents revised on 2026-10-02 is not recorded (RI-029) |
| C-05 | Monthly review of progress, risks, and blockers, with a sample of the AICC Lead's Decisions | `steering/2026-09-steering.md` | Steering Summary (`steering/`) | Open: the one record is reconstructed and records no sample (RI-024) |
| C-06 | Results, risk check with the review of each Risk Tier 3 Solution, and Maturity Level | None | Quarterly Report, with the review of each Risk Tier 3 Solution (`reports/`); Registry Snapshot (`snapshots/`) | Not yet due: first at the close of 2026-PIQ4 |
| C-07 | Report to the Board Committee | None | Quarterly Report as issued to the Board Committee, with its issuance block (`reports/`) | Not yet due; the Board Committee is not named (RI-010) |
| C-08 | Service Agreement for an Engagement | None | Service Agreement (`initiatives/INI-nnn/`); Portfolio Backlog | Open: not issued for INI-002, 003, 004, 006, 007, 008 (RI-022) |
| C-09 | Approval of the business case, and the decision after the MVP | None; the Exception for INI-001 is DR-2026-054 | Initiative Brief complete in its six sections, with the clearances of the Control Function Contacts; Decision Record; Decision Log entry | Open: INI-001 is Active in development mode without the approval of its business case, as an Exception that the Executive Sponsor has not ratified (DR-2026-054, RI-031); the other Initiatives are in Scoping |
| C-10 | Outcome Report, acceptance, and confirmation of the benefit | None | Note of the acceptance in the backlog; the release block of the Solution Definition; Outcome Report (`initiatives/INI-nnn/`) | Open: no acceptance note for the Closed Features (RI-028) |
| C-11 | Capacity used and benefit confirmed | None | Quarterly Report section 4 | Not yet due |
| C-12 | Risk Tier assignment | None | Solution Definition (`portfolio/solutions/`); AI Registry entry | Not yet due: SOL-001 is Proposed |
| C-13 | Check or validation before the first deployment | None | AI Registry entry for the check; Control Sign-Off (`sign-offs/`) | No occurrence yet |
| C-14 | Release | None | Release block of the Solution Definition; Acceptance Checklist (`checklists/`); Decision Record | No occurrence yet |
| C-15 | Approval of the use of a Solution for a data class, and training before first use | None | AI Registry, with who approved the use and when, and the completion of the training noted by the AICC Lead | Open: no use is approved for any data class (RI-019) |
| C-16 | An AI Incident, and the notice of a major one to the Board Committee | Nil statement in `risks-and-issues.md` | Risks and Issues; AI Incident Review (`incident-reviews/`); the ticket in Service Management, by reference; Decision Log entry of the notice to the Board Committee | No occurrence yet |
| C-17 | An Exception, a suspension, and a stop | DR-2026-054 (an Exception of the AICC Lead); RI-031 | Control Sign-Off for an Exception or a stop, or Decision Record for the AICC Lead; Decision Log entry for a suspension and its lifting; Risks and Issues | Open: the Exception for INI-001 is not ratified, and its monthly review is not yet recorded (RI-031, RI-027); no suspension or stop has occurred |
| C-18 | Check of a provider | None | Control Sign-Off (`sign-offs/`) | No occurrence yet |
| C-19 | Sharing of data or decisions outside the Bank | None | Decision Record | No occurrence yet |
| C-20 | A Proposal to adopt a Solution at scale, the yearly Proposal of the AI adoption strategy, and the quarterly review of the Adopted Solutions | None | Proposal (`proposals/`); Decision Record; Quarterly Report | Not yet due: the first yearly Proposal is at the yearly Steering of December 2026; no Solution is ready to be adopted |
| C-21 | Output published to investors, lenders, regulators, or the Board | None | Decision Record of the approval | No occurrence yet: the first edition of INI-004 is not issued |
| C-22 | Separation of duties and independence | RI-023 | Appointments Record Part A and B; the Acceptance Checklist or the release block | Open: the Appointments Record is incomplete (RI-021, RI-023) |
| C-23 | Capacity ceiling and intake of Engagements | None | Service Agreement; Portfolio Backlog; Teams | Open: the capacity is not stated (`teams.md`; RI-025) |
| C-24 | Completeness of the Outcome Reports | None | Steering Summary | Not yet due |
| C-25 | Access of internal audit | None | Appointments Record Part E | Open: the audit contact is not named (RI-026) |
| C-26 | Access review of the Registry, the tools, and production | None | Steering Summary | Not yet due |
| C-27 | Acceptance of a risk beyond the appetite | None | Decision Record (`decisions/`); the report to the Board Committee | No occurrence yet |
| C-28 | Reassessment of the Risk Tier and expiry of a validation | None | AI Registry; Control Sign-Off (`sign-offs/`) | Not yet due |
| C-29 | Review of live Solutions | None | Solution Definition (`portfolio/solutions/`) | Not yet due |
| C-30 | Deployment to production, and change to a released Solution | None | The Feature with its change ticket and test reference; Solution Definition; Decision Log | No occurrence yet |
| C-31 | Retirement of a Solution | None | Solution Definition; AI Registry | No occurrence yet |
| C-32 | Deficiencies and findings | None | Risks and Issues; Steering Summary | Open: the monthly review is not yet recorded (RI-027) |

## 3. Populations for sampling

| Population | Where | Items to date |
| --- | --- | --- |
| Decisions | `decision-log.md` | 55 |
| Steering Summaries | `steering/` | 1, reconstructed |
| Acceptance Checklists | `checklists/` | 0 |
| Control Sign-Offs | `sign-offs/` | 0 |
| AI Incident Reviews | `incident-reviews/` | 0 |
| Exceptions | `risks-and-issues.md` | 1 (RI-031, DR-2026-054) |
| Registry Snapshots | `snapshots/` | 0; the first is due at the close of I10 |
| Service Agreements | `initiatives/` | 0 |
| Outcome Reports | `initiatives/` | 0 |
| Appointments | `appointments.md` Part C | 0 entries |
| Solutions in the AI Registry | `ai-registry.md` | 0 |
