# Delivery measures: definitions and formulas

The course states what delivery measures and why. This page states the measures themselves: the definition, the formula where there is one, the source, where it is read, and the rule for its target. It is the reference for the boards, the Dashboard, and the records of the events, and for the live portal that will show them. The measures that the Solution Lifecycle Model defines are marked as such; the others are the standard measures of lean flow, software delivery, and service operation, stated here and proposed for the Solution Lifecycle Model 10.

## 1. Conventions

1.1. A measure has a definition, a source, a place where it is read, and a target that the Team sets with the product owner once it has a baseline. Time is counted in calendar days unless stated. Measures of flow are read as distributions and trends: the median and the eighty-fifth percentile say more than the mean. A figure of the Bank stays in its source system. No measure is used to rank people. In light mode cycle time runs from Active to Review, and Verify and Deploy are read from the check record and the change ticket.

## 2. Flow measures

| Measure | Definition | Formula | Source | Read at | Target rule | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Work in progress | The Features and Capabilities that are Active | Count of items in state Active, per column, lane, and Domain | Program Kanban | Weekly Review | At or below the limit set by the Team | Charter |
| Age of work in progress | How long each Active item has been Active | Today minus the date it became Active; the oldest per column | Program Kanban | Weekly Review | An item older than the 85th percentile of its column is raised | Charter |
| Cycle time | Days from Active to Completed, or to Review in light mode | Date Completed minus date Active | Program Kanban | Weekly Review | Median and 85th percentile per item type and lane | Charter |
| Lead time | Days from Approved to Accepted | Date Accepted minus date Approved | Program Kanban | Iteration Review and Demo; quarterly Steering | Median and 85th percentile; the measure the function feels | Charter |
| Throughput | The Features accepted in an Iteration | Count of Features reaching Accepted in the Iteration | Iteration Review and Demo | Iteration Review and Demo | A trend | Charter |
| Expected lead time | The lead time the system produces at the current load | Average work in progress divided by average throughput (Little's law) | Derived | Weekly Review | Used to set the limits | Proposed |
| Flow efficiency | The share of lead time in which an item is worked on | Active working days divided by lead time, as a percentage | Program Kanban; Waiting flags | Iteration Review and Demo | A trend; low values show waiting | Proposed |
| Waiting time | The days an item is Waiting on a Dependency | Sum of days in Waiting per item; count of Waiting items | Program Kanban | Weekly Review | Every Waiting item names its Dependency and owner | Charter |
| Items by lane | The work by class of service | Count of Active items per lane: Urgent, High priority, Normal | Program Kanban | Weekly Review | Urgent is rare; a rising share is a signal | Charter |
| Ready ahead | Readiness for the next Iteration | Features Ready, in Iterations of work ahead | Program Backlog | Backlog Refinement; Iteration Planning | One to two Iterations | Charter, in part |
| Dependency timeliness | Dependencies met by the date needed | Dependencies Met by date divided by Dependencies due, as a percentage | Program Board | PI Review and Demo | A trend; an At risk Dependency is raised at once | Charter |

## 3. Quality measures

| Measure | Definition | Formula | Source | Read at | Target rule | Status |
| --- | --- | --- | --- | --- | --- | --- |
| First-time-right rate | The share of items that meet the Verify or the Review at the first attempt | Items passed first time divided by items presented, at the test and at the acceptance | Test records; acceptances | Weekly Review; Iteration Review and Demo | A trend; a fall is a problem for the Retrospective | Charter |
| Items returned | Items returned at the test or at the acceptance | Count per Iteration, by reason | Test records; acceptances | Iteration Review and Demo | A trend by reason | Charter |
| Defects after the check | Defects found in operation after the check or validation | Count per Solution per period | Service Management; AI Registry | Iteration Review and Demo | A trend per Solution; feeds the reassessment of the Risk Tier | Charter |
| Change failure rate | Deployments and changes rolled back or causing an incident | Failed deployments divided by deployments, as a percentage | Change tickets; incidents | Iteration Review and Demo | A trend; the measure of safe deployment | Charter |
| Deployment frequency | How often Features reach their environment of use | Deployments per Iteration, per Solution | Change tickets | Iteration Review and Demo | A trend; small and frequent is the aim | Proposed |
| Lead time for a change | Days from a Feature becoming Active to its deployment | Date deployed minus date Active | Program Kanban; change tickets | Iteration Review and Demo | Median; read with cycle time | Proposed |
| Acceptance Checklist items not met | Items not met at the release decision | Count per release | Acceptance Checklist | Release | Zero: an item not met stops the release | Charter |
| Time from Completed to Accepted | How long an item waits for acceptance | Date Accepted minus date Completed | Program Kanban | Iteration Review and Demo | Within the Iteration | Charter |

## 4. Service measures of a live Solution

| Measure | Definition | Formula | Source | Read at | Target rule | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Availability | The share of the agreed service time during which the Solution is available | Available time divided by agreed service time, as a percentage | Monitoring | Iteration Review and Demo | The target of the Service Agreement | Charter |
| Incidents | Incidents by severity, and repeat incidents | Count by severity per period; repeats as a share | Incident management | Iteration Review and Demo | A trend; a repeat is a problem for problem management | Charter |
| Time to restore | From the detection of an incident to the restoration of the service | Time restored minus time detected; median and worst | Incident management | Iteration Review and Demo | The target of the Service Agreement | Charter |
| Response and resolution time | From a request to its first answer, and to its closure, against the target of its class | Time of first answer minus time of request; time closed minus time of request | Service Management | Iteration Review and Demo | The targets of the Service Agreement per class, as targets not guarantees | Charter |
| Requests within target | The share of requests handled within the target of their class | Requests within target divided by requests, as a percentage | Service Management | Iteration Review and Demo | The target of the Service Agreement | Charter |
| Adoption | The share of the intended users or cases served | Users or cases served divided by intended, as a percentage | The Solution | Live review; quarterly Steering | Set in the brief | Proposed form |
| Override and correction rate | The share of AI outputs that a person overrides or corrects, against the baseline | Outputs overridden or corrected divided by outputs produced | The Solution's log | Live review | Read with acceptance; both very high and very low are signals | Charter |
| Run cost | The cost of operating the Service: run, licenses, provider costs | As recorded by the Domain | Financial planning | Quarterly Steering | Paid from the Envelope; the sunset rule applies when it exceeds the benefit | Charter |
| Lead time of a change | Days from a change raised to its deployment, for a live Solution | Date deployed minus date raised | Program Kanban; change tickets | Iteration Review and Demo | A trend; the health of change | Charter |
| Retirements complete | Access removed, data handled, registry entry marked | Checklist complete at closure | Solution Definition; AI Registry | When the Solution is retired | Complete before Closed | Charter |

## 5. Value and predictability

| Measure | Definition | Formula | Source | Read at | Target rule | Status |
| --- | --- | --- | --- | --- | --- | --- |
| PI predictability | The share of the PI Objectives achieved of those planned, with the business value scored | Business value achieved divided by business value planned for the Program Increment, as a percentage | PI Objectives | PI Review and Demo | A trend without a target; read as a band, since the objectives are intent and not a promise | Charter |
| Features accepted against selected | The share of the Iteration's selection that was accepted | Features accepted divided by Features selected at Iteration Planning | Iteration Backlog | Iteration Review and Demo | A trend; a steady gap shows the selection is too large | Charter |
| Key results of the Initiative | The leading indicators of the Initiative Brief | Progress as (current minus baseline) divided by (target minus baseline) | The source system named in the brief | End of the MVP; quarterly Steering | Two to four per Initiative; the measure of the Portfolio | Charter |
| Benefit confirmed | The benefit the Domain Owner confirms | As confirmed at the Outcome Report and each quarter | Outcome Report; Quarterly Report | Quarterly Steering | Against the benefit claimed and the Envelope | Charter |

## 6. How the measures are kept

6.1. Each measure has one owner for its definition, the AICC Lead, and one source. A measure is added or changed by a decision at the monthly Steering and recorded; a measure that nobody reads for two quarters is removed. The definitions of the Solution Lifecycle Model prevail over this page where they differ; the proposed measures become rules when the model is revised from the baseline by a decision record.

## 7. Rule source

Solution Lifecycle Model 10; AI Competence Center Charter 7.1; Statement of Intent 11.3; Portfolio Management Model 9; Business Model 4.2.
