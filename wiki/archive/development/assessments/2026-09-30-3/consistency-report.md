# Consistency and acceptance report: the simplified corpus

Assessor: independent (did not write the documents). Date: 2026-09-30. Scope: charter/ (six documents, five Templates), portfolio/ Records (not assessments/, not DR-2026-001 to 008), wiki/ (not archive/). Every file was read in full. Nothing was edited. References are clause numbers; "OM" is the Operating Model, "SOI" the Statement of Intent, "Cat" the Document Catalog, "Voc" the Vocabulary, "Pol" the AI Policy, "CFC" Control Function Contact.

Severity: Blocker blocks activation (a binding clause contradicts another, or cannot be met on day one with no stated fallback); Major; Minor.

## 1. The ten questions of Catalog 7.1, asked literally

P = pass, F = fail, with the finding that explains it. Result: 17 of 60 pass. Q7, Q8 and Q9 fail everywhere on small literal points (change log tables, change log lineage, repeated statements); the substantive failures are in Q3, Q4, Q6 and Q10.

| Q | SOI (MND-01 0.9) | Charter (MND-02 0.2) | OM (ORG-01 2.2) | Policy (POL-01 0.1) | Vocabulary (REF-01 1.0) | Catalog (REF-02 1.0) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 Metadata, change log ends on revision | P | P | P | P | P | P |
| 2 Defined terms, no "Not used" term | F C-26, C-27 | F C-26 | F C-27 | F C-26, C-27 | F C-27 | F C-27 |
| 3 Numbered, "shall" for each obligation | F C-06 | F C-06 | F C-06 | F C-06 | F C-06 | F C-06 |
| 4 Agrees with higher documents | P (highest; lower documents disagree, C-05, C-07) | F C-05, C-18 | F C-04, C-05, C-08 | F C-01, C-17 | F C-16 | P (no place in precedence, C-23) |
| 5 Every Role, Record, Template named is defined | P | P | P (Holder, C-27) | P | P | P (TPL, C-22) |
| 6 One Role per requirement | F C-14 | P | F C-11 | F C-15 | P (Cat 1.2) | F C-12 |
| 7 No open question, lineage, file reference | F C-28, C-05, C-32 | F C-28 | F C-28 | F C-28, C-09 | F C-28, C-05 | F C-28 |
| 8 Table intro clause, links work | F C-29 | F C-29 | F C-29 | F C-29 | F C-29 | F C-29 |
| 9 Size, says nothing another says | F C-33, C-35 | F C-33 | F C-33 | F C-33, C-34 | F C-35 | F C-33, C-35 |
| 10 Doable today | F C-13, C-14 | F C-05, C-13 | F C-01 to C-04, C-13 | F C-02, C-03, C-10, C-13 | P | F C-12 |

Evidence for the main cells:

- Q3. "shall" occurs once in OM (4.4(c)), once in Charter (3.2), four times in Pol (2.1, 2.2, 2.4, 2.5) out of 19 clauses, never as an obligation in Cat or Voc (Voc 3.1 and Cat 7.1 Q3 only mention the word). Obligations in the present tense: OM 4.4(a), 4.4(b), 5.6, 5.7, 6.1, 9.1; Cat 3.1, 4.1, 7.1; Charter 3.3, 6.2, 7.2; Pol 3.3 table, 4.1, 5.3, 5.5, 6.1; SOI 6.7, 7.3.
- Q4. Charter 7.2 (the Executive Sponsor reports to the Board Committee) against SOI 12.2 (AICC reports to it); Charter 5.2 against SOI 4.2; OM 3.2 against SOI 4.1; Pol 3.2 against OM 4.2; Voc "Exception" against OM 4.2 and Pol 6.1.
- Q7. SOI change log cites F-003, F-044, F-059, F-072, F-039, F-040 (archived findings); OM 5.6 "decisions folder", OM 9.1 "files in the repository", Cat 6.1 "templates folder", Voc 3.4 "wiki"; SOI 7.6 and Voc "Board Committee" define it as "technology or risk" committee (an unresolved choice, wiki open item 14).
- Q10. See section 3.

