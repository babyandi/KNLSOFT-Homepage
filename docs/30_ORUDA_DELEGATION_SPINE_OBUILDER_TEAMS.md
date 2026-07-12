# KNLSOFT ORUDA Delegation Spine · OBuilder Team Routing v1.0 Candidate

## 1. 확정 위임 Spine

`OBusinessPlanning → OBusinessAdmin → OProjectManager → OProjectLeader → OBuilder Development Teams`

Formal GO 이전에는 OProjectManager와 OProjectLeader를 활성화하지 않는다. Formal GO 판단은 ORFP/OAcceptance와 독립 Assurance 결과를 OManager가 통제하고 Human Decision Owner가 승인하는 별도 Control Spine에서 수행한다.

## 2. 역할 경계

| Role/Program | 책임 | 산출물 | 다음 위임 | 금지 |
|---|---|---|---|---|
| OBusinessPlanning | 요청 배경, Goal Picture, Outcome, 가치·범위·가정 | Business Planning Package | OBusinessAdmin | 직접 개발팀 지시 |
| OBusinessAdmin | 사업 운영 기준, RFP/요구·승인·이해관계자 관리 | Business Administration & RFP Package | Formal GO control / OProjectManager | 프로젝트 일정·개발팀 지휘 |
| OManager | Evidence 기반 GO/HOLD·우선순위·통제 | Decision Record | OProject activation | PM 업무 수행 |
| OProject | 실행 상태·KPI·Gate·Evidence·Package 보관 | Project Execution Governance Record | OProjectManager/Leader context | 별도 실행 역할로 행동 |
| OProjectManager | 실행 계획, 일정, 범위, 자원, 이슈, 리스크, KPI, Gate | Project Execution Plan, Workstream Charter | OProjectLeader | 기술 구현 세부 지시 |
| OProjectLeader | Workstream/Component 분해, 기술 조율, Build Request 발행·통합 | Build Request Package, Integration Plan | OBuilder Teams | GO/HOLD 최종 판단 |
| OBuilder | 승인된 Build Request를 팀별 구현·통합 | Source, Component, Interface, Build Evidence | OTester | 사업 요청 직접 접수, 자체 Final PASS |

## 3. OBuilder 내부 개발팀

| Team ID | 팀 | KNLSOFT 웹사이트 책임 | 필수 입력 | 출력 | 독립 경계 |
|---|---|---|---|---|---|
| OBT-01 | Architecture & Component | 컴포넌트·경계·의존성·NFR 구조 | Approved Architecture/Workstream | Component Model, Dependency Graph | OManager/OProjectManager 역할 대체 금지 |
| OBT-02 | Frontend & Web UI | 승인된 IA·Interaction·Visual을 웹 UI로 구현 | ODesign/OVisual Contract | Accessible UI, Component Source | 디자인 임의 변경 금지 |
| OBT-03 | Backend & API | 문의·데모·CMS·상태·라우팅 API | Interface/Data/Policy Contract | Service/API Source, API Evidence | 정책 임의 확정 금지 |
| OBT-04 | Content & CMS | 구조화 콘텐츠·Claim/Evidence·발행 Workflow 구현 | OReport/ODocument Model | CMS Schema, Workflow | Claim 승인 권한 없음 |
| OBT-05 | Data & Metadata | 콘텐츠·증거·상태·분석 데이터 모델 | Data/Retention Contract | Schema, Migration, Lineage | 실제 고객 데이터 임의 사용 금지 |
| OBT-06 | Integration & Adapter | CRM·메일·검색·분석·지원 연동 | Approved Adapter Contract | Adapter, Retry/Failure Evidence | 외부 연동을 핵심 열람과 결합 금지 |
| OBT-07 | AI & Knowledge | 검증된 AI 기능의 제한적 연계 | AI I/O/Security/Human Review Contract | AI Adapter, Prompt/Model Config Evidence | AI 자기 승인 금지 |
| OBT-08 | Security & IAM | RBAC·PII·보안 헤더·비밀·감사 연계 | Security/Privacy Model | Security Controls, Scan Evidence | 법무/승인자 역할 대체 금지 |
| OBT-09 | Build & DevOps | 빌드·환경·배포 자동화·Rollback 준비 | Release/Environment Contract | Build Pipeline, SBOM, Rollback Evidence | Production GO 권한 없음 |
| OBT-10 | Developer Quality | Unit/Static/Component/Integration pre-check | Source + Developer Oracle | Developer Test Evidence | OTester/OView 독립 판정 대체 금지 |

## 4. Build Request Package

OProjectLeader가 OBuilder에 의뢰할 때 다음 항목이 필수다.

- Project/Trace/Workstream/Request ID.
- 사업 목표와 Acceptance Criteria.
- 승인된 Requirement, Content, Claim, Design, Policy, Security Contract.
- 대상 Team, Component, API, UI, Data, Integration 범위.
- Input/Output Artifact와 Dependency.
- Test Scenario, Oracle, Negative/Recovery 조건.
- Evidence와 OAsset 등록 요구.
- 일정·우선순위·위험·승인자.
- 완료 조건과 OTester 인계 조건.

## 5. KNLSOFT 1차 Routing

| Workstream | OProjectLeader routing | 선행 의존성 |
|---|---|---|
| 회사·제품 콘텐츠 | OBT-04 + OBT-02 | OBusinessPlanning, OBusinessAdmin, OReport/ODocument |
| aTops/SPACEMON 제품 페이지 | OBT-02 + OBT-04 | Product Claim/Evidence + ODesign/OVisual |
| AI 설명 | OBT-07 + OBT-04 + OBT-02 | 실제 AI I/O, Security, Human Review |
| 데모·문의 | OBT-03 + OBT-05 + OBT-06 + OBT-08 | 개인정보·라우팅·운영 책임 |
| CMS/발행 | OBT-03 + OBT-04 + OBT-05 + OBT-08 | Role/Approval/Expiry Policy |
| 빌드·운영 준비 | OBT-09 + OBT-10 | OTester/OView/OAudit/OAsset 인계 계약 |

## 6. Apply Decision

- Apply now: 위임 Spine, 역할 경계, OBuilder Team Directory, Build Request Contract.
- Do not apply: OBusinessAdmin/OManager를 PM으로 사용, OProjectLeader를 생략한 개발팀 직접 의뢰.
- Defer: 실제 팀 인스턴스 활성화와 코드 작업.
- Trigger: OBusinessPlanning→OBusinessAdmin 산출물과 Formal GO, OProjectManager/Leader binding PASS.

