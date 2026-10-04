# Russian-language naming evidence

Reviewed 2026-10-04. This is implementation evidence, not a normative charter document.

All 71 existing entries were checked against their corpus meanings and the sources below. Sources establish actual usage or the underlying technical concept; they do not establish a measured percentage of industry acceptance. Names are selected for the concept in this corpus, rather than copied indiscriminately from machine-localized vendor prose. Existing English and Russian definitions and application rules are preserved.

The Russian-language column is explanatory for fixed international forms. It does not replace AI, IT, AI agents, workflow, FSM, DAG, KPI, SLA or protected product names where the Application column retains them. “Universal term” identifies the common entry; it does not make every English phrase mandatory.

Specific decisions:

- business case: use the established loanword бизнес-кейс. Microsoft's Russian finance scenario uses it for investment justification. Keep the distinction from the AICC Initiative Brief record.
- KPI: use ключевой показатель эффективности (результативности). The parenthetical keeps the meaning linked to achievement of objectives, as in the corpus; it does not restrict KPI to cost efficiency.
- RACI: use матрица распределения ответственности. The existing definition distinguishes execution from ultimate accountability; a source's simplified role translation does not override that distinction.
- lead time, cycle time and throughput: use the names in an actual Russian software vendor's methodology material. Existing corpus boundaries continue to define start/end events; duration includes waiting within those boundaries.
- WSJF: retain метод приоритизации WSJF, as the acronym is used in Russian vendor material. Do not invent an allegedly standard Russian expansion.
- ACL and PI/IP: the corpus's record prefix and planning periods are explicit local meanings. ACL's technical alternative is documented separately; IP is not translated as an Internet Protocol here.
- knowledge layer, model gateway, tool gateway and Platform guardrails: these are qualified AICC designations. External architecture documentation supports the component responsibilities, but does not establish the exact Russian phrase as a universal industry standard. Keep the existing corpus designations and label their scope.
- evaluation set: набор данных для оценки follows Microsoft terminology and covers cases and expected results. It is not automatically a holdout test set or a training set.
- fallback: резервный механизм is attested in Microsoft documentation; резервный сценарий expresses the corpus's process alternative, including manual operation.
- drift: retain дрейф with the affected subject; Russian Yandex security documentation uses data/model drift. Do not collapse it into an incident or a single quality measure.
- prompt injection: промпт-инъекция is used by Positive Technologies researchers. Keep внедрение инструкций as the explanatory corpus expression.
- open model: preserve the distinction between an open model and a specific open-source license; the name alone grants no rights.
- Brand names are repeated unchanged in the local column. AICC and O!Bank identities follow the corpus; no external website is used to redefine the organizational mandate or legal entity name.

## Entry evidence matrix

Source codes resolve below. AICC indicates the existing governing corpus, including its specific designations, rather than a claim of general industry acceptance.

