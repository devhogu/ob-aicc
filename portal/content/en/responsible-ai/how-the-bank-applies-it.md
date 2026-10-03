# How the Bank applies it

The principles of responsible AI become the Bank's rules in the AI Policy and in the AI Risk Appetite Statement, and they become practice in the way AICC and the functions work. This page explains the rules in plain terms for the person who will use AI, build it, or approve it. The AI Policy is the rule and prevails; this page is the explanation.

## 1. What the Bank accepts and does not accept

1.1. The Bank accepts risk from the use of AI where the benefit is measured and the controls are proportionate to the risk. It does not accept a breach of law or regulation. It accepts only a low level of risk of harm to customers and of loss or misuse of confidential or personal data. It accepts a moderate level of risk of error in internal productivity uses where a person reviews the output. It does not accept AI that takes a decision without review in a regulated process, or an agent that acts on systems or funds, without validation by the Control Functions and the release decision of the Executive Sponsor.

1.2. This is the AI Risk Appetite Statement of the AICC Charter. Every use of AI is assessed against it, and a risk beyond it may be accepted only by the Executive Sponsor, with a report to the Board Committee.

## 2. The Risk Tiers

2.1. Every Solution carries a Risk Tier, assigned by the AICC Lead when the Solution is defined, or by the Executive Sponsor for a Solution that the AICC Lead built, and recorded in the AI Registry. The tier is the highest that any of four attributes indicates: the class of data, the influence of the AI on a decision, whether the output reaches or affects a customer, and the degree of autonomy. A Control Function Contact may raise it for any other reason within its remit, such as the scale of use, the provider, or whether the effect can be reversed, and only the Contact of model risk may lower it. The tier sets the validation, the human oversight, the testing, the monitoring, the disclosure, and the release that apply, and a higher tier includes the requirements of the lower.

| Risk Tier | What it covers | What it requires, in short |
| --- | --- | --- |
| 1, Low | Personal productivity on public or unclassified data; no customer data; no influence on a decision; the user reviews the output | A Solution Definition and an AI Registry entry; a check by a person other than the builder; periodic monitoring; release by the Domain Owner after the check; reassessment on change |
| 2, Medium | Internal, confidential, personal, or customer data; output that informs work or a decision, or reaches a customer under human review | Validation by the Control Function Contacts of model risk and information security, and of each other remit concerned, with a security test against attacks on AI; a person reviews the output and decides each case that affects an individual; testing for bias and error where the output affects persons; logs kept; disclosure, explanation, and contestability where the output reaches a customer; release by the Domain Owner after validation; reassessment on change and each year |
| 3, High | AI that decides or acts without review in a regulated process; an agent with rights over systems or funds; a credit or insurance decision on a natural person taken without review | The same, reviewed at the quarterly risk check; oversight designed with authority to stop and no autonomy without the release decision of the Executive Sponsor; continuous testing, monitoring with alerts, and logs as the rules require; disclosure, explanation, and contestability required; release by the Executive Sponsor after validation; reassessment on change and each six months |

2.2. A Solution in a category that the law applicable to the Bank treats as high risk is at least Risk Tier 2. A change that raises the tier returns the Solution to Discovery for the checks that the change touches, and a Solution whose tier rises to 3 is not used beyond its first users until the Executive Sponsor releases it. The table is the explanation; the AI Policy states the tiers and their requirements in full.

## 3. The rules of use for everyone

3.1. A person who uses AI at the Bank uses only the Solutions that are approved for the data class and the purpose and recorded in the AI Registry, and does not send data of a class to a model or a service that is not approved for it, at any point, including discovery. A person completes the training that AICC sets for a Solution before its first use, or uses it first under supervision as training. A person reviews the output of an assistant before it is relied on, except where the Risk Tier allows otherwise, and the person who relies on the output or signs it is accountable for it. A customer is told when the output reaches them where the Risk Tier requires it, can reach a person, and can contest a decision taken with the assistance of AI. Output published to investors, lenders, regulators, or the Board is approved by the Executive Sponsor before it is issued. Nobody uses AI to bypass a control, a limit, or a decision of a Control Function; AI that uses personal data uses only the data the Solution requires; and AI that records or transcribes a meeting is used only with the consent of all participants.

