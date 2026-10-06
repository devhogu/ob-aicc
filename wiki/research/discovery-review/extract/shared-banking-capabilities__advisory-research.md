# 

source: html-alt/financial-services/en/shared-banking-capabilities/advisory-research/index.html


[PAGE TEXT]
Earnings call synthesis
Rapid extraction and synthesis of management guidance, financial metric revisions, and forward-looking commentary from earnings call transcripts — compared against prior periods and analyst consensus — within the compressed post-earnings window. Earnings calls generate 60-90 minutes of transcript content per issuer; analysts covering 20-50 issuers cannot process, compare, and synthesize every transcript within the window when earnings seasons concentrate calls across a narrow period.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] Earnings call historical guidance tracker
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/earnings-call-synthesis/earnings-call-historical-guidance-tracker
intent: Automated accumulation of management guidance statements from earnings call transcripts into a structured per-issuer, per-metric guidance history — capturing the guidance given, the period it covered, and the actual outcome versus guidance at period close. The guidance accuracy record supports analyst assessment of management credibility and the weight to assign to forward guidance in current-period analysis.
Problem to solve: Management guidance credibility — whether an issuer's forward statements have historically been accurate, conservative, or optimistic — is institutional knowledge held by experienced analysts and not systematically available to the broader research team. Assessing guidance credibility requires tracing multiple prior earnings transcripts per issuer; rebuilding this history manually for each analysis consumes time that is not available within the post-earnings window.
Solution: Agent extracts forward guidance statements from each earnings transcript on ingestion, tags them by metric and period, and appends them to a per-issuer guidance history record alongside the actual outcome at period close. Analysts access the guidance history at the start of each earnings analysis, with a pre-computed guidance accuracy score per issuer and per metric type available for direct use in the research note.
OKR objective: A structured per-issuer guidance history is maintained from earnings transcript extraction and available to analysts at the start of each post-earnings analysis cycle.
OKR KR [Adoption]: Guidance history records covering ≥80% of the covered issuer universe available within 6 months of go-live.
OKR KR [Acceptance]: ≥90% of analyst teams report using the guidance history record in at least one earnings analysis within the first full earnings season after go-live.
OKR KR [Cycle]: Guidance history updated within 4 hours of transcript ingestion so the record is current before the analyst begins post-earnings review.

### CARD 2 [Enablement|M] Research Production Automation
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/earnings-call-synthesis/research-production-automation
intent: Agent extracts management guidance, financial metric revisions, and forward-looking commentary from earnings transcripts, and drafts the data-driven sections of research notes from model outputs and historical data, ready for analyst authoring of the investment thesis. The analyst receives a pre-populated draft covering financial performance narrative, valuation comparison, historical ratio tables, and required regulatory disclosures. Analyst effort concentrates on the investment summary, investment thesis, and risk assessment.
Problem to solve: Analysts covering 20 to 50 issuers cannot process and publish on every earnings transcript within the post-earnings window when earnings seasons concentrate calls across a narrow period. The data-driven sections of each research note — financial performance narrative, valuation comparison, historical ratio tables, and regulatory disclosures — follow a consistent format but consume the majority of production time, leaving less time for the investment thesis and risk assessment that represent analyst value-add. Publication delays during earnings season reduce the commercial relevance of research output to institutional clients.
Solution: Agent reads earnings transcripts, extracts management guidance, financial metric revisions, and forward-looking commentary, and compares against prior period and consensus estimates. For full research notes, agent generates the data-driven sections from financial model outputs — financial performance narrative, valuation comparison, historical ratio tables, and required regulatory disclosures. Analyst authors the investment summary, investment thesis, and risk section from the pre-populated draft, concentrating effort on the sections that carry the most advisory value.
OKR objective: Data-driven sections of research notes — financial performance narrative, valuation comparison, historical ratio tables, and required regulatory disclosures — are drafted from earnings transcript extraction and model outputs and available for analyst authoring of the investment thesis within the post-earnings publication window.
OKR KR [Adoption]: Agent used to produce data-driven sections for ≥80% of research notes published during earnings season within year 1; all prescribed data-driven section types covered.
OKR KR [Acceptance]: ≥85% of agent-drafted data sections accepted by analysts without material restatement; management guidance extraction accuracy from earnings transcripts confirmed at ≥90% on periodic editorial review.
OKR KR [Cycle]: Pre-populated research note draft available for analyst authoring within 4 hours of earnings transcript release, vs. 1–2 days of manual section production per note in the prior process.

