"""Deterministic deployment: deploy, doctor, uninstall, package.

Everything humanize writes into a repository is recorded in <repo>/.humanize/manifest.json
(versions, providers, every file with its sha256, managed blocks, Vale provisioning), so a later
deploy upgrades exactly, doctor verifies exactly, and uninstall removes exactly what was installed.
"""
import datetime
import hashlib
import io
import json
import os
import platform
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path

from humanize import DATA, VERSIONS, __version__

PKG_ROOT = Path(__file__).resolve().parents[1]
PAYLOAD_EXCLUDE = {"tests", "dist", "build", "__pycache__", "install.sh", ".DS_Store"}
MANIFEST = Path(".humanize") / "manifest.json"
BLOCK_RE = r"<!-- humanize:begin[^\n]*-->.*?<!-- humanize:end -->\n?"
GITIGNORE_RE = r"# >>> humanize \(managed\) >>>.*?# <<< humanize \(managed\) <<<\n?"
MANAGED_VALE_HEADER = "# managed by humanize"
PROVIDERS = {
    "claude": {"skill": Path(".claude/skills/humanize"), "entry": "CLAUDE.md", "agent": Path(".claude/agents/humanize-editor.md")},
    "codex": {"skill": Path(".agents/skills/humanize"), "entry": "AGENTS.md", "agent": None},
}


class Log:
    def __init__(self, dry):
        self.dry, self.lines = dry, []

    def __call__(self, step, detail=""):
        line = f"{'[dry-run] ' if self.dry else ''}{step}" + (f": {detail}" if detail else "")
        self.lines.append(line)
        try:
            print(line, flush=True)
        except BrokenPipeError:  # output cut off (e.g. piped into head): finish the deploy silently
            sys.stdout = open(os.devnull, "w")


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _repo(path):
    root = Path(path).resolve()
    if not root.is_dir():
        raise SystemExit(f"humanize deploy: not a directory: {root}")
    return root


def _payload_files():
    for p in sorted(PKG_ROOT.rglob("*")):
        rel = p.relative_to(PKG_ROOT)
        if p.is_file() and not (set(rel.parts) & PAYLOAD_EXCLUDE) and not rel.name.endswith(".pyc"):
            yield rel


WORKER_BLOCK_RE = r"(<!-- humanize:worker:start -->\n).*?(\n<!-- humanize:worker:end -->)"
VERSION_LINE_RE = r"\n\nVersion: humanize [^\n]*\.\n"


def _skill_body(text):
    """SKILL.md without the provider's worker section and version line: the same in the package and every install."""
    text = re.sub(WORKER_BLOCK_RE, lambda m: m.group(1) + m.group(2), text, flags=re.S)
    return re.sub(VERSION_LINE_RE, "\n", text, count=1)


def compose_skill(provider):
    skill = _skill_body((PKG_ROOT / "SKILL.md").read_text())
    block = (DATA / "providers" / f"worker-{provider}.md").read_text().strip()
    skill = re.sub(WORKER_BLOCK_RE, lambda m: m.group(1) + block + m.group(2), skill, flags=re.S)
    return skill.replace("\n# Humanize\n", f"\n# Humanize\n\nVersion: humanize {__version__} ({provider}).\n", 1)


def _wiring_block(provider):
    worker = ("a fresh `humanize-editor` sub-agent (latest Opus, effort high)" if provider == "claude"
              else "a fresh Codex worker on the latest Sol model (reasoning effort high)")
    skill_dir = PROVIDERS[provider]["skill"]
    return (f"<!-- humanize:begin v{__version__} (managed by humanize deploy; edit outside this block) -->\n"
            f"## Humanize\n\n"
            f"To humanize, de-AI, or line-edit prose (one file, several, or a folder), use the `humanize` skill "
            f"(`/humanize`). It runs the local tool `{skill_dir}/bin/humanize` (not on PATH; call it by this path), which "
            f"never calls a model: each "
            f"document is edited by {worker}, gated, and reported under `.runtime/humanize/<YYYYMMDDHHMMSS>/`. "
            f"Folders default to Markdown files. Sources are never modified. Do not edit files under "
            f"`{skill_dir}/`; verify with `{skill_dir}/bin/humanize doctor .` and update by deploying a newer package.\n\n"
            f"When you write or edit Markdown, never hard-wrap prose to a line width: keep each paragraph and each list "
            f"item on one line, so no sentence is split across lines. Breaks between paragraphs, headings, list items, "
            f"and table rows stay as they are. To find wrapped files, run "
            f"`{skill_dir}/bin/humanize tidy --check <files or folders>`; to rejoin them, use `--write` (the rendered "
            f"Markdown does not change).\n"
            f"<!-- humanize:end -->\n")


def _upsert_block(path, block, pattern, log, dry, created):
    old = path.read_text() if path.exists() else None
    if old is None:
        new = block
        created.append(str(path.name))
    elif re.search(pattern, old, re.S):
        new = re.sub(pattern, lambda _: block, old, flags=re.S)
    else:
        new = old.rstrip("\n") + "\n\n" + block
    if new != old:
        log("update" if old is not None else "create", f"{path.name} (humanize block)")
        if not dry:
            path.write_text(new)
    else:
        log("unchanged", f"{path.name} (humanize block)")


