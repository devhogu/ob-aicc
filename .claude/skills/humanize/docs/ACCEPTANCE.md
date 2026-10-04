# Verify and accept a deployment

Run this flow after every deploy or update, before anyone relies on humanize in the repository. Steps 1 and 2 are automated, call no model, and take under a minute. Step 3 is optional and uses a real worker model. Deployment: [DEPLOY.md](DEPLOY.md).

In the commands below, `H` is the tool of the installation:

```sh
H=/path/to/repo/.claude/skills/humanize/bin/humanize      # Codex-only install: /path/to/repo/.agents/skills/humanize/bin/humanize
```

## Step 1: health check

```sh
$H doctor /path/to/repo
```

Pass: the last line is `doctor: READY`, and no line starts with `FAIL`. Exit code 0.

| Check | Confirms |
|---|---|
| `manifest` | `.humanize/manifest.json` exists; shows version, providers, install time |
| `files` | every installed file matches the sha256 recorded at deploy |
| `skill (claude)`, `skill (codex)` | each provider's skill is present, at this version, with its own worker section |
| `worker agent (claude)` | `.claude/agents/humanize-editor.md` uses model opus at effort high |
| `wiring (CLAUDE.md)`, `wiring (AGENTS.md)` | the managed humanize block is present |
| `gitignore` | `.runtime/` is ignored |
| `vale`, `vale styles` | the pinned Vale and styles are in place (or Vale was skipped on purpose) |
| `self-test gate` | the gate passes a known edit, with Vale |
| `codex worker model` | the latest Sol model is found; a `WARN` here means Codex has not run on this machine yet |
| `acceptance` | `WARN` until step 2 has passed for this version |

Checks for a provider you did not install are not shown.

## Step 2: acceptance test

```sh
$H accept /path/to/repo
```

Pass: the last line is `accept: ACCEPTED humanize <version> (12/12 checks)`. Exit code 0.

The test creates four sample documents in a temporary folder outside the repository, runs the whole workflow on them with a simulated worker, checks every stage, and cleans up after itself (the sample run is removed and `latest` points where it did before; `--keep` keeps the run for inspection).

| # | Check | Confirms |
|---|---|---|
| 1 | health check | step 1 passes |
| 2 | start a run | a run folder is created with all four documents |
| 3 | triage | only the document with real edits needs a worker; the tool finishes the agent rules and the code sample, and marks the copy as a copy |
| 4 | worker instruction | the instruction for this installation's provider is produced |
| 5 | worker gate run | a correct edit passes the worker's own gate |
| 6 | closing gate | the whole run passes: no failures, nothing missing |
| 7 | layout | the gate rejoined the hard-wrapped edit, made the double space inside a sentence single, and kept the double space between sentences |
| 8 | duplicate | the copy received the same edit |
| 9 | reports | the document report records "Layout (applied by humanize)" and the run report counts the tool-finished documents |
| 10 | tidy | `tidy --check` finds the wrapped samples and exits 1 |
| 11 | sources | the sample sources were not modified |
| 12 | Vale profile | clean governance text (obligations with "shall", passives with no named actor, defined terms in headings, "O!Bank") gets no Vale work items, so workers are not pushed toward harmful edits; skipped when the repository uses its own `.vale.ini` |

The result is recorded for this machine in `.runtime/humanize/acceptance.json` (gitignored; every machine that deploys accepts its own installation): version, components, providers, date, and every check. After a pass, `doctor` shows `OK acceptance: accepted <version> on <date>`.

## Step 3: live worker check (optional; uses a model)

Do this once per provider when model use is in scope, for example on first adoption or after an update that changes workers. Make a small sample in the repository, for example `docs/humanize-sample.md` with a few hard-wrapped sentences that say "leverage" and "seamless".

**Claude Code.** Start a new session in the repository (agents load at session start) and ask: `humanize docs/humanize-sample.md`.

**Codex.** From the repository: `codex exec "Humanize docs/humanize-sample.md."`

Pass when all of these hold:

- The assistant used the humanize workflow: it started a run under `.runtime/humanize/` and did not edit the document itself.
- The document report's Worker line names the expected worker: `claude opus (effort high)` for Claude Code, `codex <latest Sol> (effort high)` for Codex.
- `$H gate --run latest` exits 0, and the edited document has each paragraph on one line.
- `git status` shows the sample unchanged.
- Codex only: the session log shows one `humanize dispatch` per document that needed a worker, and no duplicate workers.

Delete the sample and its run afterwards.

## Accepting the deployment

The deployment is accepted, and humanize is active in the repository, when:

1. `doctor` reports `READY` with no `FAIL`;
2. `accept` reports `ACCEPTED` for the installed version on this machine (recorded in `.runtime/humanize/acceptance.json`);
3. if model use is in scope, step 3 passed for each provider you use.

The acceptance record is per machine and is not committed. To keep it on record, attach the `accept` output to your change or ticket.

## If something fails

- `doctor` FAIL: follow the troubleshooting table in [DEPLOY.md](DEPLOY.md), redeploy, and start again at step 1.
- `accept` NOT ACCEPTED: the failing check names the stage. Run `$H accept /path/to/repo --keep` to keep the sample run, inspect it under `.runtime/humanize/`, and redeploy the package. If it still fails, the package is faulty: report the failing check and `.runtime/humanize/acceptance.json` to whoever built it.
- Step 3 fails while steps 1 and 2 pass: the installation is sound and the problem is the assistant or the model setup (agent not loaded because the session predates the deploy, no Opus access, Codex not logged in). Fix that and repeat step 3.
