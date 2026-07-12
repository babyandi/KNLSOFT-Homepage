# KNLSOFT Functional Architecture v0.2 Candidate

## 1. 기능 아키텍처 원칙

기능은 화면 목록이 아니라 사용자 결과와 운영 책임을 제공하는 Capability로 정의한다. Profile A를 중심으로 E와 C를 필요한 곳에만 결합한다.

## 2. Capability Map

| Layer | Capability | 책임 | Profile | 현재 결정 |
|---|---|---|---|---|
| Experience | Global Navigation | 역할·제품·지원 경로 탐색 | A | APPLY |
| Experience | Product Role Comparison | aTops/SPACEMON 시간축·문제 경계 이해 | A/E | APPLY |
| Experience | Evidence Presentation | 화면·문서·사례·제약의 근거 표시 | A | APPLY |
| Experience | AI Explanation | 입력-분석-출력-근거-사람판단 설명 | E | APPLY |
| Experience | Resource Discovery | 제품/버전/유형별 자료 탐색 | A/C | APPLY, 자료 존재 확인 필요 |
| Conversion | Demo Request | 제품·과업·환경을 포함한 접수 | C | APPLY |
| Conversion | General/Partner Inquiry | 목적별 라우팅 | C | APPLY |
| Support | Support Entry | 기존 고객 지원 경로 분리 | C | APPLY, 범위 확인 필요 |
| Content Ops | Structured CMS | Product/Feature/AI/Case/Document 관리 | A/C/E | APPLY |
| Governance | Claim & Evidence Registry | 주장-근거-소유자-만료 연결 | A/E | APPLY |
| Governance | Review Workflow | 기술·Claim·권리·법무 승인 | C | APPLY |
| Governance | Publication Control | 승인·예약·회수·대체 | C | APPLY |
| Platform | Search/Index/SEO | 검색과 정식 URL 제공 | A | APPLY |
| Platform | Form Routing | 검증·중복방지·배정·상태 | C | APPLY |
| Platform | Consent/Analytics | 최소 동의와 결과 측정 | C | DEFER 상세 도구 |
| Platform | Audit/Observability | 실패·발행·라우팅의 추적 | C | APPLY 원칙 |
| Platform | Security/Privacy | PII 최소화, 권한, 보존, 삭제 | C | APPLY 원칙 |

## 3. 논리 구성

### Public Experience

- Home, Company, aTops, SPACEMON, AI & Technology, Resources, Support, Inquiry.
- 렌더링된 텍스트가 사실과 접근성의 기준이며 이미지 속 텍스트가 기준이 되지 않는다.
- 제품 UI는 원본/가공/개념을 구분한다.

### Content & Evidence Domain

- Product, Feature, AI Capability, Supported Technology, Case, Credential, Document.
- Claim, Evidence, Approval, Rights, Version, Publication State.
- 모든 공개 블록은 콘텐츠 객체와 Claim 상태를 참조한다.

### Workflow Domain

- Inquiry/Demo Request, validation, routing, acknowledgment, assignment, closure.
- Content draft, review, approval, publication, expiration, withdrawal.

### Integration Boundary

- 이메일, CRM, 캘린더, 헬프데스크, 분석, 스토리지, 검색은 Adapter 경계로 둔다.
- 특정 도구를 W10 전에 고정하지 않는다.
- 연동 실패가 공개 콘텐츠 열람을 중단시키지 않게 한다.

## 4. 범위 경계

### In Scope

- 제품·AI 설명, 증거·자료, 회사 신뢰 정보, 데모/문의/지원 진입, CMS와 승인 흐름, 검색·SEO·접근성·분석 준비.

### Out of Scope until approved

- 고객 포털 로그인, 라이선스 관리, 제품 원격 운영, AI 챗봇, 자동 견적, 자동 일정 예약, 실시간 제품 데이터 연동, 고객별 대시보드.

## 5. 기능 우선순위

| Priority | Capability | 이유 |
|---|---|---|
| P0 | 구조화 콘텐츠, Claim/Evidence, 제품 경계, 페이지 탐색 | 사실과 설계의 기반 |
| P0 | 데모/문의 검증·라우팅·복구 | 핵심 전환과 업무 연결 |
| P0 | 접근성·반응형·보안 기본 | 출시 전 필수 |
| P1 | 자료 검색·필터, 지원 진입 | 기존 고객과 기술 평가 지원 |
| P1 | CMS 승인·만료·회수 | 운영 지속성 |
| P2 | 분석 대시보드·개선 루프 | 실제 트래픽 이후 |
| HOLD | 챗봇·자동 추천·개인화 | 근거·운영·개인정보 미확보 |

## 6. Apply Decision

- Apply now: Capability와 경계, P0/P1 우선순위.
- Do not apply: 솔루션/프레임워크/벤더 확정, 고객 포털·챗봇 추가.
- Defer: W10 기술 아키텍처와 비용/운영 모델.
- Trigger: W08 승인, CMS 운영자·폼 수신자·개인정보 책임자 확정.

