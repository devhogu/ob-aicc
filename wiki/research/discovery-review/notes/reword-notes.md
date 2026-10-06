# Points raised during the rewording of the Discovery Catalog (English)

Prepared 6 October 2026. Each rewording worker recorded the points where it had to choose and a person should confirm: a contradiction inside a card that it resolved or left, two role names it merged, a condition it added, a near-duplicate pair, a term it kept. They are listed by page as recorded. Numbers in brackets are the positions of the text in the working files of the run.

Pages: 69. Points: 292.

## (overview)

- Fix 017 changes only the visible label (key 394); the aria-label of the same list is not a line of this view and still reads 'Customer-facing value streams'. The alternative in owner question 9 (keep the label, move Treasury & Funding to Cross-cutting flows) is a structural choice left to the owner.
- Fixes 019 and 020 reword the two peer-framework titles; whether these two boxes are shown at all is owner question 10.

## banking-data-analytics

- Card cross-domain-data-quality-posture: the objective said 'continuously updated' while Adoption and Cycle measure a monthly scorecard; the card is now stated as monthly throughout. Confirm monthly is the intended cadence.
- Card data-mesh-domain-api-registry presupposes domain teams publishing data products through APIs (a data-mesh architecture). This is not in the rules' list of scale-dependent practices, so no condition was added; the owner may want one.

## banking-data-analytics/credit-exposure-data

- Key 94 read 'Basel III Part 4'; the part number could not be confirmed and is now 'in line with Basel III'. Confirm, or name the large-exposures framework.
- Fix 018 changes the visible tab label (key 112); the aria-label of the tab input is not a line of this view.
- Cards counterparty-group-aggregation and the section introduction: the 25% of Tier 1 limit is now stated as common practice ('commonly 25%'); the 20% early-warning threshold is kept as the Bank's own level.
- Card connected-party-group-mapping: the objective said 'continuous analysis' while Adoption and Cycle measure a monthly pass; it now says monthly.
- Cards ECL Provision Narrative and ECL Stage Movement Analysis overlap (both draft quarterly stage-movement text, for different reviewers); no fix entry directs a change, so both are left as they are.

## banking-data-analytics/customer-data

- Fix 015 changes the visible tab label (key 112); the aria-label of the tab input is not a line of this view.
- Card consent-posture-monitoring (keys 650, 662) speaks of consent coverage falling 'below regulatory thresholds'; personal-data law does not normally set a coverage threshold, and the sibling card consent-coverage-by-product-segment uses 'the threshold defined in the data privacy governance framework'. Left as written; the owner may want the same wording in both.
- Section title 'Segmentation & behavioural data' (key 1740) and the card title in part 2 are respelled 'behavioral'; the link label on the area page is respelled to match.

## banking-data-analytics/data-cycles

- Golden Record Deduplication Assist (1052, 1072, 1108): 'Cyrillic-Latin transliterations' kept, as fix 117 proposes and so that the card matches its twin on the Master & reference data page. It is a regional detail; decide whether both cards should say 'transliterations between scripts' instead.
- Regulatory data submission cycle (2400, 2428): the three named supervisors became 'the regulator', and the parallel perimeters are now conditional ('Where the Bank operates in more than one jurisdiction'). 'By supervisor' and 'each supervisor' are kept as neutral wording for a bank that reports to one or several authorities.
- Master Data Estate Health Monitor, problem (1304): 'Board reporting' written as 'Data governance council reporting', the recipient named in the intent and the OKR of the card. Restore if Board reporting is meant.
- Regulatory data submission cards (2568–3088) and stages (s46, s63, s67, s78): the three named supervisors and 'three regulatory perimeters' were removed. 'Each supervisor' and 'by supervisor' are kept as neutral wording; only Cross-Supervisor Exception Pattern Analysis carries the condition 'Where the Bank operates in more than one jurisdiction' (2916), since that card has no content for a bank with a single supervisor. Its title is unchanged.
- Cross-Supervisor Exception Pattern Analysis (2916, 2960): 'the data team' written as 'the data quality team', the team that resolves the root causes in the solution and confirms them in the OKR. Restore if a different team is meant.
- Lineage Documentation Currency Dashboard, solution (2184): the data governance team's confirmation of stale flags was carried in from the OKR acceptance line, which was the only place naming a reviewer.
- Lineage Documentation Currency Dashboard, intent (2152): 'on a continuous basis' is kept next to the weekly-updated signal of fix 123; the comparison still runs weekly in the solution. Decide whether 'continuous' should also become 'weekly'.

## banking-data-analytics/market-data

- Fixes 065–068 proposed Kyrgyz names (National Statistical Committee of the Kyrgyz Republic, NBKR, 'the Kyrgyz Republic and its main trading partners'). Under section 3 of the rules they are written in the neutral form: 'the national statistics office', 'the central bank', 'the domestic market and its main trading partners' (580, 630, 746, 766).
- Fix 069 (968): the NBKR is written as 'the central bank'; the Federal Reserve Bank of New York is kept as the administrator of SOFR, as the fix proposes. SOFR and EURIBOR are kept as international benchmarks; TONIA and MOSPRIME became 'the domestic benchmark rate'. Decide whether naming the SOFR administrator is wanted on the page.
- The central bank as a publisher of official exchange rates and macro data is written 'the central bank', not 'the regulator', since the text is about its publications and not its supervision (580, 630, 746, 968).
- Yield Curve Input Quality Gate, OKR adoption (1850): 'all three curve families' (KZT, RUB, USD) became 'all curve families', since the count followed from the three named currencies.
- Yield Curve Construction Commentary, intent (1910): the sparse-liquidity statement named KZT, RUB and USD; it now says 'local-currency markets', as the problem of the same card does (KZT and RUB only).
- Interpolation Methodology Review Brief (2026, 2046, 2058): the intent names 'the market risk team' as the user of the brief, while the problem and the OKR name 'the market risk quant team' as its author and reviewer. The solution's 'quant team' was written as 'the market risk quant team'; the intent is left as it is. Confirm that these are one team.

## banking-data-analytics/master-reference-data

- Fixes 022–025 and 028 proposed 'the Kyrgyz market' and 'the state register of legal entities of the Kyrgyz Republic'; written in the neutral form instead ('where names are written in more than one script, such as Cyrillic and Latin'; 'the official registers of legal entities'). Decide whether 'Cyrillic and Latin' may stay as the example of two scripts (144, 192, 474) or should go as well.
- Card title 'Organisational Hierarchy Currency Check' respelled 'Organizational …' (854); the urn keeps 'organisational'. Link labels on the area page and overview that show this title need the same spelling.
- Customer Master Onboarding Quality Check: 'the onboarding team' in the intent (1134) written as 'the onboarding officer', the role name that fixes 033 and 034 set for the rest of the card.
- Organizational Hierarchy Currency Check, Acceptance (930): the reviewer was 'the finance team'; written as 'the finance and regulatory reporting teams', the recipients named in the intent, problem and solution. Restore if only the finance team confirms the flags.
- Catalog Lineage Completeness Check, problem (2434): the card cites BCBS 239 Principles 2 and 3 for lineage. Fix 030 on this page renumbered accuracy and integrity to Principle 3; lineage evidence is usually tied to Principle 2 (data architecture) and Principle 3. Numbers kept as written; confirm.

## banking-data-analytics/regulatory-data

