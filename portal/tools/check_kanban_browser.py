#!/usr/bin/env python3
"""Exercise shared selection on real Portfolio and nonempty Delivery consumers."""
from collections import Counter
from copy import deepcopy
from functools import partial
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import shutil
import tempfile
import threading
from playwright.sync_api import sync_playwright
from check_delivery_browser import Quiet
from check_lab_browser import contrast
from export_portable import export
import delivery
import kanban
import portfolio
import workspace

REPORT=workspace.ROOT/'.runtime/kanban'


def fixture(output,lang):
    data=delivery.project(lang=lang)
    rows=[]
    for identifier,state,lane,rank in [('FEAT-901','Waiting','Normal','1'),('FEAT-902','Approved','High priority','2')]:
        rows.append({'Identifier':identifier,'Feature':'Source-linked case history' if identifier=='FEAT-901' else 'Approved analysis request','Parent: Capability or Standing Initiative':'INI-009','Lane':lane,'State':state,'Stage':'Develop' if state=='Waiting' else '', 'Rank':rank,'Acceptance criteria and Dependencies':'Given a permitted case, show source-linked history; DEP-014','Data-use approval reference':'No AI use in this fixture','Approved by and date':'2026-10-06','Accepted by and date':'','Waiting from':'Active' if state=='Waiting' else '', 'Waiting Dependency':'DEP-014' if state=='Waiting' else ''})
    data['items']=delivery.validate([],rows,data['portfolio']['items'],data['dependencies'])
    for row in data['items']:
        row.update(title=row['Feature'] if lang=='en' else ('История обращения с источниками' if row['Identifier']=='FEAT-901' else 'Одобренный запрос на анализ'),status=row['State'] if lang=='en' else ('Ожидание' if row['State']=='Waiting' else 'Одобрено'),stage_label=row['Stage'],rank=int(row['Rank']),criteria=row['Acceptance criteria and Dependencies'],approval='2026-10-06',accepted='')
    data['counts']={'Backlog':0,'Ready':1,'Active':1,'Review':0,'Done':0}
    data['portfolio']['capacity']['feature']={'progress':1,'ready':1}
    for url,item in [(f'/{lang}/program/',None)]+[(f'/{lang}/program/items/{r["Identifier"].lower()}/',r) for r in data['items']]:
        body=delivery.render(data,url,item)
        page=workspace.page(url,lang,'program','Delivery fixture',body,'',body_class='delivery-workspace')
        page=page.replace('</head>',f'<link rel="stylesheet" href="{workspace.asset(url,"delivery.css")}"><script defer src="{workspace.asset(url,"delivery.js")}"></script>'+kanban.assets(url)+'</head>',1)
        target=output/url.strip('/')/'index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(page)


def inspect(page,first,second,close,counts):
    one=page.locator(first);two=page.locator(second);pane=page.locator('[data-kb-panel]:visible')
    assert pane.count()==0
    one.focus();page.keyboard.press('Enter')
    assert pane.count()==1
    assert one.get_attribute('aria-expanded')=='true'
    assert pane.locator('h2').evaluate('e=>e===document.activeElement')
    assert pane.locator('[data-kb-identity]').inner_text()==one.get_attribute('data-kb-open')
    page.keyboard.press('Escape')
    assert pane.count()==0 and one.evaluate('e=>e===document.activeElement')
    one.click();two.click()
    assert pane.count()==1
    assert pane.locator('[data-kb-identity]').inner_text()==two.get_attribute('data-kb-open')
    assert one.get_attribute('aria-expanded')=='false'
    page.locator(close).click()
    assert pane.count()==0 and two.evaluate('e=>e===document.activeElement')
    counts['selection_replacement_focus']+=1


