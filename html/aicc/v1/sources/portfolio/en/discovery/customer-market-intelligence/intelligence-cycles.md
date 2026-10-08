# Intelligence Cycles

The analytics and intelligence cycle set that anchors customer and market understanding — from segmentation refresh through retention review, competitive intelligence, and brand sentiment monitoring.

## Customer insights {#customer-insights}

### Segmentation refresh cycle {#segmentation-refresh-cycle}

- URN: urn:financial-services:flow:customer-market-intelligence/intelligence-cycles/segmentation-refresh-cycle
- Summary: Periodic review and update of the customer segmentation model — sampling current behavior, re-running the analytical model, validating segment stability, obtaining governance approval, and deploying updated segment assignments to marketing and product systems. The cycle anchor is elapsed time from data sample to live deployment.

The segmentation refresh cycle maintains the currency of the Bank's customer segmentation model — the classification of customers into behavioral, value-based, or needs-based groups that drives product targeting, campaign design, retention investment prioritization, and pricing decisions. GenAI compresses the validation and approval preparation stages — drafting the segment-stability narrative, highlighting the most significant boundary changes, and preparing the governance pack for approval — so the data science team concentrates on model calibration rather than documentation.

| Lens | Problem |
| --- | --- |
| Analyze | Segment migration patterns and behavioral shifts that signal a segmentation model becoming stale are visible only at the annual or quarterly refresh cycle boundary. Continuous monitoring of segment assignment stability — detecting cohort behavioral drift before it reaches the formal refresh trigger — is absent from the standard intelligence operating cycle. |
| Optimize | Segmentation model calibration — which variables drive segment differentiation, what the optimal number of segments is, whether the model produces commercially actionable boundaries — is assessed informally by the data science team at each refresh. Structured model comparison (alternative segmentation approaches, different variable sets, different cluster counts) is rarely conducted between major refresh cycles. |
| Automate | Segment stability assessment documentation, governance approval pack production, and segment-definition communication to consuming teams are structured, recurring tasks that follow a consistent format each cycle. Each is amenable to AI-assisted drafting with data science and governance review. |
| Enrich | Segment refresh retrospective findings — which segments proved unstable, which boundary changes were later reversed, which model variables drifted — are not captured in a structured form that improves the design of the next cycle's model. The Bank reconstructs the same analytical framework each refresh cycle without building on what earlier cycles learned. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| sample | Sample | Extract and prepare the analytical data sample | Extracts the customer transaction, product holding, and demographic data sample from the core banking and CRM systems for the segmentation model run. The stage that establishes the data foundation for all analytical work in the cycle. | Sample extraction requires coordination between the data engineering and data science teams across systems with different refresh cadences — core banking data, mobile banking event logs, and CRM contact records. Sample quality issues (missing transaction history for recently onboarded customers, stale demographic records) are identified only after the extract is complete, requiring partial re-extraction that delays the analysis stage. |
| analyze | Analyze | Run segmentation model and assess segment stability | Runs the segmentation model against the current data sample, assesses the stability of segment boundaries relative to the prior cycle, and identifies customer cohorts that have migrated materially between segments. The analytical core of the refresh cycle. | Segment stability assessment requires comparison of current-cycle assignments to prior-cycle assignments at the individual customer level, then aggregation to identify net migration flows. This comparison is performed manually by the data science team; the absence of a standard stability metric means different analysts apply different thresholds for material segment boundary change, producing inconsistent governance inputs across refresh cycles. |
| validate | Validate | Business stakeholder validation of segment definitions | Presents the updated segment definitions and stability assessment to commercial stakeholders — product, marketing, and segment heads — for business-sense validation. The stage that confirms the analytically derived segments are operationally useful before governance approval. | Business-sense validation is conducted as a workshop session where stakeholders review segment profiles and migration tables. The session absorbs two to three days of senior commercial time per cycle and frequently surfaces disagreements about segment boundary definitions that require the data science team to run additional model variations — extending the validation stage by one to two weeks. |
| approve | Approve | Governance approval of updated segment model | Obtains formal governance approval of the updated segmentation model from the credit risk, marketing, and data governance committees as required. The approval gate ensures the model meets data quality, fairness, and explainability standards before live deployment. | Governance approval packs for model updates are authored manually by the data science team and reviewed sequentially across multiple committees. The approval cycle adds four to six weeks between validated model and live deployment; during this window, the marketing and product teams are operating on an outdated segment assignment, reducing campaign relevance. |
| deploy | Deploy | Deploy updated segment assignments to production systems | Loads the approved segment assignments into the marketing automation, CRM, and product eligibility systems; updates the segment-to-product mapping tables; and distributes the updated segment definitions to all consuming teams. The stage that makes the refresh cycle's output operationally effective. | Segment assignment deployment involves coordinated updates across multiple systems with different deployment windows and change-management requirements. Deployment errors — mismatched customer IDs between the analytical data extract and the production CRM, or failed loads in downstream marketing automation — are identified after deployment and require rollback and re-run procedures. |

#### Segmentation Governance Pack Drafting

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/segmentation-refresh-cycle/segmentation-governance-pack-drafting
- Lens: Automation
- Complexity: S
- Intent: The AI agent drafts the governance approval pack for the updated segmentation model — segment-stability narrative, boundary-change summary, and committee-ready documentation — from the data science team's analytical outputs. The data science team reviews and submits; drafting effort is eliminated.
- Problem to solve: Governance approval packs for segmentation model updates are authored manually by the data science team, taking three to five days per cycle, before sequential review across credit risk, marketing, and data governance committees. Manual drafting delays the start of an approval cycle that already adds four to six weeks between validated model and live deployment, during which marketing and product teams operate on outdated segment assignments.
- Solution: The AI agent reads the current-cycle segmentation model outputs, prior-cycle assignments, and governance pack template, then drafts the stability narrative, boundary-change commentary, and committee submission. The data science team reviews the draft and submits for approval, concentrating effort on model calibration rather than documentation production.
- OKR: A committee-ready segmentation governance approval pack — covering segment-stability narrative, boundary-change summary, and supporting documentation — is drafted from the data science team's analytical outputs and available for team review within 48 hours.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces a draft governance pack for ≥90% of segmentation refresh cycles requiring committee approval from go-live. |
| Acceptance | ≥80% of AI-drafted governance packs accepted by the data science lead for committee submission with minor amendment or none. |
| Cycle | Governance pack drafting time reduced from 3–5 days of manual document assembly to ≤48 hours of AI-assisted review and submission. |

