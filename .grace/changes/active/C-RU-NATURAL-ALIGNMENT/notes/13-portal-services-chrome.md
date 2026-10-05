# Notes: batch 13 — portal services pages, authored.json (ru), messages/ru.json, build.py Russian literals

## portal/content/ru/services/ (all 23 pages, general)

- QUESTION — category names kept as in the Business Model and in Registry/Portfolio records: «Оценка и проверки», «Надзор», «Сервисы знаний», «Управление содержанием», «Исследования и изучение возможностей». «Проверки» clashes with the term Check and «надзор» is a supervisory-authority word (map row oversee); alternatives «Оценка и тестирование», «Контроль за внедрёнными решениями». Kept so that page titles match the Registry «Направление и категория услуг» fields, which this batch may not edit. Only «business cases и сценарии» was changed, to «Бизнес-кейсы и сценарии».
- QUESTION — the services page title «Как взаимодействовать с AICC» became «Порядок взаимодействия с AICC» (STYLE §5: noun headings); series title in messages/ru.json changed to match. Other workers' pages that cite «Как взаимодействовать с AICC» should follow.
- QUESTION — recurring category headings (EN «What it is», «What the function receives», «How it runs», «What it leads to», «Run-rate work or an Initiative», «Who decides») rendered as noun headings «Содержание категории», «Результаты для подразделения», «Порядок работы», «Ожидаемый эффект», «Режим», «Полномочия по принятию решений».
- QUESTION — "engine" rendered «программный компонент» (map row engine); Portfolio PKG names still say «программный механизм».
- QUESTION — "edition" of a report or document family rendered «издание» (not «редакция», which STYLE §3 retires, nor «выпуск», the term Release).
- QUESTION — references now use «п. 4.7 Бизнес-модели», «разделы 7 и 8 Модели …». build.py links only the number adjacent to the document title, so in lists such as «пункты 2.4, 4.5 и 4.10 Бизнес-модели» no number is linked (the old «Бизнес-модель 2.4, 4.5 и 4.10» linked the first one). Single references («п. 4.7 Бизнес-модели») link correctly.

## portal/content/ru/services/service-model.md

- DRIFT — intro: EN "is not a promise in the air"; old «Услуга AICC — конкретное обязательство». Wrote «не абстрактное обещание».
- DRIFT — 2.2: old «осуществляет надзор за Внедрённым решением» (map-rejected); wrote «контролирует внедрённое решение».

## portal/content/ru/services/how-to-engage.md

- DRIFT — 3.1: old «с приложением максимально возможных усилий в пределах доступных ему возможностей» (map-rejected); wrote «с приложением усилий в разумных пределах, исходя из имеющихся у него ресурсов».
- DRIFT — 5.1: EN "the management" rendered «руководства»; wrote «Правления Банка» (map row management).
- DRIFT — 2.2: old pointed to the page «Каталог услуг»; the page with the form is «Каталог услуг: форма».

## portal/content/ru/services/catalog-form.md

- DRIFT — 5.1 example: SOL-001 title aligned with the Portfolio record («Конвейер отчётности FP&A для Совета директоров»); old RU had «Конвейер подготовки финансовой отчётности FP&A …».

## portal/content/ru/services/normatives-and-processes.md

- DRIFT — examples: EN "actions" from a meeting; old «мероприятий». Wrote «поручений» (map row actions).
- DRIFT — examples: old «Описание и Workflow по документам…» for "A process mapped and drawn"; wrote «Процесс, описанный и представленный в виде схемы…».

## portal/content/ru/services/business-cases-and-scenarios.md

- DRIFT — 5.1: "Decisions taken on evidence"; old «на основе подтверждающих материалов». Wrote «на основе фактических данных» (map row evidence, basis of decisions).

## portal/content/ru/services/adoption-and-lifecycle-management.md

- ENGLISH? — 1.1 says revision goes "through the Portfolio Backlog", 4.1 says "a revision enters the Program Backlog". Translated as written.

## portal/content/ru/services/strategy-and-governance.md

- DRIFT — 5.1: old «регулятору» kept as «надзорному органу» (map row regulator); "baselined charter" now «утверждённая базовая версия» (not «редакция»).

