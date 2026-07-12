# KNLSOFT WebSite Strategy & Evidence Blueprint v0.2 Candidate

## 1. 문서 목적

KNLSOFT 웹사이트를 회사·제품을 보기 좋게 소개하는 홈페이지가 아니라, 사용자의 기술·구매 의사결정을 돕고 KNLSOFT의 상담·데모·지원 업무를 연결하는 디지털 서비스로 정의한다. 디자인과 코드는 이 설계를 시각화하고 실행하는 후속 결과물이다.

## 2. 기준선 판정

| 항목 | 상태 | 판정 |
|---|---|---|
| 공개 Sites 버전 8 | DEPRECATED_REFERENCE | 최종 기준선이 아니며 디자인 근거로 사용하지 않음 |
| 기존 Hero/Visual Asset | CONCEPT_REFERENCE | 구도·메시지 후보만 보존, 공식 제품 화면이나 기능 증거로 사용 금지 |
| 누적 `globals.css`와 하단 레이아웃 | RETIRE | 추가 덮어쓰기 금지, 승인 설계 후 새 기준선에서 재구축 |
| PR #1의 v0.1 전략 문서 | REFERENCE_BASELINE | 사실·가정·미확보 항목을 분리한 선행 자료로 유지 |
| 본 v0.2 문서군 | ACTIVE_CANDIDATE | W00~W08 및 콘텐츠·증거 Gate의 현재 작업 기준선 |

## 3. 서비스 목적과 성과

### 사업 목적

1. KNLSOFT를 DB·SQL 전문 기업으로 명확히 인식시킨다.
2. aTops와 SPACEMON의 역할 차이를 방문자가 스스로 판단할 수 있게 한다.
3. AI를 독립적인 유행어가 아니라 검증 가능한 분석 지원 역할로 설명한다.
4. 기술 검토자가 도입 가능성·제약·증거를 확인한 뒤 상담 또는 데모 요청으로 이동하게 한다.
5. 기존 고객이 최신 자료와 지원 경로를 빠르게 찾게 한다.

### 사용자 성과

- 5초 안에 회사 전문 영역과 두 제품의 역할을 이해한다.
- 자신의 문제에 맞는 제품과 다음 검토 자료를 찾는다.
- AI가 무엇을 입력받아 어떤 분석을 제공하고 누가 판단하는지 이해한다.
- 확인되지 않은 기능·성과에 오도되지 않는다.
- 문의가 접수·검증·배정·응답되는 상태를 예측할 수 있다.

### 측정 원칙

초기에는 수치를 임의 확정하지 않는다. 분석 도구와 실제 트래픽이 준비된 뒤 기준선을 측정하고 목표를 승인한다.

| Outcome | 측정 후보 | 확정 조건 |
|---|---|---|
| 역할 이해 | 5초 테스트의 회사/제품 역할 정답률 | 대표 사용자 테스트 5명 이상 |
| 제품 탐색 | 제품 페이지 도달, 주요 근거 열람, CTA 이동 | 분석 이벤트 정의·동의 정책 승인 |
| 리드 품질 | 유효 문의율, 제품·도입시기·환경 정보 충족률 | CRM/담당자 분류 기준 확정 |
| 지원 효율 | 지원 자료 탐색 성공, 중복 문의 감소 | 기존 지원 기준선 확보 |
| 신뢰 | 사실 오인·과장 인지·증거 부족 피드백 | 인터뷰 질문과 판정 기준 승인 |

## 4. 방법론 프로파일

| Profile | 적용 범위 | 핵심 규칙 |
|---|---|---|
| A 콘텐츠형 | 회사·제품·기술·사례·자료 | 정확성, 최신성, 검색성, 소유자, 근거, 버전 |
| E AI형 | aTops AI, SPACEMON AI, AI & Technology | 입력·분석·출력·근거·한계·사람의 판단을 함께 표시 |
| C 업무형 일부 | 문의·데모·CMS·지원 접수 | 역할, 권한, 상태, 예외, 복구, 감사 기록 |

## 5. W00~W14 산출물 체계

