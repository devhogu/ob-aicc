# Acceptance, end to end: documents and Records walked through nine scenarios

Assessor: independent (did not write or fix the documents). Date: 2026-09-30. Nothing existing was edited. Read in full: charter/ (six documents, five Templates), portfolio/ Records, INI-001..008 briefs, UC-001..006, DR-2026-009..014, the re-check report 2026-09-30-4 (history only). Scripted: ID existence, link resolution, Decision Log against decision files, metadata and change-log tail, clause counts, Vocabulary "Not used" terms.
Abbreviations: SOI Statement of Intent, Chr Charter, OM Operating Model, Pol AI Policy, Cat Catalog, Voc Vocabulary, CFC Control Function Contact, ES Executive Sponsor, DO Domain Owner, DE Domain Expert, CL change log.
Marks: OK, BLOCKED (cannot proceed today, needs a named person), GAP (no clause or Record), CONTRADICTION (two texts disagree).
State today: all six documents and Templates are draft (none in force); ES not formally confirmed (RI-001); every Contact, head, Platform Owner, checker, DE row in Appointments is empty; only Ademi Moldogazieva is named DO (no From date, no deputy).

## 0. Mechanical results

- IDs: INI-001..008, UC-001..006, DR-2026-001..014, RI-001..015, MS-001..014, PRI-1..7, ARC-001..002, PLT-001..006 all referenced IDs exist. INI-005 appears only in DR-012, DR-013 and the Decision Log (merged, correct). PLT-001..006 are referenced only in standards.md.
- Links: 14 relative links in charter and portfolio (outside assessments), 0 broken. Decision Log rows (14) equal decision files (14).
- Metadata and CL: six documents end their CL on their revision; Catalog 5.1 and 6.1 ids match the files; Templates have no CL by design. Clauses: SOI 52, Chr 15, OM 31, Pol 21, Voc 11, Cat 14 (limit 150).
- "Not used" terms: none in the six documents. Records use "goal" (Voc: Objective; "goal" not used) in seven briefs, Appointments, DR-012/013; Records yield to documents (Voc 2.1) but the mismatch is real (E-27).
- Re-check history: N-01 (release at Pilot exit), N-02/N-03 (acting holders), N-04, N-05, N-07, N-10 are fixed in the text now read. The new findings below are different.
- Not found in the repo: the "confirmation attached" named in DR-012 and Notes 2026-09 (E-04).

## S1 INI-002 service landscape: Backlog to outcome

| Step | Who decides | Clause | Record or Template | Mark |
| --- | --- | --- | --- | --- |
| 1 Enter the Initiative | AICC Lead | OM 6.2 (Initiative leaves Intake with a Backlog entry; enabling work has no Risk Tier) | Backlog rank 2, Tier "n/a", brief | OK, clean |
| 2 Approval of the Initiative | ES | Chr 4.2 (until Guardrails set, ES approves any commitment) | Brief status "approved", DR-012 | OK on paper; evidence missing (E-04) |
| 3 Name DO (EA lead) and DE; set baselines "in the first month" | Head of technology names DO (OM 4.6); ES names acting until then | OM 4.6, OM 6.3 Discovery exit | Appointments (blank), Notes action "October" | BLOCKED on a person (E-02); no RI row |
| 4 Collect artifacts that functions hold | AICC Lead with service owners | Brief item 2 | none | GAP: no clause gives artifacts a data class, or says the map takes the highest class of its sources (E-20) |
| 5 Consolidate in EA repository, publish portal | AICC Lead; infosec confirms access | Brief risk cites RI-005 | RI-005 is about "this repository", not the EA repository or the landscape portal | GAP: access has no owner and no Record; portal README says "behind the bank network" (source file only) |
| 6 Owners review each part | Service owners | Brief item 4; MS-009 | Roadmap MS-009 | OK |
| 7 Mark where AI is used | AICC Lead | Pol 2.1 (90-day listing) | AI Registry (empty) | OK; feeds MS-003. Listing has no performer in Pol 2.1 (passive); INI-002 is the de facto performer |
| 8 Rank candidates into Backlog | AICC Lead | OM 6.1, 6.2 | Backlog (Intake rows); Use Case Card per candidate later | OK |
| 9 Close the Initiative | ES (retirement of an Initiative) | OM 4.2; OM 6.3 Stage table assumes a Use Case after Intake | none | GAP (E-22): no completion step for an Initiative; UC-001..004 sit at "Operate" with "Status: Done" |

Enabling work (no Risk Tier): handled cleanly by OM 6.2 and UC-005/006 "not applicable". One hole: Pol 2.1 and 2.2 bind every use of AI, so AICC's own use of an AI tool on Bank artifacts is not exempt by OM 6.2, and nothing is registered (E-21). Doable today by one person: steps 1, 4 to 8 for functions that cooperate.

