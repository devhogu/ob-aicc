# START_MODULE_CONTRACT
#   PURPOSE: Package complete independent EN/RU light-only editions with no JavaScript.
#   SCOPE: Native reading adapters, standalone language links/assets and verified owned output.
#   DEPENDS: M-PORTAL-PROJECTION, M-PORTABLE-EXPORT
#   LINKS: M-PORTABLE-EXPORT, V-M-PORTABLE-EXPORT
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   STATIC_KIND - static package ownership marker
#   VOID - HTML elements requiring XML closure in standalone SVGs
#   WORDS - native reading labels by language
#   SECTIONS - topic index groups by language: the five branches
#   branch_of - the topic group of a page
#   Node - retain HTML/SVG structure and original case-sensitive markup
#   Tree - preserve source HTML/SVG while changing selected reading controls
#   element - construct a native reading element
#   text_content - extract readable text from retained markup
#   replace - replace one control in its owning container
#   embed_fonts - bundle local fonts into portable stylesheets
#   adapt - expose runtime-only content and replace script-only UI
#   standalone_url - route links inside one language package
#   index_page - project source page and heading destinations into native navigation
#   edition - assemble one independently portable language tree
#   validate_edition - reject scripts, dead controls and missing local destinations
#   export_static - validate then replace exporter-owned published output
# END_MODULE_MAP
"""Static mode of export_portable.py; source HTML remains authoritative."""
import base64
import hashlib
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import posixpath
import re
import tempfile
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree

from export_portable import ROOT, MARKER, KIND, Page, snapshot, digest, local_target, file_url
import workspace

STATIC_KIND = 'aicc-static-languages-v1'
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())
WORDS = {
    'en': {'contents': 'Topics', 'edition': 'English', 'find': 'Browse the topics below or use your browser’s Find command (Ctrl+F / ⌘F).', 'diagram': 'Open full diagram', 'problem': 'Problem to solve', 'feedback': 'Page feedback'},
    'ru': {'contents': 'Темы', 'edition': 'Русский', 'find': 'Выберите тему ниже или используйте поиск браузера (Ctrl+F / ⌘F).', 'diagram': 'Открыть схему полностью', 'problem': 'Решаемая задача', 'feedback': 'Обратная связь'},
}
# Topic groups are the five branches, named as in the navigation.
SECTIONS = {lang: {s['id']: s['label'][lang] for s in workspace.SECTIONS} for lang in ('en', 'ru')}


def branch_of(page, lang):
    """The branch of a page of an edition; the router and pages outside the branches are listed with the Center."""
    parts = page.split('/')
    return parts[1] if len(parts) > 2 and parts[1] in SECTIONS[lang] else 'center'


class Node:
    def __init__(self, tag='', attrs=None, raw='', single=False):
        self.tag, self.attrs, self.raw, self.single = tag, dict(attrs or []), raw, single
        self.original = self.attrs.copy()
        self.original_tag = tag
        self.children, self.parent = [], None

    def append(self, child):
        self.children.append(child)
        if isinstance(child, Node):
            child.parent = self
        return child

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Node):
                yield from child.walk()

    def has(self, name):
        return name in self.attrs.get('class', '').split()

    def remove(self):
        if self.parent is not None and self in self.parent.children:
            self.parent.children.remove(self)
            self.parent = None

    def body(self, xml=False):
        def literal(value):
            if xml:
                return re.sub(r'&([A-Za-z][A-Za-z0-9]+);', lambda m: m[0] if m[1] in ('amp', 'lt', 'gt', 'apos', 'quot') else html.unescape(m[0]), value)
            return value
        return ''.join(c.render(xml=xml) if isinstance(c, Node) else literal(c) for c in self.children)

    def render(self, xml=False):
        if not self.tag:
            return self.body(xml=xml)
        if self.raw and self.attrs == self.original and self.tag == self.original_tag:
            start = self.raw
        else:
            # Keep SVG's case-sensitive names and attributes, including viewBox.
            original_name = re.match(r'<\s*([^\s/>]+)', self.raw)
            name = original_name[1] if original_name and self.tag == self.original_tag else self.tag
            names = {m[1].lower(): m[1] for m in re.finditer(r'([\w:-]+)\s*=', self.raw)}
            attributes = ''.join(' ' + names.get(k, k) + ('' if v is None else '="' + html.escape(v, quote=True) + '"') for k, v in self.attrs.items())
            start = '<' + name + attributes + ('/>' if self.single else '>')
        if self.single or self.tag in VOID:
            if xml and not start.endswith('/>'):
                start = start[:-1] + '/>'
            return start
        original_name = re.match(r'<\s*([^\s/>]+)', start)
        return start + self.body(xml=xml) + '</' + original_name[1] + '>'


