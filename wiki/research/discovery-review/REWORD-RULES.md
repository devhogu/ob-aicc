# Rewording rules for the Discovery Catalog (English)

The catalog describes banking concerns where AI may add value. The concerns are the same in any bank; what made the text regional was the naming of regulators, laws, currencies and markets, and a few facts asserted about a particular bank. The rewording keeps every concern and makes its statement neutral, correct and clear. The tie to O!Bank is made once, on the landing page, not in the cards.

## 1. What you edit and what you must not touch

You edit a JSON view of one page: `page` (text nodes outside the cards), `cards` (each with its `urn`, `lens`, `complexity` and text `nodes`), and `stages` (texts of the cycle or value-stream stages). You change only the value of `text`. You must not add, remove or reorder nodes, cards or stages, and you must not change `id`, `role`, `path`, `urn`, `lens`, `complexity` or `file`. A node whose text needs no change stays exactly as it is. The tool rejects a file whose node set differs.

Roles tell you what a node is: `title`, `intent`, `problem`, `solution`, `okr-objective`, `okr-adoption`, `okr-acceptance`, `okr-cycle` inside a card; `page-header__title`, `page-header__intent`, `problems-lens`, `problems-statement`, `problems-tab-label`, `l3-section__title`, `l3-section__intent`, `sub-group__label`, `card-link`, `card__title`, `card__count`, `card-link__count` and similar outside. Leave counts, column labels (`scenarios-col-label`), lens names and single-character markers alone unless a fix entry says otherwise.

## 2. Apply the fix entries for the page

You receive the fix-map entries for your page. Apply each one: its `proposed` text replaces the `current` text in the node it names (by `urn` and `field`, or by `locator`). Where `current` is a sentence inside a longer node, replace that sentence and keep the rest. Then make the result conform to the rules below (a proposed text may itself name a regulator or use British spelling; neutralize and correct it like any other text). Entries with field `okr`, `lens` or `complexity` are already applied; entries with field `structure`, `count`, or a missing `problem_row` are handled separately and are not yours. Report every entry id as applied, already applied, or not applied with the reason.

## 3. Neutral statement of the concern

| In the text | Write |
| --- | --- |
| A named national regulator or supervisor: NBKR, CBR, Bank of Russia, NBK, National Bank of Kazakhstan, ARDFM, AFSA, and lists of them ("NBKR and CBR", "NBKR, NBK/ARDFM and CBR") | "the regulator" (or "the supervisor", "supervisory requirements", "prudential requirements"), once, not a list |
| A numbered national act, resolution, ordinance or form ("NBKR Resolution No. 47/4", "CBR Ordinance No. 59-I", "NBKR Form 700", "Regulation No. 9") | The subject of the rule, without the number: "consumer-protection requirements", "the prudential return", "large-exposure limits", "applicable law on personal data" |
| A national financial intelligence unit: FinCEN, Rosfinmonitoring, AFMRK, "NBKR FIU" | "the financial intelligence unit" |
| US, UK or EU officers and bodies used as the bank's own: BSA officer, MLRO, CFPB, OCC, FCA, PRA, Consumer Duty, state money-transmitter licences | The neutral role or duty: "the AML compliance officer", "the conduct regulator", "licences and registrations" |
| Countries and markets as the bank's own: Kazakhstan, Russia, "the three jurisdictions", KZ and RU populations, CIS jurisdictions | "the bank's market", "the domestic market"; where a card is about operating across several jurisdictions, say "where the Bank operates in more than one jurisdiction" |
| Currencies and market infrastructure: KZT, RUB, tenge, ruble, KASE, MOEX, TONIA, MOSPRIME, KazPost, Rosstat | "local currency", "local-currency and major-currency curves", "the domestic exchange", "the domestic benchmark rate", "the national card scheme", "the national statistics office" |
| International standards: Basel III, IFRS 9, BCBS 239, FATF Recommendations, ISO 20022, ISO 27001, TCFD, ISSB | Keep the name. State it as a standard or reference ("in line with the BCBS 239 principles", "under IFRS 9"), not as a finding or an order addressed to the bank |
| EU, US and UK regimes stated as binding: COREP, FINREP, EBA guidelines, DORA, SR 11-7, MiFID, PSD2, GDPR, SREP | Drop where the sentence works without them; otherwise name the subject ("supervisory reporting", "operational-resilience requirements", "model-risk guidance") and, at most once in a field, "such as …" a named framework as an example |
| Facts asserted about a particular bank: "the regulator has repeatedly found…", "in the last examination…", branches, managers, licences or obligations in a named country | A general pattern: "supervisors commonly find…", "banks often…"; or delete the clause |
| A practice that only larger or differently licensed banks have: internal-ratings models (IRB), an internal-models trading book, advanced operational-risk capital (AMA), AT1 or covered-bond issuance, a sell-side research desk, private banking books, an open-banking API platform, analyst earnings calls | Keep the scenario; open the dependent statement with the condition: "Where the Bank uses internal models…", "For a bank with a trading book…" |

