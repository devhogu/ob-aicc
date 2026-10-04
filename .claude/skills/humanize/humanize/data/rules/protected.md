# Modes: untouchable, protected, standard

Pick exactly one mode. Sources are cited so each rule can be re-checked against the vendored skill it came from.

## Untouchable: return the text unchanged

Contract terms, regulated disclosures, legal or compliance language, direct quotes attributed to a person, code, commit messages, PR descriptions, changelogs, SEO structural elements (title tags, meta descriptions, keywords).
Add `Note: untouchable (<reason>); returned unchanged.` (`humanize-pro` trigger exclusions and "Do not humanize"; `unslop` Boundaries.)

## Protected: restricted edits only

Triggers: medical, clinical, or behavioral guidance; safety instructions; security warnings; irreversible or ordered procedures; runbooks; incident timelines; any text where a qualifier carries accuracy. (`unslop` Auto-Clarity; `humanize-pro` "Do not humanize"; `humanize-writing` "When NOT to Use".)

Permitted edits, and nothing else:

1. **Delete pure filler:** openers, connectives, and closers from `../vendor/humanize-pro/references/ai-tells.md` section 2 ("It should be stressed that", "Furthermore,", "In conclusion,"), when every claim and instruction survives the deletion.
2. **Shorten filler constructions** from the "Filler" row of `ai-tells.md` section 3: "in order to" becomes "to", "due to the fact that" becomes "because".
3. **Replace inflated vocabulary** from `ai-tells.md` section 1 with a plain word of the same meaning and strength ("a pivotal factor" becomes "a major factor"; "utilize the inhaler" becomes "use the inhaler"). In instructions, "it is essential to check X" may become "check X": both are instructions of the same strength.
4. **Plain constructions:** copula avoidance ("serves as", "stands as", "represents") becomes "is" when the meaning is identical ("serves as a reminder" becomes "is a reminder"); a pair of near-synonyms becomes one plain word ("clear and transparent" becomes "clear").
5. **Collapse hedge stacks** to one hedge of the same strength ("could possibly" becomes "could"). Never remove the last hedge on a claim.
6. **Fix punctuation:** em dash to parentheses, comma, colon, or period; curly quotes to straight.
7. **Fix Markdown heading case** to sentence case, unless the heading is the document's name or contains a defined term.
8. **Normalize layout:** join a paragraph or list item that is hard-wrapped mid-sentence into one line, and make a double space inside a sentence single. Keep the spacing between sentences, blank lines between paragraphs and sections, one-sentence-per-line paragraphs, a two-space line break at the end of a line, and every line in tables, headings, and labeled lines. `humanize tidy` makes exactly these changes; in a run, the gate applies them to your edit automatically.

A word is a term of art if a practitioner in the field uses it with a specific meaning ("vital signs", "contraindicated", "person-centred care"). Never replace a term of art. If unsure, keep the word.

Forbidden: changing any instruction, number, unit, identifier, quoted script, term of art, hedge strength, step order, list or heading structure, or bold label; adding anything; deleting a sentence that carries a claim or an instruction (rewrite its wording under the permitted edits instead); rhythm or voice changes; converting bullets to prose or prose to bullets. Headings, list items, and labeled lines keep their line structure; never wrap a line to a width.

If no permitted edit applies, return the text unchanged and say so in one note: in a run, under "Notes for the author" in the report (never in the document); outside a run, as `Note: protected mode (<trigger>); no permitted edits applied.` after the text. If a high-signal tell remains because protected mode may not touch it (a word from `ai-tells.md` section 1 that might be a term of art, a candor adverb from section 3 such as "truly", a promotional takeaway sentence), add one `Note:` in total that names them and asks what they should say concretely. That limit covers leftover tells only; other notes from the output contract (unfamiliar identifiers, missing information) are separate. Do not note contrast or hedging structures; in this mode they usually carry accuracy.

In protected mode, `humanize gate` enforces these limits: it fails on lost numbers, codes, quoted scripts, bold labels, negations, or hedges.

## Standard: everything else

Choose a register (`register.md`). Short text that already reads clean may need nothing; do not hunt for edits.
