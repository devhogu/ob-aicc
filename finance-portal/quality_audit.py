#!/usr/bin/env python3
"""Exhaustive rendered-layout and control audit for the finance trial."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import json
import sys

from playwright.sync_api import sync_playwright

import verify

BASE = "http://127.0.0.1:8906/"
OUTPUT = Path(__file__).resolve().parent.parent / "html/financial-services"
PATHS = sorted(p.relative_to(OUTPUT).as_posix() for p in OUTPUT.rglob("index.html") if p.parent != OUTPUT)
REPORT = Path(__file__).resolve().parent / "verification/quality-report.json"
WIDTHS = (1440, 1024, 768, 600, 390, 320)

MEASURE = """() => {
  const visible = e => !!e.getClientRects().length;
  const clipped = [...document.querySelectorAll('*')].filter(e => {
    if (!visible(e) || !e.clientWidth) return false;
    const s = getComputedStyle(e);
    return ['hidden', 'clip'].includes(s.overflowX) && e.scrollWidth > e.clientWidth + 3;
  }).map(e => ({tag:e.tagName, cls:String(e.className).slice(0,70),
                have:e.clientWidth, need:e.scrollWidth, text:e.textContent.trim().slice(0,70)}));
  const scrollable = [...document.querySelectorAll('*')].filter(e => {
    if (!visible(e) || !e.clientWidth) return false;
    const s = getComputedStyle(e);
    return ['auto', 'scroll'].includes(s.overflowX) && e.scrollWidth > e.clientWidth + 3;
  }).map(e => ({tag:e.tagName, cls:String(e.className).slice(0,70),
                have:e.clientWidth, need:e.scrollWidth}));
  const siblings = new Map(), overlap = [];
  for (const e of document.querySelectorAll('.card, .scenario-card, .flow-detail')) {
    if (!visible(e)) continue;
    if (!siblings.has(e.parentElement)) siblings.set(e.parentElement, []);
    siblings.get(e.parentElement).push(e);
  }
  for (const group of siblings.values()) for (let i=0;i<group.length;i++)
    for (let j=i+1;j<group.length;j++) {
      const a=group[i].getBoundingClientRect(), b=group[j].getBoundingClientRect();
      if (Math.min(a.right,b.right)-Math.max(a.left,b.left)>2 &&
          Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>2)
        overlap.push([group[i].className,group[j].className]);
    }
  return {
    viewport:innerWidth, document:document.documentElement.scrollWidth,
    h1:document.querySelectorAll('h1').length, main:document.querySelectorAll('#main-content').length,
    header:document.querySelectorAll('.finance-shell-header').length,
    font:getComputedStyle(document.body).fontFamily,
    images:[...document.images].filter(e=>!e.complete || !e.naturalWidth).map(e=>e.src),
    clipped, scrollable, overlap,
    cls:window.__cls || 0
  };
}"""

HIT_TEST = """() => {
  const errors=[]; let checked=0, hidden=0;
  for (const a of document.querySelectorAll('a[href]')) {
    if (a.classList.contains('skip-link')) continue;
    if (!a.textContent.trim() && !a.getAttribute('aria-label') &&
        !a.getAttribute('title') && !a.querySelector('img[alt]:not([alt=""])'))
      errors.push({href:a.getAttribute('href'), kind:'unnamed'});
    if (!a.getClientRects().length) { hidden++; errors.push({href:a.getAttribute('href'), kind:'hidden'}); continue; }
    a.scrollIntoView({block:'center',inline:'nearest'});
    const boxes=[...a.getClientRects()]; let reachable=false;
    for (const b of boxes) {
      const points=[[.5,.5],[.12,.12],[.88,.12],[.12,.88],[.88,.88]];
      for (const [fx,fy] of points) {
        const x=b.left+b.width*fx, y=b.top+b.height*fy;
        if(x<0||x>=innerWidth||y<0||y>=innerHeight)continue;
        const hit=document.elementFromPoint(x,y);
        if(hit && (hit===a || hit.closest('a')===a)) { reachable=true; break; }
      }
      if(reachable)break;
    }
    checked++;
    if(!reachable)errors.push({href:a.getAttribute('href'), kind:'obscured',
                               cls:String(a.className), text:a.textContent.trim().slice(0,60)});
  }
  return {checked,hidden,errors};
}"""


def geometry() -> dict:
    errors = []
    counts = Counter()
    high_cls = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        for width in WIDTHS:
            page = browser.new_page(viewport={"width": width, "height": 900})
            page.add_init_script("""window.__cls=0;
              new PerformanceObserver(list=>{for(const e of list.getEntries())
                if(!e.hadRecentInput) window.__cls+=e.value})
              .observe({type:'layout-shift',buffered:true});""")
            page.on("pageerror", lambda e: errors.append(f"JavaScript: {page.url}: {e}"))
            page.on("requestfailed", lambda r: errors.append(f"Request: {page.url}: {r.url}: {r.failure}"))
            page.on("response", lambda r: errors.append(f"HTTP {r.status}: {r.url}") if r.status >= 400 else None)
            for path in PATHS:
                response = page.goto(BASE + path, wait_until="load", timeout=30000)
                counts["page_width_loads"] += 1
                if not response or response.status != 200:
                    errors.append(f"Page failed: {width} {path}")
                    continue
                page.evaluate("document.fonts.ready")
                state = page.evaluate(MEASURE)
                if state["document"] > width + 1:
                    errors.append(f"Document overflow {width} {path}: {state['document']}")
                if (state["h1"], state["main"], state["header"]) != (1, 1, 1):
                    errors.append(f"Missing landmarks {width} {path}")
                for key in ("images", "clipped", "overlap"):
                    for issue in state[key]:
                        errors.append(f"{key} {width} {path}: {issue}")
                counts["intentional_scroll_containers"] += len(state["scrollable"])
                if state["cls"] > .1:
                    high_cls.append([width, path, round(state["cls"], 4)])
                if width in (1440, 390):
                    page.evaluate("document.querySelectorAll('details').forEach(e=>e.open=true)")
                    page.evaluate("document.fonts.ready")
                    expanded = page.evaluate(MEASURE)
                    counts["expanded_layouts"] += 1
                    if expanded["document"] > width + 1:
                        errors.append(f"Expanded overflow {width} {path}: {expanded['document']}")
                    for key in ("images", "clipped", "overlap"):
                        for issue in expanded[key]:
                            errors.append(f"Expanded {key} {width} {path}: {issue}")
                    hit = page.evaluate(HIT_TEST)
                    counts["links_hit_tested"] += hit["checked"]
                    for issue in hit["errors"]:
                        errors.append(f"Link {width} {path}: {issue}")
            page.close()
        browser.close()
    return {"counts": dict(counts), "high_cls": high_cls, "errors": errors}


def interactions() -> dict:
    errors = []
    counts = Counter()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.on("pageerror", lambda e: errors.append(f"JavaScript: {page.url}: {e}"))
        for path in PATHS:
            page.goto(BASE + path, wait_until="load")
            page.evaluate("document.fonts.ready")
            detail = page.evaluate("""() => {
              let tested=0,failed=0;
              for(const e of document.querySelectorAll('details')) {
                const s=e.querySelector(':scope > summary');
                if(!s) { failed++; continue; }
                const before=e.open; s.click();
                if(e.open===before) failed++;
                s.click(); if(e.open!==before) failed++;
                tested++;
              }
              return {tested,failed};
            }""")
            counts["disclosures_toggled"] += detail["tested"]
            if detail["failed"]:
                errors.append(f"Disclosure toggle {path}: {detail['failed']} failed")
            tabs = page.locator(".problems-tab-label")
            for index in range(tabs.count()):
                label = tabs.nth(index)
                target = label.get_attribute("for")
                label.click(timeout=5000)
                state = page.evaluate("""id => {
                  const input=document.getElementById(id);
                  const panel=document.getElementById(id.replace('problems-tab-', 'problems-panel-'));
                  return [!!input?.checked, !!panel && getComputedStyle(panel).display !== 'none'];
                }""", target)
                counts["tabs_clicked"] += 1
                if state != [True, True]:
                    errors.append(f"Tab {path} {target}: {state}")
            stages = page.locator(".flow-stages__stage")
            if stages.count():
                page.evaluate("document.querySelectorAll('details').forEach(e=>e.open=true)")
            for index in range(stages.count()):
                button = stages.nth(index)
                slug = button.get_attribute("data-stage")
                try:
                    button.click(timeout=5000)
                    state = page.evaluate("""() => {
                      const modal=document.getElementById('stageModal');
                      return [modal?.classList.contains('is-open'),
                              modal?.getAttribute('aria-hidden'),
                              !!modal?.querySelector('.modal__title')?.textContent.trim(),
                              document.activeElement === modal?.querySelector('.modal__close'),
                              modal?.getAttribute('aria-labelledby') === 'stage-modal-title'];
                    }""")
                    counts["stages_clicked"] += 1
                    if state != [True, "false", True, True, True]:
                        errors.append(f"Stage {path} {slug}: {state}")
                    page.keyboard.press("Tab")
                    if not page.locator(".modal__close").evaluate("el => document.activeElement === el"):
                        errors.append(f"Focus escaped modal {path} {slug}")
                    page.keyboard.press("Escape")
                    if page.locator("#stageModal").get_attribute("aria-hidden") != "true":
                        errors.append(f"Stage modal remained open {path} {slug}")
                    if not button.evaluate("el => document.activeElement === el"):
                        errors.append(f"Focus not restored {path} {slug}")
                except Exception as exc:
                    errors.append(f"Stage click {path} {slug}: {str(exc)[:180]}")
        browser.close()
    return {"counts": dict(counts), "errors": errors}


def click_links() -> dict:
    """Activate every anchor in its source page and verify the browser lands there."""
    errors = []
    counts = Counter()

    def same_destination(actual: str, expected: str) -> bool:
        a, e = urlsplit(actual), urlsplit(expected)
        return (a.scheme, a.netloc, unquote(a.path), unquote(a.fragment)) == \
               (e.scheme, e.netloc, unquote(e.path), unquote(e.fragment))

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        for width in (1440, 390):
            page = browser.new_page(viewport={"width": width, "height": 900})
            for path in PATHS:
                source = BASE + path
                page.goto(source, wait_until="load")
                anchors = page.locator("a[href]")
                links = anchors.evaluate_all("els => els.map(e => [e.getAttribute('href'), e.className])")
                anchors.evaluate_all("els => els.forEach(e => e.target='_blank')")
                for index, (href, klass) in enumerate(links):
                    anchor = page.locator("a[href]").nth(index)
                    anchor.evaluate("""el => {
                      let parent=el.parentElement;
                      while(parent) { if(parent.tagName==='DETAILS')parent.open=true; parent=parent.parentElement; }
                    }""")
                    if "skip-link" in klass:
                        anchor.focus()
                    options = {"timeout": 5000}
                    if "card__click-target" in klass:
                        options["position"] = {"x": 12, "y": 12}
                    popup = None
                    try:
                        with page.expect_popup(timeout=5000) as opened:
                            anchor.click(**options)
                        popup = opened.value
                        popup.wait_for_load_state("domcontentloaded")
                        counts["anchors_clicked"] += 1
                        expected = urljoin(source, href)
                        if not same_destination(popup.url, expected):
                            errors.append(f"Wrong destination {width} {path} [{index}] {href}: {popup.url}")
                        if urlsplit(expected).fragment:
                            popup.wait_for_function("""() => {
                              const e=document.getElementById(decodeURIComponent(location.hash.slice(1)));
                              const header=document.querySelector('.finance-shell-header');
                              if(!e || !header || !e.getClientRects().length)return false;
                              const r=e.getBoundingClientRect(), h=header.getBoundingClientRect();
                              return r.bottom > h.bottom && r.top < innerHeight;
                            }""", timeout=1500)
                            target = popup.evaluate("""() => {
                              const id=decodeURIComponent(location.hash.slice(1));
                              const e=document.getElementById(id);
                              if(!e)return {found:false};
                              const r=e.getBoundingClientRect();
                              const header=document.querySelector('.finance-shell-header').getBoundingClientRect();
                              return {found:true, visible:!!e.getClientRects().length,
                                      top:r.top, bottom:r.bottom, header:header.bottom};
                            }""")
                            counts["fragments_opened"] += 1
                            if not target["found"] or not target.get("visible") or \
                               target["bottom"] <= target["header"] or target["top"] >= 900:
                                errors.append(f"Fragment hidden {width} {path} [{index}] {href}: {target}")
                    except Exception as exc:
                        errors.append(f"Click failed {width} {path} [{index}] {href} ({klass}): {str(exc)[:180]}")
                    finally:
                        if popup and not popup.is_closed():
                            popup.close()
                        if "skip-link" in klass:
                            page.evaluate("document.activeElement.blur()")
                if counts["anchors_clicked"] % 100 < len(links):
                    print(f"Link clicks: {counts['anchors_clicked']} / {1806 * 2}", flush=True)
            page.close()
        browser.close()
    return {"counts": dict(counts), "errors": errors}


def modal_layout() -> dict:
    errors = []
    counts = Counter()
    flow_paths = [path for path in PATHS if '.flow-stages__stage' in
                  (OUTPUT / path).read_text()]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        for width in (1440, 390, 320):
            page = browser.new_page(viewport={"width": width, "height": 850})
            for path in flow_paths:
                page.goto(BASE + path, wait_until="load")
                page.evaluate("document.querySelectorAll('details').forEach(e=>e.open=true)")
                stages = page.locator(".flow-stages__stage")
                for index in range(stages.count()):
                    stage = stages.nth(index)
                    stage.click(timeout=5000)
                    state = page.evaluate("""() => {
                      const panel=document.querySelector('.modal__panel');
                      const r=panel.getBoundingClientRect();
                      return {left:r.left,right:r.right,top:r.top,bottom:r.bottom,
                        have:panel.clientWidth,need:panel.scrollWidth,
                        height:panel.clientHeight,contentHeight:panel.scrollHeight,
                        overflow:getComputedStyle(panel).overflowY,
                        doc:document.documentElement.scrollWidth,
                        focus:document.activeElement===panel.querySelector('.modal__close')};
                    }""")
                    counts["modal_layouts"] += 1
                    if state["left"] < -1 or state["right"] > width+1 or \
                       state["top"] < -1 or state["bottom"] > 851 or \
                       state["need"] > state["have"]+3 or state["doc"] > width+1 or \
                       not state["focus"] or \
                       (state["contentHeight"] > state["height"]+3 and state["overflow"] not in ("auto", "scroll")):
                        errors.append(f"Modal fit {width} {path} stage {index}: {state}")
                    page.keyboard.press("Escape")
            page.close()
        browser.close()
    return {"counts": dict(counts), "errors": errors}


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    report = json.loads(REPORT.read_text()) if REPORT.exists() else {}
    if mode in ("geometry", "all"):
        report["geometry"] = geometry()
    if mode in ("interactions", "all"):
        report["interactions"] = interactions()
    if mode in ("links", "all"):
        report["links"] = click_links()
    if mode in ("modals", "all"):
        report["modals"] = modal_layout()
    report["static"] = verify.static_audit()
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({name: {"counts": section.get("counts", {}),
                             "errors": len(section.get("errors", [])),
                             "high_cls": len(section.get("high_cls", []))}
                      for name, section in report.items()}, indent=2))
    for name, section in report.items():
        for error in section.get("errors", [])[:20]:
            print(name, error)
    raise SystemExit(any(section.get("errors") for section in report.values()))
