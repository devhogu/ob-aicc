# Accounting & financial close

Accounting and financial close is the month-end and quarter-end discipline that produces the Bank's authoritative financial record — from journal posting and accruals through consolidation, reconciliation, and the trial balance that feeds management reporting and external filings. The close cycle is governed by a fixed task calendar, a hierarchy of approvals, and IFRS-based accounting standards as adopted under the applicable regulatory framework. Close quality determines the accuracy of every downstream report: management accounts, regulatory returns, and statutory financial statements all start from the same ledger. **The GenAI opportunity is automating the mechanical elements of the close cycle — status monitoring, exception identification, reconciliation matching, and narrative drafting — so Controllers focus on judgment and audit-readiness.**

## Problems

### Period-end close {#period-end-close}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Close progress — task completion by owner, outstanding approvals, and items at risk of missing the publication deadline — is tracked in shared spreadsheets updated manually by individual team members. The Controller assembles an end-of-day status update each close day by chasing owners by phone and email rather than reading from a live tracking system. |
| Enablement | Close analysts spend a significant share of close-week time on mechanical data assembly — pulling system exports, reformatting tables, and populating templates — before any analytical judgment is applied. The tools available to a typical Controller team were designed for data capture, not for exception-surfacing or anomaly detection during the close. |
| Automation | The close task calendar, approval workflow, reminder escalations, and end-of-day status reporting are all manual coordination activities that follow a predictable pattern each cycle. The task structure is known; the coordination overhead is the constraint. Each month-end cycle consumes an estimated 20–40 coordination hours above the core accounting work. |
| New business opportunities | Banks that close faster — and with higher first-time accuracy — have more time between close completion and the external filing deadline for management review, audit committee discussion, and disclosure quality checking. A compressed close cycle is also a competitive signal: investors and rating agencies note consistent on-time, accurate filings. |

## Close task management {#close-task-management}

Month-end and quarter-end close involves 80–150 discrete tasks — journal postings, accrual approvals, sub-ledger locks, and system sign-offs — coordinated across Controllers, segment Finance teams, and shared service centers within a fixed publication window. The Controller tracks task completion, escalates delays, and produces end-of-day status reports for the CFO throughout the close period.

### Close Critical Path Monitoring

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/close-task-management/close-critical-path-monitoring
- Lens: Insights
- Complexity: S
- Intent: The AI agent identifies the close task dependencies that constitute the critical path to the publication deadline, monitors completion status of critical-path tasks in real time, and alerts the Controller when a delay on a critical-path task threatens the publication window before the impact propagates to downstream tasks.
- Problem to solve: The close task calendar records individual task status but does not model the dependency chain that determines which tasks constitute the critical path to publication. Controllers identify critical-path delays when a downstream task reports it is waiting on an upstream output — by which point the available recovery time has already compressed.
- Solution: The AI agent reads the close task calendar with declared dependencies and the current completion status of each task. It constructs the dependency network, identifies the critical path from current status to the publication deadline, and monitors critical-path task completion in real time. When a critical-path task falls behind schedule, the AI agent issues an alert to the Controller with the downstream cascade impact — which subsequent tasks are affected, by how long the publication window is compressed, and which team owns each affected task. The Controller reviews and determines the recovery action.
- OKR: The Controller receives an alert when a delay on a critical-path close task threatens the publication window — the downstream tasks affected, the compression of the window, and the team that owns each task — before the impact propagates.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-maintained dependency network and critical-path monitoring active for ≥10 of 12 monthly close cycles in year 1; all close tasks with declared dependencies covered. |
| Acceptance | ≥80% of critical-path alerts confirmed by the Controller as genuine threats to the publication window; ≥90% of critical-path delays alerted before a downstream task reports that it is waiting. |
| Cycle | Critical-path delay alerted within 1 hour of the task falling behind schedule, vs. identification only when a downstream task reports waiting in the prior process. |

