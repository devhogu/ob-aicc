# AI Lab

The source record of the AI Lab section. Each row is one unit of text, identified by its Key; the Russian edition has the same Keys in the same order.

## Page

| Key | Text |
| --- | --- |
| subtitle | Experiments with AI scenarios |
| intro | The AI Lab runs continuously on the Bank's own infrastructure, isolated from its production systems. A scenario can enter at any time as an Experiment; data arrives as read-only extracts from the Bank's systems and never leaves the Bank; the AI-agent workflow is built, measured, and then accepted, turned into a Proposal for delivery, or rejected. The Lab is where the Bank tries generative AI before it commits to it. |
| systems-title | How people and AI agents work together |
| systems-intro | People steer: they set the intent and carry accountability. AI agents gather signals, analyze, reason, execute, and learn. The two work in parallel, joined by one intent loop and a trust perimeter that is not negotiable. |
| systems-connection | The intent loop |
| implication-label | What this means |
| implication | Decision rights stay with people. AI agents make decisions faster, wider in scope, and better evidenced. The Bank does not hand over judgment; it equips it. |
| loop-title | The intent loop |
| loop-intro | How people and AI agents work together: intent → insight → action → audit, continuously |
| guardrails-title | Lab practice maturity |
| guardrails-intro | How far good practice is applied in each control area of the Lab, measured against what the Bank expects of a production system. The Lab has not yet been assessed: no Experiment has run, and its guardrails are not yet due. Each area shows the practice the Lab intends; point at its status to see what it must show to reach each level. |

## Stages

| Key | Stage |
| --- | --- |
| stage-0 | Set up once |
| stage-1 | Intake |
| stage-2 | Scope & hypothesis |
| stage-3 | Data |
| stage-4 | Build |
| stage-5 | Evaluate |
| stage-6 | Decide & report |

## Workstreams

| Key | Workstream |
| --- | --- |
| lane-A | Governance & decisions |
| lane-B | Risk & controls |
| lane-C | Operations & processes |
| lane-D | Data & analytics |
| lane-E | Measurement |

## Tasks

| Key | Workstream | Stage | Task | Description |
| --- | --- | --- | --- | --- |
| task-a-0-1 | A | 0 | Request the environment | Infrastructure request approved; IT security sign-off |
| task-a-0-2 | A | 0 | Set access roles | Access by role; every action logged |
| task-a-1-1 | A | 1 | Secure a sponsor | Name the Executive Sponsor or Domain Owner who will accept the result |
| task-a-1-2 | A | 1 | Pick the scenario | Take the next scenario from the prioritized backlog |
| task-a-2-1 | A | 2 | Agree the time-box | Fix the number of Iterations and the date of the review |
| task-a-2-2 | A | 2 | Requirements & acceptance | Record what the sponsor needs and how the result will be accepted |
| task-a-3-1 | A | 3 | Data ownership | Confirm each source has a named owner and the right to use it |
| task-a-4-1 | A | 4 | Select the architecture | Choose the AI-agent pattern; check it against the guardrails |
| task-a-5-1 | A | 5 | Sponsor demo | Show the result to the sponsor; record feedback |
| task-a-6-1 | A | 6 | Outcome Report | Record the result, the evidence, and the lessons |
| task-a-6-2 | A | 6 | Decision | The sponsor accepts and closes, turns the result into a Proposal for delivery, or rejects it |
| task-b-0-1 | B | 0 | Lab isolation | Separate network segment and key management; no write access to production |
| task-b-0-2 | B | 0 | Keep the guardrails | Hold the Lab guardrails and their evidence in the Standards record |
| task-b-2-1 | B | 2 | Risk Tier | The AICC Lead assigns the Risk Tier; set the risk limits for this Experiment |
| task-b-2-2 | B | 2 | Personal data sign-off | Minimize personal data; assess it with the data-protection Control Function Contact before it enters |
| task-b-3-1 | B | 3 | Extract rules | Read-only extracts only; nothing written back to the Bank's systems |
| task-b-4-1 | B | 4 | AI-agent checks | Drift, bias, and grounding checks on an evaluation set during the build |
| task-b-5-1 | B | 5 | Guardrail check | Check the workflow against the Lab guardrails |
| task-c-0-1 | C | 0 | Set up services | Provision Lab services and the base configuration |
| task-c-1-1 | C | 1 | Map the service | Map the current service workflow; choose the points to change |
| task-c-2-1 | C | 2 | Scope | Set the boundaries, the target workflow, and dependencies |
| task-c-4-1 | C | 4 | Build the workflow | Build the AI-agent workflow; orchestrate its steps |
| task-c-6-1 | C | 6 | Adoption guide | What would change in the service if the result goes to production |
| task-d-0-1 | D | 0 | Extract pipeline | Build the read-only extract pipeline into the Lab |
| task-d-1-1 | D | 1 | Service catalog | List the service's functions and dependencies |
| task-d-3-1 | D | 3 | Catalog & map data | List the available data; trace what the scenario needs |
| task-d-3-2 | D | 3 | Extract & check quality | Run the extract for the scenario; check the data is fit for use |
| task-d-4-1 | D | 4 | Data flows | Connect the data to the AI-agent workflow |
| task-d-4-2 | D | 4 | Analytics | Analytics over the workflow's outputs |
| task-d-5-1 | D | 5 | Data correctness | Check analytical results against reference data |
| task-d-5-2 | D | 5 | Analytics quality | Check the analytics outputs are correct and consistent |
| task-e-2-1 | E | 2 | Hypothesis targets | Define what success looks like; choose the KPIs and the baseline |
| task-e-3-1 | E | 3 | Data quality metrics | Track completeness, freshness, and drift |
| task-e-4-1 | E | 4 | Workflow metrics | Basic functional and monitoring tests |
| task-e-5-1 | E | 5 | KPI evaluation | Measure the KPIs against the targets |
| task-e-5-2 | E | 5 | Benchmarking | Compare with the baseline; analyze cost |
| task-e-5-3 | E | 5 | Acceptance check | Check the result against the acceptance criteria |