#### Segmentation Cycle Retrospective

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/segmentation-refresh-cycle/segmentation-cycle-retrospective
- Lens: New opps
- Complexity: S
- Intent: The AI agent produces a structured retrospective after each segmentation refresh cycle — capturing which segments proved unstable, which boundary changes were later reversed, and which model variables drifted — as a compounding knowledge record for subsequent cycle design.
- Problem to solve: Segmentation refresh retrospective findings are not captured in a structured form that improves subsequent cycle models. The data science team reconstructs the same analytical framework each refresh without reference to prior-cycle insights; boundary decisions that proved commercially invalid are repeated.
- Solution: The AI agent reads prior-cycle segment assignments, current-cycle model outputs, and post-deployment commercial performance data, then produces a structured retrospective identifying stability patterns, reversed boundary changes, and variable drift. The data science lead reviews the retrospective, which is appended to the segmentation knowledge base and referenced in the next cycle's model design brief.
- OKR: A structured retrospective after each segmentation refresh cycle — capturing segment instability findings, reversed boundary changes, and drifted model variables — is available as a compounding knowledge record for subsequent cycle design.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces a structured retrospective for ≥95% of completed segmentation refresh cycles within 30 days of cycle close. |
| Acceptance | ≥70% of retrospective findings rated as directly applicable to the next cycle's design decisions by the data science lead. |
| Cycle | Retrospective production cycle reduced from ad hoc post-cycle documentation effort to structured automated assembly completed within 5 days of cycle close. |

#### Segment Stability Continuous Monitor

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/segmentation-refresh-cycle/segment-stability-continuous-monitor
- Lens: Insights
- Complexity: M
- Intent: The AI agent monitors segment assignment stability on a continuous cadence between formal refresh cycles, detecting cohort behavioral drift before it reaches the formal refresh trigger. Segment heads receive an alert when boundary movement crosses a defined materiality threshold.
- Problem to solve: Segment migration patterns that signal a stale segmentation model are visible only at the quarterly or annual refresh cycle boundary. Customers exhibiting material behavioral shifts — high-value downgraders, emerging mid-tier — are identified retrospectively, after the commercial window for intervention has passed.
- Solution: The AI agent reads transaction, product-holding, and digital engagement feeds daily, recalculates segment assignment likelihood per customer, and detects cohorts where boundary movement exceeds the defined materiality threshold. Segment heads and the data science team receive a drift alert with the affected cohort profile and a recommended trigger assessment for an off-cycle refresh.
- OKR: Segment assignment stability is monitored continuously between formal refresh cycles, with an alert to segment heads when boundary movement crosses the defined materiality threshold — enabling intervention before the formal refresh trigger.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent monitors segment stability and evaluates materiality thresholds continuously from go-live, with ≥98% of scheduled daily evaluation cycles completed for ≥48 consecutive weeks. |
| Acceptance | ≥75% of boundary movement alerts confirmed as warranting segment review by the segment head on receipt. |
| Cycle | Segment drift detection cycle reduced from formal refresh cadence (quarterly or annually) to continuous monitoring with ≤24-hour alert latency from threshold crossing to segment head notification. |

#### Segmentation Model Calibration Sandbox

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/segmentation-refresh-cycle/segmentation-model-calibration-sandbox
- Lens: Optimize
- Complexity: M
- Intent: The AI agent generates structured comparisons across alternative segmentation approaches — different variable sets, cluster counts, and boundary definitions — so the data science team evaluates a wider model space before committing to the refresh-cycle model. The assessment replaces informal calibration judgment with a documented comparison record.
- Problem to solve: Segmentation model calibration is assessed informally at each refresh; structured comparison across alternative approaches is rarely conducted between major cycles. The data science team applies the same variable set and cluster count unless a material commercial concern prompts a review, leaving potential improvements in model granularity unexplored.
- Solution: The AI agent runs parameterized model variants against the current data sample — varying variable inclusion, cluster count, and boundary sensitivity — and produces a comparison table scored on stability, commercial discriminability, and segment size distribution. The data science team reviews the ranked alternatives and selects the model for validation, with the comparison record serving as governance documentation.
- OKR: Structured comparisons across alternative segmentation approaches — covering different variable sets, cluster counts, and boundary definitions — are available to the data science team before the refresh-cycle model commitment, expanding the evaluated model space without increasing analyst workload.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent generates a structured multi-approach comparison for ≥90% of segmentation refresh cycles requiring model calibration from go-live. |
| Acceptance | ≥75% of comparison outputs rated as materially expanding the model evaluation space by the data science lead on review. |
| Cycle | Model calibration scenario generation cycle reduced from 2–3 weeks of manual model-by-model analytical work to ≤3 days of AI-assisted parallel comparison production. |

### Retention review cycle {#retention-review-cycle}

- URN: urn:financial-services:flow:customer-market-intelligence/intelligence-cycles/retention-review-cycle
- Summary: Recurring cycle of churn risk detection, root-cause diagnosis, retention intervention design and execution, outcome tracking, and learning capture. The cycle anchor is elapsed time from at-risk signal detection to intervention execution.

