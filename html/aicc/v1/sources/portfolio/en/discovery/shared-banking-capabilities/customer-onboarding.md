# Customer onboarding

Customer onboarding is the regulated entry process through which the Bank establishes a customer's identity, assesses their risk profile, and activates their products — governed by AML/CFT and customer due diligence (CDD) requirements. KYC document collection, CDD risk classification, sanctions and PEP screening, and account activation each run as distinct operational steps with prescribed evidence standards. Onboarding failure or delay is both a regulatory exposure and a commercial drag — incomplete KYC triggers supervisory findings; slow activation loses customers at the moment of highest intent. **The opportunity for GenAI is to automate document extraction and CDD classification, compress the KYC review cycle, and surface early cross-sell signals at the point of activation.**

## Problems

### Identity verification {#identity-verification}

| Lens | Problem |
| --- | --- |
| Insights & analytics | KYC completion rates, document rejection reasons, CDD classification distributions, and sanctions-hit rates are tracked by the onboarding operations team but rarely synthesized into a cross-segment view. Relationship managers and the Head of Onboarding lack a current picture of where the KYC funnel is losing customers, which document types drive the most rework, and how CDD risk classifications are trending by product line. |
| Enablement | CDD risk classification for complex counterparties — corporates with multi-jurisdictional ownership structures, PEPs with layered beneficial ownership, or high-risk-country nationals — requires senior KYC analysts to work through source-of-funds narratives, corporate registry filings, and adverse media in multiple languages. The judgment bottleneck limits onboarding throughput for complex cases without adding senior headcount. |
| Automation | KYC document extraction — reading identity documents, utility bills, corporate registry filings, and financial statements to populate structured CDD fields — is high-volume, rule-governed, and format-predictable. Across retail, SME, and corporate onboarding, document processing consumes the largest share of KYC analyst time and is the strongest automation candidate in the onboarding workflow. |
| New business opportunities | Banks that reduce average KYC completion time — from days to hours for standard retail cases — convert more applicants at the point of intent and reduce acquisition cost per funded account. GenAI-backed document extraction and CDD automation creates a structural speed advantage that manual KYC workflows cannot replicate at the same quality threshold. |

## KYC document extraction {#kyc-document-extraction}

Structured extraction of customer identity, address, and beneficial ownership fields from submitted documents — including passports, national IDs, utility bills, corporate registry filings, and company accounts — into the CDD system of record. Under CDD rules, prescribed fields must be captured with source-document traceability. Extraction is currently manual for all document types, consuming the majority of KYC analyst time on standard cases.

### KYC Extraction and CDD Classification

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/kyc-document-extraction/kyc-extraction-cdd-classification
- Lens: Automation
- Complexity: M
- Intent: The AI agent extracts prescribed KYC fields from submitted identity and address documents into the CDD system, applies the Bank's risk-rating methodology to the extracted data, and routes standard cases for analyst spot-check while flagging EDD triggers for mandatory senior review. Standard-case classification — which follows a rule-based methodology for the majority of applicants — is completed without analyst intervention, concentrating analyst capacity on complex and elevated-risk cases. Source citations accompany each extracted field, maintaining the evidentiary audit trail required under CDD obligations.
- Problem to solve: KYC analysts populate CDD records manually from each submitted identity document, utility bill, and corporate registry filing — extraction consumes 15–30 minutes per applicant on standard retail cases and is the primary throughput constraint on the onboarding team. Standard-case classification follows a rule-based methodology for 80–90 percent of applicants, applying analyst capacity to low-judgment work that does not require professional assessment. Manual extraction introduces transcription error into CDD records; errors identified during periodic CDD refresh reviews require remediation work that compounds the original extraction cost.
- Solution: The AI agent reads submitted documents via OCR and structured extraction, populates prescribed CDD fields with source citations, and applies the Bank's risk-rating methodology to produce a classification recommendation with supporting rationale. Standard cases route for analyst spot-check; EDD triggers — PEP indicators, high-risk-country nationals, complex ownership structures — route for mandatory senior review. Analyst capacity concentrates on the complex and elevated-risk population where classification requires professional judgment and regulatory accountability.
- OKR: KYC fields are extracted from submitted identity and address documents into the CDD system with source citations, risk-rating is applied per the Bank's methodology, and standard cases route for analyst spot-check while EDD triggers route for mandatory senior review — concentrating analyst capacity on the complex and elevated-risk population.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used for KYC extraction and initial CDD classification for ≥90% of retail and SME onboarding applications within 12 months of go-live. |
| Acceptance | ≥95% of standard-case classifications confirmed correct on analyst spot-check; EDD trigger accuracy (PEP, high-risk-country, complex ownership) ≥90% on periodic Compliance QA review against CDD obligations. |
| Cycle | CDD extraction and classification recommendation available within 15 minutes of document submission without analyst data entry, vs. 15–30 minutes of analyst extraction time per standard case in the prior process. |

