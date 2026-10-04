"""gate: post-assessment of an edit against its source. Exit 1 on any FAIL."""
import json

from humanize import detect, lexicon, text, vale


def _count(pattern, s):
    return len(pattern.findall(s))


def _is_prose(value):
    return isinstance(value, str) and len(value.split()) >= 3


def _strings(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from _strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _strings(v)
    elif _is_prose(obj):
        yield obj


def prose(raw, kind):
    """The text the checks run on: prose strings for JSON, the whole text otherwise."""
    if kind != "json":
        return raw
    try:
        return "\n\n".join(_strings(json.loads(raw))) + "\n"
    except json.JSONDecodeError:
        return raw


def _structure_diff(a, b, path="$"):
    if type(a) is not type(b):
        return [f"{path}: type changed"]
    if isinstance(a, dict):
        if set(a) != set(b):
            return [f"{path}: keys changed ({', '.join(sorted(set(a) ^ set(b)))})"]
        return [d for k in a for d in _structure_diff(a[k], b[k], f"{path}.{k}")]
    if isinstance(a, list):
        if len(a) != len(b):
            return [f"{path}: list length {len(a)} -> {len(b)}"]
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in _structure_diff(x, y, f"{path}[{i}]")]
    if not _is_prose(a) and a != b:
        return [f"{path}: non-prose value changed"]
    return []