def _remove_block(path, pattern, log):
    if path.exists():
        old = path.read_text()
        new = re.sub(r"\n*" + pattern, "\n", old, flags=re.S).rstrip("\n") + "\n"
        if new != old:
            if new.strip():
                path.write_text(new)
            else:
                path.unlink()
            log("removed block", path.name)


def _platform_key():
    system = {"darwin": "darwin", "linux": "linux"}.get(sys.platform)
    machine = platform.machine().lower()
    return f"{system}-{machine}" if system else None


def _vale_version(binary):
    try:
        out = subprocess.run([binary, "--version"], capture_output=True, text=True, timeout=20).stdout
        m = re.search(r"(\d+\.\d+\.\d+)", out)
        return m.group(1) if m else None
    except (OSError, subprocess.SubprocessError):
        return None


def _download(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def provision_vale(root, policy, log, dry):
    """Return {'binary', 'version', 'source'}; download the pinned release unless an identical one exists."""
    pinned = VERSIONS["components"]["vale"]
    tools = root / ".runtime" / "humanize" / "tools"
    local = tools / "vale"
    if policy == "skip":
        log("vale", "skipped by --vale skip (the gate will report vale: skipped)")
        return {"binary": None, "version": None, "source": "skipped"}
    if local.is_file() and _vale_version(str(local)) == pinned:
        log("vale", f"repo-local {pinned} already present")
        return {"binary": str(local.relative_to(root)), "version": pinned, "source": "downloaded"}
    system = shutil.which("vale")
    sys_version = _vale_version(system) if system else None
    if system and policy != "download" and (sys_version == pinned or policy == "system"):
        log("vale", f"using system vale {sys_version} at {system}")
        return {"binary": system, "version": sys_version, "source": "system"}
    if policy == "system":
        raise SystemExit("humanize deploy: --vale system requested but vale is not on PATH")
    key = _platform_key()
    asset_tpl = VERSIONS["vale"]["assets"].get(key or "")
    if not asset_tpl:
        raise SystemExit(f"humanize deploy: no pinned Vale build for platform {key}; install vale {pinned} and use --vale system")
    asset = asset_tpl.format(version=pinned)
    url = VERSIONS["vale"]["release"].format(version=pinned, asset=asset)
    sums_url = VERSIONS["vale"]["release"].format(version=pinned, asset=VERSIONS["vale"]["checksums"].format(version=pinned))
    log("vale", f"download pinned {pinned} ({asset}) to {local.relative_to(root)}"
        + (f"; system vale is {sys_version}" if sys_version else ""))
    if dry:
        return {"binary": str(local.relative_to(root)), "version": pinned, "source": "downloaded"}
    blob, sums = _download(url), _download(sums_url).decode()
    expected = next((l.split()[0] for l in sums.splitlines() if l.strip().endswith(asset)), None)
    actual = hashlib.sha256(blob).hexdigest()
    if expected != actual:
        raise SystemExit(f"humanize deploy: Vale checksum mismatch for {asset} (expected {expected}, got {actual})")
    log("vale", f"checksum verified ({actual[:16]}...)")
    tools.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(blob)) as tar:
        member = next(m for m in tar.getmembers() if Path(m.name).name == "vale")
        data = tar.extractfile(member).read()
    local.write_bytes(data)
    local.chmod(local.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return {"binary": str(local.relative_to(root)), "version": _vale_version(str(local)), "source": "downloaded"}


def _load_manifest(root):
    p = root / MANIFEST
    return json.loads(p.read_text()) if p.exists() else None


def deploy(repo, providers=("claude", "codex"), vale_policy="auto", dry=False):
    root = _repo(repo)
    log = Log(dry)
    old = _load_manifest(root)
    log("humanize deploy", f"{__version__} -> {root}"
        + (f" (upgrade from {old['package']})" if old and old["package"] != __version__ else
           " (reinstall)" if old else " (fresh install)"))
    if sys.version_info < tuple(int(x) for x in VERSIONS["requires"]["python"].split(".")):
        raise SystemExit(f"humanize deploy: Python {VERSIONS['requires']['python']}+ required")
    log("preflight", f"python {platform.python_version()} ({sys.executable}), platform {_platform_key()}, "
        f"git: {'repo' if (root / '.git').exists() else 'no repo'}{'' if shutil.which('git') else ' (git not installed)'}")
    problems = verify_package()
    if problems:
        raise SystemExit(f"humanize deploy: the package does not match its {PACKAGE_MANIFEST} "
                         f"({len(problems)} file(s), e.g. {problems[:3]}); download it again")
    log("package", "verified against MANIFEST.json" if problems == [] else "source tree (no MANIFEST.json)")
    if "codex" in providers:
        from humanize import workers
        if not workers.latest_sol():
            log("note", "codex: " + CODEX_LATER)

    files, created = {}, list(old.get("created", [])) if old else []
    for prov in providers:
        target = root / PROVIDERS[prov]["skill"]
        changed = 0
        for rel in _payload_files():
            dest = target / rel
            files[str(dest.relative_to(root))] = None
            if dry:
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            content = compose_skill(prov).encode() if rel == Path("SKILL.md") else (PKG_ROOT / rel).read_bytes()
            if not dest.exists() or dest.read_bytes() != content:
                changed += 1
                dest.write_bytes(content)
                shutil.copymode(PKG_ROOT / rel, dest)
        log("install skill + tool" if changed or dry else "unchanged",
            f"{prov} -> {PROVIDERS[prov]['skill']}" + (f" ({changed} file(s) written)" if changed else ""))
        if PROVIDERS[prov]["agent"]:
            agent = root / PROVIDERS[prov]["agent"]
            files[str(PROVIDERS[prov]["agent"])] = None
            src_agent = DATA / "agents" / "claude" / "humanize-editor.md"
            same = agent.exists() and agent.read_bytes() == src_agent.read_bytes()
            log("unchanged" if same else "install worker agent", str(PROVIDERS[prov]["agent"]))
            if not dry and not same:
                agent.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_agent, agent)

    if old:  # files from the previous version that this version no longer ships
        for rel in set(old.get("files", {})) - set(files):
            p = root / rel
            if p.exists() and _sha(p) == old["files"][rel]:
                log("remove obsolete", rel)
                if not dry:
                    p.unlink()

    vale = provision_vale(root, vale_policy, log, dry)
    vale_ini = root / ".vale.ini"
    from humanize import vale as _vale
    managed_text = _vale.config_text(".vale/styles",
                                     f"{MANAGED_VALE_HEADER} {__version__}; replaced on deploy, removed on uninstall\n")
    if not vale_ini.exists() or vale_ini.read_text().startswith(MANAGED_VALE_HEADER):
        log("unchanged" if vale_ini.exists() and vale_ini.read_text() == managed_text else "write",
            ".vale.ini (managed, pinned styles)")
        if not vale_ini.exists() and ".vale.ini" not in created:
            created.append(".vale.ini")
        if not dry and (not vale_ini.exists() or vale_ini.read_text() != managed_text):
            vale_ini.write_text(managed_text)
    else:
        log("keep", ".vale.ini exists and is not managed by humanize (used as house style)")
    stamp = root / ".vale" / "styles" / ".humanize-styles"
    pinned = json.dumps(VERSIONS["vale"]["styles"], sort_keys=True)
    styles_current = (stamp.exists() and stamp.read_text() == pinned
                      and all((root / ".vale" / "styles" / s).is_dir() for s in VERSIONS["vale"]["styles"]))
    if vale["binary"] and not dry and styles_current:
        log("unchanged", "vale styles (already at the pinned versions)")
    elif vale["binary"] and not dry:
        vbin = vale["binary"] if os.path.isabs(vale["binary"]) else str(root / vale["binary"])
        (root / ".vale" / "styles").mkdir(parents=True, exist_ok=True)
        r = subprocess.run([vbin, "sync"], cwd=root, capture_output=True, text=True)
        if vale_ini.exists() and vale_ini.read_text().startswith(MANAGED_VALE_HEADER):
            removed = _vale.prune_unpinned(root / ".vale" / "styles")
            if removed:
                log("vale styles", f"removed styles no longer pinned: {', '.join(removed)}")
        if r.returncode == 0:
            stamp.write_text(pinned)
        log("vale sync", "styles installed in .vale/styles" if r.returncode == 0 else f"FAILED: {r.stderr.strip()[:200]}")
    elif vale["binary"]:
        log("unchanged" if styles_current else "vale sync",
            "vale styles (already at the pinned versions)" if styles_current else "styles into .vale/styles")

    existing = re.sub(GITIGNORE_RE, "", (root / ".gitignore").read_text(), flags=re.S) if (root / ".gitignore").exists() else ""
    needed = [e for e in (".runtime/", ".vale/styles/") if not _ignored_elsewhere(root, e, existing)]
    gitignore = ("# >>> humanize (managed) >>>\n" + "".join(e + "\n" for e in needed)
                 + ("# (entries already present above)\n" if not needed else "") + "# <<< humanize (managed) <<<\n")
    _upsert_block(root / ".gitignore", gitignore, GITIGNORE_RE, log, dry, created)
    for prov in providers:
        _upsert_block(root / PROVIDERS[prov]["entry"], _wiring_block(prov), BLOCK_RE, log, dry, created)
    if not dry:
        (root / ".runtime" / "humanize").mkdir(parents=True, exist_ok=True)

    if dry:
        log("done", "dry run; nothing was changed")
        return 0
    manifest = {
        "package": __version__, "components": VERSIONS["components"],
        "installed": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "source": f"humanize {__version__} ({'package' if (PKG_ROOT / 'VERSION').exists() else 'source tree'})",
        "providers": list(providers), "vale": {"pinned": VERSIONS["components"]["vale"], "policy": vale_policy},
        "created": sorted(set(created)),
        "files": {rel: _sha(root / rel) for rel in sorted(files) if (root / rel).exists()},
    }
    (root / STATE).parent.mkdir(parents=True, exist_ok=True)
    state = json.dumps({"vale": vale, "deployed": manifest["installed"], "package": __version__}, indent=2) + "\n"
    if not (root / STATE).exists() or json.loads((root / STATE).read_text()).get("vale") != vale:
        (root / STATE).write_text(state)
    if (root / OLD_ACCEPTANCE).exists():  # 1.9.0 kept acceptance in the committed folder; it is per machine now
        (root / OLD_ACCEPTANCE).replace(root / ACCEPTANCE)
    if old and {k: v for k, v in old.items() if k != "installed"} == {k: v for k, v in manifest.items() if k != "installed"}:
        log("manifest", f"{MANIFEST} unchanged (already up to date)")
    else:
        (root / MANIFEST).parent.mkdir(exist_ok=True)
        (root / MANIFEST).write_text(json.dumps(manifest, indent=2) + "\n")
        log("manifest", f"{MANIFEST} ({len(manifest['files'])} files)")
    tool = root / PROVIDERS[providers[0]]["skill"] / "bin" / "humanize"
    log("done", f"humanize {__version__} deployed; verify with: {tool} doctor {root}; accept with: {tool} accept {root}")
    return 0


