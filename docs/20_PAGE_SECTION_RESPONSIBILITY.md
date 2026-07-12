# KNLSOFT Page · Section Responsibility Matrix v0.2 Candidate

## 1. 책임 정의

페이지는 정보를 모아두는 그릇이 아니라 사용자의 하나 이상의 결정에 책임을 진다. 섹션은 `Question → Answer → Evidence → Next action` 계약을 갖는다.

## 2. Page Responsibility

| Page | 결정 질문 | 필수 답변 | 필수 증거 | 금지 | Exit |
|---|---|---|---|---|---|
| Home | KNLSOFT와 두 제품은 내 문제와 관련 있는가 | 회사 전문영역, 제품 경계, AI 역할 | 최소 1개 검증 신뢰군 또는 `증거 준비 중` 내부 차단 | 통합 콘솔·가공 수치·과장 AI | 제품/상담 |
| Product Comparison | 운영 전 품질과 운영 중 성능 중 무엇을 검토해야 하는가 | 시간축, 사용자, 과업, 입력/출력 | 각 제품 공식 정의 | 자동 추천 | 제품 상세 |
| aTops | aTops가 내 SQL 품질 과업에 맞는가 | 문제, 과업, 기능, 환경, AI, 제약 | 최신 명세·실제 화면·지원 범위 | 자동 튜닝 완료 | aTops 데모 |
| SPACEMON | SPACEMON이 내 DB 운영 과업에 맞는가 | 모니터링·분석·DBMS 조건·AI·제약 | 최신 명세·실제 화면·지원 매트릭스 | 자동 원인 해결 | SPACEMON 데모 |
| AI & Technology | AI를 어디까지 신뢰·통제할 수 있는가 | 입력, 기존 분석, AI, 출력, 근거, 사람, 보안 | 실제 I/O·아키텍처·제한 | 자율/100%/장식형 AI | 제품 데모/기술문의 |
| Evidence/Case | 무엇으로 효과와 신뢰를 판단할 수 있는가 | 문제, 범위, 측정, 결과, 승인 | 고객 승인·측정 원본·자격 | 익명 사례를 실제 고객처럼 표현 | 상담/자료 |
| Resources | 최신이고 내 환경에 맞는 자료는 무엇인가 | 제품, 유형, 버전, 유효일 | 원본·체크섬·소유자 | 구버전 무표시 | 열람/지원 |
| Support | 기존 고객은 어디서 해결하는가 | 지원 범위, 자료, 접수 경로 | 운영 정책·최신 문서 | 영업 폼과 혼합 | 자료/지원 접수 |
| Company | 공급자로 신뢰할 수 있는가 | 회사 사실, 역량, 연혁, 자격, 연락 | 공식 회사자료·증서 | 임의 연혁·고객 로고 | 문의/오시는 길 |
| Demo/Inquiry | 어떤 정보로 다음 검토를 시작하는가 | 목적, 제품, 과업, 환경, 처리 안내 | 개인정보 고지·수신 운영 | 즉시 확정·불명확한 SLA | 접수 확인 |

## 3. Home Section Responsibility

| Order | Section | 사용자 질문 | Content 상태 | Evidence Gate | Visual 책임 |
|---:|---|---|---|---|---|
| 1 | Hero | 이 회사는 무엇을 해결하는가 | SAFE_COPY | CEG-WF | 강한 초점 1개, CTA 2개 이하 |
| 2 | Product Boundary | aTops와 SPACEMON은 어떻게 다른가 | CANDIDATE | 공식 정의 필요 | 시간축·관계, 카드 나열 금지 |
| 3 | aTops Evidence | 운영 전에 무엇을 관리하는가 | VERIFY | 명세+화면 | 실제 증거 중심 |
| 4 | SPACEMON Evidence | 운영 중 무엇을 파악하는가 | VERIFY | 명세+화면 | aTops와 다른 장면 |
| 5 | AI Role | AI가 무엇을 하고 누가 결정하는가 | VERIFY | 실제 I/O | 입력→근거→권고→사람 |
| 6 | Trust | 왜 믿을 수 있는가 | BLOCKED/PARTIAL | 3개 신뢰 범주 중 최소 조건 | 로고 벽보다 근거 우선 |
| 7 | Next Step | 무엇을 준비해 문의하는가 | CANDIDATE | 운영 절차 | 폼 이전 기대 설정 |

## 4. Section Contract Template

- Section ID / Page / Owner / User role.
- User question / promised answer / allowed claim IDs.
- Data source / evidence IDs / content status / review date.
- Primary action / secondary action / success state.
- Empty / loading / error / expired / permission-denied behavior.
- Desktop/tablet/mobile reading order.
- Accessibility name, heading level, alt/description requirement.

## 5. Visual Layout Constraints for W09

- 12컬럼 공통 그리드, 의미 순서가 DOM과 일치.
- 한 화면의 강한 강조 요소 최대 2개.
- 동일 레이아웃을 연속 사용하지 않되, 차이를 만들기 위한 무의미한 장식 금지.
- 한글 의미 단위 조판, `word-break: keep-all`만으로 해결하지 않고 문장 길이·컨테이너 폭을 함께 설계.
- Scale, Visual Hierarchy, Balance, Contrast, Gestalt를 섹션 책임과 함께 검증.

## 6. Apply Decision

- Apply now: 페이지·Home 섹션 책임과 Section Contract.
- Do not apply: 현재 공개 화면에 맞춘 섹션 순서·CSS 수정.
- Defer: 실제 와이어프레임과 최종 콘텐츠 길이.
- Trigger: `CEG-WF` PASS.

