"""check (pre-assessment) and brief (edit instructions for the agent)."""
from humanize import DATA, detect, lexicon, text, vale

VALE_HINTS = {
    "write-good.Passive": "use active voice only if the source makes the actor clear",
    "Microsoft.Passive": "use active voice only if the source makes the actor clear",
    "Microsoft.Headings": "sentence case",
    "write-good.TooWordy": "shorten",
    "Microsoft.Wordiness": "shorten",
    "write-good.Cliches": "replace with plain words",
    "write-good.Weasel": "keep only if it carries meaning; otherwise cut or add a Note asking for the figure",
    "Microsoft.Adverbs": "cut if it adds nothing",
    "Microsoft.FirstPerson": "keep the source's person; do not drift into 'I'",
    "Microsoft.SentenceLength": "split if it reads better",
}


def check(source_text, vale_config=None, near=None, glossary=None, kind="markdown"):
    body, notes, _ = text.split_notes(source_text)
    hits = lexicon.scan(text.mask_code(body))
    for h in hits:
        h.pop("start"), h.pop("end")
    return {
        "mode": detect.suggest_mode(body),
        "register": detect.suggest_register(body),
        "protected": text.protected_items(body, glossary),
        "tells": hits,
        "em_dash_lines": sorted({text.line_of(body, i) for i, c in enumerate(body) if c == "—"}),
        "curly_quotes": sum(body.count(c) for c in "‘’“”"),
        "title_case_headings": text.title_case_headings(body, text.defined_terms(body, glossary)),
        "hard_wraps": text.hard_wraps(body) if kind == "markdown" else [],
        "inner_spaces": text.inner_spaces(body) if kind == "markdown" else [],
        "sentences": text.sentence_stats(text.mask_code(body)),
        "vale": vale.assess(body, vale_config, near),
    }


def needs_worker(r, mode):
    """False when the tool can finish the document alone: untouchable, or protected with no permitted edit flagged
    (no unmarked tell, em dash, title-case heading, or curly quote). Layout is applied by the tool either way."""
    if mode == "untouchable":
        return False
    if mode != "protected":
        return True
    return bool([h for h in r["tells"] if not h["marked"]] or r["em_dash_lines"] or r["title_case_headings"]
                or r.get("curly_quotes"))


def format_check(r):
    out = [f"mode: {r['mode']['mode']} (suggested; "
           + ("evidence" if r["mode"]["mode"] != "standard" else "protected-mode signals below the threshold")
           + f": {', '.join(r['mode']['evidence']) or 'none'})",
           f"register: {r['register']['register']} (suggested; internal signals {r['register']['internal_signals']}, "
           f"external signals {r['register']['external_signals']})"]
    v = r["vale"]
    if v["status"] == "ok":
        out.append(f"vale: {v['gate']} errors+warnings ({v['counts']['error']} errors) [{v['config_source']}]")
    else:
        out.append(f"vale: skipped ({v['reason']})")
    unmarked = [h for h in r["tells"] if not h["marked"]]
    out.append(f"tells: {len(unmarked)} ({', '.join(sorted({h['category'] for h in unmarked})) or 'none'})")
    for h in unmarked:
        out.append(f"  line {h['line']}: \"{h['match']}\" [{h['category']}]")
    p = r["protected"]
    for key in ("numbers", "codes", "quotes", "bold_labels"):
        if p[key]:
            out.append(f"protected {key}: {', '.join(p[key])}")
    if p["defined_terms"]:
        out.append(f"defined terms ({len(p['defined_terms'])}): {', '.join(p['defined_terms'][:15])}"
                   + (" ..." if len(p["defined_terms"]) > 15 else ""))
    if p["code_blocks"]:
        out.append(f"code blocks: {len(p['code_blocks'])} (kept verbatim, not scanned)")
    if r["em_dash_lines"]:
        out.append(f"em dashes on lines: {', '.join(map(str, r['em_dash_lines']))}")
    for line, h in r["title_case_headings"]:
        out.append(f"title-case heading line {line}: {h}")
    if r.get("hard_wraps"):
        out.append(f"hard wraps (paragraphs broken mid-sentence) starting on lines: {', '.join(map(str, r['hard_wraps']))}")
    if r.get("inner_spaces"):
        out.append(f"double spaces inside sentences on lines: {', '.join(map(str, r['inner_spaces']))}")
    s = r["sentences"]
    out.append(f"sentences: {s['sentences']}, mean {s['mean']} words, stdev {s['stdev']}")
    return "\n".join(out)


