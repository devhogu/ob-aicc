#!/usr/bin/env python3
"""Exercise the assembled website and a disposable direct-file package in Chromium."""
from collections import Counter
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import sys
import tempfile
import threading
from urllib.parse import parse_qs, urlsplit

from playwright.sync_api import sync_playwright

from export_portable import export

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'html/aicc'
REPORT = ROOT / '.runtime/portal-neighbours'
GROUPS = ['aicc', 'discovery', 'initiatives', 'projects', 'lab']
MEASURE = """() => {
 const visible = e => !!e.getClientRects().length;
 const overlap=[];
 const groups=new Map();
 for(const e of document.querySelectorAll('.discovery-content .card,.discovery-content .scenario-card')){
  if(!visible(e))continue;
  if(!groups.has(e.parentElement))groups.set(e.parentElement,[]);
  groups.get(e.parentElement).push(e);
 }
 for(const group of groups.values())for(let i=0;i<group.length;i++)for(let j=i+1;j<group.length;j++){
  const a=group[i].getBoundingClientRect(),b=group[j].getBoundingClientRect();
  if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>2&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>2)overlap.push([i,j]);
 }
 const chrome=['.o-header','.o-frame','.o-nav','.o-footer'].map(selector=>{
  const e=document.querySelector(selector);if(!e)return null;
  const r=e.getBoundingClientRect(),s=getComputedStyle(e);
  return {x:r.x,width:r.width,padding:s.padding,font:s.fontFamily,size:s.fontSize,line:s.lineHeight};
 });
 return {width:innerWidth,scroll:document.documentElement.scrollWidth,chrome,
  h1:document.querySelectorAll('h1').length,main:document.querySelectorAll('main').length,
  groups:[...document.querySelectorAll('.portal-section-link')].map(e=>e.dataset.section),
  font:getComputedStyle(document.body).fontFamily,
  theme:document.documentElement.dataset.theme,
  brokenImages:[...document.images].filter(e=>!e.complete||!e.naturalWidth).map(e=>e.src),overlap};
}"""


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def check_page_chrome(page, counts):
    """Readers can identify a page, open feedback and reach the common legal pages."""
    lang = page.locator('html').get_attribute('lang')
    assert page.locator('.nav-foot .nav-legal a').count() == 2, 'Missing sidebar legal links'
    assert '2.2' in page.locator('.nav-foot .o-caption').inner_text(), 'Missing site version'
    for container in ('.nav-foot', '.o-footer'):
        for target in ('privacy', 'terms-of-use'):
            link = page.locator(container + f' a[href*="{target}/"]')
            assert link.count() == 1
            assert urlsplit(link.evaluate('e=>e.href')).path.rstrip('/').endswith('/' + lang + '/' + target)
    trigger = page.locator('.o-footer .pagefb')
    assert trigger.count() == 1, 'Missing page feedback control'
    trigger.click()
    dialog = page.locator('#fb')
    assert dialog.is_visible(), 'Feedback dialog did not open'
    ref = dialog.get_attribute('data-ref')
    assert ref and ('ID: ' + ref) in trigger.inner_text()
    title = dialog.get_attribute('data-page')
    mail = urlsplit(dialog.locator('a[data-mail]').get_attribute('href'))
    query = parse_qs(mail.query)
    assert mail.scheme == 'mailto' and mail.path == 'talimbayev@obank.kg'
    assert ref in query['subject'][0]
    assert all(value in query['body'][0] for value in (ref, title, page.url))
    dialog.locator('.fb-copy').click()
    assert dialog.is_visible(), 'Copying the reference closed feedback'
    assert page.evaluate('navigator.clipboard.readText()') == ref
    page.keyboard.press('Escape')
    assert not dialog.is_visible()
    assert trigger.evaluate('e=>document.activeElement===e'), 'Feedback did not restore focus'
    counts['page_feedback_checks'] += 1


