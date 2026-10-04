"""Runs: folder intake, run folders under <repo>/.runtime/humanize/, manifests, batch gating, reports."""
import datetime
import fnmatch
import hashlib
import json
import os
import re
import secrets
import shutil
import subprocess
import sys
from pathlib import Path

from humanize import __version__, assess, env, gate, reports, text

DEFAULT_PATTERNS = ["*.md"]
SKIP_DIRS = {"node_modules", "__pycache__", "venv", "dist", "build", "site-packages"}
OUR_SUFFIXES = (".humanized", ".source", ".brief", ".notes", ".report")
MAX_ATTEMPTS = 3
STRUCTURED = {".json"}


def repo_root():
    return env.find_root() or Path.cwd()


def runs_dir(root=None):
    return (root or repo_root()) / ".runtime" / "humanize"


def _is_ours(path):
    stem = Path(path.stem)
    return any(stem.name.endswith(s) for s in OUR_SUFFIXES)


def _git_ignored(root, paths):
    if not paths or not env.has_git(root):
        return set()  # without git, folder scans simply do not filter gitignored files
    r = subprocess.run(["git", "-C", str(root), "check-ignore", "--stdin"], input="\n".join(map(str, paths)),
                       capture_output=True, text=True)
    return {Path(line).resolve() for line in r.stdout.splitlines() if line}


def collect(inputs, patterns=None, root=None):
    """Explicit files are always taken; folders are scanned for patterns (default *.md)."""
    root = root or repo_root()
    patterns = patterns or DEFAULT_PATTERNS
    explicit, scanned = [], []
    for raw in inputs:
        p = Path(raw).resolve()
        if p.is_file():
            explicit.append(p)
        elif p.is_dir():
            for dirpath, dirnames, filenames in os.walk(p):
                dirnames[:] = sorted(d for d in dirnames if not d.startswith(".") and d not in SKIP_DIRS)
                for name in sorted(filenames):
                    f = Path(dirpath) / name
                    if any(fnmatch.fnmatch(name, pat) for pat in patterns) and not _is_ours(f):
                        scanned.append(f)
        else:
            raise SystemExit(f"humanize: no such file or folder: {raw}")
    ignored = _git_ignored(root, scanned)
    seen, docs = set(), []
    for f in explicit + [s for s in scanned if s not in ignored]:
        if f not in seen:
            seen.add(f)
            docs.append(f)
    return docs, sorted(ignored)


def _rel(path, root, taken, external_base=None):
    try:
        rel = path.resolve().relative_to(root.resolve())
    except ValueError:
        base = external_base or path.parent
        rel = Path("_external") / path.resolve().relative_to(base)
    candidate, n = rel, 2
    while str(candidate) in taken:
        candidate = rel.with_name(f"{rel.stem}-{n}{rel.suffix}")
        n += 1
    return candidate


def _names(rel):
    ext = rel.suffix or ".txt"
    base = rel.with_suffix("")
    return {
        "source": str(base) + f".source{ext}",
        "brief": str(base) + ".brief.md",
        "edit": str(base) + f".humanized{ext}",
        "report": str(base) + ".humanized.report.md",
    }


def words(raw, kind):
    """Prose words: what humanize edits. Code blocks, front matter, and managed blocks are not counted."""
    return len(text.mask_code(gate.prose(raw, kind)).split())


def _kind(path):
    ext = path.suffix.lower()
    return "json" if ext == ".json" else ("markdown" if ext in (".md", ".markdown") else "text")


def _sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _manifest_path(run):
    return run / "run.json"


def load(run):
    """Load a run manifest; fill fields that runs from older versions lack."""
    manifest = json.loads(_manifest_path(run).read_text())
    for d in manifest["documents"]:
        d.setdefault("report", str(Path(d["edit"]).with_suffix("")).replace(".humanized", "") + ".humanized.report.md")
        d.setdefault("attempts", 1 if d.get("result") else 0)
    return manifest


def save(run, manifest):
    _manifest_path(run).write_text(json.dumps(manifest, indent=2) + "\n")


def resolve_run(ref, root=None):
    base = runs_dir(root)
    if ref in (None, "latest"):
        latest = base / "latest"
        if not latest.exists():
            raise SystemExit("humanize: no runs yet; start one with 'humanize start <files or folders>'")
        return latest.resolve()
    run = base / ref
    if not run.is_dir():
        raise SystemExit(f"humanize: no run {ref} in {base}")
    return run


def _new_run_dir(base):
    """Run folders are named by local time to the second (YYYYMMDDHHMMSS); a clash takes the next free second."""
    base.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now().astimezone().replace(microsecond=0)
    while True:
        run = base / stamp.strftime("%Y%m%d%H%M%S")
        try:
            run.mkdir()
            return run, stamp
        except FileExistsError:
            stamp += datetime.timedelta(seconds=1)