CODEX_LATER = ("no Codex model list on this machine yet (~/.codex/models_cache.json); Codex workers become available "
               "after Codex has run once here. Claude workers and the tool are unaffected.")


def doctor(repo):
    root = _repo(repo)
    m = _load_manifest(root)
    results, warnings = [], []

    def check(name, ok, detail="", warn=False):
        results.append((name, ok or warn, detail))
        if warn and not ok:
            warnings.append(name)
        print(f"{'OK  ' if ok else 'WARN' if warn else 'FAIL'} {name}" + (f": {detail}" if detail else ""), flush=True)

    if not m:
        check("manifest", False, f"{MANIFEST} not found; run humanize deploy")
        return 1
    check("manifest", True, f"humanize {m['package']}, providers {', '.join(m['providers'])}, installed {m['installed']}")
    if m["package"] != __version__:
        check("version", False, f"installed {m['package']}, this package is {__version__}; run humanize deploy to update")
    bad = [rel for rel, h in m["files"].items() if not (root / rel).exists() or _sha(root / rel) != h]
    check("files", not bad, f"{len(m['files'])} files match their recorded sha256" if not bad else
          f"{len(bad)} changed or missing, e.g. {bad[:3]}")
    for prov in m["providers"]:
        skill = root / PROVIDERS[prov]["skill"] / "SKILL.md"
        text_ = skill.read_text() if skill.exists() else ""
        want = "Workers (Claude Code)" if prov == "claude" else "Workers (Codex)"
        check(f"skill ({prov})", want in text_ and f"humanize {m['package']}" in text_, str(skill.relative_to(root)))
        if PROVIDERS[prov]["agent"]:
            agent = root / PROVIDERS[prov]["agent"]
            ok = agent.exists() and "model: opus" in agent.read_text() and "effort: high" in agent.read_text()
            check("worker agent (claude)", ok, f"{PROVIDERS[prov]['agent']} (model opus, effort high)")
        entry = root / PROVIDERS[prov]["entry"]
        check(f"wiring ({PROVIDERS[prov]['entry']})", entry.exists() and "<!-- humanize:begin" in entry.read_text())
    from humanize import env as _env
    if _env.has_git(root):
        probe = subprocess.run(["git", "-C", str(root), "check-ignore", "-q", ".runtime/humanize/x"], capture_output=True)
        check("gitignore", probe.returncode == 0, ".runtime/ and .vale/styles/ ignored")
    else:
        check("gitignore", True, "not a git repository or git not installed; the managed .gitignore block is in place")
    tool = root / PROVIDERS[m["providers"][0]]["skill"] / "bin" / "humanize"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    v = json.loads((root / STATE).read_text()).get("vale", {}) if (root / STATE).exists() else {}
    house_style = (root / ".vale.ini").exists() and not (root / ".vale.ini").read_text().startswith(MANAGED_VALE_HEADER)
    if not (root / STATE).exists():
        check("vale", False, "not provisioned on this machine (a fresh clone or pull); run deploy here")
    elif v.get("binary"):
        vbin = v["binary"] if os.path.isabs(v["binary"]) else str(root / v["binary"])
        ver = _vale_version(vbin)
        check("vale", ver == VERSIONS["components"]["vale"] or v.get("source") == "system", f"{vbin} ({ver})")
        styles = root / ".vale" / "styles"
        if house_style:
            check("vale styles", True, "the repository's own .vale.ini (house style) decides the styles; humanize keeps it")
        else:
            check("vale styles", all((styles / s).is_dir() for s in VERSIONS["vale"]["styles"]),
                  ", ".join(f"{s} {VERSIONS['components']['vale-style-' + s]}" for s in VERSIONS["vale"]["styles"]))
    else:
        check("vale", True, "not provisioned (--vale skip); gate runs without Vale")
    from humanize import vale as _vale, workers as _workers
    check("environment", True, f"python {platform.python_version()} ({sys.executable}); platform {_platform_key()}; "
          f"vale {_vale.binary(root) or 'not found'}; git {shutil.which('git') or 'not installed'}"
          + (f"; codex {_workers.codex_binary() or 'not found'}, model list {_workers.CODEX_MODELS}"
             if "codex" in m["providers"] else ""))
    st = DATA / "selftest"
    r = subprocess.run([str(tool), "gate", str(st / "source.md"), str(st / "edit.md"), "--mode", "standard",
                        "--register", "internal"], capture_output=True, text=True, cwd=root, env=env)
    run_line = next((l for l in r.stdout.splitlines() if l.startswith("Run:")), "")
    vale_ok = "vale=skipped" not in run_line or not v.get("binary") or house_style
    check("self-test gate", r.returncode == 0 and vale_ok, run_line or r.stdout.strip()[-200:] or r.stderr.strip()[-200:])
    if house_style and "vale=skipped" in run_line:
        check("house vale config", False, "Vale does not run with the repository's own .vale.ini (check its StylesPath "
              "and Packages, then run vale sync); every other gate check still runs", warn=True)
    w = subprocess.run([str(tool), "worker", "--provider", "codex"], capture_output=True, text=True, cwd=root, env=env)
    if "codex" in m["providers"]:
        model = next((l.split(": ", 1)[1] for l in w.stdout.splitlines() if l.startswith("model:")), "none")
        check("codex worker model", w.returncode == 0, f"latest Sol: {model}" if w.returncode == 0 else CODEX_LATER,
              warn=True)
        blocked = _workers.codex_sandbox_blocked()
        check("codex sandbox", not blocked, blocked or "Codex can run worker commands on this host", warn=True)
    acc = json.loads((root / ACCEPTANCE).read_text()) if (root / ACCEPTANCE).exists() else {}
    accepted = acc.get("accepted") and acc.get("package") == m["package"]
    check("acceptance", accepted, f"accepted {acc['package']} on {acc['date']}" if accepted else
          f"not yet accepted for {m['package']}; run: {tool} accept {root}", warn=True)
    ok = all(r[1] for r in results)
    print(f"doctor: {'READY' if ok else 'NOT READY'} ({sum(r[1] for r in results)}/{len(results)} checks"
          + (f"; {len(warnings)} warning(s): {', '.join(warnings)}" if warnings else "") + ")")
    return 0 if ok else 1


