# AI Lab: language review (English and Russian)

Prepared 6 October 2026; applied the same day with the owner's framing: the Lab runs on the Bank's own infrastructure (on premises), named simply AI Lab, with no cloud provider named. Scope: wording, titles, section names and box labels of the AI Lab page in both languages, for a fintech reader, and the Russian as a proper translation. Layout and interaction are reviewed separately.

## Findings

1. **One name for the Lab.** The page says "AI Lab" in the navigation, "Cloud LAB" in the text and "On-Prem Lab" for the target. The corpus calls it "the Lab" (Vocabulary; Standards, Guardrails of the Lab), in Russian «лабораторная среда». Proposal: "AI Lab" as the section name, "the Lab" in text; Russian navigation «AI-лаборатория», text «лабораторная среда»; "On-Prem" becomes "the Bank's own environment".
2. **Corpus terms.** A scenario tested in the Lab is an Experiment, which ends accepted, as a Proposal for delivery, or rejected. "Promote / Discard" and "shelved" are replaced by those outcomes. "PII" becomes "personal data", "sandbox" becomes "the Lab" (Russian: no «песочница»), "GenAI" becomes "generative AI", "agentic" becomes "AI-agent", as in the catalog.
3. **Titles are titles.** Two section titles carry a second sentence ("Business Agility. What the operating model can do."; "The Intent Loop. How the two systems converse."). The second sentence moves to the introduction line; titles become "Capabilities" and "The intent loop". "Cloud LAB Governance Guardrails Scorecard" becomes "Lab guardrails scorecard".
4. **Case and spelling.** Stage names are typed in capitals (DEFINE SCENARIOS); the capitals belong to the style sheet, not the text. Labels go to sentence case. British spellings (authorise, formalised, categorised, prioritisation, anonymisation) become American, as in the catalog.
5. **Plain fintech English.** Metaphors that do not land with bank readers are replaced: "public covenant", "instruments it", "decision-grade", "risk envelope", "folds outcomes back", "sense-making", "Agentic Intelligence", "The Dual Operating System". Meaning is kept.
6. **Errors.** "Performance Metrics (KRIs)" describes KPIs (KRIs are risk indicators): now "Performance metrics (KPIs)". "Observability" as a lane holds success measures, not system telemetry: now "Measurement".
7. **Russian.** Calques replaced: «Двойная операционная система», «агентный интеллект», «авторитетные источники», «агентный паттерн», «Изоляция песочницы», «Продолжить / отказаться». Stage names become nouns («Отбор сценариев», «Подготовка данных»), which is how Russian labels a process step. «Направление работы» for a lane is replaced by «Блок работ», because «направление» is the corpus term for a Domain. Guardrails are «защитные механизмы», as in the Standards record («Защитные механизмы лабораторной среды»).
8. **Grounding, for a later pass.** The scorecard's concerns overlap with the seven guardrails of the Lab in the Standards record (LAB-001 to LAB-007) but are not the same list. The page should show those seven, with their evidence, once the wording is settled.

Changes proposed: English 175 texts, Russian 120 texts, of 209. Interface labels: see the end.

## Proposed wording

**subtitle**
- EN now: Scenario Hypothesis Validation
- EN new: Experiments with AI scenarios
- RU now: Проверка гипотез по сценариям
- RU new: Эксперименты со сценариями AI

**intro**
- EN now: Once established, the Cloud LAB runs continuously. New scenarios enter the validation flow at any time; data flows from production into the sandbox via read-only ETL; agentic workflows are constructed, measured, and either promoted toward production or shelved. The lab persists indefinitely as the bank's GenAI exploration runtime.
- EN new: The Lab is an isolated environment that runs continuously. A scenario can enter it at any time as an Experiment; data arrives as read-only extracts from the Bank's systems; the AI-agent workflow is built, measured, and then accepted, turned into a Proposal for delivery, or rejected. The Lab is where the Bank tries generative AI before it commits to it.
- RU now: После создания Cloud LAB работает непрерывно. Новые сценарии могут поступать на проверку в любой момент; данные из промышленных систем передаются в песочницу через ETL только для чтения; агентные процессы разрабатываются, оцениваются и либо направляются к промышленному внедрению, либо откладываются. Лаборатория постоянно служит средой для исследования возможностей GenAI в банке.
- RU new: Лабораторная среда — изолированная среда, которая работает постоянно. Сценарий может поступить в неё в любой момент в виде эксперимента; данные поступают в виде выгрузок из систем Банка, доступных только для чтения; процесс с участием AI-агентов разрабатывается, измеряется и по итогам принимается, преобразуется в предложение о разработке и внедрении или отклоняется. Здесь Банк проверяет генеративный AI до того, как брать на себя обязательства.

**stage-1**
- EN now: DEFINE SCENARIOS
- EN new: Define scenarios
- RU now: ОПРЕДЕЛИТЬ СЦЕНАРИИ
- RU new: Отбор сценариев

**stage-2**
- EN now: ESTABLISH CLOUD LAB
- EN new: Set up the Lab
- RU now: СОЗДАТЬ CLOUD LAB
- RU new: Подготовка лабораторной среды

**stage-3**
- EN now: CHOOSE SCENARIO
- EN new: Choose a scenario
- RU now: ВЫБРАТЬ СЦЕНАРИЙ
- RU new: Выбор сценария

**stage-4**
- EN now: PREPARE DATA
- EN new: Prepare data
- RU now: ПОДГОТОВИТЬ ДАННЫЕ
- RU new: Подготовка данных

