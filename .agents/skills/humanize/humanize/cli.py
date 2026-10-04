"""humanize command line."""
import argparse
import json
import shlex
import sys
from pathlib import Path

from humanize import VERSIONS, __version__, assess, gate, runs, text, vale, workers


def _read(path):
    if path == "-":
        return sys.stdin.read(), None
    p = Path(path)
    if not p.is_file():
        sys.exit(f"humanize: not a file: {path}")
    return p.read_text(), p.resolve().parent


def _provider():
    """The provider this copy was installed for: .agents/skills/humanize is Codex; anything else is Claude Code."""
    return "codex" if ".agents" in Path(__file__).resolve().parts else "claude"


def _tool_path():
    """How to call this tool: `humanize` when it is on PATH, else its bin/humanize path relative to the cwd."""
    import shutil
    here = Path(__file__).resolve().parents[1] / "bin" / "humanize"
    on_path = shutil.which("humanize")
    if on_path and Path(on_path).resolve() == here.resolve():
        return "humanize"
    try:
        return str(here.relative_to(Path.cwd()))
    except ValueError:
        return str(here)


def _kind(path):
    return "markdown" if path == "-" else runs._kind(Path(path))


def _ensure_utf8():
    """Text files are UTF-8. Under a non-UTF-8 locale (C/POSIX on Linux servers) re-run in Python's UTF-8 mode."""
    import locale
    import os
    if sys.flags.utf8_mode or "utf" in (locale.getpreferredencoding(False) or "").lower():
        return
    if os.environ.get("PYTHONUTF8") != "1":
        os.environ["PYTHONUTF8"] = "1"
        os.execv(sys.executable, [sys.executable, "-m", "humanize", *sys.argv[1:]])


