# Portfolio and service delivery workflow

## 1. Intent and scope

This workflow is the value stream of AICC from a business need to a retired solution. It follows the flow of the Scaled Agile Framework: a portfolio funnel that ends in a ranked backlog, the breakdown into capabilities and features, the execution in the Program Increments, and the continuous delivery pipeline. It covers the business scoping, the business case, the definition of the solution, its capabilities and features, the backlog, the execution, and the deployment, operation, and life cycle of what AICC delivers.

AICC is a lab. It defines and tries solutions with the functions, so that the Bank can decide on adoption at scale. Some solutions become services that AICC runs. Some are products built for one consumer. Some are experiments that end in a proposal, which another owner may adopt. AICC also oversees the adoption of solutions that others deliver.

The Engagement workflow sits on top of this one: it states the commitment to the function, and this workflow carries the work. The rules are in the Operating Model, the AI Policy, and the Vocabulary. This workflow shows the flow and the intent, and states no rule of its own. The events are those of the Cadence.

## 2. The levels

The work has six levels. Each level has its own backlog or board, its own stages, and its own horizon.

Figure 1 shows the levels and how each one is broken into the next.

```mermaid
flowchart TB
  T["Strategic Priority: a strategic theme set with the Board"] --> I["Initiative: a business program, long-term, held in the Portfolio Backlog"]
  I --> S["Solution: a solution or service, with a type, a Risk Tier, and a Receiver"]
  S --> E["Capability: a capability, runs over one or more PIs, held in the Program Backlog"]
  E --> F["Feature: closes within one PI, worked in the IT Backlog"]
  F --> W["Work Item: a task of the Team"]
```

Figure 1: the levels of the work.

| Level | Backlog or board | Horizon | Closes |
| --- | --- | --- | --- |
| Strategic Priority | Priorities | Years, reviewed yearly | Closed or cancelled by the Executive Sponsor |
| Initiative | Portfolio Backlog and Portfolio Kanban | Long-term | When its outcome is reviewed and accepted |
| Solution | The Portfolio | Per type | When its type ends |
| Capability | Program Backlog and Program Kanban | One or more PIs | When its Features are closed |
| Feature | Program Backlog, then IT Backlog | Within one PI | Within its PI, or split |
| Work Item | The Team board | Within the IT | With its Feature |

## 3. The states

Every item of every level has one of thirteen states, defined in the Vocabulary. A Stage is a phase of the work inside the discovery state or the active state.

Figure 2 shows how an item moves between the states. It follows the transition table of the Solution Lifecycle Model 4.1, which is the only source of the moves. Waiting returns to the state the item came from.

```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Discovery: taken in
  Proposed --> Rejected: decided against
  Proposed --> Deferred: on hold
  Discovery --> Approved: conditions met
  Discovery --> Waiting: Dependency
  Discovery --> Deferred: on hold
  Discovery --> Rejected: decided against
  Discovery --> Pivoted: rerouted
  Discovery --> Cancelled: no longer needed
  Approved --> Active: pulled
  Approved --> Waiting: Dependency
  Approved --> Deferred: on hold
  Approved --> Pivoted: rerouted
  Approved --> Cancelled: no longer needed
  Active --> Completed: work finished
  Active --> Waiting: Dependency
  Active --> Deferred: on hold
  Active --> Pivoted: rerouted
  Active --> Cancelled: no longer needed
  Active --> Discovery: Solution only, Risk Tier change
  Active --> Closed: Solution only, retired or handed off
  Waiting --> Active: Dependency cleared
  Waiting --> Deferred: will not clear
  Waiting --> Cancelled: no longer needed
  Deferred --> Proposed: taken up again
  Deferred --> Rejected: never approved
  Deferred --> Cancelled: no longer needed
  Completed --> Review: assessed
  Review --> Active: returned
  Review --> Accepted: criteria met
  Review --> Cancelled: outcome not wanted
  Accepted --> Closed: finished
  Closed --> [*]
  Pivoted --> [*]
  Rejected --> [*]
  Cancelled --> [*]
```

Figure 2: the states of an item.

## 4. The portfolio flow: from need to Initiative to Solution

The portfolio flow takes a need through the discovery stages of an Initiative and defines its Solutions. Each step ends in a decision that can approve, return, defer, or reject the item. The Portfolio Kanban holds the Initiatives.

| Step | Level and Stage | Intent | Who | Output |
| --- | --- | --- | --- | --- |
| Funnel | Initiative, proposed | Capture every idea or need from a function, from discovery work, or from AICC itself | Anyone; the AICC Lead keeps the funnel | An Initiative in the Portfolio Backlog |
| Business scoping | Initiative, discovery: Scoping | Scope the need with the function: the problem, the outcome wanted, the fit with the Strategic Priorities | AICC Lead with the Domain Owner | The scope |
| Business case | Initiative, discovery: Business case | State the hypothesis, the minimum scope, the benefit and how it is measured, the cost, and the risk | Domain Owner with the AICC Lead; the Executive Sponsor above a guardrail | The Initiative Brief; the Initiative is approved |
| Solution definition | Solution, discovery: Definition | Define each Solution: its type, its Receiver, its scope, its capabilities, its architecture, its data classes, and its Risk Tier | AICC Lead with the Domain Expert; the Domain Owner approves | The Solution Definition in the Portfolio; the AI Registry entry |
| Capabilities and features | Capability, discovery: Analysis; Feature, discovery: Explore and Design | Break the Solution into Capabilities and the Capabilities into Features, each with acceptance criteria and Dependencies | AICC Lead with the Domain Owner | Capabilities and Features in the Program Backlog; the Dependency Map |

## 5. The execution in the Program Increment

The execution takes the approved Features and builds them, on the loops of the Cadence. The Program Increment states intent and direction, and what is done in an IT is decided in that IT.

