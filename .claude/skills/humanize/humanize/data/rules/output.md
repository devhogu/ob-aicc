# Output contract

1. The edited text, with nothing before it. In standard mode, hollow words the edit would delete stay in place in square brackets for the author to keep or cut (`fidelity.md`, "Marked words").
2. In a run, the edited document holds only the text; notes go in the report's "Notes for the author" section, one bullet per item. Outside a run, add them after the text instead: a blank line, then one line per item starting `Note:`. Notes cover missing information the author should add, claims with no proof, identifiers or jargon the intended reader probably will not know (an internal framework or form code in text for a parent or client), vague terms kept on purpose (ask what they mean concretely), rule conflicts, or why protected mode changed nothing (that note comes first). Notes address the author, invent nothing, and never suggest cutting a sentence that carries a claim or an instruction. Do not note what is already fine.
3. When another agent invoked you or the user asked how it ran, end with the `Run:` line that `humanize gate` prints.

Never narrate the edit, list changes, or add a preamble unless asked.

Other constraints: no em dashes; Markdown headings in sentence case; keep paragraph breaks (protected mode also keeps list, heading, and labeled-line structure); one line per paragraph and per list item, never hard-wrapped to a width (a wrap mid-sentence breaks the sentence for editors, diff tools, and other agents); single spaces inside sentences, but keep the source's spacing between sentences and its blank lines; keep the source's person and pronoun; vary sentence length only where the content varies (no formula such as forced "And/But" openers).
