# Portfolio measures: definitions and formulas

The course states what the Portfolio measures and why. This page states the measures themselves, one by one, as lean and portfolio practice defines them: the definition, the formula where there is one, the source, where it is read, and the rule for its target. It is the reference for the Dashboard, the Steering Summary, and the Quarterly Report, and for the live portal that will show them. The measures that the charter defines are marked as such; the others are the standard measures of lean flow and portfolio economics, stated here and proposed for the Solution Lifecycle Model 10 and the AI Competence Center Charter 7.

## 1. Conventions

1.1. A measure has a definition, a source, a place where it is read, and a target that is set once there is a baseline. A figure of the Bank stays in its source system, and the record points to it. Time is counted in calendar days unless stated; a Program Increment is one quarter; an Iteration is one month. Measures of flow are read as distributions and trends, not as single numbers: the median and the eighty-fifth percentile say more than the mean. No measure is used to rank people.

## 2. Flow measures

| Measure | Definition | Formula | Source | Read at | Target rule | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Work in progress (WIP) | The Initiatives Active at one time; the items in each step of the Kanban | Count of Initiatives in state Active; count per step | Portfolio Backlog | Monthly Steering | At or below the limit on the Active Initiatives; the limit is set within the mix | Charter |
| Throughput | Initiatives accepted per Program Increment; Features accepted per Iteration | Count of items reaching Accepted in the period | Portfolio Backlog; Program Backlog | Quarterly Steering; Iteration Review and Demo | A trend; rises as WIP is held and blockers removed | Charter |
| Lead time | Days from Approved to Accepted for an Initiative | Date Accepted minus date Approved | Portfolio Backlog | Quarterly Steering | Median and 85th percentile; falls as WIP falls | Charter |
| Time to decision | Days from a proposal to its approval | Date Approved minus date Proposed | Portfolio Backlog | Monthly Steering | Median; an upper bound set by the Steering | Charter |
| Cycle time | Days from Active to Completed, or to Review in light mode | Date Completed minus date Active | Program Backlog; boards | Weekly Review | Median and 85th percentile per item type | Charter |
| Expected lead time | The lead time the system will produce at the current load | Average WIP divided by average throughput (Little's law) | Derived | Monthly Steering | Used to set the limit: the limit that gives the lead time the functions can accept | Proposed |
| Flow efficiency | The share of lead time in which an item is worked on | Active working days divided by lead time, as a percentage | Boards; Waiting flags | Monthly Steering | A trend; low values show waiting, not slow work | Proposed |
| Aging | How long an item has been in its current step | Today minus the date it entered the step; the oldest item per step | Portfolio Backlog; boards | Weekly Review | An item older than the 85th percentile of its step is raised | Charter, in part |
| Waiting | Items Waiting on a dependency outside AICC, and the days Waiting | Count of Waiting items; sum of days Waiting | Boards | Weekly Review | Each Waiting item has a named Dependency and an owner | Charter |
| Flow load | The demand against the capacity of the Portfolio | Approved Initiatives waiting in the Portfolio Backlog; their days waiting | Portfolio Backlog | Monthly Steering | A queue that grows for two quarters is a signal to the strategic loop | Charter, in part |
| Flow distribution | The mix of the work in progress by kind | Share of Active Initiatives and Features by kind: business, enabling, risk and compliance | Portfolio Backlog; Program Backlog | Quarterly Steering | The Executive Sponsor sets the mix; enabling and risk work are not starved | Proposed |
| Gate returns | Business cases and items returned at a gate | Returns divided by items presented at the gate, as a percentage | Decision Log | Monthly Steering | A trend; a rising rate shows that the entry criteria are not understood | Charter, in part |
| Predictability | PI Objectives achieved against planned | Business value achieved divided by business value planned for the Program Increment, as a percentage | PI Objectives | PI Review and Demo | A trend, without a target; read as a band, since both very low and perfect values mean the plan is not honest | Charter |

## 3. Outcome measures of an Initiative

| Measure | Definition | Formula | Source | Read at | Target rule | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Key result | A leading indicator of the Initiative Brief with source system, baseline, and target | Current value against baseline and target; progress as (current minus baseline) divided by (target minus baseline) | The source system named in the brief | End of the MVP; quarterly Steering | Two to four per Initiative; a baseline before the MVP | Charter |
| Adoption | The share of the intended users or cases that use the Solution | Users or cases served by the Solution divided by the intended users or cases | The Solution; the function | Quarterly Steering; live review | Set in the brief; the first key result of most Solutions | Proposed form |
| Acceptance | The share of the Solution's outputs that the person accepts without change | Outputs promoted without change divided by outputs produced | The Solution's log | Live review | Set in the brief; read with the override rate | Proposed form |
| Cycle | The change in the time or the effort of the process the Solution serves | Time or effort after divided by time or effort before, against the baseline | The function's measure | Quarterly Steering | Set in the brief; the measure the business case rests on | Proposed form |
| Benefit claimed | The benefit the business case states | As stated in the Initiative Brief, pointing to the figure in the financial planning | Initiative Brief | Approval | Within the Envelope | Charter |
| Benefit confirmed | The benefit the Domain Owner confirms after delivery | As confirmed at the Outcome Report and each quarter | Outcome Report; Quarterly Report | Quarterly Steering | Read against benefit claimed and against the Envelope | Charter |
| Benefit realization | How much of the claimed benefit arrived | Benefit confirmed divided by benefit claimed, as a percentage | Derived | Quarterly Steering; yearly Steering | A trend per priority; a persistent shortfall changes how briefs are written | Proposed |

## 4. Portfolio economics: the profit and loss view

4.1. The Portfolio has no revenue of its own; its economics are the investment the Bank puts into each Strategic Priority and the benefit that comes back, read as a profit and loss view per priority and for the whole. The figures stay in the financial planning of the Bank; the Portfolio reads them.

| Measure | Definition | Formula | Source | Read at | Target rule | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Investment Envelope | The investment set for a Strategic Priority for the year | As set by the Executive Sponsor | Priorities Record; financial planning | Yearly Steering | Set each year | Charter |
| Committed | The cost of the approved and Active Initiatives of a priority | Sum of the cost stated in the briefs of the Initiatives of the priority | Initiative Briefs | Monthly Steering | At or below the Envelope; an Initiative above a guardrail needs the Executive Sponsor | Charter, in part |
| Spent | The cost incurred against the Envelope to date | As recorded in the financial planning of the Bank | Financial planning | Quarterly Steering | Read against the Envelope and the time elapsed | Proposed |
| Envelope utilization | How much of the Envelope is used | Spent divided by the Envelope, as a percentage | Derived | Quarterly Steering; yearly Steering | Neither far below nor above; both inform the next Envelope | Proposed |
| Benefit against the Envelope | The return of a priority | Sum of the benefit confirmed of the Initiatives of the priority, against the Envelope | Quarterly Report | Quarterly Steering; yearly Steering | The measure of the Charter 7.1; informs the next yearly decision | Charter |
| Benefit-to-investment ratio | The return per unit of investment | Benefit confirmed divided by spent | Derived | Yearly Steering | A trend per priority; read with the Maturity Level, since early priorities invest in foundations | Proposed |
| Payback | The time until a Solution's confirmed benefit covers its cost | Months until cumulative benefit confirmed equals cost spent plus run cost | Derived | Quarterly Steering | Stated in the brief for a Service; read at the sunset review | Proposed |
| Run cost | The cost of operating a Service: run, licenses, provider costs | As stated in the business case and recorded by the Domain | Business case; financial planning | Live review; quarterly Steering | Paid by the Domain from its Envelope; the sunset rule applies when it exceeds the benefit | Charter |
| Cost of the probe | What an MVP cost before the decision | Cost spent from pull to the decision after the MVP | Financial planning; time records | Decision after the MVP | Narrow scope by rule; informs the size of future probes | Proposed |
| Weighted shortest job first | The rank of an approved Initiative | (Value plus urgency plus risk reduction or opportunity) divided by effort, each scored from 1 to 5 | Portfolio Backlog | Monthly Steering | The AICC Lead may depart from the rank for a stated reason | Charter |
| Cost of delay, as the rank reads it | What waiting costs | The numerator of the rank: value plus urgency plus risk reduction or opportunity | Portfolio Backlog | Monthly Steering | Used to order; not a currency figure in the charter | Charter, as scores |

4.2. Read together, the view for a priority is: the Envelope; committed and spent against it; the benefit claimed by its Initiatives; the benefit confirmed; the ratio of the two; and the ratio of benefit to investment. For the whole Portfolio, the same across priorities, with the flow distribution showing how much of the investment went to business, enabling, and risk work. The yearly Steering reads this view when it renews the Envelopes.

## 5. Control and quality measures

| Measure | Definition | Formula | Source | Read at | Target rule | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Limit adherence | Whether the Active Initiatives stayed within the limit | Days in the period with Active above the limit | Portfolio Backlog | Monthly Steering | Zero; an excess is a decision of the Steering, recorded | Charter, in part |
| Decision sample | The share of the AICC Lead's decisions sampled at the monthly Steering and found in order | Decisions found in order divided by decisions sampled | Decision Log | Monthly Steering | Set by the Steering; a finding is a deficiency | Charter |
| First-time pass | The share that meets the check or the validation first time | Items passed first time divided by items presented | Check and validation records | Weekly Review; Iteration Review and Demo | A trend; a falling rate shows quality is inspected in | Charter |
| Defects after the check | Defects found in operation after the check or validation | Count per Solution per period | Service Management; AI Registry | Iteration Review and Demo | A trend per Solution; feeds the reassessment of the Risk Tier | Charter |
| Override rate | How often a person corrected the output of a Solution | Outputs overridden or corrected divided by outputs produced | The Solution's log | Live review | Read with acceptance; both very high and very low values are signals | Statement of Intent, as a Measure |
| Incidents and control breaches | AI Incidents and control breaches per Solution and in total | Count by severity per period | AI Incident Reviews; Risks and Issues Record | Quarterly Steering | Reported each quarter; a major incident at once | Charter |
| Dependencies met | Dependencies met by their date | Dependencies met divided by dependencies due | Program Board | PI Review and Demo | A trend | Charter |

## 6. How the measures are kept

6.1. Each measure above has one owner for its definition, the AICC Lead, and one source. A measure is added or changed by a decision at the monthly Steering and recorded; a measure that nobody reads for two quarters is removed. The definitions of the charter prevail over this page where they differ; the proposed measures become rules when the Solution Lifecycle Model 10 and the Charter 7 are revised from the baseline by a decision record.

## 7. Rule source

Solution Lifecycle Model 10; Portfolio Management Model 5.4, 6.5, and 9; AI Competence Center Charter 7.1; Statement of Intent 11.3; Business Model 6; the lean portfolio management practice recorded in the Reference.
