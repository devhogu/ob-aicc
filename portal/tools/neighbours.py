# START_MODULE_CONTRACT
#   PURPOSE: Compose independent Discovery, Portfolio, Delivery Pipeline and CloudLab sections.
#   SCOPE: Retained scenario projection, bounded authored landing pages, local search and assets.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   ROOT - repository root
#   SOURCE - retained Financial Services source tree
#   PAGES - authored neighbour page routing
#   DOMAIN_ORDER - stable Discovery area order
#   OVERVIEW - local navigation labels
#   INTRO - Discovery landing introduction
#   reading_guide - render the authored reading aid of the landing page
#   finance_renderer - load the established Financial Services source adapter
#   VisibleText - extract searchable text without embedded code
#   title_of - extract a page's visible title
#   write - write a generated section file
#   local_links - render section-local navigation
#   workflow_card - render expandable workflows with links to retained stage details
#   discovery_page - retain scenario bodies while replacing presentation chrome
#   search_entries - index Discovery pages and scenario fragments
#   build_discovery - generate both retained catalogue editions
#   build_landings - generate the independent authored pages and search indexes
#   build_neighbours - compose all four neighbours
# END_MODULE_MAP
"""Section content stays separate from the charter renderer and its term links."""
from html import escape, unescape
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import shutil

from markdown_it import MarkdownIt
import workspace

ROOT = workspace.ROOT
SOURCE = ROOT / 'html-alt/financial-services'
PAGES = json.loads((ROOT / 'portal/sections/pages.json').read_text())
DOMAIN_ORDER = ('strategic-portfolio', 'strategic-initiatives', 'value-streams',
                'customer-market-intelligence', 'customer-channels', 'risk-control',
                'shared-banking-capabilities', 'finance-treasury', 'banking-data-analytics')
OVERVIEW = {'en': 'Overview', 'ru': 'Обзор'}
INTRO = {
    'en': 'The Discovery Catalog is a map of a bank and, for each part of the map, a list of scenarios in which AI could help. It gives a uniform view of the Bank\'s primary value chains, shared capabilities, steering and control, and for each it shows where AI can increase visibility and insight, automate operational flows, enable people at the point of work, and open new offerings. It holds 1,101 scenarios in nine areas. Use it to find and compare opportunities; nothing in it has been selected or approved.',
    'ru': 'Банковские услуги, клиентские пути и операционные возможности, в которых AI может принести пользу. Изучите карту и оцените каждую возможность с учётом условий её применения.',
}


def reading_guide(lang):
    """Render the authored reading aid of the Discovery landing page, where an edition has one."""
    path = ROOT / 'portal/sections/discovery' / lang / 'guide.md'
    if not path.exists():
        return ''
    body = MarkdownIt('commonmark', {'html': False}).enable('table').render(path.read_text())
    title = re.search(r'<h1>(.*?)</h1>', body, re.S)
    if not title:
        raise ValueError(f'Reading guide needs one h1: {path}')
    body = body.replace(title[0], '', 1)
    body = re.sub(r'<table>.*?</table>', lambda m: '<div class="o-table-wrap">' + m[0] + '</div>', body, flags=re.S)
    return ('<details class="discovery-guide"><summary>' + title[1] + '</summary>'
            '<div class="discovery-guide__body">' + body + '</div></details>')


def finance_renderer():
    spec = importlib.util.spec_from_file_location('finance_renderer', ROOT / 'finance-portal/build.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VisibleText(HTMLParser):
    def __init__(self, markup):
        super().__init__(convert_charrefs=True)
        self.parts, self.hidden = [], 0
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'svg'):
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'svg'):
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)

    def text(self):
        return ' '.join(' '.join(self.parts).split())


def title_of(markup):
    match = re.search(r'<h1\b[^>]*>(.*?)</h1>', markup, re.S)
    if not match:
        raise ValueError('Section page needs one h1')
    return VisibleText(match.group(1)).text()


def write(output, path, text):
    target = output / path.lstrip('/')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text)


