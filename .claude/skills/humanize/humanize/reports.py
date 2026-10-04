"""Per-document reports (<name>.humanized.report.md) and the run report (<run-id>.report.md).

The tool owns the facts sections (between markers); the worker owns the judgment sections;
the orchestrator owns the run report's synthesis section. Rebuilding never erases owned text.
"""
import collections
import difflib
import re

from humanize import text

FACTS = ("<!-- humanize:facts:start -->", "<!-- humanize:facts:end -->")
SYNTH = ("<!-- humanize:synthesis:start -->", "<!-- humanize:synthesis:end -->")

WORKER_SECTIONS = [
    ("Decisions", "The mode and register used, and why; the edits made and the editorial reason for them, "
                  "with a few concrete examples."),
    ("Flagged but kept", "Each flagged word or possible change left as it was, with the editorial reason (for example: "
                         "precise word, term of art, protected-mode limit, would change meaning)."),
    ("Notes for the author", "One bullet per item the author should act on: missing facts, claims with no proof, "
                             "unclear terms or codes. Invent nothing. Write 'None.' if there are none."),
    ("Anomalies", "Anything odd in the source: inconsistencies, broken references, formatting problems, "
                  "terms used differently from their definition."),
    ("Tool feedback", "Where the humanize brief or gate was wrong, noisy, or missing something, with the exact line. "
                      "Write 'None.' if it worked well."),
]


def skeleton(doc_rel, worker=None):
    lines = [f"# humanize report: {doc_rel}", "",
             f"Worker: {worker or '(fill in: provider, model, effort)'}", "",
             FACTS[0], "_Filled in by `humanize gate`._", FACTS[1], ""]
    for title, hint in WORKER_SECTIONS:
        lines += [f"## {title}", "", f"<!-- {hint} -->", ""]
    return "\n".join(lines).rstrip() + "\n"


def tool_report(doc_rel, worker, why):
    """A filled report for a document the tool finished without a worker."""
    lines = [f"# humanize report: {doc_rel}", "", f"Worker: {worker}", "",
             FACTS[0], "_Filled in by `humanize gate`._", FACTS[1], "",
             "## Decisions", "", f"- {why}", "",
             "## Flagged but kept", "", "- None.", "",
             "## Notes for the author", "", "- None.", "",
             "## Anomalies", "", "- None (no worker read this document).", "",
             "## Tool feedback", "", "- None."]
    return "\n".join(lines) + "\n"


def section(report_text, title):
    m = re.search(rf"^## {re.escape(title)}\s*$(.*?)(?=^## |\Z)", report_text, re.M | re.S)
    if not m:
        return ""
    return re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S).strip()


def notes(report_text):
    body = section(report_text, "Notes for the author")
    items = [re.sub(r"^[-*]\s+", "", l).strip() for l in body.splitlines() if re.match(r"^[-*]\s+", l)]
    return [i for i in items if i and i.lower() not in ("none", "none.")]


def unfilled(report_text):
    worker = re.search(r"^Worker:\s*(.*)$", report_text, re.M)
    missing = [] if worker and worker.group(1).strip() and "(fill in" not in worker.group(1) else ["Worker line"]
    return missing + [t for t, _ in WORKER_SECTIONS if not section(report_text, t)]


def _between(textblock, markers, replacement):
    start, end = markers
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    new = f"{start}\n{replacement.rstrip()}\n{end}"
    if pattern.search(textblock):
        return pattern.sub(lambda _: new, textblock)
    return textblock.rstrip() + "\n\n" + new + "\n"


def change_ratio(source_body, edit_body):
    a, b = source_body.split(), edit_body.split()
    if not a and not b:
        return 0.0
    return round(1 - difflib.SequenceMatcher(None, a, b, autojunk=False).ratio(), 3)


