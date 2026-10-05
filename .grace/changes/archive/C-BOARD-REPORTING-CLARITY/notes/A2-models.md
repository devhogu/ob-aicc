# A2: Portfolio Management Model, Solution Lifecycle Model, AI Policy, Business Model, shared terminology, translation map

## charter/en/documents/portfolio-management-model.md

- ENGLISH-CHANGE: 3.1 table, Executive Sponsor row. Old: "issues the Quarterly Report to the Board Committee". New: "approves the Quarterly Report and decides whether to bring it to the Board Committee or the Board" (R2, R5).
- ENGLISH-CHANGE: 4.3. Old: "The plan confirms the Roadmap, the mix of Initiatives for the next Program Increment within the Envelopes." New: "The plan confirms the Roadmap and the mix of Initiatives …" (REPORT.md §4 missing "and").
- ENGLISH-CHANGE: 4.3. Old: "the Executive Sponsor adjusts the mix and reports to the Board Committee." New: "the Executive Sponsor adjusts the mix and approves the Quarterly Report, and may bring it to the Board Committee or the Board." (R1, R2).
- ENGLISH-CHANGE: Figure 2, Act node. Old: "continue, pivot, defer, or reject; report to the Board Committee". New: "continue, pivot, defer, or reject; approve the Quarterly Report". Topology unchanged.
- Kept: 2.1 "sets them with the Board" (strategy setting, not reporting).

## charter/en/documents/solution-lifecycle-model.md

- ENGLISH-CHANGE: 4.1. Old: "Each is ranked by value and urgency relative to effort". New: "Each item of the two backlogs is ranked …". This matches the existing Russian «Элементы бэклогов ранжируются».
- ENGLISH-CHANGE: 6.6. Old: "and Work Items are not tracked in the charter." New: "and Work Items are not tracked." "In the charter" referred to nothing (the working state lives in the Registry and later in Jira).
- ENGLISH-CHANGE: Figure 11, Plan node. Old: "support level, monitoring, Limits". New: "support level and monitoring". This matches 8.4, which names only the support level and the monitoring. Alert levels and cost limits stay where 3.7 of the AI Policy states them.
- QUESTION: portal/content/en/delivery/the-cadence.md 4.1 and portal/content/en/organization/how-the-organization-grows.md 1.1 still say "Work Items are not tracked in the charter". These are other workers' files; they should get the same fix.
- Kept: 8.2 "the Executive Sponsor presents it" (the yearly strategy Proposal goes to the yearly Steering under Operating Model 6.5, and the Bank decides). It is not a periodic Board report.

## charter/en/documents/ai-policy.md

- ENGLISH-CHANGE: 5.7. Old: "without waiting for the next report". New: "without waiting for any report". The escalation stays mandatory (R3). There is no periodic Board report to wait for any more.
- Kept: 2.4 unchanged. It requires Executive Sponsor approval of AI output published to the Board. That is a condition on whatever is published, not a reporting duty, so it already fits R2.

## charter/en/documents/business-model.md

- No Board or Board Committee reporting statement, so the English is unchanged. The Russian got only the term updates, and source_sha256 still matches.

## charter/en/shared-technology-terminology.md

- ENGLISH-CHANGE: 2.3. Old: "Examples include AI capabilities, an IT function, …". New: "Examples include the use of AI, an IT function, …". "AI capabilities" clashed with the protected Capability, and the translation map rejects «возможности AI». The Russian already used «применение AI».
- ENGLISH-CHANGE: value stream, Application. Added: "Value stream is the fixed name in all language versions and keeps its Latin spelling in each of them; a language version may explain it at its first use in a document."
- ENGLISH-CHANGE: workflow, Application. Old: "Workflow is the fixed name in all language versions." New: "… and keeps its Latin spelling in each of them." (REPORT.md §4 conflict resolved by the owner decision of 5 October 2026.)

## charter/ru/documents/portfolio-management-model.md

- The reporting sentences of 3.1, 4.3 and Figure 2 now match the new English. source_sha256 was refreshed.
- All 166 occurrences of Initiative and Initiatives now use «инициатива» in the right case, including the heading «Структура инициатив и точки контроля», «## 8. Инициатива, Capability и Feature», «шаблоном «Паспорт инициативы»» and the change-log text.
- 8.3: «рабочий элемент — подзадаче» became «Feature — отдельному типу задач Jira, а задача — подзадаче». I avoided «Feature — типу задачи» because задача now means Work Item.

