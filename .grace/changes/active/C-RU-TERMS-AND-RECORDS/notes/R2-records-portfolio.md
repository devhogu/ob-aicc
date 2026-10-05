# R2 notes: Registry records (decisions, initiatives, pi) and Portfolio

Scope: registry/ru/decisions/**, registry/ru/initiatives/**, registry/ru/pi/**, portfolio/ru/**. Style: C-RU-NATURAL-ALIGNMENT/STYLE.md (revised 5 October 2026).

## General

- QUESTION (all records) — Decision Record field names and headings follow the Russian template «Запись о решении» (AICC-TPL-08-RU): «Наименование», «Вид», «Кем принято», «Статус: Принято», «4. Конфликт интересов и рекомендации», «5. Канал принятия», «Дата повторного рассмотрения». The old records used «Название», «Тип», «Решение принято», «Где принято решение». Alternative: keep the old record wording; chosen form keeps records and template aligned.
- QUESTION (all records) — "baseline" of documents is «базовая версия» (STYLE §3: version, not «редакция»). The Russian decision log (registry/ru/decision-log.md, not my file) still says «базовая редакция»; whoever owns it may want to align.
- QUESTION (all records) — ISO dates in prose are kept as ISO (2026-12-01), not «1 декабря 2026 года», because the build compares the multiset of record identifiers and ISO dates in Registry and Portfolio translations with the English (localization.py). STYLE §5 prose-date rule cannot apply here.

## registry/ru/decisions/README.md

- DRIFT — old Russian said the Operating Model 8 «требует такого подтверждения» for every decision; English: decisions that Operating Model section 8 names as evidenced by a Decision Record. Rewritten as «подтверждающей записью которого согласно разделу 8 Операционной модели служит запись о решении».

## registry/ru/decisions/DR-2026-060-baseline-of-the-charter-and-the-registry.md

- DRIFT — Facts: "controls its load by the Limit on Work in Progress" was rendered with Latin «WIP limit»; now «WIP-лимитом».
- DRIFT — D5: "are made by 2026-12-01" was «до 2026-12-01» (ambiguous: before vs not later than); now «не позднее 2026-12-01».

## registry/ru/decisions/DR-2026-061-the-first-steering.md

- No drift in meaning; terms lowercased.

## registry/ru/decisions/DR-2026-062-revision-2-0-of-the-documents.md

- DRIFT — findings table: Feature was rendered «Функциональность», Iteration «Итерация» (capital), Capability-type wording; now Latin Feature and lowercase «итерация» per STYLE §3.
- DRIFT — "SLM 10.3" in the findings table was left as the English abbreviation; now «Пункт 10.3 Модели жизненного цикла решений».
- QUESTION — "source edition" (English source edition 2.1 / 2.2) rendered «издание источников», to keep the distinction the English draws between the source edition and each document's revision («версия»). Old Russian used «редакция источников», which STYLE §3 rules out. Alternative: «выпуск источников» (collides with the AICC term Release = «выпуск»).
- QUESTION — quoted owner instructions are kept verbatim in English with a Russian gloss («в переводе: …»), as the old Russian did; meaning unchanged.

## registry/ru/decisions/DR-2026-063-approved-english-baseline.md

- DRIFT — D3.4/D3.5: Feature and Capability were rendered «Функциональность» / «Функциональная возможность»; now Latin Feature / Capability. "Ready holds at most two Features" was «Колонка «Готово к работе»» (a column name the English does not state); now «Готовыми к работе одновременно могут быть не более двух Features».
- DRIFT — D3.2: "becomes Active when its first approved run-rate Feature is pulled" was «при принятии … Функциональности»; now «когда в разработку принята её первая одобренная Feature текущих работ» (map row "take in, pull").

## registry/ru/decisions/DR-2026-064-shared-industry-terminology.md

- DRIFT — D3.2/D3.3: the old Russian listed the permitted terms in Latin («WIP limit», «business case») and called the brief «Паспорт инициативы — соответствующую Запись AICC»; now the Russian accepted forms «WIP-лимит», «бизнес-кейс», value stream/workflow Latin.
- DRIFT — D3.4: the reference was named by its English title "Shared Business and Technology Terminology"; now its Russian title «Общая деловая и технологическая терминология».
- ENGLISH? — D3.4 writes "the White recommendations" (capital W) and "gray entries" (lowercase g) for what look like two categories of the same scale; kept as «категории White» / «категории gray».

## registry/ru/initiatives/README.md

- DRIFT — PRI-4 and PRI-3 names differed from the Statement of Intent (old: «Экспертные знания на месте выполнения работы», «Внедрение в Доменах»); now «Экспертные знания на рабочем месте», «Внедрение в доменах» (Statement of Intent 9.4–9.5, map row "at the place of work"). The Russian Priorities Record (registry/ru/priorities.md, not my file) still uses the old forms.
- DRIFT — "Capabilities and Features" were «Функциональные возможности и Функциональности»; now Latin.

## registry/ru/initiatives/INI-002 … INI-008 (brief.md, six files)

- DRIFT (all six) — "Open sections: … 6 (the approver …)" was «лицо, одобряющее Инициативу»; section 6 records the approval of the business case, so now «лицо, одобряющее бизнес-кейс».
- DRIFT (all six) — "Portfolio Management Model 5" was cited as «Модель управления портфелем 5»; now «раздел 5 Модели управления портфелем». References in the form «п. X Документа» throughout.
- QUESTION (all six) — field and heading names follow the Russian Initiative Brief template (AICC-TPL-02-RU): «Незаполненные разделы», «Источник числовых значений», «Соглашение о взаимодействии оформлено», «Приёмка переданного результата», «Управленческие решения и приёмка». The old briefs used «Открытые разделы», «Место хранения числовых значений», «Выпуск Соглашения», «Приёмка при поставке».
- QUESTION (INI-004) — report "edition" rendered «издание (отчёта)» to avoid the AICC term Release («выпуск»); old Russian used «выпуск».
- QUESTION (INI-003, INI-008, objectives) — "functions" as the Bank's units rendered «подразделения» (STYLE §3); the function names: «правовое подразделение» for legal, «подразделения комплаенса, HR, правовое, финансовое и бухгалтерия».
- QUESTION (INI-007) — "Standards ARC-004" rendered «ARC-004 записи о стандартах» (entry of the Standards Record); same for ARC-001 in INI-008.

## registry/ru/initiatives/INI-009 … INI-012 (standing, four files)

- DRIFT (all four) — Feature / Capability were «Функциональность» / «Функциональная возможность»; Iteration capitalised; now Latin Feature and lowercase «итерация».
- QUESTION (all four) — service categories use the Business Model 4.5 names: «Бизнес-кейсы и сценарии» (old: «business cases и сценарии»), «Оценка и экспертиза», «Мониторинг».
- QUESTION (all four) — "Iteration Review and Demo" rendered «ревью и демонстрация итерации» as in the Russian SLM; the old briefs used «Обзор и демонстрация Итерации».

## registry/ru/pi/2026-PIQ4/ip-week.md

- DRIFT — English source changed (C-07 rewording): the quarterly Steering decisions now include "the approval of the Quarterly Report, and whether to submit it to the Board Committee", and C-07 is "the approval of the Quarterly Report, and its submission to the Board Committee where the Executive Sponsor decides". The old Russian said the report to the Board Committee is «Квартальный отчёт в редакции, одобренной и направленной Куратором AICC» and C-07 «отчёт Комитету Совета директоров» (submission as given). Rewritten to the new English: submission is optional, by decision of the Executive Sponsor. source_sha256 updated to 83b95815….
- DRIFT — Inspect and Adapt was rendered «Анализ и адаптация»; the map keeps the protected term in Latin («Inspect and Adapt»). PI Planning now «PI-планирование».
- QUESTION — "PI Review and Demo" rendered «обзор и демонстрация PI» (as in the Russian SLM 6.x), while "Iteration Review and Demo" is «ревью и демонстрация итерации»; the corpus uses both nouns. Someone may want one noun for both.

## registry/ru/pi/2026-PIQ4/iterations.md, objectives.md, I10.md, I11.md, I12.md

- DRIFT (I10–I12) — "Waiting on" column was «Ожидаемая Зависимость»; now «Чего ожидает». The lane "Normal" was «Обычный»; now «Обычный приоритет» (class-of-service name in the Russian SLM).
- QUESTION (iterations) — iteration status values "In progress / Planned" rendered «Идёт / Запланирована» (agree with «итерация»); old «В работе / Запланировано» read as item states.

## portfolio/ru/README.md

- DRIFT — "Solutions that AICC delivers or oversees" was «поставляет … осуществляет надзор»; the map rules out «надзор» for AICC; now «создаёт … или контролирует».

## portfolio/ru/packages.md and portfolio/ru/packages/PKG-001 … PKG-012

- DRIFT (PKG-005) — "Process-drawing kit" was «Комплект средств построения workflows»; the kit draws process flows, not workflow documents; now «Комплект инструментов для построения схем процессов».
- DRIFT (PKG-011, catalog) — service category "Assessments and evaluations" was «Оценка и проверки»; now the Business Model name «Оценка и экспертиза».
- DRIFT (PKG-001 … PKG-012) — the field "Owner" was «Владелец»; the Russian template uses «Ответственный» (a Package has an owner who keeps it, not a Domain Owner); "Produced by" was «Происхождение», now «Создан по итогам» per template.
- QUESTION (all) — Package kinds follow the Russian template: kit «комплект инструментов» (old «комплект средств»), engine «программный компонент» (map row "engine"; old «программный механизм»), status values «запланирован / в подготовке / доступен / отозван».
- QUESTION (PKG-008) — "ETL and dashboard patterns" rendered «Типовые схемы ETL и панелей показателей», avoiding «типовые решения» because «решение» alone is the AICC term Solution.
- QUESTION (PKG-001 … PKG-003) — section 2 link targets point to charter/ru and registry/ru files, as in the old Russian, while the English links to charter/en; kept (Russian files exist).

## portfolio/ru/solutions/SOL-001-fpa-board-reporting-pipeline.md

- DRIFT — "Publishing is a human act" was «выполняет человек»; now «работник» (STYLE §5, map row "human, person").
- DRIFT — heading 2 "Scope and capabilities" was «функциональные возможности»; now «Объём работ и Capabilities» as in the template.