| 단계 | 질문 | 필수 산출물 | 현재 상태 |
|---|---|---|---|
| W00 Intake | 무엇이 사실이고 무엇이 미확보인가 | Source Register, Assumption Log, 폐기 범위 | PARTIAL |
| W01 Purpose & Outcome | 누구의 어떤 결과를 만들 것인가 | Outcome Map, KPI 가설 | CANDIDATE |
| W02 User · Role · Context | 누가 어떤 맥락에서 쓰는가 | Role Matrix | CANDIDATE |
| W03 Job · Journey · Scenario | 어떤 과업과 실패를 다루는가 | Journey, Scenario Catalog | CANDIDATE |
| W04 Content · Data · Evidence | 무엇을 어떤 근거로 말하는가 | Claim–Data–Evidence Matrix | BLOCKED/PARTIAL |
| W05 Functional Architecture | 어떤 서비스 기능이 필요한가 | Capability Map, Boundary | CANDIDATE |
| W06 IA · Navigation · Task · State | 어떻게 찾고 이동하며 상태를 아는가 | Sitemap, Task/State Flow | CANDIDATE |
| W07 Policy · Permission · Security | 누가 무엇을 보고 바꾸는가 | Policy/RBAC/PII Matrix | CANDIDATE |
| W08 UX · Interaction Specification | 화면이 어떻게 반응하는가 | Interaction Contract | CANDIDATE |
| W09 Visual Design | 설계를 어떤 시각 체계로 표현하는가 | 대표 화면, Visual System | NOT EXECUTED |
| W10 Technical Architecture | 어떤 기술 구조로 실행하는가 | Front/CMS/API/Analytics/Security Architecture | NOT EXECUTED |
| W11 Implementation | 승인 설계를 어떻게 구현하는가 | Source, Content Migration | STOPPED |
| W12 Test · Validation · Evidence | 결과가 설계·사실·품질을 지키는가 | Test/Evidence Pack | NOT EXECUTED |
| W13 Release · Operation | 어떻게 안전하게 공개·운영하는가 | Release/Runbook/Rollback | NOT EXECUTED |
| W14 Measure · Improve | 실제 결과로 무엇을 개선하는가 | Measurement Review, Backlog | NOT EXECUTED |

## 6. 상위 설계 원칙

1. 사실이 없으면 `확정`, `검증`, `개념`, `예정`, `금지` 상태로 분리한다.
2. 한 주장에는 데이터 원천, 증거, 소유자, 검토일, 공개 권한이 있어야 한다.
3. aTops와 SPACEMON을 하나의 통합 제품처럼 표현하지 않는다.
4. AI는 분석 보조이며 자동 승인·자동 해결·100% 정확성을 암시하지 않는다.
5. 페이지와 섹션은 하나의 사용자 질문 또는 과업에 책임을 진다.
6. 장식이 정보 구조·근거·실패 처리를 대신하지 못한다.
7. 구현은 승인된 대표 화면과 명세를 변경 없이 재현해야 한다.

## 7. 의사결정

### Apply now

- W00~W08 문서군을 현행 Candidate 기준선으로 적용한다.
- 공개 화면과 기존 CSS를 `DEPRECATED_REFERENCE`로 격리한다.
- aTops=운영 전 SQL 품질, SPACEMON=운영 중 DB 성능이라는 경계를 사용한다.
- 검증되지 않은 AI 기능·성과는 공개 카피에서 제외한다.

### Do not apply now

- 새 Hero, 하단 레이아웃, 디자인 토큰, 최종 메뉴 시각화.
- 기존 시안의 통합 콘솔·가공 UI를 실제 제품 증거로 사용하는 것.
- 고객 로고, 성과 수치, 지원 DBMS, 폐쇄망, 연계 기능의 무근거 공개.

### Defer

- W09 Visual Design, W10 기술 선택, W11 구현, 실제 배포.

### Trigger

- Wireframe: Content & Evidence Gate `CEG-WF` PASS.
- Visual Design: `CEG-VD` PASS와 대표 페이지 와이어프레임 승인.
- Implementation: 대표 Visual Design, interaction contract, content snapshot 승인.
- Release: W12 검증 증적과 명시적 Production GO.

