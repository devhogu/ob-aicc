# Coverage report: first corpus and Statement of Intent against the simplified corpus

Independent analysis, 2026-09-30. No existing file was edited.

Sources read: the six documents and five Templates in `charter/`; the Records in `portfolio/`; DR-2026-009; the archived first corpus in `wiki/archive/charter-v1/` (20 documents, 5 policies, 23 Templates) and the first Records in `wiki/archive/records-v1/`; and every "shall" and commitment in sections 5 to 13 of the Statement of Intent (SoI).

Reading notes. (a) Four of the five v1 policies, and the v1 Charter, Funding Model, Metrics, Evolution Plan and Enablement Plan, were stubs holding an intent only. Where the archive had no provisions, the test is whether the intent is carried now. (b) Status COVERED means a clause or Record row exists that a person can follow; a carrier that only names the topic is marked GAP. (c) Abbreviations: OM Operating Model, AIP AI Policy, Cat Document Catalog, QR Quarterly Report template, R&I Risks and Issues Record, UCC Use Case Card, CFC Control Function Contact, CF Control Function, IA internal audit, ES Executive Sponsor.

## 1. Coverage matrix

### 1.1 Commitments of the Statement of Intent (sections 5 to 13)

| Aspect | Where it was | Status | Where it is now, or why acceptable | Severity |
| --- | --- | --- | --- | --- |
| Adopt where value is measured; discontinue where none (5.1) | SoI 5.1; v1 PM 4.1 Retire | GAP | OM 3.1(e) and Quarterly Review score value, but no Role decides retirement of a Use Case or Initiative and no trigger is stated (v1: Domain Owner, AI Steering Committee) | Minor (G17) |
| Pilot, measure, extend only on evidence (5.2) | SoI 5.2; OM v1 3.3(d) | COVERED | OM 3.1(d), 6.3 (Pilot and Scale exit) | - |
| AI answers from approved, current, cited sources (5.3) | SoI 5.3; none in v1 | GAP | No clause, Standards row or Registry field | Major (G8) |
| Reuse of shared components over one-off Solutions (5.4) | SoI 5.4; OM v1 9.4 | COVERED | Charter 6.1(d); OM 4.2 (AICC Lead sets standards); Standards Record | - |
| Domain specialists shape adoption (5.5) | Roles 4.2 | COVERED | OM 4.2, 4.6, 8.1(b); Appointments | - |
| Employees trained before use (5.5, 10.1, 4.2) | AI Use stub; Enablement Plan stub | GAP | Only the Domain Expert is trained (OM 6.3 Pilot, 8.1(f)); AIP 2.1 sets no training condition; ML2 measure "trained in its use" has no carrier | Major (G6) |
| Federation: Group minimum, Entity applies within own regulation (5.6, 7.2) | OM v1 4.2; Roles 1.4 | COVERED | OM 1.2, 2.3; Charter 3.2, 3.3; AIP 1.1; OM 4.6 (CFC per Entity) | - |
| Accountability of a named individual; AI holds none; bought AI same as built (2.3, 6.1) | Roles; RTP 1.2 | COVERED | AIP 2.3, 4.2; UCC (Domain Owner); OM 4.2 | - |
| Board oversees through regular reporting (6.1, 7.6, 12.2) | Reporting 2.1, 4.2; Roles 2.3 | GAP | Charter 7.2 says ES "reports at regular intervals"; no preparer, content, interval, approval or trigger (see 1.2) | Major (G1) |
| Fairness: bias tested before release and monitored (6.2) | RTP 4.1; DR-007 | COVERED | AIP 3.3 row "Testing for bias and error"; Control Sign-Off section 1 | - |
| Disclosure to individuals (6.3) | RTP 4.1 | COVERED | AIP 2.4, 3.3; ARC-003 | - |
| Outputs explainable to customers, regulators, auditors (6.3) | v1 Impact Assessment row only | GAP | No requirement or Tier row; the Impact Assessment row that named it was dropped | Minor (G22) |
| Data minimization; retained within Entity and classification (6.4) | none; Charter stub | GAP | Entity and class rules are in AIP 2.2, Charter 3.3, PLT-004; "only the data it requires" is nowhere | Minor (G22) |
| AI tested, monitored, protected against AI-specific attacks (6.5) | Roles 5.2.1 (infosec remit) | GAP | Testing and monitoring: AIP 3.3. Attacks: only in the incident definition (5.1); no security test in the Tier table and no infosec remit | Minor (G22) |
| Fallback and exit for critical services and providers (6.5, 10.5) | Third-Party stub | COVERED | AIP 4.1 | - |
| Humans can stop or override; customer reaches a person and contests (6.6) | RTP 4.1; ARC rows | COVERED | AIP 3.3 (oversight; disclosure and contestability); ARC-001 to 003 | - |
| No bypass of a control; Exception by the CF, recorded, time-limited (6.7) | DM 8 | COVERED | AIP 2.5, 6.1; R&I Record (type Exception, Review column) | - |
| Data and decisions stay in the Entity unless a Group Arrangement (7.2) | DM 9 | COVERED | Charter 3.3; PLT-004 | - |
| CF independent; validate and may stop; nobody validates own work (7.3) | Roles 5, 8 | COVERED | OM 4.2, 4.4, 5.4; Control Sign-Off; except IA (see row in 1.2) | - |
| AICC is governance framework and program office; Domains execute (7.4) | OM v1 2 | COVERED | OM 2.1, 2.2 | - |
| AI Steering Committee advises on Portfolio and conflicts (7.5) | Roles 2.2 | COVERED | OM 4.5, 7.1 (Steering), 5.2(a) | - |
| Risk appetite statement maintained, activated, assessed against (7.7) | Roles 2.1; DR-003 | COVERED | Charter 5; OM 4.2, 5.4, 7.2; approval is draft (RI-002). Reporting against it: G10 | - |
| Each Use Case has a Risk Tier that sets review, validation, oversight, release speed (7.8) | RTP | COVERED | AIP 3.1 to 3.3; OM 6.3 | - |
| Areas of application (8) | SoI 8 | DROPPED BY DESIGN | Descriptive scope, no commitment; outside the corpus; AIP 1.2 applies to every use | - |
| Investor, lender and Board information: figures traceable, human approval before publication (9.3) | Reporting 4.1, 4.2 | GAP | AIP 2.3 requires a person to review output, but nothing makes a named person approve what reaches investors, lenders or the Board | Major (G1) |
| Knowledge with named owners, review cycles, access control, citation (9.5, 10.2) | none | GAP | As 5.3; PRI-4 and the ML2 measure depend on it | Major (G8) |
| Systems record AI contribution and the decision; no action without human unless the Tier allows (9.6 to 9.8) | RTP 4.1 | COVERED | ARC-001, ARC-004; AIP 3.1, 3.3; Charter 5.3 | - |
| Training, templates and Communities of Practice maintained by AICC (10.1) | Roles 3.5; Forums 5.6; Enablement stub | GAP | Templates: Cat 6. Training: Charter 6.1(e) names Domain Experts only. No Community of Practice anywhere | Major (G6) |
| Data classified; class decides which models and where they run (10.2) | Data Classification stub | COVERED | AIP 2.2, 4.1 (where processed); Bank rules not yet checked (RI-003, open issue, acceptable as tracked) | - |
| Shared AI Platform, data separated by Entity, outside AICC (10.3) | Roles 6.1 | COVERED | OM 2.2, 4.2 (Platform Owner); PLT-001 to 005 | - |
| Funding by Envelope and Guardrail; Brief and ES approval above guardrail (10.4) | Funding stub | COVERED | Charter 4.1, 4.2; Priorities Record; Initiative Brief; values "not yet set" is an open item not logged in R&I | - |
| Providers: due diligence, terms, ongoing monitoring, fallback, exit (10.5) | Third-Party stub | GAP | Due diligence, terms, exit: AIP 4.1. "Ongoing monitoring" and concentration across the Group are not carried | Minor (G12) |
| Portfolio on common cadence; work visible and limited (10.6) | OM v1 12 | COVERED | OM 6.1, 7.1 | - |
| Maturity Level reached when Measures met; own pace per Priority (11.1) | PM 6.4 | COVERED | Priorities Record (level reached, target); QR section 3 | - |
| Platform capability by level (11.2) | Standards Record v1 | COVERED | Standards PLT-001 to 005 cover Levels 1 to 3; rows for gateways and agent limits are added as levels near | - |
| Measures by Maturity Level, baselines, targets, who measures (11.3, 12.1, 2.2(e)) | Metrics stub | GAP | Charter 7.1 says ES sets targets; no Record lists Measures, baselines, owners or sources; Vocabulary says a Measure has an owner but none is named; ML1 "baselines established" has no owner | Major (G7) |
| Audit and regulatory findings on AI as a Measure (11.3 level 4) | Registers 4.5 | GAP | Vocabulary defines Finding as a deviation found by a check of documents only | Minor (G7) |
| Quarterly report to AI Steering Committee (12.2) | Reporting 2.1 | COVERED | Charter 7.2; QR Template | - |
| Benefits against Investment Envelope (12.3) | Reporting 3.1(e); Benefits Register | COVERED | Charter 7.1; QR section 4; Steering review (OM 7.1). Actuals per Use Case: G20 | - |
| Internal audit provides independent assurance (12.4) | Roles 5.2; Registers 4.4 | GAP | One sentence in Charter 7.2; see 1.2 | Major (G2) |
| Satisfy applicable law in each jurisdiction (13.1) | Open item 10 | GAP | Left to CFC validation; no statement that the compliance CFC confirms the applicable law per Entity at Intake, and no list of laws | Minor (G19) |
| Continual improvement (13.2) | OM v1 3.3(g) | COVERED | OM 3.1(g); Quarterly Review "agree improvements" | - |
| Statement reviewed yearly and on material change, provider change, regulation, audit or supervisory finding (13.3) | Forums 4.10; Cat 5.4; Assessment 4.3 | GAP | OM 7.2 reviews the OM and the Appetite Statement only; SoI, Charter and AIP have no annual review and no trigger | Major (G5) |
| Statement communicated to all employees; available to regulators, investors, customers (13.4) | Cat v1 | GAP | Cat 4 activates; nothing communicates or publishes | Minor (G18) |
| Effect on activation, recorded in change log (13.5) | Cat 6 | COVERED | Cat 4.1 | - |