def check_existing_aicc(page, base, counts):
    """Exercise the existing document paths through the new common shell."""
    page.set_viewport_size({'width': 1440, 'height': 1000})
    page.context.grant_permissions(['clipboard-read', 'clipboard-write'])
    for lang in ('en', 'ru'):
        page.goto(base + lang + '/')
        page.locator('#q').fill('Operating Model' if lang == 'en' else 'Операционная модель')
        result = page.locator('#results a').first
        result.wait_for()
        assert '/discovery/' not in result.get_attribute('href')
        result.click()
        assert page.locator('body').get_attribute('data-portal-section') == 'aicc'
        page.goto(base + lang + '/delivery/')
        trigger = page.locator('.dz-open').first
        trigger.click()
        assert page.locator('#dz').is_visible()
        assert page.locator('#dz svg').count() > 0
        page.keyboard.press('Escape')
        page.locator('#dz').wait_for(state='detached')
        assert trigger.evaluate('e=>document.activeElement===e')
        page.goto(base + lang + '/knowledge-base/initiative-brief/')
        copy = page.locator('[data-copy]').first
        expected = page.locator('#' + copy.get_attribute('data-copy')).text_content()
        copy.click()
        assert page.evaluate('navigator.clipboard.readText()') == expected
        counts['aicc_interactions'] += 3


def check_workflow_stage_links(page, overview, counts, *, all_stages=False):
    """A stage link opens that stage's source content, on HTTP and file URLs."""
    source = (ROOT / 'html-alt/financial-services/en/value-streams/index.html').read_text()
    catalogue = json.loads(re.search(r'const FLOW_STAGES = (.*?);\n', source)[1])
    expected = [(flow, stage) for flow, stages in catalogue.items() for stage in stages]
    page.goto(overview)
    card = page.locator('[data-ui-pattern=workflows]')
    assert card.locator('.workflow-preview').count() == 11
    assert not card.locator('input[name="workflow-view"],.workflow-count-note,.workflow-explore').count()
    links = card.locator('.workflow-preview__stages a').evaluate_all(
        'els=>els.map(e=>({href:e.getAttribute("href"),label:e.textContent.trim()}))')
    assert len(links) == len(expected) == 56
    assert [link['label'] for link in links] == [stage['label'] for _, stage in expected]
    cases = list(zip(links, expected)) if all_stages else [(links[1], expected[1])]
    for link, (flow, stage) in cases:
        page.goto(overview)
        anchor = page.locator('.workflow-preview__stages a[href="' + link['href'] + '"]')
        preview = anchor.locator('xpath=ancestor::details')
        if not preview.evaluate('e=>e.open'):
            preview.locator(':scope > summary').click()
        anchor.focus()
        page.keyboard.press('Enter')
        page.wait_for_url(lambda url: urlsplit(url).path.endswith('/value-streams/index.html') and bool(urlsplit(url).fragment))
        modal = page.locator('#stageModal')
        assert modal.get_attribute('aria-hidden') == 'false'
        assert modal.locator('.modal__title').inner_text() == stage['title']
        assert modal.locator('.modal__intent').inner_text() == stage['intent']
        assert modal.locator('.modal__problem p').inner_text() == stage['problem']
        button = page.locator('.flow-stages__stage[data-flow-id="' + flow + '"][data-stage="' + stage['slug'] + '"]')
        assert button.locator('xpath=ancestor::details').evaluate('e=>e.open')
        assert modal.locator('.modal__close').evaluate('e=>document.activeElement===e')
        page.keyboard.press('Escape')
        assert modal.get_attribute('aria-hidden') == 'true'
        assert button.evaluate('e=>document.activeElement===e')
        counts['workflow_stage_links'] += 1
    # Refresh and same-page fragment navigation preserve the chosen stage.
    page.reload()
    assert page.locator('#stageModal').get_attribute('aria-hidden') == 'false'
    assert page.locator('#stageModal .modal__title').inner_text() == cases[-1][1][1]['title']
    page.keyboard.press('Escape')
    page.evaluate('location.hash="stage-deposits-transaction-banking--transact"')
    page.wait_for_function('document.querySelector("#stageModal").getAttribute("aria-hidden")==="false"')
    assert page.locator('#stageModal .modal__title').inner_text() == 'Day-to-day payment and transfer execution'
    page.goto(overview)


