# Recheck report: the corpus after DR-2026-010

Assessor: independent (did not write or fix the documents). Date: 2026-09-30. Scope: charter/ (six documents, five Templates), portfolio/ Records (not assessments/, not DR-2026-001 to 008), wiki/ (not archive/). All read in full; numbering, links, Catalog against files and the Vocabulary "Not used" column were checked by script. Nothing was edited. Abbreviations: OM Operating Model, SOI Statement of Intent, Cat Catalog, Voc Vocabulary, Pol AI Policy, CFC Control Function Contact, CF Control Function.

## 1. Earlier findings

FIXED, PARTLY, NOT FIXED, with the clause that shows it.

### 1.1 Blocker and Major (C-01 to C-15)

| Id | Status | Clause and remark |
| --- | --- | --- |
| C-01 | FIXED | OM 4.4(a) now covers validating and checking only; 4.4(b) lets the owner accept and release; release rows stand. |
| C-02 | FIXED | OM 4.4(e): checker named by the AICC Lead in Appointments until a second engineer; Pol 3.3 "other than the builder". Day one still needs a named person (RI-007, RI-011 open). Residue: N-09. |
| C-03 | FIXED | Pol 3.2 last sentence: the AICC Lead assigns Tier 1 provisionally and records it. New limit: N-02, N-04. |
| C-04 | PARTLY | Releasers now agree (OM 4.2, 6.3; Pol 3.3; DR-2026-010 item 1) and validation precedes a Tier 2 or 3 Pilot (OM 6.3 Pilot). But the placement of the Release in the Stage table is self-contradictory: N-01. |
| C-05 | FIXED | Charter 7.2 (preparer, approver, quarterly, traceable figures, High incident and appetite breach told at once); SOI 7.6 and Voc "Board Committee" as the Board names it (RI-010 tracks the name). |
| C-06 | PARTLY | "shall" now OM 11, Pol 16, SOI 17, Cat 5, Charter 2, Voc 1. Still present tense for duties: OM 4.6, 6.3 ("confirms"), 7.x; Charter 3.1, 4.1, 5.4, 6.2. Voc 3.1 makes present tense "otherwise", so Q3 stays ambiguous. |
| C-07 | FIXED | SOI 7.3, Voc "Control Function", OM 4.4(f), Appointments separate audit table. |
| C-08 | FIXED | OM 3.2 now "the Values and the Principles of the Statement of Intent"; second list removed. |
| C-09 | PARTLY | Pol 3.1 limits attributes to four with thresholds; other reasons are raised by a CFC. But Use Case Card 3 does not ask for influence on a decision or autonomy; the "law treats as high risk" list is absent (Pol 3.2). See N-04. |
| C-10 | FIXED | Pol 2.1: AICC Lead approves with the infosec Contact; 90-day listing and tolerance. The listing has no performer (passive voice). |
| C-11 | PARTLY | Done: Tier 1 check (OM 6.3 Pilot), provider check (Discovery), return to Discovery, AICC Lead confirms exits, conditions met at Pilot exit. Open: Initiatives beyond Intake and enabling work (N-11); Operate "To leave" still lists a recurring duty. |
| C-12 | FIXED | Cat 7.1: check on change of meaning and yearly, by a person the Executive Sponsor names. Person not named (RI-011). Cat 4.2 now clashes with 7.1 (N-12). |
| C-13 | FIXED | Pol 7.1 (nothing needing an unnamed CF proceeds; Sponsor may name who acts). Does not cover heads, Platform Owner, incidents: N-03, N-16. |
| C-14 | PARTLY | SOI 13.3 and 13.4 now carry a Role (Charter 3.1, OM 7.2, Cat 4.2); training and Community of Practice in Charter 6.1(e), OM 7.1, Pol 2.1. SOI 10.1 still says all employees, by role, before any AI use; SOI 10.2, 10.3, 10.5, 10.6, 12.1 still have no Role beyond Charter 3.1's general sentence. |
| C-15 | PARTLY | Pol 3.5 names the AICC Engineer, Domain Owner, Platform Owner, CFCs. Reassessment row (Pol 3.3) and monitoring in operation have no performer; the Platform Owner is not named (N-03). |

### 1.2 Coverage gaps G1 to G9