The retention review cycle governs how the Bank identifies customers at material churn risk, diagnoses the behavioral and product drivers of that risk, designs and deploys retention interventions, tracks their effectiveness, and updates its retention models and playbooks from outcomes. GenAI compresses the detect-to-engage sequence — generating at-risk cohort profiles, drafting intervention briefs, and producing campaign content variants — so the retention team acts on signals within days rather than weeks.

| Lens | Problem |
| --- | --- |
| Analyze | Churn risk accumulates in customer behavior data between monthly scoring runs. Continuous monitoring of individual customer engagement signals — balance flows, transaction frequency, product interaction — would enable the Bank to act on retention risk before the customer has decided to leave. Such continuous monitoring is not yet standard practice in retail banking. |
| Optimize | Retention offer calibration — which offers produce the highest save rate for which risk profiles — is managed through qualitative campaign experience rather than structured A/B testing at scale. The Bank cannot systematically optimize its offer mix because outcome attribution across simultaneous campaigns is not tracked at the required granularity. |
| Automate | At-risk cohort profiling, retention brief preparation, campaign content variant drafting, and outcome tracking report production are structured, recurring tasks that follow a consistent pattern each cycle. Each is amenable to AI-assisted production, with retention team judgment concentrated on intervention design and escalation decisions. |
| Enrich | Retention intervention outcomes and churn driver patterns accumulate across cycles but are not organized into an institutional knowledge base that improves subsequent cycle design. The Bank's understanding of its customers' churn dynamics is rebuilt informally by whichever analyst leads the current cycle rather than from a compounding retention intelligence record. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| detect | Detect | Detect at-risk cohorts from behavioral signals | Identifies customers exhibiting behavioral patterns associated with churn risk — declining transaction frequency, product holding reduction, balance migration to other institutions, reduced digital engagement, or increased complaint activity. The stage that opens the retention cycle and determines the at-risk population for the current period. | At-risk cohort detection is performed through a monthly batch scoring run against the churn propensity model. The monthly cadence means that customers who exhibit acute churn signals — sudden balance outflow, account deactivation initiation — are not identified until the next scoring run; real-time churn signal detection is not yet standard practice in retail banking operations. |
| diagnose | Diagnose | Root-cause diagnosis by cohort and product driver | Diagnoses the principal drivers of churn risk for the identified cohort — product, pricing, service experience, competitor offer, or life-event trigger — at a level of specificity that enables targeted intervention design. The stage that translates a list of at-risk customers into an actionable retention brief. | Root-cause diagnosis for churn cohorts requires cross-referencing the churn-propensity scores with complaint data, product-holding changes, branch and contact-center interaction logs, and NPS survey responses. This cross-source analysis is performed manually by the retention analytics team for each cohort; the diagnostic is qualitative and inconsistently documented across cycles. |
| engage | Engage | Retention intervention design and execution | Designs and executes the retention intervention — channel selection, offer design, contact sequencing, and personalization — for the at-risk cohort. The stage where the diagnostic brief becomes customer-facing activity. | Retention intervention design is conducted by the CRM and campaign team from a limited playbook of pre-approved retention offer types. Personalization at the individual customer level — tailoring the offer and the communication to the specific driver of that customer's risk — is not operationally feasible with manual campaign design; the Bank sends uniform cohort offers that are poorly matched to individual customer situations. |
| track | Track | Intervention outcome tracking and cohort attrition measurement | Measures the outcome of the retention intervention — contacted versus uncontacted split, save rate by offer type, residual attrition in the treated cohort, and revenue impact of saves. The stage that determines whether the intervention cycle was effective. | Retention intervention outcomes are tracked through campaign response reports that measure contact rate and immediate offer acceptance. Longer-term retention outcomes — whether the saved customer remained active at ninety and one-hundred-and-eighty days — are not systematically tracked; the Bank cannot determine whether its retention interventions produce durable relationship saves or short-term deferrals. |
| learn | Learn | Model update and playbook refinement from outcomes | Updates the churn propensity model and retention playbook from the current cycle's intervention outcomes — which signals predicted genuine churn, which offer types produced durable saves, which cohort characteristics predicted intervention success. The stage that improves the next cycle's detection and intervention quality. | Retention model updates occur infrequently — typically annually alongside the segmentation refresh — rather than after each retention cycle. Intervention outcome data accumulates in campaign systems but is not fed back into the churn model or the retention playbook in a structured form; the Bank does not compound its retention intelligence cycle over cycle. |

#### Retention Cohort Profiling Brief

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/retention-review-cycle/retention-cohort-profiling-brief
- Lens: Automation
- Complexity: S
- Intent: The AI agent generates at-risk cohort profiles and retention intervention briefs each cycle from churn model outputs and diagnostic cross-reference data. The retention team reviews the brief and directs intervention design; profile assembly and brief production effort is eliminated.
- Problem to solve: At-risk cohort profiling requires the retention analytics team to cross-reference churn-propensity scores with complaint data, product-holding changes, branch interaction logs, and NPS responses. The diagnostic is qualitative, inconsistently documented across cycles, and absorbs analyst capacity that should concentrate on intervention design.
- Solution: The AI agent reads the batch churn-propensity scores and cross-references each at-risk customer against complaint, product, and interaction histories, then generates a cohort profile summarizing the top churn drivers and recommended intervention types by sub-cohort. The retention team reviews the brief at the start of each cycle and designs the intervention from the AI-produced diagnostic.
- OKR: At-risk cohort profiles and retention intervention briefs — generated from churn model outputs and diagnostic cross-reference data — are available to the retention team at the start of each cycle, with profile assembly and brief production effort eliminated.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces cohort profiling briefs for ≥95% of at-risk clusters identified in each scoring cycle for ≥12 consecutive monthly cycles post go-live. |
| Acceptance | ≥80% of cohort briefs confirmed as sufficient for intervention design without supplementary manual profiling by the retention team lead. |
| Cycle | Cohort brief preparation cycle reduced from 3–5 days of manual cohort assembly and narrative drafting to ≤24 hours of automated production. |

