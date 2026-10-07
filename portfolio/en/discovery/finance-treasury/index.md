# Finance & Treasury

Finance & Treasury is the Bank's financial planning and control discipline — the function that measures every value stream in margin terms, steers the balance sheet, and presents a financially defensible picture to regulators, boards, and investors. It spans eight sub-concerns: financial planning & analysis, capital management, liquidity management, asset-liability management, performance measurement, accounting & financial close, regulatory financial reporting, and tax management. Under supervisory requirements, most of these sub-concerns carry formal reporting obligations with fixed submission cycles, prescribed formats, and supervisory review. **The GenAI opportunity is continuous financial instrumentation — condensing the cycle from data-to-decision across every planning, close, reporting, and disclosure workflow from weeks to hours.**

## Problems

### Planning & balance-sheet steering {#planning-balance-sheet-steering}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Capital, liquidity, and interest-rate sensitivity positions are each measured on separate cycles by separate teams — capital monthly by Finance, LCR and NSFR daily by Treasury, NII and EVE sensitivity monthly by ALM. ALCO and the CFO assemble a composite balance-sheet picture manually, and emerging cross-dimensional pressure — a rate shift that simultaneously tightens NIM, compresses CET1 via accumulated OCI, and reduces the HQLA buffer — is identified reactively. |
| Enablement | Reforecast, capital projection, and rate-scenario analyses are bottlenecked on small specialist teams with bespoke models. When the CFO needs a same-day sensitivity on a central bank rate decision or a rating agency press call surfaces a capital question, the answer requires a multi-team escalation chain that typically takes one to three days. Planning and treasury functions cannot operate at the speed the business requires. |
| Automation | Budget narratives, ICAAP chapters, ALCO rate packs, FTP memos, and rolling reforecasts are assembled manually each cycle from model outputs and system exports. Each document is structurally predictable — the inputs are known, the format is prescribed — making them primary candidates for AI-driven drafting with human sign-off. |
| New business opportunities | A continuously instrumented balance sheet — capital headroom, liquidity surplus, and rate sensitivity refreshed from live feeds — creates a forward signal for capital deployment and pricing decisions. Banks operating on weekly rather than monthly cycles can move on acquisition targets, deposit repricing, and portfolio rebalancing faster than peers constrained by the standard reporting cadence. |

## Overview

### FP&A {#fpa}

- Group: Planning & balance-sheet steering

| Sub-group | Items |
| --- | --- |
| Planning & forecasting | annual-budget-cycle, rolling-forecast |
| Variance & decision support | budget-to-actual-variance, cfo-alco-qa-support |

### ALM {#alm}

- Group: Planning & balance-sheet steering

| Sub-group | Items |
| --- | --- |
| IRRBB & balance-sheet hedging | nii-eve-sensitivity, irrbb-limit-monitoring |
| FTP & rate-scenario reasoning | ftp-curve-governance, alco-rate-pack |

### Finance Cycles {#finance-cycles}

- Group: Finance governance

| Section | List name | Flows |
| --- | --- | --- |
| Planning & balance-sheet steering | Planning & balance-sheet steering | budget-forecast-cycle, alm-balance-sheet-steering-cycle, liquidity-steering-cycle |
| Reporting & close | Reporting & close | financial-close-cycle, regulatory-reporting-cycle |

### Capital management {#capital-management}

- Group: Planning & balance-sheet steering

| Sub-group | Items |
| --- | --- |
| Capital position & projection | cet1-tier1-position, icaap-stress-capital |
| Capital actions & supervisory dialog | supervisory-communications, capital-actions |

### Liquidity management {#liquidity-management}

- Group: Planning & balance-sheet steering

| Sub-group | Items |
| --- | --- |
| Cash & liquidity position | daily-lcr-nsfr, investment-portfolio |
| Liquidity stress & contingency | contingency-funding-plan, funding-strategy |

### Performance measurement {#performance-measurement}

- Group: Planning & balance-sheet steering

| Sub-group | Items |
| --- | --- |
| Profit attribution | segment-pl, budget-variance-attribution |
| Risk-adjusted returns | raroc-by-bu, lending-default-attribution |

### Accounting & financial close {#accounting-financial-close}

- Group: Accounting, reporting & tax

| Sub-group | Items |
| --- | --- |
| Period-end close | close-task-management, close-narrative |
| Reconciliations & sub-ledger discipline | gl-sub-ledger-reconciliations, lending-default-close |

### Regulatory financial reporting {#regulatory-financial-reporting}

- Group: Accounting, reporting & tax

| Sub-group | Items |
| --- | --- |
| Basel & supervisory reporting | corep-finrep-validation, regulatory-narrative |
| Local regulatory submissions | local-prudential-returns, investor-disclosure |

