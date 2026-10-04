# Russian register review of the charter, 4 October 2026

The question: the Russian edition of the charter reads clumsy next to how Russian-language financial institutions write. Is the terminology wrong, and do the sentences sound like modern Russian? Five reviewers each researched the authorities of one subject and read the matching documents against the English source. The method and rules are in [BRIEF.md](BRIEF.md). Nothing in the corpus was changed.

| Subject | Documents | Report | Findings |
| --- | --- | --- | --- |
| Mandate | Statement of Intent, AICC Charter, Executive Summary, Document Catalog | [mandate.md](mandate.md) | 87 |
| Business and portfolio | Business Model, Portfolio Management Model | [business-and-portfolio.md](business-and-portfolio.md) | 80 |
| Governance | Operating Model | [operating-model.md](operating-model.md) | 92 |
| Delivery | Solution Lifecycle Model | [solution-lifecycle.md](solution-lifecycle.md) | 79 |
| AI and terms | AI Policy, Vocabulary | [ai-policy-and-vocabulary.md](ai-policy-and-vocabulary.md) | ~90 + every defined term |

The main authorities used: the NBKR internal control and audit rules and the Mbank corporate governance code drafted under the 2024 NBKR requirements; the Bank of Russia's Corporate Governance Code, Указание 3624-У, the AI ethics code for the financial market and its AI reports; ГОСТ Р ИСО/МЭК 20000-1-2021, ГОСТ Р 71476 (ISO/IEC 22989), ГОСТ Р ИСО/МЭК 42001, ГОСТ Р 54870/54871, ГОСТ Р ИСО 21504; the official Russian Scrum Guide; public documents of Bakai Bank, Otbasy bank, МТС-Банк, Sber, and bank engineering blogs. Each report lists its URLs; quotations marked "not fetched" rest on well-known usage and should be checked before external use.

## 1. Verdict

The meaning carries over faithfully, and most terminology is defensible. Куратор AICC, Паспорт инициативы, Заявление о риск-аппетите, Валидация, Сигнальное значение, Недостаток контроля, Заключение контрольной функции, Введение в действие, and Реестр AI are all confirmed by Russian-language sources. The clumsiness comes from **English structure carried into Russian**, not mainly from wrong words. Six patterns account for most of it. They are measured below over the nine documents (39,800 words).

| Pattern | Count | Per 1,000 words | What a Russian regulation does instead |
| --- | --- | --- | --- |
| Defined terms capitalized mid-sentence (Решения, Домена, Итерации, Функциональности, Категории, Записи…) | 4,456 | 112 | Lowercase common nouns; capitals only for bodies, the Bank, and titles |
| «должен» for every *shall*, and for *should* | 236 corpus-wide | 4.4 | Present tense for norms (утверждает, обеспечивает), «обязан» where emphasis is needed, «не вправе» / «не допускается» for prohibitions |
| «Запись о …» for living records | 171 | 4.3 | реестр, журнал, перечень, протокол |
| «который…» relative clauses | 160 | 4.0 | Participles, shorter sentences |
| «возможность / функциональная возможность» for *capability* | 105 | 2.6 | инструмент, компетенция, функции; a separate word for the defined term |
| Latin words other than the fixed AI and IT (business case 54, WIP 32, AI agent 25, value stream, Workflow, Epic, KPI) | 323 | 8.1 | бизнес-кейс, лимит незавершённой работы, AI-агент, поток создания ценности |

Smaller recurring patterns:

- An event or a document as the actor («Ретроспектива совершенствует…»).
- Chains of verbal nouns («поставка», «осуществление»).
- «является» used as a link verb (100 times).
- Calqued table headers («Что возвращает», «Ряд», «Ритм»).
- ISO dates in running text.
- The same thing named differently in two documents: «выгода» and «эффект» for benefit; «функция-заказчик» and «функция заказчика» for client function.

