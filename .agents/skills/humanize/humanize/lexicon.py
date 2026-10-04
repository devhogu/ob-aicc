"""The tell lexicon: load tells.json and scan text for hits."""
import json
import re
from functools import lru_cache

from humanize import DATA
from humanize.text import inside_mark, line_of, normalize

SUFFIXES = r"(?:e|s|es|d|ed|ing|ly|y|ally)?"


def _pattern(term):
    words = term.lower()
    if re.fullmatch(r"[a-z]+", words):
        stem = words[:-1] if words.endswith("e") and len(words) > 4 else words
        return r"\b" + re.escape(stem) + SUFFIXES + r"\b"
    escaped = re.escape(words).replace(r"\-", "[- ]").replace(r"\ ", r"\s+")
    return r"\b" + escaped + r"\b"


@lru_cache(maxsize=1)
def load():
    data = json.loads((DATA / "tells.json").read_text())
    entries = []
    for e in data["terms"]:
        e = dict(e)
        e.setdefault("s", "high")
        e["re"] = re.compile(e.get("pattern") or _pattern(e["t"]), re.I)
        entries.append(e)
    return data["categories"], data["sources"], entries


START_CONTEXT = re.compile(r"(?:^|[.!?:]\s+|\n)\s*(?:[-*]\s+|\d+\.\s+|\*\*)?$")

# A mention names a word instead of using it: "delve", `delve`, *delve* mid-sentence, "delve -> explore",
# or a short table cell. Word lists and style guides are full of mentions; they are not tells.
QUOTED_RE = re.compile(r"\"[^\"\n]{1,80}\"|`[^`\n]+`|(?<=[\w,;)] )\*\*[^*\n]{1,60}\*\*|(?<![*\w])\*[^*\n]{1,60}\*(?![*\w])"
                       r"|(?<![\w])_[^_\n]{1,60}_(?![\w])|'[^'\n]{1,40}'(?!\w)")


def _mentions(text):
    spans = [(m.start(), m.end()) for m in QUOTED_RE.finditer(text)]
    for m in re.finditer(r"^.*$", text, re.M):
        line = m.group(0)
        stripped = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)
        items = [i for i in re.split(r",\s*|\s+(?:and|or)\s+", stripped.rstrip(".;")) if i.strip()]
        if len(items) >= 5 and sum(len(i.split()) <= 3 for i in items) >= len(items) - 1:
            spans.append((m.start(), m.end()))  # "delve, tapestry, landscape, ...": a list of words, not prose
        elif re.search(r"\s(?:→|->|=>)\s", line):  # "delve -> explore": the line maps words to replacements
            spans.append((m.start(), m.end()))
        elif line.strip().startswith("|"):
            for c in re.finditer(r"[^|]+", line):
                if 0 < len(c.group(0).split()) <= 3:
                    spans.append((m.start() + c.start(), m.start() + c.end()))
        elif ":" in stripped[:45] and (re.match(r"^(?:\*\*|\*|_|\"|`)", stripped)
                                       or len(stripped.split(":")[0].split()) == 1) \
                and len(re.sub(r"[*_\"`]", "", stripped.split(":")[0]).split()) <= 3:
            # "**Delve:** ..." or "Delve: ...": the head names the word the line defines
            head = line.index(":")
            spans.append((m.start(), m.start() + head))
    return spans


def scan(text, mentions=False):
    """Return non-overlapping hits, longest match first, in reading order. Mentions are skipped unless asked for."""
    text = normalize(text)
    categories, _, entries = load()
    spans = [] if mentions else _mentions(text)
    hits = []
    for e in entries:
        for m in e["re"].finditer(text):
            if e.get("start") and not START_CONTEXT.search(text[:m.start()]):
                continue
            if any(a <= m.start() and m.end() <= b for a, b in spans):
                continue
            hits.append({"start": m.start(), "end": m.end(), "match": " ".join(m.group(0).split()), "term": e["t"],
                         "category": e["c"], "signal": e["s"], "plain": e.get("plain", []),
                         "source": e["src"], "line": line_of(text, m.start()),
                         "marked": inside_mark(text, m.start(), m.end())})
    hits.sort(key=lambda h: (h["start"], -(h["end"] - h["start"])))
    kept, last_end = [], -1
    for h in hits:
        if h["start"] >= last_end:
            kept.append(h)
            last_end = h["end"]
    return kept


def action(category):
    return load()[0][category]["action"]


def fails(category, mode):
    key = "fail_protected" if mode == "protected" else "fail_standard"
    return load()[0][category][key]
