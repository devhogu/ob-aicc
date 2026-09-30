```yaml
id: AICC-REF-03-EN
title: Document Catalog
status: draft
revision: 0.7
created: 2026-09-29
revised: 2026-09-30
```

# Document Catalog

## 1. Purpose and scope

1.1. This catalog is the register of the documents in the charter folder. It states how documents are labeled, what the metadata
block at the top of each document means, how a document changes state, and how a change is recorded.

1.2. The AICC Lead owns the catalog and every document in it.

1.3. The documents are kept in the repository like software documentation. A change is a revision, recorded in the change log,
and the repository history holds every earlier text.

## 2. Labeling

2.1. Each document has an identifier of the form `AICC-<category>-<number>-<language>`, for example `AICC-ORG-01-EN`.

2.2. The category states the subject of the document.

| Category | Subject | Documents |
| --- | --- | --- |
| MND | Mandate: what AICC is for and why | Statement of Intent, AICC Charter |
| ORG | Organization: structure, Roles, and authority | Operating Model, Roles and Responsibilities, Decision Rights, Register of Appointments |
| GOV | Governance: how decisions, documents, and quality are controlled | Governance Forums, Decision Management, Corpus Assessment |
| OPS | Operations: how work is run | Portfolio Management, Service Catalog, Registers, Reporting |
| POL | Policy: rules that bind staff | AI Use Policy, Data Classification Policy, Risk Tier Policy, Third-Party AI Policy, AI Incident Policy |
| PLN | Plan: money, measures, and development | Funding Model, Metrics, Evolution Plan, Enablement Plan |
| REF | Reference: terms, standards, and this catalog | Vocabulary and Style, Artifact Standards, Document Catalog |
| TPL | Template: the prescribed form of a Record | The Templates in section 10 |

2.3. The number is sequential within the category and follows the order of precedence, which the Vocabulary and Style states. It is not reused, and it does not change
when the title changes.

2.4. The language is an ISO 639-1 code: EN for English, RU for Russian, and KY for Kyrgyz. English is the source. Each document
has an English text. A Russian text follows, and a Kyrgyz text may follow. A translation keeps the number and changes the
language code, and is held in a file named with the language, for example `operating-model.ru.md`.

2.5. The Records of the Portfolio have their own identifiers, which the Artifact Standards define. A document identifier does not
collide with them.

## 3. Metadata block

3.1. Each document begins with a block in this form.

```yaml
id: AICC-ORG-01-EN
title: Operating Model
status: draft
revision: 0.8
created: 2026-09-29
revised: 2026-09-30
```

3.2. The fields have the following meaning.

| Field | Meaning |
| --- | --- |
| id | The identifier in section 2 |
| title | The title of the document, in title case, equal to the heading |
| status | draft, active, or deprecated, as section 4 states |
| revision | The revision in major.minor form, as section 5 states |
| created | The date on which the document was first written |
| revised | The date of the latest revision, equal to the last date in the change log |
| source | Translations only: the identifier and revision of the English text that it translates, for example `AICC-ORG-01-EN 0.8` |

3.3. The owner is the AICC Lead for every document, so no field states it. Activation follows section 6.

## 4. Status

4.1. A document has one of three statuses.

| Status | Meaning |
| --- | --- |
| draft | The document is being written or reviewed and may change without notice. A document that holds only a title and an intent is a draft |
| active | The document is in force. It changes by revision, and each revision is entered in the change log |
| deprecated | The document is no longer in force. It is kept, and its change log names what replaces it |

4.2. A draft becomes active by activation under section 6. An active document becomes deprecated by a decision of the same
authority. A deprecated document is not made active again. A replacement has a new identifier.

## 5. Revision

5.1. A revision is written major.minor. A draft has a major number of zero. The revision at first activation is 1.0.

5.2. Every merged change to a document increases the minor number. A change to the structure of a document, or to the authority of
a Role, increases the major number and resets the minor number to zero.

5.3. The Metadata block and the change log are updated in the same change as the text.

5.4. An active document is reviewed at least each year and at each quarterly Assessment. A review that changes nothing needs no
revision.

5.5. The repository history and its tags hold every earlier text, for the period that the record retention rules of the Bank require.

## 6. Activation

6.1. A document that allocates duties or authority to persons outside AICC becomes active by a decision of the Executive
Sponsor. The Operating Model, the Roles and Responsibilities, the Decision Rights, the Governance Forums, the Decision
Management, and the Portfolio Management are therefore activated by the Executive Sponsor.

6.2. Every other document becomes active by a decision of the AICC Lead.

6.3. Before activation the document is assessed under the Corpus Assessment and the result is acceptance for activation.

