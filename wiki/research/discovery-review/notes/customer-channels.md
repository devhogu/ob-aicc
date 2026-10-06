# Customer & Channels — review notes

Reviewer id: `customer-channels`. Source: `html-alt/financial-services/en/customer-channels/` (8 pages). Fix map: `fixmap/customer-channels.jsonl` (128 entries).

## Summary

- Read 8 pages and all 97 cards: the area page (5 cards), six sub-area pages (75 cards) and Channel Cycles (17 cards), plus the page header intents, problem rows and the 20 stage dialogs, which are not in the extract and were read from the source HTML (see "About the extract" below).
- 61 of the 75 sub-area cards have an empty OKR (the OKR block is present in the HTML but has no objective and no key results). All 61 are drafted in the fix map. The 5 area-level cards and the 17 cycle cards are filled.
- Intent, problem and solution are present on every card; no card is truncated, no placeholder other than `service.eyebrow`, no duplicated URN or title. Every count shown on the area page matches the cards present.
- The text is written for a bank regulated in Kazakhstan, Kyrgyzstan and Russia at once. Beyond the measured NBKR/CBR pattern, this area names the National Bank of Kazakhstan (NBK) about 38 times and ARDFM 6 times, cites four specific regulatory acts by number, and has sentences and one whole card that only work for three jurisdictions.
- The contact center page uses "agent" for the human operator and "Agent" for the AI actor, sometimes in one sentence. This must be untangled before the global "Agent" → "AI agent" replacement.
- One real duplicate: "Branch Operations Intelligence" repeats "Branch Performance Pack Intelligence", and its OKR measures the other card's output.
- Group labels on the area page and tab labels on the sub-area pages are generated from slugs ("Rm productivity", "Open banking api governance"), and "Outbound multichannel" labels a group that contains nothing outbound.
- Eleven of the 36 filled OKRs do not agree with their own card (wrong durations, roles the card does not have, a metric the card never mentions); six of them are on the cycles page. The cycle cards are otherwise the best-written part of the area.
- Partner & API channels as a whole (open banking, third-party providers, a priced API catalogue) and parts of Relationship management (private banking, wealth) need the owner's decision on fit before polishing.

## How to read the fix map

- `current` is the exact string to find in the file (a label, a sentence, or a whole field); `proposed` replaces exactly that string. Where `current` is `S`, `M` or a lens name, it is the card's complexity or lens value.
- For `field: okr`, `proposed` is the complete OKR (objective, adoption, acceptance, cycle). For the 61 drafted OKRs `current` is empty. For corrections to an existing OKR, `current` holds the changed lines separated by " | " and the unchanged lines are repeated verbatim in `proposed`.
- Every `current` string was checked by script against the source HTML.
- Drafted OKRs say "the regulator" or "regulatory" and do not name NBKR, NBK or CBR, so the global regulator decision does not have to touch them. They keep "Agent" for the AI actor, as the filled cards do, and write "contact center agent" or "handling agent" for the human.
- Nine drafted Cycle key results carry a "before" figure that the card does not state (for example "30–45 minutes of manual end-of-day reconciliation"). They are illustrative in the same way as the filled cards; the cards are Vault Cash Reconciliation Automation, Schedule Efficiency Optimisation, Complaint Response Drafting, Complaint Pattern Intelligence, Client Relationship Continuity Brief, Post-Meeting CRM Update Automation, KYC Document Verification Automation, ATM Incident Response Automation and ATM Replenishment Logistics Briefing.

## Counts: overview page against the cards present

