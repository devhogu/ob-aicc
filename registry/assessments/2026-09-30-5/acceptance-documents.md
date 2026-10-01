# Acceptance assessment of the six documents and five Templates

Assessor: independent (did not write or fix the documents). Date: 2026-09-30. Nothing was edited. Scope: charter/ (six documents at SOI 1.0, Charter 0.5, OM 3.1, Policy 0.4, Vocabulary 1.3, Catalog 2.0; five Templates), portfolio/ Records (not assessments/, not DR-2026-001 to 008), wiki/ (not archive/). Working tree clean at c3c0235; the only charter change since the last re-check is Policy 2.4 (DR-2026-014). Mechanical checks were scripted: metadata block, change log end, numbering, introducing clauses, 103 links, "Not used" terms, spelling, "shall", 9-word overlap between documents, clause counts. Abbreviations: SOI Statement of Intent, Cat Catalog, Voc Vocabulary, OM Operating Model, Pol AI Policy, CF Control Function, CFC Control Function Contact.

## 1. Criteria verdicts

| Criterion | Verdict | Basis |
| --- | --- | --- |
| A1 Completeness | PASS WITH NOTES | Every "shall" of SOI 5-13 has a carrier; 8 have a weak or no performing Role (A-15, A-16, A-17) |
| A2 Internal consistency | PASS WITH NOTES | The named disputes are closed (release, Tiers, cadence, reporting, internal audit). One real contradiction inside Pol 2 (A-04); five wording conflicts (A-08 to A-12) |
| A3 Ten questions | PASS WITH NOTES | Q1, Q8 pass for all six; Q3, Q5, Q6, Q7 fail in part (section 4) |
| A4 Terminology | PASS WITH NOTES | No defined term is unused; no real "Not used" hit; undefined and lowercase terms (A-19, A-20) |
| A5 Operability, present team | PASS WITH NOTES | Enabling work, Intake and a Tier 1 Use Case with no provider work today; activation itself creates unmet duties (A-03) |
| A6 Proportionality | PASS WITH NOTES | Far lighter than before. One rule a team would not follow (A-07); duplication (A-24) |
| A7 Bank-grade safety | PASS WITH NOTES | Controls are present for all nine areas; four real gaps (A-04, A-05, A-12, A-29) |
| A8 Activation readiness | FAIL (fixable) | Path is not complete or unambiguous: Cat 7.2 gate, no named checker, appetite level, Participating Entities (A-01, A-02, A-05, A-06) |

## 2. State of the earlier findings

N-01 to N-20 of the re-check (2026-09-30-4), checked against the files:

- FIXED (17): N-01 (OM 6.3 Pilot exit holds the Release, Scale "starts with the release", Voc "Release" at exit from Pilot); N-02, N-03, N-16 (Pol 7.1 and OM 4.6: Sponsor names acting Holders at any time, incident included); N-04 (Pol 3.2 checker confirms Tier, Tier 1 data "public or unclassified", Card 3 asks influence and autonomy); N-05 (OM 6.3, Pol 3.4: use continues unless suspended); N-06 (Pol 3.3 Tier 2 validation by model risk and infosec only without customer effect or personal data); N-07; N-08 (OM 5.4); N-09; N-10 (no live "Risk Tier Policy"); N-11 (OM 6.2, 6.3); N-12 (Cat 4.1, 4.2); N-13; N-15; N-19 (Charter 4.2); N-20 (RI-008, RI-011, Severity note, assessments index).
- PARTLY (2): N-14 (Community of Practice and Check defined; "Team", "Platform Guardrails", "Validation" still not), N-18 (Level 1 seeded with an owner; other measures have none).
- OPEN (1): N-17 (Stage, Tier, Domain Owner still in Backlog, Card, Registry; Registry has 15 columns; A-26).
- Earlier Minor items: fixed C-29, C-31. Partly: C-27, C-30, C-32. Still open: C-24 (wiki open items), C-25 (portal JSON, tracked RI-004), C-28, C-33, C-37, C-38, C-39 (see A-21, A-24, A-28, A-33).

## 3. A1 Completeness: commitments of SOI sections 5 to 13