#### Real-Time Churn Signal Detection

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/retention-review-cycle/real-time-churn-signal-detection
- Lens: Insights
- Complexity: M
- Intent: The AI agent monitors individual customer engagement signals on a continuous cadence — balance flows, transaction frequency, product interaction, and digital engagement — detecting acute churn indicators between monthly scoring runs. The retention team receives an alert for customers crossing the high-risk threshold with sufficient lead time to act.
- Problem to solve: At-risk cohort detection depends on a monthly batch scoring run. Customers who exhibit acute churn signals — sudden balance outflow, account deactivation initiation, digital disengagement — are not identified until the next scoring run; the intervention window closes before the Bank is aware of the risk.
- Solution: The AI agent monitors transaction, balance, and digital-engagement feeds continuously, applies the Bank's churn-signal taxonomy at the individual customer level, and generates an alert when a customer crosses the real-time high-risk threshold. The retention team receives the alert with a preliminary driver profile and recommended contact priority, acting within the intervention window rather than after it.
- OKR: Acute churn signals — detected from continuous monitoring of balance flows, transaction frequency, product interaction, and digital engagement — trigger a retention team alert for customers crossing the high-risk threshold between monthly scoring runs.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent monitors engagement signals continuously and generates alerts for ≥95% of customers crossing the defined acute churn threshold within 24 hours of signal detection, across ≥48 consecutive weeks. |
| Acceptance | ≥70% of acute churn alerts confirmed as requiring retention intervention by the retention team lead on weekly review; churn rate among alerted customers who receive intervention tracked against the non-alerted at-risk baseline. |
| Cycle | Acute churn detection cycle reduced from monthly batch scoring to continuous monitoring with ≤24-hour alert latency from signal to retention team notification. |

#### Retention Offer A/B Optimization

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/retention-review-cycle/retention-offer-ab-optimisation
- Lens: Optimize
- Complexity: M
- Intent: The AI agent tracks retention intervention outcomes at the offer-type and cohort-profile level across simultaneous campaigns, producing a ranked offer-effectiveness matrix that the retention team uses to calibrate its offer mix each cycle. Attribution is maintained at the individual customer level to separate overlapping campaign effects.
- Problem to solve: Retention offer calibration is managed through qualitative campaign experience rather than structured A/B testing at scale. Outcome attribution across simultaneous campaigns is not tracked at the required granularity; the Bank cannot determine which offer type produces the highest save rate for which customer risk profile.
- Solution: The AI agent reads campaign response data and matched control groups at the individual customer level, applies offer-type and cohort-profile attribution, and produces a ranked effectiveness matrix covering save rate, durability at 90 and 180 days, and revenue impact. The retention team uses the matrix to adjust offer selection criteria for the following cycle, with the AI agent updating the matrix after each campaign closes.
- OKR: A ranked offer-effectiveness matrix — tracking retention intervention outcomes at offer-type and cohort-profile level across simultaneous campaigns with individual-level attribution — is available to the retention team for offer mix calibration each cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the offer-effectiveness matrix for ≥95% of scheduled monthly review cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥75% of offer-effectiveness rankings confirmed as directionally accurate by the retention team lead on monthly review; offer mix calibration decisions documented and tracked against subsequent save rate outcomes. |
| Cycle | Offer effectiveness analysis cycle moved from qualitative review of campaign experience to monthly automated matrix production within 48 hours of period close. |

#### Retention Intervention Personalization

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/retention-review-cycle/retention-intervention-personalisation
- Lens: Enablement
- Complexity: M
- Intent: The AI agent generates individual-level retention communication and offer recommendations from the cohort diagnostic, enabling the CRM team to execute personalized outreach at scale. The recommendation is calibrated to the specific churn driver identified for that customer rather than a uniform cohort offer.
- Problem to solve: Retention interventions are designed at the cohort level from a limited playbook of pre-approved offer types. Personalization at the individual customer level — tailoring the offer and communication to the specific driver of that customer's risk — is not operationally feasible with manual campaign design; uniform cohort offers are poorly matched to individual situations.
- Solution: The AI agent reads the per-customer churn driver diagnosis from the cohort profiling brief, maps each driver to the approved retention offer and communication template library, and generates an individual-level recommendation covering offer type, channel preference, and message framing. The CRM team reviews the recommendations for the highest-value segment and executes the campaign from the AI-prepared content.
- OKR: Individual-level retention communication and offer recommendations — calibrated to the specific churn driver identified for each customer rather than a uniform cohort offer — are available to the CRM team for personalized outreach execution at scale.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent generates a personalized retention recommendation for ≥90% of customers in the prioritized at-risk intervention queue on each weekly cycle for ≥48 consecutive weeks. |
| Acceptance | Save rate for customers receiving personalized AI-recommended offers ≥15% higher than the prior uniform-cohort-offer baseline on a 12-month cohort comparison. |
| Cycle | Individual retention communication and offer preparation cycle reduced from 2–3 days of manual CRM segmentation and copywriting to ≤4 hours of automated recommendation generation and CRM team review. |

#### Retention Intelligence Knowledge Base

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/retention-review-cycle/retention-intelligence-knowledge-base
- Lens: New opps
- Complexity: M
- Intent: The AI agent aggregates retention intervention outcomes, churn driver patterns, and model update records across cycles into a structured knowledge base, enabling the retention team to design each subsequent cycle from a compounding evidence record rather than from individual analyst memory.
- Problem to solve: Retention intervention outcomes accumulate in campaign systems but are not fed back into the churn model or retention playbook in a structured form. The Bank's understanding of its customers' churn dynamics is rebuilt informally by whichever analyst leads the current cycle; institutional retention intelligence does not compound over time.
- Solution: The AI agent reads closed-cycle intervention outcomes, model update logs, and churn driver diagnoses, structures the findings into a queryable retention knowledge base, and surfaces relevant prior-cycle patterns at the start of each new cycle's design brief. The retention team references prior evidence when selecting detection thresholds and offer mixes, with the AI agent flagging analogous prior situations and their outcomes.
- OKR: Retention intervention outcomes, churn driver patterns, and model update records are aggregated across cycles into a structured knowledge base, enabling the retention team to calibrate each subsequent cycle from a compounding evidence record.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent indexes retention cycle outcomes and churn driver findings for ≥95% of closed retention cycles within 14 days of cycle close, continuously from go-live. |
| Acceptance | ≥70% of knowledge base retrievals rated as directly applicable to current cycle design by the retention team lead. |
| Cycle | Prior-cycle retention evidence retrieval reduced from 1–2 days of manual report search and analyst recall to ≤1 hour of structured knowledge base query. |

