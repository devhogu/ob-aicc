"""Shared reading presentation for Registry-derived Kanban boards."""
# START_MODULE_CONTRACT
# PURPOSE: Give Portfolio and Delivery consistent compact cards and inline inspection.
# SCOPE: Escaped presentation helpers and progressive assets; no workflow authority.
# DEPENDS: M-PORTAL-NEIGHBOURS
# LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# MAP_MODE: SUMMARY
# END_MODULE_CONTRACT
# START_MODULE_MAP
# card - render a native record link with compact identity, state and rank
# column_header - render consistent column titles, counts and capacity captions
# detail_panel - render a hidden inline inspection region
# compact_summary - keep decision sections visible and disclose secondary record content
# assets - reference and copy common presentation assets
# END_MODULE_MAP
from html import escape
import shutil
import re
import workspace


def card(identifier, title, href, *, kind, state, priority='', rank=None, lang='en', attributes='', classes='', order_label=None):
    order = ('Rank ' if lang == 'en' else 'Место ') + str(rank) if rank else ('Unranked' if lang == 'en' else 'Без места')
    order = order_label or order
    return f'<a class="kb-card {classes}" data-kb-open="{escape(identifier)}" href="{escape(href)}" title="{escape(title)}" {attributes}><div class="kb-meta"><span>{escape(identifier)}</span><span>{escape(kind)}</span></div><h3>{escape(title)}</h3><div class="kb-state">{escape(state)}</div><div class="kb-foot"><span>{escape(priority)}</span><span>{escape(order)}</span></div></a>'


def column_header(label, count, caption):
    match = re.fullmatch(r'(.+) \(([A-Za-z ]+)\)', label)
    title = escape(label) if not match else escape(match[1])+'<span class="kb-step-en" lang="en">'+escape(match[2])+'</span>'
    return f'<div class="kb-column-head"><div><h3>{title}</h3><span class="kb-count">{count}</span></div><small>{escape(caption)}</small></div>'


def detail_panel(lang):
    full, close = ('Full record →', 'Close') if lang == 'en' else ('Полная запись →', 'Закрыть')
    return f'<section class="kb-detail" data-kb-panel hidden><div class="kb-detail-actions"><span data-kb-identity></span><div><a data-kb-full>{full}</a><button type="button" data-kb-close>{close} ×</button></div></div><div class="kb-detail-body"></div></section>'


def assets(url, output=None):
    if output:
        for name in ('kanban.css', 'kanban.js'):
            shutil.copyfile(workspace.ROOT/'portal/site'/name, output/'assets'/name)
    return f'<link rel="stylesheet" href="{workspace.asset(url,"kanban.css")}"><script defer src="{workspace.asset(url,"kanban.js")}"></script>'


def compact_summary(body, section_class, lang):
    """Keep goal, facts, first two decision sections and notices visible."""
    sections = list(re.finditer(r'<section class="'+section_class+r'[^\"]*">.*?</section>', body, re.S))
    if len(sections) < 3:
        return body
    front = '<div class="kb-detail-main">'+''.join(m.group() for m in sections[:2])+'</div>'
    more = '<details class="kb-more"><summary>'+('Scope, controls and references' if lang == 'en' else 'Объём, контроль и ссылки')+'</summary>'+''.join(m.group() for m in sections[2:])+'</details>'
    for match in reversed(sections):
        body = body[:match.start()]+(front if match is sections[0] else '')+body[match.end():]
    return body+more
