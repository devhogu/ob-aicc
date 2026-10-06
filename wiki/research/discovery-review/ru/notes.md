# Points raised in the Russian rewrite of the Discovery Catalog

Prepared 6 October 2026. The translators recorded the choices a person should confirm: names of units and roles not settled by the translation map, terms they chose for the whole catalog, and doubts about the English source. Listed by page as recorded.

Pages: 62. Points: 302.

## (overview)

- Key 62 (language switch, English source «Russian») written as «English», as in the old Russian page, since on the Russian page the link leads to the English edition; scan flags the Latin word. Confirm.
- Key 50 breadcrumb «Financial Services» rendered «Финансовые услуги»; the map gives «Каталог сценариев» for navigation, so confirm which the breadcrumb should show.
- Key 390 «Customer and balance-sheet value streams» rendered with the brief's settled «Клиентские потоки», which drops «balance-sheet»; «Клиентские и балансовые потоки» would render it fully.
- Link labels must match the final page titles written by other parts. Kept the old Russian titles except: ALM → «Управление активами и пассивами» (map), Customer onboarding → «Оформление клиентов» (map), Transaction processing & settlement → «Обработка операций и расчёты», Advisory & research → «Консультирование и исследования», Performance measurement → «Оценка результатов деятельности», Accounting & financial close → «Бухгалтерский учёт и закрытие периода». Cycles pages keep their old names («Управленческие циклы», «Циклы изменений», «Аналитические циклы», «Циклы развития возможностей», «Финансовые циклы»).
- «Framework» rendered «модель» (title, «Смежные модели», «Модель информационных технологий (отложена)»); confirm against the portal's chosen word.

## banking-data-analytics

- Data steward rendered «стюард данных», as on the sub-pages; the map has no row for steward or stewardship. Confirm for the whole data section.
- Navigation labels aligned with the titles already written on the sub-pages (for example «Ведение и качество данных», «Данные по картам и ТСП», «Данные об ОКУ и резервах»); if a sub-page title changes, the label here must follow.
- Master data rendered «основные данные», the master-and-reference card «Нормативно-справочные данные»; data domain «домен данных»; case taxonomy «единый классификатор».

## banking-data-analytics/credit-exposure-data

- Заголовок страницы оставлен прежним («Кредитные данные и данные об экспозициях»), чтобы совпадать с навигационными ссылками; exposure на всей странице передано как «экспозиция». Если владелец предпочитает «кредитные требования», нужно менять страницу и ссылки на неё вместе.
- core banking передано как «автоматизированная банковская система (АБС)»; credit operations team — «подразделение кредитного администрирования»; Chief Credit Officer — «директор по кредитным рискам» (как на остальном портале). В справочнике перевода этих строк нет.
- Карточка connected-party-group-mapping: в источнике «flagged for CDE refresh» в контексте сведений о бенефициарных владельцах. Передано как «критически важные элементы данных (CDE)»; возможно, в английском тексте имелось в виду CDD (надлежащая проверка клиента). Нужно уточнить источник.
- Сокращения CRE и SICR не входят в список допустимой латиницы: CRE опущено (написано «коммерческая недвижимость»), SICR передано как «значительное увеличение кредитного риска» без сокращения. Cures передано как «выздоровление кредитов».

## banking-data-analytics/customer-data

- Customer 360 rendered «единый профиль клиента» throughout the page (matches the existing aria-label «Единый профиль клиента (360)»); confirm.
- UBO rendered «конечный бенефициарный владелец», then «бенефициарный владелец»; the old abbreviation КБВ is dropped because it is not in the map.
- Compliance team rendered «служба комплаенса», compliance analyst «аналитик по комплаенсу», data privacy officer «ответственный за обработку персональных данных» (map DPO row), data privacy team «подразделение по защите персональных данных»; confirm against the Bank's unit names.
- Where an OKR deadline such as «within 45 days» has no anchor of its own, the go-live date from the same line is used: «не позднее 45 дней с даты запуска».
- Suppression lists rendered «списки исключения».
- Revenue tier rendered «категория доходности», product-affinity rules «правила склонности к продуктам», completeness scorecard «оценочная карта полноты» (map scorecard row), core banking «автоматизированная банковская система (АБС)».
- Line 2106: «within 6 months» has no go-live anchor in English and is rendered «в течение 6 месяцев»; confirm whether it should be counted from go-live like the other lines.

## banking-data-analytics/data-cycles

- Термины управления данными, которых нет в справочнике по переводу, приняты единообразно для всех пяти частей: data steward — «стюард данных»; master data — «основные данные», master & reference data — «нормативно-справочные данные»; golden record — «золотая запись»; lineage — «происхождение данных» (документ — «описание происхождения данных»); attestation — «подтверждение» (не «аттестация»); validation exception — «отклонение, выявленное при валидации» (не «исключение»); CDE — «критически важные элементы данных (CDE)». Нужно решение, закрепить ли их в справочнике для всех страниц раздела «Банковские данные и аналитика».
- Метки проблем цикла (Analyze, Optimize, Automate, Enrich) оставлены по сводке от 6 октября 2026 года: «Анализ», «Оптимизация», «Автоматизация», «Накопление знаний», хотя в брифе аспекты названы «Аналитика»…«Новые возможности». Нужно подтвердить.
- Термины управления данными, которых нет в справочнике по переводу, приняты единообразно для всех пяти частей: data steward — «стюард данных»; master data — «основные данные», master & reference data — «нормативно-справочные данные»; golden record — «золотая запись»; lineage — «происхождение данных» (документ — «описание происхождения данных»); attestation — «подтверждение» (не «аттестация»); validation exception — «отклонение, выявленное при валидации» (не «исключение»); CDE — «критически важные элементы данных (CDE)». Нужно решение, закрепить ли их в справочнике для всех страниц раздела «Банковские данные и аналитика».
- Термины управления данными, которых нет в справочнике по переводу, приняты единообразно для всех пяти частей: data steward — «стюард данных»; master data — «основные данные», master & reference data — «нормативно-справочные данные»; golden record — «золотая запись»; lineage — «происхождение данных» (документ — «описание происхождения данных»); attestation — «подтверждение» (не «аттестация»); validation exception — «отклонение, выявленное при валидации» (не «исключение»); CDE — «критически важные элементы данных (CDE)». Нужно решение, закрепить ли их в справочнике для всех страниц раздела «Банковские данные и аналитика».
- Термины управления данными, которых нет в справочнике по переводу, приняты единообразно для всех пяти частей: data steward — «стюард данных»; master data — «основные данные», master & reference data — «нормативно-справочные данные»; golden record — «золотая запись»; lineage — «происхождение данных» (документ — «описание происхождения данных»); attestation — «подтверждение» (не «аттестация»); validation exception — «отклонение, выявленное при валидации» (не «исключение»); CDE — «критически важные элементы данных (CDE)». Нужно решение, закрепить ли их в справочнике для всех страниц раздела «Банковские данные и аналитика».
- Термины управления данными, которых нет в справочнике по переводу, приняты единообразно для всех пяти частей: data steward — «стюард данных»; master data — «основные данные», master & reference data — «нормативно-справочные данные»; golden record — «золотая запись»; lineage — «происхождение данных» (документ — «описание происхождения данных»); attestation — «подтверждение» (не «аттестация»); validation exception — «отклонение, выявленное при валидации» (не «исключение»); CDE — «критически важные элементы данных (CDE)». Нужно решение, закрепить ли их в справочнике для всех страниц раздела «Банковские данные и аналитика».

## banking-data-analytics/market-data

