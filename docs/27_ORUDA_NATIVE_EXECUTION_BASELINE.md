# KNLSOFT WebSite ORUDA-Native Execution Baseline v1.0 Candidate

## 1. 전환 결정

KNLSOFT 웹사이트는 더 이상 독립적인 홈페이지 기획·디자인 프로젝트로 진행하지 않는다. ORUDA가 입력을 해석하고 사업 목적, 요구, 콘텐츠, 설계, 구축, 테스트, 검증, 증적, 자산, 릴리스와 운영을 단계적으로 인계하는 ORUDA-native 프로젝트로 진행한다.

기존 `docs/13~26`은 폐기하지 않지만 최상위 승인 기준이 아니다. 모두 `ORUDA_INTAKE_INPUT_CANDIDATE`로 전환하여 OBusinessPlanning과 ODocument가 읽고 재구성해야 할 입력자료로 사용한다.

## 2. ORUDA 기준선

| 항목 | 값 | 상태 |
|---|---|---|
| Repository | `babyandi/ORUDA` | VERIFIED |
| Main baseline | `89b1b8a83ff98b71ea971b8bc1757b677e0361c7` | VERIFIED 2026-07-12 |
| Methodology state | `PROGRAM_METHOD_PROFILES_BOUND_CONTROL_CANDIDATE` | VERIFIED |
| Program profiles | 24 | VERIFIED |
| Shared component profiles | 9 | VERIFIED |
| Runtime execution | false | HOLD |
| Actual test execution | false | HOLD |
| Production/Commercial/FinalLock | false | HOLD |

## 3. 시작 프로그램과 현재 Gap

ORUDA 프로젝트의 진입점은 기존 결정대로 `OBusinessPlanning`이다. 그러나 현재 ORUDA main의 프로그램 방법론 Matrix와 저장소 검색에서는 다음 선행 프로그램/컴포넌트가 발견되지 않았다.

| Dependency | 역할 | 저장소 상태 | 판정 |
|---|---|---|---|
| OBusinessPlanning | 사업 목적·성과·범위·가설·의사결정 구조 | ORUDA PR #25 Role Binding Candidate / Runtime 미확인 | TRUE HARD GATE |
| OBusinessAdmin | 사업 운영·정책·RFP·승인 기준 관리. PM 아님 | ORUDA PR #25 Role Binding Candidate / Runtime 미확인 | DEPENDENCY BLOCK |
| ORFP / OAcceptance | 요구·평가·인수 기준 자산 | ORUDA PR #25 Role Binding Candidate / Runtime 미확인 | ASSURANCE DEPENDENCY BLOCK |
| OProjectManager | Formal GO 이후 프로젝트 범위·일정·인력·이슈·리스크·KPI 관리 | ORUDA PR #25 Role Binding Candidate / Runtime 미확인 | EXECUTION ROLE BLOCK |
| OProjectLeader | Workstream 분해·기술 실행·OBuilder 팀 의뢰·통합 조율 | ORUDA PR #25 Role Binding Candidate / Runtime 미확인 | EXECUTION ROLE BLOCK |
| OVisual | 시각 구조·재생성·시각 검증 계약 | NOT FOUND in current method matrix | DESIGN DEPENDENCY BLOCK |

Role Binding Gap은 ORUDA Draft PR #25에서 Candidate로 보완됐고 전용/공통 CI가 모두 성공했다. 그러나 main 미적용이며 실행 가능한 Runtime 증거가 없으므로 이 Gap을 우회하여 ODesign 또는 OBuilder부터 시작하지 않는다. 기존 문서를 OBusinessPlanning의 공식 산출물로 소급 표시하지 않는다.

## 4. 적용되는 ORUDA 프로그램