def _point_latest(base, run_id):
    tmp = base / f".latest-{secrets.token_hex(3)}"
    try:
        os.symlink(run_id, tmp)
        os.replace(tmp, base / "latest")
    except OSError:
        (base / "latest.txt").write_text(run_id + "\n")


def gitignore_warning(root):
    if not env.has_git(root):
        return None
    probe = root / ".runtime" / "humanize" / "probe.md"
    r = subprocess.run(["git", "-C", str(root), "check-ignore", "-q", str(probe)], capture_output=True)
    if r.returncode != 0:
        return f"warning: {root}/.runtime/ is not gitignored; humanized drafts could be committed. Add '.runtime/' to .gitignore."
    return None


def start(inputs, patterns=None, run_ref=None, vale_config=None, all_workers=False):
    root = repo_root()
    docs, _ = collect(inputs, patterns, root)
    if not docs:
        raise SystemExit("humanize: nothing to process (folders default to *.md; use --include or name files)")
    base = runs_dir(root)
    if run_ref:
        run = resolve_run(run_ref, root)
        manifest = load(run)
    else:
        run, created = _new_run_dir(base)
        manifest = {"run": run.name, "created": created.isoformat(timespec="seconds"),
                    "tool": f"humanize {__version__}", "repo": str(root), "documents": []}
    try:
        added = _add_documents(run, manifest, docs, root, vale_config, all_workers)
    except BaseException:
        if not run_ref:
            shutil.rmtree(run, ignore_errors=True)
        raise
    save(run, manifest)
    _point_latest(base, manifest["run"])
    return run, manifest, added, gitignore_warning(root)


def _run_glossary(docs, manifest):
    """Glossary terms from any document in the run that holds a Term table (a vocabulary or glossary)."""
    terms = set(manifest.get("glossary", []))
    for path in docs:
        if path.suffix.lower() in (".md", ".markdown"):
            terms.update(text.glossary_terms(path.read_text(errors="replace")))
    manifest["glossary"] = sorted(terms)
    return manifest["glossary"]


TOOL_WORKER = "none (completed by the humanize tool; no model)"


def _duplicate_report(run, doc, twin):
    """A copy's report: the tool's decision plus the original's notes for the author, refreshed at every gate."""
    twin_report = (run / twin["report"]).read_text() if (run / twin["report"]).exists() else ""
    notes = reports.notes(twin_report)
    text_ = reports.tool_report(doc["rel"], TOOL_WORKER, f"Identical to {twin['rel']} (same sha256); its edit is "
                                f"copied here. Its report has the editor's decisions.")
    if notes:
        text_ = text_.replace("## Notes for the author\n\n- None.", "## Notes for the author\n\n"
                              + "\n".join(f"- {n}" for n in notes))
    return text_


def _complete_by_tool(run, doc, why, edit_text):
    """Finish a document without a worker: write the edit and a filled report. The closing gate checks it."""
    (run / doc["edit"]).write_text(edit_text)
    doc["worker"] = "tool"
    (run / doc["report"]).write_text(reports.tool_report(doc["rel"], TOOL_WORKER, why))


def _add_documents(run, manifest, docs, root, vale_config, all_workers=False):
    glossary = _run_glossary(docs, manifest)
    taken = {d["rel"] for d in manifest["documents"]}
    sources = {d["source_path"] for d in manifest["documents"]}
    outside = [d for d in docs if not str(d).startswith(str(root.resolve()) + os.sep)]
    external_base = Path(os.path.commonpath([str(d.parent) for d in outside])).parent if outside else None
    added = []
    # Among identical files, the one with the shortest name is the original (status.md before status-copy.md);
    # originals are added first so their copies can point at them.
    groups = {}
    for path in docs:
        groups.setdefault(_sha(path), []).append(path)
    rank = {p: (0 if p == min(g, key=lambda q: (len(q.name), str(q))) else 1) for g in groups.values() for p in g}
    docs = sorted(docs, key=lambda p: rank[p])
    for path in docs:
        if str(path) in sources:
            continue
        rel = _rel(path, root, taken, external_base)
        taken.add(str(rel))
        names = _names(rel)
        (run / names["source"]).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, run / names["source"])
        source_text = path.read_text()
        result = assess.check(gate.prose(source_text, _kind(path)), vale_config, path.parent, glossary, _kind(path))
        doc = {"rel": str(rel), "source_path": str(path), "sha256": _sha(path), "kind": _kind(path),
               "mode": result["mode"]["mode"], "register": result["register"]["register"],
               "mode_evidence": result["mode"]["evidence"], **names, "status": "pending", "attempts": 0}
        write_brief(run, manifest["run"], doc, result)
        (run / doc["report"]).write_text(reports.skeleton(doc["rel"]))
        twin = next((d for d in manifest["documents"] if d["sha256"] == doc["sha256"]), None)
        if twin and not all_workers:
            doc["duplicate_of"] = twin["rel"]
            doc["worker"] = "tool"
            (run / doc["brief"]).write_text(f"# humanize brief: {doc['rel']}\n\nNo worker: identical to {twin['rel']} "
                                            f"(same sha256). The tool copies that document's edit and notes here.\n")
            (run / doc["report"]).write_text(_duplicate_report(run, doc, twin))
        elif not all_workers and not assess.needs_worker(result, doc["mode"]):
            if doc["mode"] == "untouchable" or doc["kind"] != "markdown":
                _complete_by_tool(run, doc, f"Mode {doc['mode']}: returned unchanged.", source_text)
            else:
                _complete_by_tool(run, doc, "Protected mode and the scan flagged no permitted edit, so no worker "
                                  "was needed. The tool applied layout only (see Facts).", text.tidy(source_text))
        manifest["documents"].append(doc)
        added.append(doc)
    return added


