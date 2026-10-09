#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Open every page of every edition of the built Hub site from the folder (file://) in a browser: it renders without errors at desktop and phone width in light and dark, its layout matches its Russian twin, and the interactions behave the same in each edition.
#   SCOPE: Reads html/aicc/v2; writes only a report under .runtime/hub-v2.
#   DEPENDS: playwright (the repository virtual environment)
#   LINKS: C-HUB-V2, C-HUB-V2-EN, V-M-PORTAL-PROJECTION
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   sweep - every page of an edition at both widths in both themes
#   interact - the interactions of one edition (search, switch, tabs, tiles, chips, maps, theme)
#   check - sweep and interact for every edition, compare page heights between twins
# END_MODULE_MAP
"""Browser check of html/aicc/v2: portal/tools/with-browser-env.sh portal/.venv/bin/python aicc/v2/tools/check_browser.py"""
import asyncio
import json
import os
from pathlib import Path
import sys

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[3]
SITE = Path(os.environ.get('AICC_V2_OUT') or ROOT / 'html' / 'aicc' / 'v2')
sys.path.insert(0, str(ROOT / 'portal' / 'tools'))
from browser_check import browser_env  # noqa: E402  (the shared browser environment of the repository)

REPORT = ROOT / '.runtime' / 'hub-v2'
SEARCH = {'ru': 'воронка', 'en': 'funnel'}  # a vocabulary term each edition must find
VIEWS = ((1440, 'light'), (390, 'light'), (1440, 'dark'), (390, 'dark'))


def editions():
    site = json.loads((ROOT / 'aicc' / 'v2' / 'site.json').read_text(encoding='utf-8'))
    return [lang for lang in site.get('languages', ['ru']) if (SITE / lang).exists()]


async def sweep(browser, lang, heights, problems):
    pages = sorted(p for p in (SITE / lang).rglob('index.html') if 'catalog/assets' not in p.as_posix())
    for width, theme in VIEWS:
        context = await browser.new_context(viewport={'width': width, 'height': 900})
        await context.add_init_script(f"try{{localStorage.setItem('hub-theme','{theme}')}}catch(e){{}}")
        page = await context.new_page()
        seen = []
        page.on('pageerror', lambda e: seen.append('script: ' + str(e)))
        page.on('requestfailed', lambda r: seen.append('failed: ' + r.url))
        page.on('request', lambda r: seen.append('external: ' + r.url) if r.url.startswith(('http:', 'https:')) else None)
        for path in pages:
            seen.clear()
            name = path.relative_to(SITE).as_posix()
            await page.goto(path.as_uri(), wait_until='load')
            if await page.locator('h1').count() != 1:
                problems.append(f'{width} {theme} {name}: h1 count')
            if not await page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'):
                problems.append(f'{width} {theme} {name}: horizontal overflow')
            if await page.locator('.status-chip').count() != 1 or await page.locator('.pagefb').count() != 1:
                problems.append(f'{width} {theme} {name}: chip or feedback button missing')
            if await page.locator('html').get_attribute('data-theme') != theme:
                problems.append(f'{width} {theme} {name}: theme not applied')
            if theme == 'light':
                heights[(width, name.split('/', 1)[1])] = heights.get((width, name.split('/', 1)[1]), {}) | {lang: await page.evaluate('document.documentElement.scrollHeight')}
            problems.extend(f'{width} {theme} {name}: {s}' for s in seen)
        await context.close()
    return len(pages)