## 2. Findings

Columns: id, severity, category, evidence, recommended fix.

### 2.1 Blockers

| Id | Sev | Category | Evidence | Fix |
| --- | --- | --- | --- | --- |
| C-01 | Blocker | contradiction | OM 4.4(a) "No person validates or releases work that the person built, owns, or benefits from" contradicts OM 4.2 and Pol 3.3 (Release row): the AICC Engineer, who builds, releases Tier 1; the Domain Owner, who owns the Use Case as product owner, releases Tier 2; the Executive Sponsor, who holds the funding and the mandate, releases Tier 3. Read literally, every release is a breach. | Limit 4.4(a) to validation ("no person validates work that the person built") and state separately who releases, so the release rows in 4.2 and Pol 3.3 stand. |
| C-02 | Blocker | operability | The Tier 1 check "by a person other than the owner" (Pol 3.3; DR-2026-008) and the "peer check" (OM 4.2) cannot be done: AICC has one member (Appointments rows for AICC Lead and AICC Engineer are the same person; RI-007). "Owner" is undefined (Domain Owner or builder?). OM assumes a team (2.1, 4.2 "peers", 4.3, 7.1 "AICC team"; Standards "peer review"). The only fallback is RI-007, a Record, and it names no Role. | Say "a person other than the builder"; add to OM 4.4 that until AICC has a second engineer the check is done by an engineer named in Appointments from the technology function or the Domain; use one term (check) for it. |
| C-03 | Blocker | operability | Pol 3.2 gives Risk Tier assignment at Intake only to the model risk CFC (Use Case Card 4 repeats it); OM 6.3 Intake cannot be left without a Risk Tier. That CFC is not named (Appointments, model risk row; RI-008). RI-008 says "until then take only Risk Tier 1 Use Cases", which still needs the assignment. No Use Case, of any tier, can leave Intake. | Add an interim rule to Pol 3.2 (for example the AICC Lead assigns Tier 1 provisionally, records it, and nothing above Tier 1 proceeds) and correct RI-008. |
| C-04 | Blocker | contradiction | "Release" is not a Stage. OM 6.3 lets a Pilot ("a narrow trial in real work") start before any validation; validation comes at Pilot exit. Charter 5.3 accepts an agent that acts on systems or funds only with validation and the Sponsor's release decision; Pol 3.3 makes the Sponsor's release follow validation. Actors also differ: OM 5.3 gives the Team the release of Tier 1 and 2, OM 4.2 gives Tier 2 to the Domain Owner, OM 6.3 Scale gives Tier 1 and 2 to the Domain Owner, Pol 3.3 gives Tier 1 to the AICC Engineer. OM 5.3 sends Tier 3 to "after asking the AI Steering Committee"; Pol 3.3 and OM 4.2 do not. | Define Release as the exit from Pilot to Scale; require validation before a Tier 2 or 3 Pilot uses real data or customers; make OM 4.2, 5.3, 6.3 and Pol 3.3 name the same releaser for each tier. |

### 2.2 Major