Carrier and performer for each "shall" (and the present-tense commitments of 5, 6, 7, 9, 11, 13). "Others" means explicitly for a person outside AICC.

| SOI | Carrier | Performer | Result |
| --- | --- | --- | --- |
| 5.1-5.3, 5.5, 5.6 | OM 3.1(d), 6.3 Pilot exit; ARC-001; Pol 2.1; Charter 3.3 | AICC Lead confirms exits; Domain Owner | OK |
| 5.4 Reuse | Charter 6.1(d) "architecture guidance" only; no standard in Standards | none | No carrier (A-16) |
| 6.1 | Pol 2.3, 4.2; Charter 7.2 | Domain Owner; Sponsor | OK |
| 6.2, 6.3 | Pol 3.3 (testing, disclosure rows), 3.5 | AICC Engineer; Domain Owner | OK |
| 6.4 | Pol 2.2, 2.5; PLT-004 | All employees; Platform Owner (unnamed) | OK |
| 6.5 | Pol 3.3 security test, 4.1 fallback and exit; ARC-002, PLT-005 | CFCs check; "critical" undefined | Note (A-16) |
| 6.6 | Pol 3.3 oversight row, 3.5 | Domain Owner | OK |
| 6.7 | Pol 6.1; OM 4.2 | CFC | OK |
| 7.1-7.6, 7.8 | Charter 3.2, 3.3; OM 2.3, 4.4, 4.5; Pol 3 | Sponsor; CFs | OK; Board Committee unnamed (RI-010) |
| 7.7 appetite "activated at the appropriate level" | Charter 5; Charter 5.4 | Sponsor | Level undecided (A-05) |
| 9.3 figures traceable, human approval | Charter 7.2; Pol 2.4 | AICC Lead; Sponsor | OK (see A-07) |
| 9.6 "system records the AI contribution and the decision" | Pol 3.3 logging (Tier 2, 3) only | Platform Owner | Weak (A-16) |
| 10.1 training by role before any AI use | Pol 2.1 (per Solution); Charter 6.1(e); OM 7.1 | "AICC" (not a Role); no Record of who is trained | Partial (A-15) |
| 10.1 Domain Experts; 10.1 AICC maintains templates, CoP | OM 4.6, 7.1; OM 4.2 | Domain Owner; AICC Lead | OK |
| 10.2 classification; knowledge owners | Pol 2.2; ARC-001; Card 3; Registry column | Bank (RI-003 open); performer of ARC-001 not stated | Partial (A-15) |
| 10.3 AI Platform | Charter 3.2; OM 4.2; PLT-001 to 006 | Platform Owner, outside AICC, not named | Others; OK |
| 10.4 funding | Charter 4.1, 4.2; Priorities | Sponsor | OK |
| 10.5 providers, "ongoing monitoring" | Pol 4.1 (repeat at reassessment or change of terms) | CFCs; nobody notices a model change | Partial (A-15) |
| 10.6 delivery | OM 3.1(c), 6.1, 7.1 | AICC team | OK |
| 11.1-11.3 Levels and Measures | Priorities, Roadmap, QR sections 3, 4 | AICC Lead; "reached" declared by nobody | Note (A-17) |
| 12.1 baselines at Level 1 | Priorities Level 1 row | AICC Lead | OK; 6 of 7 rows have no owner |
| 12.2 report to Steering and Board Committee | Charter 7.2; OM 7.1; Pol 5.3 | AICC Lead prepares; Sponsor issues | OK |
| 12.3 benefits against Envelope | Charter 7.1; QR section 4 | AICC Lead | OK |
| 12.4 internal audit assurance | OM 4.4(f), 9.1; Appointments | Internal audit | Others; OK |
| 13.1, 13.2 | Pol 3.2 (law of the Entity); OM 3.1(g), 7.1 | Compliance CFC; team | OK |
| 13.3 annual and event review | OM 7.2; Charter 3.1, 5.4 | Sponsor | OK |
| 13.4 communicated to employees; available to regulators, investors, customers | Cat 4.2 (employees); Charter 3.1 | Sponsor (employees); nobody for the others | Partial (A-16) |