| Id | Status | Clause |
| --- | --- | --- |
| G1 | FIXED | Charter 7.2; Pol 2.4 (named approver for investor, regulator, Board output); Pol 5.3; Quarterly Report section 5. |
| G2 | FIXED | OM 4.4(f), 9.1; SOI 7.3; Voc; Appointments audit table. |
| G3 | FIXED | OM 4.6 deputy and two-week delegation; Appointments "Deputy" columns. Names open (RI-009). |
| G4 | FIXED | Pol 3.4; Control Sign-Off "Valid until"; AI Registry columns. Too broad: N-05. |
| G5 | FIXED | OM 7.2 (SOI, Charter, OM, Policy, appetite; extra review on trigger); SOI 13.3. |
| G6 | FIXED | Pol 2.1 training; Charter 6.1(e). No Record holds the training content or who is trained. |
| G7 | PARTLY | Priorities has a Measures table with baseline, target, owner, source; Voc "Finding" includes audit and supervisor. Only 6 of the SOI 11.3 Measures are seeded; none for Level 1: N-18. |
| G8 | FIXED | Standards ARC-001; AI Registry column; Card 3. |
| G9 | FIXED | OM 9.1 (closed not deleted, retention, history not rewritten, audit read access). |

### 1.3 Minor findings (C-16 to C-41) still open

Fixed and not listed: C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-23, C-26, C-34, C-35, C-36, C-40, C-41 (14 of 26). Open or partly open (12):

- C-24 wiki/operating-model-open-items.md still has stale rows (3 "AI solution engineers", 5 "replenishment", 6 "stage policies", 11 "AI use policy", 14 "positioning section", 18 "within one hour", 19 "Artifact Standards"; 13 and 15 are decided).
- C-25 portal/content/statement-of-intent.json still cites wiki/statement-of-intent.md at revision add2031 (tracked RI-004, UC-006).
- C-27 (partly) still undefined: "activator", "corpus", "Team" as a level, Community of Practice, Platform Guardrails, first and third line; new: "AI services". See N-14.
- C-28 change logs still name removed documents (OM 2.0, Charter 0.2, Cat 1.0, Pol 0.1); "charter folder" in Voc 1.1, 4.1 and Cat 1.1.
- C-29 (partly) Voc 3.7 exempts change logs but Cat Q8 does not; Pol 3.1 tier table and OM 7.1 meeting table lack an introducing clause (N-15).
- C-30 (partly) Initiative Brief status lacks "returned" (section 4 uses it); one Domain Owner per Initiative; UC-001 to 006 are not AI Use Cases (N-11).
- C-31 (partly) Voc and Cat 7.2 accept Severity for Risk and Issue; the risks-and-issues.md intro still says Incident and Finding only.
- C-32 Sponsor's mandate has no source ("Appointed by" blank); SOI 7.7 still "activated at the appropriate level"; a CEO of the Bank activates a policy for Participating Entities (Pol 1.1).
- C-33 duplication persists: Tier 3 release in six places; internal audit read access in OM 4.4(f), 9.1 and Appointments; activation in OM 4.2 and Cat 4.1 while Cat 1.1 says "the only place".
- C-37 Voc 3.8 (diagram rule) with no diagram; Q2 and Q8 not scripted.
- C-38 Limits on Work in Progress per Stage and Domain, monthly Steering with an empty committee, SOI 11.2 and 11.3 detail in the Group statement (see section 4).
- C-39 British spelling in 17 wiki research files (wiki README says American).

## 2. New findings introduced by the fixes (and found on the re-read)

Mechanical results: clause numbering has no gaps or repeats in all six documents; all six change logs end on the revision in the metadata; Catalog 5.1 and 6.1 match the six files and five Template ids; 105 links checked in charter, portfolio and wiki (without archive and assessments), 0 broken; the "Not used" column hits only "approval" where it is not about a document (legitimate, but a scripted Q2 will flag it). Ghost names (Forum, Register, Delivery Lead, Portfolio Manager, Tier 4, Design Review) survive only in change logs, superseded Decision Log rows and wiki pages that carry the archive banner. Two survive in live text: "Risk Tier Policy" (N-10) and "peer" (N-09).