## S2 INI-004 FP&A Board reporting to a first monthly Board edition

| Step | Who decides | Clause | Record or Template | Mark |
| --- | --- | --- | --- | --- |
| 1 Stock-take of FP&A's existing AI reports; metric definitions | AICC Lead with DO Ademi Moldogazieva | Brief items 1-2 | Brief; Appointments (DO row, no From date, no deputy (OM 4.6)) | OK today |
| 2 Appointment of the DO | Head of Domain (OM 4.6) | OM 4.6 | Appointments says "Executive Sponsor, by the goal of INI-004"; DR-013 item 3 says AICC Lead decided | CONTRADICTION (E-05) |
| 3 Name the DE | DO | OM 4.6, Discovery exit | Appointments blank | BLOCKED on Ademi (quick) |
| 4 Use Case and Card for the monthly edition | AICC Engineer and DE | OM 6.3 Intake; Card | No UC id exists for INI-004; Backlog says "per Use Case, at Intake" | GAP: none created (should be UC-007) |
| 5 Risk Tier | CFC of model risk (Pol 3.2). Lead may assign only Tier 1 where all attributes indicate it | Pol 3.1 (confidential data, informs a Board decision = Tier 2), 3.2, 7.1 | Card 4, Backlog, Registry | BLOCKED: no model-risk Contact; the Use Case "waits". Needs an acting Contact from ES (Pol 7.1) |
| 6 Is the pipeline a Solution with a Tier? | Model risk | Voc "Solution"; Pol 3.1 "agent with rights over systems"; Chr 5.3 | Brief says "Tier 2 expected"; steps say the pipeline "publishes" | GAP (E-06): the agent collects from financial sources and writes to the Board portal; the brief does not say publish is a human act after ES approval, so Tier 3 is open |
| 7 AI Registry entry | AICC Lead | OM 6.3 Intake | Registry (empty, 15 columns) | OK once the Card exists |
| 8 Validation before Pilot | CFCs of model risk and infosec only (no customer, no personal data); security test against AI attacks; error testing; logs | Pol 3.3 Tier 2; DR-011 item 5 | Control Sign-Off (TPL-03) per CFC | BLOCKED: no CFCs, no Platform Owner for logs (Pol 3.5; PLT-002; OM 4.6 acting holder rule exists, nobody named). Tier 1 check also applies (Pol 3.3 "higher includes lower") but OM 6.3 Pilot omits it (E-23) |
| 9 Pilot = first monthly edition | Team; ES approves the edition | OM 6.3 Pilot; Pol 2.4; DR-014; Brief item 5 | Card; UC folder | OK in rule; no Record for approval (E-08) |
| 10 Traceability of figures | DO / AICC Lead | Brief; SOI 9.3; RI-015 "keep the source and date of each figure" | none | GAP (E-07): "governed source" is undefined; Chr 7.2 is the rule for AICC's own report to the Board Committee, but the brief and RI-015 cite it for FP&A editions; no Standard, Template or folder for figure lineage |
| 11 Approval by ES before issue | ES, optional delegate | Pol 2.4; Chr 7.2; DR-014 | Decision Log line per approval? OM 5.6 would require it; Appointments has no delegate row; no deputy for ES (RI-009) | GAP (E-08); single point of failure each month |
| 12 Release (leaving Pilot) | DO Ademi, after validation (Tier 2) | OM 6.3; Pol 3.3 | Registry "Released by" | OK; two distinct approvals (release of the Solution, approval of each edition) are not distinguished in DR-014 or the brief |
| 13 Quarterly edition designed; Board Committee report | AICC Lead prepares; ES approves and issues | Chr 7.2 | Quarterly Report (TPL-05) | GAP: no Template or Record for the Board Committee version; Board Committee unnamed (RI-010) |

Domain Owner: Ademi Moldogazieva (Backlog, Priorities PRI-2, Appointments, MS-011, brief agree; five Records consistent). Domain Expert: not named. Records updated along the path: Backlog (Stage), UC card, Registry, Sign-Offs, Appointments (DE, acting Contacts, Platform Owner, delegate), Risks and Issues, Decision Log (ES approvals, if OM 5.6 is applied to each edition), Notes (Steering), Roadmap MS-011, Quarterly Report. Also: FP&A already sends AI-assisted reports to the Board today; Pol 2.4 has no tolerance period, so from activation each such report needs ES approval (Pol 2.1 tolerance covers only listing). Investor-facing figures have no Control Function check of disclosure: Tier 2 remits are triggered only by customer or personal data (E-09).

## S3 INI-003 functions adopt a generative AI assistant

