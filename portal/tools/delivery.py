"""Program delivery views of the maintained Portfolio, linked to native projects."""
# START_MODULE_CONTRACT
# PURPOSE: Present Competence Center delivery without manufacturing admissions or operational state.
# SCOPE: Program records, parent validation, Kanban, intake relationships and documents.
# DEPENDS: M-PORTAL-LOCALIZATION
# LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# MAP_MODE: SUMMARY
# END_MODULE_CONTRACT
# START_MODULE_MAP
# position - map Program state to column, retaining Waiting context
# validate - validate hierarchy, admission, stages and delivery evidence
# project - join maintained bilingual delivery and Portfolio records
# render - render the common delivery dashboard and item summaries
# build - publish paired routes and scoped search entries
# END_MODULE_MAP
from html import escape
import json
from pathlib import Path
import re
import shutil
from localization import Sources
import portfolio
import workspace
import kanban

COLUMNS = ('Backlog', 'Ready', 'Active', 'Review', 'Done')
LANES = ('Urgent', 'High priority', 'Normal')


def position(state, waiting_from='', dependency=''):
    if state == 'Waiting':
        if waiting_from not in ('Proposed','Discovery','Approved','Active','Completed','Review') or not dependency:
            raise ValueError('Waiting requires previous state and Dependency')
        state = waiting_from
    if state in ('Proposed','Discovery','Deferred'): return 'Backlog'
    if state == 'Approved': return 'Ready'
    if state in ('Active','Completed'): return 'Active'
    if state == 'Review': return 'Review'
    if state in ('Accepted','Closed'): return 'Done'
    if state in ('Rejected','Pivoted','Cancelled'): return 'Off-flow'
    raise ValueError('Unknown Program state: ' + state)


def validate(capabilities, features, initiatives, dependencies):
    """A parent and admission are actual recorded facts, never inferred from a workbook."""
    parents = {i['id']:i for i in initiatives}
    caps = {r['Identifier']:r for r in capabilities}
    all_rows = capabilities + features
    if len({r['Identifier'] for r in all_rows}) != len(all_rows): raise ValueError('Duplicate Program identifier')
    for r in all_rows:
        identifier = r['Identifier']; capability = identifier.startswith('CAP-')
        if not re.fullmatch(r'(CAP|FEAT)-\d+', identifier): raise ValueError('Invalid Program identifier')
        if capability:
            parent = parents.get(r['Initiative'])
            if not parent or parent['standing'] or not parent.get('continuation_ref'):
                raise ValueError('Capability requires ordinary Initiative MVP continue decision')
            if not r['Solution']: raise ValueError('Capability requires Solution reference')
        else:
            ref = r['Parent: Capability or Standing Initiative']
            cap = caps.get(ref)
            parent = parents.get(cap['Initiative']) if cap else parents.get(ref)
            if not parent or (not cap and not parent['standing']): raise ValueError('Feature parent must be Capability or Standing Initiative')
            if parent['standing'] and (parent['state'] not in ('Approved','Active') or not parent['approval_ref']):
                raise ValueError('Run-rate parent must have approved Standing Brief')
        if r['Lane'] not in LANES: raise ValueError('Program service class must be recorded')
        state = r['State']; stage = r['Stage']; underlying = r.get('Waiting from','') if state == 'Waiting' else state
        column = position(state,r.get('Waiting from',''),r.get('Waiting Dependency',''))
        if underlying == 'Discovery' and stage not in (('Analysis',) if capability else ('Explore','Design')):
            raise ValueError('Invalid discovery Stage')
        if underlying == 'Active' and stage not in (('Implementation',) if capability else ('Develop','Verify','Deploy')):
            raise ValueError('Invalid Active Stage')
        deps = re.findall(r'DEP-\d+', r.get('Acceptance criteria and Dependencies','') + ' ' + r.get('Waiting Dependency',''))
        if any(d not in dependencies for d in deps): raise ValueError('Unknown Program Dependency')
        criteria = r.get('Acceptance criteria','') if capability else r['Acceptance criteria and Dependencies']
        if underlying in ('Approved','Active','Completed','Review','Accepted'):
            if not criteria or not r.get('Approved by and date'): raise ValueError('Approved work requires acceptance criteria and admission record')
            if not capability and parent['standing'] and not r.get('Data-use approval reference'):
                raise ValueError('Run-rate data-use disposition must be recorded')
        if state == 'Accepted' and not r['Accepted by and date']: raise ValueError('Accepted work requires acceptance record')
        if r.get('Rank') and (not r['Rank'].isdigit() or int(r['Rank']) < 1): raise ValueError('Invalid Program rank')
        if r.get('Stage entered on') and not re.fullmatch(r'\d{4}-\d{2}-\d{2}',r['Stage entered on']): raise ValueError('Invalid stage entry date')
        r.update(column=column,initiative=parent['id'],kind='Capability' if capability else 'Feature',dependencies=list(dict.fromkeys(deps)))
    ranks = [int(r['Rank']) for r in features if r.get('Rank')]
    if len(ranks) != len(set(ranks)): raise ValueError('Duplicate Feature rank')
    return all_rows