def write_brief(run, run_id, doc, result=None, vale_config=None, glossary=None):
    source_text = (run / doc["source"]).read_text()
    if result is None:
        result = assess.check(gate.prose(source_text, doc["kind"]), vale_config, None, glossary, doc["kind"])
    brief_text = assess.brief(doc["rel"], result, doc["mode"], doc["register"], kind=doc["kind"],
                              edit_path=str(run / doc["edit"]), notes_path=str(run / doc["report"]),
                              gate_cmd=f"humanize gate --run {run_id} --doc {doc['rel']}",
                              body=gate.prose(source_text, doc["kind"]))
    (run / doc["brief"]).write_text(brief_text)


def rebrief(run, doc_rel, mode=None, register=None):
    manifest = load(run)
    doc = _find(manifest, doc_rel)
    if mode:
        doc["mode"] = mode
    if register:
        doc["register"] = register
    write_brief(run, manifest["run"], doc, glossary=manifest.get("glossary"))
    save(run, manifest)
    return doc


def _find(manifest, doc_rel):
    for d in manifest["documents"]:
        if d["rel"] == doc_rel or d["source_path"] == str(Path(doc_rel).resolve()):
            return d
    raise SystemExit(f"humanize: {doc_rel} is not in run {manifest['run']}")


def tidy_doc(run, doc_rel, force=False):
    """Seed a document's edit with its tidied source (Markdown, not untouchable); other documents get a verbatim copy."""
    manifest = load(run)
    doc = _find(manifest, doc_rel)
    edit = run / doc["edit"]
    if edit.exists() and not force:
        sys.exit(f"humanize: {edit} already exists; edit it, or pass --force to start over from the source")
    source = (run / doc["source"]).read_text()
    if doc["kind"] == "markdown" and doc["mode"] != "untouchable":
        result = text.tidy(source)
        note = "written from the source, tidied" if result != source else "written from the source (already tidy)"
    else:
        result, note = source, f"copied verbatim ({doc['kind']}, mode {doc['mode']}: not tidied)"
    edit.write_text(result)
    return edit, note