**stage-5**
- EN now: AGENTIC WORKFLOW
- EN new: Build the AI-agent workflow
- RU now: АГЕНТНЫЙ ПРОЦЕСС
- RU new: Разработка процесса с AI-агентами

**stage-6**
- EN now: VALIDATE
- EN new: Validate
- RU now: ПРОВЕРИТЬ
- RU new: Проверка

**lane-A**
- EN now: Governance & Decisions
- EN new: Governance & decisions

**lane-B**
- EN now: Risk & Controls
- EN new: Risk & controls

**lane-C**
- EN now: Operations & Processes
- EN new: Operations & processes

**lane-D**
- EN now: Data & Analytics
- EN new: Data & analytics

**lane-E**
- EN now: Observability
- EN new: Measurement
- RU now: Наблюдаемость
- RU new: Измерение результатов

**task-a-1-1-name**
- EN now: Secure Commitment
- EN new: Secure a sponsor
- RU now: Заручиться поддержкой
- RU new: Найти спонсора

**task-a-1-1-desc**
- EN now: Identify business sponsor; informal commitment
- EN new: Name the business sponsor and agree informally
- RU now: Определить бизнес-спонсора; получить предварительную договорённость
- RU new: Назначить бизнес-спонсора и получить его предварительное согласие

**task-a-1-2-name**
- EN now: Identify Scenarios
- EN new: Identify scenarios

**task-a-1-2-desc**
- EN now: Map service-level scenarios to validate
- EN new: List the scenarios to test, service by service
- RU now: Составить карту сценариев на уровне сервисов для проверки
- RU new: Составить перечень сценариев для проверки по каждой услуге

**task-a-2-1-name**
- EN now: Account Registration
- EN new: Open the cloud account
- RU now: Регистрация аккаунта
- RU new: Открыть облачную учётную запись

**task-a-2-1-desc**
- EN now: AWS approvals; vendor onboarding sign-off
- EN new: Cloud provider approvals; provider check signed off
- RU now: Согласования AWS; одобрение подключения поставщика
- RU new: Согласования с облачным провайдером; проверка провайдера завершена

**task-a-2-2-name**
- EN now: Define IAM and Policies
- EN new: Set access roles and policies
- RU now: Определить IAM и политики
- RU new: Настроить роли и политики доступа

**task-a-2-2-desc**
- EN now: Roles, access policies, audit gates
- EN new: Roles, access policies, audit checkpoints

**task-a-3-1-desc**
- EN now: Pick next scenario from validated backlog
- EN new: Pick the next scenario from the validated backlog

**task-a-4-1-name**
- EN now: Data Ownership
- EN new: Data ownership

**task-a-4-1-desc**
- EN now: Verify usage rights and privacy stance
- EN new: Confirm the right to use the data and the privacy position
- RU now: Проверить права использования и подход к конфиденциальности
- RU new: Подтвердить право использования данных и требования к их защите

**task-a-4-2-name**
- EN now: Identify Data Sources
- EN new: Identify data sources

**task-a-4-2-desc**
- RU now: Авторитетные источники для сценария
- RU new: Достоверные источники данных для сценария

**task-a-5-1-desc**
- EN now: Capture stakeholder requirements and acceptance
- EN new: Record stakeholder requirements and acceptance criteria
- RU now: Зафиксировать требования заинтересованных сторон и условия приёмки
- RU new: Зафиксировать требования заинтересованных сторон и критерии приёмки

**task-a-5-2-name**
- EN now: Select Architecture
- EN new: Select the architecture

**task-a-5-2-desc**
- EN now: Pick agentic pattern; vet against constraints
- EN new: Choose the AI-agent pattern; check it against constraints
- RU now: Выбрать агентный паттерн; проверить соответствие ограничениям
- RU new: Выбрать архитектурный шаблон для AI-агентов и проверить его на соответствие ограничениям

**task-a-6-1-name**
- EN now: Stakeholder Demo
- EN new: Sponsor demo
- RU now: Демонстрация заинтересованным сторонам
- RU new: Демонстрация спонсору

**task-a-6-1-desc**
- EN now: Show to sponsor; capture feedback
- EN new: Show the result to the sponsor; record feedback

**task-a-6-2-name**
- EN now: Promote / Discard
- EN new: Accept, propose or reject
- RU now: Продолжить / отказаться
- RU new: Принять, предложить или отклонить

**task-a-6-2-desc**
- EN now: Compare to KPIs; route to On-Prem or shelve
- EN new: Compare with the KPIs; propose for delivery in the Bank's environment, or close
- RU now: Сопоставить с KPI; передать в локальную среду (On-Prem) или отложить
- RU new: Сопоставить с KPI; предложить для разработки и внедрения в среде Банка или закрыть

**task-b-2-1-name**
- EN now: Sandbox Isolation
- EN new: Isolate the Lab
- RU now: Изоляция песочницы
- RU new: Изоляция лабораторной среды

**task-b-2-2-name**
- EN now: Define Guardrails
- EN new: Define guardrails
- RU now: Определить ограничения
- RU new: Определить защитные механизмы

**task-b-2-2-desc**
- EN now: Lab-level constraints on agentic outputs
- EN new: Lab-wide limits on what AI agents may produce and do
- RU now: Ограничения на результаты работы агентов на уровне лаборатории
- RU new: Общие для лабораторной среды ограничения на результаты и действия AI-агентов

**task-b-3-1-name**
- EN now: Risk Assessment
- EN new: Risk assessment

**task-b-3-1-desc**
- EN now: What's the risk envelope for this scenario?
- EN new: Set the risk limits for this scenario
- RU now: Каковы границы риска для этого сценария?
- RU new: Определить допустимые границы риска для сценария

