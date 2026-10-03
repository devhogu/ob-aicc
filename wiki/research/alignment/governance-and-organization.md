# Site-to-corpus alignment: Governance and Organization

Working record, 2026-10-03. Gap list between the site pages of the Governance and Organization sections and the corpus. The corpus is normative; the site explains it. Site paths are under `portal/content/`. OM = Operating Model, OG = Organization guide, UGG = Unit governance guide.

The site follows the OM closely. The real gaps are in four places: controls (what a control is, status meanings, which loop carries each control); governance measures (the site has ten, the corpus none); organization (how it grows, the RACI in families of activity); terms (three lines, Steering composition, "event", "control loop").

## A. Operating Model

### A1. New on the site
1. What a control has: reference, title, objective, type, test (`governance/controls-and-the-catalogue.md` 1.1). OM 8.1 lists Ref, Rule, Owner, When, Evidence, Template; objective, type, test only in UGG 7. Propose OM 8.4: "Each control has a reference, a title, an objective, the rule and its clause, an owner, a timing, an evidence record, a Template where one applies, a type, and a test. The type is Directive, Preventive, or Detective."
2. What each status means (same file 3.1). OM 8.3 names the five statuses without defining them; meanings only in the Control Matrix. Propose OM 8.5: a table (see A2-2 for which meaning).
3. Where a control is reviewed: at the Steering of its loop (3.1). Propose OM 8.3 addition.
4. The audit trail: reference → rule → evidence record → status → Steering Summary (`governance/records-evidence-and-assurance.md` 5.1). Propose OM 8.6.
5. The governance measures: ten measures with Definition, Source, Read at, Target rule (`governance/measures-and-reporting.md` 1): Control status; Deficiencies and findings; Exceptions; Decision sample; Risk Tier reassessments due; AI Incidents and control breaches; Risks beyond appetite; Access review; Appointments; Document review. OM has no measures section. Propose OM 6.11 with the table.
6. Maturity targets set yearly, Maturity Level per priority confirmed quarterly (measures 4.1). Propose OM 6.5 and 6.6 additions.
7. Who attends the Steering (`governance/the-steerings-and-the-bodies.md` 1). Propose OM 6.2A: "The Executive Sponsor chairs the Steering. The AICC Lead prepares it and attends. The Domain Owners concerned and the Control Function Contacts attend, and the members of the AI Steering Committee advise."
8. Who attends the Weekly Review: the AICC Lead and the Team. Propose OM 6.8 addition.
9. Internal audit stands outside the chain (steerings 3.1). Propose OM 6.10 amendment.
10. The three lines (records 4.1). Propose OM 2.4 (needs term fix F1).
11. The evidence records listed, "closed, dated, and traceable" (records 1, 2.1). Propose OM 7.2A.
12. No Bank data or code in the Registry (records 2.1). Propose OM 7.4 addition.
13. Snapshot at Iteration close, PI close, cutover (steerings 2; records 1.1). Propose OM 7.3 addition.
14. Decision levels: AICC Lead row adds "the Risk Tier; whether a change needs a new check" (`governance/decisions-and-escalation.md` 1). Amend OM 5.3.
15. Risk beyond appetite accepted only by the Executive Sponsor, with a report (decisions 3.1). Align OM 5.4 with Charter 5.4.
16. The escalation model is the same at every scale (decisions 5.1). Propose OM 5.8.
17. "Governance adds no meeting and no second record" (`governance/overview.md` 2.1). OM 6.1 addition.
18. Who enters each appointment, "Entered by" (`organization/people-and-appointments.md` 1). Propose OM 4.8 addition.
19. Onboarding and relief steps: deputy, access, charter read, training; access removed on change (people 2). Propose OM 4.9.
20. Time allocation with the line manager's consent (people 2). OM 4.6 addition.
21. How the organization grows: second Solution Engineer, product owner other than the AICC Lead, fourth person ends light mode, Domain Team, Domain Experts in each Domain (`organization/how-the-organization-grows.md` 2). Propose OM 4.10.
22. The shape as it scales: adds Holders and Teams, no layers, meetings, records; hand-off at scale to a platform team or IT function (3.1). Propose OM 4.11.

