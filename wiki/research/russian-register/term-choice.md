# Form of shared terms in the Russian edition: evidence record

This record states, for each entry of the Shared Business and Technology Terminology and for terms used in the Russian edition but not yet listed there, the form proposed for the column «Форма в русском корпусе», the inflection pattern, the strength of the evidence and the effect on the corpus. The evidence and sources are in [term-choice-business-and-delivery.md](term-choice-business-and-delivery.md) and [term-choice-technology-and-ai.md](term-choice-technology-and-ai.md). The forms established on 4 October 2026 are stated in the draft Edition 1.6 of the technology vocabulary ([English](../../../charter/en/shared-technology-terminology.md), [Russian](../../../charter/ru/shared-technology-terminology.md)); the rendering of ordinary words and constructions by situation is stated in the draft Russian-only [EN–RU translation map](../../../charter/ru/translation-en-ru-map.md). The Status column records "Established" or "Under review".

## How Russian practice decides, in five rules

1. **Acronyms with no Cyrillic form stay Latin and indeclinable:** KPI, SLA, MVP, OKR, ESG, WSJF, WIP, PI, KYC, LLM, RAG, DAG, CI/CD. Each attaches to Russian through a head noun («матрица RACI», «метод WSJF», «архитектура RAG»).
2. **Compounds are hyphenated hybrids with a Russian head noun, never an English plural:** «WIP-лимиты», «PI-планирование», «BI-система», «AI-агенты», «ESG-факторы».
3. **Settled agile words are Cyrillic borrowings that decline:** бэклог, спринт, релиз, эпик, дашборд, канбан, код-ревью, бизнес-кейс, пайплайн, промпт-инъекция.
4. **Process, security, IT service management, data and governance concepts are Russian, as the standards and regulators write them:** поток создания ценности, рабочий процесс, развёртывание, промышленная среда, запрос на изменение, регистрация событий, управление доступом, инцидент, откат, модельный риск.
5. **Established exception:** AI, IT and ICT are written in Latin letters although regulators write ИИ and ИКТ; current practice also supports the Latin form, for example Yandex Cloud's «AI‑агент» and «агентный AI».

The corpus breaks these rules mainly with multi-word English phrases inside Russian sentences. These are the corpus changes, roughly by count: «business case» (~112) → «бизнес-кейс»; «workflow(s)» (~72) → «рабочий процесс»; «AI agent(s)» (~30) → «AI-агент(ы)»; «WIP limit(s)» (~30) → «WIP-лимит(ы)»; «журналирование» (15) → «регистрация событий»; «Заявка на изменение» (13) → «запрос на изменение»; «value stream» (11) → «поток создания ценности»; «Epic» (10) → «эпик».

## A. Entries of the shared terminology (sections 3–6)

