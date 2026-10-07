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
import kanban

COLUMNS = ('Funnel', 'Reviewing', 'Analyzing', 'Portfolio Backlog', 'MVP', 'Implementation', 'Done')
OFF_FLOW = ('Deferred', 'Rejected', 'Pivoted', 'Cancelled')
# The Portfolio holds the working state; the Registry holds governance and evidence (Operating Model 7.1-7.3).
BASE = 'portfolio/en/'
GOVERNANCE = 'registry/en/'
SHARE = {'portfolio': 'smb://10.128.20.244/aicc/portfolio/', 'registry': 'smb://10.128.20.244/aicc/governance/registry/'}


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
    # A Completed Initiative stays in Implementation and keeps its place until it moves to Review.
    active = sum(not x['standing'] and (x['state'] in ('Active', 'Completed') or
                 x['state'] == 'Waiting' and x.get('waiting_from') in ('Active', 'Completed')) for x in items)
    def program(rows):
        progress = sum(x['State'] in ('Active', 'Completed', 'Review') or
                       x['State'] == 'Waiting' and x.get('Waiting from') in ('Active', 'Completed', 'Review') for x in rows)
        ready = sum(x['State'] == 'Approved' or x['State'] == 'Waiting' and x.get('Waiting from') == 'Approved' for x in rows)
        return {'progress': progress, 'ready': ready}
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
        authority = None
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
            log = {r['Identifier']: r for r in en.table(GOVERNANCE + 'decision-log.md', 'Identifier | Date')}
            local_log = {r['Identifier']: r for r in sources.table(GOVERNANCE + 'decision-log.md', 'Identifier | Date')}
            refs = approval_ref.split(', ')
            if any(r not in log for r in refs): raise ValueError('Unknown Decision Record: ' + identifier)
            # Business Model 4.9: the Executive Sponsor approves; show the authority actually recorded.
            authority = None if all('Executive Sponsor' in log[r]['Decided by'] for r in refs) else '; '.join(_plain(local_log[r]['Decided by']) for r in refs)
        items.append({'id': identifier, 'title': _plain(public_meta['Title']), 'state': state, 'stage': stage,
                      'status': public_meta['State and Stage'], 'standing': standing, 'column': column,
                      'rank': int(row['Rank']) if row['Rank'] else None, 'priorities': row_priorities,
                      'priority': local['Strategic Priority'], 'owner': owner, 'acceptor': _plain(local['Business acceptor']),
                      'outcome': outcome, 'mvp': mvp, 'scope_steps': steps, 'out_scope': out_scope,
                      'risk': risk, 'controls': controls, 'pending': pending, 'wsjf': wsjf,
                      'dependencies': [{**depmap[k], 'id': k} for k in dep_ids], 'path': sources.resolve(path).path,
                      'stage_entered': row.get('Stage entered on') or (row.get('Funnel entered on') if state == 'Proposed' else None),
                      'goal_confirmation': 'DR-2026-061' if re.search(r'confirmed .*goal.*DR-2026-061', sec[6], re.I) else None,
                      'continuation_ref': next((r.get('Record') for r in decision_rows if r['Decision'].startswith('Decision after the MVP') and (r.get('Result','').lower() == 'continue' or re.search(r': continue',r['Decision'],re.I))), None),
                      'waiting_from': waiting_from, 'approval_ref': approval_ref,
                      'approved_on': row['Approved on'] or None, 'active_on': row['Active on'] or None,
                      'review_date': review_date, 'agreement': public_meta['Service Agreement'], 'scenario': public_meta['Source scenario'], 'authority': authority})
    mapping_path = Path(root) / 'portal/sections/program/mapping.json'
    mapping = json.loads(mapping_path.read_text()) if mapping_path.exists() else {}
    if set(mapping) - {'service-resolution'}: raise ValueError('Project mapping lacks native renderer')
    if len(set(mapping.values())) != len(mapping): raise ValueError('Ambiguous project mapping')
    if set(mapping.values()) - {x['id'] for x in items}: raise ValueError('Unknown mapped Initiative')
    for item in items:
        item['project_key'] = next((key for key, identifier in mapping.items() if identifier == item['id']), None)
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
    priorities = [{k: r[k] for k in ('Identifier', 'Strategic Priority')} for r in sources.table(GOVERNANCE + 'priorities.md', 'Identifier | Strategic Priority')]
    return {'lang': lang, 'date': date[1], 'frame': frame, 'items': ordinary + [x for x in items if x['standing']],
            'capacity': capacity(items, limits, features, capabilities), 'counts': {k: len(v) for k, v in projected.items()},
            'features': len(features), 'capabilities': len(capabilities), 'measures': measures,
            'horizons': horizons, 'milestones': milestones, 'priorities': priorities}