### 1.2 Requirements, controls and Records of the archived corpus

| Aspect | Where it was | Status | Where it is now, or why acceptable | Severity |
| --- | --- | --- | --- | --- |
| Report to the Board Committee: owner, preparer, interval, approved by ES before issue, figures traceable with date | Reporting 2.1, 4.1, 4.2; Roles 2.1.2(g) | GAP | Charter 7.2 only; QR Template is "for the AI Steering Committee", no Board summary | Major (G1) |
| High Severity incident reaches ASC and, by implication, Board | Incident 5.1(f) | GAP | AIP 5.3 sends it to ES; no duty to tell the Board Committee before the next report | Major (G1) |
| Quarterly Report content | Reporting 3.1 | COVERED | QR sections 1 to 6; Decisions taken, Portfolio by Stage, readiness of documents dropped (by design) | - |
| Independent assurance by IA over AICC and Portfolio | Roles 5.2, DR 4.5 | GAP | Charter 7.2 sentence; IA needs only access and no interference, see next two rows | Major (G2) |
| IA independence from delivery; IA not a validator or stopper | Roles 8.5; Forums 4.3 | GAP | Vocabulary makes IA a Control Function, and OM 4.2 lets every CFC "validate" and "stop"; v1 8.5 dropped | Major (G2) |
| IA read access to Records; closed not deleted; retention per Bank rules | Registers 4.2, 4.4; AS 7.1, 7.2 | GAP | OM 9.1 "history of the repository is the audit trail"; no retention, no access, no rule against rewriting history (logs only: ARC-004, PLT-002) | Major (G9) |
| Three lines of defense | OM v1 4.1, 4.3 | COVERED | First line and CF independence: OM 2.3, 4.4(b), 5.4. Third line: see G2. Vocabulary bars "second line", acceptable | - |
| Stop authority of CFs; nobody overrides | Roles 5.1.2(d); DM 6.2 | COVERED | OM 4.2, 5.4; AIP 5.4; PLT-005; Control Sign-Off "stopped" | - |
| Suspend by AICC Lead or any CFC | Incident 5.1(b) | COVERED | AIP 5.4 | - |
| Escalation; objection on control grounds goes to head of CF | DM 6.1, 6.2 | GAP | OM 5.4 says nobody overrides a CF, then sends the disagreement to ES "who may accept a risk"; unclear whether ES can set aside a stop | Minor (G14) |
| Decision accountability, levels, reversible decisions | DR, DM 2 | COVERED | OM 5.1 to 5.3 | - |
| Decision recording with facts, decider, revisit date | DM 3, 10, 11 | COVERED | OM 5.6; Decision Log columns | - |
| Timing limits, proposal workflow, quorum, secretary, written procedure | DM 4, 5; Forums 4 to 6 | DROPPED BY DESIGN | Bureaucracy for a small team; OM 7.3 keeps a between-meeting ES decision after asking risk and compliance | - |
| Dissent noted | Forums 4.5 | COVERED | OM 5.5 | - |
| Conflict of interest | Forums 6.3; Roles 8 | COVERED | OM 5.7, 4.4(a) | - |
| Rules of separation | Roles 8.1 to 8.8 | COVERED | OM 4.4. Internal contradiction: see section 4 | - |
| Delegation, deputy, absence; team of one | DM 7; Forums 6.2; Appointments 4.6 | GAP | No deputy for AICC Lead, ES or any CFC; RI-007 covers only the peer checker; absence of a CFC freezes Tier 2 and 3 and incident suspension | Major (G3) |
| Seven Roles instead of 13; other duties as hats | Roles 3, 9 | DROPPED BY DESIGN | OM 4.3; duties fall to AICC Lead and Engineers; training and Community of Practice duty not carried (G6) | - |
| Remit of each Control Function | Roles 5.2.1 | GAP | "Within the remit" used throughout, remit defined nowhere; only fragments in AIP 3.2, 4.1, 5.4 | Minor (G15) |
| Appointments, appointers, Roles held | Appointments 2, 3 | COVERED | Appointments Record; OM 4.6. "Roles held" column dropped: acceptable | - |
| Functional Direction of engineers line-managed elsewhere | OM v1 10.5, 10.6 | COVERED | OM 8.1(c) | - |
| Platform Owner duties (registry, evidence, separation) | Roles 6.1 | COVERED | OM 4.2; PLT-001 to 005 | - |
| Intake and request of services | SC 3; PM 4 | COVERED | Charter 6.2; OM 6.3. Response times dropped by design | - |
| Service Portfolio and Catalog of reusable Solutions | SC 2, 4 | DROPPED BY DESIGN | Backlog and AI Registry hold the Solutions; revisit when reuse begins (Level 3 to 4) | - |
| Risk Tier assignment by model risk; others raise only | RTP 3; DR 2.3 | COVERED | AIP 3.2; UCC section 4; OM 6.3 | - |
| Risk Tier reassessment on change and by interval | RTP 5; Registers 3.2 | COVERED | AIP 3.3, 3.4; AI Registry "Reassess by"; OM 6.3. No owner duty to trigger it on change (low) | - |
| Three Tiers instead of four | RTP 2 | DROPPED BY DESIGN | Old Tiers 2 and 3 merged into Tier 2; see section 4 on weight | - |
| Impact Assessment of effect on affected persons | RTP 4.1; template | GAP | OM 6.3 Discovery exit says "assessed in the UCC", but UCC section 3 only describes data and effect; no harms, mitigation, residual risk | Minor (G16) |
| Validation by CFCs, by Tier | RTP 4.1; Validation Sign-Off | COVERED | AIP 3.3; Control Sign-Off | - |
| Validity of a validation; revalidation on material change; model or provider change returns to Discovery | PM 4.2; Sign-Off 7 | GAP | AIP 3.4 returns to Discovery only when the Tier rises; a new model version or provider at the same Tier needs no revalidation; Sign-Off has no validity field | Major (G4) |
| Human oversight, disclosure, contestability, logging, monitoring by Tier | RTP 4.1 | COVERED | AIP 3.3; ARC-001 to 004; PLT-002, 003 | - |
| AI Registry with owner, scope, data, Tier, reassessment | Registers 3.2 | COVERED | portfolio/ai-registry.md; OM 6.3, 9.2; model "versions" field dropped (in G4) | - |
| Release record (who released, when) | Scale Decision | GAP | Tier 2 release is a Team decision "noted in the work item" (OM 5.6); no Registry column or Card row | Minor (G4) |
| Approved tools only, by data class and purpose | none (AIP new) | COVERED | AIP 2.1, 2.2 via AI Registry | - |
| Detection of unapproved AI use | none | GAP | ML2 measure compares approved with unapproved use; nobody detects it | Minor (G11) |
| Design Review against Standards | Forums 5.4 | DROPPED BY DESIGN | Standards Record intro (peer review); Control Sign-Off checks ARC rows | - |
| Pilot Report, Scale Decision, Domain Engagement Record, Objectives, Roster, Delivery Review Notes, Benefits Report (Templates) | Templates | DROPPED BY DESIGN | Content moved to UCC, Notes, QR; Domain Expert time share and Objectives confidence dropped | - |
| Limits on work in progress; capacity | PM 3.7 | COVERED | OM 3.1(c), 6.1; QR section 3. Limit values are not yet set | - |
| Ranking by value, urgency, risk reduction, effort (1 to 5) | PM 3.4 to 3.6 | COVERED | OM 6.1; Backlog; UCC section 5 | - |
| Benefits tracking per Use Case and evidence source | Benefits Register and Report | GAP | UCC has target but no actual or evidence; QR shows realized benefit by Priority with no rule on who measures it | Minor (G20) |
| Investment mix guardrail | OM v1 6.2 | DROPPED BY DESIGN | Guardrails not yet set; premature | - |
| Retire: decider, withdraw data and access, notify users | PM 4.1; Retirement Notice | GAP | OM 6.3 says only "AI Registry entry is closed" | Minor (G17) |
| Exceptions: by CF within remit; AICC Lead for AICC rules; time limit | DM 8 | COVERED | AIP 6.1; OM 4.2; R&I Record. Compensating-controls field dropped: fits the Action column | - |
| AI Incident definition, Severity, report, contain, assess, review in 10 days, no blame | Incident 2 to 5 | COVERED | AIP 5.1 to 5.5 | - |
| One-hour deadline for High incident | Incident 5.1(a) | DROPPED BY DESIGN | "At once"; the law sets external deadlines and compliance decides (wiki open item 18) | - |
| Regulator and customer notification | Incident 4.3 | COVERED | AIP 5.4 | - |
| Provider notification; Platform Owner in report chain; Domain Owner accountable for incident | Incident 4.2, 5.1(d) | GAP | Dropped with the policy; Platform Owner can suspend (PLT-005) yet is not told | Minor (G21) |
| Incident Register and Report | Incident 6; Registers 3.4 | COVERED | R&I Record (type Incident); report form dropped by design | - |
| Third-party due diligence and exit | TP stub | COVERED | AIP 4.1, 4.2 | - |
| Ongoing provider monitoring, concentration | TP stub | GAP | See G12 | Minor (G12) |
| Data classification; Entity separation | DC stub | COVERED | AIP 2.2; Charter 3.3; PLT-004 | - |
| Group Arrangement content: Entities, data, legal basis, controls, end date, review | DM 9.1 | GAP | Charter 3.3 records it as a Decision Log line; no required content | Minor (G13) |
| Activation by ES for binding documents, AICC Lead otherwise | Cat 6 | COVERED | Cat 4.1 | - |
| Deprecation; replacement takes new identifier | Cat 4.2 | DROPPED BY DESIGN | Cat 3.2 keeps status deprecated | - |
| Translation RU and KY; English is the source; translation names revision | Cat 2.4, 3.2 | GAP | Cat 2.1 keeps the identifier; no source rule, no freshness rule | Minor (G18) |
| Metadata, revision, change log | Cat 3, 5, 7 | COVERED | Cat 3 | - |
| Quarterly check of corpus by a person other than the author | Assessment 2.4, 4.2 | COVERED | Cat 7.1; staffing is RI-007 | - |
| Readiness Levels, 81 checks, IA sampling of assessment | Assessment | DROPPED BY DESIGN | Ten questions; IA assurance covered by G2 | - |
| Yearly review of active documents | Cat 5.4; Forums 4.10 | GAP | See G5 | Major (G5) |
| Identifiers, folder structure, work tracker mapping | Artifact Standards | DROPPED BY DESIGN | Portfolio README; Cat 2 | - |
| Minutes, agendas, quorum records of 6 forums | Forums 6.6 | DROPPED BY DESIGN | Notes Template keeps Decisions and actions | - |
| Recording a meeting only with consent of all | Forums 6.9 | GAP | Dropped; AI transcription of meetings is itself an AI use | Minor (G23) |
| Stand-up, Replenishment, Delivery Review, Quarterly Planning | Forums 5 | COVERED | OM 7.1 (Sync and Demo, Quarterly Review); stand-up dropped by design | - |
| Appetite Statement reported and used | Roles 2.1; Forums 4.10 | GAP | Approved by ES and reviewed yearly (Charter 5.4); never reported against, Board Committee not told | Minor (G10) |
| Applicable laws per Entity | Open item 10 | GAP | See G19 | Minor (G19) |
| Evolution Plan (separate combined Roles, sunset) | Evolution stub | DROPPED BY DESIGN | DR-009 revisit 2026-12-31; RI-007 | - |
| Funding Model, Service response times, Metrics intervals | stubs | DROPPED BY DESIGN | Charter 4, 6.2, 7.1 | - |

