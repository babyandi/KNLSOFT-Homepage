# KNLSOFT WebSite ORUDA Program · Artifact · Handoff Map v1.0 Candidate

## 1. End-to-End Handoff

| Stage | Owner | Input | Required output | Receiver | Exit Gate | Current |
|---|---|---|---|---|---|---|
| S00 Intake | ODocument | docs/01~26, public sources, assets | Source Register, Classification, Claim Candidate, Provenance Gap | OBusinessPlanning | SOURCE_AUTHORITY | INPUT READY/PARTIAL |
| S01 Business Plan | OBusinessPlanning | S00 bundle | Goal Picture, Business Mission, Outcome Map, Scope, KPI Hypothesis, Decision Log | OBusinessAdmin | OBP-ENTRY / BUSINESS_VALUE | BLOCKED |
| S02 Business Admin | OBusinessAdmin + ORFP + OAcceptance | S01 | Governance Model, Stakeholder/Approval, RFP/Requirement, Acceptance Package | Assurance + OManager | AUTHORITY / REQUIREMENT / ACCEPTANCE | BLOCKED |
| S03 Pre-GO Assurance | OTester + OView + OAudit + OAsset.Candidate | S01~S02 | Test/Verification Result, Evidence Index, Candidate Asset Package | OManager + Human Decision Owner | ASSURANCE_COVERAGE | BLOCKED |
| S04 Formal Control | OManager + Human Decision Owner | S01~S03 | Formal GO/HOLD Decision Record, Project Handoff Package | OProject + OProjectManager | FORMAL_GO | NOT GRANTED |
| S05 Execution Container | OProject | Approved Handoff | Execution State, KPI, Gate, Evidence, Package Registry | OProjectManager | PROJECT_ACTIVATION | NOT EXECUTED |
| S06 Project Delivery | OProjectManager | Project Handoff | Execution Plan, Schedule, Scope, Resource, RAID, Workstream Charter | OProjectLeader | PROJECT_BASELINE | NOT EXECUTED |
| S07 Workstream Delivery | OProjectLeader | Workstream Charter | Work Breakdown, Build Request Packages, Integration/Test Handoff Plan | OReport/ODesign/OVisual + OBuilder Teams | BUILD_REQUEST_READINESS | NOT EXECUTED |
| S08 Content/Design Support | OReport + ODocument + ODesign + OVisual | Approved Business/Workstream Pack | Source–Claim Map, Content Model, IA, Interaction, Visual Contract | OProjectLeader + OBuilder | CONTENT/DESIGN GATES | BLOCKED |
| S09 Build Teams | OBuilder internal teams | OProjectLeader Build Request | Component, Interface, Source, Build/Developer-Test Evidence | OProjectLeader + OTester | SECURE_BUILD / QUALITY_MODEL | NOT EXECUTED |
| S10 Independent Test | OTester | Integrated Build + Scenario + Oracle | Test Plan, Result, Defect, Regression | OView | TEST_COVERAGE / ORACLE_VALIDITY | NOT EXECUTED |
| S11 Verify | OView | Artifacts + Test Evidence | Independent Gate Result, False-Pass Challenge | OAudit | INDEPENDENT_VERIFICATION | NOT EXECUTED |
| S12 Audit | OAudit | Full Evidence | Evidence Index, Findings, Decision Trail | OAsset + OManager | EVIDENCE_INTEGRITY / NO_SELF_PASS | NOT EXECUTED |
| S13 Asset | OAsset | Approved outputs/evidence | Asset ID, Provenance, Version Lineage, BOM, Disposition | OManager + ORelease | IDENTITY / VERSION / LICENSE | NOT EXECUTED |
| S14 Release Decision | OManager + ORelease | OView+OAudit+OAsset bundle | Release/HOLD Decision, Manifest, Deployment/Rollback Plan | OOps | RELEASE_READINESS | HOLD |
| S15 Operate | OOps | Released service | Service Model, SLO/SLI, Incident/Problem/Improvement | OBusinessPlanning | SERVICE_READINESS / IMPROVEMENT | HOLD |

## 2. 기존 문서 재매핑

| Existing documents | ORUDA classification | 공식성 |
|---|---|---|
| docs/01~12 | Historical design-first reference | REFERENCE_ONLY |
| docs/13~16 | Business/Claim input candidates | NOT OBP/OReport OUTPUT |
| docs/17~22 | Scenario/Function/IA/Policy/UX input candidates | NOT ODesign/OTester OUTPUT |
| docs/23~24 | Local Gate/RCA input | NOT OView/OAudit RESULT |
| docs/25~26 | Source inventory and risk input | NOT ODocument VERIFIED REGISTER |
| docs/27~30 | ORUDA project control/delegation baseline | CONTROL_CANDIDATE |

## 3. Handoff Contract

모든 Handoff는 다음 필드를 가져야 한다.

- `project_id`, `trace_id`, `stage_id`, `producer`, `receiver`.
- `method_profile_ids`, `input_asset_ids`, `output_artifact_ids`.
- `claim/evidence links`, `version`, `hash`, `owner`, `approver`.
- `test_result`, `view_result`, `audit_evidence`, `asset_registration`.
- `decision`: PASS / PASS_WITH_CONDITION / REWORK / BLOCK / HOLD.
- `failure_route`, `resume_trigger`, `next_authority`.

## 4. Apply Decision

- Apply now: Stage/Owner/Input/Output/Receiver/Gate 매핑.
- Do not apply: 이전 문서를 공식 ORUDA 결과로 소급 승격.
- Defer: 실제 Artifact ID/Hash/Evidence 생성.
- Trigger: 해당 ORUDA 프로그램 runtime과 Contract 등록.