### A2. Contradictions
1. Controls carried by the loops: site says thirty-two carried by the five loops; OM 6.1 assigns 20; C-08, C-09, C-10, C-12, C-13, C-14, C-15, C-18, C-21, C-22, C-23, C-25 are in no loop.
2. Deficiency and Open: site Deficiency "did not operate or evidence shows a failure" (Review → Deficiency); OM Fig. 8 and Control Matrix §1 "Open → Deficiency: not corrected". Open: "due and evidence not yet in" (site) vs "due or in force… missing or incomplete; Risks and Issues holds an item" (Matrix).
3. Monthly sample size: "Set by the Steering" (site) vs "at least three Decisions of the AICC Lead, chosen by the Executive Sponsor" (OM 6.7).
4. Appointments listed among the Executive Sponsor's decisions (site) vs spread across the Board, AICC Lead, heads of Domain, Control Functions, head of technology (OM 4.6; not in OM 5.3).
5. Level examples left out: AICC Lead row omits "standards, Templates, questions between Domains"; Executive Sponsor row omits "retirement of a Service across Domains" (OM 5.3).
6. Snapshot as evidence of "the living records" (site) vs of the Solution Definitions (OM 7.3) / "the state of the working state" (Vocabulary).
7. Baseline date: organized 2 September, missing appointment by 1 December (site); OM 4.8 "missing on 2026-10-02 shall be made by 2026-12-01"; OG 6 "within 60 days".
8. Delegation limit: site drops "except a decision under 5.4 and 5.7" (OM 4.7).
9. Who sets the Priorities: direction loop (site) vs strategic loop of the PMM (OM 6.5) while OM 6.1 assigns C-02 to the direction loop (corpus inconsistency).
10. Monthly agenda: "gate decisions due, deficiencies, expired Exceptions" (site) vs "progress, risks, blockers, the acceptances, and the sample" (OM 6.7).
11. Event loop: site lists incident, Exception, stop, risk, finding, change of Holder, provider or regulation; OM 6.1 has the event loop carry C-19, C-30, C-31 (data sharing, deployment or change, retirement), not listed as events in OM 6.9.
12. "The person who states the value is not the person who ranks" (`organization/who-does-what.md` 2.1) vs light mode: the AICC Lead is product owner (states value, SLM 3.5) and ranks (OM 4.2).

## B. AICC Charter
1. "The Quarterly Report is the one report of the unit" (measures 3.1). Charter 7.2 addition.
2. Contents of the Quarterly Report: each Active Initiative and decision, control status and open deficiencies, risks accepted beyond appetite, reliance on providers, predictability trend, Maturity Level per priority. Propose Charter 7.4.
3. No administrative line over assigned people (`organization/the-place-of-aicc-in-the-bank.md` 3.1; only OG 2). Charter 3.2 addition.
4. Reporting through the Executive Sponsor to the Board Committee (the-place intro). Charter 3.1 addition.
5. Governance measures reference. Charter 7.1 addition.

## C. Unit governance workflow and guide
New: industry practice paragraph (overview 3.1) → UGG §1; design aim "light enough to run every week and strong enough to satisfy a supervisor and an auditor" → UGG §1; three-lines figure → UGG §5; "What an auditor finds" → UGG §7; life of a control, "a deficiency is governance working" → UGG §7; catalogue by loop with "What they cover" → UGG §3; loops with Plans/Checks/Acts columns → UGG §3; "One cadence, three readings" → workflow §2.
Contradictions: UGG §4 "significant cost" vs OM 5.2(b) "cost or harm" (fix the guide); UGG Fig. 2 event loop omits "a change of provider or regulation"; workflow Fig. 5 Steering = Executive Sponsor and AI Steering Committee only; the monthly Steering leaves a Snapshot at the Iteration close (site) vs quarter only (workflow §2, §5).