### Tax management {#tax-management}

- Group: Accounting, reporting & tax

| Sub-group | Items |
| --- | --- |
| Tax position & filings | etr-reconciliation, rating-agency-tax |
| Transfer pricing & tax information reporting | transfer-pricing-documentation, fatca-crs-reporting |

## Scenarios

### CFO Ad-Hoc Financial Q&A

- URN: urn:financial-services:scenario:finance-treasury/cfo-adhoc-financial-qa
- Lens: Enablement
- Complexity: M
- Intent: Conversational interface through which the CFO retrieves attributed answers to cross-function financial questions during board sessions, investor meetings, or supervisory meetings — drawing simultaneously on FP&A, capital, liquidity, ALM, performance, close, regulatory reporting, and tax data. No request to any individual L2 team is required.
- Problem to solve: CFO-level questions arising in board sessions and investor meetings frequently span multiple L2 disciplines simultaneously — a question on NIM trajectory requires FP&A, ALM, and liquidity data; a capital adequacy question requires capital, regulatory reporting, and performance data. Each cross-function answer currently requires a separate queue to the relevant team, with responses arriving after the meeting.
- Solution: The AI agent maintains a continuously refreshed parametric view of the Bank's financial position across all L2 disciplines. The CFO queries conversationally; the AI agent retrieves and reconciles the relevant data across functions and delivers an attributed answer within the session. L2 team involvement is reserved for follow-up analytical work the answer identifies; Finance periodically reviews answers for reconciliation errors.
- OKR: The CFO retrieves attributed answers to cross-function financial questions — spanning FP&A, capital, liquidity, ALM, performance, close, regulatory reporting, and tax data — within the session during board, investor, and regulatory interactions, without queuing to individual L2 teams.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-powered CFO Q&A interface used for ≥80% of cross-function financial questions arising in board, investor, and supervisory sessions within 12 months of go-live. |
| Acceptance | ≥85% of session answers rated as accurate and sufficiently attributed by the CFO without requiring L2 team follow-up to correct the response; data reconciliation errors ≤3% on periodic Finance review. |
| Cycle | Cross-function financial question answered within the session, vs. 4–24 hours of L2 team queue time in the prior process. |

### Finance Production Calendar Sequencing

- URN: urn:financial-services:scenario:finance-treasury/finance-production-calendar-sequencing
- Lens: Optimize
- Complexity: S
- Intent: The AI agent maps the Bank's full annual Finance production calendar — close, ALCO, board pack, ICAAP, prudential returns, FATCA/CRS, transfer pricing, and other regulatory reporting deadlines — identifies dependency chains and scheduling conflicts, and recommends a sequenced production calendar that minimizes elapsed time across all L2 disciplines.
- Problem to solve: The CFO's office manages fifteen to twenty annual submission and reporting events across eight L2 disciplines, each with its own internal lead times, cross-discipline data dependencies, and hard regulatory deadlines. Cross-function sequencing conflicts — close delays cascading into prudential returns, or ICAAP drafting compressing ALCO preparation — are identified when they occur, not in advance.
- Solution: The AI agent reads the regulatory submission calendar, internal governance schedule, and declared lead times for each L2 production workflow. It constructs an integrated dependency model identifying which L2 outputs feed downstream L2 or L1 workflows, and produces a sequenced production calendar with slack analysis per event and conflict flags where current schedules create downstream compression. The CFO's office reviews and approves the recommended schedule.
- OKR: An integrated Finance production calendar — covering close, ALCO, board pack, ICAAP, prudential returns, FATCA/CRS, transfer pricing, and all other regulatory reporting deadlines with dependency chains and slack analysis — is available for review by the CFO's office at the start of each calendar year.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced integrated production calendar used for ≥1 annual calendar cycle within year 1; all 8 L2 disciplines and all material regulatory submission events covered. |
| Acceptance | ≥80% of scheduling conflicts identified by the AI agent confirmed as genuine cross-discipline compression risks by the CFO's office; calendar adopted without material re-sequencing in ≥75% of identified conflict resolutions. |
| Cycle | Integrated production calendar with dependency mapping available for review by the CFO's office within 5 business days of the new calendar year, vs. 3–4 weeks of sequential cross-discipline coordination in the prior process. |

### CFO Cross-Function Finance Briefing