def uninstall(repo, force=False, purge_runs=False):
    root = _repo(repo)
    log = Log(False)
    m = _load_manifest(root)
    if not m:
        raise SystemExit(f"humanize uninstall: {MANIFEST} not found; nothing to remove")
    kept = []
    for rel, h in m["files"].items():
        p = root / rel
        if p.exists():
            if _sha(p) == h or force:
                p.unlink()
            else:
                kept.append(rel)
    for prov in m["providers"]:
        skill = root / PROVIDERS[prov]["skill"]
        if skill.exists():
            for cache in list(skill.rglob("__pycache__")):
                shutil.rmtree(cache, ignore_errors=True)
            for d in sorted((d for d in skill.rglob("*") if d.is_dir()), key=lambda d: -len(d.parts)) + [skill]:
                if d.exists() and not any(d.iterdir()):
                    d.rmdir()
        log("removed", f"{prov} skill and tool" + (" (some modified files kept)" if skill.exists() else ""))
        _remove_block(root / PROVIDERS[prov]["entry"], BLOCK_RE, log)
    vale_ini = root / ".vale.ini"
    if vale_ini.exists() and vale_ini.read_text().startswith(MANAGED_VALE_HEADER):
        vale_ini.unlink()
        shutil.rmtree(root / ".vale", ignore_errors=True)
        log("removed", ".vale.ini and .vale/styles")
    shutil.rmtree(root / ".runtime" / "humanize" / "tools", ignore_errors=True)
    _remove_block(root / ".gitignore", GITIGNORE_RE, log)
    if purge_runs:
        shutil.rmtree(root / ".runtime" / "humanize", ignore_errors=True)
        log("removed", ".runtime/humanize (runs)")
    (root / MANIFEST).unlink()
    (root / ACCEPTANCE).unlink(missing_ok=True)
    (root / OLD_ACCEPTANCE).unlink(missing_ok=True)
    (root / STATE).unlink(missing_ok=True)
    for d in [MANIFEST.parent, Path(".claude/agents"), Path(".claude/skills"), Path(".claude"),
              Path(".agents/skills"), Path(".agents"), Path(".runtime/humanize"), Path(".runtime")]:
        if (root / d).is_dir() and not any((root / d).iterdir()):
            (root / d).rmdir()
    if kept:
        log("kept (locally modified)", ", ".join(kept))
    log("done", f"humanize {m['package']} uninstalled" + ("" if purge_runs else "; runs in .runtime/humanize kept"))
    return 0


