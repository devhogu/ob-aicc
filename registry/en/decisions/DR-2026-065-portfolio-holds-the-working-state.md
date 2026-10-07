# DR-2026-065 The Portfolio holds the working state

| Field | Entry |
| --- | --- |
| Identifier | DR-2026-065 |
| Title | The Portfolio holds the working state of the portfolio and the program; the Registry keeps governance and evidence; Jira runs the daily work |
| Date | 2026-10-07 |
| Type | Records and tooling: location and ownership of the working state |
| Level | Corpus and Records; operational decisions retain their existing owners |
| Decided by | AICC Lead, by the instruction recorded below |
| Status | Decided |

## 1. Facts

The Operating Model 7.1 kept the working state in the Registry until a cutover and then moved it to Jira. Jira is a runtime tool and an auditor does not accept it as persistent storage with full history. Initiatives, the Discovery catalog, and the projects carry much more than Jira and Confluence hold. The Registry mixed governance and evidence with the daily working state of the portfolio and the program.

## 2. Options

1. Keep the cutover: the working state moves to Jira, and the Registry keeps extracts.
2. Keep the working state of the portfolio and the program in the Portfolio as its persistent source of truth, from the Discovery catalog to delivery; keep governance and evidence in the Registry; let Jira run the daily work and mirror the portfolio and program levels.

## 3. Decision

The second option is adopted.

1. The Portfolio (`portfolio/`) holds the catalog of the Solutions and the Packages and the working state: the Discovery catalog, the Portfolio Backlog and Kanban with the Initiative Briefs, the Roadmap, the Program Backlog and Kanban, the Program Board, the Program Increments, the Calendar, the Teams, the Dashboard, and the register of the projects with their documents.
2. The Registry (`registry/`) keeps the living governance records, the Decision Log and Decision Records, the Steering Summaries, the reports, the Registry Snapshots, and the closed and dated evidence records.
3. Jira holds the Work Items of the Teams and a mirror of the Initiatives, Capabilities, and Features. The Portfolio owns identity, parent, rank, class of service, definitions, acceptance criteria, gate states, and their dates. A gate decision is recorded in the Portfolio and in the Registry first, and then in Jira. The progress of the Features is recorded from Jira in the Portfolio at each Weekly Review, and at once at a gate.
4. There is one Portfolio Backlog and Kanban and one Program Backlog and Kanban. The service area is a field of each item. Each item keeps one path; its state is a field with the date of each state.
5. The cutover is redefined: from it the Work Items of the Teams and the mirror run in Jira and Confluence; the working state of the portfolio and the program stays in the Portfolio.
6. The Portfolio is kept under the same rules as the Registry: a protected main branch, restricted visibility, history not rewritten, read access for internal audit, and the quarterly access review.

## 4. Authority and limits

This record captures the instruction of the AICC Lead as the owner of the Records and of the Operating Model (Operating Model 3). It changes where the working state is kept and who owns each field. It changes no state, rank, limit, decision, appointment, or commitment that is recorded today.

## 5. Instruction and evidence

The AICC Lead's instructions in the project conversation on 2026-10-07:

> since initiatves, discovery catalog, projects are much more than jira and confluence they need to be handled as sot elsewhere but actual daily runtime is handled in tooling

> lets do that and setup solid fondation in our repo for this runtime work running projects from discovery to delivery

The document changes and the move of the records are recorded with change C-PORTFOLIO-RUNTIME-STORE in repository history.

## 6. Review

| Field | Entry |
| --- | --- |
| Funding reference | None; no funding or procurement decision |
| Revisit | At the first Jira integration, or when the Discovery catalog moves into the Portfolio |
| Supersedes | The cutover of the working state of the portfolio and the program to Jira in Operating Model 7.1 revision 2.0; no operational decision is superseded |
