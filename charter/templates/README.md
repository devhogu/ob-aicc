# Templates

The forms of the records that AICC produces. A Template gives the form of a Record in the Registry or the Portfolio, and its rules are in the documents. The Document Catalog 6 lists them. Copy a Template from its title and omit the metadata block (Document Catalog 6.1). The Templates are in the order of use: an Initiative starts at the first and an Engagement ends at the eighth. The Appointments Record, the Registry Snapshot, the Quarterly Report, and the Proposal are used on their own cycle.

| Order | Id | Template | File | Used when | Kept in |
| --- | --- | --- | --- | --- | --- |
| 1 | AICC-TPL-02 | Initiative Brief | [initiative-brief.md](initiative-brief.md) | A need becomes an Initiative | `registry/initiatives/` |
| 2 | AICC-TPL-06 | Service Agreement | [service-agreement.md](service-agreement.md) | The study of an Engagement starts | `registry/initiatives/` |
| 3 | AICC-TPL-01 | Solution Definition | [solution-definition.md](solution-definition.md) | A Solution is defined | `portfolio/solutions/` |
| 4 | AICC-TPL-13 | Acceptance Checklist | [acceptance-checklist.md](acceptance-checklist.md) | AICC hands a ready Solution to a Domain for use at scale, before its release beyond the first users | `registry/checklists/` |
| 5 | AICC-TPL-03 | Control Sign-Off | [control-sign-off.md](control-sign-off.md) | A Control Function Contact validates, clears a business case, stops, checks a provider, or grants an Exception | `registry/sign-offs/` |
| 6 | AICC-TPL-08 | Decision Record | [decision-record.md](decision-record.md) | A Decision needs a record | `registry/decisions/` |
| 7 | AICC-TPL-04 | Steering Summary | [steering-summary.md](steering-summary.md) | Each Steering | `registry/steering/` |
| 8 | AICC-TPL-07 | Outcome Report | [outcome-report.md](outcome-report.md) | An Engagement ends | `registry/initiatives/` |
| 9 | AICC-TPL-10 | AI Incident Review | [ai-incident-review.md](ai-incident-review.md) | After the post-incident review of an AI Incident (AI Policy 5.8) | `registry/incident-reviews/` |
| 10 | AICC-TPL-11 | Registry Snapshot | [registry-snapshot.md](registry-snapshot.md) | The close of an Iteration and a PI, and at the cutover | `registry/snapshots/` |
| 11 | AICC-TPL-05 | Quarterly Report | [quarterly-report.md](quarterly-report.md) | Each quarter | `registry/reports/` |
| 12 | AICC-TPL-09 | Appointments Record | [appointments-record.md](appointments-record.md) | An appointment, acting designation, change, or relief | `registry/appointments.md` |
| 13 | AICC-TPL-12 | Proposal | [proposal.md](proposal.md) | A Solution is proposed for adoption at scale, and the yearly Proposal of the AI adoption strategy | `registry/proposals/` |

A Capability has no Template. It is a line in the Program Backlog. A Feature that needs more than a line in the Program Backlog has a short file in the folder of its Initiative, in the form of the Solution Lifecycle Model 3.3:

| Field | Entry |
| --- | --- |
| Identifier | FT-[nnn] |
| Capability | [the Capability that the Feature delivers] |
| Feature | For [the user], [the Feature]. We believe that it will [benefit] |
| Acceptance criteria | Given [situation], when [action], then [result that can be observed] |
| Dependencies | [on other items, functions, or persons] |
| Test reference | [reference of the test by a person other than the builder, Solution Lifecycle Model 7.1] |
| Change ticket key | [key of the change in the change management of the Bank, Solution Lifecycle Model 8.3] |
| Accepted by, and date | [the product owner, and the date, Solution Lifecycle Model 7.3(a)] |