## Market position {#market-position}

### Competitive intelligence cycle {#competitive-intelligence-cycle}

- URN: urn:financial-services:flow:customer-market-intelligence/intelligence-cycles/competitive-intelligence-cycle
- Summary: Recurring cycle of competitive signal scanning, analytical synthesis, leadership briefing production, and tracking of strategic moves by named competitors. The cycle anchor is elapsed time from signal emergence to decision-ready brief.

The competitive intelligence cycle produces the recurring view of the competitive landscape that strategy and commercial leadership use to calibrate product, pricing, and positioning decisions. GenAI enables near-continuous competitive monitoring by aggregating signals from public sources automatically and generating structured competitive summaries on a weekly or event-triggered cadence.

| Lens | Problem |
| --- | --- |
| Analyze | The competitive landscape is assessed at quarterly briefing cycle boundaries. Market-share shifts, competitor product launches, and pricing moves that occur between briefing cycles accumulate without a structured early-escalation mechanism. Commercial decisions made between briefing cycles are made without current competitive context. |
| Optimize | Competitive intelligence scope — which competitors to monitor, which signals to prioritize, which analytical frameworks to apply — is set by the strategy team based on current management priorities. Systematic coverage optimization (ensuring high-signal sources are covered proportionally to their competitive significance) is not performed; source and coverage gaps accumulate over time. |
| Automate | Signal aggregation, competitor-specific summary production, cross-competitor theme extraction, and briefing-format variants for different audiences are all structured, recurring production tasks. Each follows a consistent structure across cycles; the variable is the current-cycle signal content. These are strong candidates for AI-assisted production with strategy team editorial review. |
| Enrich | Competitive intelligence briefs from prior cycles, together with the subsequent commercial outcomes of the competitive moves that were assessed, represent a cumulative evidence base for calibrating competitive signal significance. This retrospective evidence is not systematically organized to improve the accuracy of the next cycle's competitive assessment. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| scan | Scan | Scan competitive signals from public and network sources | Collects competitive signals from regulatory filings, published financial results, press and social media, product announcements, recruitment patterns, and management network intelligence for the defined competitor set. The stage that determines the raw intelligence available for synthesis. | Signal scanning is conducted by strategy analysts using manual monitoring of a curated source list — regulatory portals, news aggregators, competitor websites, and LinkedIn. The monitoring is periodic; signals that emerge between scanning sessions are missed or identified late. Source breadth is limited by analyst time, meaning competitor moves in less-monitored channels (regulatory working groups, fintech partnership announcements) are under-represented in the synthesis. |
| analyze | Analyze | Analytical assessment of competitor moves and implications | Assesses the significance of collected signals — which competitor moves are strategic, which are tactical, which imply shifts in competitor positioning, pricing, or capability investment — and estimates their commercial and strategic implications for the Bank. The stage that transforms raw intelligence into assessed findings. | Competitive analysis is conducted by a small strategy team whose analytical bandwidth limits the depth of assessment across the full competitor set. The team applies consistent analytical frameworks to tier-1 competitors but covers tier-2 and fintech competitors only reactively when a specific move attracts management attention. The assessment is qualitative and largely undocumented between formal briefing cycles. |
| synthesize | Synthesize | Cross-competitor synthesis and strategic implications | Synthesizes assessed findings across competitors into a coherent competitive-landscape picture — relative positioning shifts, emerging competitive themes, and the aggregate strategic implications for the Bank's product, pricing, and market priorities. The stage that moves from individual competitor assessments to a portfolio-level competitive view. | Cross-competitor synthesis requires the strategy team to hold multiple competitor assessments in working memory simultaneously and identify the cross-cutting themes and relative positioning implications. The synthesis is produced once per quarter for the formal briefing cycle; between cycles, no mechanism exists to update the cross-competitor picture as new signals arrive. |
| brief | Brief | Competitive intelligence brief production and delivery | Produces and delivers the competitive intelligence brief to strategy, commercial, and product leadership — in the appropriate format for each audience (ExCo summary, product head competitive card, regional commercial brief). The stage where intelligence becomes leadership input. | Competitive intelligence briefs are produced in a uniform format for the full leadership audience, without calibration for the different competitive intelligence needs of product heads (feature-level comparisons), commercial leads (pricing and offer benchmarks), and ExCo (strategic positioning shifts). Audience-specific customization is manual and not systematically produced within the standard briefing cycle. |
| track | Track | Ongoing tracking of priority competitor strategic themes | Maintains a structured watch on named strategic themes identified in prior briefing cycles — competitor product launches, pricing moves, market entry or exit, and partnership announcements — between formal briefing cycles. The stage that ensures material developments are escalated on an event-triggered basis rather than waiting for the next cycle. | Between formal briefing cycles, there is no structured mechanism for tracking whether identified strategic themes have progressed. Significant competitor moves — a major product launch, a pricing restructuring, a regulatory application — are identified through informal channels and escalated inconsistently. The tracking function is performed through management awareness rather than a systematic watch mechanism. |