def layout_line(layout):
    """What the tool did to the layout of an edit, in one line (None when layout was not normalized)."""
    if not layout:
        return None
    w, s = layout["source_wraps"], layout["source_spaces"]
    dw, ds = layout["draft_wraps"], layout["draft_spaces"]
    if not (w or s or dw or ds):
        return "no hard-wrapped prose or double spaces inside sentences; nothing to fix"
    done = []
    if w or dw:
        done.append(f"rejoined {w} paragraph(s) or list item(s) hard-wrapped mid-sentence in the source"
                    + (f" ({dw} still wrapped in the worker's draft)" if dw else ""))
    if s or ds:
        done.append(f"made double spaces inside sentences single on {s} source line(s)"
                    + (f" ({ds} in the worker's draft)" if ds else ""))
    return "; ".join(done) + "; each paragraph and list item is now one line"


def facts_block(doc, result, attempts, ratio, source_words, edit_words, layout=None):
    lines = ["## Facts (from the tool)", "",
             f"- Gate: **{result['status'].upper()}** "
             + ("(finished by the tool, no worker)" if doc.get("worker") == "tool" else f"after {attempts} attempt(s)")
             + f"; {result['run_line']}",
             f"- Words: {source_words} -> {edit_words}; changed: {ratio:.1%} of words",
             f"- Mode: {doc['mode']}" + (f", register {doc['register']}" if doc["mode"] == "standard" else "")
             + (f"; suggested evidence: {', '.join(doc.get('mode_evidence') or []) or 'none'}")]
    if layout_line(layout):
        lines.append(f"- Layout (applied by humanize): {layout_line(layout)}")
    issues = [c for c in result["checks"] if c["status"] != "pass"]
    if issues:
        lines.append("- Gate findings:")
        lines += [f"  - {c['status'].upper()} {c['check']}: {c['detail']}" for c in issues]
    else:
        lines.append("- Gate findings: none")
    return "\n".join(lines)


def fill_facts(report_text, block):
    return _between(report_text, FACTS, block)


def cross_document_terms(docs_bodies):
    """Defined terms (capitalized) in one document that appear lowercased in another."""
    terms = {}
    for rel, body in docs_bodies.items():
        for t in text.defined_terms(body):
            if " " in t and not t.isupper():
                terms.setdefault(t, set()).add(rel)
    findings = []
    for term, owners in sorted(terms.items()):
        lower = re.compile(r"\b" + re.escape(term.lower()) + r"s?\b")
        for rel, body in docs_bodies.items():
            masked = text.mask_code(body)
            hits = [m for m in lower.finditer(masked) if masked[m.start():m.end()] != masked[m.start():m.end()].title()]
            if hits:
                findings.append(f"'{term}' (capitalized in {', '.join(sorted(owners))}) appears lowercase "
                                f"{len(hits)}x in {rel}")
    return findings


def _workers_summary(docs, per_doc):
    tool = sum(d.get("worker") == "tool" for d in docs)
    named = collections.Counter(per_doc[d["rel"]]["worker"] for d in docs
                                if d.get("worker") != "tool" and per_doc[d["rel"]]["worker"])
    unrecorded = len(docs) - tool - sum(named.values())
    parts = [f"{w} ({n})" for w, n in sorted(named.items())]
    parts += [f"the humanize tool, no model ({tool})"] if tool else []
    parts += [f"not recorded yet ({unrecorded})"] if unrecorded else []
    return "; ".join(parts) or "none"


def _layout_summary(layouts):
    done = [l for l in layouts if l]
    if not done:
        return "not yet applied (no gated Markdown edits)"
    wraps = sum(l["source_wraps"] for l in done)
    spaces = sum(l["source_spaces"] for l in done)
    docs = sum(1 for l in done if l["source_wraps"] or l["source_spaces"])
    if not (wraps or spaces):
        return f"nothing to fix in {len(done)} document(s)"
    parts = ([f"{wraps} hard-wrapped paragraph(s) or list item(s) rejoined"] if wraps else []) + \
            ([f"double spaces inside sentences fixed on {spaces} line(s)"] if spaces else [])
    return f"{' and '.join(parts)}, in {docs} of {len(done)} document(s); every paragraph and list item is one line"