### Close Exception Escalation

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/close-task-management/close-exception-escalation
- Lens: Automation
- Complexity: S
- Intent: The AI agent monitors the end-of-day close status report for tasks that remain open beyond their scheduled completion time, drafts escalation messages to the relevant team lead with the task context and downstream impact, and updates the Controller's status log automatically.
- Problem to solve: End-of-day close status reports identify open tasks but require the Controller to manually compose escalation messages to each responsible team lead — an activity that repeats each evening throughout the close period and consumes Controller capacity that should be applied to judgment-intensive oversight rather than communication logistics.
- Solution: The AI agent reads the current close task status against the scheduled completion calendar each evening. For each task that is open beyond its scheduled time, it drafts an escalation message to the responsible team lead, including the task description, the hours overdue, and the downstream tasks that depend on the output. The Controller reviews the drafts and releases them for dispatch; no escalation is sent without Controller review. The AI agent also updates the status log entry for each affected task with the escalation timestamp and reason.
- OKR: The Controller receives, each evening of the close period, drafted escalation messages for every task open beyond its scheduled completion time — task description, hours overdue, and dependent downstream tasks — ready to review and release, with the status log updated.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted escalations produced on ≥90% of close days in year 1; all tasks open beyond their scheduled time covered. |
| Acceptance | ≥85% of drafted escalations released by the Controller without material edit; status log entries confirmed accurate in ≥98% of sampled tasks. |
| Cycle | Escalation drafts ready within 30 minutes of the end-of-day status report, vs. manual composition by the Controller each evening in the prior process. |

### Month-End Close Management

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/close-task-management/month-end-close-management
- Lens: Automation
- Complexity: M
- Intent: The AI agent monitors month-end close task completion, surfaces a prioritized exception report of overdue items, runs GL-to-sub-ledger reconciliation matching, and drafts the close narrative for CFO review on the first day of reporting.
- Problem to solve: Month-end close involves 80–150 discrete tasks coordinated across Controllers, segment finance, and shared service centers within a fixed publication window. Tracking task completion, escalating delays, and reconciling GL balances to sub-ledger each consume significant Controller time during the close period; the close narrative is drafted after data is finalized, compressing the CFO's review window.
- Solution: The AI agent monitors the close task log and issues automated reminders to owners of items approaching their deadline, generates a real-time status report for the Controller, and runs GL-to-sub-ledger matching with unmatched items classified by materiality and age. On close completion, it drafts the close narrative from the finalized P&L and prior-period narrative as a style anchor. The Controller reviews task exceptions; the CFO edits the narrative draft before distribution.
- OKR: Month-end close task completion is monitored continuously, GL-to-sub-ledger reconciliation matching is automated with unmatched items classified by materiality, and the close narrative is available for CFO review on the first day of the reporting window.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-assisted close management used for ≥10 of 12 monthly close cycles in year 1; all material close tasks, GL-to-sub-ledger pairs, and narrative sections covered. |
| Acceptance | ≥85% of close narratives accepted by the CFO without material structural amendment; GL-to-sub-ledger unmatched item classification accuracy ≥90% on Controller review. |
| Cycle | Close narrative available on day 1 of the reporting window; Controller time on close coordination reduced by ≥30% vs. pre-deployment baseline. |

## GL-to-sub-ledger reconciliations {#gl-sub-ledger-reconciliations}

GL-to-sub-ledger reconciliation matches every general ledger balance to the underlying sub-ledger that supports it — loan sub-ledger to loan GL accounts, deposit sub-ledger to deposit GL accounts, fixed asset register to the balance sheet. Unexplained breaks indicate a posting error, system interface failure, or accounting judgment issue. Supervisors commonly expect the GL to be fully reconciled before regulatory returns are submitted.