def main():
    REPORT.mkdir(parents=True,exist_ok=True);counts=Counter();errors=[];views=[]
    with tempfile.TemporaryDirectory(prefix='aicc-kanban-') as tmp:
        output=Path(tmp)/'site';shutil.copytree(workspace.ROOT/'html/aicc',output)
        for lang in ('en','ru'):fixture(output,lang)
        server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(output)))
        threading.Thread(target=server.serve_forever,daemon=True).start();base=f'http://127.0.0.1:{server.server_port}/'
        try:
            with sync_playwright() as pw:
                browser=pw.chromium.launch(headless=True);context=browser.new_context();page=context.new_page()
                page.on('pageerror',lambda e:errors.append(str(e)))
                page.on('response',lambda r:errors.append(f'{r.status} {r.url}') if r.status>=400 else None)
                for lang in ('en','ru'):
                    for width in (1440,900,390,320):
                        page.set_viewport_size({'width':width,'height':1000})
                        for theme in ('light','dark'):
                            page.goto(base+lang+'/portfolio/')
                            page.evaluate('t=>document.documentElement.dataset.theme=t',theme)
                            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                            widths=page.locator('.kb-column').evaluate_all('es=>es.map(e=>e.getBoundingClientRect().width)')
                            assert max(widths)-min(widths)<1
                            starts=page.locator('.kb-column .kb-stack').evaluate_all('es=>es.map(e=>e.getBoundingClientRect().top)')
                            assert max(starts)-min(starts)<1
                            inspect(page,'#board [data-kb-open=INI-013]','#board [data-kb-open=INI-004]','[data-pf-panel]:visible [data-kb-close]',counts)
                            page.locator('#board [data-kb-open=INI-004]').click();page.locator('[data-pf-search]').fill('INI-013')
                            assert page.locator('[data-kb-panel]:visible').count()==0
                            assert page.locator('[data-pf-search]').evaluate('e=>e===document.activeElement')
                            page.locator('[data-pf-search]').fill('');page.locator('#board [data-kb-open=INI-004]').click();page.locator('[data-pf-tab=review]').click()
                            assert page.locator('[data-kb-panel]:visible').count()==0
                            page.locator('#review [data-kb-open=INI-004]').click();assert page.locator('#review [data-kb-panel]').is_visible()
                            page.locator('[data-pf-tab=standing]').click();page.locator('#standing [data-kb-open=INI-009]').click()
                            assert page.locator('#standing [data-kb-panel]').is_visible()
                            if width in (1440,390):page.screenshot(path=str(REPORT/f'{lang}-{width}-{theme}-portfolio.png'),full_page=True)
                            pfstyle=page.locator('#standing [data-kb-open=INI-009]').evaluate('e=>({font:getComputedStyle(e.querySelector("h3")).font, padding:getComputedStyle(e).padding, radius:getComputedStyle(e).borderRadius,bg:getComputedStyle(e).backgroundColor,fg:getComputedStyle(e).color})')
                            page.goto(base+lang+'/program/');page.evaluate('t=>document.documentElement.dataset.theme=t',theme)
                            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                            inspect(page,'[data-kb-open=FEAT-901]','[data-kb-open=FEAT-902]','[data-kb-close]',counts)
                            dlstyle=page.locator('[data-kb-open=FEAT-901]').evaluate('e=>({font:getComputedStyle(e.querySelector("h3")).font, padding:getComputedStyle(e).padding,radius:getComputedStyle(e).borderRadius,bg:getComputedStyle(e).backgroundColor,fg:getComputedStyle(e).color})')
                            assert pfstyle==dlstyle,(pfstyle,dlstyle)
                            assert contrast(dlstyle['fg'],dlstyle['bg'])>=4.5
                            page.locator('[data-kb-open=FEAT-901]').click()
                            pane=page.locator('[data-kb-panel]:visible');assert 'DEP-014' in pane.inner_text()
                            assert 'INI-009' in pane.inner_text()
                            assert pane.locator('.dl-facts').is_visible()
                            if width in (1440,390):page.screenshot(path=str(REPORT/f'{lang}-{width}-{theme}-delivery.png'),full_page=True)
                            page.locator('[data-dl-tab=intake]').click();assert page.locator('[data-kb-panel]:visible').count()==0
                            page.locator('[data-dl-tab=board]').click();page.locator('[data-kb-open=FEAT-901]').click();page.locator('[data-kb-full]').click()
                            assert '/items/feat-901/' in page.url
                            views.append({'lang':lang,'width':width,'theme':theme})
                    page.goto(base+lang+'/program/')
                    with context.expect_page() as opened:page.locator('[data-kb-open=FEAT-902]').click(modifiers=['Control'])
                    child=opened.value;child.wait_for_load_state();assert '/items/feat-902/' in child.url;child.close()
                    assert not page.locator('[data-kb-panel]').is_visible()
                    plain=browser.new_context(java_script_enabled=False);reader=plain.new_page();reader.goto(base+lang+'/program/')
                    reader.locator('[data-kb-open=FEAT-901]').click();assert '/items/feat-901/' in reader.url;plain.close();counts['native_fallback']+=1
                package=Path(tmp)/'Portable package';export(output,package)
                for lang in ('en','ru'):
                    page.goto((package/lang/'program/index.html').as_uri())
                    inspect(page,'[data-kb-open=FEAT-901]','[data-kb-open=FEAT-902]','[data-kb-close]',counts)
                    counts['nonempty_portable']+=1
                browser.close()
        finally:
            server.shutdown();server.server_close()
            (REPORT/'browser-report.json').write_text(json.dumps({'counts':counts,'views':views,'errors':errors},ensure_ascii=False,indent=2))
    assert not errors,errors
    print(json.dumps({'counts':counts,'views':len(views),'errors':errors}))


if __name__=='__main__':main()
