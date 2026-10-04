"""Suggest a mode (untouchable, protected, standard) and a register (internal, external).

These are suggestions with evidence. The agent confirms or overrides them with
--mode / --register and says why.
"""
import re

from humanize.text import glossary_terms

LEGAL_MARKERS = [r"\bhereby\b", r"\bherein\b", r"\bthereof\b", r"\bpursuant to\b", r"\bindemnif\w*",
                 r"\bgoverning law\b", r"\bthis agreement\b", r"\bthe parties\b", r"\bparty hereto\b",
                 r"\bin witness whereof\b", r"\bnotwithstanding\b", r"\bliabilit\w*"]

# Whole-document shapes: a commit message starts with a type prefix; a changelog has several version headings.
COMMIT_RE = re.compile(r"^(?:feat|fix|chore|refactor|docs)(?:\([^)]*\))?!?:\s", re.I)
CHANGELOG_RE = re.compile(r"^#+\s*\[?v?\d+\.\d+\.\d+\]?", re.M)

PROTECTED = [
    (r"\b(?:call|dial)\s+(?:999|911|112|000)\b|\bA&E\b|\bambulance\b|\bemergency (?:help|services|department|room)\b", "emergency instruction", 3),
    (r"\bchok\w*|\bdifficulty breathing\b|\bseizure\w*|\ballerg\w*|\banaphyla\w*|\boverdose\b", "medical warning sign", 3),
    (r"\bdos(?:e|age)s?\b|(?-i:\d\s?mg\b)|\bmedication\w*|\bprescription\w*|\bsymptom\w*|\bdiagnos\w*", "medical content", 2),
    (r"\bclinical\b|\bpatient\w*|\bcaregiver\w*|\bcarer\w*|\btherap\w*|\bbehaviou?r\w*|\breinforc\w+|\bantecedent\w*", "clinical or behavioral guidance", 2),
    (r"\bchild\b|\bchildren\b|\btoddler\w*|\binfant\w*|\bdistress\w*|\bsafeguard\w*|\bself-harm\b", "care of a child or vulnerable person", 1),
    (r"\bdanger\w*|\bhazard\w*|\bwarning:|\birreversibl\w*|\bpermanently delet\w*|\bCVE-\d", "safety or security warning", 2),
    (r"\brunbook\b|\brollback\b|\bstep \d+\b", "ordered procedure", 1),
    (r"\b(?:do not|don't|never)\s+(?:withhold|withdraw|provoke|punish|restrain|force|shake|give|leave|use|ignore|delete|run)\b", "safety instruction", 2),
    (r"\btantrum\w*|\bmeltdown\w*|\battention-seeking\b|\bde-?escalat\w*|\bsupport plan\b", "behavior-support guidance", 2),
]

# Words like "behavior", "diagnose", "symptom", "child", or "do not use" are everyday vocabulary in software and
# process documents. These signals count only when the document is about the care of a person.
NEEDS_CARE_CONTEXT = {"medical content", "clinical or behavioral guidance", "care of a child or vulnerable person",
                      "safety instruction"}
CARE_CONTEXT = re.compile(
    r"\bpatients?\b|\bclinicians?\b|\bcaregivers?\b|\bcarers?\b|\bnurs(?:e|es|ing)\b|\bGP\b|\bNHS\b|\bA&E\b"
    r"|\bambulance\b|\bmedication\w*|\bdos(?:e|age)s?\b|\d\s?mg\b|\btoddlers?\b|\binfants?\b|\bbab(?:y|ies)\b"
    r"|\b(?:your|my|her|his|their|our) (?:child|children|daughter|son|toddler|baby)\b|\bparents? (?:or|and) carers?\b"
    r"|\bautis\w*|\bmeltdowns?\b"
    r"|\btantrums?\b|\bsafeguarding\b|\btherapists?\b|\bpupils?\b|\bresidents?\b|\bservice users?\b"
    r"|\bhomework\b|\bclassroom\b|\bteachers?\b|\b(?:an|the) adults?\b|\battention-seeking\b|\bdistress\w*", re.I)

# Rules an agent or a reader must follow exactly; dense use marks instructions, procedures, or policy.
NORMATIVE_RE = re.compile(r"\b(?:must(?: not)?|never|do not|don't|only (?:when|if)|requires?|shall|may not|cannot)\b", re.I)

EXTERNAL = r"\byou\b|\byour\b|\bproposal\b|\bclient\w*\b|\bcustomer\w*\b|\bpartner\w*\b|\bwe propose\b|\bsolution\w*\b|\bpricing\b|\boffer\w*\b"
INTERNAL = r"\bhi team\b|\bteam\b|\bstatus\b|\bupdate\b|\bQ[1-4]\b|\bsprint\b|\bmilestone\w*\b|\bstakeholder\w*\b|\bour\b|\bproject\b|\binternal\b"


def suggest_mode(body):
    code = sum(len(b) for b in re.findall(r"^```.*?^```", body, re.M | re.S))
    if body.strip() and code / len(body) > 0.5:
        return {"mode": "untouchable", "evidence": ["mostly code"], "score": None}
    legal = [m for m in LEGAL_MARKERS if re.search(m, body, re.I)]
    if len(legal) >= 2:
        return {"mode": "untouchable", "evidence": [f"legal or contract language ({len(legal)} distinct markers)"],
                "score": None}
    first = next((l for l in body.splitlines() if l.strip()), "")
    if COMMIT_RE.match(first):
        return {"mode": "untouchable", "evidence": ["commit message"], "score": None}
    if len(CHANGELOG_RE.findall(body)) >= 2:
        return {"mode": "untouchable", "evidence": ["changelog"], "score": None}
    care = bool(CARE_CONTEXT.search(body))
    score = 0
    weighted = []
    for pattern, reason, weight in PROTECTED:
        if reason in NEEDS_CARE_CONTEXT and not care:
            continue
        found = re.findall(pattern, body, re.I | re.M)
        if found:
            score += weight
            weighted.append((weight * len(found), f"{reason} ({len(found)}x)"))
    evidence = [e for _, e in sorted(weighted, key=lambda x: -x[0])]
    rules = len(NORMATIVE_RE.findall(body))
    if re.match(r"\A---\s*\n(?:.*\n)*?name:.*\n(?:.*\n)*?description:", body):
        score += 3
        evidence.insert(0, "instructions for an assistant (skill or role front matter)")
    elif rules >= 8 and rules * 100 / max(len(body.split()), 1) >= 1.0:
        score += 3
        evidence.insert(0, f"normative instructions ({rules} must/never/do-not/only-when rules)")
    terms = glossary_terms(body)
    if len(terms) >= 5:  # a glossary defines terms other documents rely on: its wording is normative
        score += 3
        evidence.insert(0, f"glossary of defined terms ({len(terms)} terms)")
    shall = len(re.findall(r"\bshall\b", body, re.I))
    if shall >= 3:
        score += 3
        evidence.insert(0, f"normative policy wording ({shall}x shall)")
    mode = "protected" if score >= 3 else "standard"
    return {"mode": mode, "evidence": evidence, "score": score}


def suggest_register(body):
    ext = len(re.findall(EXTERNAL, body, re.I))
    internal = len(re.findall(INTERNAL, body, re.I))
    register = "internal" if internal > ext else "external"
    return {"register": register, "external_signals": ext, "internal_signals": internal}