| # | Universal term | Current RU | Proposed form in the RU corpus | Pattern | Conf. | Corpus change | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.1 | business case | бизнес-кейс | «бизнес-кейс» | m.; «бизнес-кейса», «бизнес-кейсы», «в бизнес-кейсе» | established | Yes: «business case» about 106, «business cases» 3, «Business case» 3; the corpus also mixes masculine and neuter agreement (BP P7). Application note «Форма множественного числа: business cases» must change | Established: бизнес-кейс |
| 3.2 | business intelligence / customer intelligence | бизнес-аналитика / клиентская аналитика | «бизнес-аналитика» / «клиентская аналитика» | f.; Latin only as compound prefix «BI-система» | high | No: Statement of Intent 2 occurrences already Russian | |
| 3.3 | dashboard | дашборд; информационная панель | «дашборд» | m.; «дашборда», «дашборды». The defined Record stays «Панель показателей» | high | Minor: the one generic occurrence; Record name unchanged. Drop «информационная панель» as an alternative to keep one form | Established: дашборд |
| 3.4 | ESG | экологические, социальные факторы и факторы корпоративного управления | «ESG» | indeclinable; compounds «ESG-факторы», «ESG-повестка» | high | No | |
| 3.5 | HR | управление персоналом; кадровая функция | «кадровая функция» in normative text; «HR» only in compounds | f.; «кадровой функции»; compounds «HR-функция», «HR-директор» | medium | No: corpus already writes «кадровая функция»; the entry should state that HR is the abbreviation, not the running-text form | |
| 3.6 | KPI | ключевой показатель эффективности (результативности) | «KPI» | indeclinable m.; «KPI цели», «несколько KPI»; avoid «KPI-показатель» (tautology) | high | No (5 occurrences already Latin) | |
| 3.7 | KYC | «Знай своего клиента» | «KYC» | indeclinable; first use «надлежащая проверка клиента (KYC)» or «принцип «Знай своего клиента» (KYC)» | medium | No (Statement of Intent 11.3.1 keeps KYC). Consider adding the Russian expansion at first use | |
| 3.8 | OKR | цели и ключевые результаты | «OKR» | indeclinable; «метод OKR», «по OKR», «цели OKR» | high | No | |
| 3.9 | RACI | матрица распределения ответственности | «матрица RACI» | «матрицы RACI», «по матрице RACI»; letters R, A, C, I stay Latin | high | No (corpus writes RACI with Russian head word). Current RU term could become «матрица RACI (матрица распределения ответственности)» | |
| 3.10 | SOW | описание работ | «описание работ (SOW)» at first use, then «SOW» | «описание работ» is neuter; «SOW» indeclinable, used with a head noun: «в SOW», «документ SOW» | low | No (Vocabulary 106 already pairs it with Соглашение о взаимодействии) | |
| 4.11 | backlog | бэклог | «бэклог» | m.; «бэклога», «бэклоги»; AICC names «Бэклог портфеля», «Бэклог программы», «Бэклог Итерации» | high | No (236 occurrences already Cyrillic) | |
| 4.12 | code review | код-ревью; рецензирование кода | «код-ревью» | indeclinable n.; «на код-ревью», «результаты код-ревью» | medium | Minor: Statement of Intent 9.8 wording to align; drop the second variant | |
| 4.13 | cutover | переключение на новую систему | «переключение» | n.; «переключение на Jira и Confluence», «до переключения» | medium | Yes: the corpus says «Переход» in Operating Model 7.1–7.3 and Collaboration tooling; the RU term «переключение на новую систему» is not used anywhere outside the terminology file | |
| 4.14 | deployment | развёртывание | «развёртывание» | n.; «развёртывания»; verb «развернуть» | high | No (70 occurrences) | |
| 4.15 | Epic / issue / sub-task | эпик / задача / подзадача | «эпик» / «задача» / «подзадача» | m. «эпика», «эпики»; exact Jira label kept only when quoting a configured English interface | medium-high | Yes: «Epic» 10 occurrences (PMM 8.3 and diagram) become «эпик», unless the Bank's Jira runs in English, in which case quote it as «тип задачи Epic» | Established: Epic (EN; protected agile term); задача / подзадача for issue / sub-task in Jira |
| 4.16 | Kanban | канбан | «канбан» (method); «Канбан-доска» in AICC names | m.; «по канбану»; compounds «канбан-доска», «канбан-метод»; AICC names «Канбан-доска портфеля», «Канбан-доска программы» | medium | No (42 occurrences already Cyrillic) | |
| 4.17 | lead time / cycle time | время выполнения / время цикла | «время выполнения» / «время цикла» | n.; «времени выполнения»; Latin only in parentheses at first use | medium | Yes: the measure is named «Полное время выполнения» in PMM 327 and SLM 573 (16 occurrences); align to «Время выполнения» or align the terminology to «полное время выполнения» | |
| 4.18 | MVP | минимально жизнеспособный продукт | «MVP» | indeclinable m.; «MVP Решения», «после MVP», «в рамках MVP» | high | No (78 occurrences) | |
| 4.19 | PI / IP | Программный инкремент / Неделя инноваций и планирования | «PI» / «IP»; spelled out «Инкремент программы» | PI and IP indeclinable m.; «Цели PI», «Неделя IP» | high (abbreviations); medium (spelled-out form) | Abbreviations: no. Spelled-out form: yes if adopted, «Программный инкремент» 67 occurrences (an adjective calque, SL glossary) | |
| 4.20 | production | промышленная среда; продакшн | «промышленная среда» | f.; «в промышленной среде»; «промышленная эксплуатация» for the operating state | high | No; drop «продакшн» from the RU term (1 occurrence, in the terminology file) | |
| 4.21 | release | релиз; в корпусе AICC — Выпуск | «релиз» (generic); «Выпуск» (AICC decision) | m.; «релиза», «релизы» | high | No | |
| 4.22 | root cause analysis | анализ первопричин | «анализ первопричин» | m.; «анализа первопричин» | medium-high | No (Statement of Intent 9 already uses it) | |
| 4.23 | service desk | служба поддержки пользователей; сервис-деск | «служба поддержки пользователей» | f.; «в службу поддержки» | medium | No (1 occurrence). Drop «сервис-деск» from the RU term | |
| 4.24 | Service Management | управление услугами | «Service Management» as the system name, with a Russian head noun on first use: «система Service Management»; the practice in prose: «управление услугами» | indeclinable; «в системе Service Management», «заявка в Service Management» | medium | No for the system name (26 occurrences); the entry should separate the system name from the practice | |
| 4.25 | SLA | соглашение об уровне обслуживания | «SLA» | indeclinable n. (agrees with «соглашение»): «SLA заключено», «в SLA» | high | No | |
| 4.26 | sprint / sprint backlog | спринт / бэклог спринта | «спринт» / «бэклог спринта» | m.; «спринта», «спринты» | high | No (only in the terminology file) | |
| 4.27 | story points / velocity | стори-пойнты / скорость команды | «story points» / «скорость команды» | «story points» used as an indeclinable unit after a Russian noun: «оценка в story points»; «скорость команды» f. | medium | No (only in the terminology file) | |
| 4.28 | throughput | пропускная способность | «пропускная способность» | f.; «пропускной способности» | high | No | |
| 4.29 | value stream | поток создания ценности | «поток создания ценности» | m.; «потока создания ценности», «потоки создания ценности» | high | Yes: «value stream» 10 occurrences, «value streams» 1; Vocabulary entry «value stream» and the application note that fixes the Latin form | Established: value stream (EN) |
| 4.30 | WIP | незавершённая работа | «WIP» | indeclinable; «объём WIP», «незавершённая работа (WIP)» at first use | medium-high | No (11 occurrences) | |
| 4.31 | WIP limit | лимит незавершённой работы | «WIP-лимит» | m.; «WIP-лимита», «WIP-лимиты», «в пределах WIP-лимитов» | high | Yes: «WIP limits» 18 and «WIP limit» 12 (English plural inside Russian syntax, e.g. «в пределах WIP limits»); application note «Форма множественного числа: WIP limits» | Established: WIP-лимит / WIP-лимиты (protected: limit → лимит) |
| 4.32 | workflow | рабочий процесс; в корпусе AICC — поясняющий Workflow | «рабочий процесс»; for the AICC document type «Рабочий процесс» (capitalized like other defined terms) | m.; «рабочего процесса», «рабочие процессы»; «Указатель рабочих процессов»; folder path `workflows/` unchanged (rule 2.7) | medium | Yes: «workflow» 36, «workflows» 17, «Workflow» 12, «Workflows» 7, including the page titles «Workflow: …», the section 4 heading «Термины поставки и workflows» and the Vocabulary entry. Workflow is a defined AICC term | Established: Workflow (EN) |
| 4.33 | WSJF | метод приоритизации WSJF | «WSJF» | indeclinable; «метод WSJF», «оценка по WSJF» | high | Yes, small: PMM 6.5 «метод взвешенной приоритизации кратчайших работ (WSJF)» → «метод WSJF» | |
| 5.34 | access control | управление доступом | «управление доступом» | declines normally: «правила управления доступом» | high | no | |
| 5.35 | ACL | Контрольный лист приёмки (corpus); список управления доступом (technical) | «ACL» only inside the identifier `ACL-[nnn]`; in technical text «список управления доступом (ACL)» | identifier is not declined: «Контрольный лист приёмки ACL-012» | high | no | |
| 5.36 | agentic | агентный | «агентный» | «агентное применение», «агентный AI», «агентные сценарии» | medium (regulator writes «агентский») | no; the corpus already writes «Агентное применение» (SoI 11.1, 11.3) | |
| 5.37 | AI | искусственный интеллект | «AI» | not declined; prefix compounds with hyphen («AI-агент», «AI-решение», «AI-ассистент»); postposed after a Russian head («платформа AI», «Инцидент AI», «применение AI») | established | no | Established: AI |
| 5.38 | AI agent / AI agents | ИИ-агент / ИИ-агенты (column); running text «AI agent», «AI agents» | «AI-агент» | pl. «AI-агенты»; declines as «агент»: «AI-агента», «AI-агентам», «реестр AI-агентов»; never «AI agents» inside a Russian sentence | high | yes: about 30 occurrences of «AI agent(s)» outside the terminology (SoI 9, AI Policy 4, Vocabulary 4, Charter 1, plus the terminology rows); the RU-term column «ИИ-агент» also changes to «AI-агент» under the established rule for AI; the English plural row label stays only in the universal-term column | |
| 5.39 | audit trail | журнал аудита (terminology); «аудиторский след» (SoI 11.2) | «журнал аудита» | «журнал аудита Решения», pl. «журналы аудита» | medium-low | yes: SoI 11.2 «аудиторский след» → «журнал аудита» (1), so the corpus uses one form | |
| 5.40 | cloud | облако; облачная среда | «облачная среда» (generic: «облако») | adjective «облачный»: «облачные услуги», «в облачной среде» | high | no | |
| 5.41 | DAG | ориентированный ациклический граф; направленный ациклический граф | «DAG»; on first use «направленный ациклический граф (DAG)» | not declined; with a Russian head («граф DAG», «в DAG») or as a hyphen prefix («DAG-файл»); avoid «DAG'и», «дагов» | high | terminology row only: list «направленный ациклический граф» first (the form Yandex uses; «ориентированный» is the mathematics form); DAG does not occur elsewhere in the corpus | |
| 5.42 | drift | дрейф данных, модели или её поведения | «дрейф» with a qualifier: «дрейф данных», «дрейф модели» | declines normally: «мониторинг дрейфа» | high | no | |
| 5.43 | evaluation set | набор данных для оценки (terminology); defined term «Оценочный набор» (Vocabulary) | «тестовый набор данных» | pl. «тестовые наборы данных»; short «тестовый набор» after first use | medium | yes: the defined term «Оценочный набор» (5, plus one lower-case «оценочная карта» that is unrelated) and the terminology RU term; the alternative is to keep «Оценочный набор» and make the terminology row say so, so that the two references agree | |
| 5.44 | fallback | резервный механизм; резервный сценарий (terminology); «резервный вариант» (AI Policy, Solution Definition template) | «резервный вариант» | qualifiers as needed: «резервная модель», «резервный поставщик»; pl. «резервные варианты» | medium | terminology row only: put «резервный вариант» first, the form the corpus already uses (3) | |
| 5.45 | Finite State Machine / FSM | конечный автомат | «конечный автомат»; on first use «конечный автомат (FSM)» | declines normally: «состояния конечного автомата»; avoid «модель FSM» as the main form | medium | terminology row only: status fixed → the Russian term is the form, FSM the abbreviation; the term occurs nowhere else in `charter/ru/` | |
| 5.46 | human oversight | контроль со стороны человека | «контроль со стороны человека» | declines on «контроль» | high | no | |
| 5.47 | ICT | информационно-коммуникационные технологии | «информационно-коммуникационные технологии»; abbreviation «ИКТ» if needed | «инциденты ИКТ», «риски ИКТ»; Latin «ICT» only in quoted external titles | medium-low (Latin «ICT» was considered for symmetry with «IT») | terminology row only: status fixed «ICT» does not match the corpus, which never writes ICT in Russian text | Established: ICT (EN) |
| 5.48 | IT | информационные технологии | «IT» | «IT-функция», «IT-услуги», «подразделение IT» (as now: «IT-функция» 37, «IT-услуг» 2) | established | no | Established: IT |
| 5.49 | knowledge base | база знаний | «база знаний» | pl. «базы знаний» | high | no | |
| 5.50 | knowledge layer | слой работы со знаниями | «слой работы со знаниями» | declines on «слой» | low | no | |
| 5.51 | language model | языковая модель | «языковая модель»; «большая языковая модель (LLM)», then «LLM» | «LLM» not declined; with a Russian head («модель LLM») or hyphen prefix («LLM-решение») | high | no | |
| 5.52 | lineage | происхождение данных и история их преобразований | «происхождение данных»; for the capability «прослеживаемость происхождения данных» | declines on «происхождение» | medium | no; SoI 11.2 already writes «прослеживаемость происхождения данных» | |
| 5.53 | logging | логирование; журналирование событий (terminology); «журналирование» in text (15) | «регистрация событий»; the records are «журналы событий» | «регистрация событий и мониторинг»; «журналы событий сохраняются» | medium | yes: «журналирование» (15, AI Policy, Acceptance Checklist, Unit Governance Guide, Vocabulary «Лабораторная среда») → «регистрация событий»; terminology RU term changes | |
| 5.54 | model gateway | шлюз доступа к моделям | «шлюз доступа к моделям» | declines on «шлюз»; short «шлюз моделей» acceptable after first use | medium-low | no. «AI-шлюз» would fit the established rule for AI but loses the model/tool distinction the corpus needs | |
| 5.55 | monitoring | мониторинг | «мониторинг» | declines normally | high | no | |
| 5.56 | observability | наблюдаемость | «наблюдаемость» | declines normally | high | no | |
| 5.57 | open model | открытая модель | «открытая модель»; where only weights are published, «модель с открытыми весами» | declines normally | medium | no | |
| 5.58 | pipeline | конвейер обработки (terminology); «Конвейеры обработки данных» (Business Model 4.5, 1) | «пайплайн» («пайплайн обработки данных») | Cyrillic borrowing, declines like «бэклог»: pl. «пайплайны», «в пайплайне»; hyphen compounds «ML-пайплайн» | medium-low (the established «бизнес-кейс» form points to the practitioner borrowing; «конвейер» is the safe literary alternative) | yes if adopted: Business Model 4.5 (1) and the terminology RU term | Established: pipeline (EN) |
| 5.59 | Platform guardrails | Защитные механизмы платформы | «Защитные механизмы платформы» | declines on «механизмы» | medium | no | Established: рамки (guardrails → рамки); Platform guardrails → рамки платформы |
| 5.60 | prompt injection | промпт-инъекция; внедрение инструкций (terminology); AI Policy 3.3 «внедрения вредоносных инструкций в запрос к модели» | «промпт-инъекция» | pl. «промпт-инъекции»; «прямая / непрямая промпт-инъекция»; on first use «промпт-инъекция (внедрение вредоносных инструкций в запрос к модели)» | medium | optional: AI Policy 3.3 (1) may add the short form; terminology RU term drops «внедрение инструкций» as a second name | |
| 5.61 | read-only | доступ только для чтения | «доступ только для чтения» | «права только на чтение» | high | no | |
| 5.62 | repository / protected main branch | репозиторий / защищённая основная ветвь | «репозиторий» / «защищённая основная ветка» | «в репозитории»; branch names such as `main` stay as code | medium (both «ветвь» and «ветка» are correct; «ветка» is practice) | terminology row only; the corpus has no other occurrence | |
| 5.63 | retrieval | поиск и извлечение данных | «поиск и извлечение информации»; RAG as «генерация с дополненным поиском (RAG)», then «RAG» | «RAG» not declined: «архитектура RAG», «сценарий RAG» (T11) | medium | terminology row only («данных» → «информации», since the material is documents) | |
| 5.64 | tool gateway | шлюз доступа к инструментам | «шлюз доступа к инструментам» | declines on «шлюз» | low | no | |
| 6.65 | AICC | Центр компетенций по AI (AICC) | «AICC»; expansion «Центр компетенций по AI» | not declined: «в AICC», «Руководитель AICC» | high | no | Established: keep |
| 6.66 | Amazon CloudWatch / CloudWatch | Amazon CloudWatch / CloudWatch | «Amazon CloudWatch», then «CloudWatch» | not declined; Russian head word as needed: «метрики в CloudWatch» | high | no | Established: keep |
| 6.67 | Amazon Web Services / AWS | Amazon Web Services / AWS | «Amazon Web Services (AWS)», then «AWS» | not declined | high | no | Established: keep |
| 6.68 | Atlassian | Atlassian | «Atlassian» | not declined: «продукты Atlassian» | high | no | Established: keep |
| 6.69 | Confluence | Confluence | «Confluence» | not declined: «в Confluence» | high | no | Established: keep |
| 6.70 | Jira | Jira | «Jira» | not declined: «в Jira», «из Jira» | high | no | Established: keep |
| 6.71 | O!Bank | O!Bank | «O!Bank» | not declined | high | no | Established: keep |