### KYC document completeness pre-screening

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/kyc-document-extraction/kyc-document-completeness-pre-screening
- Lens: Automation
- Complexity: S
- Intent: Automated pre-screening of submitted KYC document sets for completeness — identifying missing required documents, expired identity documents, and low-quality image submissions before the extraction and CDD workflow begins. Pre-screening reduces the rate of incomplete submission re-requests, which are a primary source of onboarding cycle time extension and customer attrition.
- Problem to solve: Incomplete or poor-quality KYC document submissions are identified after the documents enter the extraction and CDD workflow; the identification and re-request cycle extends onboarding time by 2–5 business days per affected customer. CDD rules require prescribed field completeness before account opening proceeds; processing incomplete submissions into the workflow consumes analyst time on cases that will be suspended for re-request.
- Solution: The AI agent screens each KYC document submission at intake against the prescribed document set for the customer type and jurisdiction, flagging missing documents, expired identity documents, and low-resolution images before the submission enters the extraction workflow. Customers receive a targeted re-submission request identifying the specific gap rather than a generic re-submission notice, reducing the re-submission cycle from multiple rounds to a single targeted request.
- OKR: KYC document set completeness is verified at intake before extraction and CDD workflow begins, reducing incomplete submission re-request cycles.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced completeness pre-screening covering ≥95% of KYC submissions within 6 months of go-live. |
| Acceptance | Incomplete submission re-request rate reduced by ≥40% vs. pre-deployment baseline; mean KYC submission-to-extraction cycle time improved by ≥1 business day within 12 months. |
| Cycle | Completeness pre-screening completed within 15 minutes of document submission so re-submission requests are issued within the same business day as the initial submission. |

### KYC extraction quality analytics

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/kyc-document-extraction/kyc-extraction-quality-analytics
- Lens: Insights
- Complexity: M
- Intent: Continuous analysis of KYC document extraction outcomes — tracking extraction accuracy rates by document type, field, and customer segment to identify the document types and field combinations where extraction errors occur at elevated frequency. The analysis drives targeted retraining or rule adjustment for the extraction model and surfaces the document submission patterns that produce the highest error rates for customer guidance improvement.
- Problem to solve: KYC document extraction errors — missed fields, incorrect values, or low-confidence outputs requiring manual review — are monitored at aggregate accuracy rates; the specific document type, field, and submission condition combinations that generate the highest error concentration are not systematically identified. Without granular extraction quality analytics, model improvement effort is allocated across the full extraction scope rather than concentrated on the highest-error document type and field combinations.
- Solution: The AI agent analyzes extraction outcome data — accuracy rate, confidence score distribution, and manual review trigger rate — by document type, field, and submission condition, producing a ranked error concentration report with the specific combinations requiring model improvement or customer guidance adjustment. The extraction model team uses the concentration report to prioritize retraining data collection and rule adjustment, with the field-level error evidence available for model validation documentation.
- OKR: KYC extraction error concentration by document type and field is identified each week and available for model improvement prioritization.

| Dimension | Key result |
| --- | --- |
| Adoption | Extraction quality analytics covering ≥90% of monthly KYC extraction volume within 6 months of go-live; used in ≥4 model improvement reviews per year. |
| Acceptance | Extraction accuracy rate improves by ≥10 percentage points within 12 months of first model improvement cycle informed by the analytics; manual review trigger rate reduced by ≥20%. |
| Cycle | Quality analytics refreshed weekly from extraction outcomes so model improvement decisions are based on the most recent document submission patterns. |