Do not replace a foreign specific with a Kyrgyz one (no "som", "Elcart", "State Financial Intelligence Service", no Kyrgyz act numbers): the Bank's equivalents are given once on the landing page. If a proposed fix inserts one, write the neutral form.

## 4. Wording

- American spelling throughout (optimization, analyze, organization, center, modeling, program, judgment, license as noun and verb).
- The actor is "the AI agent" ("The AI agent reads…", "an AI agent drafts…"), never bare "Agent". A human agent (contact-center agent, branch agent, relationship manager) keeps its human name; where both appear in one sentence, write "the AI agent" and "the contact-center agent" so that they cannot be confused. Titles of sections and cards that name human agents are not changed.
- Compounds of the AI actor take "AI": "agent-produced" → "AI-produced", "agent-drafted" → "AI-drafted", "agent-generated" → "AI-generated", "agent-driven" → "AI-driven"; "agent output" → "the AI agent's output". Compounds of a human agent stay ("agent desktop", "agent-assist").
- "the Bank" with a capital for the institution; "a bank" or "banks" for banks in general.
- "100%" where the text says "≥100%" or "≥ 100%".
- Remove authoring notes and scaffolding left in the text ("L complexity is retained because…", "TODO", placeholders). The breadcrumb token `service.eyebrow` stays in the source: both builders replace it with the name of their site.
- A label printed from an identifier is written as a proper label: "Aml investigations sar" → "AML investigations & SAR", "Rm productivity" → "RM productivity", "Pricing models ftp" → "Pricing models & FTP".
- Keep the catalog's voice: third person, present tense, concrete roles, artifacts and cadences. Keep each text at about the length it had (within a fifth). Do not add claims, figures or roles that the card does not already have. Do not change a figure or target except "≥100%" or where a fix entry says so.
- Fix what is wrong or unclear: a truncated sentence, text from another card, a contradiction inside the card (cadence, threshold, count, recipient), a sentence that says nothing, a sentence too long to follow. Do not rewrite a sentence that is correct, clear and already neutral.

## 5. A card as a whole

After the edits, read each card once as its reader would. The intent says what the scenario does and for whom. The problem states a real problem. The solution answers that problem with the AI agent's part and the human's part stated. The OKR measures this card: the objective names the outcome and its recipient; Adoption says how consistently the scenario runs; Acceptance says how often the named reviewer accepts or acts on the output; Cycle gives the before and the after of time or cadence. The four OKR texts name the same roles, outputs and cadences as the intent, problem and solution. Where two cards on the page describe the same scenario, do not merge them: make each say what is specific to it, as the fix entry directs.

## 6. Output

Write the edited JSON to the output path given, with the same structure. Then write the report file given: a JSON object `{"file": …, "fixes": {"<id>": "applied" | "already applied" | "not applied: <reason>"}, "notes": ["…"]}` with any point that needs a human decision. Do not edit any other file.

## 7. Points settled by the pilot (Contact center page)

- A title respelled to American spelling ("Optimisation" → "Optimization") is changed wherever the same title is shown as text on other pages (link labels on the area page and the overview); identifiers (`urn`, anchors, slugs) keep their original spelling.
- Compounds are hyphenated the same way throughout a page: "contact-center agent", "contact-center supervisor", "contact-center operations".
- Number ranges use an en dash without spaces ("1–3%", "4–8 hours") in every field.
- One name per role on a page ("complaint handler", not also "complaints handler").
- A statement that a rule sets a specific level (a wait time, a deadline, a threshold) is written as common practice ("requirements commonly provide…", "typically within…") unless the level is the Bank's own target in the card.
- A detail may be carried from one field of a card into another to make the card coherent; nothing may be added that the card does not already say.
