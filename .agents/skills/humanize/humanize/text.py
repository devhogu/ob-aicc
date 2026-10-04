"""Text parsing: body vs notes, protected items, sentence statistics."""
import re
import statistics

NUM_RE = re.compile(r"\d+(?:[.,:]\d+)*%?")
CODE_RE = re.compile(r"\b(?:[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+|[A-Z]{1,3}\d{1,4}[A-Za-z0-9]*)\b")
QUOTE_RE = re.compile(r"\"([^\"\n]+)\"")
BOLD_LABEL_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s+(\*\*[^*\n]+?\*\*)", re.M)
HEADING_RE = re.compile(r"^(#+)\s+(.*)$", re.M)
MARK_RE = re.compile(r"\[([^\]\n]{1,40})\](?!\()")
# Kept verbatim and never scanned: fenced code, YAML front matter, and blocks another tool manages
# (<!-- name:begin ... --> ... <!-- name:end -->, e.g. the humanize block in CLAUDE.md).
FENCE_RE = re.compile(r"^```.*?^```[ \t]*$|\A---[ \t]*\n.*?^---[ \t]*$"
                      r"|^<!-- ([\w-]+):(?:begin|start)\b.*?^<!-- \1:end\b[^\n]*-->", re.M | re.S)
CAP_RUN_RE = re.compile(r"\b(?:[A-Z][A-Za-z0-9-]*)(?:\s+(?:of|and|for|on|the|to|in)?\s*[A-Z][A-Za-z0-9-]*)*")
NEGATION_RE = re.compile(r"\b(?:not|never|no|cannot|can't|don't|doesn't|didn't|won't|shouldn't|isn't|aren't|wasn't|without)\b", re.I)
HEDGE_RE = re.compile(r"\b(?:may|might|could|possibly|perhaps|likely|unlikely|appears?|seems?)\b", re.I)
SENT_RE = re.compile(r"[^.!?\n]+[.!?]?")


def normalize(text):
    return (text.replace("’", "'").replace("‘", "'")
                .replace("“", '"').replace("”", '"'))


def split_notes(text):
    """Return (body, notes, run_line). Notes are trailing 'Note:' lines; 'Run:' is the run record."""
    lines = normalize(text).rstrip().splitlines()
    notes, run = [], None
    while lines and (not lines[-1].strip() or lines[-1].startswith(("Note:", "Run:"))):
        line = lines.pop()
        if line.startswith("Note:"):
            notes.insert(0, line)
        elif line.startswith("Run:"):
            run = line
    return "\n".join(lines).strip() + "\n", notes, run


def flat(s):
    return re.sub(r"\s+", " ", s).strip()


def protected_items(body, glossary=None):
    prose = mask_code(body)
    terms = defined_terms(body, glossary)
    codes = set(CODE_RE.findall(prose))
    return {
        "numbers": sorted(set(NUM_RE.findall(CODE_RE.sub(" ", prose)))),
        "codes": sorted(codes),
        "quotes": sorted({flat(q) for q in QUOTE_RE.findall(prose) if len(q.strip()) >= 3}),
        "bold_labels": sorted(set(BOLD_LABEL_RE.findall(body))),
        "placeholders": sorted(set(MARK_RE.findall(mask_code(body)))),
        "code_blocks": code_blocks(body),
        "defined_terms": sorted(terms, key=lambda t: (-terms[t], t)),
    }


def headings(body):
    return [(m.group(2), body[:m.start()].count("\n") + 1) for m in HEADING_RE.finditer(body)]


def capitalized_words(body):
    """Words the text capitalizes mid-sentence at least once (names), with singular/plural variants."""
    found = set()
    for line in mask_code(body).splitlines():
        if line.lstrip().startswith("#"):
            continue
        for sentence in re.split(r"(?<=[.!?:])\s+|\|", line):
            for w in sentence.strip().lstrip("-*0-9.() ").split()[1:]:
                w = w.strip(".,;:()\"'*")
                if w[:1].isupper() and not w.isupper():
                    found.update({w, w + "s", w[:-1] if w.endswith("s") else w})
    return found