#### Competitive Signal Continuous Scan

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/competitive-intelligence-cycle/competitive-signal-continuous-scan
- Lens: Automation
- Complexity: S
- Intent: The AI agent monitors the defined competitor source universe on a continuous cadence — regulatory portals, product pages, press, and recruitment signals — and generates structured competitor-event entries for each material signal detected between formal briefing cycles. Strategy analysts review and escalate; manual periodic scanning is eliminated.
- Problem to solve: Competitive signal scanning is conducted manually by strategy analysts on a periodic schedule against a curated source list. Signals emerging between scanning sessions are missed or identified late; competitor moves in lower-monitored channels — regulatory working groups, fintech partnership announcements — are systematically under-represented in the intelligence synthesis.
- Solution: The AI agent monitors the defined source list continuously, detects competitor events against a defined signal taxonomy, and generates a structured event entry with competitor, event type, and preliminary significance assessment. The strategy team reviews the event queue daily, escalates material signals, and feeds confirmed events into the next briefing synthesis.
- OKR: Structured competitor-event entries from continuous monitoring of regulatory portals, product pages, press, and recruitment signals are available to the strategy team on the next business day after signal detection.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent monitors the full defined competitor source universe and produces structured event entries for ≥98% of scheduled daily scanning cycles from go-live. |
| Acceptance | ≥80% of structured competitor-event entries confirmed as material and accurately categorized by the strategy team on weekly sampling review. |
| Cycle | Competitor signal detection and entry production cycle reduced from weekly manual monitoring passes to daily automated scan with same-day event entry. |

#### Competitive Brief Audience Variants

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/competitive-intelligence-cycle/competitive-brief-audience-variants
- Lens: Enablement
- Complexity: S
- Intent: The AI agent generates audience-calibrated variants of the competitive intelligence brief — ExCo strategic positioning summary, product head feature comparison card, and commercial lead pricing benchmark — from a single synthesis input. The strategy team reviews each variant; customization effort is eliminated.
- Problem to solve: Competitive intelligence briefs are produced in a uniform format for the full leadership audience. Product heads require feature-level competitor comparisons; commercial leads require pricing and offer benchmarks; ExCo requires strategic positioning shifts. Audience-specific customization is manual and inconsistently produced within the standard briefing cycle.
- Solution: The AI agent reads the strategy team's synthesis and applies audience-specific brief templates — feature-table format for product heads, pricing grid for commercial leads, and strategic-narrative format for ExCo — generating three calibrated brief variants from a single analytical input. Each variant is reviewed and distributed by the strategy team within the standard briefing cadence.
- OKR: Audience-calibrated competitive intelligence brief variants — ExCo strategic positioning summary, product head feature comparison card, and commercial lead pricing benchmark — are available from each competitive brief cycle without separate manual derivation per audience.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent generates all three audience variants for ≥90% of competitive intelligence brief cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥80% of audience-variant outputs rated as appropriately calibrated by the respective audience head without requiring material rework. |
| Cycle | Audience variant production time reduced from 1–2 days of separate manual tailoring per audience to ≤2 hours of automated generation and review per cycle. |

#### Competitive Coverage Gap Audit

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/competitive-intelligence-cycle/competitive-coverage-gap-audit
- Lens: Optimize
- Complexity: S
- Intent: The AI agent audits the competitive monitoring source coverage against the defined competitor set and signal taxonomy, identifying unmonitored sources and coverage imbalances before they produce blind spots. The strategy team receives a quarterly coverage gap report with prioritized source additions.
- Problem to solve: Competitive intelligence scope and source coverage are set by the strategy team based on current management priorities. Gaps accumulate over time — competitor Telegram channels, fintech partnership announcements, regional news sources — and are discovered only when a material signal surfaces through an unmonitored channel after the fact.
- Solution: The AI agent maps the active monitoring source list against the full competitor set and a reference source taxonomy, scores each competitor-source combination on estimated signal density versus current coverage, and produces a ranked gap list with recommended source additions. The strategy team reviews the report quarterly and updates the monitoring configuration.
- OKR: An audit of competitive monitoring source coverage against the defined competitor set and signal taxonomy — identifying unmonitored sources and coverage imbalances — is available before each competitive briefing cycle closes.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent completes a coverage gap audit for ≥90% of scheduled competitive briefing cycles from go-live. |
| Acceptance | ≥75% of identified coverage gaps confirmed as material by the strategy team, resulting in source additions or explicit exclusion decisions. |
| Cycle | Coverage audit cycle reduced from periodic manual source review to automated audit completed within 4 hours of each brief cycle trigger. |

#### Competitive Intelligence Evidence Base

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/competitive-intelligence-cycle/competitive-intelligence-evidence-base
- Lens: New opps
- Complexity: M
- Intent: The AI agent maintains a retrospective evidence base linking prior competitive assessments to subsequent market outcomes — competitor product launches to observed share shifts, pricing moves to margin impact — calibrating the strategy team's signal-significance judgments across cycles.
- Problem to solve: Competitive intelligence briefs from prior cycles and the subsequent commercial outcomes of the competitive moves assessed are not systematically organized. The Bank cannot determine retrospectively which competitive signals predicted material outcomes; signal-significance calibration remains an informal team judgment that does not improve over time.
- Solution: The AI agent reads prior competitive intelligence outputs and links each assessed competitor event to subsequent observable outcomes — market-share data, product adoption trends, pricing announcements — tracking the accuracy of significance assessments over time. The strategy team reviews the outcome-attribution record before each major briefing cycle to recalibrate its signal-weighting criteria.
- OKR: A retrospective evidence base linking prior competitive assessments to subsequent market outcomes — competitor launches to observed share shifts, pricing moves to margin impact — is maintained continuously, available to each new competitive assessment cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent indexes competitive assessment outcomes for ≥90% of assessed competitor events within 30 days of observable market outcome availability. |
| Acceptance | ≥70% of evidence base retrievals rated as directly applicable to current competitive assessment calibration by the strategy team. |
| Cycle | Prior competitive outcome retrieval for new assessment work reduced from 1–2 days of manual record search to ≤1 hour of structured evidence base query. |

