# Verification

Completed 4 October 2026.

- Source comparison: 217 English source hashes and 214 reviewed Russian source files pass. Record identities, dates, numbered clauses and paired table structures pass the existing checks.
- Portal tests: 22 passed. The new regression distinguishes the Business Case concept from its stage in both languages. Before the anchor correction, it failed in both languages because the two search results had one URL; after the correction, each result identifies one matching row. Existing copy expectations were updated to the agreed international names.
- Build: 460 pages (230 EN, 230 RU); 196 diagrams rendered, none missing.
- Scaffolding: 198 pages, nine sections; check passed with its existing long-page warnings.
- Static site: route, counterpart, link, anchor and asset checks passed; repeated build left 477 files unchanged.
- Terminology sweep: all 460 rendered pages scanned, including diagram text and tooltip attributes. No unresolved fixed-name misses. Explanatory Russian names, exact external titles and non-AI uses of agent are recorded as reviewed exceptions.
- Browser: all 460 pages loaded in the correct language with working counterparts, no fallback notice, no horizontal page overflow at 1440px and no JavaScript errors. Sixteen representative mobile pages passed at 390px. Eight searches opened the correct concept or stage, and an actual EN-to-RU switch preserved the AI agent definition.
- Search harness: the initial run appended a query after same-document hash navigation. Clearing the input before typing fixed the harness; the final run above passed. No production search behavior was changed for that harness issue.
- The Russian mobile engagement-guide screenshot was inspected; international terminology fits its navigation, heading and content.
- Scoped whitespace check passed.
- Final GRACE gate: 9/9 commands passed, zero errors; six existing Python heuristic warnings remain. Logs: `/home/dev-one/.cache/grace/run-commands/aicc-9d0a0eda/runs/2026-10-04T10-51-47_C-INTERNATIONAL-TERMINOLOGY`.

Artifacts:

- `/home/dev-one/.bb/thread-storage/thr_ypkxiubq2g/artifacts/international-terminology-browser.json`
- `/home/dev-one/.bb/thread-storage/thr_ypkxiubq2g/artifacts/international-terminology-sweep.json`
- `international-{en,ru}-{vocabulary,engagement-guide}-390.png` in the same directory.

Source changes and reviewed exceptions are described in `review.md` and `source-review.json`. No commit, push, deployment or durable GRACE apply/archive was performed. Unrelated work was preserved.