| Step | Event of the Cadence | Intent | Who | Output |
| --- | --- | --- | --- | --- |
| Set the intent | PI Planning | Choose the Capabilities and Features that the PI aims at, with their Dependencies | The Teams, the Domain Owners, the Executive Sponsor | The PI Objectives; the Roadmap |
| Select the Features | IT Planning | Select the Features for the month into the IT Backlog | The Team with the product owners | The IT Backlog |
| Develop | Weekly loops | Build the minimum solution with the function | Solution Engineer with the Domain Expert | Working increments |
| Verify | Before the first deployment | The check for Risk Tier 1; the validation by the Control Function Contacts for Risk Tier 2 and 3 | The Checker; the Control Function Contacts | The check, or the Control Sign-Off |
| Deploy | Weekly loops | Deploy the first Feature to the function, with training for the users, only after the check or the validation | Solution Engineer; the Platform Owner for the platform | A deployed Feature |
| Release | At the IT Review, or when ready | Decide that the Solution goes beyond its first users | Domain Owner; Executive Sponsor for Risk Tier 3 | The release, in the Solution Definition |
| Demonstrate and accept | IT Review and Demo | Show what works, and take the acceptance | Product owner | The acceptance, with who and when |
| Control the flow | Weekly Review | Keep the boards, the Limits, and the Dependencies under control | AICC Lead | The Dashboard |

A Feature closes within its Program Increment. A Feature that cannot close is split: the part that is done is a Feature that goes to review, and the rest is a new Feature in the next Program Increment. The original is Pivoted and linked to both. A Feature does not become approved until its Dependencies are known.

## 6. After delivery: three types of Solution

The offering type of a Solution, set in its definition, decides its life after delivery and who owns it. The Receiver is named in the Solution Definition before the Solution is approved.

Figure 3 shows the three lives.

```mermaid
flowchart LR
  D["Solution delivered"] --> SV
  D --> PR
  D --> EX
  subgraph SV["Service: AICC owns the whole life cycle"]
    direction LR
    S1["Operate"] --> S2["Evolve"] --> S3["Retire"]
    S2 -.new Capabilities and Features.-> S1
  end
  subgraph PR["Product: built for one consumer"]
    direction LR
    P1["Handover"] --> P2["Support on demand"] --> P3["Revise: a new version"] --> P4["Retire for the consumer"]
    P3 -.through the Portfolio Backlog.-> P1
  end
  subgraph EX["Experiment: time-boxed, no consumer"]
    direction LR
    X1["Trial"] --> X2["Proposal"] --> X3["Handover to the Receiver"]
    X3 -.AICC oversees.-> A["Adopted Solution"]
  end
```

Figure 3: the life of a Solution by type.

| Type | Owner after delivery | Stages | Rule | End |
| --- | --- | --- | --- | --- |
| Service | AICC | Operate, Evolve, Retire | A business case with the run cost and a sunset rule | Retired or cancelled |
| Product | The consumer owns the version; AICC supports on demand | Handover, Support, Revise, Retire for the consumer | A Product with many consumers or recurring requests becomes a Service through a business case | Retired for the consumer |
| Experiment | None yet | Trial, Proposal, Handover | Time-boxed to a stated number of ITs; the Handover is complete when the Receiver accepts it | Handed off, closed with its lessons, or cancelled |

Operation and support answer the requests of the users and the incidents, with the lane Urgent first. AICC reassesses the Risk Tier on a change and on its date in the AI Registry.

## 7. Oversight of the Adopted Solutions

AICC oversees the Adopted Solutions that others deliver, in the Portfolio, with their state, and reports on what was adopted and what works. The AI adoption strategy is a series of Proposals that AICC shapes from what it learns, and the Bank decides on them. This is the mission side of the lab.

## 8. Decisions along the stream

Who decides what along the stream is in the Operating Model 4.2 and 5.3, in the Solution Lifecycle Model 4 to 7, and in the AI Policy 2 and 3. This workflow states no decider of its own.

## 9. Where it runs

From the cutover of the working state (Operating Model 7.1) the stream runs in Jira and Confluence. The charter holds this schema, and the Registry and the Portfolio hold the records that an auditor may ask for. Jira stays clean: a few statuses, one flag, and one resolution, while the business states are in the charter and a field.

| Business state | Jira status |
| --- | --- |
| Proposed, discovery, deferred | Backlog |
| Approved | Ready |
| Active (waiting is a flag on the issue) | Active |
| Completed, review | Review |
| Accepted, closed, pivoted, rejected, cancelled | Done, with a resolution: Closed (for accepted and closed, the acceptance with who and when in a field), Pivoted, Rejected, or Cancelled |

| In the stream | In Jira and Confluence | Kept in the Registry or the Portfolio |
| --- | --- | --- |
| Initiative, Epic, Feature, Work Item | Initiative above Epic, Epic, a Feature issue type, and a sub-task. The Initiative level needs the edition of Jira that has it | The Initiative Brief; the Program Backlog at the close of the PI |
| The Stage and the exact business state of an item | Fields on the issue, where the five statuses are not enough to tell proposed, discovery, and deferred apart | The state and Stage in the snapshot |
| A Solution | A Confluence page for its Solution Definition, and a label or component on its Epics | The Solution Definition in the Portfolio |
| Waiting on a Dependency | A link between items and a flag on the issue | The Dependency Map at the close of the PI |
| Lanes | The priority of the issue: Urgent, High, Normal | Not kept |
| IT and PI | A Jira sprint for each IT, and a field for the PI | The Calendar |
| Solution definitions, notes, forms, and reports | Confluence pages and page templates | The Solution Definition, the decisions, the Control Sign-Offs, the incident records, and the Quarterly Report |
