# Service operations

The Business Model states that the support of a Service is managed in Service Management and that requests and incidents come to the queue of AICC. This page states the practices behind that sentence, sized to a small unit: how a request, an incident, a problem, a change, and a question are handled for a Service that AICC runs, what the service levels are, and what each practice leaves on record. It is the run-book template of a Service of AICC; each Service fills it in its Service Agreement and its Solution Definition.

## 1. The practices

| Practice | What it covers for a Service of AICC | Who acts | Record |
| --- | --- | --- | --- |
| Request handling | A request or a question from a consumer, triaged by class of service (Urgent, High priority, Normal), handled, and closed | The Solution Engineer; the AICC Lead for the class | The Service Management ticket |
| Incident handling | An outage or a failure; the incident management of the Bank applies; an AI Incident, where AI is involved, is reviewed as the AI Policy states, with the AICC Lead as a stakeholder | The incident management of the Bank; the Solution Engineer; the Control Function Contacts for an AI Incident | The incident record; the AI Incident Review |
| Problem management | A cause behind repeated incidents or requests, found and removed | The Solution Engineer; the Team at the Iteration Retrospective | A Feature in the Program Backlog; the Risks and Issues Record where a risk remains |
| Change enablement | A change or a new feature, raised by the Domain Owner or the product owner, built and verified as any Feature, deployed through the change management of the Bank; the AICC Lead decides whether a new check or validation is needed | The Team; the change management of the Bank | The change ticket and test reference; the Solution Definition; the Decision Log for a new-check decision |
| Knowledge | The user guide, the known errors, and the answers to recurring questions, kept with the Service and in the knowledge base of the function | The Solution Engineer with the Domain Expert | The Solution Definition; the Knowledge base |
| Service levels | The response targets of the Service Agreement, read at each Iteration Review and Demo; targets, not guarantees | The AICC Lead with the Domain Owner | The Service Agreement; the live review note |
| Run cost | The run cost against the business case, the licenses and the provider costs paid by the Domain from its Envelope, and the sunset rule | The AICC Lead; the Domain Owner | The business case; the Quarterly Report |
| Suppliers | The providers of models and services behind the Service: checked before use by the Control Function Contacts, with the fallback and the exit of each, and their notices read at each review | The Control Function Contacts; the Solution Engineer; the AICC Lead | The AI Registry; the Control Sign-Off of the provider check |

## 2. The classes of service

2.1. Unless the Service Agreement states otherwise: Urgent means a Service down or producing wrong output that reaches people, with a response within the day; High priority means a consumer blocked in a process with a date, with a response within the week; Normal is every other request, ranked in the backlog. The classes and these defaults are those of the Solution Lifecycle Model 8.5, and the response targets of each Service Agreement state what they mean for that Service.

## 3. The health of a Service

3.1. Four signals, read with the notices of the providers by the Domain Owner, or the Executive Sponsor for a Service across Domains, at each Iteration Review and Demo, and carried into the Quarterly Report: service levels met against the targets; incidents, including AI Incidents, by severity; use, the users who use the Solution each week; and cost, the run cost against the business case (Solution Lifecycle Model 8.4). The signals feed the service steps of the life of a Service and its sunset rule.

## 4. Sizing for a small unit

4.1. While the Team has up to three people, light mode applies: one queue, one weekly session for requests and problems, and the practices as a checklist in the Solution Definition rather than as separate procedures. The practices grow into procedures when the number of Services or the Risk Tier requires it.

## 5. Rule source

Business Model 4.2; Solution Lifecycle Model 6, 7, and 8, with the practices in 8.10; AI Policy 4 and 5; Operating Model 7 and 8. The practices draw on the IT service management practice recorded in the Industry body of knowledge.