- «Bloomberg Economics» is flagged by the scan as Latin; it is a brand name and kept.
- Vendor feed rendered «поток данных поставщика» (not «фид»); valuation/risk engine «система оценки», «система расчёта рисков»; the domestic exchange «национальная биржа»; market data team «группа рыночных данных»; risk desk «отдел контроля рыночных рисков». Confirm against the Bank's unit names.
- Benchmark rates rendered «эталонные (процентные) ставки», the domestic benchmark rate «национальная эталонная ставка», rate engine «система курсов и ставок», treasury desk «дилинговый отдел казначейства».
- SLA credits rendered «компенсации за нарушение SLA»; vintage of macro data «выпуск данных» (the map's vintage row covers loans only).
- Quant rendered «специалист по количественному анализу» / «группа количественного анализа»; bootstrapping «бутстрэппинг»; local-currency and major-currency «в национальной и основных иностранных валютах».

## banking-data-analytics/master-reference-data

- Термины страницы: master data — «основные данные», reference data — «справочные данные», заголовок страницы оставлен «Нормативно-справочные данные»; golden record — «золотая запись»; data steward — «стюард данных»; survivorship rules — «правила приоритета источников»; MDM hub — «MDM-система»; core banking — «автоматизированная банковская система (АБС)». В справочнике этих строк нет; нужно решение, вносить ли их.
- Data lineage передан как «происхождение данных» (lineage link — «связь происхождения данных»): строка traceable to запрещает «прослеживаемость до»; в справочнике отдельной строки lineage нет.
- Data governance team / council — «подразделение управления данными» / «совет по управлению данными»; ticket — «заявка на исправление».
- Data catalog & stewardship — «Каталог данных и работа стюардов» (не «стюардство»); approved pricing schedule — «утверждённые тарифы»; profitability attribution — «атрибуция доходности».

## banking-data-analytics/regulatory-data

- Terms not in the translation map, used consistently across all three parts: data lineage = «происхождение данных»; data residency = «размещение данных» (localization = «локализация данных»); CDE = «ключевые элементы данных (CDE)»; data steward = «ответственный за данные» (other Russian catalog pages still use «стюард данных»); regulatory validation rules = «контрольные соотношения». Propose them for the map or choose others.
- Terms not in the translation map, used consistently across all three parts: data lineage = «происхождение данных»; data residency = «размещение данных» (localization = «локализация данных»); CDE = «ключевые элементы данных (CDE)»; data steward = «ответственный за данные» (other Russian catalog pages still use «стюард данных»); regulatory validation rules = «контрольные соотношения». Propose them for the map or choose others.
- Three reporting roles kept distinct: regulatory reporting manager = «менеджер по регуляторной отчётности»; regulatory reporting lead = «руководитель группы регуляторной отчётности»; Head of Regulatory Reporting = «руководитель подразделения регуляторной отчётности». Confirm against the Bank's staff schedule.
- Terms not in the translation map, used consistently across all three parts: data lineage = «происхождение данных»; data residency = «размещение данных» (localization = «локализация данных»); CDE = «ключевые элементы данных (CDE)»; data steward = «ответственный за данные» (other Russian catalog pages still use «стюард данных»); regulatory validation rules = «контрольные соотношения». Propose them for the map or choose others.
- Source issue: the card with the URN slug regulatory-reporting-pack-assembly is titled «Regulatory Change Data Impact Assessment». Its content largely duplicates the next card, regulatory-change-data-gap-assessment. The English edition may need a fix.

## banking-data-analytics/risk-position-data

- Термины не из справочника, выбраны для всей страницы: desk — «торговое подразделение» (не «деск»); risk officer — «риск-менеджер»; risk governance team — «подразделение по методологии и контролю рисков»; risk operations team — «группа операционного сопровождения рисков»; risk engine — «система расчёта рисков». Нужно подтвердить или заменить на штатные наименования Банка.
- Greeks переданы как «греки» в кавычках, при первом упоминании — «чувствительности («греки»)»; IMA и SA написаны полностью («подход на основе внутренних моделей», «стандартизированный подход») без латинских сокращений, так как их нет в списке допустимых.
- risk technology team — «группа IT-сопровождения риск-систем»; peak intraday exposure — «пиковая внутридневная потребность в ликвидности»; LCR и NSFR — «коэффициент покрытия ликвидности», «коэффициент чистого стабильного фондирования» (общие базельские формы, без наименований конкретного регулятора). Нужно подтвердить.
- Risk Committee передан как «комитет по рискам», board Risk Committee — «комитет Совета директоров по рискам»; если в Банке это один орган, наименования нужно свести.

## banking-data-analytics/transaction-data

- Terms not in the translation map, chosen for this page and kept across all three parts: payment rail = «платёжный канал»; merchant = «торгово-сервисное предприятие (ТСП)», MCC = «код категории ТСП (MCC)»; enrichment pipeline = «конвейер обогащения»; lineage = «происхождение данных»; reconciliation break = «расхождение при сверке»; payment reference = «назначение платежа»; chargeback = «чарджбэк». Owner may wish to add them to the map.
- The national card scheme and domestic interbank payment systems are left unnamed («национальная карточная система», «национальные межбанковские платёжные системы»), as in the English; the old Russian names (KASE, MOEX, КазПочта, Мир) were removed.
- «within N months of go-live» is rendered as «в течение первых 12 месяцев после запуска» for running targets and «не позднее N дней/месяцев с даты запуска» for one-off milestones (map row within N days).
- Terms not in the translation map, chosen for this page and kept across all three parts: payment rail = «платёжный канал»; merchant = «торгово-сервисное предприятие (ТСП)», MCC = «код категории ТСП (MCC)»; enrichment pipeline = «конвейер обогащения»; lineage = «происхождение данных»; reconciliation break = «расхождение при сверке»; payment reference = «назначение платежа»; chargeback = «чарджбэк». Owner may wish to add them to the map.
- The national card scheme and domestic interbank payment systems are left unnamed («национальная карточная система», «национальные межбанковские платёжные системы»), as in the English; the old Russian names (KASE, MOEX, КазПочта, Мир) were removed.
- STR is rendered «сообщение о подозрительной операции (сделке)»; AML investigation team = «подразделение расследований ПОД/ФТ», investigator = «сотрудник, ведущий расследование».
- Terms not in the translation map, chosen for this page and kept across all three parts: payment rail = «платёжный канал»; merchant = «торгово-сервисное предприятие (ТСП)», MCC = «код категории ТСП (MCC)»; enrichment pipeline = «конвейер обогащения»; lineage = «происхождение данных»; reconciliation break = «расхождение при сверке»; payment reference = «назначение платежа»; chargeback = «чарджбэк». Owner may wish to add them to the map.
- The national card scheme and domestic interbank payment systems are left unnamed («национальная карточная система», «национальные межбанковские платёжные системы»), as in the English; the old Russian names (KASE, MOEX, КазПочта, Мир) were removed.
- AML typologies: layering = «расслоение», structuring = «дробление операций», pass-through = «быстрый транзит средств».

## customer-channels

- 1431, 1463, 1475: CCO here is read as Chief Customer Officer and rendered «директор по работе с клиентами». Translation map section 3 sets CCO = «директор по комплаенсу», which does not fit the customer-segment context. Owner to confirm the reading and whether the map needs a context row for CCO.
- Head of Channels is rendered «руководитель по каналам», following the old Russian edition. The map has no row for this role.
- Navigation labels for sub-pages translated by other parts (for example 252 «Физические отделения», 568 «Подсказки операторам и пошаговое решение вопросов», 609 «Планирование персонала», 363 «Цифровое оформление клиентов») must match the page titles those parts chose. Check them at assembly.

## customer-channels/atms-self-service

- Role names chosen here and used throughout both parts; there is no row for them in the map: ATM operations team/manager → «служба эксплуатации банкоматов» / «руководитель службы эксплуатации банкоматов»; fraud operations team → «подразделение по противодействию мошенничеству»; field service provider → «сервисная организация»; Head of Self-Service → «руководитель направления самообслуживания». Confirm, or align with the Bank's staff titles.
- Cash replenishment is rendered as «пополнение банкоматов наличными», and armored carrier work as «инкассация» / «инкассаторы». The old text used «инкассация» for both.
- 'push notification' is rendered as «уведомление в мобильном приложении», which keeps the text free of Latin; «push-уведомление» would be the usual alternative.
- Same role names as part 1, plus: cash logistics team/manager → «служба кассовой логистики» / «руководитель службы кассовой логистики»; cash carrier supervisor → «руководитель инкассаторской службы».
- cash recycler → «банкомат с рециркуляцией наличных», multi-function kiosk → «многофункциональный терминал», hurdle rate → «минимальная требуемая доходность»; none of these is in the map.

## customer-channels/channel-cycles

- Lenses Analyze/Optimize/Automate/Enrich (flow pages) rendered «Анализ», «Оптимизация», «Автоматизация», «Накопление знаний», as in the old edition; the brief's lens list covers only the five-lens set. Confirm for all flow pages.
- Head of Channels rendered «руководитель блока каналов»; channel teams as descriptive units («подразделение управления каналами», «группа финансового анализа каналов», «рабочая группа по обзору каналов»). Confirm against the Bank's structure.
- The «approved adjustment playbook» rendered «утверждённый перечень типовых корректирующих мер»: the map's playbook row («практика») covers AICC material only.
- Go-live rendered «ввод в эксплуатацию»; stage label Triage rendered «Оценка» (title: «Оценка критичности, масштаба и порядка эскалации»).
- Governance committee rendered «управляющий комитет» per the map's governance row; here it is the committee that approves channel plans. Confirm.
- Channel rebalancing rendered «перераспределение между каналами»; channel mix «структура каналов»; digital deflection «перевод операций в цифровые каналы».
- Channel evolution rendered «развитие каналов» (not «эволюция»); stage label Sunset rendered «Закрытие формата» to keep the label to two words.
- Coordinated deployment board (s75, part 4) and governance committees follow the map («борд», «управляющий комитет»).
- Distribution investment committee rendered «инвестиционный комитет по каналам продаж и обслуживания»; Board-level committee «комитет Совета директоров, к компетенции которого относятся инвестиции в каналы». Confirm the Bank's actual committee names.

## customer-channels/contact-center

- IVR containment rate rendered «уровень самообслуживания в IVR» rather than «удержание», because «удержание» would clash with putting a caller on hold («режим ожидания») on the same page; confirm.
- Coaching rendered «коучинг», «сессия коучинга» (the established loanword in Russian contact centres); confirm it is acceptable in the formal register, or name an alternative such as «наставничество».
- Team names rendered «операционная группа контакт-центра», «группа сопровождения IVR», «группа проектирования IVR», «группа контроля качества», «менеджер по контролю качества», «подразделение комплаенса»; confirm against the Bank's actual unit names.
- Contact-center supervisor rendered «руководитель смены контакт-центра» rather than the loanword «супервайзер»; confirm the Bank's job title.
- Workforce management rendered «планирование персонала» (section title and «группа планирования персонала»); confirm.
- Head of Complaints / complaint handler rendered «руководитель подразделения по работе с жалобами» / «специалист по работе с жалобами»; confirm against the Bank's unit names.
- Head of Complaints rendered «руководитель подразделения по работе с жалобами», consistent with part 2; confirm the actual title.

## customer-channels/digital-channels

- Head of Digital rendered as «руководитель по цифровым каналам» (the old text mixed it with «руководитель цифрового направления»); confirm against the Bank's staff list.
- Digital operations team rendered as «операционная команда цифровых каналов»; KYC operations team as «подразделение KYC». Confirm the Bank's unit names.
- Following the map row onboarding (клиенты), «онбординг» was replaced with «цифровое оформление клиентов». Deflection is rendered descriptively as «перевод обращений в цифровые каналы» / «доля обращений, урегулированных в цифровом канале».
- Digital adoption rendered as «использование цифровых каналов» (rate: «уровень использования цифровых каналов»; segment penetration: «доля цифровых клиентов по сегментам»). The old text used «цифровое принятие». Consider adding a map row.
- Next-best-action rendered as «наилучшее следующее действие»; consent scope as «рамки согласия»; offer fatigue as «усталость от предложений». None of these is in the translation map.

## customer-channels/partner-api-channels

- Settled terms for this page, not in the map: third-party provider = «сторонний поставщик услуг»; consent framework = «порядок получения согласий»; audit trail = «аудиторский след»; API governance team/committee = «подразделение/комитет по управлению API»; exception (compliance) = «отклонение»; go-live = «ввод в эксплуатацию»; revenue ledger = «книга учёта доходов». Owner to decide whether any belong in the map.
- Terms are the same as in part 1. Head of API Products = «руководитель по API-продуктам»; Head of Partner Channels = «руководитель партнёрских каналов». The map has no rows for these roles.

## customer-channels/physical-branches

- Page name kept as «Физические отделения» (matches the existing breadcrumb and nav label); «Отделения» or «Сеть отделений» would read more naturally if the parent page changes too.
- Role names chosen without a map entry: Head of Branches — «руководитель сети отделений»; Head of Network Planning — «руководитель планирования сети»; regional manager — «региональный управляющий»; branch manager — «управляющий отделением»; compliance team — «служба комплаенс-контроля». Confirm against the Bank's staff list.
- Financial inclusion «regulatory credit» rendered as «регуляторный зачёт за финансовую доступность»; financial inclusion — «финансовая доступность».
- Cash terms without a map entry: cash replenishment — «подкрепление (отделений) наличными»; treasury operations — «подразделение казначейских операций», Head of Treasury Operations — «руководитель казначейских операций»; armored carrier — «инкассаторская служба»; idle cash — «неработающие наличные».
- The old Russian of card branch-operations-intelligence (keys 1242–1330) described a performance pack; it was discarded and rewritten from the English (queue and staffing brief).

## customer-channels/relationship-management

- 188 (l3-section__title): «Управление портфелем клиентского менеджера» replaces the old abbreviation КМ; the area page customer-channels still links this section as «Управление портфелем КМ» and should match.
- 506, 518: the English says 'under-resourced books with capacity for additional client assignments', which contradicts 494 (under-resourced books create service gaps). Rendered as «недозагруженные портфели, которые могут принять дополнительных клиентов»; the English source may need correcting.
- 94: 'the regulator's conduct requirements' rendered as «требования регулятора к добросовестному поведению на рынке»; 'suitability' throughout as «оценка соответствия продукта потребностям клиента». Neither is in the translation map; worth settling for the whole catalog.
- 'coaching' rendered as «коучинг» (cyrillic borrowing) and 'coaching conversation' as «беседа о развитии навыков»; not in the translation map, worth settling for the whole catalog.

## customer-market-intelligence

- CCO in the Customer & Commercial Metrics Digest card (1123–1191) is the Chief Commercial Officer by context, so it is rendered «коммерческий директор». The map row for CCO gives «директор по комплаенсу» (Chief Compliance Officer), which does not fit here; a map row for the commercial sense may be needed.
- Card-link labels of pages outside this part were reworded where the old text was wrong or clumsy: «Доля рынка по регионам» (old «Географическая доля рынка»), «Измерение доли кошелька» (old «Измерение доли рынка», a mistranslation), «Рост доли кошелька» (old «Рост доли рынка»), «Сравнение продуктов с банками-аналогами», «Признаки в характере обращений», «Жалобы на недобросовестные практики», «Применение сегментации». The target pages' titles must use the same names.
- «Customer lifetime value» kept as «Долгосрочная ценность клиента» (old form) for consistency with the CLV page; «пожизненная ценность клиента» is the other common Russian form.

## customer-market-intelligence/brand-reputation

- Brand equity rendered «капитал бренда», brand recall «узнаваемость бренда», peer set «группа банков-аналогов», brief «справка»; confirm for the catalog.
- Unit names are generic and need checking against the Bank's structure: «служба коммуникаций», «служба клиентского опыта», «маркетинговая служба», «служба комплаенс-контроля», «подразделение по правовым вопросам» (map row legal), «подразделение по обеспечению непрерывности деятельности».
- «Regulatory communication volume» rendered «объём переписки с регулятором» (two-way correspondence, so «регулятор» rather than «надзорный орган»).
- Conduct risk / conduct supervision rendered «поведенческий риск» / «поведенческий надзор»; regulator-referred complaints «жалобы, поступившие через регулятора». Confirm as catalog-wide forms.
- Regulator-notification draft rendered «проект уведомления надзорного органа» (the Bank notifies), per map row regulator.

## customer-market-intelligence/customer-lifetime-value

- Page name kept «Долгосрочная ценность клиента» to match existing navigation; the more common banking term is «пожизненная ценность клиента». Owner to choose one form for all pages.
- Origination vintage rendered «поколение привлечения» (map row vintage), explained at first use in the Cohort-level CLV section; tenure «срок обслуживания» (map row tenure).
- CLV and LTV treated as feminine (agreeing with «ценность»).
- Segments rendered «массовый розничный сегмент», «формирующийся состоятельный сегмент» (emerging affluent), «микробизнес» (SME micro), «основной сегмент МСБ» (SME core); confirm against the Bank's segment names.
- Core banking rendered «автоматизированная банковская система (АБС)».

## customer-market-intelligence/customer-segmentation

- Section names chosen here are reused as card-link labels on customer-market-intelligence/index: «Сегментация по ценности» (old «Ценностная сегментация»), «Сегментация по потребностям» (old «Сегментация на основе потребностей»), «Сегментация по уровням риска» (old «…по рисковым ярусам»), «Сопоставление сегментов и продуктов», «Отслеживание миграции между сегментами». Confirm these as the settled names.
- «tier» rendered as «уровень» (уровень ценности, уровень риска, ценовой уровень) throughout, never «тир»/«ярус»; «affluent» as «состоятельные клиенты» per the map (emerging-affluent = «сегмент формирующихся состоятельных клиентов»).
- Card 1524: the old Russian said 5–7 days; the English says one to two analyst days; the English was followed.
- «conduct-risk profile» (2054) rendered as «профиль поведенческого риска»; the map has no row for conduct risk.

## customer-market-intelligence/intelligence-cycles

- Метки проблем цикла Analyze, Optimize, Automate, Enrich переданы как «Анализ», «Оптимизация», «Автоматизация», «Накопление знаний» — так же, как на других страницах циклов; в списке аспектов брифа их нет. Нужно подтвердить для всех страниц циклов.
- Sandbox в названии сценария «Segmentation Model Calibration Sandbox» передан по справочнику: «Зона контролируемого тестирования для калибровки модели сегментации». Здесь речь идёт об аналитической среде для сравнения вариантов модели, а не о регуляторной зоне; нужно решить, допустимо ли в этом значении другое название (например, «Сравнение вариантов калибровки модели сегментации»).
- Слово governance в составе governance approval, governance pack и governance committees передано по объекту: «утверждение комитетами», «пакет документов на утверждение», «комитет по управлению данными». Brief передан как «справка», retention playbook — как «методика удержания» (не «практика», поскольку это не материал AICC). Эти формы используются во всех четырёх частях страницы.
- Метки проблем цикла Analyze, Optimize, Automate, Enrich переданы как «Анализ», «Оптимизация», «Автоматизация», «Накопление знаний» — так же, как на других страницах циклов; в списке аспектов брифа их нет. Нужно подтвердить для всех страниц циклов.
- Competitive intelligence передано как «конкурентная разведка», brief — как «справка о конкурентах», ExCo — как «Правление»; regulatory portals — «сайты регулятора».
- Response protocol (порядок реагирования на угрозы бренду) передан как «порядок реагирования», а не «протокол»: по справочнику «протокол» в банковской практике — документ о заседании. Head of Communications — «руководитель службы коммуникаций»; core banking — «автоматизированная банковская система».
- CEO office передан как «аппарат председателя Правления» по строке Chief Executive Officer справочника.

## customer-market-intelligence/market-share-positioning

- «pricing committee» передан как «тарифный комитет»: подтвердить наименование комитета в Банке.
- «digital challengers» переданы как «цифровые банки-челленджеры» (кириллическое заимствование); альтернатива — «цифровые банки».
- Сегменты: retail mass — «массовый розничный сегмент», emerging affluent — «клиенты с растущим достатком», SME micro — «микробизнес», SME core — «основной сегмент МСБ»; сверить с сегментацией Банка.
- IR раскрыто как «руководство по стратегии и по работе с инвесторами (IR)»; enforcement actions — «меры воздействия».
- «distribution leadership» передано как «руководство по развитию сети продаж»; уточнить наименование подразделения в Банке.

## customer-market-intelligence/retention-churn

- save rate — «доля удержанных клиентов», save program — «программа удержания», intervention — «мера удержания», cohort brief — «рекомендации по когортам», core banking — «автоматизированная банковская система (АБС)»; формы общие для обеих частей страницы.
- Сегменты (emerging affluent и др.) переданы так же, как на странице о доле рынка; сверить с сегментацией Банка.
- Ключ 2016: в английском «contacted within 5 business days» не указано, от какой даты; передано как «в срок до пяти рабочих дней» без добавления точки отсчёта.
- «conduct-supervision requirements» переданы как «надзор за соблюдением прав потребителей финансовых услуг».

## customer-market-intelligence/voice-of-customer

- VoC rendered «голос клиента» throughout (abbreviation VoC not used); CX rendered «клиентский опыт» per the map.
- "VoC governance meeting" and "CX governance committee" both rendered as one body, «управляющий комитет по клиентскому опыту» (map: governance committee → «управляющий комитет»); confirm they are the same body at the Bank.
- Customer complaint escalation to the regulator (customer referral) kept as «регулятор»; the Bank's own reporting rendered «отчётность для надзорного органа».
- "Conduct supervision" rendered «поведенческий надзор»; confirm the term.
- Same governance-body rendering as part 1: «управляющий комитет (по клиентскому опыту)».
- Regulatory-exposure tiers rendered «обязательный ответ, рекомендательный, только коммерческий».

## customer-market-intelligence/wallet-share

- Primary/secondary bank rendered «основной/дополнительный банк»; section title «Доля клиентов, для которых Банк основной».
- CLV rendered «долгосрочная ценность клиента (CLV)», matching the Russian page name of customer-lifetime-value; core banking rendered «автоматизированная банковская система (АБС)»; SME «МСБ».
- Next-best-offer rendered «следующее лучшее предложение»; confirm against the Bank's CRM vocabulary.
- "Targeting brief" rendered «подборка клиентов» (title «Подборка клиентов с высокой долей конкурентов»).

## finance-treasury

- Navigation labels for sections of other pages (ALM, liquidity, performance, accounting, regulatory reporting, tax, Finance Cycles) were written here without their pages' Russian titles; they must be aligned with whatever those parts settle. FP&A and capital-management labels match their pages.
- ALM rendered «управление активами и пассивами» (map); «Finance governance» / «Finance Cycles» rendered «Управление финансами» / «Циклы управления финансами» following the pattern «Управление каналами» / «Циклы управления каналами».
- L2 (catalog level) rendered «направления второго уровня (L2)» at first use on a card, then «направления (L2)». Confirm whether readers should see L2 at all.
- «every value stream» rendered «каждый операционный и клиентский поток» after the catalog page names, avoiding the protected term value stream; «Local prudential returns» rendered «Национальная пруденциальная отчётность».

## finance-treasury/capital-management

- Lens column label kept as «Аспект», as on the other Russian pages; the brief names the lenses but not the column label.
- Pillar 1/2 rendered «Компонент 1/2» with «(Pillar 2)» at first use in each section; confirm this Basel rendering for the whole catalog.
- Finance, Risk, Capital Management teams rendered «финансовый блок», «блок управления рисками», «подразделение управления капиталом»; confirm against the Bank's actual unit names.
- Term windows («within N business days») follow map row 309 («не позднее N рабочих дней с даты …»), not the brief's example «в течение пяти рабочих дней».
- AT1 and Tier 2 kept in Latin where they appear together (brief allows it in lists with AT1); elsewhere Tier 1 is «капитал первого уровня».
- Pro forma rendered «проформа-значения нормативов»; syndicate banks rendered «банки — организаторы выпуска».

## finance-treasury/finance-cycles

- Terms not in the translation map, chosen for this page: FTP rate curve «кривая трансфертных ставок»; exception commentary (LCR/NSFR) «пояснения к отклонениям»; Contingency Funding Plan «план финансирования в кризисной ситуации»; funding maturity cliff «пики погашения фондирования»; ALM officer «специалист по управлению активами и пассивами»; ALM model «модель управления активами и пассивами» (ALM is not on the Latin allow-list). Confirm or set map rows.
- Liquidity stage labels set here and reused in part 5: «Прогнозирование», «Стресс-тестирование», «Планирование», «Отчётность», «Корректировка».
- Close cycle: reconciliation exception rendered «расхождение»; sub-ledger «аналитический учёт»; Controllers team «подразделение финансового контроля»; Financial Controller «финансовый контролёр»; close manager «руководитель процесса закрытия»; cut-off «отсечка». Regulatory cycle: validation exception «нарушение правил валидации»; Head of Regulatory Reporting «руководитель подразделения регуляторной отчётности». None of these is in the map; confirm.
- Stage labels set here and reused in part 5: close «Отсечка», «Сверка», «Корректировка», «Закрытие», «Отчётность»; regulatory «Агрегирование», «Валидация», «Представление», «Сверка», «Аудит и запросы».
- ALM stage 3 label kept as «Решение» to match part 1, although map row 199 reserves bare «решение» for the AICC term Solution; the owner may prefer «Выбор мер» or «Управленческое решение» on both the diagram (part 1, key 992) and here (s28).
- FRAs rendered «соглашения о будущей процентной ставке» without the abbreviation, which is not on the Latin allow-list.
- Regulatory own funds rendered «регуляторный капитал (собственные средства)»; production pipeline «промышленный конвейер подготовки отчётности»; upstream systems «предшествующие системы» (mirror of the map row downstream «последующие системы»). Confirm.

## finance-treasury/fpa

- Page title rendered «Финансовое планирование и анализ» (FP&A kept for the team in running text); the top page card title and breadcrumb use the same form.
- FTP curve rendered «кривая трансфертного ценообразования (FTP)», then «кривая FTP»; deposit beta rendered «бета-коэффициент депозитов»; NIM always «чистая процентная маржа» per the map, although NIM is on the scan allow-list.
- BU rendered «бизнес-подразделение»; Finance «финансовый блок»; Capital Management «подразделение управления капиталом», as on the capital-management model page.
- «CFO Scenario Sandbox» rendered «Среда сценарного анализа для финансового директора», not the map's «зона контролируемого тестирования»: here sandbox means an exploratory modelling tool, not a controlled test environment. Confirm.
- ALCO action items rendered «поручения» (map row actions); CFO's office «служба финансового директора», as on the model page.

## risk-control

- Key 548: ERMC is not on the allowed Latin list, so it is written as «комитет по управлению рисками»: «Цикл отчётности о рисках (комитет по управлению рисками и Совет директоров)». risk-control__risk-cycles.3 (not yet written) should use the same form.
- Key 978: «Model inventory & governance» is rendered as «Реестр моделей и система управления и контроля»; the model-risk page (not yet written) should use the same section title.
- RAF and SMA/SA/IMA are written in Russian («система риск-аппетита», «стандартизированный подход», «подход на основе внутренних моделей») because they are not on the allowed Latin list.
- Outside this part: risk-control__compliance-financial-crime.1 key 58 has the breadcrumb «Риски и контроль»; every other page has «Риск и контроль».

## risk-control/climate-esg-risk

- Team names rendered as units: sustainability team → «подразделение устойчивого развития», credit/climate risk team → «подразделение кредитных/климатических рисков»; confirm against the Bank's actual unit names.
- NGFS scenario names rendered «Текущая политика», «Определяемые на национальном уровне вклады», «Нулевые нетто-выбросы к 2050 году», «Упорядоченный переход», «Неупорядоченный переход», «Мир-теплица»; PCAF expanded as «Партнёрство по углеродному учёту для финансовых организаций». Confirm these renderings for the catalog.
- Pillar 3 rendered «Компонент 3 (Pillar 3)»; ICAAP, TCFD, ISSB and NGFS expanded at first use on the page.
- Adoption windows («within 12 months of go-live») rendered «не позднее чем через 12 месяцев после запуска»; cycle deadlines follow map row 309 («не позднее пяти рабочих дней с даты …»).
- Same choices as part 1 (unit names, NGFS scenario names, deadlines). «carbon exposure» rendered «подверженность углеродному риску» in titles; confirm.

## risk-control/compliance-financial-crime

- 968: the English says «A Suspicious Transaction Report (STR) — called a suspicious transaction report in some jurisdictions —», which is tautological (left over from the SAR→STR replacement). The parenthetical was omitted in Russian; the English source should be corrected.
- Roles not in the translation map, chosen for this page: AML compliance officer → «ответственный сотрудник по ПОД/ФТ»; AML supervisor → «руководитель группы ПОД/ФТ»; AML program manager → «руководитель программы ПОД/ФТ»; compliance officer → «сотрудник службы комплаенса»; Head of Compliance → «руководитель службы комплаенса»; General Counsel → «директор по правовым вопросам»; conduct risk → «поведенческий риск» (as in brand-reputation); AML alert → «сигнал»; mule network → «сети дропов». Owner may want these added to the map.
- 2132: CAMELS kept in Latin as the name of an international supervisory rating framework; scan flags it as not on the allow list.
- 2214/2226/2238: RAG kept in Latin in parentheses after «база знаний … с поиском и генерацией ответов»; confirm the Russian rendering.
- Sanctions compliance officer → «сотрудник по санкционному контролю»; examination/examiner → «надзорная проверка»/«проверяющие»; regulatory complaint escalation → «передача регулятору». Not in the map; owner may want to settle them.

## risk-control/internal-audit

- "Audit manager" is rendered «руководитель проверки» (part 1 has no settled form for it); please confirm or name the Bank's job title.

## risk-control/liquidity-risk

- The abbreviation CFP is not used: «план экстренного фондирования» throughout, following the finance-treasury/liquidity-management page; CFP triggers are «условия (индикаторы) срабатывания плана».
- Roles not in the map: Head of Treasury → «руководитель казначейства»; treasury risk officer/team → «специалист/группа по рискам казначейства»; treasury operations → «подразделение казначейских операций». Please confirm against the Bank's structure.
- "Go-live" is rendered «после ввода в эксплуатацию» as in internal-audit part 1; other pages use «с даты запуска». The map has no row for it.
- Same role and go-live choices as part 1 of this page.

## risk-control/market-risk

- Terms not in the translation map, used consistently across both parts: desk → «торговое подразделение» (as on the risk-position-data pages); Market Risk Officer → «риск-менеджер по рыночному риску»; backtesting exception → «пробой (VaR)»; Market Risk Committee → «комитет по рыночному риску»; trading book → «торговая книга». Candidates for the map.
- Internal Models Approach rendered «подход на основе внутренних моделей» without the abbreviation IMA, which is not on the Latin allow-list.
- Same unmapped terms as part 1 (торговое подразделение, комитет по рыночному риску, риск-менеджер по рыночному риску).

## risk-control/model-risk

- scan.py flags «SR 11-7» in key 94 as a hyphenated range; it is the document name and is kept.
- Chief Model Risk Officer → «руководитель подразделения по управлению модельным риском» and model-risk guidance → «рекомендации по управлению модельным риском», following the credit-risk page; Model Risk Committee → «комитет по модельному риску». Not in the map; candidates for it.
- CSI dropped as an abbreviation (not on the allow-list): «индекс стабильности характеристик».
- The Bank's AI register (AI governance cards) is rendered «реестр AI-систем», not the AICC term «реестр AI-решений» (map row AI Registry). Decide whether the catalog scenario should name the AICC registry.
- EU Artificial Intelligence Act rendered «Регламент ЕС об искусственном интеллекте».
- Role names not in the map: compliance officer → «сотрудник по комплаенсу»; incident manager → «ответственный за управление инцидентами»; third-party risk manager → «ответственный за риски поставщиков»; complaint handler → «сотрудник по работе с жалобами».

## risk-control/operational-risk

- near-miss передан как «инцидент без потерь» (определение дано в разделе «События с потерями и инциденты без потерь»); loss event — «событие с потерями». В справочнике строк нет; нужно подтверждение формы.
- AMA (Advanced Measurement Approach) оставлено латиницей в скобках после «продвинутый подход к измерению» (строки 94, 192, 242); сокращения нет в списке допустимой латиницы.
- exit plan передан как «план выхода» с пояснением «(прекращения работы с поставщиком)» при первом упоминании на карточке; TPRM lead — «руководитель направления TPRM».
- Хлебная крошка Risk & Control оставлена как «Риск и контроль» — по действующему наименованию области на портале.
- BCM и DR переданы по-русски без латинских сокращений («обеспечение непрерывности деятельности», «аварийное восстановление»); BCP вводится как «план обеспечения непрерывности деятельности (BCP)» и далее сокращается.
- BCP: полная форма «план обеспечения непрерывности деятельности (BCP)» при первом упоминании на карточке, далее — «BCP»; BCM team — «команда по обеспечению непрерывности деятельности», BCM lead — «руководитель по обеспечению непрерывности деятельности», DR program — «программа аварийного восстановления». Нужно подтверждение, допустимо ли сокращение BCP в тексте.

## risk-control/risk-cycles

- ERMC and BRC are not in the translation map. Rendered as «комитет по управлению рисками при Правлении» (short: «комитет по управлению рисками») and «комитет Совета директоров по рискам»; full board as «Совет директоров в полном составе». Please confirm; the flow-item__name in risk-control.1 (key 548, 'Risk reporting cycle (ERMC & board)') should match the title used here: «Цикл отчётности о рисках (комитет по управлению рисками и Совет директоров)».
- Risk pack / pre-read rendered as «пакет материалов о рисках» (short «пакет о рисках») and «материалы к заседанию комитета»; soft breach kept as «мягкое нарушение», following part 2.
- Risk-reporting stage 'Validate' rendered as «Сверка данных» (not «Проверка», reserved by the map for the AICC term).
- SR 11-7 kept as a named international reference (scan flags '11-7' as a hyphen range; false positive).
- Stage label 'Retire' rendered as «Вывод из эксплуатации» (three words; no natural two-word form). Model owners rendered as «ответственные за модели» to avoid «владелец», per the map row 'is the owner of'.

## shared-banking-capabilities

- Key 201: the English sub-group label reads 'Limit & line management' over the scorecard and underwriter links, the same as key 231, while the credit-decisioning page names that tab 'Application underwriting'. Rendered as the English says («Управление лимитами и кредитными линиями»), which duplicates the label; the English source likely needs «Андеррайтинг заявок».
- Credit decisioning card title follows its own page («Принятие кредитных решений»); the home page (_root) still links it as «Кредитный анализ и принятие решений» and should be aligned.
- 'Capability' is rendered «общебанковские возможности» (settled page name) and «направление» for a single capability; the map's general row for capability discourages «возможность». Confirm.
- 'Board operations committee' rendered «комитет Совета директоров по операционной деятельности»; confirm against the Bank's actual committee name.

## shared-banking-capabilities/capability-cycles

- Flow title «Vendor & sourcing review cycle» rendered as «Цикл проверки поставщиков и стратегии закупок»; the navigation label flow-item__name (key 460) in part shared-banking-capabilities.1 should use the same wording.
- Vendor onboarding rendered as «подключение поставщика» (stage label «Подключение»); the translation map has onboarding rows only for systems and clients. Sourcing team rendered as «подразделение по работе с поставщиками»; redline summary as «сводка правок».
- Vendor-cycle stage labels («Оценка», «Переговоры», «Подключение», «Мониторинг», «Продление или выход») follow part 3; the other three cycles keep the labels already set in parts 1–2 (investment cycle stage 5 = «Сопровождение», improvement cycle stage 5 = «Закрепление»).

## shared-banking-capabilities/customer-servicing

- Conduct risk rendered as «поведенческий риск» (as on the Compliance page) and unfair practices as «недобросовестные практики»; the translation map has no rows for either. Support ticket rendered as «заявка в службу поддержки».

## shared-banking-capabilities/pricing-profitability

- RAROC hurdle rendered «пороговое значение RAROC», front-book pricing «цены новых выдач», cost-to-serve «стоимость обслуживания», benchmark «ориентир»; NIM written in full («чистая процентная маржа»), as map row NII/NIM gives no abbreviation.
- Board exception approval for below-hurdle pricing rendered «согласие Совета директоров на отступление от порогового значения»; confirm this is not confused with the AICC term «отступление от требований».

## shared-banking-capabilities/transaction-processing

- Page name follows the root card link «Обработка операций и расчёты» (not «Обработка платежей и расчёты»).
- Terms chosen here, not in the translation map: payment rail → «платёжный канал»; exception → «исключение»; investigator → «специалист по расследованиям» (old «следователь» dropped as a law-enforcement word); STP → «сквозная обработка (STP)»; merchant → «торгово-сервисное предприятие (ТСП)», as in the transaction-data pages.
- Terms chosen here, not in the translation map: mule account → «счёт дропа» (as in risk-control__compliance-financial-crime); cash-management service → «услуга управления денежными средствами»; payment repair → «исправление платежей»; central bank digital currency → «цифровая валюта центрального банка»; head of payments → «руководитель платёжного направления».
- 1190: the English "used for ≥90% of payment investigations opened within 12 months of go-live" is read as a deadline (≥90% coverage within 12 months), not as a count of investigations opened in that window.

## strategic-initiatives

- Stage-gate rendered as «поэтапный отбор», gate as «контрольный рубеж» (to keep it apart from milestone = «контрольная точка»); the map has no row. Flow label 548 «Цикл поэтапного отбора инноваций» must match the title chosen on strategic-initiatives__change-cycles, which another writer handles.
- General Counsel rendered «директор по правовым вопросам», following risk-control parts; the map has no row for it.
- Card links 267–336, 379–448, 606–664, 707–776, 937–1006 name sections of the M&A, programs, partnerships, ecosystem and ESG pages written by others; align them with those section titles (e.g. 954 «Отчётность по выбросам охватов 1–3», 407 «Управляющий комитет программы»).
- Investment committee (IC) rendered «инвестиционный комитет»; no map row.

## strategic-initiatives/change-cycles

- Partner onboarding is rendered as «подключение партнёра». Map section 3 covers onboarding only for software (заведение в систему) and clients (оформление клиентов). Is a row needed for partners?
- KYB is rendered as «надлежащая проверка партнёра (KYB)», by analogy with CDD → «надлежащая проверка клиента». The map has no KYB row.
- The M&A regulatory filing (an application for approval) is rendered as «пакет документов для надзорного органа». The map row filing → «представление отчётности регулятору» covers periodic reporting and does not fit an application for approval.
- The Operate stage label is «Сопровождение»; the old «Операционная деятельность» was too long for the diagram.
- RAG status is rendered as «цветовой статус», with «(красная, жёлтая, зелёная зона)» at first use. The map has only amber/red → «жёлтая зона; красная зона»; a RAG row may be needed.
- Stage-gate is rendered as «поэтапный отбор» (cycle «Цикл поэтапного отбора инноваций») and gate as «рубеж». The map has no row for either.
- Scope 1/2/3 emissions are rendered as «выбросы охвата 1, 2 и 3 (Scope 1, 2, 3)», then «охват 3». The map has no row.
- ESG framework (TCFD, ISSB, GRI) is rendered as «стандарт»; framework-to-metric mapping as «сопоставление требований стандартов с показателями». The map has no row.

## strategic-initiatives/ecosystem-platform-strategy

- BigTech передан как «крупные технологические компании» (латиница не оставлена); fintech challengers — «новые финтех-игроки»; ecosystem topology — «структура экосистемы»; brief — «обзор». Подтвердите формы.
- Соседняя страница customer-channels__partner-api-channels пишет «аудиторский след»; бриф требует «аудиторский трейл», здесь применён «аудиторский трейл» — соседнюю страницу стоит выровнять.
- Adoption S-curve передана описательно: «кривая роста числа участников (медленный старт, ускорение, насыщение)», чтобы не оставлять латинскую S; при желании можно вернуть «S-образная кривая».
- Take rate везде — «комиссия платформы» по справочнику (строка take rate).
- Onboarding разработчиков и партнёров передан по справочнику как «заведение на платформу» (строка onboarding — программное обеспечение, сервис); соседняя страница partner-api-channels использует «подключение» сторонних поставщиков — нужно решение, какую форму держать в каталоге.
- Platform governance team — «команда управления и контроля платформы»; governance reports — «контрольные отчёты».

## strategic-initiatives/esg-commitments

- CSO: на этой странице CSO означает Chief Sustainability Officer, а не Chief Strategy Officer. Карта (раздел 3, строка COO; CDO; …; CSO) даёт «директор по стратегии», однако здесь написано «директор по устойчивому развитию». Нужно решение: добавить в карту строку CSO (устойчивое развитие) или ввести иную форму.
- Scope 1/2/3: написано «охват 1, 2 и 3» (термин русского перевода GHG Protocol), латиница Scope 1/2/3 дана один раз в скобках во вводном абзаце страницы. Если корпус предпочитает латиницу Scope, формы нужно заменить на всей странице.
- External assurance: передано как «внешнее заверение» и «организация, проводящая внешнее заверение». В карте строки нет; строка assurance (внутренний аудит) к этой ситуации не относится.
- Строки 114 и 396: scan.py отмечает «C» в обозначении «°C». Это единица измерения, а не слово, поэтому она оставлена.
- CSO передан как «директор по устойчивому развитию» (см. заметку к части 1): карта для CSO даёт «директор по стратегии».
- ESG KPI передано как «ключевые ESG-показатели»; KPI латиницей сохранено только в сочетании «финансовые KPI».

## strategic-initiatives/innovation-portfolio

- Innovation board rendered «комитет по инновациям», sponsor «куратор (идеи, программы, эксперимента)», adoption curve «кривая освоения»; no map rows. «Куратор» is also the AICC role name «куратор AICC»; confirm no clash is felt.
- Chief Innovation Officer (CIO) rendered «директор по инновациям» without the Latin abbreviation, which would read as Chief Information Officer.
- Keys 1640 and 2028 (okr-cycle): the old Russian stated different targets (+20%, +15%); the new text follows the English only.

## strategic-initiatives/ma

- Page name, breadcrumb and title kept as «M&A» (Latin allowed); the intent opens with «Слияния и поглощения (M&A)». Confirm whether the parent page card should read «M&A» too.
- Due diligence follows map row 239: «комплексная проверка (due diligence)» at first use (page intent), then «комплексная проверка»; DD in titles rendered the same way.
- Terms not in the map, chosen for the whole page: workstream — «направление работ» / «направление комплексной проверки»; data room — «виртуальная комната данных», then «комната данных»; IC — «инвестиционный комитет»; enforcement action — «меры воздействия»; brief — «записка»; HR — «служба персонала». Confirm.
- «Valuation Scenario Sandbox» rendered «Зона контролируемого тестирования сценариев оценки» to follow the brief and map row 248; this is a valuation modelling tool, not a regulatory sandbox, so the term reads oddly. An alternative is «Среда сценарного моделирования оценки». Owner to decide.
- Integration steering committee rendered «управляющий комитет по интеграции»; ExCo «Правление»; IR team «служба по связям с инвесторами»; earn-out and term sheet per map rows 256 and 241; DCF expanded at first use per card.

## strategic-initiatives/major-transformation-programs

- Program-management terms not in the translation map, used consistently across all three parts: workstream — «рабочий поток»; milestone — «контрольная точка»; scope — «объём работ»; brief — «записка»; stakeholder — «заинтересованные стороны»; PMO — «проектный офис». Confirm or set in the map.
- NPV/IRR rendered as «чистая приведённая стоимость (NPV)» and «внутренняя норма доходности (IRR)», Latin kept after first use. The Russian abbreviations ЧПС/ВНД were deliberately avoided: in the map, ВНД means «внутренние нормативные документы».
- conditions precedent rendered as «отлагательные условия» (legal-banking term); confirm.
- Steering Governance Longitudinal Record rendered as «Сквозной реестр решений управляющего комитета», following the map row Living record → «реестр» to avoid «запись».
- "within 12 months of go-live" rendered as «не позднее 12 месяцев с даты запуска», as on earlier pages; English leaves open whether go-live is the AI agent's or the program's.
- adoption (of change) rendered as «освоение»; cohort as «группа»; fortnightly as «раз в две недели».

## strategic-initiatives/strategic-partnerships

- Role names not in the translation map: CSO is «директор по стратегии» (map row); 'partnership governance lead/team' is rendered «руководитель / подразделение по управлению партнёрствами»; Legal is «юридическая служба». Confirm if the Bank uses other titles.
- BATNA (card partnership-negotiation-position-modeling) is not on the allowed Latin list; rendered descriptively as «наилучшая альтернатива на случай срыва переговоров» without the abbreviation. Confirm or allow «(BATNA)».

## strategic-portfolio

- Sub-concerns (the six areas of the Strategic Banking Portfolio) rendered as «области портфеля», following the brief's «область» for one area of the map; the term is not in the translation map.
- Narrative rendered by object: board/executive narrative → «обзор», «записка»; equity story / investor narrative → «инвестиционная история», «история для инвесторов». «Нарратив» not used.
- Executive committee (EC) rendered as «Правление» (map row ExCo); board → «Совет директоров».
- CEO/CFO portfolio-modeling sandbox rendered with the settled «зона контролируемого тестирования», although it is a what-if modeling environment rather than a regulatory sandbox; «среда моделирования» would read more naturally if the owner allows it.
- Operating model «capabilities, value streams» (card posture-vs-execution) rendered «ключевые возможности, цепочки создания ценности», as in shared-banking-capabilities; the map's Latin «value stream» is an AICC lean term and was not applied here.
- Hub card-link labels must match the titles the sub-pages receive (e.g. «Способность принимать риск» for Risk capacity, «Инвестиции и страхование» for Wealth & insurance, «Особые сегменты и состоятельные клиенты» for Specialty & wealth); check against the sibling parts.
- Same choices as part 1: «области портфеля» for sub-concerns, «Правление» for EC; «engine» → «программный компонент сценарного анализа» (map row engine).

## strategic-portfolio/capital-allocation

- 'CFO office' rendered «служба финансового директора»; 'Executive Committee' rendered «Правление» per the brief; 'sub-ledger' rendered «данные аналитического учёта».
- TCR is not on the allowed Latin list; rendered «норматив совокупного капитала» throughout without the abbreviation (incl. card titles). bps rendered «б. п.». Confirm or allow «(TCR)».

## strategic-portfolio/geographic-footprint

- «Rationalization» (branch network) rendered «оптимизация» throughout, not «рационализация»; «distribution committee» rendered «комитет по каналам продаж» and «network strategy team» «команда по стратегии развития сети». The map has no rows for these; confirm.
- Section title 187 «Domestic markets» rendered in the singular «Внутренний рынок» (one home market); the old page had «Внутренние рынки». Confirm, since the page navigation may show this label.
- «Expansion» rendered «расширение» throughout (titles «Стратегические цели расширения», «рынки для расширения»), not «экспансия» as on the old page; confirm.

## strategic-portfolio/product-portfolio

- Product head rendered «руководитель продукта» to keep «направление» for Domains; ALCO pricing committee → «ценовой комитет при КУАП».
- Lending what-if sandbox rendered «зона контролируемого тестирования» (see the note on part strategic-portfolio.1).
- Islamic-product variants and murabaha kept, as the English keeps them conditionally («если Банк их предлагает»); AUM rendered «активы под управлением» (not on the allowed Latin list).
- Product governance committee → «продуктовый комитет» (part 1) and product management committee → «комитет по управлению продуктами» kept distinct, following the English; merge them if the Bank has one body.

## strategic-portfolio/risk-appetite

- RAS rendered as the document name «Заявление о риск-аппетите» (capitalised, as in the charter) with no Latin abbreviation; «risk tolerance levels» rendered «уровни толерантности к риску»; «risk capacity» rendered «способность (Банка) принимать риск», not the calque «риск-ёмкость». The map has no rows for these; confirm before they spread to other pages.
- «Executive committee» rendered «Правление» per the map (ExCo); «board» rendered «Совет директоров».
- Card 1242 «Tolerance Recalibration Scenario Sandbox»: «sandbox» rendered «зона контролируемого тестирования» as the brief requires, although here it means an internal modelling environment for the CRO, not a regulatory sandbox. «Среда сценарного моделирования» would fit the meaning better; confirm.
- Key 2132: RORAC kept in Latin with an expansion («доходность капитала, скорректированного на риск (RORAC)») as a risk metric alongside RAROC and EVA; scan flags it because RORAC is not on the allowed list. Confirm or add it to the list.
- «Recovery planning» rendered «планирование восстановления финансовой устойчивости» (title 2018 «Автоматизация сценариев восстановления финансовой устойчивости»); confirm the term.

## strategic-portfolio/steering-cycles

- Page name kept as «Управленческие циклы» to match the root navigation label already written; «Циклы стратегического управления» would render «Steering cycles» more exactly, but all labels would have to change together.
- «capability owners» rendered «руководители функциональных областей» (the brief bars «направление» for a capability; «business line» is «направление бизнеса», as on the model page). Confirm.
- «supervisory review» rendered «надзорная оценка» throughout the page (the old text had SREP). Confirm the term.
- «implementation mandate / implementation brief» rendered «задание на реализацию» (old text: «операционный мандат»); used consistently in parts 2 and 4. Confirm.
- «legal approval / legal review» rendered «правовая экспертиза» and «legal team» as «юристы»; «General Counsel» (part 4) as «руководитель юридической службы». Confirm against the Bank's own titles.
- Key s55: «franchise risk» rendered «риск для ценности бизнеса Банка»; no settled form in the map.

## strategic-portfolio/strategic-priorities

- Chief customer officer is rendered «директор по работе с клиентами», following earlier catalog usage; the map has no row for it. «Директор по клиентскому опыту» would match the CX row better and needs a decision.
- Operational excellence is rendered «операционная эффективность», and stage-gate is rendered «рубеж отбора» as in strategic-initiatives. The map has no rows for either.
- Go/no-go is rendered «продолжить или прекратить», and graduated programs are rendered «программы, переведённые в промышленную эксплуатацию». The map has no rows for either.

## strategic-portfolio/target-markets-segments

- Section title 576 stays «Private banking» in Latin under the map row private banking; scan.py flags the capitalised word. Confirm that a Latin section title is acceptable.
- AUM and RAS are written out in Russian («активы под управлением», «заявление о риск-аппетите») because scan.py does not allow them in Latin.
- Tier 1/Tier 2 corporate and public-sector clients are rendered «клиенты первой (второй) категории» so they are not confused with capital tiers.

## value-streams

- Метки этапов: «Funding» (Кредитование) передано как «Выдача» вместо прежнего «Финансирование»; остальные метки этапов сохранены в прежнем виде. Данные этапов (stage N label, части 8–9) пишет другой исполнитель — их нужно согласовать с этими метками.
- Payment/dispute «exceptions» переданы как «нештатные ситуации/платежи/случаи», чтобы не путать с термином AICC «отступление» и словом «исключение».
- Stage label Close rendered «Закрытие» (the old Russian had «Измерение»); Adjust «Корректировка».
- Метки этапов банкострахования изменены: «Identify trigger» — «Выявление повода» (было «Идентификация триггера»), «Position offer» — «Предложение» (было «Позиционирование предложения»), «Sell & onboard» — «Продажа и оформление» (было «Продажа и онбординг», по справочнику onboarding клиентов = оформление). Согласовать с данными этапов в частях 8–9.
- «Affluent and high-net-worth clients» передано как «состоятельные клиенты»: по справочнику и affluent, и HNW — «состоятельные клиенты», различие сегментов теряется. Нужна ли отдельная форма для HNW?
- Investment policy statement (IPS) передано как «инвестиционная декларация»; head of wealth — «руководитель подразделения по управлению благосостоянием».
- Метки этапов казначейства: «Execute» — «Исполнение» (было ошибочное «Исполнить»), «Report & narrate» — «Отчётность и пояснения» (было «Отчётность и нарратив»). Согласовать с данными этапов в частях 8–9.
- Leverage ratio передан как «норматив финансового рычага»; maturity ladder — «шкала сроков погашения».
- Метка этапа «Onboard» (Жизненный цикл клиента) — «Оформление» вместо прежнего «Онбординг» (справочник: onboarding клиентов = оформление). «Exit» оставлен «Выход». Согласовать с данными этапов в части 9.
- Payment factory передано как «платёжный центр Банка»; FX — «валютные операции» по справочнику, название потока «Валютные операции и международные платежи» как в каталоге.
- Stage label Mitigate rendered «Снижение рисков» (two words; bare «Снижение» is ambiguous). The button with the same label in parts 1–4 must match: please align.
- Lens Enrich rendered «Накопление знаний», as in the 31 existing catalog pages; the brief's lens list (Аналитика, Автоматизация, Поддержка, Оптимизация, Новые возможности) has no row for the verb-form lenses Analyze/Optimize/Automate/Enrich.
- AML investigator rendered «аналитик» (as in risk-control__compliance-financial-crime), AML alert rendered «сигнал»; the old text used «следователь», which suggests law enforcement.
- IIA kept in Latin as the name of an international standard-setting body (scan flags it).
- Stage label Close (financial cycle) rendered «Закрытие»; the old Russian had «Измерение», which was a mistranslation.
- Stage labels chosen here must match the buttons in parts 1–4: Account opening «Открытие счёта», Fund «Пополнение», Transact «Операции», Funding (lending) «Финансирование» (the stage is loan disbursement; «Выдача» would be more exact), Discover «Выявление», Implement «Исполнение», Identify trigger «Выявление события», Position offer «Подача предложения», Sell & onboard «Продажа и оформление», Plan funding «Планирование фондирования», Report & narrate «Отчётность и пояснения».
- Chief Accounting Officer rendered «главный бухгалтер» and Credit Risk (function) «подразделение кредитных рисков»; neither is in the translation map.
- Stage labels to align with buttons in parts 1–4: Capture order «Приём поручения», Price & quote «Котировка», Settle «Расчёты», Onboard «Оформление» (map row onboarding (клиенты)), Exit «Уход», Mitigate «Снижение», Execute (internal audit) «Проведение», Remediate «Устранение».
- SWIFT message types MT199/MT299 kept in Latin script as standard names.