def project(root=workspace.ROOT,lang='en'):
    pf = portfolio.project(root,lang); en = Sources(root,'en'); local = Sources(root,lang)
    path='portfolio/en/program-backlog.md'
    caps=en.table(path,'Identifier | Capability'); features=en.table(path,'Rank | Identifier | Feature')
    deps=en.table('portfolio/en/dependencies.md','Identifier | Item'); depmap={r['Identifier']:r for r in deps}
    items=validate(caps,features,pf['items'],depmap)
    board=en.table('portfolio/en/board.md','Lane | Backlog (proposed, discovery, deferred)')
    fields=dict(zip(COLUMNS,('Backlog (proposed, discovery, deferred)','Ready (approved)','Active','Review','Done')))
    if [r['Lane'] for r in board[1:]] != list(LANES): raise ValueError('Program lanes disagree')
    for row in board[1:]:
        for column,field in fields.items():
            recorded=re.findall(r'(?:CAP|FEAT)-\d+',row[field])
            expected=[r['Identifier'] for r in items if r['Lane']==row['Lane'] and r['column']==column]
            if sorted(recorded)!=sorted(expected): raise ValueError('Program Backlog/board placement disagreement')
    review=re.search(r'Last Weekly Review baseline: (\d{4}-\d{2}-\d{2})',en.text('portfolio/en/dashboard.md'))

    translated=local.table(path,'Identifier | Capability')+local.table(path,'Rank | Identifier | Feature')
    for r,t in zip(items,translated):
        r['title']=t['Capability' if r['kind']=='Capability' else 'Feature']
        r['status']=t['State'];r['stage_label']=t['Stage']
        r['criteria']=t.get('Acceptance criteria','') if r['kind']=='Capability' else t['Acceptance criteria and Dependencies']
        # Signer names stay in maintained evidence; public fields show references and dates only.
        r['approval']=', '.join(re.findall(r'\b(?:DR-\d{4}-\d+|\d{4}-\d{2}-\d{2})\b',r.get('Approved by and date','')))
        r['accepted']=', '.join(re.findall(r'\b(?:DR-\d{4}-\d+|\d{4}-\d{2}-\d{2})\b',r.get('Accepted by and date','')))
        r['rank']=int(r['Rank']) if r.get('Rank') else None
    items.sort(key=lambda r:(r['rank'] is None,r['rank'] or 0,r['Identifier']))
    counts={col:sum(r['column']==col for r in items) for col in COLUMNS}
    reported=en.table('portfolio/en/dashboard.md','Program Kanban: Capabilities and Features | Backlog')[-1]
    if any(int(reported[col])!=counts[col] for col in COLUMNS) or int(reported['Waiting (flag, in any column)'])!=sum(r['State']=='Waiting' for r in items):
        raise ValueError('Dashboard/Program count disagreement')
    return {'lang':lang,'portfolio':pf,'items':items,'counts':counts,'dependencies':depmap,'review_date':review[1] if review else None}