class Tree(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.root = Node()
        self.stack = [self.root]
        self.feed(text)
        if len(self.stack) != 1:
            raise ValueError('Unclosed source HTML: ' + ', '.join(n.tag for n in self.stack[1:]))

    def handle_starttag(self, tag, attrs):
        node = self.stack[-1].append(Node(tag, attrs, self.get_starttag_text()))
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].append(Node(tag, attrs, self.get_starttag_text(), single=True))

    def handle_endtag(self, tag):
        if self.stack[-1].tag == tag:
            self.stack.pop()
        elif tag not in VOID:
            raise ValueError(f'Unbalanced source HTML: expected {self.stack[-1].tag}, got {tag}')

    def handle_data(self, data):
        self.stack[-1].append(data)

    def handle_entityref(self, name):
        self.handle_data('&' + name + ';')

    def handle_charref(self, name):
        self.handle_data('&#' + name + ';')

    def handle_comment(self, data):
        self.handle_data('<!--' + data + '-->')

    def handle_decl(self, decl):
        self.handle_data('<!' + decl + '>')


def element(tag, attrs=None, text=None):
    node = Node(tag, attrs)
    if text is not None:
        node.append(html.escape(text))
    return node


def text_content(node):
    return html.unescape(re.sub(r'<[^>]+>', '', node.body())).strip()


def replace(node, new):
    parent = node.parent
    parent.children[parent.children.index(node)] = new
    new.parent = parent


def embed_fonts(files):
    for path, data in list(files.items()):
        if not path.endswith('.css'):
            continue
        def font(match):
            target = local_target(match[2], path)
            if target and target.endswith(('.woff2', '.woff')):
                mime = 'font/woff2' if target.endswith('.woff2') else 'font/woff'
                return 'url("data:' + mime + ';base64,' + base64.b64encode(files[target]).decode() + '")'
            return match[0]
        files[path] = re.sub(r'''url\(\s*(["']?)([^)'"\s]+)\1\s*\)''', font, data.decode()).encode()


