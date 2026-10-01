```yaml
id: AICC-POL-01-EN
title: AI Policy
status: active
revision: 1.1
created: 2026-09-30
revised: 2026-10-01
```

# AI Policy

## 1. Purpose and scope

1.1. This policy states the rules for the use of AI in the Bank and in each Participating Entity: the rules of use, the Risk
Tiers and what each requires, AI from providers, and AI Incidents and Exceptions.

1.2. It applies to every use of AI, including the work of AICC itself, whether the Solution is built or bought.

## 2. Rules of use

2.1. Employees shall use only Solutions that are approved for the data class and the purpose and recorded in the AI Registry. The
Domain Owner approves the use of a Solution in the Domain, and is responsible for obtaining any approval that the rules of the Bank
require. AICC provides the technical means and records the approval. The AICC Lead approves the use of a Solution in AICC. An employee shall complete the training
that AICC sets for a Solution before first use, or use it first under supervision as training. The AICC Lead shall list the uses already in place in the AI Registry within 90 days of the
activation of this policy. Such a use is tolerated until the Domain Owner has approved it or stopped it, and in any case for no longer than those 90 days.

2.2. The data classification rules of the Bank apply to AI. Data of a class shall not be sent to a model or a service that is not
approved for that class. Data of a class for which no Solution is approved shall not be used with AI at any point, including
discovery, until the Domain Owner has obtained the approvals that the rules of the Bank require.

2.3. A named person is accountable for each Solution and its outcome. A person shall review AI output before it is relied on, except
where the Risk Tier allows otherwise.

2.4. AI output that reaches a customer shall be identified as AI output where the Risk Tier requires it. AI output published to
investors, lenders, regulators, or the Board shall be approved by the Executive Sponsor before it is issued, and the review and the approval shall be recorded for each edition. The
Executive Sponsor may name a delegate in the Appointments Record. AI output is content that AI drafted or produced.

2.5. No person shall use AI to bypass a control, a limit, or a Decision of a Control Function. AI that uses personal data shall
use only the data that the Solution requires. AI that records or transcribes a meeting shall be used only with the consent of
all participants.

## 3. Risk Tiers

3.1. There are three Risk Tiers, which the following table states. The Risk Tier of a Solution is the highest that any of its attributes indicates. The
attributes are the class of data, the influence of the AI on a decision, whether the output reaches or affects a customer, and
the degree of autonomy. A Control Function Contact may raise the Risk Tier for any other reason within its remit, such as the
scale of use, the provider, or whether the effect can be reversed.

| Risk Tier | Name | Description |
| --- | --- | --- |
| 1 | Low | Personal productivity on data that is public or unclassified under the rules of the Bank; no customer data; no influence on a decision; the user reviews the output |
| 2 | Medium | Internal, confidential, personal, or customer data; output that informs work or a decision, or reaches a customer under human review |
| 3 | High | AI that decides or acts without review in a regulated process; an agent with rights over systems or funds; a decision on credit or insurance for a natural person that the AI takes without review |

3.2. The AICC Lead shall assign the Risk Tier when the Solution is defined, using the attributes in 3.1, and shall inform the Domain Owner of the
Risk Tier assigned. The Contact of any Control Function may raise it within its remit, and only the Contact of model risk may
lower it. A Solution in a category that the law of the Entity treats as high risk is at least Risk Tier 2. The person who checks a
Risk Tier 1 Solution confirms the Risk Tier and asks whether the Solution is in such a category.

3.3. The requirements of each Risk Tier are in the following table. A higher Risk Tier includes the requirements of the lower.

| Requirement | Risk Tier 1 | Risk Tier 2 | Risk Tier 3 |
| --- | --- | --- | --- |
| Solution Definition and AI Registry entry | Required | Required | Required |
| Validation | A check by a person other than the builder, noted in the AI Registry | Validation by the Control Function Contacts of model risk and of information security, and of each other remit concerned where the output reaches or affects a customer or the Solution uses personal data; it includes a security test against attacks on AI | The same, with review at the quarterly risk check |
| Human oversight | The user reviews the output | A person reviews the output; a person decides each case that affects an individual | Oversight designed with authority to stop; no autonomy without the release decision of the Executive Sponsor |
| Testing for bias and error | Not required | Before the first deployment to real users or data, and in monitoring, where the output affects persons | Before the first deployment to real users or data, and continuously |
| Monitoring and logging | Periodic | Logs kept | Continuous, with alerts, and logs kept as the rules require |
| Disclosure, explanation, and contestability | Not applicable | Where the output reaches or affects a customer | Required |
| Release | The Domain Owner, after the check | The Domain Owner, after validation | The Executive Sponsor, after validation |
| Reassessment of the Risk Tier | On change | On change and each year | On change and each six months |

3.4. A change that raises the Risk Tier, or that the check or the validation named as requiring a new check, returns the Solution
to discovery for the checks that the change touches. A validation states the date until which it is valid and the changes that
require a new one. Use continues unless the checker, the AICC Lead, or a Control Function Contact suspends it.

