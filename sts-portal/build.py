#!/usr/bin/env python3
"""Build the standalone O!-styled STS trial from retained STS pages."""
from __future__ import annotations

from html import escape, unescape
from pathlib import Path
import os
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "html-alt/sts/en"
OUTPUT = ROOT / "html/sts"
KIT = ROOT / "obank-uiux/site"
HERE = Path(__file__).resolve().parent
MARKER = ".sts-o-uiux-output"

PAGES = [
    ("index.html", "Overview"),
    ("operating-model/index.html", "Operating model"),
    ("managed-service-model/index.html", "Managed service"),
    ("reference/index.html", "Industry reference"),
    ("prototypes/spom/index.html", "Prototype lab"),
    ("prototypes/spom/01-control-plane.html", "Control plane"),
    ("prototypes/spom/02-service-lifecycle.html", "Portfolio lifecycle"),
    ("prototypes/spom/03-portfolio-operating-model.html", "Portfolio view"),
]


def rel(from_file: Path, target: Path) -> str:
    return os.path.relpath(target, from_file.parent).replace(os.sep, "/")


def lifecycle_states() -> list[tuple[str, str, str, str]]:
    source = (SOURCE / "prototypes/spom/02-service-lifecycle.html").read_text()
    states = []
    for match in re.finditer(r'<button[^>]+data-state="([^"]+)"[^>]*>(.*?)</button>', source, re.S):
        key, body = match.groups()
        def field(tag: str) -> str:
            item = re.search(fr"<{tag}[^>]*>(.*?)</{tag}>", body, re.S)
            if not item:
                raise ValueError(f"Missing {tag} for {key}")
            return unescape(re.sub(r"<[^>]+>", "", item.group(1))).strip()
        group = "Onboarding" if len(states) < 3 else "In service" if len(states) < 5 else "Transition"
        states.append((key, field("strong"), field("small"), group))
    if len(states) != 7:
        raise ValueError(f"Expected seven source lifecycle states, got {len(states)}")
    return states


def landing_map(states: list[tuple[str, str, str, str]], page: Path) -> str:
    target = OUTPUT / "en/prototypes/spom/02-service-lifecycle.html"
    cards = "".join(
        f'<li><button type="button" data-sts-state="{escape(key)}" aria-pressed="false" '
        f'data-group="{escape(group)}" data-target="{escape(rel(page, target))}#state-{escape(key)}">'
        f'<span class="sts-map-index">{i:02}</span><strong>{escape(title)}</strong><small>{escape(summary)}</small>'
        f'</button></li>'
        for i, (key, title, summary, group) in enumerate(states, 1)
    )
    return f'''<section id="portfolio-path" class="sts-map" aria-labelledby="sts-map-title">
  <div class="sts-map-heading"><div><p class="eyebrow">Lifecycle view · seven visible states</p>
    <h2 id="sts-map-title">From candidate to migration</h2>
    <p>This is the source prototype's conceptual managed-service portfolio path. Improvement can recur; the cards show states, not a mandatory one-way runtime workflow.</p></div>
    <button id="sts-map-focus" type="button" aria-pressed="false">Expand map</button></div>
  <div class="sts-map-scroll" role="region" tabindex="0" aria-label="Scrollable managed-service lifecycle map">
    <ol class="sts-map-track">{cards}</ol>
  </div>
  <div class="sts-map-inspector" aria-live="polite"><div><p class="eyebrow">Selected state</p>
    <h3 id="sts-state-title">Candidate</h3><p id="sts-state-summary">Potential shared service</p></div>
    <div><p id="sts-state-group">Onboarding</p><a id="sts-state-link" href="{escape(rel(page, target))}#state-candidate">Explore lifecycle state →</a></div></div>
</section>'''


def navigation(page: Path) -> str:
    groups = [("Models and reference", PAGES[:4]), ("Explore the concept", PAGES[4:])]
    parts = []
    for heading, items in groups:
        parts.append(f'<span class="sts-nav-group">{escape(heading)}</span>')
        for path, label in items:
            target = OUTPUT / "en" / path
            current = ' aria-current="page"' if target == page else ""
            parts.append(f'<a href="{escape(rel(page, target))}"{current}>{escape(label)}</a>')
    return "".join(parts)