UI = {
'en': {
 'title':'Portfolio', 'page_title':'Overview', 'snapshot':'As of', 'recorded':'Maintained in the Portfolio of the Competence Center', 'week':'current week',
 'board':'Portfolio Kanban', 'review':'Review queue', 'standing':'Standing Initiatives', 'roadmap':'Roadmap', 'register':'Initiative register', 'selection':'Review and decisions',
 'discovery':'In Discovery', 'approved':'Approved, awaiting pull', 'active':'Active against the limit', 'ordinary':'Ordinary initiatives',
 'owner_missing':'Not yet appointed', 'all':'All priorities', 'enabling':'Enabling work', 'search':'Find an initiative', 'filter':'Strategic Priority',
 'empty':'No initiatives', 'no_results':'No matching initiatives', 'next':'Next gate', 'gate_prefix':'Gate', 'owner':'Domain Owner', 'sponsor':'Executive Sponsor (enabling work)',
 'state':'State and Stage', 'rank':'Rank', 'score':'WSJF score', 'unknown':'Not recorded', 'age':'Entered the current step / age',
 'source':'Record references', 'scenario':'Source scenario','exit':'Exit criterion','model':'Clause numbers refer to','order':'The Competence Center Lead sets the rank (Portfolio Management Model 6.5). The recorded rank follows the goals of the first 100 days and departs from the WSJF order; the reason for each departure is still to be recorded.',
 'shared':'MVP and Implementation count against one limit on Active Initiatives; a Completed Initiative still counts until it moves to Review. Standing Initiatives take no place under that limit; their Features count against the shared Team limits.',
 'capacity':'Work in progress against the limits', 'features':'Features in progress', 'ready':'Features Ready (cap; target: one to two Iterations ahead)', 'capabilities':'Capabilities in progress', 'capabilities_ready':'Capabilities Ready',
 'offflow':'Off the main flow', 'review_intro':'Initiatives before a portfolio gate. Each card shows the next gate and what the Initiative still needs.',
 'blocked':'The Scoped gate needs a Domain Owner; none is appointed yet.',
 'missing':'Open sections of the Initiative Brief (needed for the Approval gate)', 'gate':'Gate and decision', 'decider':'Decided by',
 'mvp':'Planned MVP', 'planned':'The MVP starts only after the business case is cleared by the Control Function Contacts, approved, and pulled within the limit.',
 'mvp_gate':'Decision after the MVP', 'impl_gate':'No portfolio gate (each Solution passes its own gates)', 'risk':'Risk and clearances', 'risk_note':'An expected Risk Tier is not an assigned tier, and it does not mean that the business case is cleared or validated.',
 'dependencies':'Dependencies', 'agreement':'Service Agreement', 'approval':'Business-case approval',
 'confirmation':'Decision Record DR-2026-061 confirms a goal of the first 100 days. It does not approve the business case.',
 'standing_intro':'Standing Initiatives, one per service area, approved for small run-rate requests. They take no place under the limit on Active Initiatives.',
 'standing_gate':'Admit the next eligible Feature at the Weekly Review', 'standing_decider':'Competence Center Lead, within the shared Team limits',
 'standing_note':'Each Feature needs a client function and its Domain Owner, acceptance criteria, known dependencies, AI use approval for its data class where AI applies, and a scope that fits one Iteration.',
 'standing_review':'Next quarterly review', 'standing_approval':'Approval recorded', 'no_mvp':'No MVP of its own; the work is done as run-rate Features.',
 'authority_note':'Decider recorded in {ref}: {by}. Business Model 4.9 gives the approval of a Standing Initiative to the Executive Sponsor; that approval is still to be recorded.',
 'roadmap_intro':'Intent for the current Program Increment, planned work for the next, and indicative direction beyond. Milestones are not achieved outcomes.',
 'measures':'Recorded flow measures', 'measure_intro':'Values that are not recorded are not estimated. Item age is calculated once the date of entry to each step is recorded.',
 'workflow_intro':'These gates prepare the reviews of the portfolio; clause numbers refer to the Portfolio Management Model. State changes are recorded in the Portfolio and decisions in the Registry, and then shown here.',
 'rhythm':'Review cadence', 'weekly':'Weekly Review: scope, complete Briefs, resolve blockers, and raise the items that reach a gate.',
 'monthly':'Monthly Steering: decide at gates, review the rank and the work in progress, and pull within the limit.',
 'quarterly':'Quarterly Steering: review the outcomes of Active Initiatives against their leading indicators, decide to continue, pivot, defer or reject, confirm the Roadmap, and review the Standing Initiatives.',
 'yearly':'Yearly Steering: set the Strategic Priorities, Investment Envelopes and Guardrails.',
 'authority':'Business-case approval: the Domain Owner, within one Domain and the Guardrails; otherwise, and for enabling work, the Executive Sponsor.',
 'open':'Open progress summary', 'close':'Close', 'full':'Full initiative page', 'back':'Back to portfolio', 'visible':'Matching ordinary initiatives',
 'waiting':'Waiting: stays in its column and counts against the limit', 'source_note':'Summaries show role names, not people. The working state is kept in the Portfolio, and decisions and restricted evidence in the Registry, both on the corporate share.',
 'months':('January','February','March','April','May','June','July','August','September','October','November','December'),
},
'ru': {
 'scenario':'Исходный сценарий', 'exit':'Критерий выхода', 'model':'Номера пунктов относятся к документу',
 'title':'Портфель инициатив', 'page_title':'Обзор', 'snapshot':'По состоянию на', 'recorded':'Рабочее состояние ведётся в портфеле Центра Компетенций', 'week':'текущая неделя',
 'board':'Канбан портфеля', 'review':'Очередь на рассмотрение', 'standing':'Постоянные инициативы', 'roadmap':'Дорожная карта', 'register':'Реестр инициатив', 'selection':'Рассмотрение и решения',
 'discovery':'В проработке', 'approved':'Ожидают принятия в работу', 'active':'В работе, в пределах лимита', 'ordinary':'Обычные инициативы',
 'owner_missing':'Ещё не назначен', 'all':'Все приоритеты', 'enabling':'Обеспечивающие работы', 'search':'Найти инициативу', 'filter':'Стратегический приоритет',
 'empty':'Инициатив нет', 'no_results':'Инициативы не найдены', 'next':'Следующая контрольная точка', 'gate_prefix':'Контрольная точка', 'owner':'Владелец направления', 'sponsor':'Куратор Центра Компетенций (обеспечивающие работы)',
 'state':'Состояние и стадия', 'rank':'Место в бэклоге портфеля', 'score':'Оценка WSJF', 'unknown':'Не указано', 'age':'Дата перехода на текущий шаг / возраст элемента',
 'source':'Ссылки на рабочие документы', 'order':'Место в бэклоге портфеля определяет руководитель Центра Компетенций (п. 6.5 Модели управления портфелем). Зафиксированный порядок следует целям первых 100 дней и отличается от порядка по оценке WSJF; основание каждого отступления ещё не зафиксировано.',
 'shared':'Стадии «MVP» и «Реализация» учитываются в одном лимите инициатив в работе; инициатива в состоянии «Завершено» учитывается в нём до перехода на рассмотрение. Постоянные инициативы мест в этом лимите не занимают; их Features входят в общие WIP-лимиты команды.',
 'capacity':'Незавершённая работа в сопоставлении с WIP-лимитами', 'features':'Features в работе', 'ready':'Features в колонке «Готово к работе» (предел; целевой запас — одна-две итерации)', 'capabilities':'Capabilities в работе', 'capabilities_ready':'Capabilities в колонке «Готово к работе»',
 'offflow':'Инициативы вне основного потока', 'review_intro':'Инициативы перед контрольной точкой портфеля. На каждой карточке указаны следующая контрольная точка и то, чего инициативе ещё не хватает.',
 'blocked':'Для контрольной точки «Определение объёма» нужен владелец направления; он ещё не назначен.',
 'missing':'Незаполненные разделы паспорта инициативы (требуются к контрольной точке «Одобрение»)', 'gate':'Контрольная точка и управленческое решение', 'decider':'Лицо, принимающее решение',
 'mvp':'Планируемый MVP', 'planned':'Работа над MVP начинается только после согласования бизнес-кейса представителями контрольных функций, его одобрения и принятия инициативы в работу в пределах лимита.',
 'mvp_gate':'Управленческое решение по итогам MVP', 'impl_gate':'Контрольной точки портфеля нет (каждое решение проходит собственные контрольные точки)', 'risk':'Риск и согласования', 'risk_note':'Указание ожидаемой категории риска не означает её присвоения, а также согласования или валидации бизнес-кейса.',
 'dependencies':'Зависимости', 'agreement':'Соглашение о взаимодействии', 'approval':'Одобрение бизнес-кейса',
 'confirmation':'Протоколом решения DR-2026-061 подтверждена цель первых 100 дней. Бизнес-кейс этим протоколом не одобрен.',
 'standing_intro':'Постоянные инициативы, по одной на каждое направление услуг, одобрены для выполнения небольших текущих запросов. Мест в лимите инициатив в работе они не занимают.',
 'standing_gate':'Принять в работу следующую Feature, отвечающую требованиям, на еженедельном обзоре', 'standing_decider':'Руководитель Центра Компетенций в пределах общих WIP-лимитов команды',
 'standing_note':'Для каждой Feature необходимы подразделение-заказчик и владелец направления, критерии приёмки, известные зависимости, одобрение применения AI для соответствующего класса данных (если используется AI) и объём, укладывающийся в одну итерацию.',
 'standing_review':'Следующее ежеквартальное рассмотрение', 'standing_approval':'Одобрение зафиксировано', 'no_mvp':'Собственный MVP не требуется; работа выполняется в виде Features текущих работ.',
 'authority_note':'Лицо, принявшее решение, по протоколу {ref}: {by}. Согласно п. 4.9 Бизнес-модели постоянную инициативу одобряет куратор Центра Компетенций; это одобрение ещё не зафиксировано.',
 'roadmap_intro':'Для текущего программного инкремента (PI) указаны намерения, для следующего — запланированная работа, для последующих — ориентиры. Вехи не означают достигнутых результатов.',
 'measures':'Зафиксированные показатели потока', 'measure_intro':'Значения, которые не зафиксированы, не указываются и не оцениваются. Возраст элемента рассчитывается после внесения дат перехода на шаги.',
 'workflow_intro':'Приведённые ниже контрольные точки используются при подготовке к рассмотрению портфеля; номера пунктов относятся к Модели управления портфелем. Изменения состояний вносятся в портфель Центра Компетенций, управленческие решения — в папку Центра Компетенций, после чего они отражаются на этой странице.',
 'rhythm':'Периодичность рассмотрения', 'weekly':'Еженедельный обзор: определение объёма, подготовка паспортов инициатив, устранение препятствий, вынесение элементов, достигших контрольной точки.',
 'monthly':'Ежемесячное управляющее совещание: управленческие решения на контрольных точках, ранжирование и незавершённая работа, принятие инициативы в работу в пределах лимита.',
 'quarterly':'Ежеквартальное управляющее совещание: результаты инициатив в работе в сопоставлении с опережающими индикаторами, решение о продолжении, перенаправлении, откладывании или отклонении, подтверждение дорожной карты, рассмотрение постоянных инициатив.',
 'yearly':'Ежегодное управляющее совещание: стратегические приоритеты, инвестиционные бюджеты и инвестиционные ограничения.',
 'authority':'Бизнес-кейс одобряет владелец направления, если инициатива не выходит за пределы одного направления и не превышает инвестиционного ограничения; в остальных случаях, а также для обеспечивающих работ — куратор Центра Компетенций.',
 'open':'Открыть сводку инициативы', 'close':'Закрыть', 'full':'Полная страница инициативы', 'back':'К портфелю', 'visible':'Найдено обычных инициатив',
 'waiting':'Ожидание: остаётся в своей колонке и учитывается в лимите', 'source_note':'В сводках указаны роли, а не имена исполнителей. Рабочее состояние ведётся в портфеле Центра Компетенций, управленческие решения и подтверждающие документы ограниченного доступа хранятся в папке Центра Компетенций; оба размещены на корпоративном файловом ресурсе.',
 'months':('января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря'),
}}


