# START_MODULE_CONTRACT
#   PURPOSE: Compose independent Discovery, Portfolio, Delivery Pipeline and AI Lab sections.
#   SCOPE: Retained scenario, laboratory and project projection, authored neighbour pages, local search and assets.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   ROOT - repository root
#   SOURCE - retained Financial Services source tree
#   PAGES - authored neighbour page routing
#   DOMAIN_ORDER - stable Discovery area order
#   OVERVIEW - local navigation labels
#   CATALOG_TITLE - full catalog name on the landing page
#   INTRO - Discovery landing introduction
#   horizon_themes - regulatory horizon themes with their standing from the Registry
#   scenario_index - scenarios of an edition by urn, for links from authored pages
#   horizon_page, horizon_box, horizon_chips - render the Regulatory Horizon page, its overview box and card marks
#   reading_guide - render the authored reading aid of the landing page
#   finance_renderer - load the established Financial Services source adapter
#   VisibleText - extract searchable text without embedded code
#   title_of - extract a page's visible title
#   write - write a generated section file
#   local_links - render section-local navigation
#   workflow_card - render bilingual workflow previews with source stage destinations
#   discovery_layout - apply shared cards and context presentation without rewriting content
#   discovery_page - retain scenario bodies while replacing presentation chrome
#   search_entries - index Discovery pages and scenario fragments
#   build_discovery - generate both retained catalogue editions
#   build_landings - generate the independent authored pages and search indexes
#   build_neighbours - compose all four neighbours
# END_MODULE_MAP
"""Section content stays separate from the charter renderer and its term links."""
from html import escape, unescape
import functools
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
# Full name of the catalog on its landing page; navigation and breadcrumbs use the short section label.
CATALOG_TITLE = {'en': 'Discovery Catalog', 'ru': 'Каталог сценариев для применения AI'}
INTRO = {
    'en': 'The Discovery Catalog is a map of a bank and, for each part of the map, a list of scenarios in which AI could help. It gives a uniform view of the Bank\'s primary value chains, shared capabilities, steering and control, and for each it shows where AI can increase visibility and insight, automate operational flows, enable people at the point of work, and open new offerings. It holds 1,110 scenarios in nine areas. Use it to find and compare opportunities; nothing in it has been selected or approved.',
    'ru': 'Каталог — это карта банка: для каждой её части приведены сценарии, в которых AI может принести пользу. Он охватывает основные бизнес-процессы, общие банковские функции, управление и контроль и показывает, где AI помогает лучше видеть и анализировать, автоматизировать операции, поддерживать сотрудников в работе и создавать новые продукты. В каталоге 1 110 сценариев в девяти областях. Используйте его, чтобы находить и сравнивать возможности: ни один сценарий пока не отобран и не утверждён.',
}


HORIZON = ROOT / 'portal/sections/discovery/horizon.json'
HORIZON_TEXT = {
    'en': {'title': 'Regulatory Horizon', 'eyebrow': 'Cross-cutting view', 'box': 'Readiness for rules ahead', 'instruments': 'Instruments', 'chip': 'Regulatory Horizon',
           'intro': 'The kinds of rules that already bind the Bank or are expected to reach it, and the scenarios in this catalog that prepare the Bank for them. Each theme names example instruments as references. Its standing for the Bank comes from the Standards record of the Registry and is to be confirmed by the Control Function Contacts. Preparing early lets the work be planned, piloted and measured before a rule applies.',
           'groups': {'Applies': 'Applies to the Bank', 'Expected': 'Expected', 'Reference': 'Reference'}, 'scenarios': 'scenarios'},
    'ru': {'title': 'Регуляторные требования', 'eyebrow': 'Сквозной взгляд', 'box': 'Готовность к новым требованиям', 'instruments': 'Акты', 'chip': 'Регуляторные требования',
           'intro': 'Виды правил, которые уже обязательны для Банка или предположительно будут на него распространены, и сценарии каталога, которые готовят к ним Банк. Для каждой темы приведены примеры актов. Её статус для Банка взят из реестра «Стандарты» и подлежит подтверждению представителями контрольных функций.',
           'groups': {'Применяется': 'Применяется', 'Ожидается': 'Ожидается', 'Справочный': 'Справочный'}, 'scenarios': 'сценариев'},
}


@functools.cache
def horizon_themes_cached(lang):
    return horizon_themes(lang)


