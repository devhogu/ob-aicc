# Fidelity

The source is the only authority on what is true. The edit may say less in fewer words; it may never say something different.

## Never add

- Numbers, dates, names, places, quotes, examples, or customers.
- Commitments or next steps the source does not make (turning "updates will follow" into "next week's update will include the budget").
- Certainty or doubt the source does not state. "We are sure the rollout will go smoothly" keeps its certainty in plain words; it may not become "we expect a smooth rollout" (weaker) or "we have not tested the rollout yet" (invented doubt).
- Statements about what the author knows ("we don't have the figure yet").
- Causes, reasons, explanations, or an actor the source does not name. Turning a passive into an active is fine when the source makes the actor clear (a document written as "we" about its own team's work); otherwise keep the passive.

These look like honest gap-flagging and are invented.

## Gaps go in notes

When a reader needs something the source omits (a date, a metric, proof), keep the sentence at the source's level of detail in plain words, and add a `Note:` line after the text addressed to the author:

- Source: "The vendor review is expected to conclude at some point soon."
- Text: "The vendor review should finish soon."
- Note: "No end date for the vendor review; add one if known."

## Deletion by mode

- **Standard, internal:** delete only what `register.md` lists as carrying no information.
- **Standard, external:** keep every claim; drop the hype around it.
  - A **claim** is a checkable assertion about the offer: what it does, what it works with, how it compares, what the team has done, what result to expect. Each claim survives once, in plain words.
  - Sort every promotional word into one of four kinds, then act:

    | Kind | Examples | Action |
    |---|---|---|
    | Comparison or superlative | "world-class", "unmatched", "state-of-the-art" (newest) | A real claim. Keep it at full strength in plain words: "unmatched reliability" becomes "more reliable than any alternative", not "more reliable than most". |
    | Magnitude | "significant", "major", "substantial" | A real claim. Keep the word and add a `Note:` asking for the figure. |
    | Hollow intensifier | "seamless", "groundbreaking", "first-rate", "successfully", "truly", "just" in "in just a few clicks", "renowned" with no source; any adjective that says something is real, genuine, or concrete without saying how much ("genuine value", "meaningful difference", "concrete results") | No checkable content. Keep it in place, marked in square brackets: "a [groundbreaking] design", "[successfully] delivered". Never swap in another adjective. See "Marked words" below. |
    | Inflated outcome | "empower", "unlock", "supercharge", "take to the next level" | State the outcome plainly: "unlock new growth" becomes "help you grow". |

  - "We are confident" stays "we are confident"; do not soften it to "we expect".
  - Swapping one hype word for another is not a fix ("unmatched" to "second to none", "groundbreaking" to "pioneering", "seamless" to "frictionless"); see "Moves, not strings" in `ai-tells.md`.
  - Feelings and stance ("We are excited to present") are not claims and may go. Keep one plain closing ask; it is the "ask" in `channels.md` section 11.
  - Source: "Our award-winning designers bring unmatched creativity and a passion for excellence to every single engagement."
  - Good: "Our designers have won awards, and no one we compete with does more creative work." Kept: awards, a comparison at full strength.
    Dropped: "passion for excellence" (stance, nothing to check).
  - Bad: "Our award-winning designers bring unrivaled creativity to each engagement." Synonym swap; the hype survived ("Moves, not strings" in `../vendor/humanize-pro/references/ai-tells.md`).
  - Bad: deleting the sentence, or "Our designers do good work". Claims lost.
  - Add a `Note:` when a claim has no proof (which awards? compared with whom?). One note per missing fact; merge related gaps; usually five notes or fewer.
- **Protected:** delete only what `protected.md` permits.

## Marked words

In standard mode, a single word the edit would otherwise delete as a hollow intensifier (the table above, in either register) stays in the text inside square brackets. The author decides: delete the brackets to keep the word, or delete the word. Rules:

- Mark only words that appear in the source, exactly as they appear. Never add a word just to mark it.
- Mark single words or two-word modifiers ("[remarkable]", "[truly unique]"), not whole phrases or sentences. Filler sentences, openers, and closers on the deletion lists are still deleted outright.
- Do not mark comparisons, magnitude words, or inflated outcomes; handle them as the table says.
- Keep grammar valid with or without the marked word: "a [genuine] improvement" reads correctly either way.
- When any word is marked, add one `Note:`: "Words in [brackets] add no checkable claim; delete the brackets to keep a word, or delete the word." Do not also list them as removed.

Protected mode does not mark words; it follows `protected.md`.

## Person and pronoun

Keep the source's. A document written as "we" stays "we"; do not drift into "I" when adding notes or rewording. When the source mixes "I" and "we", keep each sentence's own person.