def main(argv=None):
    if argv is None:
        _ensure_utf8()
    p = argparse.ArgumentParser(prog="humanize",
                                description="Deterministic pre/post assessment for line-editing AI-drafted prose. "
                                            "No model calls: the agent rewrites, humanize checks.")
    sub = p.add_subparsers(dest="cmd", required=True)

    st = sub.add_parser("start", help="start a run over files and/or folders (folders default to *.md)")
    st.add_argument("paths", nargs="+", help="files (any type) and/or folders")
    st.add_argument("--include", action="append", default=[],
                    help="extra filename pattern for folder scans, e.g. '*.json' (default: *.md)")
    st.add_argument("--only", action="append", default=[], help="replace the default pattern instead of adding to it")
    st.add_argument("--run", help="add to an existing run (ID or 'latest') instead of starting a new one")
    st.add_argument("--dry-run", action="store_true", help="list the documents that would be included, change nothing")
    st.add_argument("--all-workers", action="store_true",
                    help="send every document to a worker (default: the tool finishes untouchable documents, protected "
                         "documents with no permitted edit flagged, and duplicates)")
    st.add_argument("--json", action="store_true")
    st.add_argument("--vale-config")

    rs = sub.add_parser("runs", help="list runs in <repo>/.runtime/humanize")
    rs.add_argument("--json", action="store_true")

    c = sub.add_parser("check", help="pre-assessment of one file: Vale, tells, protected items, mode and register")
    c.add_argument("file", help="source file or - for stdin")
    c.add_argument("--json", action="store_true")
    c.add_argument("--vale-config")

    b = sub.add_parser("brief", help="edit instructions for one file, or re-brief a run document with a new mode")
    b.add_argument("file", nargs="?")
    b.add_argument("--run", help="run ID or 'latest' (with --doc)")
    b.add_argument("--doc", help="document path as listed in the run")
    b.add_argument("--mode", choices=["standard", "protected", "untouchable"])
    b.add_argument("--register", choices=["internal", "external"])
    b.add_argument("--vale-config")

    g = sub.add_parser("gate", help="post-assessment: one source/edit pair, or a whole run (exit 1 on any fail)")
    g.add_argument("source", nargs="?")
    g.add_argument("edit", nargs="?")
    g.add_argument("--run", help="gate a run: ID or 'latest'")
    g.add_argument("--doc", help="gate one document of the run")
    g.add_argument("--mode", choices=["standard", "protected", "untouchable"])
    g.add_argument("--register", choices=["internal", "external"])
    g.add_argument("--allow", action="append", default=[], help="a flagged term that is the precise word here")
    g.add_argument("--json", action="store_true")
    g.add_argument("--vale-config")

    td = sub.add_parser("tidy", help="find and rejoin Markdown prose hard-wrapped mid-sentence, and single double "
                                     "spaces inside sentences; nothing else changes")
    td.add_argument("paths", nargs="*", help="one file (prints the result), or files and folders with --check/--write "
                                             "(folders: *.md, skipping hidden, gitignored, and humanize files)")
    td.add_argument("-o", "--out", help="with one file: write the result here instead of printing")
    td.add_argument("--check", action="store_true", help="list files that need tidying; exit 1 if any (for CI or hooks)")
    td.add_argument("--write", action="store_true", help="rewrite the files in place (rendered Markdown is unchanged)")
    td.add_argument("--exclude", action="append", default=[], help="skip paths matching this glob, e.g. 'archive/*'")
    td.add_argument("--run", help="run ID or 'latest' (with --doc): write the tidied source to the document's edit path")
    td.add_argument("--doc")
    td.add_argument("--force", action="store_true", help="with --run: overwrite an existing edit")

    s = sub.add_parser("setup", help="write a Vale config and sync styles (repository root, or --user)")
    s.add_argument("repo", nargs="?", help="absolute path to the repository root")
    s.add_argument("--user", action="store_true", help="set up ~/.cache/humanize/vale for repos without .vale.ini")

    w = sub.add_parser("worker", help="the worker model for this provider: latest Opus (claude) or latest Sol (codex), high reasoning")
    w.add_argument("--provider", choices=["claude", "codex"], required=True)
    w.add_argument("--json", action="store_true")

    t = sub.add_parser("task", help="print the self-contained worker instruction for one document of a run")
    t.add_argument("--run", default="latest")
    t.add_argument("--doc", required=True)
    t.add_argument("--provider", choices=["claude", "codex"], required=True)

    ds = sub.add_parser("dispatch", help="run the Codex worker for one document and wait for it (refuses while "
                                         "one is already running for that document)")
    ds.add_argument("--run", default="latest")
    ds.add_argument("--doc", required=True)
    ds.add_argument("--force", action="store_true", help="run again even if the document already passed")

    r = sub.add_parser("report", help="rebuild <run-id>.report.md for a run (keeps the synthesis section)")
    r.add_argument("--run", default="latest")

    d = sub.add_parser("deploy", help="install or upgrade humanize in a repository (idempotent, fully automated)")
    d.add_argument("repo", help="path to the repository root")
    d.add_argument("--providers", default="claude,codex", help="comma-separated: claude, codex (default both)")
    d.add_argument("--vale", choices=["auto", "download", "system", "skip"], default="auto",
                   help="auto: use system vale if it is the pinned version, else download the pinned release (default); "
                        "download: always use the pinned, checksum-verified release in .runtime/humanize/tools")
    d.add_argument("--dry-run", action="store_true")

    dr = sub.add_parser("doctor", help="verify an installation: files, skills, wiring, vale, self-test")
    dr.add_argument("repo", nargs="?", default=".")

    ac = sub.add_parser("accept", help="acceptance test of an installation: doctor plus the whole run lifecycle on "
                                       "sample documents (no model); records .runtime/humanize/acceptance.json")
    ac.add_argument("repo", nargs="?", default=".")
    ac.add_argument("--keep", action="store_true", help="keep the acceptance run folder for inspection")

    u = sub.add_parser("uninstall", help="remove everything humanize deploy installed (runs are kept)")
    u.add_argument("repo")
    u.add_argument("--force", action="store_true", help="also remove locally modified installed files")
    u.add_argument("--purge-runs", action="store_true", help="also delete .runtime/humanize runs")

    pk = sub.add_parser("package", help="build the deployable humanize-<version>.tar.gz")
    pk.add_argument("--out", default="dist")

    ver = sub.add_parser("version")
    ver.add_argument("--components", action="store_true")
    a = p.parse_args(argv)

    if a.cmd == "version":
        print(f"humanize {__version__}")
        if a.components:
            for name, v in VERSIONS["components"].items():
                print(f"  {name}: {v}")
        return 0

    if a.cmd in ("deploy", "doctor", "uninstall", "package", "accept"):
        from humanize import deploy as dep
        if a.cmd == "deploy":
            provs = tuple(x.strip() for x in a.providers.split(",") if x.strip())
            bad = [x for x in provs if x not in dep.PROVIDERS]
            if bad or not provs:
                p.error(f"--providers takes claude and/or codex, not {bad}")
            return dep.deploy(a.repo, provs, a.vale, a.dry_run)
        if a.cmd == "doctor":
            return dep.doctor(a.repo)
        if a.cmd == "accept":
            return dep.accept(a.repo, a.keep)
        if a.cmd == "uninstall":
            return dep.uninstall(a.repo, a.force, a.purge_runs)
        return dep.package(a.out)

    if a.cmd == "setup":
        return _setup(p, a)

    if a.cmd == "tidy":
        if a.run:
            if not a.doc:
                p.error("--run needs --doc")
            path, changed = runs.tidy_doc(runs.resolve_run(a.run), a.doc, a.force)
            print(f"{path}: {changed}")
            return 0
        if not a.paths:
            p.error("tidy needs files or folders, or --run with --doc")
        if a.check or a.write:
            return _tidy_many(a)
        if len(a.paths) > 1 or Path(a.paths[0]).is_dir():
            p.error("several files or a folder: add --check to list them or --write to fix them in place")
        source, _ = _read(a.paths[0])
        result = text.tidy(source)
        if a.out:
            Path(a.out).write_text(result)
            print(f"{a.out}: {'tidied' if result != source else 'already tidy'}")
        else:
            print(result, end="")
        return 0

    if a.cmd == "worker":
        info = workers.resolve(a.provider)
        print(json.dumps(info, indent=2) if a.json else "\n".join(f"{k}: {v}" for k, v in info.items()))
        return 1 if info.get("error") else 0

    if a.cmd == "task":
        run = runs.resolve_run(a.run)
        manifest = runs.load(run)
        doc = runs._find(manifest, a.doc)
        if doc.get("worker") == "tool":
            why = f"a copy of {doc['duplicate_of']}" if doc.get("duplicate_of") else "finished by the tool"
            print(f"No worker needed for {doc['rel']}: {why}. Skip it; `humanize gate --run {manifest['run']}` checks it.")
            return 0
        info = workers.resolve(a.provider)
        print(workers.task_prompt(run, manifest["run"], doc, workers.label(info)))
        return 0

    if a.cmd == "dispatch":
        run = runs.resolve_run(a.run)
        manifest = runs.load(run)
        code, message = workers.dispatch(run, manifest, runs._find(manifest, a.doc), a.force)
        print(message)
        if code == 0:
            manifest = runs.load(run)
            doc = runs._find(manifest, a.doc)
            print(f"{doc['rel']}: status {doc.get('status')} after {doc.get('attempts', 0)} gate run(s)")
        return code

    if a.cmd == "report":
        run = runs.resolve_run(a.run)
        print(runs.build_run_report(run))
        return 0

    if a.cmd == "runs":
        items = runs.list_runs()
        if a.json:
            print(json.dumps(items, indent=2))
        elif not items:
            print("no runs yet")
        for r in [] if a.json else items:
            print(f"{r['run']}  {r['documents']} docs  pass {r['pass']}  fail {r['fail']}  open {r['pending']}  ({r['created']})")
        return 0

    if a.cmd == "start":
        patterns = a.only or (runs.DEFAULT_PATTERNS + a.include)
        if a.dry_run:
            docs, ignored = runs.collect(a.paths, patterns)
            total = 0
            for d in docs:
                n = len(d.read_text(errors="replace").split())
                total += n
                print(f"{d}  ({n} words)")
            print(f"{len(docs)} document(s), {total} words; patterns: {', '.join(patterns)}"
                  + (f"; {len(ignored)} gitignored file(s) skipped" if ignored else ""))
            return 0
        run, manifest, added, warning = runs.start(a.paths, patterns, a.run, a.vale_config, a.all_workers)
        if a.json:
            print(json.dumps({"run": manifest["run"], "folder": str(run), "added": added, "warning": warning}, indent=2))
            return 0
        if warning:
            print(warning)
        print(f"run: {manifest['run']}  folder: {run}")
        print(f"added {len(added)} document(s); run has {len(manifest['documents'])}")
        words, need = 0, []
        tool = _tool_path()
        for d in added:
            n = runs.words((run / d["source"]).read_text(), d["kind"])
            words += n
            is_tool = d.get("worker") == "tool"
            need += [] if is_tool else [d]
            label = ((f"copy of {d['duplicate_of']}" if d.get("duplicate_of") else "done by the tool") if is_tool
                     else "needs a worker")
            print(f"- {d['rel']}  [{d['mode']}{'/' + d['register'] if d['mode'] == 'standard' else ''}]  {n} words  ({label})")
            if not is_tool:
                if _provider() == "codex":
                    print(f"    worker: {tool} dispatch --run {manifest['run']} --doc {shlex.quote(d['rel'])}")
                else:
                    print(f"    task:   {tool} task --run {manifest['run']} --doc {shlex.quote(d['rel'])} --provider claude")
                print(f"    edit:   {run / d['edit']}")
        print(f"total {words} prose words; {len(need)} document(s) need a worker, {len(added) - len(need)} finished by the "
              f"tool (untouchable, protected with nothing to edit, or duplicates).")
        print("Each worker: the command under its document, one document at a time.")
        print(f"Then close the run: {tool} gate --run {manifest['run']} && {tool} report --run {manifest['run']}")
        return 0

    if a.cmd == "brief":
        if a.run:
            if not a.doc:
                p.error("--run needs --doc")
            run = runs.resolve_run(a.run)
            doc = runs.rebrief(run, a.doc, a.mode, a.register)
            print((run / doc["brief"]).read_text(), end="")
            return 0
        if not a.file:
            p.error("brief needs a file, or --run with --doc")
        source, near = _read(a.file)
        kind = _kind(a.file)
        result = assess.check(gate.prose(source, kind), a.vale_config, near, kind=kind)
        print(assess.brief(a.file, result, a.mode, a.register, kind=kind, body=gate.prose(source, kind)), end="")
        return 0

    if a.cmd == "check":
        source, near = _read(a.file)
        result = assess.check(gate.prose(source, _kind(a.file)), a.vale_config, near, kind=_kind(a.file))
        print(json.dumps(result, indent=2) if a.json else assess.format_check(result))
        return 0

    if a.run:
        run = runs.resolve_run(a.run)
        manifest, docs = runs.gate_run(run, a.doc, a.allow, a.vale_config)
        if a.json:
            print(json.dumps(docs, indent=2))
        else:
            for d in docs:
                r = d.get("result")
                if not r:
                    print(f"MISSING {d['rel']}: write {run / d['edit']}")
                    continue
                print(f"{r['status'].upper():4} {d['rel']}  {r['run_line']}")
                for ch in r["checks"]:
                    if ch["status"] != "pass":
                        print(f"     {ch['status'].upper():4} {ch['check']}: {ch['detail']}")
            print(f"run report: {run / (manifest['run'] + '.report.md')}")
        return 0 if all(d["status"] == "pass" for d in docs) else 1

    if not (a.source and a.edit):
        p.error("gate needs SOURCE EDIT, or --run")
    source, near = _read(a.source)
    edit, _ = _read(a.edit)
    result = gate.gate(source, edit, a.mode, a.register, a.allow, a.vale_config, near, kind=_kind(a.source))
    print(json.dumps(result, indent=2) if a.json else gate.format_gate(result))
    return 0 if result["status"] == "pass" else 1


