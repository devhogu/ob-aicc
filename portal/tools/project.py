# START_MODULE_CONTRACT
#   PURPOSE: Promote the retained bilingual project workbook into Delivery Pipeline.
#   SCOPE: Complete document projection, local destinations, native diagrams and search.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
#   MAP_MODE: SUMMARY
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   documents - extract source document bodies and their destination ownership
#   render - adapt presentation without changing authored content
#   build - publish both editions, assets and section-scoped search
# END_MODULE_MAP
from html import escape, unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil

import workspace

SOURCE = workspace.ROOT / 'html-alt/intelligent-customer-service-resolution'
ROUTES = {'start': '', 'business-use-case': 'business-case/', 'charter-guide': 'charter-selection/',
          'payment-charter': 'payment-issue/', 'dispute-charter': 'card-dispute/', 'kyc-charter': 'onboarding-kyc/',
          'technical-blueprint': 'technical-blueprint/', 'journey-profiles': 'journey-profiles/',
          'platform-map': 'platform-readiness/'}
UI = {'en': {'overview': 'Project overview', 'documents': 'Project documents', 'contents': 'In this document', 'register': 'Project register',
             'proposal': 'Proposal', 'expand': 'Expand diagram', 'close': 'Close', 'fit': 'Fit', 'actual': '100%',
             'out': 'Zoom out', 'in': 'Zoom in', 'view': 'Expanded diagram', 'hint': 'Scroll to pan · Ctrl/⌘ + wheel to zoom'},
      'ru': {'overview': 'Обзор проекта', 'documents': 'Документы проекта', 'contents': 'Разделы документа', 'register': 'Реестр проектов',
             'proposal': 'Предложение', 'expand': 'Развернуть диаграмму', 'close': 'Закрыть', 'fit': 'Вписать', 'actual': '100%',
             'out': 'Уменьшить', 'in': 'Увеличить', 'view': 'Развернутая диаграмма', 'hint': 'Прокрутка для перемещения · Ctrl/⌘ + колесо для масштаба'}}


class _Text(HTMLParser):
    def __init__(self, markup):
        super().__init__(); self.skip = 0; self.parts = []; self.feed(markup)
    def handle_starttag(self, tag, attrs):
        if tag in ('style', 'script'): self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('style', 'script'): self.skip -= 1
    def handle_data(self, text):
        if not self.skip: self.parts.append(text)
    def text(self):
        return ' '.join(' '.join(self.parts).split())


class _Source(HTMLParser):
    """Use byte-preserving slices, so SVG case, geometry and document HTML survive."""
    def __init__(self, text):
        super().__init__(); self.text = text; self.lines = [0]; self.current = None
        self.depth = 0; self.sections = {}; self.owners = {}
        for match in re.finditer('\n', text): self.lines.append(match.end())
        self.feed(text)
    def position(self):
        line, col = self.getpos(); return self.lines[line - 1] + col
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'section':
            if 'data-document' in a:
                if self.current: raise ValueError('Nested source documents are unsupported')
                self.current = a['data-document']; self.start = self.position(); self.depth = 0
            if self.current: self.depth += 1
        if self.current and 'id' in a:
            if a['id'] in self.owners: raise ValueError('Duplicate source identity: ' + a['id'])
            self.owners[a['id']] = self.current
    def handle_endtag(self, tag):
        if tag == 'section' and self.current:
            self.depth -= 1
            if self.depth == 0:
                end = self.position() + len('</section>')
                self.sections[self.current] = self.text[self.start:end]; self.current = None


def documents(lang):
    text = (SOURCE / lang / 'index.html').read_text()
    parsed = _Source(text)
    expected = [lang + '-' + key for key in ROUTES]
    if list(parsed.sections) != expected: raise ValueError('Project document structure drift: ' + lang)
    labels = {}
    for match in re.finditer(r'<details class="nav-doc"[^>]*>\s*<summary>(.*?)</summary>(.*?)</details>', text, re.S):
        identifier = re.search(r'data-doc-link="([^"]+)"', match[2])[1]
        labels[identifier] = _Text(match[1]).text()
    docs = []
    for key, route in ROUTES.items():
        identifier = lang + '-' + key; body = parsed.sections[identifier]
        heading = re.search(r'<h[12]\b[^>]*>(.*?)</h[12]>', body, re.S)
        docs.append({'id': identifier, 'key': key, 'url': f'/{lang}/projects/service-resolution/' + route,
                     'title': _Text(heading[1]).text(), 'label': labels.get(identifier, UI[lang]['overview']), 'body': body})
    owners = {identifier: next(d['url'] for d in docs if d['id'] == owner) for identifier, owner in parsed.owners.items()}
    return docs, owners


def _headings(body):
    return [(m[1], _Text(m[2]).text()) for m in re.finditer(r'<h[23]\b[^>]*id="([^"]+)"[^>]*>(.*?)</h[23]>', body, re.S)]


def _nav(docs, current, lang):
    ui = UI[lang]; url = current['url']
    out = f'<a href="{workspace.relative(url, "/" + lang + "/projects/")}">{ui["register"]}</a>'
    for doc in docs:
        label = ui['overview'] if doc['key'] == 'start' else doc['label']
        state = ' aria-current="page"' if doc is current else ''
        out += f'<a href="{workspace.relative(url, doc["url"])}"{state}>{escape(label)}</a>'
        if doc is current:
            links = ''.join(f'<a href="#{escape(identifier)}">{escape(title)}</a>' for identifier, title in _headings(doc['body']) if identifier != re.search(r'<h2\b[^>]*id="([^"]+)"', doc['body'])[1]) if doc['key'] != 'start' else ''
            if links:
                out += f'<details class="project-nav-topics"><summary>{ui["contents"]}</summary><div>{links}</div></details>'
    return out