UI={
'en':{'title':'Program Backlog','subtitle':'Delivery of the Competence Center, connected to initiative goals and project documents.','board':'Program Kanban','intake':'Portfolio intake','documents':'Project documents',
      'snapshot':'Recorded snapshot','features':'Features in progress','ready':'Ready Features','capabilities':'Capabilities in progress','upstream':'Initiatives not yet in delivery',
      'columns':COLUMNS,'lanes':LANES,'captions':('Proposed / Discovery','Approved','Active / Completed','Review','Accepted / Closed'),
      'empty':'No Capabilities or Features have been admitted yet.','admission':'Ordinary delivery enters after the MVP continue decision. Run-rate Features enter under approved Standing Initiatives at Weekly Review.',
      'next':'Next decision','unknown':'Not recorded','waiting':'Waiting','shared':'Shared Team limits across all projects and classes of service','intake_title':'Prepare the next portfolio decision','intake_note':'These rows retain their Portfolio state; they are not delivery cards.',
      'standing':'Run-rate admission sources','standing_note':'Approved Standing Initiatives share the Team limits. Each Feature needs its own admission.','open':'Open initiative','open_project':'Open project','none':'No Program items admitted','full':'Complete native workbook','search':'Find an initiative','priority':'Priority','all':'All priorities','showing':'Showing',
      'source':'The Portfolio records own the working state, and the Registry holds the decisions. Changes follow the Portfolio and Registry workflow.','offflow':'Other exits','back':'Program Backlog','criteria':'Acceptance criteria','parent':'Parent and goal','dependencies':'Dependencies','approval':'Admission reference / date','accepted':'Acceptance reference / date','age':'Entered the current step','rank':'Rank','risk':'Expected Risk Tier 2; not assigned or cleared','footer':'Last Weekly Review baseline',
      'gates':{'Funnel':'Screen the need and confirm requester','Reviewing':'Confirm scope, owner and indicator sources','Analyzing':'Complete the business case and clearances','Portfolio Backlog':'Rank and pull within the limit','MVP':'Evaluate the MVP and decide on continuation','Implementation':'Deliver admitted Capabilities and Features','Done':'Inspect acceptance and confirmed outcome','Off-flow':'Inspect the recorded exit decision'}},
'ru':{'title':'Бэклог программы','subtitle':'Реализация в Центре Компетенций — от целей инициатив к проектным документам.','board':'Канбан программы','intake':'Поступление из портфеля','documents':'Документы проектов',
      'snapshot':'По состоянию на','features':'Features в работе','ready':'Features в колонке «Готово к работе»','capabilities':'Capabilities в работе','upstream':'Инициативы, ещё не перешедшие к реализации',
      'columns':('Бэклог (Backlog)','Готово к работе (Ready)','В работе (Active)','Рассмотрение (Review)','Готово (Done)'),'lanes':('Срочно (Urgent)','Высокий приоритет (High priority)','Обычный приоритет (Normal)'),'captions':('Предложено / Проработка','Одобрено','В работе / Выполнено','На рассмотрении','Принято / Закрыто'),
      'empty':'Capabilities и Features ещё не включены в бэклог программы.','admission':'Capabilities обычной инициативы поступают после управленческого решения о продолжении по итогам MVP. Features текущих работ принимаются в работу в рамках одобренных постоянных инициатив на еженедельном обзоре.',
      'next':'Следующее решение','unknown':'Не указано','waiting':'Ожидание','shared':'Общие WIP-лимиты команды для всех проектов и классов обслуживания','intake_title':'Подготовка следующего решения по портфелю','intake_note':'Строки сохраняют состояние в портфеле; это не карточки реализации.',
      'standing':'Источники текущих работ','standing_note':'Одобренные постоянные инициативы входят в общие WIP-лимиты команды. Каждая Feature принимается в работу отдельно.','open':'Открыть инициативу','open_project':'Открыть проект','none':'Элементы программы ещё не приняты','full':'Полный комплект документов','search':'Поиск инициативы','priority':'Приоритет','all':'Все приоритеты','showing':'Показано',
      'source':'Рабочее состояние ведётся в портфеле Центра Компетенций, управленческие решения — в папке Центра Компетенций. Изменения вносятся в установленном порядке ведения портфеля и папки Центра Компетенций.','offflow':'Прочие выходы','back':'Бэклог программы','criteria':'Критерии приёмки','parent':'Родительский элемент и цель','dependencies':'Зависимости','approval':'Ссылка и дата принятия в работу','accepted':'Ссылка и дата приёмки','age':'Дата перехода на текущий шаг','rank':'Место в бэклоге программы','risk':'Ожидаемая категория риска 2; не присвоена и не согласована','footer':'Базовое состояние последнего еженедельного обзора',
      'gates':{'Funnel':'Рассмотреть потребность и подтвердить заявителя','Reviewing':'Уточнить объём, владельца и источники индикаторов','Analyzing':'Подготовить бизнес-кейс и получить согласования контрольных функций','Portfolio Backlog':'Ранжировать и принять в работу в пределах лимита','MVP':'Оценить MVP и принять решение о продолжении','Implementation':'Реализовать принятые Capabilities и Features','Done':'Проверить приёмку и подтверждённый результат','Off-flow':'Проверить записанное решение о выходе'}}}


