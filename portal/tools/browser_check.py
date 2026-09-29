#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Browser verification of html/aicc in both languages, themes and viewports.
#   SCOPE: Serves the output locally, checks fonts, layout, interaction and language switching, writes report and screenshots.
#   DEPENDS: M-PORTAL-PROJECTION
#   LINKS: M-PORTAL-PROJECTION, V-M-PORTAL-PROJECTION
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   ROOT - module-internal helper or constant
#   OUT_SITE - module-internal helper or constant
#   VERIFY - module-internal helper or constant
#   LOCAL_LIBS - module-internal helper or constant
#   VIEWPORTS - module-internal helper or constant
#   PAGES - module-internal helper or constant
#   THEMES - module-internal helper or constant
#   LANGS - module-internal helper or constant
#   Quiet - module-internal helper or constant
#   browser_env - module-internal helper or constant
#   check - run all browser checks
#   main - command-line entry point
# END_MODULE_MAP
"""Browser check of the generated site in html/aicc.

Run with the local environment created by portal/tools/setup_browser.sh:
  portal/.venv/bin/python portal/tools/browser_check.py
Rootless Chromium system libraries come from portal/.tools/pw-syslibs when present.
Writes portal/verification/browser-report.json and screenshots/. Exit code 1 on any failed check.
"""
import argparse
import asyncio
import json
import os
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT_SITE = ROOT.parent / 'html' / 'aicc'
VERIFY = ROOT / 'verification'
LOCAL_LIBS = ROOT / '.tools' / 'pw-syslibs'
VIEWPORTS = {'mobile': (390, 844), 'desktop': (1440, 900)}
PAGES = {'home': '', 'statement': 'statement-of-intent/'}
THEMES = ('light', 'dark')
LANGS = ('ru', 'en')


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class Prefixed(SimpleHTTPRequestHandler):
    """Serve html/aicc under /aicc the way Caddy handle_path does: /aicc itself is answered with the site
    index and no redirect, so relative links on it resolve against the server root."""

    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path.split('?')[0] == '/aicc':
            body = (OUT_SITE / 'index.html').read_bytes()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def translate_path(self, path):
        if path.startswith('/aicc/'):
            return super().translate_path(path[len('/aicc'):])
        return super().translate_path('/__none__')


def browser_env():
    env = dict(os.environ)
    if LOCAL_LIBS.is_dir():
        p = str(LOCAL_LIBS)
        env['LD_LIBRARY_PATH'] = ':'.join([p + '/usr/lib/x86_64-linux-gnu', p + '/lib/x86_64-linux-gnu', p + '/usr/lib',
                                           env.get('LD_LIBRARY_PATH', '')]).strip(':')
        env['FONTCONFIG_PATH'] = p + '/etc/fonts'
        env['FONTCONFIG_FILE'] = p + '/etc/fonts/portal.conf'
    return env


