# The life of a Service

A Service that AICC runs lives after its release. The Solution Lifecycle Model gives it three Stages, Operate, Evolve, and Retire, and refines them into seven service steps, each with the question that is asked at it, the signals that answer it, the action that follows, and the gate to the next step (Solution Lifecycle Model 8.8). The service steps are not states: the Service stays Active until it is Closed, and the Solution Engineer enters each step and the date on which it was reached in the Solution Definition and the AI Registry.

## 1. The service steps

| Service step | Stage | The question | Signals read | Action | Gate to the next step |
| --- | --- | --- | --- | --- | --- |
| Admitted | Operate | Is the Service ready for its first request? | None yet; the run cost and the sunset rule of its business case | Make the catalog entry, issue the Service Agreement, and open the queue | The three are in place; the AICC Lead confirms |
| Catalogued | Operate | Does it serve its first requests at the response targets? | Service levels; incidents | Serve the first requests, and set the alert levels of the monitoring | The first request served within its target |
| In service | Operate | Is it healthy, used, and worth its run cost? | The four signals: service levels, incidents, use, and cost | Run it under the practices of service operations, and review it at each Iteration Review and Demo | A change is needed: Improving. The reading calls for a transition: Transition planned |
| Improving | Evolve | Does the change correct what the signals show? | The signal that called for the change | A change as a Feature, verified and deployed as any Feature; a new check or validation where the AICC Lead decides | The change accepted, or released where it is significant: In service |
| Transition planned | Evolve | Should the Bank run it at scale, or should it end? | The four signals against the business case and the sunset rule | A Proposal of Handover with a named Receiver, or a plan of retirement | The decision of the Domain Owner, or of the Executive Sponsor for a Service across Domains |
| Migrating | Retire | Have the users, the data, and the run moved without harm? | Service levels; incidents | Move the users and the run to the Receiver, or to what replaces the Service | The Receiver accepts the Handover, or the steps of retirement are done |
| Handed over or Retired | Retire | None | None | The Service is Closed; after a Handover AICC oversees it as an Adopted Solution | None |

## 2. The reviews

2.1. The Domain Owner reviews each live Service at the Iteration Review and Demo on its four signals and the notices of its providers, and the Executive Sponsor does for a Service across Domains (Solution Lifecycle Model 8.4). The same person decides a transition, to hand the Service over or to retire it under its sunset rule, on the reading of its four signals at the quarterly Steering, and the AICC Lead enters the decision in the Decision Log and the Solution Definition (Solution Lifecycle Model 8.11).

## 3. The Handover to scale

3.1. A Service that the Bank should run at scale is not scaled by AICC. It goes through Transition planned and Migrating to an IT function of the Bank, on a Proposal that names the Receiver, and it is Closed as handed off when the Receiver accepts the Handover; AICC then oversees it as an Adopted Solution (Solution Lifecycle Model 8.2, 8.11).

## 4. Rule source

Solution Lifecycle Model 8.4 and 8.8 to 8.12; Business Model 2.5 and 4.2; Operating Model 4.2 and 6. The service steps draw on the practice of service portfolio management recorded in Standards and frameworks.
