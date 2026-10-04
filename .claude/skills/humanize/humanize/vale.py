"""Vale integration: config resolution, runs, and comparison."""
import configparser
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from humanize import DATA

USER_CONFIG = Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache") / "humanize" / "vale" / ".vale.ini"


class Unavailable(Exception):
    pass


def _repo_root(start):
    from humanize import env
    return env.find_root(start)


def resolve_config(explicit=None, near=None):
    if explicit:
        return Path(explicit).resolve(), "--vale-config"
    if os.environ.get("HUMANIZER_VALE_CONFIG"):
        return Path(os.environ["HUMANIZER_VALE_CONFIG"]).resolve(), "HUMANIZER_VALE_CONFIG"
    for start in (Path.cwd(), near):
        root = _repo_root(start) if start else None
        if root and (root / ".vale.ini").is_file():
            return root / ".vale.ini", "repository .vale.ini"
    return USER_CONFIG, "user config (humanize setup --user)"


COMMON_BIN_DIRS = ("/opt/homebrew/bin", "/usr/local/bin", "/usr/bin", str(Path.home() / ".local" / "bin"))


def _executable(path):
    return bool(path) and Path(path).is_file() and os.access(path, os.X_OK)


def binary(near=None):
    """The Vale binary, found the same way in any shell (agent sandboxes often have a minimal PATH):
    $HUMANIZE_VALE_BIN, the repo's downloaded Vale, the Vale recorded at deploy, PATH, then common locations."""
    if os.environ.get("HUMANIZE_VALE_BIN"):
        return os.environ["HUMANIZE_VALE_BIN"]
    for start in (Path.cwd(), near):
        root = _repo_root(start) if start else None
        if not root:
            continue
        local = root / ".runtime" / "humanize" / "tools" / "vale"
        if _executable(local):
            return str(local)
        state = root / ".runtime" / "humanize" / "state.json"
        if state.exists():
            recorded = (json.loads(state.read_text()).get("vale") or {}).get("binary")
            recorded = recorded if not recorded or os.path.isabs(recorded) else str(root / recorded)
            if _executable(recorded):
                return recorded
    found = shutil.which("vale")
    return found or next((str(Path(d) / "vale") for d in COMMON_BIN_DIRS if _executable(Path(d) / "vale")), None)


def check_ready(config, near=None):
    if not binary(near):
        raise Unavailable("vale is not installed (run 'humanize deploy' to install the pinned version)")
    if not config.is_file():
        raise Unavailable(f"no Vale config; run 'humanize setup <repo>' or 'humanize setup --user'")
    parser = configparser.ConfigParser(strict=False, interpolation=None)
    parser.read_string("[root]\n" + config.read_text())
    styles = (config.parent / parser.get("root", "StylesPath", fallback="styles")).resolve()
    if not styles.is_dir() or not any(styles.iterdir()):
        raise Unavailable(f"Vale styles missing in {config.parent}; run 'humanize setup {config.parent}' "
                          "or redeploy humanize with --vale auto")


# Two spaces after a sentence are a spacing choice the edit keeps (see `text.tidy`), so Vale's spacing rule
# is not counted on those lines.
SENTENCE_GAP_RE = re.compile(r"[.!?:][\"')\]]* {2,}\S")


def run(body, config):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(body)
        path = f.name
    try:
        r = subprocess.run([binary(config.parent), f"--config={config}", "--output=JSON", path],
                           capture_output=True, text=True)
    finally:
        os.unlink(path)
    try:
        data = json.loads(r.stdout or "{}")
    except json.JSONDecodeError:
        raise Unavailable(f"vale failed: {(r.stderr or r.stdout).strip()[:200]}")
    gaps = {body.count("\n", 0, m.start()) + 1 for m in SENTENCE_GAP_RE.finditer(body)}
    alerts = [a for items in data.values() for a in items
              if not (a["Check"] == "Microsoft.Spacing" and a["Line"] in gaps)]
    counts = {"error": 0, "warning": 0, "suggestion": 0}
    for a in alerts:
        counts[a["Severity"]] = counts.get(a["Severity"], 0) + 1
    findings = [{"line": a["Line"], "severity": a["Severity"], "rule": a["Check"],
                 "text": " ".join(a.get("Match", "").split()), "message": a["Message"]}
                for a in alerts if a["Severity"] in ("error", "warning")]
    return {"counts": counts, "gate": counts["error"] + counts["warning"], "findings": findings}


def assess(body, config_arg=None, near=None):
    config, source = resolve_config(config_arg, near)
    try:
        check_ready(config, near)
    except Unavailable as e:
        return {"status": "skipped", "reason": str(e), "config": str(config), "config_source": source}
    result = run(body, config)
    result.update({"status": "ok", "config": str(config), "config_source": source})
    return result


def config_text(styles_path, header=""):
    """The managed Vale profile with its Packages line built from the pinned versions in versions.json."""
    from humanize import VERSIONS
    packages = ", ".join(VERSIONS["vale"]["styles"].values())
    text = (DATA / "vale.ini").read_text().replace("StylesPath = styles", f"StylesPath = {styles_path}")
    text = text.replace("Packages = (generated)", f"Packages = {packages}")
    return header + text


def prune_unpinned(styles_dir):
    """Remove everything in the humanize-managed .vale/styles folder that humanize does not pin: styles from earlier
    versions (vale sync never deletes) and package configs that Vale would merge into every config (.vale-config).
    A house-style configuration keeps whatever it has. Returns the removed names."""
    from humanize import VERSIONS
    keep = set(VERSIONS["vale"]["styles"])
    removed = []
    for d in Path(styles_dir).iterdir() if Path(styles_dir).is_dir() else ():
        if d.is_dir() and d.name not in keep:
            shutil.rmtree(d, ignore_errors=True)
            removed.append(d.name)
    return sorted(removed)


def setup(target_dir, styles_dir_name):
    """Write a Vale config into target_dir (if absent) and sync its styles."""
    target_dir.mkdir(parents=True, exist_ok=True)
    config = target_dir / ".vale.ini"
    created = False
    if not config.exists():
        config.write_text(config_text(styles_dir_name))
        created = True
    synced = False
    vale_bin = binary(target_dir)
    if vale_bin:
        (target_dir / styles_dir_name).mkdir(parents=True, exist_ok=True)
        subprocess.run([vale_bin, "sync"], cwd=target_dir, capture_output=True, text=True, check=True)
        synced = True
    return config, created, synced
