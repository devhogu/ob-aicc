#!/usr/bin/env python3
"""Exercise AI Lab's actual reading path in both editions, themes and viewports."""
from collections import Counter
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import tempfile
import threading

from playwright.sync_api import sync_playwright

from export_portable import export
import lab

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'html/aicc'
REPORT = ROOT / '.runtime/ai-lab'


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


MEASURE = """() => {
 const visible=e=>!!e.getClientRects().length;
 const clipped=[...document.querySelectorAll('.lab-card,.lab-controls')].filter(e=>visible(e)&&(e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2)).map(e=>e.id||e.className);
 const text=[...document.querySelectorAll('.lab-content p,.lab-content h2,.lab-task h4,.lab-options button,.lab-guardrail-group td')].filter(visible).map(e=>{const s=getComputedStyle(e);return {color:s.color,font:s.fontFamily,size:s.fontSize}});
 return {width:innerWidth,scroll:document.documentElement.scrollWidth,clipped,text,
  theme:document.documentElement.dataset.theme,
  background:getComputedStyle(document.querySelector('.lab-card')).backgroundColor,
  muted:getComputedStyle(document.querySelector('.lab-task p')).color,
  h1:document.querySelectorAll('h1').length,main:document.querySelectorAll('main').length,
  groups:[...document.querySelectorAll('.portal-section-link')].map(e=>e.textContent.trim())};
}"""


def contrast(first, second):
    def luminance(value):
        parts = [int(part) / 255 for part in value.removeprefix('rgb(').removesuffix(')').split(',')]
        parts = [part / 12.92 if part <= .04045 else ((part + .055) / 1.055) ** 2.4 for part in parts]
        return sum(part * weight for part, weight in zip(parts, (.2126, .7152, .0722)))
    values = sorted((luminance(first), luminance(second)))
    return (values[1] + .05) / (values[0] + .05)


def interactions(page, counts):
    for step in range(1, 7):
        button = page.locator(f'[data-lab-stage="{step}"]')
        button.focus()
        page.keyboard.press('Enter')
        assert button.get_attribute('aria-pressed') == 'true'
        assert page.locator('.lab-stage:visible').count() == 1
        assert page.locator('.lab-cell:visible').count() == 5
        assert page.locator('.lab-cell:visible').evaluate_all('els=>els.every(e=>e.dataset.stage===String(' + str(step) + '))')
        assert button.evaluate('e=>document.activeElement===e')
        counts['stage_selections'] += 1
        for lane in 'ABCDE':
            page.locator(f'[data-lab-lane="{lane}"]').click()
            cell = page.locator('.lab-cell:visible')
            assert cell.count() == 1 and cell.get_attribute('data-lane') == lane
            assert cell.get_attribute('data-stage') == str(step)
            counts['stage_lane_combinations'] += 1
        page.locator('[data-lab-lane=all]').click()
    page.locator('[data-lab-reset]').focus()
    page.keyboard.press('Space')
    assert page.locator('.lab-cell:visible').count() == 30
    assert page.locator('.lab-task:visible').count() == 41
    assert page.locator('[data-lab-stage=all]').get_attribute('aria-pressed') == 'true'
    assert page.locator('[data-lab-lane=all]').get_attribute('aria-pressed') == 'true'
    # Search or a local fragment must reveal content hidden by a selected view.
    page.locator('[data-lab-stage="1"]').click()
    page.locator('[data-lab-lane="E"]').click()
    page.evaluate('location.hash="task-a-2-2"')
    page.wait_for_function('!document.querySelector("#task-a-2-2").closest(".lab-cell").hidden')
    assert page.locator('#task-a-2-2').is_visible()
    assert page.locator('#task-a-2-2').evaluate('e=>document.activeElement===e')
    page.reload()
    assert page.locator('#task-a-2-2').is_visible()
    counts['fragment_reveal_checks'] += 2