def _rules(names):
    vendor = str(DATA / "vendor")
    parts = []
    for name in names:
        body = (DATA / "rules" / f"{name}.md").read_text().replace("../vendor", vendor)
        parts.append(text.tidy(body).strip())
    return "\n\n---\n\n".join(parts)


def _protected_action(category):
    return {
        "phrase": "delete (permitted edit 1)",
        "filler": "shorten (permitted edit 2)",
        "hedge_stack": "collapse to one hedge of the same strength (permitted edit 5)",
        "vocab": "replace with a plain word of the same meaning, unless it is a term of art (permitted edit 3)",
    }.get(category, "leave as is; name it in the single leftover-tells Note if it matters")


KIND_GUIDANCE = {
    "json": ("This is a JSON file. Edit only prose string values. Keep every key, the structure, and every "
             "non-prose value (IDs, URLs, codes, numbers) exactly. The edited file must stay valid JSON. "
             "Put notes for the author in your report, not in the JSON."),
    "text": "This is a plain-text file. Keep its layout; put Note: lines at the end.",
    "markdown": None,
}


def brief(source_name, r, mode=None, register=None, kind="markdown", edit_path=None, notes_path=None,
          gate_cmd=None, body=""):
    mode = mode or r["mode"]["mode"]
    register = register or r["register"]["register"]
    lines = [f"# humanize brief: {source_name}", ""]
    lines.append(f"Mode: **{mode}**" + ("" if mode == r["mode"]["mode"] else " (overridden)")
                 + f". Suggested {r['mode']['mode']}; "
                 + ("evidence" if r["mode"]["mode"] != "standard" else "protected-mode signals below the threshold")
                 + f": {', '.join(r['mode']['evidence']) or 'none'}.")
    if mode == "untouchable":
        lines += ["", "Return the text unchanged with one line:",
                  "`Note: untouchable (<reason>); returned unchanged.`"]
        return "\n".join(lines) + "\n"
    if mode == "standard":
        lines.append(f"Register: **{register}**" + ("" if register == r["register"]["register"] else " (overridden)")
                     + f". Override with --register if wrong, and say why.")
    lines.append("If the mode is wrong, re-run `humanize brief` with --mode and say why.")
    if KIND_GUIDANCE.get(kind):
        lines += ["", KIND_GUIDANCE[kind]]
    if edit_path:
        lines += ["", f"Write the edited document to: `{edit_path}`"]
        if notes_path:
            lines.append(f"Fill in your report (decisions, rejected changes, notes for the author, anomalies, "
                         f"tool feedback): `{notes_path}`. The edited document holds only the edited text.")

    p = r["protected"]
    keep = [(k, p[k]) for k in ("numbers", "codes", "quotes", "bold_labels", "placeholders") if p[k]]
    lines += ["", "## Must survive verbatim (the gate checks these)"]
    lines += [f"- {k}: " + "; ".join(v) for k, v in keep] or ["- nothing listed"]
    if p["defined_terms"]:
        lines.append("- defined terms (names: keep their exact wording and capitalization, never paraphrase, "
                     "never lowercase): " + "; ".join(p["defined_terms"]))
    if p["code_blocks"]:
        lines.append(f"- code blocks: {len(p['code_blocks'])} fenced block(s) (front matter, diagrams, code) "
                     "must be copied byte for byte")

    lines += ["", "## Work list", "", "Line numbers refer to the source snapshot; the gate reports lines of your edit."]
    work = 0
    for h in r["tells"]:
        if h["marked"]:
            continue
        act = _protected_action(h["category"]) if mode == "protected" else lexicon.action(h["category"])
        plain = f" (plain: {', '.join(h['plain'])})" if h["plain"] and h["category"] in ("vocab", "filler", "hedge_stack") else ""
        lines.append(f"- line {h['line']}: \"{h['match']}\" ({h['category']}) -> {act}{plain}")
        work += 1
    v = r["vale"]
    if v["status"] == "ok" and mode == "protected" and v["findings"]:
        rules = {}
        for f in v["findings"]:
            rules[f["rule"]] = rules.get(f["rule"], 0) + 1
        top = ", ".join(f"{k} {n}" for k, n in sorted(rules.items(), key=lambda kv: -kv[1])[:6])
        lines.append(f"- Vale: {len(v['findings'])} findings ({top}). Information only: in protected mode they are "
                     "not instructions. Never change modal verbs (shall, must, may), voice, or defined terms to "
                     "satisfy Vale; the gate only checks that the edit does not add Vale problems.")
    elif v["status"] == "ok":
        tell_spans = {(h["line"], h["match"].lower()) for h in r["tells"]}
        heading_lines = {ln for ln, _ in r["title_case_headings"]}
        merged = {}  # several styles often flag the same words; one work item per (line, words)
        for f in v["findings"]:
            if (f["line"], f["text"].lower()) in tell_spans or any(
                    f["line"] == ln and f["text"].lower() in m for ln, m in tell_spans):
                continue
            if f["rule"] == "Microsoft.Headings" and f["line"] in heading_lines:
                continue
            merged.setdefault((f["line"], f["text"].lower()), []).append(f)
        for group in merged.values():
            f = group[0]
            hint = VALE_HINTS.get(f["rule"]) or (f["message"].rstrip(".") + "; fix if the fix does not change meaning")
            rules = ", ".join(dict.fromkeys(g["rule"] for g in group))
            lines.append(f"- line {f['line']}: \"{f['text']}\" (Vale {rules}) -> {hint}")
            work += 1
    for ln in r["em_dash_lines"]:
        lines.append(f"- line {ln}: em dash -> period, comma, colon, or parentheses")
        work += 1
    for ln, h in r["title_case_headings"]:
        act = ("sentence case only if no word in it is a name or defined term; otherwise leave it"
               if mode == "protected" else "sentence case (keep names and defined terms capitalized"
               + ("; capitalize the first word after the colon)" if ":" in h else ")"))
        lines.append(f"- line {ln}: heading \"{h}\" -> {act}")
        work += 1
    if r.get("hard_wraps") or r.get("inner_spaces"):
        lines.append(f"- layout (done by the tool, not by you): {len(r.get('hard_wraps') or [])} hard-wrapped "
                     f"paragraph(s) and {len(r.get('inner_spaces') or [])} line(s) with double spaces inside sentences. "
                     "The gate rejoins and fixes them in your edit and reports it; write each paragraph and list item "
                     "on one line and keep the spacing between sentences.")
    if mode == "standard" and r["sentences"]["sentences"] >= 4 and r["sentences"]["stdev"] < 4:
        lines.append(f"- rhythm: sentence lengths are uniform (stdev {r['sentences']['stdev']}); vary them where the content varies")
    if not work:
        lines.append("- no permitted edit flagged; the text may need no change" if mode == "protected"
                     else "- nothing flagged; the text may need no change")
    lines.append("")
    lines.append("The list is a floor, not a ceiling: also apply the rules below to anything the scan missed.")

    lines += ["", "## Rules", ""]
    lines.append(_rules(["protected", "fidelity", "output"] if mode == "protected" else ["register", "fidelity", "output"]))
    if gate_cmd:
        verify = f"Then run: `{gate_cmd}`"
    else:
        verify = (f"Save the deliverable to a file and run: `humanize gate {source_name} <edit.md> --mode {mode}"
                  + (f" --register {register}`" if mode == "standard" else "`"))
    lines += ["", "## Then verify", verify, "(`humanize` means this skill's `bin/humanize` when it is not on PATH.)",
              "Fix every FAIL and run the gate again until it passes."]
    return "\n".join(lines) + "\n"