def adapt(text, page, lang, files):
    root = Tree(text).root
    words = WORDS[lang]
    # FLOW_STAGES is source JSON embedded in executable HTML. Read it before removing scripts.
    stages = {}
    for match in re.finditer(r'\bconst\s+FLOW_STAGES\s*=\s*', text):
        stages.update(json.JSONDecoder().raw_decode(text[match.end():])[0])
    labels = {n.attrs.get('for'): text_content(n) for n in root.walk() if n.has('problems-tab-label')}
    stage_count = 0
    for n in list(root.walk()):
        if n.has('flow-stages__stage'):
            slug, flow = n.attrs['data-stage'], n.attrs['data-flow-id']
            stage = next((s for s in stages.get(flow, []) if s['slug'] == slug), None)
            if not stage:
                raise ValueError(f'{page}: missing source stage {flow}/{slug}')
            identifier = n.attrs.pop('id', f'stage-{flow.rsplit(":", 1)[-1]}--{slug}')
            n.tag = 'a'
            n.attrs['href'] = '#' + identifier
            n.attrs.pop('type', None)
            detail = element('details', {'class': 'static-stage-details'})
            detail.append(element('summary', text=stage['title']))
            body = detail.append(element('div', {'id': identifier}))
            body.append(element('p', text=stage.get('intent', '')))
            if stage.get('problem'):
                problem = body.append(element('div', {'class': 'static-stage-problem'}))
                problem.append(element('strong', text=words['problem']))
                problem.append(element('p', text=stage['problem']))
            (n.parent.parent if n.parent.tag == 'nav' else n.parent).append(detail)
            stage_count += 1
    for n in list(root.walk()):
        ancestor = n
        while ancestor.parent is not None:
            ancestor = ancestor.parent
        if ancestor is not root:
            continue
        if n.tag == 'html':
            n.attrs['data-theme'] = 'light'
        if n.tag == 'meta' and n.attrs.get('name') == 'color-scheme':
            n.attrs['content'] = 'light'
        if n.tag in ('script', 'template', 'dialog') or n.has('modal') or n.has('mm-dark') or n.has('kb-detail'):
            n.remove()
            continue
        if n.tag == 'meta' and n.attrs.get('http-equiv', '').lower() == 'refresh' and page == lang + '/index.html':
            n.attrs['content'] = '0; url=center/index.html'  # the language entry forwards to the Center
            continue
        if n.tag == 'meta' and n.attrs.get('http-equiv', '').lower() == 'refresh' or n.tag == 'link' and n.attrs.get('rel') in ('alternate', 'modulepreload', 'preload'):
            n.remove()
            continue
        if n.attrs.get('id') == 'theme-switch' or any(n.has(c) for c in ('lang-switch', 'theme-switch', 'pf-filter', 'dl-filters', 'lab-view-bar')):
            n.remove()
            continue
        if n.has('o-search'):
            section = branch_of(page, lang)
            target = posixpath.relpath(lang + '/contents.html', posixpath.dirname(page))
            replace(n, element('a', {'class': 'static-contents-link', 'href': target + '#contents-' + section}, words['contents']))
            continue
        if n.tag == 'input' and n.has('problems-tab-input'):
            n.remove()
            continue
        if n.has('problems-tab-label'):
            n.tag = 'a'
            n.attrs['href'] = '#' + n.attrs['aria-controls']
            n.attrs['id'] = n.attrs.pop('for')
        if n.has('problems-panel'):
            title = labels.get(n.attrs.get('aria-labelledby'))
            if title:
                n.children.insert(0, element('h2', {'class': 'static-panel-title'}, title))
        if n.has('o-tools'):
            n.append(element('span', {'class': 'static-edition'}, words['edition']))
        if n.tag == 'button':
            if n.has('pagefb'):
                footer = next((a for a in n.parent.walk() if a.tag == 'a' and a.attrs.get('href', '').startswith('mailto:')), None)
                replace(n, element('a', {'class': 'pagefb', 'href': footer.attrs['href'] if footer else 'mailto:talimbayev@obank.kg'}, text_content(n)))
            elif n.has('lab-step'):
                stage = n.attrs['data-lab-stage']
                header = next(h for h in root.walk() if h.has('lab-stage') and h.attrs.get('data-stage') == stage)
                header.attrs.setdefault('id', 'static-lab-stage-' + stage)
                n.tag = 'a'
                n.attrs['href'] = '#' + header.attrs['id']
                n.attrs.pop('type', None)
            elif n.has('dz-open') or n.has('project-diagram-open'):
                container = n.parent
                while container.parent and not (container.tag == 'figure' or container.has('project-diagram')):
                    container = container.parent
                svg = next((s for s in container.walk() if s.tag == 'svg' and not s.has('o-icon') and not s.has('mm-dark')), None)
                if svg is None:
                    raise ValueError(f'{page}: diagram control has no diagram')
                filename = 'assets/diagrams/' + hashlib.sha256((page + str(len(files))).encode()).hexdigest()[:16] + '.svg'
                # SVGs opened as documents need their own bundled fonts too.
                svg_text = svg.render(xml=True)
                css = files.get('assets/ui/fonts.css', b'').decode()
                css += '\nsvg{background:#fff;color:#222;font-family:"Golos Text",sans-serif}'
                svg_text = re.sub(r'(<svg\b[^>]*>)', lambda m: m[1] + '<style>' + css + '</style>', svg_text, count=1)
                try:
                    ElementTree.fromstring(svg_text)
                except ElementTree.ParseError as error:
                    raise ValueError(f'{page}: invalid standalone diagram: {error}') from error
                files[filename] = svg_text.encode()
                replace(n, element('a', {'class': 'static-diagram-link', 'href': posixpath.relpath(lang + '/' + filename, posixpath.dirname(page)), 'target': '_blank', 'rel': 'noopener'}, words['diagram']))
            elif 'data-copy' in n.attrs or 'data-copy-text' in n.attrs:
                n.remove()  # The selectable source/template text remains in the page.
            else:
                raise ValueError(f'{page}: unadapted script-only button {n.attrs}')
            continue
        if n.tag in ('input', 'select'):
            # The charter's controls register has a script-only filter bar.
            n.parent.remove()
            continue
        if 'hidden' in n.attrs:
            if n.has('pf-empty') or n.has('dl-empty') or n.has('o-search-results'):
                n.remove()
                continue
            n.attrs.pop('hidden')
        if n.tag == 'a' and n.attrs.get('href', '').lower().startswith('javascript:'):
            n.tag = 'span'
            n.attrs.pop('href')
        for key in list(n.attrs):
            if key.startswith('on') or key in ('aria-pressed', 'aria-selected', 'aria-controls', 'aria-haspopup') or key == 'role' and n.attrs[key] in ('tab', 'tablist', 'tabpanel'):
                n.attrs.pop(key)
    head = next((n for n in root.walk() if n.tag == 'head'), None)
    if head:
        href = posixpath.relpath(lang + '/assets/static-export.css', posixpath.dirname(page))
        head.append(element('link', {'rel': 'stylesheet', 'href': href}))
    return root.render(), stage_count


