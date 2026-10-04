# Brief: naturalness review of the Russian charter

Read-only review of the Russian edition of the AICC charter (`charter/ru/`) against how the same subject is written in modern Russian financial and banking texts. The owner finds the Russian clumsy: calqued from English, wrong or unidiomatic financial terminology, and sentences that do not sound like modern Russian. The goal is evidence-based findings and natural rewrites, plus reusable term pairs and stock phrasings.

## Ground rules

- Do not edit anything under `charter/`, `registry/`, `portfolio/`, `portal/`. Write only your own report file in `wiki/research/russian-register/`.
- The English edition (`charter/en/`) is the source of meaning. A rewrite must keep the meaning, the decision rights (who decides, who is accountable), the obligations, the clause numbering, and the table structure. Natural ≠ looser.
- Fixed international names are an owner decision: AI and IT stay in Latin script, product names stay as they are (see `charter/ru/shared-technology-terminology.md` §2). Do not report these as errors. You may add ONE observation on how the Russian sources you read actually write them (e.g. ИИ vs AI), with sources, in a separate "Observation" note.
- Defined terms (capitalized in the corpus, defined in `charter/ru/documents/vocabulary.md`) must stay consistent across documents. If you think a defined term itself is badly chosen, do not rewrite it ad hoc in one clause: put it in the Glossary section with the proposed replacement, the reason, the source, and the note "changes every occurrence".
- Mixed scripts inside a phrase that is not a fixed name (e.g. "AI agent", "workflow" where a Russian word exists) may be reported.

## Authorities, in order of weight

1. National Bank of the Kyrgyz Republic (НБКР): Russian-language normative acts, e.g. on corporate governance, internal control, risk management, information security, outsourcing in commercial banks. O!Bank is a Kyrgyz bank, so Kyrgyz banking Russian is the closest register.
2. Bank of Russia (ЦБ РФ): normative acts and reports (e.g. Указание 3624-У on risk management and risk appetite; Положение 716-П on operational risk; the Corporate Governance Code; reports and consultation papers on AI in the financial market; the AI ethics code for the financial market).
3. Russian national standards (ГОСТ Р, ГОСТ Р ИСО, ГОСТ Р ИСО/МЭК), e.g. 22989 (AI concepts and terminology), 42001 (AI management system), 20000 (service management), 21500/21504 (project and portfolio management), 31000 (risk management).
4. Official Russian translations of practice bodies: ITIL 4 glossary (RU), Scrum Guide (RU), PMBOK (RU).
5. Public documents of major banks in Russia, Kazakhstan, Kyrgyzstan (Сбербанк, ВТБ, Альфа-Банк, Т-Банк, Halyk, KICB, Оптима, etc.): policies, annual reports, governance documents, and their engineering blogs (Habr) for agile and IT practice.

Use WebSearch and WebFetch (load them with ToolSearch "select:WebSearch,WebFetch" if they are not loaded). Cite a URL for each source you actually read. If a fetch fails, you may still cite well-known usage, marked "not fetched". Never invent a quotation.

## What to look for

- Calques: English structure or word choice carried over (capability → возможность; to deliver → доставлять; ownership; "is responsible for ensuring"; "in the scope of").
- Terminology: a term that differs from the established Russian financial, governance, IT, or AI term for the same concept.
- Register: phrasing that does not match Russian internal regulations (внутренние нормативные документы) or modern Russian business writing; bureaucratic noun chains (осуществление проведения…), stacked genitives, overuse of "который", "должен" for every "shall", passive constructions with "осуществляется", unnatural word order, unnecessary capitalization, unnatural punctuation.
- Repetition and over-literal enumerations.

## Report format (one Markdown file, no hard-wrapped lines)

1. **Summary**: 5–8 lines: overall verdict, the main patterns, and how often they occur (count them with grep where you can).
2. **Sources read**: list with URLs and what each is authoritative for.
3. **Patterns**: each recurring pattern with 2–3 examples (current → proposed) and a general rule for fixing it.
4. **Findings**: a table: | Location (file clause) | Current | Proposed | Type | Basis | Confidence |. Prioritize impact: the 40–80 most important findings for your documents. Do not list trivial variants.
5. **Glossary**: term pairs: | EN term | Current RU | Proposed RU | Where it is used in practice (source) | Note (changes every occurrence? defined term?) |.
6. **Phrase bank**: stock phrasings for recurring statements of your subject as Russian financial documents write them (e.g. how a regulation states who approves, who is accountable, what is prohibited, when a review happens), each with an example from a source.
7. **Observation** (optional, one paragraph): on AI/IT script, if relevant.

Write in English for the analysis, Russian for the examples. Keep it compact and concrete.
