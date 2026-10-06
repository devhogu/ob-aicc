"""Role-safe, dated operating views derived from the maintained Registry."""
# START_MODULE_CONTRACT
# PURPOSE: Project the actual portfolio without creating a second operational register.
# SCOPE: Registry validation, state/capacity mapping, bilingual summaries and scoped search.
# DEPENDS: M-PORTAL-LOCALIZATION
# LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# MAP_MODE: SUMMARY
# END_MODULE_CONTRACT
# START_MODULE_MAP
# position - map recorded states to portfolio columns, retaining Waiting context
# capacity - count shared ordinary Active and Program work against recorded limits
# project - validate maintained working records and select public progress fields
# render - compose dashboard, register, workflow and initiative summary bodies
# build - publish paired routes, assets and section-local search
# END_MODULE_MAP
from collections import Counter
from html import escape
import json
from pathlib import Path
import re
import shutil

from localization import Sources, _tables
import workspace

COLUMNS = ('Funnel', 'Reviewing', 'Analyzing', 'Portfolio Backlog', 'MVP', 'Implementation', 'Done')
OFF_FLOW = ('Deferred', 'Rejected', 'Pivoted', 'Cancelled')
BASE = 'registry/en/'


def position(state, stage='', *, waiting_from=None, dependency=None):
    """Waiting cannot be placed without its recorded previous state and dependency."""
    if state == 'Waiting':
        if not waiting_from or not dependency:
            raise ValueError('Waiting requires a recorded underlying state and Dependency')
        state = waiting_from
    if state in OFF_FLOW:
        return 'Off-flow'
    if state == 'Proposed': return 'Funnel'
    if state == 'Discovery' and stage in ('Scoping', 'Business case'):
        return 'Reviewing' if stage == 'Scoping' else 'Analyzing'
    if state == 'Approved': return 'Portfolio Backlog'
    if state == 'Active' and stage in ('MVP', 'Implementation'): return stage
    if state == 'Completed': return 'Implementation'
    if state in ('Review', 'Accepted', 'Closed'): return 'Done'
    raise ValueError(f'Unmapped portfolio state/stage: {state}: {stage}')


def capacity(items, limits, features=(), capabilities=()):
    active = sum(not x['standing'] and (x['state'] == 'Active' or
                 x['state'] == 'Waiting' and x.get('waiting_from') == 'Active') for x in items)
    def program(rows):
        progress = sum(x['State'] in ('Active', 'Completed', 'Review') or
                       x['State'] == 'Waiting' and x.get('Waiting from') in ('Active', 'Completed', 'Review') for x in rows)
        return {'progress': progress, 'ready': sum(x['State'] == 'Approved' for x in rows)}
    return {'active': active, 'limit': limits['initiative'], 'feature': program(features),
            'capability': program(capabilities), 'limits': limits}


def _sections(text):
    return {int(m[1]): m[2].strip() for m in re.finditer(r'^## ([1-6])\.[^\n]*\n(.*?)(?=^## |\Z)', text, re.M | re.S)}


def _paragraphs(text):
    text = re.sub(r'^```yaml\n.*?```\s*', '', text, flags=re.S)
    return [x.strip() for x in re.split(r'\n\s*\n', text) if x.strip()]


def _pair_paragraph(en, localized, prefix, required=True):
    original, selected = _paragraphs(en), _paragraphs(localized)
    matches = [i for i, p in enumerate(original) if p.startswith(prefix)]
    if not matches:
        if required: raise ValueError('Missing source paragraph: ' + prefix)
        return ''
    if len(original) != len(selected): raise ValueError('Public paragraph translation structure differs')
    return selected[matches[0]]


def _entry(sources, path):
    return {r['Field']: r['Entry'] for r in sources.table(path, 'Field | Entry', ('Field',))}


def _number(cell):
    match = re.search(r'\b(\d+)\b', cell)
    if not match: raise ValueError('Missing maintained WIP limit: ' + cell)
    return int(match[1])