**task-b-4-1-name**
- EN now: PII Assessment
- EN new: Personal data assessment

**task-b-4-1-desc**
- RU now: Маскировать, скрыть или исключить персональные данные
- RU new: Маскировать, удалить или исключить персональные данные

**task-b-4-2-name**
- EN now: Data Export Rules
- EN new: Data export rules

**task-b-4-2-desc**
- EN now: Confirm export-only; no production write-back
- EN new: Confirm read-only extracts; nothing written back to the Bank's systems
- RU now: Подтвердить режим только экспорта; исключить запись в промышленные системы
- RU new: Подтвердить, что данные только выгружаются и ничего не записывается обратно в системы Банка

**task-b-5-1-name**
- EN now: Agentic Guardrails
- EN new: AI-agent guardrails
- RU now: Ограничения для агентов
- RU new: Защитные механизмы для AI-агентов

**task-b-5-1-desc**
- EN now: Drift, bias, grounding checks at build time
- EN new: Drift, bias, and grounding checks during the build
- RU now: Проверки дрейфа, смещений и опоры на источники при разработке
- RU new: Проверка дрейфа, смещений и привязки к источникам в ходе разработки

**task-b-6-1-name**
- EN now: Workflow Validation
- EN new: Workflow validation

**task-b-6-1-desc**
- EN now: Validate agentic workflow against guardrails
- EN new: Check the AI-agent workflow against the guardrails
- RU now: Проверить агентный процесс на соответствие ограничениям
- RU new: Проверить процесс с AI-агентами на соответствие защитным механизмам

**task-c-1-1-name**
- EN now: Scenario Mapping
- EN new: Scenario mapping
- RU now: Карта сценария
- RU new: Описание сценария

**task-c-1-1-desc**
- EN now: Map current service workflow; pick touchpoints
- EN new: Map the current service workflow; choose the points to change
- RU now: Описать текущий сервисный процесс; выбрать точки взаимодействия
- RU new: Описать текущий процесс оказания услуги и выбрать точки изменения

**task-c-2-1-name**
- EN now: Setup Services
- EN new: Set up services

**task-c-2-1-desc**
- EN now: Provision lab services; baseline scaffolding
- EN new: Provision Lab services and the base setup
- RU now: Развернуть сервисы лаборатории; подготовить базовую структуру
- RU new: Развернуть сервисы лабораторной среды и базовую конфигурацию

**task-c-3-1-desc**
- EN now: Define boundaries, expected workflow, dependencies
- EN new: Set the boundaries, the expected workflow, and dependencies

**task-c-3-2-name**
- EN now: Workflow Map
- EN new: Workflow map

**task-c-3-2-desc**
- EN now: Trace target workflow end-to-end
- EN new: Trace the target workflow end to end
- RU now: Проследить целевой процесс от начала до конца
- RU new: Описать целевой процесс от начала до конца

**task-c-4-1-name**
- EN now: ETL Execution
- EN new: Run the extract
- RU now: Выполнение ETL
- RU new: Выгрузка данных

**task-c-4-1-desc**
- EN now: Run scenario-specific extract + load
- EN new: Run the extract and load for the scenario
- RU now: Выполнить извлечение и загрузку данных для сценария
- RU new: Выгрузить и загрузить данные для сценария

**task-c-4-2-name**
- EN now: ETL Pipeline
- EN new: Extract pipeline
- RU now: Конвейер ETL
- RU new: Конвейер выгрузки

**task-c-4-2-desc**
- EN now: Build read-only export to AWS
- EN new: Build the read-only export to the cloud environment
- RU now: Организовать экспорт в AWS только для чтения
- RU new: Настроить выгрузку данных в облачную среду только для чтения

**task-c-5-1-name**
- EN now: Workflow Build
- EN new: Build the workflow

**task-c-5-1-desc**
- EN now: Construct agentic workflow; orchestrate sub-tasks
- EN new: Build the AI-agent workflow; orchestrate its steps
- RU now: Построить агентный процесс; организовать выполнение подзадач
- RU new: Построить процесс с AI-агентами и организовать выполнение его шагов

**task-c-6-1-name**
- EN now: Adoption Guidelines
- EN new: Adoption guide

**task-c-6-1-desc**
- EN now: What changes if this lands in production
- EN new: What changes if this goes into production
- RU now: Что изменится при промышленном внедрении
- RU new: Что изменится при промышленной эксплуатации

**task-d-1-1-name**
- EN now: Service Catalog
- EN new: Service catalog

**task-d-1-1-desc**
- EN now: Inventory service capabilities and dependencies
- EN new: List each service's functions and dependencies
- RU now: Описать возможности сервисов и их зависимости
- RU new: Описать функции услуг и их зависимости

**task-d-2-1-name**
- EN now: Define Data Pipeline
- EN new: Design the data pipeline
- RU now: Определить конвейер данных
- RU new: Спроектировать конвейер данных

**task-d-2-1-desc**
- EN now: Design read-only export pipeline
- EN new: Design the read-only export pipeline

**task-d-4-1-name**
- EN now: Catalog & Map
- EN new: Catalog & map data

**task-d-4-1-desc**
- EN now: Inventory available data; trace what scenario needs
- EN new: List the available data; trace what the scenario needs

**task-d-4-2-name**
- EN now: Extract & QC
- EN new: Extract & check quality
- RU now: Извлечение и контроль качества
- RU new: Выгрузка и контроль качества

**task-d-4-2-desc**
- EN now: Run scenario ETL; verify data fitness
- EN new: Run the scenario extract; check the data is fit for use
- RU now: Выполнить ETL для сценария; проверить пригодность данных
- RU new: Выполнить выгрузку для сценария и проверить пригодность данных

