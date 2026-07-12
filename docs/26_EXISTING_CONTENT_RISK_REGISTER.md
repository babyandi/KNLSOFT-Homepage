# KNLSOFT Existing Site Content Risk Register v0.2 Candidate

## 1. 대상

공개 Sites 버전 8과 `knlsoft-ai-products` 시안의 문구·자산을 최종 기준선으로 사용하지 않기 위한 위험 등록부다. 코드가 존재하거나 화면에 보인다는 사실은 제품 증거가 아니다.

## 2. 위험 항목

| Risk ID | 기존 표현/구조 | 위험 | Status | 조치 |
|---|---|---|---|---|
| CR-001 | `6+ SUPPORTED DBMS` | 지원 버전·기능 차이 미표시 | VERIFY/BLOCK | 지원 매트릭스 승인 전 제거 |
| CR-002 | `ON-PREMISE SECURE DEPLOYMENT` | 제품별 배포·보안 근거 없음 | OPTION/VERIFY | 아키텍처·보안 검토 후 조건부 |
| CR-003 | `금융권 구축 경험` | 고객/사업/권리 미확인 | APPROVAL/BLOCK | 승인 사례 없으면 제거 |
| CR-004 | `전 과정 추적` | 범위와 E2E 연결 근거 없음 | VERIFY/HIGH_RISK | 상태·ID·이력 증거 필요 |
| CR-005 | `운영 데이터가 다시 개발 품질을 높이는 선순환` | 자동 폐쇄 루프 오인 | PROHIBITED until verified | 현재 카피에서 제거 |
| CR-006 | `검토·승인, 배포 이력` | aTops 현재 기능/옵션 불명 | VERIFY | 제품 명세와 실제 흐름 필요 |
| CR-007 | `DevOps 기반 변경 이력관리` | Git/배포 연계 옵션·범위 불명 | VERIFY/OPTION | 연계 명세 전 제거 |
| CR-008 | `SPACEMON 143개 이상 KPI` | 버전·DBMS·출처 불명 | VERIFY/BLOCK | 공식 매트릭스 없으면 숫자 제거 |
| CR-009 | `이상 징후·장애 원인 분석` | AI/규칙/수동 분석 경계 불명 | VERIFY | 입력·출력·한계 분리 |
| CR-010 | 두 제품 화면의 `AI` 라벨 | 실제 AI I/O 없이 기능 오인 | VERIFY/BLOCK | 증거 없으면 라벨 제거 |
| CR-011 | `ACTUAL PRODUCT INTERFACE/SCREEN` | 파일 버전·원본·권리 미확인 | MISLEADING/BLOCK | provenance 확인 전 실제 라벨 금지 |
| CR-012 | 현재 Hero의 제품 화면 합성 | 통합 콘솔처럼 오인 가능 | CONCEPT_REFERENCE | 제품별 실제 근거로 분리 |
| CR-013 | 이메일 링크만 있는 도입 문의 | 검증·동의·라우팅·복구 없음 | FUNCTION_GAP | C-profile 문의 흐름 설계 |
| CR-014 | 임의 `K` 브랜드 심볼 | 공식 CI 미확보 | BRAND_BLOCK | 공식 벡터 회수 전 사용 금지 |
| CR-015 | 주소·연락처 직접 하드코딩 | 공개 원천 간 주소 충돌 | DATA_CONFLICT | canonical company data로 관리 |

## 3. 코드/콘텐츠 격리 규칙

- 현행 Sites와 시안 코드는 `DEPRECATED_REFERENCE`이며 W09 Visual 입력이 아니다.
- 제품 화면 PNG는 `RECOVER/VERIFY` 보관하며 재사용 전에 메타데이터와 권리를 확인한다.
- 위험 문구는 Claim ID와 Evidence가 연결되지 않으면 새 Content Snapshot에 복사하지 않는다.
- 새 구현은 기존 CSS 위에 추가하지 않고 승인된 새 기준선에서 작성한다.

## 4. Apply Decision

- Apply now: CR-001~015를 W04/W12 검증 입력으로 사용.
- Do not apply: 기존 화면의 AI/실제 화면/수치/고객/배포 문구 재사용.
- Defer: 파일 물리 삭제와 배포 교체.
- Trigger: 공식 원본·제품 명세·권리·운영 데이터 승인.

