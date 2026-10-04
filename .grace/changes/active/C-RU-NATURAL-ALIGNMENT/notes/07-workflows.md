# Notes: batch 07 — workflows (charter/ru/workflows/)

General choices for all seven files:

- QUESTION — workflow titles kept as they are referenced elsewhere in the corpus (charter/ru/README.md, shared-technology-terminology.md): «Портфель и поставка услуг», «Взаимодействие с заказчиком», «Риски и контроль AI», «Ритм работы», «Инструменты совместной работы», «Управление подразделением». The map discourages «поставка» for deliver; alternative title «Портфель и оказание услуг». Not changed because it is a fixed document name used in other files.
- QUESTION — event names follow the rewritten Vocabulary list (row «Мероприятие»): «ежедневная планёрка», «еженедельное планирование», «еженедельный обзор», «уточнение бэклога», «планирование итерации», «ревью и демонстрация итерации», «ретроспектива итерации», «обзор и демонстрация PI», «Inspect and Adapt», «PI-планирование», «инновации», «ежемесячное / ежеквартальное / ежегодное управляющее совещание». Loop names follow the rewritten Operating Model 6 and Portfolio Management Model 4.
- QUESTION — Work Item → «рабочий элемент» (STYLE §4); the older Russian corpus used «Рабочая задача». If the Vocabulary keeps «рабочая задача», replace in service-delivery, ai-risk-control, cadence, collaboration-tooling, unit-governance.
- QUESTION — figure captions written «Рисунок N — Название» (GOST style) instead of «Рисунок N: …».
- QUESTION — "the charter" (the body of documents) rendered «корпус»; the old text had «корпус Положения», which reads as the Положение об AICC (see DRIFT below).

## charter/ru/workflows/README.md

- DRIFT — intro and last paragraph: "the documents of the charter" / "The charter holds the schema" were «документах корпуса Положения» / «Корпус Положения содержит схему», which suggests the Положение об AICC; wrote «документами корпуса» / «Схема … содержится в корпусе». Same correction in every workflow file (§ "Where it runs").
- QUESTION — table column "Read when" → «Повод для обращения» (noun header).

## charter/ru/workflows/engagement.md

- QUESTION — table column "Consulting counterpart" → «Этап консалтингового проекта»; "Lead" → «Первичный контакт»; "Managed service" → «Сопровождение на условиях управляемой услуги»; "follow-on" → «последующее взаимодействие».
- QUESTION — "Initiative package" (§6) → «комплект материалов Initiative», to avoid «пакет», which is the AICC term Package.

## charter/ru/workflows/service-delivery.md

- DRIFT — table "Life of a live Solution", row Change: "reviews it within five working days" was «в течение пяти рабочих дней»; wrote «не позднее пяти рабочих дней с даты изменения» (start date taken from the terminology entry "emergency change"; the English row does not name it).
- QUESTION — step "Verify" → «Верифицировать», to keep «проверка» for the AICC term Check.
- QUESTION — service steps in Figure 10 keep the names of the current Russian Solution Lifecycle Model 8.8 («Допущен», «Внесён в каталог», «Обслуживает», «Улучшается», «Переход запланирован», «Мигрирует»); align if the worker on the lifecycle model renames them (e.g. «Эксплуатируется», «Миграция»).
- QUESTION — "benchmark" (Experiment table) → «базовые значения (для сравнения)»; old «база сравнения».
- ENGLISH? — Figure 1: "Capability: a capability" is circular; rendered «Capability: крупная функциональность решения» per the terminology reference.

## charter/ru/workflows/ai-risk-control.md

- QUESTION — "a category that the law … treats as high risk" → «группа систем AI, которую законодательство относит к высокорисковым», to keep «категория» for the Risk Tier.
- QUESTION — §6 "each edition" of an output published to investors → «каждая версия» («выпуск» is the AICC term Release; «редакция» is replaced by «версия» per STYLE §3).

## charter/ru/workflows/cadence.md

- DRIFT — §6, yearly Steering, "Takes in": "the findings of the year" was «отклонения, выявленные за год» (narrows to deviations); wrote «выводы, сделанные за год на эту дату» (map row "findings").
- DRIFT — §6, yearly Steering, "Gives": "the appointments in order" was «Актуальные назначения»; wrote «Подтверждение того, что все назначения произведены» (map row "in order"). Same in unit-governance §2 (old «Надлежащие назначения»).

## charter/ru/workflows/collaboration-tooling.md

- QUESTION — "Portal tooling" → «Средства формирования портала»; "Supporting knowledge folder" → «Папка вспомогательных материалов»; table column "Audience" → «Пользователи».

## charter/ru/workflows/unit-governance.md

- DRIFT — §4, row AI Incident: "the AICC Lead … reviews it afterwards" was «участвует в последующем разборе»; wrote «после устранения инцидента проводит его разбор».
- DRIFT — §4, row change of Holder: "names a deputy" was «назначает заместителя» (implies a post); wrote «определяет лицо, замещающее его на период отсутствия»; "accepts the Role" → «подтверждает согласие исполнять роль».
- DRIFT — Figure 5: internal audit "independent assurance" was «независимая оценка с предоставлением уверенности»; wrote «независимая оценка».
- QUESTION — §4 row "A change of provider or regulation" → «Изменение у поставщика или в регулировании» (read as a change on the provider's side, matching ai-risk-control §8); if a switch of provider is meant, use «Смена поставщика».
