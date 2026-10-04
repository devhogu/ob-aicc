# Terminology language editions: verification

Completed implementation and verification on 4 October 2026 under the user's explicit correction that each corpus language contains its own definitions. The earlier C-SHARED-TERMINOLOGY specification and plan were preserved; this successor replaces their English-only reference constraint.

Edition 1.3 has separate English and Russian corpus files. Each contains the same 71 term identities in the same four subject groups, with three columns: term, meaning and application. The English file contains no Russian explanatory prose. The Russian edition includes translated definitions, usage notes, provisions, references and change history; international term and product names retain their identity. Definitions and usage were reviewed against the corresponding English concepts and the existing Russian Vocabulary, including the distinctions between SLA and Support level, KPI and Measure, WIP and WIP limit, and platform and investment controls.

Vocabulary and Style and Document Catalog revision 3.1 state the language structure in both languages. The reading maps link to their own language reference, and each charter directory contains 40 Markdown files. The portal search uses the Meaning column of the selected language source. Its regression covers source identity, absence of a fallback notice, localized headers and an actual definition in both languages; all 71 entries are present in each search index. The Registry's earlier decision history remains unchanged.

Baseline command evidence: `/home/dev-one/.cache/grace/run-commands/aicc-9d0a0eda/runs/2026-10-04T09-25-15_C-TERMINOLOGY-LANGUAGE-EDITIONS`.

Final command: `grace lint --path . --change C-TERMINOLOGY-LANGUAGE-EDITIONS --assertions final --run-commands`.

All six command assertions passed, including the other active plans' source checks. The result was zero errors and the same six existing heuristic warnings. Source validation verified 217 comparison hashes and 214 reviewed Russian files; all 20 tests passed; scaffolding coverage passed; all 460 pages and 196 diagrams rendered; all 477 generated files were identical on a repeat build. Links, anchors and language parity passed. Final evidence: `/home/dev-one/.cache/grace/run-commands/aicc-9d0a0eda/runs/2026-10-04T09-38-59_C-TERMINOLOGY-LANGUAGE-EDITIONS`.

Browser verification covered the reference and Catalog in both languages at 1440 and 390 pixels, plus English and Russian search navigation to the FSM definition. All eight page checks and both searches passed without script errors or horizontal page overflow. The reference has four tables with 10, 23, 31 and 7 entries, each with three columns. The entire Russian output has no English fallback notices. Browser evidence: `/home/dev-one/.bb/thread-storage/thr_ypkxiubq2g/artifacts/terminology-local-editions-browser.json`; inspected screenshot: `terminology-local-ru.png` beside it.

No durable graph or verification projection change was required. No lifecycle apply/archive, commit, push or deployment was performed. Unrelated workspace work was preserved.
