# Russian rewrite: style sheet for C-RU-NATURAL-ALIGNMENT

Revised 5 October 2026: Initiative is Russian again, Work Item is «задача», workflow and value stream stay Latin; board is «борд», Cadence is «рабочий цикл», after delivery is «пост-внедрение», the continuous delivery pipeline is «непрерывная разработка и внедрение», Unit governance is «Контроль работы подразделения».

Binding for every worker. Owner decisions of 4 October 2026 override older wording in the corpus, the
terminology reference and the translation map where they differ. Approvals and decision records are
not required (pre-production tuning); do not add Registry records.

## 1. Goal for each file

1. Compare the Russian file with its English source sentence by sentence. The English is the reference
   for meaning. Fix every drift: added, missing or changed rights, duties, conditions, limits, periods,
   quantities, roles, states, references. Record every drift found in your notes file.
2. Rewrite the Russian as natural formal Russian of a bank's internal regulations (положение, регламент),
   not as a word-for-word rendering of English. Restructure sentences freely; never change meaning.
3. Apply, in this order: this style sheet; `charter/ru/shared-technology-terminology.md` (accepted forms,
   except where §3 here overrides); `charter/ru/translation-en-ru-map.md` sections 3–4 (every «не: …» form
   is an error in the situation the row describes); `charter/ru/documents/vocabulary.md` 3.1–3.9.

## 2. Hard structural rules (the build rejects violations)

- Keep the YAML front matter exactly, including `source_sha256`, `source_revision`, `id`, `status`,
  `translation_status: reviewed`. Change only `title:` if the Russian title changes.
- Same headings in the same order with the same numbers; same numbered clauses (`1.1.`, `4.2.` …) in the
  same order; every table keeps its row count and column count; empty cells stay empty.
- Keep link targets `(...)`, `page:` references, anchors, identifiers (C-01, DR-2026-060, AICC-ORG-01-RU),
  ISO dates in tables/metadata, numbers, code spans, placeholders like `{title}`.
- Mermaid blocks: keep node IDs, edges, classes and layout lines; translate only label text in quotes.
- Change-log tables: translate text; keep version numbers, dates, decision IDs. Column header «Версия».
- Run `python3 .grace/changes/active/C-RU-NATURAL-ALIGNMENT/check_one.py <your files>` after each file;
  it must print OK. Then fix what the scan reports for your file.

## 3. Owner term decisions (override the terminology reference where different)

- Revision = **версия** (not «редакция»): «версия 2.1», column «Версия», «Версия 1.6 · 4 октября 2026 года».
  Language edition = **языковая версия** («русскоязычная версия корпуса»).
- **итерация**, **программный инкремент (PI)** — Russian, lowercase; after first use in a document «PI»
  is allowed, and in compounds PI stays: цель PI, PI-планирование, предсказуемость PI, неделя IP.
- Protected Latin work-item names, written with a capital letter, not translated, not declined:
  **Capability** (мн. ч. Capabilities, ж. р.), **Feature** (Features, ж. р.), **Story** (Stories, ж. р.),
  **Task** (Tasks, ж. р.), **Spike** (Spikes, м. р.), **Bug** (Bugs, м. р.), **Epic** (Epics, м. р.).
  Case is shown by the surrounding words: «по каждой Feature», «Feature принята в разработку».
- **Initiative is Russian** (owner decision of 5 October 2026): «инициатива», «паспорт инициативы»
  (template title «Паспорт инициативы»), «постоянная инициатива», «структура инициатив», «инициативы в
  работе». Ordinary business initiatives: «бизнес-инициативы».