# Per-machine state lives under the gitignored .runtime/humanize/: the committed manifest stays identical on every
# machine, so a clone can pull a deployment and redeploy without a dirty tree.
STATE = Path(".runtime") / "humanize" / "state.json"           # how Vale was provisioned on this machine
ACCEPTANCE = Path(".runtime") / "humanize" / "acceptance.json"  # acceptance of this machine's installation
OLD_ACCEPTANCE = Path(".humanize") / "acceptance.json"          # before 1.9.1
PACKAGE_MANIFEST = "MANIFEST.json"


def verify_package():
    """Check the unpacked package against its MANIFEST.json before installing anything (None when deploying from a
    source tree, which has no manifest). Returns a list of problems."""
    path = PKG_ROOT / PACKAGE_MANIFEST
    if not path.exists():
        return None
    manifest = json.loads(path.read_text())
    problems = []
    for rel, h in manifest["files"].items():
        p = PKG_ROOT / rel
        if not p.is_file():
            problems.append(rel)
        elif _sha(p) != h and not (rel == "SKILL.md" and  # an installed copy carries its provider's worker section
                                   hashlib.sha256(_skill_body(p.read_text()).encode()).hexdigest()
                                   == manifest.get("skill_body_sha256")):
            problems.append(rel)
    return problems