| Id | Sev | Category | Evidence | Fix |
| --- | --- | --- | --- | --- |
| C-05 | Major | gap | Board reporting is not operable. Charter 7.2 says the Sponsor reports to the Board Committee "at regular intervals"; SOI 12.2 says AICC does; the only report Template (Quarterly Report) is for the AI Steering Committee; no owner, content or cadence for the Board report. The Board Committee is "technology or risk" (SOI 7.6, Voc), so there is no addressee. | Name the committee (or the rule to choose it), the interval, and who prepares the report; reuse the Quarterly Report. |
| C-06 | Major | style | Q3 fails in all six documents (counts in section 1). OM is the main case: a binding document with one "shall". | Convert each obligation to "shall" (OM and Cat first) or restate Voc 3.1 so present tense with a named Role counts as an obligation. |
| C-07 | Major | contradiction | SOI 7.3 says internal audit validates AI use and may stop it; Voc lists internal audit as a Control Function and a CFC "validates and may stop"; Appointments has an internal audit CFC row. SOI 12.4 and Charter 7.2 make internal audit the independent assurance provider. The third line cannot validate and then audit. | Remove internal audit from SOI 7.3, from the Voc Control Function definition and from Appointments CFC rows; keep it as assurance. |
| C-08 | Major | contradiction | SOI 4.1 "three values: integrity, prudence, and respect for people"; OM 3.2 "The AICC Values are alignment, openness, respect for people, and relentless improvement". OM 3.2 also says AICC applies "the Values" of SOI; "Values" is undefined. | Delete the second list in OM 3.2, or drop the word "Values" and keep it as a principle of work. |
| C-09 | Major | gap | Pol 3.1 says the tier is the highest that any attribute indicates, listing eight attributes; the table gives thresholds only for data class, influence, customer reach and autonomy. Scale, provider, reversibility and regulatory regime indicate no tier. The Use Case Card (3) asks only for data and customer effect, so the assigner lacks inputs. Pol 3.2 "category that the law treats as high risk" has no list (wiki item 10). | Give each attribute a threshold or delete the ones that have none; add the attributes to the Card. |
| C-10 | Major | gap | "Approved" has no owner: Pol 2.1 (tools "approved for the data class"), Charter 7.1 and SOI 11.3 ("approved assistant") rely on it. No Role approves, and the AI Registry has no approval field. With the Registry empty, all current AI use breaches Pol 2.1 on activation; no transition rule. | Say who approves a tool and add the field; add a transition clause (known uses are listed within a stated period and are tolerated until then). |
| C-11 | Major | gap | Stage exits against Pol and Templates: (a) Tier 1 check (Pol 3.3, DR-2026-008) is in no exit; (b) the provider check (Pol 4.1) is in no Stage and has no form (Control Sign-Off covers Pol 3.3 rows only); (c) Pol 3.4 "returns to Discovery" is not in OM 6.3; (d) no Role confirms that an exit condition is met at Intake, Discovery, Pilot; (e) Initiatives pass the same Stages but Intake demands a Use Case Card and an AI Registry entry, which an Initiative has not; (f) Control Sign-Off result "validated with conditions" is not said to satisfy Pilot exit; (g) Operate "To leave" lists a recurring duty, not an exit. | Add to 6.3: Tier 1 check, provider check, who confirms each exit, exit rule for Initiatives, treatment of conditions; move reassessment out of "To leave". |
| C-12 | Major | operability | Cat 7.1 needs a check "by a person other than the author" before activation, and each quarter; Cat 4.2 applies it to every change. No Role names the checker (Q6), no such person exists in AICC (RI-006, RI-007). Sixty answers per quarter by a volunteer outside AICC will not happen. | Name the Role that appoints the checker (for example the Sponsor names one from risk or technology); check on revisions that change meaning (x.0), annually for the corpus. |
| C-13 | Major | operability | Duties that need CFCs or heads who are not named (RI-008): Pol 4.1 provider check; Pol 5.3 and 5.4 incident escalation and regulator notice; Charter 3.3 Group Arrangement; OM 7.3 time-critical Decision; SOI Level 1 Measure (CFCs appointed). The corpus gives one fallback (RI-008: only Tier 1), which is wrong (C-03), and none for providers, incidents or Group Arrangements. | Add in Pol and Charter: until a CFC is named, the Sponsor names who acts, in the Appointments Record; no provider, Group Arrangement or Tier 2 and 3 Use Case proceeds without the CFC. |
| C-14 | Major | gap | Obligations without one Role (Q6): SOI 2.2(b), 10.1 (training by role before use; "AICC shall maintain training, templates, and Communities of Practice"), 10.2, 10.3, 10.5, 10.6, 12.1, 13.3 (annual review), 13.4 (communicate to all employees, make available to regulators, investors, customers). Training and a Community of Practice for the Group are beyond a team of one and appear in no Record; Charter 6.1(e) offers only coaching of Domain Experts. | Assign each to a Role (for example the AICC Lead for 13.3), cut 10.1 to what AICC can do, and drop "Communities of Practice" until staffed. |
| C-15 | Major | gap | Pol 3.3 rows with no performer or evidence: human oversight, testing for bias and error, monitoring and logging, disclosure and contestability, reassessment (5 of 8 rows). Standards PLT-002, PLT-003 depend on a Platform Owner who is not named. | Add a "Who" to each row (Engineer, Domain Owner, Platform Owner) and the Record where it is noted. |