- The overview page (`en/index.html`) shows "Customer & Channels (80)" and six sub-areas: 12 + 15 + 12 + 12 + 12 + 12 = 75.
- Cards actually present in the area: 75 in the sub-areas, 5 on the area page itself, 17 on Channel Cycles — 97.
- The 80 is 75 + 5: the sub-area cards plus the five area-level cards. The 17 Channel Cycles cards are not counted and the cycles page is not listed on the overview at all.
- So a reader who adds the six numbers shown gets 75, sees 80, and finds 97 after opening the area. Nothing is wrong inside the area: every sub-area count, every section count "(3)" and the cycle counts (5, 4, 4, 4) match the cards.
- The same rule holds for all eight areas (for example Banking Data & Analytics shows 114 = 109 + 5 and has 20 more cycle cards), so this is one catalogue-wide decision, not a fix in this area. It is in "Questions for the owner".

## About the extract

- The extract files for this area do not contain the page header intent or, on the area page and the six sub-area pages, the problem rows. A script check shows the header intent is missing from the extract of all 76 pages of the catalogue and the problem rows from 48 pages. The stage dialog texts of the cycle pages (title, intent, problem per stage) are also missing; they live in a `FLOW_STAGES` object in the page script.
- For this area all of that was read from the source HTML. Reviewers of other areas who worked from the extract alone will not have seen these parts.
- The raw `<button class="flow-stages__stage" …>` text in the Channel Cycles extract is an artefact of the extraction. The page itself is correct.

## Special cases of the global patterns in this area

- NBK and ARDFM. The measured pattern covers CBR and NBKR. This area also cites NBK (about 38 times in the source, on every page) and ARDFM (6 times, area page and cycles). They need the same decision.
- Sentences that cite only foreign rules. Removing CBR and NBK leaves nothing behind in: the "Digital engagement & personalisation" section and the Consent Scope Enforcement card ("CBR and NBK data protection regulations", "GDPR-aligned consent framework") — fixes 084 and 085; the partner page ("CBR GOST R 57580" four times, "NBK open banking guidance", "PSD2-aligned") — fix 110 covers the header intent; the section-level and card-level mentions follow the global decision.
- Country names instead of acronyms. "Kazakhstan, Kyrgyzstan, and Russia" appears on five pages, "KZ, KG, and RU" and "the three jurisdictions" on the partner page, "CIS" five times (four on the cycles page). The global regulator fix will not catch these; the ones that state the bank's footprint are in the fix map (024, 077, 096, 110–114, 127, 128).
- Acts cited by number: NBKR Resolution No. 47/4 (complaint handling, 6 times), NBKR Resolution No. 50/4 (remote onboarding, 2), CBR Ordinance No. 59-I (6), CBR Ordinance No. 4243-U (2). None was verified. They are in the questions.
- Human "agent" and AI "Agent". On the contact center page lower-case "agent" is the human operator (agent population, agent desktop, handling agent) and capitalised sentence-initial "Agent" is the AI actor. Exceptions that break this rule: "Agent after-call work time" (human, capitalised), "the agent records the decision and outcome" (AI, lower case), and the section and card titles "Agent assist & guided resolution", "Agent Assist Effectiveness Intelligence", "Agent Real-Time Knowledge Assist" (human). Fixes 044–050 remove the collisions in running text; the three titles must be excluded from the global replacement.

## Area page — Customer & Channels (`customer-channels/index.html`)

What is on it: header intent, one problems tab ("Assisted channels", 4 rows), seven navigation cards with counts, 5 scenario cards (all with OKR).

1. Problem rows exist only for "Assisted channels". The other group, "Self-service & partner" (digital, ATMs, partner — half of the area), has no problem rows. Four rows are drafted in the fix map (008–011) from the sub-area pages' own rows. The same one-tab pattern exists in other areas, so applying them is the owner's call.
2. Group labels are generated from slugs: "Rm productivity", "Open banking api governance", "Network design operations", "Web mobile experience" (001–004).
3. "Outbound multichannel" labels the group that holds Contact center quality assurance and Workforce management. The area has no outbound or multichannel scenario (005). Two weaker mislabels: "Service evolution" holds ATM fraud detection (006); "Digital engagement operations" holds servicing and adoption tracking while "Digital engagement & personalisation" sits in the other group (007).
4. "Omnichannel Service-Recovery Orchestration" is rated S although it matches cases across every channel's records; the neighbouring complaint card that does the same matching is M (012).
5. The two cards above overlap: both detect that one customer raised one issue in several channels. They differ in output (resolution path against regulatory complaint record), so they can stay, but a reader will ask.
6. "Cross-Channel Segment Gap Intelligence" names "the CCO" in the intent and OKR; the abbreviation is not explained and appears nowhere else in the area. The solution names only the Head of Channels.
7. Problem rows use four lenses (Insights & analytics, Enablement, Automation, New business opportunities); cards use five (the same four plus Optimize). Three Optimize cards in the area have no problem row to answer.

