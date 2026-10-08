```yaml
id: AICC-POL-01-EN
title: AI Policy
status: draft
revision: 2.3
created: 2026-10-02
revised: 2026-10-07
```

# AI Policy

## 1. Purpose and scope

1.1. This policy states the rules for the use of AI in the Bank: the rules of use, the Risk Tiers and what each requires, AI from providers, and AI Incidents and Exceptions.

1.2. It applies to every use of AI, including the work of the Competence Center itself, whether the Solution is built or bought.

1.3. The Control Function Contacts of compliance and of legal shall confirm, each within its remit, which laws, regulations, and external standards apply to the use of AI in the Bank. The Competence Center Lead records each confirmation in the Standards Record, with who confirmed it and when.

1.4. The policies of the Bank on information security, data classification and protection, model risk where the Bank has one, change management, and procurement apply to AI. This policy adds to them and does not replace them.

## 2. Rules of use

2.1. Employees shall use only Solutions that are approved for the data class and the purpose and recorded in the AI Registry. The Domain Owner approves the use of a Solution in the Domain, and is responsible for obtaining any approval that the rules of the Bank require. The Competence Center provides the technical means and records the approval. The Competence Center Lead approves the use of a Solution in the Competence Center, and the Executive Sponsor does for a Solution that the Competence Center Lead built (Operating Model 4.4). An employee shall complete the training that the Competence Center sets for a Solution before first use, or use it first under supervision as training. The Competence Center Lead shall note in the AI Registry entry of the Solution when the training of its users is complete, without their names. The Competence Center Lead shall list the uses already in place on 2026-10-02 in the AI Registry by 2026-12-31. Such a use is tolerated until the Domain Owner has approved it or stopped it, and in any case not beyond 2026-12-31.

2.2. The data classification rules of the Bank apply to AI. Data of a class shall not be sent to a model or a service that is not approved for that class. Data of a class for which no Solution is approved shall not be used with AI at any point, including discovery, until the Domain Owner has obtained the approvals that the rules of the Bank require.

2.3. A named person is accountable for each Solution and its outcome. The person who relies on AI output, or signs it, is accountable for it. A person shall review AI output before it is relied on, except where the Risk Tier allows otherwise.

2.4. AI output that reaches a customer shall be identified as AI output where the Risk Tier requires it. AI output published to investors, lenders, regulators, or the Board shall be approved by the Executive Sponsor before it is issued, and the review and the approval shall be recorded for each edition. The Executive Sponsor may name a delegate in the Appointments Record. The person accountable for AI output that the Bank publishes shall make sure that it respects the rights in the material used to produce it and is traceable to its governed source. AI output is content that AI drafted or produced.

2.5. No person shall use AI to bypass a control, a limit, or a Decision of a Control Function. AI that uses personal data shall use only the data that the Solution requires. AI that records or transcribes a meeting shall be used only with the consent of all participants.

2.6. No person shall enter an internal document, or data of the Bank other than public data, into an external site, form, tool, or model that is not an approved Solution, except a use tolerated under 2.1 until the date stated there. A model or a service enters the Bank only through the provider check of 4.1.

2.7. For each unapproved use of AI that is reported, the Competence Center Lead shall list it in the AI Registry and propose to the Domain Owner an approved Solution that serves the need, or the stop of the use. A reported use is tolerated only as 2.1 states.

## 3. Risk Tiers

3.1. There are three Risk Tiers, which the following table states. The Risk Tier of a Solution is the highest that any of its attributes indicates. The attributes are the class of data, the influence of the AI on a decision, whether the output reaches or affects a customer, and the degree of autonomy. A Control Function Contact may raise the Risk Tier for any other reason within its remit, such as the scale of use, the provider, or whether the effect can be reversed.

| Risk Tier | Name | Description |
| --- | --- | --- |
| 1 | Low | Personal productivity on data that is public or unclassified under the rules of the Bank; no customer data; no influence on a decision; the user reviews the output |
| 2 | Medium | Internal, confidential, personal, or customer data; output that informs work or a decision, or reaches a customer under human review |
| 3 | High | AI that decides or acts without review in a regulated process; an AI agent with rights over systems or funds; a decision on credit or insurance for a natural person that the AI takes without review |

