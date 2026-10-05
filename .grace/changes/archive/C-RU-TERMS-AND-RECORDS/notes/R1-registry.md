# R1: notes on the Russian Registry root files, steering/ and reports/

Scope: registry/ru/*.md (16 root files), registry/ru/steering/README.md, registry/ru/steering/2026-09-02-first.md, registry/ru/reports/README.md. All were rewritten in the revised STYLE.md style (Russian «инициатива», lowercase AICC terms, «версия», references like «п. 8.5 Операционной модели»). Each one passes check_one.py. Record identifiers and ISO dates match the English multiset.

## registry/ru/control-matrix.md
- DRIFT: source_sha256 was stale. English row C-07 was reworded to "Approval of the Quarterly Report, and its submission to the Board Committee or the Board where the Executive Sponsor decides", and its evidence to "Quarterly Report with its approval block, and the submission where made". The old Russian still had the earlier wording («Отчёт Комитету Совета директоров», «в направленной … редакции»). It now reads «Утверждение квартального отчёта и его направление Комитету Совета директоров или Совету директоров, если так решит куратор AICC», and the hash is updated.
- DRIFT: C-01. The old Russian said «распоряжение Совета директоров … не зафиксировано»; the English is "the order of the Board … is not recorded". It now says «реквизиты решения Совета директоров … не внесены».
- DRIFT: C-08 and C-32. "did not operate" was given as «не сработала» (colloquial); it is now «не выполнена». C-04: "revision 2.1 correction rows" is now «строки журнала изменений версии 2.1 об исправлениях».
- QUESTION: code spans `portfolio/en/solutions/` were kept as `portfolio/ru/solutions/`, as the earlier reviewed Russian had them, because that folder exists. The alternative is to copy the English path literally.

## registry/ru/decision-log.md
- DRIFT: the statuses were inconsistent: «Решение принято» for DR-060 to DR-063 and «Принято» for DR-064. All five are now «Принято», which matches the Decision Record template (Принято / Заменено / Отменено).
- DRIFT: "English source edition 2.2" was rendered as «английская редакция источников»; it is now «англоязычная версия источников 2.2» (language edition is «языковая версия»). "Baseline owner" is «владелец базовой версии».

## registry/ru/appointments.md
- QUESTION: "Simen Munter, Chief Executive Officer of the Bank" was rendered as «председатель Правления Банка», the usual title of a bank CEO in Kyrgyz practice. The old Russian had «главный исполнительный директор Банка». Please revert if the Bank's own post title differs.
- DRIFT: "Internal audit gives assurance only" was rendered as «независимое подтверждение»; the map form is now used: «проводит только независимую оценку». "Legal" was «Юридическая функция»; it is now «Правовые вопросы». "Deputy" was «Заместитель»; it is now «Замещающее лицо» (map: deputy for absence).
- QUESTION: the heads of the AI Steering Committee "functions" (Business, Technology, Risk, Compliance) are rendered as «направления», to avoid «функция» for a part of the Bank. "Head of technology" is «Руководитель по технологиям».

## registry/ru/board.md, dashboard.md
- DRIFT: the Program Kanban column "Review" was «На рассмотрении», which matches the state name, not the column name. It is now «Рассмотрение», as in п. 4.2 of the Solution Lifecycle Model (Russian). The lane "Normal" is now «Обычный приоритет».
- QUESTION: "Shared in-progress limit" is rendered as «Общий лимит работы в процессе» in board.md and as «общий» in the dashboard. «WIP-лимит» would also fit.

## registry/ru/dependencies.md, roadmap.md
- DRIFT: the section heading had a typo «Вехаs». The column "Roadmap" was left in English. Dependency statuses were neuter («Открыто»/«Выполнено»); they are now «Открыта»/«Выполнена»/«Под угрозой», as in п. 4.3 of the Solution Lifecycle Model (Russian). Milestone status «Запланировано» is kept as the status label.

## registry/ru/risks-and-issues.md, standards.md
- DRIFT: "to confirm" was «требует подтверждения»; it is now «подлежит подтверждению», the same in both files, including the quoted mark in RI-006. "regulators" was «регуляторов»; it is now «надзорных органов» (map).
- DRIFT: standards ARC-008. "an alert level that is crossed triggers a review" was «пересечение Сигнального значения запускает пересмотр»; it is now the map form «достижение сигнального значения служит основанием для рассмотрения». ARC-005: "reads untrusted content" now uses the map form («обрабатывает содержимое из недоверенных источников»).
- QUESTION: the Lab section heading "Guardrails of the Lab" was «Ограничения Лабораторной среды». It is now «Защитные механизмы лабораторной среды», as SLM 8 (Russian) puts it. "Investment Guardrails" stays «инвестиционные ограничения».

## registry/ru/calendar.md
- QUESTION: "Iteration Review week" is rendered as «неделя обзора» (Vocabulary term «неделя обзора»). The IP-week note "holds the Iteration Review and Demo of the third Iteration" is rendered as «ревью и демонстрация третьей итерации». The event names follow the Cadence workflow (Russian): «обзор и демонстрация PI», Inspect and Adapt, «инновации», «PI-планирование».

## registry/ru/ai-registry.md
- ENGLISH?: the assistant entry has the Stage "In use", but the Vocabulary defines no stage of that name. «Используется» is kept as written.