def gate_run(run, doc_rel=None, allow=(), vale_config=None):
    if not doc_rel:  # the closing gate never judges a run while a worker is still writing
        from humanize import workers
        workers.wait_for_workers(run, "closing gate", include_queued=True)
    manifest = load(run)
    docs = [_find(manifest, doc_rel)] if doc_rel else manifest["documents"]
    for doc in docs:
        edit = run / doc["edit"]
        twin = _find(manifest, doc["duplicate_of"]) if doc.get("duplicate_of") else None
        if twin:
            if (run / twin["edit"]).exists():
                edit.write_text((run / twin["edit"]).read_text())
            (run / doc["report"]).write_text(_duplicate_report(run, doc, twin))
        if not edit.exists():
            doc.update({"status": "missing", "result": None})
            continue
        report_path = run / doc["report"]
        report_text = report_path.read_text() if report_path.exists() else reports.skeleton(doc["rel"])
        edit_text = edit.read_text()
        if doc["kind"] == "markdown" and doc["mode"] != "untouchable":
            # Layout is part of every edit: rejoin prose hard-wrapped mid-sentence and make double spaces inside
            # sentences single, whatever the worker wrote. Recorded in the report so the requester knows.
            source_text = (run / doc["source"]).read_text()
            doc["layout"] = {"source_wraps": len(text.hard_wraps(source_text)),
                             "source_spaces": len(text.inner_spaces(source_text)),
                             "draft_wraps": len(text.hard_wraps(edit_text)),
                             "draft_spaces": len(text.inner_spaces(edit_text))}
            tidied = text.tidy(edit_text)
            if tidied != edit_text:
                edit.write_text(tidied)
                edit_text = tidied
        r = gate.gate((run / doc["source"]).read_text(), edit_text, doc["mode"], doc["register"],
                      allow, vale_config, run, kind=doc["kind"],
                      notes_text="\n".join("Note: " + n for n in reports.notes(report_text)),
                      glossary=manifest.get("glossary"))
        if doc.get("worker") != "tool":
            # The worker's change log must be filled: a reminder on the worker's own gate runs (it may gate before
            # writing the report), a failure at the closing gate.
            gaps = reports.unfilled(report_text)
            r["checks"].append({"check": "report_complete",
                                "status": ("warn" if doc_rel else "fail") if gaps else "pass",
                                "detail": ("report not filled: " + ", ".join(gaps)) if gaps else ""})
            if gaps and not doc_rel:
                r["status"] = "fail"
        leftover = [l for l in edit_text.splitlines() if l.startswith(("Note:", "Run:"))]
        r["checks"].append({"check": "clean_document", "status": "fail" if leftover else "pass",
                            "detail": f"{len(leftover)} Note:/Run: line(s) belong in the report" if leftover else ""})
        if leftover:
            r["status"] = "fail"
        if doc_rel:  # a worker's gate run on its document; the orchestrator's whole-run check is not an attempt
            doc["attempts"] = doc.get("attempts", 0) + 1
        status = r["status"]
        if status == "fail" and doc["attempts"] >= MAX_ATTEMPTS:
            status = "failed"
        doc.update({"status": status, "result": r})
        src_body = text.mask_code(gate.prose((run / doc["source"]).read_text(), doc["kind"]))
        out_body = text.mask_code(gate.prose(edit_text, doc["kind"]))
        ratio = reports.change_ratio(src_body, out_body)
        report_path.write_text(reports.fill_facts(report_text, reports.facts_block(
            doc, r, max(doc["attempts"], 1), ratio, len(src_body.split()), len(out_body.split()), doc.get("layout"))))
    save(run, manifest)
    build_run_report(run, manifest)
    return manifest, docs


def build_run_report(run, manifest=None):
    manifest = manifest or load(run)
    per_doc, bodies = {}, {}
    for d in manifest["documents"]:
        src = (run / d["source"]).read_text()
        src_body = gate.prose(src, d["kind"])
        bodies[d["rel"]] = src_body
        edit = run / d["edit"]
        out_body = gate.prose(edit.read_text(), d["kind"]) if edit.exists() else ""
        rep = (run / d["report"]).read_text() if (run / d["report"]).exists() else ""
        worker = re.search(r"^Worker:\s*(.+)$", rep, re.M)
        worker = worker.group(1).strip() if worker and "(fill in" not in worker.group(1) else ""
        r = d.get("result") or {}
        per_doc[d["rel"]] = {
            "source_words": words(src, d["kind"]), "edit_words": words(edit.read_text(), d["kind"]) if edit.exists() else 0,
            "edited": edit.exists(),
            "ratio": reports.change_ratio(src_body, out_body) if out_body else 0.0,
            "vale": (r.get("run_line") or "").split("vale=")[-1] if r else "",
            "notes": reports.notes(rep), "worker": worker,
            "sections": {t: reports.section(rep, t) for t in ("Anomalies", "Tool feedback")},
            "unfilled": reports.unfilled(rep) if edit.exists() else [],
            "layout": d.get("layout"),
        }
    path = run / f"{manifest['run']}.report.md"
    previous = path.read_text() if path.exists() else ""
    path.write_text(reports.run_report(manifest, per_doc, reports.cross_document_terms(bodies), previous))
    return path


def list_runs(root=None):
    base = runs_dir(root)
    out = []
    if not base.is_dir():
        return out
    for run in sorted((p for p in base.iterdir() if p.is_dir() and not p.is_symlink()), reverse=True):
        try:
            m = load(run)
        except (OSError, json.JSONDecodeError):
            continue
        statuses = [d["status"] for d in m["documents"]]
        out.append({"run": m["run"], "created": m["created"], "documents": len(statuses),
                    "pass": statuses.count("pass"), "fail": statuses.count("fail") + statuses.count("failed"),
                    "pending": statuses.count("pending") + statuses.count("missing")})
    return out