### GL Reconciliation Break Triage

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/gl-sub-ledger-reconciliations/gl-reconciliation-break-triage
- Lens: Automation
- Complexity: S
- Intent: When GL-to-sub-ledger breaks are identified in the close cycle, the AI agent classifies each break by probable cause — timing difference, interface failure, posting error, or accounting judgment item — and routes each to the relevant resolution owner, reducing the manual triage time that precedes remediation.
- Problem to solve: GL-to-sub-ledger breaks surface at multiple points in the close cycle and are triaged manually by the Controllers team. Identifying whether a break reflects a known timing difference, a system interface failure, or a posting error requires the Controller to query the sub-ledger, the interface log, and the journal history for each item — a process that takes 30–60 minutes per break and serializes the remediation queue.
- Solution: The AI agent reads the current reconciliation output, the interface error log, the pending journal queue, and the known timing difference register. For each break it applies a classification logic — matching breaks against known timing patterns, interface error codes, and pending journals — and assigns each item to a classification category and resolution owner. The Controller reviews the triage output and confirms the classification before owners are notified. Items that cannot be classified are escalated to the Controller with the relevant system data attached.
- OKR: The Controller receives each GL-to-sub-ledger break classified by probable cause — timing difference, interface failure, posting error, or accounting judgment item — and assigned to a resolution owner, with unclassifiable items escalated with the relevant system data attached.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced triage applied to ≥90% of GL-to-sub-ledger breaks in ≥10 of 12 monthly close cycles in year 1. |
| Acceptance | ≥85% of classifications confirmed by the Controller without change; ≤10% of breaks escalated as unclassified. |
| Cycle | Triage output available within 1 hour of the reconciliation output, vs. 30–60 minutes of manual triage per break in the prior process. |

### GL Reconciliation Pattern Analysis

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/gl-sub-ledger-reconciliations/gl-reconciliation-pattern-analysis
- Lens: Insights
- Complexity: S
- Intent: The AI agent analyzes the rolling twelve-month history of GL-to-sub-ledger breaks by account, system interface, and break type to identify recurring patterns — accounts or interfaces that produce a disproportionate share of breaks — and surface root-cause candidates for the Controller's quarterly reconciliation quality review.
- Problem to solve: GL reconciliation breaks are resolved individually each close cycle without a systematic analysis of recurring patterns. Accounts or interfaces that produce the same type of break repeatedly indicate a systemic issue — an interface configuration problem, a flawed accounting rule, or a posting convention inconsistency — that persists because each individual break is resolved without the root cause being identified at the system level.
- Solution: The AI agent maintains a rolling twelve-month registry of GL reconciliation breaks by account, interface, and break type. Each close cycle it appends the new break data and runs a frequency and clustering analysis to identify accounts and interfaces that appear in the break registry consistently. The analysis is presented to the Controller at the quarterly reconciliation quality review — showing the top ten recurring break sources, estimated cumulative Controller time consumed per source, and candidate root-cause hypotheses for each. The Controller determines which root causes to investigate for permanent remediation.
- OKR: The Controller receives, for each quarterly reconciliation quality review, the top ten recurring sources of GL-to-sub-ledger breaks over the rolling twelve months, with the estimated Controller time consumed per source and candidate root-cause hypotheses.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-maintained break registry updated for ≥10 of 12 monthly close cycles and pattern analysis presented at ≥4 quarterly reconciliation quality reviews within year 1. |
| Acceptance | ≥70% of candidate root-cause hypotheses rated by the Controller as worth investigating; ≥50% of the top ten recurring sources selected for permanent remediation within two quarters. |
| Cycle | Recurring break sources surfaced each quarter, vs. breaks resolved individually each close cycle without pattern analysis in the prior process. |