## Account setup & activation {#account-setup-activation}

Post-KYC workflow that provisions the customer's accounts and products in the core banking system, generates welcome communications, routes any outstanding CDD items for resolution, and confirms activation to downstream systems. Under account-opening rules, prescribed steps must complete in a defined sequence with documented audit trails. Multi-product onboarding — concurrent current account, savings, and lending product setup — requires coordinated orchestration across product-specific activation workflows.

### Welcome communication personalization

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/account-setup-activation/welcome-communication-personalisation
- Lens: Automation
- Complexity: S
- Intent: Automated drafting of personalized welcome communications for newly activated accounts — tailored to the customer's product set, segment, and any specific onboarding commitments made during the sales process — in the channel format appropriate for the customer's stated communication preference. The communications consolidate account activation confirmation, product usage guidance, and any pending onboarding steps into a single coherent sequence.
- Problem to solve: Welcome communications for newly activated accounts are generated from standard templates that do not reflect the customer's specific product set, onboarding commitments, or communication preferences; template-based communications carry generic product messaging that is not relevant to every product combination. Customers who receive welcome communications that do not reflect their actual products or pending setup steps contact the service channel for clarification, creating avoidable first-contact volume in the onboarding window.
- Solution: The AI agent reads the activated account record — product set, customer segment, onboarding commitments, and communication preference — and drafts the personalized welcome communication sequence tailored to the customer's specific product configuration and any outstanding activation steps. Operations reviews and dispatches the communication sequence, with the personalization rationale logged to the CRM record.
- OKR: Welcome communications for newly activated accounts are personalized to the customer's product set and onboarding commitments and dispatched without manual communication drafting.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted welcome communications used for ≥85% of new account activations within 6 months of go-live. |
| Acceptance | Onboarding-related service channel contact in the first 30 days post-activation reduced by ≥20% vs. pre-deployment baseline within 12 months. |
| Cycle | Welcome communication dispatched within 4 hours of account activation confirmation so the customer receives confirmation within the same business day as activation. |

### Account activation exception triage

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/account-setup-activation/account-activation-exception-triage
- Lens: Automation
- Complexity: M
- Intent: Automated classification and routing of account setup exceptions — provisioning failures, outstanding CDD items, and downstream system activation errors — generated during post-KYC account activation, with each exception matched to the resolution workflow and the responsible team. Exceptions are resolved in parallel across responsible teams rather than queued sequentially, reducing activation delay for multi-product onboarding.
- Problem to solve: Multi-product onboarding — concurrent current account, savings, and lending product setup — requires coordinated activation across product-specific workflows; provisioning exceptions in one product stream block activation across all concurrent streams when routing is sequential. Under account-opening rules, prescribed steps must complete in a defined sequence with documented audit trails; unresolved activation exceptions that delay account access create regulatory timing risk and customer attrition in the onboarding window.
- Solution: The AI agent reads each activation exception, classifies it by type — provisioning failure, CDD item, or downstream system error — and routes it to the responsible resolution team with the prescribed resolution workflow and the relevant audit trail requirement. Operations monitoring receives an exception dashboard with resolution status by product stream and customer, enabling management intervention before the regulatory activation deadline.
- OKR: Account activation exceptions are classified and routed to the responsible resolution team within the activation cycle without manual triage by operations staff.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced exception routing covering ≥90% of account activation exceptions within 6 months of go-live. |
| Acceptance | Mean activation exception resolution time reduced by ≥30% vs. pre-deployment baseline; regulatory activation deadline missed rate below 2% within 12 months. |
| Cycle | Exception routed within 30 minutes of detection so resolution can begin within the same business day as the activation attempt. |