| Universal term | Adopted Russian-language name | Evidence |
| --- | --- | --- |
| business case | бизнес-кейс | MS-CASE |
| business intelligence / customer intelligence | бизнес-аналитика / клиентская аналитика | YC-BI, SAS-CI |
| dashboard | дашборд; информационная панель | YC-DASH |
| ESG | экологические, социальные факторы и факторы корпоративного управления | CBR-ESG |
| HR | управление персоналом; кадровая функция | YP-MANAGEMENT |
| KPI | ключевой показатель эффективности (результативности) | ATL-KPI |
| KYC | «Знай своего клиента» | CBR-KYC |
| OKR | цели и ключевые результаты | YP-MANAGEMENT |
| RACI | матрица распределения ответственности | YP-MANAGEMENT |
| SOW | описание работ | IIBA |
| backlog | бэклог | YP-IT |
| code review | код-ревью; рецензирование кода | YP-REVIEW |
| cutover | переключение на новую систему | MS-CUTOVER |
| deployment | развёртывание | ATL-DEVOPS |
| Epic / issue / sub-task | эпик / задача / подзадача | ATL-EPIC, AICC |
| Kanban | канбан | ELMA-KANBAN |
| lead time / cycle time | время выполнения / время цикла | ELMA-KANBAN |
| MVP | минимально жизнеспособный продукт | YP-MANAGEMENT |
| PI / IP | Программный инкремент / Неделя инноваций и планирования — в корпусе AICC | AICC |
| production | промышленная среда; продакшн | YP-IT |
| release | релиз; в корпусе AICC — Выпуск | ATL-JIRA, AICC |
| root cause analysis | анализ первопричин | ATL-RCA |
| service desk | служба поддержки пользователей; сервис-деск | ITSM-SD |
| Service Management | управление услугами | ATL-SM |
| SLA | соглашение об уровне обслуживания | ATL-SLA |
| sprint / sprint backlog | спринт / бэклог спринта | SCRUM |
| story points / velocity | стори-пойнты / скорость команды | YP-POINTS |
| throughput | пропускная способность | ELMA-KANBAN |
| value stream | поток создания ценности | ATL-DEVOPS |
| WIP | незавершённая работа | ELMA-KANBAN, AICC |
| WIP limit | лимит незавершённой работы | ELMA-KANBAN, AICC |
| workflow | рабочий процесс; в поясняющих документах AICC — Схема процесса | ATL-JIRA, AICC |
| WSJF | метод приоритизации WSJF | KAITEN-WSJF |
| access control | управление доступом | YC-ACL |
| ACL | Контрольный лист приёмки — в корпусе AICC; список управления доступом — в техническом контексте | AICC, YC-ACL |
| agentic | агентный | YC-AGENTS |
| AI | искусственный интеллект | YC-AGENTS |
| AI agent / AI agents | ИИ-агент / ИИ-агенты | YC-AGENTS |
| audit trail | журнал аудита | MS-AUDIT |
| cloud | облако; облачная среда | AWS-CLOUD |
| DAG | ориентированный ациклический граф; направленный ациклический граф | YC-DAG |
| drift | дрейф данных, модели или её поведения — по контексту | YC-SECURITY |
| evaluation set | набор данных для оценки | MS-EVAL |
| fallback | резервный механизм; резервный сценарий | MS-FALLBACK, AICC |
| Finite State Machine / FSM | конечный автомат | YA-FSM |
| human oversight | контроль со стороны человека | UNESCO |
| ICT | информационно-коммуникационные технологии | ITU |
| IT | информационные технологии | YP-IT |
| knowledge base | база знаний | ATL-SM |
| knowledge layer | слой работы со знаниями — в корпусе AICC | AICC, YC-ARCH |
| language model | языковая модель | YC-AGENTS |
| lineage | происхождение данных и история их преобразований | MS-LINEAGE |
| logging | логирование; журналирование событий | YC-LOG |
| model gateway | шлюз доступа к моделям — в корпусе AICC | AICC, MS-GATEWAY |
| monitoring | мониторинг | YC-OBS |
| observability | наблюдаемость | YC-OBS |
| open model | открытая модель | YC-OPEN |
| pipeline | конвейер обработки | MS-PIPELINE |
| Platform guardrails | Защитные механизмы платформы — в корпусе AICC | AICC, YC-ARCH |
| prompt injection | промпт-инъекция; внедрение инструкций | PT-INJECTION, AICC |
| read-only | доступ только для чтения | YC-ACL |
| repository / protected main branch | репозиторий / защищённая основная ветвь | GH-BRANCH |
| retrieval | поиск и извлечение данных | YC-ARCH |
| tool gateway | шлюз доступа к инструментам — в корпусе AICC | AICC, MS-GATEWAY |
| AICC | Центр компетенций по AI (AICC) | AICC |
| Amazon CloudWatch / CloudWatch | Amazon CloudWatch / CloudWatch | AWS-CW |
| Amazon Web Services / AWS | Amazon Web Services / AWS | AWS-CLOUD |
| Atlassian | Atlassian | ATL-JIRA |
| Confluence | Confluence | ATL-JIRA |
| Jira | Jira | ATL-JIRA |
| O!Bank | O!Bank | AICC |