### Brand sentiment cycle {#brand-sentiment-cycle}

- URN: urn:financial-services:flow:customer-market-intelligence/intelligence-cycles/brand-sentiment-cycle
- Summary: Recurring cycle of brand and reputation signal listening, aggregation, analytical synthesis, alerting, and response coordination. The cycle anchor is elapsed time from reputation signal emergence to management awareness and response.

The brand sentiment cycle governs how the Bank monitors and responds to its brand and reputation standing across public channels — social media, press, regulatory commentary, customer complaint platforms, and market research. GenAI enables continuous brand signal aggregation — monitoring the defined source universe and generating structured alerts for material sentiment shifts — so the Bank responds to brand threats within hours rather than at the next weekly or monthly reporting cycle.

| Lens | Problem |
| --- | --- |
| Analyze | Brand signals accumulate across monitoring channels between reporting cycles. Significant sentiment shifts that begin in social media or Telegram channels and escalate to press or regulatory commentary progress through their early stages without management awareness. A continuous-form brand signal posture would enable the Bank to respond at the early-warning phase rather than after the escalation. |
| Optimize | Brand monitoring source coverage — which channels to monitor, with what frequency, at what signal-to-noise threshold — is set by the current monitoring tool configuration and analyst routine. Coverage gaps (unmonitored Telegram channels, complaint aggregator platforms, regional news sources) accumulate without a systematic coverage audit; the Bank discovers source gaps when a material signal surfaces through an unmonitored channel. |
| Automate | Signal aggregation, categorization, sentiment scoring, trend summary production, and alert generation are all structured, recurring tasks with defined criteria. Each is amenable to AI-assisted processing that compresses the signal-to-management-awareness interval from days to hours. |
| Enrich | Brand sentiment trends and their correlation with downstream outcomes — customer acquisition rate, complaint volume, deposit flow — are not analyzed systematically to build a predictive model of brand impact on commercial performance. The brand function tracks sentiment as an end in itself rather than as a leading indicator of commercial and reputational outcomes. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| listen | Listen | Monitor brand signals across channels and sources | Monitors the defined source universe for brand and reputation signals — social media mentions, press coverage, regulatory commentary, complaint platform activity, and market research inputs. The stage that determines the raw signal flow available for aggregation and analysis. | Brand monitoring is conducted through a combination of a commercial media monitoring tool, manual social media review, and periodic customer satisfaction surveys. The commercial tool covers press and mainstream social media; Telegram channel monitoring, complaint aggregator platforms, and regulator-published supervisory findings are tracked informally. Signal coverage is therefore incomplete and inconsistent across channels. |
| aggregate | Aggregate | Aggregate and categorize brand signals by theme and sentiment | Aggregates collected signals into a structured dataset categorized by theme (product complaint, service incident, brand campaign response, regulatory comment, peer comparison) and sentiment polarity. The stage that transforms a raw signal feed into a structured analytics input. | Signal aggregation across channels with different data formats requires manual categorization by the brand analytics team. Categorization consistency — applying the same theme taxonomy across different signal types — relies on individual analyst judgment; theme and sentiment categories drift across reporting periods, making trend analysis unreliable. |
| analyze | Analyze | Trend analysis and reputational risk assessment | Analyzes aggregated signals for material trends — sentiment trajectory, emerging theme concentrations, competitor brand comparison, and leading-indicator patterns that precede significant reputational events. The stage that assesses whether the current brand signal picture represents business-as-usual or an emerging risk. | Trend analysis is performed manually by the brand team from the aggregated signal dataset. The analysis is focused on current-period signal volume and sentiment rather than on leading indicators that precede reputational escalations; the Bank's analytical capability is reactive rather than predictive. |
| alert | Alert | Alert management to material sentiment shifts | Generates alerts to marketing, communications, and senior management for material sentiment shifts — significant volume spikes, rapid sentiment deterioration, or emerging themes with reputational escalation potential — outside the normal reporting cycle. The stage that ensures management awareness of brand risks on an event-triggered basis. | The alert threshold for management escalation is defined informally. In practice, analysts escalate when individual signals attract their attention rather than when the aggregate signal pattern crosses a defined materiality threshold. The result is inconsistent escalation — some material brand risks reach management attention late; others are escalated on individual signals that prove non-material in aggregate. |
| respond | Respond | Response coordination and communications execution | Coordinates the Bank's response to identified brand risks — communications strategy, customer messaging, press engagement, regulatory interaction, and campaign adjustment — and tracks the impact of the response on subsequent brand signal data. The stage that closes the loop between signal detection and institutional action. | Response coordination involves multiple teams — communications, marketing, legal, operations, and sometimes the CEO office — without a defined response protocol that specifies escalation path, approval authority, and response timeline by risk category. Coordination under time pressure produces inconsistent response quality; response effectiveness is not systematically tracked against subsequent brand signal data. |

#### Brand Signal Continuous Aggregation

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/brand-sentiment-cycle/brand-signal-continuous-aggregation
- Lens: Automation
- Complexity: S
- Intent: The AI agent monitors the defined brand signal source universe on a continuous cadence — press, social media, Telegram channels, complaint platforms, and regulatory commentary — and produces a structured daily signal feed categorized by theme and sentiment. The brand analytics team reviews the feed; manual aggregation across disparate sources is eliminated.
- Problem to solve: Brand signal aggregation spans sources with different formats — commercial media monitoring tools, manual social media review, and informal Telegram tracking — and relies on manual analyst categorization. Coverage is incomplete; categorization consistency degrades across reporting periods, making trend analysis unreliable.
- Solution: The AI agent reads the full defined source list on a continuous cadence, applies a unified theme and sentiment taxonomy, and generates a structured daily signal feed with source attribution and volume counts by theme. The brand analytics team reviews anomalies and updates theme assignments; trend analysis is performed against a consistent, AI-maintained categorization rather than manually recoded data.
- OKR: A structured daily brand signal feed covering press, social media, Telegram channels, complaint platforms, and regulatory commentary — categorized by theme and sentiment — is available to the brand analytics team from continuous source monitoring, eliminating manual aggregation across sources.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the structured daily brand signal feed for ≥98% of scheduled calendar days from go-live. |
| Acceptance | ≥85% of daily feeds rated as materially complete and consistently categorized by the brand analytics team on weekly sampling review. |
| Cycle | Daily brand signal collection and categorization cycle reduced from 2–3 hours of manual monitoring and aggregation to ≤15 minutes of brand analytics team review. |

