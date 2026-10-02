# aicc-deploy

Publishes the generated portal (`html/aicc/`) into the clean deploy repository and pushes it, so the web server updates itself. Rust, standard library only.

## How publishing works

1. Copy the site into `/devops/websvc/websvc-ob-aicc/html/aicc/` and commit it there.
2. Push `origin` (GitHub). This stores history and deploys nothing.
3. Push `websvc` (`websvc-host:/home/websvc/repos/aicc.git`). This runs the server's post-receive hook, which checks the files out into `/home/websvc/deploy/aicc`. Caddy serves that folder. No restart is needed.

`aicc-deploy --publish` does all three, then fetches `package-manifest.json` from the served URL and confirms it equals what was published.

## Use

```sh
cargo build --release --manifest-path deploy/Cargo.toml       # once, or after changing the tool
deploy/target/release/aicc-deploy                             # dry run (default): shows added, changed, removed; writes nothing
deploy/target/release/aicc-deploy --publish                   # mirror, commit, push origin then websvc, verify
```

`cargo` lives in `~/.cargo/bin`. Run from the repository root. Options: `aicc-deploy --help`.

## What it refuses

It stops with one message, before writing anything, when:

- `html/aicc` lacks `index.html`, `ru/index.html` or `en/index.html`;
- the source checkout has uncommitted changes to tracked files, or the generated site has uncommitted or untracked files (commit the rebuilt site first, so the manifest names a real commit);
- `python3 portal/tools/check.py --idempotent` fails, meaning `html/aicc` is not a verified fresh build;
- the deploy repository is not on `main`, lacks the `origin` or `websvc` remote, or has changes outside `html/aicc/`.

It only writes under `html/aicc/` in the deploy repository, never edits its README, `.gitignore` or git configuration, and never force-pushes. If a push fails, it says which remotes were already pushed and that the commit still exists locally.

## Manifest

`html/aicc/package-manifest.json` lists every published file with its SHA-256 and size, plus the source commit. It has no timestamp, so an unchanged site produces no commit. It is excluded when comparing folders and is rewritten only when something else changed.

## Roll back

In the deploy repository, `git revert <publish commit>`, then push `origin` and `websvc`. On the server, `sudo websvc-ctl redeploy aicc` re-checks out the bare repository's HEAD (operator).

## Tests

```sh
cargo test --offline --manifest-path deploy/Cargo.toml
```

Unit tests cover hashing (standard vectors), folder diff, manifest, HTTP client and safety checks. Integration tests run the real binary against temporary repositories with local bare remotes and never touch the real deploy repository. `deploy/verification/dry-run.txt` records a dry run against the real deploy repository.