SAMPLE_STATUS = ("This sprint the team will leverage the new pipeline to deliver a seamless rollout\n"
                 "for finance.  The  dashboards moved to the shared workspace, and two teams already\n"
                 "use them. The remaining 3 reports move on 14 November.\n")
SAMPLE_RULES = ("---\nname: sample-rules\ndescription: Sample agent rules for the humanize acceptance test.\n---\n\n"
                "You must run the checks before you open a pull request, and you must never push to\n"
                "main. Do not skip review. You must keep tests green. Never commit secrets. You must\n"
                "log decisions. Do not force-push. You must ask when you are unsure.\n")
SAMPLE_CODE = "```sh\necho one\necho two\necho three\n```\n"
# Clean governance text that the default Microsoft and write-good rules misread ("shorten shall", passives with no named
# actor, defined terms in headings, "significant change", "O!Bank"): the tuned profile must give it no Vale work items.
SAMPLE_GOVERNANCE = '# Engagement guide\n\n## AI Incident Review\n\nAn AI Incident is reviewed by the Control Function within five working days. The review record is retained for seven years. The Owner of the Initiative shall attend the review and shall bring the evidence pack.\n\n## 6. Single decisions of the Executive Sponsor\n\nThe Executive Sponsor decides on a significant change to a Solution. A significant change is any change that raises the Risk Tier. In addition to the review, the change is recorded in the Registry. Several reviewers may take part.\n\n## Step 2: the review\n\nEach agent that acts on Bank data is registered before use. O!Bank treats customers fairly, as the Fairness principle requires. When no owner is known, enter "none yet". The decision is published in the Registry by the next working day.\n'


def accept(repo, keep=False):
    """Acceptance test for an installed humanize: the health check, then the whole run lifecycle on sample documents
    with a simulated worker (no model is called). Records the result in .runtime/humanize/acceptance.json."""
    root = _repo(repo)
    m = _load_manifest(root)
    if not m:
        raise SystemExit(f"humanize accept: {MANIFEST} not found; deploy humanize first")
    provider = m["providers"][0]
    tool = str(root / PROVIDERS[provider]["skill"] / "bin" / "humanize")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    results = []

    def check(name, ok, detail=""):
        results.append({"check": name, "ok": bool(ok), "detail": detail})
        print(f"{'PASS' if ok else 'FAIL'} {name}" + (f": {detail}" if detail else ""), flush=True)
        return ok

    def run(*args):
        return subprocess.run([tool, *args], capture_output=True, text=True, cwd=root, env=env)

    r = run("doctor", str(root))
    check("1 health check (doctor)", r.returncode == 0, (r.stdout.strip().splitlines() or [""])[-1])
    runs_dir = root / ".runtime" / "humanize"
    latest = runs_dir / "latest"
    previous = os.readlink(latest) if latest.is_symlink() else None
    sample = Path(tempfile.mkdtemp(prefix="humanize-accept-"))
    run_dir = None
    try:
        docs = sample / "docs"
        docs.mkdir()
        (docs / "status.md").write_text(SAMPLE_STATUS)
        (docs / "status-copy.md").write_text(SAMPLE_STATUS)
        (docs / "rules.md").write_text(SAMPLE_RULES)
        (docs / "snippet.md").write_text(SAMPLE_CODE)

        r = run("start", str(docs), "--json")
        info = json.loads(r.stdout) if r.returncode == 0 else {}
        run_id = info.get("run")
        run_dir = runs_dir / run_id if run_id else None
        added = {Path(d["rel"]).name: d for d in info.get("added", [])}
        check("2 start a run", r.returncode == 0 and len(added) == 4, f"run {run_id}, {len(added)} documents")
        need = [n for n, d in added.items() if d.get("worker") != "tool"]
        check("3 triage: tool finishes what needs no worker", need == ["status.md"]
              and added.get("status-copy.md", {}).get("duplicate_of", "").endswith("status.md"),
              f"needs a worker: {', '.join(need) or 'none'}; copy of: {added.get('status-copy.md', {}).get('duplicate_of')}")
        status = added.get("status.md")
        if not (run_dir and status):
            raise RuntimeError("the run did not start; later checks skipped")
        r = run("task", "--run", run_id, "--doc", status["rel"], "--provider", provider)
        check("4 worker instruction", r.returncode == 0 and "humanize worker for exactly one document" in r.stdout,
              f"provider {provider}")

        # A simulated worker: a real edit, still hard-wrapped, and a filled change log.
        (run_dir / status["edit"]).write_text(SAMPLE_STATUS.replace("leverage", "use").replace("seamless", "[seamless]"))
        report = run_dir / status["report"]
        text_ = report.read_text().replace("(fill in: provider, model, effort)", "acceptance test (simulated worker)")
        for title in ("Decisions", "Flagged but kept", "Notes for the author", "Anomalies", "Tool feedback"):
            text_ = re.sub(rf"(## {re.escape(title)}\n\n)<!--.*?-->", rf"\1- Simulated entry.", text_, flags=re.S)
        report.write_text(text_)
        r = run("gate", "--run", run_id, "--doc", status["rel"])
        check("5 worker gate run", r.returncode == 0, (r.stdout.strip().splitlines() or [""])[0][:100])
        r = run("gate", "--run", run_id)
        check("6 closing gate (whole run)", r.returncode == 0,
              f"{r.stdout.count('PASS ')} pass, {r.stdout.count('FAIL ')} fail, {r.stdout.count('MISSING ')} missing")

        from humanize import text as _text
        edit = (run_dir / status["edit"]).read_text()
        check("7 layout applied to the edit", not _text.hard_wraps(edit) and not _text.inner_spaces(edit)
              and "finance.  The" in edit, "wraps rejoined, inner double space fixed, sentence spacing kept")
        copy = added["status-copy.md"]
        check("8 duplicate receives the edit", (run_dir / copy["edit"]).read_text() == edit)
        r = run("report", "--run", run_id)
        run_report = (run_dir / f"{run_id}.report.md").read_text()
        check("9 reports record layout and workers", "Layout (applied by humanize)" in report.read_text()
              and "the humanize tool, no model (3)" in run_report, "document report and run report")
        r = run("tidy", "--check", str(docs))
        check("10 tidy --check finds wrapped sources", r.returncode == 1, (r.stdout.strip().splitlines() or [""])[-1])
        check("11 sources unchanged", (docs / "status.md").read_text() == SAMPLE_STATUS)
        vale_ini = root / ".vale.ini"
        governance = sample / "governance.md"
        governance.write_text(SAMPLE_GOVERNANCE)
        if not vale_ini.exists() or not vale_ini.read_text().startswith(MANAGED_VALE_HEADER):
            check("12 Vale profile on clean governance text", True, "skipped: the repository uses its own .vale.ini")
        else:
            r = run("brief", str(governance), "--vale-config", str(vale_ini))
            items = [l for l in r.stdout.splitlines() if "(Vale " in l]
            skipped = "vale: skipped" in run("check", str(governance), "--vale-config", str(vale_ini)).stdout
            check("12 Vale profile on clean governance text", r.returncode == 0 and not items,
                  "Vale not provisioned; skipped" if skipped else
                  ("no Vale work items" if not items else f"{len(items)} unexpected: {items[0][:80]}"))
    except Exception as e:  # report, do not crash: the record says what failed
        check("lifecycle", False, str(e))
    finally:
        shutil.rmtree(sample, ignore_errors=True)
        if run_dir and not keep:
            shutil.rmtree(run_dir, ignore_errors=True)
            if latest.is_symlink():
                latest.unlink()
                if previous and (runs_dir / previous).exists():
                    latest.symlink_to(previous)
    ok = all(c["ok"] for c in results)
    record = {"package": m["package"], "components": m["components"], "providers": m["providers"],
              "accepted": ok, "date": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
              "checks": results, "kept_run": str(run_dir) if keep and run_dir else None}
    (root / ACCEPTANCE).write_text(json.dumps(record, indent=2) + "\n")
    print(f"accept: {'ACCEPTED' if ok else 'NOT ACCEPTED'} humanize {m['package']} "
          f"({sum(c['ok'] for c in results)}/{len(results)} checks); recorded in {ACCEPTANCE}")
    if ok:
        print("Optional live check with a real worker: see docs/ACCEPTANCE.md, step 3.")
    return 0 if ok else 1