def _diagram(match, lang):
    svg = re.search(r'<svg\b.*?</svg>', match[0], re.S)[0]
    label = unescape(re.search(r'<svg\b[^>]*aria-label="([^"]+)"', svg)[1])
    # Replace only the old presentation CSS; all labels, edges and geometry remain.
    svg = re.sub(r'<style>.*?</style>', '', svg, flags=re.S)
    svg = re.sub(r' role="graphics-document document"', '', svg, count=1)
    ui = UI[lang]
    width = re.search(r'viewBox="([^"]+)"', svg)[1].split()[2]
    return f'<figure class="project-diagram"><div class="project-diagram-preview" tabindex="0" role="region" aria-label="{escape(label)}" style="--project-graph-width:{width}px">{svg}</div><figcaption><span>{escape(label)}</span><button type="button" class="oc-button project-diagram-open" aria-haspopup="dialog" aria-label="{escape(ui["expand"] + ": " + label)}">{ui["expand"]}</button></figcaption></figure>'


def render(doc, docs, owners, lang):
    body = doc['body']; url = doc['url']; ui = UI[lang]
    diagrams = []
    def take(match):
        diagrams.append(_diagram(match, lang)); return f'<!--PROJECT_DIAGRAM_{len(diagrams)-1}-->'
    body = re.sub(r'<figure class="diagram"[^>]*>.*?</figure>', take, body, flags=re.S)
    def link(match):
        identifier = unescape(match[1])
        if identifier not in owners: raise ValueError('Unknown project reference: ' + identifier)
        href = '#' + identifier if owners[identifier] == url else workspace.relative(url, owners[identifier]) + '#' + identifier
        return 'href="' + escape(href) + '"'
    body = re.sub(r'href="#([^"]+)"', link, body)
    if doc['key'] != 'start':
        # Each original document becomes its own page; keep source heading IDs.
        body = re.sub(r'<(/?)h([234])\b', lambda m: '<' + m[1] + 'h' + str(int(m[2]) - 1), body)
        chunks = re.split(r'(?=<h2\b)', body)
        body = chunks[0] + ''.join('<section class="project-topic">' + chunk + '</section>' for chunk in chunks[1:-1])
        if len(chunks) > 1:
            last = chunks[-1]; end = last.rfind('</section>')
            body += '<section class="project-topic">' + last[:end] + '</section>' + last[end:]
    else:
        cards = ''.join(f'<a class="project-card" href="{workspace.relative(url, other["url"])}"><strong>{escape(other["label"])}</strong><span>{escape(other["title"])}</span></a>' for other in docs[1:] if other['key'] not in ('payment-charter', 'dispute-charter', 'kyc-charter'))
        body += f'<section class="project-topic"><h2>{ui["documents"]}</h2><div class="project-document-grid">{cards}</div></section>'
    for number, markup in enumerate(diagrams): body = body.replace(f'<!--PROJECT_DIAGRAM_{number}-->', markup)
    back = '' if doc['key'] == 'start' else f'<nav class="project-breadcrumb" aria-label="{ui["overview"]}"><a href="{workspace.relative(url, docs[0]["url"])}">{escape(docs[0]["title"])}</a><span aria-hidden="true"> / </span><span>{escape(doc["label"])}</span></nav>'
    return '<article class="project-content"><span class="neighbour-status">' + ui['proposal'] + '</span>' + back + body + '</article>'


def build(output):
    output = Path(output)
    for lang in ('en', 'ru'):
        docs, owners = documents(lang); index_path = output / f'assets/search-projects-{lang}.json'
        entries = json.loads(index_path.read_text())
        for doc in docs:
            url = doc['url']; body = render(doc, docs, owners, lang)
            page = workspace.page(url, lang, 'projects', doc['title'], body, _nav(docs, doc, lang), body_class='project-workspace')
            head = f'<link rel="stylesheet" href="{workspace.asset(url, "project.css")}"><script defer src="{workspace.asset(url, "project.js")}" data-project-ui="{escape(json.dumps(UI[lang], ensure_ascii=False))}"></script>'
            page = page.replace('</head>', head + '\n</head>', 1)
            target = output / url.strip('/') / 'index.html'; target.parent.mkdir(parents=True, exist_ok=True); target.write_text(page)
            entries.append({'u': url, 't': doc['title'], 'h': doc['label'], 'x': _Text(doc['body']).text()})
            for match in re.finditer(r'<h[34]\b[^>]*id="([^"]+)"[^>]*>(.*?)</h[34]>(.*?)(?=<h[34]\b|$)', doc['body'], re.S):
                entries.append({'u': url + '#' + match[1], 't': doc['title'], 'h': _Text(match[2]).text(), 'x': _Text(match[3]).text()})
        index_path.write_text(json.dumps(entries, ensure_ascii=False, separators=(',', ':')))
    for name in ('project.css', 'project.js'): shutil.copyfile(workspace.ROOT / 'portal/site' / name, output / 'assets' / name)
    return 18
