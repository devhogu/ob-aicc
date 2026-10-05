# Notes 11: portal/content/ru/portfolio and portal/content/ru/responsible-ai

Batch-wide choices (apply to every file below):

- QUESTION (all portfolio pages): PDCA step "Check" rendered «контроль» («планирование — выполнение — контроль — корректировка»), not «проверка», because STYLE §3 reserves bare «проверка» for the AICC Check. The PMM and Operating Model currently use «Проверка» in their PDCA diagrams; whoever rewrites them may want the same choice.
- QUESTION (all portfolio pages): "the decision after the MVP" written «управленческое решение после MVP» in prose and tables (STYLE §3, «решение» alone = Solution); in Mermaid gate labels the short «решение после MVP» is kept for space. Alternative: a fixed gate name in quotes.
- QUESTION (all portfolio pages): "gate" = «контрольная точка»; "decider" = «уполномоченное лицо»; "lead time" = «время выполнения» (accepted form of the terminology reference; the old text had «полное время выполнения»).
- QUESTION (all portfolio pages): "evidence" (that returns to the frame) = «фактические данные» (map, evidence as basis of decisions), not «свидетельства».

## portal/content/ru/portfolio/overview.md

- DRIFT 3.1: EN "rather than through a committee at the start and an audit at the end"; old RU «а не только через комитет…» added «только». Wrote «а не через комитет в начале и аудит в конце».

## portal/content/ru/portfolio/strategy-and-investment.md

- DRIFT 2.2: old RU dropped "It is no longer a negotiation over funds for one piece of work". Restored.
- DRIFT 1.1 and table: "sets them with the Board" was «совместно с Советом директоров» (map: rejected). Wrote «по согласованию с Советом директоров».
- QUESTION 5.1: "the findings of the year" — old RU «Выявленных отклонений года» (AICC term Finding). Chose general «выводов, сделанных за год» (map row findings, general). Alternative: «выявленных отклонений за год» if the term Finding is meant.

## portal/content/ru/portfolio/the-flow.md

- DRIFT table, Funnel row: EN "A function, the discovery work, or AICC proposes"; old RU kept the order but read as «работы по выявлению потребностей предлагают». Rewritten so the idea comes from a function, AICC, or discovery work.

## portal/content/ru/portfolio/the-lanes-and-the-front-door.md

- DRIFT 2.1 table "Normatives and processes", run-rate column: EN "a process drawing"; old RU «Workflow». Wrote «схема процесса».
- QUESTION category names: kept the Business Model names «Оценка и проверки» (Assessments and evaluations) and «Надзор» (Oversight) for consistency with the Business Model and the services pages, although bare «проверки» collides with the Check term and the map reserves «надзор» for supervisory authorities. Alternatives: «Оценка и экспертиза», «Мониторинг внедрённых решений». Changed «business cases и сценарии» to «Бизнес-кейсы и сценарии» and «Определение Категории риска» to lowercase per STYLE.
- QUESTION table 1 and 2.1: "engine" = «программный компонент» (map); "pipeline" = «конвейер обработки данных» (as in the Business Model) rather than the Latin accepted form "pipeline".

## portal/content/ru/portfolio/the-business-case-and-the-mvp.md

- DRIFT 2.1: "within their remit" was «в пределах полномочий»; wrote «в пределах своей компетенции» (map).

## portal/content/ru/portfolio/the-loops-and-governance.md

- DRIFT table 1, strategic row: "the AI Steering Committee advising" was «при консультации Управляющего комитета по AI»; wrote «с учётом рекомендаций Управляющего комитета по AI» (map; the Committee advises, the Executive Sponsor decides).
- QUESTION 4.1: "assurance loop" kept as «цикл подтверждения надлежащего функционирования» (Operating Model name), not «независимая оценка» (map row assurance applies to internal audit).

## portal/content/ru/portfolio/measures-and-tracking.md

- DRIFT intro: EN "A Portfolio that cannot say whether its Initiatives worked … is a list of hopes"; old RU turned it into an obligation («Портфель должен показывать»). Restored the statement.

## portal/content/ru/portfolio/measures-definitions-and-formulas.md

- ENGLISH? section 5, "First-time-right rate": "meet the Verify or the Review at the first attempt" — elsewhere the English says "the check or the validation"; "Verify"/"Review" look like leftover names. Translated literally as «проверку или рассмотрение».
- QUESTION section 3: measure "Adoption" = «Степень использования» (old «Внедрение», which collides with deployment); "Cycle" = «Цикл процесса»; "live review" = «обзор действующего решения».