| Step | Who decides | Clause | Record | Mark |
| --- | --- | --- | --- | --- |
| 1 Meet functions, list routine tasks, rank by time and risk | AICC Lead with function heads | Brief 1-2; OM 8.1 | Backlog | OK today; five DOs unnamed (E-02) |
| 2 Approve an assistant for a data class and purpose | AICC Lead with the infosec Contact | Pol 2.1, 2.2 | Registry "Approved for (data class)" | BLOCKED: no infosec Contact; no assistant is named anywhere; Registry is per Use Case, so an assistant shared by five functions has no row and no approval date (E-11) |
| 3 Provider check | Contacts of infosec, data protection, legal | Pol 4.1, 7.1; OM 6.3 Discovery exit | Registry "providers" column only; no check date or Template | BLOCKED (three Contacts) and GAP (E-11) |
| 4 Tier | Model risk; Lead provisionally Tier 1 only | Pol 3.1, 3.2 | Card 4 | HR, compliance, finance, accounting data is confidential or personal: Tier 2, BLOCKED. Tier 1 needs public or unclassified data (Pol 3.1) and the Bank classification is unchecked (RI-003) |
| 5 Personal and confidential data | DP and infosec Contacts | Pol 2.2, 2.5, 3.3 | Sign-Off | BLOCKED; data classes agreed "with information security" (brief item 4) has no Record except Registry "Approved for" |
| 6 Training | AICC | Pol 2.1 (before first use) | none | GAP (E-24): brief says training "on the job"; no Record of content or attendance; "guidance for each function" has no home |
| 7 Pilot, first working use | Team | OM 6.3 | Card, Backlog | Only Tier 1 without a provider can start; a hosted assistant needs step 3 |
| 8 Existing uses listed within 90 days of activation | Nobody named (passive) | Pol 2.1; PLT-006 | Registry; MS-003 (Q1) | GAP (E-10): tolerance covers listing, not approval; after the 90 days an existing use still needs approval with an infosec Contact; Tier 2 uses cannot be assigned a Tier (Level 1 measure) without a model-risk Contact |

What can begin before Contacts are named: ranking of tasks; conversations; drafting Cards; guidance text; Tier 1 use of public data on a locally run model if one exists. Nothing with a provider, nothing on HR or compliance data. On the day of activation no Solution is approved, so every new use breaches Pol 2.1 (E-10).

## S4 INI-007 mortgages: analysis of rejection reasons on real customer data

| Step | Who decides | Clause | Record | Mark |
| --- | --- | --- | --- | --- |
| 1 Sessions with the retail credit function; rank opportunities | AICC Lead with the function | Brief 1-2; MS-013 | Backlog | OK today; DO unnamed |
| 2 Risk Tier of the analysis | Model risk; any CFC may raise | Pol 3.1 (personal, credit data; influences a decision: Tier 2; "decision on credit for a natural person" is Tier 3) | Card 4 | BLOCKED; Tier 2 at least. Risk that it rises to Tier 3 is not analyzed (E-12) |
| 3 Who validates | Model risk, infosec, data protection, compliance (customers affected, credit law), legal if a provider | Pol 3.3, OM 6.3 Intake exit (compliance confirms applicable law for Tier 2/3), Pol 4.1 | Sign-Off per CFC | BLOCKED: all five Control Functions unnamed. Separation holds: CFCs outside AICC (OM 4.4(c)), DO releases and does not validate (4.4(b)), Lead may build but not validate (4.4(d)) |
| 4 First analysis on real data "where permitted" | see 5 | Brief item 5 | none | GAP (E-13): the Stage table ties validation to Pilot; "controlled experiment" (SOI level 1) is undefined; nothing says whether aggregated, de-identified or synthetic data is a lower data class |
| 5 Allowed before Contacts exist | AICC Lead | Pol 7.1 | - | Only sessions, discovery, approach design, and a written data request. No real customer data, no provider |
| 6 "A person always decides on a mortgage" | DR-013 item 5 (AICC Lead); brief "Out of scope" | Pol 3.3 Tier 2 "a person decides each case that affects an individual"; SOI 9.6 (system records both AI contribution and decision); Chr 5.3 | Brief, DR-013, MS-013 | The statement exists; it is not a control |
| 7 Recorded and protected against silent drift | DO in operation (Pol 3.5) | Pol 3.3 (Tier 2 monitoring: "logs kept"; reassessment each year; Pol 3.4 returns to Discovery only on a change that the validation named) | Registry "scope" column; Sign-Off "revalidate on" | GAP (E-12): no clause, Standard, Card field or Sign-Off condition says output is aggregate only, no output on an individual application, who reviews logs for case-level use, or that a case-level output is a named revalidation trigger |