def _gates(lang):
    rows = Sources(workspace.ROOT, lang).table('charter/en/documents/portfolio-management-model.md', 'Kanban step | State and Stage', ('Kanban step',))
    return {r['Kanban step']: r for r in rows}


def _h(value): return escape(_plain(str(value)))


def _date(lang, value):
    # A recorded ISO date reads as a date of the edition's language.
    match = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})', value or '')
    if not match: return value
    day, month = int(match[3]), UI[lang]['months'][int(match[2]) - 1]
    return f'{day} {month} {match[1]} года' if lang == 'ru' else f'{day} {month} {match[1]}'


def _prose_dates(lang, text):
    # Registry records keep ISO dates so that the editions can be checked against each other; readers see words.
    return re.sub(r'(?<![\w/-])\d{4}-\d{2}-\d{2}(?![\w/-])', lambda m: _date(lang, m[0]), text)


def _decimal(lang, value):
    text = f'{value:.2f}'.rstrip('0').rstrip('.')
    return text.replace('.', ',') if lang == 'ru' else text


def _priority(item, data):
    names = {p['Identifier']: p['Strategic Priority'] for p in data['priorities']}
    return '; '.join(f'{k} · {names[k]}' for k in item['priorities'] if k in names) or UI[data['lang']]['enabling']


