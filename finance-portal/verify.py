#!/usr/bin/env python3
"""Check preserved finance content and all generated routes in Chromium."""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re

from build import localize_breadcrumb

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "html-alt/financial-services"
OUTPUT = ROOT / "html/financial-services"
BASE = "http://127.0.0.1:8906/"


class Tags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.counts: Counter[str] = Counter()
        self.links: list[str] = []
        self.anchors: list[dict[str, str | None]] = []
        self.ids: set[str] = set()
        self.id_counts: Counter[str] = Counter()
        self.references: list[tuple[str, str]] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.counts[tag] += 1
        for klass in (a.get("class") or "").split():
            self.counts["." + klass] += 1
        if a.get("id"):
            self.ids.add(a["id"])
            self.id_counts[a["id"]] += 1
        for name in ("aria-controls", "aria-labelledby", "for"):
            for reference in (a.get(name) or "").split():
                self.references.append((name, reference))
        if tag in {"a", "link", "img", "script"}:
            uri = a.get("href") or a.get("src")
            if uri:
                self.links.append(uri)
        if tag == "a":
            self.anchors.append(a)


def parse(page: Path) -> Tags:
    result = Tags()
    result.feed(page.read_text())
    return result


def local_target(page: Path, uri: str) -> tuple[Path | None, str]:
    url = urlsplit(uri)
    if url.scheme or url.netloc or uri.startswith(("mailto:", "tel:", "javascript:")):
        return None, ""
    if not url.path:
        return page, unquote(url.fragment)
    root = OUTPUT if url.path.startswith("/") else page.parent
    target = (root / unquote(url.path.lstrip("/"))).resolve()
    if target.is_dir() or url.path.endswith("/"):
        target /= "index.html"
    return target, unquote(url.fragment)


def static_audit() -> dict:
    source_pages = {p.relative_to(SOURCE) for p in SOURCE.rglob("*.html")}
    built_pages = {p.relative_to(OUTPUT) for p in OUTPUT.rglob("*.html")} - {Path("index.html")}
    errors: list[str] = []
    if source_pages != built_pages:
        errors.append(f"Route set changed: removed={source_pages-built_pages}, added={built_pages-source_pages}")
    all_ids = {p: parse(p).ids for p in OUTPUT.rglob("*.html")}
    counts = Counter()
    for relative in sorted(source_pages & built_pages):
        source_text, built_text = (SOURCE / relative).read_text(), (OUTPUT / relative).read_text()
        marker = '<div class="page">'
        label = "Financial Services" if relative.parts[0] == "en" else "Финансовые услуги"
        expected_content = localize_breadcrumb(source_text, OUTPUT / relative, relative.parts[0]) if marker in source_text else ""
        expected_content = expected_content[expected_content.index(marker):].replace('>service.eyebrow<', f'>{label}<') if expected_content else ""
        if relative == Path("ru/index.html"):
            expected_content = expected_content.replace('>Financial Services</span>', f'>{label}</span>', 1)
        if marker not in source_text or marker not in built_text or \
           expected_content != built_text[built_text.index(marker):]:
            errors.append(f"Page content changed: {relative}")
        if relative.parts[0] == "ru" and len(relative.parts) == 4:
            section = relative.parts[1]
            parent_text = (OUTPUT / "ru" / section / "index.html").read_text()
            title = re.search(r'<span class="breadcrumb__current" aria-current="page">([^<]+)</span>', parent_text)
            parent_link = re.search(r'<a class="breadcrumb__link" href="../index.html">([^<]+)</a>', built_text)
            if not title or not parent_link or parent_link.group(1) != title.group(1):
                errors.append(f"Russian parent breadcrumb differs from section title: {relative}")
        source, built = parse(SOURCE / relative), parse(OUTPUT / relative)
        for selector in (".card", ".scenario-card", ".flow-detail", ".flow-stages__stage", ".problems-tab-input", ".problems-panel", ".l3-section", "details", "h1", "h2", "h3"):
            if source.counts[selector] != built.counts[selector]:
                errors.append(f"{relative}: {selector} {source.counts[selector]} -> {built.counts[selector]}")
        if built.counts[".finance-shell-header"] != 1:
            errors.append(f"{relative}: missing or repeated shell header")
        for name, count in built.id_counts.items():
            if count > 1:
                errors.append(f"{relative}: duplicate id {name} ({count})")
        for name, reference in built.references:
            if reference not in built.ids:
                errors.append(f"{relative}: {name} references missing id {reference}")
        for uri in built.links:
            target, fragment = local_target(OUTPUT / relative, uri)
            if target is None:
                continue
            if not target.is_file():
                errors.append(f"{relative}: missing {uri}")
            elif fragment and target.suffix == ".html" and fragment not in all_ids.get(target, set()):
                errors.append(f"{relative}: missing fragment {uri}")
        for anchor in built.anchors:
            uri = anchor.get("href") or ""
            target, _ = local_target(OUTPUT / relative, uri)
            if target is None or target.suffix != ".html":
                continue
            try:
                destination_lang = target.relative_to(OUTPUT).parts[0]
            except ValueError:
                continue
            if destination_lang in {"en", "ru"} and destination_lang != relative.parts[0] and anchor.get("hreflang") != destination_lang:
                errors.append(f"{relative}: unmarked language change in {uri}")
        counts["links"] += len(built.links)
        counts["details"] += built.counts["details"]
        counts["flow_stages"] += built.counts[".flow-stages__stage"]
        counts["cards"] += built.counts[".card"]
    return {"pages": len(source_pages), "counts": dict(counts), "errors": errors}


