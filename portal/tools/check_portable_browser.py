#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Verify the real portable folder through file URLs with no HTTP server.
#   SCOPE: Every page, network isolation, fonts, search, navigation, themes, diagrams and clipboard fallback.
#   DEPENDS: M-PORTABLE-EXPORT
#   LINKS: M-PORTABLE-EXPORT, V-M-PORTABLE-EXPORT
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   ROOT - source repository root
#   check - exercise a relocated export without an HTTP server
# END_MODULE_MAP
"""Run after export_portable.py using portal/.venv/bin/python."""
import argparse
import asyncio
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
from urllib.parse import urlsplit

from playwright.async_api import async_playwright
from browser_check import browser_env

ROOT = Path(__file__).resolve().parents[2]


async def check(source, report_dir):
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / 'browser-report.json').unlink(missing_ok=True)
    manifest = json.loads((source / 'portable-manifest.json').read_text())
    for path, expected in manifest['files'].items():
        assert hashlib.sha256((source / path).read_bytes()).hexdigest() == expected, path
    errors, external, failed, checked = [], [], [], []
    with tempfile.TemporaryDirectory(prefix='AICC file test ') as temporary:
        # Moving to an unrelated path containing spaces also detects absolute-path leaks.
        folder = Path(temporary) / 'Копия портала'
        shutil.copytree(source, folder)
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(env=browser_env(), args=['--no-sandbox'])
            context = await browser.new_context(viewport={'width': 1440, 'height': 900})
            context.on('request', lambda r: external.append(r.url) if r.url.startswith(('http:', 'https:')) else None)
            context.on('requestfailed', lambda r: failed.append({'url': r.url, 'failure': r.failure}))
            context.on('page', lambda p: p.on('pageerror', lambda e: errors.append(str(e))))
            entries = ('en/index.html', 'ru/index.html')
            paths = sorted(p for p in manifest['files'] if p.endswith('.html') and p not in entries and not p.startswith('sources/'))
            for entry in entries:  # the language entries forward to the Center
                forward = await context.new_page()
                await forward.goto((folder / entry).as_uri(), wait_until='load')
                await forward.wait_for_url('**/' + entry.split('/')[0] + '/center/index.html')
                assert await forward.locator('h1').count() == 1, entry
                await forward.close()
            queue = asyncio.Queue()
            for path in paths:
                queue.put_nowait(path)

            async def sweep():
                page = await context.new_page()
                while not queue.empty():
                    path = queue.get_nowait()
                    await page.goto((folder / path).as_uri(), wait_until='load')
                    assert await page.locator('h1').count() == 1, path
                    if path.startswith(('en/', 'ru/')):
                        assert await page.locator('nav.lang-switch a').count() == 2, path
                        assert await page.evaluate('Array.isArray(window.AICC_SEARCH_INDEX)'), path
                    checked.append(path)
                await page.close()
            await asyncio.gather(*(sweep() for _ in range(3)))
            page = await context.new_page()
            await page.goto((folder / 'aicc.html').as_uri())
            await page.locator('a[lang="ru"]').click()
            await page.wait_for_url('**/ru/center/index.html')
            await page.locator('#theme-switch').click()
            selected = await page.locator('html').get_attribute('data-theme')
            await page.evaluate('localStorage.clear()')
            await page.locator('nav.lang-switch a[lang="en"]').click()
            # A file navigation can commit before its head scripts finish loading.
            await page.wait_for_load_state('load')
            assert await page.locator('html').get_attribute('data-theme') == selected
            assert urlsplit(page.url).path.endswith('/en/center/index.html')
            for lang in ('en', 'ru'):
                # Global search covers every branch: each branch index loads as a script, never by fetch.
                await page.goto((folder / lang / 'center/index.html').as_uri())
                await page.evaluate("() => { window.fetch = () => { throw new Error('fetch is unavailable in the file edition'); }; }")
                await page.locator('#q-all').check()
                await page.locator('#q').fill('Frontline Service Copilot' if lang == 'en' else 'AI-помощник сотрудника первой линии')
                found = page.locator('#results a[href*="discovery/"]').first
                await found.wait_for(state='visible')
                assert await found.locator('.search-branch').count() == 1
                await page.goto((folder / lang / 'center/index.html').as_uri())
                # Block fetch explicitly so the real search must use the bundled index.
                await page.evaluate("() => { window.fetch = () => { throw new Error('fetch is unavailable in the file edition'); }; }")
                heading = await page.evaluate("window.AICC_SEARCH_INDEX.find(e => e.u.includes('/reference/vocabulary/index.html')).h")
                await page.locator('#q').fill(heading)
                result = page.locator('#results a[href*="reference/vocabulary/index.html"]').first
                await result.wait_for(state='visible')
                await result.click()
                assert urlsplit(page.url).path.endswith('/reference/vocabulary/index.html')
                await page.evaluate('document.fonts.ready')
                fonts = await page.evaluate('''async () => {
                  await document.fonts.load('16px "Golos Text"', 'Термин');
                  await document.fonts.load('16px "TT Norms Pro"', 'Title');
                  return document.fonts.check('16px "Golos Text"', 'Термин') && document.fonts.check('16px "TT Norms Pro"', 'Title');
                }''')
                assert fonts, lang
            await page.goto((folder / 'ru/center/delivery/index.html').as_uri())
            await page.locator('.dz-open').first.click()
            assert await page.locator('#dz').is_visible()
            assert await page.locator('#dz svg').count() > 0
            await page.keyboard.press('Escape')
            await page.goto((folder / 'ru/center/knowledge-base/initiative-brief/index.html').as_uri())
            await page.evaluate("Object.defineProperty(navigator, 'clipboard', {value: undefined, configurable: true}); document.execCommand = () => false;")
            copy = page.locator('[data-copy]').first
            target = await copy.get_attribute('data-copy')
            expected = await page.locator('#' + target).text_content()
            await copy.click()
            field = page.locator('dialog[open] textarea')
            assert await field.input_value() == expected
            await page.keyboard.press('Escape')
            await page.goto((folder / 'ru/index.html').as_uri())
            await page.screenshot(path=str(report_dir / 'desktop.png'), full_page=True)
            await page.set_viewport_size({'width': 390, 'height': 844})
            await page.reload()
            assert await page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'), 'Mobile overflow'
            await page.screenshot(path=str(report_dir / 'mobile.png'), full_page=True)
            assert not errors, errors[:10]
            assert not external, external[:10]
            assert not failed, failed[:10]
            await browser.close()
    report = {'status': 'passed', 'package_manifest_sha256': hashlib.sha256((source / 'portable-manifest.json').read_bytes()).hexdigest(), 'protocol': 'file:', 'pages': len(checked), 'relocated_with_spaces_and_cyrillic': True,
              'checks': ['entry point', 'all pages', 'EN/RU switch', 'theme across files with storage cleared', 'global search from the router without fetch', 'search without fetch', 'search result navigation', 'embedded fonts', 'diagram zoom', 'manual copy fallback', 'mobile layout'],
              'external_requests': external, 'failed_requests': failed, 'page_errors': errors,
              'limitation': 'Windows SMB access and corporate browser policy require a workstation check.'}
    (report_dir / 'browser-report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--folder', type=Path, default=ROOT / 'portal/published')
    parser.add_argument('--report', type=Path, default=ROOT / '.runtime/portable')
    args = parser.parse_args()
    asyncio.run(check(args.folder.resolve(), args.report.resolve()))