### 2.3 Minor

| Id | Sev | Category | Evidence | Fix |
| --- | --- | --- | --- | --- |
| C-16 | Minor | contradiction | Exception decider: Voc and SOI 6.7 "the Control Function concerned"; OM 4.2 and Pol 6.1 add the AICC Lead for AICC-only requirements. Voc prevails on terms (2.1). Nobody decides an Exception to a non-control rule that AICC did not set. | Align the Voc definition to Pol 6.1 and say who decides the remainder. |
| C-17 | Minor | contradiction | Pol 3.2 only the model risk CFC assigns the tier; OM 4.2 (CFC "assigns or raises") and OM 8.1(d) ("Control Function Contacts assign") and Charter 6.1(c) imply any CFC. | Use the Pol 3.2 rule in OM 4.2 and 8.1(d). |
| C-18 | Minor | contradiction | SOI 4.2 "compliance with law and policy without exception" and 13.1; Charter 5.2 "low appetite for ... breach of law or regulation" (implies some tolerance). | Charter 5.2: no appetite for breach of law. |
| C-19 | Minor | gap | Cadence. Charter 7.2 and SOI 12.2 report quarterly to the AI Steering Committee; the Quarterly Review (OM 7.1) does not include it; Steering is monthly; which meeting receives the report is unsaid. "Quarterly risk check" (OM 6.4, Pol 3.3) is not one of the "three meetings" and is undefined; the quarterly corpus check (Cat 7.1) is a fourth event. | Say the Quarterly Report goes to the next Steering; define the quarterly risk check as part of the Quarterly Review. |
| C-20 | Minor | gap | OM 5.3 "goes to the next level" but 4.2 sends Tier 3 and activation of binding documents straight to the Sponsor; 5.7 conflict of interest "does not decide" has no substitute, and the AICC Lead holds all Team and Lead decisions. | Say "to the level named in 4.2"; name who decides when the Lead is conflicted (the Sponsor). |
| C-21 | Minor | gap | Pol 5.4 "suspend a Solution" (AICC Lead or any CFC); OM 4.2 and 5.4 "stop a Use Case", "Nobody overrides it". Nobody is said to lift a suspension or stop. | One term; state who lifts it. |
| C-22 | Minor | gap | Templates carry ids AICC-TPL-01 to 05, but Cat 2.2 has no TPL category and Cat 5.1 and 6.1 do not list the ids; Templates have status and revision but no change log (Cat 3.1). Control Sign-Off binds CFCs, yet OM 4.2 and DR-2026-001 give Templates to the AICC Lead (Cat 4.1 would give the Sponsor). Template metadata blocks are not said to be dropped when copied. | Add TPL to 2.2, list ids in 6.1, state that Templates need no change log and no block in copies, and decide the activator for Control Sign-Off. |
| C-23 | Minor | gap | Voc 2.1 precedence lists SOI, Charter, OM, Pol; Cat, Templates and Records have no place, so Q4 is undefined for Voc and Cat and a Cat versus OM 4.2 clash has no rule. | Add Cat after Pol; say Templates and Records yield to documents. |
| C-24 | Minor | ghost reference | wiki/operating-model-open-items.md: item 3 "AI solution engineers" (Not used), 5 "replenishment and delivery review" and "stage policies", 6 "initiative briefs", 8 "the register", 11 "AI use policy", 14 "positioning section", 19 "Artifact Standards"; item 18 says High incident report "within one hour" while Pol 5.3 says "at once"; items 13 and 15 are decided (Charter 5; Cat 4.1). wiki/research/operating-model/responsible-ai/README.md table of mechanisms (enablement group, RACI rows, policy stubs, AI use policy) has no "first corpus" banner unlike the other lineage pages. priorities-basis.md "metrics document". wiki/README "Forums" in the scaffolding-basis description is acceptable (banner present). | Rewrite or delete the stale rows; add the banner to responsible-ai/README.md. |
| C-25 | Minor | ghost reference | portal/content/statement-of-intent.json line 5 has source "wiki/statement-of-intent.md", which moved to charter/statement-of-intent.md; the published page is still v0.1 (RI-004, UC-006). | Fix the source path and revision when UC-006 republishes. |
| C-26 | Minor | style | "Not used" terms present: Pol 2.1 "AI tools" (also shows no term for a general assistant; Solution needs a Use Case); Charter 4.1 "projects"; SOI 11.2.1 "Checks at gates"; Appointments "head of AICC" (twice). Voc "approval" as Not used clashes with legitimate uses (Charter 4.2, SOI 10.4, Priorities, Initiative Brief status). | Replace the terms; narrow the "approval" entry to documents. |
| C-27 | Minor | gap | Used but undefined: Portfolio (Charter 6.1, SOI, Voc), Holder (OM 4.2, 4.6), Milestone (OM 9.2), Team as a Decision level (OM 5.3), Board (SOI, OM), Platform Guardrails (SOI 11), Communities of Practice, corpus and activator (Cat), quarterly risk check, first line (OM 2.3; "second line" is Not used), "owner" (Pol 3.3). Defined but barely used: Hat (only lowercase "hat", OM 4.3), Work Item (once), Activation (heading only). | Define the needed ones in Voc; drop Hat and Work Item or use them. |
| C-28 | Minor | style | Lineage and references in defining documents: change logs name removed documents (OM 2.0, Charter 0.2, Cat 1.0, Pol 0.1, Voc 1.0) and SOI cites archived finding ids; file or folder references (OM 5.6, 9.1; Cat 6.1; Voc 3.4). Early rows missing: SOI 0.1 to 0.4, OM 0.1 to 0.7, Voc 0.1. | Say "see DR-2026-009" in change logs; drop folder words; ignore pre-0.5 history. |
| C-29 | Minor | style | Every change log table lacks an introducing clause (Voc 3.7, Cat Q8) and the section is unnumbered. | Exempt change logs in Voc 3.7. |
| C-30 | Minor | gap | Records against documents and Templates: AI Registry has no "scope" column (OM 9.2, Voc, SOI 11.2) and PLT-001 says the Platform holds it while ai-registry.md says the file is the Registry; Backlog has four scores while OM 6.1 names three; Initiative Brief status list lacks "returned" (section 4); UC-001 to UC-006 are not AI Use Cases, have Risk Tier "n/a", no Registry entry, no Measures, sit in Stage "Operate" with Status "Done", and name the AICC Lead as Domain Owner and Domain Expert (none defined for AICC; Appointments has no row); Initiative Brief has one Domain Owner though an Initiative crosses Domains. | Add a line to OM 6.2 for enabling work with no Risk Tier; align the columns. |
| C-31 | Minor | gap | Severity Major or Minor is used for Issue and Risk rows (RI-001 to RI-008) though Voc and the Record define it for Incidents and Findings only; Cat 7.2 counts only Findings, so it is unclear whether the seven Major items block. | Say Severity applies to all types, or convert to Findings. |
| C-32 | Minor | gap | Authority: the heads of function who name Domain Owners, the Platform Owner and sit in the AI Steering Committee (OM 4.5, 4.6) are in no Appointments table; the Sponsor's own mandate has no source ("Appointed by" blank) and he activates the documents that grant it; SOI 7.7 "activated at the appropriate level"; the Bank's CEO approves a Group appetite (Charter 5.4) and a policy for Participating Entities (Pol 1.1). | Add a table of heads to Appointments; state who confers the mandate; name the level in SOI 7.7. |
| C-33 | Minor | duplication | Said in several places: Tier 3 release by the Sponsor (OM 4.2, 5.3, 6.3; Pol 3.3; Charter 5.3; Standards ARC-002); Exception rule (SOI 6.7, Pol 6.1, Voc, OM 4.2); AICC owns no AI Platform (SOI 7.4, 10.3; OM 2.2; Charter 3.2); independence and no self-validation (SOI 7.3, OM 2.3, 4.4, 5.4, Charter 3.2); quarterly report (SOI 12.2, Charter 7.2, OM 7.1, Voc, Template); funding (SOI 10.4, Charter 4, OM 4.2, 7.2); who activates (OM 4.2, Cat 4.1, while Cat 1.1 says the Catalog is "the only place"); data stays in the Entity (SOI 6.4, 7.2, Charter 3.3, PLT-004). | Keep each rule in one document and refer by title. |
| C-34 | Minor | duplication | Standards ARC-001 to ARC-004 restate Pol 3.3 (Human oversight, Disclosure, Monitoring rows) nearly word for word. | Delete ARC-001 to ARC-004 or make them technical. |
| C-35 | Minor | duplication | SOI 1.1 redefines Bank, Group, Entity, Participating Entity, Domain, AICC (also in Voc, against Voc 3.5); Cat 5.1 repeats Status and Revision of each file, so any revision of any document forces a Catalog revision; the ten questions restate Voc 3.x. | Drop SOI 1.1 definitions; drop Status and Revision columns from Cat 5.1. |
| C-36 | Minor | bureaucracy | OM 8.1 is a seven-step written procedure that repeats 4.2 and 6.3 (DR-2026-009 item 3 says no written procedures). A Decision may be written in up to four places: Notes, Decision Log, decision note, work item (plus change log Decision column) (OM 5.6, Notes Template, 7.1). Notes Template Actions repeat "work items" (OM 7.1). | Delete 8.1 or cut it to two lines; Notes only when a Decision or action exists. |
| C-37 | Minor | bureaucracy | Cat 7.1 and 4.2: ten questions by an outsider on every change and each quarter; Voc has 55 terms and about 75 "Not used" words that Q2 asks a person to check by hand (scriptable); Voc 3.8 diagram rule with no diagram; Cat language columns RU and KY are empty. | See C-12; script Q2 and Q8; drop 3.8 and the empty columns until needed. |
| C-38 | Minor | bureaucracy | For a team of one: Limits on Work in Progress per Stage and per Domain, a visible board and a four-score ranking (OM 6.1); a monthly Steering with the chief executive (OM 7.1, rev 2.1); 12 Records and 5 Templates; SOI 11.2 and 11.3 (platform capability and Measures for five levels) sit in a Group statement, so every edit needs the Sponsor's activation. | Steering quarterly until a Tier 2 Use Case exists; move 11.2 and 11.3 detail for Levels 3 to 5 to Priorities when needed. |
| C-39 | Minor | style | British spelling (behaviour, summarise, organisation, programme, judgement, personalis-) in 16 wiki research files against the wiki README "American spelling"; none in charter/ or portfolio/. | Run a spelling pass on the wiki pages that remain. |
| C-40 | Minor | gap | Identifier schemes are defined nowhere: DR-, RI-, MS-, ARC-, PLT-, PRI- (Templates use INI-[nnn], UC-[nnn], PRI-n). | State them in portfolio/README.md. |
| C-41 | Minor | gap | Cat 4.2 "a small correction needs no more than a change log row": unclear whether a binding document then needs the Sponsor; "small" is undefined. | Say the keeper may correct without activation when the meaning is unchanged (revision 0.1 step). |