## D. Organization guide
New: "Whom it works with" table → OG §2; three constraints and industry practice → OG §1–2; "Who appoints whom" table with "Entered by" → OG §6; RACI letter meanings → OG §4; families with no row in OG §4: "Design, build, and the MVP", "Operation, support, and the live review", "Adoption in the Domain and training", "Oversight, the Risk Tier, and the AI Registry"; how the organization grows → OG §6A; bodies incl. the Steering, Control Functions, Weekly Review with a "Decides" column → OG §5; access reviewed each quarter (OM 7.6).
Contradictions (RACI unless noted): accepted limits listed in Risks and Issues (site) vs Appointments Record Part B (OG, template); taking a need in; test/check/validation Accountable; acceptance of Features; final acceptance; business acceptance and release; ranking; the business case; the Quarterly Report; change and retirement; the Service Agreement (AICC Lead R vs Solution Engineer R); oversight and the Risk Tier; design, build, MVP (Solution Engineer A vs Domain Owner/Executive Sponsor A); OG §5 lists "Executive Sponsor" as a body vs the site "The Steering".

## E. Templates
New: Quarterly Report — predictability trend (§3); open deficiencies and findings with age (§7); Maturity Level per Strategic Priority table (§3); governance measures table. Steering Summary — "events of the month" row; "share found in order" field (§7); yearly row for Maturity targets; quarterly Control Matrix status row. Appointments Record — "Entered by" (Part C); "Due by" (Part A); "Charter read (date)" (Part D).
Contradiction: Appointments Record Part B "accepted limits listed here" vs site "Risks and Issues".

## F. Vocabulary
1. "second line" is Not used under Control Function; the site uses it. 2. first line, third line, three lines undefined. 3. Steering: Vocabulary "the meeting of the Executive Sponsor and the AI Steering Committee" vs the site's wider membership. 4. Monthly/Quarterly Steering undefined. 5. Control loop has two meanings (all five vs the monthly loop). 6. Event: "a meeting of a loop" vs an occurrence (event loop). 7. Control catalogue. 8. Deficiency. 9. Control statuses. 10. Living record. 11. Accepted limit, compensating control. 12. Deputy, acting Holder, delegation. 13. "report to the Board" vs "Report to the Board Committee". 14. Corporate folder vs corporate share. 15. tracker, wiki vs Jira, Confluence. 16. Escalation. 17. Measure (no baseline/owner on the site's governance measures). 18. Domain Team. 19. Community of practice. 20. Head of the Domain, head of technology. 21. Gate decision, Decision sample. 22. Checker, product owner listed as Roles (they are designations). 23. Internal audit, executive management.

## G. Registry impact
1. `control-matrix.md`: dated summary of status counts. 2. `control-matrix.md`: Loop, Reviewed at (Steering Summary), Risks and Issues ref and due date columns. 3. New governance measures table (own Record or Dashboard section). 4. `risks-and-issues.md`: Control Function, Control ref, Source columns. 5. RI-005 is Issue/Open; the site says the missing appointments are "an accepted limit". 6. `appointments.md` Part A: "Due by" for vacant Roles; Executive Sponsor decision reference. 7. `appointments.md`: Entered by (C), Charter read (D), empty time allocation for two Holders. 8. `decision-log.md`: "Sampled at" and "Result" columns. 9. `teams.md`: Product owner column. 10. Calendar: "Mode (light/full) and from-date". 11. `steering/`: future Summaries carry the sample result and event-loop items.

## Count

| Class | Items |
|---|---|
| New | 54 (OM 22, Charter 5, UG workflow and guide 8, OG 8, Templates 11) |
| Contradictions | 31 (OM 12, UG 4, OG 14, Templates 1); A2-9, C2-1, C2-2 are inside the corpus |
| Terms | 23 |
| Registry impact | 11 |
| Total | 119 |