#### Brand Materiality Alert Calibration

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/brand-sentiment-cycle/brand-materiality-alert-calibration
- Lens: Optimize
- Complexity: S
- Intent: The AI agent monitors the brand signal feed against defined materiality thresholds — volume spike, sentiment deterioration rate, and emerging theme concentration — and generates a management alert when any threshold is crossed. The threshold configuration is reviewed quarterly by the brand team against prior alert accuracy data.
- Problem to solve: Management escalation thresholds for brand risk are informal; analysts escalate when individual signals attract attention rather than when the aggregate pattern crosses a defined materiality level. Material brand risks reach management late; non-material signals are over-escalated. Escalation calibration does not improve over time.
- Solution: The AI agent applies defined materiality thresholds to the continuous brand signal feed — volume spike above rolling baseline, sentiment deterioration above a defined rate, or emerging theme reaching a defined share of total signal volume — and generates a structured management alert on threshold crossing. The brand team reviews alert accuracy quarterly and recalibrates threshold parameters based on prior false-positive and missed-escalation data.
- OKR: Management alerts are generated automatically when brand signal volume, sentiment deterioration rate, or emerging theme concentration crosses defined materiality thresholds, and the brand team recalibrates the thresholds quarterly from prior alert accuracy data.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent monitors brand signal inputs and evaluates threshold conditions for ≥99% of scheduled daily monitoring cycles from go-live; threshold configuration reviewed by the brand team in 100% of quarters. |
| Acceptance | ≥80% of materiality alerts confirmed as warranting management attention by the brand team on quarterly accuracy review. |
| Cycle | Time from threshold breach to management alert delivery reduced from 24–48 hours of manual monitoring to ≤2 hours of automated detection and alert generation. |

#### Brand Response Protocol Assistant

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/brand-sentiment-cycle/brand-response-protocol-assistant
- Lens: Enablement
- Complexity: S
- Intent: The AI agent identifies the applicable response protocol category from the brand alert content, surfaces the pre-defined escalation path and approval authority, and drafts a first-version response communication for the communications team's review. Response coordination is structured from the start of the incident rather than assembled under time pressure.
- Problem to solve: Brand risk response coordination involves communications, marketing, legal, and operations without a defined protocol specifying escalation path, approval authority, and response timeline by risk category. Coordination under time pressure produces inconsistent response quality; teams reconstruct the process for each incident.
- Solution: Communications, legal, and operations define a response protocol taxonomy once — escalation path, approval authority, and timeline by risk category. The AI agent reads the brand alert, classifies its risk category against that taxonomy, and generates a response brief: escalation path, approval authority, timeline, and a first-version draft communication. The communications team refines the draft and the Head of Communications approves it; the classification removes the overhead of determining who needs to be involved.
- OKR: A first-version response communication draft — with applicable protocol category, escalation path, and approval authority identified — is available to the communications team within minutes of a brand alert, enabling review-and-approve rather than draft-under-pressure workflows.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent generates a protocol-matched response draft for ≥90% of brand alerts classified above the defined severity threshold within 30 minutes of alert receipt. |
| Acceptance | ≥75% of AI-drafted response communications approved by the Head of Communications with minor amendment or none. |
| Cycle | Initial response draft preparation time reduced from 2–4 hours of manual protocol review and drafting to ≤30 minutes of AI-assisted review and sign-off. |

#### Brand Commercial Impact Model

- URN: urn:financial-services:scenario:flow/customer-market-intelligence/intelligence-cycles/brand-sentiment-cycle/brand-commercial-impact-model
- Lens: New opps
- Complexity: M
- Intent: The AI agent correlates brand sentiment trends against downstream commercial indicators — customer acquisition rate, deposit flow, NPS trajectory, and complaint volume — to build a predictive model of brand impact on commercial performance. Marketing and strategy leadership use the model to quantify the commercial case for brand investment.
- Problem to solve: Brand sentiment trends and their correlation with downstream commercial outcomes are not analyzed systematically. The brand function tracks sentiment as an end in itself rather than as a leading indicator of commercial performance; the commercial case for brand protection investment cannot be quantified from existing data.
- Solution: The AI agent reads multi-period brand sentiment scores alongside commercial KPI series — acquisition volume, deposit inflow, NPS scores, and complaint volume — and identifies leading-indicator relationships with statistical confidence ranges. Marketing and strategy leadership use the model to set brand health thresholds with commercial consequence and to quantify the expected commercial impact of sustained sentiment deterioration.
- OKR: A predictive model linking brand sentiment trends to downstream commercial indicators — customer acquisition rate, deposit flow, NPS trajectory, and complaint volume — is maintained on a continuous basis, giving marketing and strategy leadership a quantified view of brand materiality.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent refreshes the brand-commercial correlation model for ≥90% of scheduled update cycles for ≥12 consecutive months. |
| Acceptance | ≥75% of brand-to-commercial impact projections rated as directionally accurate by marketing and strategy leadership against observed outcomes on quarterly review. |
| Cycle | Brand materiality modeling cycle reduced from quarterly commissioned analysis to monthly automated refresh. |
