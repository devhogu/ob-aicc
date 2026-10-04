# Brief: the chosen form of each shared term in the Russian corpus

The shared terminology (`charter/ru/shared-technology-terminology.md`, English edition `charter/en/shared-technology-terminology.md`) lists each common business, delivery, and technology term with a universal (English) term, a Russian term, a meaning, and an application note that says whether the universal form is fixed or a Russian language variant is permitted. The owner will add a column «Форма в русском корпусе»: the exact form that the Russian corpus writes, either the English form, a Russian form, or a hybrid (e.g. «AI-агент», «WIP-лимит»). This research proposes that form for each entry, from how the concept is actually written in Russian-language banking, regulatory, and IT texts today.

## Owner decisions already taken (do not research, just record)

- AI → «AI» (Latin), including in compounds («AI-агент», «AI-решение», «платформа AI»).
- IT → «IT» (Latin).
- business case → «бизнес-кейс».
- Company and product names (AICC, O!Bank, Atlassian, Jira, Confluence, AWS, CloudWatch, …) keep their form.

The owner's preference is: keep the English form where Russian banking and IT practice actually keeps it (as with IT, KPI, SLA, MVP, API), and use the Russian form where Russian practice uses a Russian or Cyrillic form (as with бизнес-кейс).

## For each entry, decide with evidence

1. How do Russian-language sources write this concept in running text: English form (Latin), Cyrillic borrowing (бэклог, дашборд), or a Russian term (лимит незавершённой работы)? Look at, in order of weight: NBKR and Bank of Russia texts; ГОСТ Р and official Russian translations (ITIL 4, Scrum Guide, PMBOK, ГОСТ Р ИСО/МЭК); public documents and engineering blogs of banks in Russia, Kazakhstan, Kyrgyzstan (Sber, VTB, T-Bank, Alfa, Halyk, Kaspi, KICB, Mbank, Bakai) and large IT companies (Yandex, VK); Habr; vacancies on hh.ru / hh.kz / hh.kg (they show how practitioners name things). Use WebSearch and WebFetch (load them with ToolSearch "select:WebSearch,WebFetch"). Cite the URLs you actually read; never invent a quotation; mark well-known usage that you did not fetch as "not fetched".
2. How does the form behave in a Russian sentence: does it decline, take a hyphen, have a plural (WIP limits → «WIP-лимиты»)? The chosen form must be writable inside Russian grammar without leaving an English plural or an English word order.
3. Propose the chosen form, one exact string (plus its plural or compound pattern if needed), and a confidence (high / medium / low). Where the corpus currently uses a different form, say so.

Also list, separately, terms that the Russian corpus (`charter/ru/`) uses in Latin script or as an awkward Russian term but that are missing from the shared terminology (e.g. value stream, Workflow, WIP limit, Epic, Service Management, Program Increment, if absent), with the same research and proposal. Check quickly with grep.

## Output

Write `wiki/research/russian-register/term-choice-<your part>.md` with:

1. A table: | Section | Universal term | Current RU term | Current status (fixed / variant) | Real-world usage (Latin / Cyrillic borrowing / Russian), with sources | Proposed «Форма в русском корпусе» | Inflection or compound pattern | Confidence | Changes the corpus? |
2. The list of missing terms in the same format.
3. Sources read, with URLs.
4. A 5-line summary of the pattern you observed (where Russian practice keeps English, where it does not).

Do not edit anything under `charter/`, `registry/`, `portfolio/`, `portal/`. Write analysis in English and forms in Russian. One line per paragraph, no hard wrapping.
