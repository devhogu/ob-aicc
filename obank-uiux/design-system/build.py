#!/usr/bin/env python3
"""Build the standalone internal UI/UX guide from the shared source kit."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
from string import Template
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from markdown_it import MarkdownIt

HERE = Path(__file__).resolve().parent
PORTAL = HERE.parent
ASSETS = PORTAL / "ui-comps"
PAGES = [
    ("index", "Начало", "Start here", "ui-map"),
    ("foundations", "Бренд и стиль", "Brand and style", "ui-layers"),
    ("layout", "Макет и навигация", "Layout and navigation", "ui-panel-left"),
    ("components", "Компоненты", "Components", "ui-table-properties"),
    ("patterns", "Сценарии и примеры", "Patterns and examples", "ui-workflow"),
    ("cloud-lab", "Карта Cloud LAB", "Cloud LAB map", "ui-git-branch"),
    ("assets", "Ресурсы", "Assets", "ui-download"),
    ("adoption", "Как использовать", "Adoption", "ui-file-text"),
]
FONTS = [("Golos Text", "100 900", "golos-text/GolosText-variable.woff2")]
FONTS += [("TT Norms Pro", str(weight), f"tt-norms-pro/tt-norms-pro-{weight}.woff2") for weight in (400, 500, 700)]


def write(root: Path, relative: str, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy(root: Path, source: Path, relative: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, path)


def icon(name: str) -> str:
    return (ASSETS / f"icons/{name}.svg").read_text().replace(
        "<svg ", '<svg class="o-icon" aria-hidden="true" focusable="false" ', 1
    )


def navigation(current: str) -> str:
    return "".join(
        f'<a href="{slug}.html"' + (' aria-current="page"' if slug == current else '')
        + f'>{icon(glyph)}<span data-ru="{ru}" data-en="{en}">{ru}</span></a>'
        for slug, ru, en, glyph in PAGES
    )


def tokens(base: dict, preset: dict) -> str:
    def rule(selector: str, values: dict) -> str:
        return selector + " {\n" + "".join(f"  --{k}: {v};\n" for k, v in values.items()) + "}\n"
    result = "/* Generated from obank-uiux/tokens/tokens.json + design-system/theme.json. */\n"
    result += rule(":root", base["global"] | preset["global"])
    for theme in ("light", "dark"):
        result += rule(f':root[data-theme="{theme}"]', base["themes"][theme] | preset["themes"][theme])
        result += f':root[data-theme="{theme}"] {{ color-scheme: {theme}; }}\n'
    return result


def asset_gallery(output: Path) -> str:
    selected = []
    cards = []
    inventory = json.loads((ASSETS / "manifest.json").read_text())
    for asset in inventory["assets"]:
        if asset["group"] != "logos":
            continue
        relative = "assets/" + asset["file"]
        copy(output, ASSETS / asset["file"], relative)
        selected.append(asset)
        background = "dark" if asset["background"] in ("dark", "either") else "light"
        cards.append(
            f'<article class="o-asset" data-asset="{asset["id"]} logo">'
            f'<div class="o-asset-sample logo-{background}"><img src="{relative}" '
            f'alt="{asset["id"]}" width="160" height="44" loading="lazy"></div>'
            f'<strong>{asset["id"]}</strong><p>Logo · {asset["background"]} background</p>'
            f'<a href="{relative}" download>Download original</a></article>'
        )
    for path in sorted((ASSETS / "icons").glob("ui-*.svg")):
        relative = "assets/icons/" + path.name
        copy(output, path, relative)
        cards.append(
            f'<article class="o-asset" data-asset="{path.stem} icon">'
            f'<div class="o-asset-sample">{icon(path.stem)}</div>'
            f'<strong>{path.stem}</strong><p>Lucide · SVG · currentColor</p>'
            f'<a href="{relative}" download>Download SVG</a></article>'
        )
    write(output, "assets/manifest.json", json.dumps({"logos": selected}, indent=2, ensure_ascii=False) + "\n")
    for family, weight, file in FONTS:
        role = "body" if family == "Golos Text" else "heading"
        cards.append(
            f'<article class="o-asset" data-asset="{family} {weight} font">'
            f'<div class="o-asset-sample" style="font-family:var(--font-{role});font-size:26px">Aa · Яя</div>'
            f'<strong>{family}</strong><p>WOFF2 · {weight} · {role}</p>'
            f'<a href="assets/fonts/{file}" download>Download font</a>'
            '<a href="assets/FONT-USE.md">Font use and licences</a></article>'
        )
    return (
        '<div class="o-toolbar"><a class="oc-button oc-button--primary" href="o-uiux-kit.zip" download>Download implementation kit</a>'
        '<a class="oc-button" href="manifest.json">Build manifest</a></div>'
        '<label class="oc-field" for="asset-search">Filter assets<input class="oc-input" type="search" id="asset-search"></label>'
        f'<p class="o-caption" id="asset-count" role="status">{len(cards)} assets</p>'
        '<div class="o-asset-grid">' + "".join(cards) + '</div>'
    )


def fonts(output: Path) -> None:
    css = []
    for family, weight, file in FONTS:
        relative = "assets/fonts/" + file
        copy(output, ASSETS / "fonts" / file, relative)
        css.append(f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};font-display:swap;src:url('{relative}') format('woff2');}}")
    write(output, "fonts.css", "\n".join(css) + "\n")
    copy(output, ASSETS / "fonts/golos-text/OFL.txt", "assets/licenses/Golos-OFL.txt")
    copy(output, ASSETS / "licenses/lucide-LICENSE.txt", "assets/licenses/Lucide-LICENSE.txt")
    write(output, "assets/FONT-USE.md", "# Font use\n\nGolos Text includes its OFL licence. TT Norms Pro follows the practitioner's 14 September 2026 authorization for internal O! portal use. Do not redistribute licensed group fonts in a public bundle; revisit font selection for public publication. Provider marks retain their original identity and usage context.\n")


def foundation_samples() -> str:
    roles = ["brand", "surface", "surface-subtle", "text", "text-muted", "action"]
    return '<h2>Live palette and type</h2><div class="o-grid">' + "".join(
        f'<div class="o-card"><div class="o-swatch" style="background:var(--{role})"></div><code>--{role}</code></div>' for role in roles
    ) + '</div><div class="o-card"><h3 style="font-size:28px">TT Norms Pro · Сервисы и возможности</h3><p style="font-size:18px">Golos Text · Понятная информация, ясные связи.<br>Readable information, clear relationships. 0123456789</p></div>'


def component_samples() -> str:
    return '''<h2>Working component specimens</h2>
<div class="o-toolbar"><a class="oc-button oc-button--primary" href="examples.html?pattern=form">Open form example</a><a class="oc-button" href="examples.html?pattern=profile">Explore tabs</a><button class="oc-button" disabled aria-describedby="disabled-reason">Save record</button></div>
<p class="o-caption" id="disabled-reason">Save is unavailable: this guide has no record-storage connection.</p>
<div class="o-toolbar"><span class="oc-badge oc-badge--success">Example confirmed</span><span class="oc-badge oc-badge--warning">Needs clarification</span><span class="oc-badge">Not supplied</span></div>
<details class="oc-disclosure"><summary>Show supporting detail</summary><div>This disclosure keeps the core explanation visible while letting the reader expand supporting context.</div></details>
<h3>Distinguish feedback states</h3><p class="o-error">Example error: a required name is missing. Enter a name to continue.</p><p class="o-success">Example success: the local preview was confirmed. No record was saved.</p>'''


def build(output: Path) -> None:
    # Refuse to mix a generated package with arbitrary files or any source directory.
    marker = output / ".o-uiux-output"
    if output.exists() and any(output.iterdir()) and not marker.is_file():
        raise SystemExit("Choose an empty output directory or an existing O! UI/UX build directory.")
    output.mkdir(parents=True, exist_ok=True)
    if marker.exists():
        old_manifest = output / "manifest.json"
        if old_manifest.exists():
            for entry in json.loads(old_manifest.read_text()).get("files", []):
                path = (output / entry["path"]).resolve()
                if path.is_relative_to(output) and path.is_file():
                    path.unlink()
    write(output, ".o-uiux-output", "Generated UI/UX guide. Edit obank-uiux/design-system sources.\n")
    preset = json.loads((HERE / "theme.json").read_text())
    base = json.loads((PORTAL / "tokens/tokens.json").read_text())
    write(output, "tokens.css", tokens(base, preset))
    copy(output, PORTAL / "tokens/tokens.json", "base-tokens.json")
    primitives = (ASSETS / "ui.css").read_text()
    write(output, "primitives.css", "\n".join(line for line in primitives.splitlines() if not line.lstrip().startswith("@import")) + "\n")
    for file in ("workspace.css", "app.js", "ADOPT.md", "theme.json"):
        copy(output, HERE / file, file)
    for path in (HERE / "content").glob("*.md"):
        copy(output, path, "content/" + path.name)
    fonts(output)
    gallery = asset_gallery(output)
    template = Template((HERE / "shell.html").read_text())
    md = MarkdownIt("commonmark").enable("table")
    search_index = []
    for slug, ru, en, _ in PAGES:
        source = HERE / "ADOPT.md" if slug == "adoption" else HERE / f"content/{slug}.md"
        raw = source.read_text()
        rendered = md.render(raw)
        for page, *_ in PAGES:
            rendered = rendered.replace(f'href="content/{page}.md"', f'href="{page}.html"')
        extra = {"foundations": foundation_samples(), "components": component_samples(), "assets": gallery,
                 "patterns": ""}.get(slug, "")
        if slug == "patterns":
            rendered = rendered.replace("<table>", '<div id="pattern-cards" class="o-grid" lang="ru"></div><h2>Pattern anatomy</h2><table>', 1)
        body = '<p class="o-eyebrow" data-ru="Правила и пояснения · текст на английском" data-en="Guidelines and explanation · English source text">Правила и пояснения · текст на английском</p>'
        body += f'<div class="o-reading"><article class="o-copy o-guide-copy" lang="en">{rendered}{extra}</article>'
        body += '<nav class="o-context" id="page-contents" aria-label="On this page" lang="en"><strong>On this page</strong></nav></div>'
        write(output, slug + ".html", template.substitute(title=en, version=preset["version"], navigation=navigation(slug), body=body))
        search_index.append({"href": slug + ".html", "title": {"ru": ru, "en": en}, "text": raw})
    body = '<p class="o-eyebrow" data-ru="Сценарий · интерактивный пример" data-en="Pattern · interactive example">Сценарий · интерактивный пример</p><h1 id="demo-title">Пример</h1><div id="demo-note"></div><div id="mockup"></div>'
    nav = '<a href="patterns.html">' + icon("ui-arrow-left") + '<span data-ru="Все примеры" data-en="All examples">Все примеры</span></a><div id="demo-navigation"></div>'
    write(output, "examples.html", template.substitute(title="Examples", version=preset["version"], navigation=nav, body=body))
    icons = {path.stem: icon(path.stem) for path in sorted((ASSETS / "icons").glob("ui-*.svg"))}
    write(output, "data.js", "window.UI_ICONS=" + json.dumps(icons, ensure_ascii=False) + ";\nwindow.GUIDE_INDEX=" + json.dumps(search_index, ensure_ascii=False) + ";\n")
    write(output, "README.md", f"# O! UI/UX kit {preset['version']}\n\nInternal O! portal implementation kit. Serve this directory as static files and open index.html. Start with ADOPT.md for reuse. Editable source: obank-uiux/design-system/ in the AICC repository; base tokens: obank-uiux/tokens/; curated assets: obank-uiux/ui-comps/.\n\nGuide explanations are English; shell and interactive examples support Russian and English. Example records are fictional and browser-only. Fonts retain the internal-use restriction in assets/FONT-USE.md.\n")
    # The extracted kit is a complete static guide. Replace its self-download links
    # and give it a manifest of its own bytes, rather than promising a nested ZIP.
    packaged = {}
    for path in sorted(output.rglob("*")):
        if not path.is_file() or path in (output / "o-uiux-kit.zip", output / "manifest.json", marker):
            continue
        payload = path.read_bytes()
        if path.suffix == ".html":
            payload = re.sub(
                r'<a\b[^>]*href="o-uiux-kit\.zip"[^>]*>.*?</a>',
                '<span class="o-caption" lang="en">Implementation kit: this package</span>',
                payload.decode("utf-8"),
            ).encode("utf-8")
        packaged[path.relative_to(output).as_posix()] = payload
    packaged["manifest.json"] = (json.dumps({
        "name": preset["name"], "version": preset["version"],
        "files": [{"path": name, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
                  for name, data in packaged.items()],
    }, indent=2) + "\n").encode("utf-8")
    # Stable timestamps make the downloadable artifact reproducible.
    with ZipFile(output / "o-uiux-kit.zip", "w", compression=ZIP_DEFLATED) as bundle:
        for name, data in packaged.items():
            info = ZipInfo(name, (2026, 10, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            bundle.writestr(info, data)
    files = [{"path": path.relative_to(output).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "bytes": path.stat().st_size}
             for path in sorted(output.rglob("*")) if path.is_file() and path != output / "manifest.json"]
    write(output, "manifest.json", json.dumps({"name": preset["name"], "version": preset["version"], "standing": preset["standing"], "files": files}, indent=2) + "\n")
    print(f"Built {len(PAGES) + 1} pages, 7 interactive patterns and {len(files)} files in {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    build(parser.parse_args().output.resolve())
