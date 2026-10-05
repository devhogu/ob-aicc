# Delivery measures: definitions and formulas

The course states what delivery measures and why. This page states the measures themselves: the definition, the formula where there is one, the source, where it is read, and the rule for its target. It is the reference for the boards, the Dashboard, and the records of the events. The measures are those that the Solution Lifecycle Model 10.3 defines, with the leading indicators and the benefit of the Portfolio Management Model, given here with their formulas; the definitions of the models prevail where this page differs.

## 1. Conventions

1.1. A measure has a definition, a source, a place where it is read, and a target that the Team sets with the product owner once it has a baseline. Time is counted in calendar days unless stated. Measures of flow are read as distributions and trends: the median and the eighty-fifth percentile say more than the mean. A figure of the Bank stays in its source system. No measure is used to rank people. In light mode cycle time runs from Active to Review, and Verify and Deploy are read from the check record and the change ticket.

## 2. Flow measures

| Measure | Definition | Formula | Source | Read at | Target rule |
| --- | --- | --- | --- | --- | --- |
| Work in progress | The Features and Capabilities that are Active | Count of items in state Active, per column, lane, and Domain | Program Kanban | Weekly Review | At or below the limit set by the Team |
| Age of work in progress | How long each Active item has been Active | Today minus the date it became Active; the oldest per column | Program Kanban | Weekly Review | An item older than the 85th percentile of its column is raised |
| Cycle time | Days from Active to Completed, or to Review in light mode | Date Completed minus date Active | Program Kanban | Weekly Review | Set with the product owner once a baseline exists; read as the median and the 85th percentile per item type and lane |
| Lead time | Days from Approved to Accepted | Date Accepted minus date Approved | Program Kanban | Iteration Review and Demo; quarterly Steering | Set with the product owner once a baseline exists; read as the median and the 85th percentile; the measure the function feels |
| Throughput | The Features accepted in an Iteration | Count of Features reaching Accepted in the Iteration | Iteration Review and Demo | Iteration Review and Demo | A trend, with no target |
| Expected lead time | An estimate of the days from approval to acceptance for a stable flow of Features | Average approved Features not yet Accepted or otherwise closed divided by Features Accepted per calendar day over the same observation period (Little's law) | Program Kanban; approval and exit dates | Weekly Review | Read against the lead time; no target. Not available with zero throughput, an insufficient observation period, or material non-acceptance exits |
| Flow efficiency | The share of lead time in which an item is Active and not Waiting | Days Active and not Waiting divided by lead time, as a percentage | Program Kanban; Waiting flags | Weekly Review | Set once a baseline exists; low values show waiting |
| Waiting time | The days an item is Waiting on a Dependency | Sum of days in Waiting per item; count of Waiting items | Program Kanban | Weekly Review | Every Waiting item names its Dependency |
| Items by lane | The work by class of service | Count of Active items per lane: Urgent, High priority, Normal | Program Kanban | Weekly Review | Urgent is rare; a lasting rise is raised at the Iteration Retrospective |
| Ready ahead | Readiness for the next Iteration | Features Ready, in Iterations of work ahead | Program Backlog | Backlog Refinement; Iteration Planning | One to two Iterations |
| Dependency timeliness | Dependencies met by the date needed | Dependencies Met by date divided by Dependencies due, as a percentage | Program Board | PI Review and Demo | Set once a baseline exists; an At risk Dependency is raised to the monthly Steering |

2.1. For expected lead time, count only Features in the measured flow: from approval until acceptance or another terminal exit, including Ready, Completed, Review, Waiting, and returns or deferrals after approval. Do not add Capabilities to the count. Use the average count and the accepted Features per calendar day over the same period. For illustration, an average of four Features and two acceptances in 30 calendar days gives 4 / (2 / 30) = 60 calendar days. This is an estimate for a stable flow, not a completion promise.

## 3. Quality measures

| Measure | Definition | Formula | Source | Read at | Target rule |
| --- | --- | --- | --- | --- | --- |
| First-time-right rate | The share of items that pass the test in Verify or the acceptance at the Iteration Review at the first attempt | Items passed first time divided by items presented, at the test and at the acceptance | Test records; acceptances | Weekly Review; Iteration Review and Demo | Set once a baseline exists; a fall is a problem for the Retrospective |
| Items returned by reason | Items returned at the test in Verify or at the acceptance at the Iteration Review, counted by the reason entered | Count per Iteration, by reason | Test records; acceptances | Iteration Review and Demo | Set once a baseline exists; a repeated reason is raised at the Iteration Retrospective |
| Defects after the check | Defects found in operation after the check or validation | Count per Solution per period | Service Management; AI Registry | Iteration Review and Demo | Each one is read at the next reassessment of the Risk Tier |
| Change failure rate | Deployments and changes rolled back or causing an incident | Failed deployments divided by deployments, as a percentage | Change tickets; incidents | Iteration Review and Demo | Set in the Service Agreement; the measure of safe deployment |
| Deployment frequency | How often Features are deployed to production | Deployments to production per Iteration, per Solution | Change tickets | Iteration Review and Demo | A trend, with no target; small and frequent is the aim |
| Acceptance Checklist items not met | The items marked Not met in the Acceptance Checklists of the period | Count per release | Acceptance Checklist | Iteration Review and Demo | Each one stops the release |
| Time from Completed to Accepted | How long an item waits for acceptance | Date Accepted minus date Completed | Program Kanban | Iteration Review and Demo | Within the Iteration |

## 4. Service measures of a live Solution

| Measure | Definition | Formula | Source | Read at | Target rule |
| --- | --- | --- | --- | --- | --- |
| Availability | The share of the agreed service time during which the Solution is available | Available time divided by agreed service time, as a percentage | Monitoring | Iteration Review and Demo | The target of the Service Agreement |
| Incidents and repeats | Incidents by severity, and the share that repeat an earlier incident with the same cause | Count by severity per period; repeats as a share | Incident management | Iteration Review and Demo | A repeat is taken into problem management |
| Time to restore | From the detection of an incident to the restoration of the service | Time restored minus time detected; median and worst | Incident management | Iteration Review and Demo | The target of the Service Agreement |
| Response and resolution time | From a request to its first answer, and to its closure, against the target of its class | Time of first answer minus time of request; time closed minus time of request | Service Management | Iteration Review and Demo | The targets of the Service Agreement per class, as targets not guarantees |
| Requests within target | The share of requests handled within the target of their class | Requests within target divided by requests, as a percentage | Service Management | Iteration Review and Demo | Set once a baseline exists |
| Use | The users who use the Solution each week | Count of the users in the week | The Solution | Live review; quarterly Steering | A trend against the users stated in the Solution Definition |
| Human override and correction rate | The share of AI outputs that a person overrides or corrects, against the baseline | Outputs overridden or corrected divided by outputs produced | The Solution's log | Live review | A rate that is very high or very low is raised at the review of the live Solution |
| Run cost | The cost of running a Service in a period: run, licenses, provider costs, against the run cost of its business case | As read from its source | Financial planning | Live review; quarterly Steering | Paid from the Envelope; the sunset rule applies when it exceeds the benefit |
| Lead time of a change | Days from Active to the deployment to production of a Feature that changes a released Solution | Date deployed minus date Active | Program Kanban; change tickets | Iteration Review and Demo | Set once a baseline exists; the health of change |
| Retirements complete | The share of the retired Solutions whose access is removed, data handled, and AI Registry entry marked | Retired Solutions complete divided by retired Solutions | Solution Definition; AI Registry | When the Solution is retired | All, before Closed |

## 5. Value and predictability

| Measure | Definition | Formula | Source | Read at | Target rule |
| --- | --- | --- | --- | --- | --- |
| PI predictability | The business value achieved against the business value planned of the PI Objectives, as scored at the PI Planning and the PI Review and Demo | Business value achieved divided by business value planned, summed over the PI Objectives of the Program Increment, as a percentage | PI Objectives | PI Review and Demo | A trend without a target; read as a band, since the objectives are intent and not a promise |
| Features accepted against selected | The share of the Features selected at Iteration Planning that was accepted within that Iteration | Selected Features accepted within the Iteration divided by all Features selected at Planning; later admissions and their acceptances are shown separately | Iteration Backlog | Iteration Review and Demo | A steady gap shows over-selection and is raised at the Iteration Retrospective |
| Leading indicators of the Initiative | The two to four leading indicators of the Initiative Brief | Progress as (current minus baseline) divided by (target minus baseline) | The source system named in the brief | End of the MVP; quarterly Steering | Two to four per Initiative, each with its baseline before approval; the measure of the Portfolio |
| Benefit confirmed | The benefit the Domain Owner confirms | As confirmed at the Outcome Report and each quarter | Outcome Report; Quarterly Report | Quarterly Steering | Against the benefit claimed and the Envelope |

## 6. How the measures are kept

6.1. Each measure has one owner for its definition, the AICC Lead, and one source. The AICC Lead adds, changes, or removes a measure by a Decision taken at the monthly Steering and entered in the Decision Log, and removes a measure that is not read for two Program Increments (Solution Lifecycle Model 10.5). The definitions of the Solution Lifecycle Model prevail over this page where they differ.

## 7. Rule source

Solution Lifecycle Model 10; AICC Charter 7.1; Statement of Intent 11.3; Portfolio Management Model 9; Business Model 4.2.
