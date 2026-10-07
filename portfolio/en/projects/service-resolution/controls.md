---
key: "controls"
label: "Controls and evidence"
section: "Solution"
---

## Controls and evidence {#controls-controls-and-evidence}

This page is written for the Control Function Contacts and for the people who decide on the pilot. For each obligation it shows the mechanism that meets it, who meets it, who checks it, and the record that holds the evidence. The rules themselves are in the AI Policy, the Solution Lifecycle Model and the Standards Record. The evidence is kept in the Solution Definition, the AI Registry and the Control Sign-Offs, not on this page.

### Expected Risk Tier 2, and what keeps it there {#controls-risk-tier}

The Competence Center Lead assigns the Risk Tier when each Solution is defined and tells the Domain Owner; if the Competence Center Lead builds the Solution, the Executive Sponsor assigns it. Any Control Function Contact may raise it within their remit; only the model risk Contact may lower it. The Tier is the highest that any attribute indicates.

| Attribute | This pilot | Tier indicated | What holds it there |
| --- | --- | --- | --- |
| Class of data | customer personal data and confidential service records: contacts, cases, complaints, and the journey's status | 2 | the context contract lists the fields; the Domain Owner approves the use for the data class |
| Influence on a decision | informs the employee's explanation and next step; the employee decides each case | 2 | nothing happens until the employee decides; there is no default action |
| Output reaches a customer | only through the employee, after review | 2 | the workspace has no send function; drafts are marked "AI-drafted" |
| Degree of autonomy | an Assistant: no tools and no writes | 2 (an AI agent with rights over systems would be 3) | the model holds no credentials; every write is a workspace action that the employee clicks |

The Tier would rise with any write or tool held by the model, any customer-facing output without employee review, an external provider if a Contact raises the Tier for that reason, or a scale of use that a Contact judges material. For the Onboarding/KYC (know-your-customer) journey, compliance may raise it for its financial-crime context. Each of these is a significant change or a new Solution. At Tier 3 the release would pass to the Executive Sponsor.

### Data and model hosting {#controls-data-and-hosting}

| Topic | Mechanism | Who decides or checks | Record |
| --- | --- | --- | --- |
| Where the model runs | In the Bank. The in-Bank model is checked as a provider before it processes any data of the Bank, and the license of each open component and model is recorded. | information security, data protection and legal Contacts (provider check) | Control Sign-Off of the provider check; Solution Definition, section 3 |
| An external model | Not used unless three things are in place: the provider check (where data is processed and kept, training on the data, contract terms, fallback and exit); approval for the data class; and the Contacts' confirmation of the Bank's outsourcing and personal-information rules (Standards Record EXT-001, EXT-002). The contract forbids training on the Bank's data. Introducing one later is a significant change. | the same Contacts; the Domain Owner for the data class | Control Sign-Off; AI Registry "Models, versions, and providers" |
| Use for the data class and purpose | No customer data is used with AI, in discovery or later, before the Domain Owner approves the use, after the approvals the Bank's rules require from each source owner and from data protection. The Executive Sponsor approves instead if the Competence Center Lead built the Solution. | Domain Owner, or Executive Sponsor | AI Registry "Approved for", "Approved by and date" |
| Phase 1 data in the Lab | Read-only extracts, each with its source owner and class. Personal data is minimized and assessed before it enters. Nothing is written back. Access is by role and every action is logged. Any re-identification key is kept outside the Lab and away from the model. | data protection Contact; source owners | Experiment block "Data extracts" and "Environment record"; Control Sign-Off of data protection |
| Phase 2 live reads | Only after validation. The context service reads only the fields in the context contract and drops any other before the model call. The customer segment is not read unless the journey needs it and data protection agrees. | data protection Contact at validation | context contract, referenced in Solution Definition section 3 |
| Purpose | Pilot outputs serve service resolution and the evaluation of the assistant only. Any other use needs its own approval for the data class and purpose. | Domain Owner; data protection Contact | Solution Definition, Conditions of use |
| Retention | Logs, snapshots and the pilot store are kept or deleted under the Bank's retention rules. At the end, access is removed and the AI Registry entry is marked retired. | Domain Owner approves the retirement | Solution Definition "Retirement or end" |

### Risk Tier 2 obligations and who meets each {#controls-tier-2-obligations}

