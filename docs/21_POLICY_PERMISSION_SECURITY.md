# KNLSOFT Policy · Permission · Security v0.2 Candidate

## 1. 공개/운영 역할

| Role | Read | Create/Edit | Review | Approve/Publish | Withdraw | Audit |
|---|---|---|---|---|---|---|
| Public Visitor | Published public content | Inquiry/Demo submission | - | - | 본인 요청의 삭제 요구 | 자신의 접수 확인 범위 |
| Content Owner | Assigned content/evidence | Draft | 자기 점검 | - | 회수 요청 | 자기 변경 이력 |
| Technical Reviewer | 제품·기술 대상 | Review note | 기술 사실 | - | 차단 요청 | 기술 검토 이력 |
| Claim/Legal Reviewer | Claim·권리 대상 | Review note | 공개 적정성 | - | 차단 요청 | 검토 이력 |
| Publisher | Approved content | 게시 설정 | 승인 완결성 | Schedule/Publish | Withdraw | 게시 이력 |
| Form Operator | Assigned leads | 상태·담당 업데이트 | 유효성 | Close/Reject | - | 라우팅 이력 |
| Administrator | 시스템 설정 | 역할·정책 설정 | - | 긴급 차단 | 긴급 회수 | 전체, 최소권한 |

작성자 단독 승인·게시를 기본 허용하지 않는다. 소규모 운영으로 겸직이 불가피하면 이중 확인과 감사 사유를 요구한다.

## 2. 콘텐츠 정책

- 공개 대상은 `APPROVED/PUBLISHED`이며 `VERIFY`와 권리 미확보 자산은 제외한다.
- 제품·AI·지원 DBMS 콘텐츠는 버전과 검토일을 갖는다.
- 고객·사례·성과·인용은 공개 범위와 만료일을 갖는다.
- 승인 후 원본이 바뀌면 승인 상태를 자동 승계하지 않는다.
- 긴급 회수는 가능하되 사유·영향 페이지·대체 경로를 기록한다.

## 3. 문의·개인정보 정책

### 최소 수집 후보

- 목적, 관심 제품, 이름, 회사/기관, 업무 이메일 또는 연락 수단, 역할, 관심 과업, 환경 요약, 동의.
- 민감정보, 비밀번호, 운영 로그, 실제 SQL, 고객 데이터의 입력을 요구하지 않는다.

### 처리 원칙

- 수집 목적, 필수/선택, 보유 기간, 수신 주체, 삭제 요청 경로를 제출 전에 표시한다.
- 영업, 파트너, 지원 접수를 목적별로 라우팅하고 목적 외 이용을 금지한다.
- 정확한 보존 기간과 위탁/국외 이전은 법무·운영 확인 전 확정하지 않는다.
- PII는 애플리케이션 로그·분석 이벤트·오류 메시지에 원문으로 남기지 않는다.

## 4. 보안 기본선

- Server-side validation, output encoding, CSRF/Origin 검토, rate limit, bot/spam 방어.
- 전송/저장 암호화, 비밀정보 소스 분리, 최소 권한, 관리자 MFA를 기술 설계에서 강제.
- 업로드 기능은 현재 범위에서 제외한다. 도입 시 파일형식·크기·악성코드·보관·삭제 정책을 별도 승인한다.
- 보안 헤더, 의존성 점검, 관리자 감사 로그, 백업·복구, 취약점 대응 책임을 W10/W13에서 구체화한다.
- 분석 도구는 동의 정책을 따르며 필수 기능과 분리한다.

## 5. 권한·상태 실패 처리

| Failure | 사용자 표시 | 운영 처리 | 증거 |
|---|---|---|---|
| 권한 없음 | 존재 여부를 과도하게 노출하지 않는 안내 | 권한 요청/담당자 안내 | actor, resource, time, result |
| 승인 없는 게시 시도 | 게시 불가와 미충족 Gate | 승인자에게 반환 | missing gate list |
| 만료 증거 참조 | 현재 게시 차단 또는 대체 | 영향 Claim/Page 탐색 | dependency trace |
| 문의 라우팅 실패 | 접수 유지, 지연·대체 연락 안내 | 재시도/수동 큐 | error ID, retry |
| 중복 제출 | 새 접수 남발 금지 | 기존 접수 연결 | idempotency record |

## 6. Apply Decision

- Apply now: 역할 분리, 최소수집, 로깅 금지, 보안 기본선.
- Do not apply: 보유기간·SLA·위탁사를 임의 확정, 파일 업로드 추가.
- Defer: 실제 IAM/CMS/CRM/메일 제품과 세부 보안 설정.
- Trigger: 개인정보 책임자, 운영 수신자, 법무 검토, W10 기술 선택.

