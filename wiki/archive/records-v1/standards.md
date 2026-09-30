# Standards Record

| Field | Entry |
| --- | --- |
| Identifier | STD |
| Title | Standards Record |
| Status | Active |
| Owner | Lead Architect |
| Date of last change | 2026-09-30 |
| Tracker reference | [reference, if a work tracker is used] |

This Record holds the architecture standards of AICC, against which the Design Review approves the design of a Solution, and the requirements that the use of AI places on the AI Platform. Each entry has an identifier, and the date is the date on which the entry took effect. Entries are closed and not deleted.

## Architecture standards

| Identifier | Standard | Applies to | Date |
| --- | --- | --- | --- |
| ARC-001 | The design provides that a person decides each case. | Risk Tier 3 | 2026-09-30 |
| ARC-002 | The design provides oversight with the authority to stop, and no autonomy without the decision of the AI Steering Committee. | Risk Tier 4 | 2026-09-30 |
| ARC-003 | The design discloses to customers that they interact with AI. | Risk Tier 3 and 4 | 2026-09-30 |
| ARC-004 | The design lets a customer reach a person and contest a decision. | Risk Tier 3 and 4 | 2026-09-30 |
| ARC-005 | The design logs the use of the Solution, with the retention that the rules require. | Risk Tier 2 to 4 | 2026-09-30 |

## Requirements placed by the use of AI on the AI Platform

| Identifier | Requirement | Applies to | Date |
| --- | --- | --- | --- |
| PLT-001 | The AI Platform holds the AI Registry and keeps it current. | Every Use Case | 2026-09-30 |
| PLT-002 | The AI Platform provides logging, with the retention that the rules require. | Risk Tier 2 to 4 | 2026-09-30 |
| PLT-003 | The AI Platform supports continuous monitoring, with alerts. | Risk Tier 3 and 4; alerts for Risk Tier 4 | 2026-09-30 |
| PLT-004 | The AI Platform keeps the data of each Entity separated, as the Data Classification Policy requires. | Every Entity | 2026-09-30 |
| PLT-005 | The AI Platform allows a Solution to be suspended pending review. | Every Solution | 2026-09-30 |
