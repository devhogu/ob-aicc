```yaml
id: AICC-POL-03-EN
title: Risk Tier Policy
status: draft
revision: 0.2
created: 2026-09-29
revised: 2026-09-30
```

# Risk Tier Policy

## 1. Purpose and scope

1.1. This policy states how a Use Case is assigned a Risk Tier and the requirements that each Risk Tier imposes.

1.2. It applies to every Use Case of the Bank and of each Participating Entity, whether the Solution is built or bought.

## 2. Risk Tiers

2.1. There are four Risk Tiers.

| Risk Tier | Name | Description |
| --- | --- | --- |
| 1 | Minimal | AI is used for personal productivity on data that is not confidential. It uses no customer data, does not influence a decision, and its output is reviewed by the user |
| 2 | Limited | AI is used with internal or confidential data. Its output informs the work of employees and is not customer-facing. It does not support a decision in a regulated process |
| 3 | High | AI uses personal or customer data, or its output supports a decision about a customer, an employee, a credit, a transaction, or a regulatory obligation, or is customer-facing under human review |
| 4 | Critical | AI takes or carries out an action or a decision without review by a person in a regulated process, or an agent has rights to act on systems or on funds, or AI decides on credit or insurance for a natural person |

## 3. Assignment

3.1. The Risk Tier is assigned at Intake by the Control Function Contact of model risk, on the basis of the following
attributes of the Use Case: the class of data used; the influence of the AI on a decision; whether the output reaches a
customer; the degree of autonomy; the regulatory regime of the Entity; whether the effect can be reversed; the scale of
use; and the provider.

3.2. The highest Risk Tier that any attribute indicates applies.

3.3. The Control Function Contact of another Control Function may raise the Risk Tier for its remit. Only the Control Function
Contact of model risk may lower it.

3.4. A Use Case in a category that the law treats as high risk is assigned at least Risk Tier 3.

3.5. The Risk Tier is recorded on the Risk Tier assessment and in the AI Registry.

## 4. Requirements

4.1. Each Risk Tier imposes at least the following requirements. A higher Risk Tier includes the requirements of the lower
tiers.

| Requirement | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
| --- | --- | --- | --- | --- |
| Use Case card | Required | Required | Required | Required |
| Recording in the AI Registry | Required | Required | Required | Required |
| Impact Assessment | Not required | Not required | Required | Required |
| Validation | Check by a person other than the owner, recorded in the AI Registry | Review of the documentation by the Control Function Contacts | Validation by the Control Function Contacts of model risk and of each remit concerned | Validation, and review at the Control Review |
| Human oversight | The user reviews the output | The user reviews the output | A person decides each case | Oversight designed with the authority to stop, and no autonomy without the decision of the AI Steering Committee |
| Testing for bias and error | Not required | Required for material use | Required before release and in monitoring | Required before release and in continuous monitoring |
| Monitoring | Periodic | Periodic | Continuous | Continuous, with alerts |
| Disclosure to customers | Not applicable | Not applicable | Required | Required |
| Contestability by a customer | Not applicable | Not applicable | Required | Required |
| Logging | As the AI Platform provides | Required | Required, with the retention that the rules require | Required, with the retention that the rules require |
| Approval to release | Domain Owner | Domain Owner | Domain Owner, after validation | AI Steering Committee, after validation |
| Reassessment of the Risk Tier | On change | On change | On change and each year | On change and each six months |

## 5. Reassessment

5.1. The Risk Tier is reassessed when the scope, the data, the Solution, the provider, or the regulatory regime changes, and
at the interval in section 4.1.

5.2. A change that raises the Risk Tier returns the Use Case to Discovery.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 0.1 | 2026-09-30 | Drafted. | none |
| 0.2 | 2026-09-30 | Iteration 3 of INI-001: F-009, F-038. | DR-2026-002, DR-2026-008 |
