# KNLSOFT Public Source · Legacy URL Inventory v0.2 Candidate

## 1. 수집 원칙

2026-07-12 공개 검색으로 회수한 원천 후보를 기록한다. 검색 노출 또는 기존 사이트 게시 사실은 최신성·정확성·공개권리의 최종 승인을 의미하지 않는다.

## 2. 공식 도메인 후보

| Source ID | 영역 | URL | 회수 내용 | 상태 | 다음 검증 |
|---|---|---|---|---|---|
| PS-001 | 회사 CI | https://www.knlsoft.com/knlsoft/sub-knlsoftCI | CI 설명, 회사 메뉴 구조 | PUBLIC_INDEXED/VERIFY | 로고 원본·가이드·권리 회수 |
| PS-002 | 회사 인사말 | https://www.knlsoft.com/knlsoft/sub-knlsoftIntro | DBMS/APM 방법론, 회사·제품 서술 | PUBLIC_INDEXED/VERIFY | 현재 회사 정의·문구 승인 |
| PS-003 | 회사 연혁 | https://www.knlsoft.com/knlsoft/sub-knlsoftHistory | 인증·연구소·제품 출시 연혁 후보 | PUBLIC_INDEXED/VERIFY | 날짜별 원본 증빙 |
| PS-004 | 오시는 길 | https://www.knlsoft.com/knlsoft/sub-knlsoftCome | 영등포구 영등포로 150 A동 1211호, 연락처 후보 | PUBLIC_INDEXED/CONFLICT | 행정 담당자 최신 확인 |
| PS-005 | 포트폴리오 | https://www.knlsoft.com/knlsoft/sub-knlsoftPortfolio | 고객/포트폴리오 구조 후보 | PUBLIC_INDEXED/APPROVAL | 고객 공개권리와 최신성 |
| PS-006 | aTops 주요기능 | https://www.knlsoft.com/atops/sub-atopsFunction | 사용자 역할과 SQL 기능 후보 | PUBLIC_INDEXED/VERIFY | 현재 버전 명세·화면 연결 |
| PS-007 | aTops 제품군 | https://www.knlsoft.com/atops/sub-atopsIntro | 다양한 버전 존재 후보 | PUBLIC_INDEXED/VERIFY | 현재 판매 버전·명명·범위 |
| PS-008 | aTops EE | https://www.knlsoft.com/atops/sub-atopsIntroEE | SQL 관리 가치·특징 후보 | PUBLIC_INDEXED/VERIFY | 기능/효과 근거 |
| PS-009 | aTops SE | https://www.knlsoft.com/atops/sub-atopsIntroSE | 개발 시점 SQL 관리 후보 | PUBLIC_INDEXED/VERIFY | 현재 버전·기능 |
| PS-010 | aTops History | https://www.knlsoft.com/atops/sub-atopsHistory | 제품 탄생 배경과 장애 통계 | PUBLIC_INDEXED/HIGH_RISK | 통계 원출처 없으면 폐기 |
| PS-011 | aTops Review | https://www.knlsoft.com/atops/sub-atopsReview | 고객 후기 후보 | PUBLIC_INDEXED/APPROVAL | 고객·문구·기간 서면 승인 |
| PS-012 | aTops Board | https://www.knlsoft.com/atops/board/sub-atopsBoard-all | 게시/자료 콘텐츠 후보 | PUBLIC_INDEXED/INVENTORY | 전체 URL·첨부·버전 export |
| PS-013 | aTops 전용 도메인 | https://www.atops.co.kr/ | PE 등 별도 마케팅 정보 후보 | PUBLIC_INDEXED/VERIFY | 공식 운영 주체·최신성·통합 정책 |
| PS-014 | SPACEMON Solution | https://www.knlsoft.com/spacemon/sub-spacemonSolution | 이기종 DBMS 통합 관제·SQL 성능 후보 | PUBLIC_INDEXED/VERIFY | 버전/DBMS별 실제 범위 |
| PS-015 | SPACEMON Product | https://www.knlsoft.com/spacemon/sub-spacemonProductIntro | Oracle 등 제품별 설명 후보 | PUBLIC_INDEXED/VERIFY | ProductIntro-2~6 전체 매핑 |
| PS-016 | SPACEMON Guide | https://www.knlsoft.com/spacemon/sub-spacemonGuide | Oracle/DB2 가이드 후보 | PUBLIC_INDEXED/VERIFY | 최신 파일·버전·공개범위 |
| PS-017 | SPACEMON Resource | https://www.knlsoft.com/spacemon/board/sub-spacemonRefer | 자료실과 연락처 후보 | PUBLIC_INDEXED/INVENTORY | 첨부·중복·구버전 export |
| PS-018 | SPACEMON Case | https://www.knlsoft.com/spacemon/sub-spacemonReview | 구축사례 표현 후보 | PUBLIC_INDEXED/APPROVAL | 고객·성과·표현 승인 |
| PS-019 | SPACEMON Inquiry | https://www.knlsoft.com/spacemon/board/sub-spacemonBoard | 기존 문의 게시판 | PUBLIC_INDEXED/PII_RISK | 공개범위·보관·마이그레이션 정책 |