def horizon_themes(lang):
    """Themes of the regulatory horizon: standing and instruments from the Registry, links from the section data."""
    if not HORIZON.exists():
        return []
    register = {}
    for line in (ROOT / 'registry' / lang / 'standards.md').read_text().splitlines():
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if cells and re.fullmatch(r'HZ-\d{3}', cells[0]):
            register[cells[0]] = {'title': cells[1], 'instruments': cells[2], 'standing': cells[3]}
    present = scenario_index(lang)
    themes = []
    for theme in json.loads(HORIZON.read_text())['themes']:
        if theme['id'] not in register:
            raise ValueError(f'Regulatory horizon theme missing from the Registry: {theme["id"]}')
        text = {key: theme[key] for key in ('asks', 'readiness') if lang == 'en' and theme.get(key)}
        # An edition links the scenarios it holds; new scenarios reach the Russian edition with its own round.
        held = [urn for urn in theme['scenarios'] if urn in present]
        themes.append({**theme, **register[theme['id']], **text, 'scenarios': held})
    return themes


@functools.cache
def scenario_index(lang):
    """Every scenario of an edition by urn: its page, anchor, title and lens."""
    index = {}
    for path in sorted((SOURCE / lang).rglob('index.html')):
        relative = path.relative_to(SOURCE / lang).parent.as_posix()
        source = path.read_text()
        page_title = title_of(source)
        for match in re.finditer(r'<details class="scenario-card" data-urn="([^"]+)">(.*?)</details>', source, re.S):
            title = re.search(r'<h3 class="scenario-card__title">(.*?)</h3>', match[2], re.S)
            lens = re.search(r'<span class="scenario-lens[^"]*">(.*?)</span>', match[2], re.S)
            index[match[1]] = {'page': '' if relative == '.' else relative + '/', 'page_title': page_title,
                               'anchor': 'scenario-' + match[1].rsplit('/', 1)[-1],
                               'title': VisibleText(title[1]).text().lstrip('▸ ') if title else match[1], 'lens': VisibleText(lens[1]).text() if lens else ''}
    return index


def standing_group(standing, lang):
    return next(label for key, label in HORIZON_TEXT[lang]['groups'].items() if standing.startswith(key))


def horizon_page(lang, themes, index):
    """The Regulatory Horizon page of an edition, inside the Discovery content frame."""
    text = HORIZON_TEXT[lang]
    url = f'/{lang}/discovery/regulatory-horizon/'
    sections = []
    for theme in themes:
        items = []
        for urn in theme['scenarios']:
            card = index[urn]
            href = workspace.relative(url, f'/{lang}/discovery/{card["page"]}') + '#' + card['anchor']
            items.append(f'<li><a href="{escape(href)}">{escape(card["title"])}</a>'
                         f'<span class="horizon-scenarios__where">{escape(card["lens"])} · {escape(card["page_title"])}</span></li>')
        prose = ''.join(f'<p>{escape(theme[key])}</p>' for key in ('asks', 'readiness') if theme.get(key))
        sections.append(f'<section class="horizon-theme" id="{theme["slug"]}"><header class="horizon-theme__head">'
                        f'<span class="horizon-theme__id">{theme["id"]}</span><h2>{escape(theme["title"])}</h2>'
                        f'<span class="horizon-standing">{escape(theme["standing"])}</span></header>'
                        f'<p class="horizon-theme__instruments"><strong>{text["instruments"]}:</strong> {escape(theme["instruments"])}</p>{prose}'
                        f'<ol class="horizon-scenarios">{"".join(items)}</ol></section>')
    contents = ''.join(f'<li><a href="#{t["slug"]}">{escape(t["title"])}</a> <span class="card-link__count">({len(t["scenarios"])})</span></li>' for t in themes)
    label = workspace.section_label('discovery', lang)
    header = (f'<header class="page-header"><nav class="breadcrumb" aria-label="Breadcrumb"><span class="breadcrumb__item">'
              f'<a class="breadcrumb__link" href="../">{escape(label)}</a></span><span class="breadcrumb__item">'
              f'<span class="breadcrumb__sep" aria-hidden="true">/</span><span class="breadcrumb__current" aria-current="page">{text["title"]}</span></span></nav>'
              f'<h1 class="page-header__title">{text["title"]}</h1><p class="page-header__intent">{escape(text["intro"])}</p></header>')
    body = header + f'<div class="horizon"><ol class="horizon-contents">{contents}</ol>{"".join(sections)}</div>'
    return url, text['title'], body