## charter/ru/documents/solution-lifecycle-model.md

- The reporting and clarity sentences now match the new English: 6.6 «задачи не учитываются» and Figure 11 «уровень поддержки и мониторинг». 4.1 already matched. source_sha256 was refreshed.
- «рабочий элемент» became «задача» everywhere: in the 3.2 table row «Задача | Работа команды в составе Feature» (matching the Vocabulary article «Задача»), in Figures 1 and 2, in the 4.2 board table, in the 6.1 Day row, in 6.3 and in the feedback table.
- «рабочий процесс» became workflow in 1.3 (sentence rebuilt so that workflows is not the subject), 4.4 «условие workflow», 6.1 and 6.8 «workflow «Ритм работы»».
- QUESTION: in heading 3, 3.4 and the Figure 2 caption, the English says "the flow of value", not "value stream". Following the brief, «поток создания ценности» became «Value stream» (heading and caption) and «value stream (сквозная последовательность действий, …)» at its first use in the body (3.4). The alternative is a plain Russian phrase such as «движение ценности», if the owner wants the English wording followed literally.

## charter/ru/documents/ai-policy.md

- 5.7 now reads «не дожидаясь какого-либо отчёта». source_sha256 was refreshed.

## charter/ru/documents/business-model.md

- Initiative became «инициатива» in 27 places. 1.2 now reads «ход работ показан в workflows». The English is unchanged, so source_sha256 is unchanged.

## charter/ru/shared-technology-terminology.md

- 2.3 «выполнение workflow». The value stream and workflow rows now give the accepted forms value stream / workflow (мн. ч. workflows), Latin, lowercase, indeclinable and masculine; the value stream row keeps the Russian explanation in its definition. source_sha256 was refreshed.
- value stream is explained at its first use in the document, in the Lean Portfolio Management row: «value streams (сквозным последовательностям действий, …)».
- Work Item: the task, ticket and Epic / issue / sub-task rows now use «задача» or «задача команды (Work Item)». Where "work item" is generic (the 1.3 table, 2.11, class of service, Bug, DoR, the 1.6 change log) it became «элемент работы», so that the AICC Work Item («задача») stays distinct from the work-item hierarchy. I did not use «задача» there.
- Initiative has no row of its own in the terminology. It is defined in Vocabulary. The 11 occurrences in other rows now use «инициатива».
- QUESTION: the RU column (Russian equivalent) of the value stream and workflow rows still shows «поток создания ценности» and «рабочий процесс», as the other rows list Russian equivalents of Latin accepted forms (for example Feature | функция; фича). As a result, the scan reports one rejected form «поток создания ценности» in this file. Clear the RU cell if the owner wants no Russian equivalent shown.
- Section 4 heading: «Термины разработки, внедрения и workflow».

## charter/ru/translation-en-ru-map.md

- Version 0.4 · 5 October 2026, with a 0.4 change-log row.
- Rows replaced: the protected-names row (Initiative removed, Work Item → «задача», не: «рабочий элемент»), Initiative/initiative (Russian forms, не: «Initiative», «Initiatives», «паспорт Initiative», «постоянная Initiative»), value stream (Latin, explained at first use, не: «поток создания ценности», «поток ценности»), workflow (Latin, не: «рабочий процесс «…»», «рабочие процессы», «перечень рабочих процессов») and state names in running text («инициативы в работе»).
- Examples changed to «инициатива» in the benefit, defer, committed, serves, when X is completed, as clause N states and AICC term capitalized rows. The work flows row now refers to workflow.
- DRIFT (reporting rule): the examples of report to (the chain ended at the Board Committee), without waiting for the next report («очередного отчёта» implies a periodic report) and sent as («направляет его Комитету Совета директоров») stated the old periodic reporting. They now follow R1–R5: the chain ends at «управляющее совещание (куратор AICC)», «не дожидаясь какого-либо отчёта», and «решает, направлять ли его Комитету Совета директоров». This goes slightly beyond "keep everything else", but it follows the spec acceptance criterion.
- Note: the new rejected forms («Initiative», «Initiatives», «рабочие элементы», «поток создания ценности», «рабочие процессы») will now show up in the scan of other workers' files that still use the old forms.