- **Work Item = «задача»** (generic work item in Jira or the backlog); the Jira type Task stays «Task».
- Lowercase AICC terms (Vocabulary 3.3). Capitals only for: first word of a body's name (Совет директоров,
  Комитет Совета директоров, Правление Банка, Управляющий комитет по AI), «Банк», document titles
  (Положение об AICC, Бизнес-модель, Операционная модель, Модель управления портфелем, Модель жизненного
  цикла решений, Политика применения AI, Терминология и стиль, Заявление о намерениях по внедрению AI,
  Каталог документов, Общая деловая и технологическая терминология, guide titles), template titles when the
  template itself is meant (шаблон «Описание решения»), state and stage names when named as such in quotes
  («В работе», «Определение объёма»), the protected Latin names above and fixed names (AI, AICC, Jira, …).
- «решение» alone = the AICC term Solution. A decision is «управленческое решение», or a verb
  («решает», «утверждает», «принимает решение о …» only where no Solution is nearby). Avoid
  «решение о выпуске решения»-type sentences: «О выпуске решения решает куратор AICC».
- «проверка» alone = the AICC term Check (verification step). An ordinary check: «контроль», «сверка»,
  «убедиться», or «проверка» with a complement («проверка выполнимости»).
- «подразделение» for a function of the Bank (client function → «подразделение-заказчик»); keep the AICC
  terms «контрольная функция», «IT-функция».
- **workflow** stays Latin, lowercase in running text, indeclinable, masculine agreement: «workflow
  «Взаимодействие с заказчиком»», «каждый workflow», «в workflow «Рабочий цикл»»; part heading «Workflows».
- **value stream** stays Latin, lowercase, indeclinable, masculine; at its first use in each document or
  page explain it once: «value stream (сквозная последовательность действий, в ходе которой потребность
  превращается в ценный для клиента результат)».
- business case → **бизнес-кейс** (declined, masculine). AI agent → **AI-агент**. WIP limit → **WIP-лимит**.

## 4. Term table (English → Russian form in running text)

