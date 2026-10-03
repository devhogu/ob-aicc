# Quality, verification, and release

Quality is built into the flow of delivery, not inspected at its end. Every Feature is tested by a person other than its builder before it is deployed; every Solution is checked or validated in proportion to its Risk Tier before it reaches real users or data; acceptance is given at three levels, each against written criteria; and release beyond the first users is a separate decision, with a signed checklist. This part states the gates in order and the reasoning behind each.

## 1. The gates in order

```mermaid
flowchart TB
  subgraph ROW1["A Feature: from build to acceptance"]
    direction LR
    B["Built<br/>within the Iteration"] --> T["Gate: test<br/>by a person other than<br/>the builder, not in<br/>production; result<br/>referenced in the Feature"]
    T --> CV["Gate: check or validation<br/>of the Solution, at the first<br/>Feature that reaches real users<br/>Checker for Tier 1; Control<br/>Function Contacts for Tier 2 and 3"]
    CV --> D["Deploy<br/>to the environment of use,<br/>through change management"]
    D --> A1["Gate: acceptance<br/>product owner, at the<br/>Iteration Review and Demo,<br/>against the criteria"]
  end
  subgraph ROW2["A Solution: from the Team to the Bank"]
    direction LR
    A2["Gate: final acceptance<br/>of the Team<br/>AICC Lead, before the first<br/>users and each significant<br/>change"] --> FU["Deployed to<br/>the first users<br/>named and trained"]
    FU --> A3["Gate: business acceptance<br/>Domain Owner as the requester;<br/>Executive Sponsor across<br/>Domains, for enabling work,<br/>or an Experiment without<br/>a Domain"]
    A3 --> CL["Acceptance Checklist<br/>each party signs<br/>within its remit"]
    CL --> RL["Gate: release<br/>beyond the first users<br/>Domain Owner for Tier 1 and 2;<br/>Executive Sponsor for Tier 3<br/>or where the AICC Lead built it"]
    RL --> LV(["Live Solution"])
  end
  ROW1 ~~~ ROW2
```

Figure 1: the gates of quality, acceptance, and release.

## 2. Testing by another person

2.1. Every Feature, and the MVP of an Initiative, is tested by a person other than its builder, in an environment that is not production, before it is deployed, and the result is referenced in the Feature. The rule is the oldest control of software engineering and it is kept without exception: the builder's own tests are necessary and are not sufficient. A failure returns the Feature to the builder; the first-time pass rate is read at the Weekly Review as the measure of whether quality is built in.

## 3. The check or validation by Risk Tier

3.1. The check for Risk Tier 1 and the validation by the Control Function Contacts for Risk Tier 2 and 3 attach to the Solution, not to each Feature, and they are taken in the Verify step of the first Feature that reaches real users or data. For Risk Tier 2 and 3 the validation replaces the check and includes a security test against the attacks specific to AI; the Control Function Contacts take part when the Solution is defined and in its validation, and they rely on the evidence, the logs, and the traces that the Platform Owner keeps. A validation states the date until which it is valid and the changes that require a new one. AICC does not validate its own work.

## 4. The three acceptances

4.1. Acceptance closes an item, and it is given at three levels, each against the acceptance criteria and each noted with who and when. During development, the product owner accepts each Feature and each Capability at the Iteration Review and Demo: accept, return with what is missing, or reject when the outcome is not wanted. Before a Solution is provided to the Domain Owner for judgment, the AICC Lead gives the final acceptance of the Team: the criteria of the Solution Definition met, the tests referenced, the check or validation in place, recorded in the release block. Then the requester, the Domain Owner for a Solution of a Domain, judges the working Solution deployed to its first users and accepts, returns, or rejects it; for an Engagement, this is also the acceptance of the Outcome Report.

4.2. Three acceptances are not bureaucracy; they are three different questions. Does the Feature do what we wrote? Is the Solution safe and complete enough to put in front of people? Does it solve the problem the function brought? Each is asked by the person entitled to answer it. While the Team is small, the AICC Lead may give the first two for a Solution the AICC Lead built, never the third, and never the check, the validation, or the release; the limit is recorded, and the compensating controls are the test by another person, the check or validation by another, the Domain Owner's acceptance, the release decision, and the monthly sample of the AICC Lead's decisions.

## 5. Deployment and release

5.1. Deployment and release are different acts. A Feature is deployed to its environment of use after its test and its check or validation; a deployment to production follows the change management of the Bank, with the change ticket and the test result entered in the Feature, and access granted through the access process of the Bank. The first users are named by the Domain Owner in the Solution Definition and trained before use. Release beyond the first users is a separate decision, by the Domain Owner for Risk Tier 1 and 2 and by the Executive Sponsor for Risk Tier 3 or where the AICC Lead is the Domain Owner, taken when the Acceptance Checklist is signed: each party, the Domain Owner, the Solution Engineer, the AICC Lead, the Checker, the Control Functions concerned, and the IT function that operates the Solution with the Platform Owner, confirms the items within its remit, and an item not met stops the release.

5.2. The separation is what lets delivery be continuous and release be deliberate. Features flow to their environment of use at the pace of the Team; the Bank switches value on at the pace of its judgment.

## 6. Built-in quality beyond the gates

6.1. The gates are the visible part. Behind them stand the practices that make them pass: acceptance criteria written before the work; small Features that close within an Iteration; integration as the work goes, so that the test is of the whole; a definition of done that includes the test, the deployment, and the record; and the measures of quality, first-time pass, defects found after the check, change failure rate, read at the Weekly Review and the Iteration Review and Demo. A failing measure is a problem for Inspect and Adapt, not a reason to add a gate.

## 7. Rule source

Solution Lifecycle Model 7 and 8.3; AI Policy 3; Operating Model 4.4; the Acceptance Checklist and Control Sign-Off templates; the Service delivery workflow and guide.
