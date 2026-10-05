# Terminology research and drafting record

Retained on 4 October 2026 when the shared terminology reference was recast in formal institutional language. This is development evidence, not operative charter wording. Decision authority remains recorded in DR-2026-064. The following text preserves the prior assessment and scan history; its qualitative bands are not survey results.

## 2. How to read the selections

### Acceptance bands

The intended audience is AICC's business and technology practitioners. Familiarity within that audience matters more than familiarity among the general public.

| Band | Interpretation | Editorial treatment |
| --- | --- | --- |
| White — the requested 80%+ band | Strong candidate for a stable international name: an established acronym, a precise technical label, or a proper name | Recommend retaining the listed form across languages, within the stated scope |
| Gray — the requested 70–79% band | Recognizable in specialist use, but English, transliteration, and natural Russian wording coexist | Present the choice explicitly; do not assume that recognition makes English wording preferable |

These are qualitative editorial bands, not measured acceptance rates or survey results. The sources cited below establish identity and meaning, and sometimes illustrate usage; they do not establish a percentage of Russian speakers who prefer a term. A brand is preserved because it identifies a particular entity, independently of how many readers know it.

**Owner-selected** is a naming decision, separate from the band. AI, AI agent / AI agents, IT, workflow, Finite State Machine / FSM, and DAG are owner-selected. The request also establishes preservation of company and product names, illustrated by AWS and CloudWatch. A gray assessment of workflow does not undo that explicit selection.

The owner's clarification extends this principle to common business and delivery terms. KPI, SLA, WIP, WIP limit, business case, and value stream are selected for inclusion and use with their proper meanings. Admission to the vocabulary does not make two different concepts interchangeable or establish an operational arrangement by naming it.

**Observed** means that the term or the stated variant occurs in the 39 English charter files scanned for this edition. **Requested addition** means that it was supplied by the owner but was absent from those files. **Related name** identifies the maker of an observed product; it is not presented as a corpus occurrence. The scan includes definitions, explanatory prose, tables, template prompts, and diagram labels. An occurrence in a prohibition or a “Not used” column describes the previous editorial position; it does not determine the new selection.


## 10. Scan coverage and evidence

The initial scan covered every Markdown file under `charter/en/` at source commit `fc67054bda2c0d2387129246903e94c498a6b7b9`: 39 files, including the reading maps, executive summary, nine governing documents, five guides, six workflows, and fourteen templates. It examined the entire file set rather than just Vocabulary and Style. Registry, Portfolio, authored portal content, and implementation code were outside this initial extraction.

Capitalized words and abbreviations were checked in context. Diagram node identifiers, document IDs, record prefixes, language codes, and file-path fragments were not treated as evidence of industry terminology. The scan distinguished use from prohibition. The entries above identify the source concept or a representative source; repeated occurrences do not imply a higher acceptance rate.

FSM, DAG, AWS, and CloudWatch are owner-requested additions. Atlassian is added to explain the ownership of Jira and Confluence. Terms such as API, LLM, RAG, ETL, Git, and Markdown were not found as terms in this charter scan and are not presented as extracted findings. They can be added when Solution descriptions introduce them. The source format being Markdown does not make Markdown an occurrence in the authored corpus.

The following files comprise the scan:

| Area | Files scanned |
| --- | --- |
| Reading map and executive summary (2) | [README.md](../../../../charter/en/README.md), [executive-summary.md](../../../../charter/en/executive-summary.md) |
| Governing documents (9) | [ai-policy.md](../../../../charter/en/documents/ai-policy.md), [aicc-charter.md](../../../../charter/en/documents/aicc-charter.md), [business-model.md](../../../../charter/en/documents/business-model.md), [document-catalog.md](../../../../charter/en/documents/document-catalog.md), [operating-model.md](../../../../charter/en/documents/operating-model.md), [portfolio-management-model.md](../../../../charter/en/documents/portfolio-management-model.md), [solution-lifecycle-model.md](../../../../charter/en/documents/solution-lifecycle-model.md), [statement-of-intent.md](../../../../charter/en/documents/statement-of-intent.md), [vocabulary.md](../../../../charter/en/documents/vocabulary.md) |
| Guides and index (6) | [README.md](../../../../charter/en/guides/README.md), [cadence-guide.md](../../../../charter/en/guides/cadence-guide.md), [engagement-guide.md](../../../../charter/en/guides/engagement-guide.md), [organization-guide.md](../../../../charter/en/guides/organization-guide.md), [service-delivery-guide.md](../../../../charter/en/guides/service-delivery-guide.md), [unit-governance-guide.md](../../../../charter/en/guides/unit-governance-guide.md) |
| Workflows and index (7) | [README.md](../../../../charter/en/workflows/README.md), [ai-risk-control.md](../../../../charter/en/workflows/ai-risk-control.md), [cadence.md](../../../../charter/en/workflows/cadence.md), [collaboration-tooling.md](../../../../charter/en/workflows/collaboration-tooling.md), [engagement.md](../../../../charter/en/workflows/engagement.md), [service-delivery.md](../../../../charter/en/workflows/service-delivery.md), [unit-governance.md](../../../../charter/en/workflows/unit-governance.md) |
| Templates and index (15) | [README.md](../../../../charter/en/templates/README.md), [acceptance-checklist.md](../../../../charter/en/templates/acceptance-checklist.md), [ai-incident-review.md](../../../../charter/en/templates/ai-incident-review.md), [appointments-record.md](../../../../charter/en/templates/appointments-record.md), [control-sign-off.md](../../../../charter/en/templates/control-sign-off.md), [decision-record.md](../../../../charter/en/templates/decision-record.md), [initiative-brief.md](../../../../charter/en/templates/initiative-brief.md), [outcome-report.md](../../../../charter/en/templates/outcome-report.md), [package-definition.md](../../../../charter/en/templates/package-definition.md), [proposal.md](../../../../charter/en/templates/proposal.md), [quarterly-report.md](../../../../charter/en/templates/quarterly-report.md), [registry-snapshot.md](../../../../charter/en/templates/registry-snapshot.md), [service-agreement.md](../../../../charter/en/templates/service-agreement.md), [solution-definition.md](../../../../charter/en/templates/solution-definition.md), [steering-summary.md](../../../../charter/en/templates/steering-summary.md) |

## Edition history

| Edition | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-10-04 | Initial corpus scan, owner-selected names, proposed White and Gray entries, Russian explanations, protected product aliases, and governing-vocabulary boundaries. Corpus companion only; existing prose and the portal have not been migrated to it |
| 0.2 | 2026-10-04 | Owner clarified that established business terminology belongs in normal corpus usage. Expanded the scope to business and technology; added KPI, SLA, WIP, WIP limit, business case, and value stream as selected terms; replaced the preservation of older naming exclusions with meaning-based distinctions and a requirement to reconcile the governing vocabulary |
| 1.0 | 2026-10-04 | Reconciled the governing rule and definitions in both languages under DR-2026-064; integrated this English companion into the portal. The full Russian wording pass remains separate |