## 3. Operability: one person (AICC Lead holding AICC Engineer) plus the Executive Sponsor, today

Yes = doable; No = blocked; Part = doable in part. "Corpus says" is what the documents and Records say to do.

| Obligation | Today | Why, and what the corpus says |
| --- | --- | --- |
| Pol 2.1 use only approved tools | No | Registry empty, nobody approves (C-10). Nothing said. |
| Pol 2.2 data class rules | Part | Bank rules not checked (RI-003). Says to compare. |
| Pol 2.3 accountable person, review of output | Yes | Card names the person. |
| Pol 3.2 model risk CFC assigns tier | No | No such Contact (C-03). RI-008 fallback is wrong. |
| Pol 3.3 Tier 1 check by another person; release by AICC Engineer | No | One person (C-01, C-02). RI-007: name a peer outside AICC; no Role, no rule in a binding document. |
| Pol 3.3 Tier 2 and 3 validation, bias testing, logs | No | No CFCs, no Platform Owner (C-13, C-15). RI-008: take only Tier 1 (insufficient). |
| Pol 3.3 Tier 3 release | No | Sponsor can act only after validation, which is impossible. |
| Pol 4.1 provider check | No | Three CFCs unnamed (C-13). Nothing said. |
| Pol 5.3 to 5.5 incidents | Part | Lead can contain and review; High incident reports to CFCs and regulator notice need named Contacts. |
| Pol 6.1 Exceptions | Part | Lead decides AICC-only ones; CFC ones blocked. |
| OM 4.4(a) separation | No | Same person builds, checks, releases (C-01, C-02). |
| OM 4.4(c) Lead does not validate CFC-remit work | Yes | Follows from having no CFC work. |
| OM 4.6 Holders named | Part | Three rows filled; Domain, Platform Owner, CFC rows empty (MS-002). |
| OM 5.6 Decision Log, notes | Yes | Done for DR-2026-001 to 009. |
| OM 5.7 conflict of interest | Part | No substitute for the Lead (C-20). |
| OM 6.3 Intake exit | No | Risk Tier (C-03). |
| OM 6.3 Discovery exit | Part | Domain Owner and Domain Expert not named (Appointments). |
| OM 6.3 Pilot exit | No | Tier 2 and 3 validation; Tier 1 check not in the exit (C-11). |
| OM 6.3 Scale exit | Part | Domain Owner decides; Tier 3 blocked. |
| OM 6.3 Operate and Retire | Yes | Reassess by date; close entry. |
| OM 7.1 Sync and Demo every two weeks | Part | A demo to Domain Owners and Experts who do not exist yet. |
| OM 7.1 Quarterly Review with CFCs | No | No CFCs. |
| OM 7.1 Steering monthly with the AI Steering Committee | Part | Sponsor plus Lead only (RI-008). |
| OM 7.3 time-critical Decision after asking the heads of risk and compliance | No | Heads unnamed. |
| OM 9 Records | Yes | Files exist; Registry, Appointments, Standards partly empty. |
| Charter 3.3 Group Arrangement | No | Three CFCs unnamed. |
| Charter 4 Envelopes and Guardrails | Part | "not yet set" (Priorities); first Steering sets them. |
| Charter 5.4 approve appetite | Yes | The Sponsor, once confirmed (RI-001, RI-002). |
| Charter 7.2 Quarterly Report | Yes | Lead can write it; Board report undefined (C-05). |
| SOI 10.1, 13.3, 13.4 | No | No Role, beyond the team (C-14); publication blocked by RI-005. |
| Cat 4.1 activation | Part | Lead activates Voc and Cat; Sponsor unconfirmed for the other four (RI-001). |
| Cat 7.1 independent check | No | No person outside AICC is named (C-12). UC-005 is the current route. |

