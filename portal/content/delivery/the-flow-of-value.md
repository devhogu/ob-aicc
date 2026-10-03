# The flow of value

Value flows from a strategic theme to a task on a board through a small number of levels, and each level is worded in the language of the business so that the client, the Team, and the product owner read the same words. This part states the levels, how work enters, the Team that delivers it, and the stream of Stages a Feature travels.

## 1. The levels of the work

| Level | Meaning | Worded as | Kept in | Decided by |
| --- | --- | --- | --- | --- |
| Strategic Priority | A strategic theme set with the Board, with an Investment Envelope | A theme with an objective, a scope, and an intended outcome | Priorities | Executive Sponsor |
| Initiative | A business program that delivers one or more Solutions; an Engagement when it has a client function | A hypothesis, in the Initiative Brief | Portfolio Backlog | Domain Owner, or Executive Sponsor |
| Solution | A solution or service that an Initiative delivers for a Domain, with a type, a Risk Tier, and an AI Registry entry | A Solution Definition, with its acceptance criteria | The Portfolio | Domain Owner approves; AICC Lead assigns the Risk Tier |
| Capability | A capability of a Solution, delivered over one or more Program Increments | A hypothesis | Program Backlog | AICC Lead, with the Domain Owner consulted |
| Feature | A deliverable of a Capability, closed within one Program Increment, delivered over one or more Iterations | A benefit hypothesis with acceptance criteria in the form Given, When, Then | Program Backlog, then Iteration Backlog | The Team at Iteration Planning; the product owner accepts |
| Work Item | A task of a Team within a Feature | A task | The Team board | The Team |

1.1. The Portfolio Management Model manages the first two levels; the Solution Lifecycle Model begins where the Capabilities of an Initiative enter the Program Backlog. In the tracker, an Initiative sits above the Epic, a Capability is an Epic, a Feature is an issue type, and a Work Item is a sub-task; the word Epic is used in the tracker only.

## 2. The contract of each level

2.1. Each level is a short contract in the language of the business. An Initiative and a Capability are worded as a hypothesis the work tests: for whom, the need, the proposal, the value hypothesis, the difference it makes, the leading indicator. A Feature adds the scope and the acceptance criteria, written as Given a situation, When an action, Then an observable result, so that the person who builds, the person who tests, and the person who accepts agree in advance on what done means. The contract is the definition of done of the level; nothing is accepted against a criterion that was not written before the work.

## 3. How work enters

3.1. Work enters the program in three ways. The Capabilities of an Initiative enter the Program Backlog after the decision to continue at the end of its MVP. A change or a new feature of a released Solution is raised by its Domain Owner or its product owner and enters under the Capability of that Solution. Enabling work of AICC enters under an Initiative of enabling work. Every item is ranked in the Program Backlog before a Team takes it, by value and urgency relative to effort, and a Feature is approved only when its Dependencies are known.

## 4. The Team

4.1. A Team delivers the work: a Solution Engineer with the Domain Expert of the function, the Domain Owner who owns the outcome, and the product owner who accepts the Features during development. While the Team has up to three people, the AICC Lead is the product owner; later the AICC Lead may name another person in the Appointments Record. AICC has the AICC Team, and a Domain may have its own Team working the same method. The AICC Lead ranks the Program Backlog; the Team pulls the Features it can finish in the Iteration and decides how the work is built.

## 5. The stream a Feature travels

5.1. A Feature moves through five Stages inside its Active state: Explore, the need and the options; Design, the Feature with its acceptance criteria and its Dependencies; Develop, the build within the Iteration and the limits; Verify, the test by a person other than the builder in an environment that is not production, and the check or validation of the Solution by its Risk Tier at the first Feature that reaches real users; and Deploy, through the change management of the Bank to the environment of use. A Capability has two Stages, Analysis and Implementation. The Stages are held in a field of the tracker, the state in its status, and the conditions to move on are the conditions of the staging workflow of the model.

5.2. The stream is the Bank's form of the continuous delivery pipeline: exploration before integration, integration before deployment, and deployment before release, with release a separate decision. Each Feature travels the whole stream; what makes delivery continuous is not that the stream is short, but that many small Features travel it in a steady flow.

## 6. Rule source

Solution Lifecycle Model 3 and 5; Portfolio Management Model 8; the Vocabulary.