**task-d-5-1-name**
- EN now: Data Flows
- EN new: Data flows

**task-d-5-1-desc**
- EN now: Wire data through the agentic workflow
- EN new: Connect the data to the AI-agent workflow
- RU now: Подключить потоки данных к агентному процессу
- RU new: Подключить данные к процессу с AI-агентами

**task-d-5-2-name**
- EN now: Analytics Flows
- EN new: Analytics
- RU now: Аналитические потоки
- RU new: Аналитика

**task-d-5-2-desc**
- EN now: Analytics layer over workflow outputs
- EN new: Analytics over the workflow's outputs
- RU now: Аналитический слой над результатами процесса
- RU new: Аналитика по результатам процесса

**task-d-6-1-name**
- EN now: Data Correctness
- EN new: Data correctness

**task-d-6-1-desc**
- EN now: Validate analytical results against ground truth
- EN new: Check analytical results against reference data

**task-d-6-2-name**
- EN now: Analytics Quality
- EN new: Analytics quality

**task-d-6-2-desc**
- EN now: Check correctness and consistency of analytics outputs
- EN new: Check the analytics outputs are correct and consistent

**task-e-1-1-name**
- EN now: Hypothesis OKRs
- EN new: Hypothesis targets
- RU now: OKR гипотезы
- RU new: Целевые показатели гипотезы

**task-e-1-1-desc**
- EN now: Define what success looks like; pick KPI
- EN new: Define what success looks like; choose the KPIs

**task-e-3-1-name**
- EN now: Scenario Metric
- EN new: Scenario metric

**task-e-3-1-desc**
- EN now: Per-scenario success criterion
- EN new: The success criterion for this scenario
- RU now: Критерий успеха для конкретного сценария
- RU new: Критерий успеха для сценария

**task-e-4-1-name**
- EN now: Data Quality Metrics
- EN new: Data quality metrics

**task-e-4-1-desc**
- EN now: Track completeness, freshness, drift
- EN new: Track completeness, freshness, and drift

**task-e-5-1-name**
- EN now: Workflow Metrics
- EN new: Workflow metrics

**task-e-5-1-desc**
- EN now: Functional + observability sanity tests
- EN new: Basic functional and monitoring tests
- RU now: Базовые проверки функциональности и наблюдаемости
- RU new: Базовые проверки работоспособности и мониторинга

**task-e-6-1-name**
- EN now: KPI Evaluation
- EN new: KPI evaluation

**task-e-6-1-desc**
- EN now: Hypothesis validation result; decision input
- EN new: Result of the hypothesis test; input to the decision

**task-e-6-2-name**
- EN now: Benchmarking Framework
- EN new: Benchmarking
- RU now: Система сравнительной оценки
- RU new: Сравнительная оценка

**task-e-6-2-desc**
- EN now: Compare against baseline; cost analysis
- EN new: Compare with the baseline; analyze cost

**task-e-6-3-name**
- EN now: Acceptance Criteria
- EN new: Acceptance criteria

**task-e-6-3-desc**
- EN now: Per-scenario acceptance gates
- EN new: Acceptance conditions for this scenario
- RU now: Контрольные условия приёмки для сценария
- RU new: Условия приёмки для сценария

**systems-title**
- EN now: The Dual Operating System
- EN new: Two operating systems: people and AI agents
- RU now: Двойная операционная система
- RU new: Две системы: люди и AI-агенты

**systems-intro**
- EN now: The dual model means Human Governance steers, sets intent, owns accountability; Agentic Intelligence collects signals, analyzes, reasons, executes, learns. They run in parallel, bound by a single intent loop and a non-negotiable trust perimeter.
- EN new: People steer: they set the intent and carry accountability. AI agents gather signals, analyze, reason, execute, and learn. The two work in parallel, joined by one intent loop and a trust perimeter that is not negotiable.
- RU now: В двойной модели люди управляют, определяют намерение и несут ответственность; агентный интеллект собирает сигналы, анализирует, рассуждает, исполняет и обучается. Обе системы работают параллельно, связаны единым циклом взаимодействия и обязательными границами доверия.
- RU new: Люди направляют работу: определяют цель и несут ответственность. AI-агенты собирают сигналы, анализируют, рассуждают, исполняют и обучаются. Обе системы работают параллельно и связаны единым циклом управления и неизменными границами доверия.

**systems-connection**
- EN now: The Intent Loop
- EN new: The intent loop
- RU now: Цикл взаимодействия
- RU new: Цикл управления

**system-1-duty-1-name**
- EN now: Strategic Direction
- EN new: Strategic direction

**system-1-duty-2-name**
- EN now: Ethical & Regulatory Stewardship
- EN new: Ethics & regulation
- RU now: Этическая и регуляторная ответственность
- RU new: Этика и соблюдение требований

**system-1-duty-2-desc**
- EN now: Owns the relationship with regulators, customers, and the public covenant.
- EN new: Owns the relationship with regulators, customers, and the public.
- RU now: Отвечает за отношения с регуляторами, клиентами и выполнение обязательств перед обществом.
- RU new: Отвечает за отношения с регуляторами, клиентами и обществом.

**system-1-duty-3-name**
- EN now: Final Decision Rights
- EN new: Final decision rights

**system-1-duty-3-desc**
- EN now: Reserves authority over high-stakes, irreversible, and reputational calls.
- EN new: Keeps authority over high-stakes, irreversible, and reputational decisions.
- RU now: Сохраняет полномочия в решениях с высокими ставками, необратимыми последствиями и репутационными рисками.
- RU new: Сохраняет за собой решения с высокими ставками, необратимыми последствиями и репутационным риском.