| Id | Sev | Evidence | Fix |
| --- | --- | --- | --- |
| N-01 | Blocker | OM 6.3 Scale row: Purpose "Adoption across the Domain, started by the release" and "To leave the Stage: The release". Voc "Release": "at the exit from Scale ... beyond the pilot group". The release is both the start and the exit of Scale; Pilot exit has no release. Read literally, a Tier 3 agent is adopted before the Sponsor's release, against Charter 5.3 and Pol 3.3 (Tier 3 oversight row). | Put the release in the Pilot exit ("Scale starts with the release"), remove it from the Scale exit, correct Voc "Release" to "at the exit from Pilot". |
| N-02 | Major | Pol 4.1 needs the infosec, data protection and legal Contacts for every provider; Pol 2.1 needs the infosec Contact to approve any service; Pol 7.1 blocks "no provider" until they are named, and lets the Sponsor name an acting person only "when a matter is urgent". OM 6.3 Discovery exit needs the provider check. So no Tier 1 Use Case with a bought service can proceed, against RI-008 ("only Tier 1 proceed") and DR-2026-010 item 3. | Pol 7.1: the Sponsor names who acts in Appointments at any time, not only when urgent; correct RI-008; first Steering names infosec, data protection and legal Contacts. |
| N-03 | Major | OM 4.6: the head of a Domain names the Domain Owner, the head of technology names the Platform Owner; Appointments heads and Platform Owner rows are empty; Pol 7.1 covers only Control Functions. Discovery exit needs a Domain Owner and Domain Expert; Tier 2 and 3 need the Platform Owner for logs (Pol 3.5). No fallback. The AICC Lead is Domain Owner in UC-001 to 006 by custom, not by rule. | OM 4.6: until a head is named, the Sponsor names an acting Holder; for AICC's own work the AICC Lead is Domain Owner. |
| N-04 | Major | Interim Tier 1 (Pol 3.2) is assigned by the builder who wants the pilot, and nobody looks at it: the Tier 1 check (Pol 3.3) has no stated scope. Boundary is unclear: Tier 1 "data that is not confidential", Tier 2 "Internal, confidential ... data", so internal source code is Tier 2 by the table; the Bank classification is unchecked (RI-003). The Card does not ask influence on a decision or autonomy. The law-category test (Pol 3.2) is not an "attribute", so the interim rule skips it. | Say the Tier 1 checker confirms the Tier; define Tier 1 data as "public or unclassified under the Bank rules"; add influence and autonomy to Card 3. |
| N-05 | Major | Pol 3.4 and OM 6.3: any change of model version, provider, data or scope, at any Tier, returns the Use Case to Discovery. SaaS assistants change model versions without notice. Not said whether use stops. OM 6.3 omits Pol 3.4's "for the checks that the change touches". | Return to Discovery only for a change that the validation or the check named (Control Sign-Off already has "revalidate on"); say use continues unless the checker or a CFC suspends it. |
| N-06 | Major (bureaucracy) | Pol 3.1 and 3.3: Tier 2 holds every internal or confidential use (an internal coding or drafting assistant) and every customer use under review. One validation by model risk plus each remit, bias testing, a security test, logs, Sign-Off with validity date. For a team of one this is the same load for a developer assistant and a customer-facing tool, and it depends on up to five unnamed Contacts. The coverage report (section 4) raised it; DR-2026-010 did not address it. | Split Tier 2 by customer effect, or let the Domain Owner release an internal Tier 2 use with no customer effect after validation by model risk and infosec only. |
| N-07 | Minor | Pol 3.3 "Testing for bias and error: before release" while OM 6.3 lets the Pilot (real work) start after validation; a Tier 2 or 3 pilot can reach people before the test. | "Before Pilot". |
| N-08 | Minor | OM 5.4: the Sponsor "may accept a risk only within the AI Risk Appetite Statement"; Charter 5.4 and OM 4.2: the Sponsor is the only person who may accept a risk beyond it; Charter 7.2 presumes he does. | State in OM 5.4 whether the Sponsor can set aside a stop with a risk beyond appetite (suggest: no; beyond appetite only with a Board Committee report). |
| N-09 | Minor | Residue of the checker fix: OM 4.2 AICC Engineer "reviews the work of peers"; OM 4.4(b) "owner of a Use Case" (undefined); Standards intro "Peer review"; RI-007 "peer check"; DR-2026-008 "other than the owner"; RI-011 makes the Sponsor owner of naming the Tier 1 checker while OM 4.4(e) gives it to the AICC Lead; the yearly document checker (Cat 7.1) has no Appointments row. "Benefits from" (4.4(a)) is undefined and excludes the natural checker, a developer who would use the assistant. | One term "check by a person other than the builder"; define "benefits from" as "gains personally or in the own Domain's results"; add the document checker to Appointments. |
| N-10 | Minor | OM 6.3 intro: "in a way the Risk Tier Policy states"; no such document (Pol 3.4 now holds it). | "as the AI Policy states". |
| N-11 | Minor | OM 6.2 says enabling work has no Risk Tier, but the Intake exit in 6.3 demands a Risk Tier and an AI Registry entry for every Use Case; UC-001 to 006 are "Use Cases" with Tier "n/a", Stage Operate, Status Done. Exits for Initiatives after Intake are undefined; "Retire" requires a Registry entry an Initiative lacks; Operate exit still holds a duty. | One clause: enabling work and Initiatives leave Intake with a Backlog entry; Risk Tier, Registry and release apply to Use Cases that build AI; Operate exit is "Retirement" only. |
| N-12 | Minor | Cat 4.2 "activated when it passes the checks in section 7" vs 7.1 "checked when its meaning changes" and "a correction needs only a change log row". Meaning-changing fixes were logged as OM 2.3, Charter 0.3, Pol 0.2, Voc 1.1, Cat 1.1 against Cat 3.3 (next whole number on change of meaning). Cat 4.1 "when its activator shall set" is misphrased. | Cat 4.2: "passes the checks of 7.1 where they apply"; apply 3.3 at activation; recast 4.1. |
| N-13 | Minor (bureaucracy) | Cat 4.2: the activator announces every activation to all employees, including each Vocabulary or Catalog revision. | Announce only documents that bind persons outside AICC. |
| N-14 | Minor | Used but undefined: "AI services" (Pol 2.1, Voc bars "AI tool"), "activator", "corpus", "Team", Community of Practice, Platform Guardrails, first and third line. "Check" is defined for Tier 1 only but used for provider check, quarterly risk check, document check; lowercase "work item" vs Work Item. | Define the six needed terms; rename the others; define "Check" as any review by a person other than the builder or author. |
| N-15 | Minor | Pol 3.1 tier table and OM 7.1 meeting table have no introducing clause (Cat Q8); Cat Q8 does not exempt change logs although Voc 3.7 does. | Add "The following table ..." lines; add the exemption to Q8. |
| N-16 | Minor | Pol 5.4: compliance and data protection decide on notices and Pol 6.1 Exceptions need the CFC, but Pol 7.1 says only what "does not proceed"; an incident before Contacts exist has no decider. | Pol 7.1: the Sponsor names an acting Contact for an AI Incident too. |
| N-17 | Minor (bureaucracy) | Stage, Risk Tier and Domain Owner are kept in Backlog, Use Case Card and AI Registry (Domain Owner also in Appointments); the AI Registry has 15 columns. | Keep each in one Record; the Card links to it. |
| N-18 | Minor | priorities.md Measures: 6 of the SOI 11.3 measures; none for Level 1 (policy active, Contacts named, Registry complete, baselines), the first level to reach. | Seed Level 1 with owners. |
| N-19 | Minor | Charter 4.2, OM 6.2, priorities.md: Investment Guardrails "not yet set", no rule for spend meanwhile (a licence for the assistant). | "Until set, the Sponsor approves any commitment." |
| N-20 | Minor | Records not aligned with the fixes: RI-008 text (N-02); RI-011 owner; risks-and-issues.md Severity note; portfolio/assessments/README.md lists two of three assessments and names removed files (charter/corpus-assessment.md, Risk and Issue Register); RI-013 will need update. | Edit the five lines; add 2026-09-30-4 to the index. |