The statement is a Decision of the AICC Lead about another function's process; it sits only in DR-013, the brief and MS-013. It would be protected if (a) the Sign-Off lists it as a condition with "revalidate on any output about an individual application", (b) the Registry scope says so, (c) a Standard requires logging of queries and review in the quarterly risk check.

## S5 INI-006 customer experience, INI-008 knowledge bases

| Step | Who decides | Clause | Record | Mark |
| --- | --- | --- | --- | --- |
| INI-006 1-2 Map sources with owner, format, volume, data class | AICC Lead with owners | Brief | none named for the source map | GAP: no Record for the source map; data class needs the Bank rules (RI-003) |
| INI-006 4 Sample test on customer data | see S4 step 4 | Pol 2.2, 2.5 (only the data required), 3.3 | Sign-Off | BLOCKED until Contacts; ambiguity E-13 |
| INI-006 6 Proposal for the next quarter | ES, after asking the AISC | OM 5.3, 7.1 quarterly Steering | Notes, Decision Log, Backlog | OK; first quarterly Steering is January 2027, after the 31 December outcome date; AISC is empty (E-29) |
| INI-008 1 Common approach; owner and review date per source | AICC Lead | Standards ARC-001; Registry column "Knowledge sources, owner, review date"; Card 3 | Registry, Card | OK in rule; GAP (E-26): one cell per knowledge base cannot hold dozens of sources, no per-source list, so the Measure "sources with an owner and a review date" has no place to be counted |
| INI-008 4 First base with legal | Model risk, infosec (confidential contracts: Tier 2); provider check | Pol 3.1, 3.3, 4.1 | Card, Sign-Off | BLOCKED (Contacts, Platform Owner for the knowledge layer and access by class; SOI 11.2 places the knowledge layer at Level 2) |
| INI-008 legal as Domain and as Control Function | DO of legal; legal CFC validates provider terms | OM 4.4(b), 5.7 | Appointments | GAP (E-25): same function is owner and validator; no rule for different persons |

Tier 2 is correct for both. Enabling work: none. The decision on next quarter, the "second knowledge base, started" by December, and any spend need ES approval until Guardrails are set (Chr 4.2): no default for what a "commitment" is when cost is "the time of the AICC Lead".

## S6 A quarterly cycle

| Item | Documents say | Records and Templates | Mark |
| --- | --- | --- | --- |
| Quarterly Review | AICC team, DOs, CFCs; sets Objectives, scores value, quarterly risk check; output is the Quarterly Report (OM 7.1, Voc) | Notes (TPL-04); Report section 2 has "Value scored by the Domain Owner" | OK in form; today only the AICC Lead exists; quarterly risk check has no CFC |
| Quarterly Report | AICC Lead prepares (OM 4.2, Chr 7.2); goes to next quarterly Steering (Chr 7.2 rev 0.5); for the AISC (TPL-05) | reports/ named `2027Q1.md` | OK, names and owners agree; sections 4 (Envelope) and 3 (Measures against baseline) cannot be filled: no Envelope is set for 2026, baselines are blank |
| Quarterly Steering | Assesses the past quarter from the Report; confirms priorities, funding; first one of the year also sets Priorities, Envelopes, Guardrails, roadmap and reviews four documents and the appetite (OM 7.1, 7.2; SOI 13.3) | Notes; DR-012 and DR-014 revisit "January 2027" | OK, aligned on January 2027 |
| Board Committee report | AICC Lead prepares from the Report; ES approves and issues (Chr 7.2; Pol 2.4) | No Template, no Record, Board Committee unnamed (RI-010) | GAP (E-28) |
| Yearly review and yearly check | OM 7.2 (review at first quarterly Steering); Cat 7.1 (check once a year by the ES-named person) | Appointments checker row blank | GAP (E-29): the check has no anchor date; RI-011 names it only "each year" |
| Quarter 0 | Roadmap: Quarter 0 = September to December 2026; next is Quarter 1 (`2027Q1`) | Template field "year and quarter" | GAP (E-27): Q0 is not a calendar quarter and has no report name; its Objectives were set by the ES as "goals", not by a Quarterly Review; Quarterly Review needs DOs and CFCs who do not exist |

## S7 High Severity AI Incident in a live Solution; only the ES and the AICC Lead exist

