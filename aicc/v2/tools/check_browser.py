#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Open every page of the built Hub site from the folder (file://) in a browser and check it renders, searches and switches theme without errors.
#   SCOPE: Reads html/aicc/v2; writes only a report under .runtime/hub-v2.
#   DEPENDS: playwright (the repository virtual environment)
#   LINKS: C-HUB-V2, V-M-PORTAL-PROJECTION
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   check - sweep every page at two widths, then exercise search, theme and the entry
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


async def check():
    pages = sorted(p for p in (SITE / 'ru').rglob('index.html'))
    problems, counts = [], {'pages': len(pages)}
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(env=browser_env(), args=['--no-sandbox'])
        for width in (1440, 390):
            context = await browser.new_context(viewport={'width': width, 'height': 900})
            page = await context.new_page()
            seen = []
            page.on('pageerror', lambda e: seen.append('script: ' + str(e)))
            page.on('requestfailed', lambda r: seen.append('failed: ' + r.url))
            page.on('request', lambda r: seen.append('external: ' + r.url) if r.url.startswith(('http:', 'https:')) else None)
            for path in pages:
                seen.clear()
                await page.goto(path.as_uri(), wait_until='load')
                if await page.locator('h1').count() != 1:
                    problems.append(f'{width} {path.relative_to(SITE)}: h1 count')
                if not await page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'):
                    problems.append(f'{width} {path.relative_to(SITE)}: horizontal overflow')
                if await page.locator('.status-chip').count() != 1 or await page.locator('.pagefb').count() != 1:
                    problems.append(f'{width} {path.relative_to(SITE)}: chip or feedback button missing')
                problems.extend(f'{width} {path.relative_to(SITE)}: {s}' for s in seen)
            counts[f'swept_{width}'] = len(pages)
            await context.close()

        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()
        await page.goto((SITE / 'index.html').as_uri())
        await page.wait_for_url('**/ru/index.html')
        counts['entry'] = 'ok'
        # search finds a term and a page, and a result leads there
        await page.locator('#q').fill('воронка')
        await page.locator('#results a').first.wait_for()
        found = await page.locator('#results a').count()
        if not found:
            problems.append('search found nothing for «воронка»')
        first = page.locator('#results a').first
        await first.click()
        await page.wait_for_load_state('load')
        if '/ru/' not in page.url:
            problems.append('a search result leads outside the site: ' + page.url)
        counts['search_results'] = found
        # a card page and the card views are reachable from the navigation
        await page.goto((SITE / 'ru' / 'index.html').as_uri())
        await page.locator('.portal-section-link[data-section="projects"]').click()
        await page.wait_for_load_state('load')
        if '/projects/' not in page.url:
            problems.append('the Projects section is not reachable from the navigation')
        # theme switch persists across files
        await page.locator('#theme-switch').click()
        chosen = await page.locator('html').get_attribute('data-theme')
        await page.goto((SITE / 'ru' / 'process' / 'index.html').as_uri())
        if await page.locator('html').get_attribute('data-theme') != chosen:
            problems.append('the theme does not persist across pages')
        counts['theme'] = chosen
        await context.close()
        await browser.close()
    REPORT.mkdir(parents=True, exist_ok=True)
    (REPORT / 'browser-report.json').write_text(json.dumps({'counts': counts, 'problems': problems}, ensure_ascii=False, indent=1))
    return counts, problems


def main():
    counts, problems = asyncio.run(check())
    print(json.dumps({'counts': counts, 'errors': problems[:40]}, ensure_ascii=False, indent=1))
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
