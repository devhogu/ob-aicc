```yaml
id: AICC-TPL-01-EN
title: Solution Definition
status: active
revision: 1.0
created: 2026-10-02
revised: 2026-10-02
```

# Solution Definition

**Template.** Copy for each Solution when it is defined. The Solution Engineer and the Domain Expert complete it, the AICC Lead assigns the Risk Tier, and the Domain Owner approves it. For a Solution that the AICC Lead built, the Executive Sponsor approves the Definition and assigns the Risk Tier. It describes the Solution: its scope, methods, and architecture. It carries no figures of the Bank, no data, and no code. Keep it short, in one form.

| Field | Entry |
| --- | --- |
| Identifier | SOL-[nnn] |
| Title | [title] |
| State and Stage | [state, and Stage if in discovery or active] |
| Initiative | [INI-nnn] |
| Type | [Service / Product / Experiment] |
| Receiver | [who runs or adopts it after delivery; for an Experiment, "none yet, to be asked" is allowed] |
| Approved by the Domain Owner on | [date; for a Solution that the AICC Lead built, by the Executive Sponsor] |
| Approved for the data class by | [Role], on [date] (noted in the AI Registry); the Executive Sponsor for a Solution that the AICC Lead built (Operating Model 4.4(d)) |
| Time-box | [for an Experiment: the number of Iterations] |
| Domain, Domain Owner | [names] |
| Domain Expert, Solution Engineer | [names] |
| Date of last change | [date] |

## 1. The need and the outcome

[The routine work or problem, who does it, how it is done today, and the outcome wanted.]

## 2. Scope and capabilities

[The minimum scope that tests the hypothesis and what is excluded. The Capabilities that deliver it.]

## 3. Architecture and data

[The architecture in outline. The data classes used, whether the AI influences a decision and how autonomous it is, the users, and whether the output reaches or affects a customer or an employee, and how. Knowledge sources, with owner and review date.]

## 4. Risk Tier

[Tier 1, 2, or 3, with the reasons, assigned by the AICC Lead, or by the Executive Sponsor for a Solution that the AICC Lead built, on [date] and told to the Domain Owner; raised by a Control Function Contact where that applies. (AI Policy 3.2; Portfolio Management Model 6.4). For Tier 2 and 3: the confirmation of the Control Function Contact of compliance that the applicable law is met, with the date.]

## 5. Acceptance criteria

[The criteria for the acceptance of the Solution, in the form Given a situation, when an action is taken, then a result that can be observed (Solution Lifecycle Model 3.3), on which the AICC Lead gives the final acceptance of the Team and the Domain Owner judges it. The benefit and the outcome targets are in the Initiative Brief.]

## 6. Check or validation, and release block

[The check of a Risk Tier 1 Solution, with the Checker and the date, noted in the AI Registry; or the Control Sign-Off of the validation, by reference. The AI Registry entry, by reference.]

**Release block.**

| Item | Entry |
| --- | --- |
| First users | [named; trained before use] |
| Check or validation | [reference] |
| Team final acceptance, before the first deployment to the first users | [who, date] |
| First deployment | [key of the change ticket; reference of the test] |
| Business acceptance by the Domain Owner, or the Executive Sponsor | [decision: accepted, returned, or rejected; who; date] |
| Release decision beyond the first users | [decision, who decided, date] |
| Acceptance Checklist | [reference] |

## 7. Life after delivery

[For a Service: the run cost source and the sunset rule. For a Product: the consumer and the version. For an Experiment: the time-box in Iterations, and the receiver of the proposal.]

**Review of the live Solution.** [The note at each Iteration Review and Demo on the monitoring, incidents, use, and notices of the providers.]

| Date of the Iteration Review and Demo | Reviewed by | Note |
| --- | --- | --- |
| [date] | [Domain Owner, or the Executive Sponsor for a Service across Domains] |  |

**Changes and new-check decisions.** [Each significant change, and the decision of the AICC Lead on whether it requires a new check or validation, with the reason, the date, and its Decision Log reference.]

**Significant change.** [Team final acceptance and release of a significant change: by whom and on [date] (Solution Lifecycle Model 7.3(b), 8.6).]

**Emergency change.** [Authorized by [the AICC Lead] on [date], reviewed by the Executive Sponsor within five working days, Decision Log reference; for Risk Tier 3 the Control Function Contacts told (Solution Lifecycle Model 8.6).]

**Backup and recovery.** [Those of the AI Platform and of the Bank that apply, by reference.]

**Retirement or end.** [Handover accepted by the Receiver on [date] (Solution Lifecycle Model 8.1). Approval, by whom and when; date the access was removed; how the data and the logs were handled; AI Registry entry marked retired. Also for a Cancelled Solution that had real users or data.]

**Adopted Solution.** [Marked as adopted: yes or no; the Receiver as owner.]

## 8. Next step

[The next step, who, and when.]