## 4. A3 The ten questions, run for each document

P pass, N fail in part (finding id), P* passes but see the note. Q4 is read as "agrees with every higher document".

| Q | SOI | Charter | OM | Pol | Voc | Cat |
| --- | --- | --- | --- | --- | --- | --- |
| 1 metadata and change log end | P | P | P | P | P | P |
| 2 terms, none "Not used" | P* | P | P | P | P | P |
| 3 clauses numbered, "shall" | N A-18 | N A-18 | N A-18 | N A-18 | P | N A-18 |
| 4 agrees with higher documents | P | P* A-32 | N A-08, A-09 | N A-04, A-09, A-11 | P | P |
| 5 Roles, Records, Templates defined | P | P | N A-19 | N A-19 | P | P |
| 6 one Role per requirement | N A-15, A-16 | P | N A-14 | N A-14 | P | P |
| 7 no open questions, lineage, files | P | P* A-21 | P* A-21 | P* A-21 | N A-21 | N A-21 |
| 8 intro clause for each table, links | P | P | P | P | P | P |
| 9 size, nothing said elsewhere | P* | P | N A-24 | N A-24 | P* | P |
| 10 doable today | P* A-06 | P* A-30 | N A-03 | N A-03, A-04 | P | N A-02, A-22 |

Script results. Q1: six fields in every block; last change log row equals the revision in all six (1.0, 0.5, 3.1, 0.4, 1.3, 2.0) and the Templates carry no log as Cat 6.1 states. Numbering: no gap, no repeat, no section mismatch in the six. Q2: the "Not used" column hits only "sponsor" inside "Executive Sponsor" (false positive of a literal script), "goal" in the Group's pillar name "ESG goals" (SOI 3.2), and "Position against the AI Risk Appetite Statement" in the Quarterly Report Template (different sense); no other hit. Q3 spelling: no British form in the six or the Templates. Q8: every table outside a change log has an introducing clause in the six documents; the six documents contain no links; 103 links in charter, portfolio, wiki (not archive, not assessments): 0 broken. Q9: six documents (limit eight); largest SOI with 61 clauses (limit "about 150"); Decision and Record names agree with Cat 5.1 and 6.1.

## 5. A5 Operability with one person and the Executive Sponsor

State: all six documents draft; Sponsor and Lead are in Appointments with no date and no deputy; Ademi Moldogazieva is Domain Owner of INI-004; every other head, Contact, Domain Owner, Platform Owner, both checkers and internal audit are empty (Appointments).

What the present team can do after activation: Intake of any idea (OM 4.2); enabling work with no Tier (OM 6.2); a Tier 1 Use Case with no provider, Tier assigned provisionally by the AICC Lead (Pol 3.2), checked by a named engineer (OM 4.4(e)), released by the AICC Lead as Domain Owner for AICC's own work (OM 4.6, last sentence); the three meetings with the Sponsor and the Lead; Decision Log, Records.

What stops until the Sponsor names persons (Pol 7.1, OM 4.6): every Tier 2 or 3 Use Case; every provider (three CFCs, Pol 4.1); approval of any Solution (infosec CFC, Pol 2.1); a Domain Owner for INI-002, 003, 006, 007, 008. The Steering notes already carry both actions for the Sponsor. The goals of the first 100 days are scoping, so they can proceed; INI-004 cannot reach its first edition without a Tier 2 validation (RI-014).

Walk of one edition of INI-004: Card and Tier (model risk CFC or acting, Pol 3.2) - provider check - validation by model risk and infosec, plus data protection or legal if personal data is used (Pol 3.3) - Pilot - Domain Owner releases (Ademi, OM 4.2) - each figure traced (Charter 7.2) - Sponsor approves each edition (Pol 2.4) - Decision Log line (OM 5.6). Workable once two acting Contacts exist; a Decision Log line each month is the audit trail.

Day-one breaches created by activation: OM 4.6 "Each Holder shall name a deputy" (none named; for a team of one the deputy must come from outside AICC); OM 4.6 heads and Platform Owner; Pol 2.1 listing "within 90 days" (no performer); Cat 7.1 checker (A-02, A-03).

