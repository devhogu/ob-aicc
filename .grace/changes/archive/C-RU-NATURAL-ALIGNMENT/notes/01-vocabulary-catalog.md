# Notes: batch 01 — Vocabulary, Document Catalog, Statement of Intent, Executive Summary, charter README

## charter/ru/documents/vocabulary.md

- DRIFT — Ежегодное управляющее совещание: EN "the findings of the year to that date"; old RU added «включая выявленные отклонения» (narrowed to the AICC term Finding). Wrote «выводы, сделанные за год на эту дату» (map row findings).
- DRIFT — Валидация: old RU defined it as «Проверка Представителями контрольных функций…», using the AICC term Check inside the Validation definition. Wrote «Рассмотрение представителями контрольных функций того, соответствует ли решение…».
- DRIFT — Перенаправлено, толкование: old «Связь с итоговым элементом сохраняет…» (map-rejected «связь сохраняет»). Rewritten; meaning unchanged.
- DRIFT — Приостановление и остановка: old «прекращает работу Решения»; EN suspends/ends the Solution (its use). Wrote «прекращает применение решения» (map row suspend).
- QUESTION — 3.3: added to the capital-letter list the Latin work-item names (Initiative, Capability, Feature, Story, Task, Spike, Bug, Epic) and a sentence that bare «проверка» means the term Check, per STYLE §3. Alternative: leave 3.3 as it was. Chosen because the Vocabulary is the rule source the other files cite.
- QUESTION — term names: per assignment, Work Item = «Рабочий элемент» (was «Рабочая задача»), Business case = «Бизнес-кейс» (concept and stage), Iteration = «Итерация», PI = «Программный инкремент (PI)», Value stream = «Поток создания ценности», Workflow = «Рабочий процесс», Hat = «Дополнительная обязанность», Three lines = «Модель трёх линий». The shared terminology reference (task/ticket entries) and portal/tools/build.py (line ~1704 «Рабочих задач») still say «Рабочая задача».
- QUESTION — events: used the accepted forms of the shared terminology reference: «ежедневная планёрка», «ревью и демонстрация итерации», «ретроспектива итерации», «PI-планирование», «Inspect and Adapt», «обзор и демонстрация PI». Old: «Ежедневная короткая встреча», «Обзор и демонстрация Итерации», «Анализ и адаптация», «Планирование PI». Other files must match.
- QUESTION — Соглашение об обмене данными: EN "data or decisions" kept as «данные или решения», following the finished Charter sample (3.3), although bare «решение» is the Solution term. Alternative: «данные или результаты принятия решений».
- QUESTION — Принято: EN "accepts an Initiative outcome under 5.1" names no document; rendered «в соответствии с пунктом 5.1 той же модели» (the Solution Lifecycle Model 5.1 transition table, which holds the Initiative acceptance rule).
- QUESTION — assurance loop kept as «цикл подтверждения надлежащего функционирования» (as in the Operating Model); internal audit's assurance is «независимая оценка».
- QUESTION — test `test_business_case_search_distinguishes_the_concept_from_the_stage` (portal/tests/test_localization.py) expects the Russian vocabulary labels to start with "business case"; with the required «Бизнес-кейс» labels it now fails. The test needs `'бизнес-кейс'` for ru (not edited: outside my files).
- QUESTION — portal/tools/build.py `load_terms` matches Russian vocabulary labels case-sensitively; with lowercase terms in prose («роль», «итерация») term linking will match only sentence-initial occurrences. Build-side change needed (T-002 scope).

## charter/ru/documents/document-catalog.md