| 단계 | Program/Component | 책임 | Method profile |
|---|---|---|---|
| Intake | ODocument | 원천 수집·분류·추출·Claim 후보화 | Controlled Content |
| Business | OBusinessPlanning | 목적·Outcome·사업 범위·성공 기준 | Enterprise Governance + Hybrid PM |
| Business Control | OBusinessAdmin / ORFP / OAcceptance | 정책·요구·평가·인수 기준. OBusinessAdmin은 PM이 아님 | Governance + Process |
| Control | ORUDA Core / OManager | 전체 Control Baseline·GO/HOLD·Decision·Risk. OManager는 PM이 아님 | Enterprise Governance |
| Execution Container | OProject | KPI·Gate·Evidence·Execution Package 상태를 보관하는 거버넌스 컨테이너 | Hybrid PM + Process |
| Project Delivery | OProjectManager | 프로젝트 실행 계획, 일정·범위·인력·이슈·리스크·KPI·Gate 관리 | Hybrid PM |
| Workstream Delivery | OProjectLeader | 실무 Workstream 분해, Build Request Package 작성, OBuilder 팀 배정·조율 | CBD + Hybrid PM |
| Orchestration | OFlowOrchestrator | 상태·Queue·Retry·Failure Routing | Process Orchestration |
| Content | OReport / ODocument / OOutput | Mission·Source–Claim·콘텐츠·출력 | Controlled Content |
| UX/Visual | ODesign / OVisual | Context·IA·Interaction·Visual System | HCD/UIUX |
| Build | OBuilder | Component·Interface·UI·API·Build | CBD + AI Secure Delivery |
| Test | OTester | Test Strategy·Case·Oracle·Regression | Test/V&V |
| Verify | OView | 독립 검증·False-Pass 차단 | Test/V&V + Governance |
| Audit | OAudit | Evidence Index·Finding·Decision Trail | Governance + Test/V&V |
| Asset | OAsset | Provenance·Version·BOM·Lifecycle | Governance + Engineering |
| Release/Ops | ORelease / OOps | Release·Rollback·SLO·Improvement | Service Ops |

## 5. 강제 실행 순서

업무 위임 Spine은 다음과 같다.

`OBusinessPlanning → OBusinessAdmin → OManager (Formal GO/HOLD) → OProjectManager → OProjectLeader → OBuilder 내부 개발팀`

독립 Assurance Spine은 이 위임 흐름 옆에서 동작한다.

`ORFP/OAcceptance → OTester → OView → OAudit → OAsset → OManager/Human Decision`

전체 강제 원칙은 다음과 같다.

`입력 → 방법론 선택·Tailoring → 산출물 → 테스트 → 독립 검증 → 증적 → 자산 등록 → 승인/HOLD → 다음 위임`

- 산출물이 없으면 테스트할 수 없다.
- 검증기와 Oracle이 없으면 PASS할 수 없다.
- OView 검증이 없으면 단계 PASS는 무효다.
- OAudit Evidence가 없으면 승인할 수 없다.
- OAsset Identity/Provenance가 없으면 재사용 기준본이 아니다.
- ORelease는 OView/OAudit/OAsset 묶음이 없으면 시작할 수 없다.
- OBuilder는 OProjectLeader가 발행한 Build Request Package만 접수한다.
- OBuilder 내부 개발팀의 자체 테스트는 OTester의 독립 테스트를 대체하지 않는다.

## 6. 현행 상태

- ORUDA 프로젝트 등록 구조: CREATED CANDIDATE.
- 기존 문서의 ORUDA 입력 재분류: APPLIED.
- ORUDA 실제 런타임 실행: NOT EXECUTED.
- OBusinessPlanning 공식 실행: BLOCKED — program binding missing.
- OProjectManager/OProjectLeader 위임 실행: BLOCKED — role/program bindings missing.
- Wireframe/Visual Design/Build: NOT AUTHORIZED.

## 7. Apply Decision

### Apply now

- ORUDA-native 프로젝트 등록 파일과 검증 Harness.
- 기존 `docs/13~26`을 입력 후보로 재분류.
- 프로그램별 Artifact/Handoff/Gate 계약.
- 누락 프로그램을 TRUE HARD GATE로 등록.

### Do not apply now

- 기존 W00~W08 문서를 ORUDA 실행 완료 산출물로 표시.
- OBusinessPlanning을 건너뛰고 ODesign/OBuilder 실행.
- 기존 홈페이지 코드·CSS·Visual Asset 수정.

### Defer

- 실제 ORUDA runtime activation, 실제 OTester/OView/OAudit/OAsset 처리.
- Wireframe, Visual Design, implementation, deployment.

### Trigger

- ORUDA 저장소에 OBusinessPlanning과 필수 선행 Contract가 등록·검증된 후 `OBP-ENTRY` 재판정.
