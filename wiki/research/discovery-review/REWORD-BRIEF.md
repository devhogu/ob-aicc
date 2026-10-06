# Rewording brief: Discovery Catalog, English

You are rewording part of the Discovery Catalog of the O!Bank AI Competence Center portal: 76 pages, 1,101 scenario cards in which AI could help a bank. The text was written for another region. It names foreign regulators, laws, currencies and markets, asserts facts about a bank that is not ours, mixes British and American spelling, and calls the AI "Agent" so that it cannot be told from a human agent. The owner has decided that every scenario stays, stated in terms that hold for any bank. Readers are bank managers who will pick scenarios from this catalog, so each card must be correct, clear and coherent on its own.

The binding rules are in `/devops/obank/aicc/wiki/research/discovery-review/REWORD-RULES.md`. Read all of it before you start, and follow it. Its sections 1 and 6 describe a JSON file per page; in this run the files differ, as described below. Everything else in it applies unchanged.

## Your files

For each part named in your task (for example `risk-control__credit-risk.1`):

- Read `/tmp/dc-run/view/<part>.txt`: the text of the part. Each line is `key <tab> role <tab> text`. Blocks are headed `== page ==`, `== card <urn> | lens … | complexity … ==` or `== stages of <flow> ==`. Blocks appear in page order: a section title and its introduction, then the cards of that section.
- Read `/tmp/dc-run/fix/<part>.json`: the fix entries for this part, found by an earlier review (may be an empty list).
- Write `/tmp/dc-run/patch/<part>.json`: one JSON object, `{"<key>": "<the complete new text of that line>", …}`, holding only the lines you changed. Plain text: no HTML tags, no entities (write `&`, not `&amp;`). Never invent a key; never include a line you did not change.
- Write `/tmp/dc-run/report/<part>.json`: `{"part": "<part>", "fixes": {"<fix id>": "applied" | "already applied" | "not applied: <reason>"}, "notes": ["…"]}`. Every fix id of the part appears. Notes hold only points that need a human decision, and the foreign citations you removed in the form `"citation removed: <the act, form or named instrument as it was written> — <key>"`. A citation is a numbered act or form, or a named instrument of a named national regulator ("NBKR IRRBB guidance"); a bare regulator name is not logged.

Write only these two files per part. Do not edit anything in the repository and do not run git.

## How the lines relate

- Several consecutive lines with the same role (for example three `page-header__intent` lines) are one paragraph that the page prints with the middle piece in bold or italics. Keep the split: edit each piece so that the paragraph still reads as continuous text.
- `stage N label | title | intent | problem` lines are the steps of a workflow shown as a diagram. `label` is the short name on the diagram: change it only for spelling.
- Navigation labels (`card-link`, `card__title`, `card__eyebrow`, `sub-group__label`, `flow-item__name`, `problems-tab-label`, `problems-lens`) are changed only for American spelling, for a label printed from an identifier (rules, section 4), or where a fix entry says so. A separate step keeps link labels equal to the titles they point to.
- The OKR lines of many cards and the `problems-statement` rows of some pages were drafted in this round. They are drafts: check them against their card or page and apply the same rules to them.

## What the work is

Go through every line of every part. Do not sample and do not stop early: a line you skip goes to the site as it is. Most lines need a change (the actor, "the Bank", spelling, a regulator), so expect to patch well over half of them. For each card, after the line edits, read it once as a whole as section 5 of the rules says, and fix what does not hold together.

Points that the rules settle and that are easy to get wrong:

- The AI actor: "The AI agent reads…", "an AI agent drafts…". Compounds take "AI": "agent-produced" → "AI-produced", "agent-drafted" → "AI-drafted", "agent-generated" → "AI-generated", "agent-driven" → "AI-driven"; "agent output" → "the AI agent's output". Human agents keep their names ("contact-center agent", "collections agent", "agent desktop", "agent-assist").
- "the Bank" for the institution; "a bank", "banks" in general statements.
- Regulators become "the regulator" once, not a list. Numbered national acts and forms become the subject of the rule. No Kyrgyz specifics either. International standards (Basel III, IFRS 9, BCBS 239, FATF, ISO 20022, TCFD, ISSB) stay, as references.
- A fact asserted about a particular bank or market becomes a general pattern or goes.
- Keep figures, targets, roles, cadences and length. Do not add claims.
- A practice that only some banks have (rules, section 3, last row) gets its condition once per card, in the first statement that depends on it, and once in the section introduction if the whole section depends on it. Titles stay; later mentions in the card need no condition.
- Where only the OKR names the person who reviews the output, carry that reviewer into the solution, so the solution states the human's part.
- Merge two role names only where they plainly denote the same role on the page ("complaint handler", "complaints handler"). A distinct person or unit stays distinct, an abbreviation introduced earlier may be used later, and the name of a discipline or function ("ALM", "Treasury") is never replaced by a team name.
- "AOCI" is written "accumulated OCI". Basel terms such as "Pillar 2" stay.

Apply every fix entry of the part as section 2 of the rules says: the `proposed` text is the intended meaning, and you still bring it under the rules (it may itself name a regulator or use British spelling).

## Check before you finish

After writing the patch and the report of a part, run `python3 /tmp/dc-run/scan.py <part>`. It applies your patch to the view and lists what remains. Clear every "must fix" line by correcting the patch, except where the hit is right as it stands: a human agent without "AI", a word the scanner mistakes for British spelling, a scale-dependent practice whose condition the card already states, "som" or "law" used in an ordinary sense. "To review" lines are judgment calls: a foreign regime kept once as "such as …" is allowed; a scale-dependent practice needs its condition. Rerun until the remaining lines are all justified. If the scanner says a key is unknown or the JSON is invalid, fix it; such a patch is rejected.

Your final message: the parts done, the number of lines patched in each, the number of scanner lines you left and why (in one phrase), and any point that needs the owner's decision. Keep it under 150 words.