Bank Банк · Board Совет директоров · Board Committee Комитет Совета директоров · Data Sharing Arrangement
соглашение об обмене данными · Role роль · Hat дополнительная обязанность · Executive Sponsor куратор AICC ·
Holder исполнитель роли · Chief Executive Officer (position) председатель Правления Банка — a position; it fills the role куратор AICC, never replaces the role name · AICC Lead руководитель AICC · AICC Team команда AICC · Solution Engineer инженер
решений · AI Steering Committee Управляющий комитет по AI · Steering управляющее совещание (ежемесячное,
ежеквартальное, ежегодное управляющее совещание) · Domain направление · Product owner владелец продукта · Domain
Owner владелец направления · Domain Expert эксперт направления · Control Function контрольная функция · Three lines
модель трёх линий · Control Function Contact представитель контрольной функции · Platform Owner владелец
платформы · AI Platform платформа AI · Platform guardrails защитные механизмы платформы · Model модель ·
AI agent AI-агент · Assistant ассистент · Provider поставщик · AI output результат AI · Data class класс
данных · Human oversight контроль со стороны человека · Evaluation set оценочный набор · Alert level
сигнальное значение · Lab лабораторная среда · IT function IT-функция · Platform team платформенная
команда · Service Management система Service Management · Strategic Priority стратегический приоритет ·
Strategic Pillar стратегическое направление · Investment Envelope инвестиционный бюджет · Investment
Guardrails инвестиционные ограничения · Kind of work вид работ · Mix of Initiatives структура инициатив ·
Service area направление услуг · Service category категория услуг · Mode режим · Run-rate work текущие
работы · Standing Initiative постоянная инициатива · Enabling work обеспечивающие работы · Engagement
взаимодействие с заказчиком · Phase фаза · Service Agreement соглашение о взаимодействии · Assumption
допущение · Support level уровень поддержки · Outcome Report отчёт о результатах · Stakeholder
заинтересованное лицо · Package пакет · Package Definition описание пакета · Catalog каталог · Portfolio
портфель · Initiative инициатива · Initiative Brief паспорт инициативы · Business case бизнес-кейс ·
Solution решение · Solution Definition описание решения · Service сервис (service offered = услуга) · Service
step шаг обслуживания · Four signals четыре сигнала · Run cost эксплуатационные затраты · Sunset rule правило
вывода из эксплуатации · Product продукт · Experiment эксперимент · Receiver получатель · Handover передача ·
Proposal предложение · Adopted Solution внедрённое решение · Capability Capability · Feature Feature ·
Definition of ready критерии готовности к работе (DoR) · Definition of done критерии завершённости (DoD) ·
Work Item задача · Portfolio Backlog бэклог портфеля · Program Backlog бэклог программы · Iteration
Backlog бэклог итерации · Portfolio Kanban канбан портфеля · Portfolio management управление
портфелем · Funnel воронка · MVP минимально жизнеспособный продукт (MVP), далее MVP · Leading indicator
опережающий индикатор · Acceptance criteria критерии приёмки · Value hypothesis гипотеза ценности · Value
stream value stream · Program Kanban канбан программы · Class of service класс
обслуживания · Lane дорожка · Team команда · Teams Record состав команд · Program Increment программный
инкремент (PI) · Iteration итерация · Innovation and Planning week неделя инноваций и планирования (неделя
IP) · PI Objective цель PI · Dependency зависимость · Calendar календарь (not «запись о календаре») · Cadence рабочий цикл (masculine; not «расписание работы», «ритм работы»; descriptive «в едином ритме» stays; bare «цикл» is Loop — where both meet in one sentence, rephrase so they cannot be confused) · Blocked day
нерабочий день · gray day день ограниченной доступности · AICC portal портал AICC · Operating portal
операционный портал · Corporate share корпоративный сетевой ресурс · Dashboard панель показателей · Stage
стадия · Environment of use среда использования · Check проверка · Checker проверяющий · Validation
валидация · Suspension and stop приостановление и остановка · Governed source контролируемый источник ·
Acceptance приёмка · Release выпуск · First users первые пользователи · Release block раздел о выпуске ·
Emergency change экстренное изменение · Limit on Work in Progress WIP-лимит · WIP WIP · Risk Tier категория
риска · AI Registry реестр AI-решений · AI Incident инцидент AI · Severity степень серьёзности · Exception
отступление от требований (далее в том же пункте или абзаце — отступление; не «исключение») · Deficiency недостаток контроля · Control status статус контрольной процедуры · Accepted limit
принятое ограничение · Risks and Issues Record реестр рисков и проблем · AI Risk Appetite Statement
Заявление о риск-аппетите в отношении AI (title) · Maturity Level уровень зрелости · Measure показатель ·
Metric метрика · KPI KPI · Governance measures показатели управления · Milestone веха · Decision
управленческое решение · Escalation эскалация · Delegation делегирование · Decision Log журнал решений ·
Decision Record протокол решения · Appointments Record реестр назначений · Control Sign-Off заключение
контрольной функции · Business acceptor представитель заказчика по приёмке · Acceptance Checklist
контрольный лист приёмки · AI Incident Review разбор инцидента AI · Registry Snapshot снимок папки ·
Program Board борд программы · Team board борд команды · board борд, борды (masculine; never «доска»; Portfolio / Program Kanban stay «канбан»; dashboard stays «дашборд» / «панель показателей») · Roadmap дорожная карта · Template шаблон · Priorities Record список
приоритетов · Standards Record реестр стандартов · Control Matrix матрица контроля · Registry папка AICC (кратко: папка; «реестр» означает только Living record) ·
Workflow workflow · Record рабочий документ, рабочие документы (masculine; never «учётная запись», which means a user account and stays only in that sense: «учётные записи пользователей»; with governing documents: «нормативные и рабочие документы»; with Evidence record: «рабочие и подтверждающие документы»; обычная «запись в журнале», «запись каталога» сохраняется) · Living record реестр · Evidence record
подтверждающий документ · Working state рабочее состояние · cutover переход · Light mode облегчённый режим ·
Loop цикл · Review week неделя обзора · Short forms сокращения · Event мероприятие · Steering Summary итоги
управляющего совещания · Quarterly Report квартальный отчёт · Report to the Board Committee отчёт Комитету
Совета директоров · quarterly risk check ежеквартальная проверка рисков · Finding выявленное отклонение ·
Activation введение в действие · State состояние · Delivery (activity; portal section) разработка и внедрение · Service delivery оказание услуг · Delivery (stage of a Solution; phase of an Engagement) разработка · after delivery (the stage; titles, tabs, headings, table headers) пост-внедрение: «Пост-внедрение», «на этапе пост-внедрения», «в пост-внедрении» (plain «после внедрения» only as an ordinary time reference) · Continuous delivery pipeline непрерывная разработка и внедрение (short form after first mention: «поток НРВ»; never «конвейер», «доставка») · Unit governance (workflow, guide, set) Контроль работы подразделения: «workflow «Контроль работы подразделения»», «Руководство по контролю работы подразделения» (ordinary «управление» stays elsewhere) · Delivery measures показатели разработки и внедрения (never «поставка», which means a supply by a Provider).

