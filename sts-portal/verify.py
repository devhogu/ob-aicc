#!/usr/bin/env python3
"""Check the generated STS trial's browser paths and source-content preservation."""
from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "html-alt/sts/en"
OUTPUT = ROOT / "html/sts/en"
PAGES = [
    "index.html", "operating-model/index.html", "managed-service-model/index.html",
    "reference/index.html", "prototypes/spom/index.html",
    "prototypes/spom/01-control-plane.html", "prototypes/spom/02-service-lifecycle.html",
    "prototypes/spom/03-portfolio-operating-model.html",
]


class Headings(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: list[str] = []
        self.tag: str | None = None
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3"):
            self.tag = tag
            self.parts = []

    def handle_data(self, data):
        if self.tag:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == self.tag:
            self.values.append(" ".join("".join(self.parts).split()))
            self.tag = None


def headings(path: Path) -> list[str]:
    parser = Headings()
    parser.feed(path.read_text())
    return parser.values


def verify(base: str, artifacts: Path) -> dict:
    artifacts.mkdir(parents=True, exist_ok=True)
    results = {"pages": len(PAGES), "layout_cases": 0, "interactions": [], "failures": []}
    for relative in PAGES:
        original = headings(SOURCE / relative)
        rendered = iter(headings(OUTPUT / relative))
        if not all(any(candidate == heading for candidate in rendered) for heading in original):
            results["failures"].append(f"Heading content changed: {relative}")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        errors = []
        external = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("response", lambda response: errors.append(f"HTTP {response.status}: {response.url}") if response.status >= 400 else None)
        page.on("request", lambda request: external.append(request.url) if not request.url.startswith(base) and not request.url.startswith("data:") else None)
        for theme in ("dark", "light"):
            page.goto(f"{base}/index.html")
            page.evaluate("theme=>{localStorage.setItem('obank-sts-theme',theme)}", theme)
            for relative in PAGES:
                for width in (1440, 768, 390, 320):
                    page.set_viewport_size({"width": width, "height": 900})
                    page.goto(f"{base}/{relative}")
                    page.evaluate("document.fonts.ready")
                    geometry = page.evaluate("({viewport:innerWidth,document:document.documentElement.scrollWidth})")
                    if geometry["document"] > geometry["viewport"] + 1:
                        results["failures"].append({"page": relative, "theme": theme, "width": width, "overflow": geometry})
                    if page.locator("h1").count() != 1:
                        results["failures"].append({"page": relative, "theme": theme, "width": width, "heading": "Expected one h1"})
                    if page.locator("html").get_attribute("data-theme") != theme:
                        results["failures"].append({"page": relative, "theme": theme, "width": width, "theme_state": "Wrong theme"})
                    results["layout_cases"] += 1
                if theme == "dark" and relative in ("index.html", "reference/index.html", "prototypes/spom/02-service-lifecycle.html"):
                    page.set_viewport_size({"width": 1440, "height": 900})
                    page.screenshot(path=str(artifacts / (relative.replace("/", "-") + ".png")), full_page=True)

        page.set_viewport_size({"width": 1440, "height": 900})
        page.goto(f"{base}/index.html")
        page.locator('[data-sts-state="active"]').click()
        assert page.locator("#sts-state-title").inner_text() == "Active"
        assert page.locator('[data-sts-state="active"]').get_attribute("aria-pressed") == "true"
        page.locator("#sts-state-link").click()
        assert page.url.endswith("#state-active")
        assert page.locator('[data-state="active"]').get_attribute("aria-pressed") == "true"
        results["interactions"].append("Overview state selection follows the same state into the lifecycle prototype")

        page.goto(f"{base}/index.html")
        page.locator("#sts-map-focus").click()
        assert page.locator("body").evaluate("e=>e.classList.contains('sts-map-focus')")
        assert page.locator("#sts-map-focus").get_attribute("aria-pressed") == "true"
        page.locator("#sts-map-focus").click()
        assert page.locator("#sts-map-focus").get_attribute("aria-pressed") == "false"
        page.locator("#theme-switch").click()
        theme = page.locator("html").get_attribute("data-theme")
        page.goto(f"{base}/managed-service-model/index.html")
        assert page.locator("html").get_attribute("data-theme") == theme
        results["interactions"].append("Map focus restores navigation; theme persists across pages")

        page.goto(f"{base}/reference/index.html")
        tabs = page.locator('[data-flow-tab]')
        assert tabs.count() == 3
        tabs.first.focus()
        page.keyboard.press("ArrowRight")
        assert tabs.nth(1).get_attribute("aria-selected") == "true"
        assert page.locator('[data-flow-panel="itil-service-value-chain"]').is_visible()
        page.keyboard.press("End")
        assert tabs.last.get_attribute("aria-selected") == "true"
        results["interactions"].append("Industry reference tabs switch by keyboard")

        page.goto(f"{base}/prototypes/spom/01-control-plane.html")
        page.locator('[data-node="scheduler"]').click()
        assert page.locator("#detail-title").inner_text() == "Portfolio scheduler"
        page.goto(f"{base}/prototypes/spom/02-service-lifecycle.html")
        page.locator('[data-state="migrating"]').click()
        assert page.locator("#state-title").inner_text() == "Migrating"
        page.locator('[data-control="decision"]').click()
        assert page.locator('[data-control="decision"]').get_attribute("aria-pressed") == "true"
        results["interactions"].append("Control-plane and lifecycle inspectors respond to selection")

        page.set_viewport_size({"width": 390, "height": 850})
        page.goto(f"{base}/index.html")
        assert not page.locator(".o-nav details").evaluate("e=>e.open")
        page.locator(".o-nav summary").click()
        assert page.get_by_role("link", name="Industry reference").is_visible()
        results["interactions"].append("Mobile navigation opens as a labelled disclosure")
        browser.close()
        results["failures"].extend(errors)
        results["failures"].extend(f"External request: {url}" for url in external)
    (artifacts / "report.json").write_text(json.dumps(results, indent=2) + "\n")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8904/en")
    parser.add_argument("--artifacts", type=Path, default=ROOT / "sts-portal/verification")
    args = parser.parse_args()
    report = verify(args.url.rstrip("/"), args.artifacts)
    print(json.dumps(report, indent=2))
    raise SystemExit(1 if report["failures"] else 0)
