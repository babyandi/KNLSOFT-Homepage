# KNLSOFT UX · Interaction Specification v0.2 Candidate

## 1. 상호작용 원칙

1. 상호작용은 정보 이해, 비교, 탐색, 제출, 복구 중 하나를 돕는다.
2. Hover만으로 의미나 기능을 제공하지 않는다.
3. 애니메이션은 상태 변화·인과·초점만 설명하며 `prefers-reduced-motion`을 존중한다.
4. 로딩·빈 상태·오류·만료·권한 상태를 정상 화면과 함께 설계한다.
5. 사용자가 제출·다운로드·외부 이동 전에 결과를 예측할 수 있어야 한다.

## 2. Global Navigation Contract

- Desktop: 로고, 6개 이하 주 메뉴군, 핵심 CTA 1개. 현재 위치와 키보드 초점 표시.
- Mobile: 메뉴 열기 버튼에 상태와 접근 가능한 이름 제공. 열림 시 초점 이동·가두기·Esc 닫기·복귀.
- Mega menu가 필요하면 콘텐츠 규모와 사용자 테스트로 정당화하며 장식용으로 사용하지 않는다.
- 스크롤에 따른 헤더 변화가 콘텐츠를 가리거나 초점을 잃게 하지 않는다.

## 3. Product Comparison Contract

- 비교축: 적용 시점, 사용자, 문제, 입력, 출력, AI, 환경, 다음 검토.
- 모바일에서 표 전체를 축소하지 않고 항목별 두 제품 비교 순서를 유지한다.
- 선택 상태는 필터일 뿐 자동 추천·적합성 보증이 아니다.

## 4. Evidence/UI Contract

- 실제 화면: 제품·버전·캡처일·마스킹 상태.
- 가공 화면: 원본 기능·값을 바꾸지 않고 crop/annotation만 별도 레이어로 사용.
- 개념 화면: `개념 시각화 — 실제 제품 UI 아님`을 인접 표시.
- 확대가 필요한 화면은 대체 설명, 키보드 닫기, 초점 복귀를 제공한다.
- 증거가 만료되면 조용히 숨기지 않고 대체 또는 확인 경로를 제공한다.

## 5. Form Contract

### Before submit

- 목적/제품을 먼저 선택하고 조건부 필드는 필요한 경우만 표시한다.
- 라벨을 placeholder로 대체하지 않는다.
- 필수/선택, 형식, 개인정보 처리, 제출 후 절차를 사전 안내한다.

### Validation

- 필드 인접 오류 + 상단 오류 요약 + 오류 필드로 이동 가능한 링크.
- 사용자가 입력한 정상 값은 보존한다.
- 색상만으로 오류를 표시하지 않는다.

### Submission

- 중복 클릭 방지와 진행 상태 표시.
- 성공: 접수 여부, 접수 식별자, 다음 단계, 대체 연락 경로.
- 실패: 재시도 가능 여부, 입력 보존, 오류 식별자, 대체 경로.
- `담당자가 확인 후 연락`을 사용하며 즉시 예약/응답을 보장하지 않는다.

## 6. Responsive/Reflow Contract

| View | Grid | Interaction |
|---|---|---|
| ≥1280 | 12 columns | 비교·증거 병렬, 강한 초점 2개 이하 |
| 768–1279 | 8 columns | 핵심 순서 유지, 복잡 비교 단계화 |
| 320–767 | 4 columns | 단일 읽기 흐름, 터치 44px 후보, 표 재구성 |
| 400% zoom | single logical flow | 가로 스크롤 없이 읽기·폼·CTA 수행 |

한글은 의미 단위로 줄바꿈하고 제목·본문의 최대 글자폭을 설정한다. 이미지 크롭이 증거의 핵심 값을 제거하면 다른 구성을 사용한다.

## 7. UX Validation

- 5초 테스트: 회사 전문성, 두 제품 역할, AI 역할, CTA.
- Squint Test: 시각적 초점이 페이지 책임과 일치하는지 확인.
- Keyboard/Screen reader: 메뉴, 비교, 증거 확대, 폼, 오류, 성공.
- Reflow: 320px 및 400% 확대.
- Scenario: SCN-01~17 정상·예외·복구.
- 시안 충실도: 승인 와이어프레임/Visual Spec과 DOM·좌표·상태 비교.

## 8. Apply Decision

- Apply now: Navigation, comparison, evidence, form, reflow 계약.
- Do not apply: 현재 시안에 CSS로 부분 이식.
- Defer: 모션 값, 컴포넌트 토큰, 실제 breakpoint 미세값.
- Trigger: 대표 와이어프레임 승인과 W09 Visual System.