def browser_audit() -> dict:
    paths = sorted(p.relative_to(OUTPUT).as_posix() for p in OUTPUT.rglob("*.html") if p.name == "index.html" and p.parent != OUTPUT)
    errors: list[str] = []
    checks = Counter()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.on("pageerror", lambda e: errors.append(f"JS error on {page.url}: {e}"))
        page.on("requestfailed", lambda r: errors.append(f"Request failed on {page.url}: {r.url}: {r.failure}"))
        for path in paths:
            response = page.goto(BASE + path, wait_until="load", timeout=30000)
            checks["desktop_pages"] += 1
            if not response or response.status != 200:
                errors.append(f"HTTP {response.status if response else 'none'}: {path}")
                continue
            state = page.evaluate("""() => ({
                width: document.documentElement.scrollWidth,
                client: innerWidth,
                h1: document.querySelectorAll('h1').length,
                header: document.querySelectorAll('.finance-shell-header').length,
                main: document.querySelectorAll('#main-content').length,
                links: [...document.querySelectorAll('.finance-shell-links a')].map(a => a.href),
                details: document.querySelectorAll('details').length,
                radio: document.querySelectorAll('.problems-tab-input').length,
                stages: document.querySelectorAll('.flow-stages__stage').length
            })""")
            if state["width"] > state["client"] + 1:
                errors.append(f"Desktop overflow {path}: {state['width']} > {state['client']}")
            if (state["h1"], state["header"], state["main"]) != (1, 1, 1):
                errors.append(f"Missing landmarks {path}: {state}")
            if len(state["links"]) != 2:
                errors.append(f"Missing shell links {path}")
            if state["details"]:
                detail = page.locator("details").first
                detail.locator("summary").first.click(timeout=5000)
                if not detail.evaluate("el => el.open"):
                    errors.append(f"Disclosure did not open: {path}")
                checks["disclosures_opened"] += 1
            if state["radio"]:
                first = page.locator(".problems-tab-input").first
                first.check(force=True)
                if not first.is_checked():
                    errors.append(f"Tab did not select: {path}")
                checks["tabs_selected"] += 1
            if state["stages"]:
                stage = page.locator(".flow-stages__stage").first
                stage.click(timeout=5000)
                if not page.locator("#stageModal").evaluate("el => el.classList.contains('is-open')"):
                    errors.append(f"Stage modal did not open: {path}")
                page.keyboard.press("Escape")
                if page.locator("#stageModal").evaluate("el => el.classList.contains('is-open')"):
                    errors.append(f"Stage modal did not close: {path}")
                checks["modals_opened_closed"] += 1
            route = Path(path).parts
            if len(route) == 4 and route[0] == "ru":
                page.locator('.breadcrumb a[href="../index.html"]').click(timeout=5000)
                expected = BASE + f"ru/{route[1]}/index.html"
                if page.url != expected:
                    errors.append(f"Russian parent navigation left its section: {path} -> {page.url}")
                checks["russian_parent_links_clicked"] += 1
        for width in (390, 320):
            page.set_viewport_size({"width": width, "height": 850})
            for path in paths:
                response = page.goto(BASE + path, wait_until="load", timeout=30000)
                checks[f"mobile_{width}_pages"] += 1
                if not response or response.status != 200:
                    errors.append(f"HTTP mobile {width}: {path}")
                    continue
                actual = page.evaluate("document.documentElement.scrollWidth")
                if actual > width + 1:
                    errors.append(f"Mobile overflow {width} {path}: {actual}")
        browser.close()
    return {"checks": dict(checks), "errors": errors}


if __name__ == "__main__":
    report = {"static": static_audit(), "browser": browser_audit()}
    destination = Path(__file__).resolve().parent / "verification/report.json"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"static": {"pages": report["static"]["pages"], "counts": report["static"]["counts"], "error_count": len(report["static"]["errors"])}, "browser": {"checks": report["browser"]["checks"], "error_count": len(report["browser"]["errors"])}}, indent=2))
    for kind in ("static", "browser"):
        for error in report[kind]["errors"][:20]:
            print(kind, error)
    raise SystemExit(bool(report["static"]["errors"] or report["browser"]["errors"]))