## Systems

| Key | Label | Name | Role |
| --- | --- | --- | --- |
| system-1 | ◆ System A | People | Authority · Judgment · Intent |
| system-2 | ● System B | AI agents | Monitoring · Analysis · Execution · Learning |

## Duties

| Key | System | Number | Duty | Description |
| --- | --- | --- | --- | --- |
| system-1-duty-1 | system-1 | A.1 | Strategic direction | Sets the intent, the risk appetite, and the boundary of acceptable action. |
| system-1-duty-2 | system-1 | A.2 | Ethics & regulation | Owns the relationship with regulators, customers, and the public. |
| system-1-duty-3 | system-1 | A.3 | Final decision rights | Keeps authority over high-stakes, irreversible, and reputational decisions. |
| system-1-duty-4 | system-1 | A.4 | Accountability | Answers to the Board, the regulator, the shareholder, the customer. |
| system-1-duty-5 | system-1 | A.5 | Review & recalibration | Checks the Bank against its purpose; resets the intent when the context changes. |
| system-2-duty-1 | system-2 | B.1 | Continuous monitoring | Watches signals on customers, markets, risk, operations, and staff in real time. |
| system-2-duty-2 | system-2 | B.2 | Multi-angle analysis | Weighs decisions across competing factors — risk, return, customer, conduct. |
| system-2-duty-3 | system-2 | B.3 | Options for decision | Presents worked-out options with confidence, trade-offs, and sources. |
| system-2-duty-4 | system-2 | B.4 | Execution & automation | Carries out authorized actions and routine work, and keeps the audit trail. |
| system-2-duty-5 | system-2 | B.5 | Learning from results | Feeds results back into models; flags drift; proposes adjustments to people. |

## Intent loop

| Key | Step | Description |
| --- | --- | --- |
| loop-1 | Intent | People set the outcome, the constraints, the risk appetite, and the ethical limits. Direction, not instructions. |
| loop-2 | Insight | AI agents analyze the data from several angles and present options for decision, with confidence and trade-offs. |
| loop-3 | Action | People authorize. AI agents execute or hand over. Every step has an owner and limits, and can be reversed where possible. |
| loop-4 | Audit | Results are logged, evaluated, challenged if needed, and used to sharpen the next intent. Each turn makes the loop more precise. |

## Areas

| Key | Area |
| --- | --- |
| guardrails-1 | Governance & decisions |
| guardrails-2 | Risk & controls |
| guardrails-3 | Operations & processes |
| guardrails-4 | Data & analytics |
| guardrails-5 | Measurement |

## Concerns