### Onboarding completion rate analytics

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/account-setup-activation/onboarding-completion-rate-analytics
- Lens: Insights
- Complexity: M
- Intent: Analysis of account activation completion rates and drop-off points across the post-KYC onboarding workflow — by product type, channel, customer segment, and exception category — to identify the activation steps and exception types that produce the highest customer attrition. The analysis surfaces the specific workflow bottlenecks and exception patterns that account for the majority of activation failures, enabling targeted process improvement.
- Problem to solve: Account activation completion rates are reported at aggregate level; the specific workflow steps and exception types that drive completion failures — and the customer and product segments where attrition is highest — are not systematically identified from the activation event data. Onboarding attrition during account activation represents a direct cost of the KYC investment for customers who do not complete activation; without root-cause attribution, process improvement effort is allocated without evidence of where the highest impact changes lie.
- Solution: The AI agent analyzes activation event data across the post-KYC workflow, attributing completion failures to specific exception types, workflow steps, channels, and product segments, and produces a ranked bottleneck report with the attrition rate and volume per failure category. Operations management uses the bottleneck report to prioritize process improvement initiatives, with the exception category and segment evidence available for initiative scoping.
- OKR: Account activation completion failures are attributed to specific exception types and workflow steps and available for process improvement prioritization on a rolling basis.

| Dimension | Key result |
| --- | --- |
| Adoption | Completion rate analytics used in ≥2 process improvement planning cycles within the first 12 months of go-live. |
| Acceptance | Overall account activation completion rate improves by ≥10% within 18 months of first process improvement cycle informed by the analysis. |
| Cycle | Bottleneck report refreshed monthly from activation event data so improvement prioritization reflects the most recent onboarding cohort experience. |

## CDD risk classification {#cdd-risk-classification}

Assignment of the customer's AML/CFT risk rating — standard, enhanced, or simplified due diligence — based on prescribed risk factors including country of residence, business type, product profile, source of funds, and PEP status. In line with FATF Recommendation 10 and applicable CDD rules, the classification drives the depth of due diligence applied and the ongoing review frequency. Complex corporate structures and PEP-adjacent relationships require senior analyst judgment to classify correctly.

### Complex CDD Research Pack

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/cdd-risk-classification/complex-cdd-research-pack
- Lens: Enablement
- Complexity: M
- Intent: The AI agent assembles source-of-funds narrative, beneficial ownership map, adverse media summary, and sanctions screening results for complex corporate or PEP-adjacent onboarding cases, ready for senior analyst classification decision. The research pack covers available corporate registry and adverse media sources, maps the beneficial ownership structure, and presents findings with source citations for senior analyst review. The senior analyst reviews the pack, applies judgment on the classification decision, and documents the rationale.
- Problem to solve: Complex onboarding cases — multi-jurisdictional corporates, PEP-adjacent individuals, and high-risk-country nationals — require senior KYC analysts to research source of funds across corporate registry filings, financial statements, and adverse media in multiple languages before CDD classification can be reached. Each complex case consumes two to six hours of senior analyst time, and throughput on this population is the binding constraint on EDD capacity. The volume of EDD cases cannot be expanded to support business growth without either increasing senior analyst headcount or reducing the time each case requires.
- Solution: The AI agent reads submitted documents, pulls available corporate registry and adverse media sources, maps the beneficial ownership structure, and assembles a structured research pack with source citations. The pack covers source-of-funds narrative, beneficial ownership map, adverse media summary with severity indicators, and sanctions and PEP screening results in a format aligned to the Bank's CDD classification framework. The senior analyst reviews the pack, applies judgment on the classification decision, and documents the rationale; EDD throughput capacity is the primary outcome metric.
- OKR: The CDD research pack for complex corporate and PEP-adjacent onboarding cases — source-of-funds narrative, beneficial ownership map, adverse media summary, and sanctions screening — is assembled and ready for senior analyst classification before the analyst begins the classification review.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-assembled research pack used for ≥85% of EDD cases within 12 months of go-live. |
| Acceptance | ≥85% of research packs rated by senior analysts as complete and sufficient for the classification decision; source citation accuracy confirmed in ≥95% of sampled packs. |
| Cycle | EDD case pack assembly time reduced from 2–6 hours of senior analyst research to ≤30 minutes of analyst review and classification judgment. |