## Sources

- AICC: [Vocabulary and Style](../../../../charter/ru/documents/vocabulary.md), [Statement of Intent](../../../../charter/ru/documents/statement-of-intent.md), [Portfolio Management Model](../../../../charter/ru/documents/portfolio-management-model.md) and the entry's existing governing references. These establish the local meaning, not market prevalence.
- MS-CASE: [Microsoft finance scenario: business case](https://enablement.microsoft.com/ru-ru/scenario-library/finance/build-a-business-case/).
- YC-BI: [Yandex Cloud: Business Intelligence](https://yandex.cloud/ru/blog/bi-business-intelligence).
- SAS-CI: [SAS: Customer Intelligence and client analytics](https://www.sas.com/content/dam/SAS/ru_ru/doc/Events/old-presentations/2014/1_Alexey_Rundasov.pdf).
- YC-DASH: [Yandex Monitoring: dashboards](https://yandex.cloud/ru/docs/monitoring/operations/dashboard/create).
- CBR-ESG: [Bank of Russia: sustainable-finance terminology](https://cbr.ru/develop/ur/faq/). Naming evidence only; no claim that Russian regulation governs AICC.
- CBR-KYC: [Bank of Russia: KYC / Знай своего клиента](https://www.cbr.ru/press/event/?id=6837). Naming evidence only; the entry's Bank-specific requirements remain unchanged.
- YP-MANAGEMENT: [Yandex Practicum: management terminology](https://practicum.yandex.ru/production-anglicizm-glossary/management-courses-glossary).
- ATL-KPI: [Atlassian: incident metrics and key performance indicators](https://www.atlassian.com/ru/incident-management/kpis).
- IIBA: [IIBA BABOK v3 Russian glossary](https://production.iiba.org/globalassets/standards-and-resources/glossary/files/babok_guide_v3_glossary_russian.pdf), statement of work. The named record is not automatically an AICC Engagement Agreement.
- YP-IT: [Yandex Practicum: IT terminology](https://practicum.yandex.ru/blog/populyarnye-terminy-it-sfery/).
- YP-REVIEW: [Yandex Practicum: code review](https://practicum.yandex.ru/blog/chto-takoe-kod-review/).
- MS-CUTOVER: [Microsoft: migration and cutover](https://learn.microsoft.com/ru-ru/azure/postgresql/migrate/migration-service/tutorial-migration-service-iaas-online).
- ATL-DEVOPS: [Atlassian: DevOps, deployment and value streams](https://www.atlassian.com/ru/devops).
- ATL-EPIC: [Atlassian: epics, tasks and backlogs](https://wac-cdn.atlassian.com/ru/agile/tutorials/epics). AICC's actual issue mapping remains defined by the Portfolio Management Model.
- ELMA-KANBAN: [ELMA365: Kanban and flow metrics](https://elma365.com/ru/baza-znaniy/kanban-kanban/).
- ATL-JIRA: [Atlassian: Jira, workflows and related product names](https://www.atlassian.com/ru/software/jira). Also confirms Atlassian and Confluence spellings in Russian-language product material.
- ATL-RCA: [Atlassian: root cause analysis](https://www.atlassian.com/ru/work-management/project-management/root-cause-analysis).
- ITSM-SD: [ITSM 365: service desk](https://itsm365.com/product/outsource/client-service/). Spelling varies in vendor material; the formal function remains user support.
- ATL-SM: [Atlassian: service management and knowledge base](https://www.atlassian.com/ru/software/jira/templates/general-service-management).
- ATL-SLA: [Atlassian: service level agreements](https://wac-cdn-a.atlassian.com/ru/itsm/service-request-management/slas).
- SCRUM: [Scrum Guide, Russian 2020](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Russian.pdf), glossary on page 17. The guide retains international names in its body and lists Russian equivalents; this does not change AICC's calendar-month Iteration.
- YP-POINTS: [Yandex Practicum: story points and velocity](https://practicum.yandex.ru/blog/story-points-kak-ocenivat-zadachi-v-agile-i-scrum/).
- KAITEN-WSJF: [Kaiten: prioritisation models](https://kaiten.ru/blog/3-modieli-prioritizatsii-zadach/).
- YC-ACL: [Yandex Cloud: access control lists](https://yandex.cloud/ru/docs/cloud-desktop/concepts/acl) and [Object Storage permissions](https://yandex.cloud/ru/docs/storage/concepts/acl).
- YC-AGENTS: [Yandex Cloud: AI agents and agentic systems](https://yandex.cloud/ru/blog/ai-agents). Supports the agent terminology and the language-model context; does not override the AICC Agent/Assistant distinction.
- MS-AUDIT: [Microsoft: audit trail](https://learn.microsoft.com/ru-ru/windows-server/administration/windows-commands/netsh-winsock).
- AWS-CLOUD: [AWS: cloud computing](https://aws.amazon.com/ru/what-is-cloud-computing/).
- YC-DAG: [Yandex Cloud: directed acyclic graphs](https://yandex.cloud/ru/docs/data-proc/tutorials/airflow-automation). The vendor uses направленный; ориентированный is the equivalent mathematical wording already used by the corpus.
- YC-SECURITY: [Yandex Cloud: AI security standard](https://yandex.cloud/ru/docs/security/standard-ai/all), data/model drift and monitoring controls.
- MS-EVAL: [Microsoft: datasets for evaluation](https://learn.microsoft.com/ru-ru/azure/foundry/observability/how-to/traces-to-dataset).
- MS-FALLBACK: [Microsoft: fallback mechanism](https://learn.microsoft.com/ru-ru/entra/identity-platform/concept-native-authentication-web-fallback).
- YA-FSM: [Yandex Education: finite state machines](https://education.yandex.ru/handbook/flutter/article/sostoianie-chto-eto).
- UNESCO: [UNESCO: human oversight](https://www.unesco.org/ru/articles/globalnyy-dialog-po-voprosam-upravleniya-iskusstvennym-intellektom?hub=67098).
- ITU: [ITU-T Y.4904 Russian terminology](https://www.itu.int/rec/dologin_pub.asp?id=T-REC-Y.4904-201912-I%21%21PDF-R&lang=s&type=items), ICT abbreviation.
- YC-ARCH: [Yandex Cloud: secure AI architecture](https://yandex.cloud/ru/docs/security/standard-ai/secure-architecture), retrieval, source metadata and technical controls. The exact AICC component names are internal designations.
- MS-LINEAGE: [Microsoft Purview: data lineage](https://learn.microsoft.com/ru-ru/purview/data-gov-classic-lineage).
- YC-LOG: [Yandex Cloud: monitoring and logging](https://yandex.cloud/ru/docs/overview/concepts/monitoring-logging-tools).
- MS-GATEWAY: [Microsoft: AI Gateway concepts](https://learn.microsoft.com/ru-ru/azure/api-management/ai-gateway-overview), models, tools and controlled access; not evidence of an exact universal Russian name for two separate AICC components.
- YC-OBS: [Yandex Cloud: observability and monitoring](https://yandex.cloud/ru/docs/glossary/observability).
- YC-OPEN: [Yandex Cloud: open models](https://yandex.cloud/ru/blog/ai-review-2025).
- MS-PIPELINE: [Microsoft: pipeline definition](https://learn.microsoft.com/ru-ru/azure/devops/pipelines/yaml-schema/pipeline).
- PT-INJECTION: [Positive Technologies researchers: prompt injection](https://www.securitylab.ru/blog/company/pt/355867.php).
- GH-BRANCH: [GitHub: protected branches and repositories](https://docs.github.com/ru/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- AWS-CW: [AWS Russian CloudWatch product page](https://aws.amazon.com/ru/cloudwatch/).
