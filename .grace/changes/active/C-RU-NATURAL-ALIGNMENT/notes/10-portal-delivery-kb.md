# Notes: portal delivery and knowledge base (batch 10)

## Batch-wide choices

- QUESTION — section title «Поставка» (EN «Delivery»). Kept as the H1 of `delivery/overview.md`, because the
  portal navigation in `authored.json` (not in this batch) says «Поставка» and the guide and workflow titles
  use «поставка услуг». In prose, verbs follow the map (разработать, внедрить, передать, выполнить); the noun
  «поставка» is used for the area and the stage. Alternative: «Разработка и внедрение решений» for the whole
  section, changed together with the navigation.
- QUESTION — event names. STYLE.md gives only «мероприятие»; the forms follow the accepted forms of the
  terminology reference, lowercase: ежедневная планёрка, еженедельное планирование, еженедельный обзор,
  уточнение бэклога, планирование итерации, ревью и демонстрация итерации, ретроспектива итерации,
  PI-планирование, обзор и демонстрация PI, Inspect and Adapt, инновации, управляющее совещание.
  Alternative: «обзор и демонстрация итерации» (current Vocabulary wording) and «Анализ и адаптация»
  (current Vocabulary) — the terminology reference marks Inspect and Adapt as protected Latin.
- QUESTION — «руководитель AICC является владельцем домена» rewritten as «роль владельца домена исполняет
  руководитель AICC» (map row «is the owner of» is about assets; the sentence is about holding the role, but
  the scan flags the string). Alternative: keep «является владельцем домена».
- QUESTION — PDCA step names kept as «Планирование — Выполнение — Проверка — Корректировка»; «Проверка» here
  is the PDCA step, not the AICC term Check. Alternative: «Контроль».
- QUESTION — Kanban column «Review» kept as «Рассмотрение» (as in the Solution Lifecycle Model); the state is
  «На рассмотрении».

## portal/content/ru/delivery/overview.md

- No meaning drift. Old text used rejected «поставлять» and «не являющимся разработчиком».

## portal/content/ru/delivery/the-flow-of-value.md

- Title changed from Latin «Value stream» to «Поток создания ценности» (EN title «The flow of value»).

## portal/content/ru/delivery/backlogs-boards-and-kanbans.md

- No meaning drift.

## portal/content/ru/delivery/the-cadence.md

- DRIFT — table row «Неделя»: EN «in a clean calendar» (no blocked or gray days, per the Cadence workflow);
  old RU «в календаре без переносов». Now «если в календаре нет нерабочих дней и дней ограниченной доступности».

## portal/content/ru/delivery/events-and-rituals.md

- No meaning drift (old «одобряет» the Quarterly Report → «утверждает» per map).

## portal/content/ru/delivery/the-loops-of-delivery.md

- No meaning drift.

## portal/content/ru/delivery/quality-verification-and-release.md

- DRIFT — 2.1: EN «security test against the attacks specific to AI»; old RU «проверку безопасности в
  отношении специфических атак» (security check, and «проверка» = Check). Now «тестирование защищённости от
  атак, характерных для AI».
- DRIFT — 2.3: EN «an item not met stops the release»; old RU «невыполненный пункт останавливает Выпуск»
  (a checklist item as actor). Now «При наличии невыполненного пункта выпуск не допускается» (map row 4).

## portal/content/ru/delivery/measures-and-tracking.md

- No meaning drift.

## portal/content/ru/delivery/measures-definitions-and-formulas.md

- No meaning drift. «Response and resolution time» rendered «Время реакции и разрешения запроса» to keep
  «решение» for Solution.

## portal/content/ru/delivery/roles-and-records.md

- No meaning drift.

## portal/content/ru/delivery/life-cycle-management.md

- DRIFT — 3.1: EN «A Service the Bank should run at scale»; old RU «Сервис, который Банк должен
  эксплуатировать» (recommendation turned into obligation). Now «целесообразно эксплуатировать силами Банка
  в масштабе Банка».

## portal/content/ru/delivery/life-of-a-service.md

- DRIFT — 3.1: same «should run at scale» → old «должен эксплуатировать»; now «целесообразно».

## portal/content/ru/delivery/service-operations.md

- QUESTION — table row «Обработка запросов», column «Кто действует»: EN «the AICC Lead for the class»; old RU
  «Руководитель AICC определяет класс». Written «руководитель AICC — в части класса обслуживания», which keeps
  the EN vagueness. Alternative: «руководитель AICC определяет класс обслуживания».
- QUESTION — «the incident management of the Bank» as actor rendered «подразделение Банка, отвечающее за
  управление инцидентами» (same for change management). Alternative: «управление инцидентами Банка».

## portal/content/ru/delivery/experiment-workflow.md

- QUESTION — 2.3: EN «An Experiment keeps its one offering type»; old RU «сохраняет свой тип предложения»
  (clashes with «предложение» = Proposal). Now «Эксперимент не меняет свой тип».

## portal/content/ru/knowledge-base/overview.md

- No meaning drift. Old «юридической функции» → «по правовым вопросам» (map).

## portal/content/ru/knowledge-base/guides.md

- No meaning drift. Link text for the How-to-engage page follows its current Russian title
  «Порядок взаимодействия с AICC».

## portal/content/ru/knowledge-base/learning-paths.md

- QUESTION — page title «Учебные траектории» kept; the home-page link in `authored.json` (not in this batch)
  says «Учебные маршруты». One of the two should be aligned.
- Link texts follow the current Russian titles of the target pages («Распределение обязанностей»,
  «Работники и назначения», «Управленческие решения и эскалация»); they need updating if those titles change.

## portal/content/ru/knowledge-base/templates-and-forms.md

- DRIFT — row «Итоги управляющего совещания», column «Когда используется»: EN «the decisions, the actions»;
  old RU «решения, мероприятия». Now «управленческие решения, поручения» (map row «actions»).
- DRIFT — row «Запись о назначениях»: EN «deputies», «the named deputy»; old RU «заместители», «назначенный
  заместитель» (map: not a deputy position). Now «лица, замещающие их на период отсутствия».

## portal/content/ru/knowledge-base/playbooks-and-lessons.md

- QUESTION — 5.1: EN «the governance catalog» rendered by the Portfolio package name «Каталог управления»
  (PKG-002, Portfolio is outside this batch). The name reads poorly; alternative «каталог механизмов
  управления» (as on the services page) or «каталог контрольных процедур», changed together with the Portfolio.

## portal/content/ru/knowledge-base/acts-and-compliance.md

- DRIFT — table row «Законодательство о защите прав потребителей…»: EN «can contest a decision»; old RU
  «возможность оспорить решение». Now «потребовать пересмотра принятого в отношении него решения» (map).
- No other drift; «confirmed by the Contacts … each within its remit» → «определяют … каждый в пределах своей
  компетенции» (map).

## portal/content/ru/knowledge-base/questions-people-ask.md

- DRIFT — «Какие обязательства принимает AICC…»: EN «on a best-effort basis within its capability»; old RU
  «с приложением максимально возможных усилий» (overstates the commitment; rejected in the map). Now
  «с приложением усилий в разумных пределах, исходя из имеющихся у него возможностей».
- DRIFT — «Можно ли получить исключение…»: EN «an Exception, decided by the Control Function Contact»; old RU
  «Его одобряет» (decided ≠ approved). Now «О нём решает представитель контрольной функции…».
- DRIFT — «Что происходит, если AI становится причиной инцидента?»: EN «a major incident»; old RU
  «существенном инциденте». Now «крупном» (as in the AICC Charter 7.2).