### CDD classification consistency analytics

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/cdd-risk-classification/cdd-classification-consistency-analytics
- Lens: Insights
- Complexity: M
- Intent: Systematic analysis of CDD risk classification decisions across the onboarding population — comparing classification outcomes for comparable customer profiles across analysts and teams to identify inconsistency patterns that indicate calibration gaps in the CDD risk assessment framework. Inconsistency signals are surfaced to compliance management for targeted analyst calibration or framework adjustment before a supervisory examination reviews the classification record.
- Problem to solve: In line with FATF Recommendation 10 and applicable CDD rules, the risk classification drives the depth of due diligence applied and the ongoing review frequency; inconsistent classification of comparable customer profiles produces uneven due diligence depth and creates a supervisory examination risk. Classification inconsistency — where analysts reach different outcomes for materially comparable profiles — is not systematically identified between examination cycles; it emerges as a finding during supervisory review of the classification record.
- Solution: The AI agent analyzes completed CDD risk classification decisions, grouping customers by profile comparability — country, business type, product, and PEP status — and identifies analyst pairs or teams where classification outcomes diverge materially for comparable profiles. Compliance management reviews the inconsistency report, determines whether the divergence reflects legitimate analytical judgment or calibration gaps, and directs targeted training or framework adjustment where gaps are confirmed.
- OKR: CDD risk classification inconsistency across analysts and teams is identified each month and available for compliance management intervention before examination.

| Dimension | Key result |
| --- | --- |
| Adoption | Consistency analytics covering ≥80% of monthly CDD classification volume within 6 months of go-live; used in ≥4 compliance calibration reviews per year. |
| Acceptance | Classification inconsistency rate for comparable profiles reduced by ≥30% within 18 months; supervisory examination findings on CDD classification consistency reduced to zero within 24 months. |
| Cycle | Inconsistency report refreshed monthly from completed classification decisions so calibration interventions are based on the most recent 30 days of classification activity. |

### Enhanced due diligence research pack

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/cdd-risk-classification/enhanced-due-diligence-research-pack
- Lens: Automation
- Complexity: M
- Intent: Automated assembly of the enhanced due diligence research pack for customers classified as high-risk or PEP-adjacent — aggregating adverse media, corporate registry ownership traces, sanctions and PEP database results, and source-of-funds documentation — into a structured analyst dossier before the EDD review begins. Pre-assembled research packs reduce the investigation preparation time for EDD cases, enabling the analyst to focus on the judgment assessment rather than the data gathering step.
- Problem to solve: Enhanced due diligence investigations require the compliance analyst to assemble adverse media results, corporate ownership traces, sanctions screening outputs, and source-of-funds documentation from multiple sources before the substantive risk assessment can begin. Pack assembly typically consumes 60–120 minutes per EDD case; for institutions onboarding significant volumes of high-risk customers, the assembly step is the primary constraint on EDD throughput and cycle time.
- Solution: The AI agent reads the customer's classification record and assembles the EDD research pack — adverse media search results, corporate registry ownership trace, sanctions and PEP screening outputs, and source-of-funds documentation — from connected source systems and approved external data providers. The compliance analyst receives the pre-assembled pack before beginning the EDD review, with each source cited and the pack structure aligned to the Bank's EDD assessment template.
- OKR: EDD research packs are assembled from internal and external data sources before the analyst begins substantive review, reducing investigation preparation time per case.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-assembled EDD packs used for ≥80% of high-risk and PEP-adjacent onboarding cases within 9 months of go-live. |
| Acceptance | EDD case preparation time reduced by ≥50% vs. pre-deployment manual assembly baseline; analyst confirmation of pack completeness ≥90% on quality review. |
| Cycle | Research pack assembled within 2 hours of EDD trigger so the analyst can begin substantive review the same business day. |

## Early cross-sell signals {#early-cross-sell-signals}

Behavioral and transactional signals in the first 30–90 days of the customer relationship that indicate readiness for additional products — salary credit patterns signaling payroll account consolidation, spending patterns suggesting credit card appetite, business turnover trajectory indicating SME lending eligibility. Banks that surface these signals early and act on them within the onboarding window convert single-product customers to multi-product relationships at a higher rate than those who rely on scheduled portfolio review cycles.