- URN: urn:financial-services:scenario:finance-treasury/cfo-cross-function-finance-briefing
- Lens: Insights
- Complexity: M
- Intent: The AI agent ingests the full set of L2 function reports each month-end — FP&A, capital, liquidity, ALM, performance, close, regulatory reporting, and tax — and produces a unified CFO briefing ranked by materiality. Cross-function correlations are made explicit in a single synthesized view.
- Problem to solve: The CFO receives reports from eight L2 functions each month in different formats, vocabularies, and analytical frames. Cross-function patterns — NIM compression touching ALM, FP&A, and close simultaneously — are invisible because no single report owner holds the whole picture.
- Solution: The AI agent reads each L2 function report, extracts KPI movements and decisions required, checks numerical consistency where the same figure should reconcile across reports, and links correlated themes across functions. Output is a unified CFO briefing ranked by decision materiality, not by source function. The CFO reviews the synthesized view and applies judgment on priority and response.
- OKR: The CFO receives a unified monthly briefing ranked by decision materiality — with cross-function correlations explicit and numerical consistency verified — drawn from all eight L2 function reports, available on the first day of the reporting window.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced unified CFO briefing used for ≥10 of 12 monthly cycles in year 1; all 8 L2 reports integrated in each briefing. |
| Acceptance | ≥85% of unified briefings rated by the CFO as materially improving cross-function visibility vs. reading individual L2 reports; cross-function numerical consistency errors surfaced and flagged before CFO review in ≥95% of reviewed cycles. |
| Cycle | Unified CFO briefing available on day 1 of the reporting window, vs. 2–3 days for full L2 stack review in the prior process. |

### CFO Board & Investor Pack Assembly

- URN: urn:financial-services:scenario:finance-treasury/cfo-board-investor-pack-assembly
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles the quarterly CFO board pack and investor disclosure from closed outputs across all L2 disciplines — performance, capital, liquidity, ALM, close, regulatory reporting, FP&A, and tax — into a single consistent document. The pack is available for CFO review on the first day of reporting.
- Problem to solve: Quarterly board packs and investor disclosures are assembled by Finance, IR, and Controllers drawing on outputs from eight L2 disciplines produced at different times and in different formats. Cross-section consistency — NIM figures reconciling across the management accounts, ALCO pack, and investor release — is checked manually, and a complete draft is rarely available before the penultimate day.
- Solution: The AI agent reads the closed L2 outputs and applies the Bank's standard pack structure — headline performance, capital and liquidity position, ALM summary, regulatory position, and outlook — populating each section from the authoritative source for that discipline. Cross-section consistency is checked automatically; figures that differ across sections are flagged before CFO review. The CFO edits for judgment and forward framing.
- OKR: The quarterly CFO board pack and investor disclosure are assembled from closed L2 outputs across all Finance disciplines into a consistent document available for CFO review on the first day of the reporting window.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced CFO board pack used for ≥4 quarterly reporting cycles within year 1; all 8 L2 disciplines covered in each cycle. |
| Acceptance | ≥85% of assembled packs accepted by the CFO for distribution without material structural amendment; cross-section figure consistency errors flagged and resolved before CFO review in ≥97% of reviewed cycles. |
| Cycle | Complete CFO board pack available for CFO review on day 1 of reporting, vs. penultimate day in the prior manual process. |

### Continuous CFO Financial Posture

- URN: urn:financial-services:scenario:finance-treasury/cfo-continuous-financial-posture
- Lens: New opps
- Complexity: M
- Intent: The AI agent maintains a continuously updated financial posture for the CFO across all eight L2 disciplines — capital, liquidity, ALM, FP&A, performance, close, regulatory reporting, and tax — refreshed from live feeds and available on demand between formal reporting cycles.
- Problem to solve: Between formal reporting cycles, the CFO holds a point-in-time picture from the last set of L2 reports. Intra-period movements in capital headroom, liquidity ratios, NIM trajectory, or tax provision are visible only when the next scheduled report is assembled; emerging cross-function patterns are not surfaced until each movement appears in its own monthly L2 report.
- Solution: The AI agent reads current data feeds across all L2 disciplines on a rolling basis — regulatory capital feeds, treasury liquidity positions, ALM model outputs, FP&A tracking actuals, and tax provision movements — and maintains a continuously updated posture summary in the CFO's house format. Cross-function threshold breaches trigger a proactive alert with attributed narrative; L2 teams retain ownership of their data and analytical conclusions.
- OKR: The CFO holds a continuously updated financial posture across all eight L2 disciplines — capital, liquidity, ALM, FP&A, performance, close, regulatory reporting, and tax — refreshed from live feeds and available on demand between formal reporting cycles.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-maintained posture summary accessed by the CFO on ≥80% of working days between formal reporting cycles within year 1; all 8 L2 disciplines covered in each refresh. |
| Acceptance | ≥85% of cross-function threshold breach alerts rated as accurate and decision-relevant by the CFO without requiring L2 team correction; posture data reconciles to the next formal L2 report in ≥97% of sampled cells. |
| Cycle | Intra-period cross-function position available on demand between formal reporting cycles, vs. waiting for the next scheduled monthly report in the prior process. |