## 6. A7 Bank-grade safety

| Area | Result | Evidence or gap |
| --- | --- | --- |
| Accountability | PASS | Named individual per Use Case (SOI 2.3, Pol 2.3); Board reporting (Charter 7.2) |
| Human oversight | PASS | Pol 3.3 oversight row, Tier 3 stop authority; ARC-002, PLT-005 suspend |
| Data protection | PASS WITH NOTES | Pol 2.2, 2.5, PLT-004, data protection CFC validates personal data. Gap: tolerance clause lets unapproved tools keep confidential data for 90 days (A-04) |
| Vendor risk | PASS WITH NOTES | Pol 4.1, 4.2, concentration in the Quarterly Report. Not scaled by Tier; nobody notices a silent model change (A-13, A-15) |
| Incident handling | PASS WITH NOTES | Pol 5: Severity, at-once report, regulator and data subject decisions, review in ten days. Domain Owner is not told of a High incident (A-31) |
| Model validation | PASS WITH NOTES | Independent validation, valid-until date, Tier-based. Law-category test is not performed for a Tier 1 candidate (A-12) |
| Audit trail | PASS WITH NOTES | Decision Log, Registry, Sign-Off, file history (OM 9.1). The Records are files in a repository whose classification is unconfirmed (RI-005); no control on rewriting; DR-2026-012 has no date and its "attached" confirmation is not in the repository (A-29) |
| Reporting to the Board | PASS WITH NOTES | Charter 7.2, Pol 5.3. The appetite is approved by the Executive alone, the Board Committee is told only of a breach (A-05); Board Committee unnamed, no fallback (A-30) |
| Separation of duties | PASS WITH NOTES | OM 4.4(a) to (f) hold. One person is Lead, Engineer and Domain Owner and names the Tier 1 checker, so the checker is the only independent element; the Sponsor names acting CFCs, which weakens their independence (A-10) |

## 7. A8 Activation readiness

Rule: Cat 4.1 (Sponsor sets status, dates the change log, enters the Decision Log), 4.2 (checks of section 7 where 7.1 requires; announcement), 7.1 (check by a person the Sponsor names), 7.2 (no open Blocker or Major Finding, Risk or Issue that concerns the documents).

Steps before any of the four, in order:

1. Sponsor confirms his own appointment and the mandate (RI-001; Appointments "Appointed by" blank for him).
2. Sponsor names the checker of the documents in Appointments and the Decision Log, and states that this report is the check (RI-011; otherwise Cat 7.1 is not met, A-02). AICC Lead then closes RI-006 and RI-013.
3. Sponsor names deputies and acting Contacts at least for model risk and information security (A-03).
4. Sponsor decides the open items that sit above the documents: who approves the Group statement and for which Entities (wiki open items 7, 15), the level of the appetite (RI-002, SOI 7.7), the Board Committee (RI-010).
5. AICC Lead activates the Vocabulary and the Catalog (Cat 4.1), then the Sponsor activates the four and the Lead records it; the Sponsor announces to all employees (Cat 4.2).
6. AICC Lead regenerates the portal (RI-004, UC-006).

| Document | Sponsor must additionally | Open in the path |
| --- | --- | --- |
| SOI 1.0 | Decide who is bound (A-06); approve SOI 7.7 level; set revision | "Appropriate level", Entities, communication to regulators and investors (A-16) |
| Charter 0.5 | Approve the AI Risk Appetite Statement (Charter 5.4, RI-002); set or bridge Envelopes | Approval of appetite and activation of the Charter are two acts in the text; revision 0.5 (A-23) |
| OM 3.1 | Name heads, Platform Owner or acting, deputies | 4.6 unmet on day one (A-03) |
| Pol 0.4 | Name infosec and model risk CFC or acting; decide tolerance scope; check classification (RI-003) | Pol 2.1 versus 2.2 (A-04); Pol 2.4 scope (A-07) |

Unambiguous today: who activates, where it is recorded, who announces. Ambiguous: what revision number a document carries when it goes active (Cat 3.3 gives no rule; 0.4 and 0.5 would be active), the order of activation, how the Sponsor "sets" a status in a repository the Lead keeps, and Cat 7.2 (A-01).

