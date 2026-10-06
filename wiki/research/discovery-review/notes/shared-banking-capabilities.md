# Shared Banking Capabilities — review notes

Reviewer id: `shared-banking-capabilities`. Source: `html-alt/financial-services/en/shared-banking-capabilities/` (10 pages). Fix map: `fixmap/shared-banking-capabilities.jsonl` (86 entries: 7 high, 36 medium, 43 low).

## Summary

- Read: 10 pages, 132 cards (4 on the area page, 108 on eight sub-area pages, 20 on the cycles page). Every card has intent, problem, solution and a full OKR; no empty fields, no truncated sentences, no template tokens other than the known `service.eyebrow`.
- The extract does not contain the page header intents, the "problems" rows, or the stage dialog texts of the cycles page. I read those from the source HTML. Other reviewers working from the extract alone will not have seen them.
- OKRs: all but two measure their own card. One measures another cycle (Cross-Capability Improvement Prioritisation). One is partly borrowed from a twin card (Research note data section drafting). Three Cycle KRs compare elapsed time with effort so that the "after" is no better than the "before". About 40 Acceptance KRs measure a business outcome and not acceptance by a reviewer (see Questions).
- The sub-area pages are two layers of cards merged together: 20 Title Case cards whose intent starts "Agent …", and 88 sentence-case cards whose intent is a noun phrase ("Automated drafting of …"). The first layer is broader and overlaps the second; four pairs are near-duplicates.
- Jurisdiction is the weakest point of this area, beyond the known CBR pattern. The National Bank of Kazakhstan (NBK/ARDFM) is cited 55 times, 29 of them on the cycles page, which says outright "In Kazakhstan and the Kyrgyz Republic". The SAR section sends reports to FinCEN, Rosfinmonitoring or "AFMRK (for NBKR-regulated entities)"; AFMRK is, to my knowledge, the Kazakh agency. US-only vocabulary is concentrated here: BSA (19, of which "BSA officer" 15), UDAAP (8), FinCEN (9), ACH (2), adverse action, fair lending.
- Advisory & research describes a sell-side research desk and an investment advisory business (earnings calls, analyst consensus, target prices, MiFID II-equivalent rules). Whether this fits the Bank at all is an owner decision.
- Cycles: the four cycles are coherent in steps and cadence, with three exceptions listed under the cycles page (a card with the wrong cycle's OKR, a vendor stage chain that mixes a review loop with a one-off onboarding, and stages that have no card).
- Counts: every count printed on the area page and on the overview matches the cards present, except the area total. The overview shows 112; 132 cards exist. The 20 cycle cards are not counted and the cycles page is not listed on the overview.
- Group labels are printed from slugs ("Aml investigations sar", "Pricing models ftp", "Activation cross sell").

## Overview count versus cards present

The overview page (`_root.md`) shows "Shared Banking Capabilities (112)" with eight sub-areas: Credit decisioning 12, Transaction processing & settlement 12, Pricing & profitability 12, Financial crime 12, Collections & recoveries 15, Customer onboarding 15, Customer servicing 18, Advisory & research 12. Each of these eight numbers matches the cards on its page. They add up to 108.

The area total of 112 is 108 plus the 4 cards that sit on the area page itself. The 20 cards on the Capability Cycles page are left out, and the cycles page does not appear on the overview at all; it is reachable only from the area page, where it is shown as "Capability Cycles (20)". The real total is 132.

This is the generator's rule, not a slip in this area: the same arithmetic holds for the other areas (for example Banking Data & Analytics shows 114 = 109 + 5 and leaves out 20 cycle cards). It is a single decision for the whole catalog, so it is in Questions and not in the fix map.

## Patterns across the area

- Two layers of cards. On the eight sub-area pages, 20 cards have Title Case titles, an intent that begins "Agent …", and a solution that ends with "… is the primary outcome metric". The other 88 have sentence-case titles and a noun-phrase intent. Each section holds three cards and usually one of them is from the first layer, written as the whole section in one card. This is where the duplicates and the implausible complexities come from.
- Section restated as a card. In most sections one card's intent repeats the section intent almost word for word (for example "Payment investigation dossier assembly" and the section "Case dossier builder"; "Collections trajectory change detection" and "Early warning & escalation signals"). Not wrong, but the reader gets the same paragraph twice.
- Problem rows cover half of each page. Each sub-area page has two groups of sections, but the "problems" block has a tab for the first group only (for example Credit decisioning has rows for "Application underwriting" and none for limit and line management). The area page has rows for "Operational capabilities" only. Nine groups have no problem rows.
- No card answers the "New business opportunities" row. Every sub-area page has that row, but none of the 108 sub-area cards carries the New opps lens (nor Optimize). Those lenses appear only on the area page (1 card) and the cycles page (8 cards).
- Section order mixes the two groups. On every sub-area page the sections alternate between the first and second group (Credit decisioning: scorecard, annual review, underwriter review, covenants). The area page also lists the sub-areas in a different order from the overview and puts the cycles tile third.
- "Continuous" in the objective, periodic in the KR. Five cards say "on a continuous basis" in the objective and "refreshed monthly" or "refreshed weekly" in the Cycle KR. All five are in the fix map.
- Percentages on four events. Several quarterly scenarios set targets such as "≥85% of quarterly submissions in the first year" or "≥97% of sampled quarters". With four events a year these are not meaningful. Left as is; noted for the global round.
- Supervisor as a KPI source. Several Acceptance KRs depend on what a supervisory examination "confirms" (for example "supervisory examination confirms root-cause documentation completeness in ≥97% of sampled investigations"). The Bank cannot measure this itself.

## Area page — `shared-banking-capabilities/index.html`

On it: header intent; problem rows for "Operational capabilities" only; nine tiles (eight sub-areas and the cycles page) with their section lists and counts; 4 cards (Insights M, Enablement M, New opps M, Automation L). All counts on the tiles match.

- Nine group labels are printed from slugs: "Aml investigations sar", "Pricing models ftp", "Activation cross sell", "Fraud sanctions detection", "Complaints conduct", "Inquiry case handling", "Limit line management", "Settlement reconciliation", "Early stage delinquency". Four of them are repeated as tab labels on sub-area pages. All in the fix map.
- The page intent names five capabilities; the area has eight (pricing & profitability, collections, advisory & research are missing). In the fix map.
- The page intent says the capabilities operate "under direct supervisory mandates from NBKR, NBK/ARDFM, CBR, and FATF". FATF is not a supervisor. Left for the global regulator decision.
- "Regulatory Examination Pack Assembly" speaks of "NBKR, NBK/ARDFM, and CBR supervisory examinations", and its Adoption KR measures use across all three. Only NBKR examines the Bank.
- "Cross-Capability Operations Readiness Brief" speaks of "eight separate capability teams", which matches the eight sub-areas. One stray hyphen fixed.
- The four cards are sound: each OKR measures its own card, cadences agree between intent, solution and KRs.

## Credit decisioning (12 cards: 7 Automation, 4 Insights, 1 Enablement; 5 S, 7 M)

Sections: Scorecard & model performance, Annual credit review, Underwriter review & override, Covenant monitoring; 3 cards each.

- "Credit Origination Analytics" is rated S although it joins three sources weekly and does clustering and attribution; its single-source neighbours are M. Proposed M.
- The section "Underwriter review & override" does not cover its card "Adverse Action Notification Drafting" (a decline letter to the customer). One sentence added to the section intent.
- "Covenant compliance continuous monitoring" runs once per borrower reporting cycle. Title corrected.
- Basel III IRB is cited as binding in five places ("Under NBKR credit-risk model governance rules and Basel III IRB requirements, material model drift triggers a mandatory recalibration and board notification cycle"). See Questions.
- US vocabulary: "adverse action", "fair-lending monitoring", "disparate impact signals". The scenarios themselves hold anywhere (a compliant decline notice; equal treatment across segments), so no fix is proposed; a wording decision for the global round.
- Two small wording fixes ("every decline volume"; "capacity … is the primary capacity metric").

## Transaction processing & settlement (12 cards: 7 Insights, 4 Automation, 1 Enablement; 4 S, 8 M)

Sections: Payment failure & exception pattern analytics, Nostro reconciliation, Investigation triage & next-step support, Case dossier builder; 3 cards each.

- "Payment exception queue prioritisation": the problem says investigators give "low-value or early-deadline cases" the same attention as urgent ones; "early-deadline" means the opposite of what is intended. The regulatory sentence in the same field is copied from the pattern-analytics section. Both fixed.
- "ACH" (the US clearing network) appears in the page intent and the first section intent. Replaced with neutral rail names.
- "Payment Exception Pattern Analytics" and "Payment failure root-cause attribution" overlap: the first already attributes failures to internal, counterparty or customer causes, and the second says pattern analysis identifies families "by symptom" only. Not a duplicate, but the boundary is blurred.
- "Fraud and dispute pattern signal" sits in the section "Case dossier builder", whose intent is about pre-assembled dossiers. It reads as a financial-crime card. One sentence added to the section intent; moving the card is an owner decision.
- "Straight-through processing gap signal" says continuous in the intent and weekly everywhere else. Fixed.
- The page's Automation problem row is about closure letters and investigation summaries; no card drafts them (only the nostro card drafts correspondent messages).
- Two small consistency fixes (customer history missing from a solution; "settlement/settlements staff").

## Pricing & profitability (12 cards: 6 Automation, 5 Insights, 1 Enablement; 4 S, 8 M)

Sections: Pricing experiment analytics, Segment profitability deep-dive, FTP & RAROC pricing signal, Profitability pack production; 3 cards each.

- "Pricing and Profitability Analytics" is the whole page in one card: weekly hurdle monitoring, experiment synthesis, the quarterly pack and ad-hoc deep-dives. Each of these is a separate M card on the same page ("RAROC hurdle breach alert", "Pricing experiment result synthesis", "Profitability pack assembly automation", "Segment profitability attribution analysis"). It is rated M; proposed L. Whether to keep it at all is in Questions.
- The same card says each pack takes "multi-week assembly"; the section intent and the pack card say two to three days. Problem and Cycle KR aligned to two to three days.
- "Profitability pack assembly automation": the second sentence of the intent is regulatory background copied from the section intent. Replaced with what the scenario delivers.
- The page assumes an A/B pricing experiment practice with a statistics function. Plausible for a digital bank, but it is an assumption about scale.
- All other OKRs measure their own card.

## Financial crime (12 cards: 6 Automation, 5 Insights, 1 Enablement; 4 S, 8 M)

Sections: Transaction monitoring alert triage, AML alert investigation pack, False-positive root-cause analysis & rule tuning, SAR drafting; 3 cards each.

- SAR section, wrong addressees. The section intent reads "FinCEN (for US-regulated entities), Rosfinmonitoring (for CBR-regulated entities), or AFMRK (for NBKR-regulated entities)". To my knowledge AFMRK is Kazakhstan's Agency for Financial Monitoring, and the Kyrgyz unit is the State Financial Intelligence Service; Compliance should confirm. The same list is in the page intent and in two cards. The risk-control area uses yet another name ("KFM") for the same list. The fix map replaces the list with "the national financial intelligence unit" (5 entries, high); the official name is for Compliance to supply.
- SAR section, US rules and roles. The filing deadline is given as "30 days … under FinCEN rules"; the role throughout is "BSA officer" (15 times), with "BSA program" and "BSA management". Replaced in the fix map. The KR "within 5 business days of suspicion determination" may be longer than the local deadline allows; see Questions.
- Page scope does not match the cards. The page intent promises "AML/CFT monitoring, sanctions screening, fraud detection, and SAR filing"; the first group is labelled "Fraud sanctions detection"; the Enablement and Automation problem rows are entirely about sanctions hit review. All 12 cards are about AML transaction-monitoring alerts and SARs. The sanctions cards are on the Customer onboarding page and the only fraud card is on Transaction processing.
- Near-duplicate pair: "Transaction monitoring alert pre-investigation pack" and "AML Alert Investigation Pack" both assemble KYC, transaction history, prior alerts and related accounts before the analyst starts. Their baselines disagree (15 to 45 minutes against 30 to 180 minutes per alert).
- The section intent on rule tuning cites "FATF Recommendation 10" as the reason rule changes need model-risk committee approval. Recommendation 10 is customer due diligence. Fixed. The other uses of Recommendation 10 on the page (review obligation, investigation records) are loose but arguable; left.
- "Transaction monitoring alert priority triage scoring" reorders a work queue and carries the Insights lens; the two equivalent cards in this area are Automation. Proposed Automation.
- Two small consistency fixes (objective "continuous" against monthly KRs; "compliance team" against "transaction monitoring team").

## Collections & recoveries (15 cards: 8 Insights, 5 Automation, 2 Enablement; 6 S, 9 M)

Sections: Delinquency segmentation & contact strategy, Legal referral triage, Promise-to-pay arrangement documentation, Portfolio write-off & sale analysis, Early warning & escalation signals; 3 cards each.

- Two Cycle KRs where the "after" is not better than the "before": "Legal Referral Triage" (pack within 4 hours against 2–4 hours of assembly) and "Broken arrangement re-engagement brief" (brief within 2 hours against 15 to 30 minutes of reconstruction). Both compare elapsed time with effort. Reworded.
- The page intent cites "FATF guidance on financial crime typologies in recovery processes" as a source of supervisory oversight for collections. Nothing of the kind exists and nothing else on the page touches financial crime. Removed.
- The page intent mentions restructuring; no section covers it.
- Regulatory claims that need checking: "Under NBKR consumer credit protection rules, banks are required to assess hardship assistance eligibility"; "collections strategies must be proportionate and evidence-based"; "payment arrangement terms must be … provided to the borrower in writing". See Questions.
- Four small consistency fixes (dossier contents; CFO and CRO as reviewers; an undefined "escalation watch list"; a redundant tail).
- Otherwise the page is the most coherent in the area: each section has an operational card, a feedback-analytics card and a pattern card, and each OKR measures its own card.

## Customer onboarding (15 cards: 7 Automation, 6 Insights, 2 Enablement; 4 S, 11 M)

Sections: KYC document extraction, Account setup & activation, CDD risk classification, Early cross-sell signals, Sanctions & PEP screening; 3 cards each.

- Near-duplicate pair: "Complex CDD Research Pack" and "Enhanced due diligence research pack" both assemble adverse media, ownership traces, sanctions and PEP results and source of funds for high-risk cases. Baselines disagree (two to six hours against 60 to 120 minutes per case).
- "KYC Extraction and CDD Classification" spans two sections (extraction and risk classification) and is rated S. Proposed M. Its Cycle KR sets "within 15 minutes" against "15–30 minutes of manual extraction"; reworded.
- "PEP and adverse media continuous monitoring": the before → after of time is in the Acceptance KR, and the Cycle KR has no baseline. Re-split.
- "Early-Tenure Cross-Sell Signal" ends its intent with a sentence about outcome metrics. Replaced. It also overlaps "Early tenure product propensity scoring" and "Onboarding window activation coaching": three cards on steering the first 90 days. All three address relationship managers; for mass retail customers served through the app there is no relationship manager.
- Sanctions lists: the section names "OFAC SDN, UN, EU, and HM Treasury" lists and no national list. See Questions.
- The page intent cites "NBKR Instruction No. 5"; the data area cites "NBKR AML/CFT Regulation No. 2" for the same subject. One of them is wrong or both need confirming.
- "Account activation exception triage" measures a "regulatory activation deadline missed rate". It is not clear such a deadline exists.
- Small consistency fixes (hyphenation of a title; "disposition" used for a classification review; digital channels dropped from a solution; two "continuous" objectives).

## Customer servicing (18 cards: 11 Insights, 6 Automation, 1 Enablement; 10 S, 8 M)

Sections: Frontline policy & next-step copilot, Complaint response drafting & QA, Customer interaction summarization & follow-up extraction, Complaint pattern & conduct analytics, Service intake & structured case skeleton, Support ticket pattern mining; 3 cards each.

- "UDAAP" is used 8 times in the complaint-pattern section ("UDAAP risk indicator", "UDAAP indicator phrases"). It is a US statutory concept. One replace-all entry in the fix map. The same section cites "NBK/ARDFM consumer protection rules" four times.
- "Customer Interaction Summarization" says documentation time "is eliminated from AHT" while the representative still reviews and submits and the KR targets a 40% cut. Fixed; AHT expanded.
- "Interaction quality signal synthesis": the Acceptance KR ends "NPS improvement attributable to early coaching intervention measurable within 12 months", which cannot be measured as written. Rewritten.
- "Complaint Pattern Intelligence" classifies every ticket and every regulatory-portal complaint weekly and is rated S; the ticket-only card beside it is M. Proposed M. It also overlaps "Support ticket cluster root-cause synthesis" (two sections cluster the same tickets).
- Baselines disagree in two places: a policy lookup costs "5-15 minutes" in the problem row and "2–5 minutes" in the copilot's KR (aligned); complaint pattern lag is "four to six weeks" in the section intent and "13 weeks" in the pattern card (left: a quarterly cycle gives both).
- "Complaint response tone consistency analytics" speaks of "ombudsman referrals" and calls tone failures "the primary driver of complaint escalations". The first assumes a financial ombudsman; the second is unsupported.
- Small consistency fixes (objective 100% against KR 95%; chat dropped from an Adoption KR; two "continuous" objectives).
- The page is the most Insights-heavy in the area (11 of 18) and has one Enablement card for an Enablement problem row that describes the largest pain.

## Advisory & research (12 cards: 7 Automation, 4 Insights, 1 Enablement; 6 S, 6 M)

Sections: Earnings call synthesis, Client suitability assessment, Issuer & sector research note drafting, Portfolio review narratives; 3 cards each.

- Fit of the whole page. Six cards assume a sell-side research desk ("analysts covering 20-50 issuers", earnings seasons, "sell-side consensus estimates", "rating or target-price revision", "institutional clients"). Six assume an investment advisory business with suitability files and quarterly portfolio reviews. The regulation cited is "NBK/ARDFM MiFID II-equivalent rules" (15 mentions of NBK on the page) and "NBKR suitability rules"; to my knowledge the securities market in the Kyrgyz Republic is supervised by a separate authority, not NBKR. See Questions.
- Near-duplicate pair: "Research Production Automation" and "Research note data section drafting" draft the same four data-driven sections, with the same Acceptance wording and the same "within 4 hours, vs. 1–2 days" Cycle KR. The first carries the Enablement lens although its title says Automation.
- "Research note data section drafting": objective and Adoption KR speak of the "post-earnings publication window" and "earnings season", which belong to the twin card. Rewritten to this card's own scope.
- "Research coverage gap signal" is about events on already covered issuers that call for a note update, not about coverage gaps. Title changed to "Research update trigger signal".
- "Portfolio review narrative drafting": baseline "2 to 3 days of manual drafting per client" is impossible for a large book reviewed every quarter. Changed to hours.
- Four Acceptance KRs state the same figure twice ("≥85% … confirmed; fewer than 15% dismissed"). Harmless; not in the fix map.

## Capability Cycles (20 cards, 4 cycles of 5 cards; each cycle has one card per lens: Insights, Enablement, Automation, Optimize, New opps; 9 S, 11 M)

On it: a one-line page intent; for each cycle a title, a one-line intent, a three-paragraph description, four problem rows (Analyze, Optimize, Automate, Enrich), a chain of five stages, and five cards. Each stage opens a dialog with a title, an intent and a problem; these texts live in a script block and are not in the extract. Cards are not attached to stages in the markup; the link is only in the wording ("at the identify stage").

Capability KPI & SLA review cycle. Stages: Measure → Review → Identify breaches → Plan remediation → Track. Cadence: monthly at operational level, quarterly at senior management.

- Steps and cadence are consistent between the description, the stage dialogs and the cards (scorecard within one business day of period close; root-cause draft within 4 hours of breach confirmation; ranked remediation queue within 2 business days; daily mid-cycle signal).
- Stage references cross over in two cards. The stage dialogs put breach prioritisation in "Identify breaches" and root-cause attribution in "Plan remediation". The root-cause card places itself "at the identify stage"; the prioritisation card places itself "at the plan stage", and its problem text is the Identify stage's problem almost word for word.
- Scope: "across all shared capabilities" in the text, but the cycle and its scorecard card cover five domains (credit decisioning, payments, KYC, AML, collections). Pricing, servicing and advisory are out. The continuous improvement cycle lists a different five.

Continuous improvement cycle. Stages: Identify → Prioritise → Implement → Measure benefit → Sustain. Cadence: rolling quarterly, with a quarterly prioritisation committee.

- "Cross-Capability Improvement Prioritisation" has the investment cycle's OKR: "annual investment prioritisation cycles", "investment committee", "annual prioritisation intake close". This cycle is quarterly and decided by a prioritisation committee. Rewritten (high).
- The cards chain well: intake unification builds the register, business-case drafting reads it, prioritisation ranks it, benefit measurement checks it at 30, 60 and 90 days, the knowledge base keeps the outcome.
- "Implement" and "Sustain" have no card. The Sustain dialog describes improvements eroding within two to four quarters; the only card near it is a knowledge base, which does not watch for erosion.
- Problem rows and cards do not line up: the Analyze row asks for a view of the whole pipeline (no card); the Automate row lists business-case modelling and the prioritisation pack, while the Automation card is intake unification, which no row mentions.
- "Improvement Opportunity Intake Channel Unification" is measured on duplicate detection, which the card never describes. One clause added to the solution.

Capability investment cycle. Stages: Plan → Approve → Build → Deploy → Sustain. Cadence: annual planning with a mid-year window.

- Steps, cadence and cards agree (gap register at planning kick-off; case assembly and build-buy-partner comparison for approval; weekly delivery variance during build; quarterly benefit tracking).
- The cycle "anchor" is "the time from strategic gap identification to approved investment mandate", which covers only the first two of the five stages. "Deploy" has no card.
- The Approve dialog lists "technology investment committee, ALCO, or board". ALCO does not approve capability investment. Fixed.
- "Programme Delivery Variance Monitoring" monitors and flags, like the Insights cards of the other cycles, but carries Enablement; the one-card-per-lens pattern seems to have forced the label.
- The text says significant technology and outsourcing investments "must be notified or pre-approved" under "NBKR and NBK/ARDFM supervisory frameworks".

Vendor & sourcing review cycle. Stages: Evaluate → Negotiate → Onboard → Monitor → Renew or exit. Cadence: critical and material vendors quarterly, others annually.

- Written for two countries. "In Kazakhstan and the Kyrgyz Republic, NBK and NBKR outsourcing regulations impose formal obligations …"; oversight must be evidenced "to NBKR/NBK inspectors and, where applicable, to EBA-aligned supervisors". Three entries in the fix map rewrite the cycle description for the Kyrgyz Republic. The cards and stage dialogs still name NBK about 25 times; that is for the global regulator decision.
- The stage chain mixes two things. Evaluate, Negotiate, Monitor and Renew form a review loop for an existing vendor; Onboard is a one-off event for a new vendor and sits in the middle. The Evaluate dialog says it "opens each vendor review cycle" and the Renew dialog says it "closes one cycle and opens the next", so the chain is meant as a loop, and onboarding does not belong inside it.
- The problem rows and the cards do not line up. The Optimize row (sourcing strategy and concentration risk) is answered by the card labelled New opps ("Sourcing Concentration Risk Analysis at Renewal"). The card labelled Optimize is an onboarding timeline planner that no row mentions. The Enrich row (a consolidated vendor knowledge base) has no card. The Renew dialog's problem (generic, untested exit plans) has no card.
- "Continuous Vendor Risk Monitoring": the Acceptance KR asks for ≥80% material alerts and a false-positive rate of ≤15%; the two do not agree. Fixed. One clumsy phrase fixed in the card and in the Monitor dialog.
- Whether NBKR sets outsourcing "concentration limits", on which two cards and a KR depend, needs checking.

Catalog-wide note: the problem rows on every cycles page use the labels Analyze, Optimize, Automate, Enrich, while the cards use Insights, Automation, Enablement, Optimize, New opps, and the sub-area pages use Insights & analytics, Enablement, Automation, New business opportunities. Three vocabularies for the same lenses.

## Questions for the owner

1. Area total on the overview: should it count the cycle cards (132) or stay at 112 with the cycles page listed separately? Today the cycles page is not on the overview at all. The same choice applies to every area.
2. Two layers of cards: keep both, or fold the 20 broad "Agent …" cards into the detailed ones? At minimum, decide the four near-duplicate pairs: transaction monitoring pre-investigation pack / AML Alert Investigation Pack; Complex CDD Research Pack / Enhanced due diligence research pack; Research Production Automation / Research note data section drafting; and Pricing and Profitability Analytics against the four detailed pricing cards. My recommendation is to keep the detailed cards and remove or narrow the broad one in each case. Title casing (Title Case against sentence case) should be settled with the same decision.
3. Advisory & research: does the Bank run, or plan, a research desk and an investment advisory service? If not, should the page be kept as reference, cut down to suitability and portfolio review, or removed? Which authority's rules should it cite?
4. Kazakhstan: should NBK/ARDFM be handled in the same global decision as CBR? It is cited 55 times in this area and about 250 times in the extracts of the whole catalog, and is not on the list of global patterns.
5. Suspicious activity reporting: what is the official English name of the Kyrgyz financial intelligence unit to print, is the local term SAR or STR, and what is the filing deadline? Two KRs ("within 5 business days of suspicion determination"; "within 4 hours of investigation completion") should be reset against it.
6. Financial crime page: should the sanctions and fraud cards move here from Customer onboarding and Transaction processing, or should the page intent, the problem rows and the group label be rewritten to say AML monitoring and reporting only?
7. Problem rows: is one tab per page intended, or are rows for the second group of each page missing (nine groups, plus two on the area page)? And should each sub-area page have at least one New opps card to answer its "New business opportunities" row?
8. Acceptance KRs: about 40 cards measure a business outcome there ("exception volume reduces by ≥20% within 18 months") and not acceptance by the named reviewer. Rewrite to the pattern in the brief, or accept as a second valid form?
9. Cycles: (a) should the vendor stage chain be reordered so that onboarding is not inside the review loop (for example Onboard → Monitor → Evaluate → Negotiate → Renew or exit)? (b) In the KPI cycle, does root-cause attribution belong to Identify or to Plan remediation? (c) Should stages without a card (Implement, Sustain, Deploy, exit planning) and the vendor cycle's missing Enrich card be filled? (d) Should the KPI and improvement cycles cover all eight capabilities?
10. Regulatory statements to confirm with Compliance and Risk: Basel III IRB treated as binding; an NBKR obligation to assess hardship eligibility and to confirm payment arrangements in writing; a regulatory deadline for account activation; "NBKR Instruction No. 5"; NBKR outsourcing notification lead times of four to twelve weeks and concentration limits; the sanctions lists the Bank must screen against (the text names OFAC, UN, EU and HM Treasury and no national list); the existence of a financial ombudsman.
11. Role names: "Head of Shared Capabilities", "Head of Onboarding", "CTO" as owner of capability investment, "model risk committee". Which of these exist at the Bank, and what should replace the others?
12. Section order: should sections on each sub-area page follow their group (all of group one, then group two), and should the area page list sub-areas in the overview's order?