Stage exit conditions (OM 6.3) against Pol and Templates:

| Stage | Exit | Match with Pol and Templates | Doable today |
| --- | --- | --- | --- |
| Intake | Card; Risk Tier; Registry entry | Matches Pol 3.3 row 1 and Card 4; Initiatives cannot meet it (C-11) | No |
| Discovery | Measures; Domain Owner and Expert named; effect on persons for Tier 2 and 3 | Card 2 and 3 match; Tier 1 check absent | Part |
| Pilot | Results; validation Tier 2 and 3; Pol met for Tier 3 | Control Sign-Off matches; validation may come after real-work start (C-04) | No for Tier 2 and 3 |
| Scale | Domain Owner; Sponsor for Tier 3 | Pol 3.3 names the AICC Engineer for Tier 1 (C-04) | Part |
| Operate | Reassess on change and by date | Pol 3.3 intervals (year, six months) match; Registry "Reassess by" matches | Yes |
| Retire | Registry entry closed | No Template or Record rule | Yes |

## 4. Mechanical checks

| Check | Result |
| --- | --- |
| Clause numbering (script, six documents) | No gaps or repeats. Clauses: SOI 52, OM 31, Pol 19, Charter 15, Cat 14, Voc 11; all within 150. The change log is an unnumbered section in each. |
| Catalog 5.1 against file metadata | 6 of 6 match on id, title, status, revision. |
| Templates and Records against real files | Five Templates and twelve Records match by name. Not in OM 9.2: the decisions/ folder (in 5.6) and assessments/ (in portfolio/README). Template ids are not in the Catalog (C-22). |
| Links that do not resolve (charter/, portfolio/, wiki/ without archive/ and assessments/) | 0. Charter documents hold no links (Voc 3.5). |
| Tables without an introducing clause | Six change log tables (C-29). All other tables in charter/ have one; OM 7.1 introduces its table indirectly. |
| American spelling | charter/ and portfolio/: no British form found. wiki/: 16 research files (C-39). |
| "shall" | SOI 17, Pol 4, Charter 1, OM 1, Cat 0, Voc 0 (C-06). |
| Ghost names (Forum, Register, Decision Record Template, Delivery Program, Lead Architect, Portfolio Manager, Design Review, Risk Tier Policy, Tier 4, Readiness Level) | charter/ and portfolio/: only in change logs and in superseded Decision Log rows (accepted as history). wiki/: open items, responsible-ai/README, priorities-basis; "Lead Architect", "Portfolio Manager", "delivery program" remain only in agile-mapping.md, which carries the archive banner. |
| Risk Tiers | Three everywhere in charter/, Records, Standards, Templates, Backlog, AI Registry. "Tier 4" occurs once, in the superseded DR-2026-002 row. Names Low, Medium, High match Voc. One wording clash: Pol 3.2 "law treats as high risk" gives at least Tier 2, while Tier 3 is named "High". |
| Roles | Seven Roles agree in OM 4.1, 4.2, Voc, Appointments, DR-2026-009. SOI and Charter name only some; none name an eighth. Appointments lists six Control Functions (C-07 on internal audit). |

## 5. Verdict

Not ready to activate. Activation is also blocked by an external condition: the Executive Sponsor has not confirmed the appointment (RI-001).

Counts: 4 Blocker, 11 Major, 26 Minor (41 findings). By category (the first category of each finding): contradiction 7, gap 17, operability 4, duplication 3, bureaucracy 3, ghost reference 2, style 5.

Top five fixes:

1. Rewrite OM 4.4(a) and define the Tier 1 check as "a person other than the builder", with a stated interim checker until AICC has two engineers (C-01, C-02).
2. Add an interim rule for unnamed CFCs: who assigns the Risk Tier, and what may proceed; correct RI-008 (C-03, C-13).
3. Define Release, require validation before a Tier 2 or 3 Pilot uses real data, and align OM 4.2, 5.3, 6.3, Pol 3.3 and Charter 5.3 on who releases (C-04, C-11).
4. Put "shall" and one performing Role on every obligation, starting with OM, Cat, Pol 3.3 and SOI 10 to 13 (C-06, C-14, C-15).
5. Remove the contradictions of internal audit, the two sets of values and the Board reporting line (C-07, C-08, C-05).