## 8. Verdict

Accept after named fixes. There is no Blocker. The seven Majors are each one action or one clause: A-01, A-03, A-04, A-07 are edits by the AICC Lead; A-02, A-05, A-06 need a decision by the Executive Sponsor first. The Minor findings can follow in one wording pass after activation, except A-08 to A-12, which change meaning and should go in with the Majors (then the documents need the next whole revision and a re-check of the changed clauses under Cat 7.1).

Counts: Blocker 0, Major 7, Minor 26 (33 findings). Earlier: N-01 to N-20 17 fixed, 2 partly, 1 open.

## 9. Findings

| Id | Sev | Category | Evidence | Fix |
| --- | --- | --- | --- | --- |
| A-01 | Major | A8 gate | Cat 7.2 needs no open Major Finding, Risk or Issue "that concerns the documents"; 11 Major items are open (RI-001 to 004, 006 to 009, 011, 013, 014), several about staffing (RI-007, 008, 009, 014), none closable by editing text; no waiver rule | Limit 7.2 to Findings of the check and to RI-001, 002, 003, 006, 013; put staffing items under the rule of A-03 |
| A-02 | Major | A8 precondition | Appointments "Checker of the documents" empty (RI-011); Cat 7.1 requires a person the Sponsor names; RI-006 and RI-013 wait for it | Sponsor names the independent assessor in Appointments and the Decision Log and accepts this report as the 7.1 check |
| A-03 | Major | A5, A8 transition | OM 4.6 (deputy for each Holder, heads, Platform Owner), Pol 2.1 (90-day listing, training), OM 4.4(e) checker, Charter 7.2 Board Committee are unmet at activation; Appointments blank; no deadline or transition clause | Add one clause to Cat 4.2 or OM 4.6: missing Appointments are made within 60 days, acting Holders named by the Sponsor meanwhile, tracked in RI-008 and RI-009 |
| A-04 | Major | A2, A7 | Pol 2.1 tolerates existing uses until 90 days; Pol 2.2 forbids data of a class going to a model not approved for it; at activation no Solution is approved, so confidential data in current use is both forbidden and tolerated | Pol 2.1: the tolerance covers only data that is public or unclassified; other data stops at activation unless approved |
| A-05 | Major | A7, A8 | SOI 7.7 "activated at the appropriate level"; Charter 5.4 Sponsor alone approves, Board Committee told only of a breach; wiki open items 13 and 15 undecided; RI-002 Major open | Decide and state: the Sponsor approves the appetite and the Board Committee notes it at its first report, or the Board approves; same in SOI 7.7 and Charter 5.4 |
| A-06 | Major | A8, A1 | SOI 1.1, 13.5 and Pol 1.1 bind "each Participating Entity"; no Record or clause says how an Entity takes part; Cat 4.1 has the CEO of the Bank activate; SOI 11.3 Level 1 needs Contacts "for each Participating Entity" (Appointments Entity column empty; wiki item 7) | State in SOI 13.5 and Cat 4.1 that activation binds the Bank and that an Entity takes part by its own recorded decision; list Entities in Appointments |
| A-07 | Major | A6, A2 | Pol 2.4: every AI output published to investors, lenders, regulators or the Board needs the Executive Sponsor's approval, bank-wide; "AI output" and "published" undefined; no delegate named, no deputy (RI-009); not listed in OM 4.2 or 5.3; DR-2026-014 facts speak only of AICC | Scope 2.4 to output issued without review by the person who signs it, let the Sponsor's delegate be a named Role, define "AI output", add to OM 4.2 |
| A-08 | Minor | A2 | OM 4.4(b) "The Domain Owner ... accepts and releases it"; OM 4.2, 6.3, Pol 3.3 give the Tier 3 release to the Sponsor | "accepts it and, for Risk Tier 1 and 2, releases it" |
| A-09 | Minor | A2 | Decisions given in the Policy are absent from OM 4.2, 5.3: AICC Lead approves Solutions (Pol 2.1), assigns Tier 1 (3.2), suspends (3.4, 5.4); Sponsor approves output (2.4) and names acting CFCs (7.1); Charter 3.1 bases AICC authority on OM | Add these to the Decides column of OM 4.2 |
| A-10 | Minor | A2, A7 | Pol 7.1 lets the Sponsor name who acts for a Control Function; OM 4.6 says each CF names its Contact; no eligibility rule; Appointments has no "acting" marker | Acting person is a member of that function named with its head's consent and marked "acting" |
| A-11 | Minor | A2 | Pol 3.1 Tier 3 "a decision on credit or insurance for a natural person" reads as any credit use; SOI 9.6, INI-007 (person decides) are Tier 2 by the same table | "a decision on credit or insurance that the AI takes without review" |
| A-12 | Minor | A7 | Pol 3.2 law-category test rests on the compliance CFC; OM 6.3 Intake asks compliance only for Tier 2 or 3; a Tier 1 candidate is never tested | The Tier 1 checker asks the question; compliance CFC confirms when named |
| A-13 | Minor | A6 | Pol 4.1 needs three CFCs for every provider, any Tier, per use or per provider unstated; Pol 3.3 asks bias testing of every Tier 2 use, including an internal coding assistant | 4.1: infosec alone for Tier 1 and for a provider already checked; 3.3: bias testing where output affects persons |
| A-14 | Minor | A3 Q6 | No performer: Tier reassessment (OM 6.3 Operate, Pol 3.3 last row); review of monitoring and alerts (Pol 3.3); listing within 90 days (Pol 2.1); setting training (Pol 2.1 "AICC"); noting knowledge owners (ARC-001) | Name AICC Engineer or Domain Owner for each in one line of Pol 3.5 |
| A-15 | Minor | A1 | SOI 10.1 training "by role before any AI use" (Pol 2.1 covers only a Solution; no Record of who is trained); 10.2 knowledge owners; 10.5 "ongoing monitoring" (Pol 4.1 repeats only at reassessment or change; nobody sees a silent model change) | Add training to Registry or Appointments; Domain Owner checks provider notices at each Sync; Tier 1 provider recheck yearly |
| A-16 | Minor | A1 | No carrier: SOI 5.4 Reuse; 9.6 record of AI contribution (logging Tier 2, 3 only); 6.5 "critical" undefined; 13.4 availability to regulators, investors, customers has no performer or rule | One line each in Standards or Charter 3.1; or qualify SOI 13.4 as "by decision of the Sponsor" |
| A-17 | Minor | A1 | Priorities Measures: seven rows of about 25; only Level 1 has an owner; nobody declares a Level "reached" (SOI 11.1) | Seed all Level 2 measures with owners; Quarterly Report states the Level, Sponsor confirms at Steering |
| A-18 | Minor | A3 Q3 | Duties in present tense, for example Charter 4.2, 6.2, 7.1, 7.2 (sentences 2 to 5); OM 4.6, 6.4, 7.2; Pol 2.3, 3.4, 4.1 last sentence, 5.3; Cat 4.2 "announces"; Voc 3.1 "present tense otherwise" | Voc 3.1: "shall" for a duty, present tense for a fact or an authority; convert the listed clauses |
| A-19 | Minor | A4, A3 Q5 | Used undefined: Validation, checker (Appointments row, OM 4.4(e), Pol 3.3, 3.4), head of function/technology/Domain, stop versus suspend, AI output, Team (OM 5.3), Platform Guardrails (SOI 11), Control Sign-Off | Define Validation, Checker, Stop and suspend in Voc; one line for heads |
| A-20 | Minor | A4 | Defined with capital but used lowercase: Check (about 30 uses), Release (15), Finding (4), Work Item ("work item" OM 5.6, 7.1) | Capitalize in the six documents or define the lowercase sense |
| A-21 | Minor | A3 Q7 | Cat 7.1 Q7 bars lineage but change logs name removed documents (OM 2.0, Charter 0.2, Cat 1.0, Pol 0.1, Voc 1.0); "charter folder" in Voc 1.1, 4.1, Cat 1.1; Voc 3.8 diagram rule, no diagram | Q7 excludes change logs; say "the documents" for "charter folder"; drop Voc 3.8 |
| A-22 | Minor | A3, A8 Templates | Cat 4.1 has the activator date the change log, Cat 6.1 says a Template has none; Template tables (Brief 3, Notes, QR 2, Card 2) have no introducing clause; Brief status lacks "returned" (section 4 uses it); one Domain Owner field, INI-003, 007, 008 have several | Cat 4.1: a Template is activated by the status field and "revised" date; Q8 covers documents only; add "returned"; allow several owners |
| A-23 | Minor | A8 | Activation mechanics: revision at activation (Charter 0.5 and Pol 0.4 go active below 1.0); order (Voc and Cat by the Lead before the four); Sponsor "sets" status while the Lead keeps the files; approval of appetite (Charter 5.4) versus activation of Charter | Cat 4.1: activation sets the next whole revision, the Lead records it on the Sponsor's written decision, Voc and Cat first |
| A-24 | Minor | A6, Q9 | Verbatim: OM 6.3 last two sentences equal Pol 3.4; AI Incident definition Pol 5.1 and Voc; Registry columns in OM 9.2, Voc, SOI 11.2. Tier 3 release in Charter 5.3, OM 4.2, 5.3, 6.3, Pol 3.3 (twice). Annual review in SOI 13.3, Charter 5.4, OM 7.2, Cat 7.1. Steering cadence in OM 7.1 and Voc | Keep each rule in one document and refer by title; cut the OM 6.3 copy |
| A-25 | Minor | A6 | Cat 5.2 limit "about 150 clauses"; largest document has 61; the limit never binds | Set about 80 clauses |
| A-26 | Minor | A6 (N-17) | Stage, Risk Tier, Domain Owner in Backlog, Card and Registry; Registry has 15 columns | Keep each in one Record; drop the copies from the Card and Backlog |
| A-27 | Minor | A2 Records | RI-012 gives the Limits on Work in Progress to the Sponsor, OM 6.1 and Backlog say the team sets them; DR-2026-013 item 4 "No Solution or architecture is produced" and "all seven goals" (six listed) versus INI-004 brief and MS-011 (portal and pipeline built) | Correct RI-012 owner; DR-2026-013: six goals, INI-004 builds under the Tier 2 checks |
| A-28 | Minor | A2 wiki | operating-model-open-items.md: row 6 contradicts Charter 4.2, row 18 "one hour" contradicts Pol 5.3, rows 3, 5, 11, 14, 19 use removed terms; about 10 wiki research files use British spelling; portal JSON cites the old Statement (tracked RI-004) | Delete decided rows; American spelling on the next edit |
| A-29 | Minor | A7 audit trail | DR-2026-012 "exact date to be entered"; Decision Log date "2026-09"; "confirmation attached" but nothing is attached; OM 9.1 relies on repository history with no stated protection | Add date and attach the confirmation; say the repository is write-protected and retained by the Bank |
| A-30 | Minor | A5, A8 | Sponsor "Appointed by" blank (mandate has no source); Board Committee unnamed (RI-010) and Charter 7.2, Pol 5.3 give no fallback | Record the mandate in Appointments; until named, reports go to the Board chair |
| A-31 | Minor | A7 | Pol 5.3 High incident goes to Lead, CFCs, Platform Owner, Sponsor, not to the Domain Owner who is accountable | Add the Domain Owner |
| A-32 | Minor | A2 | Charter 4.1 "funding goes to Strategic Priorities and capacity of teams, not to individual Initiatives"; OM 4.2 Domain Owner funds Use Cases; Charter 4.2 approves Initiatives above a Guardrail | Charter 4.1: say Domain Owners fund Use Cases from the Envelope within Guardrails |
| A-33 | Minor | A5, A6 | Monthly Steering with an empty Committee (two persons); Limits on Work in Progress per Stage and per Domain with four scores (OM 6.1); both stay by decision of the Sponsor, but the Sync and Demo and Quarterly Review name attendees who are not appointed | Keep; revisit at the January 2027 Steering; say a meeting runs with those named |
