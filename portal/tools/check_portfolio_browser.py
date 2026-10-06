#!/usr/bin/env python3
"""Exercise published portfolio tasks in both editions/themes and direct-file output."""
from collections import Counter
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import tempfile
import threading
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright
from export_portable import export
from check_lab_browser import contrast
import portfolio

OUTPUT=portfolio.workspace.ROOT/'html/aicc'
REPORT=portfolio.workspace.ROOT/'.runtime/portfolio'


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass


def interactions(page,lang,counts):
    assert page.locator('#board:visible [data-pf-item]').count()==7
    assert page.locator('.pf-column').count()==7
    page.locator('[data-pf-priority]').select_option('PRI-2')
    assert page.locator('#board [data-pf-item]:visible').count()==1
    assert page.locator('[data-pf-visible]').inner_text().endswith(': 1')
    page.locator('#board [data-pf-open="INI-004"]').click()
    dialog=page.locator('.pf-dialog')
    assert dialog.is_visible()
    assert 'INI-004' in dialog.inner_text()
    assert 'DR-2026-061' in dialog.inner_text()
    assert ('Not recorded' if lang=='en' else 'Не указано') in dialog.inner_text()
    assert urlsplit(dialog.locator('.pf-full-link').get_attribute('href')).path.endswith(('/ini-004/','/ini-004/index.html'))
    page.keyboard.press('Escape');assert not dialog.is_visible()
    assert page.locator('#board [data-pf-open="INI-004"]').evaluate('e=>e===document.activeElement')
    page.locator('[data-pf-priority]').select_option('')
    page.locator('[data-pf-search]').fill('INI-007')
    assert page.locator('#board [data-pf-item]:visible').count()==1
    page.locator('[data-pf-tab="review"]').click()
    assert page.locator('#review [data-pf-item]:visible').count()==1
    page.locator('[data-pf-search]').fill('unmatched-xyz')
    assert page.locator('.pf-review-empty').is_visible()
    page.locator('[data-pf-search]').fill('')
    page.locator('[data-pf-tab="standing"]').click()
    assert page.locator('#standing [data-pf-item]:visible').count()==4
    assert not page.locator('.pf-filter').is_visible()
    page.locator('[data-pf-tab="standing"]').focus();page.keyboard.press('ArrowRight')
    assert page.locator('#roadmap').is_visible()
    assert page.locator('#roadmap li').count()==13
    page.locator('[data-pf-tab="board"]').click()
    counts['interactive_paths']+=1


def main():
    REPORT.mkdir(parents=True,exist_ok=True)
    server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(OUTPUT)))
    threading.Thread(target=server.serve_forever,daemon=True).start()
    base=os.environ.get('PORTFOLIO_BASE',f'http://127.0.0.1:{server.server_port}/').rstrip('/')+'/'
    counts=Counter();errors=[];views=[]
    try:
        with sync_playwright() as pw:
            browser=pw.chromium.launch(headless=True)
            context=browser.new_context(viewport={'width':1440,'height':1000})
            page=context.new_page()
            page.on('pageerror',lambda error:errors.append(str(error)))
            page.on('requestfailed',lambda request:errors.append(str(request.failure)))
            page.on('response',lambda response:errors.append(f'{response.status} {response.url}') if response.status>=400 else None)
            for lang in ('en','ru'):
                for width in (1440,900,390,320):
                    page.set_viewport_size({'width':width,'height':1000})
                    for theme in ('light','dark'):
                        page.goto(base+lang+'/initiatives/')
                        page.evaluate('t=>{localStorage.setItem("aicc-theme",t);document.documentElement.dataset.theme=t}',theme)
                        page.evaluate('document.fonts.ready');
                        assert page.evaluate('document.documentElement.scrollWidth')<=width
                        assert page.locator('.pf-content').evaluate('e=>getComputedStyle(e).fontFamily').startswith('"Golos Text"')
                        colors=page.locator('.pf-content').evaluate('e=>({fg:getComputedStyle(e).color,bg:getComputedStyle(document.querySelector(".pf-card")).backgroundColor})')
                        assert contrast(colors['fg'],colors['bg'])>=4.5
                        interactions(page,lang,counts)
                        for identifier in [x['id'] for x in portfolio.project(lang=lang)['items']]:
                            page.goto(base+lang+'/initiatives/'+identifier.lower()+'/')
                            assert page.evaluate('document.documentElement.scrollWidth')<=width
                            assert page.locator('.pf-content header').is_visible()
                            counts['summary_views']+=1
                        for route in ('register/','selection/'):
                            page.goto(base+lang+'/initiatives/'+route)
                            assert page.evaluate('document.documentElement.scrollWidth')<=width
                            counts['register_workflow_views']+=1
                        page.goto(base+lang+'/initiatives/')
                        if width in (1440,390):page.screenshot(path=str(REPORT/f'{lang}-{width}-{theme}.png'),full_page=True)
                        views.append({'language':lang,'width':width,'theme':theme,'contrast':round(contrast(colors['fg'],colors['bg']),2)})
                page.set_viewport_size({'width':1440,'height':1000});page.goto(base+lang+'/initiatives/')
                page.locator('#q').fill('INI-004')
                # Use the shared section search results, never a board card as a fallback.
                page.wait_for_timeout(400)
                assert page.locator('#results a[href*="ini-004"]').count()>0
                page.locator('#results a[href*="ini-004"]').first.click()
                assert '/initiatives/ini-004/' in page.url
                page.locator('.lang-switch a').filter(has_text='RU' if lang=='en' else 'EN').click()
                assert ('ru/' if lang=='en' else 'en/')+'initiatives/ini-004/' in page.url
                counts['search_counterpart_paths']+=1
            plain=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':1000})
            for lang in ('en','ru'):
                nojs=plain.new_page();nojs.goto(base+lang+'/initiatives/')
                assert nojs.locator('[data-pf-panel]:visible').count()==4
                assert nojs.locator('[data-pf-item]:visible').count()==18
                assert not nojs.locator('.pf-filter').is_visible()
                nojs.locator('[data-pf-open="INI-004"]').first.click()
                assert nojs.locator('.pf-detail-page').is_visible()
                assert nojs.evaluate('document.documentElement.scrollWidth')<=390
                counts['no_script_paths']+=1;nojs.close()
            if not os.environ.get('PORTFOLIO_BASE'):
                with tempfile.TemporaryDirectory(prefix='aicc-portfolio-') as tmp:
                    folder=Path(tmp)/'Portfolio package';export(OUTPUT,folder)
                    for lang in ('en','ru'):
                        page.goto((folder/lang/'initiatives/index.html').as_uri())
                        interactions(page,lang,counts)
                        page.locator('#board [data-pf-open="INI-004"]').click()
                        page.locator('.pf-full-link').click()
                        assert page.locator('.pf-detail-page').is_visible()
                        counts['portable_paths']+=1
            assert not errors,errors
            browser.close()
    except Exception as error:
        errors.append(str(error));raise
    finally:
        server.shutdown();server.server_close()
        (REPORT/'browser-report.json').write_text(json.dumps({'base':base,'counts':counts,'views':views,'errors':errors},ensure_ascii=False,indent=2))
    print(json.dumps({'counts':counts,'views':len(views),'errors':errors},ensure_ascii=False))


if __name__=='__main__':main()