async def check(base, prefixed):
    results, failures = [], []

    def record(name, ok, detail=''):
        results.append({'check': name, 'ok': bool(ok), 'detail': detail})
        if not ok:
            failures.append(f'{name}: {detail}')

    (VERIFY / 'screenshots').mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(env=browser_env())
        for vp_name, (w, h) in VIEWPORTS.items():
            ctx = await browser.new_context(viewport={'width': w, 'height': h}, reduced_motion='reduce')
            page = await ctx.new_page()
            problems = []
            page.on('pageerror', lambda e: problems.append(f'pageerror {e}'))
            page.on('console', lambda m: problems.append(f'console {m.text}') if m.type == 'error' else None)
            page.on('response', lambda r: problems.append(f'{r.status} {r.url}') if r.status >= 400 else None)
            page.on('request', lambda r: problems.append(f'external {r.url}') if not r.url.startswith((base, prefixed, 'data:')) else None)
            for lang in LANGS:
                for pname, sub in PAGES.items():
                    for theme in THEMES:
                        tag = f'{lang}/{pname}/{theme}/{vp_name}'
                        await page.goto(f'{base}/{lang}/{sub}index.html')
                        await page.evaluate(f"document.documentElement.setAttribute('data-theme','{theme}')")
                        await page.evaluate('document.fonts.ready')
                        info = await page.evaluate('''() => ({
                            lang: document.documentElement.lang,
                            overflow: document.documentElement.scrollWidth - window.innerWidth,
                            h1: getComputedStyle(document.querySelector('h1')).fontFamily,
                            body: getComputedStyle(document.body).fontFamily,
                            headingLoaded: document.fonts.check('700 16px "TT Travels Text"'),
                            bodyLoaded: document.fonts.check('400 16px "Golos Text"'),
                            logo: (() => { const i = document.querySelector('.site-logo'); if (!i) return false; const r = i.getBoundingClientRect(); return r.width > 40 && r.left < 40; })(),
                        })''')
                        record(f'lang attribute {tag}', info['lang'] == lang, info['lang'])
                        record(f'no horizontal overflow {tag}', info['overflow'] <= 0, str(info['overflow']))
                        record(f'heading font {tag}', info['h1'].startswith('"TT Travels Text"') and info['headingLoaded'], info['h1'])
                        record(f'body font {tag}', info['body'].startswith('"Golos Text"') and info['bodyLoaded'], info['body'])
                        record(f'logo at far left {tag}', info['logo'])
                        record(f'one theme icon visible {tag}', await page.locator('.theme-icon:visible').count() == 1)
                        await page.screenshot(path=str(VERIFY / 'screenshots' / f'{lang}-{pname}-{theme}-{vp_name}.png'))
                    # fallback marker on the Russian statement page
                    if lang == 'ru' and pname == 'statement':
                        note = await page.locator('.oc-notice').inner_text()
                        h1lang = await page.locator('h1').get_attribute('lang')
                        record('ru statement shows translation marker', 'недоступен' in note, note)
                        record('ru statement fallback fragments carry lang=en', h1lang == 'en', str(h1lang))
                    if lang == 'en' and pname == 'statement':
                        record('en statement has no translation marker', await page.locator('.oc-notice').count() == 0)

            # interaction checks on the statement page in Russian
            await page.goto(f'{base}/ru/statement-of-intent/index.html')
            await page.evaluate("document.documentElement.setAttribute('data-theme','light')")
            await page.keyboard.press('Tab')
            skip_focused = await page.evaluate("document.activeElement.classList.contains('oc-skiplink')")
            skip_visible = await page.evaluate("(()=>{const r=document.activeElement.getBoundingClientRect();return r.left>=0&&r.width>0})()")
            record(f'skip link focusable and visible {vp_name}', skip_focused and skip_visible)
            await page.keyboard.press('Enter')
            record(f'skip link moves to main {vp_name}', await page.evaluate("location.hash==='#main'"))

            await page.goto(f'{base}/ru/index.html')
            await page.keyboard.press('Tab'); await page.keyboard.press('Tab')
            outline = await page.evaluate("(()=>{const s=getComputedStyle(document.activeElement);return [s.outlineStyle,parseFloat(s.outlineWidth)]})()")
            record(f'visible focus state {vp_name}', outline[0] != 'none' and outline[1] >= 2, str(outline))

            if vp_name == 'mobile':
                btn = page.locator('.site-menu-button')
                nav = page.locator('#site-sidebar')
                record('mobile menu button visible', await btn.is_visible())
                record('mobile sidebar hidden by default', not await nav.is_visible())
                await btn.click()
                record('mobile menu opens', await nav.is_visible() and await btn.get_attribute('aria-expanded') == 'true')
                await page.keyboard.press('Escape')
                record('mobile menu closes on Escape', not await nav.is_visible())
            else:
                record('desktop menu button hidden', not await page.locator('.site-menu-button').is_visible())
                record('desktop sidebar navigation visible', await page.locator('#site-nav').is_visible())
                box = await page.locator('.site-sidebar').bounding_box()
                record('desktop sidebar is on the left', box['x'] < 2 and box['width'] > 200, str(box))

            await page.goto(f'{base}/ru/index.html')
            await page.evaluate("localStorage.clear()")
            await page.reload()
            await page.locator('.site-theme-button').click()
            dark = await page.evaluate("document.documentElement.getAttribute('data-theme')")
            await page.reload()
            persisted = await page.evaluate("document.documentElement.getAttribute('data-theme')")
            record(f'theme switch and persistence {vp_name}', dark == 'dark' and persisted == 'dark', f'{dark}/{persisted}')

            for start, other in (('ru', 'en'), ('en', 'ru')):
                await page.goto(f'{base}/{start}/statement-of-intent/index.html')
                await page.locator(f'.site-lang a[data-lang="{other}"]').click()
                await page.wait_for_load_state()
                url_ok = page.url.endswith(f'/{other}/statement-of-intent/index.html')
                lang_ok = await page.evaluate('document.documentElement.lang') == other
                record(f'language switch {start}->{other} same page {vp_name}', url_ok and lang_ok, page.url)

            # gateway
            await page.evaluate("localStorage.clear()")
            await page.goto(f'{base}/index.html')
            await page.wait_for_url('**/ru/index.html')
            record(f'root leads to ru {vp_name}', page.url.endswith('/ru/index.html'), page.url)

            # /aicc without a trailing slash must still lead into /aicc/ru/, not the server root. Speculative
            # requests made before the redirect are expected to miss, so this page has no request listeners.
            slash = await ctx.new_page()
            try:
                await slash.goto(f'{prefixed}/aicc')
                await slash.wait_for_url('**/aicc/ru/index.html', timeout=5000)
                await slash.wait_for_selector('h1', timeout=5000)
            except Exception:
                pass
            record(f'/aicc without slash stays under /aicc {vp_name}', slash.url.endswith('/aicc/ru/index.html'), slash.url)
            await slash.close()

            record(f'no console errors, failed or external requests {vp_name}', not problems, '; '.join(problems[:3]))
            await ctx.close()
        await browser.close()
    return results, failures


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base-url', help='test an already running site instead of serving html/aicc')
    args = ap.parse_args()
    server = None
    if args.base_url:
        base = args.base_url.rstrip('/')
    else:
        handler = partial(Quiet, directory=str(OUT_SITE))
        server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
        Thread(target=server.serve_forever, daemon=True).start()
        base = f'http://127.0.0.1:{server.server_address[1]}'
    pref_server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Prefixed, directory=str(OUT_SITE)))
    Thread(target=pref_server.serve_forever, daemon=True).start()
    prefixed = f'http://127.0.0.1:{pref_server.server_address[1]}'
    try:
        results, failures = asyncio.run(check(base, prefixed))
    finally:
        if server:
            server.shutdown()
        pref_server.shutdown()
    report = {'base': 'served from html/aicc' if server else base, 'viewports': VIEWPORTS,
              'passed': sum(r['ok'] for r in results), 'failed': len(failures), 'checks': results}
    (VERIFY / 'browser-report.json').write_text(json.dumps(report, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for f in failures:
        print('FAIL', f)
    print(f'{report["passed"]} passed, {report["failed"]} failed')
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