## portal/content/authored.json (ru values)

- DRIFT — /sections/governance/intro: old RU described a different text (contours, evidence, control catalog, "status kept in the Control Matrix"); rewritten from EN (seven-part course, then the rule: control loops, records and evidence, control catalog, delivery controls, Unit governance workflow and guide).
- DRIFT — /sections/reference/intro: old RU covered only the inward part (Vocabulary, Catalog, history); rewritten to include standards, regulators and acts, research and open resources.
- DRIFT — /home/lead: old RU added a sentence («Этот сайт — место, где Банк узнаёт…») and dropped "Center of Competence and Solution Hub"; fixed.
- DRIFT — /home/priorities_lead: old RU «Семь стратегических приоритетов по порядку, каждый проходит пять уровней зрелости…»; EN "Top Strategic Priorities, aligned with the Bank's ambitions and goals." Rewritten.
- DRIFT — /routes[1]/reader: old «Исполнительный спонсор и комитет совета»; wrote «Куратор AICC и Комитет Совета директоров».
- DRIFT — /strategy_page/priorities_lead: old «совместно с Советом директоров»; wrote «по согласованию с Советом директоров» (map row set together with).
- DRIFT — /strategy_page/aspects[1]/choice: old «без Куратора AICC»; wrote «без решения куратора AICC» (map row without).
- DRIFT — /about_page/blocks[5]/text: old «могут остановить Решение», «осуществляет надзор за AI»; wrote «вправе остановить применение решения», «осуществляет контроль за применением AI».
- QUESTION — /strategy_page/pillars_carried: «Экспертные знания на месте выполнения работы» changed to «Экспертные знания на рабочем месте» (map row at the place of work; Statement of Intent 9.5). portal/tests/test_localization.py::test_mandate_projections_follow_the_selected_corpus asserts the old wording and now fails; the test needs the new form (tests not edited).
- QUESTION — kept because tests or build.py match them: /sections/about/label «О центре AICC», /sections/governance/label «Управление», /home/title, «Заявление о намерениях», /routes[1]/title «Руководство». /routes[4]/title "Review" changed from «Проверка» (term Check) to «Аудит и контроль».
- QUESTION — /explore_page/parts[0]/where and parts[1]/where: EN names a section "Governance and oversight"; the section label is "Governance" («Управление»). Used «Управление». ENGLISH? — section name differs from the section label.
- QUESTION — "Principles of delivery" kept as «Принципы поставки» (section «Поставка»); messages page description aligned («… работы и поставки»).

## portal/messages/ru.json

- DRIFT — parts_label: EN "Parts of this document or course"; old «Части документа». Wrote «Части документа или курса».
- QUESTION — kind_workflow and part_titles/services/engagement-workflow kept as «Workflow» because tests assert «Workflow: Управление подразделением: …» and «>Workflow</a>»; STYLE §3 wants «рабочий процесс». grp_workflows and companion_workflow changed to «Рабочие процессы», «Связанный рабочий процесс».
- QUESTION — owner/control_owner «Владелец» → «Ответственный» (map row is the owner of). status_deprecated «Выведен из действия» → «Утратил силу» (map row no longer in force). Footer and baseline: «Редакция комплекта документов 2.2» → «Версия корпуса документов 2.2» (STYLE §3 версия).
- QUESTION — kept because tests or build.py match them: site_name, figure «Рисунок», change_history «Журнал изменений», table/diagram labels, status_active «Действующий», capability «Возможность», page/part/series titles asserted by tests.

## portal/tools/build.py

- DRIFT — records page, Jira row: EN "Work Items"; old «Рабочих задач» (= Task). Wrote «рабочих элементов». "cutover of the working state" → «с момента перехода рабочего состояния в эти системы».
- QUESTION — records page, Registry row: "closed and dated extracts" → «неизменяемых датированных выгрузок» (map row closed extract); "corporate folder" → «корпоративном сетевом ресурсе».
- QUESTION — change-history header ('Decision', 'Решение') left unchanged: «Решение» alone is the Solution term, but the column holds DR identifiers and the same header is used in the corpus change logs; alternative «Запись о решении».
