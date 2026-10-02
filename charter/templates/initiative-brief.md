```yaml
id: AICC-TPL-02-EN
title: Initiative Brief
status: active
revision: 4.6
created: 2026-09-30
revised: 2026-10-02
```

# Initiative Brief

**Template.** The business case of an Initiative, in lean form. Copy for each Initiative. The Domain Owner and the AICC Lead complete it. It is the investment decision: it holds the business goal and the case, and the volatile detail of the trials stays in the working state (Jira and Confluence after the cutover). It carries no figures of the Bank, no data, and no code: a figure is a reference to its source. One page.

| Field | Entry |
| --- | --- |
| Identifier | INI-[nnn] |
| Title | [title] |
| State and Stage | [state, and Stage if in discovery or active] |
| Strategic Priority | [PRI-n] |
| Domain Owner (represents the client function) | [name; several for an Initiative that spans Domains] |
| Pivot of | [INI-nnn, when the Initiative is a pivot of another] |
| Solutions expected | [the Solutions it should deliver, with their types] |
| Business acceptor | [Domain Owner, or Executive Sponsor for items across Domains, enabling work, or an Experiment with no Domain] |
| Service Agreement | [AGR-nnn (for enabling work the Executive Sponsor is the client)] |
| Period | [from and to] |
| Date of last change | [date] |

Open sections: [none, or the numbers and what is missing]

## 1. Hypothesis

[For [the client] who [need], the [solution] is a [type] that [value]. Unlike [the current way], ours [difference].]

## 2. Business outcomes and leading indicators

| Business outcome | Leading indicator | Where the figures live | Date |
| --- | --- | --- | --- |
|  |  | [the source system of the function] |  |

[The baseline and the target of each indicator are figures of the Bank: they stay in the source system, and the brief points to them.]

## 3. Scope and the minimum viable product

[What is in and out of scope, any non-functional requirements, the minimum viable product that tests the hypothesis, and the Features and Solutions it may spawn.]

## 4. Cost, capacity, and value

[The capacity in days for the minimum viable product, and the estimate for the full scope if it succeeds. The cost and the Investment Envelope as references to the financial planning of the Bank. The expected value and where it is tracked. AICC supplies the capacity and does not charge; the Domain pays the run, the licenses, and the provider costs from its Envelope (Portfolio Management Model 6.6, AICC Charter 4.1).]

## 5. Risks, dependencies, and Risk Tier

[The risks, the expected Risk Tier of the Solutions, the providers, the Control Functions that clear the business case, and the Dependencies on other items, functions, or persons.]

## 6. Decision and acceptance

| Decision | By | Date | Record |
| --- | --- | --- | --- |
| Approval of the business case: [approved / returned / deferred / rejected] | [Domain Owner, or the Executive Sponsor above a guardrail, across Domains, or for enabling work (Portfolio Management Model 6.3)] | [date] | DR-[yyyy]-[nnn] |
| Clearance of the Control Function Contacts, when Risk Tier 2 or 3 is expected: [cleared / not cleared] (Portfolio Management Model 6.4; for a higher Risk Tier assigned later, AI Policy 3.2) | [Control Function Contacts concerned] | [date] | [Control Sign-Off reference] |
| Service Agreement issued | [AICC Lead] | [date] | AGR-[nnn] |
| Decision after the MVP: [continue / pivot / defer / reject] (Portfolio Management Model 7.2) | [approver of the business case] | [date] | DR-[yyyy]-[nnn] |
| Acceptance on delivery: [accepted / returned / rejected] (Solution Lifecycle Model 7.3(c)) | [Business acceptor] | [date] | [Outcome Report or release block] |

## Amendments after approval

A change after the approval of the business case is entered here with its date and its Decision Record, and the sections above stay as approved.

| Date | Section | Change | Decision Record |
| --- | --- | --- | --- |
|  |  |  | DR-[yyyy]-[nnn] |