DEPLOY_SH = """#!/bin/sh
# humanize {version}: deploy into a repository (idempotent). Usage: ./deploy.sh /path/to/repo [options]
# Options: --providers claude,codex  --vale auto|download|system|skip  --dry-run   (see: ./deploy.sh --help)
# Guides: docs/DEPLOY.md (deploy, update, remove), docs/ACCEPTANCE.md (verify and accept), docs/USAGE.md (use)
# Environment: HUMANIZE_PYTHON selects the Python (3.9+); see docs/DEPENDENCIES.md.
set -eu
DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
ok() {{ "$1" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' >/dev/null 2>&1; }}
PY=${{HUMANIZE_PYTHON:-}}
if [ -n "$PY" ]; then
  ok "$PY" || {{ echo "humanize: HUMANIZE_PYTHON=$PY is not Python 3.9+" >&2; exit 1; }}
else
  for c in python3 python3.14 python3.13 python3.12 python3.11 python3.10 python3.9 \\
           /opt/homebrew/bin/python3 /usr/local/bin/python3 /usr/bin/python3; do
    if command -v "$c" >/dev/null 2>&1 && ok "$c"; then PY=$(command -v "$c"); break; fi
  done
  [ -n "$PY" ] || {{ echo "humanize: Python 3.9+ not found; install it or set HUMANIZE_PYTHON" >&2; exit 1; }}
fi
export PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1
PYTHONPATH="$DIR${{PYTHONPATH:+:$PYTHONPATH}}" exec "$PY" -m humanize deploy "$@"
"""


