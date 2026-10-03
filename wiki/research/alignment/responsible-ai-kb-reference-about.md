# Site-to-corpus alignment: Responsible AI, Knowledge base, Reference, About, legal pages

Working record, 2026-10-03. Gap list between these site pages and the corpus. The corpus is normative; the site explains it. For the 26 regulation pages and 9 resource pages only the title and the relevance line were read.

Key points:
- Mission conflict: the site's Mission is new text; the AICC Charter's mission (Charter 2.1) appears on the site only as "Purpose".
- Portal scope: the courses and knowledge base are what the corpus assigns to the separate operating portal, not to the AICC portal.
- Not in the corpus at all: the list of acts that apply to the Bank, the learning paths, the 14th Template, the run-rate lane, the Lab, the technology vocabulary.
- Framework mappings belong in a Record (Standards), not in a document (Vocabulary 3.4: no provenance in a defining document).
- AI Registry gap: the site says the charter and portal were "developed with AI, as AICC did for itself"; the AI Registry lists no use.

Site tags (under `portal/content/`): RA1–RA7 = responsible-ai parts (understanding-ai-today, opportunities, ai-in-fintech-and-digital-banking, risks-and-challenges, what-responsible-ai-means, how-the-bank-applies-it, ai-terms-explained); KBov/KBlp/KBtf/KBpb/KBac/KBqa/KBpd = knowledge-base pages; REFov/REFsf/REFra/REFlo = reference pages; REG/* regulations; WWD what-we-do; HWW how-we-work; PRIV privacy; TOU terms-of-use; AJ.x = authored.json object.
Corpus tags: SoI, CH (AICC Charter), AIP (AI Policy), OM, VOC, DC (Document Catalog), CT (collaboration tooling), ARW (ai-risk-control), TPL (templates README), ES (executive summary), STD (standards record), AIR (ai-registry), RIR (risks-and-issues), BM, SLM.

## 1. New on the site, absent from the corpus

Statement of Intent
- N01 Jurisdiction and supervisor never named (REFra; REG/nbkr). SoI 1.5: "The Bank is licensed and supervised in the Kyrgyz Republic by the National Bank of the Kyrgyz Republic."
- N02 Pillars mapped to Strategic Priorities (AJ.strategy_page.pillars_carried). SoI 3.3 table.
- N03 "Where speed and value compete with them, the values prevail" (AJ.values_page). SoI 4.3.
- N04 Fairness: no discrimination on protected grounds (RA5 2.1). SoI 6.2.
- N05 Transparency: explanation in terms the person can act on (RA5 2.1). SoI 6.3.
- N06 Classification and residency (RA5 2.1; RA4 2.3). SoI 6.4.
- N07 Literacy: training states what AI does and does not do, and what may be shared (RA5 3.1; RA7). SoI 10.1.
- N08 Learning paths: a reading order per Role, internal audit, HR; everyone starts with the first (KBlp). SoI 10.1.
- N09 Requirements of other jurisdictions reaching the Bank through shareholders, partners, providers (KBac §2). SoI 13.1.

AICC Charter
- N10 Mission text (AJ.about_page.mission; AJ.values_page.mission). Proposed CH 2.1 mission, CH 2.2 purpose (see C01).
- N11 Not a platform team; hand-off at scale except a Service AICC runs (WWD 2.1; KBqa). CH 3.2 (see C10).
- N12 Four areas, fifteen categories (WWD §1). BM 4.5 referenced from CH 6.1.
- N13 Every Engagement leaves a reusable package (WWD §1; AJ.home.stand). BM 4.4: "…or its Outcome Report states why it leaves none."

AI Policy
- N14 Control Function Contacts of compliance and legal confirm what applies; recorded in the Standards Record (TOU 3.2; REFov). AIP 1.3.
- N15 Bank policies that apply: information security, data classification and protection, model risk, change management, procurement (KBac §3). AIP 1.4.
- N16 No Bank data into an external site, tool, form, or model; "reading is free, feeding is not"; registration with a work address; paywalled sources via procurement (REFov 3.1; TOU 4.2). AIP 2.6.
- N17 The person who relies on or signs AI output is accountable (RA6 3.1; KBqa). AIP 2.3.
- N18 Published AI output respects rights and is traceable to its governed source (RA4 2.4). AIP 2.4.
- N19 Impact assessment for higher tiers (RA5 3.1; RA7). New row in the AIP 3.3 table; needs a Contacts' decision.
- N20 Documentation: what for, how tested, where not to use (RA5 3.1). AIP 3.5.
- N21 Monitoring: performance, drift, overrides, incidents, cost, thresholds (RA5 3.1; RA4 1.2). AIP 3.5.
- N22 Agents: least function, permission, autonomy; logged; stoppable on a channel it cannot influence (RA4 3.1; RA1 3.2). AIP 3.6.
- N23 Prompt injection in the security test where the Solution reads untrusted content (RA4 2.2). AIP 3.3 Validation cell (R03 ARC-005).
- N24 Contracts forbid training on Bank data (RA4 2.3). AIP 4.1 (see C22).
- N25 An open model the Bank runs is still a provider (REFlo 4.1). AIP 4.3.
- N26 Licenses of open components recorded; security test covers the supply chain (REFlo 4.1; RA4 2.6). AIP 4.4.
- N27 Cost limits, fallback, exit as part of design (RA4 2.7). AIP 3.5.
- N28 Shadow AI remedy: an approved assistant, training, a Risk Tier for every known use (RA4 4.1). AIP 2.1 (see C21).
- N29 Lessons of an incident go into the controls and the training (RA6 6.1). AIP 5.8.

Operating Model
- N30 The portal holds no figures, data, code, personal data beyond Role names (PRIV 5.2). OM 7.6 (see C24).
- N31 Access through the access gateway; no accounts, forms, analytics, tracking (PRIV 2.1–2.3; TOU 1.2). OM 7.6.
- N32 Portal reviewed yearly with the documents; access quarterly (TOU 5.1). OM 7.6.
- N33 Feedback to the mailbox of AICC; a report that changes a document handled under DC 4 (PRIV 3; TOU 4.4). OM 7.6.
- N34 Control Function Contacts confirm, within their remit, the laws that apply (KBlp path 6; KBov 3.1). OM 4.2 "Does" column.

Document Catalog
- N35 Package Definition as AICC-TPL-14 (KBtf; KBpd). DC 6.1 row 14.
- N36 Pages authored for the site: state their edition, kept by the AICC Lead (with the Contacts for law pages), removed when unused for two quarters; a form page is the form, the instance is in the Registry or the Portfolio (KBov 3.1; TOU 3.3). DC 5.4.
- N37 Pages in RU state the revision of the source they translate (PRIV 1.1; AJ.home). DC 5.4.

Vocabulary and Style
- N38 Pages that explain the charter state no rule (TOU 3.1). VOC 2.1.
- N39 A document uses its own terms, not an external framework's; the Standards Record maps them (REFsf). VOC 3.8.

Collaboration tooling
- N40 The AICC portal row lists only "The charter and the governance with its flows"; the site also carries courses, learning paths, knowledge base, references, services, search, feedback; its workflows include Engagement (PRIV 1.2; TOU 1.1). Row text in R13; conflict C23.

AI risk and control workflow
- N41 The 12-practice table by stage (RA5 3.1): add impact assessment and documentation gates if N19/N20 adopted; map each gate to a practice.
- N42 Situation "An unapproved use of AI is reported" (RA4 4.1; STD PLT-006). ARW §8.

Executive Summary
- N43 ES §1 carries the Mission; ES §2 names the four areas.

## 2. Contradictions

- C01 Mission: new text on the site; CH 2.1 "The mission of AICC is to enable the Bank to adopt AI as a governed capability that delivers measured value" is relabelled "Purpose".
- C02 Principle names: "Security and robustness", "Lawfulness and proportionate control" (RA5 2.1) vs SoI 6.5 "Security and reliability", 6.7 "Compliance and proportionate control".
- C03 AI Incident definition (RA6 6.1) vs AIP 5.1 / VOC.
- C04 Exception: who decides (KBqa "Only by the Control Function concerned" vs AIP 6.1 AICC Lead for AICC-set requirements); Executive Sponsor deciding an Exception (RA6 7.1; corpus: CH 5.4 risk acceptance is separate); review "until closed" vs expiry date and monthly review.
- C05 "Three acceptances" (HWW 3.2) counts a Check or Validation as an Acceptance; VOC: product owner, AICC Lead, business acceptance.
- C06 Validation: by a non-builder (RA7, RA1 4.1; "human validation" RA2, RA4, WWD) vs VOC Validation = review by Control Function Contacts; Check = non-builder; AIP 2.3 "review".
- C07 Risk Tier basis (RA7; RA4 5.1) vs AIP 3.1 (data class, influence, reaches a customer, autonomy).
- C08 Gates: RA6 4.1 omits training, requires the Acceptance Checklist at release; AIP 2.1/ARW G3 include training; OM C-14: Checklist where handed to a Domain.
- C09 Provider check always by three Contacts (RA6 4.1) vs AIP 4.1 information security alone for Tier 1 / already checked.
- C10 "Does not deliver at scale… Charter 3.2" (WWD 2.1; KBqa): CH 3.2 has no such limit; OM 2.2 and VOC Service: AICC runs a Service for its whole life.
- C11 Platforms category (WWD) vs CH 3.2 "shall not own or operate the AI Platform"; no corpus distinction between AICC environments (Lab) and the AI Platform.
- C12 Assurance area "tools, providers, Solutions evaluated before use" (WWD) vs OM 2.3 not a Control Function; AIP 4.1 provider check by Contacts; VOC assurance = internal audit.
- C13 Run-rate lane "needs no business case… Business Model 6.2" (HWW; KBqa): BM 6.2 says nothing of this; CH 4.2 every Initiative has a brief; BM 5.1 Service Agreement for each Engagement.
- C14 Intake "in any form" (KBqa; PRIV mailbox) vs CT §2 one common entry via Service Management.
- C15 "support what we build" (AJ.home.stand) vs Support level none/on demand/targets/run.
- C16 "Prove before investing" (AJ.home.stand) vs business case approved and funded before the MVP (ES §4; PMM).
- C17 "keep people in charge of every decision" (AJ.home.stand) vs AIP 3.3 Tier 3 autonomy after release; SoI 11.1 level 5 agents.
- C18 First steps order (RA2 4.2; RA3 5.1) vs SoI 2.2(a) and 9.1 customer and business intelligence first.
- C19 "The strategy of AICC is the strategy of the Bank applied to AI… seven Strategic Priorities" (AJ.strategy_page) vs BM 2.3 AI adoption strategy as a series of Proposals; the Priorities are the Bank's.
- C20 Providers decider includes the Executive Sponsor (AJ.strategy_page) vs AIP 4.1 no such decision.
- C21 Shadow AI "not prohibition" (RA4 4.1) vs AIP 2.1 only approved Solutions.
- C22 Contracts "forbid training" (RA4 2.3) vs AIP 4.1 only checks whether the provider may train.
- C23 Portal scope: courses, knowledge base, learning paths, services, references on the AICC portal; VOC/CT define the AICC portal as the charter and governance; CT assigns the knowledge base to the operating portal. AJ.explore_page.control "Every page is generated from the documents" vs TOU 3.1 pages "written for the site".
- C24 PRIV 5.2 cites OM 7.6 for the no-figures rule; OM 7.6 states it only for Jira, Confluence, Service Management, operating portal.
- C25 Keeper of the site: AICC Lead (TOU 5.1) vs OM 7.6 keeper named in the Appointments Record; RI-005 keepers not appointed.
- C26 Template adopted "by a decision record" (KBpd, KBtf, TOU 5.1) vs DC 4.1 Decision Log entry.
- C27 Package states "Planned, in preparation, available" (KBpd) vs VOC 4.2 state set.
- C28 Packages: "every Engagement leaves one"; kinds method, kit, engine, catalog, template set vs BM 4.4 and VOC Reusable asset "A method or playbook".
- C29 Service life: seven states, four signals (HWW 4.1) vs VOC Stages Operate/Evolve/Retire; ARW §4 and AIP 3.5 review items.
- C30 Experiment: Lab, read-only extracts, promote/hand over/shelve (HWW 3.3) vs VOC "ends in a proposal", Stages Trial/Proposal/Handover.
- C31 Languages: Kyrgyz, Russian, English (RA3 3.1) vs SoI 3.2 Kyrgyz and Russian.
- C32 Who confirms applicability: Contacts of compliance and legal (TOU 3.2) vs AIP 5.2 the compliance function.
- C33 "set the standard by which the Bank adopts it" (mission; RA5 4.4) vs SoI 5.6, 7.1 the Bank sets the standards; AICC Lead standards are AICC-level (OM 4.2).

## 3. Terms

A. Used by the corpus, undefined in VOC (the site defines them in RA7): T01 Agent; T02 Model; T03 Provider; T04 Assistant; T05 Artificial intelligence; T06 AI output (AIP 2.4 only); T07 Guardrails / Platform Guardrails (collides with Investment Guardrails); T08 Model gateway, Tool gateway, Knowledge layer; T09 Human oversight (in/on the loop); T10 Security test against attacks on AI; T11 Disclosure, explanation, contestability vs Transparency, Explainability; T12 Model risk; T13 High-risk category; T14 Data class / classification; T15 Strategic Pillar (capitalized in SoI 3.2, fails DC 7.1 q5); T16 Evaluation / evaluation set.

B. Technology terms only the site uses: T17 Training (model) vs employee training; T18 LLM, Generative AI, Machine learning, Foundation model; T19 Fine-tuning, Prompt, Context window, Token; T20 RAG, Embedding, Grounding (overlaps Governed source); T21 Benchmark, Model card; T22 Hallucination, Bias, Drift, Over-reliance, Model collapse; T23 Prompt injection, Jailbreak, Data poisoning, Data leakage, Excessive agency, Supply chain; T24 Responsible AI, Risk-based approach, Impact assessment, AI literacy, Shadow AI; T25 Open banking, Embedded finance, Regtech, Alternative data, Liveness check, Real-time scoring.

C. Organizational terms added or used differently: T26 Mission, Purpose; T27 Lab, Solution Hub, Center of Competence; T28 Run-rate, program as a lane; T29 Package / Package Definition, kit, engine, catalog vs Reusable asset; T30 Service area / category; playbook, method note, lesson, publication; T31 Learning path, course; T32 Edition (page) vs AIP 2.4 edition of output; T33 "Charter portal" vs "AICC portal"; "corporate folder" vs "corporate share"; T34 Access gateway, mailbox of AICC; T35 Control catalogue vs Control Matrix / OM 8; T36 "Agents" (bank staff) vs AI agent; T37 "AI Competence Center Charter" vs "AICC Charter"; "Information technology operations" vs SoI 9.7 title; T38 Check-in; seven Service states; four signals.

D. Not used / style: T39 "register" (RA5 4.4); T40 "use-case discovery" (WWD); T41 "AI tools" (TOU 4.3); T42 "project" (KBqa; RA2 1.2); T43 British spellings (catalogue, centre, neighbouring, modelling, licence, programmes) vs VOC 3.2 American spelling.

## 4. Registry impact

- R01 STD new table "External instruments and standards": Id, Instrument, Body, Jurisdiction, Standing (Applies / Reference only / To confirm), Confirmed by and date, Where the charter answers it. Applies-to-confirm rows (KBac §2): KG Law on Personal Information; NBKR regulations on information security, outsourcing, operational risk; consumer protection in financial services; KG AML/CFT; jurisdictions of shareholders and partners. Reference rows (REFra, REFsf): KG digital development; KZ AI law; KZ personal data law; KZ National Bank and ARDFM; AIFC; RU 152-FZ; RU national AI strategy; Bank of Russia; RU AI ethics code; EU AI Act (reference, not obligation); GDPR; DORA and EBA; US SR 11-7 and consumer guidance; US federal and state policy; FSB, BCBS, BIS; FATF; OECD; UNESCO; Council of Europe Convention; G7 Hiroshima; NIST AI RMF and GenAI Profile; ISO/IEC 42001, 23894, 22989; OWASP Top 10 LLM; lean portfolio management and SAFe; IT service management; internal control practice.
- R02 STD table "Policies of the Bank that apply" (KBac §3): information security; data classification and protection; model risk (record whether it exists); change management; procurement and third-party; incident management; record retention; acceptable use.
- R03 STD new rows: ARC-005 untrusted content (limited permissions, filtered I/O, person before action); ARC-006 licenses of open components recorded, security test covers them; ARC-007 agent least function/permission/autonomy, logged, stoppable; ARC-008 monitoring thresholds trigger review; ARC-009 published AI output traceable, rights checked; PLT-007 cost limits per Solution at the model gateway.
- R04 AIR new columns: monitoring thresholds and who watches; impact assessment reference (if N19); evaluation set reference.
- R05 AIR new entry: the use of AI by AICC to draft the charter and generate the portal (AIR says "Uses listed to date: none"; AIP 1.2, 2.1 require listing by 2026-12-31).
- R06 RIR new Issue: acts and regulators lists unverified; Contacts not named (RI-005), so the AIP 3.2 high-risk test cannot be answered.
- R07 RIR new Risk: unapproved (shadow) AI use before the AIP 2.1 tolerance ends 2026-12-31.
- R08 RIR extend RI-005: no keeper for the AICC portal, its tooling, the mailbox (C25).
- R09 RIR new Finding (DC 7.1 check): portal scope beyond the corpus definition (C23); site pages cite clauses that do not hold the statement (CH 3.2 "deliver at scale"; BM 6.2 run-rate).
- R10 TPL and DC 6.1: row 14 AICC-TPL-14 Package Definition, kept in `portfolio/packages/`; Template file to be created in `charter/templates/`.
- R11 TPL optional columns "Filled by", "Signed or approved by" (KBtf asserts signers the corpus does not state).
- R12 Solution Definition Template: "Licenses of open components, models, datasets"; "What it shall not be used for"; "Monitoring thresholds".
- R13 CT table: update the AICC portal row (charter, Templates, explanatory pages; audience all employees; workflows add Engagement); add rows "Portal tooling" and "Mailbox of AICC"; add the generator and the access gateway to Figure 1.
- R14 Appointments Record: keeper of the AICC portal, the portal tooling, the mailbox.
- R15 Portfolio: PKG-001 charter method and templates; PKG-002 governance catalogue; PKG-003 portal generator; playbooks "The charter method", "The portal build"; the Proposals list with decision references.
- R16 Priorities Record: column "Strategic Pillar served" (N02).

## Count

| Class | Items |
| --- | --- |
| New (N01–N43) | 43: SoI 9, Charter and BM 4, AI Policy 16, OM 5, DC 3, VOC 2, CT 1, ARW 2, ES 1 |
| Contradictions (C01–C33) | 33 |
| Terms (T01–T43) | 43 |
| Registry impact (R01–R16) | 16 |
| Total | 135 |