def _plain(value):
    # Published summary fields are plain text, not Markdown links to closed evidence.
    return re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', value).replace('**', '').replace('`', '')


def project(root=workspace.ROOT, lang='en'):
    sources = Sources(root, lang); en = Sources(root, 'en')
    backlog_path = BASE + 'portfolio-backlog.md'
    canonical = en.table(backlog_path, 'Rank | Identifier')
    localized = sources.table(backlog_path, 'Rank | Identifier')
    if len({r['Identifier'] for r in canonical}) != len(canonical): raise ValueError('Duplicate initiative identity')
    dependencies = en.table(BASE + 'dependencies.md', 'Identifier | Item')
    local_deps = sources.table(BASE + 'dependencies.md', 'Identifier | Item')
    depmap = {r['Identifier']: {**t, 'state': r['Status']} for r, t in zip(dependencies, local_deps)}
    items = []
    for row, local in zip(canonical, localized):
        identifier = row['Identifier']
        files = list((Path(root) / BASE / 'initiatives').glob(identifier + '-*/brief.md'))
        if len(files) != 1: raise ValueError('Missing or ambiguous Initiative Brief: ' + identifier)
        path = files[0].relative_to(root).as_posix()
        original, translated = en.text(path), sources.text(path)
        meta, public_meta = _entry(en, path), _entry(sources, path)
        if meta['Identifier'] != identifier: raise ValueError('Brief identity mismatch: ' + identifier)
        standing = meta.get('Standing Initiative') == 'Yes'
        state, stage = row['State'], row['Stage']
        expected = state + (': ' + stage if stage else '')
        if meta['State and Stage'] != (state + '; no Stage' if standing else expected):
            raise ValueError('Backlog/Brief state disagreement: ' + identifier)
        row_priorities = re.findall(r'PRI-\d+', row['Strategic Priority'])
        if re.findall(r'PRI-\d+', meta['Strategic Priority']) != row_priorities:
            raise ValueError('Backlog/Brief priority disagreement: ' + identifier)
        sec, tr = _sections(original), _sections(translated)
        if len(sec) != 6 or len(tr) != 6: raise ValueError('Incomplete Brief structure: ' + identifier)
        waiting_from = row.get('Waiting from') or None
        dep_ids = list(dict.fromkeys(re.findall(r'DEP-\d+', sec[5])))
        if any(k not in depmap for k in dep_ids): raise ValueError('Unknown Dependency: ' + identifier)
        column = 'Standing' if standing else position(state, stage, waiting_from=waiting_from, dependency=dep_ids)
        owner = _plain(local['Domain Owner']) or UI[lang]['owner_missing']
        # The public owner is the role in the Backlog, never the named holder in a Brief.
        # Unknown/new person-bearing values fail publication instead of leaking names.
        allowed = ('Enterprise architecture lead', 'Head of the FP&A function', 'Executive Sponsor', '')
        if row['Domain Owner'] not in allowed: raise ValueError('Public owner role requires review: ' + identifier)
        scores = [row[k] for k in ('Value', 'Urgency', 'Risk or opportunity', 'Effort')]
        if any(scores) and not all(x.isdigit() and 1 <= int(x) <= 5 for x in scores):
            raise ValueError('Partial or invalid WSJF scores: ' + identifier)
        wsjf = round(sum(map(int, scores[:3])) / int(scores[3]), 2) if all(scores) else None
        outcome = _paragraphs(tr[1])[0]
        open_match = re.search(r'^Open sections: (.*)', original, re.M)
        if not open_match: raise ValueError('Open sections not recorded: ' + identifier)
        pending = _pair_paragraph(original, translated, 'Open sections:')
        if not standing:
            mvp = _pair_paragraph(sec[3], tr[3], 'Minimum viable product:')
            out_scope = _pair_paragraph(sec[3], tr[3], 'Out of scope:')
            risk = _pair_paragraph(sec[5], tr[5], 'Expected Risk Tier:')
            controls = _pair_paragraph(sec[5], tr[5], 'Control Functions', False)
            steps = [m[1].strip() for m in re.finditer(r'^\d+\. (.*)', tr[3], re.M)]
            decision_rows = en.table(path, 'Decision | By')
            approval = next(r for r in decision_rows if r['Decision'] == 'Approval of the business case')
            approval_ref = approval['Record'] or None
            if state in ('Approved', 'Active', 'Completed', 'Review', 'Accepted', 'Closed') and not approval_ref:
                raise ValueError('Approved ordinary Initiative lacks business-case record: ' + identifier)
            review_date = None
        else:
            mvp, out_scope, risk, controls, steps = '', '', '', '', []
            decision_rows = en.table(path, 'Decision | Authority and record')
            establishment = next(r for r in decision_rows if r['Decision'] == 'Establishment approval of this Brief')
            approval_ref = ', '.join(re.findall(r'DR-\d{4}-\d+', establishment['Authority and record']))
            if establishment['Result'] != 'Approved' or not approval_ref or establishment['Date'] not in row['Approved on']:
                raise ValueError('Standing approval disagreement: ' + identifier)
            review_date = next(r['Date'] for r in decision_rows if r['Decision'] == 'First recurring review') or None
        items.append({'id': identifier, 'title': _plain(public_meta['Title']), 'state': state, 'stage': stage,
                      'status': public_meta['State and Stage'], 'standing': standing, 'column': column,
                      'rank': int(row['Rank']) if row['Rank'] else None, 'priorities': row_priorities,
                      'priority': local['Strategic Priority'], 'owner': owner, 'acceptor': _plain(local['Business acceptor']),
                      'outcome': outcome, 'mvp': mvp, 'scope_steps': steps, 'out_scope': out_scope,
                      'risk': risk, 'controls': controls, 'pending': pending, 'wsjf': wsjf,
                      'dependencies': [{**depmap[k], 'id': k} for k in dep_ids], 'path': sources.resolve(path).path,
                      'stage_entered': row.get('Stage entered on') or None,
                      'waiting_from': waiting_from, 'approval_ref': approval_ref,
                      'approved_on': row['Approved on'] or None, 'active_on': row['Active on'] or None,
                      'review_date': review_date, 'agreement': public_meta['Service Agreement']})
    ordinary = sorted((x for x in items if not x['standing']), key=lambda x: x['rank'] if x['rank'] is not None else float('inf'))
    ranks = [x['rank'] for x in ordinary if x['rank'] is not None]
    if len(set(ranks)) != len(ranks): raise ValueError('Duplicate recorded rank')
    board_path = BASE + 'board.md'
    table = en.table(board_path, 'Funnel | Reviewing')
    if not table or set(table[0]) - {'_labels'} != set(COLUMNS): raise ValueError('Portfolio column structure drift')
    limits = {'initiative': _number(table[0]['MVP'])}
    if _number(table[0]['Implementation']) != limits['initiative']: raise ValueError('Shared Active limits disagree')
    board_items = {k: re.findall(r'INI-\d+', ' '.join(r[k] for r in table[1:])) for k in COLUMNS}
    projected = {k: [x['id'] for x in ordinary if x['column'] == k] for k in COLUMNS}
    if board_items != projected: raise ValueError('Portfolio Backlog/board placement disagreement')
    standing_board = en.table(board_path, 'Initiative | Service area')
    if {r['Initiative']: r['State'] for r in standing_board} != {x['id']: x['state'] for x in items if x['standing']}:
        raise ValueError('Standing board state disagreement')
    program_limit = en.table(board_path, 'Lane | Backlog (proposed, discovery, deferred)')[0]
    ready = re.fullmatch(r'(\d+) Features; (\d+) Capability', program_limit['Ready (approved)'])
    progress = re.fullmatch(r'Shared in-progress limit: (\d+) Feature and (\d+) Capability', program_limit['Active'])
    if not ready or not progress: raise ValueError('Program limits require reviewed parsing')
    limits.update(feature=int(progress[1]), capability=int(progress[2]), feature_ready=int(ready[1]), capability_ready=int(ready[2]))
    features = en.table(BASE + 'program-backlog.md', 'Rank | Identifier | Feature')
    capabilities = en.table(BASE + 'program-backlog.md', 'Identifier | Capability')
    for row in features + capabilities:
        if row['State'] == 'Waiting' and not row.get('Waiting from'):
            raise ValueError('Program Waiting requires underlying state for WIP accounting')
    dashboard_path = BASE + 'dashboard.md'
    date = re.search(r'Last updated: (\d{4}-\d{2}-\d{2})', en.text(dashboard_path))
    if not date: raise ValueError('Snapshot date not recorded')
    flow_rows = en.table(dashboard_path, 'Portfolio Kanban: Initiatives | Funnel')
    recorded_limits = next(r for r in flow_rows if r['Portfolio Kanban: Initiatives'] == 'Limit')
    if any(_number(recorded_limits[k]) != limits['initiative'] for k in ('MVP', 'Implementation')):
        raise ValueError('Dashboard/board capacity disagreement')
    reported = next(r for r in flow_rows if r['Portfolio Kanban: Initiatives'] == 'Items')
    if any(int(reported[k]) != len(projected[k]) for k in COLUMNS): raise ValueError('Dashboard/board count disagreement')
    program_report = en.table(dashboard_path, 'Program Kanban: Capabilities and Features | Backlog')
    if not features and not capabilities and any(int(v) for k, v in program_report[-1].items() if k not in ('_labels', 'Program Kanban: Capabilities and Features')):
        raise ValueError('Dashboard/Program Backlog count disagreement')
    frame = _entry(sources, dashboard_path)
    measures = sources.table(dashboard_path, 'Flow Measure | Value')
    horizons = sources.table(BASE + 'roadmap.md', 'Program Increment | Status')
    milestones = sources.table(BASE + 'roadmap.md', 'Identifier | Milestone')
    # Milestone person fields stay private: only ID, title, horizon and status are projected.
    milestones = [{k: r[k] for k in ('Identifier', 'Milestone', 'Program Increment', 'Status')} for r in milestones]
    priorities = [{k: r[k] for k in ('Identifier', 'Strategic Priority')} for r in sources.table(BASE + 'priorities.md', 'Identifier | Strategic Priority')]
    return {'lang': lang, 'date': date[1], 'frame': frame, 'items': ordinary + [x for x in items if x['standing']],
            'capacity': capacity(items, limits, features, capabilities), 'counts': {k: len(v) for k, v in projected.items()},
            'features': len(features), 'capabilities': len(capabilities), 'measures': measures,
            'horizons': horizons, 'milestones': milestones, 'priorities': priorities}

UI = {
'en': {
 'title':'Portfolio', 'subtitle':'AICC initiatives in motion', 'snapshot':'Recorded snapshot', 'recorded':'Maintained in the Registry',
 'board':'Board', 'review':'Review queue', 'standing':'Standing Initiatives', 'roadmap':'Roadmap', 'register':'Initiative register', 'selection':'Review and decisions',
 'discovery':'In discovery', 'approved':'Approved queue', 'active':'Ordinary Active', 'ordinary':'Ordinary initiatives', 'count':'initiatives',
 'owner_missing':'Domain Owner · not yet recorded', 'all':'All priorities', 'enabling':'Enabling', 'search':'Find an initiative', 'filter':'Strategic priority',
 'empty':'No recorded items', 'no_results':'No matching initiatives', 'next':'Next gate', 'owner':'Owner role', 'outcome':'Expected outcome',
 'state':'State and stage', 'rank':'Recorded order', 'score':'WSJF score', 'unknown':'Not recorded', 'age':'Stage entry / age',
 'source':'Record references', 'order':'Order follows the goals of the first 100 days. WSJF scores are shown without changing that recorded order.',
 'shared':'MVP and Implementation share one ordinary Active limit. Standing Initiatives are tracked separately; their Features share delivery capacity.',
 'capacity':'Shared delivery capacity', 'features':'Features in progress', 'ready':'Features Ready', 'capabilities':'Capabilities in progress',
 'offflow':'Deferred and other exits', 'review_intro':'Prepare the next decision with the owner. Resolve open Brief sections and missing evidence before approval.',
 'missing':'Preparation still needed', 'gate':'Gate and decision', 'decider':'Decider', 'criterion':'Before this gate',
 'mvp':'Planned MVP', 'planned':'Scope is planned; it starts after business-case approval, clearance and pull within capacity.',
 'scope':'Planned scope', 'delivery_gate':'Delivery', 'mvp_gate':'MVP decision', 'risk':'Risk and clearances', 'risk_note':'An expected Risk Tier does not establish assignment, clearance or validation.',
 'dependencies':'Dependencies', 'agreement':'Service Agreement', 'approval':'Business-case approval',
 'confirmation':'DR-2026-061 confirms a first-100-days goal. It does not approve the business case.',
 'standing_intro':'Approved service arrangements for small run-rate requests. They do not reserve four delivery slots or count against ordinary Active capacity.',
 'standing_gate':'Admit the next eligible Feature at the Weekly Review', 'standing_decider':'AICC Lead within shared Team limits',
 'standing_note':'Each Feature needs a client and Domain Owner, acceptance criteria, known dependencies, approval for its data use where AI applies, and a scope that fits one Iteration.',
 'standing_review':'Next recurring review', 'standing_approval':'Establishment approval', 'no_mvp':'No separate MVP; the work is delivered through run-rate Features.',
 'roadmap_intro':'Intent for the current Program Increment, planned work for the next, and indicative direction beyond. Milestones are not achieved outcomes.',
 'measures':'Recorded flow measures', 'measure_intro':'Missing observations remain unknown. Stage aging cannot be calculated until entry dates are recorded.',
 'workflow_intro':'Use these gates to prepare reviews of the maintained portfolio. Decisions and state changes are recorded in the Registry and then republished here.',
 'rhythm':'Review cadence', 'weekly':'Weekly Review: scope, complete Briefs, resolve blockers and raise items ready for a gate.',
 'monthly':'Monthly Steering: decide at gates, review rank and WIP, and pull within the shared limit.',
 'quarterly':'Quarterly Steering: review Active outcomes, confirmed benefit, risk and the work mix.',
 'yearly':'Yearly Steering: set Strategic Priorities, Investment Envelopes and Guardrails.',
 'authority':'Business-case authority: Domain Owner within one Domain and guardrails; Executive Sponsor for enabling work, across Domains or above a guardrail.',
 'open':'Open progress summary', 'close':'Close', 'full':'Full initiative page', 'back':'Back to portfolio', 'visible':'Matching ordinary initiatives',
 'waiting':'Waiting · retains its column and capacity place', 'source_note':'Progress summaries use public role names. Authoritative records and closed evidence remain in their maintained locations.',
},
'ru': {
 'title':'Портфель инициатив', 'subtitle':'Инициативы AICC в работе', 'snapshot':'Состояние по данным на', 'recorded':'Рабочие записи ведутся в реестре',
 'board':'Доска', 'review':'Очередь на рассмотрение', 'standing':'Постоянные инициативы', 'roadmap':'Дорожная карта', 'register':'Реестр инициатив', 'selection':'Рассмотрение и решения',
 'discovery':'На исследовании', 'approved':'Одобренная очередь', 'active':'Обычные инициативы в работе', 'ordinary':'Обычные инициативы', 'count':'инициатив',
 'owner_missing':'Владелец направления · ещё не указан', 'all':'Все приоритеты', 'enabling':'Обеспечивающая работа', 'search':'Найти инициативу', 'filter':'Стратегический приоритет',
 'empty':'Записей нет', 'no_results':'Нет подходящих инициатив', 'next':'Следующее контрольное решение', 'owner':'Роль владельца', 'outcome':'Ожидаемый результат',
 'state':'Состояние и этап', 'rank':'Порядок в реестре', 'score':'Оценка WSJF', 'unknown':'Не указано', 'age':'Дата входа в этап / возраст',
 'source':'Ссылки на рабочие записи', 'order':'Порядок соответствует целям первых 100 дней. Оценки WSJF приведены без изменения этого порядка.',
 'shared':'MVP и реализация используют общий лимит обычных инициатив в работе. Постоянные инициативы учитываются отдельно; их функциональности используют общую мощность команды.',
 'capacity':'Общая мощность команды', 'features':'Функциональности в работе', 'ready':'Функциональности в очереди Ready', 'capabilities':'Возможности в работе',
 'offflow':'Отложенные инициативы и другие выходы', 'review_intro':'Подготовьте следующее решение с владельцем. До одобрения завершите открытые разделы паспорта и соберите недостающие доказательства.',
 'missing':'Что ещё требуется подготовить', 'gate':'Контрольное решение', 'decider':'Кто решает', 'criterion':'До принятия решения',
 'mvp':'Планируемый MVP', 'planned':'Объём запланирован; работа начинается после одобрения и согласования бизнес-кейса и принятия в работу в пределах мощности команды.',
 'scope':'Планируемый объём работ', 'delivery_gate':'Поставка', 'mvp_gate':'Решение по MVP', 'risk':'Риск и согласования', 'risk_note':'Ожидаемая категория риска не означает её присвоение, согласование или валидацию.',
 'dependencies':'Зависимости', 'agreement':'Соглашение об услуге', 'approval':'Одобрение бизнес-кейса',
 'confirmation':'DR-2026-061 подтверждает цель первых 100 дней. Это не одобрение бизнес-кейса.',
 'standing_intro':'Одобренные постоянные инициативы для небольших текущих запросов. Они не резервируют четыре места в работе и не входят в лимит обычных инициатив.',
 'standing_gate':'Принять следующую подходящую функциональность на еженедельном рассмотрении', 'standing_decider':'Руководитель AICC в пределах общих лимитов команды',
 'standing_note':'Для каждой функциональности нужны заказчик и владелец направления, критерии приёмки, известные зависимости, одобрение использования данных при применении AI и объём в пределах одной итерации.',
 'standing_review':'Следующее регулярное рассмотрение', 'standing_approval':'Одобрение постоянной инициативы', 'no_mvp':'Отдельного MVP нет; работа выполняется через функциональности текущего обслуживания.',
 'roadmap_intro':'Текущий программный инкремент задаёт намерение, следующий — план, последующие — ориентир. Контрольные точки не являются достигнутыми результатами.',
 'measures':'Зафиксированные показатели потока', 'measure_intro':'Отсутствующие наблюдения остаются неизвестными. Возраст этапа нельзя рассчитать без даты входа.',
 'workflow_intro':'Контрольные решения помогают подготовить рассмотрение рабочего портфеля. Решения и изменения состояния фиксируются в реестре и затем публикуются здесь.',
 'rhythm':'Ритм рассмотрения', 'weekly':'Еженедельное рассмотрение: уточнить объём, завершить паспорта, снять блокировки и вынести готовые вопросы на решение.',
 'monthly':'Ежемесячное совещание: принять контрольные решения, проверить порядок и незавершённую работу, принять инициативу в пределах общего лимита.',
 'quarterly':'Ежеквартальное совещание: рассмотреть результаты активных инициатив, подтверждённую пользу, риск и состав работ.',
 'yearly':'Годовое совещание: определить стратегические приоритеты, инвестиционные лимиты и пороги решений.',
 'authority':'Бизнес-кейс одобряет владелец направления в пределах одного направления и порогов; куратор AICC — для обеспечивающей работы, нескольких направлений или превышения порога.',
 'open':'Открыть сводку инициативы', 'close':'Закрыть', 'full':'Полная страница инициативы', 'back':'К портфелю', 'visible':'Подходящие обычные инициативы',
 'waiting':'Ожидание · сохраняет столбец и место в мощности', 'source_note':'В сводках указаны роли. Рабочие записи и закрытые доказательства остаются в установленных местах.',
}}


def _gates(lang):
    rows = Sources(workspace.ROOT, lang).table('charter/en/documents/portfolio-management-model.md', 'Kanban step | State and Stage', ('Kanban step',))
    return {r['Kanban step']: r for r in rows}


def _h(value): return escape(_plain(str(value)))


def _route(lang, item): return f'/{lang}/initiatives/' + item['id'].lower() + '/'


def _link(url, target, label, cls=''):
    return f'<a class="{cls}" href="{workspace.relative(url, target)}">{_h(label)}</a>'


def _section(title, content, cls=''):
    return f'<section class="pf-section {cls}"><h2>{_h(title)}</h2>{content}</section>'


def _facts(pairs):
    return '<dl class="pf-facts">' + ''.join(f'<div><dt>{_h(k)}</dt><dd>{_h(v)}</dd></div>' for k, v in pairs) + '</dl>'


def summary(item, data, modal=False):
    lang = data['lang']; u = UI[lang]; g = _gates(lang).get(item['column'])
    title_tag = 'h2' if modal else 'h1'
    heading = f'<header><span class="pf-meta">{item["id"]} · {_h(item["status"])}</span><{title_tag}>{_h(item["title"])}</{title_tag}><p>{_h(item["outcome"])}</p></header>'
    facts = [(u['owner'], item['owner']), (u['rank'], item['rank'] or '—'), (u['score'], item['wsjf'] if item['wsjf'] is not None else u['unknown']),
             (u['filter'], item['priority']), (u['age'], item['stage_entered'] or u['unknown'])]
    body = heading + _facts(facts)
    if item['state'] == 'Waiting': body += '<p class="pf-notice">' + u['waiting'] + '</p>'
    if item['standing']:
        gate = _facts([(u['next'], u['standing_gate']), (u['decider'], u['standing_decider']),
                       (u['standing_approval'], (item['approved_on'] or u['unknown'])), (u['standing_review'], item['review_date'] or u['unknown'])])
        body += _section(u['gate'], gate + f'<p>{u["standing_note"]}</p><p>{u["no_mvp"]}</p>')
    elif g:
        gate = _facts([(u['next'], g['Gate']), (u['decider'], g['Decided by'])])
        body += _section(u['gate'], gate + '<p>' + _h(g['Exit criterion']) + '</p><p class="pf-muted">' + u['authority'] + '</p>')
        body += _section(u['missing'], '<p>' + _h(item['pending']) + '</p>' + _facts([(u['approval'], item['approval_ref'] or u['unknown']), (u['agreement'], item['agreement'])]))
        if not item['approval_ref']: body += f'<p class="pf-notice">{u["confirmation"]}</p>'
        scope = f'<p>{_h(item["mvp"])}</p><p class="pf-muted">{u["planned"]}</p>'
        scope += '<ol>' + ''.join('<li>' + _h(s) + '</li>' for s in item['scope_steps']) + '</ol><p>' + _h(item['out_scope']) + '</p>'
        body += _section(u['mvp'], scope)
        body += _section(u['risk'], '<p>' + _h(item['risk']) + '</p><p>' + _h(item['controls']) + '</p><p class="pf-muted">' + u['risk_note'] + '</p>')
    elif not item['standing']:
        body += _section(u['state'], f'<p>{_h(item["status"])}</p><p>{_h(item["pending"])}</p>')
    deps = '<ul class="pf-dependencies">' + ''.join(f'<li><div><strong>{d["id"]}</strong><span class="pf-badge">{_h(d["Status"])}</span></div><p>{_h(d["Needs"])}</p><small>{_h(d["From"])} · {_h(d["Needed by"])}</small></li>' for d in item['dependencies']) + '</ul>'
    body += _section(u['dependencies'], deps or '<p>' + u['unknown'] + '</p>')
    references = [item['path'], f'registry/{lang}/portfolio-backlog.md', f'registry/{lang}/dependencies.md', f'registry/{lang}/board.md']
    if item['approval_ref']: references.append(item['approval_ref'])
    body += _section(u['source'], '<p class="pf-muted">' + u['source_note'] + '</p><ul class="pf-references">' + ''.join('<li><code>' + _h(r) + '</code></li>' for r in references) + '</ul>')
    if modal:
        body = body.replace('<h2>', '<h3>').replace('</h2>', '</h3>')
        body = body.replace('<h3>', '<h2 class="pf-dialog-title">', 1).replace('</h3>', '</h2>', 1)
    return body


def _card(item, data, url, *, review=False):
    lang = data['lang']; u = UI[lang]
    next_gate = u['standing_gate'] if item['standing'] else _gates(lang).get(item['column'], {}).get('Gate', item['status'])
    labels = ' '.join([item['id'], item['title'], item['owner'], item['priority']])
    link = _link(url, _route(lang, item), item['title'], 'pf-title-link')
    link = link.replace('<a ', '<a data-pf-open="' + item['id'] + '" ', 1)
    meta = item['id'] + (f' · #{item["rank"]}' if item['rank'] else '')
    text = f'<span class="pf-status">{_h(item["status"])}</span><p class="pf-muted">{_h(item["priority"])}</p><p>{_h(item["owner"])}</p>'
    if review: text += f'<p>{_h(item["outcome"])}</p><p class="pf-muted">{_h(item["pending"])}</p>'
    if item['state'] == 'Waiting': text += '<p>' + u['waiting'] + '</p>'
    return f'<article class="pf-card" data-pf-item="{item["id"]}" data-kind="{"standing" if item["standing"] else "ordinary"}" data-priority="{" ".join(item["priorities"]) or "enabling"}" data-find="{_h(labels.casefold())}"><span class="pf-meta">{_h(meta)}</span><h3>{link}</h3>{text}<div class="pf-next"><span>{u["next"]}</span><strong>{_h(next_gate)}</strong></div></article>'


def _controls(data):
    u = UI[data['lang']]
    options = [(p['Identifier'], p['Identifier'] + ' · ' + p['Strategic Priority']) for p in data['priorities']]
    options.append(('enabling', u['enabling']))
    select = ''.join(f'<option value="{_h(k)}">{_h(v)}</option>' for k, v in options)
    return f'<div class="pf-filter" hidden><label>{u["search"]}<input type="search" data-pf-search autocomplete="off"></label><label>{u["filter"]}<select data-pf-priority><option value="">{u["all"]}</option>{select}</select></label><output data-pf-visible aria-live="polite">{u["visible"]}: {sum(not i["standing"] for i in data["items"])}</output></div>'


def _header(data, title):
    u = UI[data['lang']]
    return f'<header class="pf-header"><span class="pf-meta">{u["snapshot"]} {data["date"]}</span><h1>{_h(title)}</h1><p>{_h(data["frame"]["Program Increment"])}</p><p class="pf-muted">{u["recorded"]} · {_h(data["frame"]["Current Iteration and week"])}</p></header>'


def _capacity(data):
    u = UI[data['lang']]; c = data['capacity']
    return _section(u['capacity'], _facts([(u['features'], f'{c["feature"]["progress"]} / {c["limits"]["feature"]}'),
                       (u['ready'], f'{c["feature"]["ready"]} / {c["limits"]["feature_ready"]}'),
                       (u['capabilities'], f'{c["capability"]["progress"]} / {c["limits"]["capability"]}')]) + f'<p class="pf-muted">{u["shared"]}</p>')


def render(data, url, kind='dashboard', item=None):
    lang = data['lang']; u = UI[lang]; ordinary = [x for x in data['items'] if not x['standing']]
    standing = [x for x in data['items'] if x['standing']]; gates = _gates(lang)
    if kind == 'initiative':
        return '<article class="pf-content pf-detail-page">' + _link(url, f'/{lang}/initiatives/', u['back']) + summary(item, data) + '</article>'
    title = u['title'] if kind == 'dashboard' else u[kind]
    body = _header(data, title)
    if kind == 'dashboard':
        stats = [(u['discovery'], sum(x['state'] == 'Discovery' for x in ordinary)), (u['approved'], data['counts']['Portfolio Backlog']),
                 (u['active'], f'{data["capacity"]["active"]} / {data["capacity"]["limit"]}'), (u['standing'], len(standing))]
        body += '<div class="pf-stats">' + ''.join(f'<div><strong>{v}</strong><span>{_h(k)}</span></div>' for k, v in stats) + '</div>'
        body += '<nav class="pf-tabs" aria-label="' + u['title'] + '">' + ''.join(f'<a href="#{key}" data-pf-tab="{key}">{u[key]}</a>' for key in ('board', 'review', 'standing', 'roadmap')) + '</nav>'
        body += _controls(data)
        columns = []
        occupied = [k for k in COLUMNS if data['counts'][k]]
        for col in COLUMNS:
            cards = ''.join(_card(x, data, url) for x in ordinary if x['column'] == col)
            count = data['counts'][col]; label = gates[col]['_localized_Kanban step']
            caption = u['delivery_gate'] if col == 'Implementation' else u['mvp_gate'] if col == 'MVP' else gates[col]['Gate']
            columns.append(f'<section class="pf-column{" pf-column--occupied" if col in occupied else ""}" data-pf-column="{col}"><header><h3>{_h(label)}</h3><span class="pf-badge">{count}</span></header><p class="pf-column-gate">{_h(caption)}</p><div class="pf-column-cards">{cards}</div><p class="pf-empty" {"hidden" if cards else ""}>{u["empty"]}</p></section>')
        widths = ' '.join('minmax(360px,3fr)' if data['counts'][k] else '110px' for k in COLUMNS)
        board = '<p class="pf-muted">' + u['order'] + '</p><div class="pf-board-scroll" tabindex="0" role="region" aria-label="' + u['board'] + '"><div class="pf-board" style="--pf-board-columns:' + widths + '">' + ''.join(columns) + '</div></div>'
        off = [x for x in ordinary if x['column'] == 'Off-flow']
        board += _section(u['offflow'], '<div class="pf-grid">' + ''.join(_card(x, data, url) for x in off) + '</div>' if off else '<p class="pf-muted">' + u['empty'] + '</p>')
        board += _capacity(data)
        body += f'<section id="board" class="pf-panel" data-pf-panel><h2 class="pf-panel-title">{u["board"]}</h2>{board}</section>'
        review_items = [x for x in ordinary if x['column'] in ('Funnel', 'Reviewing', 'Analyzing', 'Portfolio Backlog', 'MVP', 'Done')]
        review = '<p class="pf-muted">' + u['review_intro'] + '</p><div class="pf-grid">' + ''.join(_card(x, data, url, review=True) for x in review_items) + '</div>'
        body += f'<section id="review" class="pf-panel" data-pf-panel><h2 class="pf-panel-title">{u["review"]}</h2>{review}<p class="pf-empty pf-review-empty" hidden>{u["no_results"]}</p></section>'
        content = '<p class="pf-muted">' + u['standing_intro'] + '</p><div class="pf-grid">' + ''.join(_card(x, data, url, review=True) for x in standing) + '</div>' + _capacity(data)
        body += f'<section id="standing" class="pf-panel" data-pf-panel><h2 class="pf-panel-title">{u["standing"]}</h2>{content}</section>'
        horizon_cards = ''
        for horizon in data['horizons']:
            pi = horizon['Program Increment']; matching = [m for m in data['milestones'] if m['Program Increment'] == pi or m['Program Increment'] in pi]
            points = ''.join(f'<li><span class="pf-meta">{m["Identifier"]} · {_h(m["Status"])}</span><p>{_h(m["Milestone"])}</p></li>' for m in matching)
            horizon_cards += f'<section class="pf-horizon"><header><span class="pf-meta">{_h(horizon["Status"])}</span><h3>{_h(pi)}</h3><p>{_h(horizon["Content"])}</p></header><ul>{points}</ul></section>'
        body += f'<section id="roadmap" class="pf-panel" data-pf-panel><h2 class="pf-panel-title">{u["roadmap"]}</h2><p class="pf-muted">{u["roadmap_intro"]}</p><div class="pf-horizons">{horizon_cards}</div></section>'
        measures = '<p class="pf-muted">' + u['measure_intro'] + '</p><dl class="pf-measures">' + ''.join('<div><dt>' + _h(r['Flow Measure']) + '</dt><dd>' + _h(r['Value'] or u['unknown']) + '</dd></div>' for r in data['measures']) + '</dl>'
        body += '<details class="pf-measure-disclosure"><summary>' + u['measures'] + '</summary>' + measures + '</details>'
    elif kind == 'register':
        body += '<p class="pf-muted">' + u['order'] + '</p>' + _controls(data)
        for label, items in ((u['ordinary'], ordinary), (u['standing'], standing)):
            rows = ''.join(f'<article class="pf-register-row" data-pf-item="{x["id"]}" data-kind="{"standing" if x["standing"] else "ordinary"}" data-priority="{" ".join(x["priorities"]) or "enabling"}" data-find="{_h((x["id"]+" "+x["title"]+" "+x["owner"]).casefold())}"><span class="pf-meta">{x["id"]}{" · #"+str(x["rank"]) if x["rank"] else ""}</span><h3>{_link(url, _route(lang,x), x["title"])}</h3><span>{_h(x["status"])}</span><span>{_h(x["owner"])}</span></article>' for x in items)
            body += _section(label, rows)
    else:
        body += '<p>' + u['workflow_intro'] + '</p><p class="pf-notice">' + u['authority'] + '</p>'
        for key, g in gates.items():
            body += _section(g['_localized_Kanban step'], _facts([(u['state'], g['State and Stage']), (u['next'], g['Gate']), (u['decider'], g['Decided by'])]) + '<p>' + _h(g['Exit criterion']) + '</p><p class="pf-muted">' + _h(g['Record']) + '</p>')
        body += _section(u['rhythm'], '<ul>' + ''.join('<li>' + u[k] + '</li>' for k in ('weekly','monthly','quarterly','yearly')) + '</ul>')
    body += '<div class="pf-record-footer"><span class="pf-meta">' + u['source'] + '</span><p><code>' + f'registry/{lang}/dashboard.md' + '</code> · <code>' + f'registry/{lang}/portfolio-backlog.md' + '</code></p><p class="pf-muted">' + u['source_note'] + '</p></div>'
    if kind == 'dashboard':
        body += ''.join(f'<template data-pf-detail="{x["id"]}">{summary(x, data, modal=True)}</template>' for x in data['items'])
        body += f'<dialog class="pf-dialog" aria-label="{u["open"]}"><button type="button" data-pf-close aria-label="{u["close"]}">×</button><div class="pf-dialog-body"></div><a class="pf-full-link">{u["full"]}</a></dialog>'
    return '<article class="pf-content" data-pf-view="' + kind + '">' + body + '</article>'


def build(output):
    output = Path(output); count = 0
    for lang in ('en', 'ru'):
        data = project(lang=lang); u = UI[lang]; entries = []
        routes = [(f'/{lang}/initiatives/', 'dashboard', None), (f'/{lang}/initiatives/register/', 'register', None),
                  (f'/{lang}/initiatives/selection/', 'selection', None)]
        routes += [(_route(lang, item), 'initiative', item) for item in data['items']]
        nav_routes = [(routes[0][0], u['title']), (routes[1][0], u['register']), (routes[2][0], u['selection'])]
        for url, kind, item in routes:
            title = item['title'] if item else u['title'] if kind == 'dashboard' else u[kind]
            body = render(data, url, kind, item)
            nav = ''.join(_link(url, target, label).replace('<a ', '<a aria-current="page" ', 1) if target == url else _link(url,target,label) for target,label in nav_routes)
            if item: nav += f'<span class="pf-nav-label">{_h(item["title"])}</span>'
            page = workspace.page(url,lang,'initiatives',title,body,nav,body_class='portfolio-workspace')
            head = f'<link rel="stylesheet" href="{workspace.asset(url,"portfolio.css")}"><script defer src="{workspace.asset(url,"portfolio.js")}"></script>'
            page = page.replace('</head>',head+'\n</head>',1)
            target = output / url.strip('/') / 'index.html'; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(page)
            searchable = summary(item,data) if item else _header(data,title)
            from neighbours import VisibleText
            entries.append({'u':url,'t':title,'h':item['id'] if item else title,'x':VisibleText(searchable).text()})
            count += 1
        (output/f'assets/search-initiatives-{lang}.json').write_text(json.dumps(entries,ensure_ascii=False,separators=(',',':')))
    for name in ('portfolio.css','portfolio.js'): shutil.copyfile(workspace.ROOT/'portal/site'/name, output/'assets'/name)
    return count