## 3. Operability today: the Sponsor and one person

Status now: all six documents are draft (none binds); the Executive Sponsor has not confirmed the appointment (RI-001); no independent checker is named (RI-011); all CFC, head, Domain and Platform rows of Appointments are empty. Activation of the four binding documents is therefore external: Sponsor confirms, names a checker, runs the ten questions, activates (Cat 4.1, 7.1).

What can proceed once active and before any Contact is named: enabling work of AICC (UC-005, UC-006); Intake of any idea; a Tier 1 Use Case that uses no provider (for example a locally run model on public data), assigned by the AICC Lead, checked by a named engineer, released by the Domain Owner (the AICC Lead for AICC's own work). Nothing that uses a provider, any Tier 2 or 3 Use Case, or a Group Arrangement (Pol 7.1). Without the first-Steering naming of infosec, data protection, legal, model risk (and a head of technology), the path to Scale is closed for real Use Cases (N-02, N-03).

Walk: an AICC Lead wants to pilot an internal AI coding assistant for developers (a bought service that sees the Bank's source code).

| Step | Who decides | Record updated | Allowed by the documents? |
| --- | --- | --- | --- |
| 1 Intake: Card, Backlog row, Registry entry | AICC Lead (OM 4.2) | Backlog, use-cases/UC-nnn, AI Registry | Yes |
| 2 Risk Tier | Model risk Contact; the Lead only for Tier 1 (Pol 3.2). Internal code is "internal" data, so Tier 2 (Pol 3.1) | Card 4, Backlog, Registry | Tier 2: blocked, no Contact. Tier 1 only if the Lead judges the data non-confidential himself (N-04) |
| 3 Approve the service for the data class | AICC Lead with infosec Contact (Pol 2.1) | AI Registry "Approved for" | Blocked: no infosec Contact (N-02) |
| 4 Provider check | Infosec, data protection, legal Contacts (Pol 4.1) | none named (Registry has no check date) | Blocked: Pol 7.1 (N-02) |
| 5 Discovery: Measures, Domain Owner and Expert, effect on persons (Tier 2) | AICC Lead confirms (OM 6.3); head of technology names Domain Owner (OM 4.6) | Card, Backlog, Appointments | Blocked on the head of technology unless the Lead is Domain Owner by custom (N-03) |
| 6 Spend | Domain Owner funds; Guardrails not set | none | Gap: no default (N-19) |
| 7 Validation (Tier 2) or check (Tier 1) before Pilot | CFCs; or an engineer named by the AICC Lead (OM 4.4(e)) | Control Sign-Off; Registry "Last validation" | Tier 1: yes if a checker is named and does not "benefit" (N-09). Tier 2: blocked |
| 8 Training of pilot users | AICC (Pol 2.1) | none | Yes, no Record |
| 9 Pilot in real work | Team; the Lead confirms the exit against Measures | Backlog, Card | Yes |
| 10 Release | Domain Owner (Tier 1 and 2), Sponsor (Tier 3) | Registry "Released by" | Placement contradictory (N-01) |
| 11 Operate, reassess on change and by date; a model update returns it to Discovery | AICC team | Registry, Risks and Issues | Workable only after N-05 |
| 12 Retire: users told, access removed, Registry closed | Domain Owner | Registry | Yes |

End to end the path exists but is not free of contradiction (N-01) and is closed today for this example at steps 2 to 5 (N-02 to N-04).

## 4. Bureaucracy, in my view, for a team of one to three

The corpus is far lighter than before (25 to 6 documents, 13 to 7 Roles). Still heavier than needed: Tier 2 scope (N-06); return to Discovery on any version change (N-05); three meetings and a monthly Steering when the AI Steering Committee and Domain Owners do not exist (C-38; make Steering quarterly until a Tier 2 Use Case exists); Limits on Work in Progress per Stage and per Domain with a four-score ranking (OM 6.1); the same facts in Backlog, Card and Registry (N-17); the announcement to all employees of every activation (N-13); a ten-question outside check per change of meaning (Cat 7.1; script Q2 and Q8); seven Appointments tables. Keep: the Tier 1 check, the Sponsor's Tier 3 release, internal audit as assurance only, the Decision Log, deputies.

## 5. Verdict

Ready after named fixes. Activation also needs three external steps: the Executive Sponsor confirms the appointment (RI-001), names an independent checker (RI-011), and names at least the infosec, data protection, legal and model risk Contacts and the head of technology (RI-008).

Counts. Earlier findings: Blocker 3 of 4 fixed, 1 partly; Major 6 fixed, 5 partly (C-06, C-09, C-11, C-14, C-15); coverage G1 to G9: 8 fixed, 1 partly (G7); Minor 14 fixed, 12 open or partly open. New: 1 Blocker, 5 Major, 14 Minor (20).

Top fixes:

1. N-01: move the release to the Pilot exit and correct Voc "Release".
2. N-02, N-03, N-16: Pol 7.1 and OM 4.6 let the Sponsor name acting Contacts, heads, Platform Owner and incident deciders at any time; correct RI-008.
3. N-04: the Tier 1 checker confirms the Tier; define the Tier 1 and 2 data boundary; add influence and autonomy to the Card.
4. N-05 and N-06: narrow the return to Discovery; give internal Tier 2 uses a lighter validation.
5. C-06, C-09, C-14, C-15: the remaining "shall" and Role gaps, with N-09, N-10, N-12, N-14 as one wording pass.
