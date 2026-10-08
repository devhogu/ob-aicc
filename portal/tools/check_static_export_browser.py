#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Verify complete script-free language editions as relocated standalone folders.
#   SCOPE: Source content/stage retention, all file routes, native controls, light-only rendering and responsive reading.
#   DEPENDS: M-PORTABLE-EXPORT
#   LINKS: M-PORTABLE-EXPORT, V-M-PORTABLE-EXPORT
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   ROOT - maintained source repository
#   atoms - collect authored reading content separately from UI controls
#   verify_content - compare retained authored reading content against the current generated site
#   check - exercise both independent packages with scripting disabled and dark OS preference
# END_MODULE_MAP
import argparse
import asyncio
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile

from playwright.async_api import async_playwright
from browser_check import browser_env
from static_export import Tree, text_content, validate_edition
from export_portable import snapshot, digest

ROOT = Path(__file__).resolve().parents[2]


def atoms(text):
    root = Tree(text).root
    # Button labels are UI affordances, not authored reading content.
    for node in list(root.walk()):
        if node.tag == 'button':
            node.remove()
    main = next(n for n in root.walk() if n.tag == 'main')
    retained = []
    for node in main.walk():
        ancestor = node
        skip = False
        while ancestor is not main:
            if ancestor.tag in ('template', 'script', 'dialog', 'button') or any(ancestor.has(c) for c in ('pf-filter', 'dl-filters', 'kb-detail', 'mm-dark', 'lab-controls')) or 'hidden' in ancestor.attrs and (ancestor.has('pf-empty') or ancestor.has('dl-empty')):
                skip = True
                break
            ancestor = ancestor.parent
        if not skip and node.tag in ('h1', 'h2', 'h3', 'h4', 'p', 'td', 'th', 'pre'):
            value = re.sub(r'\s+', ' ', text_content(node)).strip()
            if value:
                retained.append((node.tag, value))
    return Counter(retained)


def verify_content(folder, manifest):
    original = snapshot(ROOT / 'html/aicc/v1')
    assert manifest['source_tree_sha256'] == digest(original), 'Export is not from the current complete site'
    for lang in ('en', 'ru'):
        paths = [p for p in original if p.startswith(lang + '/') and p.endswith('.html')]
        assert len(paths) == manifest['source_pages'][lang]
        for path in paths:
            source, output = original[path].decode(), (folder / path).read_text()
            missing = atoms(source) - atoms(output)
            assert not missing, (path, list(missing.items())[:3])
            for match in re.finditer(r'\bconst\s+FLOW_STAGES\s*=\s*', source):
                data = json.JSONDecoder().raw_decode(source[match.end():])[0]
                rendered = re.sub(r'\s+', ' ', text_content(Tree(output).root))
                for stages in data.values():
                    for stage in stages:
                        for key in ('title', 'intent', 'problem'):
                            if stage.get(key):
                                expected = re.sub(r'\s+', ' ', stage[key])
                                assert expected in rendered, (path, stage['slug'], key)
        validate_edition(snapshot(folder / lang), lang)


