# 

source: html-alt/financial-services/en/finance-treasury/index.html


[PAGE TEXT]
Planning & balance-sheet steering
FP&A (12)
Planning forecasting
Annual budget cycle (3)
·
Rolling forecast (3)
Variance decision support
Budget-to-actual variance attribution (3)
·
CFO & ALCO Q&A support (3)
Planning & balance-sheet steering
ALM (12)
Irrbb balance sheet hedging
NII & EVE sensitivity (3)
·
IRRBB limit monitoring (3)
Ftp rate scenario reasoning
FTP curve governance (3)
·
ALCO rate-scenario pack (3)
Finance governance
Finance Cycles (25)
Planning & balance-sheet steering
Budget & forecast cycle (5)
ALM & balance-sheet steering cycle (5)
Liquidity steering cycle (LCR & ILAAP) (5)
Reporting & close
Financial close cycle (5)
Regulatory reporting cycle (5)
Planning & balance-sheet steering
Capital management (12)
Capital position projection
CET1 & Tier 1 position (3)
·
ICAAP & stress capital (3)
Capital actions supervisory dialog
Supervisory communications (3)
·
Dividend, AT1 & Tier 2 capital actions (3)
Planning & balance-sheet steering
Liquidity management (12)
Cash liquidity position
Daily LCR & NSFR monitoring (3)
·
HQLA portfolio & investment management (3)
Liquidity stress contingency
Contingency Funding Plan (CFP) (3)
·
Funding strategy & wholesale mix (3)
Planning & balance-sheet steering
Performance measurement (12)
Profit attribution
Segment P&L & management accounts (3)
·
Budget-to-actual variance & attribution (3)
Risk adjusted returns
RAROC & EVA attribution by BU (3)
·
Lending portfolio attribution & CECL / IFRS 9 (3)
Accounting, reporting & tax
Accounting & financial close (12)
Period end close
Close task management (3)
·
Close narrative & management commentary (3)
Reconciliations sub ledger discipline
GL-to-sub-ledger reconciliations (3)
·
Provisions & IFRS 9 close entries (3)
Accounting, reporting & tax
Regulatory financial reporting (12)
Basel corep finrep
COREP & FINREP data quality validation (3)
·
Regulatory submission narrative (3)
Local regulatory submissions
NBKR / NBK / CBR prudential returns (3)
·
Investor disclosure & statutory accounts (3)
Accounting, reporting & tax
Tax management (12)
Tax position filings
Effective tax rate reconciliation (3)
·
Tax position in investor & rating agency disclosure (3)
Transfer pricing indirect taxes
Transfer pricing local file documentation (3)
·
FATCA / CRS reporting compliance (3)
Scenarios
Lens
Scenario
Intent
Complexity

### CARD 1 [Enablement|S] CFO Ad-Hoc Financial Q&A
urn: urn:financial-services:scenario:finance-treasury/cfo-adhoc-financial-qa
intent: Conversational interface through which the CFO retrieves attributed answers to cross-function financial questions during board sessions, investor meetings, or regulatory hearings — drawing simultaneously on FP&A, capital, liquidity, ALM, performance, close, regulatory reporting, and tax data. No request to any individual L2 team is required.
Problem to solve: CFO-level questions arising in board sessions and investor meetings frequently span multiple L2 disciplines simultaneously — a question on NIM trajectory requires FP&A, ALM, and liquidity data; a capital adequacy question requires capital, regulatory reporting, and performance data. Each cross-function answer currently requires a separate queue to the relevant team, with responses arriving after the meeting.
Solution: Agent maintains a continuously refreshed parametric view of the bank's financial position across all L2 disciplines. The CFO queries conversationally; the agent retrieves and reconciles the relevant data across functions and delivers an attributed answer within the session. L2 team involvement is reserved for follow-up analytical work the answer identifies.
OKR objective: The CFO retrieves attributed answers to cross-function financial questions — spanning FP&A, capital, liquidity, ALM, performance, close, regulatory reporting, and tax data — within the session during board, investor, and regulatory interactions, without queuing to individual L2 teams.
OKR KR [Adoption]: Agent-powered CFO Q&A interface used for ≥80% of cross-function financial questions arising in board, investor, and supervisory sessions within 12 months of go-live.
OKR KR [Acceptance]: ≥85% of session answers rated as accurate and sufficiently attributed by the CFO without requiring L2 team follow-up to correct the response; data reconciliation errors ≤3% on periodic Finance review.
OKR KR [Cycle]: Cross-function financial question answered within the session, vs. 4–24 hours of L2 team queue time in the prior process.