def _owner(item, data):
    u = UI[data['lang']]
    return u['sponsor'] if not item['priorities'] and not item['standing'] and item['owner'] == u['owner_missing'] else item['owner']


def _sentence(text):
    text = text.strip()
    return text if not text or text[-1] in '.!?»' else text + '.'


def _route(lang, item): return workspace.route(lang, 'portfolio', item['id'].lower() + '/')


def _link(url, target, label, cls=''):
    return f'<a class="{cls}" href="{workspace.relative(url, target)}">{_h(label)}</a>'


def _section(title, content, cls=''):
    return f'<section class="pf-section {cls}"><h2>{_h(title)}</h2>{content}</section>'


def _facts(pairs):
    return '<dl class="pf-facts">' + ''.join(f'<div><dt>{_h(k)}</dt><dd>{_h(v)}</dd></div>' for k, v in pairs) + '</dl>'


def summary(item, data, embedded=False, url=None):
    url = url or _route(data['lang'],item)
    lang = data['lang']; u = UI[lang]; g = _gates(lang).get(item['column'])
    title_tag = 'h2' if embedded else 'h1'
    heading = f'<header><span class="pf-meta">{item["id"]} · {_h(item["status"])}</span><{title_tag}>{_h(item["title"])}</{title_tag}><p>{_h(item["outcome"])}</p></header>'
    scenario = item['scenario'] if item['scenario'] and not item['scenario'].startswith('[') else u['unknown']
    facts = [(u['owner'], _owner(item, data)), (u['filter'], _priority(item, data)), (u['scenario'], scenario)]
    if not item['standing']:
        # Standing Initiatives are not ranked in the Kanban (Portfolio Management Model 5.5).
        facts += [(u['rank'], item['rank'] or '—'), (u['score'], _decimal(lang, item['wsjf']) if item['wsjf'] is not None else u['unknown']),
                  (u['age'], _date(lang, item['stage_entered']) or u['unknown'])]
    body = heading + _facts(facts)
    if item['column'] == 'Reviewing' and item['owner'] == u['owner_missing'] and item['priorities']:
        body += '<p class="pf-notice">' + u['blocked'] + '</p>'
    if item['state'] == 'Waiting': body += '<p class="pf-notice">' + u['waiting'] + '</p>'
    if item['standing']:
        gate = _facts([(u['next'], u['standing_gate']), (u['decider'], u['standing_decider']),
                       (u['standing_approval'], _date(lang, item['approved_on']) or u['unknown']), (u['standing_review'], _date(lang, item['review_date']) or u['unknown'])])
        if item['authority']: gate += '<p class="pf-notice">' + _h(u['authority_note'].format(by=item['authority'], ref=item['approval_ref'])) + '</p>'
        body += _section(u['gate'], gate + f'<p>{u["standing_note"]}</p><p>{u["no_mvp"]}</p>')
    elif g:
        gate = _facts([(u['next'], g['Gate']), (u['decider'], g['Decided by'])])
        body += _section(u['gate'], gate + '<p><strong>' + u['exit'] + '.</strong> ' + _h(_sentence(g['Exit criterion'])) + '</p><p class="pf-muted">' + u['authority'] + '</p>' + _model_link(lang, url))
        body += _section(u['missing'], '<p>' + _h(item['pending']) + '</p>' + _facts([(u['approval'], item['approval_ref'] or u['unknown']), (u['agreement'], item['agreement'])]))
        if item['goal_confirmation'] and not item['approval_ref']: body += f'<p class="pf-notice">{u["confirmation"]}</p>'
        scope = f'<p>{_h(item["mvp"])}</p><p class="pf-muted">{u["planned"]}</p>'
        scope += '<ol>' + ''.join('<li>' + _h(s) + '</li>' for s in item['scope_steps']) + '</ol><p>' + _h(item['out_scope']) + '</p>'
        body += _section(u['mvp'], scope)
        body += _section(u['risk'], '<p>' + _h(item['risk']) + '</p><p>' + _h(item['controls']) + '</p><p class="pf-muted">' + u['risk_note'] + '</p>')
    elif not item['standing']:
        body += _section(u['state'], f'<p>{_h(item["status"])}</p><p>{_h(item["pending"])}</p>')
    deps = '<ul class="pf-dependencies">' + ''.join(f'<li><div><strong>{d["id"]}</strong><span class="pf-badge">{_h(d["Status"])}</span></div><p>{_h(d["Needs"])}</p><small>{_h(d["From"])} · {_h(d["Needed by"])}</small></li>' for d in item['dependencies']) + '</ul>'
    body += _section(u['dependencies'], deps or '<p>' + u['unknown'] + '</p>')
    references = [item['path'], f'portfolio/{lang}/portfolio-backlog.md', f'portfolio/{lang}/dependencies.md', f'portfolio/{lang}/board.md']
    if item.get('project_key'):
        project_url = workspace.route(lang, 'program', item['project_key'] + '/')
        body += _section('Project and delivery' if lang == 'en' else 'Проект и реализация', '<p>' + _link(url, project_url, 'Project documents' if lang == 'en' else 'Документы проекта') + ' · ' + _link(url, workspace.route(lang, 'program', '#intake'), 'Program Backlog' if lang == 'en' else 'Бэклог программы') + '</p>')
    if item['approval_ref']: references.append(f'registry/{lang}/decision-log.md')
    body += _section(u['source'], '<p class="pf-muted">' + u['source_note'] + '</p><ul class="pf-references">' + ''.join('<li>' + _reference(r) + '</li>' for r in references) + '</ul>')
    if embedded:
        body = body.replace('<h2>', '<h3>').replace('</h2>', '</h3>')
        body = body.replace('<h3>', '<h2 class="kb-summary-title">', 1).replace('</h3>', '</h2>', 1)
        body = kanban.compact_summary(body, 'pf-section', lang)
        if item.get('project_key'):
            body = body.replace('</header>', '<p>'+_link(url, workspace.route(lang, 'program', item['project_key']+'/'), 'Open project →' if lang == 'en' else 'Открыть проект →')+'</p></header>', 1)
    return body