**system-1-duty-5-name**
- EN now: Sense-making & Recalibration
- EN new: Review & recalibration
- RU now: Осмысление и корректировка
- RU new: Анализ и корректировка

**system-1-duty-5-desc**
- EN now: Reads the institution against its purpose; redirects intent when context shifts.
- EN new: Checks the Bank against its purpose; resets the intent when the context changes.
- RU now: Оценивает работу организации относительно её предназначения; пересматривает намерение при изменении контекста.
- RU new: Сверяет работу Банка с его целями и уточняет цель при изменении условий.

**system-1-label**
- EN now: ◆ SYSTEM A
- EN new: System A
- RU now: ◆ СИСТЕМА A
- RU new: Система A

**system-1-name**
- EN now: Human Governance
- EN new: People
- RU now: Управление со стороны людей
- RU new: Люди

**system-1-role**
- RU now: Полномочия · Суждение · Намерение
- RU new: Полномочия · Суждение · Цель

**system-2-duty-1-name**
- EN now: Continuous Sensing
- EN new: Continuous monitoring
- RU now: Непрерывное наблюдение
- RU new: Непрерывный мониторинг

**system-2-duty-1-desc**
- EN now: Watches signals across customer, market, risk, ops, and workforce in real time.
- EN new: Watches signals on customers, markets, risk, operations, and staff in real time.
- RU now: Отслеживает сигналы о клиентах, рынке, рисках, операциях и сотрудниках в реальном времени.
- RU new: Отслеживает сигналы о клиентах, рынках, рисках, операциях и персонале в реальном времени.

**system-2-duty-2-name**
- EN now: Multi-lens Reasoning
- EN new: Multi-angle analysis
- RU now: Многомерное рассуждение
- RU new: Многофакторный анализ

**system-2-duty-2-desc**
- EN now: Frames decisions across competing dimensions — risk, return, customer, conduct.
- EN new: Weighs decisions across competing factors — risk, return, customer, conduct.
- RU now: Рассматривает решения с учётом конкурирующих факторов — риска, доходности, интересов клиента и делового поведения.
- RU new: Оценивает решения с учётом конкурирующих факторов — риска, доходности, интересов клиента и добросовестного поведения.

**system-2-duty-3-name**
- EN now: Decision-grade Options
- EN new: Options for decision
- RU now: Варианты для принятия решений
- RU new: Варианты решений

**system-2-duty-3-desc**
- EN now: Surfaces shaped alternatives with confidence, trade-offs, and provenance.
- EN new: Presents worked-out options with confidence, trade-offs, and sources.
- RU now: Предлагает проработанные альтернативы с оценкой уверенности, компромиссов и происхождения данных.
- RU new: Предлагает проработанные варианты с оценкой уверенности, компромиссов и источников.

**system-2-duty-4-name**
- EN now: Execution & Automation
- EN new: Execution & automation

**system-2-duty-4-desc**
- EN now: Carries out authorized actions, handles routine work, holds the audit trail.
- EN new: Carries out authorized actions and routine work, and keeps the audit trail.
- RU now: Выполняет разрешённые действия и рутинные задачи, сохраняет аудиторский след.
- RU new: Выполняет разрешённые действия и рутинную работу и ведёт аудиторский след.

**system-2-duty-5-name**
- EN now: Closed-loop Learning
- EN new: Learning from results
- RU now: Обучение с обратной связью
- RU new: Обучение на результатах

**system-2-duty-5-desc**
- EN now: Folds outcomes back into models; flags drift; proposes recalibrations to humans.
- EN new: Feeds results back into models; flags drift; proposes adjustments to people.
- RU now: Возвращает результаты в модели; отмечает дрейф; предлагает людям корректировки.
- RU new: Учитывает результаты в моделях, сообщает о дрейфе и предлагает людям корректировки.

**system-2-label**
- EN now: ● SYSTEM B
- EN new: System B
- RU now: ● СИСТЕМА B
- RU new: Система B

**system-2-name**
- EN now: Agentic Intelligence
- EN new: AI agents
- RU now: Агентный интеллект
- RU new: AI-агенты

**system-2-role**
- EN now: Sensing · Reasoning · Execution · Learning
- EN new: Monitoring · Analysis · Execution · Learning
- RU now: Наблюдение · Рассуждение · Исполнение · Обучение
- RU new: Мониторинг · Анализ · Исполнение · Обучение

**implication-label**
- EN now: Implication
- EN new: What this means
- RU now: Вывод
- RU new: Что это значит

**implication**
- EN now: Decision rights remain human. Decision velocity, breadth, and confidence become agentic-augmented. The institution does not delegate judgment — it instruments it.
- EN new: Decision rights stay with people. AI agents make decisions faster, wider in scope, and better evidenced. The Bank does not hand over judgment; it equips it.
- RU now: Право принимать решения остаётся у людей. Скорость, широта охвата и уверенность в решениях растут благодаря агентам. Организация не передаёт суждение агентам — она оснащает его инструментами.
- RU new: Право принимать решения остаётся за людьми. AI-агенты делают решения быстрее, полнее и обоснованнее. Банк не передаёт суждение AI, а вооружает его.

**capabilities-title**
- EN now: Business Agility. What the operating model can do.
- EN new: Capabilities
- RU now: Гибкость бизнеса. Что умеет операционная модель.
- RU new: Возможности

