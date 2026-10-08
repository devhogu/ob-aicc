#!/usr/bin/env python3
"""Independently compare each retained project document with its published body."""
from collections import Counter
from html.parser import HTMLParser
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import project
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
# Literal source-to-reader contract; does not import the renderer or its routing data.
DOCUMENTS = [('start', ''), ('charter', 'charter'), ('journeys', 'journeys'), ('journey-payment', 'journeys/payment-issue'),
             ('journey-dispute', 'journeys/card-dispute'), ('journey-kyc', 'journeys/onboarding-kyc'), ('governance', 'governance'),
             ('how-it-works', 'how-it-works'), ('controls', 'controls-and-evidence'), ('technical-design', 'technical-design'),
             ('journey-profiles', 'journey-profiles'), ('it-readiness', 'it-readiness')]
ATOMS = {'h1', 'h2', 'h3', 'h4', 'p', 'li', 'th', 'td', 'pre'}


class Capture(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.current = None; self.depth = 0; self.skip = 0; self.svg = None
        self.documents = {}; self.ids = []; self.links = []; self.open_atoms = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'a' and 'href' in a: self.links.append(a['href'])
        if tag == 'section':
            if 'data-document' in a:
                self.current = a['data-document']; self.depth = 0
                self.documents[self.current] = {'atoms': [], 'diagrams': [], 'tables': 0, 'headings': [], 'links': []}
            if self.current: self.depth += 1
        if not self.current: return
        if tag in ('style', 'script', 'figcaption'): self.skip += 1
        if self.skip: return
        doc = self.documents[self.current]
        if tag == 'a' and 'href' in a: doc['links'].append(a['href'])
        if tag == 'table': doc['tables'] += 1
        if tag == 'svg': self.svg = []; doc['diagrams'].append(self.svg)
        if self.svg is not None:
            geometry = {key: value for key, value in a.items() if key not in {'style','role'}}
            self.svg.append((tag, geometry))
        cls = set(a.get('class', '').split())
        if tag in ATOMS or cls.intersection({'eyebrow','doc-label','pill'}) or (tag in ('strong','span','b') and self.svg is None and not self.open_atoms):
            self.open_atoms.append([tag, 'heading' if tag.startswith('h') and len(tag)==2 else tag, a.get('id'), []])
    def handle_data(self, data):
        if self.current and not self.skip:
            for item in self.open_atoms: item[3].append(data)
    def handle_endtag(self, tag):
        if tag in ('style','script','figcaption') and self.current: self.skip -= 1
        if self.current and not self.skip:
            for number in range(len(self.open_atoms)-1,-1,-1):
                item=self.open_atoms[number]
                if item[0]==tag:
                    value=''.join(item[3]) if item[0]=='pre' else ' '.join(''.join(item[3]).split())
                    self.documents[self.current]['atoms'].append((item[1],item[2],value))
                    if item[1]=='heading': self.documents[self.current]['headings'].append((item[2],value))
                    del self.open_atoms[number]; break
        if tag=='svg': self.svg=None
        if tag=='section' and self.current:
            self.depth -= 1
            if not self.depth: self.current=None


def check(output):
    errors=[];counts={}
    for lang in ('en','ru'):
        original=Capture(project._workbook(lang))
        diagrams=0;tables=0;atoms=0;heading_destinations=[]
        for source,route in DOCUMENTS:
            identifier=lang+'-'+source
            path=Path(output)/lang/'program/service-resolution'/route/'index.html'
            if not path.exists(): errors.append(f'Missing project document: {path}');continue
            text=path.read_text();published=Capture(text)
            expected=original.documents[identifier];actual=published.documents.get(identifier)
            if actual is None: errors.append(f'{path}: missing source document identity');continue
            for key in ['atoms','diagrams','tables','headings']:
                if actual[key]!=expected[key]: errors.append(f'{path}: source {key} differ')
            if len(published.ids)!=len(set(published.ids)): errors.append(f'{path}: duplicate identifiers')
            if 'html-alt/' in text or 'fonts.googleapis' in text: errors.append(f'{path}: predecessor/external dependency')
            if len(actual['links'])!=len(expected['links']): errors.append(f'{path}: source link count differs')
            for old,new in zip(expected['links'],actual['links']):
                if urlsplit(new).fragment != urlsplit(old).fragment: errors.append(f'{path}: changed project reference {old}')
            diagrams+=len(actual['diagrams']);tables+=actual['tables'];atoms+=len(actual['atoms'])
            heading_destinations.extend((identifier,heading[0]) for heading in expected['headings'] if heading[0])
        entries=json.loads((Path(output)/f'assets/search-program-{lang}.json').read_text())
        indexed={urlsplit(item['u']).fragment for item in entries}
        # Document titles have page-level entries; every subordinate heading is searchable.
        for identifier,heading in heading_destinations:
            if heading not in indexed and heading!=original.documents[identifier]['headings'][0][0]: errors.append(f'{lang}: unsearchable heading {heading}')
        # Published diagrams and tables equal those of the source workbook.
        source_text=project._workbook(lang)
        expected_diagrams=source_text.count('<figure class="diagram"'); expected_tables=len(re.findall(r'<table\b',source_text))
        if diagrams!=expected_diagrams or tables!=expected_tables: errors.append(f'{lang}: expected {expected_diagrams} diagrams and {expected_tables} tables, got {diagrams}/{tables}')
        counts.update({lang+'_project_documents':len(DOCUMENTS),lang+'_project_diagrams':diagrams,lang+'_project_tables':tables,lang+'_project_content_atoms':atoms})
    return errors,counts


if __name__=='__main__':
    errors,counts=check(ROOT/'html/aicc/v1');print(json.dumps({'counts':counts,'errors':errors},ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