def horizon_box(themes, lang):
    """The overview box that leads to the Regulatory Horizon page."""
    text = HORIZON_TEXT[lang]
    groups = {}
    for theme in themes:
        groups.setdefault(standing_group(theme['standing'], lang), []).append(theme)
    total = len({urn for theme in themes for urn in theme['scenarios']})
    rows = ''.join('<div class="sub-group"><div class="sub-group__label">' + escape(label) + '</div><div class="sub-group__items">'
                   + '<span class="dot" aria-hidden="true">·</span>'.join(
                       f'<a class="card-link" href="regulatory-horizon/index.html#{t["slug"]}">{escape(t["title"])} <span class="card-link__count">({len(t["scenarios"])})</span></a>' for t in items)
                   + '</div></div>' for label, items in groups.items())
    return (f'<div role="region" aria-label="{text["eyebrow"]}" class="horizon-region"><div class="peer-label" role="heading" aria-level="2">{text["eyebrow"]}</div>'
            f'<article class="card card--horizon" data-ui-pattern="groups"><div class="card__head"><div class="card__eyebrow">{text["box"]}</div>'
            f'<h2 class="card__title card__title--lg">{text["title"]} <span class="card__count" aria-label="{total} {text["scenarios"]}">({total})</span></h2></div>'
            f'<div class="card__body"><div class="sub-groups sub-groups--row">{rows}</div></div>'
            f'<a class="card__click-target" href="regulatory-horizon/index.html" tabindex="0" aria-label="{text["title"]}"></a></article></div>')


def horizon_chips(body, url, lang, themes):
    """Mark each linked scenario with the themes that it prepares for."""
    by_urn = {}
    for theme in themes:
        for urn in theme['scenarios']:
            by_urn.setdefault(urn, []).append(theme)
    target = workspace.relative(url, f'/{lang}/discovery/regulatory-horizon/')

    def chip(match):
        found = by_urn.get(match[1])
        if not found:
            return match[0]
        links = ''.join(f'<a href="{target}#{t["slug"]}">{escape(t["title"])}</a>' for t in found)
        return match[0] + f'<p class="horizon-chip"><span>{HORIZON_TEXT[lang]["chip"]}:</span> {links}</p>'
    return re.sub(r'<details class="scenario-card" data-urn="([^"]+)".*?<div class="scenario-card__body">', chip, body, flags=re.S)


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


def workflow_card(match, relative, lang):
    """Render workflow previews from the linked flow page in the same edition."""
    destination = re.search(r'<a class="card__click-target" href="([^"]+)"', match[0])[1]
    source = (SOURCE / lang / relative.parent / destination).read_text()
    stages_label = re.search(r'<nav class="flow-stages" aria-label="([^"]+)"', source)[1]
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
    head = re.sub(r'(<h2[^>]*>)(.*?)(</h2>)', lambda m: m[1] + f'<a class="workflow-overview-link" href="{destination}">' + m[2] + '</a>' + m[3], head, count=1, flags=re.S)
    body = re.sub(r'[ \t]+$', '', remainder.rsplit('</div>', 1)[0], flags=re.M)

    def preview(item):
        href, title = item[1], item[2]
        path, identifier = href.split('#', 1)
        intent, stages = flows[identifier]
        steps = ''.join(f'<li><a href="{path}#stage-{identifier}--{slug}">{label}</a></li>' for slug, label in stages)
        return ('<li class="flow-item"><details class="workflow-preview">'
                f'<summary>{title}</summary><div class="workflow-preview__body">'
                f'<p>{intent}</p><ol class="workflow-preview__stages" aria-label="{stages_label}">{steps}</ol>'
                '</div></details></li>')

    previews = re.sub(r'<li class="flow-item">\s*<a href="([^"]+)" class="flow-item__name card-link">(.*?)</a>\s*</li>', preview, body, flags=re.S)
    return head + '<div class="card__body">' + previews + '</div></article>'