6.4. The activation is recorded in a Decision Record, and its reference is entered in the change log in the row of the
revision that is activated.

## 7. Change log

7.1. Each document ends with a change log, in this form.

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 1.1 | 2026-10-14 | What changed, in one line | DR-2026-012, or none |

7.2. The change log has one row for each revision, the newest last, except that one row may cover a range of revisions made
while the document was a draft. The Decision column holds the Decision Record that activated the
revision or approved a change to an active document, and is none for a draft revision.

7.3. The Templates carry no change log. Their changes are recorded in the change log of this catalog.

## 8. Adding or changing a document

8.1. To add a document: take the next number in the category; copy the Metadata block; write the document; add a row to the
catalog; run the mechanical checks of the Corpus Assessment; and, when the document is ready, activate it under section 6.

8.2. To change a document: change the text, increase the revision, update the revised date, and add a change log row. Enter a
Decision Record where the document is active.

## 9. Documents

9.1. The documents are listed below. The columns RU and KY show the revision of the translation, or a dash where none exists.

| ID | Title | Purpose | Status | Revision | Revised | EN | RU | KY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AICC-MND-01 | Statement of Intent on the Adoption of Artificial Intelligence | Values, principles, strategy, governance, and Maturity Roadmap for AI adoption across the Bank and the Group | draft | 0.8 | 2026-09-30 | 0.8 | - | - |
| AICC-MND-02 | AICC Charter | Mission, scope, authority, and sponsorship of AICC, and the AI Risk Appetite Statement | draft | 0.1 | 2026-09-30 | 0.1 | - | - |
| AICC-ORG-01 | Operating Model | How AICC is structured and operates: Portfolio, Hub, Domains, Delivery Program, and cadence | draft | 1.1 | 2026-09-30 | 1.1 | - | - |
| AICC-ORG-02 | Roles and Responsibilities | The Roles, with their responsibilities and authority, and the rules of separation | draft | 0.7 | 2026-09-30 | 0.7 | - | - |
| AICC-ORG-03 | Decision Rights | Who is responsible and accountable for each decision and activity | draft | 0.8 | 2026-09-30 | 0.8 | - | - |
| AICC-ORG-04 | Register of Appointments | The Positions and Holders of the Roles, by Entity and Domain | draft | 0.4 | 2026-09-30 | 0.4 | - | - |
| AICC-GOV-01 | Governance Forums | The Forums, with their purpose, chair, members, quorum, and outputs | draft | 0.5 | 2026-09-30 | 0.5 | - | - |
| AICC-GOV-02 | Decision Management | Decision Categories, workflow, Decision Record, Decision Register, Exceptions, and Group Arrangements | draft | 0.5 | 2026-09-30 | 0.5 | - | - |
| AICC-GOV-03 | Corpus Assessment | The criteria, checklist, and routine for assessing the documents | draft | 0.4 | 2026-09-30 | 0.4 | - | - |
| AICC-OPS-01 | Portfolio Management | Stage policies, backlogs, ranking, and Roadmaps of the Portfolio | draft | 0.4 | 2026-09-30 | 0.4 | - | - |
| AICC-OPS-02 | Service Catalog | The Service Portfolio and the AICC Services | draft | 0.2 | 2026-09-30 | 0.2 | - | - |
| AICC-OPS-03 | Registers | The Registers AICC keeps, with their fields and owners | draft | 0.4 | 2026-09-30 | 0.4 | - | - |
| AICC-OPS-04 | Reporting | The reports of AICC and their content | draft | 0.3 | 2026-09-30 | 0.3 | - | - |
| AICC-POL-01 | AI Use Policy | What employees may and shall not do with AI | draft | 0.2 | 2026-09-30 | 0.2 | - | - |
| AICC-POL-02 | Data Classification Policy | Which data may reach which models and services, and where | draft | 0.1 | 2026-09-30 | 0.1 | - | - |
| AICC-POL-03 | Risk Tier Policy | How Use Cases are assigned a Risk Tier, and what each Tier requires | draft | 0.2 | 2026-09-30 | 0.2 | - | - |
| AICC-POL-04 | Third-Party AI Policy | How AI providers are vetted, contracted, monitored, and exited | draft | 0.1 | 2026-09-30 | 0.1 | - | - |
| AICC-POL-05 | AI Incident Policy | What an AI Incident is, and how it is reported, handled, and notified | draft | 0.2 | 2026-09-30 | 0.2 | - | - |
| AICC-PLN-01 | Funding Model | Investment Envelopes, Investment Guardrails, and funding of the platform and Use Cases | draft | 0.1 | 2026-09-30 | 0.1 | - | - |
| AICC-PLN-02 | Metrics | The Measures of the Maturity Roadmap and of the operation of AICC | draft | 0.1 | 2026-09-30 | 0.1 | - | - |
| AICC-PLN-03 | Evolution Plan | The sequence of development of the Operating Model, and what is active at each Maturity Level | draft | 0.1 | 2026-09-30 | 0.1 | - | - |
| AICC-PLN-04 | Enablement Plan | Training, Communities of Practice, and material of the Enablement Group | draft | 0.1 | 2026-09-30 | 0.1 | - | - |
| AICC-REF-01 | Vocabulary and Style | The terms, names, and style used in every document | draft | 0.5 | 2026-09-30 | 0.5 | - | - |
| AICC-REF-02 | Artifact Standards | Identifiers, repository structure, and mapping of Records to a work tracker | draft | 0.4 | 2026-09-30 | 0.4 | - | - |
| AICC-REF-03 | Document Catalog | The register of the documents, and the rules for labeling and metadata | draft | 0.7 | 2026-09-30 | 0.7 | - | - |

