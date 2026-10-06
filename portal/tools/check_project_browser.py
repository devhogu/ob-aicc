#!/usr/bin/env python3
"""Exercise complete project reading paths and diagram controls in real Chromium."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import tempfile
import threading
from urllib.parse import urlsplit

from playwright.sync_api import sync_playwright, expect

from check_project import DOCUMENTS
from export_portable import export

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'html/aicc'
REPORT = ROOT / '.runtime/project'


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args): pass


MEASURE = """() => ({width:innerWidth,scroll:document.documentElement.scrollWidth,
 fonts:[...document.querySelectorAll('.project-content h1,.project-content h2,.project-content>section p')].map(e=>getComputedStyle(e).fontFamily),
 clipped:[...document.querySelectorAll('.project-content .project-card,.project-content .audience-card,.project-content .value-step')].filter(e=>e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2).map(e=>e.textContent.slice(0,60)),
 tableScroll:[...document.querySelectorAll('.project-content .table-wrap')].every(e=>e.scrollWidth<=e.clientWidth+2||getComputedStyle(e).overflowX==='auto'),
 theme:document.documentElement.dataset.theme})"""


def diagram_controls(page, counts, every=False):
    triggers = page.locator('.project-diagram-open')
    for number in range(triggers.count() if every else min(1, triggers.count())):
        b = triggers.nth(number); b.scroll_into_view_if_needed(); b.focus(); page.keyboard.press('Enter')
        dialog = page.locator('.project-viewer'); expect(dialog).to_be_visible()
        assert dialog.locator('svg').count() == 1
        assert page.locator('.project-content svg').count() == triggers.count()-1
        assert page.evaluate("document.querySelectorAll('[id]').length===new Set([...document.querySelectorAll('[id]')].map(e=>e.id)).size"), 'Duplicate SVG IDs in modal'
        output=dialog.locator('output'); initial=output.inner_text()
        dialog.locator('[data-project-action=in]').click(); assert output.inner_text()!=initial
        dialog.locator('[data-project-action=actual]').click(); assert output.inner_text()=='100%'
        viewport=dialog.locator('.project-viewer-viewport')
        viewport.evaluate('e=>{e.scrollLeft=e.scrollWidth;e.scrollTop=e.scrollHeight}')
        extent=viewport.evaluate('e=>({width:e.clientWidth,scroll:e.scrollWidth,x:e.scrollLeft})')
        if extent['scroll']>extent['width']+2: assert extent['x']>0
        dialog.locator('[data-project-action=out]').click(); assert output.inner_text()=='75%'
        viewport.focus(); page.keyboard.press('+'); assert output.inner_text()=='100%'
        page.keyboard.press('-'); assert output.inner_text()=='75%'
        dialog.locator('[data-project-action=fit]').click()
        fit=viewport.evaluate('e=>({w:e.clientWidth,h:e.clientHeight,sw:e.scrollWidth,sh:e.scrollHeight})')
        assert fit['sw']<=fit['w']+10 and fit['sh']<=fit['h']+10, ('Fit failed',fit)
        page.keyboard.press('Escape'); expect(dialog).not_to_be_visible(); expect(b).to_be_focused()
        expect(page.locator('.project-content svg')).to_have_count(triggers.count())
        assert b.get_attribute('aria-expanded')=='false'
        counts['diagram_controls']+=1
    if triggers.count():
        b=triggers.first;b.click();page.locator('[data-project-action=close]').click();expect(b).to_be_focused()
        counts['close_buttons']+=1


def run():
    REPORT.mkdir(parents=True,exist_ok=True)
    counts={'page_views':0,'diagram_controls':0,'close_buttons':0,'feedback_checks':0,'search_checks':0,'no_script_pages':0,'portable_pages':0}
    errors=[]; network=[]
    server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(OUTPUT)))
    threading.Thread(target=server.serve_forever,daemon=True).start()
    base=f'http://127.0.0.1:{server.server_address[1]}'
    try:
        with sync_playwright() as playwright:
            browser=playwright.chromium.launch()
            page=browser.new_page()
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.on('requestfailed',lambda r:network.append(r.url))
            page.goto(base+'/en/projects/service-resolution/')
            for theme in ('light','dark'):
                page.evaluate('t=>localStorage.setItem("aicc-theme",t)',theme)
                for width in (1440,390):
                    page.set_viewport_size({'width':width,'height':1000})
                    for lang in ('en','ru'):
                        for source,route in DOCUMENTS:
                            url=f'/{lang}/projects/service-resolution/'+(route+'/' if route else '')
                            page.goto(base+url,wait_until='networkidle')
                            state=page.evaluate(MEASURE)
                            assert state['scroll']<=width+1, (url,width,theme,'Page overflow',state)
                            assert not state['clipped'], (url,width,theme,'Clipped cards',state)
                            assert state['tableScroll'] and state['theme']==theme
                            assert all('Golos' in f or 'TTNorms' in f for f in state['fonts'])
                            assert page.locator('h1').count()==1 and page.locator('.o-footer .pagefb').count()==1
                            diagram_controls(page,counts,every=True)
                            page.locator('.o-footer .pagefb').click();expect(page.locator('#fb')).to_be_visible();page.keyboard.press('Escape')
                            counts['feedback_checks']+=1;counts['page_views']+=1
                            if source in ('start','charter','technical-design'):
                                page.evaluate('scrollTo(0,0)');page.screenshot(path=str(REPORT/f'{lang}-{source}-{width}-{theme}.png'))
                        # Native document contents must be discoverable on desktop and mobile.
                        page.goto(base+f'/{lang}/projects/service-resolution/charter/')
                        if width<=1100: page.locator('.o-nav>details>summary').click()
                        contents=page.locator('.project-nav-topics>summary');expect(contents).to_be_visible();contents.click()
                        first=page.locator('.project-nav-topics a').first;first.click()
                        assert urlsplit(page.url).fragment.startswith(lang+'-charter-')
                        counts['section_links']=counts.get('section_links',0)+1
                        # A source reference reaches another document, rather than an absent fragment.
                        page.goto(base+f'/{lang}/projects/service-resolution/charter/')
                        page.locator(f'.project-content a[href="../journeys/#{lang}-journeys"]').first.click()
                        assert page.url.endswith('/journeys/#'+lang+'-journeys')
                        page.locator('.lang-switch a[lang="'+('ru' if lang=='en' else 'en')+'"]').click()
                        assert ('/ru/' if lang=='en' else '/en/') in page.url and '/journeys/' in page.url
                        print(f'Checked project {lang}, {width}px, {theme}',flush=True)
            for width in (320,768):
                page.set_viewport_size({'width':width,'height':1000})
                for lang in ('en','ru'):
                    for theme in ('light','dark'):
                        page.evaluate('t=>localStorage.setItem("aicc-theme",t)',theme)
                        page.goto(base+f'/{lang}/projects/service-resolution/technical-design/',wait_until='networkidle')
                        assert page.evaluate(MEASURE)['scroll']<=width+1
                        diagram_controls(page,counts);counts['page_views']+=1
            for lang in ('en','ru'):
                page.goto(base+f'/{lang}/projects/')
                page.locator('#q').fill('Functions and who uses them' if lang=='en' else 'Функции и их пользователи')
                result=page.locator('#results a').first;expect(result).to_be_visible();result.click()
                assert '/projects/service-resolution/' in page.url
                counts['search_checks']+=1
                nojs=browser.new_page(java_script_enabled=False)
                for source,route in DOCUMENTS:
                    nojs.goto(base+f'/{lang}/projects/service-resolution/'+(route+'/' if route else ''))
                    assert nojs.locator('[data-document]').count()==1 and nojs.locator('h1').is_visible()
                    assert not nojs.locator('.project-diagram-open:visible').count()
                    if nojs.locator('.project-diagram-preview').count():
                        region=nojs.locator('.project-diagram-preview').first
                        region.focus()
                        extent=region.evaluate('e=>{e.scrollLeft=e.scrollWidth;return {w:e.clientWidth,sw:e.scrollWidth,x:e.scrollLeft}}')
                        if extent['sw']>extent['w']+2: assert extent['x']>0
                    counts['no_script_pages']+=1
                nojs.close()
            # Reuse the actual portable packager; never modify portal/published.
            with tempfile.TemporaryDirectory(prefix='aicc-project-') as temp:
                target=Path(temp)/'portable';export(OUTPUT,target)
                filepage=browser.new_page()
                for lang in ('en','ru'):
                    for source,route in DOCUMENTS:
                        file=filepage.goto((target/lang/'projects/service-resolution'/route/'index.html').as_uri(),wait_until='networkidle')
                        diagram_controls(filepage,counts)
                        counts['portable_pages']+=1
                    filepage.goto((target/lang/'projects/service-resolution/index.html').as_uri())
                    filepage.locator('.project-content .audience-card').first.click()
                    filepage.wait_for_url(lambda u: urlsplit(u).path.endswith('/journeys/payment-issue/index.html') and urlsplit(u).fragment==lang+'-journey-payment')
                    filepage.locator('#q').fill('Hypothesis' if lang=='en' else 'Гипотеза')
                    result=filepage.locator('#results a').first;expect(result).to_be_visible();result.click()
                    assert '/projects/service-resolution/' in filepage.url
                    counts['search_checks']+=1
                filepage.close()
            browser.close()
    except Exception as error:
        errors.append(str(error) or repr(error))
        raise
    finally:
        server.shutdown()
        report={'counts':counts,'errors':errors,'failed_requests':network}
        (REPORT/'browser-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps(report,ensure_ascii=False,indent=2))
    assert not errors and not network


if __name__=='__main__':run()