def _model_link(lang, url):
    # The clause numbers of the gates are those of the Portfolio Management Model; the page links to it.
    if not url: return ''
    target = workspace.route(lang, 'center', 'portfolio/portfolio-management-model/')
    name = 'Portfolio Management Model' if lang == 'en' else 'Модель управления портфелем'
    label = UI[lang]['model']
    return f'<p class="pf-muted">{label}: <a href="{workspace.relative(url, target)}">{_h(name)}</a></p>'


def _reference(path):
    # Records are linked on the corporate share; the portal does not embed them.
    root, _, rest = path.partition('/')
    return f'<a href="{escape(SHARE[root] + rest)}"><code>{_h(path)}</code></a>'


def _card(item, data, url):
    lang = data['lang']
    labels = ' '.join([item['id'], item['title'], _owner(item, data), _priority(item, data)])
    attrs = f'data-pf-open="{item["id"]}" data-pf-item="{item["id"]}" data-kind="{"standing" if item["standing"] else "ordinary"}" data-priority="{" ".join(item["priorities"]) or "enabling"}" data-find="{_h(labels.casefold())}"'
    return kanban.card(item['id'], item['title'], workspace.relative(url, _route(lang,item)),
        kind=('Standing' if lang == 'en' else 'Постоянная') if item['standing'] else ('Initiative' if lang == 'en' else 'Инициатива'),
        state=item['status'], priority=item['priority'], rank=item['rank'], lang=lang, attributes=attrs, classes='pf-card pf-title-link', order_label=('Run-rate' if lang == 'en' else 'Текущие') if item['standing'] else None)


