"""Mermaid sources of the project diagrams; render: python3 newdiagrams.py (writes newdiagrams.json)."""
import json, sys
sys.path.insert(0, '/tmp/aicc-d/portal/tools')

D = {}

D['journeys'] = {
'en': ('Journey selection rule', '''flowchart TD
  A["Candidate journey"] --> B{{"Material repeat or stalled volume in an existing MI report?"}}
  B -- Yes --> C{{"Does one process function own the process?"}}
  C -- Yes --> D{{"Established process and readable records?"}}
  D -- Yes --> E{{"Outcome measurable from existing MI?"}}
  E -- Yes --> F{{"A team for first use, and Risk Tier 2 holds?"}}
  F -- Yes --> G["Record the selection in the Decision Log and complete the journey annex"]
  B -- No --> N["Narrow the scope or wait on the named Dependency"]
  C -- No --> N
  D -- No --> N
  E -- No --> N
  F -- No --> N'''),
'ru': ('Правило выбора клиентского маршрута', '''flowchart TD
  A["Кандидат: клиентский маршрут"] --> B{{"Существенный объём повторных обращений или остановившихся кейсов по действующему отчёту MI?"}}
  B -- Да --> C{{"Процессом владеет одно профильное подразделение?"}}
  C -- Да --> D{{"Процесс устоялся, а записи доступны?"}}
  D -- Да --> E{{"Результат измерим по действующей отчётности MI?"}}
  E -- Да --> F{{"Есть группа для первого применения, и категория риска 2 сохраняется?"}}
  F -- Да --> G["Внести выбор в журнал решений и заполнить приложение по клиентскому маршруту"]
  B -- Нет --> N["Сузить объём работ или ожидать выполнения указанной зависимости"]
  C -- Нет --> N
  D -- Нет --> N
  E -- Нет --> N
  F -- Нет --> N'''),
}

D['how-it-works'] = {
'en': ('Workflow for each customer case', '''flowchart TD
  T["Trigger: new contact, repeat contact or stalled case"] --> EL{{"Meets the eligibility rules?"}}
  EL -- No --> EX["Existing process; no AI output"]
  EL -- Yes --> C["Confirm the customer and the journey"]
  C --> R["Assemble the records: contacts, cases, status, complaints"]
  C -- "Uncertain link" --> M["Manual investigation"]
  R -- "Missing, stale or conflicting record" --> M
  R --> I["Interpret: assistant output, checked before display"]
  I -- "Model or check fails" --> CO["Context-only mode or existing process"]
  I --> V["Employee reviews the evidence and the proposed next step"]
  CO --> V
  V -- "Accept or correct" --> A["Act: explain, resolve, request information, refer or escalate"]
  V -- "Reject or investigate" --> M
  M --> A
  A --> TC["Tell the customer: resolution or committed next step"]
  TC --> REC["Record the decision, correction, action and result"]
  REC --> EV["Corrections and outcomes feed the evaluation"]'''),
'ru': ('Порядок обработки кейса клиента', '''flowchart TD
  T["Поступление: новое или повторное обращение, остановившийся кейс"] --> EL{{"Кейс соответствует правилам отбора?"}}
  EL -- Нет --> EX["Действующий порядок; результатов AI нет"]
  EL -- Да --> C["Подтверждение клиента и клиентского маршрута"]
  C --> R["Сбор записей: обращения, кейсы, статус, жалобы"]
  C -- "Связь неоднозначна" --> M["Ручной разбор"]
  R -- "Запись отсутствует, устарела или противоречива" --> M
  R --> I["Интерпретация: результат ассистента проходит автоматический контроль до отображения"]
  I -- "Сбой модели или контроля" --> CO["Режим «только контекст» или действующий порядок"]
  I --> V["Работник изучает подтверждающие сведения и предлагаемый следующий шаг"]
  CO --> V
  V -- "Принять или исправить" --> A["Действие: объяснить, решить, запросить сведения, передать или эскалировать"]
  V -- "Отклонить или провести разбор" --> M
  M --> A
  A --> TC["Информирование клиента: решение или следующий шаг"]
  TC --> REC["Фиксация решения, исправлений, действия и результата"]
  REC --> EV["Исправления и результаты используются для оценки ассистента"]'''),
}