**capabilities-intro**
- EN now: Analyze · Reason · Decide · Act · Learn · Govern · Engage
- EN new: What the operating model can do: analyze · reason · decide · act · learn · govern · engage
- RU now: Анализировать · Рассуждать · Решать · Действовать · Обучаться · Управлять · Взаимодействовать
- RU new: Что умеет операционная модель: анализировать · рассуждать · решать · действовать · обучаться · управлять · взаимодействовать

**capabilities-1-desc**
- EN now: Reads signals across customers, markets, risk, ops, and people in continuous streams.
- EN new: Reads signals on customers, markets, risk, operations, and people continuously.
- RU now: Непрерывно считывает сигналы о клиентах, рынках, рисках, операциях и людях.
- RU new: Непрерывно получает сигналы о клиентах, рынках, рисках, операциях и персонале.

**capabilities-2-desc**
- EN now: Frames decisions across competing dimensions — risk, return, customer, conduct.
- EN new: Weighs decisions across competing factors — risk, return, customer, conduct.
- RU now: Рассматривает решения с учётом конкурирующих факторов — риска, доходности, интересов клиента и делового поведения.
- RU new: Оценивает решения с учётом конкурирующих факторов — риска, доходности, интересов клиента и добросовестного поведения.

**capabilities-3-desc**
- EN now: Surfaces shaped alternatives with confidence, trade-offs, and provenance.
- EN new: Presents worked-out options with confidence, trade-offs, and sources.
- RU now: Предлагает проработанные альтернативы с оценкой уверенности, компромиссов и происхождения данных.
- RU new: Предлагает проработанные варианты с оценкой уверенности, компромиссов и источников.

**capabilities-4-desc**
- EN now: Carries out authorized actions with attribution and an immutable audit trail.
- EN new: Carries out authorized actions, records who did what, and keeps an unalterable audit trail.
- RU now: Выполняет разрешённые действия с указанием исполнителя и неизменяемым аудиторским следом.
- RU new: Выполняет разрешённые действия с указанием исполнителя и ведёт неизменяемый аудиторский след.

**capabilities-5-desc**
- EN now: Folds outcomes back into models — flags drift, proposes recalibrations.
- EN new: Feeds results back into models — flags drift, proposes adjustments.
- RU now: Возвращает результаты в модели — отмечает дрейф и предлагает корректировки.
- RU new: Учитывает результаты в моделях — сообщает о дрейфе и предлагает корректировки.

**capabilities-6-desc**
- EN now: Holds the perimeter, the guardrails, and the chain of accountability.
- EN new: Maintains the perimeter, the guardrails, and the chain of accountability.
- RU now: Поддерживает периметр, ограничения и цепочку ответственности.
- RU new: Поддерживает границы, защитные механизмы и цепочку ответственности.

**capabilities-7-desc**
- EN now: Connects with customers, regulators, and partners — the institution's voice.
- EN new: Speaks with customers, regulators, and partners on the Bank's behalf.
- RU now: Общается с клиентами, регуляторами и партнёрами — представляет голос организации.
- RU new: Взаимодействует с клиентами, регуляторами и партнёрами от имени Банка.

**loop-title**
- EN now: The Intent Loop. How the two systems converse.
- EN new: The intent loop
- RU now: Цикл взаимодействия. Как общаются две системы.
- RU new: Цикл управления

**loop-intro**
- EN now: Intent → Insight → Action → Audit · A continuous cycle
- EN new: How people and AI agents work together: intent → insight → action → audit, continuously
- RU now: Намерение → Анализ → Действие → Аудит · Непрерывный цикл
- RU new: Как люди и AI-агенты работают вместе: цель → анализ → действие → аудит, непрерывно

**loop-1-name**
- RU now: Намерение
- RU new: Цель

**loop-1-desc**
- EN now: Humans declare the outcome, the constraints, the risk appetite, and the ethical perimeter. Not instructions — direction.
- EN new: People set the outcome, the constraints, the risk appetite, and the ethical limits. Direction, not instructions.
- RU now: Люди определяют результат, ограничения, риск-аппетит и этические границы. Задают направление, а не инструкции.
- RU new: Люди задают результат, ограничения, риск-аппетит и этические границы — направление, а не инструкции.

**loop-2-desc**
- EN now: Agents sense across data, reason across lenses, and surface decision-grade options with confidence and trade-offs.
- EN new: AI agents analyze the data from several angles and present options for decision, with confidence and trade-offs.
- RU now: Агенты наблюдают за данными, рассуждают с разных точек зрения и предлагают варианты для принятия решений с оценкой уверенности и компромиссов.
- RU new: AI-агенты анализируют данные с разных сторон и предлагают варианты решений с оценкой уверенности и компромиссов.

**loop-3-desc**
- EN now: Humans authorize. Agents execute or hand off. Every step is attributed, bounded, and reversible where it can be.
- EN new: People authorize. AI agents execute or hand over. Every step has an owner and limits, and can be reversed where possible.
- RU now: Люди разрешают. Агенты исполняют или передают задачу дальше. Каждый шаг имеет исполнителя, ограничен и, где возможно, обратим.
- RU new: Люди дают разрешение. AI-агенты исполняют или передают задачу дальше. У каждого шага есть исполнитель и границы, и где возможно — его можно отменить.

**loop-4-desc**
- EN now: Outcomes are logged, evaluated, contested if needed, and folded back into refined intent. The loop tightens with every turn.
- EN new: Results are logged, evaluated, challenged if needed, and used to sharpen the next intent. Each turn makes the loop more precise.
- RU now: Результаты фиксируются, оцениваются, при необходимости оспариваются и возвращаются в уточнённое намерение. Каждый проход делает цикл точнее.
- RU new: Результаты фиксируются, оцениваются, при необходимости оспариваются и уточняют следующую цель. С каждым оборотом цикл становится точнее.