def local_links(url, links):
    return ''.join(f'<a href="{workspace.relative(url, target)}"' + (' aria-current="page"' if target == url else '') + f'>{escape(label)}</a>' for target, label in links)


def workflow_card(match):
    """Render expandable workflows and stage destinations on the English overview."""
    source = (SOURCE / 'en/value-streams/index.html').read_text()
    chunks = re.split(r'<details class="flow-detail" id="([^"]+)">', source)[1:]
    flows = {}
    for identifier, chunk in zip(chunks[::2], chunks[1::2]):
        intent = re.search(r'<p class="flow-detail__intent">(.*?)</p>', chunk, re.S)
        stages = re.findall(r'<button\b[^>]*data-stage="([^"]+)"[^>]*>\s*<span class="flow-stages__stage-label">(.*?)</span>', chunk, re.S)
        if not intent or not stages:
            raise ValueError(f'Missing workflow preview source: {identifier}')
        flows[identifier] = (intent[1], stages)

    article = re.sub(r'<a class="card__click-target"[^>]*>.*?</a>', '', match[0], flags=re.S)
    head, remainder = article.split('<div class="card__body">', 1)
    head = re.sub(r'(<h2[^>]*>)(.*?)(</h2>)', lambda m: m[1] + '<a class="workflow-overview-link" href="value-streams/index.html">' + m[2] + '</a>' + m[3], head, count=1, flags=re.S)
    body = re.sub(r'[ \t]+$', '', remainder.rsplit('</div>', 1)[0], flags=re.M)

    def preview(item):
        href, title = item[1], item[2]
        path, identifier = href.split('#', 1)
        intent, stages = flows[identifier]
        steps = ''.join(f'<li><a href="{path}#stage-{identifier}--{slug}">{label}</a></li>' for slug, label in stages)
        return ('<li class="flow-item"><details class="workflow-preview">'
                f'<summary>{title}</summary><div class="workflow-preview__body">'
                f'<p>{intent}</p><ol class="workflow-preview__stages" aria-label="Workflow stages">{steps}</ol>'
                '</div></details></li>')

    previews = re.sub(r'<li class="flow-item">\s*<a href="([^"]+)" class="flow-item__name card-link">(.*?)</a>\s*</li>', preview, body, flags=re.S)
    return head + '<div class="card__body">' + previews + '</div></article>'


