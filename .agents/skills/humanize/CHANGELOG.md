# Changelog

Versions follow `humanize/data/versions.json`, which also records each component's version (`humanize version --components`). Deploy a newer package over an older one to upgrade; `humanize doctor` verifies the result.

## 1.10.4

- Deploy asks git which paths a repository already ignores (discounting humanize's own block) and adds only the missing entries to its `.gitignore` block. A repository that ignores `/.runtime/*` with an exception for `.runtime/.gitkeep` no longer gets a redundant `.runtime/` line that would override the exception. Without git, the literal line check remains.

## 1.10.3

- Removed proselint, Voices, and the curated ai-tells rules after a blind A/B test: 8 AI-drafted business documents, each edited by a humanize-editor worker with and without them (separate repositories, same humanize otherwise), judged by two independent reviewers who did not know which edit was which. On the 4 documents where these styles changed the brief, the edits without them won 4-0 (4 ties) with half the meaning errors (6 vs 12), and AI-sounding residue was the same (24 vs 22). humanize's own word list and register rules had already removed 24 of the 29 phrases these styles target; their main effect was pressure toward edits that change meaning (proselint's "Very" rule pushed a worker to weaken "very positive" to "positive"). On the 4 documents with identical briefs the split was 4-2 either way, which is the noise between two workers.
- Removed Readability too: its scores never showed value in either evaluation and its targets (Flesch reading ease above 70) do not suit governance text; the information line it added to briefs is gone.
- Kept: Microsoft and write-good with the golden-set tuning, the only part with measured value (clean governance text: 440 noisy work items to 0).
- Deploy removes everything in the managed `.vale/styles` that is not pinned (earlier styles, `.vale-config`), which replaces the separate package-config cleanup.
- `tests/test_vale_profile.py` now also checks that AI wording is still caught by humanize's word list and that no removed style is active.

## 1.10.2

- The golden-set tuning is now guarded: `tests/test_vale_profile.py` fails if clean governance text gets any Vale work item, or if the kept rules stop catching AI wording (opening cliches, empty value verdicts, weak verbs, closing pleasantries). The fixture is synthetic and reproduces every pattern the default rules misread on the charter; under the 1.9.2 profile it produced 17 work items, under 1.10.1 none.
- `doctor` handles a repository with its own `.vale.ini` (house style): it no longer expects humanize's styles or fails the self-test, and warns if that config cannot run Vale.
- `humanize accept` adds check 12, so every deployment proves the tuned profile is active: the same clean governance text gets no Vale work items (skipped when the repository uses its own `.vale.ini`).

## 1.10.1

Vale tuned on the AICC charter golden set: 37 documents and 69,000 words of clean, human-reviewed governance text, with 137 findings across 20 rules judged blind by two independent reviewers (FIX, KEEP, or HARM). Only 7% were worth fixing and 48% would have done harm. Rules that fired on clean text and were wrong there are now information only (write-good Passive, TooWordy, and Weasel; Microsoft Headings, HeadingAcronyms, Terms, and FirstPerson; ai-tells OverusedVocabulary) or off (Microsoft Quotes, HeadingColons, and Spacing). Among the reasons: TooWordy flagged "shall", Headings and HeadingAcronyms flagged document names and defined terms, Terms turned "agent" into "assistant", OverusedVocabulary flagged defined triggers such as "significant change", and Spacing misread "O!Bank". humanize's own word list and heading check cover the same ground with defined-term and document-name awareness.

Result: gate items on the charter fell from 1,229 to 4 (the rules judged correct: Voices WeakVerbs and write-good ThereIs), while the AI-drafted fixtures keep 43 real catches (inflated words, AI vocabulary, clichés, padding, stacked hedges, closing pleasantries, puffery).

## 1.10.0

