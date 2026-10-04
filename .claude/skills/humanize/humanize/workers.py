"""Worker model resolution: Claude uses the latest Opus; Codex uses the latest Sol. Both at high reasoning."""
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

from humanize import text

CODEX_MODELS = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") / "models_cache.json"
CODEX_BIN_DIRS = ("/opt/homebrew/bin", "/usr/local/bin", str(Path.home() / ".local" / "bin"),
                  str(Path.home() / ".npm-global" / "bin"))


USERNS_RESTRICTION = Path("/proc/sys/kernel/apparmor_restrict_unprivileged_userns")


def codex_sandbox_blocked():
    """On Linux hosts that restrict unprivileged user namespaces (the Ubuntu 24.04+ default), Codex's bubblewrap
    sandbox cannot start, so a Codex worker cannot run commands unless Codex runs without that sandbox. Returns a
    reason string when that applies, else None."""
    if not sys.platform.startswith("linux") or not USERNS_RESTRICTION.exists():
        return None
    if USERNS_RESTRICTION.read_text().strip() != "1":
        return None
    config = CODEX_MODELS.parent / "config.toml"
    mode = re.search(r'(?m)^\s*sandbox_mode\s*=\s*"([^"]+)"', config.read_text()) if config.exists() else None
    if mode and mode.group(1) == "danger-full-access":
        return None
    return ("this host restricts unprivileged user namespaces (kernel.apparmor_restrict_unprivileged_userns=1), so "
            "Codex's bubblewrap sandbox cannot start and Codex workers cannot run commands. Fix one of: allow bwrap in "
            "AppArmor (administrator), set sandbox_mode = \"danger-full-access\" in "
            f"{config} (no sandbox), or use Claude Code workers")


def codex_binary():
    """$HUMANIZE_CODEX_BIN, then PATH, then common install locations (agent shells often have a minimal PATH)."""
    if os.environ.get("HUMANIZE_CODEX_BIN"):
        return os.environ["HUMANIZE_CODEX_BIN"]
    found = shutil.which("codex")
    return found or next((str(Path(d) / "codex") for d in CODEX_BIN_DIRS if (Path(d) / "codex").is_file()), None)
EFFORT = "high"
CLAUDE_MIN = (5, 5)


def _version(slug):
    m = re.search(r"gpt-(\d+(?:\.\d+)*)-sol\b", slug)
    return tuple(int(x) for x in m.group(1).split(".")) if m else None


def latest_sol(cache=CODEX_MODELS):
    if not cache.is_file():
        return None
    slugs = set(re.findall(r'"(gpt-\d+(?:\.\d+)*-sol)"', cache.read_text()))
    ranked = sorted((v, s) for s in slugs if (v := _version(s)))
    return ranked[-1][1] if ranked else None


def resolve(provider):
    if provider == "claude":
        return {"provider": "claude", "agent": "humanize-editor", "model": "opus", "effort": EFFORT,
                "note": f"the 'opus' alias resolves to the latest Opus; it must be {'.'.join(map(str, CLAUDE_MIN))} or newer"}
    model = latest_sol()
    if not model:
        return {"provider": "codex", "model": None, "effort": EFFORT,
                "error": f"no Sol model found in {CODEX_MODELS}; stop and tell the user"}
    return {"provider": "codex", "model": model, "effort": EFFORT,
            "command": f'codex exec -m {model} -c model_reasoning_effort="{EFFORT}" -C <repo> "<task>"'}


def _alive(pid):
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ValueError):
        return False


RUN_LOCK = ".worker.lock"
WAIT_LIMIT = 4 * 3600


def running_worker(run):
    """(pid, document) of the worker currently running in this run, or None (stale locks are removed)."""
    lock = run / RUN_LOCK
    if not lock.exists():
        return None
    pid, _, rel = lock.read_text().partition(" ")
    if pid.isdigit() and _alive(int(pid)):
        return int(pid), rel.strip()
    lock.unlink(missing_ok=True)
    return None


def queued_dispatch(run):
    """(pid, document) of a dispatch that holds a document lock (running or waiting its turn), or None."""
    for lock in sorted(run.rglob("*.worker.lock")):
        pid = lock.read_text().strip()
        if pid.isdigit() and int(pid) != os.getpid() and _alive(int(pid)):
            return int(pid), str(lock.relative_to(run)).replace(".worker.lock", "")
    return None


def wait_for_workers(run, what, include_queued=False):
    """Block until no worker is running in the run (and, for the closing gate, none is queued); say once what is
    being waited for."""
    told, start = False, time.time()
    while ((busy := running_worker(run) or (queued_dispatch(run) if include_queued else None))
           and time.time() - start < WAIT_LIMIT):
        if not told:
            print(f"{what}: waiting for the worker on {busy[1]} (pid {busy[0]}) to finish; documents run one at a "
                  f"time", flush=True)
            told = True
        time.sleep(5)