### Pre-Submission GL Completeness Check

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/gl-sub-ledger-reconciliations/pre-submission-gl-completeness-check
- Lens: Automation
- Complexity: S
- Intent: Before regulatory returns are submitted, the AI agent verifies that the GL is fully reconciled to all material sub-ledgers — loan, deposit, fixed asset, and investment — and produces a reconciliation completeness certificate for the Controller's sign-off, meeting supervisory expectations.
- Problem to solve: The regulator expects the GL to be fully reconciled before regulatory returns are submitted. The reconciliation completeness check is performed manually by the Controllers team across multiple sub-ledger systems, and the sign-off is documented in a spreadsheet tracker. Missed or incorrectly closed items are identified during external audit or regulatory inspection rather than before submission.
- Solution: The AI agent reads the reconciliation status from each sub-ledger reconciliation system — loan, deposit, fixed asset, and investment — and checks that every material GL account has a matched and signed-off reconciliation. It produces a completeness matrix showing the reconciliation status of each account group against each sub-ledger, flagging unreconciled or open items with the break amount and responsible owner. The Controller reviews the matrix and signs off the completeness certificate before any regulatory return is submitted. The certificate is retained as evidence for external audit and regulatory inspection.
- OKR: The Controller receives, before any regulatory return is submitted, a completeness matrix showing the reconciliation status of every material GL account group against each sub-ledger, and signs off the completeness certificate on that basis.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced completeness matrix used before ≥95% of regulatory return submissions in year 1; loan, deposit, fixed asset, and investment sub-ledgers covered. |
| Acceptance | ≥90% of items flagged as unreconciled or open confirmed by the Controller as genuine; no unreconciled material account first identified by external audit or regulatory inspection after submission. |
| Cycle | Completeness matrix available within 2 hours of request, vs. a manual check across sub-ledger systems documented in a spreadsheet tracker in the prior process. |

## Close narrative & management commentary {#close-narrative}

The close narrative — a 3–5 page CFO commentary on the month's financial results — synthesizes P&L performance, variance attribution, one-time items, and capital and liquidity highlights for the executive committee and board. It is the first interpretive document produced from the close and sets the tone for the management discussion that follows in ALCO and segment reviews.

### Close Narrative Cross-Document Consistency

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/close-narrative/close-narrative-consistency-check
- Lens: Insights
- Complexity: S
- Intent: Before the close narrative is distributed, the AI agent cross-references every numerical figure in the draft against the authoritative source documents — management accounts, capital report, and liquidity report — and flags any inconsistency for CFO review.
- Problem to solve: The close narrative is drafted from multiple source documents and reviewed manually before distribution to the executive committee. Numerical inconsistencies between the narrative and the underlying reports — a NIM figure in the commentary that differs from the management accounts by a rounding error, or a capital ratio that does not match the formal capital report — are identified by the reader rather than by a systematic pre-distribution check.
- Solution: The AI agent reads the draft close narrative and the authoritative source documents. It extracts every numerical figure in the narrative, maps it to the corresponding source document entry, and checks for consistency across all figures. Discrepancies — including rounding differences, period mismatches, and figures that cannot be traced to a source — are presented to the CFO in a structured exception list before distribution. The CFO confirms each exception as intentional or directs a correction.
- OKR: The CFO receives, before the close narrative is distributed, a structured exception list of every numerical figure in the draft that is inconsistent with, or cannot be traced to, the management accounts, capital report, or liquidity report.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced consistency check run on ≥10 of 12 monthly close narratives in year 1; every numerical figure in each draft checked. |
| Acceptance | ≥85% of listed exceptions confirmed by the CFO as either intentional or requiring correction; no numerical inconsistency identified by readers after distribution in ≥95% of cycles. |
| Cycle | Exception list available within 1 hour of the draft narrative, vs. inconsistencies identified by the reader after distribution in the prior process. |

### Close Narrative Peer Benchmarking Context

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/close-narrative/close-narrative-peer-benchmarking
- Lens: Enablement
- Complexity: S
- Intent: The AI agent augments the CFO's draft close narrative with a peer context section — comparing the Bank's reported NIM, cost-to-income ratio, credit cost rate, and return on equity to the most recently published figures from peer institutions — to support the board's and investors' relative performance assessment.
- Problem to solve: The close narrative presents the Bank's performance in absolute terms and against budget. Board members and investor relations staff add peer context manually, drawing on published peer results from their own reading. The peer context section is produced inconsistently — present in some months, absent in others — and without a systematic check that the peer figures used are the most recently available.
- Solution: The AI agent reads the draft close narrative, identifies the key performance metrics reported — NIM, cost-to-income ratio, credit cost rate, and return on equity — and cross-references each against the most recently published equivalent figures from a defined peer set. It produces a peer context addendum for inclusion in the close narrative, noting the period covered by each peer figure and flagging any peer whose most recent publication is more than two quarters old. The CFO reviews the addendum and confirms the peer set and period before distribution.
- OKR: The CFO receives, with each close narrative, a peer context addendum comparing the Bank's NIM, cost-to-income ratio, credit cost rate, and return on equity with the most recently published figures of a defined peer set, with the period covered by each peer figure noted.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced peer context addendum included in ≥10 of 12 monthly close narratives in year 1; all four metrics and the full defined peer set covered. |
| Acceptance | ≥85% of addenda confirmed by the CFO without correction of the peer set or period; peer figures match the published sources in ≥98% of sampled entries. |
| Cycle | Peer context available with every close narrative, vs. produced manually in some months and absent in others in the prior process. |