def _controls(data):
    u = UI[data['lang']]
    options = [(p['Identifier'], p['Identifier'] + ' · ' + p['Strategic Priority']) for p in data['priorities']]
    options.append(('enabling', u['enabling']))
    select = ''.join(f'<option value="{_h(k)}">{_h(v)}</option>' for k, v in options)
    return f'<div class="pf-filter" hidden><label>{u["search"]}<input type="search" data-pf-search autocomplete="off"></label><label>{u["filter"]}<select data-pf-priority><option value="">{u["all"]}</option>{select}</select></label><output data-pf-visible aria-live="polite">{u["visible"]}: {sum(not i["standing"] for i in data["items"])}</output></div>'


def _header(data, title):
    u = UI[data['lang']]
    return f'<header class="pf-header"><span class="pf-meta">{u["snapshot"]} {_date(data["lang"], data["date"])}</span><h1>{_h(title)}</h1><p>{_h(data["frame"]["Program Increment"])}</p><p class="pf-muted">{u["recorded"]} · {u["week"]}: {_h(data["frame"]["Current Iteration and week"])}</p></header>'


def _capacity(data):
    u = UI[data['lang']]; c = data['capacity']
    return _section(u['capacity'], _facts([(u['features'], f'{c["feature"]["progress"]} / {c["limits"]["feature"]}'),
                       (u['ready'], f'{c["feature"]["ready"]} / {c["limits"]["feature_ready"]}'),
                       (u['capabilities'], f'{c["capability"]["progress"]} / {c["limits"]["capability"]}'),
                       (u['capabilities_ready'], f'{c["capability"]["ready"]} / {c["limits"]["capability_ready"]}')]) + f'<p class="pf-muted">{u["shared"]}</p>')


