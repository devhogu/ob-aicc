# Using humanize

humanize line-edits AI-drafted prose so it reads like a careful person wrote it, without changing what it says. You ask your assistant; the assistant runs the humanize workflow; a fresh worker edits each document; the local tool checks every edit. The tool itself never calls a model. Installation: [DEPLOY.md](DEPLOY.md).

## Ask for it

In Claude Code or Codex, in a repository where humanize is deployed:

```text
/humanize docs/guide.md
humanize the docs folder
humanize these files: notes/q3-update.md, README.md
```

| You give | humanize takes |
|---|---|
| A folder | its Markdown files (`*.md`), skipping hidden folders and gitignored files |
| Named files | exactly those, whatever their type (prose inside a `.json` file works too) |
| Pasted text | the assistant saves it to a `.md` file first |

To include other file types from a folder, say so ("also the JSON files"); the assistant adds `--include '*.json'`. For more than 10 documents or 20,000 words, the assistant tells you the size and asks before starting.

## What happens

1. **Start.** The tool snapshots each document into a new run folder, suggests a mode, and writes a brief for each document: what must survive word for word, a work list, and the rules for that mode.
2. **Triage.** The tool finishes, without a model, the documents that need no editor: untouchable documents, protected documents with nothing to edit, and exact copies of another document in the run.
3. **Edit.** Every other document goes to its own fresh worker, one document at a time:
   - Claude Code: the `humanize-editor` sub-agent (latest Opus, effort high).
   - Codex: a Codex worker on the latest Sol model (reasoning high), started with `humanize dispatch`, which also makes sure only one worker runs at a time.
4. **Gate.** Each edit is checked: numbers, codes, quotes, defined terms, code blocks, placeholders, negations and hedges (protected mode), headings, em dashes, listed AI tells, JSON structure, and Vale must not get worse. Vale runs Microsoft (company and tech writing) and write-good (general prose), tuned so clean governance text gets no work items. The gate also rejoins prose that is hard-wrapped mid-sentence and makes double spaces inside sentences single, and records that it did. A worker gets up to 3 gate runs; after that the document is marked `failed` with the reasons.
5. **Report.** The assistant closes the run, writes a synthesis, and tells you the results.

## What you get

```text
<repo>/.runtime/humanize/
├── latest -> 20261004113012
└── 20261004113012/
    ├── 20261004113012.report.md        # run report: summary, index, notes, consistency, synthesis
    ├── run.json                        # machine-readable state of the run
    └── docs/guide/
        ├── setup.source.md             # snapshot of the original
        ├── setup.brief.md              # what the worker was told
        ├── setup.humanized.md          # the edited document
        └── setup.humanized.report.md   # the editor's change log
```

Read the run report first. Its **Summary** gives pass/fail counts, words, who edited what (worker or tool), and the layout fixes. Its **Index** has one row per document. **Notes for the author** collects what the editors could not fix without you: missing figures, unsupported claims, jargon the reader may not know.

Each document report starts with **Facts** written by the tool (gate result, words changed, mode, layout applied), then the editor's change log: decisions, items flagged but kept, notes for the author, anomalies found in the source, and feedback about the tool.

Words in square brackets, like `a [seamless] rollout`, are words the editor would cut because they add no checkable claim. Keep the word by deleting the brackets, or delete the word.

## Use the results

Sources are never changed. To adopt an edit, review it and copy it over the original:

```sh
diff -u docs/guide/setup.md .runtime/humanize/latest/docs/guide/setup.humanized.md
cp .runtime/humanize/latest/docs/guide/setup.humanized.md docs/guide/setup.md
```

Resolve the bracketed words and the notes for the author before you publish.

## Modes

| Mode | For | What the editor may do |
|---|---|---|
| standard (internal or external register) | status updates, memos, emails, proposals, docs | a full line edit: cut filler and AI tells, plain words, varied rhythm |
| protected | clinical, safety, procedural, or policy text; agent instructions; glossaries | only a short list of permitted edits (filler, inflated words, hedge stacks, punctuation, heading case, layout); never the meaning, an instruction, a number, or a qualifier |
| untouchable | contracts, legal or regulated text, commit messages, changelogs, mostly-code files | nothing: returned unchanged |

The tool suggests the mode with its evidence; the worker can switch to protected mode when the text needs it and says why.

## Commands for direct use

The assistant runs these for you. Call the tool by its path (`.claude/skills/humanize/bin/humanize`, or `.agents/skills/humanize/bin/humanize` in a Codex-only install); it is not on PATH.

| Command | Does |
|---|---|
| `start <files/folders> [--include '*.json'] [--dry-run]` | open a run (`--dry-run`: list documents and word counts only) |
| `task --run <id> --doc <doc> --provider claude` | print the instruction for one worker |
| `dispatch --run <id> --doc <doc>` | Codex: run one worker and wait for it |
| `gate --run <id> [--doc <doc>]` | check one document or the whole run (exit 1 if anything fails) |
| `report --run <id>` | rebuild the run report (keeps the synthesis) |
| `runs` | list runs |
| `check <file>` / `brief <file>` / `gate <source> <edit> --mode <mode>` | single-file checks without a run |
| `tidy <file>`, `tidy --check <paths>`, `tidy --write <paths>` | find or rejoin hard-wrapped Markdown and double spaces inside sentences; nothing else changes |
| `doctor`, `accept`, `version --components`, `uninstall` | operate the installation ([DEPLOY.md](DEPLOY.md), [ACCEPTANCE.md](ACCEPTANCE.md)) |

`tidy --check` exits 1 when it finds wrapped files, so it can run in CI or a pre-commit hook.

## Limits

- The gate checks mechanics; it cannot judge meaning. Workers are told to add no claim, commitment, cause, or doubt and to drop none; when you review, look for exactly that.
- humanize edits wording, not substance. It does not fact-check, restructure an argument, or write missing content; it asks for it in the notes.
- Do not use it for code, commit messages, PR descriptions, changelogs, contract terms, regulated disclosures, or fiction.