def _tidy_many(a):
    import fnmatch
    root = runs.repo_root()
    docs, _ = runs.collect(a.paths, ["*.md", "*.markdown"])
    found = 0
    for f in docs:
        try:
            rel = str(f.relative_to(root))
        except ValueError:
            rel = str(f)
        if any(fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(str(f), pat) for pat in a.exclude):
            continue
        source = f.read_text(errors="replace")
        wraps, spaces = text.hard_wraps(source), text.inner_spaces(source)
        if not (wraps or spaces):
            continue
        found += 1
        detail = ", ".join(x for x in (f"{len(wraps)} wrapped paragraph(s)" if wraps else "",
                                       f"{len(spaces)} line(s) with inner double spaces" if spaces else "") if x)
        if a.write:
            f.write_text(text.tidy(source))
            print(f"tidied  {rel}  ({detail})")
        else:
            print(f"needs tidy  {rel}  ({detail}; first at line {(wraps or spaces)[0]})")
    print(f"{found} file(s) {'tidied' if a.write else 'need tidying'} of {len(docs)} scanned")
    return 1 if found and a.check else 0


def _setup(p, a):
    if a.user == bool(a.repo):
        p.error("setup takes a repository path or --user")
    if a.user:
        target, styles = vale.USER_CONFIG.parent, "styles"
    else:
        target = Path(a.repo)
        if not target.is_absolute() or not target.is_dir():
            p.error("repository path must be an absolute directory")
        styles = ".vale/styles"
    config, created, synced = vale.setup(target, styles)
    print(f"vale config: {config} ({'created' if created else 'existing, left unchanged'})")
    print("vale styles: " + ("synced" if synced else "not synced (vale not installed: brew install vale)"))
    gitignore = target / ".gitignore"
    lines = gitignore.read_text().splitlines() if gitignore.is_file() else []
    if not a.user and ".vale/styles/" not in lines:
        print("add '.vale/styles/' to the repository .gitignore")
    if not a.user and ".runtime/" not in lines:
        print("add '.runtime/' to the repository .gitignore (humanize writes runs to .runtime/humanize/)")
    return 0
