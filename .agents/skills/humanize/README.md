# humanize

A local, deterministic tool plus a thin Claude Code / Codex skill for line-editing AI-drafted prose so it reads like a careful human wrote it, without changing what it says. It works like `graphify` in code-only mode: the tool never calls a model. The chat agent writes; `humanize` selects the documents, briefs each edit, and verifies the result.

## Documentation

| Guide | For |
|---|---|
| [docs/DEPLOY.md](docs/DEPLOY.md) | deploy, update, and remove humanize; requirements; troubleshooting |
| [docs/ACCEPTANCE.md](docs/ACCEPTANCE.md) | verify and accept a deployment: `doctor`, the automated `accept` test, and an optional live worker check |
| [docs/USAGE.md](docs/USAGE.md) | how to use humanize from Claude Code or Codex, what a run produces, and how to adopt the edits |
| [docs/DEPENDENCIES.md](docs/DEPENDENCIES.md) | dependencies, versions, how each is found on macOS and Linux, environment variables (generated) |
| [CHANGELOG.md](CHANGELOG.md) | what changed in each version |

Quick start: `tar xzf humanize-<version>.tar.gz && humanize-<version>/deploy.sh /path/to/repo`, then run the `doctor` and `accept` commands that deploy prints.

## Commands

```
humanize start  <files/folders> [--include '*.json'] [--run latest] [--dry-run]   # open or extend a run
humanize gate   --run latest [--doc <doc>] [--allow TERM]                        # gate a run, write report.md
humanize brief  --run latest --doc <doc> --mode protected                        # re-brief one document
humanize runs                                                                    # list runs
humanize check  <file>                    # single-file pre-assessment
humanize brief  <file>                    # single-file brief
humanize gate   <source> <edit> --mode M  # single-file gate
humanize tidy   <file> [-o out] | --run latest --doc <doc>   # join mid-sentence hard wraps, single inner spaces
humanize tidy   --check|--write <files/folders> [--exclude 'archive/*']   # find / rejoin wrapped Markdown in place
humanize accept  [repo] [--keep]          # acceptance test of an installation (no model); records .runtime/humanize/acceptance.json
humanize dispatch --run latest --doc <doc>   # Codex: run one worker and wait (refuses while one runs for that document)
humanize setup  /abs/path/to/repo | --user   # --user writes ~/.cache/humanize/vale (outside the repo; optional)
```

Folders are scanned for `*.md` only (hidden folders, gitignored files, and humanize's own outputs are skipped). Add patterns with `--include`, or replace them with `--only`. Files you name are always taken, whatever their type.

## Modes

`standard` (internal or external register), `protected` (clinical, safety, procedural, and normative policy text: "shall" obligations and defined terms; restricted edits only), `untouchable` (contracts with legal markers, mostly-code files: returned unchanged). The suggestion comes with evidence; the agent can override it. In protected mode, defined terms and fenced code blocks must survive verbatim, and Vale findings are information, not instructions.

## Workflow (skill)

The skill is an orchestrator. For each document it launches a fresh worker, one at a time: on Claude Code a `humanize-editor` sub-agent (latest Opus, `effort: high`, installed in `.claude/agents/`); on Codex a `codex exec` worker on the latest Sol model (`humanize worker --provider codex` picks it from the Codex model list) with `model_reasoning_effort="high"`. Each provider's copy of the skill names only its own workers. A worker gets its instruction from `humanize task`, writes `<name>.humanized.md` (text only) and fills `<name>.humanized.report.md` (an editor's change log: decisions, flagged items kept and why, notes for the author, anomalies, tool feedback), and runs the gate up to 3 times (then the document is `failed`). The orchestrator closes the run with `humanize gate --run` and `humanize report --run`, then writes the synthesis section of `<run-id>.report.md`.

## Runs

Each `start` creates a run in the repository's `.runtime/` folder; source paths are mirrored, so same-named files never collide:

```
<repo>/.runtime/humanize/
├── latest -> 20261004113012
└── 20261004113012/                    # local date and time to the second
    ├── run.json                       # manifest: sources, sha256, modes, attempts, gate results
    ├── 20261004113012.report.md       # run report: index, statistics, notes, cross-document checks, synthesis
    └── docs/guide/
        ├── setup.source.md            # snapshot of the original
        ├── setup.brief.md             # edit instructions for the agent
        ├── setup.humanized.md         # the edit: original name + .humanized (text only)
        └── setup.humanized.report.md  # the worker's change log; facts filled in by the gate
```

JSON documents get `<name>.humanized.json` (prose strings edited, structure and non-prose values unchanged, enforced by the gate) and a `<name>.notes.md`. Files outside the repository go under `_external/`. Sources are never modified. `start` warns if `.runtime/` is not gitignored.

## Layout (`tidy`)