### Close Narrative Drafting

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/close-narrative/close-narrative-drafting
- Lens: Automation
- Complexity: M
- Intent: The AI agent drafts the CFO monthly close narrative — P&L performance summary, variance attribution, one-time item schedule, and capital and liquidity highlights — from closed management accounts and prior narrative submissions as style anchors, available for CFO review on the day reporting completes.
- Problem to solve: The close narrative is drafted by the CFO's team from management accounts, the variance attribution pack, and the capital and liquidity reports — each arriving at different points in the close calendar. The drafting cycle begins only once all source documents are available, and the narrative is typically completed two to three days after the last source document is received, extending the executive committee's information wait.
- Solution: The AI agent reads the closed management accounts, the variance attribution output, the capital and liquidity position reports, and the three most recent approved close narratives as style anchors. It generates a full draft covering the CFO's standard commentary structure — consolidated P&L performance, segment commentary, variance attribution, one-time items, capital and liquidity highlights, and outlook framing — and formats it in the house template. The CFO reviews the draft and applies forward judgment and tone; the AI agent handles the assembly and initial drafting cycle.
- OKR: The CFO receives a full draft of the monthly close narrative — consolidated P&L performance, segment commentary, variance attribution, one-time items, capital and liquidity highlights, and outlook framing — in the house template on the day reporting completes.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted close narrative used for ≥10 of 12 monthly close cycles in year 1; all standard commentary sections covered. |
| Acceptance | ≥85% of drafts accepted by the CFO without material structural rewrite; figures in the draft reconcile to the closed management accounts in ≥98% of reviewed cycles. |
| Cycle | Draft available on the day the last source document is received, vs. two to three days later in the prior process. |

## Provisions & IFRS 9 close entries {#lending-default-close}

Under IFRS 9, the Bank computes expected credit loss across the full loan portfolio each close cycle — running the ECL model, booking the provision journal, and producing the stage migration analysis for disclosure. The quarter-end process feeds both the management P&L and the IFRS statutory financial statements, with external audit substantive testing focused on staging decisions and model inputs.

### ECL Model Run Validation

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/lending-default-close/ecl-model-run-validation
- Lens: Automation
- Complexity: S
- Intent: After the IFRS 9 ECL model run completes each close cycle, the AI agent validates the model output for completeness, sign coherence, and period-on-period movement reasonableness — flagging anomalies that warrant Controller review before the provision journal is booked.
- Problem to solve: The ECL model produces hundreds of output cells across portfolio segments and IFRS 9 stages. Anomalies in the model run — negative provisions, implausible stage migration ratios, or segment totals that do not reconcile to the portfolio aggregate — are identified through manual review by the Credit Modeling team and Controllers. The review takes one to two days and can delay the provision journal booking, compressing the remaining close window.
- Solution: The AI agent reads the ECL model output file as soon as the model run completes. It applies a structured validation — checking for non-negative provisions at the segment level, reconciling segment totals to the portfolio aggregate, testing period-on-period ECL movement against defined reasonableness bounds by segment, and checking that each portfolio segment has been processed and has a non-null stage distribution. Anomalies are presented to the Controllers team and Credit Modeling in a structured exception list with the relevant model output rows attached. The team confirms each exception before the provision journal is released.
- OKR: Controllers and Credit Modeling receive, as soon as each IFRS 9 ECL model run completes, a structured exception list of completeness, sign, reconciliation, and movement-reasonableness anomalies to confirm before the provision journal is released.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced validation applied to the ECL model run in ≥90% of close cycles in year 1; all portfolio segments and IFRS 9 stages checked. |
| Acceptance | ≥80% of listed anomalies confirmed by Controllers and Credit Modeling as warranting review; no provision journal corrected after booking for a model output anomaly in ≥95% of close cycles. |
| Cycle | Exception list available within 2 hours of model run completion, vs. one to two days of manual review in the prior process. |

