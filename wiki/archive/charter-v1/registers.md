```yaml
id: AICC-OPS-03-EN
title: Registers
status: draft
revision: 0.4
created: 2026-09-30
revised: 2026-09-30
```

# Registers

## 1. Purpose and scope

1.1. This document defines the Registers that AICC keeps, the purpose, owner, and fields of each, and the rules for keeping
them.

1.2. A Register is a Record that lists items of one kind. The Registers are kept in the Records of the Portfolio in
accordance with the Artifact Standards, except the Register of Appointments, which is a document of the charter folder, and
the AI Registry, which is kept on the AI Platform.

## 2. Registers

2.1. AICC keeps the following Registers.

| Register | Purpose | Update rule |
| --- | --- | --- |
| Decision Register | Indexes all Decision Records | Within two working days of a Decision |
| AI Registry | Records each Use Case, model, and agent with its owner, scope, data access, and Risk Tier | At each change of a Use Case, and at least each quarter |
| Risk and Issue Register | Records the risks and issues of the Portfolio and of the Delivery Program | Continuously, and reviewed at each Quarterly Planning and Review Event |
| AI Incident Register | Records each AI Incident and its handling | Within one working day of a report |
| Exception Register | Records each Exception, its owner, and its expiry | Within two working days of a Decision |
| Benefits Register | Records the benefit expected from each Use Case and the benefit realized | Each quarter |
| Register of Appointments | Records the Positions and Holders of the Roles | On each change |

2.2. The Decision Rights state the owner of each Register.

## 3. Fields

3.1. **Decision Register.** Identifier; title; Decision Category; date; Decider; status; review date; link to the Decision
Record.

3.2. **AI Registry.** Identifier of the Use Case; name; Domain; Entity; Domain Owner; AI Solution Engineer; Risk Tier;
models and versions used; data classes used; providers; agents and their permissions; Stage; date of the last validation;
reassessment date; link to the Use Case Record. The reassessment date is the date of the next reassessment of the Risk Tier in accordance with section 5.1 of the Risk Tier Policy: one year after the last assessment for Risk Tier 3, and six months for Risk Tier 4. A Use Case of Risk Tier 1 or 2 has no date and is reassessed on change.

3.3. **Risk and Issue Register.** Identifier; Finding; description; type (risk or issue); Domain or Use Case; likelihood; impact;
owner; response; status; review date.

3.4. **AI Incident Register.** Identifier; date and time of detection; description; Severity; Use Case; Domain; Entity;
reporter; containment; notifications made; root cause; corrective actions with owners and dates; status; date of the
review.

3.5. **Exception Register.** Identifier; requirement excepted; reason; Use Case or Domain; risk and compensating controls;
Decider; start date; expiry date; owner; status.

3.6. **Benefits Register.** Identifier; Use Case; Strategic Priority; benefit description; Measure; baseline; target;
realized value and date; owner.

3.7. **Register of Appointments.** The fields of the Register of Appointments are stated in the Register of Appointments.

## 4. Rules

4.1. Each Register has one owner, who is accountable for its completeness and accuracy.

4.2. An entry has an identifier that is not reused. An entry is closed and not deleted.

4.3. The AI Steering Committee reviews the Decision Register, the Risk and Issue Register, the AI Incident Register, the
Exception Register, and the Benefits Register each quarter.

4.4. The internal audit Control Function has read access to every Register.

4.5. The Risk and Issue Register records each open Finding of an Assessment as an issue, with the identifier of the Finding.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 0.1 | 2026-09-30 | Drafted. | none |
| 0.2 | 2026-09-30 | Document register removed; the Document Catalog replaces it. | none |
| 0.3 | 2026-09-30 | Iteration 2 of INI-001: F-016, F-071, F-072, F-037, F-003. | none |
| 0.4 | 2026-09-30 | Iteration 3 of INI-001: F-064, F-006, F-062. | none |