### CARD 2 [Optimize|S] Finance Production Calendar Sequencing
urn: urn:financial-services:scenario:finance-treasury/finance-production-calendar-sequencing
intent: Agent maps the bank's full annual Finance production calendar — close, ALCO, board pack, ICAAP, COREP/FINREP, FATCA/CRS, transfer pricing, and regulatory reporting deadlines — identifies dependency chains and scheduling conflicts, and recommends a sequenced production calendar that minimises elapsed time across all L2 disciplines.
Problem to solve: The CFO's office manages fifteen to twenty annual submission and reporting events across eight L2 disciplines, each with its own internal lead times, cross-discipline data dependencies, and hard regulatory deadlines. Cross-function sequencing conflicts — close delays cascading into COREP/FINREP, or ICAAP drafting compressing ALCO preparation — are identified when they occur, not in advance.
Solution: Agent reads the regulatory submission calendar, internal governance schedule, and declared lead times for each L2 production workflow. It constructs an integrated dependency model identifying which L2 outputs feed downstream L2 or L1 workflows, and produces a sequenced production calendar with slack analysis per event and conflict flags where current schedules create downstream compression. The CFO's office reviews and approves the recommended schedule.
OKR objective: An integrated Finance production calendar — covering close, ALCO, board pack, ICAAP, COREP/FINREP, FATCA/CRS, transfer pricing, and all regulatory reporting deadlines with dependency chains and slack analysis — is available for CFO office review at the start of each calendar year.
OKR KR [Adoption]: Agent-produced integrated production calendar used for ≥1 annual calendar cycle within year 1; all 8 L2 disciplines and all material regulatory submission events covered.
OKR KR [Acceptance]: ≥80% of scheduling conflicts identified by the agent confirmed as genuine cross-discipline compression risks by the CFO office; calendar adopted without material re-sequencing in ≥75% of identified conflict resolutions.
OKR KR [Cycle]: Integrated production calendar with dependency mapping available for CFO office review within 5 business days of the new calendar year, vs. 3–4 weeks of sequential cross-discipline coordination in the prior process.

### CARD 3 [Insights|M] CFO Cross-Function Finance Briefing
urn: urn:financial-services:scenario:finance-treasury/cfo-cross-function-finance-briefing
intent: Agent ingests the full set of L2 function reports each month-end — FP&A, capital, liquidity, ALM, performance, close, regulatory reporting, and tax — and produces a unified CFO briefing ranked by materiality. Cross-function correlations are made explicit in a single synthesised view.
Problem to solve: The CFO receives reports from eight L2 functions each month in different formats, vocabularies, and analytical frames. Cross-function patterns — NIM compression touching ALM, FP&A, and close simultaneously — are invisible because no single report owner holds the whole picture.
Solution: Agent reads each L2 function report, extracts KPI movements and decisions required, checks numerical consistency where the same figure should reconcile across reports, and links correlated themes across functions. Output is a unified CFO briefing ranked by decision materiality, not by source function. CFO reviews the synthesised view and applies judgment on priority and response.
OKR objective: The CFO receives a unified monthly briefing ranked by decision materiality — with cross-function correlations explicit and numerical consistency verified — drawn from all eight L2 function reports, available on the first day of the reporting window.
OKR KR [Adoption]: Agent-produced unified CFO briefing used for ≥10 of 12 monthly cycles in year 1; all 8 L2 reports integrated in each briefing.
OKR KR [Acceptance]: ≥85% of unified briefings rated by the CFO as materially improving cross-function visibility vs. reading individual L2 reports; cross-function numerical consistency errors surfaced and flagged before CFO review in ≥95% of reviewed cycles.
OKR KR [Cycle]: Unified CFO briefing available on day 1 of the reporting window, vs. 2–3 days for full L2 stack review in the prior process.

