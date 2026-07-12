# KNLSOFT Claim–Data–Evidence Matrix v0.2 Candidate

## 1. 상태 정의

| Status | 의미 | 공개 사용 |
|---|---|---|
| OFFICIAL | 최신 공식 원본과 소유자 승인 완료 | 가능 |
| VERIFIED | 시험·문서·화면 등 재현 가능한 근거 확인 | 가능, 범위·버전 표시 |
| VALIDATED_CONCEPT | 개념·설계이며 실제 기능이 아님 | `개념/예시` 라벨 아래 제한적 |
| VERIFY | 근거 회수 또는 최신성 확인 필요 | 사실형 카피 금지 |
| OPTION | 계약·구성·환경에 따라 제공 | 조건을 함께 표시 |
| ROADMAP | 계획 또는 후보 | 현재 기능과 분리 |
| PROHIBITED | 과장·절대·오인 가능 | 금지 |
| EXPIRED | 버전·권리·승인 만료 | 게시 중지 |

## 2. 핵심 매트릭스

| ID | 공개 주장 후보 | Status | 필요한 Data | 통과 Evidence | Owner | 현재 사용 |
|---|---|---|---|---|---|---|
| C-001 | KNLSOFT는 DB·SQL 기술을 중심으로 제품을 제공한다 | VERIFY | 회사 소개·제품 포트폴리오 | 공식 회사소개/사업자·제품자료 승인 | Management | 안전 문구만 |
| C-002 | aTops는 SQL 품질관리 플랫폼이다 | VERIFY | 최신 제품 정의 | 버전 명시 제품 명세 | aTops PO | 카테고리 표현만 |
| C-003 | aTops는 SQL 품질·성능 진단을 지원한다 | VERIFY | 기능 목록·입출력 | 실제 화면, 매뉴얼, 테스트 | aTops R&D | 상세 기능 보류 |
| C-004 | aTops는 개발/운영 SQL 비교를 지원한다 | VERIFY | 비교 기준·키·결과 | 실제 사례와 화면 | aTops R&D | 상세 기능 보류 |
| C-005 | aTops AI가 SQL 위험·실행계획을 해석한다 | VERIFY | AI 입력·모델·출력 | 동작 캡처, 테스트, 제한 | AI Owner | 비공개 |
| C-006 | aTops AI가 개선 권고를 제시한다 | VERIFY | 권고 생성·검증 흐름 | 입력/출력/검토 증적 | AI Owner | 비공개 |
| C-007 | SPACEMON은 이기종 DBMS 통합 모니터링을 지원한다 | VERIFY | 지원 DBMS/버전/항목 | 최신 지원 매트릭스와 화면 | SPACEMON PO | 일반 표현만 |
| C-008 | SPACEMON은 실시간 성능·SQL 분석과 알림을 지원한다 | VERIFY | 수집 주기·분석·알림 조건 | 매뉴얼, 화면, 테스트 | SPACEMON R&D | 범위 확인 전 보류 |
| C-009 | SPACEMON AI가 이상·시계열 패턴을 분석한다 | VERIFY | 입력 시계열·탐지 결과 | 동작 예시, 평가 방법 | AI Owner | 비공개 |
| C-010 | SPACEMON AI가 원인 후보를 권고한다 | VERIFY/ROADMAP | 후보 생성·근거·정확도 | 실제 I/O, 검토 이력 | AI Owner | 비공개 |
| C-011 | 폐쇄망/On-Premise 구성이 가능하다 | OPTION/VERIFY | 제품별 배포 구조 | 승인 아키텍처·보안 검토 | Architect/Security | 비공개 |
| C-012 | 금융·공공 고객이 사용한다 | APPROVAL/VERIFY | 고객·사업·공개 범위 | 서면 승인, 유효 기간 | Sales/Legal | 비공개 |
| C-013 | 특정 품질·성능 효과가 있다 | VERIFY | 기준선·표본·조건·측정 | 재현 가능한 측정 보고서 | Product/Customer | 수치 금지 |
| C-014 | 인증·특허를 보유한다 | VERIFY | 번호·명칭·유효 상태 | 공식 증서/등록 정보 | Management | 확인 전 보류 |
| C-015 | 전문 지원·유지보수를 제공한다 | VERIFY | 채널·시간·범위·SLA | 승인 운영 정책 | Support | 일반 문의만 |
| C-016 | 두 제품이 운영 전후를 자동 연결한다 | PROHIBITED until verified | 공통 ID·API·상태·책임 | E2E 테스트와 운영 증적 | Cross Product Owner | 금지 |
| C-017 | AI가 자동 승인·자동 해결한다 | PROHIBITED | 해당 없음 | 해당 없음 | Governance | 금지 |

## 3. 증거 최소 단위

모든 Evidence는 다음 메타데이터를 가져야 한다.

- Evidence ID, 주장 ID, 제품/버전, 원본 위치, 생성자, 검토자.
- 생성/검토/만료일, 고객 데이터 마스킹, 공개 권리.
- 재현 절차 또는 원본 문서 번호, 적용 범위, 알려진 제한.
- 화면 가공 여부와 원본 보존 여부.

## 4. 게시 규칙

1. `VERIFY`는 내부 문서에는 표시할 수 있으나 공개 사실형 문장에 사용할 수 없다.
2. `OPTION`은 조건을 같은 화면에 표시한다.
3. `ROADMAP`은 현재 기능과 시각적으로 분리하고 날짜를 보장하지 않는다.
4. 개념 화면은 실제 UI와 혼동되지 않도록 `개념 시각화`를 화면 내부 또는 바로 인접 위치에 표시한다.
5. 수치는 측정 조건과 승인 없이 게시하지 않는다.

## 5. Apply Decision

- Apply now: 상태 모델, C-001~017, 증거 메타데이터.
- Do not apply: `VERIFY` 항목을 기존 웹 카피의 근거로 승격.
- Defer: 실제 Evidence ID와 파일 연결.
- Trigger: 공식 원본 수령 및 제품/법무 소유자 승인.

