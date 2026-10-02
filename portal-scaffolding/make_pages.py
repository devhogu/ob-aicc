#!/usr/bin/env python3
"""Make sitemap.json, inventory.md, and the outline file of every page from the page definitions below.

Edit the definitions, run `python3 portal-scaffolding/make_pages.py`, and then `python3 portal-scaffolding/check.py`.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAF = os.path.join(ROOT, 'portal-scaffolding')

SECTIONS = [
    ('about', 'About AICC', 'The intent, the purpose, the mandate, and the place of AICC in the Bank.'),
    ('what-aicc-does', 'What AICC does', 'The services that AICC offers, how a function engages AICC, and the Solutions that AICC delivers.'),
    ('how-aicc-works', 'How AICC works', 'The method: how Initiatives are taken in, decided, delivered, paced, and measured.'),
    ('organization', 'Organization', 'The Roles, the decision levels, and the bodies of AICC.'),
    ('responsible-ai', 'Responsible AI', 'The rules for the use of AI, the Risk Tiers, and the gates before use.'),
    ('governance', 'Governance and oversight', 'The control loops, the records, the controls, and the way AICC is reported and assured.'),
    ('library', 'Library', 'The templates, the forms of the records that AICC produces.'),
    ('reference', 'Reference', 'The Vocabulary, the Document Catalog, the change history, and the systems that hold the records.'),
]


def read(path):
    return open(os.path.join(ROOT, path), encoding='utf-8').read()


def sections_of(path):
    """Top-level sections of a source: number -> (title, words)."""
    parts = re.split(r'^## ', read(path), flags=re.M)[1:]
    out = {}
    for p in parts:
        title = p.split('\n', 1)[0].strip()
        if title.startswith('Change log'):
            continue
        m = re.match(r'(\d+)\.\s+(.*)', title)
        if m:
            out[int(m.group(1))] = (m.group(2), len(p.split()))
    return out


def h1(path):
    for line in read(path).splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return os.path.basename(path)


PAGES = []


def add(**k):
    k.setdefault('production', 'generated')
    PAGES.append(k)


# Home
add(id='index', section=None, order=0, type='home', slug='/', title='Home', source=['charter/executive-summary.md'],
    production='authored',
    outline=['Intent of AICC in two sentences, from the Summary of intent (Statement of Intent 2) and the Mission (AICC Charter 2)',
             'Feature: the Strategic Priorities (about/statement-of-intent/strategic-priorities)',
             'Feature: the Maturity Roadmap (about/statement-of-intent/capability-and-maturity-roadmap)',
             'The map of AICC: what AICC does, how it works, how it is safeguarded, with its text version',
             'The eight sections, each with one line',
             'The reading routes',
             'Footer: baseline revision, date, owner, link to Records and systems'])

for sid, label, line in SECTIONS:
    src = ['charter/workflows/README.md'] if sid == 'how-aicc-works' else (['charter/templates/README.md'] if sid == 'library' else [])
    add(id=f'{sid}/index', section=sid, order=0, type='section', slug=f'/{sid}/', title=label, source=src,
        production='authored, with a generated list',
        outline=[f'Introduction of three to five lines: {line}',
                 'Statement of what the section does not hold and where it is kept',
                 'The pages of the section with one line each (generated)',
                 'Related sections'])


def split_doc(sid, base, src, parts, start_order):
    """parts: list of (slug or '', title, [section numbers], production-note)."""
    secs = sections_of(src)
    doc = h1(src)
    n = len(parts)
    for i, (slug, title, nums, *rest) in enumerate(parts, 1):
        words = sum(secs[x][1] for x in nums)
        full = f'/{sid}/{base}/' + (slug + '/' if slug else '')
        pid = f'{sid}/{base}' + (f'/{slug}' if slug else '')
        add(id=pid, section=sid, order=start_order + i, type='document', slug=full,
            title=doc if i == 1 and not slug else f'{doc}: {title}', source=[src], source_sections=nums,
            document=base, part=f'{i} of {n}', words=words,
            outline=None, **(rest[0] if rest else {}))


# About
split_doc('about', 'statement-of-intent', 'charter/documents/statement-of-intent.md', [
    ('', 'Intent and strategy', [1, 2, 3, 4, 5, 6, 7, 8]),
    ('strategic-priorities', 'Strategic Priorities', [9]),
    ('capability-and-maturity-roadmap', 'Capability and maturity roadmap', [10, 11]),
    ('performance-and-commitments', 'Performance and commitments', [12, 13]),
], 0)
add(id='about/aicc-charter', section='about', order=5, type='document', slug='/about/aicc-charter/', title=h1('charter/documents/aicc-charter.md'),
    source=['charter/documents/aicc-charter.md'], words=900)
add(id='about/charter-outline', section='about', order=6, type='outline', slug='/about/charter-outline/', title='The charter in outline',
    source=['charter/README.md', 'charter/executive-summary.md', 'charter/guides/README.md'], production='generated, with an authored introduction',
    outline=['Introduction: how the manual is organized and how the pages relate (authored)',
             'The document hierarchy and the contents table (from the charter README)',
             'The guides and where each is placed (from the guides README)',
             'Reading routes (reading-routes.md)',
             'Control of the charter: status, revision, and change (from the charter README)'])
add(id='about/also-stated-in', section='about', order=7, type='outline', slug='/about/also-stated-in/', title='AICC in brief: where it is stated', source=[],
    production='authored',
    outline=['Lead statements: Summary of intent (Statement of Intent 2) and Mission (AICC Charter 2)',
             'Also stated in: What AICC is (Business Model 2) and (Operating Model 2)',
             'Principles of work (Operating Model 3) and principles of adoption (Statement of Intent 5, 6)',
             'The page lists and links the statements, and restates none'])

# What AICC does
add(id='what-aicc-does/business-model', section='what-aicc-does', order=1, type='document', slug='/what-aicc-does/business-model/',
    title=h1('charter/documents/business-model.md'), source=['charter/documents/business-model.md'], words=1381)
add(id='what-aicc-does/engagement-workflow', section='what-aicc-does', order=2, type='workflow', slug='/what-aicc-does/engagement-workflow/',
    title=h1('charter/workflows/engagement.md'), source=['charter/workflows/engagement.md'], companion='what-aicc-does/engagement-guide')
add(id='what-aicc-does/engagement-guide', section='what-aicc-does', order=3, type='guide', slug='/what-aicc-does/engagement-guide/',
    title=h1('charter/guides/engagement-guide.md'), source=['charter/guides/engagement-guide.md'], companion='what-aicc-does/engagement-workflow')

# How AICC works
split_doc('how-aicc-works', 'portfolio-management-model', 'charter/documents/portfolio-management-model.md', [
    ('', 'Foundations', [1, 2, 3]),
    ('the-portfolio-loops', 'The portfolio loops', [4]),
    ('the-portfolio-kanban', 'The portfolio Kanban', [5]),
    ('the-business-case-and-the-mvp', 'The business case and the MVP', [6, 7]),
    ('levels-review-and-records', 'Levels, review, measures, and records', [8, 9]),
], 0)
split_doc('how-aicc-works', 'solution-lifecycle-model', 'charter/documents/solution-lifecycle-model.md', [
    ('', 'Foundations', [1, 2]),
    ('the-flow-of-value', 'The flow of value', [3]),
    ('backlogs-and-boards', 'Backlogs and boards', [4]),
    ('states-and-stages', 'States and Stages', [5]),
    ('the-cadence', 'The cadence', [6]),
    ('verification-release-and-acceptance', 'Verification, release, and acceptance', [7]),
    ('life-cycle-management', 'Life-cycle management', [8]),
], 10)
add(id='how-aicc-works/service-delivery-workflow', section='how-aicc-works', order=21, type='workflow', slug='/how-aicc-works/service-delivery-workflow/',
    title=h1('charter/workflows/service-delivery.md'), source=['charter/workflows/service-delivery.md'], companion='how-aicc-works/service-delivery-guide')
add(id='how-aicc-works/service-delivery-guide', section='how-aicc-works', order=22, type='guide', slug='/how-aicc-works/service-delivery-guide/',
    title=h1('charter/guides/service-delivery-guide.md'), source=['charter/guides/service-delivery-guide.md'], companion='how-aicc-works/service-delivery-workflow')
add(id='how-aicc-works/cadence-workflow', section='how-aicc-works', order=23, type='workflow', slug='/how-aicc-works/cadence-workflow/',
    title=h1('charter/workflows/cadence.md'), source=['charter/workflows/cadence.md'], companion='how-aicc-works/cadence-guide')
add(id='how-aicc-works/cadence-guide', section='how-aicc-works', order=24, type='guide', slug='/how-aicc-works/cadence-guide/',
    title=h1('charter/guides/cadence-guide.md'), source=['charter/guides/cadence-guide.md'], companion='how-aicc-works/cadence-workflow')
add(id='how-aicc-works/collaboration-tooling-workflow', section='how-aicc-works', order=25, type='workflow', slug='/how-aicc-works/collaboration-tooling-workflow/',
    title=h1('charter/workflows/collaboration-tooling.md'), source=['charter/workflows/collaboration-tooling.md'])

# Organization
split_doc('organization', 'operating-model', 'charter/documents/operating-model.md', [
    ('', 'Foundations', [1, 2, 3]),
    ('roles', 'Roles', [4]),
    ('decisions', 'Decisions', [5]),
], 0)
add(id='organization/organization-guide', section='organization', order=4, type='guide', slug='/organization/organization-guide/',
    title=h1('charter/guides/organization-guide.md'), source=['charter/guides/organization-guide.md'])
add(id='organization/roles', section='organization', order=5, type='index', slug='/organization/roles/', title='The Roles',
    source=['charter/documents/operating-model.md', 'charter/guides/organization-guide.md'], production='generated from tables',
    outline=['Introduction: a Role is named for its responsibility and not for a person (Vocabulary 3.6)',
             'The seven Roles, each with its purpose in one line (Operating Model 4.2)',
             'One page for each Role'])
ROLES = ['executive-sponsor', 'aicc-lead', 'solution-engineer', 'domain-owner', 'domain-expert', 'control-function-contact', 'platform-owner']
RNAMES = ['Executive Sponsor', 'AICC Lead', 'Solution Engineer', 'Domain Owner', 'Domain Expert', 'Control Function Contact', 'Platform Owner']
for i, (slug, name) in enumerate(zip(ROLES, RNAMES), 1):
    add(id=f'organization/roles/{slug}', section='organization', order=10 + i, type='role', slug=f'/organization/roles/{slug}/', title=name,
        source=['charter/documents/operating-model.md', 'charter/guides/organization-guide.md'], production='generated from tables',
        outline=['Purpose, main responsibilities, authority, reporting line, and typical competence (Organization guide 3)',
                 'The decisions of the Role (Operating Model 4.2) and the Decision level (Operating Model 5.3)',
                 'The RACI row of the Role (Organization guide 4)',
                 'Where the Holder is recorded: the Appointments Record (Records and systems)',
                 'The clauses that name the Role (cited by)'])

# Responsible AI
add(id='responsible-ai/ai-policy', section='responsible-ai', order=1, type='document', slug='/responsible-ai/ai-policy/',
    title=h1('charter/documents/ai-policy.md'), source=['charter/documents/ai-policy.md'], words=2155)
add(id='responsible-ai/ai-risk-control-workflow', section='responsible-ai', order=2, type='workflow', slug='/responsible-ai/ai-risk-control-workflow/',
    title=h1('charter/workflows/ai-risk-control.md'), source=['charter/workflows/ai-risk-control.md'])

# Governance
split_doc('governance', 'operating-model-governance', 'charter/documents/operating-model.md', [], 0) if False else None
for slug, title, nums, order in [('control-loops', 'The control loops', [6], 1), ('records-and-evidence', 'Records and evidence', [7], 2), ('controls', 'Controls and the control catalogue', [8], 3)]:
    secs = sections_of('charter/documents/operating-model.md')
    add(id=f'governance/{slug}', section='governance', order=order, type='catalogue' if slug == 'controls' else 'document',
        slug=f'/governance/{slug}/', title='Operating Model: ' + title, source=['charter/documents/operating-model.md'], source_sections=nums,
        document='operating-model', part='governance view', words=sum(secs[x][1] for x in nums),
        outline=(['The controls table of Operating Model 8 as a filterable list: reference, title, loop, owner, timing, type',
                  'One page for each of the 32 controls at /governance/controls/c-nn/: rule clause, owner, timing, evidence record, template, objective, type, how it is tested (Unit governance guide 7), and where it is cited',
                  'A statement that the status of each control is kept in the Control Matrix of the Registry'] if slug == 'controls' else None))
secs = sections_of('charter/documents/solution-lifecycle-model.md')
add(id='governance/delivery-records-controls-and-measures', section='governance', order=4, type='document',
    slug='/governance/delivery-records-controls-and-measures/', title='Solution Lifecycle Model: Records, controls, and measures',
    source=['charter/documents/solution-lifecycle-model.md'], source_sections=[9, 10], document='solution-lifecycle-model', part='7 of 7 (governance view)',
    words=secs[9][1] + secs[10][1])
add(id='governance/unit-governance-workflow', section='governance', order=5, type='workflow', slug='/governance/unit-governance-workflow/',
    title=h1('charter/workflows/unit-governance.md'), source=['charter/workflows/unit-governance.md'], companion='governance/unit-governance-guide')
add(id='governance/unit-governance-guide', section='governance', order=6, type='guide', slug='/governance/unit-governance-guide/',
    title=h1('charter/guides/unit-governance-guide.md'), source=['charter/guides/unit-governance-guide.md'], companion='governance/unit-governance-workflow')

# Library
TEMPLATES = ['initiative-brief', 'service-agreement', 'solution-definition', 'acceptance-checklist', 'control-sign-off', 'decision-record',
             'steering-summary', 'outcome-report', 'ai-incident-review', 'registry-snapshot', 'quarterly-report', 'appointments-record', 'proposal']
for i, f in enumerate(TEMPLATES, 1):
    add(id=f'library/{f}', section='library', order=i, type='template', slug=f'/library/{f}/', title=h1(f'charter/templates/{f}.md'),
        source=[f'charter/templates/{f}.md'])

# Reference
add(id='reference/vocabulary', section='reference', order=1, type='reference', slug='/reference/vocabulary/', title=h1('charter/documents/vocabulary.md'),
    source=['charter/documents/vocabulary.md'], words=4674,
    outline=['Purpose, precedence, and style (Vocabulary 1 to 3)', 'The defined terms as an index by letter and as a table', 'For each term: the pages where it is used (generated)'])
add(id='reference/document-catalog', section='reference', order=2, type='document', slug='/reference/document-catalog/', title=h1('charter/documents/document-catalog.md'),
    source=['charter/documents/document-catalog.md'], words=1519)
add(id='reference/change-history', section='reference', order=3, type='reference', slug='/reference/change-history/', title='Change history',
    source=['charter/documents/document-catalog.md'], production='generated',
    outline=['Introduction: the baseline and how a change is recorded (Document Catalog 3, 4)',
             'For each document: revision, date, change, decision reference (from its change-log table)',
             'A link from each row to the document page'])
add(id='reference/records-and-systems', section='reference', order=4, type='records', slug='/reference/records-and-systems/', title='Records and systems',
    source=['charter/documents/operating-model.md', 'charter/documents/document-catalog.md', 'charter/templates/README.md', 'registry/README.md'],
    production='authored from sources',
    outline=['Introduction: the manual is static; the live records are kept in other systems',
             'Table: record, template, system of record, control that it evidences, who keeps it',
             'Statement of what the site does not hold',
             'Links to the Registry, Jira, Confluence, and Service Management (to be confirmed)'])

# ---- write
SEC_ORDER = {s[0]: i for i, s in enumerate(SECTIONS, 1)}
pages_json = []
for p in PAGES:
    d = {k: v for k, v in p.items() if v is not None}
    pages_json.append(d)
json.dump({'status': 'scaffold', 'baseline': '1.0', 'baseline_date': '2026-10-02', 'source_language': 'en',
           'sections': [{'id': a, 'order': i, 'label': b, 'summary': c} for i, (a, b, c) in enumerate(SECTIONS, 1)],
           'pages': pages_json}, open(os.path.join(SCAF, 'sitemap.json'), 'w'), indent=1, ensure_ascii=False)

import shutil
shutil.rmtree(os.path.join(SCAF, 'pages'), ignore_errors=True)
TYPE_ELEMENTS = {
    'document': ['Header: title, purpose, revision, date, owner', 'The parts of the document, with the current part marked (for a split document)', 'Outline of the page (the headings below)',
                 'Clauses with permanent links and a cited-by line', 'Related pages', 'Change history (from the change-log table)', 'Previous and next'],
    'workflow': ['Header: title, purpose', 'Diagram with its text version and clause links', 'Steps table: who, when, record, clause', 'Situations',
                 'Companion guide and the templates that the workflow uses', 'Previous and next'],
    'guide': ['Header: title, purpose', 'Diagrams with text versions', 'Tables', 'Rule source', 'Companion workflow where there is one', 'Previous and next'],
    'template': ['Header: title, id, revision', 'When it is used and where the record is kept', 'The form, with a copy button', 'The clause that requires it',
                 'The workflows that use it', 'Previous and next'],
}


def fname(p):
    sec = p['section'] or ''
    if p['id'] == 'index':
        return os.path.join('pages', 'index.md')
    return os.path.join('pages', sec, p['id'].split('/', 1)[1].replace('/', '--') + '.md') if not p['id'].endswith('/index') else os.path.join('pages', sec, 'index.md')


for p in PAGES:
    path = os.path.join(SCAF, fname(p))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fm = ['---', f"id: {p['id']}", f"title: {p['title']}", f"section: {p['section'] or 'home'}", f"order: {p['order']}", f"type: {p['type']}", f"slug: {p['slug']}"]
    if p.get('source'):
        fm.append('source: ' + '; '.join(p['source']))
    if p.get('source_sections'):
        fm.append('source_sections: ' + ', '.join(str(x) for x in p['source_sections']))
    if p.get('document'):
        fm.append(f"document: {p['document']}")
    if p.get('part'):
        fm.append(f"part: {p['part']}")
    if p.get('words'):
        fm.append(f"words: {p['words']}")
    if p.get('companion'):
        fm.append(f"companion: {p['companion']}")
    fm.append(f"production: {p['production']}")
    fm += ['status: scaffold', '---']
    body = fm + ['', f"# {p['title']}", '', f"Page type: {p['type']}. Address: {p['slug']}", '']
    if p.get('source'):
        body += ['## Source', '']
        for s in p['source']:
            body.append(f'- {s}')
        body.append('')
    if p.get('source_sections'):
        secs = sections_of(p['source'][0])
        body += ['## Sections of the source', '']
        for n in p['source_sections']:
            body.append(f'- {n}. {secs[n][0]} ({secs[n][1]} words)')
        body.append('')
    body += ['## Outline', '']
    if p.get('outline'):
        for o in p['outline']:
            body.append(f'- {o}')
    elif p['type'] in TYPE_ELEMENTS:
        body.append('Elements: ' + '; '.join(TYPE_ELEMENTS[p['type']]) + '.')
        if p['type'] in ('workflow', 'guide') and p['source']:
            body += ['', 'Headings of the source:', '']
            for line in read(p['source'][0]).splitlines():
                if line.startswith('## ') and not line.startswith('## Change log'):
                    body.append(f'- {line[3:].strip()}')
    body.append('')
    open(path, 'w', encoding='utf-8').write('\n'.join(body).rstrip('\n') + '\n')

# inventory
labels = {s[0]: s[1] for s in SECTIONS}
rows = ['# Inventory of the pages', '', 'Made by make_pages.py from the page definitions. Every part of the charter appears once as a canonical page. A page that is a view for another section is marked in the part column.', '',
        '| Section | Page | Address | Type | Source | Sections | Words | Production |', '| --- | --- | --- | --- | --- | --- | --- | --- |']
for p in sorted(PAGES, key=lambda x: (SEC_ORDER.get(x['section'], 0), x['order'], x['id'])):
    src = '; '.join(s.replace('charter/', '') for s in p.get('source', [])) or 'none'
    nums = ', '.join(str(x) for x in p.get('source_sections', [])) or 'all' if p.get('source') else 'none'
    rows.append(f"| {labels.get(p['section'], 'Home')} | {p['title']} | {p['slug']} | {p['type']} | {src} | {nums} | {p.get('words', '')} | {p['production']} |")
open(os.path.join(SCAF, 'inventory.md'), 'w').write('\n'.join(rows) + '\n')
print(len(PAGES), 'pages')