## B. Terms the corpus uses that the shared terminology lacks

| # | Universal term | Current RU | Proposed form in the RU corpus | Pattern | Conf. | Corpus change | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B4.1 | Program Increment (spelled out) | Программный инкремент | «Инкремент программы» | m.; «Инкремента программы» | medium | Yes, 67 occurrences, if adopted; otherwise prefer «PI» in running text | Established: Program Increment (PI) (EN, protected); increment in general → инкремент |
| B4.2 | PI Planning | Планирование PI | «PI-планирование» | n.; «PI-планирования», «на PI-планировании» | medium | Optional: «Планирование PI» (28) is grammatical; change only for alignment with practice | |
| B4.3 | PI Objective | Цель PI | «Цель PI» | f.; «Цели PI» | medium | No (35 occurrences; the current form is fine) | |
| B4.4 | Iteration (vs sprint) | Итерация | «Итерация» | f. | high | No | Established: Iteration (EN, protected) |
| B4.5 | Capability | Функциональная возможность | «Функциональная возможность» (keep) or «Эпик»; to be established | f. | low | Yes if renamed (127 occurrences) | Established: Capability / Capabilities (EN) for a Solution, Product or Service; general sense → by context (компетенция, способность), see [EN–RU translation map](../../../charter/ru/translation-en-ru-map.md), section 3, row capability |
| B4.6 | Feature | Функциональность | «Функциональность» (keep; «фича» is too informal for a regulation) | f.; «Функциональности» | medium | No | Established: Feature (EN, protected agile term); functionality in general → функциональность |
| B4.7 | Inspect and Adapt | Анализ и адаптация | «Инспекция и адаптация» | f.; «на Инспекции и адаптации» | medium-high | Yes, 24 occurrences; also removes the clash with the Stage «Анализ» (SL glossary) | Established: Inspect and Adapt (EN, protected); inspect in general → анализ; adapt → адаптировать |
| B4.8 | Daily Stand-up | Ежедневная короткая встреча | «Ежедневная планёрка» | f. | low | Yes, about 15 occurrences; alternative «Ежедневный стендап» if a borrowing is preferred | Established: планёрка |
| B4.9 | Retrospective | Ретроспектива | «Ретроспектива» | f. | high | No | |
| B4.10 | Product Owner | Владелец продукта | «Владелец продукта» | m. | high | No (76 occurrences) | |
| B4.11 | Portfolio Kanban / Program Kanban | Канбан-доска портфеля / программы | «Канбан-доска портфеля» / «Канбан-доска программы» | f. | high | No | |
| B4.12 | swimlane | Дорожка | «Дорожка» | f. | high | No | |
| B4.13 | Definition of Ready / Done | Критерии готовности к работе / завершённости | keep the Russian names; add «(DoR)» / «(DoD)» at first use | — | medium | Small: first-use abbreviations only | |
| B4.14 | acceptance criteria | Критерии приёмки | «Критерии приёмки» | pl. | high | No | |
| B4.15 | change request | Заявка на изменение | «Запрос на изменение» | m. | medium-high | Yes, 3 occurrences | Established: change request (CR) (EN, protected) |
| B3.16 | stakeholder | Заинтересованное лицо / заинтересованные лица | «Заинтересованная сторона» | f.; «Заинтересованные стороны» | medium | Yes, 18 occurrences, if the GOST form is established; «Заинтересованное лицо» is defensible from the Scrum Guide | Established: стейкхолдер / стейкхолдеры |
| B3.17 | benefit | выгода / эффект | «эффект» (плановый / подтверждённый) | m. | medium | Yes, about 17 «выгод-» occurrences (BP glossary) | Established: выгода (in most uses) |
| B3.18 | Investment Guardrails | Инвестиционные ограничения | «Инвестиционные пороги» (BP glossary) | pl. | low | Yes, 66 occurrences, if renamed; to be established | Established: Инвестиционные рамки |
| B3.19 | roadmap | Дорожная карта | «Дорожная карта» | f. | medium | No (42 occurrences) | |
| B3.20 | leading indicator | Опережающий индикатор | «Опережающий индикатор» | m. | medium | No | |
| B3.21 | Agile / Scrum / SAFe | — (Scrum appears only in the terminology file's sprint note) | «Agile», «Scrum», «SAFe» | indeclinable; compounds «Agile-команда», «Scrum-команда» | high | No; add an entry only if the corpus starts using these words in running text | |
| B4 or 5 (ITSM).22 | incident | инцидент (very frequent, plus defined «Инцидент AI») | «инцидент» | declines normally | high | no; add a row because «Инцидент AI» depends on it | |
| B4 or 5 (ITSM).23 | problem / known error | проблема / известная ошибка (3) | «проблема» / «известная ошибка» | pl. «известные ошибки» | high | no | |
| B4 or 5 (ITSM).24 | change request | заявка на изменение (13) | «запрос на изменение»; the Jira record may be called «заявка» when the ticket itself is meant | pl. «запросы на изменение»; «ключ запроса на изменение» | medium | yes: 13 occurrences (guides, templates README, Solution Lifecycle Model) | Established: change request (CR) (EN, protected) |
| B4 or 5 (ITSM).25 | change management / change enablement | управление изменениями / обеспечение изменений (2) | «управление изменениями»; ITIL 4 practice name «обеспечение изменений» | declines normally | high | no | |
| B4 or 5 (ITSM).26 | rollback | откат (5) | «откат» | verb «откатить», «откатывается» | high | no; worth a row because the fallback row contrasts with rollback | |
| B4 or 5 (ITSM).27 | emergency change | Экстренное изменение (defined, 9) | «экстренное изменение» | declines normally | medium | no | |
| B4 or 5 (ITSM).28 | severity | Степень серьёзности (defined, 11) | «степень серьёзности» | declines on «степень» | medium (the two earlier reviews disagree; «серьёзность» has the fetched source) | no | |
| B5.29 | backup and recovery | резервное копирование и восстановление (2) | «резервное копирование и восстановление» | declines normally | high | no | |
| B5.30 | availability | доступность | «доступность» | declines normally | high | no | |
| B5.31 | information security | информационная безопасность (18) | «информационная безопасность»; «ИБ» only in tables if needed | declines normally | high | no | |
| B5.32 | personal data | персональные данные (13) | «персональные данные» | «субъект персональных данных» | high | no | |
| B5.33 | data classification / data class | классификация данных / Класс данных (defined, 46) | «классификация данных»; defined «Класс данных» | declines normally | medium | no | |
| B5.34 | model risk | модельный риск (13) | «модельный риск» | «функция управления модельным риском» | high | no | |
| B5.35 | validation | Валидация (defined, about 150) | «валидация» | declines normally | high | no | |
| B5.36 | bias | предвзятость (3) | «предвзятость» | «проверки на предвзятость» | high | no | |
| B5.37 | explainability | объяснимость (1) | «объяснимость» | declines normally | high | no | |
| B5.38 | AI output | Результат AI (defined, 13) | «Результат AI» | postposed AI, declines on «результат» | medium | no | |
| B5.39 | AI Platform | Платформа AI (defined, 33) | «Платформа AI» | postposed AI: «на Платформе AI» | high | no | |
| B5.40 | AI Incident | Инцидент AI (defined, 16+) | «Инцидент AI» | postposed AI; pl. «Инциденты AI» | medium (prefix «AI-инцидент» is equally attested) | no | |
| B5.41 | AI Registry | Реестр AI (defined, 29) | «Реестр AI» | postposed AI | high | no | |
| B5.42 | assistant | Ассистент (defined) / ассистент (5) | «ассистент»; compound «AI-ассистент» | pl. «ассистенты» | high | no | |
| B5.43 | LLM | (inside the language-model row only) | «большая языковая модель (LLM)», then «LLM» | «модель LLM», «LLM-решение» | high | no; optional separate row | |
| B5.44 | RAG | (inside the knowledge-layer row only) | «RAG»; on first use «генерация с дополненным поиском (RAG)» | not declined: «архитектура RAG» | high | no | |
| B5.45 | open-source component | открытый компонент (2, AI Policy section 3 table and 4.4) | «компонент с открытым исходным кодом» | pl. «компоненты с открытым исходным кодом» | medium | yes: AI Policy (2) | Established: open-source компонент |
| B5.46 | grounding | опора на источники (1, service-delivery workflow) | «опора на источники» | declines on «опора» | low | no | |
| B5.47 | traces / tracing | трассировки (3) | «трассировки» (data), «трассировка» (activity) | declines normally | medium | no | |
| B5.48 | alerts | оповещения (3) | «оповещения» | declines normally | high | no | |
| B5.49 | dataset | набор данных (2) | «набор данных» | pl. «наборы данных» | high | no | |
| B6.50 | Apache Airflow / Airflow | Airflow (inside the DAG row) | «Apache Airflow», then «Airflow» | not declined | high | terminology only: the DAG row names a product that section 6 does not list (section 6 says products are verified against vendor documentation) | Established: keep |