### Onboarding window activation coaching

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/early-cross-sell-signals/onboarding-window-activation-coaching
- Lens: Enablement
- Complexity: S
- Intent: Real-time guidance to relationship managers and digital channels on the specific activation actions and cross-sell contact timing that have proven most effective for customers matching the current customer's behavioral and demographic profile. The guidance draws on the accumulated outcome record across comparable prior onboarding cohorts to recommend the activation action sequence most likely to drive product adoption within the 90-day window.
- Problem to solve: Relationship managers responsible for new customer onboarding apply informal knowledge of effective activation sequences; the institutional learning accumulated across thousands of prior onboarding outcomes is not systematically accessible as guidance at the point of customer contact. New relationship managers and digital channels without institutional memory apply generic activation sequences rather than the sequences that have proven most effective for specific customer profiles.
- Solution: The AI agent reads the current customer's profile and behavioral signals and retrieves the activation action sequence — contact timing, channel, product offer sequence, and self-service activation prompts — that has produced the highest 90-day product adoption rates for comparable prior customers. The relationship manager or the digital channel receives the recommended activation sequence with the outcome evidence from comparable prior cohorts, enabling informed sequencing decisions rather than reliance on generic protocol.
- OKR: Relationship managers and digital channels receive evidence-based activation sequence guidance for each newly onboarded customer derived from comparable prior cohort outcomes.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced activation guidance used by ≥75% of relationship managers for new customer onboarding within 9 months of go-live. |
| Acceptance | ≥80% of relationship managers report that the guidance reflects effective sequences for the customer profiles they manage; 90-day product adoption rate improves by ≥10% vs. pre-deployment baseline within 12 months. |
| Cycle | Activation guidance refreshed from accumulated outcome data monthly so recommendations reflect cohort performance from the prior 12 months. |

### Early-Tenure Cross-Sell Signal

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/early-cross-sell-signals/early-tenure-cross-sell-signal
- Lens: Insights
- Complexity: M
- Intent: The AI agent monitors new customer transaction behavior on a weekly cadence during the first 90 days and surfaces product eligibility signals to the relationship manager when behavioral thresholds are crossed. The signal includes a product-specific eligibility assessment and a recommended next step. Relationship managers act on the signal within the high-engagement early-tenure window rather than at the next scheduled portfolio review.
- Problem to solve: Newly onboarded customers who meet eligibility criteria for additional products — based on salary levels, transaction volume, or savings behavior — are identified at the next scheduled portfolio review cycle rather than within the early-tenure period when customer engagement is highest. The early-tenure window, during which customers are most receptive to product additions, passes without timely cross-sell contact in the current campaign-cadence model. Revenue from the new-customer cohort is systematically below potential when eligibility signals are not surfaced at the point they emerge.
- Solution: The AI agent reads new customer transaction activity on a weekly cadence during the first 90 days; when behavioral signals cross the Bank's eligibility thresholds for additional products, the AI agent surfaces a cross-sell signal to the relationship manager. The signal includes the relevant product, the eligibility assessment based on observed behavior, and a recommended next step for the relationship manager to act on promptly. Relationship managers act within the high-engagement window; cross-sell conversion during the first 90 days is the primary metric tracked against the pre-deployment baseline.
- OKR: New customer cross-sell eligibility signals are surfaced to relationship managers within the first 90 days when behavioral thresholds are crossed, with a product-specific eligibility assessment and recommended next step provided for each signal.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced cross-sell signals delivered for ≥90% of new customers crossing eligibility thresholds within the first 90 days, within 12 months of go-live. |
| Acceptance | ≥70% of relationship managers take action on AI-surfaced signals within 5 business days; cross-sell conversion rate during the first 90 days improves by ≥15% vs. pre-deployment baseline. |
| Cycle | Cross-sell eligibility signal surfaced within 7 days of threshold crossing, vs. next scheduled portfolio review cycle (30–90 days) in the prior process. |

