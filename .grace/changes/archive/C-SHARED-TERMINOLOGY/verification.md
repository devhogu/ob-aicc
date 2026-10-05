# Shared terminology reconciliation: verification

Verified on 4 October 2026. The approved specification and plan remain unchanged.

The bilingual governing vocabulary and Catalog now prefer established industry terms and explain their relationships to AICC concepts. Vocabulary and Style and Document Catalog are revision 3.0; Portfolio Management Model is revision 2.2. DR-2026-064 records the owner's naming decision. The English shared terminology companion is edition 1.0 and has a portal route in both navigation languages. The Russian route identifies the English content; the full Russian wording migration remains outside this change.

Semantic review covered the paired definitions of KPI, metric, SLA, WIP, WIP limit, business case and value stream, the replacement of blanket exclusions with Related terms, and Epic's Jira mapping. The last repeated Epic restriction was corrected in the companion and the paired authored delivery explanation. Service commitments, measurement boundaries, authority, states and work hierarchy are preserved.

Final command gate: `grace lint --path . --change C-SHARED-TERMINOLOGY --assertions final --run-commands`.

- All five command assertions passed, with zero errors and the same six existing heuristic warnings.
- Source validation verified 217 comparison hashes and 213 reviewed Russian translations.
- All 19 regression tests passed. The added checker regression first reproduced rejection of a clickable citation, then passed after the fix; remote scripts, images, stylesheets and embedded pages remain rejected, including protocol-relative resources.
- Scaffolding coverage passed for 198 pages. All 197 existing scaffold routes retain their original URLs; the shared terminology reference is the only addition.
- The build produced 460 pages and 196 diagrams, with none missing. All 477 output files were unchanged on a repeat build; link, anchor and language checks passed.
- Browser verification covered seven representative routes in both languages at 1440 and 390 pixels: 28 page checks, plus four search-and-navigation checks for the new reference and KPI. Language switches, definitions, disclosure and navigation passed, with no page overflow, script errors or automatic external requests. Desktop and mobile screenshots were inspected.

Command evidence: `/home/dev-one/.cache/grace/run-commands/aicc-9d0a0eda/runs/2026-10-04T08-57-06_C-SHARED-TERMINOLOGY`.

Browser evidence: `/home/dev-one/.bb/thread-storage/thr_ypkxiubq2g/artifacts/terminology-browser.json`, with `terminology-{en,ru}-{1440,390}.png` screenshots beside it. The temporary browser harness was corrected to disable HTTP caching and accept section anchors in search-result links; these were harness assumptions, not product defects.

No graph or verification projection change was needed: the approved DurableScope is None. This verification records implementation evidence and does not change lifecycle status, commit, push or deploy the work. Unrelated portal work remains untouched.

## Formal wording correction

On 4 October 2026 the user clarified that the shared reference is official charter corpus and must use formal institutional wording. This directly authorized an editorial correction within the existing source and projection scope. Edition 1.1 replaces personal selection labels, requested additions, candidate discussions and future drafting notes with numbered provisions, standard names and permitted language variants. Section 3 is now “Standard technical names.” The prior assessment bands and scan evidence are retained in `terminology-research.md`; decision provenance remains in the Registry. The six narrative term definitions and all 65 tabular English meanings and Russian explanations were compared with edition 1.0 and remain unchanged.

The final command gate passed again with all five commands, zero errors and the same six heuristic warnings. Evidence: `/home/dev-one/.cache/grace/run-commands/aicc-9d0a0eda/runs/2026-10-04T09-13-20_C-SHARED-TERMINOLOGY`. The generated English and Russian routes were checked at desktop and mobile widths, including the renamed section, absence of drafting labels, source-language notice and section search result. All four page checks and the search check passed without script errors or horizontal page overflow. Browser evidence: `/home/dev-one/.bb/thread-storage/thr_ypkxiubq2g/artifacts/terminology-formal-browser.json`; screenshot: `terminology-formal-section-3.png` in the same directory. No commit, push or deployment was performed.

## Uniform entry structure

The user subsequently clarified that the supplied terms were examples and should receive the same treatment as the other entries. Edition 1.2 consolidates all 71 entries into four subject tables: business and governance (10), delivery and workflow (23), technology and AI (31), and organizations and products (7). Every entry has an English meaning, Russian explanation and application. Comparison against edition 1.1 confirmed that all definitions and Russian explanations were retained; abbreviations retain their expansions and the prior naming distinctions are stated at entry level.

The portal indexes every table entry, preserving search access when a term no longer has its own heading. A renderer regression first reproduced missing table-term results and then passed for both language routes after the search change. The final command gate passed all five assertions with 20 tests, zero errors and the same six existing warnings. Command evidence: `/home/dev-one/.cache/grace/run-commands/aicc-9d0a0eda/runs/2026-10-04T09-21-22_C-SHARED-TERMINOLOGY`. Both search indexes contain all 71 entries. Browser checks confirmed the four table sizes at desktop and mobile widths in both language routes and successful FSM search navigation, with no script errors or horizontal page overflow. Browser evidence: `/home/dev-one/.bb/thread-storage/thr_ypkxiubq2g/artifacts/terminology-unified-browser.json`, with `terminology-unified.png` beside it. Changes remain local.