def main():
    REPORT.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Quiet, directory=str(OUTPUT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{server.server_port}/'
    counts, errors = Counter(), []
    pages = []
    for lang in ('en', 'ru'):
        for section in GROUPS[1:]:
            pages += [p.relative_to(OUTPUT).as_posix() for p in sorted((OUTPUT / lang / section).rglob('index.html'))]
        pages += [f'{lang}/index.html', f'{lang}/responsible-ai/ai-policy/index.html'] if (OUTPUT / lang / 'responsible-ai/ai-policy/index.html').exists() else [f'{lang}/index.html']
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(viewport={'width': 1440, 'height': 1000})
            context.grant_permissions(['clipboard-read', 'clipboard-write'])
            page = context.new_page()
            page.on('pageerror', lambda e: errors.append('JavaScript: ' + str(e)))
            page.on('response', lambda r: errors.append(f'HTTP {r.status}: {r.url}') if r.status >= 400 else None)
            page.on('requestfailed', lambda r: errors.append('Request: ' + r.url + ': ' + str(r.failure)))
            page.goto(base + 'en/')
            for width, theme in ((1440, 'light'), (390, 'light'), (1440, 'dark'), (390, 'dark')):
                page.set_viewport_size({'width': width, 'height': 1000})
                page.evaluate('(t)=>localStorage.setItem("aicc-theme",t)', theme)
                baseline_chrome = {}
                for lang in ('en', 'ru'):
                    page.goto(base + lang + '/', wait_until='load')
                    page.evaluate('document.fonts.ready')
                    baseline_chrome[lang] = page.evaluate(MEASURE)['chrome']
                for route in pages:
                    page.goto(base + route, wait_until='load')
                    page.evaluate('document.fonts.ready')
                    state = page.evaluate(MEASURE)
                    counts['page_views'] += 1
                    problems = []
                    if state['scroll'] > width + 1:
                        problems.append(f'overflow {state["scroll"]}')
                    if state['h1'] != 1 or state['main'] != 1 or state['groups'] != GROUPS:
                        problems.append('landmarks/navigation')
                    if 'Golos Text' not in state['font'] or state['theme'] != theme:
                        problems.append('font/theme')
                    if state['brokenImages'] or state['overlap']:
                        problems.append('images/card overlap')
                    if state['chrome'] != baseline_chrome[route.split('/')[0]]:
                        problems.append('page framework differs from AICC')
                    if page.locator('.nav-foot').count() != 1 or page.locator('.o-footer .pagefb').count() != 1 or page.locator('#fb').count() != 1:
                        problems.append('sidebar/footer/feedback')
                    if problems:
                        errors.append(f'{width}/{theme} {route}: {", ".join(problems)}')
                    if route == 'en/discovery/index.html':
                        check_workflow_stage_links(page, base + route, counts, all_stages=width == 1440 and theme == 'light')
                    if width == 1440 and theme == 'light' and '/discovery/' in route:
                        disclosures = page.locator('.discovery-content details')
                        counts['disclosures_toggled'] += disclosures.count()
                        if disclosures.count():
                            summary = disclosures.first.locator(':scope > summary')
                            was_open = disclosures.first.evaluate('e=>e.open')
                            summary.click()
                            if disclosures.first.evaluate('e=>e.open') == was_open:
                                errors.append('Disclosure did not toggle: ' + route)
                            # Expand all retained disclosures and check the resulting layout.
                            disclosures.evaluate_all('elements=>elements.forEach(e=>e.open=true)')
                            if page.evaluate('document.documentElement.scrollWidth') > width + 1:
                                errors.append('Expanded overflow: ' + route)
                        for tab in page.locator('.problems-tab-label').all():
                            identifier = tab.get_attribute('for')
                            tab.click()
                            selected = page.locator('#' + identifier).is_checked()
                            panel = page.locator('#' + identifier.replace('problems-tab-', 'problems-panel-'))
                            if not selected or not panel.is_visible():
                                errors.append('Tab did not select panel: ' + route + ' ' + identifier)
                            counts['tabs_clicked'] += 1
                        for button in page.locator('.flow-stages__stage').all():
                            button.click()
                            modal = page.locator('#stageModal')
                            if modal.get_attribute('aria-hidden') != 'false' or not modal.locator('.modal__title').inner_text().strip():
                                errors.append('Modal did not open: ' + route)
                            page.keyboard.press('Tab')
                            if not modal.locator('.modal__close').evaluate('e=>document.activeElement===e'):
                                errors.append('Modal focus escaped: ' + route)
                            page.keyboard.press('Escape')
                            if modal.get_attribute('aria-hidden') != 'true' or not button.evaluate('e=>document.activeElement===e'):
                                errors.append('Modal close/focus: ' + route)
                            counts['stages_clicked'] += 1
                    if route in {f'{lang}/{section}index.html' for lang in ('en', 'ru') for section in ('', 'discovery/', 'initiatives/', 'projects/', 'lab/', 'discovery/shared-banking-capabilities/customer-servicing/')}:
                        check_page_chrome(page, counts)
                    if route in ('en/discovery/index.html', 'ru/discovery/index.html', 'en/projects/index.html', 'ru/initiatives/register/index.html', 'en/lab/index.html'):
                        page.screenshot(path=str(REPORT / f'{route.replace("/", "-")}-{width}-{theme}.png'))
                print(f'Checked {width}px {theme}: {len(pages)} pages', flush=True)
            # Visit all neighbours using the real common navigation, then the counterpart page.
            page.set_viewport_size({'width': 1440, 'height': 1000})
            page.goto(base + 'en/')
            for section in GROUPS[1:] + ['aicc']:
                page.locator(f'.portal-section-link[data-section="{section}"]').click()
                if page.locator('body').get_attribute('data-portal-section') != section:
                    errors.append('Section switch failed: ' + section)
                counts['section_switches'] += 1
            page.goto(base + 'en/discovery/shared-banking-capabilities/customer-servicing/')
            page.locator('.lang-switch a[lang="ru"]').click()
            if '/ru/discovery/shared-banking-capabilities/customer-servicing/' not in page.url:
                errors.append('Counterpart switch failed')
            page.set_viewport_size({'width': 390, 'height': 900})
            page.reload()
            if page.locator('.o-nav>details').evaluate('e=>e.open'):
                errors.append('Mobile menu starts expanded')
            page.locator('.o-nav>details>summary').click()
            page.locator('.portal-section-link[data-section="projects"]').click()
            if page.locator('body').get_attribute('data-portal-section') != 'projects':
                errors.append('Mobile section switch failed')
            # Search must find a scenario, open its disclosure and stay inside Discovery.
            page.goto(base + 'en/discovery/')
            page.locator('#q').fill('Frontline Service Copilot')
            result = page.locator('#results a').filter(has_text='Frontline Service Copilot').first
            result.wait_for()
            result.click()
            if '/en/discovery/' not in page.url or not page.locator('#scenario-frontline-service-copilot').evaluate('e=>e.open'):
                errors.append('Discovery search/deep link failed')
            page.goto(base + 'en/initiatives/')
            page.locator('#q').fill('Frontline Service Copilot')
            page.locator('#results').wait_for(state='visible')
            if page.locator('#results a').count():
                errors.append('Search crossed section boundary')
            counts['scoped_search_checks'] += 2
            check_existing_aicc(page, base, counts)
            # Direct-file test uses an isolated output and never refreshes portal/published.
            with tempfile.TemporaryDirectory(prefix='aicc-neighbours-') as temp:
                folder = Path(temp) / 'Портал AICC'
                manifest = export(OUTPUT, folder)
                filepage = context.new_page()
                filepage.on('pageerror', lambda e: errors.append('File JavaScript: ' + str(e)))
                network = []
                filepage.on('request', lambda r: network.append(r.url) if r.url.startswith(('http:', 'https:')) else None)
                check_workflow_stage_links(filepage, (folder / 'en/discovery/index.html').as_uri(), counts)
                filepage.locator('#q').fill('Frontline Service Copilot')
                filepage.locator('#results a').filter(has_text='Frontline Service Copilot').first.click()
                if not filepage.locator('#scenario-frontline-service-copilot').evaluate('e=>e.open'):
                    errors.append('Portable scenario search failed')
                filepage.locator('.lang-switch a[lang="ru"]').click()
                filepage.locator('.portal-section-link[data-section="projects"]').click()
                if '/ru/projects/index.html' not in filepage.url:
                    errors.append('Portable section/language navigation failed')
                if network:
                    errors.append('Portable external requests: ' + str(network))
                counts['portable_pages_validated'] = manifest['html_pages']
                filepage.close()
            browser.close()
    except Exception as exc:
        errors.append(str(exc))
    finally:
        server.shutdown()
    result = {'counts': dict(counts), 'errors': errors}
    (REPORT / 'browser-report.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