| Step | Who | Clause | Record | Mark |
| --- | --- | --- | --- | --- |
| Which Solutions can be live? | Tier 1 without a provider; existing uses tolerated 90 days after activation (Pol 2.1); FP&A reports to the Board | Pol 7.1 | Registry | The tolerated existing uses are the realistic source of an incident |
| Report | Anyone to AICC Engineer or Lead; High goes "at once" to Lead, CFCs, Platform Owner, ES | Pol 5.3 | none | Two recipients exist; CFCs and Platform Owner do not. Nothing assigns who classifies Severity (Pol 5.2) |
| Containment | AICC Engineer contains; AICC Lead or any CFC suspends | Pol 5.4; OM 5.4; PLT-005 | Decision Log line for a suspension (OM 5.6) | OK if AICC built it. For an existing Domain use there is no AICC Engineer and no Platform Owner (GAP). The Lead suspends and lifts his own suspension (OM 5.4) with no independent person |
| Regulator notification | Compliance decides | Pol 5.4; Pol 7.1 ("may name at any time ... including for an AI Incident") | Appointments | GAP/BLOCKED until ES names an acting compliance person; the clause is permissive, there is no pre-naming duty or time limit. Data protection notice likewise |
| Board Committee told | ES, without waiting | Pol 5.3; Chr 7.2 | none (no place records that it was told); Board Committee unnamed | GAP |
| Review within ten working days; entries | "The people involved"; entry passive | Pol 5.5 | Risks and Issues (type Incident); Registry; Quarterly Report section 5 | GAP: no Role enters the Incident (Cat Q6) |

Doable today only if the ES can name an acting compliance person and an acting data protection person within hours. E-14.

## S8 Activation

| Step | Who | Clause | Record | Mark |
| --- | --- | --- | --- | --- |
| 1 ES formally confirmed and source of mandate | ES | Chr 3.1; RI-001 | Appointments (no "Appointed by", no From) | BLOCKED on ES; no document says who appoints the ES |
| 2 ES names the checker | ES | Cat 7.1; OM 4.4(e) | Appointments checker row blank; RI-011 (Major) | BLOCKED; RI-011 says "each year" though the check is needed before first activation |
| 3 Ten questions on each document; Findings to Risks and Issues | Checker | Cat 7.1, 7.2 | Risks and Issues | GAP (E-16): no Finding row exists although the re-check listed 20 new findings; readiness (Cat 7.2) cannot be computed. Q10 fails for Pol until acting Contacts exist |
| 4 Is the first activation a "change of meaning" needing the check? | Cat 4.2, 7.1 | - | - | GAP (E-15): ambiguous; no rule for the revision or CL row at activation (Charter 0.5 to 1.0?) |
| 5 ES sets active (SOI, Chr, OM, Pol); date in CL; Decision in Decision Log | ES | Cat 4.1; OM 4.2; DR-004 | Decision Log, CL | Doable; DR-004 is an AICC Lead decision that predates the Catalog. Cat 4.1 tells the ES to act and is itself activated by the Lead |
| 6 ES announces to all employees | ES | Cat 4.2; SOI 13.4 | none | GAP: no channel; documents are EN only (Cat 5.1) while they bind employees |
| 7 AICC Lead activates Voc and Cat | AICC Lead | Cat 4.1 | Decision Log | OK; but Cat 7.1 names a duty for the ES and Voc styles every document (E-33) |
| 8 Templates | - | Cat 6.1 | - | GAP: no activation rule for the five Templates; Records are already made from draft Templates (E-33) |

Decision Log needs, per OM 5.6: date, Decision, facts (checker, date, open Findings), decided by, revisit; one line per document or one batch; a short note in decisions/ is advisable (hard to reverse). Complete except the gaps above. Also 2.1's 90 days and the Level 1 Measures start from activation.

## S9 Change of an active document (example: the Risk Tier table, Pol 3.1)

| Step | Who | Clause | Mark |
| --- | --- | --- | --- |
| Propose, edit | AICC Lead (owner, Cat 1.2) | Cat 1.2, 3.3 | OK |
| Status during the change | - | Cat 3.2 has draft, active, deprecated only | GAP (E-17): editing an active file leaves it "active" with unapproved text; setting it to draft withdraws the policy |
| Revision | Next whole number, since meaning changes | Cat 3.3, 4.2 | OK |
| Check | Person other than the author whom the ES names | Cat 7.1 | OK; one checker for all; Findings to Risks and Issues |
| Consultation | - | none | GAP: Control Functions, who apply the table, are not consulted; Tier appears in SOI 7.8, Chr 5.3, OM 4.2/6.3, Voc, which rank above Pol |
| Activation | ES (binds outside AICC) | Cat 4.1; OM 5.2(e), 5.3 (after asking the AISC, empty) | OK; SOI 13.5 covers "amendments" only for the SOI |
| Decision Log and CL row | Activator | Cat 3.1 allows "none" for the Decision; Cat 4.1 requires a Decision only for activation | GAP: after activation a meaning change could carry "none" |
| Effect on existing Registry entries | - | Pol 3.3 reassesses on change of the Use Case, not of the policy | GAP |

## A. Records integrity