3.2. The Competence Center Lead shall assign the Risk Tier when the Solution is defined, using the attributes in 3.1, and shall inform the Domain Owner of the Risk Tier assigned. The Executive Sponsor assigns it for a Solution that the Competence Center Lead built (Operating Model 4.4). A Risk Tier assigned that is higher than the one that the business case expected or that the Control Function Contacts cleared returns the business case to them for clearance (Portfolio Management Model 6.4). The Contact of any Control Function may raise it within its remit, and only the Contact of model risk may lower it. A Solution in a category that the law applicable to the Bank treats as high risk is at least Risk Tier 2. The person who checks a Risk Tier 1 Solution, and the Control Function Contacts at the validation of a Risk Tier 2 or 3 Solution, confirm the Risk Tier and ask whether the Solution is in such a category.

3.3. The requirements of each Risk Tier are in the following table. A higher Risk Tier includes the requirements of the lower.

| Requirement | Risk Tier 1 | Risk Tier 2 | Risk Tier 3 |
| --- | --- | --- | --- |
| Solution Definition and AI Registry entry | Required | Required | Required |
| Validation | A check by a person other than the builder, noted in the AI Registry | Validation by the Control Function Contacts of model risk and of information security, and of each other remit concerned where the output reaches or affects a customer or the Solution uses personal data; it includes a security test against attacks on AI, which covers prompt injection where the Solution reads untrusted content, and the open components of the Solution (4.4) | The same, with review at the quarterly risk check |
| Human oversight | The user reviews the output | A person reviews the output; a person decides each case that affects an individual | Oversight designed with authority to stop; no autonomy without the release decision of the Executive Sponsor |
| Testing for bias and error | Not required | Before the first deployment to real users or data, and in monitoring, where the output affects persons | Before the first deployment to real users or data, and continuously |
| Monitoring and logging | Periodic | Logs kept | Continuous, with alerts, and logs kept as the rules require |
| Disclosure, explanation, and contestability | Not applicable | Where the output reaches or affects a customer | Required |
| Release | The Domain Owner, after the check | The Domain Owner, after validation | The Executive Sponsor, after validation |
| Reassessment of the Risk Tier | On change | On change and each year | On change and each six months |

Where the Competence Center Lead is the Domain Owner, the Executive Sponsor releases a Solution of Risk Tier 1 or 2 (Operating Model 4.4(d)).

3.4. A change that raises the Risk Tier, or that the check or the validation named as requiring a new check, returns the Solution to discovery for the checks that the change touches. A validation states the date until which it is valid and the changes that require a new one. Use continues unless the Competence Center Lead or a Control Function Contact suspends it, and a suspension and its lifting are entered in the Decision Log (Operating Model 5.4), except that a Solution whose Risk Tier rises to 3 shall not be used beyond its first users until the Executive Sponsor releases it.

3.5. The Solution Engineer shall meet the requirements for the design of human oversight, testing, and logging. The Domain Owner shall meet those for oversight in operation, disclosure, and contestability. The Platform Owner shall provide logging and monitoring. The Control Function Contacts check them at validation. The Competence Center Lead reassesses the Risk Tier. The Domain Owner, or the Executive Sponsor for a Service across Domains, reviews monitoring and provider notices at each Iteration Review and Demo. The Competence Center Lead sets the training and notes the owners of knowledge sources in the AI Registry. For Risk Tier 2 and 3 the validation replaces the check. A condition of a validation may state what the Solution shall not be used for.

3.6. The Solution Engineer shall give an AI agent only the functions, permissions, and autonomy that its task needs, within what its Risk Tier allows and as the AI Registry records, shall have its actions logged, and shall provide a way for a person to stop it on a channel that the AI agent cannot influence.

3.7. The Solution Engineer shall state in the Solution Definition what the Solution is for, how it was tested, and what it shall not be used for; the alert levels of its monitoring and who watches them; and, where it relies on a provider, its cost limits and its fallback. The monitoring covers performance, drift, the human override and correction rate, incidents, and cost, and an alert level that is crossed triggers a review by the Domain Owner. The Competence Center Lead reassesses the Risk Tier when defects are found in operation after the check or the validation.

## 4. AI from providers

4.1. A provider of models or services shall be checked before use by the Control Function Contacts of information security, data protection, and legal: where data is processed and kept, whether the provider may train on it, the contractual terms, and the arrangements to fall back and to exit. The check is repeated at each reassessment and on a change of terms or model. For a Risk Tier 1 Solution, and for a provider already checked, the Contact of information security alone checks. The Competence Center Lead reports in the Quarterly Report the concentration of the Bank on one provider.

4.2. The Bank is answerable for AI that it buys to the same extent as for AI that it builds. The same Risk Tiers apply.

