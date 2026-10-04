#!/usr/bin/env python3
"""Exercise the shared guide's real browser paths; run against a served build."""
import argparse
import json
import os
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright, expect

HERE = Path(__file__).resolve().parent
AXE = Path(os.environ.get("AXE_CORE_PATH", HERE.parent.parent / "portal/.tools/node_modules/axe-core/axe.min.js"))
PATTERNS = ["overview", "catalogue", "profile", "flow", "comparison", "form", "activity"]
PAGES = ["index", "foundations", "layout", "components", "patterns", "cloud-lab", "assets", "adoption"]


def verify(base: str, artifacts: Path):
    artifacts.mkdir(parents=True, exist_ok=True)
    results = {"layout_cases": 0, "accessibility_cases": 0, "interactions": [], "failures": []}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("response", lambda response: errors.append(f"HTTP {response.status}: {response.url}") if response.status >= 400 else None)
        for theme in ("light", "dark"):
            for language in ("ru", "en"):
                routes = [f"examples.html?pattern={name}" for name in PATTERNS] + [f"{name}.html?guide=1" for name in PAGES]
                for route in routes:
                    for width in (1440, 768, 320):
                        page.set_viewport_size({"width": width, "height": 1000})
                        url = f"{base}/{route}&theme={theme}&lang={language}"
                        page.goto(url)
                        page.evaluate("document.fonts.ready")
                        geometry = page.evaluate("({width:innerWidth,actual:document.documentElement.scrollWidth})")
                        if geometry["actual"] > geometry["width"] + 1:
                            results["failures"].append({"url": url, "width": width, "overflow": geometry})
                        if page.locator("h1").count() != 1:
                            results["failures"].append({"url": url, "heading": "Expected one h1"})
                        results["layout_cases"] += 1
                        if width == 1440 and language == "en":
                            page.add_script_tag(path=str(AXE))
                            audit = page.evaluate("async()=> (await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}})).violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>({target:n.target,summary:n.failureSummary}))}))")
                            if audit:
                                results["failures"].append({"url": url, "axe": audit})
                            results["accessibility_cases"] += 1
        (artifacts / "layout-accessibility.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")
        assert not errors, errors

        def visit(pattern):
            page.set_viewport_size({"width": 1440, "height": 1000})
            page.goto(f"{base}/examples.html?pattern={pattern}&theme=dark&lang=en")

        visit("catalogue")
        page.locator("#catalogue-group").select_option("shared")
        page.locator("#catalogue-search").fill("billing")
        assert page.locator("#catalogue-results tbody tr").count() == 1
        page.get_by_role("link", name="Billing", exact=True).click()
        assert page.locator("#mockup h2").inner_text() == "Billing"
        assert "Explain charges and payments" in page.locator("#panel-summary").inner_text()
        page.go_back()
        page.locator("#catalogue-search").fill("no such thing")
        assert page.get_by_role("heading", name="No matches").is_visible()
        page.get_by_role("button", name="Reset", exact=True).click()
        page.wait_for_function("document.querySelectorAll('#catalogue-results tbody tr').length===4")
        results["interactions"].append("Catalogue filtering, selected-record identity, no matches and reset")

        visit("profile")
        page.locator("#tab-summary").focus()
        page.keyboard.press("ArrowRight")
        assert page.locator("#tab-relations").get_attribute("aria-selected") == "true"
        assert page.locator("#panel-relations").is_visible()
        page.keyboard.press("End")
        assert page.locator("#panel-promises").is_visible()
        page.locator('[data-profile-section="composition"]').click()
        assert page.locator("#panel-summary").is_visible()
        assert page.locator("#composition").is_visible()
        boxes = page.locator("#mockup .o-reading").evaluate("el=>[...el.children].map(c=>({left:c.getBoundingClientRect().left,width:c.getBoundingClientRect().width}))")
        assert boxes[0]["width"] > boxes[1]["width"] * 2 and boxes[0]["left"] < boxes[1]["left"]
        results["interactions"].append("Profile keyboard tabs, supporting contents and central reading space")
        page.screenshot(path=str(artifacts / "profile-dark-desktop.png"), full_page=True)

        visit("flow")
        page.locator('[data-step="1"]').focus()
        page.keyboard.press("Enter")
        assert "Applicable provision conditions" in page.locator("#step-detail").inner_text()
        page.locator(".oc-disclosure summary").click()
        assert page.locator(".oc-disclosure ol").is_visible()
        results["interactions"].append("Flow keyboard selection and text equivalent")

        visit("form")
        page.locator("#record-purpose").fill("Retain this explanation")
        page.get_by_role("button", name="Review example").click()
        assert page.locator("#name-error").is_visible()
        assert page.locator("#record-purpose").input_value() == "Retain this explanation"
        assert page.locator("#record-name").evaluate("el=>document.activeElement===el")
        payload = '<img src=x onerror="window.badInput=true">'
        page.locator("#record-name").fill(payload)
        page.get_by_role("button", name="Review example").click()
        assert page.get_by_role("dialog").is_visible()
        assert payload in page.locator("#review-data").inner_text()
        assert page.locator("#review-data img").count() == 0
        page.keyboard.press("Escape")
        assert not page.get_by_role("dialog").is_visible()
        assert page.get_by_role("button", name="Review example").evaluate("el=>document.activeElement===el")
        page.get_by_role("button", name="Review example").click()
        page.get_by_role("button", name="Confirm example").click()
        expect(page.locator("#form-status")).to_contain_text("No record was saved")
        # Closing a subsequent dialog must not reuse the previous confirm returnValue.
        page.get_by_role("button", name="Review example").click()
        page.keyboard.press("Escape")
        expect(page.locator("#form-status")).to_have_text("")
        results["interactions"].append("Form error recovery, retained input, escaped preview, confirm, Escape and focus return")

        visit("comparison")
        page.locator("#compare-aspect").select_option("knowledge")
        assert "Needs clarification" in page.locator("#comparison-result").inner_text()
        visit("activity")
        page.locator("#activity-filter").select_option("relationship")
        assert page.locator("#events li").count() == 1
        results["interactions"].append("Comparison aspect and activity type selection")

        page.goto(f"{base}/index.html?lang=en&theme=light")
        page.locator("#guide-search").fill("typography")
        assert page.locator("#search-results a").count() >= 1
        page.keyboard.press("ArrowDown")
        assert page.locator("#search-results a").first.evaluate("el=>el===document.activeElement")
        expected_path = urlparse(page.locator("#search-results a").first.get_attribute("href")).path
        page.keyboard.press("Enter")
        assert urlparse(page.url).path == expected_path
        page.locator("#language").select_option("ru")
        page.wait_for_url("**lang=ru**")
        assert page.locator("html").get_attribute("lang") == "ru"
        page.locator("#theme").click()
        assert page.locator("html").get_attribute("data-theme") == "dark"
        page.set_viewport_size({"width": 320, "height": 900})
        assert not page.locator(".o-nav details").evaluate("el=>el.open")
        page.locator(".o-nav summary").click()
        assert page.locator(".o-nav nav a").first.is_visible()
        results["interactions"].append("Global search, language/theme and collapsed mobile navigation")
        page.screenshot(path=str(artifacts / "guide-dark-mobile.png"), full_page=True)

        page.set_viewport_size({"width": 1440, "height": 1000})
        page.goto(f"{base}/assets.html?theme=light&lang=en")
        page.locator("#asset-search").fill("ui-search")
        assert page.locator("[data-asset]:visible").count() == 1
        with page.expect_download() as download:
            page.get_by_role("link", name="Download SVG", exact=True).filter(visible=True).click()
        assert download.value.suggested_filename == "ui-search.svg"
        with page.expect_download() as download:
            page.get_by_role("link", name="Download implementation kit", exact=True).click()
        assert download.value.suggested_filename == "o-uiux-kit.zip"
        results["interactions"].append("Asset search, original asset download and implementation kit download")
        page.goto(f"{base}/patterns.html?theme=light&lang=en")
        page.screenshot(path=str(artifacts / "patterns-light-desktop.png"), full_page=True)
        assert not errors, errors
        browser.close()
    (artifacts / "verification.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(results, indent=2, ensure_ascii=False))
    assert not results["failures"], "See verification.json for layout/accessibility failures"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True)
    parser.add_argument("--artifacts", type=Path, required=True)
    args = parser.parse_args()
    verify(args.url.rstrip("/"), args.artifacts)
