# Guide: Engagement

## 1. Purpose and when it applies

This guide explains how AICC works with a function of the Bank. AICC acts as an internal consulting unit: a function brings a need, AICC commits to an Engagement in a Service Agreement, delivers an outcome with its evidence, and supports it at the agreed level. It applies to every Engagement, from a short study to a Service that AICC runs, and to run-rate work. The rules are in the Business Model, the Portfolio Management Model, the Solution Lifecycle Model, and the AI Policy, and this guide states no rule of its own.

## 2. Who takes part

| Role | In an Engagement |
| --- | --- |
| Domain Owner | Represents the client function; approves the business case within a Domain and below a guardrail; judges the working Solution and accepts it as the requester; confirms the benefit |
| Domain Expert | Partner from the function who works with AICC |
| AICC Lead | Takes the need in; writes the business case with the Domain Owner; issues the Service Agreement; gives the final acceptance of the Team before the Solution is deployed to the first users; writes the Outcome Report |
| Solution Engineer | Designs, builds, and runs the Solution with the Domain Expert |
| Executive Sponsor | Is the client of enabling work; approves the Initiative Brief of each Standing Initiative, and what exceeds a guardrail or spans Domains |
| Control Function Contacts | Clear the business case when Risk Tier 2 or 3 is expected, validate the Solution, and may stop it |
| Stakeholders and other heads of function | Are notified, and commit to nothing |

## 3. How a function starts

A head of function brings a need to the AICC Lead, in any form: a conversation, a message, or a ticket in Service Management. The AICC Lead is named in the Appointments Record. The AICC Lead enters the need in the Portfolio Backlog and takes it in when it fits a Strategic Priority, has a client function with a Domain Owner, and the limit on the Active Initiatives permits it (Business Model 7.2). Otherwise it is deferred or rejected.

At intake the need finds its service category and its mode. The AICC Lead records its problem, its size, its expected Risk Tier, its service category, and its mode, and first checks whether a Solution or a Package of the catalog already answers it (Business Model 7.2). The service categories and the mode that each usually takes are in the Business Model 4.5. A small, repeatable request that can be done within one Iteration is run-rate work: the AICC Lead takes it in at the Weekly Review as a Feature of the Standing Initiative of its service area, once the Domain Owner has approved the use for its data class, and it needs no Initiative Brief, no Service Agreement, and no Outcome Report of its own (Business Model 4.8). Any other need is an Initiative and runs as section 4 shows.

## 4. How an Engagement runs

Figure 1 shows the path of an Engagement from the first contact to the approval of its business case, with the decisions that bind it.

```mermaid
flowchart LR
  C["Contact<br/>a need from a function"] --> IN{"Intake<br/>fits a Strategic Priority,<br/>has a Domain Owner,<br/>within the limit on<br/>Active Initiatives?"}
  IN -->|"no"| DR["Deferred or rejected"]
  IN -->|"yes"| ST["Study<br/>scope and business case<br/>Service Agreement issued"]
  ST --> CL{"Risk Tier 2 or 3<br/>expected?"}
  CL -->|"yes"| CF["Cleared by the<br/>Control Function Contacts"]
  CL -->|"no"| AP
  CF --> AP{"Approval of the<br/>business case"}
  AP -->|"returned"| ST
  AP -->|"deferred or rejected"| DR
  AP -->|"approved"| SA["Service Agreement<br/>amended with the<br/>later phases"]
```

Figure 1: the path of an Engagement from the contact to the approval.

Figure 2 shows the path from the approval of the business case to the close.

```mermaid
flowchart LR
  MV["MVP<br/>a probe against the<br/>leading indicators"] --> DM{"Decision after the MVP"}
  DM -->|"pivot, defer, reject"| DR["Pivoted, deferred,<br/>or rejected"]
  DM -->|"continue"| DL["Delivery<br/>build, test, check<br/>or validation"]
  DL --> TF["Final acceptance<br/>of the Team<br/>AICC Lead"]
  TF --> FU["Deployed to the<br/>first users"]
  FU --> BA{"Acceptance of the<br/>Domain Owner<br/>as the requester"}
  BA -->|"returned"| DL
  BA -->|"accepted"| OR["Outcome Report;<br/>the release beyond the first<br/>users is a separate decision"]
  OR --> SP["Support at the<br/>agreed level"]
  SP --> CK{"Check-in at<br/>each Iteration"}
  CK -->|"follow-on"| NX["A new need<br/>at Contact"]
  CK -->|"end or redirect"| CLS["Closed"]
```

Figure 2: the path of an Engagement from the MVP to the close.

An Engagement passes through the six steps of the Engagement workflow. The following table states each step, the person who acts, the time, and the record that is left. Run-rate work runs the same steps, shortened, as the Engagement workflow shows.

