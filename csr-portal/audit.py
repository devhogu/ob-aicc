#!/usr/bin/env python3
"""Exercise every retained CSR document link and diagram in headless Chromium."""
from __future__ import annotations

import json
from pathlib import Path
import re

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "portfolio"
ARTIFACTS = ROOT / "csr-portal/verification"
BASE = "http://127.0.0.1:8905"


def audit() -> dict:
    report = {"documents": 0, "source_anchor_links": 0, "unique_anchor_targets": 0,
              "desktop_navigation_clicks": 0, "mobile_navigation_clicks": 0,
              "diagram_open_close_cycles": 0, "mobile_diagram_cycles": 0, "failures": []}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("response", lambda response: errors.append(f"HTTP {response.status}: {response.url}") if response.status >= 400 else None)
        for lang in ("ru", "en"):
            source = (SOURCE / lang / "projects/service-resolution/workbook.html").read_text()
            source_hrefs = re.findall(r'<a\b[^>]*href="#([^"]+)"', source)
            page.set_viewport_size({"width": 1440, "height": 900})
            page.goto(f"{BASE}/{lang}/index.html")
            page.evaluate("document.fonts.ready")
            report["source_anchor_links"] += len(source_hrefs)
            report["unique_anchor_targets"] += len(set(source_hrefs))

            # The original proposal is the independent content and link oracle.
            preserved = page.evaluate("""source => {
              const original = new DOMParser().parseFromString(source, 'text/html');
              const clean = text => text.replace(/\\s+/g, ' ').trim();
              const failures = [];
              const sections = [...original.querySelectorAll('section[data-document]')];
              for (const oldSection of sections) {
                const current = document.querySelector('section[data-document="' + oldSection.dataset.document + '"]');
                if (!current) { failures.push('Missing document ' + oldSection.dataset.document); continue; }
                const copy = current.cloneNode(true);
                copy.querySelector('.csr-case-map')?.remove();
                if (clean(oldSection.textContent) !== clean(copy.textContent))
                  failures.push('Changed document wording ' + oldSection.dataset.document);
                if (oldSection.querySelectorAll('figure.diagram').length !== current.querySelectorAll('figure.diagram').length)
                  failures.push('Changed diagrams ' + oldSection.dataset.document);
              }
              return {documents: sections.length, failures};
            }""", source)
            report["documents"] += preserved["documents"]
            report["failures"].extend(f"{lang}: {item}" for item in preserved["failures"])

            missing = page.evaluate("""hrefs => [...new Set(hrefs)].filter(id => !document.getElementById(id))""", source_hrefs)
            report["failures"].extend(f"{lang}: broken source anchor #{item}" for item in missing)
            hash_map = page.evaluate("JSON.parse(document.getElementById('csr-hash-map').textContent)")
            unmapped = [item for item in set(source_hrefs) if item not in hash_map and item != f"{lang}-start"]
            report["failures"].extend(f"{lang}: no corresponding-language target for #{item}" for item in unmapped)
            bad_mappings = page.evaluate("""mapping => Object.entries(mapping).filter(([source,target]) =>
              !document.getElementById(source) || !target).map(([source]) => source)""", hash_map)
            report["failures"].extend(f"{lang}: bad language mapping #{item}" for item in bad_mappings)

            # Physically click every document/section link in the retained left navigation.
            nav_count = page.locator(".nav-scroll a[href^='#']").count()
            for index in range(nav_count):
                link = page.locator(".nav-scroll a[href^='#']").nth(index)
                href = link.get_attribute("href")
                link.evaluate("e=>{const doc=e.closest('.nav-doc');const group=e.closest('.nav-group');if(doc)doc.open=true;if(group)group.open=true}")
                try:
                    link.click(timeout=4000)
                    page.wait_for_timeout(20)
                    state = page.evaluate("""id => {
                      const target=document.getElementById(id);
                      const section=target?.closest('[data-document]');
                      return {hash:decodeURIComponent(location.hash.slice(1)), top:target?.getBoundingClientRect().top,
                        header:document.querySelector('.csr-header').getBoundingClientRect().bottom,
                        active:document.querySelector('.nav-overview.active')?.dataset.docLink,
                        document:section?.dataset.document};
                    }""", href[1:])
                    if state["hash"] != href[1:] or state["top"] is None or state["top"] < state["header"] - 2:
                        report["failures"].append({"lang": lang, "link": href, "desktop": state})
                    if state["document"] and state["active"] != state["document"]:
                        report["failures"].append({"lang": lang, "link": href, "active_navigation": state})
                    report["desktop_navigation_clicks"] += 1
                except Exception as error:
                    report["failures"].append(f"{lang}: desktop click {href}: {error}")

            # Each embedded SVG must survive the viewer's move/restore cycle.
            diagrams = page.locator("figure.diagram")
            for index in range(diagrams.count()):
                figure = diagrams.nth(index)
                svg_id = figure.locator("svg").get_attribute("id")
                try:
                    figure.evaluate("e=>e.focus({preventScroll:true})")
                    page.keyboard.press("Enter")
                    opened = page.evaluate("""id => {
                      const viewer=document.getElementById('diagram-viewer');
                      const svg=document.querySelector('#diagram-stage svg');
                      return {visible:!viewer.hidden, id:svg?.id, width:svg?.getBoundingClientRect().width,
                        title:document.getElementById('diagram-viewer-title').textContent.trim()};
                    }""", svg_id)
                    if not opened["visible"] or opened["id"] != svg_id or not opened["width"] or not opened["title"]:
                        report["failures"].append({"lang": lang, "diagram": index, "open": opened})
                    page.keyboard.press("Escape")
                    closed = figure.evaluate("e=>({restored:!!e.querySelector('svg'),focus:document.activeElement===e,expanded:e.getAttribute('aria-expanded')})")
                    if not closed["restored"] or not closed["focus"] or closed["expanded"] != "false":
                        report["failures"].append({"lang": lang, "diagram": index, "close": closed})
                    report["diagram_open_close_cycles"] += 1
                except Exception as error:
                    report["failures"].append(f"{lang}: diagram {index}: {error}")
                    page.reload()

            # The collapsed mobile rail must still reach every document overview.
            page.set_viewport_size({"width": 390, "height": 850})
            page.goto(f"{BASE}/{lang}/index.html")
            overview_count = page.locator(".nav-overview[data-doc-link]").count()
            for index in range(overview_count):
                link = page.locator(".nav-overview[data-doc-link]").nth(index)
                href = link.get_attribute("href")
                page.locator("#menu-button").click()
                link.evaluate("e=>{const doc=e.closest('.nav-doc');const group=e.closest('.nav-group');if(doc)doc.open=true;if(group)group.open=true}")
                try:
                    link.click(timeout=4000)
                    page.wait_for_timeout(20)
                    state = page.evaluate("""id => ({hash:decodeURIComponent(location.hash.slice(1)),
                      top:document.getElementById(id)?.getBoundingClientRect().top,
                      header:document.querySelector('.csr-header').getBoundingClientRect().bottom,
                      menu:document.getElementById('menu-button').getAttribute('aria-expanded'),
                      active:document.querySelector('.nav-overview.active')?.dataset.docLink})""", href[1:])
                    if state["hash"] != href[1:] or state["top"] is None or state["top"] < state["header"] - 2 or state["menu"] != "false" or state["active"] != href[1:]:
                        report["failures"].append({"lang": lang, "link": href, "mobile": state})
                    report["mobile_navigation_clicks"] += 1
                except Exception as error:
                    report["failures"].append(f"{lang}: mobile click {href}: {error}")
            for index in range(page.locator("figure.diagram").count()):
                figure = page.locator("figure.diagram").nth(index)
                svg_id = figure.locator("svg").get_attribute("id")
                try:
                    figure.evaluate("e=>e.focus({preventScroll:true})")
                    page.keyboard.press("Enter")
                    state = page.evaluate("""() => {
                      const close=document.getElementById('diagram-close').getBoundingClientRect();
                      return {open:!document.getElementById('diagram-viewer').hidden,
                        svg:document.querySelector('#diagram-stage svg')?.id,
                        closeVisible:close.left>=0 && close.right<=innerWidth,
                        overflow:document.documentElement.scrollWidth>innerWidth+1};
                    }""")
                    if not state["open"] or state["svg"] != svg_id or not state["closeVisible"] or state["overflow"]:
                        report["failures"].append({"lang": lang, "diagram": index, "mobile_open": state})
                    page.keyboard.press("Escape")
                    if not figure.evaluate("e=>!!e.querySelector('svg') && document.activeElement===e"):
                        report["failures"].append({"lang": lang, "diagram": index, "mobile_close": "not restored"})
                    report["mobile_diagram_cycles"] += 1
                except Exception as error:
                    report["failures"].append(f"{lang}: mobile diagram {index}: {error}")
                    page.reload()
            page.set_viewport_size({"width": 1440, "height": 900})
            other = "en" if lang == "ru" else "ru"
            page.goto(f"{BASE}/{other}/index.html")
            missing_translations = page.evaluate("""mapping => Object.values(mapping).filter(id => !document.getElementById(id))""", hash_map)
            report["failures"].extend(f"{lang}: missing corresponding-language anchor #{item}" for item in missing_translations)
        browser.close()
        report["failures"].extend(errors)
    ARTIFACTS.mkdir(exist_ok=True)
    (ARTIFACTS / "audit.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    return report


if __name__ == "__main__":
    result = audit()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(1 if result["failures"] else 0)