## Physical branches (`physical-branches/index.html`)

What is on it: header intent, one problems tab (4 rows), 4 sections with intent, 12 cards (3 per section). OKR filled on 2, empty on 10 (drafted, 013–022).

1. "Branch Operations Intelligence" (Teller & frontline operations) duplicates "Branch Performance Pack Intelligence" (Branch performance reporting): both assemble the monthly branch performance pack for regional managers. Its OKR measures only the pack, and the Adoption line calls it a "cross-channel branch performance pack". The fix map narrows the card to the queue and staffing analysis that no other card owns (027–030). If the owner prefers to keep the card as it is, at least "cross-channel" must go.
2. "Vault Cash Reconciliation Automation" carries the lens Enablement; the title, the content and the page's own Automation problem row say Automation (031).
3. The header intent says branches are an anchor "in Kazakhstan, Kyrgyzstan, and Russia" (024); the regulatory notification card speaks of "the applicable jurisdiction" (025, 026).
4. The header intent promises "a weekly signal" for the Head of Branches; the network card that would deliver it is quarterly. Small, left as is.
5. The single problems tab is labelled "Network design operations" (slug label, 023) but its rows cover the whole page, including the second group "Branch performance". The same is true on every sub-area page: one tab, named after the first group, with rows about the whole sub-area.
6. Regulatory statements that carry weight in the cards and are not verified for the Kyrgyz Republic: a 30–90 day notification deadline for branch changes; "regulatory credit" for opening branches in underserved catchments (the Site Selection card builds a "financial inclusion credit assessment" on it); maximum queue times set by consumer protection guidance; daily reconciliation records under cash circulation regulations.

## Contact center (`contact-center/index.html`)

What is on it: header intent, one problems tab (4 rows), 5 sections with intent, 15 cards (3 per section). OKR filled on 3, empty on 12 (drafted, 032–043).

1. Human "agent" against AI "Agent" (see the special cases above). Six sentences are ambiguous or wrong as written (044–049), one more is missing an article (050).
2. "IVR Caller Experience Intelligence" lists "complaint-related calls" among friction signals; it is not one, and the solution lists session abandonment instead (051).
3. "Complaint Triage & Classification" promises all intake channels including branch in the intent and OKR; the solution lists three (052).
4. The page covers voice only. There is no scenario for chat, messengers, e-mail servicing or outbound campaigns, although the area page files two sections under "Outbound multichannel".
5. Complexity looks mechanical rather than assessed: "Post-Call Documentation Automation" is S, "Contact Center QA Intelligence" (scoring 100% of calls) and "Agent Real-Time Knowledge Assist" (listening to live calls) are M. All three need reliable call transcription, here in Kyrgyz and Russian. See the questions.
6. Lens choices that do not match the title or the work done: "IVR Caller Experience Intelligence" is Enablement but is an analysis brief like the Insights cards; "Complaint Response Drafting" is Enablement while the other drafting cards in the area ("Branch Regulatory Notification Drafting", "Incident Communication Drafting") are Automation. Left for the owner's lens rule.
7. The URN of "Complaint Pattern Intelligence" ends in `channel-complaint-pattern-intelligence`; harmless, no change proposed.

## Relationship management (`relationship-management/index.html`)