def standalone_url(url, page, lang, original):
    target = local_target(url, page)
    if target is None:
        return url
    other = 'ru' if lang == 'en' else 'en'
    if target == other or target.startswith(other + '/'):
        return None
    parts = urlsplit(file_url(url, page, original))
    target = local_target(parts.geturl(), page)
    if target.startswith(lang + '/'):
        target = target[len(lang) + 1:]
    elif target in ('index.html', '.'):
        target = 'index.html'
    new_page = page[len(lang) + 1:]
    rel = posixpath.relpath(target, posixpath.dirname(new_page) or '.')
    return rel + ('?' + parts.query if parts.query else '') + ('#' + parts.fragment if parts.fragment else '')


def index_page(lang, pages, original):
    # Reuse the actual portal shell, replacing its body content only.
    root = Tree(original[lang + '/index.html'].decode()).root
    main = next((n for n in root.walk() if n.tag == 'main'), None)
    if main is None:  # Minimal CLI fixtures need no full shell.
        main = next(n for n in root.walk() if n.tag == 'body')
    title = next((n for n in root.walk() if n.tag == 'title'), None)
    if title:
        title.children = [html.escape(WORDS[lang]['contents'] + ' · Competence Center')]
    main.children = []
    article = main.append(element('article', {'class': 'static-index'}))
    article.append(element('h1', text=WORDS[lang]['contents']))
    article.append(element('p', text=WORDS[lang]['find']))
    indexes = []
    for path, data in original.items():
        if path.startswith('assets/search-') and path.endswith('-' + lang + '.json'):
            indexes.extend(json.loads(data))
    topics_by_page = {}
    for entry in indexes:
        if urlsplit(entry['u']).fragment:
            target = local_target(file_url(entry['u'], lang + '/contents.html', original), lang + '/contents.html')
            topics_by_page.setdefault(target, []).append(entry)
    for section, label in SECTIONS[lang].items():
        article.append(element('h2', {'id': 'contents-' + section}, label))
        listing = article.append(element('ul'))
        for page, title in sorted(pages.items(), key=lambda item: item[1].casefold()):
            kind = branch_of(page, lang)
            if kind != section:
                continue
            item = listing.append(element('li'))
            item.append(element('a', {'href': posixpath.relpath(page, lang)}, title))
            entries = topics_by_page.get(page, [])
            if entries:
                details = item.append(element('details'))
                details.append(element('summary', text=WORDS[lang]['contents']))
                topics = details.append(element('ul'))
                seen = set()
                for entry in entries:
                    if entry['u'] not in seen:
                        seen.add(entry['u'])
                        topics.append(element('li')).append(element('a', {'href': file_url(entry['u'], lang + '/contents.html', original)}, entry['h']))
    return root.render()


def edition(lang, original):
    files = {p: data for p, data in original.items() if p.startswith('assets/') and not p.endswith(('.js', '.json', '.map'))}
    files.update({p[len(lang) + 1:]: data for p, data in original.items() if p.startswith(lang + '/') and not p.endswith(('.html', '.js', '.json', '.map'))})
    files['assets/static-export.css'] = (ROOT / 'portal/site/static-export.css').read_bytes()
    embed_fonts(files)
    pages = {p: text_content(next(n for n in Tree(data.decode()).root.walk() if n.tag == 'h1')) for p, data in original.items() if p.startswith(lang + '/') and p.endswith('.html')}
    source_pages = {p: original[p] for p in pages}
    source_pages[lang + '/contents.html'] = index_page(lang, pages, original).encode()
    stages = 0
    for page, data in source_pages.items():
        rendered, count = adapt(data.decode(), page, lang, files)
        stages += count
        root = Tree(rendered).root
        for n in list(root.walk()):
            for key in ('href', 'src'):
                if key in n.attrs:
                    url = standalone_url(n.attrs[key], page, lang, original)
                    if url is None:
                        n.remove()
                    else:
                        n.attrs[key] = url
        files[page[len(lang) + 1:]] = root.render().encode()
    files['aicc.html'] = files['index.html']
    files['README.txt'] = (f'AI Competence Center — {WORDS[lang]["edition"]}\n\nOpen index.html. Keep this entire folder together; the other language folder is not required.\nLight theme only; no JavaScript. Use Topics, native disclosures, browser Find and browser zoom. Select text to copy.\n').encode()
    validate_edition(files, lang)
    return files, len(pages), stages