**guardrails-title**
- EN now: Cloud LAB Governance Guardrails Scorecard
- EN new: Lab guardrails scorecard
- RU now: Контрольная карта управления и ограничений Cloud LAB
- RU new: Оценка защитных механизмов лабораторной среды

**guardrails-intro**
- EN now: Tracks major concern areas by setting guardrails and measuring best-practice adoption per concern. Each concern outlines compliance and governance aspects, balancing flexibility with assurance. The lab adopts the minimum guardrails required to maintain exploratory freedom.
- EN new: Each area of concern has its guardrails and a measure of how far good practice is applied, balancing freedom to explore with assurance. The Lab keeps only the guardrails it needs to stay safe while experimenting.
- RU now: Отслеживает основные области контроля: задаёт ограничения и оценивает применение лучших практик в каждой области. Каждая область описывает вопросы соблюдения требований и управления, сохраняя баланс гибкости и надёжности. Лаборатория принимает минимальные ограничения, необходимые для свободы исследовательской работы.
- RU new: Для каждой области контроля заданы защитные механизмы и оценено, насколько применяются лучшие практики, — с балансом между свободой экспериментов и надёжностью. В лабораторной среде действуют только те ограничения, которые необходимы для безопасной работы.

**guardrails-1-name**
- EN now: Governance & Decisions
- EN new: Governance & decisions

**guardrails-1-1-name**
- EN now: Decision Rights
- EN new: Decision rights

**guardrails-1-1-desc**
- EN now: Sponsor + IT lead authorise scenario promotion
- EN new: The sponsor and the IT lead approve moving a scenario forward
- RU now: Спонсор и руководитель IT разрешают продвижение сценария
- RU new: Спонсор и руководитель IT утверждают переход сценария к следующему этапу

**guardrails-1-2-desc**
- EN now: Hard list maintained: no PII export, no production write-back
- EN new: A fixed list: no personal data leaves, nothing is written back to the Bank's systems
- RU now: Поддерживается перечень запретов: никакого экспорта персональных данных и записи в промышленные системы
- RU new: Закреплённый перечень: персональные данные не выгружаются, ничего не записывается обратно в системы Банка

**guardrails-1-3-name**
- EN now: Disagreement Protocol
- EN new: Resolving disagreements

**guardrails-1-3-desc**
- EN now: Not formalised; case-by-case
- EN new: Not formalized; case by case
- RU now: Не формализован; решения принимаются по каждому случаю
- RU new: Не формализован; решается в каждом случае отдельно

**guardrails-2-name**
- EN now: Risk & Controls
- EN new: Risk & controls

**guardrails-2-1-name**
- EN now: Risk Taxonomy
- EN new: Risk classification

**guardrails-2-1-desc**
- EN now: Lab-level risk register; categorised by type
- EN new: Lab risk register, categorized by type

**guardrails-2-2-name**
- EN now: Output Integrity (Agentic Guardrails)
- EN new: Output integrity
- RU now: Надёжность результатов (ограничения для агентов)
- RU new: Надёжность результатов

**guardrails-2-2-desc**
- EN now: Drift, bias, grounding checks at build time
- EN new: Drift, bias, and grounding checks during the build
- RU now: Проверки дрейфа, смещений и опоры на источники при разработке
- RU new: Проверка дрейфа, смещений и привязки к источникам в ходе разработки

**guardrails-2-3-name**
- EN now: Sandbox Isolation
- EN new: Lab isolation
- RU now: Изоляция песочницы
- RU new: Изоляция лабораторной среды

**guardrails-2-3-desc**
- EN now: Perimeter, key management, no production access
- EN new: Perimeter, key management, no access to production
- RU now: Периметр, управление ключами, отсутствие доступа к промышленным системам
- RU new: Периметр, управление ключами, нет доступа к промышленным системам

**guardrails-2-4-name**
- EN now: PII Protection
- EN new: Personal data protection

**guardrails-2-4-desc**
- RU now: Маскирование, скрытие данных, правила экспорта
- RU new: Маскирование, удаление данных, правила выгрузки

**guardrails-2-5-name**
- EN now: Failure Protocol
- EN new: Failure handling
- RU now: Порядок действий при сбоях
- RU new: Действия при сбоях

**guardrails-2-5-desc**
- EN now: Basic rollback + alert protocols
- EN new: Basic rollback and alerting

**guardrails-3-name**
- EN now: Operations & Processes
- EN new: Operations & processes

**guardrails-3-1-name**
- EN now: Use-Case Selection
- EN new: Scenario selection
- RU now: Отбор сценариев применения
- RU new: Отбор сценариев

**guardrails-3-1-desc**
- EN now: Scenario backlog with prioritisation
- EN new: Prioritized backlog of scenarios

**guardrails-3-2-name**
- EN now: Workflow Mapping
- EN new: Workflow mapping

**guardrails-3-2-desc**
- EN now: Service workflow documented per scenario
- EN new: Service workflow documented for each scenario
- RU now: Сервисный процесс документируется для каждого сценария
- RU new: Процесс оказания услуги описан для каждого сценария

**guardrails-3-3-name**
- EN now: Operational Lifecycles
- EN new: Scenario lifecycle
- RU now: Операционные жизненные циклы
- RU new: Жизненный цикл сценария

**guardrails-3-3-desc**
- EN now: Scenario lifecycle: choose → build → validate
- EN new: Choose → build → validate
- RU now: Жизненный цикл сценария: выбрать → разработать → проверить
- RU new: Выбор → разработка → проверка