def render(data, url, kind='dashboard', item=None):
    lang = data['lang']; u = UI[lang]; ordinary = [x for x in data['items'] if not x['standing']]
    standing = [x for x in data['items'] if x['standing']]; gates = _gates(lang)
    if kind == 'initiative':
        return '<article class="pf-content pf-detail-page">' + _link(url, workspace.route(lang, 'portfolio'), u['back']) + summary(item, data) + '</article>'
    title = u['title'] if kind == 'dashboard' else u[kind]
    body = _header(data, title)
    if kind == 'dashboard':
        stats = [(u['discovery'], sum(x['state'] == 'Discovery' for x in ordinary)), (u['approved'], data['counts']['Portfolio Backlog']),
                 (u['active'], f'{data["capacity"]["active"]} / {data["capacity"]["limit"]}'), (u['standing'], len(standing))]
        body += '<div class="pf-stats">' + ''.join(f'<div><strong>{v}</strong><span>{_h(k)}</span></div>' for k, v in stats) + '</div>'
        body += '<nav class="pf-tabs" aria-label="' + u['title'] + '">' + ''.join(f'<a href="#{key}" data-pf-tab="{key}">{u[key]}</a>' for key in ('board', 'review', 'standing', 'roadmap')) + '</nav>'
        body += _controls(data)
        columns = []
        for col in COLUMNS:
            cards = ''.join(_card(x, data, url) for x in ordinary if x['column'] == col)
            label = gates[col]['_localized_Kanban step']
            caption = (('Shared Active' if lang == 'en' else 'Общий WIP') + f' {data["capacity"]["active"]}/{data["capacity"]["limit"]}') if col in ('MVP','Implementation') else ('No WIP cap' if lang == 'en' else 'Без WIP-лимита')
            columns.append(f'<section class="pf-column kb-column" data-pf-column="{col}">{kanban.column_header(label,data["counts"][col],caption)}<div class="pf-column-cards kb-stack">{cards}<p class="pf-empty kb-empty" {"hidden" if cards else ""}>{u["empty"]}</p></div></section>')
        board = '<p class="pf-muted">' + u['order'] + '</p><div class="pf-board-scroll kb-scroll" tabindex="0" role="region" aria-label="' + u['board'] + '"><div class="pf-board kb-board">' + ''.join(columns) + '</div></div>' + kanban.detail_panel(lang)
        off = [x for x in ordinary if x['column'] == 'Off-flow']
        if off: board += _section(u['offflow'], '<div class="pf-grid">' + ''.join(_card(x, data, url) for x in off) + '</div>')
        board += '<details class="pf-measure-disclosure"><summary>'+u['capacity']+'</summary>'+_capacity(data)+'</details>'
        body += f'<section id="board" class="pf-panel" data-pf-panel><h2 class="pf-panel-title">{u["board"]}</h2>{board}</section>'
        review_items = [x for x in ordinary if x['column'] in ('Funnel', 'Reviewing', 'Analyzing', 'Portfolio Backlog', 'MVP', 'Done')]
        review = '<p class="pf-muted">' + u['review_intro'] + '</p><div class="pf-grid">' + ''.join(_card(x, data, url) for x in review_items) + '</div>'
        body += f'<section id="review" class="pf-panel" data-pf-panel><h2 class="pf-panel-title">{u["review"]}</h2>{review}{kanban.detail_panel(lang)}<p class="pf-empty pf-review-empty" hidden>{u["no_results"]}</p></section>'
        content = '<p class="pf-muted">' + u['standing_intro'] + '</p><div class="pf-grid">' + ''.join(_card(x, data, url) for x in standing) + '</div>'
        body += f'<section id="standing" class="pf-panel" data-pf-panel><h2 class="pf-panel-title">{u["standing"]}</h2>{content}{kanban.detail_panel(lang)}</section>'
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
        body += '<p>' + u['workflow_intro'] + '</p>' + _model_link(lang, url) + '<p class="pf-notice">' + u['authority'] + '</p>'
        for key, g in gates.items():
            body += _section(g['_localized_Kanban step'], _facts([(u['state'], g['State and Stage']), (u['next'], g['Gate']), (u['decider'], g['Decided by'])]) + '<p>' + _h(_sentence(g['Exit criterion'])) + '</p><p class="pf-muted">' + _h(g['Record']) + '</p>')
        body += _section(u['rhythm'], '<ul>' + ''.join('<li>' + u[k] + '</li>' for k in ('weekly','monthly','quarterly','yearly')) + '</ul>')
    footer = ' · '.join(_reference(f'portfolio/{lang}/{name}') for name in ('dashboard.md', 'portfolio-backlog.md'))
    body += '<div class="pf-record-footer"><span class="pf-meta">' + u['source'] + '</span><p>' + footer + '</p><p class="pf-muted">' + u['source_note'] + '</p></div>'
    if kind == 'dashboard':
        body += ''.join(f'<template data-kb-detail="{x["id"]}">{summary(x, data, embedded=True, url=url)}</template>' for x in data['items'])
    return '<article class="pf-content" data-kanban-workspace data-pf-view="' + kind + '">' + body + '</article>'