D['charter'] = {
'en': ('How much evidence each question needs', '''flowchart LR
  Q1["Phase 1, in the Lab<br/>Does the interpretation hold across the journey's states and exceptions?"] -- "coverage decides the size" --> S1["Normally 200–500 past cases labeled by Domain Experts"]
  Q2["Phase 2, first users<br/>Can employees use it, correct it, and fall back safely?"] -- "a representative group of employees" --> S2["At least 100 eligible live cases"]
  Q3["Phase 2, against the comparison population<br/>Did customer and operational results improve?"] -- "baseline, expected change and volume" --> S3["Calculated after the baseline"]
  S1 --> DM["Evidence for the decision after the MVP"]
  S2 --> DM
  S3 --> DM'''),
'ru': ('Объём подтверждающих данных по каждому вопросу', '''flowchart LR
  Q1["Этап 1, в лаборатории<br/>Сохраняется ли корректность интерпретации для всех состояний и исключительных ситуаций маршрута?"] -- "объём определяется охватом" --> S1["Как правило, 200–500 исторических кейсов, размеченных экспертами направления"]
  Q2["Этап 2, первые пользователи<br/>Могут ли работники пользоваться ассистентом, исправлять его и безопасно переходить на резервный режим?"] -- "репрезентативная группа работников" --> S2["Не менее 100 учитываемых кейсов в промышленной эксплуатации"]
  Q3["Этап 2, в сравнении с контрольной группой<br/>Улучшились ли результаты для клиентов и операционные показатели?"] -- "базовый уровень, ожидаемое изменение и объём" --> S3["Рассчитывается после определения базовых значений"]
  S1 --> DM["Подтверждающие данные для решения после MVP"]
  S2 --> DM
  S3 --> DM'''),
}

D['profile-payment'] = {
'en': ('Payment Issue Resolution: information flow', '''flowchart TD
  C["Customer and contacts"] --> X["Payment resolution context"]
  P["Authoritative payment state"] --> X
  K["Case or investigation state"] --> X
  KN["Approved payment-service knowledge"] --> RT["Knowledge retrieval"]
  X --> I["Issue interpretation"]
  RT --> I
  I --> V["Employee review"]
  V -- "explain or existing service action" --> O["Resolution and repeat-contact outcome"]
  V -- "fraud, dispute, sanctions or ambiguity" --> S["Existing specialist process"]'''),
'ru': ('Решение вопросов по платежам: поток сведений', '''flowchart TD
  C["Клиент и обращения"] --> X["Контекст платёжного вопроса"]
  P["Достоверный статус платежа"] --> X
  K["Статус обращения или расследования"] --> X
  KN["Утверждённая база знаний по обслуживанию платежей"] --> RT["Поиск и извлечение знаний"]
  X --> I["Интерпретация вопроса"]
  RT --> I
  I --> V["Проверка работником"]
  V -- "объяснение или действие в действующем порядке" --> O["Решение и результат по повторным обращениям"]
  V -- "мошенничество, спор, санкции или неоднозначность" --> S["Действующий порядок работы специалистов"]'''),
}

D['profile-dispute'] = {
'en': ('Card Dispute Progress Support: information flow', '''flowchart TD
  C["Customer and prior contacts"] --> X["Dispute servicing context"]
  DS["Dispute system: stage and milestones"] --> X
  EM["Evidence metadata: requested and received"] --> X
  KN["Effective scheme and Bank procedure"] --> RT["Knowledge retrieval"]
  X --> Q{{"Deadline or customer rights uncertain?"}}
  Q -- Yes --> SP["Dispute specialist"]
  Q -- No --> I["Stage and next-step interpretation"]
  RT --> I
  I --> V["Employee review"]
  V --> O["Stage explanation, precise evidence request or referral"]'''),
'ru': ('Сопровождение споров по картам: поток сведений', '''flowchart TD
  C["Клиент и предыдущие обращения"] --> X["Контекст сопровождения спора"]
  DS["Система учёта споров: стадия и контрольные даты"] --> X
  EM["Метаданные подтверждающих документов: запрошено и получено"] --> X
  KN["Действующие правила платёжной системы и процедура Банка"] --> RT["Поиск и извлечение знаний"]
  X --> Q{{"Есть неопределённость по сроку или правам клиента?"}}
  Q -- Да --> SP["Специалист по спорам"]
  Q -- Нет --> I["Интерпретация стадии и следующего шага"]
  RT --> I
  I --> V["Проверка работником"]
  V --> O["Объяснение стадии, точный запрос документов или передача специалисту"]'''),
}