def link(url,target,title,cls=''):
    return f'<a class="{cls}" href="{workspace.relative(url,target)}">{escape(title)}</a>'


def initiative_card(i,data,url):
    lang=data['lang'];u=UI[lang];target=portfolio._route(lang,i)
    project_key=i.get('project_key')
    return f'<article class="dl-card dl-proposal" data-dl-initiative="{i["id"]}"><div><div class="dl-meta">{i["id"]} · {escape(i["priority"])} <span class="dl-badge">{escape(i["status"])}</span></div><h3>{escape(i["title"])}</h3><p>{escape(i["outcome"])}</p><div class="dl-actions">{link(url,target,u["open"]+" →")}{link(url,workspace.route(lang,'program',project_key+'/'),u["open_project"]+" →") if project_key else ""}</div></div><aside><strong>{u["next"]}</strong><p>{u["gates"][i["column"]]}</p><small>{u["none"] if not any(r["initiative"]==i["id"] for r in data["items"]) else ""}</small></aside></article>'


def item_body(item,data,url,embedded=False):
    u=UI[data['lang']];parent=next(i for i in data['portfolio']['items'] if i['id']==item['initiative'])
    facts=[(u['parent'],item.get('Parent: Capability or Standing Initiative',item.get('Initiative'))),
           (portfolio.UI[data['lang']]['owner'],portfolio._owner(parent,data['portfolio'])),
           ('Solution',item.get('Solution') or next((r['Solution'] for r in data['items'] if r['Identifier']==item.get('Parent: Capability or Standing Initiative')),u['unknown'])),
           (u['rank'],item['rank'] or u['unknown']),(u['age'],item.get('Stage entered on') or u['unknown']),
           (u['approval'],item['approval'] or u['unknown']),(u['accepted'],item['accepted'] or u['unknown'])]
    body = f'<header><span class="dl-meta">{item["Identifier"]} · {escape(item["status"])} · {escape(item["stage_label"])}</span><h1>{escape(item["title"])}</h1></header><section class="dl-section"><h2>{u["parent"]}</h2>{link(url,portfolio._route(data["lang"],parent),parent["id"]+" · "+parent["title"])}<p>{escape(parent["outcome"])}</p></section><dl class="dl-facts">'+''.join(f'<div><dt>{escape(k)}</dt><dd>{escape(str(v))}</dd></div>' for k,v in facts)+f'</dl><section class="dl-section"><h2>{u["criteria"]}</h2><p>{escape(item["criteria"] or u["unknown"])}</p></section><section class="dl-section"><h2>{u["dependencies"]}</h2>'+''.join(f'<p>{d} · {escape(data["dependencies"][d]["Status"])} · {escape(data["dependencies"][d]["Needs"])}</p>' for d in item['dependencies'])+'</section>'

    if embedded:
        # Reuse the record's parent goal and evidence; this is guidance, not a decision.
        parent_section = re.search(r'<section class="dl-section">.*?</section>', body, re.S)
        body = body[:parent_section.start()] + body[parent_section.end():]
        body = body.replace('</header>', '<p>'+escape(parent['outcome'])+'</p><p>'+link(url,portfolio._route(data['lang'],parent),parent['id']+' · '+parent['title'])+'</p></header>', 1)
        next_gate = {
            'en': {'Backlog':'Prepare scope, acceptance criteria and admission.', 'Ready':'Pull within the shared Team limits.', 'Active':'Complete the current delivery stage and submit for acceptance.', 'Review':'Inspect acceptance evidence and record the decision.', 'Done':'Inspect the recorded acceptance and outcome.', 'Off-flow':'Inspect the recorded exit decision.'},
            'ru': {'Backlog':'Подготовить объём, критерии приёмки и принятие в работу.', 'Ready':'Принять в работу в пределах общих WIP-лимитов команды.', 'Active':'Завершить текущую стадию и передать элемент на рассмотрение.', 'Review':'Проверить соответствие критериям приёмки и зафиксировать решение.', 'Done':'Проверить зафиксированную приёмку и результат.', 'Off-flow':'Проверить записанное решение о выходе.'}
        }[data['lang']][item['column']]
        if (item.get('Waiting from') if item['State'] == 'Waiting' else item['State']) == 'Completed':
            next_gate = 'Submit completed work for acceptance.' if data['lang'] == 'en' else 'Передать выполненную работу на рассмотрение.'
        marker = body.index('<section class="dl-section">')
        body = body[:marker] + '<section class="dl-section"><h2>'+u['next']+'</h2><p>'+next_gate+'</p></section>' + body[marker:]
        if item['State'] == 'Waiting':
            body = body.replace('</header>', '<p class="pf-notice">'+u['waiting']+' · '+escape(item.get('Waiting Dependency',''))+'</p></header>', 1)
        body = body.replace('<h2>', '<h3>').replace('</h2>', '</h3>').replace('<h1>', '<h2>').replace('</h1>', '</h2>')
        body = kanban.compact_summary(body, 'dl-section', data['lang'])
    return body