## 2. Gaps, ranked, with the smallest restoration

The gap IDs are used in the matrix. Each fix is one sentence or one table row in an existing document.

### Major

| Rank | ID | Gap | Minimal restoration |
| --- | --- | --- | --- |
| 1 | G1 | Board and investor reporting has no owner, content, interval or approval; a High incident is not passed to the Board; information to investors, lenders or the Board needs no named approver | Charter 7.2: add "The AICC Lead prepares the report to the Board Committee from the Quarterly Report; the ES approves it before it is issued; each figure traces to a Record or governed source with its date; the ES tells the Board Committee of a High Severity AI Incident and of any risk accepted beyond the AI Risk Appetite Statement without waiting for the next report." AIP 2.3: add "AI output published to investors, lenders, regulators or the Board is approved by a named person." QR Template: add one line "Summary for the Board Committee" |
| 2 | G2 | Internal audit is a "Control Function Contact" who may validate and stop, which destroys third-line independence; assurance has no access or scope | OM 4.4: add "(d) The Control Function Contact of internal audit gives assurance only: it does not validate, release or stop, and has read access to every Record." Vocabulary: say IA is the third line, and Control Function in OM 4.2 excludes IA |
| 3 | G3 | No deputy, delegation or continuity in a team of one | Appointments Record: add a column "Deputy" to every table (the CF deputy comes from the same CF). OM 4.6: add "Each Holder names a deputy; the deputy acts during absence and the Decision Log notes a delegation for more than two weeks" |
| 4 | G4 | A change of model, version, provider or data at an unchanged Tier is not revalidated; validation has no validity date; Tier 2 release is not recorded | AIP 3.4: replace "raises the Risk Tier" with "changes the model, its version, the provider, the data or the scope, or raises the Risk Tier". Control Sign-Off: add row "Valid until / revalidate on". AI Registry: add columns "Model versions" and "Released by, date" |
| 5 | G7 | Measures of the Maturity Levels have no baseline, target, owner or source Record; audit and regulatory findings are not recorded | Priorities Record: add a table "Measure, Level, Baseline, Target, Owner, Source" seeded from SoI 11.3 (Owner and Source are required). Vocabulary: Finding includes "a deviation found by an audit or a supervisor" |
| 6 | G5 | SoI, Charter and AI Policy are not reviewed yearly and on triggers | OM 7.2: change to "reviews the Statement of Intent, the Charter, the AI Policy, this Operating Model and the AI Risk Appetite Statement; the ES calls an extra review on a material change in the use of AI, a principal provider or regulation, or an audit or supervisory finding" |
| 7 | G6 | No training of employees before use; no Community of Practice | AIP 2.1: add "An employee completes the training that AICC sets for a tool before first use; the AI Registry row states the training." Charter 6.1(e): "Training of employees and coaching of Domain Experts, and a Community of Practice held within the Sync and Demo" |
| 8 | G8 | Knowledge sources have no owners, review cycle or citation rule | Standards: add ARC-005 "A Solution that answers from knowledge cites the source, and each source has a named owner and a review date recorded in the AI Registry"; AI Registry: add column "Knowledge sources, owner, review date" |
| 9 | G9 | Record retention, integrity and audit access | OM 9.1: add "A Record is closed and not deleted, is kept for the period that the record retention rules of the Bank require, the history of the repository is not rewritten, and internal audit has read access" |