### CARD 4 [Automation|M] CFO Board & Investor Pack Assembly
urn: urn:financial-services:scenario:finance-treasury/cfo-board-investor-pack-assembly
intent: Agent assembles the quarterly CFO board pack and investor disclosure from closed outputs across all L2 disciplines — performance, capital, liquidity, ALM, close, regulatory reporting, FP&A, and tax — into a single consistent document. The pack is available for CFO review on the first day of reporting.
Problem to solve: Quarterly board packs and investor disclosures are assembled by Finance, IR, and Controllers drawing on outputs from eight L2 disciplines produced at different times and in different formats. Cross-section consistency — NIM figures reconciling across the management accounts, ALCO pack, and investor release — is checked manually, and a complete draft is rarely available before the penultimate day.
Solution: Agent reads the closed L2 outputs and applies the bank's standard pack structure — headline performance, capital and liquidity position, ALM summary, regulatory position, and outlook — populating each section from the authoritative source for that discipline. Cross-section consistency is checked automatically; figures that differ across sections are flagged before CFO review. The CFO edits for judgment and forward framing.
OKR objective: The quarterly CFO board pack and investor disclosure are assembled from closed L2 outputs across all Finance disciplines into a consistent document available for CFO review on the first day of the reporting window.
OKR KR [Adoption]: Agent-produced CFO board pack used for ≥4 quarterly reporting cycles within year 1; all 8 L2 disciplines covered in each cycle.
OKR KR [Acceptance]: ≥85% of assembled packs accepted by the CFO for distribution without material structural amendment; cross-section figure consistency errors flagged and resolved before CFO review in ≥97% of reviewed cycles.
OKR KR [Cycle]: Complete CFO board pack available for CFO review on day 1 of reporting, vs. penultimate day in the prior manual process.

### CARD 5 [New opps|M] Continuous CFO Financial Posture
urn: urn:financial-services:scenario:finance-treasury/cfo-continuous-financial-posture
intent: Agent maintains a continuously updated financial posture for the CFO across all eight L2 disciplines — capital, liquidity, ALM, FP&A, performance, close, regulatory reporting, and tax — refreshed from live feeds and available on demand between formal reporting cycles.
Problem to solve: Between formal reporting cycles, the CFO holds a point-in-time picture from the last set of L2 reports. Intra-period movements in capital headroom, liquidity ratios, NIM trajectory, or tax provision are visible only when the next scheduled report is assembled; emerging cross-function patterns are not surfaced until both appear in their respective monthly reports.
Solution: Agent reads current data feeds across all L2 disciplines on a rolling basis — regulatory capital feeds, treasury liquidity positions, ALM model outputs, FP&A tracking actuals, and tax provision movements — and maintains a continuously updated posture summary in the CFO's house format. Cross-function threshold breaches trigger a proactive alert with attributed narrative; L2 teams retain ownership of their data and analytical conclusions.
OKR objective: The CFO holds a continuously updated financial posture across all eight L2 disciplines — capital, liquidity, ALM, FP&A, performance, close, regulatory reporting, and tax — refreshed from live feeds and available on demand between formal reporting cycles.
OKR KR [Adoption]: Agent-maintained posture summary accessed by the CFO on ≥80% of working days between formal reporting cycles within year 1; all 8 L2 disciplines covered in each refresh.
OKR KR [Acceptance]: ≥85% of cross-function threshold breach alerts rated as accurate and decision-relevant by the CFO without requiring L2 team correction; posture data reconciles to the next formal L2 report in ≥97% of sampled cells.
OKR KR [Cycle]: Intra-period cross-function position available on demand between formal reporting cycles, vs. waiting for the next scheduled monthly report in the prior process.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