Models often wrap Markdown prose at the terminal width, which breaks sentences across lines. Markdown renders a line break inside a paragraph as a space, so `humanize tidy` joins those paragraphs and list items into one line each without changing the rendered document. It also makes a double space inside a sentence single. It keeps one-sentence-per-line paragraphs (a choice, not a wrap), spacing between sentences, blank lines, two-space line breaks, headings, labeled lines (`**Owner:** ...`), tables, code, front matter, and HTML. A break after a full stop also counts as a wrap when the document is wrapped elsewhere and the next word would not have fit within its wrap width. In a run this is part of every edit: each gate run applies it to the worker's Markdown edit and records it in the document's report ("Layout (applied by humanize)") and in the run report's summary and index, so whoever requested the run sees it was done. `tidy --check` finds wrapped Markdown files across folders (exit 1 if any, for CI or a hook); `--write` rejoins them in place. Deploy also adds a rule to `CLAUDE.md` and `AGENTS.md` telling agents never to hard-wrap Markdown prose, so new wraps are not written in the first place.

## Gate

The gate fails on lost or invented numbers and codes; lost quotes, emergency labels, or placeholders; bracketed words not in the source; em dashes; title-case headings; unresolved AI tells from the lexicon; Vale getting worse; changed JSON structure; Markdown paragraphs or list items hard-wrapped mid-sentence; double spaces inside a sentence; and (in protected mode) dropped negations or hedges. It cannot judge meaning: an invented commitment or a dropped claim still depends on the agent, which the skill tells it to check.

## Deploy (automated, versioned)

Build the package once, then deploy it into any repository with one command:

```
bin/humanize package --out dist                       # dist/humanize-<version>.tar.gz (+ .sha256)
tar xzf humanize-<version>.tar.gz
humanize-<version>/deploy.sh /path/to/repo   # idempotent: install, upgrade, or repair (relative paths are resolved)
```

`deploy` does everything, with no prompts:

| Step | Result |
|---|---|
| Preflight | Python 3.9+ check, platform detection |
| Skill + tool | `.claude/skills/humanize/` (Claude: Opus workers) and `.agents/skills/humanize/` (Codex: Sol workers), each with the tool in `bin/humanize`; `.claude/agents/humanize-editor.md` (model opus, effort high) |
| Vale | the pinned release (`versions.json`): the system `vale` if it is that version, otherwise downloaded into `.runtime/humanize/tools/vale` with its SHA-256 verified against the release checksums. No Homebrew, no admin rights |
| Vale config | `.vale.ini` (managed, pinned style releases) and `vale sync` into `.vale/styles/`. An existing unmanaged `.vale.ini` is kept as house style |
| Wiring | a managed `humanize` block in `CLAUDE.md` and `AGENTS.md` (created if missing) and in `.gitignore` (`.runtime/`, `.vale/styles/`) |
| Manifest | `.humanize/manifest.json`: package and component versions, providers, Vale provisioning, and every installed file with its sha256 |

Options: `--providers claude,codex`, `--vale auto|download|system|skip`, `--dry-run`.

```
humanize doctor /path/to/repo      # verify: files vs. manifest, skills, agent, wiring, gitignore, Vale, styles, self-test
humanize uninstall /path/to/repo   # remove exactly what deploy installed (runs are kept; --purge-runs to delete them)
humanize version --components      # package and per-component versions
```

Deploying a newer package over an older one upgrades in place: changed files are replaced, files the new version no longer ships are removed, and blocks and the manifest are rewritten. Versions live in `humanize/data/versions.json` (package, tool, skill, worker agent, lexicon, rules, Vale, each Vale style).

Requirements: `python3` 3.9+ (standard library only) and network access for the first Vale download and style sync (a redeploy re-syncs only when the pinned style versions change).

Codex workers resolve the newest Sol model from Codex's own model list (`~/.codex/models_cache.json`), which exists once Codex has run on the machine. Until then `doctor` reports READY with a warning, and Claude workers and the tool work normally.

Outside the repository, deploy writes nothing. Vale itself may create its empty default folder (`~/Library/Application Support/vale` on macOS) the first time it runs; humanize does not use it. The tool needs nothing on PATH; to add a `humanize` command anyway: `uv tool install /path/to/this/folder`.

## Layout

- `SKILL.md`: intake rules and workflow for agents.
- `bin/humanize`: run without installing.
- `humanize/`: the package (`runs`, `assess`, `gate`, `lexicon`, `detect`, `vale`).
- `humanize/data/tells.json`: the AI-tell lexicon, each entry with its source.
- `humanize/data/rules/`: rules printed into briefs.
- `humanize/data/vendor/`: the MIT-licensed source rule sets (see `THIRD_PARTY.md`).
- `humanize/deploy.py`: deploy, doctor, uninstall, package.
- `humanize/data/versions.json`: package and component versions, pinned Vale and styles.
- `pyproject.toml`: packaging for `uv tool install`.
- `tests/`: layout test, output checker with cases and fixtures, golden baseline (source repository only; never packaged).