### Minor

| Rank | ID | Gap | Minimal restoration |
| --- | --- | --- | --- |
| 10 | G10 | Risk appetite not reported against | QR section 5: add "Position against the AI Risk Appetite Statement and risks accepted beyond it" |
| 11 | G14 | OM 5.4 contradicts itself on a CF stop | OM 5.4: "A disagreement with a Control Function goes to the head of that Control Function; the ES may raise it with executive management and does not override it" |
| 12 | G15 | CF remits undefined | Appointments Record, CF table: add a column "Remit" (one line each, from v1 Roles 5.2.1, plus AI-specific security for information security) |
| 13 | G12 | Provider monitoring and concentration | AIP 4.1: add "and reviewed at each reassessment and on a change of terms or model, and the concentration of the Group on one provider is reported in the Quarterly Report" |
| 14 | G11 | Unapproved AI use not detected | Standards: PLT-006 "The AI Platform or information security reports use of AI services that are not in the AI Registry" |
| 15 | G16 | Impact assessment has no content | UCC section 3: add "For Risk Tier 2 and 3: the harms to affected persons, the mitigation, and the residual risk" |
| 16 | G17 | Retirement has no decider, data removal or notice | OM 4.2: "Domain Owner decides to retire a Use Case; ES an Initiative"; OM 6.3 Retire exit: "users told; data and access removed; Registry closed" |
| 17 | G13 | Group Arrangement has no required content | Charter 3.3: add "and states the Entities, the data, the legal basis, the controls and the end date" |
| 18 | G19 | Applicable law per Entity not identified | OM 6.3 Intake: "the compliance CFC confirms the applicable law for the Entity"; Standards Record may list it |
| 19 | G20 | Realized benefit per Use Case not recorded | UCC section 2: add columns "Actual" and "Confirmed by Domain Owner, date" |
| 20 | G18 | Communication to employees; translation rule | Cat 4.1: add "the activator announces it to all employees". Cat 2.1: "English is the source; a translation states the revision it translates" |
| 21 | G21 | Incident chain gaps | AIP 5.3: add the Platform Owner to the High report; 5.4: add "providers are told as the contract requires" |
| 22 | G22 | Explainability, data minimization, AI-specific security test missing from the Tier table | AIP 2.2: add "uses only the data that the Use Case requires"; AIP 3.3: add "and explanation of the output" to Disclosure and contestability, and "security testing including attacks on AI" to Validation for Tier 2 and 3 |
| 23 | G23 | Meeting recording consent | AIP 2.2: add "AI that records or transcribes a meeting is used only with the consent of all participants" |