def validate_edition(files, lang):
    pages = {p: Page(data.decode(), p) for p, data in files.items() if p.endswith('.html')}
    for path, page in pages.items():
        tree = Tree(files[path].decode()).root
        for n in tree.walk():
            if n.tag in ('script', 'button', 'input', 'select', 'dialog', 'template') or 'hidden' in n.attrs or any(k.startswith('on') for k in n.attrs):
                raise ValueError(f'{lang}/{path}: script-only content remains: {n.tag} {n.attrs}')
            if n.tag == 'html' and n.attrs.get('data-theme') != 'light':
                raise ValueError(f'{lang}/{path}: not light-only')
        for resource in page.resources:
            if urlsplit(resource).scheme not in ('', 'data') or resource.startswith('//'):
                raise ValueError(f'{lang}/{path}: external resource {resource}')
        for url in page.links:
            parts = urlsplit(url)
            if parts.scheme == 'javascript':
                raise ValueError(f'{lang}/{path}: JavaScript URL')
            if parts.scheme or parts.netloc:
                continue
            target = local_target(url, path) if parts.path else path
            if target not in files:
                raise ValueError(f'{lang}/{path}: missing file {url}')
            if parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
                raise ValueError(f'{lang}/{path}: missing anchor {url}')


def export_static(source, output):
    source, output = source.resolve(), output.absolute()
    if output.is_symlink() or source == output.resolve() or source in output.resolve().parents or output.resolve() in source.parents:
        raise ValueError('Output must be a separate directory outside the input tree')
    if output.exists():
        marker = output / MARKER
        if not marker.is_file() or json.loads(marker.read_text()).get('kind') not in (KIND, STATIC_KIND):
            raise ValueError('Refusing to replace a directory not created by this exporter')
    original = snapshot(source)
    languages = {lang: {p[len(lang) + 1:] for p in original if p.startswith(lang + '/') and p.endswith('.html')} for lang in ('en', 'ru')}
    if not languages['en'] or languages['en'] != languages['ru']:
        raise ValueError('EN/RU page sets differ or are empty')
    files, counts, stages = {}, {}, {}
    for lang in ('en', 'ru'):
        contents, counts[lang], stages[lang] = edition(lang, original)
        files.update({lang + '/' + p: data for p, data in contents.items()})
    entry = '''<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>AI Competence Center · Language editions</title><link rel="stylesheet" href="en/assets/ui/fonts.css"><link rel="stylesheet" href="en/assets/ui/tokens.css"><link rel="stylesheet" href="en/assets/static-export.css"></head><body><main class="static-entry"><h1>AI Competence Center</h1><nav aria-label="Language editions"><a href="en/index.html" lang="en">English</a><a href="ru/index.html" lang="ru">Русский</a></nav></main></body></html>'''
    files['index.html'] = files['aicc.html'] = entry.encode()
    files['README.txt'] = b'AI Competence Center static language editions\n\nOpen en/index.html for English or ru/index.html for Russian.\nEach language folder is complete and can be copied separately. Keep its own assets and subfolders together.\nNo JavaScript; light theme only. Topics replaces search. Native expandable content and email links work without scripts. Use browser zoom and select text to copy.\nRegenerate: python3 portal/tools/build.py then python3 portal/tools/export_portable.py --static\n'
    files['HOW-TO.txt'] = (ROOT / 'portal/PORTABLE-HOWTO.txt').read_bytes()
    source_hash = digest(original)
    if source_hash != digest(snapshot(source)):
        raise ValueError('Source changed during export; retry after the site build finishes')
    manifest = {'kind': STATIC_KIND, 'source_tree_sha256': source_hash, 'source_pages': counts, 'inline_workflow_stages': stages, 'html_pages': sum(p.endswith('.html') for p in files), 'files': {p: hashlib.sha256(data).hexdigest() for p, data in sorted(files.items())}}
    files[MARKER] = (json.dumps(manifest, indent=2) + '\n').encode()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.aicc-static-', dir=output.parent) as temporary:
        stage, backup = Path(temporary) / 'new', Path(temporary) / 'old'
        stage.mkdir()
        for path, data in files.items():
            target = stage / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        if output.exists():
            os.replace(output, backup)
        try:
            os.replace(stage, output)
        except OSError:
            if backup.exists():
                os.replace(backup, output)
            raise
    print(f'Exported standalone EN ({counts["en"]} pages) and RU ({counts["ru"]} pages) to {output}; light only, no JavaScript. Workflow stages: {stages}.')
    return manifest