def _card(item, data, url):
    lang=data['lang']
    return kanban.card(item['Identifier'],item['title'],workspace.relative(url,workspace.route(lang,'program',f'items/{item["Identifier"].lower()}/')),
        kind=item['kind'],state=item['status'] + (' · '+item['stage_label'] if item['stage_label'] else ''),
        priority=item['initiative'],rank=item['rank'],lang=lang,classes='dl-card')


def render(data,url,item=None):
    import project as workbook
    lang=data['lang'];u=UI[lang];pf=data['portfolio'];c=pf['capacity'];ordinary=[i for i in pf['items'] if not i['standing']];standing=[i for i in pf['items'] if i['standing']]
    if item:return '<article class="dl-content">'+link(url,workspace.route(lang,'program'),u['back'])+item_body(item,data,url)+'</article>'
    body=f'<header class="dl-intro"><div><h1>{u["title"]}</h1><p>{u["subtitle"]}</p></div><aside><strong>{escape(pf["frame"]["Program Increment"].split(" (")[0])}</strong><p class="dl-meta">{u["snapshot"]} {portfolio._date(lang, pf["date"])}</p></aside></header>'
    stats=[(f'{c["feature"]["progress"]} / {c["limits"]["feature"]}',u['features']), (f'{c["feature"]["ready"]} / {c["limits"]["feature_ready"]}',u['ready']), (f'{c["capability"]["progress"]} / {c["limits"]["capability"]}',u['capabilities']), (str(sum(i['column'] not in ('Implementation','Done','Off-flow') for i in ordinary)),u['upstream'])]
    body+='<div class="dl-stats">'+''.join(f'<div><strong>{value}</strong><span>{label}</span></div>' for value,label in stats)+'</div>'
    body+=f'<p class="dl-meta">{u["capabilities"]} · {u["columns"][1]}: {c["capability"]["ready"]} / {c["limits"]["capability_ready"]}</p>'
    body+='<nav class="dl-tabs">'+''.join(f'<a href="#{key}" data-dl-tab="{key}">{u[label]}</a>' for key,label in [('board','board'),('intake','intake'),('documents','documents')])+'</nav>'
    captions = []
    for col in COLUMNS:
        if col == 'Ready':
            caption = f'Features {c["feature"]["ready"]}/{c["limits"]["feature_ready"]} · Capabilities {c["capability"]["ready"]}/{c["limits"]["capability_ready"]}'
        elif col in ('Active','Review'):
            caption = ('Shared WIP limit' if lang == 'en' else 'Общий WIP-лимит') + f' · Features {c["feature"]["progress"]}/{c["limits"]["feature"]} · Capabilities {c["capability"]["progress"]}/{c["limits"]["capability"]}'
        else: caption = 'No WIP cap' if lang == 'en' else 'Без WIP-лимита'
        captions.append(caption)
    board='<div class="dl-board-wrap kb-scroll" tabindex="0" role="region" aria-label="'+u['board']+'"><table class="dl-board kb-table"><thead><tr><th></th>'+''.join(f'<th scope="col">{kanban.column_header(label,data["counts"][col],caption)}</th>' for col,label,caption in zip(COLUMNS,u['columns'],captions))+'</tr></thead><tbody>'
    for lane,label in zip(LANES,u['lanes']):
        board+=f'<tr><th scope="row">{kanban.bilingual(label)}</th>'
        for col in COLUMNS:
            cards=''.join(_card(r,data,url) for r in data['items'] if r['column']==col and r['Lane']==lane)
            board+='<td><div class="kb-stack">'+ (cards or '<span class="kb-empty">—</span>')+'</div></td>'
        board+='</tr>'
    board+='</tbody></table></div>'+kanban.detail_panel(lang)
    if not data['items']:board+=f'<p class="dl-empty"><strong>{u["empty"]}</strong></p>'
    board+=f'<p class="dl-meta">{u["admission"]}</p><p class="dl-meta">{u["shared"]} · {u["waiting"]}: {sum(r["State"]=="Waiting" for r in data["items"])}</p>'
    off=[r for r in data['items'] if r['column']=='Off-flow']
    if off:board+=f'<h2 class="dl-section-title">{u["offflow"]}</h2>'+'<div class="kb-grid">'+''.join(_card(r,data,url) for r in off)+'</div>'
    board+=f'<h2 class="dl-section-title">{u["intake"]}</h2>'+''.join(initiative_card(i,data,url) for i in ordinary if i.get('project_key'))
    body+=f'<section id="board" data-dl-panel>{board}</section>'
    intake=f'<h2>{u["intake_title"]}</h2><p class="dl-meta">{u["intake_note"]}</p><div class="dl-filters" hidden><label>{u["search"]} <input type="search" data-dl-search></label><label>{u["priority"]} <select data-dl-priority><option value="">{u["all"]}</option>'+''.join(f'<option>{p}</option>' for p in ['PRI-1','PRI-2','PRI-3','PRI-4','PRI-5'])+f'</select></label><span data-dl-count role="status">{u["showing"]}: {len(ordinary)}</span></div><div class="dl-rows">'
    for i in ordinary:
        find=escape(' '.join([i['id'],i['title'],i['outcome']]).lower(),quote=True)
        intake+=f'<article class="dl-row" data-dl-item="{i["id"]}" data-find="{find}" data-priority="{" ".join(i["priorities"])}"><span class="dl-meta">{i["id"]}<br>{escape(i["priority"])}</span><div><h3>{link(url,portfolio._route(lang,i),i["title"])}</h3><p class="dl-meta">{escape(i["status"])}</p><p>{escape(i["outcome"])}</p></div><div><strong class="dl-meta">{u["next"]}</strong><p>{u["gates"][i["column"]]}</p>{link(url,workspace.route(lang,'program',i['project_key']+'/'),u['open_project']+' →') if i.get('project_key') else ''}</div></article>'
    intake+=f'</div><h2 class="dl-section-title">{u["standing"]}</h2><p class="dl-meta">{u["standing_note"]}</p><div class="dl-standing">'+''.join(f'<article class="dl-card"><span class="dl-meta">{i["id"]}</span><h3>{link(url,portfolio._route(lang,i),i["title"])}</h3><span class="dl-badge">{escape(i["status"])}</span></article>' for i in standing)+'</div>'
    body+=f'<section id="intake" data-dl-panel>{intake}</section>'
    documents=''
    for i in ordinary:
        if not i.get('project_key'):continue
        docs,_=workbook.documents(lang)
        documents+=initiative_card(i,data,url)+f'<p class="dl-meta">{u["full"]} · {len(docs)} · EN / RU</p><div class="dl-documents">'+''.join(f'<a class="dl-card" href="{workspace.relative(url,d["url"])}"><span class="dl-meta">{n:02d}</span><h3>{escape(d["label"])}</h3></a>' for n,d in enumerate(docs,1))+'</div>'
    body+=f'<section id="documents" data-dl-panel>{documents}</section><footer class="dl-source"><p>{u['footer']}: {data['review_date'] or u['unknown']} · {u['snapshot']}: {pf['date']}</p><p>{u["source"]}</p></footer>'
    body+=''.join(f'<template data-kb-detail="{r["Identifier"]}">{item_body(r,data,url,embedded=True)}</template>' for r in data['items'])
    return '<article class="dl-content" data-kanban-workspace>'+body+'</article>'