| Check | Result |
| --- | --- |
| Backlog against briefs | Titles, PRI, DO, Stage agree (Oxford comma only). Rank follows the order of DR-013, not the OM 6.1 scores (INI-004 scores higher than INI-006 and INI-002 relative to effort): E-31. Enabling label differs: "none (enabling)" (INI-001) and "Enabling (all)" (INI-002) |
| Roadmap | MS-009..014 match the briefs' outcomes and INI ids. CONTRADICTION: MS-006 (first Use Case, Q1) and MS-007 (first Pilot, Q2) against MS-011, 012, 014 (live use in Q0): E-19 |
| Priorities | PRI names match SOI 9.2-9.8. "Domain Owners" column holds functions, not persons; PRI-4 omits compliance that INI-008 lists; Envelopes, targets blank (Chr 4.1 requires a yearly Envelope; RI-012 covers Guardrails only) |
| Appointments | Only Ademi named; PRI-2 and five Records agree. Basis differs (ES in Appointments, AICC Lead in DR-013); no From date, no deputy |
| Risks and Issues | IDs RI-005 and RI-014 referenced exist. RI-005 cited by INI-002 for the wrong object. RI-014 owner ES but status "waiting on the Control Functions"; review 2026-11-30 leaves about four weeks before December. RI-015 "Closed: approver named" while its action is open; severity Minor for Board figures. No row for: Domain Owners, Platform Owner, capacity, the assessment findings (E-34) |
| Decision Log against files | 14 of 14. DR-012 date "2026-09" and "(exact date to be entered)"; DR-014 facts "approves everything that AICC does" against a narrow clause (E-35). DR-001..008 not assessed (history) |
| Notes | Only file `2026-09-first-100-days.md`: name breaks the `2027-01-15-sync.md` convention; date missing (E-35) |

## B. Templates

| Template | Usable as written | Note |
| --- | --- | --- |
| Use Case Card (TPL-01 r1.2) | Yes for S2-S5; section 3 now asks influence, autonomy, knowledge sources | No field for limits of use ("no output on an individual"), for figure lineage, or for the provider check. UC-001..006 omit sections 2, 3, 5, 6, add "Status", use Stage "Operate" for finished work (E-32) |
| Initiative Brief (TPL-02 r1.0) | INI-001 follows it. INI-002..008 deviate: merged field "Domain and Domain Owner" and added "Period"; status text with a parenthesis; section 2 "and scope"; section 3 retitled "Outcome, Measures, cost, and risk", benefit table dropped, baselines "set with the Domain Owner in the first month" (five DOs unnamed, "first month" undefined); no Investment Envelope line; hypotheses lack "measured by"; section 4 gives a DR but no date | Justified in part: discovery goals have no baseline and no envelope. Not recorded: neither DR-013 nor the Template says the Template is relaxed for discovery (E-30). Length is about 45 lines each, beyond one page |
| Control Sign-Off (TPL-03 r1.1) | Yes | Covers conditions and "revalidate on"; one per Use Case, so it cannot record a provider check or an assistant approval (E-11) |
| Notes (TPL-04 r1.0) | Yes | Steering of Sept 2026 lacks date; no space for ES approvals of editions |
| Quarterly Report (TPL-05 r1.1) | Yes | Field "year and quarter" does not fit Quarter 0; section 4 has no Envelope to report against; no Board Committee variant |

## Findings

Severity: Blocker = no path even with named persons; Major = path closed, contradicted or unrecorded; Minor = fixable by a line. No Blocker found: every closed path opens when the ES names persons (E-01, E-02).