def title_case_headings(body, names=None):
    """Headings with capitalized words that are not names (defined terms, words capitalized elsewhere) or acronyms.

    A heading equal to the front-matter title is the document's name and is never flagged."""
    allowed = {w for t in (names or defined_terms(body)) for w in t.split()} | capitalized_words(body)
    title = front_matter_title(body)
    bad = []
    for text, line in headings(mask_code(body)):
        if title and text.strip() == title:
            continue
        words = [w for part in text.split(":") for w in re.findall(r"[A-Za-z][A-Za-z'-]*", part)[1:]]
        if any(w[0].isupper() and not w.isupper() and w not in allowed for w in words):
            bad.append((line, text))
    return bad


def sentence_stats(body):
    prose = "\n".join(l for l in body.splitlines() if not l.lstrip().startswith(("#", "|")))
    prose = re.sub(r"(?<!\n)\n(?!\n|\s*(?:[-*]|\d+\.)\s)", " ", prose)
    lengths = [len(s.split()) for s in SENT_RE.findall(prose) if len(s.split()) >= 2]
    if len(lengths) < 2:
        return {"sentences": len(lengths), "mean": float(lengths[0]) if lengths else 0.0, "stdev": 0.0}
    return {"sentences": len(lengths), "mean": round(statistics.mean(lengths), 1),
            "stdev": round(statistics.stdev(lengths), 1)}


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def inside_mark(text, start, end):
    for m in MARK_RE.finditer(text):
        if m.start() <= start and end <= m.end():
            return True
    return False


def code_blocks(body):
    return [m.group(0) for m in FENCE_RE.finditer(body)]


def mask_code(body):
    """Blank out fenced code blocks, keeping line numbers, so scans skip them."""
    return FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), body)


MONTHS = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
STOP = {"The", "A", "An", "It", "Its", "This", "That", "These", "Those", "To", "At", "In", "On", "Of", "For", "By",
        "With", "And", "Or", "But", "If", "When", "While", "No", "Not", "All", "Each", "Every", "Any", "Make", "Keep",
        "Check", "Met", "Figure", "Table", "Note", "See", "Yes"}


def defined_terms(body, glossary=None):
    """Names to keep verbatim: capitalized terms used at least twice mid-sentence, plus glossary terms that occur.

    Sentence-initial, cell-initial, and list-initial words are skipped; month names and common function
    words never form a term on their own; multi-word terms are kept whole."""
    prose = mask_code(body)
    counts = {}
    for line in prose.splitlines():
        if line.lstrip().startswith("#"):
            continue
        for sentence in re.split(r"(?<=[.!?:])\s+|\|", line):
            words = re.sub(r"^[-*0-9.()\s]+|^\*\*[^*]*\*\*\s*", "", sentence.strip()).split(" ", 1)
            rest = words[1] if len(words) > 1 else ""
            for m in CAP_RUN_RE.finditer(rest):
                parts = m.group(0).split()
                while parts and (parts[-1] in MONTHS or parts[-1].lower() in ("of", "and", "for", "on", "the", "to", "in")):
                    parts.pop()
                term = " ".join(parts)
                if not term or term.isdigit() or (len(parts) == 1 and (term in STOP or term in MONTHS)):
                    continue
                counts[term] = counts.get(term, 0) + 1
    terms = {t: n for t, n in counts.items() if n >= 2}
    for t in glossary or ():
        n = len(re.findall(r"(?<![A-Za-z])" + re.escape(t) + r"(?![a-z])", prose))
        if n:
            terms[t] = max(terms.get(t, 0), n)
    return terms


# Markdown layout. A line break inside a paragraph renders as a space, so joining a paragraph that is
# hard-wrapped mid-sentence never changes the rendered document. Paragraphs whose lines all end a
# sentence (one sentence per line) are left as written: that layout is a choice, not a wrap.
BLOCK_START_RE = re.compile(r"^\s*(?:#{1,6}\s|[-*+]\s|\d+[.)]\s|>|```|~~~|\[[^\]]+\]:|\*\*[^*]+(?::\*\*|\*\*:)|[A-Z][^:\n.!?]{0,40}:\s)")
RULE_RE = re.compile(r"^\s{0,3}(?:(?:[-*_]\s*){3,}|=+\s*|-+\s*)$")
SENTENCE_END_RE = re.compile(r"[.!?][\"')\]*_`]*$")
LIST_PREFIX_RE = re.compile(r"^(\s*(?:>\s?)*\s*(?:[-*+]\s+|\d+[.)]\s+|#{1,6}\s+)?)")


TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")
HTML_TAGS = ("address|article|aside|blockquote|body|br|center|details|dialog|dd|div|dl|dt|figcaption|figure|footer|"
             "form|h[1-6]|head|header|hr|html|iframe|img|li|link|main|meta|nav|ol|p|picture|pre|script|section|source|"
             "style|summary|table|tbody|td|tfoot|th|thead|tr|ul|video|a|span|sub|sup|kbd|b|i|em|strong|code")
HTML_RE = re.compile(r"^\s*(?:<!--|<\?|</?(?:" + HTML_TAGS + r")(?:\s|/?>|$)|</?[A-Za-z][\w-]*(?:\s[^<>]*)?/?>\s*$)", re.I)


def _is_table(lines, i):
    """A table row: starts or ends with a pipe outside inline code, or sits next to a separator row."""
    core = re.sub(r"`[^`]*`", "", lines[i]).strip()
    if "|" not in core:
        return False
    if core.startswith("|") or core.endswith("|") or TABLE_SEP_RE.match(lines[i]):
        return True
    return any(0 <= j < len(lines) and TABLE_SEP_RE.match(lines[j]) for j in (i - 1, i + 1))


def _layout(body):
    """Classify each line: 'prose' (may join a neighbour), 'hard' (prose ending in a Markdown line break),
    or 'fixed' (blank, code, front matter, HTML, table, heading, rule)."""
    lines = body.split("\n")
    kinds, fence, comment, managed, prev_blank = [], None, False, None, True
    for i, line in enumerate(lines):
        s = re.sub(r"^\s*(?:>\s?)*", "", line).strip() if not (i == 0 and line.strip() == "---") else "---"
        if i == 0 and s == "---":
            fence = "---"
            kinds.append("fixed")
            continue
        if fence:
            if (fence == "---" and s in ("---", "...")) or (fence != "---" and s.startswith(fence)):
                fence = None
            kinds.append("fixed")
            continue
        if s.startswith(("```", "~~~")):
            fence = s[:3]
            kinds.append("fixed")
            continue
        managed_start = re.match(r"<!-- ([\w-]+):(?:begin|start)\b", s)
        if managed or managed_start:
            if managed_start and not managed:
                managed = managed_start.group(1)
            elif managed and re.match(r"<!-- " + re.escape(managed) + r":end\b", s):
                managed = None
            kinds.append("fixed")
            continue
        if comment or s.startswith("<!--"):
            comment = "-->" not in s
            kinds.append("fixed")
            continue
        quote_only = line.strip() and not s
        if (not s or _is_table(lines, i) or HTML_RE.match(s) or s.startswith("#") or RULE_RE.match(line)
                or (prev_blank and re.match(r"^(?: {4}|\t)", line))):
            kinds.append("fixed")
        elif line.endswith("  ") or line.endswith("\\"):
            kinds.append("hard")
        else:
            kinds.append("prose")
        prev_blank = not s or bool(quote_only)
    return lines, kinds


def _quote_depth(line):
    m = re.match(r"^\s*((?:>\s?)*)", line)
    return m.group(1).count(">")


def _paragraphs(body):
    """Chains of consecutive lines that render as one paragraph or list item: (lines, [(start, end), ...])."""
    lines, kinds = _layout(body)
    chains, i = [], 0
    while i < len(lines):
        if kinds[i] == "fixed":
            i += 1
            continue
        j = i
        while (j + 1 < len(lines) and kinds[j] == "prose" and kinds[j + 1] != "fixed"
               and not BLOCK_START_RE.match(re.sub(r"^\s*(?:>\s?)*", "", lines[j + 1]))
               and _quote_depth(lines[j + 1]) == _quote_depth(lines[i])):
            j += 1
        chains.append((i, j))
        i = j + 1
    return lines, chains


ABBREV_END_RE = re.compile(r"\b(?:e\.g|i\.e|vs|cf|approx|incl|esp|viz|no|fig|sec|ch|p|pp)\.$", re.I)


def _mid_sentence(line):
    line = line.rstrip()
    return not SENTENCE_END_RE.search(line) or bool(ABBREV_END_RE.search(line))


SHORT_LINE = 40  # wrapping at a width leaves short lines only at the end of a paragraph


def _next_word(lines, k):
    return re.sub(r"^\s*(?:>\s?)*\s*", "", lines[k + 1]).split(" ", 1)[0]