def build(output):
    from neighbours import VisibleText
    output=Path(output);count=0
    for lang in ('en','ru'):
        data=project(lang=lang);u=UI[lang];entries=[]
        routes=[(workspace.route(lang,'program'),None)]+[(workspace.route(lang,'program',f'items/{r["Identifier"].lower()}/'),r) for r in data['items']]
        for url,item in routes:
            title=item['title'] if item else u['title'];body=render(data,url,item)
            nav=''.join(link(url,workspace.route(lang,'program','#'+key),u[label]) for key,label in [('board','board'),('intake','intake'),('documents','documents')])
            page=workspace.page(url,lang,'program',title,body,nav,body_class='delivery-workspace')
            page=page.replace('</head>',f'<link rel="stylesheet" href="{workspace.asset(url,"delivery.css")}"><script defer src="{workspace.asset(url,"delivery.js")}"></script>'+kanban.assets(url)+'\n</head>',1)
            target=output/url.strip('/')/'index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(page)
            entries.append({'u':url,'t':title,'h':item['Identifier'] if item else title,'x':VisibleText(body).text()});count+=1
        (output/f'assets/search-program-{lang}.json').write_text(json.dumps(entries,ensure_ascii=False,separators=(',',':')))
    for name in ('delivery.css','delivery.js'):shutil.copyfile(workspace.ROOT/'portal/site'/name,output/'assets'/name)
    kanban.assets(workspace.route('en','program'),output)
    return count