### CARD 3 [Insights|M] Earnings call consensus deviation signal
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/earnings-call-synthesis/earnings-call-consensus-deviation-signal
intent: Systematic comparison of management guidance from earnings call transcripts against prior-period guidance and sell-side consensus estimates, producing a structured deviation signal for each covered issuer within the post-earnings window. Analysts receive a prioritised list of issuers where management guidance diverges materially from consensus, enabling them to concentrate analytical effort on the cases most likely to require a rating or target-price revision.
Problem to solve: Analysts covering 20 to 50 issuers cannot read, compare, and rank-order every earnings transcript against consensus within the compressed post-earnings publication window. Issuers where management guidance diverges most from consensus represent the highest-priority analytical workload; without systematic comparison, triage is informal and dependent on analyst familiarity with each issuer's prior guidance cadence.
Solution: Agent reads each earnings transcript, extracts the management guidance points relevant to covered financial metrics, and compares them against prior-period guidance and the consensus estimate set. It produces a ranked deviation report — by issuer and metric — flagging the direction and magnitude of the divergence and surfacing the specific transcript passages that support each deviation signal for analyst review.
OKR objective: Management guidance deviations from consensus are ranked and available for analyst triage within the post-earnings window for all covered issuers.
OKR KR [Adoption]: Consensus deviation report used for ≥80% of covered issuers during the first full earnings season after go-live.
OKR KR [Acceptance]: ≥85% of top-ranked deviation signals confirmed as analytically material by the covering analyst; fewer than 15% dismissed as noise.
OKR KR [Cycle]: Deviation report available within 2 hours of transcript release, enabling analyst rating review within the same trading session.

[PAGE TEXT]
Client suitability assessment
Documentation of the suitability assessment for each advisory recommendation — evaluating whether the proposed investment is appropriate for the client given their declared risk tolerance, investment objectives, financial situation, investment experience, and time horizon. Under NBK/ARDFM investment services regulation and NBKR suitability rules, the assessment must be documented for each material recommendation and retained for supervisory review. For advisory teams managing large client books, suitability documentation creates a significant compliance workload.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] Client Suitability Documentation
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/client-suitability-assessment/client-suitability-documentation
intent: Agent generates the suitability assessment documentation for a proposed investment recommendation — cross-referencing client profile data against product characteristics — ready for relationship manager review and sign-off. The assessment covers the client's declared risk tolerance, investment objectives, financial position, investment experience, and time horizon against the product's risk characteristics and regulatory classification. The relationship manager reviews, confirms appropriateness given forward-looking client context, and signs off.
Problem to solve: Relationship managers must document suitability assessments for each material advisory recommendation under NBK/ARDFM investment services regulation and NBKR suitability rules. For advisory teams managing large client books, suitability documentation creates a compliance workload that displaces time from client dialogue and relationship development. Manual documentation quality varies across advisors and is subject to completeness gaps identified only during post-dispatch compliance review.
Solution: When a relationship manager proposes a product recommendation, agent reads the client's current profile data and the product's risk characteristics and regulatory classification. It generates the suitability assessment documentation in the prescribed format with the cross-reference rationale, covering all required disclosure elements under applicable NBK/ARDFM and NBKR rules. The relationship manager reviews the draft, confirms appropriateness in light of any forward-looking client context, and signs off before the recommendation is communicated.
OKR objective: Suitability assessment documentation for every material advisory recommendation is generated from client profile data and product characteristics in the format required by NBK/ARDFM and NBKR, ready for relationship manager review and sign-off.
OKR KR [Adoption]: Agent used to generate suitability documentation for ≥90% of material advisory recommendations within 12 months of go-live.
OKR KR [Acceptance]: ≥90% of agent-drafted suitability assessments accepted by relationship managers without material amendment; Compliance QA confirms required disclosure completeness in ≥97% of sampled assessments.
OKR KR [Cycle]: Suitability documentation available for RM review within 15 minutes of recommendation proposal, vs. 30–60 minutes of manual drafting per case in the prior process.