def _package_data():
    m = re.search(r'(?m)^humanize = \[(.*)\]', (PKG_ROOT / "pyproject.toml").read_text())
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def _ignored_elsewhere(root, entry, gitignore_without_block):
    """Whether the repository already ignores `entry` through its own rules (not humanize's block), so deploy adds
    only what is missing: a repo with `/.runtime/*` plus `!/.runtime/.gitkeep` keeps its exception. Asks git when
    it can; without git, a literal line match."""
    from humanize import env as _env
    if not _env.has_git(root):
        return entry in {l.strip() for l in gitignore_without_block.splitlines()}
    probe = entry.rstrip("/") + "/humanize-probe"
    r = subprocess.run(["git", "-C", str(root), "check-ignore", "-v", "--no-index", probe], capture_output=True, text=True)
    if r.returncode != 0:
        return False
    source, line = r.stdout.split(":", 2)[:2]
    if Path(source).name == ".gitignore" and (root / ".gitignore").exists():
        text = (root / ".gitignore").read_text()
        m = re.search(GITIGNORE_RE, text, re.S)
        if m:  # the match comes from humanize's own block: not ignored elsewhere
            start = text.count("\n", 0, m.start()) + 1
            end = text.count("\n", 0, m.end()) + 1
            if start <= int(line) <= end:
                return False
    return True


def _sync_pyproject():
    """versions.json is the single source of the version; keep pyproject.toml in step before packaging."""
    path = PKG_ROOT / "pyproject.toml"
    if path.exists():
        text = path.read_text()
        synced = re.sub(r'(?m)^version = "[^"]*"', f'version = "{__version__}"', text, count=1)
        if synced != text:
            path.write_text(synced)


def _dependencies_doc():
    """docs/DEPENDENCIES.md, generated from versions.json so the guide always matches the pins."""
    v = VERSIONS
    lines = ["# Dependencies and environment", "",
             f"Generated from `humanize/data/versions.json` for humanize {__version__}; do not edit by hand. The same "
             "data is in the package's `MANIFEST.json`. Deployment: [DEPLOY.md](DEPLOY.md).", "",
             "## Components", "", "| Component | Version |", "|---|---|"]
    lines += [f"| {k} | {val} |" for k, val in v["components"].items()]
    lines += ["", "## Dependencies", "", "| Dependency | Needed | Version | How it is found | Notes |", "|---|---|---|---|---|"]
    for name, dep in v["dependencies"].items():
        found = "; ".join(dep.get("found_by", [])) or dep.get("model_list", "")
        if name == "codex-cli":
            found += f"; model list: {dep['model_list']}"
        version = dep.get("version") or ", ".join(f"{k} {val}" for k, val in dep.get("styles", {}).items())
        notes = dep.get("notes") or dep.get("worker", "")
        if dep.get("worker") and dep.get("notes"):
            notes = f"{dep['worker']}; {dep['notes']}"
        lines.append(f"| {name} | {dep['need']} | {version} | {found} | {notes} |")
    lines += ["", "Vale release assets are pinned per platform (downloaded only when no matching system Vale exists):", ""]
    lines += [f"- `{k}`: `{a.format(version=v['components']['vale'])}`" for k, a in sorted(v["vale"]["assets"].items())]
    lines += ["", "## Environment variables", "", "| Variable | Effect |", "|---|---|"]
    lines += [f"| `{k}` | {val} |" for k, val in v["environment"].items()]
    lines += ["", "All of them are optional. Without them, humanize searches the locations above, which covers macOS "
              "(Homebrew on Apple silicon and Intel, the system Python) and Linux (distribution packages, `/usr/local`, "
              "`~/.local`), including agent shells with a minimal PATH.", ""]
    return "\n".join(lines)


def package(out_dir):
    _sync_pyproject()
    (PKG_ROOT / "docs" / "DEPENDENCIES.md").write_text(_dependencies_doc())
    import fnmatch
    missing = [str(p.relative_to(PKG_ROOT)) for p in DATA.rglob("*") if p.is_file() and "__pycache__" not in p.parts
               and not any(fnmatch.fnmatch(str(p.relative_to(PKG_ROOT / "humanize")), g) for g in _package_data())]
    if missing:
        sys.exit(f"humanize package: data files not covered by pyproject package-data: {', '.join(missing)}")
    out = Path(out_dir).resolve()
    name = f"humanize-{__version__}"
    stage = Path(tempfile.mkdtemp()) / name
    for rel in _payload_files():
        (stage / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(PKG_ROOT / rel, stage / rel)
    (stage / "deploy.sh").write_text(DEPLOY_SH.format(version=__version__))
    (stage / "deploy.sh").chmod(0o755)
    (stage / "VERSION").write_text(__version__ + "\n")
    (stage / "versions.json").write_text((DATA / "versions.json").read_text())
    files = {str(p.relative_to(stage)): _sha(p) for p in sorted(stage.rglob("*")) if p.is_file()}
    (stage / PACKAGE_MANIFEST).write_text(json.dumps({
        "name": "humanize", "version": __version__,
        "built": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "components": VERSIONS["components"], "requires": VERSIONS["requires"],
        "dependencies": VERSIONS["dependencies"], "environment": VERSIONS["environment"],
        "skill_body_sha256": hashlib.sha256(_skill_body((stage / "SKILL.md").read_text()).encode()).hexdigest(),
        "files": files}, indent=2) + "\n")
    out.mkdir(parents=True, exist_ok=True)
    tgz = out / f"{name}.tar.gz"
    with tarfile.open(tgz, "w:gz") as tar:
        tar.add(stage, arcname=name, filter=lambda ti: None if "__pycache__" in ti.name else ti)
    (out / f"{name}.tar.gz.sha256").write_text(f"{_sha(tgz)}  {tgz.name}\n")
    shutil.rmtree(stage.parent, ignore_errors=True)
    print(tgz)
    return 0