def _breaks_at_width(lines, k, width):
    """A break that wrapping could have made: the line is long, or the next word would not have fit on it.
    A short line followed by a short word ("Best regards," then "Sam") is a deliberate line break."""
    n = len(lines[k].rstrip())
    return n >= max(SHORT_LINE, int(0.5 * width)) or bool(width and n + 1 + len(_next_word(lines, k)) > width)


def _wrap_width(lines, chains):
    """The width a document was wrapped at, estimated from its lines that break mid-sentence (0 if none)."""
    widths = [len(lines[k].rstrip()) for s, e in chains for k in range(s, e)
              if _mid_sentence(lines[k]) and len(lines[k].rstrip()) >= SHORT_LINE]
    return max(widths) if len(widths) >= 2 else 0


def _width_break(lines, k, width):
    """A break after a sentence is still a wrap when the next word would not have fit on the line."""
    return width and len(lines[k].rstrip()) + 1 + len(_next_word(lines, k)) > width


def _wrapped(lines, start, end, width=0):
    """A chain is hard-wrapped if any line break falls mid-sentence or where the wrap width forced it."""
    return any((_mid_sentence(lines[k]) or _width_break(lines, k, width)) and _breaks_at_width(lines, k, width)
               for k in range(start, end))


def hard_wraps(body):
    """1-based first lines of paragraphs or list items that are hard-wrapped (mid-sentence or at a width)."""
    lines, chains = _paragraphs(body)
    width = _wrap_width(lines, chains)
    return [s + 1 for s, e in chains if e > s and _wrapped(lines, s, e, width)]


def _collapse_spaces(line):
    """Make double spaces inside a sentence single. Keeps indentation, list and heading markers, the
    two-space line break at the end, inline code, and the spacing after a sentence or a colon."""
    prefix = LIST_PREFIX_RE.match(line).group(1)
    rest, out, pos = line[len(prefix):], [], 0
    for m in re.finditer(r"`[^`]*`|(?<=\S) {2,}(?=\S)", rest):
        if m.group(0).startswith("`"):
            continue
        before = re.sub(r"[\"')\]*_]+$", "", rest[:m.start()])
        if before.endswith((".", "!", "?", ":")):
            continue
        out.append(rest[pos:m.start()] + " ")
        pos = m.end()
    return prefix + "".join(out) + rest[pos:]


def inner_spaces(body):
    """1-based lines with a double space inside a sentence."""
    lines, kinds = _layout(body)
    return [i + 1 for i, (l, k) in enumerate(zip(lines, kinds)) if k != "fixed" and _collapse_spaces(l) != l]


def tidy(body):
    """Join paragraphs and list items hard-wrapped mid-sentence into one line each, and make double spaces
    inside sentences single. Nothing else changes: rendered Markdown stays the same."""
    lines, kinds = _layout(body)
    lines = [_collapse_spaces(l) if k != "fixed" else l for l, k in zip(lines, kinds)]
    lines, chains = _paragraphs("\n".join(lines))
    width = _wrap_width(lines, chains)
    out, i = [], 0
    for s, e in chains:
        out.extend(lines[i:s])
        if e > s and _wrapped(lines, s, e, width):
            parts = [lines[s].rstrip()] + [re.sub(r"^\s*(?:>\s?)*\s*", "", lines[k]).rstrip() for k in range(s + 1, e)]
            last = re.sub(r"^\s*(?:>\s?)*\s*", "", lines[e])
            out.append(" ".join(parts + [last]))
        else:
            out.extend(lines[s:e + 1])
        i = e + 1
    out.extend(lines[i:])
    return "\n".join(out)


FRONT_TITLE_RE = re.compile(r"^(?:```ya?ml|---)\s*\n(?:.*\n)*?\s*title:\s*(.+?)\s*\n", re.M)


def front_matter_title(body):
    m = FRONT_TITLE_RE.search(body)
    return m.group(1).strip().strip("'\"") if m else None


def glossary_terms(body):
    """First-column entries of a Markdown table whose header starts with Term (a glossary or vocabulary)."""
    terms, in_table = [], False
    for line in body.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.strip().startswith("|") else None
        if not cells:
            in_table = False
            continue
        if cells[0].lower() in ("term", "terms"):
            in_table = True
            continue
        if in_table and cells[0] and not set(cells[0]) <= set("-: "):
            term = re.sub(r"[*_`]", "", cells[0]).strip()
            if term and term[0].isupper():
                terms.append(term)
    return terms