| Step | What happens | Who | When | Record left |
| --- | --- | --- | --- | --- |
| Contact | A function raises a need, or AICC finds one | Anyone; the AICC Lead takes it in | Any time | An entry in the Portfolio Backlog |
| Study | The need is scoped, and the business case is written and cleared by the Control Function Contacts when Risk Tier 2 or 3 is expected | AICC Lead with the Domain Owner | When the study starts | The Initiative Brief with the clearances |
| Service Agreement | AICC states what it commits to | AICC Lead; the function is notified | Issued when the study starts, and amended when the business case is approved | The Service Agreement |
| Delivery | The first Solution is tried as a probe (the MVP), and after the decision to continue it is built, verified, and deployed to the first users | Solution Engineer with the Domain Expert; the AICC Lead gives the final acceptance of the Team | In the Iterations of the Program Increment | The Solution Definition, the decision after the MVP, the Control Sign-Off, and the release block |
| Outcome Report | The outcome is reported, and the Domain Owner, or the Executive Sponsor for enabling work, accepts it | AICC Lead issues; the Domain Owner accepts | At the end of the Engagement | The Outcome Report |
| Support | The Solution is supported at the agreed level; at each check-in the Engagement goes on, ends, or is redirected, and a follow-on returns to Contact as a new need | Solution Engineer; the AICC Lead with the Domain Owner for the follow-on | After delivery, and at each Iteration check-in | Service Management records, the AI Incident Review, and a new entry or the close |

## 5. The commitment in practice

The Service Agreement has two parts. The commitment states the phases, the support level, the scope and what is out of scope, the deliverables and their definition of done, the Assumptions, the check-in, and the end. The working agreement states who works on it and when, how AICC and the function communicate and decide, who is notified, how data is handled, how issues are escalated, and how progress is reported. AICC works toward the outcome on a best-effort basis, within the capability that it has available, and the function commits to nothing. What AICC relies on from the function is written as an Assumption.

Figure 3 shows the Service Agreement as a loop that runs at each Iteration.

```mermaid
flowchart LR
  PL["Plan<br/>scope as a backlog,<br/>Assumptions"] --> DO["Do<br/>AICC delivers within<br/>the Limits on Work in<br/>Progress and the<br/>capability available"]
  DO --> CH["Check<br/>check-in at the Iteration<br/>with the Domain Owner<br/>and the Domain Expert"]
  CH --> DEC{"Result of the check-in"}
  DEC -->|"on track"| PL
  DEC -->|"an Assumption fails<br/>or the scope changes"| AM["Act<br/>re-plan the scope and the dates,<br/>note the change in the<br/>Service Agreement"]
  AM --> PL
  DEC -->|"either side ends<br/>or redirects"| EN["End<br/>Outcome Report<br/>records it"]
```

Figure 3: the loop of the Service Agreement.

## 6. After delivery

What AICC provides after delivery is chosen for each Engagement and is stated in its Service Agreement. The Solution type follows from it.

| Support level | What AICC does | Solution type |
| --- | --- | --- |
| None | Hands the Solution over, with the Outcome Report | Experiment, or a Product handed over |
| On demand | Answers requests and issues new versions when asked | Product |
| At agreed response targets | Supports to the targets that the Service Agreement states | Service |
| Run by AICC | Runs the Solution for its whole life, with its run cost and its sunset rule | Service |

Figure 4 shows how a request, an incident, and a change are handled after delivery. The response targets are targets and not guarantees.

```mermaid
flowchart LR
  RQ(["Request, incident,<br/>or need for a change"]) --> SM["Service Management<br/>queue of AICC"]
  SM --> TR{"Kind of matter"}
  TR -->|"request or question"| HD["Triaged by the class of service:<br/>Urgent, High priority, Normal<br/>handled and closed"]
  TR -->|"outage or failure"| IM["Incident management<br/>of the Bank<br/>AI Incident where AI is involved<br/>AICC Lead is a stakeholder"]
  TR -->|"a new feature or a change"| BL["Program Backlog<br/>a Feature, verified and deployed<br/>as any Feature is"]
  HD --> RV["Review of the live Solution<br/>by the Domain Owner<br/>at each Iteration Review and Demo"]
  IM --> RV
  BL --> RV
  RV --> CK["Check-in of the Engagement"]
```

Figure 4: support, incident, and change after delivery.

## 7. Situations

| Situation | Treatment |
| --- | --- |
| An Assumption fails, for example the Domain Expert is not available | AICC re-plans the scope and the dates and notes the change in the Service Agreement; the item is Waiting |
| The function wants a different scope | The backlog is reordered within the Limits on Work in Progress at any time; a change beyond the scope of the Service Agreement is a new Engagement or an amendment to the Service Agreement |
| Either side wants to stop | The Engagement is ended or redirected at the end of an Iteration, and the Outcome Report records it |
| The limit on the Active Initiatives is reached | A new Service Agreement is not issued above the limit; the item waits in the Portfolio Backlog |
| A request or an incident arrives after delivery | It comes through Service Management; the response targets are targets and not guarantees |
| A run-rate request cannot be done within one Iteration | It returns to Contact and is taken in as an Initiative (Business Model 4.8) |

## 8. What AICC does not do

The AICC Charter 3.2 states the limits of AICC. AICC does not own or operate the AI Platform, own the business results of a Domain, set the rules of a Control Function, validate its own work, or decide a matter that the regulation of the Bank reserves to the Board, to the management, or to a Control Function. It is not a Control Function and not a platform team of the Bank, and it does not operate a Solution at the scale of the Bank: a Solution that the Bank adopts at scale is handed to its Receiver (Business Model 2.5). When AICC drafts a strategy, a charter, or a normative document for a function, the function owns its substance (Business Model 4.10). A service category is not a commitment: AICC commits only in a Service Agreement (Business Model 4.6).

## 9. Rule source

AICC Charter 3.2; Business Model 2 to 7; Portfolio Management Model 5 to 7; Solution Lifecycle Model 7.3, 8.1, 8.4, 8.5; AI Policy 5; the Engagement workflow.
