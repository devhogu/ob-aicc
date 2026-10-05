# Portfolio measures: definitions and formulas

The course states what the Portfolio measures and why. This page states the measures themselves, one by one, as lean and portfolio practice defines them: the definition, the formula where there is one, the source, where it is read, and the rule for its target. It is the reference for the Dashboard, the Steering Summary, and the Quarterly Report. The measures that the Portfolio Management Model 9.2 and the Solution Lifecycle Model 10.3 define are given here as they define them, and they prevail; the others are the standard measures of lean flow and portfolio economics, given here as explanation, and they state no rule.

## 1. Conventions

1.1. A measure has a definition, a source, a place where it is read, and a target that is set once there is a baseline. A figure of the Bank stays in its source system, and the record points to it. Time is counted in calendar days unless stated; a Program Increment is one quarter; an Iteration is one month. Measures of flow are read as distributions and trends, not as single numbers: the median and the eighty-fifth percentile say more than the mean. No measure is used to rank people.

Standing Initiatives are shown separately from the ordinary portfolio Kanban and are excluded from its flow measures. Their run-rate Features are counted in the delivery measures (Portfolio Management Model 9.2).

## 2. Flow measures

| Measure | Definition | Formula | Source | Read at | Target rule |
| --- | --- | --- | --- | --- | --- |
| Work in progress | The Initiatives Active at one time, other than the Standing Initiatives; the items in each step of the Kanban | Count of Initiatives in state Active; count per step | Portfolio Backlog | Monthly Steering | Within the limit on the Active Initiatives, which is set within the mix |
| Throughput | Initiatives accepted per Program Increment; Features accepted per Iteration | Count of items reaching Accepted in the period | Portfolio Backlog; Program Backlog | Quarterly Steering; Iteration Review and Demo | A trend, with no target; it rises as work in progress is held and blockers removed |
| Lead time | Days from Approved to Accepted for an Initiative | Date Accepted minus date Approved | Portfolio Backlog | Quarterly Steering | Set by the Steering once a baseline exists; read as the median and the 85th percentile, and it falls as work in progress falls |
| Time to decision | Days from the entry of an Initiative in the funnel to its approval | Date Approved minus the date of entry in the funnel | Portfolio Backlog | Monthly Steering | Set by the Steering once a baseline exists |
| Cycle time | Days from Active to Review for an Initiative; for a Feature, from Active to Completed, or to Review in light mode | Date Review, or Completed, minus date Active | Portfolio Backlog; Program Backlog; boards | Quarterly Steering; Weekly Review for the Features | Set once a baseline exists; read as the median and the 85th percentile per item type |
| Expected lead time | The lead time the system will produce at the current load | The average number of Initiatives between Approved and Accepted divided by the average throughput, in Program Increments (Little's law) | Portfolio Backlog | Monthly Steering | No target; it informs the limit on the Active Initiatives |
| Flow efficiency | The share of lead time in which an item is Active and not Waiting | Days Active and not Waiting divided by lead time, as a percentage | Portfolio Backlog; boards | Monthly Steering | A trend, with no target; low values show waiting, not slow work |
| Aging | How long an item has been in its current step | Today minus the date it entered the step; the oldest item per step | Portfolio Backlog; boards | Weekly Review | An item older than the 85th percentile of its step is raised |
| Waiting | Items Waiting on a dependency outside AICC, and the days Waiting | Count of Waiting items; sum of days Waiting | Boards | Weekly Review | Every Waiting item names its Dependency |
| Flow load | The demand that waits for a place under the limit | Approved Initiatives waiting in the Portfolio Backlog; their days waiting | Portfolio Backlog | Monthly Steering | A queue that grows for two quarters goes to the strategic loop |
| Flow distribution | The mix of the work in progress by Strategic Priority and by kind | Share of the Active Initiatives by Strategic Priority and by kind of work: business, enabling, risk and compliance | Portfolio Backlog | Quarterly Steering | Within the mix that the Executive Sponsor sets, so that enabling and risk work are not starved |
| Gate returns | Business cases and items returned at a gate | Returns divided by items presented at the gate, as a percentage | Decision Log | Monthly Steering | A trend, with no target; a rising rate shows that the entry criteria are not understood |
| PI predictability | The business value achieved against the business value planned of the PI Objectives | Business value achieved divided by business value planned, summed over the PI Objectives of the Program Increment, as a percentage | PI Objectives | PI Review and Demo; quarterly Steering | A trend, without a target; read as a band, since both very low and perfect values mean the plan is not honest |

## 3. Outcome measures of an Initiative

| Measure | Definition | Formula | Source | Read at | Target rule |
| --- | --- | --- | --- | --- | --- |
| Leading indicator | A measure of a change in the business, stated in the Initiative Brief with its source system, baseline, and target | Current value against baseline and target; progress as (current minus baseline) divided by (target minus baseline) | The source system named in the brief | End of the MVP; quarterly Steering | Two to four per Initiative; the baseline in the brief before approval |
| Adoption | The share of the intended users or cases that use the Solution | Users or cases served by the Solution divided by the intended users or cases | The Solution; the function | Quarterly Steering; live review | Set in the brief, where it is a leading indicator |
| Acceptance | The share of the Solution's outputs that the person accepts without change | Outputs accepted without change divided by outputs produced | The Solution's log | Live review | Set in the brief, where it is a leading indicator; read with the human override and correction rate |
| Cycle | The change in the time or the effort of the process the Solution serves | Time or effort after divided by time or effort before, against the baseline | The function's measure | Quarterly Steering | Set in the brief; the measure the business case rests on |
| Benefit claimed | The benefit the business case states | As stated in the Initiative Brief, pointing to the figure in the financial planning | Initiative Brief | Approval | Within the Envelope |
| Benefit confirmed | The benefit the Domain Owner confirms after delivery | As confirmed at the Outcome Report and each quarter | Outcome Report; Quarterly Report | Quarterly Steering | Read against benefit claimed and against the Envelope |
| Benefit confirmed against claimed | How much of the claimed benefit arrived | Benefit confirmed against benefit claimed, by reference to the figures in their source | Initiative Brief; Outcome Report | Quarterly Steering; yearly Steering | A trend by Strategic Priority, read against the Envelope; a persistent shortfall changes how briefs are written |

## 4. Portfolio economics: the profit and loss view

4.1. The Portfolio has no revenue of its own; its economics are the investment the Bank puts into each Strategic Priority and the benefit that comes back, read as a profit and loss view per priority and for the whole. The figures, and each ratio drawn from them, stay in the financial planning of the Bank, and the records of the Portfolio point to them (Business Model 6.1).

| Measure | Definition | Formula | Source | Read at | Target rule |
| --- | --- | --- | --- | --- | --- |
| Investment Envelope | The investment set for a Strategic Priority for the year | As set by the Executive Sponsor | Priorities Record; financial planning | Yearly Steering | Set each year |
| Committed | The cost of the approved and Active Initiatives of a priority | Sum of the cost stated in the briefs of the Initiatives of the priority | Initiative Briefs | Monthly Steering | At or below the Envelope; an Initiative above a guardrail needs the Executive Sponsor |
| Spent | The cost incurred against the Envelope to date | As recorded in the financial planning of the Bank | Financial planning | Quarterly Steering | Read against the Envelope and the time elapsed |
| Envelope utilization | How much of the Envelope is used | Spent divided by the Envelope, as a percentage | Financial planning | Quarterly Steering; yearly Steering | Neither far below nor above; both inform the next Envelope |
| Benefit against the Envelope | The return of a priority | Sum of the benefit confirmed of the Initiatives of the priority, against the Envelope | Quarterly Report | Quarterly Steering; yearly Steering | The measure of the AICC Charter 7.1; informs the next yearly decision |
| Benefit-to-investment ratio | The return per unit of investment | Benefit confirmed divided by spent | Financial planning | Yearly Steering | A trend per priority; read with the Maturity Level, since early priorities invest in foundations |
| Payback | The time until a Solution's confirmed benefit covers its cost | Months until cumulative benefit confirmed equals cost spent plus run cost | Financial planning | Quarterly Steering | Stated in the brief for a Service; read with its sunset rule |
| Run cost | The cost of operating a Service: run, licenses, provider costs | As stated in the business case and recorded by the Domain | Business case; financial planning | Live review; quarterly Steering | Paid by the Domain from its Envelope; the sunset rule applies when it exceeds the benefit |
| Cost of the probe | What an MVP cost before the decision | Cost spent from pull to the decision after the MVP | Financial planning; time records | Decision after the MVP | Narrow scope by rule; informs the size of future probes |
| Weighted shortest job first | The rank of an approved Initiative | (Value plus urgency plus risk reduction or opportunity) divided by effort, each scored from 1 to 5 | Portfolio Backlog | Monthly Steering | The AICC Lead may depart from the rank for a stated reason |
| Cost of delay, as the rank reads it | What waiting costs | The numerator of the rank: value plus urgency plus risk reduction or opportunity | Portfolio Backlog | Monthly Steering | Used to order; not a currency figure in the charter |

4.2. Read together, the view for a priority is: the Envelope; committed and spent against it; the benefit claimed by its Initiatives; the benefit confirmed; the ratio of the two; and the ratio of benefit to investment. For the whole Portfolio, the same across priorities, with the flow distribution showing how much of the investment went to business, enabling, and risk work. The yearly Steering reads this view when it renews the Envelopes.

## 5. Control and quality measures

| Measure | Definition | Formula | Source | Read at | Target rule |
| --- | --- | --- | --- | --- | --- |
| Limit adherence | Whether the Active Initiatives stayed within the limit | Days in the period with Active above the limit | Portfolio Backlog | Monthly Steering | Zero; the limit may not be exceeded (Business Model 7.1; Portfolio Management Model 5.4) |
| Decision sample | The share of the sampled Decisions of the AICC Lead found in order; the sample is at least three Decisions, chosen by the Executive Sponsor | Decisions found in order divided by Decisions sampled | Decision Log; Steering Summary | Monthly Steering | All found in order (Operating Model 6.11) |
| First-time-right rate | The share of items that pass the check or the validation at the first attempt | Items passed first time divided by items presented | Check and validation records; backlogs | Weekly Review; Iteration Review and Demo | Set once a baseline exists; a falling rate shows quality is inspected in |
| Defects after the check | Defects found in operation after the check or validation | Count per Solution per period | Service Management; AI Registry | Iteration Review and Demo | Each one is read at the next reassessment of the Risk Tier |
| Human override and correction rate | How often a person overrides or corrects the output of a Solution, against the baseline | Outputs overridden or corrected divided by outputs produced | The Solution's log | Live review | A rate that is very high or very low is raised at the review of the live Solution |
| Incidents and control breaches | AI Incidents and control breaches per Solution and in total | Count by severity per period | AI Incident Reviews; Risks and Issues Record | Quarterly Steering | Reported each quarter; a major incident at once |
| Dependency timeliness | The Dependencies Met by the date on which they are needed | Dependencies Met by their date divided by Dependencies due | Program Board | PI Review and Demo | Set once a baseline exists |

## 6. How the measures are kept

6.1. Each measure above has one owner for its definition, the AICC Lead, and one source. A measure of the Portfolio is added or changed by a Decision of the Executive Sponsor at the monthly Steering, entered in the Decision Log, and a measure that is not read for two Program Increments is removed in the same way (Portfolio Management Model 9.6; Solution Lifecycle Model 10.5). The definitions of the Portfolio Management Model 9.2 and the Solution Lifecycle Model 10.3 prevail over this page where they differ, and the other measures here state no rule.

## 7. Rule source

Solution Lifecycle Model 10; Portfolio Management Model 5.4, 6.5, 6.7, and 9; Operating Model 6.11; AICC Charter 7.1; Statement of Intent 11.3; Business Model 6; the lean portfolio management practice recorded in the Reference.