| Obligation | How the pilot meets it | Meets it | Checks it | Evidence |
| --- | --- | --- | --- | --- |
| Solution Definition and AI Registry entry | One Solution Definition for each phase. The AI Registry entry reads, under AI agents and permissions: "none: Assistant; reads made by the workflow; writes are employee actions". | Solution Engineer; Competence Center Lead for the entry | Control Function Contacts at validation | Solution Definition; AI Registry |
| Validation | One Control Sign-Off for each remit (see [Validation by remit](#controls-validation-by-remit)). Its scope covers live use by the first users, the draft customer explanation, and any fallback model named in advance. | Control Function Contacts | each Contact within their remit | Control Sign-Offs, each with a valid-until date, conditions, and what the Solution shall not be used for |
| Security test against attacks on AI | Tests for prompt injection through customer messages and complaints, which are untrusted content; cross-customer access; data exfiltration; and the open components. | a tester who did not build the Solution | information security Contact | test report, referenced in the Control Sign-Off |
| Human oversight | The employee reviews every output and decides each case. No action happens without the employee's click. The manual route is always open. | Solution Engineer (design); Domain Owner (in operation) | model risk and compliance Contacts | the workspace decision record: the assistant's contribution and the employee's decision for each case |
| Testing for bias and error | See [Bias and error testing](#controls-bias-and-error). | tester who did not build | model risk and compliance Contacts | Solution Definition build notes; Outcome Report |
| Logs kept | For each case: the snapshot reference, the model and prompt version, the output, the result of each check, and the employee's decision and action. | Platform Owner provides the logging; Solution Engineer designs what is logged | information security and model risk Contacts | the logs, kept as the Bank's rules require |
| Disclosure, explanation and contestability | See [Disclosure](#controls-disclosure). | Domain Owner | compliance Contact | Control Sign-Off of compliance |
| Monitoring with alert levels | See [Monitoring](#controls-monitoring). | Solution Engineer states them; Platform Owner provides the monitoring; Domain Owner reviews | model risk Contact | Solution Definition, Conditions of use and "Review of the live Solution" |
| Knowledge sources | Every procedure the assistant uses is cited by section. Each source has an owner and a review date. | process function owns the procedures; Competence Center Lead notes the owners | model risk Contact | AI Registry |
| Training before first use | The first users are trained before they see any output. | Competence Center Lead sets the training; a Domain Expert delivers it | Domain Owner | AI Registry "Training of the users complete" (no names) |
| Release | Deployment to the first users after validation, the Team's final acceptance and the Bank's change management. Use beyond the first users only after the Acceptance Checklist is signed and the Domain Owner releases. | Competence Center Lead (Team final acceptance); change management of the Bank; Domain Owner (release) | every signatory of the Acceptance Checklist | release block of the Solution Definition; change ticket; Acceptance Checklist |
| Reassessment | On every change and each year. The provider check is repeated at each reassessment and on any change of the provider's terms or model. | Competence Center Lead; the Contacts for the provider check | model risk Contact | AI Registry "Reassess by" |

If the Competence Center Lead builds the Solution, the Competence Center Lead does not validate, release or give the business acceptance, and the test by another person is done by an engineer of the IT function or the Domain whom the Competence Center Lead names.

### Validation by remit {#controls-validation-by-remit}

| Control Function Contact | Questions the pilot answers | Mechanism or evidence presented |
| --- | --- | --- |
| Model risk | Does Tier 2 hold? Is the assistant accurate enough across case states, exceptions and languages? Does it add value over the context-only mode? Are the alert levels and the fallback right? | Tier attribute table; evaluation results on the locked cases, per state and per language; bias and error results; the context-only comparison; Conditions of use |
| Information security | Can the model reach a Bank system? Who can see the assembled context? Can one customer's data appear in another's case? Are the logs complete and protected? Does suspension work? | model has no credentials or network route; access by role and need-to-know, with an access-review owner; snapshot bound to one customer, with cross-customer tests; security test report; provider check; suspension test |
| Data protection | May the records be combined for service resolution? Which fields are necessary? How is sensitive case content handled? How long is anything kept? | purpose and legal basis; the context contract and its exclusions; the extract assessment; display and suppression rules for sensitive content; retention rules |
| Compliance (including anti-money laundering and consumer protection) | Which laws apply, and is the Solution in a category the law treats as high risk? What may be said to the customer, and how is AI involvement disclosed? Could some customers get poorer service? For Onboarding/KYC, is the financial-crime boundary held? | the applicable law, confirmed and recorded (Standards Record EXT-001 to EXT-004 still read "Applies, to confirm"); the disclosure form; bias and error results; the KYC "no data path" boundary and its tests |
| Legal | Do the provider and license terms allow this use? Are legal deadlines and customer rights in the journey protected? | contract terms (no training, fallback, exit); licenses in the Solution Definition; deadline-sensitive cases referred as the journey annex states |

### Readiness evidence for each decision {#controls-readiness-evidence}

Readiness for live use is not a separate approval. The evidence on architecture, data, controls, operability and quality is what the deciders below read. In the Competence Center flows these are not approvals. Their content is the evidence that the corpus deciders read. The IT items are listed in detail on the [IT readiness checklist](#it-readiness).

| Former gate | Evidence | Decision it supports | Decided by | Record |
| --- | --- | --- | --- | --- |
| Architecture | journey profile completed and consistent with the journey annex; disposition and owner of each capability; temporary components named; journey logic kept apart from AI Platform functions | approval of the Solution Definition | Domain Owner (Executive Sponsor if the Competence Center Lead built it) | Solution Definition, section 3 |
| Data and integration | sources, identifiers, status meanings and read paths confirmed; field and knowledge lists tested; extracts recorded with owner and class; personal data assessed | approval for the data class; entry of data into the Lab | Domain Owner with the source owners; data protection Contact | AI Registry; Experiment block; Control Sign-Off |
| Controls | identity, purpose, field access, model route, retrieval and output checks enforced and logged; prohibited data, decisions and actions blocked in code; threat model, incident path and suspension recorded | validation; provider check | Control Function Contacts | Control Sign-Offs |
| Operability | environments, deployment, secrets, logging, fallback and support exercised; manual route works when a dependency fails; incident path in the Bank's incident management; monitoring on, with alert levels and who watches them | Team final acceptance; first deployment to production | Competence Center Lead; change management of the Bank | release block; change ticket |
| Quality | results on the locked cases for common states and material exceptions; no critical error found; correction, escalation and outcome recording work end to end; each Feature tested by someone other than its builder | Team final acceptance; business acceptance | Competence Center Lead; Domain Owner | test references in the Features; Outcome Report |

A run in production with the output hidden from the employees (a silent run) is already a deployment: it comes after validation, the Team's final acceptance and the Bank's change management, not before them.

### The acceptance rule {#controls-acceptance-rule}

This is the one acceptance rule of the pilot. Other pages link to it. It has two parts and one decision.

**Part 1: mandatory gates.** They are acceptance criteria in section 5 of the Solution Definition. They are first applied to the locked cases in the Lab, and the Outcome Report shows the result; a Service is defined only if they pass there. The Competence Center Lead applies them at the Team's final acceptance, and the Domain Owner applies them to the working Service with its first users at the business acceptance. If a gate fails, the Service is returned or rejected.

| Gate | Acceptance criterion |
| --- | --- |
| Traceability | Given any fact, status or earlier action on screen, when the employee opens its source reference, then it leads to the record and version held in the case snapshot. |
| Authoritative status | Given a case, when the workspace shows its state, then the state is the value from the journey system, never text from the model. |
| Critical-error handling | Given the locked cases, when they are evaluated, then no critical error is found. A critical error found at any point blocks the first deployment, or the next release, until it is corrected and retested. A sample cannot prove that no error exists; this gate checks that none is found. |
| Quality floor | Given a sample of state and next-step interpretations, when Domain Experts review them, then quality is at or above the floor in the journey annex. The process function may raise the floor, not lower it. |
| Manual route | Given a missing, stale, conflicting or uncertainly linked record, when the case is opened, then no AI output is shown and the case goes to manual investigation. |
| Action limit | Given an output that is not an approved code for the verified state, then it is discarded and no step is proposed. Given any write, then it carries the employee's identity and click. |
| Control limits | Given the observation period, then every control limit stays within its tolerance and no zero-tolerance event occurs. |
| Process approval | Given the action list and the outcome definitions, then the process function has approved them, recorded as a Dependency met. |
| Recording | Given any correction, accepted action, escalation or result, then it is recorded in the pilot store. |

**Part 2: leading indicators.** Two to four indicators are set in the Initiative Brief: customer outcome, handling effort, and use of the assistant on eligible cases, with one indicator for the journey. Each is a reference to its source and its owner, not a figure on the portal. The comparison design, the observation period and the number of cases needed are in the measurement annex. Both are on the [Charter](#charter) page.

**The decision after the minimum viable product (MVP).** The approver of the business case (the Domain Owner, or the Executive Sponsor if the Initiative spans Domains) reads the evidence and decides.

| Evidence | Decision | What follows |
| --- | --- | --- |
| Gates pass; the indicators meet their targets; the Domain Owner sees the value | Continue | Capabilities enter the Program Backlog; use beyond the first users after the Acceptance Checklist; later a Proposal and a Handover to an IT function of the Bank as Receiver |
| Gates pass; the indicators point the right way, but there are too few cases for the claim | Return, with a stated extension | the MVP is extended by a stated number of Iterations, with what is missing, in the Decision Record and an amendment of the Brief |
| The need is confirmed, but the approach or scope must change | Pivot | a new linked Initiative; a narrower scope within the same hypothesis is an amendment of the Brief |
| Timing, a Dependency, or a higher priority | Defer | a reason and a date; the Decision Record states whether the first users keep the accepted Service |
| A gate fails and cannot be corrected; no value is seen; the state cannot be shown reliably; or a control limit cannot be held | Reject | the Service is retired: access removed, data handled, AI Registry entry marked retired |

The gain of the assistant over the context-only mode is an input to this decision, not a pass or fail test. If the linked records alone give most of the improvement, that supports investing in the context integration and limiting further model investment. A stop by a Control Function Contact within their remit is final.

### Control limits and zero-tolerance events {#controls-control-limits}

Before the first users see any output, section 7 of the Solution Definition states each control limit with its measure, source, owner, tolerance, review frequency and alert level. Zero-tolerance events are listed apart from the limits that are monitored against a tolerance.

| Zero-tolerance event | What prevents it | How it is detected |
| --- | --- | --- |
| A legal or scheme deadline missed because of the assistant | deadlines come only from the source systems and are not in the model's output format; deadline-sensitive cases are referred as the journey annex states | case review; complaints |
| Loss of a customer right | cases where rights are decided are out of scope by the eligibility rules; the complaint and human-service routes stay open | case review; complaints |
| Disclosure to someone not entitled to it, including data of another customer | the snapshot is bound to one customer; access is by role and need-to-know; cross-customer tests at validation | log checks; employee reports |
| A message reaching a customer without an employee sending it | the workspace has no send function | channel records compared with the pilot store |
| A write without the employee's action | the model has no write path; each write carries the employee's identity and click | log reconciliation |
| A prohibited action or a regulated decision put to the employee as a next step | only approved codes for the verified state pass the output check | output-check log |
| Bypass of a mandatory control, or critical customer harm | the checks above run in code before display; the manual route is always open | monitoring; incident reports |

Each zero-tolerance event is an AI Incident. Anyone who sees one reports it through the Bank's incident channel and states that AI is involved. The Bank's incident management notifies the Competence Center Lead, who enters it in the Risks and Issues Record and may suspend the Service.

The monitored limits include complaints about the journey, employee corrections and rejections, the age of unresolved cases, repeat contacts, and the share of cases sent to the manual route. None may get worse than its baseline by more than the agreed tolerance. A crossed alert level triggers a review by the Domain Owner. The validation conditions may name the levels at which the Competence Center Lead suspends.

### Monitoring: alert levels and who watches them {#controls-monitoring}

The Solution Engineer states each alert level in section 7 of the Solution Definition, and the Contacts agree it at validation. The values are fields to fill, not set here. The Platform Owner provides the logging and monitoring. The Domain Owner reviews the four signals (service levels, incidents, use and cost) and the provider notices at each Iteration Review and Demo, and notes the review in the Solution Definition.

| Signal | What is measured | Alert level | Watched by |
| --- | --- | --- | --- |
| Performance | quality on a regular sample of live cases reviewed by Domain Experts who did not build the Solution, by language; the share of outputs with statements removed | [Solution Engineer, Solution Definition section 7] | Solution Engineer, as the operating function; Domain Expert for the sample |
| Drift | changes in the language mix, case types, proposed action codes, retrieval misses, and the share of cases sent to the manual route | [Solution Engineer, Solution Definition section 7] | Solution Engineer |
| Human override and correction rate | accepted, corrected and rejected outputs by week | [Solution Engineer, Solution Definition section 7] | Solution Engineer; the Service Operations Manager for the team's use |
| Incidents | AI Incidents, near misses and zero-tolerance events | any event | the Bank's incident management; Competence Center Lead |
| Cost | cost per case and per month against the cost limit | [cost limit, Solution Definition section 7] | Solution Engineer; Domain Owner, whose Domain pays the run cost |
| Service levels | availability, response time, and how often the context-only mode is used | [Service Agreement response targets] | Solution Engineer |

### Suspension and the manual route {#controls-suspension}

- **Who suspends.** The Competence Center Lead or any Control Function Contact. The suspension and its lifting are entered in the Decision Log; the lifting records the evidence that the cause was corrected and retested.
- **The team's own switch.** The Service Operations Manager may move the team to the existing process at any time. This is not a suspension, and they tell the Competence Center Lead the same day.
- **How it works.** Three switches: generation off (the workspace stays in the context-only mode), one action off, or the whole workspace off. None of them deletes the record of use. All three are tested before the first users see output.
- **Fallback.** The context-only mode and the manual route are always allowed. A second model may be used only if it was validated in advance and named as the fallback in the Solution Definition. Nothing switches automatically to another model or provider, and nothing widens the group of users automatically.

### Disclosure, explanation and contestability {#controls-disclosure}

- **What reaches the customer.** Only what the employee says, or a written reply the employee edits and sends from the existing channel. The assistant only drafts.
- **Disclosure.** At Tier 2, output that reaches a customer is disclosed. The Domain Owner puts the disclosure in place before the first users see output; the compliance Contact decides its form at validation (for example, a sentence in written replies, and what the employee says if asked on the phone).
- **Marking.** Every draft is marked "AI-drafted" in the workspace. A "use draft" button copies it into the channel and logs that the draft was used.
- **Explanation.** The employee explains from the source records on screen, not from the model's text.
- **Contestability.** A customer who disputes an explanation uses the existing complaint and correction routes; the case record shows the source facts that were used.

### Bias and error testing {#controls-bias-and-error}

- **What is compared.** Error rates for state, blocker, next step, unsupported statements and draft quality, across cohorts agreed with the data protection and compliance Contacts: for example, the language of the records, the contact channel, the region and the case type. The cohorts use only fields already in the context contract or in the labels of the evaluation set.
- **When.** In the Lab on the locked cases, before the result is read; again before the first deployment to production; and in monitoring, on the reviewed sample of live cases.
- **Who.** Domain Experts label the locked cases, which are owned by people who did not build the Solution. A tester other than the builder runs the tests. The model risk and compliance Contacts check the results at validation.
- **What follows.** A material difference between cohorts sends the affected cohort to the manual route by an eligibility rule until it is corrected and retested. The result is recorded in the build notes of the Solution Definition and in the Outcome Report.

### Significant changes {#controls-significant-changes}

Every change is a Feature. These are significant: a change of model, model version, provider or model route; a field or data class beyond the context contract; any write or tool held by the model; customer output without employee review; a second journey; and any change the validation named. For each, the Competence Center Lead decides whether a new validation is needed and records it in the Decision Log; the change needs the Team's final acceptance and is released by the Domain Owner. Changes to prompts, output formats or the procedure set run against the locked cases first, and the Competence Center Lead decides whether they are significant. Use by more people than the first users is a release decision, not a change.

### Records that hold the evidence {#controls-records}

| Record | What it holds for this pilot |
| --- | --- |
| Solution Definition (Experiment; Service) | architecture and data, Risk Tier, acceptance criteria, release block, Conditions of use with the control limits and alert levels, reviews of the live Solution, changes |
| AI Registry entry | Tier, data classes, model and version, providers, knowledge-source owners, "none" under AI agents, approval for the data class, training complete, last validation, reassess-by date |
| Control Sign-Offs | business-case clearance, provider check, data assessment, and validation by each remit |
| Decision Log and Decision Records | new-validation decisions, suspensions and their lifting, the decision after the MVP |
| Risks and Issues Record; AI Incident Review | AI Incidents, their causes and the controls that failed |
| Outcome Report | the phase 1 result on the locked cases, and the outcome of the Engagement |
| Acceptance Checklist | the signed items before any use beyond the first users |