- Section 'Data residency & localization controls' and its three cards assumed a statutory duty to keep citizens' personal data on domestic servers. Written conditionally ('where applicable law on personal data requires it', 'personal data subject to localization requirements'). Confirm that the section should stay conditional rather than state localization as a given duty.
- Pipeline Change Lineage Impact Assessment: Acceptance (698) keeps the target 'deployment-to-lineage-update gap ≤ 5 business days in ≥ 90% of changes', while the solution and the Cycle KR say lineage entries are approved before deployment and the lag is eliminated. The target was not changed; decide whether it should read as approval before deployment.
- Pipeline Change Lineage Impact Assessment, solution (662): approval of the draft lineage entries was given to the data governance team, while the intent and the Acceptance KR name data stewards. Written so that data stewards approve the entries and the data governance team reviews the impact assessment.
- BCBS 239 Lineage Mapping, Acceptance (930): 'gap flags resolved before supervisory submission' written as 'before supervisory examination', following fixes 099 and 100 (a lineage map is examination evidence, not a submission). Restore if the next regulatory report submission was meant.
- BCBS 239 Lineage Mapping and Regulatory Dataset Lineage Record cite Principle 3 alone for lineage and reproducibility, while the section intent (fix 096) cites Principles 2 and 3. Numbers kept as written.
- Data Residency Compliance Check (1522): 'DPO' was never expanded on the page and the next card writes 'data privacy officer'; first mention written as 'the data privacy officer (DPO)'. Confirm the two are one role (a DPO is more often a data protection officer).
- Cross-Border Data Flow Monitor, intent (1754): 'cross-border transfer register' written as 'legal basis register', the name used in the solution, the Adoption KR and the rest of the section.
- Regulatory Change Readiness Tracker, solution (1942): the tracker's user written as 'the regulatory reporting and data governance leads', as in the intent and the objective; the Acceptance KR keeps the regulatory reporting lead as the one who confirms escalations.
- 'Regulatory Change Data Impact Assessment' and 'Regulatory Change Data Gap Assessment' describe almost the same scenario (map new form fields to the data catalog, list the gaps, feed the change program); the second card's problem even calls its output 'a data impact assessment'. No fix entry directs how to tell them apart, so both were reworded as written: the first serves the regulatory change program team's implementation plan, the second scopes the data remediation program. Decide whether to differentiate them further or keep one.
- 'Regulatory Change Data Impact Assessment' has the urn slug 'regulatory-reporting-pack-assembly', which does not match its title; identifiers were not touched.
- Regulatory Change Data Gap Assessment, solution (2174): the user of the assessment written as 'the data governance and regulatory reporting teams', as in the intent; the Acceptance KR names the regulatory reporting team as the one that confirms completeness.

## banking-data-analytics/risk-position-data

- Fix banking-data-analytics-019: the tab label (key 112) is corrected; the aria-label of the tab input named in the locator is not among the lines of this part and still needs the same text.
- Scale condition: 'a bank with a trading book' is stated in the 'Trading book positions' section introduction and once in each of its three cards; the Internal Models Approach is conditioned on the Bank using internal models (192, 494). The sections 'Limit & headroom data' and 'Risk metrics & sensitivities' also assume trading desks and a derivatives book (VaR by desk, Greeks) but carry no condition; decide whether they should.

## banking-data-analytics/transaction-data

- Fix banking-data-analytics-016: the tab label (key 112) is corrected; the aria-label of the tab input named in the locator is not among the lines of this part and still needs the same text.
- Fixes banking-data-analytics-055 and -056 proposed the Kyrgyz scheme 'Elcart'; under the rules the neutral form 'the national card scheme' is written instead (1744, 1826).
- Fix banking-data-analytics-062 renames the card to 'Enrichment Coverage and Accuracy Drift Detection' (1010); the title 'Transaction Behaviour Profile' is respelled 'Transaction Behavior Profile' (1514) and the section title 'Transaction enrichment & categorization' (964). Link labels on other pages must follow.
- Fixes banking-data-analytics-058, -059 and -060 proposed the Kyrgyz scheme 'Elcart'; under the rules the neutral form 'national card scheme' is written instead (2026, 2046, 2058), and the drafted Adoption line that named Elcart is neutralized the same way (2082).

## customer-channels

- Link labels respelled: 'Digital engagement & personalization' (374), 'Cash replenishment optimization' (669), 'API product catalog & monetization' (855); the section titles they point to must carry the same spelling.
- Card 'Omnichannel Service-Recovery Orchestration': the Acceptance line (1035) measures an outcome (repeat-contact rate reduced by ≥25%) and the card names no reviewer of the AI agent's resolution brief; left as drafted, since naming a reviewer and an acceptance rate would add a claim. Decide whether to restate it.
- The role is written 'complaint handler' (1199, 1231, 1243, 1267) to match the Contact center page; 'complaints team' is kept as a distinct unit.

## customer-channels/channel-cycles

- Card channel-performance-pack-automation and several other cards of this page name the Head of Channels as the accepting reviewer only in the OKR; the solutions now state that role alongside the team that was already named (332, 448, 564, 680, 1848, 1964, 2080). Confirm that the Head of Channels is the intended reviewer in each.
- Card rollout-sequencing-optimisation: the Acceptance line (2636) is an outcome target (adoption ≥15% higher in the first 90 days), not a rate at which a named reviewer accepts the recommendation. Left as drafted because no acceptance figure exists in the card; the owner may want to replace it with a channel evolution team acceptance rate and move the adoption uplift to the objective.

## customer-channels/contact-center

