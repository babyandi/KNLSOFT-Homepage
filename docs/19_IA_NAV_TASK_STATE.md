# KNLSOFT IA · Navigation · Task · State v0.2 Candidate

## 1. IA 원칙

상단 메뉴는 조직도가 아니라 사용자의 결정 질문을 따라야 한다. 제품은 독립 진입점을 갖고 AI는 두 제품에 속한 역할을 설명한다.

## 2. Candidate Navigation

| Top | 책임 | 주요 하위 항목 |
|---|---|---|
| 제품 | 두 제품의 역할 비교와 상세 진입 | 제품 비교, aTops, SPACEMON |
| AI & Technology | AI 역할·근거·보안·한계 | AI 원칙, SQL Intelligence, DB Intelligence, 배포/보안 |
| 적용과 증거 | 실제 적용 판단 근거 | 활용 시나리오, 사례, 지원 DBMS, 인증·특허 |
| 리소스 | 버전 있는 기술 자료 탐색 | 브로슈어, 가이드, 릴리스 노트, FAQ |
| 고객지원 | 기존 고객의 해결 경로 | 기술지원, 공지, 다운로드 |
| 회사소개 | 공급자 신뢰 판단 | 회사, 연혁, 역량, 파트너, 오시는 길 |
| CTA | 신규 검토 전환 | 데모·도입 상담 |

`적용과 증거`는 실제 사례·지원·자격 자료가 부족하면 출시 메뉴에서 숨기고 각 제품의 검증된 근거로 축소한다.

## 3. Sitemap Candidate

### Home

회사/제품 역할 → 문제 시간축 → aTops → SPACEMON → AI 역할 → 검증 가능한 신뢰 → 다음 행동.

### Product Comparison

운영 전/운영 중 → 사용자/과업 → 입력/출력 → AI → 지원 조건 → 제품별 이동.

### aTops / SPACEMON

Overview → User Jobs → Verified Features → How It Works → AI → Environment/Security → Evidence → Demo.

### AI & Technology

Principles → Product-specific AI → Data Flow → Evidence/Human Review → Security/Deployment → Limitations.

### Resources / Support

Search/Filter → Result → Version/Validity → View/Download 또는 Support entry.

### Inquiry

Choose Purpose → Provide Context → Review/Consent → Submit → Acknowledge/Next Step.

## 4. Task Flows

### TF-01 제품 선택

문제 시점 선택 → 제품 역할 비교 → 제품 상세 → 기술 조건 → 근거 → 데모.

### TF-02 AI 검토

제품 선택 → AI 입력/분석/출력 → 비AI 분석 구분 → 사람 검토 → 제한 → 제품 데모.

### TF-03 자료 찾기

제품/문서유형/버전 필터 → 결과 → 유효성 확인 → 열람/다운로드 → 관련 지원.

### TF-04 데모 요청

목적/제품 → 관심 과업 → 환경 → 연락정보 → 동의/검토 → 제출 → 접수/복구.

## 5. 상태 모델

### Content State

`DRAFT → TECH_REVIEW → CLAIM_REVIEW → RIGHTS_LEGAL_REVIEW → APPROVED → SCHEDULED/PUBLISHED → SUPERSEDED/EXPIRED/WITHDRAWN`

- 승인된 원본이 변경되면 `DRAFT` 파생 버전을 만들고 기존 Published는 유지한다.
- 만료·회수된 콘텐츠는 직접 접근 시 상태와 대체 자료를 안내한다.

### Inquiry State

`EDITING → SUBMITTED → VALIDATED → ROUTED → ACKNOWLEDGED → IN_REVIEW → CONTACTED → CLOSED`

예외: `VALIDATION_FAILED`, `RETRYABLE_FAILED`, `REJECTED_SPAM`, `MANUAL_FOLLOWUP_REQUIRED`, `DUPLICATE_LINKED`.

### Evidence State

`REGISTERED → OWNER_CONFIRMED → VERIFIED → PUBLICATION_APPROVED → ACTIVE → EXPIRED/REVOKED/SUPERSEDED`.

## 6. URL·이동 규칙

- 한국어 정식 URL 하나를 기준으로 하고 언어 확장 시 별도 locale 전략을 승인한다.
- 구 URL은 사용·검색·자료 링크를 확인한 뒤 301 또는 설명 가능한 대체 경로로 매핑한다.
- 새 탭 강제, 모호한 `자세히 보기`, 동일 페이지 중복 CTA를 최소화한다.
- 현재 위치, 뒤로가기, 필터 URL, 오류 후 입력 상태를 보존한다.

## 7. Apply Decision

- Apply now: IA 후보, 네 개 Task Flow, 세 상태 모델.
- Do not apply: Mega menu 시각 디자인, 검증되지 않은 `적용과 증거` 하위 페이지 공개.
- Defer: 최종 URL, 검색 기술, 다국어.
- Trigger: 콘텐츠 인벤토리와 구 사이트 URL 목록 확보.