States (quoted when named, lowercase in running text per the map): «Предложено», «Проработка», «Одобрено»,
«В работе», «Ожидание», «Отложено», «Выполнено», «На рассмотрении», «Принято», «Закрыто»,
«Перенаправлено», «Отклонено», «Отменено». Stages: «Определение объёма», «Бизнес-кейс», «MVP»,
«Реализация», «Определение», «Разработка» (Delivery, stage of a Solution), «Анализ», «Исследование», «Проектирование», «Разработка» (Develop, stage of a Feature),
«Проверка», «Развёртывание», «Эксплуатация», «Развитие», «Вывод из эксплуатации», «Передача»,
«Поддержка», «Пересмотр», «Испытание», «Предложение».

Service areas (quoted names): «Консультирование и формирование подходов», «Разработка и эксплуатация»,
«Содействие внедрению», «Контроль и оценка».

## 5. Drafting conventions

- Duties of a named party: present tense; «обязан» when emphasis is needed; «должен» only for document
  content. Rights «вправе». Prohibitions «не вправе», «не допускается», «запрещается». Recommendations
  «следует», «целесообразно».
- References: «в соответствии с разделом 4 Бизнес-модели», «(п. 5.2 Операционной модели)», «согласно
  пункту 4.1»; never «Бизнес-модели 4» or «по 6.3». Titles in references keep their capital.
- Introductions to tables: «… приведены в следующей таблице», not «Следующая таблица устанавливает».
- Headings and column headers are nouns; no question headings («Услуги AICC», not «Что предлагает AICC»).
- Dates in prose: «4 октября 2026 года»; ISO dates stay in tables and metadata.
- «(далее — X)» for abbreviations; «под X понимается» in definitions.
- People: «работник» (employee), «лицо» (person); not «человек проверяет».
- Do not overuse «осуществлять», «является», «данный», «в рамках»; prefer a plain verb with a named subject.
- Explanatory portal pages: plain, readable professional Russian (still formal); short sentences are fine.

## 6. Notes (your report)

Append to `.grace/changes/active/C-RU-NATURAL-ALIGNMENT/notes/<your batch>.md`:

- `## <file>` then bullets:
  - `DRIFT` — English and old Russian disagreed in meaning: clause, what differed, what you wrote.
  - `QUESTION` — a choice someone may want to revisit: clause, English, chosen Russian, alternative, why.
  - `ENGLISH?` — the English itself looks wrong or inconsistent (do not change English).
Keep notes short. Do not record routine rewording.

## 7. Boundaries

Edit only the files assigned to you. Never edit English files, Registry, Portfolio, other workers' files,
git state (no commit, no checkout, no stash). If a shared rule seems wrong, follow it and add a QUESTION.