def gate(source_text, edit_text, mode=None, register=None, allow=(), vale_config=None, near=None,
         kind="markdown", notes_text="", glossary=None):
    sidecar = [l for l in text.normalize(notes_text).splitlines() if l.startswith("Note:")]
    structure = []
    if kind == "json":
        try:
            structure = _structure_diff(json.loads(source_text), json.loads(edit_text))
            json_ok = True
        except json.JSONDecodeError as e:
            json_ok, structure = False, [f"edit is not valid JSON: {e}"]
        src, out, notes = prose(source_text, kind), prose(edit_text, kind), sidecar
    else:
        src, _, _ = text.split_notes(source_text)
        out, notes, _ = text.split_notes(edit_text)
        notes = notes + sidecar
    mode = mode or detect.suggest_mode(src)["mode"]
    register = (register or detect.suggest_register(src)["register"]) if mode == "standard" else "-"
    allow = {a.lower() for a in allow}
    checks = []

    def add(name, status, detail=""):
        checks.append({"check": name, "status": status, "detail": detail})

    if kind == "json":
        add("json_structure", "pass" if json_ok and not structure else "fail", "; ".join(structure[:8]))
        if not json_ok:
            return {"status": "fail", "mode": mode or "-", "register": register or "-", "notes": notes,
                    "run_line": f"Run: mode={mode or '-'} register={register or '-'} vale=skipped", "checks": checks}
    if mode == "untouchable":  # returned unchanged by design: style checks do not apply
        same = text.flat(out) == text.flat(src)
        add("unchanged", "pass" if same else "fail", "" if same else "untouchable text was edited")
        return {"status": "pass" if same else "fail", "mode": mode, "register": "-", "notes": notes,
                "run_line": f"Run: mode={mode} register=- vale=skipped", "checks": checks}
    sp, op = text.protected_items(src, glossary), text.protected_items(out, glossary)
    flat_out = text.flat(out)

    lost = [n for n in sp["numbers"] if n not in op["numbers"]]
    add("numbers_kept", "fail" if lost else "pass", ", ".join(lost))
    new = [n for n in op["numbers"] if n not in sp["numbers"]]
    add("no_new_numbers", "fail" if new else "pass", ", ".join(new))
    lost = [c for c in sp["codes"] if c not in op["codes"]]
    add("codes_kept", "fail" if lost else "pass", ", ".join(lost))
    new = [c for c in op["codes"] if c not in sp["codes"]]
    add("no_new_codes", "fail" if new else "pass", ", ".join(new))
    lost = [q for q in sp["quotes"] if q not in flat_out]
    add("quotes_kept", "fail" if lost else "pass", " | ".join(lost))
    lost = [b for b in sp["bold_labels"] if b not in out]
    add("bold_labels_kept", "fail" if lost else "pass", ", ".join(lost))
    lost = [p for p in sp["placeholders"] if f"[{p}]" not in out]
    add("placeholders_kept", "fail" if lost else "pass", ", ".join(lost))
    changed = sum(1 for blk in sp["code_blocks"] if blk not in out)
    add("code_blocks_kept", "fail" if changed else "pass", f"{changed} code block(s) changed or missing" if changed else "")
    out_terms = text.defined_terms(out, glossary)
    lost = [t for t in sp["defined_terms"] if t not in out and t not in out_terms]
    add("defined_terms_kept", ("fail" if mode == "protected" else "warn") if lost else "pass", ", ".join(lost[:12]))

    masked_out = text.mask_code(out)
    marks = [m for m in text.MARK_RE.findall(masked_out) if m not in sp["placeholders"]]
    invented = [m for m in marks if m.lower() not in text.flat(src).lower()]
    add("marks_from_source", "fail" if invented else "pass", ", ".join(invented))
    if mode == "protected":
        add("no_marks_in_protected", "fail" if marks else "pass", ", ".join(marks))
    else:
        hollow = {h["match"].lower() for h in lexicon.scan(masked_out) if h["marked"] and h["category"] == "hollow"}
        odd = [m for m in marks if m.lower() not in hollow]
        add("marks_are_hollow", "warn" if odd else "pass",
            ("not in the hollow list (fine if it adds no checkable claim): " + ", ".join(odd)) if odd else "")

    if kind == "markdown" and mode != "untouchable":
        wraps, spaces = text.hard_wraps(out), text.inner_spaces(out)
        add("no_hard_wraps", "fail" if wraps else "pass",
            ("paragraph(s) broken mid-sentence starting on line(s) " + ", ".join(map(str, wraps[:12]))
             + "; put each paragraph or list item on one line (`humanize tidy` joins them)") if wraps else "")
        add("no_inner_double_spaces", "fail" if spaces else "pass",
            ("double space inside a sentence on line(s) " + ", ".join(map(str, spaces[:12]))) if spaces else "")

    dashes = masked_out.count("—")
    add("no_em_dash", "fail" if dashes else "pass", f"{dashes} em dash(es)" if dashes else "")
    bad = text.title_case_headings(out, sp["defined_terms"])
    add("sentence_case_headings", ("warn" if mode == "protected" else "fail") if bad else "pass",
        " | ".join(h for _, h in bad))

    hard, soft = [], []
    for h in lexicon.scan(masked_out):
        if h["marked"] or h["term"].lower() in allow or h["match"].lower() in allow:
            continue
        label = f"edit line {h['line']} \"{h['match']}\" ({h['category']})"
        if lexicon.fails(h["category"], mode) and h["signal"] == "high":
            hard.append(label)
        elif h["category"] not in ("magnitude",):
            soft.append(label)
    add("tells_resolved", "fail" if hard else "pass",
        "; ".join(hard) + ("  [use --allow TERM only if it is the precise word, and say why in a Note]" if hard else ""))
    if soft:
        add("tells_review", "warn", "; ".join(soft))

    note_text = " ".join(notes).lower()
    unnoted = sorted({h["match"] for h in lexicon.scan(masked_out)
                      if h["category"] == "magnitude" and h["match"].lower() not in note_text})
    if unnoted and mode != "protected":
        add("magnitude_noted", "warn", "no note (in a run: the report's Notes for the author) asks for the figure "
            "behind: " + ", ".join(unnoted))

    strict = "fail" if mode == "protected" else "warn"
    for name, pattern in (("negations_kept", text.NEGATION_RE), ("hedges_kept", text.HEDGE_RE)):
        a, b = _count(pattern, src), _count(pattern, out)
        add(name, strict if b < a else "pass", f"{a} -> {b}" if b < a else "")

    if len(notes) > 6:
        add("notes_count", "warn", f"{len(notes)} notes; merge related gaps")

    v_src, v_out = vale.assess(src, vale_config, near), vale.assess(out, vale_config, near)
    if v_src["status"] == "ok" and v_out["status"] == "ok":
        ok = v_out["gate"] <= v_src["gate"] and v_out["counts"]["error"] <= v_src["counts"]["error"]
        seen = {(f["rule"], f["text"].lower()) for f in v_src["findings"]}
        new = [f"edit line {f['line']} {f['rule']} \"{f['text']}\"" for f in v_out["findings"]
               if (f["rule"], f["text"].lower()) not in seen]
        add("vale", "pass" if ok else "fail",
            f"{v_src['gate']} -> {v_out['gate']} (errors {v_src['counts']['error']} -> {v_out['counts']['error']})"
            + (("; new: " + "; ".join(new)) if new and not ok else ""))
        vale_value = f"{v_src['gate']}->{v_out['gate']}"
    else:
        add("vale", "warn", f"skipped ({v_out.get('reason') or v_src.get('reason')})")
        vale_value = "skipped"

    failed = [c for c in checks if c["status"] == "fail"]
    return {"status": "fail" if failed else "pass", "mode": mode, "register": register, "notes": notes,
            "run_line": f"Run: mode={mode} register={register} vale={vale_value}",
            "checks": checks}


def format_gate(r):
    out = []
    for c in r["checks"]:
        if c["status"] != "pass":
            out.append(f"{c['status'].upper():4} {c['check']}: {c['detail']}")
    fails = sum(c["status"] == "fail" for c in r["checks"])
    warns = sum(c["status"] == "warn" for c in r["checks"])
    out.append(f"gate: {r['status'].upper()} ({fails} fail, {warns} warn, "
               f"{sum(c['status'] == 'pass' for c in r['checks'])} pass)")
    out.append(r["run_line"])
    return "\n".join(out)