| Key | Area | Concern | Intended practice | Assessed coverage | Level 2 | Level 3 | Level 4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| guardrails-1-1 | guardrails-1 | Decision rights | The sponsor decides the result; the AICC Lead assigns the Risk Tier |  | Who decides is named for each Experiment. | Every approval is recorded in the Solution Definition. | Approvals are recorded and checked at each quarterly Steering. |
| guardrails-1-2 | guardrails-1 | Prohibitions | A fixed list: no personal data leaves the Lab, nothing is written back to production |  | The list is written down and known to the team. | Isolation enforces the list, and breaches are logged. | Compliance is tested on a schedule, with evidence kept. |
| guardrails-1-3 | guardrails-1 | Resolving disagreements | Escalation to the AICC Lead, then the quarterly Steering |  | Disputes are raised with the AICC Lead. | A written escalation rule is applied and its outcomes recorded. | Escalations are reviewed at Steering and the lessons applied. |
| guardrails-2-1 | guardrails-2 | Risk classification | Risk register for the Lab; a Risk Tier for each Experiment |  | Risks of the Lab are recorded by type. | Every Experiment has a risk assessment and a Risk Tier before the build. | Risk Tiers are reviewed at the close and feed the Lab register. |
| guardrails-2-2 | guardrails-2 | Output integrity | Drift, bias, and grounding checks on an evaluation set during the build |  | Checks are run on some Experiments. | Every build runs the checks on an evaluation set. | Results are reviewed independently and monitored after the build. |
| guardrails-2-3 | guardrails-2 | Lab isolation | Separate network segment, key management, no access to production |  | The Lab sits in its own network segment. | Isolation is checked at setup and after every change. | Penetration tests run on a schedule, with results recorded. |
| guardrails-2-4 | guardrails-2 | Personal data protection | Masking, redaction, and extract rules |  | Personal data is masked by hand. | Rules mask or remove personal data before every extract enters. | Each extract has a recorded sign-off by the data-protection Control Function Contact. |
| guardrails-2-5 | guardrails-2 | Failure handling | Rollback and alerting, with a named responder |  | A failed run can be rolled back. | A written runbook with a named owner is followed. | Incidents are reviewed and the runbook is updated. |
| guardrails-3-1 | guardrails-3 | Scenario selection | Prioritized backlog with written selection criteria |  | Scenarios are chosen from a list. | A prioritized backlog with written criteria is used. | Selection is reviewed against results at Steering. |
| guardrails-3-2 | guardrails-3 | Workflow mapping | Service workflow described for each scenario, to a common template |  | Workflows are described ad hoc. | Every scenario uses the common template. | Maps are reused and kept current across Experiments. |
| guardrails-3-3 | guardrails-3 | Experiment lifecycle | Time-box, build, evaluation, review, Outcome Report |  | Experiments are built and checked. | Every Experiment has a time-box and ends with an Outcome Report. | Time to decision and outcomes are tracked across Experiments. |
| guardrails-3-4 | guardrails-3 | Path to delivery | Each accepted result becomes a Proposal for delivery |  | Good results are handed over by agreement. | Every accepted result becomes a Proposal with a handover package. | Proposals are tracked to a delivery decision. |
| guardrails-4-1 | guardrails-4 | Data pipeline | Read-only extract pipeline; extracts made per scenario |  | Extracts are made by hand. | A reusable read-only pipeline, with a named owner for each source. | Pipeline runs are monitored and logged. |
| guardrails-4-2 | guardrails-4 | Data quality | Quality checked at extract |  | Quality is checked by eye. | Standard checks run at every extract. | Checks are automated and reported. |
| guardrails-4-3 | guardrails-4 | Data privacy | Masking and anonymization of sensitive fields |  | Sensitive fields are masked by hand. | Rule-based masking and anonymization for every extract. | Re-identification tests run on a schedule. |
| guardrails-4-4 | guardrails-4 | Analytics correctness | Analytics checked against reference data |  | Results are spot-checked. | Results are compared with reference data where it exists. | Reference sets exist for every scenario. |
| guardrails-5-1 | guardrails-5 | Performance metrics (KPIs) | KPIs and a baseline for each Experiment |  | KPIs are named. | KPIs are measured against a recorded baseline. | KPI results are compared across Experiments. |
| guardrails-5-2 | guardrails-5 | Hypothesis targets | A stated hypothesis and target for each Experiment |  | A hypothesis is written down. | The target is agreed with the sponsor before the build. | Targets are checked against results at the review. |
| guardrails-5-3 | guardrails-5 | Workflow metrics | Functional and integration metrics with pass thresholds |  | Metrics are recorded. | Agreed thresholds decide whether a run passes. | Metrics are monitored over time. |
| guardrails-5-4 | guardrails-5 | Acceptance criteria | Acceptance criteria agreed at the scope step |  | Criteria are written at some point. | Criteria are agreed with the sponsor at the scope step. | Every result is checked against them and signed off. |