def discovery_layout(body, relative, lang):
    """Project the approved shared constructs; source wording and identities stay intact."""
    def context_cards(match):
        rows = re.findall(r'<tr class="problems-row">\s*<th\b[^>]*>(.*?)</th>\s*<td\b[^>]*>(.*?)</td>\s*</tr>', match[0], re.S)
        if not rows or len(rows) != len(re.findall(r'<tr\b', match[0])):
            raise ValueError(f'Unrecognized context rows: {lang}/{relative}')
        return '<div class="discovery-context-grid">' + ''.join(
            '<article class="discovery-context-card"><h3>' + label + '</h3><p>' + statement + '</p></article>'
            for label, statement in rows) + '</div>'

    body = re.sub(r'<table class="problems-table">.*?</table>', context_cards, body, flags=re.S)
    overview_ids = iter('abcdefghijk')
    def card_pattern(match):
        classes = match[1]
        pattern = 'in-progress' if 'card--peer' in classes else 'workflows' if 'card--flow' in classes else 'groups'
        # Retain the overview's existing public fragment destinations.
        identifier = f' id="ui-option-{next(overview_ids)}"' if relative == Path('index.html') else ''
        return classes + f' data-ui-pattern="{pattern}"' + identifier + '>'
    body = re.sub(r'(<article class="card[^"]*")>', card_pattern, body)
    body = re.sub(r'<article class="card card--flow"[^>]*>.*?</article>',
                  lambda match: workflow_card(match, relative, lang), body, flags=re.S)
    def development_card(match):
        card = match[0].replace(' (deferred)', '').replace('card-link--deferred', 'card-link--pending')
        status = 'In progress' if lang == 'en' else 'В разработке'
        return re.sub(r'(<div class="card__eyebrow">.*?)(</div>)',
                      lambda m: m[1] + f'<span class="discovery-status">{status}</span>' + m[2], card, count=1, flags=re.S)
    body = re.sub(r'<article class="card card--peer"[^>]*>.*?</article>', development_card, body, flags=re.S)
    return re.sub(r'(<details class="scenario-card"[^>]*)(>)', r'\1 data-ui-pattern="scenario"\2', body)


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
    if relative == Path('index.html'):
        body = re.sub(r'(<h1\b[^>]*>).*?(</h1>)', lambda m: m[1] + escape(CATALOG_TITLE[lang]) + m[2], body, count=1, flags=re.S)
        body = re.sub(r'(<p class="page-header__intent">).*?(</p>)', lambda m: m[1] + escape(INTRO[lang]) + m[2], body, count=1, flags=re.S)
        body = re.sub(r'(<header class="page-header"[^>]*>.*?</header>)', lambda m: m[1] + reading_guide(lang), body, count=1, flags=re.S)
    body = discovery_layout(body, relative, lang)
    # Each stage is a stable destination, including Russian and domain workflow pages.
    def stage_target(match):
        attrs = match[1]
        flow = re.search(r'data-flow-id="([^"]+)"', attrs)[1].rsplit(':', 1)[-1].rsplit('/', 1)[-1]
        stage = re.search(r'data-stage="([^"]+)"', attrs)[1]
        return f'<button{attrs} id="stage-{flow}--{stage}">'
    body = re.sub(r'<button\b([^>]*class="flow-stages__stage"[^>]*)>', stage_target, body)
    themes = horizon_themes_cached(lang)
    if relative == Path('index.html') and themes:
        peer_region = re.search(r'<div\b[^>]*role="region"[^>]*>\s*<div\b[^>]*class="peer-label"', body)
        if not peer_region:
            raise ValueError(f'Missing peer framework region: {lang}/{relative}')
        body = body[:peer_region.start()] + horizon_box(themes, lang) + body[peer_region.start():]
    if themes:
        body = horizon_chips(body, url, lang, themes)
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
        themes = horizon_themes_cached(lang)
        if themes:
            links.append((f'/{lang}/discovery/regulatory-horizon/', HORIZON_TEXT[lang]['title']))
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
        if themes:
            url, title, body = horizon_page(lang, themes, scenario_index(lang))
            body = f'<div class="discovery-content">{body}</div>'
            head = ''.join(f'<link rel="stylesheet" href="../assets/styles/{name}">\n' for name in ('tokens.css', 'components.css', 'theme.css', 'layouts/concern.css'))
            skin = f'<link rel="stylesheet" href="{workspace.asset(url, "discovery.css")}">'
            js = f'<script defer src="{workspace.relative(url, "/assets/discovery.js")}"></script>'
            page = workspace.page(url, lang, 'discovery', title, body, local_links(url, links), extra_head=head, body_class='discovery-workspace page--concern discovery-horizon')
            write(output, url + 'index.html', page.replace('</head>', skin + '\n' + js + '\n</head>', 1))
            entries.extend(search_entries(body, url, title))
            count += 1
        write(output, f'assets/search-discovery-{lang}.json', json.dumps(entries, ensure_ascii=False, separators=(',', ':')))
    shutil.copyfile(ROOT / 'finance-portal/assets/finance.js', output / 'assets/discovery.js')
    return count


def build_landings(output):
    md = MarkdownIt('commonmark', {'html': False}).enable('table')
    count = 0
    for lang in ('en', 'ru'):
        indexes = {name: [] for name in ('initiatives', 'projects')}
        for item in PAGES:
            section = item['section']
            if item.get('renderer') in ('lab', 'project'):
                continue
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
    import lab
    import project
    output = Path(output)
    return build_discovery(output) + build_landings(output) + lab.build(output) + project.build(output)