def _acquire_run_lock(run, rel):
    start = time.time()
    while True:
        try:
            fd = os.open(run / RUN_LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(fd, "w") as f:
                f.write(f"{os.getpid()} {rel}")
            return
        except FileExistsError:
            if time.time() - start > WAIT_LIMIT:
                raise SystemExit(f"humanize: gave up waiting for the run's current worker after {WAIT_LIMIT}s")
            wait_for_workers(run, rel)


def _release_run_lock(run):
    lock = run / RUN_LOCK
    if lock.exists() and lock.read_text().partition(" ")[0] == str(os.getpid()):
        lock.unlink(missing_ok=True)


def dispatch(run, manifest, doc, force=False):
    """Run one Codex worker for one document and return when it exits. A per-document lock makes a second
    dispatch refuse while a worker is still running, so an orchestrator whose shell returned early cannot start
    a duplicate worker. Returns (exit code, message)."""
    if doc.get("worker") == "tool":
        return 0, f"{doc['rel']}: no worker needed (finished by the tool)"
    if doc.get("status") == "pass" and not force:
        return 0, f"{doc['rel']}: already passed; nothing to do (use --force to run it again)"
    info = resolve("codex")
    if info.get("error"):
        return 2, info["error"]
    base = run / doc["brief"].replace(".brief.md", "")
    lock, task, result, log = (Path(f"{base}.worker.lock"), Path(f"{base}.task.txt"),
                               Path(f"{base}.task.result.txt"), Path(f"{base}.worker.log"))
    if lock.exists():
        pid = int(lock.read_text().strip() or 0)
        if _alive(pid):
            return 3, (f"{doc['rel']}: a worker is already running (pid {pid}). Wait for it to finish; "
                       f"do not start another.")
        lock.unlink()
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return 3, f"{doc['rel']}: a worker was just started by another process; wait for it to finish."
    with os.fdopen(fd, "w") as f:
        f.write(str(os.getpid()))
    try:
        # One worker per run at a time: wait here until the run's current worker exits, even if the orchestrator
        # moved on early because its shell returned before the previous dispatch finished.
        _acquire_run_lock(run, doc["rel"])
    except BaseException:
        lock.unlink(missing_ok=True)
        raise
    try:
        task.write_text(task_prompt(run, manifest["run"], doc, label(info)))
        codex = codex_binary()
        if not codex:
            raise FileNotFoundError
        cmd = [codex, "exec", "-m", info["model"], "-c", f'model_reasoning_effort="{EFFORT}"',
               "-C", manifest["repo"], "-o", str(result), "-"]
        with task.open() as stdin, log.open("w") as out:
            code = subprocess.run(cmd, stdin=stdin, stdout=out, stderr=subprocess.STDOUT).returncode
    except FileNotFoundError:
        return 2, "codex CLI not found on PATH; install Codex or use the Claude Code skill"
    finally:
        lock.unlink(missing_ok=True)
        _release_run_lock(run)
    reply = result.read_text().strip().splitlines()[-1] if result.exists() and result.read_text().strip() else ""
    return code, f"{doc['rel']}: worker exited {code}; reply: {reply or '(none)'}; log: {log}"


def label(info):
    return f"{info['provider']} {info.get('model') or '?'} (effort {info['effort']})"


def task_prompt(run, run_id, doc, provider):
    """The self-contained instruction a worker receives for one document."""
    gate = f"humanize gate --run {run_id} --doc {doc['rel']}"
    return text.tidy(f"""You are the humanize worker for exactly one document. Work only on it.

Document: {doc['rel']} (mode {doc['mode']}{', register ' + doc['register'] if doc['mode'] == 'standard' else ''})
Brief (read first, follow exactly): {run / doc['brief']}
Original snapshot (read-only): {run / doc['source']}
Write the edited document to: {run / doc['edit']}
Fill in your report: {run / doc['report']}

Rules:
1. Follow the brief: its must-keep items, work list, and rules. The work list is a floor; fix what it missed too.
   If the suggested mode is wrong (clinical, safety, procedural, or normative policy text belongs in protected mode),
   run `humanize brief --run {run_id} --doc {doc['rel']} --mode protected`, then follow the new brief.
2. The edited document holds only the edited text: no Note: lines, no Run: line, no commentary. Write each paragraph
   and list item on one line. Layout is part of the job and the tool does it: each gate run rejoins prose that is
   hard-wrapped mid-sentence and makes double spaces inside sentences single in your edit, and records that in the
   report's facts. Do not repeat it under Decisions.
3. The report is an editor's change log. Keep the facts block as it is and fill every section: Decisions;
   Flagged but kept; Notes for the author; Anomalies; Tool feedback. Set the Worker line to: {provider}.
4. Run `{gate}`. Fix every FAIL and run it again. Stop after 3 runs: if it still fails, explain why under
   Decisions and Tool feedback.
5. Never edit the original source file, other documents in the run, or files outside this run folder.
6. Before finishing, check that the edit adds no claim, commitment, cause, or doubt and drops no claim;
   the gate cannot judge meaning.

Run `humanize` as the command if it is on PATH, otherwise as {Path(__file__).resolve().parents[1] / 'bin' / 'humanize'}.
Reply with one line: the gate result and the number of gate runs.""")
