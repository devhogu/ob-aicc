# Notes: batch 08 — templates (charter/ru/templates/)

General choices for all fifteen templates (not repeated per file):

- QUESTION — field/column "Entry" → «Содержание» (was «Значение»); "Name, signature, and date" → «ФИО, подпись, дата»; placeholder "[name]" → «[ФИО]». Alternative «Имя»; ФИО is usual in bank forms.
- QUESTION — "Decision reference" → «Реквизиты управленческого решения»; "Decision" (column/heading) → «Управленческое решение»; "Decided by" → «Кем принято» / «Кем утверждено». Keeps bare «решение» for Solution.
- QUESTION — "Risks and Issues entry" → «Позиция записи о рисках и проблемах» (was «Запись о рисках и проблемах», which names the whole record, not a line in it).
- QUESTION — Front matter `title:` changed to lowercase terms/protected names: «Паспорт Initiative», «Разбор инцидента AI», «Снимок реестра», «Итоги управляющего совещания». The Document Catalog and other files that quote these titles need the same forms.

## charter/ru/templates/README.md

- QUESTION — column "Order" → «№», "Id" → «Код» (map row table headers), "Used when" → «Случай применения», "Kept in" → «Место хранения».
- QUESTION — "use at scale" / "adoption at scale" → «масштабное применение» / «масштабное внедрение» (was «в большем масштабе»); alternative «в масштабе Банка». Same choice in acceptance-checklist and proposal.

## charter/ru/templates/acceptance-checklist.md

- QUESTION — EN items are statements, so kept as statements (not «Выполнено ли …?» questions).
- QUESTION — "Where the AICC Lead is the Domain Owner" → «если руководитель AICC исполняет роль владельца домена» (avoids rejected «является владельцем»).
- QUESTION — party "Model risk" → «Модельный риск», "Legal" → «Правовые вопросы» (map row legal).

## charter/ru/templates/ai-incident-review.md

- QUESTION — headings "What happened" → «Описание инцидента»; "Cause, actions, and lessons" → «Причина, меры и выводы» (noun headings; map row lessons).

## charter/ru/templates/appointments-record.md

- QUESTION — "Deputy" → «Лицо, замещающее на период отсутствия»; event "Deputy named" → «Определено замещающее лицо» (map row deputy).
- QUESTION — "A Checker / product owner is a designation and not a Role" → «… определяется персонально и ролью не является».
- ENGLISH? — "The heads and the Contacts named below the Roles" is vague (named where?); written «Руководители и представители контрольных функций, указанные после ролей».

## charter/ru/templates/control-sign-off.md

- QUESTION — field "Decision" → «Заключение» (the sign-off itself), to avoid «Решение» (Solution); alternative «Управленческое решение».

## charter/ru/templates/decision-record.md

- QUESTION — heading "5. Where it was decided" → «5. Канал принятия» (noun heading).
- QUESTION — "approval of published output" → «одобрение публикуемого результата AI» (AI Policy 2.4 is about AI output).

## charter/ru/templates/initiative-brief.md

- QUESTION — Kind of work values written per Vocabulary «бизнес / обеспечивающие работы / риски и соблюдение требований» (was «риск и комплаенс»).
- QUESTION — "It is the investment decision" → «Паспорт фиксирует управленческое решение об инвестициях».

## charter/ru/templates/package-definition.md

- QUESTION — field "Owner" → «Ответственный» (map row is the owner of); headings made nouns («Назначение пакета и решаемая проблема», «Порядок повторного развёртывания»).

## charter/ru/templates/proposal.md

- ENGLISH? — "Decides: [the owners and the Executive Sponsor, or the Bank]": "the owners" is not a defined role; written «владельцы доменов», alternative «ответственные лица».

## charter/ru/templates/quarterly-report.md

- QUESTION — "Issuance" → «Утверждение и направление отчёта» («выпуск» is the AICC term Release).
- QUESTION — "Target rule" column → «Порядок установления целевого значения» (map row table headers).

## charter/ru/templates/service-agreement.md

- DRIFT — intro: "on a best-effort basis, within the capability that it has available" was «прилагая максимально возможные усилия в пределах доступных возможностей» (stronger than best effort); written «с приложением усилий в разумных пределах, имеющимися у него силами и средствами» (same as guides batch).

## charter/ru/templates/solution-definition.md

- QUESTION — service step values kept as in the current Russian Solution Lifecycle Model 8.8 («Допущен / Внесён в каталог / Обслуживает / …»); they need to be synced if that file renames them.
- QUESTION — "within five working days" (emergency change) → «не позднее пяти рабочих дней с даты изменения»; "from the date of the change" taken from the terminology reference (emergency change).
- ENGLISH? — §4 "(AI Policy 3.2; Portfolio Management Model 6.4)." has a stray full stop inside the bracketed sentence.

## charter/ru/templates/steering-summary.md

- QUESTION — "assurance loop" kept as «цикл подтверждения надлежащего функционирования» (current Operating Model 6.6); "found in order" → «признанные надлежащими».
- QUESTION — "Actions" → «Поручения» (map row actions); "Appointments in order" → «Подтверждение того, что все назначения произведены» (map row in order).