3.5. The AICC Engineer shall meet the requirements for the design of human oversight, testing, and logging. The Domain Owner
shall meet those for oversight in operation, disclosure, and contestability. The Platform Owner shall provide logging and
monitoring. The Control Function Contacts check them at validation. The AICC Engineer reassesses the Risk Tier, the Domain Owner reviews monitoring and provider notices at each IT Review, and the AICC Lead sets the training and notes the owners of knowledge sources in the AI Registry. For Risk Tier 2 and 3 the validation replaces the check. A condition of a validation may state what the Solution shall not be used for.

## 4. AI from providers

4.1. A provider of models or services shall be checked before use by the Control Function Contacts of information security, data
protection, and legal: where data is processed and kept, whether the provider may train on it, the contractual terms, and the
arrangements to fall back and to exit. The check is repeated at each reassessment and on a change of terms or model. For a Risk Tier 1 Solution, and for a provider already checked, the Contact of information security alone checks. The AICC Lead
reports in the Quarterly Report the concentration of the Group on one provider.

4.2. The Bank is answerable for AI that it buys to the same extent as for AI that it builds. The same Risk Tiers apply.

## 5. AI Incidents

5.1. An AI Incident is an event in which the use of AI causes, or could cause, harm, a breach of law or policy, or a loss of
control. It includes harm to a customer or an employee, a leak or misuse of data, an attack on or through an AI system, an action
of an agent beyond its limits, a material failure of a Solution, and a near miss.

5.2. Each AI Incident has a Severity of High, Medium, or Low. High is serious harm, a material breach or loss of data, a breach
that a regulator must be told of, or an agent acting beyond its limits with effect. Medium is limited or reversible harm, a
breach of policy, or a failure that affects a Domain. Low is a near miss or an event without harm.

5.3. Anyone who becomes aware of an AI Incident shall report it to the AICC Engineer of the Solution or to the AICC Lead, who
classifies the Severity and enters the AI Incident in the Risks and Issues Record. The report of a High Severity AI Incident goes at once to the
AICC Lead, to the Control Function Contacts, to the Platform Owner, to the Domain Owner, and to the Executive Sponsor, who tells the Board Committee without waiting for the next report.

5.4. The AICC Engineer shall contain the AI Incident, and the AICC Lead or any Control Function Contact may suspend a Solution.
The Control Function Contacts assess it within their remits: compliance decides whether a regulator is notified, and data
protection decides whether a person whose data is affected is notified, as the law of the Entity requires. Providers are told as
the contract requires.

5.5. Within ten working days after containment the people involved shall review what happened and what to change, without blame. The
AI Incident and its actions are entered in the Risks and Issues Record.

## 6. Exceptions

6.1. A departure from this policy is an Exception. It is decided by the Control Function Contact for the remit concerned, is
limited in time, and shall be entered in the Risks and Issues Record. A departure from a requirement set by AICC alone is
decided by the AICC Lead. An Exception is not a bypass of a control.

## 7. Until a Contact is named

7.1. The Executive Sponsor may name at any time, in the Appointments Record, who acts for a Control Function, including for an AI
Incident. The acting person is a member of that function named with the consent of its head, and is marked as acting. Until a Control Function has a Control Function Contact or an acting person, nothing that needs that Control Function
proceeds: no Risk Tier 2 or 3 Solution, no provider, and no Group Arrangement.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 0.1 | 2026-09-30 | Drafted: replaces the AI Use, Risk Tier, Third-Party AI, and AI Incident policies and the Exception rules; three Risk Tiers. | DR-2026-009 |
| 0.2 | 2026-09-30 | Fixes from the independent check: tools approval and training, Risk Tier attributes and interim assignment, release, revalidation, providers, incident chain, Until a Contact is named. | DR-2026-010 |
| 0.3 | 2026-09-30 | Second fixes from the independent check: Tier 1 data boundary, lighter Tier 2 validation, testing before the Pilot, acting Contacts, return to Discovery. | DR-2026-011 |
| 0.4 | 2026-09-30 | The Executive Sponsor approves AI output published to investors, lenders, regulators, or the Board. | DR-2026-014 |
| 0.5 | 2026-09-30 | Acceptance fixes: transition for existing uses, data before approval, Executive Sponsor approval recorded, Tier 3 credit wording, acting persons, incident chain, performers. | DR-2026-015 |
| 0.6 | 2026-09-30 | The Domain Owner approves the use of a Solution for a data class and obtains the approvals that the rules of the Bank require. | DR-2026-016 |
| 0.7 | 2026-09-30 | AICC assigns the Risk Tier and informs the Domain Owner; Control Function Contacts may raise it; the interim rule is no longer needed. | DR-2026-017 |
| 0.8 | 2026-10-01 | Activated by the AICC Lead. | DR-2026-018 |
| 0.9 | 2026-10-01 | Iteration Review replaces the Sync and Demo. | DR-2026-020 |
| 1.0 | 2026-10-01 | Event names use the short forms IT and IP. | DR-2026-023 |
| 1.1 | 2026-10-01 | Solution replaces Use Case; the Risk Tier is assigned when the Solution is defined; testing before the first deployment. | DR-2026-024 |
