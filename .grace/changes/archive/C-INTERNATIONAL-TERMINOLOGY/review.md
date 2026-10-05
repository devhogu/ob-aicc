# International terminology alignment

Reviewed on 4 October 2026 against Shared Business and Technology Terminology edition 1.5 and Vocabulary and Style revision 3.3, in their respective languages.

The user authorized application of the agreed international terms in the Russian portal and alignment of both portal languages with both vocabularies. The changes are made in the corpus and maintained portal sources, then projected into HTML. No runtime translation layer was added.

## Naming decisions

- Fixed AI, IT and ICT abbreviations use Latin letters. AI agent / AI agents identifies the AI systems defined by the corpus. The adjective agentic retains the permitted Russian form агентный. A human contact-center agent and a monitoring/installation agent are distinct concepts and retain their appropriate names.
- Business case, workflow/workflows, value stream/value streams, WIP and WIP limit/WIP limits use the international forms in headings, prose, tables, navigation and diagrams. The Business Case stage retains its lifecycle meaning and transition rules. Related Russian agreement was adjusted after the noun substitutions.
- The shared reference explicitly records ordinary plural forms already used by the corpus. It retains all 71 accepted entries and the existing fixed / permitted-language / context-specific usage rules.
- Full Russian expansions in the shared reference's Russian-language-name column and explanatory definitions remain: their purpose is to explain the international names. PI/IP and MVP retain their defined full-name explanations and fixed abbreviations. No blanket replacement of permitted Russian terms such as Домен, Приёмка, Показатель or Проверка was made.
- Russian platform-component names use the accepted forms шлюз доступа к моделям, слой работы со знаниями and шлюз доступа к инструментам.
- Exact external document names remain where cited: the Kazakhstan law «Об искусственном интеллекте», the named AI ethics code, the EU AI Act and the Council of Europe convention. Generic descriptive references use AI. The rule does not authorize rewriting externally published titles or legal entity names.
- Product and company names retain their identity; routes, file paths, Record IDs, recorded dates and decision statuses are unchanged.

## Functional reconciliation

Both language editions now explicitly cover the Operating Model 4.4(d) business-acceptance exception where the AICC Lead is the Domain Owner, alongside the cases in Solution Lifecycle Model 7.3(c). Final Team acceptance is described at its existing times: before first deployment and before deployment of significant changes. The quality explanation gives the same actors and exceptions as the governing documents.

The delivery-record explanation now follows Operating Model 7: working state moves to Jira/Confluence at cutover, living Solution Definitions remain in the Portfolio, and Evidence records remain in the Registry. Registry Snapshots retain their stated timing and coverage.

The course glossary explains Assistant within its charter scope and the Evaluation set's Domain agreement, expected results and checks before use and after significant change. These are explanations of existing definitions, not new operational requirements.

## Projection corrections

The Statement of Intent's shortened Russian navigation title follows its updated full source title. Current test expectations follow the actual source naming.

The Business Case concept and stage previously shared one generated anchor and indistinguishable search links. The renderer and search now share the same vocabulary-entry identities: the concept keeps its existing anchor; a colliding stage receives a distinct stage anchor and a localized Stage/Стадия qualifier in search. A regression test failed for both languages before the fix and passed afterwards.

The whole-site terminology scan covers all 230 English and 230 Russian pages, including rendered diagram text and tooltip attributes. It found a business-case name split by a Mermaid line break; the source was corrected and rebuilt. Remaining matches are reviewed explanations, external titles or non-AI uses of agent.

The source-review JSON records files changed from the beginning of this task, preserving earlier and unrelated working-tree work. Verification results and artifact paths are recorded separately after the final gates.