### CARD 5 [Automation|S] Suitability refresh trigger monitoring
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/client-suitability-assessment/suitability-refresh-trigger-monitoring
intent: Automated monitoring of client profile events — life-stage changes, declared financial position updates, product maturity, and inactivity thresholds — that trigger a suitability reassessment obligation under NBK/ARDFM and NBKR rules. Agent drafts the refresh notification to the relationship manager with the specific trigger event and the required reassessment scope, ready for dispatch.
Problem to solve: Suitability reassessment obligations arise from client profile events that are recorded in disparate systems — CRM, product administration, and periodic client review schedules — without a consolidated trigger mechanism. Missed reassessment obligations constitute a regulatory breach under NBK/ARDFM investment services rules; they are typically identified only at examination or when a complaint references an outdated profile.
Solution: Agent monitors client profile events across CRM and product administration for the prescribed trigger conditions — declared profile change, product maturity, inactivity period — and drafts a reassessment notification to the responsible relationship manager. The notification identifies the specific trigger event, the client, and the scope of profile dimensions requiring refresh, enabling the relationship manager to schedule the client dialogue and initiate the updated assessment.
OKR objective: Suitability reassessment obligations arising from client profile events are identified and assigned to the responsible relationship manager without manual monitoring.
OKR KR [Adoption]: Agent-produced reassessment triggers used for ≥90% of obligatory reassessment events within 9 months of go-live.
OKR KR [Acceptance]: ≥92% of agent-generated triggers confirmed as valid reassessment obligations by relationship managers; fewer than 8% dismissed as false triggers.
OKR KR [Cycle]: Trigger notification issued to relationship manager within 1 business day of the profile event, vs. next portfolio review cycle in the prior process.

### CARD 6 [Insights|M] Suitability assessment gap analytics
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/client-suitability-assessment/suitability-assessment-gap-analytics
intent: Continuous scanning of the completed suitability assessment population to identify profile-product mismatches, incomplete field patterns, and advisor-level deviation from the prescribed assessment framework. The analysis surfaces cases where the documented rationale does not address all required profile dimensions, enabling compliance to target review resources on the highest-risk segments of the assessment book.
Problem to solve: Compliance review of suitability assessments operates on sampled populations and scheduled file reviews; systemic documentation gaps and advisor-level deviation patterns are identified weeks after they accumulate. Under NBK/ARDFM investment services regulation and NBKR suitability rules, all material advisory recommendations require documented suitability assessment; gaps identified at examination represent a regulatory breach across the period in which they occurred.
Solution: Agent reads completed suitability assessment records and classifies each against the prescribed profile-dimension checklist — risk tolerance, objectives, financial situation, experience, and time horizon — flagging incomplete rationale and scoring advisor-level adherence. Compliance receives a ranked gap report by advisor, product type, and client segment, with the specific missing dimensions identified per case, enabling targeted pre-examination remediation and ongoing coaching prioritisation.
OKR objective: Suitability assessment compliance gaps are identified continuously across the full advisory book rather than on sampled post-hoc review cycles.
OKR KR [Adoption]: Agent-produced gap report covers 100% of completed suitability assessments within 6 months of go-live, replacing sampled review as the primary gap-detection mechanism.
OKR KR [Acceptance]: ≥85% of flagged gaps confirmed as genuine by compliance reviewers on periodic quality check; false-positive rate below 15%.
OKR KR [Cycle]: Gap report available to compliance within 24 hours of assessment completion, vs. next scheduled review cycle in the prior process.