def discovery_page(source, relative, lang):
    """Retain the content layout, local links and scripts, replacing only its shell."""
    label = workspace.section_label('discovery', lang)
    url = f'/{lang}/discovery/' + (relative.parent.as_posix() + '/' if relative.parent != Path('.') else '')
    body_match = re.search(r'<body([^>]*)>(.*?)</body>', source, re.S)
    if not body_match:
        raise ValueError(f'Missing source body: {relative}')
    body = body_match.group(2)
    original_class = re.search(r'class="([^"]+)"', body_match.group(1))
    classes = original_class.group(1) if original_class else ''
    body = re.sub(r'<a class="skip-link"[^>]*>.*?</a>', '', body, count=1, flags=re.S)
    body = re.sub(r'<nav\b[^>]*>.*?</nav>', lambda m: '' if 'hreflang=' in m.group(0) else m.group(0), body, flags=re.S)
    body = body.replace('>service.eyebrow<', f'>{escape(label)}<')
    # These phrases identify the old section in the breadcrumb, not a scenario.
    body = re.sub(r'(<(?:a|span)\b[^>]*class="breadcrumb__(?:link|current)"[^>]*>)(Financial Services|Финансовые услуги)(</(?:a|span)>)', lambda m: m[1] + escape(label) + m[3], body)
    body = re.sub(r'<footer class="page-footer".*?</footer>', '', body, flags=re.S)
    body = re.sub(r'<main\b', '<div', body, count=1).replace('</main>', '</div>', 1)
    body = body.replace('class="page-header" role="banner"', 'class="page-header"')
    if lang == 'en' and relative == Path('strategic-portfolio/index.html'):
        # Page-local presentation trial; retain every authored statement and destination.
        classes += ' discovery-strategic'
        def context_cards(match):
            rows = re.findall(r'<tr class="problems-row">\s*<th\b[^>]*>(.*?)</th>\s*<td\b[^>]*>(.*?)</td>\s*</tr>', match[0], re.S)
            if len(rows) != 4:
                raise ValueError('Strategic portfolio context requires its four source lenses')
            return '<div class="discovery-context-grid">' + ''.join(
                '<article class="discovery-context-card"><h3>' + label + '</h3><p>' + statement + '</p></article>'
                for label, statement in rows) + '</div>'
        body = re.sub(r'<table class="problems-table">.*?</table>', context_cards, body, flags=re.S)
        body = re.sub(r'(<article class="card[^"]*")>',
                      lambda m: m[1] + ' data-ui-pattern="' + ('workflows' if 'card--flow' in m[1] else 'groups') + '">', body)
        body = re.sub(r'(<details class="scenario-card"[^>]*)(>)', r'\1 data-ui-pattern="scenario"\2', body)
    if relative == Path('index.html'):
        body = re.sub(r'(<h1\b[^>]*>).*?(</h1>)', lambda m: m[1] + escape(label) + m[2], body, count=1, flags=re.S)
        body = re.sub(r'(<p class="page-header__intent">).*?(</p>)', lambda m: m[1] + escape(INTRO[lang]) + m[2], body, count=1, flags=re.S)
        body = re.sub(r'(<header class="page-header"[^>]*>.*?</header>)', lambda m: m[1] + reading_guide(lang), body, count=1, flags=re.S)
        # Temporary visual comparison, confined to the English overview.
        if lang == 'en':
            options = iter((
                ('A', 'groups'), ('B', 'groups'), ('C', 'workflows'),
                ('D', 'groups'), ('E', 'groups'), ('F', 'groups'), ('G', 'groups'),
                ('H', 'groups'), ('I', 'groups'), ('J', 'in-progress'), ('K', 'in-progress'),
            ))
            def comparison_card(match):
                key, pattern = next(options)
                return match[1] + f' data-ui-option="{key}" data-ui-pattern="{pattern}" id="ui-option-{key.lower()}">'
            body = re.sub(r'(<article class="card[^"]*")>', comparison_card, body)
            body = re.sub(r'<article class="card card--flow"[^>]*>.*?</article>', workflow_card, body, count=1, flags=re.S)
            def development_card(match):
                card = match[0].replace(' (deferred)', '').replace('card-link--deferred', 'card-link--pending')
                return re.sub(r'(<div class="card__eyebrow">.*?)(</div>)',
                              r'\1<span class="discovery-status">In progress</span>\2', card, count=1, flags=re.S)
            body = re.sub(r'<article class="card card--peer"[^>]*>.*?</article>', development_card, body, flags=re.S)
    if lang == 'en' and relative == Path('value-streams/index.html'):
        # Stable destinations for the overview's individual stage links.
        def stage_target(match):
            attrs = match[1]
            flow = re.search(r'data-flow-id="([^"]+)"', attrs)[1].rsplit(':', 1)[-1]
            stage = re.search(r'data-stage="([^"]+)"', attrs)[1]
            return f'<button{attrs} id="stage-{flow}--{stage}">'
        body = re.sub(r'<button\b([^>]*class="flow-stages__stage"[^>]*)>', stage_target, body)
    # Add stable fragment targets without changing original scenario URNs or copy.
    body = re.sub(r'(<details class="scenario-card" data-urn="([^"]+)")', lambda m: m[1] + f' id="scenario-{m[2].rsplit("/", 1)[-1]}"', body)
    source_styles = re.findall(r'<link rel="stylesheet" href="([^"]+)">', source)
    head = ''.join(f'<link rel="stylesheet" href="{escape(href)}">\n' for href in source_styles)
    # The shared skin loads after the common shell so Discovery can preserve its layout.
    skin = f'<link rel="stylesheet" href="{workspace.asset(url, "discovery.css")}">'
    footer_script = f'<script defer src="{workspace.relative(url, "/assets/discovery.js")}"></script>'
    return url, title_of(body), body, classes, head, skin, footer_script