## 3. Dropped, and right to drop

1. Secretaries, quorums, chairs, deputies of chairs, written procedure, and minute deadlines: a team of one needs none; the facts live in the Decision Log.
2. Four Risk Tiers: three are enough; the floor for a law-defined high-risk category is unchanged in relative terms.
3. Readiness Levels, 81 checks and IA sampling of the assessment: replaced by ten questions and an independent person; IA keeps its own audit right.
4. Decision categories, 47 decision rows and the RACI: replaced by three levels plus the facts rule; the Role table names the decider.
5. Seven registers to one Risks and Issues Record: one list serves incidents, exceptions and findings; the Quarterly Report reads it.
6. Design Review: the Control Sign-Off checks the ARC standards; a separate forum adds no control.
7. Service Portfolio, Service Catalog, response times: the Backlog and AI Registry hold the same facts; revisit at reuse.
8. Identifier schemes, tracker mapping, Domain Engagement Record, Roster, Objectives and Pilot Report forms: content survives in the Card, Notes and Quarterly Report.
9. One-hour incident deadline: external deadlines are set by law and decided by compliance.
10. Investment mix guardrail and prohibited-use list: premature; AIP 2.1 is an allowlist, stronger than a denylist.

## 4. Other observations (not coverage)

- OM 4.4(a) says no person releases work that the person built, owns or benefits from, yet OM 4.2 lets the AICC Engineer release Tier 1 and the Domain Owner release Tier 2 and roll out. Fix in 4.4(a): "validates or accepts"; state that the peer check (Tier 1) and validation (Tier 2) are the separation.
- Tier 2 now holds v1 Tiers 2 and 3. Internal use of confidential data needs full CFC validation and bias testing, and RI-008 limits work to Tier 1 until the Contacts are named. This risks shadow AI. Consider a lighter path for Tier 2 uses with a person reviewing output and no customer effect.
- Not in R&I and worth logging: investment Guardrails and Work-in-Progress limits are not set, so no Initiative Brief is required yet.
