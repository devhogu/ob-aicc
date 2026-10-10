# English style for the AI Competence Hub

These rules apply to every English text of the Hub: pages, data files, interface strings and the catalog. Russian is the source; English is a maintained translation. Use the renderings in `terms-en.yaml` (terms, names, phrases, plurals, formats, laws); when a word is not there, translate it by its ordinary meaning.

## Voice

- Plain, friendly, professional English for bank staff. Write natural sentences, not a word-for-word rendering of the Russian.
- Address the reader as "you"; the Hub speaks as "we". The Russian polite capital «Вы» becomes plain "you".
- No legalese: no "shall", "hereinafter", "the said". Short sentences, active voice, everyday words.
- American spelling (as the English corpus requires): program, center, organization, analyze, behavior, catalog, color. Official names keep their own spelling (Astana International Financial Centre).
- Serial comma, as in the corpus: "persevere, pivot, or stop".
- Curly double quotes “…” replace «…»; an em dash — stays an em dash.
- Sentence case for headings, buttons and labels ("How we work", "Mark step as done"), except names (Knowledge Base, Discovery Catalog) and the SAFe terms Capability and Feature, which keep their capitals.

## Hub names

- **AI Competence Hub** is the full title: site title, home page heading, footer, page titles. It renders «Хаб Компетенций по AI».
- **Competence Hub** is the middle form: section label, mail subject, a second mention where the full title would repeat. It renders «Хаб Компетенций».
- **Hub** is the short form in running text, always capitalized and with the article: "the Hub". It renders «Хаб».
- «Центр Компетенций» is **Competence Center** (both words capitalized), **AI Competence Center** as a title. Never AICC in reader text.
- The three roles are business owner, product manager and project manager; the two forums are the product management forum and the program decision forum. Lowercase in running text, capitalized only at the start of a sentence or heading.

## Plain industry terms

Industry terms appear in plain English once, without the Russian: "funnel", not "funnel (воронка)". The term marker shows the English word only. Spell out an abbreviation at its first use on a page: large language model (LLM), retrieval-augmented generation (RAG), minimum viable product (MVP), weighted shortest job first (WSJF), know your customer (KYC). The English vocabulary page shows the English term and its definition only.

## What the Hub never says

- No bank name: never O!Bank or Obank. «Банк» (the organization) is "the Bank"; a generic «банк» is "a bank".
- No statement of the Hub's legal nature or authority: nothing like "has no authority", "does not take decisions", "a unit of the Bank", "consolidating". Describe what the Hub does, not what it is legally.
- None of the forbidden wording in `forbidden_en` (Executive Sponsor, Domain Owner, Head of the Competence Center, Competence Center Lead, DR-2026, v1 and the rest), and no internal document identifiers. "Steering" and "steering committee" are ordinary words and allowed (owner, 2026-10-10).
- Recommend only approved tools; say "use only the tools and accounts approved in your organization".
- No reference to v1.

## Laws, courses and products

- A law, regulation or regulator gets its official English title where one exists (`official: true` in `laws`). Otherwise give a translated title with the Russian original in brackets: Digital Code of the Kyrgyz Republic (Цифровой кодекс Кыргызской Республики). Never invent an official title. A descriptive heading (`type: topic`) is translated plainly, without the Russian.
- Course, product and interface names stay as their owners publish them: Claude Code, Claude Cowork, Claude Academy, "AI Fluency: Framework and Foundations", Settings → Memory. Where the Russian adds a translation in brackets, «Settings → Memory (Параметры → Память)», the English keeps only the original: Settings → Memory.
- A step "in Russian" (official Russian documentation) stays marked "in Russian".

## The owner's wording

The home page and any text marked as the owner's are translated faithfully, keeping their tone, capitals and exclamation marks; do not improve, shorten or smooth them. Example: «Хаб Компетенций и Решений» is "Competence and Solutions Hub".

## Markdown and HTML

- No hard wrap: each paragraph and list item on one line.
- Keep the front matter keys, `{#anchors}`, `page:` links and `{{icon:…}}` markers exactly. Translate only the visible text: titles, summaries, link text, `data-tip`, `data-tip-title`, `aria-label`.
- Term markers keep the id and translate the surface only: `[[funnel|воронки]]` becomes `[[funnel|funnel]]` or `[[funnel]]`; `[[run-rate|текущую работу]]` becomes `[[run-rate|run-rate work]]`.
- HTML blocks keep their structure and classes; inline markup uses `<a>`, `<code>` and `<b>`.

## Dates, numbers and plurals

- Dates: "8 October 2026", short "8 Oct 2026"; ranges "5–11 Oct 2026", "28 Sep – 4 Oct 2026". Month and weekday names come from `names.months` and `names.weekdays`.
- Numbers: digits; comma for thousands (1,110), point for decimals (2.5), percent without a space (45%). Durations: "about 6 min", "about 3 h", "4 wk".
- Plurals have two forms (one, other): 1 project, 2 projects. Labels stay as built: PI 2026-PIQ4, i10, I10, W2, Planning, Review.