4.3. The contract with a provider shall forbid it to train on data of the Bank that is not public, unless the Control Function Contact of data protection permits it, and the check of 4.1 confirms the term.

4.4. A model that the Bank runs itself, including an open model, is checked as a provider under 4.1 before it processes data of the Bank. The Solution Engineer shall record in the Solution Definition the license of each open component, model, and dataset that the Solution uses.

## 5. AI Incidents

5.1. An AI Incident is an event in which the use of AI causes, or could cause, harm, a breach of law or policy, or a loss of control. It includes harm to a customer or an employee, a leak or misuse of data, an attack on or through an AI system, an action of an AI agent beyond its limits, a material failure of a Solution, and a near miss.

5.2. An AI Incident is an incident of the Bank and is handled in the incident management of the Bank, in Service Management. That process owns the classification, the escalation, the communication, and the reporting to the authorities, and it meets the requirements that apply to the Bank for ICT-related incidents, for personal data breaches, and for the incidents of AI systems. The Control Function Contacts of compliance and of legal confirm which of those requirements apply to the Bank (1.3). The Competence Center sets no severity scale and no time limit of its own.

5.3. The IT function that operates a Solution is responsible for its operation and for the handling of its incidents. For a trial in the Competence Center, and for a Service that the Competence Center runs, the Solution Engineer acts as that function.

5.4. Anyone who becomes aware of an AI Incident shall report it through the incident channel of the Bank and shall state that AI is involved. The incident management of the Bank shall notify the Competence Center Lead of every AI Incident.

5.5. The Competence Center Lead is a stakeholder in every AI Incident. The Competence Center Lead advises on the aspects that concern AI, such as the Risk Tier, the data, the models and providers, and the controls of the Solution, and may bring the Solution Engineers of the Solution to join the incident. The Competence Center Lead enters the AI Incident in the Risks and Issues Record with the key of its ticket.

5.6. The Competence Center Lead or any Control Function Contact may suspend a Solution. The Control Function Contacts assess an AI Incident within their remits: compliance decides whether a regulator is notified, and data protection decides whether a person whose data is affected is notified, as the law requires and in the time that the incident management of the Bank sets. Providers are told as the contract requires.

5.7. The Competence Center Lead informs the Executive Sponsor of an AI Incident that the incident management of the Bank classifies as major, and the Executive Sponsor tells the Board Committee as the incident management of the Bank requires, without waiting for any report (AI Competence Center Charter 7.2).

5.8. The post-incident review of an AI Incident is held in the incident management of the Bank, in the time that it sets. The Competence Center Lead takes part, reassesses the Risk Tier of the Solution, and records what concerns AI in the AI Incident Review and in the Risks and Issues Record: the cause, the controls that failed, and the change to the Solution or to the Standards. The Competence Center Lead shall carry the lessons of the AI Incident into the Solution, the Standards, or the training that the Competence Center sets.

## 6. Exceptions

6.1. A departure from this policy is an Exception. An Exception is permitted only in exceptional cases. It is decided by the Control Function Contact for the remit concerned, is limited in time, shall state the date on which it expires, and shall be entered in the Risks and Issues Record. The Executive Sponsor reviews the open Exceptions each month, and an Exception that has expired is decided at once (Operating Model 6.7). A departure from a requirement set by the Competence Center alone is decided by the Competence Center Lead. An Exception is not a bypass of a control.

6.2. The controls of this policy are C-06, C-09, C-12, C-13, C-15, C-16, C-17, C-18, C-21, C-28, and C-29 of the Operating Model 8.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 1.0 | 2026-10-02 | Baseline. | — |
| 2.0 | 2026-10-03 | Adds the confirmation of the laws and standards that apply and the policies of the Bank that apply, accountability for AI output, the bar on entering data into unapproved external services, the handling of unapproved use, the rules for AI agents, documentation, monitoring, and provider training, open models and licenses, and the lessons of an AI Incident. | — |
| 2.1 | 2026-10-04 | Applied fixed international AI agent naming consistently; functional meaning and decision rights are unchanged. | none (correction under Document Catalog 4.2) |
| 2.2 | 2026-10-05 | Stated in 6.1 that an Exception is permitted only in exceptional cases. | none (correction under Document Catalog 4.2) |
| 2.3 | 2026-10-07 | The unit is named the Competence Center, and the AI Competence Center in titles; the role AICC Lead is the Competence Center Lead; AICC stays only as a code | — |
