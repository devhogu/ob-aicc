# Verification

Completed 4 October 2026 for Vocabulary and Style / Терминология и стиль revision 3.2.

- Paired semantic review: 176 concepts, 13 states and 12 stage groups; governing references and full inventory in `review.md`.
- English source hashes: 217 verified; reviewed Russian sources: 214.
- Existing portal test suite: all 21 tests passed. The existing glossary test's expected Russian lead was updated to the revised Catalog purpose. Its search, anchor and own-language checks remain in place.
- Scaffolding: 198 pages in nine sections passed; existing long-page warnings retained.
- Build: 460 pages (230 per language), 196 diagrams, none unrendered.
- Site check and repeatability: passed; all 477 generated files unchanged by a repeated build.
- Browser: English and Russian vocabulary pages at 1440px and 390px. All 201 source rows, including every definition and distinction cell, match the rendered tables. Correct document language, no fallback notice, no page overflow. Actual language-switch navigation passed. Four searches opened the appropriate Living record and Delegation definitions in both languages. No browser JavaScript errors.
- Tooltip projection: current Record definition prefixes checked across generated pages in both languages; counts in the artifact below.
- Scoped whitespace check: passed.
- Final GRACE assertion gate: all 8 commands passed; zero errors and six pre-existing Python heuristic warnings. Run logs: `/home/dev-one/.cache/grace/run-commands/aicc-9d0a0eda/runs/2026-10-04T10-27-21_C-FUNCTIONAL-VOCABULARY`.

Browser report: `/home/dev-one/.bb/thread-storage/thr_ypkxiubq2g/artifacts/functional-vocabulary-browser.json`.
Tooltip report: `/home/dev-one/.bb/thread-storage/thr_ypkxiubq2g/artifacts/functional-vocabulary-tooltips.json`.
Screenshots: `functional-vocabulary-{en,ru}-{1440,390}.png` in that artifact directory.

The browser harness initially selected an absolute href while the site uses relative links; the harness was corrected to select the language attribute and then completed successfully. No production navigation change was required.

Changes remain local. No commit, push, deployment, durable projection apply or archive was performed. Other working-tree changes were preserved.