What is on it: header intent, one problems tab (4 rows), 4 sections with intent, 12 cards (3 per section). OKR filled on 3, empty on 9 (drafted, 053–061).

1. Tab label "Rm productivity" (062).
2. "Cross-Sell Opportunity Identification": the OKR says "RM team lead"; the page says "RM team head" 16 times (063).
3. "RM Meeting Brief": the Acceptance line tracks "NPS from RM-managed relationships", which the card never mentions (064).
4. "Client Lifecycle Event Monitoring" is rated S while joining four sources including public corporate event feeds (065).
5. Fit: the page is written for corporate, private banking and wealth segments ("private banking client with a maturing term deposit", "wealth-profile data", "public corporate filings", "public corporate event feeds"). Whether these segments and data sources exist for the Bank decides how much of the page stands.
6. Three cards rest on "NBK and NBKR supervisory guidance on relationship banking" that requires documented client contact at a frequency proportional to revenue tier. Not verified; if there is no such guidance, "Book Activity Log Automation" loses its stated reason.
7. The section "Client lifecycle stewardship" has the same name as its group on the area page (the same happens with "Partner network economics" on the partner page). Not wrong, but the area page shows the name twice in a row.
8. "Cross-Sell Conversion Intelligence": the intent names RM team head coaching preparation time as a primary metric, the solution names only conversion rate. The drafted OKR tracks both.

## Digital channels (`digital-channels/index.html`)

What is on it: header intent, one problems tab (4 rows), 4 sections with intent, 12 cards (3 per section). OKR filled on 2, empty on 10 (drafted, 066–075).

1. "KYC Document Verification Automation" contradicts itself: cases that pass the threshold "are flagged for expedited KYC review", and the next sentence measures "cases approved without manual intervention" (078, 079).
2. Data protection is said to be governed by "CBR and NBK data protection regulations and the bank's GDPR-aligned consent framework" — no Kyrgyz rule at all, in the section intent and in the Consent Scope Enforcement card (084, 085). The exact Kyrgyz law reference should come from Compliance.
3. "Digital Self-Service Task Automation" is rated S although it executes transactions against the core system inside the session (080). The card also does not say what the AI agent adds: balance enquiry, mini-statement and card freeze are ordinary app functions. It reads like a conversational assistant but never says so. See the questions.
4. "Consent scope boundary contacts" in the Personalisation Effectiveness card should be "events", as in its own solution (082, 083).
5. "Low-Adoption Customer Outreach Automation" has the Head of Digital personally review every outreach queue before dispatch; the comparable card on the same page ("Onboarding Abandonment Recovery") gives this to the digital operations team. The drafted OKR follows the card as written.
6. The Enablement problem row is about A/B testing and the experiment pipeline for product managers. No card answers it; the three Enablement cards are a recovery message, a daily support brief and a reporting pack. The Automation row names digital adoption reporting, which the page files under Enablement.
7. Not verified: digital adoption rate as a "supervisory interest metric", and "NBKR and NBK digital adoption reporting submissions" that the Reporting Pack card is partly built for.
8. Header intent: "in Kazakhstan, Kyrgyzstan, and Russia" (077); tab label "Web mobile experience" (076).

## ATMs & self-service (`atms-self-service/index.html`)

What is on it: header intent, one problems tab (4 rows), 4 sections with intent, 12 cards (3 per section). OKR filled on 2, empty on 10 (drafted, 086–095).