## 3. 외부 검증 후보

| Source ID | URL | 후보 Evidence | 상태 | 사용 경계 |
|---|---|---|---|---|
| PS-020 | https://chat.kosw.or.kr/egovdata/cop/bbs/selectBoardArticle.do?bbsId=BBSMSTR_000000000141&nttId=5998 | SPACEMON 5 조달 식별번호·제품 분류·계약 정보 | THIRD_PARTY_CURRENT_CANDIDATE | 공식 조달 원문과 계약 상태 재확인 전 공개 금지 |
| PS-021 | https://www.sharedit.co.kr/partners/863 | 회사·SPACEMON 파트너 소개 | THIRD_PARTY/VERIFY | 회사 사실의 보조 자료만 |

## 4. 발견된 충돌·위험

- 주소가 가산동과 영등포구 당산으로 혼재한다. Footer/문의에 넣기 전 최신 공식 확인이 필요하다.
- 기존 페이지마다 Footer 정보가 다른 검색 결과가 있어 canonical company/contact data가 필요하다.
- aTops History의 장애 원인 비율은 원출처·조건이 없으면 사용하지 않는다.
- 제품별 소개가 번호형 URL로 분산되어 중복·구버전·지원 DBMS 오인을 만들 수 있다.
- 문의게시판의 기존 공개·개인정보 구조를 그대로 이전하지 않는다.

## 5. 로컬 회수 자산 후보

`knlsoft-ai-products/public/assets`에서 SPACEMON/aTops 추정 PNG 15개가 발견되었다. 해상도는 165×120~2360×1040이다.

- aTops 후보: `img-function1-*`, `img-function3-*`, `img-function4-1.png`.
- SPACEMON 후보: `img_spacemon_oracle_*`, `img-spacemon-featureImg-1.png`.
- 기타: `img-main-bank.png`는 고객/프로젝트 자산 가능성이 있어 즉시 격리.

이 파일들은 이름과 화면 모양만으로 공식성·버전·권리를 확정하지 않는다. Source owner, capture date, product version, masking, original URL, publication permission이 모두 필요하다.

## 6. Migration Inventory Status

- Public URL seed list: PARTIAL DONE.
- 전체 크롤/게시물/첨부/리디렉션 목록: NOT EXECUTED.
- 최신성·중복·개인정보·권리 판정: NOT EXECUTED.
- Canonical content mapping: NOT EXECUTED.

## 7. Apply Decision

- Apply now: PS-001~021을 Evidence 회수 Seed로 사용.
- Do not apply: 공개 페이지 내용을 최신 사실·공개 승인으로 자동 승격.
- Defer: URL redirect, content migration, asset reuse.
- Trigger: 원본 export, 소유자 인터뷰, 공식 문서/권리 확인.

