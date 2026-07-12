# KNLSOFT WebSite ORUDA Gate · State Ledger v1.0 Candidate

## 1. Gate Ledger

| Gate | Predicate | Evidence | Result | Failure route | Resume trigger |
|---|---|---|---|---|---|
| REG-00 | Project identity, ORUDA baseline, scope pinned | Project JSON + validator | PASS CONTROL CANDIDATE | OManager | Registry read-back |
| METHOD-00 | ORUDA program methodology baseline exists | ORUDA main `89b1b8a...` | PASS CONTROL CANDIDATE | ORUDA Core | Upstream baseline change |
| OBP-ENTRY | OBusinessPlanning role/method binding and executable runtime available | ORUDA PR #25 CI SUCCESS; runtime evidence none | BLOCK | ORUDA Runtime Gap | PR #25 main 적용 + Runtime Contract/Execution/Evidence PASS |
| DOC-INTAKE | All inputs have source/provenance/status | docs/13~26 + PS/CR registries | PARTIAL | ODocument | Source owner and originals |
| BUSINESS-01 | Mission/outcome/scope approved by OBP | none | NOT EXECUTED | OBusinessPlanning | OBP-ENTRY PASS |
| ADMIN-RFP-02 | Business governance, RFP/Requirement, Acceptance baseline | none | BLOCKED BY OBP | OBusinessAdmin/ORFP/OAcceptance | Bindings + BUSINESS-01 |
| ASSURE-03 | Pre-GO independent assurance package | none | NOT EXECUTED | OTester/OView/OAudit/OAsset | S01~S02 outputs |
| FORMAL-GO-04 | OManager control + Human Decision Evidence | none | NOT GRANTED | OManager/Human Owner | ASSURE-03 PASS |
| PROJECT-ACT-05 | OProject container and OProjectManager activated | none | BLOCKED | OProject/OProjectManager | FORMAL-GO-04 |
| PM-BASELINE-06 | Scope/schedule/resource/RAID/KPI/workstream | none | NOT EXECUTED | OProjectManager | Approved Handoff |
| LEADER-ROUTE-07 | Work breakdown and OBuilder Build Request | none | NOT EXECUTED | OProjectLeader | PM-BASELINE-06 |
| CONTENT-DESIGN-08 | Source–Claim, HCD, accessibility, OVisual contract | local candidate only | BLOCKED | OReport/ODocument/ODesign/OVisual | Approved Workstream + Evidence |
| BUILD-09 | OBuilder team routing and secure integrated build | none | NOT EXECUTED | OBuilder/OProjectLeader | LEADER-ROUTE-07 + DESIGN-08 |
| TEST-10 | Test/negative/regression/oracle evidence | none | NOT EXECUTED | OTester | Integrated build evidence |
| VIEW-11 | Independent verification and false-pass challenge | none | NOT EXECUTED | OView | Test bundle |
| AUDIT-12 | Evidence integrity and finding closure | none | NOT EXECUTED | OAudit | View result |
| ASSET-13 | Identity/hash/version/license/provenance | none | NOT EXECUTED | OAsset | Audit evidence |
| RELEASE-14 | Release evidence/SoD/rollback | none | HOLD | OManager/ORelease | OView+OAudit+OAsset bundle |
| PROD-15 | Production authority | none | HOLD | Human Authority | Explicit Production GO |

## 2. True Hard Gate

`OBP-ENTRY = BLOCK`가 현재 첫 번째 True Hard Gate다. Role Binding Candidate는 ORUDA PR #25에서 준비됐지만, main 적용과 실행 가능한 OBusinessPlanning Runtime 증거가 없으므로 실제 ORUDA 실행은 여기서 멈춘다. 다만 다음 비의존 작업은 계속할 수 있다.

- 기존 자료의 Source/Provenance 상태 정리.
- ORUDA Project/Artifact/Gate machine-readable registry 작성.
- Validator와 fail-open mutation test 작성.
- 누락 프로그램과 Contract 요구사항 등록.

## 3. False-Pass 방지

- `docs 존재 = OBusinessPlanning 실행`이 아니다.
- `방법론 Profile binding = 외부 표준 인증`이 아니다.
- `Validator PASS = website/runtime/test PASS`가 아니다.
- `OTester PASS = OView PASS`가 아니다.
- `OView PASS = OAudit Final PASS`가 아니다.
- `OAsset 등록 = Production GO`가 아니다.

## 4. Apply Decision

- Apply now: Gate 상태와 True Hard Gate.
- Do not apply: Wireframe·디자인·구현 Gate의 임의 PASS.
- Defer: release/production/commercial/final lock.
- Trigger: 각 Gate의 Resume trigger.