[PAGE TEXT]
Issuer & sector research note drafting
Production of structured research notes — equity or fixed income — covering investment summary, financial analysis, valuation, risk factors, and required regulatory disclosures for a covered issuer or sector. Under NBK/ARDFM MiFID II-equivalent rules, research notes must carry prescribed disclosures on conflicts of interest, analyst certification, and regulatory classification. The data-driven sections of each note are built from financial model outputs and historical data; the analytical sections require the analyst's investment judgment.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] Research note disclosure compliance check
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/issuer-sector-research-drafting/research-note-disclosure-compliance-check
intent: Pre-publication compliance check of research note drafts against the prescribed disclosure checklist — analyst certification, conflict of interest declaration, regulatory classification, and required risk warnings — before submission to the compliance gating queue. Agent flags missing or non-compliant disclosure elements with the specific requirement and the applicable rule reference, enabling the analyst to resolve gaps before the note enters the compliance queue.
Problem to solve: Under NBK/ARDFM MiFID II-equivalent rules, research notes failing mandatory disclosure requirements must be withheld from publication and returned for correction; compliance gating catches deficiencies after the analyst has completed the note, creating rework at the end of the production cycle. The disclosure checklist varies by issuer type, product class, and regulatory jurisdiction; compliance with every applicable requirement is not reliably internalized by all analysts, particularly for cross-border research covering multiple regulatory regimes.
Solution: Agent reads the research note draft against the applicable disclosure checklist for the issuer type, product class, and regulatory regime, and produces a gap report identifying missing or non-compliant disclosure elements with the specific rule reference. The analyst resolves flagged gaps before submitting to the compliance queue, reducing rework cycles and compression of the publication window.
OKR objective: Research note disclosure gaps are identified by the authoring analyst before compliance queue submission, reducing rework cycles in the publication process.
OKR KR [Adoption]: Pre-publication compliance check used on ≥90% of research notes before queue submission within 6 months of go-live.
OKR KR [Acceptance]: ≥95% of compliance queue rejections for disclosure deficiency eliminated within 9 months; analyst acceptance of agent gap flags above 90%.
OKR KR [Cycle]: Compliance gap report available within 15 minutes of draft submission so the analyst can resolve gaps within the same authoring session.

### CARD 8 [Insights|S] Research coverage gap signal
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/issuer-sector-research-drafting/research-coverage-gap-signal
intent: Continuous monitoring of material events — earnings releases, credit rating actions, regulatory filings, and M&A announcements — across the covered universe to flag issuers where a research note update is warranted based on the materiality of the event. The research desk receives a prioritised update queue ranked by estimated impact on the covered issuer's investment thesis, enabling proactive publication ahead of client enquiries.
Problem to solve: Material events triggering an obligation or commercial rationale to update research occur continuously across the covered issuer universe; identification of which events are material enough to warrant a note update relies on individual analyst awareness rather than systematic monitoring. Research updates published after institutional clients have already acted on market events reduce the commercial value of the research product and erode the desk's advisory standing.
Solution: Agent monitors earnings releases, credit rating actions, regulatory filings, and disclosed M&A events for all covered issuers and classifies each event against the issuer's current investment thesis for materiality. It produces a daily ranked update queue for the research desk, with the specific event, the affected thesis element, and the suggested update scope — full note revision, earnings flash, or commentary addendum — for each flagged issuer.
OKR objective: Material events across the covered issuer universe are identified and ranked for research update priority on a continuous basis.
OKR KR [Adoption]: Agent-produced update queue used by research desk for daily triage within 3 months of go-live; ≥80% of update obligations identified via the queue rather than analyst-initiated.
OKR KR [Acceptance]: ≥80% of top-ranked update signals acted on within 1 business day; fewer than 20% dismissed as non-material by the analyst.
OKR KR [Cycle]: Update queue available each morning before market open so the research desk can plan note production for the trading day.

