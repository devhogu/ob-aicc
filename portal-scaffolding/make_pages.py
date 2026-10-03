#!/usr/bin/env python3
"""Make sitemap.json, inventory.md, and the outline file of every page from the page definitions below.

Edit the definitions, run `python3 portal-scaffolding/make_pages.py`, and then `python3 portal-scaffolding/check.py`.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAF = os.path.join(ROOT, 'portal-scaffolding')

# Two layouts are defined. The layout in use, adopted on 2026-10-02, presents AICC as a consulting organization with a Services section
# and a Knowledge base. The previous layout (`--previous`, written to previous/) is the first structure of the site, kept for the record.
NEXT = '--previous' not in sys.argv
OUT = SCAF if NEXT else os.path.join(SCAF, 'previous')
S_SERVICES = 'services' if NEXT else 'what-aicc-does'
S_PORTFOLIO = 'portfolio' if NEXT else 'how-aicc-works'
S_DELIVERY = 'delivery' if NEXT else 'how-aicc-works'

SECTIONS = [
    ('about', 'About AICC', 'The intent, the strategy, the mandate, the values, and the place of AICC in the Bank; what we do and how we work in one page each.'),
    ('responsible-ai', 'Responsible AI', 'A short course on AI today, its opportunities, its risks, and what responsible use means; and the rules of the Bank: the AI Policy, the Risk Tiers, and the gates before use.'),
    ('services', 'Services', 'The service catalog of AICC: the service lines, how a function engages AICC, the service levels, and what AICC does not do.'),
    ('portfolio', 'Portfolio', 'How AICC decides which Initiatives to take in, fund, continue, defer, or reject: the strategic inputs, the portfolio loops, the Kanban, the business case, and the MVP.'),
    ('delivery', 'Delivery', 'How AICC delivers: the flow of value, the backlogs, the states, the cadence, verification and release, and the life cycle of a Solution.'),
    ('governance', 'Governance', 'How AICC is directed, controlled, reported, and assured as a unit: decision rights, the control loops, the Steerings, the controls, the records and evidence, the measures.'),
    ('organization', 'Organization', 'The Roles, the decision levels, and the bodies of AICC.'),
    ('knowledge-base', 'Knowledge base', 'The templates, the guides, the acts and compliance, and the publications of AICC.'),
    ('reference', 'Reference', 'The Vocabulary, the Document Catalog, the change history, the systems that hold the records, the industry body of knowledge, and the regulators and acts.'),
] if NEXT else [
    ('about', 'About AICC', 'The intent, the purpose, the mandate, and the place of AICC in the Bank.'),
    ('what-aicc-does', 'What AICC does', 'The services that AICC offers, how a function engages AICC, and the Solutions that AICC delivers.'),
    ('how-aicc-works', 'How AICC works', 'The method: how Initiatives are taken in, decided, delivered, paced, and measured.'),
    ('organization', 'Organization', 'The Roles, the decision levels, and the bodies of AICC.'),
    ('responsible-ai', 'Responsible AI', 'The rules for the use of AI, the Risk Tiers, and the gates before use.'),
    ('governance', 'Governance and oversight', 'The control loops, the records, the controls, and the way AICC is reported and assured.'),
    ('library', 'Library', 'The templates, the forms of the records that AICC produces.'),
    ('reference', 'Reference', 'The Vocabulary, the Document Catalog, the change history, and the systems that hold the records.'),
]
S_LIBRARY = 'knowledge-base' if NEXT else 'library'


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
    src = ['charter/workflows/README.md'] if sid in ('how-aicc-works', 'delivery') else (['charter/templates/README.md'] if sid in ('library', 'knowledge-base') else [])
    add(id=f'{sid}/index', section=sid, order=0, type='section', slug=f'/{sid}/', title=label, source=src,
        production='authored, with a generated list',
        outline=[f'Introduction of three to five lines: {line}',
                 'Statement of what the section does not hold and where it is kept',
                 'The pages of the section with one line each (generated)',
                 'Related sections'])


def split_doc(sid, base, src, parts, start_order, type_='document', series=None, series_title=None, tabs=None, part_offset=0, part_total=None, **extra):
    """parts: list of (slug or '', title, [section numbers], production-note). A workflow or a guide is split the same way as a document;
    with a series, the parts are shown as tabs and the series may join a workflow and its guide under one navigation entry."""
    secs = sections_of(src)
    doc = h1(src)
    n = part_total or len(parts)
    for i, (slug, title, nums, *rest) in enumerate(parts, 1):
        words = sum(secs[x][1] for x in nums)
        full = f'/{sid}/{base}/' + (slug + '/' if slug else '')
        pid = f'{sid}/{base}' + (f'/{slug}' if slug else '')
        kw = dict(rest[0]) if rest else {}
        if series:
            kw.update(series=series, series_title=series_title or doc, tab=(tabs[i - 1] if tabs else title))
        kw.update(extra)
        add(id=pid, section=sid, order=start_order + i, type=type_, slug=full,
            title=doc if i == 1 and not slug else f'{doc}: {title}', source=[src], source_sections=nums,
            document=base, part=f'{part_offset + i} of {n}', words=words,
            outline=None, **kw)


# About
split_doc('about', 'statement-of-intent', 'charter/documents/statement-of-intent.md', [
    ('', 'Intent and strategy', [1, 2, 3, 4, 5, 6, 7, 8]),
    ('strategic-priorities', 'Strategic Priorities', [9]),
    ('capability-and-maturity-roadmap', 'Capability and maturity roadmap', [10, 11]),
    ('performance-and-commitments', 'Performance and commitments', [12, 13]),
], 0)
add(id='about/strategy', section='about', order=5, type='outline', slug='/about/strategy/', title='Strategy', source=[], production='authored, with tables generated from the Statement of Intent',
    outline=['The strategy of the Bank: its mission and the four Strategic Pillars, and the contribution of AI to each (Statement of Intent 3)',
             'The AI adoption strategy: the seven Strategic Priorities (Statement of Intent 9) and the areas of application (8)',
             'The strategy across the aspects of AICC: commercial, investment, portfolio, adoption, delivery, solutions, platform and data, people, providers, risk, measures',
             'The road: the Maturity Roadmap and its measures (Statement of Intent 11)',
             'How the strategy is set and kept: the strategic loop, the portfolio review, the reporting (Portfolio Management Model 4, AICC Charter 7)'])
add(id='about/aicc-charter', section='about', order=6, type='document', slug='/about/aicc-charter/', title=h1('charter/documents/aicc-charter.md'),
    source=['charter/documents/aicc-charter.md'], words=900)
if NEXT:
    add(id='about/what-we-do', section='about', order=7, type='outline', slug='/about/what-we-do/', title='What we do', source=['portal/content/about/what-we-do.md'], production='authored',
        outline=['One page: AICC as the internal consulting and innovation lab of the Bank; research and consulting across strategy, programs, solutions, and ways of working',
                 'The service lines in one line each, with a link to the Services section',
                 'What AICC is not: no AI Platform, no business results of a Domain, no Control Function rules, no validation of its own work, no delivery at scale (AICC Charter 3.2)'])
    add(id='about/how-we-work', section='about', order=8, type='outline', slug='/about/how-we-work/', title='How we work', source=['portal/content/about/how-we-work.md'], production='authored',
        outline=['One page: the engagement model (a need, a study, a Service Agreement, delivery, an Outcome Report, support)',
                 'The method in brief: Portfolio decides, Delivery builds in small steps on a cadence, quality and control in the flow',
                 'Links to the Portfolio and Delivery sections and to the Engagement workflow and guide'])
add(id='about/values-and-principles', section='about', order=9 if NEXT else 7, type='outline', slug='/about/values-and-principles/', title='Values and principles', source=[],
    production='generated from the documents, with an authored statement of what each group applies to',
    outline=['Values: integrity, prudence, and respect for people (Statement of Intent 4)',
             'Principles of adoption (Statement of Intent 5) and of application (Statement of Intent 6)',
             'Principles of work (Operating Model 3) and of delivery (Solution Lifecycle Model 2)',
             'Each group states what it applies to, and links to its clause'])
add(id='about/charter-outline', section='about', order=10 if NEXT else 8, type='outline', slug='/about/charter-outline/', title='Explore AICC',
    source=['charter/README.md', 'charter/executive-summary.md', 'charter/guides/README.md'], production='generated, with an authored introduction',
    outline=['Introduction: how the manual is organized and how the pages relate (authored)',
             'The document hierarchy and the contents table (from the charter README)',
             'The guides and where each is placed (from the guides README)',
             'Reading routes (reading-routes.md)',
             'Control of the charter: status, revision, and change (from the charter README)'])

# Legal pages of the portal, authored in portal/content, last in the left navigation and linked from the footer
add(id='privacy', section=None, order=90, type='legal', slug='/privacy/', title='Privacy', source=['portal/content/privacy.md'], production='authored; aligned with the Operating Model 7 and the collaboration tooling workflow',
    outline=['What the site collects: no cookies, no analytics, search in the browser, one theme preference in browser storage, the gateway session, server logs, the repository',
             'Feedback and contact by email', 'Links from the site: the corporate share only, no external links', 'Persons named on the site: Roles, not persons; no data of the Bank', 'Questions and revision'])
add(id='terms-of-use', section=None, order=91, type='legal', slug='/terms-of-use/', title='Terms of use', source=['portal/content/terms-of-use.md'], production='authored; aligned with the Operating Model 7, the AI Policy 2, and the collaboration tooling workflow',
    outline=['Scope and access', 'Information of the Bank and ownership', 'Standing of the pages: generated and authored, the document prevails, the regulatory pages are orientation, the live records are elsewhere, no right arises from a page',
             'Use of the site, the external sources, and AI tools under the AI Policy', 'How the site is kept: the AICC Lead, the life cycle of the charter, the yearly review, the access review', 'Changes and contact'])

# What AICC does (current) / Services (next)
S = S_SERVICES
if NEXT:
    # The service lines, one page each, authored for the site from the Business Model, the Solution Lifecycle Model, and the Statement of Intent.
    # Each page: what it is, what the client receives, the typical shape, what it leads to, the templates, who decides, the governing clauses.
    # The service categories, in four areas. Each category page is authored for the site: what it is, examples, what the function receives,
    # how it runs, what it leads to, the Package, run-rate work or an Initiative, who decides, rule source.
    AREAS = [
        ('advise', 'Advise and formulate', [
            ('strategy-and-governance', 'Strategy and governance', 'Strategy, charter, operating and governance model, portal and repository of a function or an Initiative, drafted with AI, as AICC did for itself', 'Business Model 2.4, 4.5, and 4.10'),
            ('normatives-and-processes', 'Normatives and processes', 'Policies, procedures, regulations, runbooks, and process descriptions drafted, aligned, and maintained with AI for a function', 'Business Model 4.5 and 4.10'),
            ('research-and-exploration', 'Research and exploration', 'Regulatory and technology watch with digests, trials in the Lab, partnering with organizations and providers', 'Business Model 2.3, 4.5, 4.11; Statement of Intent 10.5'),
            ('business-cases-and-scenarios', 'Business cases and scenarios', 'The discovery of needs, scenarios with their problem, Solution, and leading indicators, the audit of readiness and of sources, and the business case the Portfolio decides on', 'Business Model 3, 4.1; Portfolio Management Model 5, 6'),
        ]),
        ('build', 'Build and run', [
            ('knowledge-services', 'Knowledge services', 'The corpus of a function, and the state and regulator documents it works with, as a governed knowledge base it can ask', 'Statement of Intent 5.3, 9.5, 10.2; AI Policy 2, 3'),
            ('workplace-automation', 'Workplace automation', 'Routing, forms, reports, consolidation, documents from templates, and case assistance, done with AI and reviewed by a person', 'Statement of Intent 9.4; AI Policy 2, 3'),
            ('analytics-and-decision-support', 'Analytics and decision support', 'Pipelines, dashboards, analyses, and research tooling that prepare the factual base for decisions, with lineage to governed sources', 'Statement of Intent 9.3, 10.2; Business Model 6'),
            ('content-management', 'Content management', 'Public, investor, and management material generated from governed data and templates, and the templates, editions, versions, and languages behind it', 'Statement of Intent 9.3; Operating Model 4.2'),
            ('platforms', 'Platforms', 'The shared engines and environments that AICC builds, the requirements of AICC on the AI Platform, and the Handover of an engine to an IT function of the Bank', 'AICC Charter 3.2; Statement of Intent 10.3; Solution Lifecycle Model 8'),
        ]),
        ('enablement', 'Enablement', [
            ('training-and-knowledge-sharing', 'Training and knowledge sharing', 'Training by role, coaching at the workplace, skill libraries, communities of practice, playbooks and publications', 'Business Model 4.4; Statement of Intent 10.1'),
            ('adoption-and-lifecycle-management', 'Adoption and lifecycle management', 'Domain Experts and adoption plans per Domain; the Handover, support, revision, and retirement of Solutions; the life and operation of a Service', 'Statement of Intent 10.1; Solution Lifecycle Model 8; Business Model 4.2'),
        ]),
        ('assurance', 'Assurance', [
            ('policies-controls-criteria', 'Policies, controls, criteria', 'Rules of use within the AI Policy, control maps, acceptance and evaluation criteria, guardrails, stated before the build', 'AI Policy 2, 3; Operating Model 8; Solution Lifecycle Model 7'),
            ('assessments-and-evaluations', 'Assessments and evaluations', 'Solutions and providers evaluated against the cases of the function before use, and the readiness of a function assessed; the check of a provider stays with the Control Function Contacts (AI Policy 4.1)', 'AI Policy 3, 4; Solution Lifecycle Model 7'),
            ('risk-tiering', 'Risk tiering', 'The Risk Tier assigned, recorded in the AI Registry, explained, and reassessed when the use changes', 'AI Policy 3; Operating Model 4.4; AICC Charter 5'),
            ('oversight', 'Oversight', 'Adopted Solutions, the review of the Solutions in use, AI Incidents, and changes followed through the Registry and reported in the Quarterly Report', 'Business Model 2.3; AI Policy 5; AICC Charter 7'),
        ]),
    ]
    # The section page is the overview of the areas (part 1 of the series 'service-areas'); one page per area follows (parts 2 to 5).
    # The categories of an area form a series of their own, with tabs among them, and are reached from the area page, not from the navigation.
    AREA_SLUG = {'advise': 'advise-and-formulate', 'build': 'build-and-run', 'enablement': 'enablement', 'assurance': 'assurance'}
    AREA_TAB = {'advise': 'Advise and formulate', 'build': 'Build and run', 'enablement': 'Enablement', 'assurance': 'Assurance'}
    sp = next(x for x in PAGES if x['id'] == 'services/index')
    sp.update(source=['portal/content/services/areas/overview.md'], production='authored; the overview of the areas, the first part of the series',
              outline=['The four areas, each with its posture and its categories in one line', 'From the areas to an Engagement: How to engage, the catalog, the Business Model'],
              series='service-areas', series_title='Service areas', part='1 of 5', tab='Overview')
    for k, (aid, aname, cats) in enumerate(AREAS, 1):
        add(id=f'services/{AREA_SLUG[aid]}', section='services', order=k, type='outline', slug=f'/services/{AREA_SLUG[aid]}/', title=aname,
            source=[f'portal/content/services/areas/{AREA_SLUG[aid]}.md'], production='authored; generated table of the categories of the area',
            series='service-areas', series_title='Service areas', part=f'{k + 1} of 5', tab=AREA_TAB[aid],
            outline=['The posture of the area', 'The categories of the area: coverage and mode', 'How a function engages the area', 'What the area leaves behind'])
    i = 4
    for aid, aname, cats in AREAS:
        for slug, title, line, rule in cats:
            i += 1
            add(id=f'services/{slug}', section='services', order=i, type='service', slug=f'/services/{slug}/', title=title, source=[f'portal/content/services/{slug}.md'], production='authored',
                area=aid, parent=f'services/{AREA_SLUG[aid]}', series=f'service-categories-{aid}', series_title=aname, tab=title,
                outline=[f'Area: {aname}. ' + line, 'What the function receives, how it runs, and what it leads to', 'The Package; run-rate work or an Initiative; who decides', 'Rule source: ' + rule])
    add(id='services/how-to-engage', section='services', order=21, type='outline', slug='/services/how-to-engage/', title='How to engage', source=['portal/content/services/how-to-engage.md'], production='authored, with the Engagement workflow',
        series='how-to-engage', series_title='How to engage', part='1 of 3', tab='How to engage',
        outline=['The front door in six steps: contact, study, Service Agreement, delivery, Outcome Report, support (Business Model 3 to 5)',
                 'The function commits to nothing; AICC works on a best-effort basis within its capability', 'Support levels: none, on demand, agreed response targets, run by AICC, and the Solution type each gives (Engagement guide 6)',
                 'What AICC does not do (AICC Charter 3.2)', 'Links: Engagement workflow and guide, Initiative Brief, Service Agreement, Outcome Report'])
    add(id='services/catalog', section='services', order=24, type='outline', slug='/services/catalog/', title='Service catalog',
        source=['portal/content/services/catalog-form.md'], production='authored; the form of the catalog; the live catalog is an instance kept in the Portfolio (portfolio/solutions, portfolio/packages.md) for the live portal',
        series='service-catalog', series_title='Service catalog', part='1 of 2', tab='The form of the catalog',
        outline=['The two kinds of entry: Solution and Package', 'The fields of each; the states of an entry', 'One illustration of each kind'])
    add(id='services/service-model', section='services', order=25, type='outline', slug='/services/service-model/', title='The service model', source=['portal/content/services/service-model.md'], production='authored',
        series='service-catalog', series_title='Service catalog', part='2 of 2', tab='The service model',
        outline=['The composition of a service: area and category, mode, client, Solution type, support level, Risk Tier, owner, package, records', 'The life of a service; the operation of a service; the records; the catalog'])
add(id=f'{S}/business-model', section=S, order=26 if NEXT else 1, type='document', slug=f'/{S}/business-model/',
    title=h1('charter/documents/business-model.md'), source=['charter/documents/business-model.md'], words=1381)
add(id=f'{S}/engagement-workflow', section=S, order=22 if NEXT else 2, type='workflow', slug=f'/{S}/engagement-workflow/',
    title=h1('charter/workflows/engagement.md'), source=['charter/workflows/engagement.md'], companion=f'{S}/engagement-guide',
    **({'series': 'how-to-engage', 'series_title': 'How to engage', 'part': '2 of 3', 'tab': 'Engagement workflow'} if NEXT else {}))
add(id=f'{S}/engagement-guide', section=S, order=23 if NEXT else 3, type='guide', slug=f'/{S}/engagement-guide/',
    title=h1('charter/guides/engagement-guide.md'), source=['charter/guides/engagement-guide.md'], companion=f'{S}/engagement-workflow',
    **({'series': 'how-to-engage', 'series_title': 'How to engage', 'part': '3 of 3', 'tab': 'Guide: Engagement'} if NEXT else {}))

# How AICC works (current) / Portfolio and Delivery (next)
split_doc(S_PORTFOLIO, 'portfolio-management-model', 'charter/documents/portfolio-management-model.md', [
    ('', 'Foundations', [1, 2, 3]),
    ('the-portfolio-loops', 'The portfolio loops', [4]),
    ('the-portfolio-kanban', 'The portfolio Kanban', [5]),
    ('the-business-case-and-the-mvp', 'The business case and the MVP', [6, 7]),
    ('levels-review-and-records', 'Levels, review, measures, and records', [8, 9]),
], 10 if NEXT else 0)
split_doc(S_DELIVERY, 'solution-lifecycle-model', 'charter/documents/solution-lifecycle-model.md', [
    ('', 'Foundations', [1, 2]),
    ('the-flow-of-value', 'The flow of value', [3]),
    ('backlogs-and-boards', 'Backlogs and boards', [4]),
    ('states-and-stages', 'States and Stages', [5]),
    ('the-cadence', 'The cadence', [6]),
    ('verification-release-and-acceptance', 'Verification, release, and acceptance', [7]),
    ('life-cycle-management', 'Life-cycle management', [8]),
], 20 if NEXT else 10)
if NEXT:
    # A workflow and its guide form one series: the heavy ones split at their sections, the parts shown as tabs, one entry in the navigation.
    split_doc('delivery', 'service-delivery-workflow', 'charter/workflows/service-delivery.md', [
        ('', 'Intent, levels, and states', [1, 2, 3]),
        ('the-portfolio-flow', 'The portfolio flow', [4]),
        ('the-execution', 'The execution in the Program Increment', [5]),
        ('after-delivery', 'After delivery, oversight, decisions, and where it runs', [6, 7, 8, 9]),
    ], 30, type_='workflow', series='set-service-delivery', series_title='Service delivery', tabs=['Intent and levels', 'Portfolio flow', 'Execution', 'After delivery'], part_total=6)
    split_doc('delivery', 'service-delivery-guide', 'charter/guides/service-delivery-guide.md', [
        ('', 'Purpose, levels, life, and decisions', [1, 2, 3, 4]),
        ('after-delivery', 'After delivery, situations, and rule source', [5, 6, 7]),
    ], 34, type_='guide', series='set-service-delivery', series_title='Service delivery', tabs=['Guide: flow and decisions', 'Guide: after delivery'], part_offset=4, part_total=6)
    split_doc('delivery', 'cadence-workflow', 'charter/workflows/cadence.md', [
        ('', 'Week, Iteration, Program Increment, and the IP week', [1, 2, 3, 4]),
        ('the-loops', 'The loops', [5]),
        ('what-each-event-carries', 'What each event carries', [6]),
        ('rules-calendar-and-light-mode', 'Rules, the dated calendar, light mode, and vocabulary', [7, 8, 9, 10]),
    ], 36, type_='workflow', series='set-cadence', series_title='Cadence', tabs=['Week to PI', 'Loops', 'What each event carries', 'Rules and calendar'], part_total=5)
    split_doc('delivery', 'cadence-guide', 'charter/guides/cadence-guide.md', [
        ('', 'The guide', [1, 2, 3, 4, 5, 6]),
    ], 40, type_='guide', series='set-cadence', series_title='Cadence', tabs=['Guide: Cadence'], part_offset=4, part_total=5)
else:
    add(id=f'{S_DELIVERY}/service-delivery-workflow', section=S_DELIVERY, order=21, type='workflow', slug=f'/{S_DELIVERY}/service-delivery-workflow/',
        title=h1('charter/workflows/service-delivery.md'), source=['charter/workflows/service-delivery.md'], companion=f'{S_DELIVERY}/service-delivery-guide')
    add(id=f'{S_DELIVERY}/service-delivery-guide', section=S_DELIVERY, order=22, type='guide', slug=f'/{S_DELIVERY}/service-delivery-guide/',
        title=h1('charter/guides/service-delivery-guide.md'), source=['charter/guides/service-delivery-guide.md'], companion=f'{S_DELIVERY}/service-delivery-workflow')
    add(id=f'{S_DELIVERY}/cadence-workflow', section=S_DELIVERY, order=23, type='workflow', slug=f'/{S_DELIVERY}/cadence-workflow/',
        title=h1('charter/workflows/cadence.md'), source=['charter/workflows/cadence.md'], companion=f'{S_DELIVERY}/cadence-guide')
    add(id=f'{S_DELIVERY}/cadence-guide', section=S_DELIVERY, order=24, type='guide', slug=f'/{S_DELIVERY}/cadence-guide/',
        title=h1('charter/guides/cadence-guide.md'), source=['charter/guides/cadence-guide.md'], companion=f'{S_DELIVERY}/cadence-workflow')
add(id=f'{S_DELIVERY}/collaboration-tooling-workflow', section=S_DELIVERY, order=41 if NEXT else 25, type='workflow', slug=f'/{S_DELIVERY}/collaboration-tooling-workflow/',
    title=h1('charter/workflows/collaboration-tooling.md'), source=['charter/workflows/collaboration-tooling.md'])

if NEXT:
    # The Portfolio course: the section page is part 1; the Portfolio Management Model follows as the rule.
    PCOURSE = [
        ('overview', 'The Portfolio', 'Overview', 'What the Portfolio is: a commercial decision body and a control loop; one picture end to end; the principles; the lean portfolio management practice it follows'),
        ('strategy-and-investment', 'Strategy and investment', 'Strategy and investment', 'The Strategic Priorities, the Investment Envelopes, the Investment Guardrails; who decides what; how the frame is renewed'),
        ('the-flow', 'The flow: the portfolio Kanban', 'The flow', 'The seven steps with exit criteria, deciders, and records; the four outcomes at a gate; discovery and the MVP; the limit on the Active Initiatives; the states'),
        ('the-lanes-and-the-front-door', 'The modes and the front door', 'Modes', 'Run-rate work and the Initiative; the categories by mode; screening at the front door; the Portfolio at a glance'),
        ('the-business-case-and-the-mvp', 'The business case and the MVP', 'Business case and MVP', 'The one-page Initiative Brief and its five questions; the clearance of the Control Functions; the ranking; the MVP and the decision after it'),
        ('the-loops-and-governance', 'The loops and the governance', 'Loops and governance', 'The four loops; how they nest; the Portfolio as a control loop; the forums'),
        ('measures-and-tracking', 'Measures and tracking', 'Measures', 'The outcome of an Initiative: the hypothesis, the leading indicators, the MVP as the first test, the Capabilities as the means, the confirmed benefit; the flow measures of lean practice; what each loop reads; how it is tracked'),
        ('roles-and-records', 'Roles and records', 'Roles and records', 'The roles in the Portfolio; the records; the Portfolio at a glance'),
    ]
    for i, (slug, title, tab, line) in enumerate(PCOURSE, 1):
        if i == 1:
            sp = next(x for x in PAGES if x['id'] == 'portfolio/index')
            sp.update(source=[f'portal/content/portfolio/{slug}.md'], production='authored; the first part of the course, explanatory, the Portfolio Management Model is the rule', outline=[line],
                      series='portfolio-course', series_title='The Portfolio', part=f'{i} of {len(PCOURSE)}', tab=tab)
            continue
        add(id=f'portfolio/{slug}', section='portfolio', order=i, type='outline', slug=f'/portfolio/{slug}/', title=title,
            source=[f'portal/content/portfolio/{slug}.md'], production='authored; explanatory, the Portfolio Management Model is the rule', outline=[line],
            series='portfolio-course', series_title='The Portfolio', part=f'{i} of {len(PCOURSE)}', tab=tab)
    add(id='delivery/experiment-workflow', section='delivery', order=42, type='outline', slug='/delivery/experiment-workflow/', title='The Experiment workflow: the Lab',
        source=['portal/content/delivery/experiment-workflow.md'], production='authored; proposed for Solution Lifecycle Model 7; draws on Cloud LAB',
        outline=['Six stages: define, establish, prepare data, build, validate, decide, with concerns and records', 'The rules of the Lab: decision rights, data, time-box, guardrails scorecard'])
    add(id='delivery/life-of-a-service', section='delivery', order=43, type='outline', slug='/delivery/life-of-a-service/', title='The life of a Service',
        source=['portal/content/delivery/life-of-a-service.md'], production='authored; proposed for Solution Lifecycle Model 8; draws on STS',
        outline=['Seven states with question, signals, action, gate', 'The reviews', 'The hand-over to scale'])
    add(id='delivery/service-operations', section='delivery', order=44, type='outline', slug='/delivery/service-operations/', title='Service operations',
        source=['portal/content/delivery/service-operations.md'], production='authored; the run-book template of a Service; draws on STS',
        outline=['The practices: request, incident, problem, change, knowledge, service level, financial, supplier', 'The classes of service', 'The health of a Service', 'Sizing for a small unit'])

if NEXT:
    # The Delivery course: the section page is part 1; the Solution Lifecycle Model follows as the rule.
    DCOURSE = [
        ('overview', 'Delivery', 'Overview', 'What delivery is; one picture, the stream and the loops; the principles; the lean-agile practice of delivering at scale it follows'),
        ('the-flow-of-value', 'The flow of value', 'Flow of value', 'The levels of the work and their contracts; how work enters; the Team; the Stages a Feature travels'),
        ('backlogs-boards-and-kanbans', 'Backlogs, boards, and Kanbans', 'Backlogs and boards', 'The two backlogs; definition of ready and done; the four boards; how a Kanban limits the work; the Program Board; the Roadmap and the Dashboard'),
        ('the-cadence', 'The cadence: Program Increments and Iterations', 'Cadence', 'The units of the cadence; a quarter in sequence; why a fixed cadence; light mode; the cadence and the control of the unit'),
        ('events-and-rituals', 'Events and rituals', 'Events', 'Every event by level with purpose, who, input, output, record; the Steerings as interfaces; the rituals; the IP week in order'),
        ('the-loops-of-delivery', 'The loops of delivery', 'Loops', 'The control loop at each level, drawn; the exploration, build, and release loops; the feedback loops; why loops rather than a plan'),
        ('quality-verification-and-release', 'Quality, verification, and release', 'Quality and release', 'The gates in order, drawn; the test by another; the check or validation by Risk Tier; the three acceptances; deployment and release; built-in quality'),
        ('life-cycle-management', 'Life-cycle management', 'Life cycle', 'The three types; the operating loop; support; change; retirement; Adopted Solutions'),
        ('measures-and-tracking', 'Measures and tracking', 'Measures', 'What each loop reads; the flow of the work; the quality of what is built; the health of what is live; the value that arrived; how it is tracked'),
        ('roles-and-records', 'Roles and records', 'Roles and records', 'The roles in delivery and their separations; the records; where each step is controlled'),
    ]
    for i, (slug, title, tab, line) in enumerate(DCOURSE, 1):
        if i == 1:
            sp = next(x for x in PAGES if x['id'] == 'delivery/index')
            sp.update(source=[f'portal/content/delivery/{slug}.md', 'charter/workflows/README.md'], production='authored; the first part of the course, explanatory, the Solution Lifecycle Model is the rule', outline=[line],
                      series='delivery-course', series_title='Delivery', part=f'{i} of {len(DCOURSE)}', tab=tab)
            continue
        add(id=f'delivery/{slug}', section='delivery', order=i, type='outline', slug=f'/delivery/{slug}/', title=title,
            source=[f'portal/content/delivery/{slug}.md'], production='authored; explanatory, the Solution Lifecycle Model is the rule', outline=[line],
            series='delivery-course', series_title='Delivery', part=f'{i} of {len(DCOURSE)}', tab=tab)
    add(id='delivery/measures-definitions-and-formulas', section='delivery', order=50, type='outline', slug='/delivery/measures-definitions-and-formulas/', title='Delivery measures: definitions and formulas',
        source=['portal/content/delivery/measures-definitions-and-formulas.md'], production='authored; the reference of the measures of the Solution Lifecycle Model 10.3, with their formulas',
        outline=['Conventions', 'Flow measures', 'Quality measures', 'Service measures of a live Solution', 'Value and predictability', 'How the measures are kept'])
    add(id='portfolio/measures-definitions-and-formulas', section='portfolio', order=20, type='outline', slug='/portfolio/measures-definitions-and-formulas/', title='Portfolio measures: definitions and formulas',
        source=['portal/content/portfolio/measures-definitions-and-formulas.md'], production='authored; the reference of the measures of the Portfolio Management Model 9.2, with their formulas, and the measures of lean practice as explanation',
        outline=['Conventions', 'Flow measures with formulas: work in progress, throughput, lead time, cycle time, Little\'s law, flow efficiency, aging, load, distribution, gate returns, predictability',
                 'Outcome measures of an Initiative: leading indicators, adoption, acceptance, cycle, benefit claimed, confirmed, confirmed against claimed', 'Portfolio economics as a profit and loss view per priority', 'Control and quality measures', 'How the measures are kept'])

# Organization
split_doc('organization', 'operating-model', 'charter/documents/operating-model.md', [
    ('', 'Foundations', [1, 2, 3]),
    ('roles', 'Roles', [4]),
    ('decisions', 'Decisions', [5]),
], 10 if NEXT else 0, **({'series': 'set-operating-model', 'series_title': 'Operating Model', 'tabs': ['Foundations', 'Roles', 'Decisions'], 'series_order': 1} if NEXT else {}))
if NEXT:
    split_doc('organization', 'organization-guide', 'charter/guides/organization-guide.md', [
        ('', 'Purpose, the place of AICC, and the Roles and their profiles', [1, 2, 3]),
        ('who-is-responsible-for-what', 'Who is responsible for what', [4]),
        ('bodies-people-and-records', 'The governing bodies, the people records, the growth of the organization, the evidence, and the rule source', [5, 6, 7, 8, 9]),
    ], 14, type_='guide', series='set-operating-model', series_title='Operating Model', tabs=['Guide: Roles and profiles', 'Guide: Who is responsible', 'Guide: Bodies and people'], series_order=3)
    OCOURSE = [
        ('overview', 'Organization', 'Overview', 'A joint team by Roles; one picture; what the organization is for; the practice it follows'),
        ('the-place-of-aicc-in-the-bank', 'The place of AICC in the Bank', 'Place in the Bank', 'Mandate and reporting line; what AICC is; what it is not; whom it works with'),
        ('the-roles', 'The Roles', 'Roles', 'The seven Roles in one line each; Hats; the rules of separation; the limits accepted while small'),
        ('who-does-what', 'Who does what', 'Who does what', 'The responsibility pattern by family of activity; how to read it'),
        ('people-and-appointments', 'People and appointments', 'Appointments', 'Who appoints whom; joining, changing, leaving; the state at the baseline'),
        ('how-the-organization-grows', 'How the organization grows', 'Growth', 'Light mode; the steps out of it; the shape as it scales'),
    ]
    for i, (slug, title, tab, line) in enumerate(OCOURSE, 1):
        if i == 1:
            sp = next(x for x in PAGES if x['id'] == 'organization/index')
            sp.update(source=[f'portal/content/organization/{slug}.md'], production='authored; the first part of the course, explanatory, the Operating Model is the rule', outline=[line],
                      series='organization-course', series_title='Organization', part=f'{i} of {len(OCOURSE)}', tab=tab)
            continue
        add(id=f'organization/{slug}', section='organization', order=i, type='outline', slug=f'/organization/{slug}/', title=title,
            source=[f'portal/content/organization/{slug}.md'], production='authored; explanatory, the Operating Model is the rule', outline=[line],
            series='organization-course', series_title='Organization', part=f'{i} of {len(OCOURSE)}', tab=tab)
else:
    add(id='organization/organization-guide', section='organization', order=4, type='guide', slug='/organization/organization-guide/',
        title=h1('charter/guides/organization-guide.md'), source=['charter/guides/organization-guide.md'])
add(id='organization/roles', section='organization', order=20 if NEXT else 5, type='index', slug='/organization/roles/', title='The Roles',
    source=['charter/documents/operating-model.md', 'charter/guides/organization-guide.md'], production='generated from tables',
    outline=['Introduction: a Role is named for its responsibility and not for a person (Vocabulary 3.6)',
             'The seven Roles, each with its purpose in one line (Operating Model 4.2)',
             'One page for each Role'])
ROLES = ['executive-sponsor', 'aicc-lead', 'solution-engineer', 'domain-owner', 'domain-expert', 'control-function-contact', 'platform-owner']
RNAMES = ['Executive Sponsor', 'AICC Lead', 'Solution Engineer', 'Domain Owner', 'Domain Expert', 'Control Function Contact', 'Platform Owner']
for i, (slug, name) in enumerate(zip(ROLES, RNAMES), 1):
    add(id=f'organization/roles/{slug}', section='organization', order=(20 if NEXT else 10) + i, type='role', slug=f'/organization/roles/{slug}/', title=name,
        source=['charter/documents/operating-model.md', 'charter/guides/organization-guide.md'], production='generated from tables',
        outline=['Purpose, main responsibilities, authority, reporting line, and typical competence (Organization guide 3)',
                 'The decisions of the Role (Operating Model 4.2) and the Decision level (Operating Model 5.3)',
                 'The RACI row of the Role (Organization guide 4)',
                 'Where the Holder is recorded: the Appointments Record (Records and systems)',
                 'The clauses that name the Role (cited by)'])

# Responsible AI
if NEXT:
    # A short course on AI for the reader of the Bank, authored for the site; the AI Policy stays the rule.
    COURSE = [
        ('understanding-ai-today', 'Understanding AI today', 'From rules to machine learning to generative AI to agents: how each is built, what it is good at, how it fails, who is accountable, with banking examples'),
        ('opportunities', 'The opportunities', 'What changed, where the value appears in a bank, what the evidence says, where the Bank looks first'),
        ('ai-in-fintech-and-digital-banking', 'AI in fintech and digital banking', 'The fintech landscape, where it uses AI and the risk beside each, what is particular to a digital bank in the region, what the financial supervisors watch, what the Bank takes from it'),
        ('risks-and-challenges', 'The risks and challenges', 'The risks machine learning always carried, the risks generative AI added, the risks agents compound, and the challenges that are not about the technology'),
        ('what-responsible-ai-means', 'What responsible AI means', 'Where the principles come from (OECD, UNESCO, NIST, ISO/IEC 42001, the EU AI Act, the Council of Europe), the seven principles converged, the practices across the life cycle, the misunderstandings'),
        ('how-the-bank-applies-it', 'How the Bank applies it', 'The risk appetite, the Risk Tiers, the rules of use, the gates before use, providers, incidents, exceptions, who does what, in plain terms; the AI Policy prevails'),
        ('ai-terms-explained', 'AI terms explained', 'The vocabulary of the technology in plain terms: kinds of system, how they are built and used, how they fail, how they are governed'),
    ]
    TABS = {'understanding-ai-today': 'AI today', 'opportunities': 'Opportunities', 'ai-in-fintech-and-digital-banking': 'Fintech', 'risks-and-challenges': 'Risks',
            'what-responsible-ai-means': 'Responsible AI', 'how-the-bank-applies-it': 'The Bank\'s rules', 'ai-terms-explained': 'Terms'}
    # The seven parts form one series with tabs above the text, as the parts of a split document. The first part is the section page itself,
    # so that Responsible AI opens on the course and not on an index; the other parts follow at their own addresses.
    for i, (slug, title, line) in enumerate(COURSE, 1):
        if i == 1:
            sp = next(x for x in PAGES if x['id'] == 'responsible-ai/index')
            sp.update(source=[f'portal/content/responsible-ai/{slug}.md'], production='authored; the first part of the course, explanatory, the AI Policy is the rule',
                      outline=[line, 'The tabs of the course above the text; the rules (AI Policy, AI risk and control workflow) below'],
                      series='responsible-ai-course', series_title='A short course on AI', part=f'{i} of {len(COURSE)}', tab=TABS[slug])
            continue
        add(id=f'responsible-ai/{slug}', section='responsible-ai', order=i, type='outline', slug=f'/responsible-ai/{slug}/', title=title,
            source=[f'portal/content/responsible-ai/{slug}.md'], production='authored; explanatory, the AI Policy is the rule', outline=[line],
            series='responsible-ai-course', series_title='A short course on AI', part=f'{i} of {len(COURSE)}', tab=TABS[slug])
add(id='responsible-ai/ai-policy', section='responsible-ai', order=11 if NEXT else 1, type='document', slug='/responsible-ai/ai-policy/',
    title=h1('charter/documents/ai-policy.md'), source=['charter/documents/ai-policy.md'], words=2155)
if NEXT:
    split_doc('responsible-ai', 'ai-risk-control-workflow', 'charter/workflows/ai-risk-control.md', [
        ('', 'Intent, the Risk Tier, and the gates before first use', [1, 2, 3]),
        ('in-operation-and-situations', 'In operation, exceptions, single decisions, an AI Incident, situations, and where it runs', [4, 5, 6, 7, 8, 9]),
    ], 12, type_='workflow', series='set-ai-risk-control', series_title='AI risk and control workflow', tabs=['Risk Tier and gates', 'In operation and situations'])
else:
    add(id='responsible-ai/ai-risk-control-workflow', section='responsible-ai', order=2, type='workflow', slug='/responsible-ai/ai-risk-control-workflow/',
        title=h1('charter/workflows/ai-risk-control.md'), source=['charter/workflows/ai-risk-control.md'])

# Governance
split_doc('governance', 'operating-model-governance', 'charter/documents/operating-model.md', [], 0) if False else None
for slug, title, nums, order in [('control-loops', 'The control loops', [6], 11 if NEXT else 1), ('records-and-evidence', 'Records and evidence', [7], 12 if NEXT else 2), ('controls', 'Controls and the control catalog', [8], 13 if NEXT else 3)]:
    secs = sections_of('charter/documents/operating-model.md')
    add(id=f'governance/{slug}', section='governance', order=order, type='catalogue' if slug == 'controls' else 'document',
        slug=f'/governance/{slug}/', title='Operating Model: ' + title, source=['charter/documents/operating-model.md'], source_sections=nums,
        document='operating-model', part='governance view', words=sum(secs[x][1] for x in nums),
        **({'series': 'set-operating-model', 'series_title': 'Operating Model', 'tab': title, 'series_order': 2} if NEXT else {}),
        outline=(['The controls table of Operating Model 8 as a filterable list: reference, title, loop, owner, timing, type',
                  'One page for each of the 32 controls at /governance/controls/c-nn/: rule clause, owner, timing, evidence record, template, objective, type, how it is tested (Unit governance guide 7), and where it is cited',
                  'A statement that the status of each control is kept in the Control Matrix of the Registry'] if slug == 'controls' else None))
secs = sections_of('charter/documents/solution-lifecycle-model.md')
add(id='governance/delivery-records-controls-and-measures', section='governance', order=14 if NEXT else 4, type='document',
    slug='/governance/delivery-records-controls-and-measures/', title='Solution Lifecycle Model: Records, controls, and measures',
    source=['charter/documents/solution-lifecycle-model.md'], source_sections=[9, 10], document='solution-lifecycle-model', part='7 of 7 (governance view)',
    words=secs[9][1] + secs[10][1])
if NEXT:
    split_doc('governance', 'unit-governance-workflow', 'charter/workflows/unit-governance.md', [
        ('', 'Intent, the loops on the Steerings, and how a decision escalates', [1, 2, 3]),
        ('events-and-sequences', 'Events, the sequences, the reporting chain, the life of a document, and where it runs', [4, 5, 6, 7, 8, 9]),
    ], 15, type_='workflow', series='set-unit-governance', series_title='Unit governance', tabs=['Loops and decisions', 'Events and sequences'], part_total=4)
    split_doc('governance', 'unit-governance-guide', 'charter/guides/unit-governance-guide.md', [
        ('', 'Purpose, mandate, the loops, how a decision moves, reporting, and the evidence', [1, 2, 3, 4, 5, 6]),
        ('the-controls', 'The controls and how to test them, and the rule source', [7, 8]),
    ], 17, type_='guide', series='set-unit-governance', series_title='Unit governance', tabs=['Guide: governance', 'Guide: the controls'], part_offset=2, part_total=4)
    GCOURSE = [
        ('overview', 'Governance', 'Overview', 'What governance is; one picture; what it is for; the practice of internal control and assurance it follows'),
        ('decisions-and-escalation', 'Decisions and escalation', 'Decisions', 'The four levels; when a decision rises; the Control Functions decide within their remit; disagreement, conflict, record'),
        ('the-control-loops', 'The control loops', 'Control loops', 'The five loops; drawn; the events the event loop catches; one cadence, three readings'),
        ('the-steerings-and-the-bodies', 'The Steerings and the bodies', 'Steerings and bodies', 'The bodies; what each Steering carries for governance; the reporting chain'),
        ('controls-and-the-catalogue', 'Controls and the control catalog', 'Controls', 'What a control is; the catalog by loop; the life of a control; deficiencies and findings'),
        ('records-evidence-and-assurance', 'Records, evidence, and assurance', 'Records and evidence', 'Three kinds of record; what makes a record evidence; how the Registry is kept; the three lines; what an auditor finds'),
        ('measures-and-reporting', 'Measures and reporting', 'Measures', 'The measures of governance; what each loop reads; the Quarterly Report; the Measures of the Maturity Levels'),
    ]
    for i, (slug, title, tab, line) in enumerate(GCOURSE, 1):
        if i == 1:
            sp = next(x for x in PAGES if x['id'] == 'governance/index')
            sp.update(source=[f'portal/content/governance/{slug}.md'], production='authored; the first part of the course, explanatory, the Operating Model is the rule', outline=[line],
                      series='governance-course', series_title='Governance', part=f'{i} of {len(GCOURSE)}', tab=tab)
            continue
        add(id=f'governance/{slug}', section='governance', order=i, type='outline', slug=f'/governance/{slug}/', title=title,
            source=[f'portal/content/governance/{slug}.md'], production='authored; explanatory, the Operating Model is the rule', outline=[line],
            series='governance-course', series_title='Governance', part=f'{i} of {len(GCOURSE)}', tab=tab)
else:
    add(id='governance/unit-governance-workflow', section='governance', order=5, type='workflow', slug='/governance/unit-governance-workflow/',
        title=h1('charter/workflows/unit-governance.md'), source=['charter/workflows/unit-governance.md'], companion='governance/unit-governance-guide')
    add(id='governance/unit-governance-guide', section='governance', order=6, type='guide', slug='/governance/unit-governance-guide/',
        title=h1('charter/guides/unit-governance-guide.md'), source=['charter/guides/unit-governance-guide.md'], companion='governance/unit-governance-workflow')

# Library (current) / Knowledge base (next)
TEMPLATES = ['initiative-brief', 'service-agreement', 'solution-definition', 'acceptance-checklist', 'control-sign-off', 'decision-record',
             'steering-summary', 'outcome-report', 'package-definition', 'ai-incident-review', 'registry-snapshot', 'quarterly-report', 'appointments-record', 'proposal']
for i, f in enumerate(TEMPLATES, 1):
    add(id=f'{S_LIBRARY}/{f}', section=S_LIBRARY, order=(20 + i) if NEXT else i, type='template', slug=f'/{S_LIBRARY}/{f}/', title=h1(f'charter/templates/{f}.md'),
        source=[f'charter/templates/{f}.md'])
if NEXT:
    # The Knowledge base as a course of six parts; the section page is the overview. The template pages follow.
    KCOURSE = [
        ('overview', 'Knowledge base', 'Overview', 'How to navigate the Knowledge base, drawn; if you need, go to; how the Knowledge base is kept'),
        ('learning-paths', 'Learning paths', 'Learning paths', 'Reading orders by role on the courses of the site: everyone, a head of function or Domain Owner, a Solution Engineer, a Domain Expert, the Executive Sponsor, a Control Function Contact, internal audit, human resources'),
        ('templates-and-forms', 'Templates and forms', 'Templates and forms', 'Which form when, along the life of an Engagement and the cycle of the unit: used when, filled by, signed by, kept in; how a form is used'),
        ('guides', 'Guides', 'Guides', 'The five guides by the question each answers, beside their subjects; the guides and the courses'),
        ('playbooks-and-lessons', 'Playbooks and lessons', 'Playbooks and lessons', 'The charter as published; the Proposals; the playbooks and method notes; the lessons; the packages'),
        ('acts-and-compliance', 'Acts and compliance', 'Acts and compliance', 'What the applicable acts and policies require of a use of AI at the Bank, and where the charter answers it'),
        ('questions-people-ask', 'Questions people ask', 'Questions', 'Short answers grounded in the charter: using AI at work, starting with AICC, risk and approval, the unit'),
    ]
    for i, (slug, title, tab, line) in enumerate(KCOURSE, 1):
        if i == 1:
            sp = next(x for x in PAGES if x['id'] == 'knowledge-base/index')
            sp.update(source=[f'portal/content/knowledge-base/{slug}.md', 'charter/templates/README.md', 'charter/guides/README.md'], production='authored; the overview of the Knowledge base', outline=[line],
                      series='knowledge-base-course', series_title='Knowledge base', part=f'{i} of {len(KCOURSE)}', tab=tab)
            continue
        if slug == 'acts-and-compliance':
            continue    # added below with its own definition
        add(id=f'knowledge-base/{slug}', section='knowledge-base', order=i, type='outline', slug=f'/knowledge-base/{slug}/', title=title,
            source=[f'portal/content/knowledge-base/{slug}.md'] + (['charter/guides/README.md'] if slug == 'guides' else []), production='authored', outline=[line],
            series='knowledge-base-course', series_title='Knowledge base', part=f'{i} of {len(KCOURSE)}', tab=tab)
    add(id='knowledge-base/acts-and-compliance', section='knowledge-base', order=6, type='outline', slug='/knowledge-base/acts-and-compliance/', title='Acts and compliance', source=['portal/content/knowledge-base/acts-and-compliance.md'],
        series='knowledge-base-course', series_title='Knowledge base', part='6 of 7', tab='Acts and compliance',
        production='authored; curated by the AICC Lead with the Control Function Contacts',
        outline=['DECISION 5: new content, not in the charter. The acts, regulations, and internal policies that apply to the use of AI at the Bank, and what each requires of a Solution',
                 'For each: the act or policy, who oversees it, what it requires, where the AI Policy and the controls answer it', 'Links to the Reference page Regulators and acts for the bodies and the texts'])
    # The Reference as tabs: the overview, then the four outward shelves; the charter's own references follow in the navigation.
    sp = next(x for x in PAGES if x['id'] == 'reference/index')
    sp.update(source=['portal/content/reference/overview.md'], production='authored; the overview of the Reference', outline=['How to navigate the Reference, drawn; how to take an external source; using external resources safely; the categories'],
              series='reference-course', series_title='Reference', part='1 of 5', tab='Overview')
    add(id='reference/industry-body-of-knowledge', section='reference', order=1, type='outline', slug='/reference/industry-body-of-knowledge/', title='Standards and frameworks', source=['portal/content/reference/industry-body-of-knowledge.md'],
        production='authored; a curated list', series='reference-course', series_title='Reference', part='2 of 5', tab='Standards and frameworks',
        outline=['How to take a principle, a standard, a framework, a practice', 'The principles governments agreed; the standards and frameworks for AI; the practice of the financial sector; the practice of management and delivery, each with where the charter uses it'])
    add(id='reference/research-and-insight', section='reference', order=3, type='outline', slug='/reference/research-and-insight/', title='Research and insight', source=['portal/content/reference/research-and-insight.md'],
        production='authored; a curated list', series='reference-course', series_title='Reference', part='4 of 5', tab='Research and insight',
        outline=['How to read the shelf', 'The institutions and standard-setters; the academic and independent centres; the consulting houses; the fintech and banking press; for the region', 'Each with what it publishes, why it matters, how to take it, access'])
    add(id='reference/learning-and-open-resources', section='reference', order=4, type='outline', slug='/reference/learning-and-open-resources/', title='Learning and open resources', source=['portal/content/reference/learning-and-open-resources.md'],
        production='authored; a curated list', series='reference-course', series_title='Reference', part='5 of 5', tab='Learning and open resources',
        outline=['Courses and structured learning; following the field; AI security, risk, and incidents; open tools, with care', 'Each with what it is, whom it suits, how to take it, access'])
    add(id='reference/regulators-and-acts', section='reference', order=2, type='outline', slug='/reference/regulators-and-acts/', title='Regulators and acts', source=['portal/content/reference/regulators-and-acts.md'],
        production='authored; the index of the regulation pages, curated with the Control Function Contacts', series='reference-course', series_title='Reference', part='3 of 5', tab='Regulators and acts',
        outline=['The regulators, acts, standards, and frameworks the Bank is aware of, by jurisdiction, with a page for each',
                 'The split with Acts and compliance: this page and its sub-pages position each instrument; that page states what the applicable ones require and how AICC complies'])
    REGS = [['lean-portfolio-management', 'Lean portfolio management practice', 'Global', 'Industry practice and framework']] + [["oecd-ai-principles", "OECD Principles on Artificial Intelligence", "Global", "Intergovernmental principles"], ["unesco-recommendation-ethics-ai", "UNESCO Recommendation on the Ethics of Artificial Intelligence", "Global", "Normative instrument of an international organization"], ["council-of-europe-ai-convention", "Council of Europe Framework Convention on Artificial Intelligence", "Global", "International treaty"], ["g7-hiroshima-ai-process", "G7 Hiroshima AI Process", "Global", "Voluntary international commitments"], ["iso-iec-ai-standards", "ISO/IEC standards on AI: 42001, 23894, 22989", "Global", "International standards"], ["nist-ai-rmf", "NIST AI Risk Management Framework", "United States", "Voluntary framework"], ["owasp-top-10-llm", "OWASP Top 10 for Large Language Model Applications", "Global", "Community security standard"], ["financial-standard-setters-on-ai", "The financial standard-setters on AI: FSB, BCBS, BIS", "Global", "Reports and principles of the standard-setters of finance"], ["eu-ai-act", "EU Artificial Intelligence Act", "European Union", "Regulation of the European Union"], ["eu-gdpr", "EU General Data Protection Regulation", "European Union", "Regulation of the European Union"], ["eu-dora", "EU Digital Operational Resilience Act and the guidance of the European Banking Authority", "European Union", "Regulation of the European Union and supervisory guidance"], ["us-model-risk-and-consumer-guidance", "United States supervisory guidance on model risk and on AI in credit", "United States", "Supervisory guidance of the federal banking and consumer agencies"], ["us-federal-and-state-ai-policy", "United States federal and state AI policy", "United States", "Executive policy and state legislation"], ["ru-personal-data-law", "Russian Federation: the Federal Law on Personal Data (152-FZ)", "Russian Federation", "Federal law"], ["ru-national-ai-strategy", "Russian Federation: the National Strategy for the Development of AI and the experimental legal regimes", "Russian Federation", "Presidential decree and federal laws"], ["bank-of-russia-on-ai", "Bank of Russia on artificial intelligence in the financial market", "Russian Federation", "Reports and guidance of a central bank and financial supervisor"], ["ru-ai-code-of-ethics", "Russian Federation: the Code of Ethics in the Field of AI", "Russian Federation", "Voluntary industry code"], ["kz-law-on-ai", "Kazakhstan: the Law on Artificial Intelligence and the national concept for AI", "Kazakhstan", "Law of the Republic of Kazakhstan and government concept"], ["kz-personal-data-law", "Kazakhstan: the Law on Personal Data and Their Protection", "Kazakhstan", "Law of the Republic of Kazakhstan"], ["kz-financial-regulators", "Kazakhstan: the National Bank and the Agency for Regulation and Development of the Financial Market", "Kazakhstan", "Central bank and financial supervisor"], ["aifc", "Astana International Financial Centre", "Kazakhstan", "Financial centre with its own regulatory framework"], ["nbkr", "National Bank of the Kyrgyz Republic", "Kyrgyz Republic", "Central bank and banking supervisor"], ["kg-personal-information-law", "Kyrgyz Republic: the Law on Personal Information and the authorized body for personal data", "Kyrgyz Republic", "Law of the Kyrgyz Republic and its authorized body"], ["kg-digital-development", "Kyrgyz Republic: the ministry responsible for digital development and the acts on digitalization", "Kyrgyz Republic", "Ministry and the acts and programs of digital development"], ["kg-aml-body", "Kyrgyz Republic: the financial intelligence body and the legislation against money laundering and the financing of terrorism", "Kyrgyz Republic", "Law and its authorized body"]]
    for i, (slug, title, region, kind) in enumerate(REGS, 1):
        add(id=f'reference/regulations/{slug}', section='reference', order=20 + i, type='regulation', slug=f'/reference/regulations/{slug}/', title=title,
            source=[f'portal/content/reference/regulations/{slug}.md'], production='authored; orientation only, no provision quoted; verified with the Control Function Contacts', region=region,
            outline=['Identity: kind, issuer, jurisdiction, status', 'What it sets; whom it reaches; relevance to the Bank; how the charter relates to it; related pages'])
    RESOURCES = [["bis-innovation-hub", "Bank for International Settlements and its Innovation Hub", "Research and insight"], ["imf-and-world-bank", "International Monetary Fund and the World Bank on fintech and AI", "Research and insight"], ["world-economic-forum", "World Economic Forum on AI governance and financial services", "Research and insight"], ["stanford-hai-ai-index", "Stanford Institute for Human-Centered AI: the AI Index", "Research and insight"], ["mckinsey-and-quantumblack", "McKinsey, the McKinsey Global Institute, and QuantumBlack", "Research and insight"], ["deeplearning-ai", "DeepLearning.AI: the short courses and The Batch", "Learning and open resources"], ["hugging-face", "Hugging Face: open models, datasets, and documentation", "Learning and open resources"], ["arxiv-and-papers-with-code", "arXiv and Papers with Code", "Learning and open resources"], ["mitre-atlas-and-ai-incident-database", "MITRE ATLAS and the AI Incident Database", "Learning and open resources"]]
    for i, (slug, title, shelf) in enumerate(RESOURCES, 1):
        add(id=f'reference/resources/{slug}', section='reference', order=60 + i, type='regulation', slug=f'/reference/resources/{slug}/', title=title,
            source=[f'portal/content/reference/resources/{slug}.md'], production='authored; orientation only; a listing is not an endorsement', region=shelf,
            outline=['Identity: kind, who, access', 'What it publishes; why it matters to the Bank; how to take it, and for what; cautions; related pages'])

# Reference
add(id='reference/vocabulary', section='reference', order=11 if NEXT else 1, type='reference', slug='/reference/vocabulary/', title=h1('charter/documents/vocabulary.md'),
    source=['charter/documents/vocabulary.md'], words=4674,
    outline=['Purpose, precedence, and style (Vocabulary 1 to 3)', 'The defined terms as an index by letter and as a table', 'For each term: the pages where it is used (generated)'])
add(id='reference/document-catalog', section='reference', order=12 if NEXT else 2, type='document', slug='/reference/document-catalog/', title=h1('charter/documents/document-catalog.md'),
    source=['charter/documents/document-catalog.md'], words=1519)
add(id='reference/change-history', section='reference', order=13 if NEXT else 3, type='reference', slug='/reference/change-history/', title='Change history',
    source=['charter/documents/document-catalog.md'], production='generated',
    outline=['Introduction: the baseline and how a change is recorded (Document Catalog 3, 4)',
             'For each document: revision, date, change, decision reference (from its change-log table)',
             'A link from each row to the document page'])
add(id='reference/records-and-systems', section='reference', order=14 if NEXT else 4, type='records', slug='/reference/records-and-systems/', title='Records and systems',
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
os.makedirs(OUT, exist_ok=True)
json.dump({'status': 'scaffold', 'baseline': '1.0', 'baseline_date': '2026-10-02', 'source_language': 'en',
           'sections': [{'id': a, 'order': i, 'label': b, 'summary': c} for i, (a, b, c) in enumerate(SECTIONS, 1)],
           'layout': 'next' if NEXT else 'current',
           'pages': pages_json}, open(os.path.join(OUT, 'sitemap.json'), 'w'), indent=1, ensure_ascii=False)

import shutil
os.makedirs(OUT, exist_ok=True)
shutil.rmtree(os.path.join(OUT, 'pages'), ignore_errors=True)
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
    if p['id'] == 'index' or not sec:
        return os.path.join('pages', p['id'] + '.md')
    return os.path.join('pages', sec, p['id'].split('/', 1)[1].replace('/', '--') + '.md') if not p['id'].endswith('/index') else os.path.join('pages', sec, 'index.md')


for p in PAGES:
    path = os.path.join(OUT, fname(p))
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
    if p.get('area'):
        fm.append(f"area: {p['area']}")
    if p.get('region'):
        fm.append(f"region: {p['region']}")
    if p.get('series'):
        fm.append(f"series: {p['series']}")
    if p.get('series_order'):
        fm.append(f"series_order: {p['series_order']}")
    if p.get('parent'):
        fm.append(f"parent: {p['parent']}")
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
        body.append('Elements: ' + '; '.join(TYPE_ELEMENTS.get(p['type'], TYPE_ELEMENTS['outline'] if 'outline' in TYPE_ELEMENTS else [])) + '.')
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
open(os.path.join(OUT, 'inventory.md'), 'w').write('\n'.join(rows) + '\n')
if NEXT:
    # the reading routes of the next layout: the same routes with the identifiers of the new sections
    rr = read('portal-scaffolding/reading-routes.md')
    rr = rr.replace('`library/', '`knowledge-base/')
    for a, b in (('what-aicc-does/', 'services/'), ('how-aicc-works/portfolio-management-model', 'portfolio/portfolio-management-model'), ('how-aicc-works/', 'delivery/'), ('`library/', '`knowledge-base/')):
        rr = rr.replace(a, b)
    open(os.path.join(OUT, 'reading-routes.md'), 'w').write(rr)
else:
    pass
print(len(PAGES), 'pages')
