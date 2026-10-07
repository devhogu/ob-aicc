#!/usr/bin/env python3
"""Exercise actual Program Backlog, Portfolio and project paths, including file output."""
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import json
import os
from pathlib import Path
import tempfile
import threading
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright
from check_lab_browser import contrast
from export_portable import export
import workspace

ROOT=workspace.ROOT;OUTPUT=ROOT/'html/aicc';REPORT=ROOT/'.runtime/delivery'


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass


def main():
    REPORT.mkdir(parents=True,exist_ok=True)
    server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(OUTPUT)))
    threading.Thread(target=server.serve_forever,daemon=True).start()
    base=os.environ.get('DELIVERY_BASE',f'http://127.0.0.1:{server.server_port}/').rstrip('/')+'/'
    errors=[];views=[];paths=0
    try:
        with sync_playwright() as pw:
            browser=pw.chromium.launch(headless=True);context=browser.new_context();page=context.new_page()
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.on('response',lambda r:errors.append(f'{r.status} {r.url}') if r.status>=400 else None)
            for lang in ('en','ru'):
                for width in (1440,900,390,320):
                    page.set_viewport_size({'width':width,'height':1000})
                    for theme in ('light','dark'):
                        page.goto(base+lang+'/program/')
                        page.evaluate('t=>{localStorage.setItem("aicc-theme",t);document.documentElement.dataset.theme=t}',theme);page.evaluate('document.fonts.ready')
                        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(lang,width,theme)
                        assert page.locator('.dl-content').evaluate('e=>getComputedStyle(e).fontFamily').startswith('"Golos Text"')
                        assert page.locator('.dl-board thead th').count()==6
                        assert page.locator('.dl-board tbody tr').count()==3
                        assert page.locator('.dl-board .dl-card').count()==0
                        colors=page.locator('.dl-proposal').first.evaluate('e=>({fg:getComputedStyle(e).color,bg:getComputedStyle(e).backgroundColor})')
                        assert contrast(colors['fg'],colors['bg'])>=4.5
                        page.locator('[data-dl-tab=intake]').click()
                        assert page.locator('[data-dl-item]:visible').count()==7
                        page.locator('[data-dl-priority]').select_option('PRI-1')
                        assert page.locator('[data-dl-item]:visible').count()==2
                        page.locator('[data-dl-priority]').select_option('')
                        page.locator('[data-dl-search]').fill('INI-013');assert page.locator('[data-dl-item]:visible').count()==1
                        page.locator('[data-dl-search]').fill('unmatched-xyz');assert page.locator('[data-dl-item]:visible').count()==0
                        assert page.locator('[data-dl-count]').inner_text().endswith(': 0')
                        page.locator('[data-dl-search]').fill('')
                        page.locator('[data-dl-tab=intake]').focus();page.keyboard.press('ArrowRight')
                        assert page.locator('#documents').is_visible()
                        assert page.locator('.dl-documents a:visible').count()==12
                        page.locator('[data-dl-tab=board]').click()
                        page.locator('#board .dl-proposal a[href*="ini-013"]').click()
                        assert '/portfolio/ini-013/' in page.url
                        assert not page.locator('.pf-notice').count()
                        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                        page.locator('.pf-detail-page a[href$="/program/service-resolution/"]').click()
                        assert '/program/service-resolution/' in page.url
                        assert page.locator('.project-content a[href*="ini-013"]').count()==1
                        page.locator('.project-content a[href*="#intake"]').click()
                        assert page.locator('#intake').is_visible()
                        page.locator('[data-dl-tab=board]').click()
                        if width in (1440,390):page.screenshot(path=str(REPORT/f'{lang}-{width}-{theme}.png'),full_page=True)
                        views.append({'lang':lang,'width':width,'theme':theme,'contrast':round(contrast(colors['fg'],colors['bg']),2)});paths+=1
                page.goto(base+lang+'/program/');page.locator('#q').fill('INI-013');page.wait_for_timeout(400)
                assert page.locator('#results a[href*="program"]').count()>0
                assert not page.locator('#results a[href*="portfolio"]').count()
                counterpart=page.locator('.o-lang a',has_text='EN' if lang=='ru' else 'RU')
                if not counterpart.count():counterpart=page.locator('a[href*="/'+('en' if lang=='ru' else 'ru')+'/program/"]').first
                counterpart.click();assert '/'+('en' if lang=='ru' else 'ru')+'/program/' in page.url
                nojs=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':1000});reader=nojs.new_page();reader.goto(base+lang+'/program/')
                assert reader.locator('[data-dl-panel]:visible').count()==3
                assert reader.locator('[data-dl-item]:visible').count()==7
                reader.locator('#board a[href*="ini-013"]').click();assert '/portfolio/ini-013/' in reader.url
                nojs.close()
            with tempfile.TemporaryDirectory() as tmp:
                package=Path(tmp)/'aicc';export(OUTPUT,package);file_context=browser.new_context(viewport={'width':1000,'height':1000});file_page=file_context.new_page()
                for lang in ('en','ru'):
                    file_page.goto((package/lang/'program/index.html').as_uri())
                    file_page.locator('[data-dl-tab=documents]').click();file_page.locator('.dl-documents a').first.click()
                    assert '/program/service-resolution/index.html' in urlsplit(file_page.url).path
                    file_page.locator('.project-content a[href*="ini-013"]').click()
                    assert '/portfolio/ini-013/index.html' in urlsplit(file_page.url).path
                file_context.close()
            browser.close()
    finally:server.shutdown()
    (REPORT/'browser-report.json').write_text(json.dumps({'base':base,'paths':paths,'views':views,'errors':errors},indent=2))
    print(json.dumps({'paths':paths,'views':len(views),'errors':errors}));assert not errors


if __name__=='__main__':main()