## 4. The gates before use

4.1. No Solution reaches real users or real data without passing its gates, in this order: the Risk Tier is assigned and the AI Registry entry made; the Domain Owner approves the use for its data class; a provider, where one is used, is checked by the Control Function Contacts of information security, data protection, and legal, or by the Contact of information security alone for a Risk Tier 1 Solution or a provider already checked; the Solution is checked by a person other than its builder for Risk Tier 1, or validated by the Control Function Contacts for Risk Tier 2 and 3; its users complete the training that AICC sets before first use; the Team gives its final acceptance; the Domain Owner accepts the working Solution as the requester; and the release beyond the first users is decided separately, with the Acceptance Checklist signed where the Solution is handed to a Domain. The Control Functions may stop a Solution at any gate and in use, and nobody overrides the stop.

## 5. AI from providers

5.1. The Bank is answerable for AI that it buys to the same extent as for AI that it builds. A provider of models or services is checked before use by the Control Function Contacts of information security, data protection, and legal, or by the Contact of information security alone for a Risk Tier 1 Solution or a provider already checked: where data is processed and kept, whether the provider may train on it, the contractual terms, and the arrangements to fall back and to exit. The check is repeated at each reassessment and on a change of terms or model. The same Risk Tiers apply to a bought Solution as to a built one.

## 6. When something goes wrong

6.1. An AI Incident is an event in which the use of AI causes, or could cause, harm, a breach of law or policy, or a loss of control. It includes harm to a customer or an employee, a leak or misuse of data, an attack on or through an AI system, an action of an agent beyond its limits, a material failure of a Solution, and a near miss. It is handled under the incident management of the Bank, with the AICC Lead as a stakeholder, and it is reviewed afterwards in an AI Incident Review: what happened, why, what was done, and what changes. The reviews are reconciled each quarter, a major incident is reported to the Board Committee without waiting for the next report, and the lessons go into the controls and the training.

## 7. Exceptions

7.1. A control requirement is not bypassed. A departure from the AI Policy is an Exception: it is decided by the Control Function Contact for the remit concerned, or by the AICC Lead for a requirement that AICC alone set; it is limited in time and states the date on which it expires; and it is entered in the Risks and Issues Record. The Executive Sponsor reviews the open Exceptions each month, and an Exception that has expired is decided at once. A risk beyond the AI Risk Appetite Statement is not an Exception: only the Executive Sponsor may accept it, with a report to the Board Committee.

## 8. Who does what

| Who | Responsibility |
| --- | --- |
| The person who uses AI | Uses approved Solutions within the rules, reviews the output, stays accountable for what they rely on or sign |
| The Domain Owner | Owns the results of the Solutions of the Domain, approves the use for a data class, accepts and releases, reviews each live Solution |
| The AICC Lead | Assigns the Risk Tier, keeps the AI Registry, sets the training, oversees the Portfolio, reports each quarter |
| The Control Function Contacts | Clear business cases of Risk Tier 2 and 3, check providers, validate, decide Exceptions in their remit, and may stop |
| The Executive Sponsor | Decides the risk appetite, releases Risk Tier 3 Solutions, accepts a risk beyond appetite, issues the report to the Board Committee |
| Internal audit | Gives independent assurance over the Portfolio and over AICC |
| The Board Committee | Oversees AI through the quarterly report and is told of major incidents and risks beyond appetite |

## 9. Where to read the rules

9.1. The regulators and the instruments the Bank is aware of are listed, with a page for each, on [Regulators and acts](../reference/regulators-and-acts.md), and what the applicable ones require of a use of AI is stated on [Acts and compliance](../knowledge-base/acts-and-compliance.md). The AI Policy states the rules of use, the Risk Tiers, the providers, the AI Incidents, and the Exceptions. The AI risk and control workflow shows how a Solution, a provider, and a use pass the controls. The Statement of Intent states the principles; the AICC Charter states the risk appetite; the Operating Model states the controls that can be tested and the Registry holds their evidence.