| Id | Sev | Scen | Evidence | Fix |
| --- | --- | --- | --- | --- |
| E-01 | Major | S2-S5,S7 | Appointments: no Contact, Platform Owner, Tier 1 checker; Pol 7.1, 3.2; RI-008, RI-014 (review 2026-11-30); Notes action "as soon as possible" | ES names acting model risk, infosec, data protection, compliance, legal Contacts, Platform Owner and the checker in Appointments by 2026-10-31; move RI-014 review to 2026-10-31 |
| E-02 | Major | S1-S5 | Five of six briefs: DO "to be named"; baselines "set with the Domain Owner in the first month"; OM 6.3 Discovery exit; only a Notes action, no RI row | Add an RI row owned by the ES with date; set baselines to a dated point; name the five DOs and DEs |
| E-03 | Major | S2,S3,S5 | DR-013 item 4 "No Solution ... is produced in this period" against INI-004 items 3-4 and outcomes, INI-008 "first knowledge base in use", INI-003 "first working use", MS-011/012/014 | Reword DR-013 item 4: discovery first; any Solution goes through the Stages as a Use Case with its checks |
| E-04 | Major | S8,S2 | DR-012 and Notes say "confirmation attached"; no file exists; date "2026-09 (to be entered)"; all six approvals rest on it | Attach the confirmation or record the ES's own decision line with its exact date |
| E-05 | Major | S2 | DR-013 (AICC Lead) merges INI-005 (OM 4.2: ES decides retirement), widens INI-008, names a DO (OM 4.6: head of Domain names; Appointments says ES); briefs say "approved" for the restated scope | ES confirms DR-013 in a Decision Log line; align Appointments "Appointed by" |
| E-06 | Major | S2 | Brief item 4 "publishes"; Pol 3.1 Tier 3 "agent with rights over systems"; Chr 5.3; brief "Tier 2 expected"; no UC card | Put in the Card: read-only sources, publish is a human act after ES approval; model risk confirms the Tier |
| E-07 | Major | S2 | "governed source" undefined (Chr 7.2, SOI 9.3); Chr 7.2 cited for FP&A editions but governs the Board Committee report; Standards hold only ARC-001/002; RI-015 closed, Minor | Add ARC-003 (figure, source, date, calculation, reviewer per edition); reopen RI-015 at Major; cite SOI 9.3 |
| E-08 | Major | S2 | Pol 2.4, DR-014, OM 5.6: no Record of each approval, no reviewer before ES, no delegate row, no ES deputy (RI-009) | Per edition: one file in the UC folder with review and ES approval; add delegate row to Appointments |
| E-09 | Major | S2 | DR-012 "to investors"; brief "may reach investors"; Pol 3.3 remits triggered by customer or personal data only | Card records whether output reaches investors; compliance Contact confirms disclosure rules before first issue |
| E-10 | Major | S3,S8 | Pol 2.1: no approved Solution, Registry empty; tolerance covers listing only; 90-day listing has no performer; Pol 2.4 has no tolerance; Level 1 Tier needs model risk | Approve one first assistant at activation; name the performer; state that listed uses keep tolerance until approved or stopped, with a date |
| E-11 | Major | S3-S5 | Pol 2.1 approval and Pol 4.1 provider check: Registry row is a Use Case; no provider row, check date or Template; Sign-Off is per Use Case | Registry rows of type model or provider with "Approved for", check date, valid until; or Sign-Off variant |
| E-12 | Major | S4 | "A person always decides" only in DR-013, brief, MS-013; Pol 3.3 Tier 2 monitoring "logs kept"; Pol 3.4; Tier 3 "decision on credit" | Sign-Off condition: no output on an individual application, revalidate on any; Registry scope; Standard for query logs and recording AI contribution and decision (SOI 9.6); check in quarterly risk check |
| E-13 | Major | S4,S5 | Brief INI-006 item 4 and INI-007 item 5 (real data in Discovery); OM 6.3 ties validation to Pilot; "controlled experiment" (SOI 11.1) undefined; no rule for de-identified data | One clause: any use of Tier 2 data, in any Stage, needs approval of the service for the class and model-risk and data-protection clearance; define de-identified data class |
| E-14 | Major | S7 | Pol 5.3-5.5, 7.1 permissive; no Severity classifier; no containment for existing Domain uses; Lead suspends and lifts (OM 5.4); Board Committee unnamed; Pol 5.5 passive | ES pre-names acting compliance and data protection persons at activation; Lead classifies Severity; lifting after High needs ES or CFC; a Role enters the Incident |
| E-15 | Major | S8 | Cat 4.2/7.1 silent on first activation and on revision and CL row at activation; Cat 7.2 not met (RI-002, 003, 006, 013 open Major); Pol Q10 fails without Contacts | State: first activation needs the ten questions; activation sets revision 1.0 and a CL row with the DR |
| E-16 | Major | S8,S9 | Cat 7.1 requires Findings in Risks and Issues; none exist; assessments README says findings are tracked there; 20 re-check findings (N-01..N-20) and this report | Enter each open Finding with Severity and owner; close those fixed with the DR |
| E-17 | Major | S9 | Cat 3.2 statuses; Cat 4.1 covers activation only; Cat 3.1 "none"; SOI 13.5 covers SOI only | Add: a change to an active document is a new draft revision that does not replace the active one until activated, and needs a Decision Log entry |
| E-18 | Major | all | Seven Initiatives, UC-005/006, all cost "time of the AICC Lead"; one person builds, leads, confirms exits (OM 6.3), is DO of own work; Limits on Work in Progress unset (RI-012 Minor) | Set a Limit on Work in Progress now; add an RI row for capacity; sequence INI-004 and INI-008 builds after acting Contacts exist |
| E-19 | Minor | A | Roadmap MS-006 Q1, MS-007 Q2 against MS-011, 012, 014 Q0 | Move MS-006/007 to Q0 or narrow MS-011/012/014 |
| E-20 | Minor | S1 | No clause on class of collected artifacts; brief cites RI-005 (this repository) for the landscape portal | New RI row for the EA repository and portal with infosec; rule: map takes highest class of its sources |
| E-21 | Minor | S1 | OM 6.2 no Tier for enabling work; Pol 2.1, 2.2 bind all use; Registry empty; repo uses an AI tool (CLAUDE.md) | Register the AICC tools, or state that Pol 2.1 applies to AICC's own work |
| E-22 | Minor | S1 | OM 6.3 stages assume a Use Case; UC-001..004 "Operate"/"Done"; OM 4.2 ES retires an Initiative | Define done for an Initiative and for enabling work (Backlog status Done plus Decision Log line) |
| E-23 | Minor | S2 | Pol 3.3 "higher includes lower" against OM 6.3 Pilot (check for Tier 1, validation for 2 and 3) | Say whether Tier 2 also needs the Tier 1 check |
| E-24 | Minor | S3 | Brief "training on the job" against Pol 2.1 "before first use"; no Record of training | Allow supervised first use as training, or put training before; add a place for guidance |
| E-25 | Minor | S5 | Legal is Domain and Control Function; OM 4.4, 5.7 | Require different persons for DO/DE and the legal Contact; note in Appointments |
| E-26 | Minor | S5 | ARC-001 and Registry column hold owner and date in one cell per knowledge base | One source list per base in the UC folder, linked from the Registry |
| E-27 | Minor | S6 | Quarter 0 versus `2027Q1`; Template "year and quarter"; "goal" in Records against Voc "Objective" | Name the first report `2026Q4` or `Q0`; say the ES's goals are the Objectives of Q0 |
| E-28 | Minor | S6 | Chr 7.2 Board Committee report: no Template or Record; Envelope not set (Chr 4.1) | Add a Board Committee section to TPL-05 or a file name; set Envelopes or state "none for 2026" |
| E-29 | Minor | S5,S6 | January 2027 Steering carries Q0 assessment, annual settings, document review, four proposals; OM 5.3 asks an empty AISC; Cat 7.1 check has no date | Plan two sessions; say the ES decides alone while the AISC is empty; anchor the yearly check |
| E-30 | Minor | B | Briefs INI-002..008 deviate from TPL-02 unrecorded; status text; no decision date | Record the relaxation for discovery in a DR or amend the Template |
| E-31 | Minor | A | Backlog rank against OM 6.1 scores; no note | Note that order follows DR-013 |
| E-32 | Minor | B | UC-001..006 against TPL-01 | Add a short enabling-work form or mark cards "no AI" |
| E-33 | Minor | S8 | Templates have no activation rule; Cat 4.1 binds the ES though Cat is activated by the Lead; EN only; no Record of Participating Entities (Bank CEO activates for the Group) | Add Template activation; state that scope is the Bank until an Entity joins; plan RU and KY |
| E-34 | Minor | A | RI-005 object; RI-014 owner and status; RI-015 closed with open action; RI-011 scope | Edit the four lines |
| E-35 | Minor | A | DR-014 facts "approves everything"; DR-012 date format; Notes file name and date | Correct wording, date, file name |

