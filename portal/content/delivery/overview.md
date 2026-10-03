# Delivery

Delivery is how an approved idea becomes a working Solution in the hands of a function, and how that Solution is kept, changed, and retired. AICC delivers in small steps on a fixed cadence, with the work visible and limited, with quality built into the flow rather than inspected at the end, and with a decision and a record at each step. This course explains the method in ten parts, as a reader new to agile delivery at scale would need it; the Solution Lifecycle Model is the rule and prevails.

## 1. One picture

1.1. Figure 1 shows the delivery of a Solution end to end: from the Capability that the Portfolio approved to a Solution in use, and the loops that run around it.

```mermaid
flowchart TB
  subgraph ROW1["The stream: from an approved Capability to a released Solution"]
    direction LR
    CAP["Capability<br/>from the Portfolio,<br/>in the Program Backlog"] --> EX["Explore<br/>the need, the options,<br/>the benefit hypothesis"]
    EX --> DS["Design<br/>the Feature, its<br/>acceptance criteria,<br/>its Dependencies"]
    DS --> DV["Develop<br/>in the Iteration,<br/>within the limits"]
    DV --> VF["Verify<br/>test by another person;<br/>check or validation<br/>by Risk Tier"]
    VF --> DP["Deploy<br/>through change<br/>management, to the<br/>environment of use"]
    DP --> AC["Accept<br/>product owner; the Team;<br/>the Domain Owner"]
    AC --> RL["Release<br/>beyond the first users,<br/>a separate decision"]
  end
  subgraph ROW2["The life after release, and the loops that run around the stream"]
    direction LR
    OP["Operate<br/>support, monitoring,<br/>live review"] --> EV["Evolve<br/>a change is a Feature;<br/>significant changes<br/>re-checked"]
    EV --> RT["Retire<br/>access removed, data<br/>handled, registry closed"]
    L1(["Day and week<br/>stand-up, planning,<br/>review of the flow"]) ~~~ L2(["Iteration<br/>plan, demo and<br/>acceptance,<br/>retrospective"]) ~~~ L3(["Program Increment<br/>PI Planning, PI Review<br/>and Demo, Inspect<br/>and Adapt"])
  end
  ROW1 ~~~ ROW2
```

Figure 1: delivery end to end, the stream and the loops.

1.2. Run-rate work follows the route in Solution Lifecycle Model 3.1 and 5.2: a Feature sits directly under an approved Standing Initiative and is admitted at the Weekly Review within the current Iteration's limits. It records its client, acceptance criteria, Dependencies, delivery, and product-owner acceptance. A document or training result has delivery and acceptance evidence; Solution, validation, release, and production-change gates apply when the work includes a Solution or production deployment.

## 2. What delivery is for

2.1. The Portfolio decides what is worth doing; delivery makes it real without betraying the decision. Its job is to turn a hypothesis into working software and working practice in a function, to learn early whether the hypothesis holds, to keep the Bank safe while doing so, and to do it at a rhythm the functions can plan around. For a unit of a few people, the method matters more than for a large one: the cadence, the limits, and the gates are what let three people deliver without heroics and without surprises.

2.2. The principles of the Solution Lifecycle Model state it in eight lines: make work visible, limit work in progress, and pull; deliver in small steps, probe, measure, then scale; put value first; plan on a cadence, where the plan of a quarter states intent and not a promise; build quality in; decide where the facts are; make dependencies visible and manage them as work; improve continuously.

## 3. The industry practice it follows

3.1. The method is the lean-agile practice of delivering at scale, adapted to a small unit in a bank: work in levels worded as hypotheses with acceptance criteria; a fixed cadence that synchronizes planning, delivery, and review; Kanbans with limits; a board of dependencies; a pipeline from exploration to release on demand, with deployment and release separated; quality built in; events that plan, demonstrate, and improve; flow measured rather than effort. The practice is recorded in the [Industry body of knowledge](../reference/industry-body-of-knowledge.md).

3.2. Where the Bank's model differs from the common form, it is because of scale and regulation: one Team rather than many, a month-long Iteration rather than two weeks, an Innovation and Planning week that also hosts the quarterly Steering, light mode while the Team has up to three people, and the check or validation by a person other than the builder, in proportion to the Risk Tier, written into the Verify step.

## 4. How to read this course

4.1. The course is the overview: each part states one aspect of the method in a few lines and a figure. The detail is in the pages that follow it in this section: the Solution Lifecycle Model is the rule; the Service delivery and Cadence workflows and guides show the flows, the events, and the records step by step; The Experiment workflow, The life of a Service, and Service operations state the life of a Solution in depth; and Delivery measures states every measure with its definition and formula.
