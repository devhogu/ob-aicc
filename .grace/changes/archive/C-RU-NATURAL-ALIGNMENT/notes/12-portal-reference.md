# Notes: batch 12 (portal/content/ru/reference, 40 files)

Common changes in all regulation and resource pages: template headings made nouns («Общие сведения», «Содержание» / «Публикации», «Сфера применения», «Порядок и цели использования», «Меры предосторожности»); footer now says that the requirements applicable to the Bank are determined by «представители контрольных функций по комплаенсу и правовым вопросам» (was «Представители контрольных функций комплаенса и юридической функции подтверждают применимость»); AICC terms lowercased; «Workflow Эксперимента» → «рабочий процесс эксперимента»; «AI agents» → «AI-агенты»; «проверка безопасности» → «тестирование защищённости»; «оспаривание» → «пересмотр решения»; «Отраслевая база знаний» link labels → «Стандарты и методологии» (the page title).

## portal/content/ru/reference/overview.md

- QUESTION — H1 «Справочные материалы» → «Справочник», to match the section label in authored.json («Справочник»). Alternative: keep «Справочные материалы».
- QUESTION — 3.1 "Registration with a work address": rendered «Регистрироваться с рабочим адресом» (kept literal); alternative «с рабочим адресом электронной почты».

## portal/content/ru/reference/industry-body-of-knowledge.md

- QUESTION — page title "Standards and frameworks": «Стандарты и подходы» → «Стандарты и методологии» ("framework" = «методология» throughout the batch). No other Russian file quoted the old title.
- QUESTION — row "Lean portfolio management practice": accepted form of the terminology reference used («эффективное управление портфелем»), the SAFe competency name kept in Latin. Same as batch 02's question; alternative «бережливое управление портфелем».
- QUESTION — row ISO/IEC 42001: label uses the GOST title «Искусственный интеллект. Система менеджмента» (ГОСТ Р ИСО/МЭК 42001-2024, listed in the translation map, section 6).
- DRIFT — row Internal control: old «независимая оценка с предоставлением уверенности» (rejected form; adds "assurance" twice); now «независимая оценка». Row OWASP: «Проверка безопасности» (the AICC term "Check") → «тестирование защищённости».
- ENGLISH? — intro says "Each source has a page under Reference", but ISO/IEC 23894, ISO/IEC 22989, the SAFe row and the IT service management and internal control rows have no page of their own.

## portal/content/ru/reference/regulators-and-acts.md

- QUESTION — EU acts named by official Russian forms: «Регламент ЕС об искусственном интеллекте (AI Act)» (was «Акт Европейского союза…»), «Общий регламент ЕС по защите данных (GDPR)», «Регламент ЕС о цифровой операционной устойчивости (DORA)»; Kyrgyz AML law named after the official title «о противодействии … легализации (отмыванию) преступных доходов и финансированию террористической деятельности». The H1 of each page matches its link label.

## portal/content/ru/reference/research-and-insight.md

- QUESTION — 1.1 "their view becomes expectation": «позиция … становится основой требований и рекомендаций надзорных органов» (map row "regulatory expectations"); alternative «становится ожиданием надзорных органов».

## portal/content/ru/reference/learning-and-open-resources.md

- DRIFT — OWASP row: "red teaming" was rendered «проверкам методом моделирования атак»; now the accepted form «red-team стресс-тестирование».
- DRIFT — NIST row: "designing the controls of a use" was «контрольных процедур для применения» (unclear); now «для конкретного случая применения AI».

## portal/content/ru/reference/regulations/iso-iec-ai-standards.md

- DRIFT — section 6: the English list has an unlinked item "Governance and oversight"; the old Russian omitted it. Restored as «Управление и надзор».
- QUESTION — Status row: added the Russian national designations ГОСТ Р ИСО/МЭК 42001-2024 and ГОСТ Р 71476-2024 for ISO/IEC 42001 and 22989 (both listed in the translation map, section 6). Remove if the page should name only the international standards.

## portal/content/ru/reference/regulations/kg-personal-information-law.md

- DRIFT — 5.1: "the provider check on where data is processed and kept" was rendered «проверка мест обработки и хранения данных Поставщиком» (the check done by the provider); now «проверка поставщика в части мест обработки и хранения данных».
- QUESTION — "holders" rendered «держатели массивов персональных данных» (term of the Kyrgyz law).

## portal/content/ru/reference/regulations/kg-aml-body.md

- QUESTION — "reporting entities" rendered «лица, обязанные представлять сведения» (descriptive; the exact term of the Kyrgyz law was not verified).
- QUESTION — 4.1 and 5.1 "human decision": «принятие решения работником», «в каждом случае решает работник» (to keep «решение» for the AICC term).

## portal/content/ru/reference/regulations/council-of-europe-ai-convention.md

- QUESTION — "contestability" rendered «возможность пересмотра решений» (map row contest). The Statement of Intent 6.6 heading still reads «… возможность оспаривания»; the two should be aligned.

## portal/content/ru/reference/regulations/eu-ai-act.md

- QUESTION — "deployers" rendered «организации, применяющие систему»; "European AI Office" rendered «Европейское бюро по искусственному интеллекту».

## portal/content/ru/reference/regulations/lean-portfolio-management.md

- QUESTION — H1 «Практика бережливого управления портфелем» → «Практика эффективного управления портфелем» (accepted form, see industry-body-of-knowledge). The three SAFe dimensions use the wording of the terminology reference («стратегия и финансирование инвестиций», «гибкое управление портфельными операциями», «бережливое руководство»).
- DRIFT — intro: "a lean business case" was «краткий business case»; now «бережливый бизнес-кейс» (as in the terminology reference).

## portal/content/ru/reference/regulations/nist-ai-rmf.md

- DRIFT — 2.1: "safe" was «безопасность для людей и окружающей среды» (addition); "confabulation" was «вымышленные утверждения»; "information integrity" was «достоверность информации». Now «безопасность», «конфабуляция», «целостность информации».

## portal/content/ru/reference/regulations/oecd-ai-principles.md

- DRIFT — 4.1: "Where the Bank states its own principles, they should be recognizable" was an unconditional «Собственные принципы Банка должны быть узнаваемы»; now conditional and a recommendation («Если Банк формулирует собственные принципы, … следует …»).

## portal/content/ru/reference/resources/hugging-face.md

- QUESTION — "evaluation set" rendered «оценочный набор» (style sheet §4), not «тестовый набор данных» (older accepted form).

## portal/content/ru/reference/resources/imf-and-world-bank.md

- QUESTION — 4.1 "the Strategy and governance category use them": the category is not an actor in Russian; rendered «Руководитель AICC использует их, в том числе при оказании услуг категории «Стратегия и управление»».
- QUESTION — "Bali Fintech Agenda" rendered «Балийская повестка дня в области финансовых технологий» (was «Балийская программа»).

## portal/content/ru/reference/resources/mckinsey-and-quantumblack.md

- QUESTION — link label «business cases и сценарии» → «Бизнес-кейсы и сценарии» (service category name in the Business Model); the target page H1 still reads «Business cases и сценарии» (other batch).

## Link labels (several files)

- QUESTION — labels pointing to services/assessments-and-evaluations keep the target page's current title «Оценка и проверки», although the Business Model names the category «Оценка и экспертиза». Align when the services batch settles the title.
- ENGLISH? — several English pages label the link to industry-body-of-knowledge "Industry body of knowledge", while the page title is "Standards and frameworks". Russian labels use the page title.