D['profile-kyc'] = {
'en': ('Onboarding/KYC Progress Support: information boundary', '''flowchart TD
  Z["Restricted KYC and financial-crime zone:<br/>documents and images, analyst notes, risk scores and screening results, KYC and AML decision"]
  SYS["Onboarding/KYC source of truth"] --> PJ["Approved metadata projection"]
  PJ --> X["Onboarding progress context"]
  PC["Prior approved customer communications"] --> X
  KN["Customer-facing onboarding procedure"] --> RT["Separate servicing knowledge retrieval"]
  X --> I["Service-state explanation"]
  RT --> I
  I --> V["Employee review"]
  V --> O["Permitted information request, routing or specialist referral"]
  Z -. "no data path" .- X'''),
'ru': ('Сопровождение оформления и KYC: граница сведений', '''flowchart TD
  Z["Зона ограниченного доступа: KYC и финансовые преступления:<br/>документы и изображения, заметки аналитика, оценки риска и результаты проверки по спискам, решение по KYC и ПОД/ФТ"]
  SYS["Достоверный источник сведений об оформлении и KYC"] --> PJ["Утверждённая проекция метаданных"]
  PJ --> X["Контекст хода оформления"]
  PC["Ранее направленные утверждённые сообщения клиенту"] --> X
  KN["Клиентская процедура оформления"] --> RT["Отдельный поиск по корпусу знаний обслуживания"]
  X --> I["Объяснение статуса обслуживания"]
  RT --> I
  I --> V["Проверка работником"]
  V --> O["Допустимый запрос сведений, маршрутизация или передача специалисту"]
  Z -. "доступа к сведениям нет" .- X'''),
}

D['it-readiness'] = {
'en': ('How each capability is assessed', '''flowchart TD
  N["Capability the pilot needs"] --> A["Assess the Bank's current service and its constraints"]
  A --> D{"Disposition"}
  D -- Fits --> R["Reuse an existing service"]
  D -- "Near fit" --> E["Extend it with a limited change"]
  D -- "No shared service" --> P["Pilot-local component behind the intended interface"]
  D -- "Unsafe or unavailable" --> B["Narrow the journey or block live use"]
  P -. "stands in for a Platform function" .-> DEP["Dependency on the Platform Owner"]
  R --> O["Operate and collect evidence"]
  E --> O
  P --> O
  O --> S{{"A second consumer and proven operation?"}}
  S -- No --> K["Keep with the Solution or retire"]
  S -- Yes --> PR["Proposal to the Platform Owner (Solution Lifecycle Model 8.12)"]'''),
'ru': ('Оценка каждой функции', '''flowchart TD
  N["Функция, необходимая пилоту"] --> A["Оценить действующий сервис Банка и его ограничения"]
  A --> D{"Способ обеспечения"}
  D -- Соответствует --> R["Повторное использование действующего сервиса"]
  D -- "Почти соответствует" --> E["Доработка с ограниченным изменением"]
  D -- "Общего сервиса нет" --> P["Локальный компонент пилота за целевым интерфейсом"]
  D -- "Небезопасно или недоступно" --> B["Сужение маршрута или блокировка применения в промышленной среде"]
  P -. "заменяет функцию платформы AI" .-> DEP["Зависимость от владельца платформы"]
  R --> O["Эксплуатация и сбор подтверждающих материалов"]
  E --> O
  P --> O
  O --> S{{"Есть второй потребитель и подтверждённая эксплуатация?"}}
  S -- Нет --> K["Оставить в составе решения или вывести из эксплуатации"]
  S -- Да --> PR["Предложение владельцу платформы (п. 8.12 Модели жизненного цикла решений)"]'''),
}

# Placeholder in the page source -> new diagram key
PLACE = {'business-use-case-2': 'journeys', 'business-use-case-7': 'how-it-works', 'charter-guide-3': 'charter',
         'journey-profiles-2': 'profile-payment', 'journey-profiles-3': 'profile-dispute', 'journey-profiles-4': 'profile-kyc',
         'platform-map-1': 'it-readiness'}

if __name__ == '__main__':
    import build, html, re
    def wrap(code):
        # Break label lines before the renderer's own wrap width, so each line breaks once at a word boundary.
        return re.sub(r'"([^"]*)"', lambda m: '"%s"' % build.wrap_label(m[1], 26), code)
    jobs = [(f'project-{k}-{lang}-v5', wrap(D[k][lang][1])) for k in D for lang in ('en', 'ru')]
    out = build.render_diagrams(jobs, True)
    res = []
    for k in D:
        for lang in ('en', 'ru'):
            svg = out[f'project-{k}-{lang}-v5']
            if not svg: raise SystemExit('not rendered: ' + k + ' ' + lang)
            svg = svg['light']; ident = f'{lang}-project-{k}'; cap = D[k][lang][0]
            svg = re.sub(r'<svg\b', f'<svg role="img" aria-label="{html.escape(cap)}"', svg, count=1)
            svg = re.sub(r'(<svg\b[^>]*?) id="[^"]*"', rf'\1 id="{ident}"', svg, count=1)
            fig = f'<figure class="diagram" data-language="{lang}" tabindex="0" role="button" aria-haspopup="dialog" aria-expanded="false" aria-label="{html.escape(cap)}" title="{html.escape(cap)}">{svg}</figure>'
            res.append({'key': k, 'lang': lang, 'figure': fig})
    json.dump(res, open('/tmp/projnew/newdiagrams.json', 'w'), ensure_ascii=False)
    print('rendered', len(res))
