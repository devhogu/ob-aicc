#!/usr/bin/env python3
"""Check literal real baseline and the generated Initiative/project reader paths."""
from html import unescape
import json
from urllib.parse import urljoin,urlsplit
from check_neighbours import Inspection
import delivery
import portfolio


def main():
    root=delivery.workspace.ROOT;output=root/'html/aicc/v1'
    for lang in ('en','ru'):
        data=delivery.project(lang=lang)
        assert data['items']==[] and set(data['counts'].values())=={0}
        front=output/lang/'program/index.html';text=front.read_text();parsed=Inspection(text)
        assert parsed.section=='program'
        assert f'data-dl-item="INI-013"' in text
        assert text.count('data-dl-item=')==7 and text.count('data-dl-panel')==3
        assert 'delivery.css?' in text and 'delivery.js?' in text
        assert 'INI-006' in text
        assert not any(s in text for s in ['Moldogazieva','Молдогазиева','html-alt/'])
        record=(output/lang/'portfolio/ini-013/index.html').read_text()
        assert 'DR-2026-061 confirms' not in record and 'DR-2026-061 подтверждает' not in record
        assert 'service-resolution/' in record and '/#intake' in record
        for page in [front,*list((output/lang/'program/service-resolution').rglob('index.html'))]:
            body=page.read_text()
            assert ('to be entered in' if lang=='en' else 'подлежит внесению') not in body
            for href in Inspection(body).main_links:
                target=urlsplit(urljoin('http://portal/'+page.relative_to(output).as_posix(),href))
                if target.netloc!='portal':continue
                destination=output/target.path.strip('/')
                if target.path.endswith('/'):destination/='index.html'
                assert destination.exists(),target.path
        project=(output/lang/'program/service-resolution/index.html').read_text()
        assert 'INI-013' in project and 'ini-013/' in project
        charter=(output/lang/'program/service-resolution/charter/index.html').read_text()
        assert ('supporting business-case draft' if lang=='en' else 'проект бизнес-кейса') in charter
        search=json.loads((output/f'assets/search-program-{lang}.json').read_text())
        assert any(e['u']==f'/{lang}/program/' for e in search)
        assert all(e['u'].startswith(f'/{lang}/program/') for e in search)
        print(f'{lang}: seven ordinary intake links, four Standing sources, empty Program board and complete project relationship verified')


if __name__=='__main__':main()