async def check(folder, report_dir):
    report_dir.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((folder / 'portable-manifest.json').read_text())
    assert manifest['kind'] == 'aicc-static-languages-v1'
    for path, expected in manifest['files'].items():
        assert hashlib.sha256((folder / path).read_bytes()).hexdigest() == expected, path
    assert not list(folder.rglob('*.js'))
    verify_content(folder, manifest)
    checked, network, failed = [], [], []
    with tempfile.TemporaryDirectory(prefix='AICC static copy ') as temporary:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(env=browser_env(), args=['--no-sandbox'])
            for lang in ('en', 'ru'):
                # Sibling edition and parent entry do not exist in this relocation.
                standalone = Path(temporary) / ('Отдельная копия ' + lang)
                shutil.copytree(folder / lang, standalone)
                context = await browser.new_context(java_script_enabled=False, color_scheme='dark', viewport={'width':1440,'height':900})
                context.on('request', lambda r: network.append(r.url) if r.url.startswith(('http:', 'https:')) else None)
                context.on('requestfailed', lambda r: failed.append({'url':r.url,'error':r.failure}))
                queue = asyncio.Queue()
                for path in sorted(standalone.rglob('*.html')):
                    if path.parent == standalone and path.name in ('index.html', 'aicc.html'):
                        continue  # the entries forward to the Center and are checked below
                    queue.put_nowait(path)
                async def sweep():
                    page = await context.new_page()
                    while not queue.empty():
                        path = queue.get_nowait()
                        await page.goto(path.as_uri(), wait_until='load')
                        assert await page.locator('h1').count() == 1, path
                        assert await page.locator('html').get_attribute('lang') == lang, path
                        assert await page.locator('html').get_attribute('data-theme') == 'light', path
                        assert await page.locator('script,button,input,select,template,dialog,[hidden],.lang-switch,.theme-switch').count() == 0, path
                        assert await page.evaluate("getComputedStyle(document.documentElement).colorScheme") == 'light', path
                        checked.append(lang + '/' + path.relative_to(standalone).as_posix())
                    await page.close()
                await asyncio.gather(*(sweep() for _ in range(3)))
                page = await context.new_page()
                for diagram in sorted((standalone / 'assets/diagrams').glob('*.svg')):
                    await page.goto(diagram.as_uri())
                    assert await page.locator('svg').count() >= 1, diagram
                    assert await page.locator('parsererror').count() == 0, diagram
                for width in (1440, 900, 390):
                    await page.set_viewport_size({'width':width,'height':900})
                    for route in ('contents.html','center/index.html','center/about/values-and-principles/index.html','discovery/strategic-portfolio/index.html','discovery/value-streams/index.html','lab/index.html','portfolio/index.html','program/index.html','program/service-resolution/charter/index.html'):
                        await page.goto((standalone / route).as_uri())
                        assert await page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'), (lang, width, route, 'page overflow')
                        if route == 'discovery/strategic-portfolio/index.html':
                            panels = page.locator('.problems-panel')
                            assert await panels.count() == 2
                            for panel in await panels.all():
                                assert await panel.is_visible()
                            details = page.locator('details.scenario-card').first
                            await details.locator('summary').click()
                            assert await details.get_attribute('open') is not None
                        if route == 'discovery/value-streams/index.html':
                            target = await page.locator('.flow-stages__stage').first.get_attribute('href')
                            await page.goto((standalone / route).as_uri() + target)
                            assert await page.locator(target).is_visible(), (lang, width, 'stage fragment')
                            assert await page.locator(target + ' p').count() >= 2
                        if route == 'lab/index.html':
                            assert await page.locator('.lab-task').count() == 37
                            assert await page.locator('.lab-stage-nav a').count() == 7
                        if route == 'portfolio/index.html':
                            for panel in await page.locator('[data-pf-panel]').all():
                                assert await panel.is_visible()
                        if route == 'program/service-resolution/charter/index.html':
                            link = page.locator('.static-diagram-link').first
                            assert await link.is_visible()
                            url = await link.get_attribute('href')
                            diagram = (standalone / route).parent / url
                            assert diagram.resolve().is_file()
                    await page.goto((standalone / 'discovery/value-streams/index.html').as_uri())
                    await page.screenshot(path=str(report_dir / f'{lang}-{width}.png'), full_page=True)
                await page.goto((standalone / 'index.html').as_uri())
                await page.wait_for_url('**/center/index.html')  # the language entry forwards to the Center
                await page.locator('.static-contents-link').click()
                assert page.url.split('#')[0].endswith('/contents.html')
                await page.locator('a[href="center/about/strategy/index.html"]').click()
                assert page.url.endswith('/center/about/strategy/index.html')
                await page.wait_for_load_state('load')
                await page.evaluate('''async () => {
                    await document.fonts.load('16px "Golos Text"', 'Текст');
                    await document.fonts.load('700 24px "TT Norms Pro"', 'Title');
                    await document.fonts.ready;
                }''')
                assert await page.evaluate('document.fonts.check(\'16px "Golos Text"\') && document.fonts.check(\'700 24px "TT Norms Pro"\')')
                await context.close()
            await browser.close()
    assert not network, network[:5]
    assert not failed, failed[:5]
    report = {'status':'passed', 'package_manifest_sha256':hashlib.sha256((folder / 'portable-manifest.json').read_bytes()).hexdigest(), 'source_tree_sha256':manifest['source_tree_sha256'], 'html_pages':len(checked), 'source_pages':manifest['source_pages'], 'inline_workflow_stages':manifest['inline_workflow_stages'], 'javascript_enabled':False, 'os_color_scheme':'dark', 'rendered_theme':'light', 'independently_relocated_languages':True, 'external_requests':network, 'failed_requests':failed, 'checks':['complete authored reading content and workflow popup text', 'all file routes', 'native disclosures and stage fragment reveal', 'topic navigation', 'all Lab tasks and Portfolio sections', 'standalone diagram links', 'embedded fonts', 'desktop/intermediate/mobile layout']}
    (report_dir / 'browser-report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--folder', type=Path, default=ROOT / 'portal/published')
    parser.add_argument('--report', type=Path, default=ROOT / '.runtime/static-export')
    args = parser.parse_args()
    asyncio.run(check(args.folder.resolve(), args.report.resolve()))
