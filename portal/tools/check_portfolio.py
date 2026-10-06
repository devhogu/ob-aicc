#!/usr/bin/env python3
"""Compare actual published views with their maintained records and public boundary."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit
import portfolio

ROOT = portfolio.workspace.ROOT
OUTPUT = ROOT/'html/aicc'


class Published(HTMLParser):
    def __init__(self, text):
        super().__init__();self.cards=[];self.sections=[];self.links=[];self.templates=0;self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='template':self.templates+=1
        if 'data-pf-item' in a and not self.templates:self.cards.append(a['data-pf-item'])
        if 'data-pf-panel' in a:self.sections.append(a['id'])
        if tag=='a':self.links.append(a.get('href',''))
    def handle_endtag(self,tag):
        if tag=='template':self.templates-=1


def main():
    for lang in ('en','ru'):
        d=portfolio.project(lang=lang);ids=[x['id'] for x in d['items']]
        pages=list((OUTPUT/lang/'initiatives').rglob('index.html'))
        assert len(pages)==len(ids)+3
        board=(OUTPUT/lang/'initiatives/index.html').read_text()
        p=Published(board)
        assert p.cards[:6]==ids[:6] and p.cards[6:12]==ids[:6] and p.cards[12:]==ids[6:]
        assert p.sections==['board','review','standing','roadmap']
        assert portfolio._date(lang, d['date']) in board
        assert len(re.findall(r'<li><span class="pf-meta">MS-',board))==len(d['milestones'])
        register=Published((OUTPUT/lang/'initiatives/register/index.html').read_text())
        assert register.cards==ids
        search=json.loads((OUTPUT/f'assets/search-initiatives-{lang}.json').read_text())
        assert {entry['h'] for entry in search if entry['h'].startswith('INI-')}==set(ids)
        for item in d['items']:
            path=OUTPUT/portfolio._route(lang,item).strip('/')/'index.html'
            text=path.read_text()
            assert item['title'] in portfolio._plain(__import__('html').unescape(text))
            assert item['path'] in text
            assert item['status'] in text
            assert not item['approval_ref'] or item['approval_ref'] in text
        for page in pages:
            text=page.read_text()
            assert not re.search(r'Ademi|Moldogazieva|Адеми|Молдогазиева',text)
            assert 'html-alt/' not in text
            assert 'portfolio.css?' in text and 'portfolio.js?' in text
            assert '<link rel="alternate"' in text
            for link in Published(text).links:
                target=urlsplit(urljoin('https://portal/'+page.relative_to(OUTPUT).as_posix(),link))
                if target.netloc=='portal' and '/initiatives/' in target.path:
                    destination = OUTPUT/target.path.strip('/')
                    if target.path.endswith('/'): destination /= 'index.html'
                    assert destination.exists(),target.path
        print(f'{lang}: {len(pages)} pages; {len(ids)} record identities; board, register, summaries, roadmap and search agree')
    print('Portfolio public projection checks passed')


if __name__=='__main__':main()