### Early-tenure product propensity scoring

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/early-cross-sell-signals/early-tenure-product-propensity-scoring
- Lens: Insights
- Complexity: M
- Intent: Propensity scoring for cross-sell product offers during the first 90 days of the customer relationship — using transactional signals, channel behavior, and demographic profile to rank the probability of conversion for each eligible product in the Bank's onboarding product set. The scoring drives next-best-offer sequencing for the onboarding relationship manager, concentrating outreach on the product-customer combinations with the highest conversion probability within the activation window.
- Problem to solve: Cross-sell contact during the onboarding window uses segment-level product sequencing rather than individual-level propensity signals; customers with strong early behavioral signals for specific products receive the same product contact sequence as customers with low propensity. Banks that convert single-product onboarding customers to multi-product relationships in the first 90 days retain them at materially higher rates; low conversion rates during the activation window result in single-product customers who are significantly harder to convert at later lifecycle stages.
- Solution: The AI agent reads the newly onboarded customer's transactional signals, channel usage, and declared profile, and produces a ranked propensity score across eligible products within the Bank's onboarding cross-sell set. Relationship managers and digital channels use the product propensity ranking to sequence cross-sell contact during the first 90 days, with the specific behavioral signals supporting each recommendation available for the contact rationale.
- OKR: Individual-level product propensity scores are available for all newly onboarded customers within the first 90 days to guide cross-sell contact sequencing.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced propensity scores used by relationship managers or digital channels for ≥80% of new customer cross-sell contact within 6 months of go-live. |
| Acceptance | Cross-sell conversion rate in the first 90 days improves by ≥15% vs. segment-level sequencing baseline within 12 months. |
| Cycle | Propensity scores updated weekly from accumulated transactional signals so the contact sequence reflects the customer's most recent behavioral pattern. |

## Sanctions & PEP screening {#sanctions-pep-screening}

Automated matching of customer identity data against the UN and other applicable sanctions lists, and against PEP databases, at onboarding and on a continuous basis as list updates occur. Under anti-money laundering rules, in line with FATF Recommendations 6 and 12, sanctions hits must be escalated immediately and PEP relationships require enhanced due diligence. False-positive alert rates on standard screening tools range from 90–98%, generating significant manual review volume.

### Sanctions false-positive triage

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/sanctions-pep-screening/sanctions-false-positive-triage
- Lens: Automation
- Complexity: M
- Intent: Automated pre-classification of sanctions and PEP screening alerts into probable true-positive and false-positive categories — using name match score, country, date of birth, and contextual discriminators — before manual analyst review begins. Pre-classification reduces the manual review burden for the 90–98% of alerts that are false positives, enabling analyst capacity to be concentrated on the true-positive population.
- Problem to solve: False-positive alert rates on standard screening tools range from 90–98%; each alert carries a mandatory review obligation under anti-money laundering rules, in line with FATF Recommendations 6 and 12, generating significant manual review volume regardless of the predicted outcome. Without pre-classification, analysts allocate equal review time to high-probability false positives and genuine match candidates, creating unnecessary volume load and increasing the mean time to identify and escalate true-positive hits.
- Solution: The AI agent reads each sanctions and PEP screening alert, scores the match against the name, country, date of birth, and contextual discriminators available in the customer record, and pre-classifies the alert as probable false positive or requiring analyst review. Probable false-positive alerts are routed to a streamlined confirmation queue with the discriminating evidence pre-populated; probable true positives and uncertain alerts are routed to the full analyst investigation queue.
- OKR: Sanctions and PEP screening alerts are pre-classified by false-positive probability before analyst review begins, concentrating analyst capacity on the probable true-positive population.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced pre-classification covering ≥95% of daily screening alert volume within 6 months of go-live. |
| Acceptance | Mean analyst review time per alert reduced by ≥40% for pre-classified false-positive queue; true-positive detection rate maintained at 100% on periodic quality review of false-positive closures. |
| Cycle | Alert pre-classification completed within 30 minutes of alert generation so the analyst queue reflects pre-classified alerts before the start of each review shift. |