def transform(source: Path, target: Path, states: list[tuple[str, str, str, str]]) -> str:
    content = source.read_text()
    content = re.sub(r'<nav class="(?:site-nav|prototype-nav)"[^>]*>.*?</nav>', '', content, count=1, flags=re.S)
    if source.name == "02-service-lifecycle.html":
        content = re.sub(r'(<button[^>]*data-state="([^"]+)"[^>]*)(>)', lambda m: m.group(1) + f' id="state-{m.group(2)}"' + m.group(3), content)
    if "visual-stage" in content:
        content = content.replace('<section class="visual-stage', '<p class="sts-scroll-hint">Swipe or scroll within the diagram to explore its full width.</p>\n<section role="region" tabindex="0" aria-label="Scrollable STS diagram" class="visual-stage', 1)
    if source == SOURCE / "index.html":
        context_start = content.index('<p class="hero__definition">')
        context_end = content.index('</header>', context_start)
        context = content[context_start:context_end]
        content = content[:context_start] + content[context_end:]
        content = content.replace('<section class="section section--roots"', landing_map(states, target) + '\n<section class="sts-context" aria-label="Reading frame">' + context + '</section>\n<section class="section section--roots"', 1)
    prefix = rel(target, OUTPUT / "en/assets/o-uiux")
    style = "".join(f'<link rel="stylesheet" href="{prefix}/{name}">\n' for name in ("fonts.css", "tokens.css", "workspace.css", "sts.css"))
    early_theme = '<script>try{document.documentElement.dataset.theme=localStorage.getItem("obank-sts-theme")==="light"?"light":"dark"}catch{document.documentElement.dataset.theme="dark"}</script>\n'
    content = content.replace("</head>", early_theme + style + '</head>', 1)
    content = re.sub(r'<a class="skip-link"[^>]*>.*?</a>', '', content, count=1, flags=re.S)
    match = re.search(r'<main\b[^>]*>', content)
    if not match:
        raise ValueError(f"No main in {source}")
    opening = match.group(0)
    classes = re.search(r'class="([^"]+)"', opening)
    page_class = classes.group(1) if classes else "page"
    new_main = f'<main id="main" class="o-main {escape(page_class)}">'
    content = content[:match.start()] + new_main + content[match.end():]
    brand = rel(target, OUTPUT / "en/assets/o-uiux/o-mark.svg")
    home = rel(target, OUTPUT / "en/index.html")
    header = f'''<a class="o-skip" href="#main">Skip to content</a>
<header class="o-header"><a class="o-identity" href="{escape(home)}"><img src="{escape(brand)}" width="34" height="38" alt=""><span>Shared Technology Services</span></a>
  <span class="sts-header-scope">O! workspace · conceptual explorer</span><div class="o-tools"><button id="theme-switch" type="button">Light theme</button></div></header>
<div class="o-frame"><aside class="o-nav"><details><summary>STS sections</summary><nav aria-label="STS sections">{navigation(target)}</nav></details>
  <p class="o-caption">Framework, lifecycle and practice references</p></aside>'''
    content = content.replace('<body>', '<body class="sts-portal">\n' + header, 1)
    foot = '<footer class="sts-footer">Conceptual STS framework and reference views. This presentation does not establish a current O!Bank service inventory or operating assignment.</footer>'
    content = content.replace('</main>', foot + '</main>\n</div>', 1)
    script = f'<script src="{prefix}/sts.js" defer></script>\n'
    content = content.replace('</body>', script + '</body>', 1)
    # Keep the source layout and interactions but remove remote-font import.
    return re.sub(r'[ \t]+(?=\r?$)', '', content, flags=re.M)


def build() -> None:
    if not SOURCE.is_dir() or not KIT.is_dir():
        raise SystemExit("STS source or O! UI/UX build is missing")
    if OUTPUT.exists():
        if not (OUTPUT / MARKER).is_file():
            raise SystemExit("Refusing to replace a non-generated html/sts directory")
        shutil.rmtree(OUTPUT)
    shutil.copytree(SOURCE, OUTPUT / "en")
    (OUTPUT / MARKER).write_text("Generated by sts-portal/build.py from html-alt/sts/en\n")
    styles = OUTPUT / "en/assets/o-uiux"
    styles.mkdir(parents=True)
    for name in ("fonts.css", "tokens.css", "workspace.css"):
        shutil.copyfile(KIT / name, styles / name)
    for name in ("sts.css", "sts.js"):
        shutil.copyfile(HERE / "assets" / name, styles / name)
    shutil.copyfile(KIT / "assets/logos/o-mark.svg", styles / "o-mark.svg")
    shutil.copytree(KIT / "assets/fonts", styles / "assets/fonts")
    source_tokens = OUTPUT / "en/assets/styles/tokens.css"
    source_tokens.write_text(re.sub(r"^@import[^\n]*\n", "", source_tokens.read_text(), count=1))
    states = lifecycle_states()
    for relative, _ in PAGES:
        source = SOURCE / relative
        target = OUTPUT / "en" / relative
        target.write_text(transform(source, target, states))
    (OUTPUT / "index.html").write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=en/index.html"><title>STS</title><a href="en/index.html">Open STS</a></html>\n')
    print(f"Built {len(PAGES)} STS pages + entry point in {OUTPUT}")


if __name__ == "__main__":
    build()