## 2. Errors of meaning, to fix regardless of style

These are not matters of taste. The Russian says something different from the English, or can be read so.

| Where | Current | Problem | Fix |
| --- | --- | --- | --- |
| Statement of Intent 1.1 | «AI («AI»)» | The definition of the abbreviation is lost | «искусственный интеллект (далее — AI)» |
| Executive Summary 4 | «Приёмку Командой» | Means acceptance *of* the Team | «приёмку от имени Команды» |
| Executive Summary 7 | «Корпус Положения» | Says the Charter's corpus, not the whole corpus | «корпус документов» |
| Document Catalog 5.2 | — | The limit "no more than about 80 clauses" is dropped | Restore it |
| Business Model 2.4 | «протокол» | In bank Russian «протокол» means meeting minutes | «порядок работы» |
| PMM 4.2 | «отклонения» | "Findings" became "deviations" | «выводы» or «замечания» |
| PMM 4.6 | «направленные на риск» | Reads as "aimed at creating risk" | «связанные со снижением риска» |
| PMM 5.5 | — | Can be read as "work on defining the Business Model" | Reorder the sentence |
| PMM 7.3 | «Решение о Выпуске Решения» | Solution and decision collide in one phrase | «решение о выпуске AI-решения» or a reworded sentence |
| SLM 8.11 and others | «должен» for *should* | Raises a recommendation to an obligation | «целесообразно», «следует» |
| SLM | «Элемент блокирует Зависимость» | Reads backwards | «элемент заблокирован зависимостью» |
| SLM 8.12 | business case … «одобренное» | Gender agreement; elsewhere the term is masculine | «одобренный» |
| Operating Model | «инициировать событие» | Means *causing* the event; the English is *raising* it | «сообщить о событии», «вынести на рассмотрение» |
| Operating Model | «несекретная информация» | Wrong category; "secret" is a state-secrets term | «информация, не относящаяся к информации ограниченного доступа» |
| Operating Model | «заместитель» | In Russian a deputy is a post; the English means whoever covers an absence | «лицо, его замещающее» (716-П wording) |
| Operating Model | «действия» in a Steering record | Records of meetings carry instructions | «поручения» |
| Operating Model, Charter 3.2 | «исполнительное руководство», «руководство» | The executive body of a Kyrgyz bank is the Правление | «Правление Банка» (to confirm against O!Bank's charter) |
| AI Policy 2.7, 3.2, 4.1, 6.1 | — | Unclear antecedent or word order that changes the parse | Rewrites in the report |
| AI Incident definition | — | Narrower than AI Policy 5.1 | «повлекло или могло повлечь причинение вреда…; утрата контроля» |

## 3. Proposed style rules for the Russian edition

These eight rules remove most of the clumsiness without touching any term. Rules 1 and 2 change rules of the corpus (Vocabulary 3.1, Document Catalog 7.1 question 3), so they need your decision.

1. **Obligations.** State a norm in the present tense: «Куратор AICC утверждает…», «AICC не владеет… и не эксплуатирует…». Use «обязан» only where the duty must stand out. Prohibitions take «не вправе» or «не допускается». Commitments take «обязуется». *Should* takes «следует» or «целесообразно», never «должен».
2. **Capitalization.** Capitalize the Bank, its bodies (Совет директоров, Комитет Совета директоров, Правление, Управляющий комитет по AI), AICC and its named Roles (Куратор AICC, Руководитель AICC), and document titles in «». Write every other defined term in lowercase: решение, домен, владелец домена, инициатива, итерация, функциональность, категория риска, валидация, выпуск. The glossary keeps them defined; capitals do not. This depends on decision D2 below, because capitals are today the only thing that separates Решение (Solution) from решение (decision).
3. **Actors.** A person or a body acts, not an event or a document. «На ретроспективе команда определяет…», not «Ретроспектива совершенствует…».
4. **Verbs over nouns.** «Банк внедряет», not «осуществляет внедрение». Drop «является» where a dash or a plain verb works.
5. **Deliver.** «передать», «внедрить», «создать», and «результат» for the outcome. Keep «поставка» only as the name of a phase.
6. **Tables.** Headers are nouns: «Периодичность», «Результат», «Участники», «Строка», not «Ритм», «Что возвращает», «Ряд».
7. **Dates and references.** Write «2 октября 2026 г.» in running text; ISO dates stay in metadata and tables. For a cross-reference, write «(п. 5.2 Операционной модели)».
8. **Drafting formulas.** Use the stock phrases of Russian internal regulations: «если иное не предусмотрено…», «отнесённые к компетенции…», «утверждает», «вводится в действие», «утратил силу». The full phrase bank is in each report, section 6.

## 4. Decisions for you

Each of these changes a defined term in every document and on the portal. The reviewers' evidence is in the reports; where they disagreed, the recommendation below says which way I lean and why.

| # | Decision | Options | Lean |
| --- | --- | --- | --- |
| D1 | Obligation style and capitalization (rules 1 and 2) | Keep «должен» and capitals / adopt the Russian norm | Adopt. It is the largest single gain in naturalness. |
| D2 | Solution (Решение, 125 uses) next to decision (решение, 103 uses) | Keep with a style rule / «AI-решение» / «система AI» | «AI-решение». It keeps the fixed Latin AI, matches «ИИ-решения» in bank texts, and frees «решение» for decisions so that «Управленческое решение» can become plain «решение». |
| D3 | Latin terms in Russian sentences (business case, WIP limit, AI agent, value stream, Workflow) | Keep / Russian forms | **business case** → «бизнес-кейс». **WIP limit** → «лимит незавершённой работы (WIP)». **AI agent** → «AI-агент». **value stream** → «поток создания ценности». **Workflow** → «процесс» or «описание процесса». The AI and IT rule stays. Service Management, Jira and Confluence stay as product names. This partly reverses the recent international-terminology change, so it is yours to call. |
| D4 | Registry and the records in it | Keep «Реестр» + «Запись о …» / rename | Rename the folder «Хранилище записей» (or «Регистр») and give each living record its natural Russian name: «Реестр рисков и проблем», «Реестр назначений», «Реестр стандартов», «Перечень приоритетов», «Состав команд», «Протокол Управляющего совещания» for the Steering Summary. |
| D5 | Risk Tier | Keep «Категория риска» / «Уровень риска» | «Уровень риска». It is the Bank of Russia AI code's own term. The clash with Уровень зрелости and Уровень поддержки is tolerable because a different noun always follows. |
| D6 | Verify Stage (Проверка, which collides with Check) | «Тестирование» / «Верификация» | «Верификация». The Stage covers test, check, and validation, which «Тестирование» is too narrow for. |
| D7 | Engagement (Взаимодействие с заказчиком) | Keep / «Клиентская инициатива» / «Клиентский проект» | «Клиентская инициатива». It follows the definition ("an Initiative with a client function") and avoids «проект», which the Vocabulary excludes. |
| D8 | Capability and Feature (Функциональная возможность / Функциональность: near-homonyms) | Keep / «Эпик» and «Функциональность» | «Эпик». Bank teams say «эпик» and «фича», and the Jira mapping already equates Capability with Epic. |

Agreed by the reviewers. These are recommended without further evidence needed, and each changes every occurrence:

| EN | Current | Proposed |
| --- | --- | --- |
| assurance (internal audit) | оценка с предоставлением уверенности | независимая оценка (эффективности системы управления рисками и внутреннего контроля) |
| Three lines | Три линии | три линии защиты (NBKR corporate governance Code, п. 117) |
| Finding | Выявленное отклонение | Замечание |
| Steering Summary | Итоги Управляющего совещания | Протокол Управляющего совещания |
| Investment Guardrails | Инвестиционные ограничения | Инвестиционные лимиты |
| deprecated (status) | выведен из действия | утратил силу |
| revision (of a document) | версия | редакция |
| Stakeholder | Заинтересованное лицо | заинтересованная сторона |
| benefit claimed / confirmed | выгода / эффект (mixed) | плановый эффект / подтверждённый эффект |
| control status Operating | Выполняется | Функционирует |
| control test | способ проверки | тестирование |
| Inspect and Adapt | Анализ и адаптация | Инспекция и адаптация (Scrum Guide RU) |
| Daily Stand-up | Ежедневная короткая встреча | ежедневная планёрка |
| Pivoted (state) | Перенаправлено | Преобразовано |
| PDCA | Планирование — Выполнение — Проверка — Корректировка | Планируй — Делай — Проверяй — Действуй |
| change ticket | Заявка на изменение | Запрос на изменение (ГОСТ Р ИСО/МЭК 20000-1) |
| Evaluation set | Оценочный набор | тестовый набор данных |
| oversee (AICC over Solutions) | осуществлять надзор | контролировать («надзор» is the regulator's word) |
| function (organizational unit, in running text) | функция | подразделение (the defined «Контрольная функция» stays) |

## 5. What it sounds like

Three clauses of the AICC Charter, rewritten under rules 1–8 and decisions D1–D2. These are illustrations, not a final text.

**2.1**

- *Now:* «Миссия AICC — сделать AI надёжной повседневной возможностью Банка: подтверждать его ценность совместно с функциями, обслуживающими клиентов Банка, формировать практику его внедрения в пределах установленных Банком стандартов и сохранять ответственность людей за каждое его применение.»
- *Natural:* «Миссия AICC — сделать AI надёжным повседневным инструментом Банка: вместе с подразделениями, которые обслуживают клиентов, доказывать его пользу на деле, выстраивать порядок его внедрения в рамках стандартов Банка и сохранять за людьми ответственность за каждый случай его применения.»

**3.2**

- *Now:* «AICC не должен быть владельцем Платформы AI или эксплуатировать её, нести ответственность за бизнес-результаты Домена, устанавливать правила Контрольной функции, проводить Валидацию собственной работы или принимать решения по вопросам, отнесённым нормативными документами Банка к компетенции Совета директоров, руководства или Контрольной функции.»
- *Natural:* «AICC не владеет платформой AI и не эксплуатирует её, не отвечает за бизнес-результаты домена, не устанавливает правила контрольных функций, не проводит валидацию собственной работы и не принимает решений по вопросам, отнесённым внутренними нормативными документами Банка к компетенции Совета директоров, Правления или контрольных функций.»

**6.2**

- *Now:* «Заказчиками AICC являются функции Банка. Функция направляет запрос в AICC для изучения потребности, определения решения и предложения подходящего решения на основе AI.»
- *Natural:* «Заказчики AICC — подразделения Банка. Подразделение обращается в AICC, чтобы изучить потребность, определить подход к её решению и получить предложение по подходящему AI-решению.»

## 6. On AI and ИИ

You decided that AI and IT stay in Latin script, and none of the reviewers treats it as an error. For the record, every regulator and bank source read writes «ИИ» in running text: the Bank of Russia, the ГОСТ Р standards, the AI ethics code, Sber, and the Kyrgyz banks. Latin «AI» appeared once, in the Association of Russian Banks' Положение. Keeping AI is consistent and readable. It is simply the one place where the corpus will always look different from the sources it is measured against.

## 7. How to proceed

1. Fix the errors of meaning in section 2 now. They need no decision.
2. Decide D1–D8.
3. Pilot one document under the decisions. The AICC Charter has 1,051 words, so you can hear the result before the corpus changes.
4. Then rewrite the rest document by document, with the Vocabulary first so that every defined term changes once, and record it as a Russian-edition revision with a change-log row and a Decision Log entry.