def main():
    REPORT.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Quiet, directory=str(OUTPUT)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f'http://127.0.0.1:{server.server_port}/'
    counts, errors, observations = Counter(), [], []
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(viewport={'width': 1440, 'height': 1000})
            page = context.new_page()
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.on('requestfailed', lambda request: errors.append(str(request.failure)))
            page.on('response', lambda response: errors.append(f'HTTP {response.status} {response.url}') if response.status >= 400 else None)
            page.goto(base + 'en/lab/')
            for width in (1440, 768, 390, 320):
                page.set_viewport_size({'width': width, 'height': 1000})
                for theme in ('light', 'dark'):
                    page.evaluate('t=>localStorage.setItem("aicc-theme",t)', theme)
                    for lang in ('en', 'ru'):
                        page.goto(base + lang + '/lab/')
                        page.evaluate('document.fonts.ready')
                        page.screenshot(path=str(REPORT / f'{lang}-{width}-{theme}-viewport.png'))
                        assert page.locator('.lab-controls').is_visible()
                        state = page.evaluate(MEASURE)
                        assert state['scroll'] <= width + 1, f'{lang}/{width}/{theme}: overflow {state["scroll"]}'
                        assert not state['clipped'], f'{lang}/{width}/{theme}: clipped {state["clipped"]}'
                        assert state['theme'] == theme and state['h1'] == state['main'] == 1
                        assert state['groups'][-1] == 'AI Lab'
                        assert all('Golos Text' in item['font'] or 'TT Norms Pro' in item['font'] for item in state['text'])
                        assert contrast(state['muted'], state['background']) >= 4.5, state
                        interactions(page, counts)
                        # Common page feedback, legal links, sidebar anchors and section-local search.
                        page.locator('.o-footer .pagefb').click()
                        assert page.locator('#fb').is_visible()
                        page.keyboard.press('Escape')
                        assert not page.locator('#fb').is_visible()
                        if width < 1101:
                            page.locator('.o-nav>details>summary').click()
                        page.locator('.portal-local-nav a[href="#guardrails"]').click()
                        assert page.locator('#guardrails').evaluate('e=>document.activeElement===e')
                        page.locator('#q').fill('Define IAM and Policies' if lang == 'en' else 'Определить IAM и политики')
                        result = page.locator('#results a').first
                        result.wait_for()
                        assert '#task-a-2-2' in result.get_attribute('href')
                        result.click()
                        assert page.locator('#task-a-2-2').is_visible()
                        page.locator('.lang-switch a[lang="' + ('ru' if lang == 'en' else 'en') + '"]').click()
                        assert page.locator('html').get_attribute('lang') != lang
                        page.goto(base + lang + '/lab/')
                        page.screenshot(path=str(REPORT / f'{lang}-{width}-{theme}.png'), full_page=True)
                        observations.append({'lang': lang, 'width': width, 'theme': theme, 'muted_contrast': round(contrast(state['muted'], state['background']), 2)})
                        counts['page_views'] += 1
                        print(f'Checked AI Lab {lang}, {width}px, {theme}', flush=True)
            # Scripting-disabled readers still receive the complete model in both languages.
            plain = browser.new_context(java_script_enabled=False, viewport={'width': 390, 'height': 1000})
            for lang in ('en', 'ru'):
                nojs = plain.new_page()
                nojs.goto(base + lang + '/lab/')
                assert nojs.locator('.lab-task:visible').count() == 41
                assert nojs.locator('[data-lab-unit]').count() == 209
                assert not nojs.locator('.lab-controls').is_visible()
                assert nojs.evaluate('document.documentElement.scrollWidth') <= 390
                counts['no_script_editions'] += 1
                nojs.close()
            # Deliberate temporary export proves the new controls also work under file URLs.
            with tempfile.TemporaryDirectory(prefix='aicc-lab-') as temp:
                folder = Path(temp) / 'AI Lab package'
                export(OUTPUT, folder)
                filepage = context.new_page()
                for lang in ('en', 'ru'):
                    filepage.goto((folder / lang / 'lab/index.html').as_uri())
                    assert filepage.locator('.lab-controls').is_visible()
                    interactions(filepage, counts)
                    counts['portable_editions'] += 1
                filepage.close()
            browser.close()
    except Exception as error:
        errors.append(str(error))
    finally:
        server.shutdown()
        server.server_close()
    report = {'counts': dict(counts), 'observations': observations, 'errors': errors}
    (REPORT / 'browser-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