- DRIFT — 5.1, AICC-ORG-02 purpose: old RU added «перенаправлении» (pivot), not in EN (take in, fund, continue, defer, reject). Removed.
- DRIFT — 5.1, AICC-ORG-03 purpose: old RU added «и Приёмка» to "verification and release". Removed.
- DRIFT — 7.1 question 3: EN "with 'shall' for each obligation"; old RU required «должен/должна/должны», which contradicts Russian Vocabulary 3.1. Wrote «выражена ли каждая обязанность так, как установлено пунктом 3.1 документа «Терминология и стиль»».
- DRIFT — 5.4: old RU «должен вести … должен удалять» for "shall keep … shall remove"; now «обязан вести … и удалять». Old «больше не полезна читателю» → «больше не нужна пользователям» (map readers).
- QUESTION — 5.3: EN "They state no rule of their own" after a sentence about Templates; rendered as workflows, guides and templates. Alternative: workflows and guides only.
- QUESTION — 6.1 row 6: "an approval of output" rendered «одобрение результата AI» (control C-21, AI output published to investors/Board). Old: «одобрения выходного результата».
- QUESTION — 6.1 row 1: "lean business case" → «бережливый бизнес-кейс» (shared terminology reference, entry lean). Old: «краткий business case».
- QUESTION — 5.1 AICC-REF-01 purpose kept as «Определения, толкование и стиль документов» because test_reader_can_find_a_late_glossary_term asserts that exact lead text.
- ENGLISH? — 5.3 "They" is ambiguous (workflows and guides, or also Templates).

## charter/ru/documents/statement-of-intent.md

- DRIFT — 1.1: old «в отношении внедрения AI («AI»)» lost "artificial intelligence"; wrote «искусственного интеллекта (далее — AI)», likewise «(далее — AICC)» in 1.2.
- DRIFT — 2.1: "a governed capability" was «управляемую функциональную возможность» (feature sense); wrote «управляемый инструмент» (map capability).
- DRIFT — 6.6: "contest a decision" was «оспорить решение»; wrote «потребовать пересмотра решения»; "Humans … are able to stop" → «Работники … вправе остановить».
- DRIFT — 6.7: "limited in time" was «ограничивается сроком»; wrote «предоставляется на ограниченный срок».
- DRIFT — 7.3: "No person validates their own work" was «Никто не проводит Валидацию…»; wrote «Валидация собственной работы не допускается».
- DRIFT — 11.3.1: "read as a trend and has no target" was «оценивается как тенденция»; wrote «отслеживается динамика, целевое значение не устанавливается».
- DRIFT — 13.5: «вступает в силу … делает его обязательным» → «вводится в действие … обязательно для исполнения в Банке» (map entry into force).
- QUESTION — section 10 heading "Capability and enablers" → «Ресурсы и условия внедрения» (map row question-style headings); 11.2 heading "AI Platform capability by level" → «Функциональность платформы AI по уровням» (map rejects «возможности Платформы»). Alternative: «Компетенции и обеспечивающие условия».
- QUESTION — 6.3: EN "Individuals are informed" → «Клиентов и работников информируют о применении AI» (map row inform). Alternative: «Лиц, взаимодействующих с AI, информируют об этом».
- QUESTION — 2.2, 10.x, 12.x: "shall" rendered by «обязуется» (2.2) and present tense (10.x, 12.x) per Vocabulary 3.1 and the map; the build parsers for 4.2, 5.x, 9.x formats are respected.
- ENGLISH? — 12.2 says AICC reports to the Board Committee each quarter; the AICC Charter 7.2 and the Executive Summary say the Executive Sponsor issues the report to the Board Committee. Translated as written.

## charter/ru/executive-summary.md

- DRIFT — §3: "on a best-effort basis" was «прилагая максимально возможные усилия» (stronger duty); wrote «с приложением усилий в разумных пределах».
- DRIFT — §5: "no one overrides them" was «никто не отменяет действие их решений»; wrote «их управленческие решения отмене не подлежат».
- QUESTION — "charter" (the corpus) rendered «корпус документов AICC» instead of «корпус Положения», since «Положение об AICC» is a separate document (AICC-MND-02). About 30 occurrences of «корпус Положения» remain in other workers' files (guides, workflows, templates, solution-lifecycle-model).

## charter/ru/README.md

- QUESTION — title «Корпус Положения Центра компетенций по AI» → «Корпус документов Центра компетенций по AI»; same reasoning as above (the portal strips this H1).
- QUESTION — template link texts use the template titles with STYLE capitalisation («Паспорт Initiative», «Разбор инцидента AI», «Снимок реестра», «Итоги управляющего совещания»); guide link texts kept as «Руководство по …» while the guide H1s read «Руководство: …». They should match whatever the template/guide workers settle.
- QUESTION — section 4 heading "How to read the charter" → «Порядок чтения корпуса документов»; column "Answers" → «Вопрос», "To find" → «Искомые сведения»; "Id" → «Код» (map table headers).