def build(output):
    output = Path(output); count = 0
    for lang in ('en', 'ru'):
        data = project(lang=lang); u = UI[lang]; entries = []
        routes = [(workspace.route(lang, 'portfolio'), 'dashboard', None), (workspace.route(lang, 'portfolio', 'register/'), 'register', None),
                  (workspace.route(lang, 'portfolio', 'selection/'), 'selection', None)]
        routes += [(_route(lang, item), 'initiative', item) for item in data['items']]
        nav_routes = [(routes[0][0], u['title']), (routes[1][0], u['register']), (routes[2][0], u['selection'])]
        for url, kind, item in routes:
            title = item['title'] if item else u['page_title'] if kind == 'dashboard' else u[kind]
            body = _prose_dates(lang, render(data, url, kind, item))
            nav = ''.join(_link(url, target, label).replace('<a ', '<a aria-current="page" ', 1) if target == url else _link(url,target,label) for target,label in nav_routes)
            if item: nav += f'<span class="pf-nav-label">{_h(item["title"])}</span>'
            page = workspace.page(url,lang,'portfolio',title,body,nav,body_class='portfolio-workspace')
            head = f'<link rel="stylesheet" href="{workspace.asset(url,"portfolio.css")}"><script defer src="{workspace.asset(url,"portfolio.js")}"></script>'
            page = page.replace('</head>',head+kanban.assets(url)+'\n</head>',1)
            target = output / url.strip('/') / 'index.html'; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(page)
            searchable = summary(item,data) if item else re.sub(r'<template\b.*?</template>', ' ', body, flags=re.S)
            from neighbours import VisibleText
            entries.append({'u':url,'t':u['title'] if kind == 'dashboard' else title,'h':item['id'] if item else title,'x':_prose_dates(lang, VisibleText(searchable).text())})
            count += 1
        (output/f'assets/search-portfolio-{lang}.json').write_text(json.dumps(entries,ensure_ascii=False,separators=(',',':')))
    for name in ('portfolio.css','portfolio.js'): shutil.copyfile(workspace.ROOT/'portal/site'/name, output/'assets'/name)
    kanban.assets(workspace.route('en', 'portfolio'), output)
    return count
