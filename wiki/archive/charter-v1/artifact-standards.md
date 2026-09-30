```yaml
id: AICC-REF-02-EN
title: Artifact Standards
status: draft
revision: 0.4
created: 2026-09-30
revised: 2026-09-30
```

# Artifact Standards

## 1. Purpose and scope

1.1. This document defines the identifiers, the folder structure, and the Templates of the Records of the Portfolio, and the
mapping of the Records to a work tracker.

1.2. It applies to every Record kept by AICC. The documents of the charter folder are governed by the Document Catalog.

## 2. Repositories

2.1. AICC keeps two kinds of content. The charter folder holds the documents that define the adoption of AI and the operation
of AICC, in accordance with the Document Catalog. The portfolio folder holds the Records of the Portfolio, which change
continuously. The wiki holds working material and reference material, which is not activated.

2.2. The listing below shows the structure of the repository.

```text
charter/                          documents of the charter folder
  statement-of-intent.md, operating-model.md, roles.md, decision-rights.md, ...
  policies/                       the policies
  templates/                      the Templates of the Records
portfolio/                        Records of the Portfolio
  priorities.md                   Strategic Priorities and Investment Envelopes
  portfolio-backlog.md            Portfolio Backlog
  roadmap.md                      Portfolio Roadmap
  service-portfolio.md            Service Portfolio and Service Catalog
  standards.md                    Standards Record: architecture standards and platform requirements
  registers/                      Decision, Risk and Issue, AI Incident, Exception, and Benefits Registers, and the interim AI Registry
  decisions/                      Decision Records
  incidents/                      AI Incident Reports
  exceptions/                     Exception Requests
  meetings/<forum>/               agenda and minutes of each Forum, by date
  reports/                        Quarterly Reports and other reports
  assessments/<date>/             Records of each Assessment: the Corpus Assessment Report and the Document Assessment Reports
  initiatives/INI-nnn-title/      Initiative Brief and related Records
  programs/<program>/             one folder for each Delivery Program
    delivery-backlog.md, roadmap.md, roster.md
    domains/                      Domain Engagement Records
    objectives/                   Objectives by quarter
    reviews/                      Delivery Review notes
    use-cases/UC-nnn-title/       the Records of one Use Case: Use Case Card, Risk Tier Assessment, Impact Assessment,
                                  Pilot Report, Validation Sign-Offs, Scale Decision, Benefits Reports, and Retirement Notice
wiki/                             working and reference material
```

## 3. Identifiers

3.1. Each Record has an identifier that is unique and is not reused.

