# C-RU-NATURAL-ALIGNMENT — report

4 October 2026 · branch `claude/ru-alignment`

## 1. Result

Every in-scope Russian source was compared with its English counterpart sentence by sentence and rewritten
from a word-for-word rendering into formal, natural Russian:

| Area | Files |
| --- | --- |
| Charter: governing documents, terminology, translation map, summary, reading map | 14 |
| Charter: guides, workflows (now «рабочие процессы»), templates | 28 |
| Portal pages (`portal/content/ru`) | 118 |
| Portal interface text: `authored.json` (Russian fields), `messages/ru.json`, Russian literals in `build.py` | 3 |

English sources, Registry and Portfolio are byte-identical to the start (`protected-files.sha256`).
Structure is unchanged: clause numbers, headings, table rows and columns, links, identifiers, Mermaid
node IDs and edges. The generated portal changes only in its Russian pages and Russian search index.

| Marker (same scan rules before and after) | Before | After |
| --- | --- | --- |
| Rejected forms of the translation map | 1,721 | 455 (≈445 are correct uses: «записи» at cell starts, «проверка» as the Check term) |
| Latin words in Russian prose | 747 | 347 (English term references on terminology pages, paths, placeholders, accepted fixed forms) |
| Capitalised AICC terms inside sentences (heuristic) | 11,774 | 631 (document titles, bodies of the Bank, state and stage names, sentence starts) |

Meaning drift between English and the old Russian: **148 corrections**, each recorded in `notes/`.
Typical patterns: «руководство» for the Management Board, «должен» turning a recommendation into a duty,
«максимально возможные усилия» overstating "best effort", «корпус Положения» for the charter corpus,
a RACI header «Консультируется» meaning the reverse of "Consulted", dropped or added qualifiers.

Verification: source check (217 English pins, 214 reviewed translations), 22 unit tests, scaffolding
check, full build (460 pages, 197 diagrams), repeatable build, site check — all pass.

## 2. Owner decisions applied

- Revisions are «версия» (column «Версия», «Версия 1.6 · …»); language edition «языковая версия».
- «итерация», «программный инкремент (PI)» in Russian.
- Protected Latin work-item names with a capital letter: Initiative, Capability, Feature, Story, Task,
  Spike, Bug, Epic (gender and plural in the style sheet; case shown by surrounding words).
- AICC terms in lowercase; capitals only for bodies of the Bank, «Банк», document titles, quoted state
  and stage names, fixed names. Bare «решение» = Solution; a decision is «управленческое решение» or a verb.
  Bare «проверка» = the Check term.
- Present-tense duties, «вправе», «не вправе» / «не допускается»; «должен» only for document content
  (Vocabulary 3.1, Russian edition).
- Translation map: section 5 reviewed and moved into sections 3–4 (version 0.3 now).

## 3. Choices made during the run — revisit candidates

Each is applied consistently and can be reverted by search and replace.

1. **Initiative Brief → «паспорт Initiative»**, template title «Паспорт Initiative». Also renamed template
   titles: «Разбор инцидента AI», «Снимок реестра», «Итоги управляющего совещания».
2. **Work Item → «рабочий элемент»** (was «рабочая задача», now avoided because Task is a Latin name).
3. **Plan–do–check–act "check" → «контроль»** everywhere («планирование — выполнение — контроль —
   корректировка»), so that «проверка» stays the Check term.
4. **value stream → «поток создания ценности»; Workflow → «рабочий процесс»** (interface labels too).
   The English terminology still says Workflow and value stream are fixed in all language versions
   — see §4.
5. **Event names**: «ежедневная планёрка», «планирование итерации», «ревью и демонстрация итерации»,
   «ретроспектива итерации», «PI-планирование», «обзор и демонстрация PI», «Inspect and Adapt» kept Latin.
6. **Service categories** follow the rewritten Business Model: «Оценка и экспертиза» (Assessments and
   evaluations), «Мониторинг» (Oversight; «надзор» is reserved for supervisory authorities).
   «Сервисы знаний» kept.
7. **Lean Portfolio Management → «эффективное управление портфелем»** (terminology accepted form);
   the usual Russian is «бережливое управление портфелем».
8. **audit trail → «аудиторский след»** (terminology changed from «аудиторский трейл»).
9. **Assurance loop → «цикл подтверждения надлежащего функционирования»** (kept from the Operating
   Model; long — a shorter name may read better).
10. **Service step names kept** («Допущен», «Внесён в каталог», «Обслуживает», «Мигрирует» …): they are
    shared by the lifecycle model, Solution Definition, service delivery workflow and portal pages.
11. **Operating Model 4.8**: "within five working days" rendered «не позднее пяти рабочих дней с даты
    соответствующего управленческого решения» — the start date is inferred.
12. **AICC Charter 3.3**: «Данные и управленческие решения» for "data and decisions" (not Solutions).
13. **ISO page** adds the Russian national designations ГОСТ Р ИСО/МЭК 42001-2024 and ГОСТ Р 71476-2024,
    which the English page does not name.
14. **«Каталог управления»** (package name from the Portfolio) reads poorly; the Portfolio is out of scope.
15. Templates use «ФИО» for name fields; RACI letter expansions stay in English in the organization guide.

The per-batch notes hold about 180 smaller QUESTION items (term and field-label choices) with the
alternatives considered.

## 4. English issues found (English not changed)

- Statement of Intent 12.2 says AICC reports to the Board Committee each quarter; Charter 7.2 and the
  Executive Summary say the Executive Sponsor issues the report.
- Terminology: "Workflow is the fixed name in all language versions" and value stream "Fixed form"
  conflict with the Russian forms now used.
- Operating Model 7.3 "which the monthly Steering leaves" is unclear; 7.4 "It is promoted…" has an
  unclear subject.
- Solution Lifecycle Model 4.1 "Each is ranked" (backlog or item?); 6.6 "not tracked in the charter";
  Figure 11 "Limits".
- Portfolio Management Model 4.3 list seems to miss an "and".
- Document Catalog 5.3 "They" is ambiguous.
- Engagement guide §7 "a change beyond it"; unit governance guide C-31 "leaves no … registry entry".
- Service delivery workflow Figure 1 "Capability: a capability" is circular.
- Templates: Appointments Record "named below the Roles"; Proposal "the owners"; Solution Definition §4
  stray full stop.
- Portal: portfolio measures "the Verify or the Review" (elsewhere "check or validation"); opportunities
  page shortens the sixth Strategic Priority's title; industry body of knowledge says every source has a
  page (several do not) and links are labelled with an older page title; adoption and lifecycle page
  says revision goes through the Portfolio Backlog (1.1) and the Program Backlog (4.1); a section is
  called "Governance and oversight" while its label is "Governance".

## 5. Outside this change

- **Registry and Portfolio Russian** still use the old capitalisation and some old names (e.g. «Паспорт
  инициативы», category names). The portal does not publish them, but readers of the repository will
  see the difference.
- The build now links Russian number-first references («разделом 4 Бизнес-модели», «п. 5.4 …»,
  «пункты 4.4, 4.5 и 4.10 …») and lowercase glossary terms; both are covered by tests.

## 6. Files

- Style sheet and term table: `STYLE.md` · per-file checker: `check_one.py` · scan: `scan.py`
- Scans: `baseline-scan.json`, `after-scan.json`
- Per-batch notes (DRIFT / QUESTION / ENGLISH?): `notes/01` … `notes/13`