### CARD 9 [Automation|M] Research note data section drafting
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/issuer-sector-research-drafting/research-note-data-section-drafting
intent: Automated drafting of the structured data-driven sections of equity and fixed-income research notes — financial performance narrative, valuation comparison, historical ratio tables, and required regulatory disclosures — from financial model outputs and historical data. The analyst receives a pre-populated draft covering all disclosure-obligated sections, concentrating authoring effort on the investment summary, investment thesis, and risk assessment.
Problem to solve: Under NBK/ARDFM MiFID II-equivalent rules, research notes must carry prescribed disclosures on conflicts of interest, analyst certification, and regulatory classification alongside the financial analysis sections. The data-driven sections — financial performance, valuation comparison, ratio tables, and disclosures — follow a consistent format but consume the majority of production time per note, leaving analysts limited time for the investment thesis and risk sections that carry the most advisory value.
Solution: Agent reads the financial model outputs and historical data for the covered issuer, drafts the financial performance narrative, valuation comparison, and historical ratio tables in the prescribed research note format, and appends the required regulatory disclosures. The analyst authors the investment summary, investment thesis, and risk assessment from the pre-populated draft, with the data-driven sections available for review rather than production.
OKR objective: Data-driven sections of research notes are drafted from model outputs and available for analyst authoring within the post-earnings publication window.
OKR KR [Adoption]: Agent-drafted data sections used in ≥75% of research notes published during the first full earnings season after go-live.
OKR KR [Acceptance]: ≥85% of agent-drafted data sections accepted by analysts without material restatement; required disclosure completeness confirmed at ≥97% on compliance review.
OKR KR [Cycle]: Pre-populated draft available within 4 hours of model output availability, vs. 1 to 2 days of manual section production per note in the prior process.

[PAGE TEXT]
Portfolio review narratives
Quarterly production of personalized portfolio review narratives for advisory clients — covering portfolio performance attribution, benchmark comparison, asset allocation assessment, and recommended adjustments — in a format that satisfies the relationship documentation requirements under NBK/ARDFM advisory conduct rules. Each review narrative is personalized to the client's portfolio and objectives; the structure and disclosure language are standardized. Production across a large advisory book is the primary time constraint on the relationship manager's quarterly cycle.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|S] Review meeting pre-read assembly
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/portfolio-review-narratives/review-meeting-pre-read-assembly
intent: Automated assembly of the client pre-read pack for the quarterly advisory review meeting — portfolio summary, performance attribution, pending service items, and the draft agenda — delivered to the relationship manager before client preparation begins. The pre-read consolidates data from portfolio administration, CRM, and the client service queue into a single structured document.
Problem to solve: Relationship managers assemble quarterly review pre-reads manually from portfolio administration, CRM, and service queue systems; the assembly step consumes 60 to 90 minutes per client and is the primary scheduling constraint on the quarterly review cycle for large advisory books. Incomplete pre-reads — missing pending service items or stale portfolio data — lead to client queries that the relationship manager cannot address in the review meeting, creating follow-up obligations and reducing advisory quality perception.
Solution: Agent reads the client's portfolio data, performance attribution, CRM history, and open service items, and assembles the quarterly review pre-read in a standardised format — portfolio summary, performance attribution, pending items, and draft agenda — for relationship manager review. The relationship manager reviews and customises the draft agenda with forward advisory points before the client meeting.
OKR objective: Quarterly advisory review pre-reads are assembled from portfolio and CRM data and available to relationship managers without manual data consolidation.
OKR KR [Adoption]: Agent-produced pre-reads used for ≥85% of quarterly advisory review meetings within 6 months of go-live.
OKR KR [Acceptance]: ≥90% of relationship managers report pre-read completeness as sufficient for client meeting preparation without additional manual data retrieval.
OKR KR [Cycle]: Pre-read available 3 business days before the scheduled review meeting, enabling relationship manager preparation within a single working session.