### Provision Journal Audit Trail

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/lending-default-close/provision-journal-audit-trail
- Lens: Automation
- Complexity: S
- Intent: The AI agent generates a fully traced audit trail from the ECL model inputs through the provision calculation to the booked GL journal entries, structured for external auditor review and formatted to address the auditor's standard substantive testing questions for IFRS 9 close.
- Problem to solve: External auditors substantively test the IFRS 9 provision each quarter by tracing from GL journal entries back through the ECL model to the underlying data. Assembling the trace for each auditor request requires Controllers and Credit Modeling to retrieve and cross-reference data from the ECL model system, the journal posting system, and the provision register. Each auditor query takes one to two days to respond to, and the queries accumulate across the close period.
- Solution: The AI agent reads the ECL model input data snapshot, the model output, and the GL journal entries for the provision booking. It constructs a structured audit trail document — mapping each GL provision entry to the corresponding ECL model output cell, the input data used in the calculation, and the model methodology reference. The document is formatted to address the auditor's standard substantive testing questions for IFRS 9 close and is available at the start of the audit window. Controllers review the audit trail for accuracy before it is shared with the auditors.
- OKR: The external auditors receive, at the start of the audit window, a Controller-reviewed audit trail mapping each GL provision entry to its ECL model output cell, input data, and methodology reference, structured around their standard IFRS 9 substantive testing questions.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced audit trail prepared for ≥4 quarterly IFRS 9 closes within year 1; all provision journal entries traced. |
| Acceptance | ≥90% of audit trail documents released by Controllers without material correction; ≥70% of auditor trace queries on the provision answered from the document without a separate data retrieval. |
| Cycle | Audit trail available at the start of the audit window, vs. one to two days per auditor query in the prior process. |

### Stage Migration Analysis Drafting

- URN: urn:financial-services:scenario:finance-treasury/accounting-financial-close/lending-default-close/stage-migration-analysis-drafting
- Lens: Insights
- Complexity: M
- Intent: The AI agent produces the IFRS 9 stage migration analysis — showing flows between Stage 1, Stage 2, and Stage 3 by portfolio segment with driver attribution — from the ECL model output, providing the first quantified view of portfolio credit quality movement each close cycle.
- Problem to solve: The stage migration analysis required for IFRS 9 disclosure and external audit review is assembled manually from the ECL model output by the Credit Modeling and Finance teams. The analysis requires mapping each borrower's stage movement to a driver category — significant increase in credit risk, cure, write-off — and aggregating across the portfolio. Assembly takes two to three days and is one of the last close items completed, leaving the CFO without a credit quality movement view until late in the cycle.
- Solution: The AI agent reads the ECL model output with borrower-level stage assignments for the current and prior period. It constructs the stage migration matrix — flows between Stage 1, Stage 2, and Stage 3 by portfolio segment — and attributes each migration category to its primary driver from the model's input data. The migration analysis is available to Controllers and Credit Modeling on the day the ECL model run is validated. The teams review and add narrative commentary for the disclosure; the AI agent handles the structured migration table and quantitative driver attribution.
- OKR: Controllers and Credit Modeling receive the IFRS 9 stage migration matrix — flows between Stage 1, Stage 2, and Stage 3 by portfolio segment with quantitative driver attribution — on the day the ECL model run is validated.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced stage migration analysis used for ≥90% of close cycles in year 1; all portfolio segments covered. |
| Acceptance | ≥85% of migration tables accepted by Controllers and Credit Modeling without material restatement; migration flows reconcile to the ECL model stage assignments in ≥98% of reviewed cycles. |
| Cycle | Migration analysis available on the day the ECL model run is validated, vs. two to three days of manual assembly late in the close cycle in the prior process. |