### Sanctions screening rule calibration

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/sanctions-pep-screening/sanctions-screening-rule-calibration
- Lens: Insights
- Complexity: M
- Intent: Analysis of sanctions and PEP screening alert dispositions — true-positive rate, false-positive driver profile, and closed-alert characteristics — to identify the name matching thresholds and rule parameters that generate disproportionate false-positive volume without improving true-positive detection. The calibration analysis informs rule parameter adjustments that reduce false-positive burden while preserving detection coverage, with the evidence base required for model risk committee and regulatory documentation.
- Problem to solve: Sanctions screening rule parameters are set at system configuration and adjusted infrequently; the relationship between specific matching thresholds and observed false-positive rates by name type, country, and customer segment is not systematically analyzed against accumulated alert disposition data. Rule changes require documentation and model risk committee approval under AML/CFT supervisory expectations; without a calibration analysis grounded in disposition outcomes, rule change proposals lack the quantitative evidence base required for committee approval.
- Solution: The AI agent analyzes the accumulated alert disposition record — true-positive rate, false-positive driver by name matching threshold, country, and customer segment — and produces a calibration analysis identifying the specific parameter adjustments that would reduce false-positive volume by the estimated magnitude without reducing true-positive detection coverage. The compliance team uses the calibration output as the evidence base for the model risk committee rule change proposal, with the quantitative impact estimate and the detection coverage preservation argument documented.
- OKR: Sanctions screening rule calibration is grounded in disposition outcome analysis, providing the quantitative evidence base required for model risk committee rule change approval.

| Dimension | Key result |
| --- | --- |
| Adoption | Calibration analysis used in ≥1 model risk committee rule review within the first 18 months of go-live. |
| Acceptance | False-positive alert rate reduced by ≥20% following rule parameter adjustments informed by calibration analysis; true-positive detection rate maintained at 100% on post-change quality review. |
| Cycle | Calibration analysis refreshed semi-annually from accumulated disposition data so rule review proposals reflect the most recent 12 months of alert performance. |

### PEP and adverse media continuous monitoring

- URN: urn:financial-services:scenario:shared-banking-capabilities/customer-onboarding/sanctions-pep-screening/pep-adverse-media-continuous-monitoring
- Lens: Automation
- Complexity: M
- Intent: Continuous monitoring of existing customers against PEP database updates and adverse media sources — identifying newly PEP-designated individuals, family and close associates of newly designated PEPs, and adverse media events affecting current customers — and routing material changes to the CDD refresh queue. In line with FATF Recommendation 12, PEP status changes for existing customers trigger enhanced due diligence review; continuous monitoring ensures the obligation is met as list updates occur rather than at the next scheduled periodic review.
- Problem to solve: PEP database changes and adverse media events that affect existing customers occur continuously between periodic CDD review cycles; customers who become PEP-adjacent or who generate adverse media events after onboarding are not identified until the next scheduled review cycle. Under anti-money laundering rules, in line with FATF Recommendation 12, PEP status changes require immediate enhanced due diligence; identification at the next periodic review rather than at the time of the change represents a compliance gap for the intervening period.
- Solution: The AI agent monitors PEP database update feeds and approved adverse media sources for events matching existing customer records, classifies each event by type and materiality, and routes material changes to the CDD refresh queue with the specific triggering event and the required EDD scope. Compliance receives a daily event log of PEP and adverse media matches across the existing customer base, with the cases requiring immediate EDD action distinguished from those requiring documentation only.
- OKR: PEP status changes and material adverse media events affecting existing customers are identified at the time of the change and routed to the CDD refresh queue without waiting for the scheduled periodic review cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced continuous monitoring covering ≥90% of the existing customer base within 9 months of go-live, subject to data source access agreements. |
| Acceptance | ≥85% of routed PEP and adverse media events confirmed by compliance as correctly classified for type and materiality; compliance confirms EDD response completeness in ≥97% of sampled events. |
| Cycle | PEP designation changes routed to the CDD refresh queue within 24 hours of the database update, vs. identification at the next periodic review cycle in the prior process; daily event log reviewed by compliance and CDD refresh queue cases actioned within 2 business days of routing. |