- customer-channels-045: written as "The handling agent's after-call work time" rather than "per handling agent", because the solution and the OKR of the card measure after-call work time per interaction; confirm the wording.
- customer-channels-050: written as "exit to a contact-center agent" (the page's one name for the human role) rather than "a human agent"; "human agent" is kept only in the section introduction, where it is contrasted with the automated IVR.

## customer-channels/digital-channels

- customer-channels-077: the proposed "in the Kyrgyz Republic" is not inserted (rules, section 3); the three countries are removed and the sentence is left as a general statement about retail and SME customers.
- customer-channels-084, customer-channels-085: the proposed "personal data legislation of the Kyrgyz Republic" is written as "applicable law on personal data" (rules, section 3); the exact reference, if wanted, belongs on the landing page.
- Keys 1522, 1554, 1658 (digital adoption reporting): the cards assume that digital adoption is reported to the regulator; kept as a neutral statement ("digital adoption reporting to the regulator", "commonly a supervisory interest metric"). Confirm that such reporting exists for the Bank, or the regulatory half of the reporting-pack card should be made conditional.

## customer-channels/partner-api-channels

- Whole page depends on a practice only some banks have (an API platform open to partners; rules, section 3, last row). The condition is stated once in the page introduction, once in each of the four section introductions, and once in the intent of each of the 12 cards ("Where the Bank operates an open banking API platform…" in the governance section, "Where the Bank operates an API platform for partners…" elsewhere). Confirm this is wanted on every card of a page whose title already says "Partner & API channels".
- customer-channels-110: the proposed sentence about the Kyrgyz Republic and NBKR is not inserted (rules, section 3); written as "Open banking frameworks are still developing in many markets", with PSD2 kept once as an example ("such as PSD2").
- customer-channels-112, customer-channels-113: the proposed "open banking framework of the Kyrgyz Republic" is written without the country.
- customer-channels-117: card title changed to "Partner Performance Pack Intelligence"; the intent now names the monthly partner performance pack, carried from the solution. Link labels on other pages must follow.
- Titles respelled: section "API product catalog & monetization" (964) and card "API Catalog Expansion Opportunities" (1242); link labels on other pages must follow.
- One name per role: "governance team" is written "API governance team" throughout the governance section (keys 242, 274, 286, 310, 358, 402, 494); the "API governance committee" stays a distinct body.
- One name per role: "finance" is written "the finance team" in the billing reconciliation card (keys 1018, 1050, 1062, 1086).

## customer-channels/physical-branches

- customer-channels-024 proposed 'in the Kyrgyz Republic'; written without a country, as the rules require (no Kyrgyz specifics in the cards).
- The card title 'Branch Site Selection Modelling' is respelled 'Branch Site Selection Modeling' (key 466); link labels on the area page and the overview that show this title need the same spelling.
- The 30–90 day notification lead time in 'Branch Regulatory Notification Drafting' (key 262) is kept as 'typically 30–90 days'; the review flagged the figure as unverified.

## customer-channels/relationship-management

- Private banking is treated as a practice that only some banks have: the condition is stated once in the page header (94), once in each of the two section introductions that mention it (968, 1356) and once in the card 'Cross-Sell Opportunity Identification' (1658). The general market statement in 168 is left as it is. Owner to confirm whether private banking should be conditioned on this page.
- The statement that supervisors expect documented client contact at a frequency proportional to the client's revenue tier (192, 262, 766) is kept as common supervisory guidance; owner to confirm it holds, or it can be restated as the Bank's own contact standard.

## customer-market-intelligence

- customer-market-intelligence-004 proposed 'Reputation defence'; written 'Reputation defense' (American spelling).
- customer-market-intelligence-011: 'Pillar 3' is kept next to the neutral wording because it is a Basel term and the card's intent names it.
- Link labels respelled on this page: 'Behavioral segmentation' (273) and 'Acquisition channel prioritization' (839); the titles they point to on the sub-pages need the same spelling.
- Peer-Bank Competitive Intelligence depends on peers holding earnings calls; the condition is stated once in the intent (1471). Owner to confirm that peer earnings calls are a relevant source for the Bank's peer set, or the scenario should rest on published results and filings only.
- Voice-of-Customer / NPS Verbatim Synthesis: the dashboard is delivered for monthly CX review cycles (1411) while classification runs weekly (1435); kept as written, since the two cadences can coexist.
- Customer Health Score and Retention Prioritization: the solution has no reviewer who accepts the score; acceptance is measured by churn outcome and model accuracy (1771). Left as written.

## customer-market-intelligence/brand-reputation

- The card title 'Reputation Risk Composite Signal' is now 'Reputational Risk Composite Signal' (660); link labels that show this title need the same change.
- 'Reputational Risk Composite Automation' and 'Reputational Risk Composite Signal' describe nearly the same weekly composite score for the CRO and the quarterly board section; no fix entry separates them, so both are kept as written. Owner to decide whether one should be narrowed (for example, automation of the team inputs versus the driver decomposition).
- Named social platforms (Telegram, VKontakte, Instagram, Twitter/X) in the section introduction and the card 'Social and Media Brand Monitor' are replaced by 'messaging platforms, local social networks, and global platforms' (890, 960, 972), because they were stated as the channels of a named regional market. Owner to confirm, or restore the global platform names as examples.
- The statement that a rising product complaint volume, or complaint rate relative to book size, triggers conduct supervision (1666, 1736) is kept as common practice; it was asserted of named regulators without a source.

## customer-market-intelligence/customer-lifetime-value

- Acquisition Channel Mix Optimizer (784): the intent names "regulatory constraints" on the channel mix, while the problem, solution and OKR name only capacity and budget constraints. Left as written; the owner may wish to drop "regulatory" from the intent or name the constraint.
- CLV-Weighted Retention Prioritization (1476, 1512): the solution names the "save-program team" and the OKR the "retention team lead"; both kept as distinct roles. Confirm whether they are one team.

## customer-market-intelligence/customer-segmentation

- Behavioral Segment Refresh (396–476): "fortnightly" and "fortnights" kept. The word is British usage rather than a spelling; the American "biweekly" is ambiguous. Decide whether to write "every two weeks" across the catalog.
- Needs Segment Transaction Inference (1948): the intent says the segments serve "product and pricing prioritization", while the solution and OKR name product and marketing teams. Left as written; confirm whether pricing or marketing is meant.
- Segment-Product Eligibility Sync (584, 632): the comparison runs weekly, yet eligibility is said to be refreshed within 48 hours of a segment update. The figures are kept; they hold only if the weekly run follows the segment refresh directly.

## customer-market-intelligence/intelligence-cycles

- Telegram channels are kept as a named source throughout the page (keys 2184, 2196, 1952, 2336, 2356, 2380, and stage s63 in part 2), as fix 163 itself proposes; the owner may prefer a platform-neutral term such as "messaging-app channels".
- Segmentation Cycle Retrospective: Adoption counts retrospectives produced within 30 days of cycle close (472) while Cycle targets completion within 5 days of cycle close (496). Figures left unchanged; the owner should confirm which one holds.
- Retention Intervention Personalization: Acceptance (1352) is an outcome measure (save rate ≥15% above baseline), not a reviewer acceptance rate; left as it is because the card names no reviewer rate.

## customer-market-intelligence/market-share-positioning

- Fix 117 proposed naming the Kyrgyz Republic and the NBKR as the data source; written in the neutral form ("the regulator") as the rules require (key 114).
- Fix 130 changes the card title to "Segment Share Gap-to-Target Analysis" (key 1164); link labels pointing to this card on other pages must follow in the separate label step.
- Competitor Move Intelligence Brief: the objective named "strategy and commercial leadership" as recipient while intent and solution name strategy leadership only; the objective (1488) was aligned to strategy leadership. The owner may prefer to add commercial leadership to the card instead.
- Segment Share Monitoring Report and Segment Share Estimation Model describe closely related quarterly outputs from the same inputs; no fix entry covers them and both were kept as they are.

## customer-market-intelligence/retention-churn

- Role names merged on the page: "programme team" → "save-program team" (Intervention Efficacy Trend Report, Intervention ROI by Cohort); "retention lead" → "retention team lead" (Save-Program Efficacy Report, including the wording of fix 071). The owner should confirm that these denote the same roles at the Bank.
- Save-Program Cohort Brief: the solution names the save-program team while the OKR named the retention team and the retention team lead; the objective (712) now names the save-program team and the solution (700) has the team review the brief with the retention team lead. The owner may prefer a single owner for this card.
- Fix 068 proposed "a threshold calibrated on the retail base"; written as "calibrated on the full active base" to match the card's problem (key 972).
- Four card titles changed (272 by fix 061; 544, 660, 1320 respelled "Save-Program"); link labels on other pages must follow in the separate label step.

## customer-market-intelligence/wallet-share

- The 40% wallet figure in the page introduction (94) and the 'three to five times' revenue-potential figure (114) are kept as general patterns; neither has a stated source.

## finance-treasury

- Fix finance-treasury-090 proposed the sub-group label 'Basel, COREP & FINREP' (862); COREP and FINREP are EU reporting regimes, so the label is written 'Basel & supervisory reporting'. Confirm the label.
- Link labels 898 'NBKR / NBK / CBR prudential returns' and 868 'COREP & FINREP data quality validation' are left as they are: they follow the section titles of the Regulatory financial reporting page and must be brought in step once those titles are reworded.
- Link label 729 is changed to 'Lending portfolio attribution & IFRS 9 provisioning' (fix finance-treasury-093); the section title on the Performance measurement page must match it.
- Page introduction (84): 'each sub-concern carries formal reporting obligations' is softened to 'most of these sub-concerns', since FP&A and performance measurement have no supervisory submissions. Confirm.

## finance-treasury/alm

- FTP-Driven Product Pricing Signals, OKR cycle (438): the draft measured from a 'monthly FTP curve update' and compared with a 'quarterly ALCO cycle', while the page has ALCO meeting monthly and the FTP curve reviewed quarterly. Reworded to a monthly signal measured from the month's product margin data, against the quarterly ALCO review of the FTP curve. Confirm the intended trigger.
- 'ALM desk' (IRRBB Early Warning Signal), 'ALM officer' (ALCO Rate-Scenario Pack, OKR cycle) and bare 'ALM' (Hedge Portfolio Effectiveness Review) were written as 'the ALM team', the name used on the rest of the page. Restore if a separate desk or officer role is intended.
- IRRBB Early Warning Signal, intent (1134): 'in real time' replaced with 'each business day' to agree with the daily feeds in the solution and the 1-business-day cycle target.
- 'AOCI' (1134, 1166) is a US GAAP term; under IFRS the equivalent is the OCI reserve. Kept as written; decide whether to rename across the catalog.
- Fix 102 changes the card title to 'IRRBB Limit Utilization Report' (American spelling); the urn keeps 'utilisation-dashboard'.

## finance-treasury/capital-management

- Problems row 'Automation' (156): the draft put ICAAP sections, capital ratio walk reports for ALCO and board capital plan summaries all 'on an annual or semi-annual cycle', while the page reports the capital position to ALCO monthly. Reworded to 'in every reporting cycle'. Confirm.
- RWA Movement Attribution (506): the driver 'model changes' presumes internal models; the condition '(where the Bank uses internal models)' was added in the solution only. 'Model parameter changes' and 'rating migrations' in the intent and problem are left as written; decide whether the card should be restated for a standardized-approach bank.
- ICAAP Narrative Drafting, OKR adoption (1306): 'across NBKR, NBK/ARDFM, or CBR perimeters as applicable' was dropped without a multi-jurisdiction replacement.
- 'Pillar 2 guidance' (580, 862, 906, 1554) is kept; as a separate supervisory instrument (P2G) it belongs to the EU/UK framework. 'AOCI' (192, 262, 274, 390, 414) is a US GAAP term. Decide whether to neutralize both across the catalog.
- Supervisory Observation Tracker: the intent and objective categorize the register 'by topic, due date, and closure status', the solution and adoption 'by risk type and regulatory framework'. Left as written (read as compatible); align if one scheme is intended.
- Fix 110 card title respelled to 'Dividend Policy Scenario Modeling'; the urn keeps 'modelling'.

## finance-treasury/finance-cycles

- Fixes 141, 143, 145, 146: BCBS 368 'Principle 4' changed to 'Principle 5' as proposed. The fix note asks for a check against the standard; the published text was not available in this run, so confirm that Principle 5 is the one on behavioral and modeling assumptions.
- Fix 151 (order of countries and regulators, 1652): the sentence no longer names countries or regulators, so the ordering problem is gone; reported as applied.
- Fix 152 (2424): 'Under IFRS as adopted in Kazakhstan, Kyrgyzstan, and Russia' became 'Under IFRS'; the sentence now presumes the Bank's statutory accounts are prepared under IFRS.
- Intra-Quarter NIM and FTP Signal Monitoring, solution (340): the brief's recipient 'the Treasurer and FP&A' written as 'Treasury and FP&A', the name used in the intent and the three OKR lines. Restore if the Treasurer in person is the intended recipient.
- Daily LCR/NSFR Submission Exception Commentary (1828–1908) presumes a daily LCR/NSFR return to the regulator with exception commentary in a prescribed format. Kept as written; the scenario applies only where the regulator requires a daily return.
- Card title 'BCBS 368 Behavioural Assumption Backtesting' respelled 'Behavioral' (1524) and 'Rolling Reforecast Model Compression' retitled per fix 138 (764); the urns keep the original words.
- Regulatory Reporting Quality Trend Analytics (3476–3532) and Supervisory Query Response Knowledge Base (3824–3868): breakdowns 'by supervisor' and 'three supervisor perimeters' were removed, so both cards now read for a single regulator. Add 'where the Bank operates in more than one jurisdiction' if a per-supervisor breakdown should stay.
- Regulatory Validation Exception Triage, OKR cycle (3672): '1–3 days of manual investigation start' was unclear; reworded as manual investigation starting 1–3 days later, by analogy with the close triage card (2912). Confirm that the 1–3 days is the wait before investigation, not its duration.
- Fix 154 (3360) and the solution (3392): 'COREP/FINREP reconciliation' written as reconciliation of the returns, and 'COREP capital figures' as the capital figures in the return; the page names COREP and FINREP once, as an example, in the regulatory reporting cycle description.

## finance-treasury/fpa

- 'Investor calls' (section 'CFO & ALCO Q&A support', 1356, and CFO Scenario Sandbox, 1426) were given the condition 'where the Bank holds them', by analogy with analyst earnings calls in the rules; the scanner does not check this phrase. Drop the condition if investor calls are to be treated as common to every bank.
- Fix 098 lengthens the section introduction (1356) by about 60%, as proposed.
- 'the consolidated bank' (580, 746, 790) written as 'the Bank as a whole'.

## finance-treasury/liquidity-management

- ILAAP is kept as the name of the Bank's internal liquidity adequacy assessment in three cards (894/918, 1250–1306); it is a term of some supervisory regimes rather than a Basel text. Decide whether to keep the abbreviation or write it out as a neutral phrase.
- Page problem statement 156 says the daily report assembly takes two to three hours before the Treasurer's review window opens; the card Daily LCR / NSFR Monitoring & Commentary (322) measures the report as arriving 1–2 hours post-open. Different measures, left as they are; align if one figure is intended.
- CFP Stress Analysis (778): the OKR names the Treasurer as approver of the narrative while the solution named only ALCO; the Treasurer's check was carried into the solution ahead of the ALCO review. Confirm that order of review.

## finance-treasury/performance-measurement

- "Basel II Pillar 2 and regional ICAAP guidance" is written "Pillar 2 of the Basel framework and supervisory ICAAP guidance" (94, 580), following fixes 119 and 120.
- Provision Sensitivity Scenario Analysis uses the scenario set base, adverse, severe (1522); Lending Portfolio Performance Attribution uses base, stress, severe (1438), now stated the same way in its intent and objective. Decide whether the two cards should name one scenario set.
- Lending Portfolio Performance Attribution (1474) mentions a "provision committee" that no other line of the page names; left as it is.
- RAROC & EVA Attribution by BU (778): the OKR names Finance and Risk as the reviewers; their review was carried into the solution. Confirm.

## finance-treasury/regulatory-financial-reporting

- Fix finance-treasury-126 proposed the tab label 'Basel, COREP & FINREP' (112). COREP and FINREP are EU reporting regimes, so the label is written 'Basel & supervisory reporting', the same wording the area page uses for this sub-group. Confirm the label.
- Titles that named EU reporting regimes or national regulators are reworded to the subject, and link labels on the area page and overview must follow: section 188 'COREP & FINREP data quality validation' → 'Supervisory template data quality validation'; section 576 'NBKR / NBK / CBR prudential returns' → 'Local prudential returns'; card 234 'COREP & FINREP Movement Commentary' → 'Supervisory Template Movement Commentary'; card 350 'COREP & FINREP Submission Readiness Check' → 'Supervisory Template Submission Readiness Check'; card 466 'COREP / FINREP Data Quality Validation' → 'Supervisory Template Data Quality Validation'. Decide whether the three card titles should keep 'COREP & FINREP' instead.
- The first section now depends on a condition stated in its introduction (192): the regulator prescribes a standardized template framework, with COREP and FINREP kept once per field as an example (94, 132, 192, 242, 358, 474). Its three cards and the three cards of 'Local prudential returns' describe parallel scenarios (movement commentary, readiness or calendar, data validation); they stay distinct only by the kind of return. Decide whether both sections are wanted for a bank with a single regulator.
- Regulatory Submission Narrative & Investor Disclosure Drafting (1250–1330) and the section 'Investor disclosure & statutory accounts' presuppose a bank with public investors (quarterly earnings releases, MD&A, investor letters); no condition was added. 'MD&A' is a US filing term kept as written. Decide whether to state the condition or rename MD&A to management commentary.
- Page statement 168 asserted that four named supervisors each increased reporting granularity and frequency over the past five years; written as a general pattern without the five-year figure.

## finance-treasury/tax-management

- The page is written for a group with entities in several tax jurisdictions (Group Tax, ETR by jurisdiction, jurisdiction concentration, intra-group transfer pricing, local files per entity). The condition 'where the Bank operates in more than one jurisdiction' is stated once in the page introduction (94); the cards keep 'by jurisdiction' and 'each jurisdiction' as neutral wording. Decide whether the transfer pricing section should also open with a condition (a bank with intra-group transactions).
- FATCA is kept with its US name and 'US-connected customers', 'US indicia' (1356, 1658): the US act is the subject of the scenarios, not a regime applied to the Bank by mistake.
- Section introduction 1356 said that two named countries are CRS signatories; written as 'CRS applies in jurisdictions that have adopted the standard'.
- FATCA & CRS XML Submission Validation (1398) and FATCA / CRS Reporting Quality Check (1514) overlap on XML schema checks before submission and name different recipients (Group Tax; Tax Operations). No fix entry covers them; both left distinct as written. Decide whether to sharpen the difference.
- Effective Tax Rate Reconciliation (426): Acceptance has the audit committee confirm the flagged disclosure items, while the solution names only Group Tax as reviewer. Left as written; confirm who confirms.

## risk-control

- Line 559, the link label "Model validation cycle (SR 11-7)", names a US supervisory letter. It is a navigation label and was left unchanged; it should follow the title of the model validation cycle on the Risk Cycles page once that title is reworded.

## risk-control/climate-esg-risk

- The EU taxonomy is kept once as an example ("such as the EU taxonomy") in the section introduction 580 and in the problem 998; elsewhere it is written as "external taxonomy" or "taxonomy-based".
- Card Green Finance Pipeline Screening (978): green bond issuance is a practice only some banks have, so the intent now carries the condition "where the Bank issues green bonds". Green bonds are not in the rules' list of scale-dependent practices; confirm that the condition is wanted.
- Card Transition Risk & Carbon Exposure Analysis: following fix 058 the card consumes financed emissions and no longer computes them, so the adoption line 1306 now measures the financed-emission narrative, not financed emission calculations; the intent 1250 was aligned to the solution and objective (narrative for ICAAP and TCFD disclosure, where it said ICAAP and supervisory stress tests).
- The page names a sustainability team, a climate risk team and (in one card, 1282 and 1294) "ESG teams". They were kept as distinct units; if the ESG team is the sustainability team, the two lines should be renamed.
- Fix 056 asked the owner to confirm the regulator's position on mandatory TCFD disclosure; the neutral wording ("in a growing number of jurisdictions") no longer depends on it.

## risk-control/compliance-financial-crime

- Fix 018 proposed "AML/CFT compliance officer" for "BSA officer"; the rules (section 3) give "the AML compliance officer", which is used in all 22 lines of the three SAR cards. Confirm the role name.
- Fix 005 proposed naming the Kyrgyz financial intelligence unit and Kyrgyz terminology; written in the neutral form ("the financial intelligence unit", "a suspicious transaction report in some jurisdictions") as the rules require.
- Fixes 010–012 proposed "EAG" (the regional FATF-style body for the Bank's region); written as "the regional FATF-style body" to avoid a regional specific. Confirm whether the body may be named.
- The page names both the CCO and the Head of Compliance (complaint cards 1522–1718). They were kept as distinct roles; if they are the same person at the Bank, one name should be chosen.
- Card License Renewal Pack Assembly: after fixes 001–003 the card speaks of renewals and re-confirmations of the Bank's licenses, permits and approvals; the OKR lines 802 and 826 now say "renewal cycle" where they said "renewal season" (a term of the removed US state-license framing).
- Section introduction 1744 keeps one foreign list as an example ("such as the OFAC SDN list"); section introduction 2132 keeps "such as CAMELS" as an example of a supervisory rating framework. Confirm or drop.

## risk-control/credit-risk

- The page gives two large-exposure levels: 10% of Tier 1 capital for enhanced reporting (section 'Counterparty exposure analytics', key 192) and 25% for supervisory notification (section 'Concentration & sector risk', key 580). Both are now worded as common practice and the breach-notification card names the limit without a figure; the owner may wish to confirm the two levels.

## risk-control/cyber-risk

- Fix risk-control-1-122 proposed CERT-KG; under the rule against Kyrgyz specifics the line (key 192) now reads 'the national CERT'.
- Two card titles named DORA as the Bank's regime and were changed without a fix entry: 'DORA Incident Notification Draft' → 'Major ICT Incident Notification Draft' (key 738) and 'DORA TLPT Preparation Support' → 'TLPT Preparation Support' (key 1514). Owner to confirm the titles; link labels on other pages must follow.
- DORA is kept once as an example ('such as DORA') in keys 94, 580, 766 and 1356; elsewhere it is replaced by 'regulatory notification', 'operational-resilience requirements' or 'the prescribed format'. The 4-hour and 72-hour notification levels and the three-year TLPT cadence are now stated as common practice.
- The SWIFT program is written 'Customer Security Program (CSP)' for American spelling (key 94); its official name is spelled 'Programme'. Owner to decide whether the proper name keeps its spelling.

## risk-control/internal-audit

- Fix risk-control-2-042 retitles the card 'Mid-Year Audit Universe Re-Ranking' (key 466); the review left open whether the card should instead become quarterly or event-driven. The body still describes one re-ranking at mid-year.

## risk-control/liquidity-risk

- ILAAP is an EU supervisory term used throughout the page as the Bank's own process; it was kept as written. Decide whether a neutral name (internal liquidity adequacy assessment) should replace it.
- Problems row 132 said both ratios are calculated daily; aligned with the page (LCR daily, NSFR monthly).

## risk-control/market-risk

- Fix risk-control-1-056 proposed 'KGS'; written as 'the local currency', as the rules require.
- The whole page depends on a trading book, and four cards (VaR Model Backtesting Pack, Stressed VaR Scenario Narrative, Backtesting Exception Documentation Pack, and the IMA sentences of two section introductions) on internal models. Each card intent and each section introduction now opens with the condition. Decide whether twelve conditioned intents on one page read acceptably or whether the condition should be stated only at page and section level.
- Limits Framework Calibration Review Support names no person who conducts the annual limits review; the solution now says the review decides on flagged limits, but the owner of that review remains unnamed.

## risk-control/model-risk

- SR 11-7 is kept once, in the page introduction (94), as an example: 'model-risk guidance such as SR 11-7'. Everywhere else it is 'model-risk guidance'. Decide whether the one example should stay.
- Shadow Model Identification Scan (474, 506) applied 'the SR 11-7 model definition'; now 'the model definition in model-risk guidance'. If the Bank's MRM policy holds its own model definition, that would be the more exact reference.
- Model Performance Monthly Dashboard: after fix risk-control-1-111 the problem speaks of a monthly reporting cycle, while intent, solution and OKR still place the monthly dashboard in 'the committee pack'; the Model Risk Committee is quarterly elsewhere on the page. Decide which pack the monthly dashboard goes into.
- Model Validation Finding Synthesis and Model Risk Portfolio Reporting both cluster validation findings for systemic patterns (annual review versus quarterly committee pack); no fix entry covers the overlap and both were left as they are.

## risk-control/operational-risk

- DORA is kept as an example ('operational-resilience requirements such as DORA') once each in the page introduction (94), the TPRM section introduction (580) and the intent of the card 'DORA Third-Party Register Extraction' (746), whose title stays. Decide whether that card title should be renamed to a neutral one (for example 'ICT Third-Party Register Extraction'); the title also appears as a link label on other pages.
- The Advanced Measurement Approach is a Basel II approach that Basel III replaced with the standardized approach. The page introduction, the loss-events section introduction and the card 'Operational Loss Event Data Quality Check' now state it as a condition ('where a bank uses …'). The quality check is useful for any loss database; decide whether that card should drop the AMA framing altogether.
- DORA Third-Party Register Extraction named the reviewer 'the risk team' in the solution and acceptance and 'the TPRM team' in the objective; written as 'the TPRM team' throughout.
- 1356: 'test these against defined scenarios at least annually' was stated as a rule; now 'typically at least annually'.

## risk-control/risk-cycles

- Flow title changed without a fix entry: "Model validation cycle (SR 11-7)" → "Model validation cycle (model risk management)" (key 3138), because the title named a US supervisory letter as the cycle's framework. SR 11-7 is kept once as an example ("such as SR 11-7") in the flow's short and full intent (keys 3144, 3152). Confirm the new title; link labels that show it must follow.
- Card title changed by fix risk-control-2-117 (key 1276) and respelled to American spelling (key 2040, "Utilization"): link labels on other pages must follow.
- SREP (an EU term) is written "supervisory review cycles" throughout the stress-testing cards; ICAAP and ILAAP are kept as Basel Pillar 2 terms. Confirm if the Bank's supervisor uses a different name for these documents.
- TCFD/NGFS mix-up (fixes 109, 110) also corrected in the cards and problem rows of the same cycle where NGFS scenarios were called TCFD scenarios or pathways (keys 876, 912, 1052, 1432).
- Fix risk-control-2-099 is listed with part 1, but its line (RCSA cycle, Document stage, problem) is key s15 of this part; it is applied here.
- Card title respelled to American spelling (key 3660, "Re-Prioritization"): link labels on other pages must follow.
- SR 11-7 is removed from every card of the model validation cycle and written as "model-risk guidance" or "the validation framework"; the cycle's own intent (part 1) keeps it once as an example. Confirm that no card needs to name it.
- Dynamic Soft-Breach Threshold Calibration: fix risk-control-2-107 names the Risk Strategy team as the approver of the recalibration bounds; the card did not name an approver before. Confirm the owner of these bounds.

## risk-control/strategic-reputational-risk

- Fix risk-control-2-074 proposed "digital som adoption impacts"; written in the neutral form "central bank digital currency adoption impacts" (key 132), as the rules forbid a Kyrgyz specific.
- Problem row "New business opportunities" (key 168) said "weekly scan"; changed to "monthly and quarterly scans" for the reason given in fix risk-control-2-073 (no card on the page runs weekly). Confirm the cadence.
- Executive Mention & Media Monitor: fixes 076 and 077 add an intraday alert for high-severity signals; the drafted OKR objective and cycle (keys 674, 710) were aligned to it. No alert latency target exists in the card; confirm whether one is wanted.
- ESG Rating Agency Signal Monitor: the card depends on the Bank holding ESG ratings, so its intent opens with "Where the Bank holds ESG ratings" (key 746). The agency names MSCI, Sustainalytics and ISS are kept as written; confirm whether commercial rating agencies should be named.
- Strategic-Decision Risk Analysis and Strategic Risk Appetite Alignment Check both give the CRO an AI-drafted assessment of a strategic proposal against risk appetite; no fix entry separates them and they are left as two cards (the first a four-part risk opinion for Board or EXCO, the second an RAF metric mapping for EXCO). Decide whether both stay.
- Role names merged on the page: "legal", "the legal function" and "legal teams" in Market Entry Regulatory Constraint Mapping are written "the legal team" in the solution and OKR (keys 506, 518, 542); the problem keeps "legal and compliance functions" as the units that do the mapping today.

## shared-banking-capabilities/advisory-research

- Owner decision: the whole page depends on practices only some banks have. The condition is written as 'a research desk' (research cards) and 'provides investment advice' (suitability and portfolio-review cards), once in the page header, each section introduction and each card; confirm this wording.
- Owner decision: cards 'Research Production Automation' (earnings-call section) and 'Research note data section drafting' describe the same drafting of data-driven research note sections; no fix entry directs how to differentiate them, so both were left with their scope.
- 'advisor' was merged into 'relationship manager' on this page (suitability cards and page header), since the page gives the suitability assessment to relationship managers.

## shared-banking-capabilities/capability-cycles

- Owner decision: card title 'KPI/SLA Scorecard Assembly Agent' named the AI as bare 'Agent'; written 'KPI/SLA Scorecard Assembly' (the alternative is 'KPI/SLA Scorecard Assembly AI Agent').
- Fixes 082–084 proposed NBKR-specific wording; written neutrally (outsourcing requirements, the regulator), with the EBA guidelines kept once in the cycle description as an example.

## shared-banking-capabilities/collections-recoveries

- The page names 'collections managers' and 'collections management' for the same reviewers; written 'collections managers' throughout (keys 426, 506, 542, 894). In the card 'Legal referral cost-recovery analytics' the triage criteria are adjusted by collections managers although triage itself is done by the recoveries team; kept as written — the owner may wish to name the recoveries lead instead.
- Card 'Write-off cohort recovery retrospective': the model risk committee, named only in the Acceptance line, is carried into the solution as the approver of assumption revisions (key 1438).
- Card 'Portfolio sale bid analysis': the intent said 'CFO and board approval' while the solution and OKR have the CFO and CRO review before board submission; intent aligned to 'CFO and CRO review and board approval' (key 1638).

## shared-banking-capabilities/credit-decisioning

- Card titles changed: 'Annual review portfolio scheduling optimisation' → '… optimization' (key 622, spelling) and 'Covenant compliance continuous monitoring' → 'Covenant compliance monitoring' (key 1514, fix shared-banking-capabilities-019); link labels on the area page and the overview that show these titles need the same text.
- Basel III IRB is kept as a reference with the condition 'where the Bank uses internal-ratings models' in the section introductions (keys 192, 968) and once in each dependent card (keys 378, 494, 1270). The scenarios themselves (scorecard drift, recalibration brief, override analytics) hold for any bank with a scorecard.
- Cards 'Underwriter override pattern analytics' and 'Covenant breach pattern analytics' named 'the credit risk team' in the intent and 'credit risk management' in the solution and OKR; written 'credit risk management' (keys 1250, 1638).
- The card title 'Adverse Action Notification Drafting' uses a US consumer-credit term ('adverse action'); kept, since titles are not changed — the owner may prefer 'Credit decline notification drafting'.

## shared-banking-capabilities/customer-onboarding

- Card titles changed: 'Welcome communication personalisation' → '… personalization' (key 622, spelling) and 'Early tenure product propensity scoring' → 'Early-tenure product propensity scoring' (key 1630, fix shared-banking-capabilities-057); link labels on the area page and the overview that show these titles need the same text.
- Fix shared-banking-capabilities-056: the proposed closing sentence repeated the clause before it ('enabling the RM to act within the high-engagement early-tenure window'); the two are written as one sentence, and 'RM' is spelled out in the solution (keys 1522, 1554).
- Cards 'Complex CDD Research Pack' (pack for the senior analyst's classification decision on complex cases) and 'Enhanced due diligence research pack' (pack for the compliance analyst's EDD review of customers already classified high-risk) assemble nearly the same pack from the same sources. Both are kept as written; the owner may wish to have them differentiated further or reviewed as a possible duplicate.
- The sanctions-list enumeration 'OFAC SDN, UN, EU, and HM Treasury' is written 'the UN and other applicable sanctions lists' (key 1744); the owner may prefer to keep the foreign lists as examples, since banks commonly screen against them.
- The cards write 'digital service channels', 'digital servicing channels' and 'digital channels' for the same recipients; written 'digital channels' (keys 1406, 1438, 1670).
- The 90–98% false-positive rate for screening tools (keys 1744, 1794, 1814) is kept as a general industry figure; it has no source in the card.

## shared-banking-capabilities/financial-crime

- FATF Recommendation 10 (customer due diligence) is kept as a reference for the alert-review obligation and for investigation documentation (keys 192, 378, 580, 882); Compliance may wish to confirm it is the right Recommendation or generalize to 'the FATF Recommendations'.
- The SAR filing deadline is stated without a number of days (keys 1356, 1542), as the fix entries direct; the local deadline can be added on the landing page if the owner wishes.

## shared-banking-capabilities/transaction-processing

- Acceptance lines 310, 542, 930, 1086, 1474 and 1706 measure a downstream outcome (STP rate, exception volume, resolution time) rather than how often the reviewer accepts the output; left as drafted because no acceptance figure exists in the card to restate.

## strategic-initiatives

- Card regulatory-change-impact-assessment: the Cycle line (1516) says 80–100 combined person-hours, while the problem (1456) can be read as 110–150 (30–50 hours each for the CCO and the General Counsel plus 50 across business lines). Figure kept; the owner should confirm which reading is meant.
- Card earnings-call-qa-prep depends on analyst earnings calls; the condition is stated once, in the intent (1668). The fix 005 wording was shortened to keep the six components of the original solution within the length limit.
- Sub-group labels without a fix entry ("Program planning", "Partner sourcing", "Partner performance", "Ecosystem positioning", "Platform monetization") were left as they are; they may have lost an "&" in the same way as the seven corrected labels.

## strategic-initiatives/change-cycles

- EU CSRD is kept once in the ESG reporting cycle long intent (2340) as a "such as" example of sustainability-reporting rules that reach banks with foreign subsidiaries or investors; drop it if no foreign regime should be named.
- "relationship manager(s)" in the Partnership lifecycle problem rows (808, 820) was merged into "partnership manager(s)", the role name used by the cards of that cycle.
- Card innovation-experiment-knowledge-base: the solution named no human part; the innovation leads' check of relevance and tagging was carried in from the Acceptance line (2252). Card program-benefits-realization-assessment: program directors' review carried into the solution from the Acceptance line (1500).
- Card esg-regulatory-standard-monitoring: the Adoption line (2680) counted "all six regulatory and standard-setting sources" (three named regulators plus ISSB, TCFD, GRI). With the regulators reduced to "the regulator" the count no longer holds, so it now reads "all regulatory and standard-setting sources in scope"; the owner may prefer to state a number.

## strategic-initiatives/ecosystem-platform-strategy

- Fix 044 proposed naming Kyrgyzstan (NBKR), Kazakhstan (ARDFM/NBK) and Russia (CBR); written neutrally as 'Where the regulator has introduced an open-banking framework', as the rules require.
- Condition for the scale-dependent practice: the sections and cards on API integration, revenue and margin, network economics and partner governance now open with 'Where the Bank operates an open-banking API platform' (or 'integrates with third parties through open-banking APIs'). The Ecosystem mapping cards and the peer positioning and options analysis cards carry no condition: they describe market monitoring and a role decision that any bank can make. Confirm this split.
- 'platform commercial team' (Network Participant Acquisition Economics Brief) and bare 'commercial team' (take-rate and benchmarking problems) were written as 'commercial platform team', the name used on the rest of the page; 'compliance team' in Ecosystem Compliance Monitoring was written as 'platform compliance team'. Restore if separate teams are intended.
- Ecosystem Competitive Threat Scoring: the brief is quarterly but the solution had the board review it only at the annual strategy review. Reworded so that the CSO reviews each quarterly brief and the board takes the latest one into the annual strategy review. Confirm the intended board cadence.
- Platform Revenue Model Insights Brief, intent (1444): 'before the annual investment review' changed to 'before the annual revenue model design discussion' to agree with the solution and the OKR cycle.
- Ecosystem Compliance Monitoring, OKR acceptance (2288): '≥85% of flags confirmed as genuine' and 'false-positive rate ≤10%' do not agree arithmetically (85% confirmed allows up to 15% false positives). Figures kept as written; decide which target holds.
- Titles respelled to American spelling: 'API Integration Portfolio Prioritization Brief' (660), 'Network Take-Rate Optimization Brief' (1708), 'Partner Ecosystem Onboarding Optimization Brief' (2096); urns keep the original spelling.

## strategic-initiatives/esg-commitments

- 'sustainability team' was written as 'sustainability function' throughout the page (both names were used for the same role, often inside one card), and 'compliance and sustainability teams' as 'the sustainability and compliance functions'. Restore if a separate team is intended.
- Section 'TCFD/ISSB disclosure' (114): 'TCFD disclosure requires scenario analysis under at least two climate pathways (1.5°C and 2°C+)' was written as common practice ('typically includes'); the TCFD recommendations ask for scenario analysis including a 2°C or lower scenario, not these two pathways by name.
- Section 'Regulatory ESG filings' (2054): mandatory ESG filings exist only where the regulator requires them, so the introduction now says 'to the regulator, where it requires them'. The cards of the section keep 'mandatory' without a further condition. Confirm.
- Sustainability Target Gap Brief (1832, 1876): 'real-time accountability' changed to 'monthly accountability', and 'within the reporting cycle' to 'within the month', to agree with the monthly brief.
- ESG KPI Business Line Accountability Brief (1360): the solution had the brief distributed 'at' the monthly business review and the intent 'before' it; both now say 'before'.
- Transition Plan Portfolio Pathway Brief: the OKR acceptance names the credit risk committee as confirming deviation flags, while the intent and solution name only the board and sustainability function. Left as written; decide whether the credit risk committee belongs in the solution.
- Scope 3 Counterparty Data Collection Brief, OKR cycle (1020): 'Tier 1 vs Tier 3 data' does not match PCAF, which scores data quality 1 to 5. Left as written; decide the measure.
- The page uses 'CSO' without expansion; on the Ecosystem page of the same area it reads as the strategy officer, here as the sustainability officer. Left as written.
- 'Compliance and sustainability teams', 'Compliance and the sustainability function' and 'compliance team' were written as 'the sustainability and compliance functions' / 'compliance function', the names used in the section introduction and the Filing Calendar card. Restore if separate teams are intended.
- Regulatory ESG Filing Quality Gate: the problem names 'the sustainability function and legal' as today's reviewers, while the intent and solution give the review to compliance and sustainability. Left as written (the problem describes the current state); confirm whether legal has a part in the new process.

## strategic-initiatives/innovation-portfolio

- Two cards in "MVP design & hypothesis testing" describe nearly the same scenario and no fix entry directs how to tell them apart: "Hypothesis Design Review" (Enablement; rubric review with recommendations to innovation leads, confirmed by experienced innovation leads) and "Hypothesis Design Quality Review" (Insights; quality brief against the Bank's experiment design framework for experiment sponsors and the innovation function). Both are kept as written; decide whether one should be refocused.
- The card "Innovation Portfolio Health Brief" abbreviates Chief Innovation Officer as "CIO", which usually reads as Chief Information Officer; the abbreviation is now introduced in the intent (key 1444) and kept. Confirm, or spell the role out throughout.
- "MVP Test Results Interpretation Brief" (key 1748) has the sponsor present to "the gate committee", while every other card names "the innovation board" as the body that holds the gate review; left as written because the text does not show that they are the same body.

## strategic-initiatives/ma

- The abbreviation "CSO" in the card "Target Screening Brief" (keys 396, 428) is not expanded anywhere on the page; other pages of the catalog use "CSO" beside the CRO for sustainability disclosure. Left as written; confirm that Chief Strategy Officer is meant and whether to spell it out.
- "Post-Merger Investor Integration Disclosure Pack": earnings calls are a practice of only some banks; the condition "where the Bank holds them" is stated once, in the problem (key 2124), and the Adoption line (key 2160) keeps "earnings calls and investor events" as written.

## strategic-initiatives/strategic-partnerships

- Card partnership-compliance-monitoring-brief: the intent and Adoption give a monthly brief, while the Cycle target is awareness within ≤5 business days of a regulatory change. The solution (1980) now says the AI agent flags a change when it is identified and maps it in the monthly brief; confirm that an alert between monthly briefs is intended, or change the Cycle target.
- The term sheet drafting card (940, 972, 984) no longer names open banking: its knowledge base is stated as 'applicable regulatory requirements'. Open banking is kept, with its condition, in the section introductions and the compliance review and monitoring cards.

## strategic-portfolio

- Title 2577 changed by fix strategic-portfolio-011 to 'Defensible positioning scan'; link labels that show the old title on other pages need the same text.
- Objectives 1817, 2513 and 2629 said 'continuously' while Adoption and Cycle of the same cards give a monthly check or scan; the objectives now say 'monthly'. Confirm monthly is the intended cadence.
- Cards 'Rating-agency relationship briefings' and 'Equity story / investor-day pack assembly' assume a rated bank with outside investors; no condition was added because these are not on the rules' list of scale-dependent practices. Decide whether they need one.
- Card 'CEO/CFO portfolio-modeling sandbox' (1689) describes a self-service sandbox and never names the AI agent; left as written, since naming the AI agent's part would add a claim.

## strategic-portfolio/capital-allocation

- Cadence of business-line capital allocation differs between two cards of one section: 'refreshed quarterly' (746, BU capital reallocation scenario engine) and 'set annually' (882 and problems row 168, Dynamic capital reallocation). Both left as written; the owner may want one base cadence.
- SIFI surcharge is treated as a scale-dependent practice: the condition is stated in the section introduction (already 'where applicable') and once in card 2182; the cards 'Buffer requirement change briefing' and its OKR keep the term without a condition.
- Card titles on this page mix sentence case and title case ('Tier 1 Ratio Variance Attribution', 'RAROC Narrative per Business Line', 'Dynamic Capital Reallocation Across Business Lines'); left unchanged because titles are changed only for spelling.

## strategic-portfolio/geographic-footprint

- Cross-border corridor economics monitor (1017–1097) is restated for a bank in its domestic market: corridors the Bank serves (remittances, trade finance, correspondent relationships) rather than an international presence; 'international strategy team' became 'strategy team', the name the card's problem already uses.
- Cross-border market entry scenario (1249) opens with 'Where the Bank operates in more than one jurisdiction or plans to', because the card is about entering a first or further market; the owner may prefer the plain condition.
- Digital-Bank License Window Monitoring (1405) now opens with the condition 'Where the regulator issues digital-bank licenses'; the scenario depends on such a licensing regime existing in the Bank's market.
- Two cards of the Branch network density section cover branch rationalization scenarios ('Branch density rationalization scenario' for the distribution committee, 'Branch Rationalization Scenario Modeling' for the network strategy team); no fix entry directs how to separate them, so each keeps its own recipient and cadence.
- Expansion market attractiveness insights: the intent said 'continuously updated' while the solution and OKR say quarterly; the intent (1909) now says 'updated quarterly'.

## strategic-portfolio/product-portfolio

- Insurance product regulatory compliance monitor: the Adoption measure counted 'active bancassurance jurisdictions'; stated for a bank in its domestic market it now counts insurance regulatory publications relevant to bancassurance (1693), with the 95% figure kept. The owner may prefer another unit of coverage.
- Lending product-mix what-if sandbox (473): Islamic-product variants now carry the condition 'where the Bank offers them'; the problem keeps 'murabaha structures' as an example.
- Titles changed by fix entries 110 and 120 (keys 465, 2405) and for American spelling (349, 1241): link labels on the area page and the overview need the same text.
- Cards portfolio economics insights: 'product management team' in Acceptance (1861) was aligned to 'product management committee', the recipient named in the intent; revert if the team is a distinct reviewer.

## strategic-portfolio/risk-appetite

- Three card titles keep the word 'continuous' (keys 350, 1786, 2174) although their cards refresh monthly; the card texts now say 'refreshed monthly'. Decide whether the titles should be reworded as well.
- The risk-appetite cards speak of an 'executive committee'; the steering-cycles page of the same area abbreviates it 'EC'. Left as written on each page.

## strategic-portfolio/steering-cycles

- SREP (the EU supervisory review and evaluation process) is written 'supervisory review' throughout the capital management cycle (keys 936, 1072, 1084, 1096, 1108, 1132, 1200); 'Pillar 2' and 'ICAAP' are kept as Basel terms.
- Capital deployment drift detection (keys 1688–1756): the intent and objective sent the drift brief to the ALCO while the solution sent it to the capital team. The solution now says the capital team confirms the signal and brings the brief to the ALCO. Confirm that this is the intended routing.
- The legal and investor-relations reviewers were named four ways on the page ('legal and IR review team', 'IR and legal review team', 'IR and legal team', 'IR and legal teams'); now 'IR and legal team' in both parts.
- Investor question and analyst theme intelligence (key 2888): earnings calls are stated with the condition 'where the Bank holds earnings calls'. If the Bank holds them as a matter of course, the condition can be dropped.
- Key 2924 measured 'theme coverage in agent-produced communications', although this card's AI agent produces an input, not the communications; reworded to 'the cycle's communications'.

## strategic-portfolio/strategic-priorities

- Innovation regulatory horizon scan: the intent named 'the strategy and technology leadership' as recipient while the solution and OKR name 'the innovation committee'; the intent (1522) now says 'the innovation committee'. Confirm the recipient.
- ESG Priority Progress Report: 'local central bank ESG guidance' (and 'local CB', fix 074) is written 'the regulator's ESG guidance' in 1794–1850, to match 'the regulator' used elsewhere on the page. Confirm if 'central bank' should be kept.

## strategic-portfolio/target-markets-segments

- Public sector tender opportunity detection: the adoption measure (2470) counted '≥90% of active jurisdictions'; with the multi-jurisdiction framing removed it now reads '≥90% of the government procurement portals in the Bank's market'. Confirm the measure base.
- Wealth client review advisory briefs: the solution (1554) says RMs review 'a ten-minute briefing' while the cycle target (1602) is '≤15 minutes of briefing review'. Compatible, but two figures; left as written. Decide whether to align.
- Public-Sector Banking Obligation Monitoring: the title (2174) keeps its hyphen while the section and the other texts on the page write 'public sector'; titles were not changed for hyphenation.
- Wealth management is treated as an ordinary segment (no condition added to its section or cards); only private banking carries the 'where the Bank has a private banking business' condition. Confirm if wealth management should carry one too.

## value-streams

- overview-value-streams-029 (owner question 9): "The cycle anchor is" is replaced by "The stream turns on" in all 11 stream summary lines (keys 176, 928, 1692, 2456, 3208, 3960, 4724, 5488, 6240, 6980, 7720). The five cross-cutting flows are titled "… Cycle" but their summaries now also say "The stream"; if the owner prefers to keep "cycle anchor", all 11 must be reverted together.
- overview-value-streams-081 (owner question 12): the Compliance stream description and its Automate row now say "STR" only, and the description introduces it once as "suspicious transaction report (STR)" (keys 6248, 6288); the same choice is applied to the cfc-* cards in part 3 and matches the stage texts in part 4.
- overview-value-streams-078 and -095: the stage buttons now read "Act" (6340) and "Close" (7820), matching the stage dialog labels changed in part 4.
- overview-value-streams-054: the bracket in the Treasury description is written as "the regulator (including liquidity returns under prudential standards such as the Basel III LCR and NSFR)"; the proposed "NBKR" is not inserted. Whether LCR/NSFR returns apply to the Bank is owner question 5.
- overview-value-streams-059: the sentence about three CIS markets is written as a general pattern, "In markets with currency controls, the cycle carries additional regulatory specificity…" (3968); "CIS-corridor payments" in the Optimize row became "cross-border payments" (3996).
- Wealth Management and Bancassurance are whole streams that only some banks run (advisory mandates, an investment committee, a partner insurer). No condition was added to their introductions, because neither is in the list of scale-dependent practices of the rules; the owner may want one opening clause in each stream description (1700, 2464).
- overview-value-streams-031: the card title is now "Dispute and investigation queue routing optimization" (692); link labels to this card on other pages must follow.
- The lens row 976 (Lending, Automate) now says "post-decision notification cascades", as the card corrected by fix 037 does; rows 1728 and the card 2248 spell out "investment committee pre-reads" where "IC" was not introduced.
- overview-value-streams-057: after the fix the AI agent takes the LCR and NSFR ratios from the approved regulatory calculation, yet the title (3724), the objective (3776) and the Adoption key result (3788) still say that it assembles the regulatory liquidity returns. Kept, because the title is not in the fix entry; the owner may want to limit the card to the ALCO pack and narrative.
- The FX cards on purpose codes and currency-control notifications (4128–4216, 4476–4564) presume a market with currency controls; the regulator is neutral and the condition is stated once, in the stream description (part 1, key 3968). The card on correspondent routing keeps "the payment factory" (4400), which not every bank runs.
- overview-value-streams-062: "CIS-corridor" is written "cross-border corridors" / "each corridor" in the routing card (4368, 4388, 4400, 4412, 4424).
- Card 4244 (corridor exception analytics): the intent and objective name "Operations and Treasury" as recipients, the solution and key results name "treasury operations" as the reviewer. Left as two names, since they may be two units.
- overview-value-streams-081 (owner question 12): the four cfc-* cards that named the report now say "STR" only, including the card title "Financial crime investigation pack and STR draft automation" (6744) and the compounds "STR-filing probability" and "high-STR-probability cases"; link labels to this card on other pages must follow.
- "MLRO" is written "the AML compliance officer" in the two AML cards (6552–6600, 6868–6936), as the rules direct.
- overview-value-streams-070 and -092: the card titles are now "Lifecycle task orchestration automation" (5136) and "Cross-business-line audit control learning propagation" (7600); link labels on other pages must follow.
- Card 5020 (onboarding sequencing): the solution and objective said the model retrains and optimizes "continuously", the Cycle key result commits to a weekly model refresh; both now say weekly (5060, 5072). Confirm weekly is the intended cadence.
- Card 6004 (stress-test enrichment): the Cycle key result spoke of a "risk-function-reviewed" narrative, but the solution gives the risk function no review step (it is only notified); the qualifier was removed from the key result (6092). If the risk function is meant to review each narrative, the solution should say so.
- Cards 6512 and 6860 (AML analytics and program health): "live view", "live data" and "live dashboard" were brought to the daily update that the solution and Adoption key result commit to (6520, 6900, 6936).
- Card 5368 (lifetime value): after fix 073 the card is monthly; the objective's "continuously updated" became "updated monthly" (5420) and the problem no longer says "in real time" (5396). "Lifecycle value view" was corrected to "lifetime value view" here and in the lens row of part 1 (4784).
- Card 8120 (close narrative) includes MD&A drafting, which presumes a bank that publishes one; no condition added, as it is not in the list of scale-dependent practices.
- overview-value-streams-081: the stage texts of the Compliance stream now say "STR" only (s178, s182, s183, s186, s187), as the fix proposes; this is owner question 12 (STR or SAR as the single name), and the cards and stream description of the same stream are in parts 1 and 3, so the choice must be the same there.
- overview-value-streams-078 and -095: the stage labels in the stage dialogs are now "Act" (s180) and "Close" (s212); the matching stage buttons (keys 6340 and 7820) are in part 1 and must carry the same labels.
- overview-value-streams-080: written as "the financial intelligence unit"; the proposed Kyrgyz body name is not inserted (rules, section 3).
- overview-value-streams-079: the stage title s181 ("Disposition — blocking, filing, and enhanced monitoring") still says "filing", while the intent now places drafting and approval here and filing in the Report stage; the title was not in the fix entry and is left for the owner.
- s106: the stage assumes LCR and NSFR liquidity returns; written as "the regulatory liquidity returns (such as the Basel LCR and NSFR)". s110, s111, s126, s127 assume currency-control reporting, which not every bank has; kept as written, with the regulator neutral.
- s119: "CIS-corridor payments — KG, KZ, RU" became "Payments in some regional corridors"; "the payment factory" is kept, though not every bank runs one.
