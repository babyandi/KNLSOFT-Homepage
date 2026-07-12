# KNLSOFT WebSite RCA · Decision Ledger v0.2 Candidate

## 1. Root Cause Analysis

| RCA ID | 실패/누락 | 근본 원인 | 영향 | 재발 방지 | Regression Gate |
|---|---|---|---|---|---|
| RCA-001 | 설계 전 Hero·화면 제작 | 디자인을 상위 설계가 아닌 시작점으로 취급 | 메시지·증거·기능 불일치 | W00~W08/CEG 선행 강제 | CEG-WF/VD |
| RCA-002 | `globals.css` 누적 덮어쓰기 | 승인된 구조·토큰 없이 증상별 CSS 패치 | 우선순위 충돌, 반응형 drift, 유지보수 불가 | 승인 설계 후 새 stylesheet 기준선; override 금지 | Source diff + visual regression |
| RCA-003 | 하단 레이아웃 반복 수정 | 섹션 책임과 콘텐츠 길이 미정 | 동일 레이아웃 반복·과대 글자·균형 붕괴 | Page/Section Responsibility와 content snapshot 고정 | Squint/5초/Layout QA |
| RCA-004 | AI 강조가 기능 증거보다 앞섬 | 마케팅 우선, 실제 I/O·한계·사람 판단 미연결 | 자율/통합 기능 오인 | AI Capability schema와 Evidence Gate | Claim test + false-inference test |
| RCA-005 | 개념 UI가 실제처럼 보임 | 자산 부족을 가공 화면으로 대체 | 제품 신뢰와 정확성 훼손 | Real/Processed/Concept 라벨과 source metadata | Asset provenance test |
| RCA-006 | 디자인 점수·완료도 조기 확정 | Gate와 증적 없이 주관 점수 사용 | 잘못된 완료 인식 | 단계별 PASS 조건과 NOT EXECUTED 유지 | Gate ledger read-back |
| RCA-007 | 사용자에게 반복 승인 질문 | 실행 순서·중지 조건이 문서화되지 않음 | 결정 피로, 진척 지연 | 자동 진행 범위와 true decision point 정의 | Decision matrix audit |
| RCA-008 | 외부 UI 원칙이 CSS 팁으로 축소 | 목적·과업·정보 구조와 분리 적용 | 표면적 보정 반복 | UX 원칙을 Section Contract/Test Oracle에 연결 | UX contract coverage |

## 2. 재발 방지 규칙

1. 새 화면 요청이 들어와도 먼저 해당 Page 책임, Claim, Scenario, State, Evidence를 읽는다.
2. Gate가 없는 PASS, 완료율, 최종 기준선 주장을 금지한다.
3. 현재 공개 버전은 별도 `DEPRECATED_REFERENCE`로 유지하며 신규 설계 입력과 혼합하지 않는다.
4. 디자인 변경은 CSS patch가 아니라 승인된 Wireframe/Visual Spec 변경으로 시작한다.
5. 실패는 dependent lane만 막고 Evidence 회수·콘텐츠 모델·정책 작업은 계속한다.

## 3. Decision Ledger

| ID | Decision | Apply now | Do not apply | Defer | Trigger |
|---|---|---|---|---|---|
| D-001 | 웹사이트=디지털 서비스 | W00~W14 기준 | 단순 홈페이지 관점 | - | 변경 시 사업 승인 |
| D-002 | 현재 공개 화면 | 참고 후보로만 보존 | 최종 기준선·승인 시안 취급 | 회수/대체 | 새 구현 검증 완료 |
| D-003 | 기존 CSS/하단 | 폐기 대상으로 등록 | 추가 override | 물리 삭제 | 새 구현 브랜치 시작 |
| D-004 | 제품 경계 | aTops 운영 전 / SPACEMON 운영 중 | 통합 제품 암시 | 상세 모듈·연계 | 최신 명세·E2E 증거 |
| D-005 | AI | 증거 기반 분석 지원, 사람 판단 | 자율 승인·해결·100% | 실제 세부 기능 | I/O·테스트·보안 증거 |
| D-006 | Wireframe | 조건 해결 작업 | 지금 시작 | 실제 작성 | CEG-WF PASS |
| D-007 | Visual/Code | 중단 유지 | 기존 화면 수정 | W09~W11 | CEG-VD/IM PASS |
| D-008 | Git/Release | Draft PR 문서 기준선 갱신 | main merge·Production GO | 배포 | 사용자 승인+W12/W13 |

## 4. 다음 자동 진행 순서

1. AE-001~020과 C-001~017 소유자·원천 연결.
2. Home/aTops/SPACEMON/AI 허용 Claim 세트 확정.
3. 회사·연락·문의 운영 사실 확인.
4. 구 사이트 URL·자료·지원 인벤토리 작성.
5. CEG-WF 재판정.
6. PASS 후 대표 Wireframe: Home → aTops → SPACEMON → AI → Inquiry.

