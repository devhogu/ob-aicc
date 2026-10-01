```yaml
id: AICC-TPL-13-EN
title: Acceptance Checklist
status: active
revision: 2.1
created: 2026-10-01
revised: 2026-10-01
```

# Acceptance Checklist

**Template.** One checklist for each Solution when AICC hands it to a Domain as ready for use at scale, before its release beyond the first users. It is not used during development or trials, where the check and the validation of the Solution Lifecycle Model 6.1 apply. The AICC Lead completes it, each party answers and signs its items within its remit, and the Domain Owner receives it signed and signs the acceptance of the package. It is an evidence record and adds no approval of its own: the decisions are those of the parties under the AI Policy. It carries no figures of the Bank, no data, and no code.

| Field | Entry |
| --- | --- |
| Identifier | ACL-[nnn] |
| Solution | SOL-[nnn] |
| Receiver | [the Domain and the Domain Owner, or the Receiver named in the Solution Definition] |
| Risk Tier | [1 / 2 / 3] |
| Completed by the AICC Lead on | [date] |

**Result.** Met, Not met, or Not applicable with the reason. An item that is Not met stops the release. For a Risk Tier 2 or 3 Solution, the Contacts of model risk, compliance, information security, and legal answer every item of their party, and data protection answers where the Solution uses personal data. For a Risk Tier 1 Solution, the Checker and the Contact of information security answer. A Solution of Risk Tier 1 or 2, which is low or medium risk, is adopted by the Domain Owner on the risk of the Domain. A Solution of Risk Tier 3, which is high impact and high risk, is adopted only with the signature of the Executive Sponsor.

| Party | Item | Result | Evidence | Name, signature, and date |
| --- | --- | --- | --- | --- |
| Domain Owner | The Solution is received as ready for use, with its Solution Definition, its limits and conditions of use, and its support arrangements | [Met / Not met / Not applicable] | [Solution Definition] | [name, date] |
| Domain Owner | The use is approved for the data classes and the purpose (AI Policy 2.1) | | [AI Registry] | |
| Domain Owner | The users are trained, or use the Solution first under supervision as training | | | |
| Domain Owner | Oversight in operation, disclosure, and contestability are in place (AI Policy 3.5) | | | |
| Solution Engineer | The Solution is handed over to the Receiver named in the Solution Definition, who accepts the handover | | [Solution Definition] | |
| Solution Engineer | Human oversight, testing, and logging are in the Solution as built (AI Policy 3.5) | | | |
| AICC Lead | The Risk Tier is recorded in the AI Registry, with who assigned it and when | | [AI Registry] | |
| AICC Lead | The owners of the knowledge sources are noted, and the training is set (AI Policy 3.5) | | | |
| Checker (Risk Tier 1) | The Solution was checked by a person who did not build it, and the check holds for use at scale | | [AI Registry] | |
| Model risk | The validation holds for use at scale, with its conditions and its date | | [Control Sign-Off] | |
| Compliance | The applicable law is confirmed for use at scale, including whether the Solution is in a category treated as high risk (AI Policy 3.2) | | [Control Sign-Off] | |
| Compliance | Where the output reaches a customer, the disclosure and the right to contest meet the requirements | | | |
| Information security | The security requirements and the access are met for use at scale, and the providers are checked (AI Policy 4.1) | | [Control Sign-Off] | |
| Data protection | The lawful use of personal data, the retention, and the transfer or sharing are confirmed, where personal data is used | | [Control Sign-Off] | |
| Legal | The contracts, the intellectual property, the partners, and the liability, including the terms of the providers, are confirmed | | [Control Sign-Off] | |
| Executive Sponsor (Risk Tier 3) | The residual risk of adopting the Solution is accepted within the AI Risk Appetite Statement, or beyond it with a report to the Board Committee (Operating Model 5.4) | | [Decision Record] | |
| IT function that operates the Solution, and Platform Owner | The logging and the monitoring are provided for use at scale | | | |
| IT function that operates the Solution, and Platform Owner | The operating function is named, and the path of an incident in the incident management of the Bank is known (AI Policy 5) | | | |
| IT function that operates the Solution, and Platform Owner | The support is in place at the level that the Service Agreement states | | | |

## Conditions

[The conditions of any validation, with owner and date, and what the Solution shall not be used for.]

## Acceptance and release

[The Domain Owner accepts the package and releases a Solution of Risk Tier 1 or 2 on the risk of the Domain. The Executive Sponsor accepts the risk and releases a Solution of Risk Tier 3. Each decision follows when every item is Met or Not applicable, with the date and, for Risk Tier 3, the Decision Record.]
