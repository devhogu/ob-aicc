#!/usr/bin/env python3
"""Browser checks for the generated bilingual CSR trial."""
from __future__ import annotations

import json
from pathlib import Path
import re

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "html-alt/intelligent-customer-service-resolution"
OUTPUT = ROOT / "html/csr"
ARTIFACTS = ROOT / "csr-portal/verification"
BASE = "http://127.0.0.1:8905"


def headings(content: str) -> list[str]:
    return [" ".join(re.sub(r"<[^>]+>", " ", match).split())
            for match in re.findall(r"<h[1-5]\b[^>]*>.*?</h[1-5]>", content, re.S)]


def verify() -> dict:
    ARTIFACTS.mkdir(exist_ok=True)
    result = {"languages": 2, "layouts": 0, "source_diagrams_per_language": 34, "interactions": [], "failures": []}
    for lang in ("ru", "en"):
        original = (SOURCE / lang / "index.html").read_text()
        rendered = (OUTPUT / lang / "index.html").read_text()
        expected = headings(original)
        actual = iter(headings(rendered))
        if not all(any(item == title for item in actual) for title in expected):
            result["failures"].append(f"Source heading changed or lost: {lang}")
        if original.count('<figure class="diagram"') != 34 or rendered.count('<figure class="diagram"') != 34:
            result["failures"].append(f"Source diagrams changed: {lang}")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        errors = []
        external = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("response", lambda response: errors.append(f"HTTP {response.status}: {response.url}") if response.status >= 400 else None)
        page.on("request", lambda request: external.append(request.url) if not request.url.startswith(BASE) and not request.url.startswith("data:") else None)
        for theme in ("dark", "light"):
            page.goto(BASE + "/ru/index.html")
            page.evaluate("value=>localStorage.setItem('obank-csr-theme',value)", theme)
            for lang in ("ru", "en"):
                for width in (1440, 768, 390, 320):
                    page.set_viewport_size({"width": width, "height": 900})
                    page.goto(f"{BASE}/{lang}/index.html")
                    page.evaluate("document.fonts.ready")
                    state = page.evaluate("({viewport:innerWidth,document:document.documentElement.scrollWidth,theme:document.documentElement.dataset.theme,header:document.querySelector('.csr-header').getBoundingClientRect().height})")
                    if state["document"] > state["viewport"] + 1:
                        result["failures"].append({"page": lang, "theme": theme, "width": width, "overflow": state})
                    if state["theme"] != theme:
                        result["failures"].append({"page": lang, "theme": theme, "width": width, "state": state})
                    if page.locator("h1").count() != 1 or page.locator("[data-csr-step]").count() != 8:
                        result["failures"].append({"page": lang, "width": width, "structure": "missing heading or stage"})
                    result["layouts"] += 1
                if theme == "dark":
                    page.set_viewport_size({"width": 1440, "height": 900})
                    page.goto(f"{BASE}/{lang}/index.html")
                    page.screenshot(path=str(ARTIFACTS / f"{lang}-desktop.png"), full_page=False)
        page.set_viewport_size({"width": 1440, "height": 900})
        page.goto(BASE + "/ru/index.html")
        page.locator('[data-csr-step="4"]').click()
        assert page.locator('[data-csr-step="4"]').get_attribute("aria-pressed") == "true"
        assert page.locator("#csr-step-title").inner_text() == page.locator('[data-csr-step="4"] strong').inner_text()
        assert "step=4" in page.url
        page.locator("#csr-map-focus").click()
        assert page.locator("body").evaluate("e=>e.classList.contains('csr-map-focused')")
        page.locator("#csr-map-focus").click()
        assert not page.locator("body").evaluate("e=>e.classList.contains('csr-map-focused')")
        result["interactions"].append("stage selection, inspector, URL and map focus")

        page.goto(BASE + "/ru/index.html#ru-business-use-case-карта-встраивания-в-процесс")
        page.locator('[data-csr-language]').click()
        assert "en-business-use-case-process-integration-map" in page.url
        assert page.locator("html").get_attribute("lang") == "en"
        result["interactions"].append("language switch preserves matching source section")

        page.locator("#csr-theme").click()
        chosen = page.locator("html").get_attribute("data-theme")
        page.reload()
        assert page.locator("html").get_attribute("data-theme") == chosen
        result["interactions"].append("theme persists across navigation")

        figure = page.locator("figure.diagram").first
        figure.focus()
        page.keyboard.press("Enter")
        assert page.locator("#diagram-viewer").is_visible()
        page.locator("#diagram-zoom-in").click()
        assert page.locator("#diagram-zoom-value").inner_text() != "100%"
        page.keyboard.press("Escape")
        assert page.locator("#diagram-viewer").is_hidden()
        assert figure.evaluate("e=>document.activeElement===e")
        result["interactions"].append("diagram opens by keyboard, zooms, closes and restores focus")

        page.set_viewport_size({"width": 390, "height": 850})
        page.goto(BASE + "/ru/index.html")
        page.locator("#menu-button").click()
        assert page.locator("#menu-button").get_attribute("aria-expanded") == "true"
        page.locator("#mobile-shade").click(position={"x": 380, "y": 200})
        assert page.locator("#menu-button").get_attribute("aria-expanded") == "false"
        result["interactions"].append("mobile document navigation opens and closes")
        browser.close()
        result["failures"].extend(errors)
        result["failures"].extend(f"External request: {url}" for url in external)
    (ARTIFACTS / "report.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    return result


if __name__ == "__main__":
    report = verify()
    print(json.dumps(report, indent=2, ensure_ascii=False))
    raise SystemExit(1 if report["failures"] else 0)
