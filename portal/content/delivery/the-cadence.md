# The cadence: Program Increments and Iterations

Delivery runs on a fixed rhythm. A Program Increment is one quarter; it holds three Iterations of one calendar month each; the last week of the third Iteration is the Innovation and Planning week; every week starts with planning and ends with review; every working day starts with a stand-up. The dates are fixed in advance in the Calendar Record, and the plan of a quarter states intent and direction, not a promise of scope. This part states the cadence and why a fixed rhythm is the opposite of rigidity.

## 1. The units of the cadence

| Unit | Length | Holds | Named |
| --- | --- | --- | --- |
| Program Increment (PI) | One quarter | Three Iterations; the IP week in the last week of the third | PIQ1 to PIQ4 of a year |
| Iteration | One calendar month of four or five whole weeks | The weeks; the review week last, except where the IP week takes its place | I01 to I12 |
| IP week | The last week of the third Iteration | PI Review and Demo, Inspect and Adapt, Innovation, PI Planning, the quarterly Steering | The IP week of PIQn |
| Week | Monday to Friday | Weekly Planning on Monday, the work, Weekly Review on Friday | W1 to W5 of an Iteration |
| Day | A working day | The Daily Stand-up and the work | |

1.1. The Calendar Record may place the IP week earlier and keep a year-end week free of events. An event that falls on a blocked or gray day moves to the working day before it, never after; when moved events meet, the larger keeps the day. Innovation is optional and is dropped first when days are lost. An event that is missed is not held later; its intent is covered at the next event.

## 2. A quarter in sequence

2.1. Figure 1 shows a Program Increment: three Iterations, each with its planning, its working weeks, and its review week, and the IP week that closes the quarter and opens the next.

```mermaid
flowchart LR
  subgraph I1["Iteration 1"]
    direction LR
    P1["Iteration<br/>Planning"] --> W1["Weeks<br/>plan, work, review"] --> R1["Review week<br/>Review and Demo,<br/>Retrospective,<br/>monthly Steering"]
  end
  subgraph I2["Iteration 2"]
    direction LR
    P2["Iteration<br/>Planning"] --> W2["Weeks"] --> R2["Review week"]
  end
  subgraph I3["Iteration 3"]
    direction LR
    P3["Iteration<br/>Planning"] --> W3["Weeks"] --> IP["IP week<br/>PI Review and Demo,<br/>Inspect and Adapt,<br/>Innovation, PI Planning,<br/>quarterly Steering"]
  end
  I1 --> I2 --> I3
```

Figure 1: a Program Increment in sequence.

## 3. Why a fixed cadence

3.1. A fixed cadence synchronizes everyone without a meeting to arrange it, bounds the batch so that work is cut into pieces that finish, and makes learning regular: every month ends with a demonstration and a retrospective, every quarter with a review and an improvement. The cadence is fixed; the content is not: the PI Objectives are intent, scored afterwards, and the Iteration Backlog is selected month by month from a backlog that changes.

## 4. Light mode

4.1. While the AICC Team has up to three people, AICC runs in light mode: the Weekly Planning and the Weekly Review are one session; the Iteration Retrospective and the monthly Steering are held in the Iteration Review and Demo; Inspect and Adapt is held in the PI Review and Demo; the Daily Stand-up, Backlog Refinement, and Innovation are optional; Work Items are not tracked in the charter; and the AICC Lead is the product owner. Everything else stays as stated, so that the method grows without changing when the Team does.

## 5. The cadence and the control of the unit

5.1. The loops of delivery, the portfolio loops, and the control loops of the unit run on the same events and add no meeting: one calendar serves all three. The Cadence workflow and guide state the events by week, Iteration, and Program Increment, with the days and the exceptions.

## 6. Rule source

Solution Lifecycle Model 6.1, 6.5, 6.6, and 6.7; the Cadence workflow and guide; the Calendar Record.