**guardrails-3-4-name**
- EN now: Promotion Pathway
- EN new: Path to delivery

**guardrails-3-4-desc**
- EN now: Informal handoff to On-Prem Lab
- EN new: Informal handover to the Bank's own environment
- RU now: Неформальная передача в локальную лабораторию (On-Prem)
- RU new: Неформальная передача в собственную среду Банка

**guardrails-4-name**
- EN now: Data & Analytics
- EN new: Data & analytics

**guardrails-4-1-name**
- EN now: Data Pipeline
- EN new: Data pipeline

**guardrails-4-1-desc**
- EN now: ETL pipeline operational; scenario-specific extracts
- EN new: Extract pipeline running; extracts made per scenario
- RU now: Конвейер ETL работает; выгрузки формируются под сценарий
- RU new: Конвейер выгрузки работает; выгрузки формируются под сценарий

**guardrails-4-2-desc**
- EN now: Quality checks at extract; correctness validated
- EN new: Quality checked at extract; correctness confirmed
- RU now: Проверки качества при извлечении; корректность подтверждается
- RU new: Качество проверяется при выгрузке; корректность подтверждается

**guardrails-4-3-name**
- EN now: Data Privacy
- EN new: Data privacy
- RU now: Конфиденциальность данных
- RU new: Защита данных

**guardrails-4-3-desc**
- EN now: Masking, anonymisation for sensitive fields
- EN new: Masking and anonymization of sensitive fields

**guardrails-4-4-name**
- EN now: Analytics Correctness
- EN new: Analytics correctness

**guardrails-4-4-desc**
- EN now: Analytics flows validated against ground truth
- EN new: Analytics checked against reference data
- RU now: Аналитические потоки проверяются по эталонным данным
- RU new: Аналитика проверяется по эталонным данным

**guardrails-5-name**
- EN now: Observability
- EN new: Measurement
- RU now: Наблюдаемость
- RU new: Измерение результатов

**guardrails-5-1-name**
- EN now: Performance Metrics (KRIs)
- EN new: Performance metrics (KPIs)
- RU now: Метрики результативности (KRI)
- RU new: Показатели результативности (KPI)

**guardrails-5-1-desc**
- EN now: Scenario-level KPIs tracked
- EN new: KPIs tracked for each scenario
- RU now: Отслеживаются KPI на уровне сценариев
- RU new: KPI отслеживаются по каждому сценарию

**guardrails-5-2-name**
- EN now: Hypothesis OKRs
- EN new: Hypothesis targets
- RU now: OKR гипотезы
- RU new: Целевые показатели гипотезы

**guardrails-5-2-desc**
- EN now: Hypothesis target defined per scenario
- EN new: Target set for each scenario's hypothesis
- RU now: Целевой результат гипотезы определён для каждого сценария
- RU new: Целевой результат гипотезы задан для каждого сценария

**guardrails-5-3-name**
- EN now: Workflow Metrics
- EN new: Workflow metrics

**guardrails-5-3-desc**
- EN now: Functional + integration metrics captured
- EN new: Functional and integration metrics recorded

**guardrails-5-4-name**
- EN now: Acceptance Criteria
- EN new: Acceptance criteria

**guardrails-5-4-desc**
- EN now: Per-scenario acceptance defined
- EN new: Acceptance defined for each scenario
- RU now: Условия приёмки определены для каждого сценария
- RU new: Условия приёмки заданы для каждого сценария

## Interface labels

| Label | EN now | EN new | RU now | RU new |
| --- | --- | --- | --- | --- |
| capabilities | Capabilities | Capabilities | Возможности | Возможности |
| concern | Concern | Concern | Область контроля | Область контроля |
| guardrails | Guardrails | Guardrails | Ограничения и контроль | Защитные механизмы |
| lanes | Workstream | Workstream | Направление работы | Блок работ |
| loop | Intent loop | Intent loop | Цикл взаимодействия | Цикл управления |
| matrix | Validation workflow | Experiment workflow | Проверка гипотез | Процесс эксперимента |
| posture | Posture | Posture | Подход | Подход |
| selection | Workflow view | Workflow view | Представление процесса | Вид процесса |
| systems | Operating model | Operating model | Операционная модель | Операционная модель |
| navigation | AI Lab | AI Lab | AI Lab | AI-лаборатория |

## Restructure, 6 October 2026

The language pass left the page's structure as it was; a reading for meaning showed that it did not hold. The page was restructured as follows, in both languages.

1. **Guardrails from the corpus.** The page opens with the seven guardrails of the Lab (LAB-001 to LAB-007) with their evidence, read by the builder from the Standards record, so the page cannot drift from the corpus.
2. **Experiment workflow.** A one-time setup column, then six steps that follow the corpus (Solution Lifecycle Model 8.13): intake, scope and hypothesis, data, build, evaluate, decide and report. Added: time-box, Risk Tier, data-protection sign-off, Outcome Report, and the decision by the Executive Sponsor or Domain Owner (accept, Proposal, reject). Merged: the four extraction cards, the duplicate acceptance and target cards. 41 cards became 37.
3. **People and AI agents.** The "Capabilities" section repeated the AI-agent duties word for word and claimed that the model decides, governs and speaks to regulators; it was removed. The two systems and the intent loop remain, under "How people and AI agents work together".
4. **Practice maturity.** The former "guardrails scorecard" is a self-assessment of how far good practice is applied in each control area, as a percentage of what the Bank expects of a production system. It now says so, shows four bands (0–25% not in place, 26–50% basic, 51–75% established, 76–100% strong), and each figure has a popup with its band, the band's meaning, the reason for the figure, and what would raise it. The figures themselves are unchanged.