def search_entries(body, url, title):
    entries = [{'u': url, 't': title, 'h': title, 'x': VisibleText(body).text()[:500]}]
    pattern = r'<details class="scenario-card"[^>]*id="([^"]+)"[^>]*>(.*?)</details>'
    for match in re.finditer(pattern, body, re.S):
        name = re.search(r'<h3[^>]*>(.*?)</h3>', match[2], re.S)
        if name:
            entries.append({'u': url + '#' + match[1], 't': title, 'h': VisibleText(name[1]).text(), 'x': VisibleText(match[2]).text()[:1200]})
    return entries


def build_discovery(output):
    finance = finance_renderer()
    count = 0
    for lang in ('en', 'ru'):
        output_assets = output / lang / 'discovery/assets'
        shutil.copytree(SOURCE / lang / 'assets', output_assets)
        for css in output_assets.rglob('*.css'):
            text = css.read_text()
            text = re.sub(r'@import\s+url\(.*?\);', '', text, flags=re.S)
            text = text.replace(':root', '.discovery-content')
            css.write_text(text)
        links = [(f'/{lang}/discovery/', OVERVIEW[lang])]
        for domain in DOMAIN_ORDER:
            markup = finance.discovery_source(Path(domain) / 'index.html', lang)
            links.append((f'/{lang}/discovery/{domain}/', title_of(markup)))
        entries = []
        for path in sorted((SOURCE / lang).rglob('*.html')):
            relative = path.relative_to(SOURCE / lang)
            source = finance.discovery_source(relative, lang)
            url, title, body, classes, head, skin, js = discovery_page(source, relative, lang)
            body = f'<div class="discovery-content">{body}</div>'
            page = workspace.page(url, lang, 'discovery', title, body, local_links(url, links), extra_head=head, body_class='discovery-workspace ' + classes)
            page = page.replace('</head>', skin + '\n' + js + '\n</head>', 1)
            write(output, url + 'index.html', page)
            entries.extend(search_entries(body, url, title))
            count += 1
        write(output, f'assets/search-discovery-{lang}.json', json.dumps(entries, ensure_ascii=False, separators=(',', ':')))
    shutil.copyfile(ROOT / 'finance-portal/assets/finance.js', output / 'assets/discovery.js')
    return count


def build_landings(output):
    md = MarkdownIt('commonmark', {'html': False}).enable('table')
    count = 0
    for lang in ('en', 'ru'):
        indexes = {name: [] for name in ('initiatives', 'projects', 'lab')}
        for item in PAGES:
            section = item['section']
            url = f'/{lang}/' + item['path']
            text = (ROOT / 'portal/sections' / section / lang / item['source']).read_text()
            body = md.render(text)
            if title_of(body) != item['title'][lang]:
                raise ValueError(f'Landing title drift: {section}/{lang}/{item["source"]}')
            body = re.sub(r'<table>.*?</table>', lambda m: '<div class="o-table-wrap">' + m[0] + '</div>', body, flags=re.S)
            links = [(f'/{lang}/' + q['path'], q['title'][lang]) for q in PAGES if q['section'] == section]
            status = f'<span class="neighbour-status">{escape(item["status"][lang])}</span>'
            wrapped = '<article class="neighbour-content">' + status + body + '</article>'
            page = workspace.page(url, lang, section, item['title'][lang], wrapped, local_links(url, links))
            write(output, url + 'index.html', page)
            indexes[section].append({'u': url, 't': item['title'][lang], 'h': item['title'][lang], 'x': VisibleText(body).text()})
            count += 1
        for section, entries in indexes.items():
            write(output, f'assets/search-{section}-{lang}.json', json.dumps(entries, ensure_ascii=False, separators=(',', ':')))
    return count


def build_neighbours(output):
    output = Path(output)
    return build_discovery(output) + build_landings(output)
