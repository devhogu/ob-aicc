---
name: humanize
description: >-
  Humanize AI-drafted prose: line-edit one document, several, or a whole
  folder so it reads like a careful human wrote it without changing what it
  says. The local humanize tool selects documents, briefs each edit, and gates
  the result; a fresh high-reasoning sub-agent edits each document and reports
  on it. Use when the user asks to humanize, clean up, de-AI, de-slop,
  line-edit, or tighten status updates, memos, emails, proposals, marketing
  copy, docs, or guidance text, or says drafts read like AI. Clinical, safety,
  procedural, and policy text is handled in a restricted protected mode. Do
  not use for code, commit messages, PR descriptions, changelogs, contract
  terms, regulated disclosures, fiction, or requests to review the substance
  of a text rather than its wording.
---

# Humanize

Version: humanize 1.10.4 (claude).

You orchestrate; workers edit; the tool checks. `humanize` is a local, deterministic tool that never calls a model. Run it as `humanize` if it is on PATH; otherwise as `<this directory>/bin/humanize`.

## 1. Intake

- **A folder:** Markdown files only (`*.md`). Add other types only when the user asks (`--include '*.json'`), or when the user names the files.
- **Named files:** exactly those, whatever their type.
- **Pasted text:** save it to a `.md` file first.

Run `humanize start --dry-run <paths>` and tell the user the list and the word count. If there are more than 10 documents or more than 20,000 words, confirm before starting.

## 2. Start the run

`humanize start <paths> [--include PATTERN]` creates `<repo>/.runtime/humanize/<YYYYMMDDHHMMSS>/` with, for each document: a source snapshot, a brief, the path for `<name>.humanized.md`, and a report skeleton `<name>.humanized.report.md`. The sources are never modified.

<!-- humanize:worker:start -->
## Workers (Claude Code)

Each document is edited by its own fresh `humanize-editor` sub-agent: latest Opus at high reasoning, defined in `.claude/agents/humanize-editor.md`. Do not edit the documents yourself, and do not use another provider's agents.

For each document that `start` lists as "needs a worker", one at a time (the tool already finished the others: untouchable documents, protected documents with nothing to edit, and duplicates):

1. `humanize task --run <run-id> --doc <doc> --provider claude` prints its instruction.
2. Launch the Agent tool with `subagent_type: humanize-editor` and that instruction as the prompt, in the foreground. Wait for it to finish before starting the next document.

If the `humanize-editor` agent type is not available, stop and tell the user to reinstall humanize; do not fall back to a different model.
<!-- humanize:worker:end -->

Layout is part of every edit: when the gate checks a Markdown edit, the tool rejoins prose hard-wrapped mid-sentence and makes double spaces inside sentences single, then records what it fixed in the document's report and the run report. Each worker writes the edited document (text only, one line per paragraph), fills its report as an editor's change log (decisions, flagged items kept and why, notes for the author, anomalies, tool feedback), and runs the gate up to 3 times. A document that still fails after 3 gate runs is marked `failed`, with the reasons in its report.

## 3. Close the run

1. `humanize gate --run <run-id>` re-checks every document. Investigate any document that is missing or failed: re-launch its worker once, or record why not.
2. `humanize report --run <run-id>` writes `<run-id>.report.md`: an index of files, statistics, all notes, cross-document defined-term consistency, and the workers' anomalies and tool feedback.
3. Read every `<name>.humanized.report.md`, then replace the text between the `humanize:synthesis` markers in `<run-id>.report.md` with your synthesis:
   - anomalies that recur across documents;
   - suggestions for the document set as a whole;
   - suggestions for improving the humanize skill or tool, citing the reports.

   Re-running `humanize report` keeps your synthesis.
4. Deliver: the run folder, the pass/fail summary, the most important notes for the author, and the synthesis highlights.

## What the gate cannot see

It checks numbers, codes, quotes, emergency labels, defined terms, code blocks, negations, hedges, marked words, em dashes, headings, hard wraps and double spaces inside sentences, listed AI tells, JSON structure, and Vale. It cannot judge meaning; the workers are told to. When reviewing, look for added claims, commitments, causes, or doubt, and for dropped claims.

## Other commands

`humanize check|brief <file>` and `humanize gate <source> <edit> --mode <mode>` handle a single file without a run. When the user only wants hard-wrapped Markdown rejoined (sentences split across lines), use `humanize tidy --check <files or folders>` to find the files and `--write` to fix them in place; it changes nothing else and the rendered Markdown stays the same. `humanize runs` lists runs. If the gate reports `vale: skipped`, Vale is not set up: the other checks still run, and `humanize setup /absolute/path/to/repo` sets it up. Do not install anything without the user's go-ahead.