def run_report(manifest, per_doc, cross_terms, previous=""):
    docs = manifest["documents"]
    count = {s: sum(d["status"] == s for d in docs) for s in ("pass", "fail", "failed", "missing", "pending")}
    lines = [f"# humanize run {manifest['run']}", "",
             f"Created {manifest['created']} with {manifest['tool']}. Repository: `{manifest['repo']}`.", "",
             "## Summary", "",
             f"- Documents: {len(docs)}; pass {count['pass']}, fail {count['fail']}, failed after retries "
             f"{count['failed']}, missing {count['missing']}, pending {count['pending']}",
             f"- Words (prose, in the {sum(p['edited'] for p in per_doc.values())} document(s) with an edit): "
             f"{sum(p['source_words'] for p in per_doc.values() if p['edited'])} -> "
             f"{sum(p['edit_words'] for p in per_doc.values() if p['edited'])}; all documents: "
             f"{sum(p['source_words'] for p in per_doc.values())} words",
             "- Workers: " + _workers_summary(docs, per_doc),
             "- Layout (applied by humanize to every Markdown edit): "
             + _layout_summary([p.get("layout") for p in per_doc.values()]),
             "", "## Index", "",
             "| Document | Mode | Status | Attempts | Vale | Changed | Layout | Notes | Edited file | Report |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for d in docs:
        p = per_doc[d["rel"]]
        mode = d["mode"] + ("/" + d["register"] if d["mode"] == "standard" else "")
        lay = p.get("layout")
        lay = (f"{lay['source_wraps']} rejoined, {lay['source_spaces']} spacing" if lay else "not applied")
        attempts = "tool" if d.get("worker") == "tool" else d.get("attempts", 0)
        lines.append(f"| {d['rel']} | {mode} | {d['status']} | {attempts} | {p['vale']} | "
                     f"{p['ratio']:.1%} | {lay} | {len(p['notes'])} | {d['edit']} | {d['report']} |")
    lines += ["", "## Notes for the author", ""]
    any_notes = False
    for d in docs:
        if per_doc[d["rel"]]["notes"]:
            any_notes = True
            lines.append(f"### {d['rel']}")
            lines += [f"- {n}" for n in per_doc[d["rel"]]["notes"]]
            lines.append("")
    if not any_notes:
        lines += ["None.", ""]
    lines += ["## Cross-document consistency (from the tool)", ""]
    lines += [f"- {c}" for c in cross_terms] or ["- No defined term is capitalized in one document and lowercased in another."]
    for title in ("Anomalies", "Tool feedback"):
        lines += ["", f"## {title} (from the workers)", ""]
        found = False
        for d in docs:
            body = per_doc[d["rel"]]["sections"].get(title, "")
            if body and body.lower().strip(". ") != "none":
                found = True
                lines += [f"### {d['rel']}", body, ""]
        if not found:
            lines.append("None reported.")
    gaps = [f"{d['rel']}: {', '.join(per_doc[d['rel']]['unfilled'])}" for d in docs if per_doc[d["rel"]]["unfilled"]]
    if gaps:
        lines += ["", "## Incomplete worker reports", ""] + [f"- {g}" for g in gaps]
    m = re.search(re.escape(SYNTH[0]) + r"(.*?)" + re.escape(SYNTH[1]), previous, re.S)
    synthesis = m.group(1).strip() if m else ("_To be written by the orchestrator: global anomalies, cross-document "
                                              "suggestions for the document set, and suggestions for improving the "
                                              "humanize skill or tool._")
    lines += ["", "## Synthesis", "", SYNTH[0], synthesis, SYNTH[1]]
    return "\n".join(lines).rstrip() + "\n"