- Vale styles: Microsoft (company and tech), write-good and proselint (general prose), Voices and Readability (plain language and readability), and 13 curated ai-tells rules (AI-written prose), all pinned in `versions.json`. Chosen by benchmarking every candidate on 38,000 words of fixtures and policy text: Google duplicated Microsoft alert for alert, RedHat and Elastic target product documentation, AiTells was mostly duplicate passive-voice alerts, Harper fired one rule, Voices' Simple and Direct voices were noise, and the full ai-tells style flagged policy enumerations and formal semicolons as AI tells.
- Readability scores are information: one compact line in each brief and in `humanize check` (for example "Flesch reading ease score 58.8 (target above 70)"), never gate items.
- Several styles flagging the same words on the same line become one work item; a Vale finding without a humanize hint shows Vale's own advice.
- Package configs that `vale sync` stores in `.vale/styles/.vale-config` are removed after every sync: Vale would merge them into every config, silently enabling extra styles and changing ignored scopes.
- The `Packages` line of every generated `.vale.ini` is built from `versions.json`, so the config and the pins cannot drift.

## 1.9.2

- Linux: `doctor` warns (`codex sandbox`) when the host restricts unprivileged user namespaces (`kernel.apparmor_restrict_unprivileged_userns=1`, the Ubuntu 24.04+ default) and Codex is not configured to run without its sandbox, because Codex's bubblewrap sandbox then cannot start and Codex workers cannot run commands. The fix options are in `docs/DEPLOY.md`. Found while validating on Ubuntu 26.04, where humanize itself, Claude Code, and Codex without the sandbox all worked.

## 1.9.1

- The committed install record is machine-independent: Vale provisioning moved from `.humanize/manifest.json` to `.runtime/humanize/state.json`, and the acceptance record to `.runtime/humanize/acceptance.json` (both gitignored, per machine; 1.9.0 records are migrated on deploy). A clone that pulls a committed deployment runs `deploy.sh` once to provision its own Vale; tracked files stay unchanged and `git status` stays clean.
- `doctor` on a machine that has the files but no local provisioning reports `vale: not provisioned on this machine` with the fix.

## 1.9.0

- Clean package: `MANIFEST.json` lists every file with its sha256 plus the components and the dependency map; deploy verifies the unpacked package against it before installing. `docs/DEPENDENCIES.md` is generated from `versions.json`.
- Runtime discovery on macOS and Linux, including agent shells with a minimal PATH: the launcher and `deploy.sh` find Python 3.9+ (`HUMANIZE_PYTHON`, `python3`, versioned names, common locations) and follow symlinks; Vale is found via `HUMANIZE_VALE_BIN`, the repo's download, the binary recorded at deploy, PATH, and common locations; Codex via `HUMANIZE_CODEX_BIN`, PATH, and common locations, with the model list under `$CODEX_HOME`.
- UTF-8 everywhere: the launcher sets `PYTHONUTF8=1`, and the tool switches to UTF-8 itself under a C/POSIX locale.
- git is optional: without it, folder scans do not filter gitignored files and doctor skips the gitignore probe. The user-level Vale config follows `XDG_CACHE_HOME`.
- `doctor` prints an environment line (Python, platform, Vale, git, Codex); deploy's preflight shows the Python in use.
- Deploying from an installed copy no longer adds a second version line to SKILL.md.

## 1.8.0

- Documentation ships in the package and is installed with the skill: `docs/DEPLOY.md` (deploy, update, remove, troubleshooting), `docs/ACCEPTANCE.md` (verify and accept a deployment), and `docs/USAGE.md` (how to use humanize and adopt its edits).
- `humanize accept [repo] [--keep]`: an automated acceptance test of an installation. It runs `doctor`, then the whole run lifecycle on sample documents with a simulated worker (no model), checks triage, gates, layout, duplicates, reports, tidy, and that sources are untouched, cleans up, and records the result in `.humanize/acceptance.json`.
- `doctor` shows whether the installed version has been accepted (a warning until it has); deploy prints the `accept` command; uninstall removes the acceptance record.

## 1.7.0

Validated end to end with the Codex CLI (0.160): a Codex-only deploy, skill discovery from `.agents/skills`, and a Codex orchestrator running Sol workers on a real run.

