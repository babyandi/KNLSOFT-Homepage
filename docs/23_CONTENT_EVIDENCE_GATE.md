# KNLSOFT Content & Evidence Gate v0.2 Candidate

## 1. Gate 목적

설계가 없는 상태를 디자인으로 감추거나, 미확인 주장을 그럴듯한 화면으로 사실화하는 것을 막는다. Wireframe, Visual Design, Implementation, Publication은 서로 다른 Gate를 갖는다.

## 2. Gate 단계

| Gate | Entry | PASS 조건 | 현재 |
|---|---|---|---|
| CEG-0 Intake Integrity | W00 | 원천·가정·폐기·미확보 목록과 소유자 | PARTIAL |
| CEG-1 Strategy Integrity | W01~W03 | 목적·사용자·구매흐름·제품 경계·시나리오 | PASS CANDIDATE |
| CEG-2 Claim Integrity | W04 | 공개 후보 Claim마다 상태·근거·소유자·제약 | PARTIAL |
| CEG-3 Service Integrity | W05~W08 | 기능·IA·상태·정책·UX·페이지 책임 연결 | PASS CANDIDATE |
| CEG-WF Wireframe Entry | CEG-1~3 | 아래 Wireframe 체크 전부 충족 | NOT GRANTED |
| CEG-VD Visual Design Entry | Wireframe 승인 | 공식 Brand/Product/Content/Evidence subset | BLOCKED |
| CEG-IM Implementation Entry | Visual 승인 | 대표 화면·상태·콘텐츠 snapshot·기술 계약 | BLOCKED |
| CEG-PB Publication Entry | W12/W13 | 사실·권리·보안·접근성·성능·복구 증적 | BLOCKED |

## 3. CEG-WF PASS Checklist

- [x] 사이트 목적과 사용자 Outcome.
- [x] 사용자 역할과 구매 의사결정 흐름.
- [x] aTops/SPACEMON/AI 공개 경계.
- [x] 정상·예외·복구 시나리오.
- [x] 기능 아키텍처와 범위 경계.
- [x] IA·Task·State 흐름.
- [x] 페이지·섹션 책임.
- [x] 정책·권한·보안·UX 계약.
- [ ] Home/aTops/SPACEMON/AI 페이지의 허용 Claim ID 확정.
- [ ] 회사·연락·문의 수신 운영 주체 확인.
- [ ] 필수 콘텐츠 블록별 실제 원천 또는 명시적 placeholder 상태.
- [ ] 구 URL·자료·지원 콘텐츠 인벤토리.
- [ ] Product Owner/Management의 Candidate 검토 기록.

따라서 문서 설계는 진행 가능하지만 Wireframe 진입은 아직 `NOT GRANTED`이다.

## 4. CEG-VD 최소 조건

- 공식 KNLSOFT/aTops/SPACEMON 벡터 로고와 사용 규칙.
- 최신 제품 정의와 주요 기능 범위.
- 공개 가능한 실제 화면 각 제품 최소 2개와 메타데이터.
- AI를 강조할 경우 해당 제품 실제 AI I/O 최소 1개. 없으면 AI는 원칙·계획 수준으로 축소.
- 연락처, 개인정보 처리, 문의 운영 흐름.
- Hero와 제품 페이지의 승인된 Wireframe/Content Snapshot.
- 자산 권리 Manifest와 개념 화면 라벨 규칙.

## 5. Evidence Coverage Rule

페이지별 주요 Claim은 다음 중 하나여야 한다.

1. `OFFICIAL/VERIFIED` + Active Evidence.
2. `OPTION` + 조건과 Evidence.
3. `VALIDATED_CONCEPT` + 명확한 개념 라벨.
4. 미충족 시 비공개 또는 페이지에서 제거.

한 페이지의 디자인 완성도가 높아도 1~4를 위반하면 Gate는 PASS가 아니다.

## 6. Gate 판정 형식

- Result: PASS / PASS WITH CONDITIONS / REWORK / BLOCK.
- Scope: 전체 사이트가 아니라 페이지·Claim·Capability 단위.
- Evidence: 문서/파일/테스트 ID.
- Open gaps: owner, due/trigger, dependent lane.
- Apply now / Do not apply / Defer / Trigger.

## 7. 현재 판정

- Apply now: W00~W08 문서 기준선과 Evidence 회수 작업.
- Do not apply: Wireframe, Visual Design, CSS/화면 구현, 기존 공개 화면의 최종 승인.
- Defer: W09~W14.
- Trigger: CEG-WF 미충족 5개 항목 해결 후 Wireframe 시작.