| Record | Identifier | Example |
| --- | --- | --- |
| Strategic Priorities | PRI | PRI |
| Strategic Priority | PRI-n | PRI-1 |
| Portfolio Backlog | PBL | PBL |
| Portfolio Roadmap | RMP | RMP |
| Service Portfolio | SPF | SPF |
| Standards Record | STD | STD |
| Initiative, Initiative Brief | INI-nnn | INI-001 |
| Delivery Program | PRG-program | PRG-main |
| Delivery Backlog | DBL-program | DBL-main |
| Program Roadmap | PRM-program | PRM-main |
| Roster | ROS-program | ROS-main |
| Delivery Team | DT-nnn | DT-001 |
| Objective | OBJ-yyyyQq-nn | OBJ-2027Q1-01 |
| Objectives of a Delivery Team for a quarter | OBJ-yyyyQq-DT-nnn | OBJ-2027Q1-DT-001 |
| Milestone | MS-nnn | MS-001 |
| Domain Engagement Record | DEN-nnn | DEN-001 |
| Use Case, Use Case Card | UC-nnn | UC-001 |
| Risk Tier Assessment | UC-nnn-RTA | UC-001-RTA |
| Impact Assessment | UC-nnn-IMP | UC-001-IMP |
| Pilot Report | UC-nnn-PLT | UC-001-PLT |
| Validation Sign-Off | UC-nnn-VAL-n | UC-001-VAL-1 |
| Scale Decision | UC-nnn-SCL | UC-001-SCL |
| Benefits Report | UC-nnn-BNR-yyyyQq | UC-001-BNR-2027Q1 |
| Retirement Notice | UC-nnn-RET | UC-001-RET |
| Solution | SOL-nnn | SOL-001 |
| AICC Service | SVC-nnn | SVC-001 |
| Architecture standard | ARC-nnn | ARC-001 |
| Platform requirement | PLT-nnn | PLT-001 |
| Decision Record | DR-yyyy-nnn | DR-2027-001 |
| Risk or issue | RSK-nnn | RSK-001 |
| AI Incident, AI Incident Report | INC-nnn | INC-001 |
| Exception, Exception Request | EXC-nnn | EXC-001 |
| Benefit | BEN-nnn | BEN-001 |
| Decision Register | REG-DEC | REG-DEC |
| AI Registry | REG-AI | REG-AI |
| Risk and Issue Register | REG-RSK | REG-RSK |
| AI Incident Register | REG-INC | REG-INC |
| Exception Register | REG-EXC | REG-EXC |
| Benefits Register | REG-BEN | REG-BEN |
| Agenda, minutes, or notes of a Forum | Forum name, date, and agenda, minutes, or notes | AI Steering Committee, 2027-01-15, minutes |
| Quarterly Report | QR-yyyyQq | QR-2027Q1 |
| Corpus Assessment Report | ASM-date | ASM-2026-09-30 |
| Document Assessment Report | ASM-date-document identifier | ASM-2026-09-30-AICC-REF-01-EN |

3.2. Folder and file names are in lower case, use hyphens, and begin with the identifier where one exists.

## 4. Record header

4.1. Each Record begins with a header that states the identifier, the title, the status, the owner, the date of the last
change, and, where a work tracker is used, the reference of the tracker item.

4.2. The status of a Record is Draft, Active, or Closed. Draft means that the Record is being completed and is not yet in
use. Active means that the Record is in use and that its owner keeps it current, even when it holds no entries. Closed
means that the Record is no longer kept current and is retained.

4.3. A Record that is a list, such as a backlog, a Roadmap, a Register, the Strategic Priorities, the Service Portfolio, or
the Standards Record, holds the status Active while it is in use.

4.4. Where a Template states its own status values, as the Decision Record and the Initiative Brief do, those values are the
status of the Record.

## 5. Templates

5.1. Each Record is created from its Template in the templates folder. The Templates are listed in the Document Catalog. A Record that is a list is created from the table layout given in the document that defines it, which is Portfolio Management or Registers, and needs no Template.

## 6. Work tracker

6.1. When a work tracker is introduced, the Records map to it as follows.

| Record | Tracker item |
| --- | --- |
| Initiative | An item of the type Initiative, in the portfolio project |
| Use Case | An item of the type Use Case, in the project of the Delivery Program |
| Work Item | A task or sub-task of a Use Case |
| Delivery Program board | A flow board whose columns are the Stages and whose rows are the Domains, with a Limit on Work in Progress for each column |
| Roadmaps | The roadmap view of the tracker |

6.2. The backlogs, the boards, and the Roadmaps are then maintained in the tracker. The Records refer to the items of the
tracker by reference. Decision Records, minutes, Registers other than the backlogs, and reports remain in the repository.

## 7. Access and retention

7.1. The Records are stored in the repository of AICC, and the access rules of the repository apply. Internal audit has read
access.

7.2. Records are retained for the period that the record retention rules of the Bank require. A Record is closed and not
deleted.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 0.1 | 2026-09-30 | Drafted. | none |
| 0.2 | 2026-09-30 | Template list replaced by the Document Catalog; references updated. | none |
| 0.3 | 2026-09-30 | Iteration 2 of INI-001: F-044, F-015. | none |
| 0.4 | 2026-09-30 | Iteration 3 of INI-001: F-054, F-055, F-056. | none |