## Verdict: accept after named fixes

Counts: Blocker 0, Major 18, Minor 17 (35 findings).
Named fixes: E-01 to E-05 (persons, evidence and scope of the approvals), E-06 to E-09 (INI-004 path), E-10 to E-13 (assistant, provider, credit control, real data), E-14 to E-18 (incident, activation, change, capacity). Minor findings can follow in one wording pass.

## What can start today, and what waits

Can start today (no document in force is needed; drafts and discovery only), by the AICC Lead alone:
- INI-002 steps 1, 4 to 8 on artifacts that functions offer, with the classification question raised with information security.
- INI-004 stock-take, metric definitions, the approval flow, the lineage table, with Ademi (DO named); Card drafts for UC-007.
- INI-003, INI-006, INI-007, INI-008: sessions, source maps, ranked lists, approach text, data requests; Cards in draft. No real personal, customer or confidential data into any model.
- UC-005: the independent check, after the ES names the checker; entering Findings.

Waits on the Executive Sponsor: formal confirmation and mandate source (RI-001); checker (RI-011); acting Contacts for model risk, information security, data protection, compliance, legal; Platform Owner; acting heads; Board Committee (RI-010); Guardrails and Envelopes; naming the five DOs with the heads; activation and announcement of SOI, Charter, OM, Policy; confirmation of DR-013; deputies and delegate.
Waits on the heads of function: DO and DE for INI-002, 003, 006, 007, 008.
Waits on Ademi Moldogazieva: the DE for INI-004; baselines.
Waits on the Contacts once named: Risk Tier, validation, provider check, data class approval, compliance confirmation of applicable law.
Waits on the AICC Lead after activation: Tier 1 provisional assignment, assistant approval with infosec, the 90-day listing, the activation of Vocabulary and Catalog.
