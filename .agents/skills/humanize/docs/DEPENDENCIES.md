# Dependencies and environment

Generated from `humanize/data/versions.json` for humanize 1.10.4; do not edit by hand. The same data is in the package's `MANIFEST.json`. Deployment: [DEPLOY.md](DEPLOY.md).

## Components

| Component | Version |
|---|---|
| tool | 1.10.4 |
| skill | 1.10.0 |
| worker-agent | 1.3.0 |
| lexicon | 1.6.0 |
| rules | 1.10.3 |
| vale | 3.24.0 |
| vale-style-Microsoft | 0.15.1 |
| vale-style-write-good | 0.4.1 |

## Dependencies

| Dependency | Needed | Version | How it is found | Notes |
|---|---|---|---|---|
| python | required | >=3.9 | $HUMANIZE_PYTHON; python3; python3.14 ... python3.9; /opt/homebrew/bin/python3; /usr/local/bin/python3; /usr/bin/python3 | standard library only; no pip packages |
| git | recommended |  |  | folder scans skip gitignored files and doctor checks .gitignore; without git both are skipped |
| vale | recommended | 3.24.0 | $HUMANIZE_VALE_BIN; <repo>/.runtime/humanize/tools/vale; the binary recorded at deploy (.runtime/humanize/state.json); PATH; /opt/homebrew/bin, /usr/local/bin, /usr/bin, ~/.local/bin | pinned release, SHA-256 verified on download; every other check runs without it |
| vale-styles | with vale | Microsoft 0.15.1, write-good 0.4.1 |  | synced into <repo>/.vale/styles by deploy, which also removes style folders that are no longer pinned |
| claude-code | for Claude Code workers |  |  | humanize-editor agent, model opus, effort high; loads skills and agents at session start; start a new session after deploy |
| codex-cli | for Codex workers |  | $HUMANIZE_CODEX_BIN; PATH; /opt/homebrew/bin, /usr/local/bin, ~/.local/bin, ~/.npm-global/bin; model list: $CODEX_HOME/models_cache.json (default ~/.codex), written once Codex has run | latest Sol model, model_reasoning_effort high; on Linux hosts that restrict unprivileged user namespaces (Ubuntu 24.04+ default), Codex's bubblewrap sandbox cannot start; allow bwrap in AppArmor or set sandbox_mode = "danger-full-access" in $CODEX_HOME/config.toml. doctor warns when this applies |
| network | at deploy only |  |  | Vale download and style sync; runs need no network (workers use their own provider) |

Vale release assets are pinned per platform (downloaded only when no matching system Vale exists):

- `darwin-arm64`: `vale_3.24.0_macOS_arm64.tar.gz`
- `darwin-x86_64`: `vale_3.24.0_macOS_64-bit.tar.gz`
- `linux-aarch64`: `vale_3.24.0_Linux_arm64.tar.gz`
- `linux-arm64`: `vale_3.24.0_Linux_arm64.tar.gz`
- `linux-x86_64`: `vale_3.24.0_Linux_64-bit.tar.gz`

## Environment variables

| Variable | Effect |
|---|---|
| `HUMANIZE_PYTHON` | Python 3.9+ to use for the launcher and deploy.sh |
| `HUMANIZE_VALE_BIN` | Vale binary to use |
| `HUMANIZE_CODEX_BIN` | codex CLI to use for Codex workers |
| `CODEX_HOME` | Codex home (model list); default ~/.codex |
| `XDG_CACHE_HOME` | base for the optional user-level Vale config (humanize setup --user); default ~/.cache |
| `PYTHONUTF8` | set to 1 by the launcher; the tool also switches to UTF-8 itself under a non-UTF-8 locale |

All of them are optional. Without them, humanize searches the locations above, which covers macOS (Homebrew on Apple silicon and Intel, the system Python) and Linux (distribution packages, `/usr/local`, `~/.local`), including agent shells with a minimal PATH.