1. "ATM Fraud Pattern Detection": the OKR objective speaks of a "regulatory notification threshold" for customer losses, which the card does not have, and the Cycle line replaces "3–5 days of manual transaction clustering" that does not happen today — the card says patterns surface from customer fraud reports (097).
2. Header intent: "in Kazakhstan, Kyrgyzstan, and Russia, where cash usage remains significant by Central Asian and CIS standards" (096).
3. "ATM Demand Forecast Intelligence": "— signal for logistics reallocation decisions" lost its article (098).
4. Three cards draft a regulatory notification (outage, skimming incident, terminal configuration change). Whether NBKR requires such notifications, and within what time, is not verified. If it does not, part of each card falls away.
5. "ATM Cash Load Optimisation" and "ATM Demand Forecast Intelligence" both forecast per-machine demand (three-day horizon for load orders, weekly for routing). They mirror the two branch cash cards. Acceptable, but the pair could be one card.
6. "ATM Fraud Customer Alert Dispatch" is Enablement although it drafts and queues messages like the Automation cards. Left for the owner's lens rule.

## Partner & API channels (`partner-api-channels/index.html`)

What is on it: header intent, one problems tab (4 rows), 4 sections with intent, 12 cards (3 per section). OKR filled on 2, empty on 10 (drafted, 099–108).

1. Fit of the whole page. It assumes the bank runs an open banking API platform with authorised third-party providers, a priced API product catalogue, tiered billing and a partner network with contracted minimums. Whether the Bank has or plans this decides whether the page is kept, reduced or marked as future.
2. "API Catalogue Expansion Opportunities" is written for three jurisdictions ("KZ, KG, and RU open banking frameworks", "across the three jurisdictions") (112–114). The section intent says endpoints are mandated "in KZ and KG" (111).
3. The header intent describes open banking in Kazakhstan and Russia and calls GOST R 57580 "open banking standards"; it is a Russian information-security standard (110).
4. Who breaches whom. In "Partner performance monitoring" the section intent says the bank, as API provider, is accountable for availability, and also that "an SLA-breaching partner creates … risk". "Partner SLA Breach Alert Automation" then has the bank sending the partner a breach notification with a "contractual consequence reference", while its problem text speaks of the bank's own availability failures and reporting duties. The card does not say whose SLA is breached. The drafted OKR follows the card as written; the direction needs the owner.
5. "Partner Contract Renewal Automation": "Partners whose contracts have lapsed … have legally reverted to informal continuation arrangements" states a present fact about the Bank and contradicts itself (115).
6. "Partner Network Intelligence" produces the monthly partner performance pack; the title belongs to the next section (117). Its portfolio economics summary overlaps with "Partner Network Portfolio Intelligence" (quarterly).
7. "Partner" and "third-party provider" are used for the same parties in some cards and for different parties in others.
8. Tab label "Open banking api governance" (109). "Confirmed as regulatory material" in one OKR (116).

## Channel Cycles (`channel-cycles/index.html`)

What is on it: header intent, 4 cycles each with a three-paragraph introduction, 4 problem rows (Analyze, Optimize, Automate, Enrich) and 5 stage dialogs, 17 cards (5, 4, 4, 4), all with OKR.

1. Six OKRs disagree with their card. Pack Automation: 2–4 days in the card, 3–5 in the OKR (118). Root-Cause Synthesis: "24 hours of pack delivery" and 3–7 days in the card, "24 hours of period close" and 3–5 days in the OKR (119). Demand Forecast Automation: the OKR names treasury, a "finance team lead" and a "finance-technology team" that the card does not have (120). Smaller: 121, 122, 123.
2. Three-country statements: "smartphone penetration has reached seventy to ninety percent in urban Kazakhstan, Kyrgyzstan, and Russia" (127), "open banking regulatory frameworks (ARDFM, NBK sandbox)" (128), regulatory notifications "for each regulator" (124). The Incident Communication Drafting card and its OKR list "NBKR / ARDFM / NBK / CBR"; that follows the global decision.
3. Problem rows with no card to answer them. Service-level & incident governance: the Enrich row (a reliability knowledge base) — the other three cycles each have a knowledge-base or retrospective card, this one does not. Channel-mix steering: the Analyze row (continuously current channel-mix economics) — no Insights card. Channel evolution: the Automate row names rollout communication content and sunset migration tracking — no card for either. This is why three cycles have 4 cards and one has 5.
4. Stage dialogs are complete (title, intent, problem for all 20). Two wording slips in "Detect": "customer contact center volume spikes" and the only "call center" in the area (125, 126). Stages with no card of their own: Adjust; Detect, Triage, Resolve (the introduction explains why); Approve in channel-mix steering; Pilot and Sunset.
5. The problem-row lenses here are Analyze, Optimize, Automate, Enrich; the sub-area pages use Insights & analytics, Enablement, Automation, New business opportunities. Cards on this page carry the lens "New opps" for knowledge bases and retrospectives (the Enrich row) and "Enablement" for two cards that have no row.

