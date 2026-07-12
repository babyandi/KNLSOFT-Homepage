# KNLSOFT User · Role · Buying Journey v0.2 Candidate

## 1. 역할 분류 원칙

방문자를 직책 하나로 단순화하지 않는다. 한 사람도 탐색 단계에 따라 사용자, 기술 평가자, 보안 검토자, 구매 승인자 역할을 함께 가질 수 있다.

| Role | 주요 맥락 | 핵심 질문 | 완료 과업 | 필요한 증거 | 주 CTA |
|---|---|---|---|---|---|
| Executive Sponsor | 장애·품질·비용·책임 리스크를 줄여야 함 | 왜 지금, 어떤 사업 효과인가 | 검토 우선순위와 예산 논의 결정 | 문제-가치 구조, 승인 사례, 측정 방식 | 도입 상담 |
| Economic Buyer / Procurement | 비교·계약·공급 안정성 검토 | 범위·구축·지원·계약 조건은 무엇인가 | RFI/RFP 또는 견적 절차 진입 | 회사·지원·구축 범위, 공식 자료 | 견적·도입 문의 |
| Technical Evaluator | 제품 적합성과 연계 난이도 검토 | 무엇을 수집·분석하고 어디까지 지원하는가 | 기술 검토 목록 작성, 데모 요청 | 기능 명세, 아키텍처, DBMS/버전, 제약 | 기술 데모 |
| DBA / Operations | 운영 성능·이상·원인 분석 | 현장 과업이 어떻게 빨라지는가 | SPACEMON 적합성 판단 | 실제 화면, 흐름, 지원 범위 | SPACEMON 데모 |
| Development / SQL Quality Lead | 운영 전 SQL 위험 통제 | 개발·검증·승인 흐름을 어떻게 관리하는가 | aTops 적합성 판단 | 실제 프로세스, 규칙, 비교·이력 근거 | aTops 데모 |
| Security / Architecture | 데이터 반출·권한·망 구성 검토 | 어떤 데이터가 어디서 처리되는가 | 보안 검토 가능/조건부/불가 판단 | 배포 구조, 데이터 흐름, 권한, 로그 | 보안·기술 문의 |
| Existing Customer | 버전별 자료와 지원 필요 | 최신 문서와 접수 경로는 어디인가 | 문서 확보 또는 지원 접수 | 버전, 공개범위, 지원 절차 | 자료 찾기/지원 접수 |
| Partner / SI | 공동 제안·연계 가능성 검토 | 역할·책임·연계 범위는 무엇인가 | 파트너 상담 진입 | 제품 경계, 연계 조건, 지원 체계 | 파트너 문의 |
| Content Owner | 제품·회사 콘텐츠 관리 | 무엇을 언제 갱신해야 하는가 | 초안·근거 제출 | 데이터 원천, 검토일, 소유자 | CMS 초안 |
| Reviewer / Approver | 사실·법무·공개 적정성 검토 | 이 주장을 공개해도 되는가 | 승인/반려/만료 판정 | 증거, 권리, 변경 이력 | 검토 Gate |

## 2. 구매 의사결정 흐름

| Stage | 사용자 질문 | 사이트 책임 | 주요 진입 | 다음 상태 |
|---|---|---|---|---|
| B0 Trigger | SQL 품질/DB 성능 문제가 왜 반복되는가 | 문제를 과장 없이 구조화 | Home, 검색, 공유 링크 | AWARE |
| B1 Category | 어떤 관리 범주가 필요한가 | 운영 전 품질과 운영 중 성능을 구분 | Home, 제품 비교 | ORIENTED |
| B2 Product Fit | aTops 또는 SPACEMON이 내 과업에 맞는가 | 역할·사용자·입력·출력·제약 설명 | Product overview | FIT_CANDIDATE |
| B3 Technical Fit | 환경·DBMS·망·연계 조건이 맞는가 | 검증된 기술 조건과 미지원 범위 제공 | Architecture, support matrix | TECH_REVIEW |
| B4 Trust | 실제로 믿을 근거가 있는가 | 화면·문서·사례·자격·측정 근거 제공 | Evidence, case, resources | EVIDENCE_REVIEW |
| B5 Evaluation | 데모/미팅에서 무엇을 확인할 것인가 | 제품·환경·관심 과업을 사전 수집 | Demo request | REQUESTED |
| B6 Internal Approval | 조직 내 검토 자료를 확보했는가 | 버전 관리된 문서와 연락 창구 제공 | Resources, inquiry | QUALIFIED |
| B7 Procurement | 견적·범위·일정을 논의할 수 있는가 | 담당자에게 안전하게 배정 | Inquiry workflow | IN_DISCUSSION |
| B8 Adoption/Support | 도입 후 어디서 지원받는가 | 문서·릴리스·지원 접수 제공 | Support | CUSTOMER_SERVICE |

## 3. 제품별 핵심 Journey

### aTops Journey

SQL 품질 문제 인지 → 운영 전 관리 범주 이해 → 개발/검증/비교/이력 과업 확인 → 지원 환경·연계 조건 확인 → 실제 증거 검토 → aTops 데모 요청.

### SPACEMON Journey

운영 성능·이상 문제 인지 → 실시간 관찰·SQL 분석 범주 이해 → DBMS별 지원 과업 확인 → 배포·데이터 수집 조건 확인 → 실제 증거 검토 → SPACEMON 데모 요청.

### AI Journey

문제 데이터 확인 → 규칙/통계 분석과 AI 분석의 역할 구분 → 입력·출력·근거·한계 확인 → 사람의 검토·결정 위치 확인 → 해당 제품 데모로 이동.

AI Journey는 별도의 AI 제품 구매 흐름으로 만들지 않는다. 공식 제품 전략이 확인되면 재검토한다.

## 4. 이탈·불확실성 처리

- 제품을 결정하지 못한 사용자는 `제품 선택 진단`이 아니라 두 제품의 역할 비교와 일반 상담으로 연결한다.
- 검증 자료가 없는 질문에는 답을 만들어내지 않고 `확인 필요`와 담당 문의를 제시한다.
- 데모 요청은 예약 확정이 아니라 접수이며, 담당자 확인 전 시간을 확정하지 않는다.
- 기존 고객 지원과 신규 영업 문의를 같은 폼/상태로 섞지 않는다.

## 5. Apply Decision

- Apply now: 역할·단계·질문·증거·CTA 매핑.
- Do not apply: 직책별 별도 페이지의 무조건적 생성, 자동 제품 추천, 자동 데모 확정.
- Defer: 실제 CRM 단계와 SLA 수치.
- Trigger: 영업·지원 운영 절차와 개인정보 정책 승인.