- `humanize dispatch --run <id> --doc <doc>` runs the Codex worker for one document and returns when it exits. A per-document lock makes a second dispatch refuse (exit 3) while a worker is running. The Codex skill uses it instead of hand-written `codex exec` lines, because a Codex orchestrator whose shell returned early started a duplicate worker on the same document.
- In a Codex install, `start` prints the `dispatch` command for each document that needs a worker.
- One worker per run at a time is enforced by the tool, not left to the orchestrator: a dispatch for the next document waits until the current worker exits, and the closing `gate --run` waits for running and queued dispatches. (A Codex orchestrator whose shell returned early had moved on to the next document while the first worker was still running.)
- Layout: a short line followed by a short word is a deliberate break, not a wrap ("Best regards," then "Sam"); wrapping at a width leaves short lines only at the end of a paragraph.

## 1.6.0

- The tool finishes documents that need no worker: untouchable documents, protected documents with no permitted edit flagged (layout only), and exact duplicates of another document in the run. `start` lists each document as "needs a worker" or "done by the tool"; `--all-workers` turns this off.
- Lexicon: "harness" is flagged only as a verb ("harness the power"), not as the software noun; "navigate to" a page is not flagged; comma-separated word lists count as mentions, not uses.
- Gate: untouchable documents are checked only for being unchanged.
- Packaging keeps `pyproject.toml` in step with `versions.json` and refuses to build if a data file is missing from the package data.
- Production acceptance (two independent passes, Python 3.9.6):
  - Deploy is READY on a machine where Codex has never run: `doctor` warns that Codex workers become available after Codex runs once, and deploy says so in its preflight.
  - A redeploy touches no file: Vale styles re-sync only when the pinned versions change, and the log says "unchanged".
  - A deploy whose output is cut off (for example piped into `head`) still completes; `deploy.sh` writes no bytecode caches outside the repository.
  - The closing gate fails a document whose worker report is not filled (Worker line and every section); a worker's own gate run shows it as a warning.
  - `start` prints the exact `task` command for each document that needs a worker and the closing commands with the tool's real path.
  - Duplicates: the file with the shortest name is the original; the copy's brief and report say so from the start, and its report carries the original's notes.
  - Word counts are prose words (code, front matter, and managed blocks excluded) everywhere; tool-finished documents report "finished by the tool, no worker" instead of an attempt count.

## 1.5.0

- Mode detection: clinical and care signals need care context (a patient, your child, medication, a carer), so software words such as "diagnose", "behavior", and "parent/child" no longer trigger protected mode. Agent instructions (skill or role front matter, or dense must/never/do-not rules) and glossaries suggest protected mode.
- Mentions of AI tells (quoted, in backticks, in replacement maps, short table cells, definition heads) are not counted as uses.
- Front matter and managed blocks (`<!-- name:begin -->` ... `<!-- name:end -->`) are kept verbatim and not scanned.
- Gate findings say "edit line"; brief line numbers refer to the source.

## 1.4.0

- Layout is part of every edit: each gate run rejoins Markdown prose hard-wrapped mid-sentence and makes double spaces inside sentences single, and records it in the document report and the run report.
- Stricter table and HTML detection, so wraps next to inline-code pipes or `<placeholders>` are found.

## 1.3.0

- `humanize tidy --check|--write <files or folders>` finds and rejoins wrapped Markdown across folders (exit 1 with `--check` if any, for CI or hooks).
- A break after a full stop counts as a wrap when the document is wrapped elsewhere and the next word would not have fit.
- Deploy adds a no-hard-wrap rule to the managed block in `CLAUDE.md` and `AGENTS.md`.

## 1.2.0

- `humanize tidy` and the gate checks `no_hard_wraps` and `no_inner_double_spaces`.
- Vale's spacing rule no longer counts a double space after a sentence; headings may capitalize the first word after a colon.

## 1.1.1

- Deploy output and wiring use the full tool path; `.gitignore` gets only missing entries; the manifest records the package version; a redeploy rewrites nothing.

## 1.1.0

- First automated, versioned package: `deploy.sh`, `doctor`, `uninstall`, `package`, pinned Vale with checksum verification, managed wiring for Claude Code and Codex.