## Questions for the owner

1. Overview counts. Should the area total on the overview page include the cycle cards (97 instead of 80) and list Channel Cycles, or should the number shown be the sum of the six sub-areas a reader can see (75)? Today it is neither. The answer applies to all eight areas.
2. Partner & API channels. Does the Bank operate or plan an open banking API platform with third-party providers and a priced API catalogue? If not: remove the page, cut it to partner and agent-network monitoring, or keep it marked as a future channel?
3. Relationship management. Do private banking, wealth management and corporate RM books exist at the Bank as described, and are public corporate filings and corporate event feeds available for Kyrgyz clients? If not, which segments should the page name?
4. Regulatory statements. The cards lean on specific duties: NBKR Resolution No. 47/4 (complaints) and No. 50/4 (remote onboarding); notification of ATM outages, skimming incidents and terminal changes; a 30–90 day notice for branch changes; maximum queue times; documented RM contact frequency; digital adoption reporting; "regulatory credit" for branches in underserved areas. Who verifies these with Compliance, and should unverified ones be softened to "where required by the regulator" in the fix round?
5. Problem rows. Each page has one problems tab named after its first group, and on the area page the second group (digital, ATMs, partner) has no rows. Do you want rows per group (drafts 008–011 are ready for the area page), or one untitled set of rows per page? On the sub-area pages the rows already cover the whole page, so there the simplest fix is to drop or rename the tab label.
6. Lens rule. Is the lens meant to describe what the card does, or to spread one card per lens across a section? Cards such as "Complaint Response Drafting", "ATM Fraud Customer Alert Dispatch", "IVR Caller Experience Intelligence", "Third-Party Provider Onboarding Automation" and "Onboarding Abandonment Recovery" are Enablement while similar cards are Automation or Insights. And should problem rows and card lenses use one set of names (Optimize has no row on sub-area pages; the cycles page uses Analyze, Automate, Enrich)?
7. Complexity. Almost every Automation card is S and every Insights card M; there is one L and no XL in 97 cards. Scenarios that need call transcription in Kyrgyz and Russian, real-time assistance during calls, or execution against the core system are rated S or M. Should complexity assume those platforms already exist, or be re-rated for the Bank?
8. "Branch Operations Intelligence". Accept the narrowing to queue and staffing analysis (027–030), or merge the card into "Branch Performance Pack Intelligence" and have 11 cards on the page?
9. "Partner SLA Breach Alert Automation". Whose SLA is breached — the bank's API availability towards partners, or the partner's obligations towards the bank? The card mixes both.
10. "Digital Self-Service Task Automation". Is this a conversational assistant inside the app? The card should say so, because balance enquiry and card freeze are ordinary app functions.
11. Roles. The cards name a Head of Channels, Head of Branches, Head of Network Planning, Head of Digital, Head of Contact Center, Head of Complaints, Head of Self-Service, Head of Partner Channels, Head of API Products, Head of Treasury Operations and a "CCO". Should these be mapped to the Bank's actual roles, and what does CCO stand for here?
12. Missing cards. Do you want cards added for the uncovered problem rows on the cycles page (reliability knowledge base; current channel-mix economics; rollout communication and sunset tracking) and for non-voice contact center channels, or should the rows be trimmed to what the cards cover?