## 10. Templates

10.1. The Templates are in the templates folder and are used in accordance with the Artifact Standards.

| ID | Title | Used for | Revision |
| --- | --- | --- | --- |
| AICC-TPL-01-EN | Decision Record | One Decision | 0.2 |
| AICC-TPL-02-EN | Meeting Agenda | The agenda of a Forum | 0.2 |
| AICC-TPL-03-EN | Meeting Minutes | The minutes of a Forum | 0.2 |
| AICC-TPL-04-EN | AI Steering Committee Agenda | The agenda of the AI Steering Committee | 0.3 |
| AICC-TPL-05-EN | AI Steering Committee Minutes | The minutes of the AI Steering Committee | 0.2 |
| AICC-TPL-06-EN | Initiative Brief | An Initiative that needs a brief | 0.2 |
| AICC-TPL-07-EN | Use Case Card | A Use Case at Intake | 0.3 |
| AICC-TPL-08-EN | Risk Tier Assessment | The Risk Tier of a Use Case | 0.2 |
| AICC-TPL-09-EN | Impact Assessment | Effects on affected persons | 0.2 |
| AICC-TPL-10-EN | Domain Engagement Record | Engagement of a Domain | 0.2 |
| AICC-TPL-11-EN | Pilot Report | The result of a Pilot | 0.2 |
| AICC-TPL-12-EN | Validation Sign-Off | Validation by a Control Function | 0.2 |
| AICC-TPL-13-EN | Scale Decision | Acceptance and rollout | 0.2 |
| AICC-TPL-14-EN | Objectives | Objectives of a Delivery Team for a quarter | 0.3 |
| AICC-TPL-15-EN | Delivery Review Notes | A Delivery Review | 0.2 |
| AICC-TPL-16-EN | Roster | The Delivery Teams of a Delivery Program | 0.2 |
| AICC-TPL-17-EN | Benefits Report | Benefits of a Use Case | 0.2 |
| AICC-TPL-18-EN | AI Incident Report | An AI Incident | 0.3 |
| AICC-TPL-19-EN | Exception Request | An Exception | 0.2 |
| AICC-TPL-20-EN | Retirement Notice | Retirement of a Solution | 0.2 |
| AICC-TPL-21-EN | Quarterly Report | The Quarterly Report | 0.3 |
| AICC-TPL-22-EN | Document Assessment Report | The Assessment of one document | 0.3 |
| AICC-TPL-23-EN | Corpus Assessment Report | The Assessment of the Corpus | 0.3 |

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 0.1 | 2026-09-29 | Index of the documents | none |
| 0.2 to 0.4 | 2026-09-30 | Became the Document Catalog: labeling, Metadata block, status, revision, activation, change log, and templates list. Metadata blocks and change logs added to every document. Approver, class, and lineage fields removed. Document Control folded into this catalog; Corpus Assessment renumbered AICC-GOV-03 | none |
| 0.5 | 2026-09-30 | Light lifecycle applied across the documents: activation replaces approval, Document Control removed, revisions raised for the documents changed | none |
| 0.6 | 2026-09-30 | Iteration 2 of INI-001: F-059, F-060, F-003. Section numbers and titles corrected in 2.2; Next action column removed; one row may cover a range of draft revisions; Templates changed to 0.2: Objectives, Use Case Card, AI Incident Report, AI Steering Committee Agenda, Quarterly Report, Document Assessment Report, Corpus Assessment Report (F-016, F-025, F-044). | none |
| 0.7 | 2026-09-30 | Iteration 3 of INI-001: F-042, F-058. Activation defined by rule; order of precedence referred to the Vocabulary and Style. | DR-2026-004 |
