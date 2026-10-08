# Research report: ITSM and IT governance

Collected on 2026-10-08 by an independent research agent for the flow redesign (change C-FLOW-REDESIGN), from the brief in this folder. Source quality is stated in each report: claims marked unverified come from memory, and several official pages (SAFe, PMI, ITIL) were gated or paywalled, so summaries and practitioner pages were used.

**Research return: ITSM and governance practices for a light AICC process (about 690 words)**

**1. Best-fit practices**
1. **Standard change with a pre-agreed rule** (Portfolio, Program, decision-making). A repeatable, low-risk change is approved once, as a documented type with entry conditions, steps and a rollback. Each later instance needs no new approval. Map AICC run-rate work to this: a small request done within one Iteration under a standing Initiative is a standard change or service request. A three-person unit cannot afford a meeting per request.
2. **Change authority as a role, not a board** (decision-making). ITIL 4 lets the authority be a named person, a peer review, or automation. Use a named person per class: peer review for standard work, the Domain Owner for normal work, the Executive Sponsor for high-risk work.
3. **Peer review plus automation instead of external boards** (Team, controls). DORA found no evidence that external approval lowers change failure. It recommends peer review plus automated testing and monitoring. Use a Jira pull-request or review step with automated checks.
4. **Service and demand catalogue in one list** (Discover). ITIL 4 service catalogue management means a single consistent source about services and offerings. Keep one table with a row per offering (what you deliver, requester, standard or Initiative, size, approval class, risk tier). Your Discover scenario catalogue already is this. Scenarios become offerings once they repeat. Unmatched demand goes to the Funnel.
5. **Direct-Plan-Improve** (Portfolio, Program). Direction is strategic priorities, envelopes and guardrails, set yearly. Planning is the monthly Iteration and quarterly PI. Improvement is one short retrospective. This replaces three forum tiers with three activities, and one meeting can hold more than one of them.
6. **Service request management** (Team, Discover). A pre-defined request type has a fixed form, an owner and a target time. This fits the "small repeatable request" mode.
7. **Continual improvement register** (controls). One list of improvement ideas with an owner and a status. ITIL 4 treats this as a standing practice.
8. **Flow metrics from DORA** (Team, Program). Track change lead time, deployment frequency, change fail rate and recovery time. Use a lead-time-per-class view rather than WSJF recalculation for run-rate work.

**2. Decision rights and forums**
- **By rule, with no meeting:**
  - Intake: a request that matches a catalogue offering is accepted.
  - Run-rate: it is a standard change if it fits the entry conditions, which are an existing tier, no new data class, no new model and under N days (a number you set).
  - Pull from the Backlog: take the highest WSJF item within the WIP limit.
  - Acceptance: the stated exit criterion is met and the reviewer signs off.
- **By one named person:**
  - Initiative approval is the Domain Owner on the Initiative Brief.
  - Spending beyond the envelope goes to the Executive Sponsor.
- **In one forum:** a single monthly session handles Funnel ranking, the post-MVP decision (continue, pivot, defer, reject) and exceptions. Quarterly planning is the PI event. The yearly session sets strategic priorities, envelopes and guardrails, and can be a quarterly one extended.
- **Evidence:** the Brief, the MVP result against the exit criterion, risk-tier clearances, and flow data.
- **Emergency changes** go to a pre-named person immediately and get a short review afterwards.

**3. Artefacts**
- **Keep:**
  - The catalogue and its standard-change definitions, one per type.
  - The Initiative Brief and the post-MVP decision record, which is a short entry with date, decider, options and reason.
  - A risk-tier and clearance record per Initiative.
  - Jira items, which carry the Team-level history.
  - The change or request log, which can be the Jira history.
  - The improvement register.
- **Drop:**
  - Separate minutes of routine meetings.
  - Per-request change records for standard changes beyond the Jira item.
  - A forward schedule of change.
  - Duplicate status reports.
  - Full CAB packs.

**4. Avoid or discard**
- Multiple tiers of approval for the same decision, such as Scoped then Approval then Pull. Merge them where one person is the decider anyway.
- CAB-style boards for normal changes. Unverified: ITIL 4 itself says a CAB is optional and should not hear every change.
- Heavy service financial management. Keep envelopes and a simple cost-per-offering view; skip chargeback.
- Full ISO/IEC 20000 or COBIT 2019 implementation (unverified in detail). Use COBIT only as a checklist of governance objectives when mapping to the bank's own framework. For example, the APO and BAI domains cover portfolio and delivery.
- Relationship management as a separate process. At this size, the Domain Owner conversation is the practice.
- WSJF re-scoring for run-rate items. It is overhead where the rule already decides.

**5. Regulated-bank points**
- Standard changes work only if the rule is itself approved by the right body (model risk, information security) once, and kept under version control. Any input that changes the risk tier (new data class, new model, new vendor) makes the work not a standard change. Make that a hard exclusion in the definition.
- Segregation of duties: the person who makes a change should not be its sole approver, so peer review is the minimum. With three people this may need a reviewer from outside the unit, for example for high-risk tiers.
- Audit read access favours records that are append-only and tied to a person and date. Jira history and a Git history can serve, so avoid a second ledger.
- Emergency changes need a recorded after-the-fact review.
- Check whether the National Bank of the Kyrgyz Republic or the bank's policy fixes any retention periods. I have no verified source for this.

**6. Sources**
- DORA, "Streamlining change approval": https://dora.dev/capabilities/streamlining-change-approval/ (DORA / Google Cloud, current page; fetched; no login). Source for the lack of evidence for external boards.
- DORA, "DORA's software delivery metrics": https://dora.dev/guides/dora-metrics/ (DORA / Google Cloud, current page; fetched). Lists the five metrics, including change fail rate and deployment rework rate.
- itsm.tools, "Change Enablement in ITIL 4": https://itsm.tools/change-enablement/ (practitioner write-up, undated in my fetch; fetched). Source for standard changes as pre-approved and for the change authority options. It gives nothing on change-record content.
- AXELOS, "Service catalogue management, ITIL 4 practice guide": https://www.axelos.com/resource-hub/practice/service-catalogue-management-itil-4-practice-guide (AXELOS/PeopleCert). The search snippet gave the purpose statement. My fetch returned only a page header, so the full guide is probably behind a login or purchase. Treat as unverified beyond the purpose line.
- Unverified (memory only): the Direct-Plan-Improve model, ISO/IEC 20000, COBIT 2019 objectives, VeriSM, the SRE book and the book "Accelerate" (Forsgren, Humble, Kim, 2018). I did not fetch these. The detail on CABs being optional in ITIL 4 is also memory-based beyond what itsm.tools states.