async def interact(browser, lang, problems):
    """The behaviour of one edition; every step names the edition in its problem."""
    context = await browser.new_context(viewport={'width': 1440, 'height': 900})
    page = await context.new_page()
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    root = SITE / lang
    # search finds a term and a result leads into the same edition
    await page.goto((root / 'index.html').as_uri())
    await page.locator('#q').fill(SEARCH[lang])
    await page.locator('#results a').first.wait_for()
    await page.locator('#results a').first.click()
    await page.wait_for_load_state('load')
    if f'/{lang}/' not in page.url:
        problems.append(f'{lang}: a search result leads outside the edition: {page.url}')
    # the language switch keeps the page and the part (#anchor in a tabbed guide)
    others = [x for x in editions() if x != lang]
    if others:
        await page.goto((root / 'kb' / 'guides' / 'skills-complete-guide' / 'index.html').as_uri() + '#test')
        await page.locator('[data-lang-switch]').first.click()
        await page.wait_for_load_state('load')
        if f'/{others[0]}/kb/guides/skills-complete-guide/' not in page.url or not page.url.endswith('#test'):
            problems.append(f'{lang}: the language switch did not keep the page and part: {page.url}')
        elif await page.evaluate("(document.querySelector('[data-tab-panel]:not([hidden])')||{}).id") != 'test':
            problems.append(f'{lang}: the language switch did not open the same tab')
    # projects: tabs by hash, tiles fill in place, the filter counts
    await page.goto((root / 'projects' / 'index.html').as_uri() + '#plan')
    if not await page.locator('[data-tab-panel="plan"]').is_visible():
        problems.append(f'{lang}: the plan tab does not open from its address')
    tiles = page.locator('[data-here-it]')
    if await tiles.count() > 1:
        await tiles.nth(1).click()
    select = page.locator('[data-kb-filter]').first
    if await select.count():
        options = await select.locator('option').count()
        if options > 1:
            await select.select_option(index=1)
            if not await page.locator('[data-kb-count]').first.inner_text():
                problems.append(f'{lang}: the filter count is empty')
    # knowledge base: a chip filters the guide grid
    await page.goto((root / 'kb' / 'index.html').as_uri())
    chips = page.locator('.lib-chip')
    if await chips.count() > 2:
        before = await page.locator('[data-lib-item]:not([hidden])').count()
        await chips.nth(2).click()
        after = await page.locator('[data-lib-item]:not([hidden])').count()
        if not 0 < after < before:
            problems.append(f'{lang}: a knowledge base chip does not filter ({before} -> {after})')
    # a learning map: ticking a step moves the progress, and the bar on a guide follows
    await page.goto((root / 'kb' / 'maps' / 'foundations' / 'index.html').as_uri())
    await page.evaluate("localStorage.removeItem('hub-learning')")
    await page.reload()
    await page.locator('.lm-step [data-step-toggle]').first.click()
    progress = await page.locator('.lm-head [data-map-progress] b').inner_text()
    if not progress.startswith('1'):
        problems.append(f'{lang}: ticking a step does not move the map progress ({progress})')
    await page.goto((root / 'kb' / 'guides' / 'getting-started' / 'index.html').as_uri())
    if await page.locator('nav.lm-walk--bottom [data-step-toggle][aria-pressed="true"]').count() != 1:
        problems.append(f'{lang}: the step bar on the guide does not show the ticked step')
    await page.evaluate("localStorage.removeItem('hub-learning')")
    # a course: «next» opens the next part
    await page.goto((root / 'responsible-ai' / 'index.html').as_uri())
    first = await page.evaluate("document.querySelector('[data-tab-panel]:not([hidden])').id")
    await page.locator('.tab-panel:not([hidden]) .course-next a').click()
    await page.wait_for_timeout(300)  # the tab follows the address change, which the browser delivers after the click
    if await page.evaluate("document.querySelector('[data-tab-panel]:not([hidden])').id") == first:
        problems.append(f'{lang}: the course «next» link does not open the next part')
    # theme persists across files
    await page.locator('#theme-switch').click()
    chosen = await page.locator('html').get_attribute('data-theme')
    await page.goto((root / 'process' / 'index.html').as_uri())
    if await page.locator('html').get_attribute('data-theme') != chosen:
        problems.append(f'{lang}: the theme does not persist across pages')
    problems.extend(f'{lang}: script error during interactions: {e}' for e in errors)
    await context.close()


async def check():
    problems, counts, heights = [], {}, {}
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(env=browser_env(), args=['--no-sandbox'])
        langs = editions()
        for lang in langs:
            counts[f'pages_{lang}'] = await sweep(browser, lang, heights, problems)
            await interact(browser, lang, problems)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto((SITE / 'index.html').as_uri())
        await page.wait_for_url('**/ru/index.html')
        await context.close()
        await browser.close()
    # layout parity: a translated page about as long as its Russian twin (text length differs, structure must not)
    uneven = []
    for (width, name), by in sorted(heights.items()):
        if 'ru' in by and len(by) > 1:
            for lang, h in by.items():
                if lang != 'ru' and by['ru'] > 600 and not 0.6 <= h / by['ru'] <= 1.4:
                    uneven.append(f'{width} {lang}/{name}: height {h} vs {by["ru"]} in Russian')
    problems.extend(uneven)
    counts['views'] = [f'{w} {t}' for w, t in VIEWS]
    REPORT.mkdir(parents=True, exist_ok=True)
    (REPORT / 'browser-report.json').write_text(json.dumps({'counts': counts, 'problems': problems}, ensure_ascii=False, indent=1))
    return counts, problems


def main():
    counts, problems = asyncio.run(check())
    print(json.dumps({'counts': counts, 'errors': problems[:40], 'error_count': len(problems)}, ensure_ascii=False, indent=1))
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