## portal/content/ru/portfolio/roles-and-records.md

- DRIFT table 1: "conflicts between Domains" was «конфликтам между Доменами», "Client function" was «функция заказчика» (map: rejected). Wrote «разногласиям между доменами», «подразделение-заказчик».

## portal/content/ru/responsible-ai/understanding-ai-today.md

- DRIFT intro: old RU dropped "Artificial intelligence is not one thing". Restored.
- QUESTION title: «AI сегодня: основные понятия» (old «Современное понимание AI»); no other page links the title.

## portal/content/ru/responsible-ai/ai-terms-explained.md

- QUESTION: "evaluation set" = «оценочный набор» (STYLE term table) although the terminology reference gives «тестовый набор данных»; "assistant, copilot" = «ассистент, copilot» (accepted form; old «помощник»).
- DRIFT section 4, Validation row: "until the date it expires" was rendered as validation lasting «до истечения срока действия» as if part of the review period; rewritten so that the validation result is valid until its expiry date.

## portal/content/ru/responsible-ai/opportunities.md

- ENGLISH? 4.1: the sixth Strategic Priority is called "information technology operations"; the Statement of Intent 9.7 title is "Information technology operations and service lifecycle". Old RU used the full title; I followed the page («эксплуатация информационных технологий»).
- QUESTION: page titles referenced from other pages («Риски и трудности», «AI в финансовых технологиях и цифровом банкинге», «Что означает ответственный AI») kept unchanged because reference pages outside this batch link to them by name.

## portal/content/ru/responsible-ai/ai-in-fintech-and-digital-banking.md

- DRIFT 4.1: old RU dropped "did not write new rulebooks for AI". Restored.
- DRIFT 4 table, consumer protection row: "can contest a decision" was «оспорить решение» (map: rejected). Wrote «потребовать пересмотра решения».

## portal/content/ru/responsible-ai/risks-and-challenges.md

- DRIFT 4.2: heading "Ownership" was «Владение»; wrote «Ответственность» with «ответственный» for owner (map: is the owner of).
- DRIFT 2.3: "contracts that forbid training on it" was «запрещающим обучение на них» (map: rejected); wrote «запрещающим поставщику использовать эти данные для обучения моделей».

## portal/content/ru/responsible-ai/what-responsible-ai-means.md

- DRIFT 4.4: "audit assures" was «независимую оценку с предоставлением уверенности» (map: rejected); wrote «внутренний аудит проводит независимую оценку».
- DRIFT 2.1 table: "can reach a person and contest a decision" was «могут обратиться … и оспорить решение» (map: rejected forms); wrote «вправе обратиться … и потребовать пересмотра решения»; principle name aligned with the Statement of Intent 6.6 («возможность пересмотра решений»).
- DRIFT 3.2: old RU dropped "None of these is exotic". Restored.

## portal/content/ru/responsible-ai/how-the-bank-applies-it.md

- DRIFT 1.1: EN "accepts only a low level of risk of harm … and of loss or misuse"; old RU «Допускается только низкий риск» is equivalent, but wording aligned with AICC Charter 5.2 (risk-appetite statement).
- DRIFT 2.2: "at least Risk Tier 2" was «как минимум» (map); wrote «не ниже 2». 2.1 table: "each six months" was «каждые шесть месяцев» (map: rejected); wrote «не реже одного раза в шесть месяцев, а также при изменении»; tier 2 likewise «не реже одного раза в год, а также при изменении».
- DRIFT 4.1: "nobody overrides the stop" was «никто не отменяет» (map: rejected); wrote «такая остановка отмене не подлежит».
- DRIFT 6.1: "a major incident is reported … without waiting for the next report" was «не дожидаясь следующего отчёта»; wrote «незамедлительно, не дожидаясь очередного отчёта». "near miss" rendered «событие, при котором причинение вреда было предотвращено» (map).
- DRIFT 7.1 / 8: "open Exceptions" was «открытые Исключения»; "within their remit" was «в пределах полномочий»; "legal" was «юридической функции»; "sets the training" was «устанавливает обучение»; "Internal audit gives independent assurance" was «с предоставлением уверенности»; Board Committee "oversees AI" was «осуществляет надзор за AI». All replaced by the map forms.
- QUESTION 2.1: "the Contact of model risk" = «представитель контрольной функции по модельному риску».
