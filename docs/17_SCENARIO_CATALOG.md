# KNLSOFT Normal · Exception · Recovery Scenario Catalog v0.2 Candidate

## 1. 시나리오 규칙

각 시나리오는 Actor, Trigger, Preconditions, Normal Flow, Exception, Recovery, Output, Evidence, Owner를 갖는다. 성공 화면만 설계하지 않는다.

## 2. 탐색·의사결정 시나리오

### SCN-01 회사·제품 역할 이해

- Actor: 처음 방문한 Executive/Technical Evaluator.
- Trigger: 검색, 공유 링크, 캠페인으로 Home 진입.
- Normal: 회사 전문 영역 확인 → aTops/SPACEMON 역할 구분 → 관심 제품 이동.
- Exception: AI 회사로 오인하거나 두 제품이 하나의 통합 콘솔이라고 이해.
- Recovery: Hero 바로 아래 제품 시간축 비교, AI 보조 원칙, 제품별 상세 링크 제공.
- Evidence: 5초 테스트 응답, 클릭/회상 테스트.

### SCN-02 aTops 적합성 검토

- Actor: SQL Quality Lead/DBA.
- Normal: 운영 전 문제 → 사용자 과업 → 기능 → 입력/출력 → 지원 조건 → 실제 증거 → 데모.
- Exception: 최신 기능·지원 환경이 미확인.
- Recovery: 확인되지 않은 항목은 숨기거나 `확인 필요`로 격리하고 기술 문의 경로 제공.
- Output: `FIT_CANDIDATE` 또는 `NEEDS_CONFIRMATION`.

### SCN-03 SPACEMON 적합성 검토

- Actor: DBA/Operations.
- Normal: 운영 성능 문제 → 모니터링/SQL 분석 → DBMS 지원 → 배포 조건 → 증거 → 데모.
- Exception: DBMS별 지원 기능이 다르나 동일 지원처럼 읽힘.
- Recovery: 제품 공통 기능과 DBMS별 조건을 분리하고 최신 지원 매트릭스로 연결.

### SCN-04 AI 역할·한계 검토

- Actor: Technical/Security/Executive.
- Normal: 실제 입력 → 기존 분석 → AI 해석/권고 → 근거 → 사람 검토 → 제품 데모.
- Exception: 자율 운영·자동 승인으로 오인.
- Recovery: 출력 옆에 `권고`, `검토 필요`, 제한과 책임 주체를 명시.
- Output: `AI_UNDERSTOOD`, `AI_EVIDENCE_REQUIRED`.

### SCN-05 제품을 결정하지 못함

- Actor: 일반 구매 검토자.
- Normal: 문제·적용 시점 기준 비교 → 관심 제품 선택 또는 일반 상담.
- Exception: 자동 진단이 근거 없이 제품을 추천.
- Recovery: 결과를 추천이 아닌 탐색 가이드로 표시하고 담당자 확인 전제.

## 3. 전환·업무 시나리오

### SCN-06 데모 요청 정상

- Preconditions: 개인정보 고지·동의, 필수 항목, 수신 경로 활성.
- Normal: 제품 선택 → 조직/역할/환경/관심과제 입력 → 검증 → 제출 → 접수번호/예상 다음 단계 안내 → 담당 배정.
- Output: `SUBMITTED` → `VALIDATED` → `ROUTED`.
- Evidence: 서버 접수 기록, 라우팅 기록, 사용자 확인 메시지.

### SCN-07 데모 요청 검증 실패

- Exception: 필수값 누락, 비정상 이메일, 동의 없음, 스팸 의심.
- Recovery: 입력값 보존, 문제 필드 인접 오류, 요약 오류, 재제출 가능. 스팸 판정 세부 규칙은 노출하지 않음.
- 금지: 입력 전체 초기화, 모호한 `오류가 발생했습니다`만 표시.

### SCN-08 데모 요청 전송 실패

- Exception: API/메일/CRM 장애, 중복 제출, 시간 초과.
- Recovery: idempotency key로 중복 방지 → 재시도 가능 상태 → 대체 연락처 제공 → 운영 알림.
- Output: `RETRYABLE_FAILED` 또는 `MANUAL_FOLLOWUP_REQUIRED`.
- Evidence: 오류 ID, 발생 시각, 재시도 결과. 개인정보를 로그에 직접 남기지 않음.

### SCN-09 지원 접수

- Actor: Existing Customer.
- Normal: 제품/버전/문의유형 확인 → 공개 가이드 우선 제시 → 해결 안 되면 지원 채널.
- Exception: 신규 영업 문의로 잘못 라우팅.
- Recovery: 지원과 영업 상태·담당 큐를 분리하고 재배정 이력을 남김.

### SCN-10 CMS 발행

- Actor: Content Owner/Reviewer/Approver.
- Normal: 초안 → 기술 검토 → Claim 검토 → 권리/법무 검토 → 승인 → 예약/발행.
- Exception: 증거 없음, 만료, 권리 미확인, 승인 후 원본 변경.
- Recovery: 발행 차단 → 이전 승인 버전 유지 → 수정 초안 생성 → 재검토.

### SCN-11 게시 콘텐츠 만료·회수

- Trigger: 제품 릴리스, 권리 만료, 고객 승인 철회, 오류 발견.
- Normal: 영향 Claim/Page 탐색 → 게시 중지 또는 대체 → 리디렉션/이력 보존 → 재검토.
- Evidence: 누가, 언제, 왜, 무엇을 회수했는지 기록.

## 4. 비기능 시나리오

| ID | 상황 | 기대 동작 | Recovery/Evidence |
|---|---|---|---|
| SCN-12 | 320px~400% 확대/Reflow | 가로 스크롤 없이 의미 순서 유지 | WCAG 2.2 Reflow 캡처·DOM 순서 검증 |
| SCN-13 | 키보드만 사용 | 메뉴·탭·폼·모달 완전 사용, 초점 표시 | 키보드 경로 기록 |
| SCN-14 | 이미지 차단/느린 네트워크 | 핵심 의미와 CTA 유지, 레이아웃 급변 최소화 | 네트워크 제한 테스트 |
| SCN-15 | JS 일부 실패 | 주요 콘텐츠와 연락 경로 열람 가능 | 오류 경계·서버 렌더 확인 |
| SCN-16 | 분석/동의 거부 | 사이트와 문의 사용 가능, 비필수 추적 미실행 | Consent 로그 검증 |
| SCN-17 | 오래된 공유 URL | 정식 대상 또는 설명 가능한 404로 이동 | Redirect/404 목록 테스트 |

## 5. Apply Decision

- Apply now: SCN-01~17을 와이어프레임·기능·테스트 입력으로 사용.
- Do not apply: 자동 제품 추천, 자동 예약 확정, 지원/영업 단일 큐.
- Defer: 실제 CRM·메일·지원 시스템 연동 방식.
- Trigger: 운영 담당자, 개인정보 정책, 연동 시스템 확정.

