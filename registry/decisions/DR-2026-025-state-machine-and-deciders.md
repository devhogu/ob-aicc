# DR-2026-025 One transition table, deciders, and the Solution lifecycle

Date: 2026-10-01. Decided by the AICC Lead, after the independent check of the new hierarchy (registry/assessments/2026-10-01).

## Decision

1. The Operating Model 6.4 is the only table of the moves between the states. Waiting can come from discovery, approved, or active, and returns to where it came from. A Solution that must return to discovery does so from active. Rejected applies only before approval and Cancelled after it. A suspension is a flag, a stop by a Control Function cancels, and retirement closes.
2. The person who approves an item at its level also defers, rejects, cancels, or pivots it. The AICC Lead approves Epics, the Team approves Features at IT Planning, the Domain Owner approves a Solution Definition, and the Domain Owner and the Executive Sponsor approve an Initiative as before.
3. A split Feature is Pivoted and linked to two Features: the part done, which goes to review, and the rest in the next Program Increment.
4. A Solution is delivered when its first deployment is released. The Initiative completes when its Solutions are delivered and its outcome is reviewed. A Solution is Active until the end of its life and is Closed when retired, handed off, or ended.
5. The check or validation attaches to the Solution, is taken in Verify of the first Feature that reaches real users or data, and the release is recorded in the Solution Definition.
6. An Experiment may have no Receiver yet. At the end of its time-box it goes to review.
7. Enabling work is accepted by the Executive Sponsor. Every Initiative has an Initiative Brief.
8. Until Jira and Confluence run the work, the Registry is the live state. After that, Jira and Confluence hold the live state, and the Registry holds the records and the snapshots.

## Revisit

At the first PI Planning, in the IP week of 2026-PIQ4.