### CARD 11 [Automation|M] Portfolio review narrative drafting
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/portfolio-review-narratives/portfolio-review-narrative-drafting
intent: Quarterly drafting of personalized portfolio review narratives for advisory clients — covering portfolio performance attribution, benchmark comparison, asset allocation assessment, and recommended adjustments — in the format required by NBK/ARDFM advisory conduct rules. Relationship managers review and personalise the draft with client-specific forward context before the quarterly review meeting.
Problem to solve: Each quarterly portfolio review narrative must be personalized to the client's portfolio and objectives while adhering to a standardized structure and required disclosure language under NBK/ARDFM advisory conduct rules. Production of review narratives across a large advisory book consumes the majority of the relationship manager's quarterly cycle, compressing the time available for client dialogue and advisory value-add.
Solution: Agent reads the client's portfolio positions, performance attribution data, benchmark results, and current asset allocation against the client's declared investment objectives, and drafts the quarterly review narrative in the prescribed format including required disclosure elements. The relationship manager reviews the draft, adds forward-looking advisory context specific to the client's situation, and approves the narrative before the quarterly meeting.
OKR objective: Quarterly portfolio review narratives for advisory clients are drafted from portfolio and performance data in the prescribed format and available for relationship manager review before the quarterly cycle deadline.
OKR KR [Adoption]: Agent-drafted review narratives used for ≥80% of the advisory book within the first two quarterly cycles after go-live.
OKR KR [Acceptance]: ≥85% of agent-drafted narratives accepted by relationship managers with minor personalisation only; compliance review confirms required disclosure completeness in ≥97% of sampled narratives.
OKR KR [Cycle]: Draft narrative available to relationship manager 5 business days before the quarterly review deadline, vs. 2 to 3 days of manual drafting per client in the prior process.

### CARD 12 [Insights|M] Portfolio drift advisory signal
urn: urn:financial-services:scenario:shared-banking-capabilities/advisory-research/portfolio-review-narratives/portfolio-drift-advisory-signal
intent: Continuous monitoring of client portfolio positions against declared investment objectives and agreed asset allocation bands, generating an advisory signal when drift exceeds prescribed thresholds or when a market event affects a material portfolio holding. Relationship managers receive a prioritised intervention queue with the specific drift dimension and the suggested rebalancing scope for each flagged client.
Problem to solve: Advisory client portfolios drift from agreed asset allocation bands between quarterly review cycles due to market movements and position changes; drift that accumulates beyond tolerance bands creates a suitability and conduct risk under NBK/ARDFM rules. Relationship managers monitor portfolio drift informally between reviews; the absence of systematic monitoring means that material drift may not be identified until the next scheduled review meeting.
Solution: Agent monitors each advisory client's portfolio positions continuously against declared investment objectives and agreed asset allocation bands, flagging portfolios where drift exceeds prescribed tolerance thresholds or where a market event materially affects a portfolio holding. It produces a ranked intervention queue for each relationship manager with the specific drift dimension — asset class, geographic, or sector deviation — and the suggested rebalancing scope, enabling proactive client contact between scheduled reviews.
OKR objective: Advisory client portfolio drift beyond agreed tolerance thresholds is identified continuously and flagged to relationship managers for proactive intervention between quarterly review cycles.
OKR KR [Adoption]: Agent-produced drift signal covering ≥90% of the advisory book within 6 months of go-live; relationship manager intervention queue used as primary between-cycle monitoring tool.
OKR KR [Acceptance]: ≥80% of drift flags confirmed as requiring client contact by relationship managers; fewer than 20% dismissed as within acceptable tolerance.
OKR KR [Cycle]: Drift signal available to relationship manager within 1 business day of threshold breach so proactive client contact can occur before the next scheduled review.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
