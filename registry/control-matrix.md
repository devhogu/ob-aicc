# Control Matrix

The Control Matrix keeps the state of every control of the Operating Model 8, by its reference: the latest evidence and the status. The rule, the owner, and the timing of a control are in the Operating Model 8, and its objective, type, and test are in the Unit governance guide. This Record is a living record. The AICC Lead updates it at each monthly Steering and at each Registry Snapshot, and a change of status is entered with its date.

## 1. Status

| Status | Meaning |
| --- | --- |
| Operating | The control has operated, and the latest evidence is cited |
| Open | The control is due or in force, and its evidence is missing or incomplete; the gap is stated |
| No occurrence yet | The event that triggers the control has not happened; a nil statement says so |
| Not yet due | The control is periodic, and its first occurrence has not been reached |

## 2. The state of the controls

| Ref | Control | Latest evidence | Where kept | Status |
| --- | --- | --- | --- | --- |
| C-01 | Mandate and appointment of the AICC Lead | None | Appointments Record Part A and C (`appointments.md`) | Open: the references are not entered (RI-021) |
| C-02 | Priorities, funding, and guardrails | Priorities set | Priorities (`priorities.md`); Decision Record | Open: the Guardrails and the Envelopes are not set (RI-012) |
| C-03 | Risk appetite and the policy | DR-2026-018 | Decision Record (`decisions/`) | Operating |
| C-04 | Review of the documents | DR-2026-034 | Decision Record of the check (`decisions/`); assessments | Operating |
| C-05 | Monthly review of progress, risks, and blockers, with a sample of the Decisions of the AICC Lead | `steering/2026-09-steering.md` | Steering Summary (`steering/`) | Open: the one record is reconstructed and records no sample |
| C-06 | Results, risk check, and Maturity Level | None | Quarterly Report (`reports/`); Registry Snapshot (`snapshots/`) | Not yet due: first at the close of 2026-PIQ4 |
| C-07 | Report to the Board Committee | None | Quarterly Report with its issuance block (`reports/`) | Not yet due; the Board Committee is not named (RI-010) |
| C-08 | Service Agreement for an Engagement | None | Service Agreement (`initiatives/INI-nnn/`); Portfolio Backlog | Open: not issued for INI-002, 003, 004, 006, 007, 008 (RI-022) |
| C-09 | Approval of the business case | None | Initiative Brief complete in its six sections; Decision Record | Not yet due: all Initiatives are in Scoping |
| C-10 | Outcome Report and acceptance | None | Outcome Report (`initiatives/INI-nnn/`) | Not yet due |
| C-11 | Capacity used and benefit confirmed | None | Quarterly Report section 4 | Not yet due |
| C-12 | Risk Tier assignment | None | Solution Definition (`portfolio/solutions/`); AI Registry | Not yet due: SOL-001 is Proposed |
| C-13 | Check or validation before the first deployment | None | AI Registry entry for the check; Control Sign-Off (`sign-offs/`) | No occurrence yet |
| C-14 | Release | None | Release block of the Solution Definition; Acceptance Checklist (`checklists/`); Decision Record | No occurrence yet |
| C-15 | Approval of the use of a Solution for a data class | None | AI Registry | Open: no use is approved for any data class (RI-019) |
| C-16 | AI Incident | Nil statement in `risks-and-issues.md` | Risks and Issues; AI Incident Review (`incident-reviews/`) | No occurrence yet |
| C-17 | Exception | Nil statement in `risks-and-issues.md` | Control Sign-Off or Decision Record; Risks and Issues | No occurrence yet |
| C-18 | Check of a provider | None | Control Sign-Off (`sign-offs/`) | No occurrence yet |
| C-19 | Sharing outside the Bank | None | Decision Record | No occurrence yet |
| C-20 | Proposal to adopt a Solution at scale | None | Proposal (`proposals/`); Decision Record | No occurrence yet |
| C-21 | Output published to the Board or investors | None | Decision Record of the approval | No occurrence yet: the first edition of INI-004 is not issued |
| C-22 | Separation of duties and independence | RI-023 | Appointments Record Part A and B | Open: the Appointments Record is incomplete |
| C-23 | Capacity ceiling and intake | None | Service Agreement; Portfolio Backlog; Teams | Open: the capacity is not stated (`teams.md`) |
| C-24 | Completeness of the Outcome Reports, and the sample of the Decisions of the AICC Lead | None | Steering Summary | Not yet due |
| C-25 | Confirmation of the benefit | None | Outcome Report | Not yet due |
| C-26 | Access of internal audit | None | Appointments Record Part E | Open: the audit contact is not named |

## 3. Populations for sampling

| Population | Where | Items to date |
| --- | --- | --- |
| Decisions | `decision-log.md` | 35 |
| Steering Summaries | `steering/` | 1, reconstructed |
| Acceptance Checklists | `checklists/` | 0 |
| Control Sign-Offs | `sign-offs/` | 0 |
| AI Incident Reviews | `incident-reviews/` | 0 |
| Exceptions | `risks-and-issues.md` | 0 |
| Registry Snapshots | `snapshots/` | 0; the first is due at the close of IT10 |
| Service Agreements | `initiatives/` | 0 |
| Outcome Reports | `initiatives/` | 0 |
| Appointments | `appointments.md` Part C | 0 entries |
| Solutions in the AI Registry | `ai-registry.md` | 0 |
