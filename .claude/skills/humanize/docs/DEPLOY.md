# Deploy, update, and remove humanize

This guide installs humanize into a repository, keeps it up to date, and removes it. Every step is one command; nothing asks questions. After any deploy or update, verify and accept the deployment with [ACCEPTANCE.md](ACCEPTANCE.md). How to use humanize once it is installed: [USAGE.md](USAGE.md).

## What a deployment adds

| What | Where |
|---|---|
| Skill and tool for Claude Code | `.claude/skills/humanize/` (the tool is `bin/humanize` inside it) |
| Worker agent for Claude Code (latest Opus, effort high) | `.claude/agents/humanize-editor.md` |
| Skill and tool for Codex (workers on the latest Sol, reasoning high) | `.agents/skills/humanize/` |
| Instructions for agents | a managed `humanize` block in `CLAUDE.md` and `AGENTS.md` (each file is created if missing; your own text is kept) |
| Vale (pinned version, checksum-verified) and its styles | the system `vale` if it is the pinned version, otherwise `.runtime/humanize/tools/vale`; styles in `.vale/styles/`; config in `.vale.ini` |
| Git ignores | a managed block in `.gitignore` with `.runtime/` and `.vale/styles/` (only the entries that are missing) |
| Record of what was installed | `.humanize/manifest.json`: package and component versions, providers, and the sha256 of every installed file; identical on every machine, so it can be committed |
| Per-machine state (gitignored) | `.runtime/humanize/state.json` (how Vale was provisioned here) and `.runtime/humanize/acceptance.json` (this machine's acceptance) |

Runs are written to `.runtime/humanize/<YYYYMMDDHHMMSS>/` when you use humanize. Sources are never modified.

## Requirements

- `python3` 3.9 or newer (standard library only) and `git`.
- Network access for the first Vale download and style sync.
- For Claude Code workers: Claude Code with access to Opus.
- For Codex workers: the Codex CLI, run at least once on the machine (it writes the model list humanize reads in `~/.codex/models_cache.json`). Without it, the deployment is still ready; `doctor` warns that Codex workers become available after Codex has run once.

Every dependency, the version pinned for it, and how humanize finds it on macOS and Linux are listed in [DEPENDENCIES.md](DEPENDENCIES.md). humanize searches the usual locations itself, so it works in agent shells with a minimal PATH; the environment variables there override the search (for example `HUMANIZE_PYTHON` on a server whose `python3` is older than 3.9).

humanize writes nothing outside the repository. Vale itself may create its empty default folder in your home the first time it runs (on macOS `~/Library/Application Support/vale`, on Linux `~/.config/vale`); humanize does not use it.

## 1. Get the package and check it

```sh
shasum -a 256 -c humanize-<version>.tar.gz.sha256      # expect: humanize-<version>.tar.gz: OK
tar xzf humanize-<version>.tar.gz
```

The package contains `deploy.sh`, `VERSION`, `versions.json`, `MANIFEST.json` (every file with its sha256, the components, and the dependency map), `CHANGELOG.md`, these docs, and the skill and tool. Deploy checks the unpacked files against `MANIFEST.json` before it installs anything and stops if any file differs.

## 2. Deploy

```sh
humanize-<version>/deploy.sh /path/to/repo
```

Options:

| Option | Effect |
|---|---|
| `--providers claude,codex` | which assistants to install for (default both) |
| `--vale auto` | default: use the system `vale` if it is the pinned version, otherwise download the pinned release and verify its SHA-256 |
| `--vale download` | always download the pinned release into `.runtime/humanize/tools/vale` |
| `--vale system` | use the `vale` on PATH, whatever its version |
| `--vale skip` | no Vale; every other check still runs |
| `--dry-run` | print what would change and change nothing |

The last line of the output names the commands for the next step:

```text
done: humanize <version> deployed; verify with: <repo>/.claude/skills/humanize/bin/humanize doctor <repo>; accept with: <repo>/.claude/skills/humanize/bin/humanize accept <repo>
```

Then:

1. Run the acceptance flow in [ACCEPTANCE.md](ACCEPTANCE.md).
2. Start a new Claude Code or Codex session in the repository. Both load skills and agents when a session starts, so a session that was already open does not see a fresh install.
3. Commit the deployment: the managed blocks in `CLAUDE.md`, `AGENTS.md`, and `.gitignore`, the installed folders, `.vale.ini`, and `.humanize/manifest.json`. Machine state (`.runtime/`, `.vale/styles/`) is ignored.

**Other clones of a repository with a committed deployment** pull the installed files, then run the same `deploy.sh` once on their machine. It provisions Vale and its styles locally, changes no tracked file, and leaves `git status` clean; then run `accept` there. Until then, `doctor` on that machine reports `vale: not provisioned on this machine`.

Deploy is idempotent: running it again on an up-to-date repository changes no file and reports `unchanged`. Running it on a damaged installation repairs it.

## 3. Update

Deploy the newer package the same way:

```sh
shasum -a 256 -c humanize-<new>.tar.gz.sha256
tar xzf humanize-<new>.tar.gz
humanize-<new>/deploy.sh /path/to/repo           # reports: upgrade from <old>
```

Changed files are replaced, files the new version no longer ships are removed, the managed blocks and the manifest are rewritten, and Vale styles re-sync only if their pinned versions changed. Runs are kept. What changed in each version is in `CHANGELOG.md`; the installed versions are shown by:

```sh
.claude/skills/humanize/bin/humanize version --components
```

After an update, `doctor` warns `not yet accepted for <new>` until you run the acceptance flow again. Start a new assistant session to load the new skill.

To roll back, deploy the previous package the same way.

## 4. Remove

```sh
.claude/skills/humanize/bin/humanize uninstall /path/to/repo
```

(Use `.agents/skills/humanize/bin/humanize` in a Codex-only install.)

Uninstall removes exactly what deploy installed: the skills and tool, the worker agent, the managed blocks (your own text in those files stays), the managed `.vale.ini`, `.vale/styles`, a downloaded Vale, `.humanize/`, and folders left empty. `git status` then shows the repository as it was before the deploy.

| Option | Effect |
|---|---|
| `--purge-runs` | also delete `.runtime/humanize` (runs are kept by default) |
| `--force` | also delete installed files you modified (they are kept and listed by default) |

## Troubleshooting

Run `doctor` first; every line names one check.

| `doctor` says | Fix |
|---|---|
| `FAIL files: N changed or missing` | someone edited installed files; redeploy the same package to restore them |
| `FAIL version: installed X, this package is Y` | you ran one version's tool against another's install; redeploy the package you want |
| `FAIL wiring (CLAUDE.md)` or `(AGENTS.md)` | the managed block was deleted; redeploy |
| `FAIL gitignore` | `.runtime/` is not ignored; redeploy, or add it yourself |
| `FAIL vale` or `FAIL vale styles` | redeploy with network access, or with `--vale download` |
| `deploy: the package does not match its MANIFEST.json` | the download or unpack is damaged; download the package again and check its sha256 |
| `Python 3.9+ not found` | install Python 3.9 or newer, or point `HUMANIZE_PYTHON` at one |
| `WARN codex worker model` | Codex has not run on this machine yet; run Codex once. Claude workers and the tool are unaffected |
| `WARN acceptance` | run the acceptance flow for this version |
| `WARN codex sandbox` (Linux) | the host restricts unprivileged user namespaces (Ubuntu 24.04+ default), so Codex's bubblewrap sandbox cannot start and Codex workers cannot run commands. An administrator can allow bwrap in AppArmor; otherwise set `sandbox_mode = "danger-full-access"` in `~/.codex/config.toml` (Codex then runs without a sandbox), or use Claude Code workers. humanize itself is unaffected |

If a `.vale.ini` already existed and was not written by humanize, deploy keeps it as your house style and Vale uses it.

Do not edit files under `.claude/skills/humanize/` or `.agents/skills/humanize/`: they are replaced on every deploy, and `doctor` reports edits. Change humanize by building a new package.
