# KNLSOFT Homepage — ORUDA OBuilder Role Taxonomy Inheritance v1.0 Candidate

## 원칙

S/W/H/W 아키텍처 설계자, 기획자, 디자이너, 개발자, DBA, DA 및 기타 OBuilder 직군의 공통 정의는 이 저장소에 만들지 않는다.

- Source of Truth: `babyandi/ORUDA`
- Taxonomy: `ORUDA_OBUILDER_ROLE_TAXONOMY_V1_0_0`
- Pinned candidate commit: `f72b0290c81a6bbe52cd4aed6ee2c438f1ecad86`
- Upstream Draft PR: https://github.com/babyandi/ORUDA/pull/22
- Inheritance: `PINNED_REFERENCE`
- Local override: false

KNLSOFT 홈페이지는 공통 Taxonomy를 상속하고 프로젝트에 필요한 Role ID만 선택한다. 실제 프로젝트 역할 인스턴스는 OManager 승인 이후 OProjectManager/OProjectLeader가 Build Request와 함께 생성한다.

## 선택 범위

현재 후보는 기획·분석, 솔루션/SW/보안/연계 아키텍처, UX/UI/Visual/Design System, Frontend/Backend/API/CMS, DA/Data Model/DBA/Data Engineering/Metadata/Data Quality, Integration/Automation, DevOps/SRE, Developer Quality/Performance/AppSec/Configuration/Release/A11y/Documentation이다.

AI 직군은 실제 AI Runtime 기능이 검증될 때까지, H/W/물리 인프라 직군은 해당 범위가 승인될 때까지 상속만 하고 활성화하지 않는다.

## 경계

- Role selection ≠ role instance.
- Role instance ≠ work assignment.
- OBuilder 직군은 OProjectLeader Build Request만 수신한다.
- 공통 역할 변경은 ORUDA Role Governance Change Request로만 요청한다.
- OTester/OView/OAudit/OAsset 독립성은 유지한다.

## Decision

- Apply now: pinned reference와 KNLSOFT activation-profile 후보.
- Do not apply: 공통 직군 정의의 로컬 복사·수정.
- Defer: 실제 인력/Agent 배정과 OBuilder 실행.
- Trigger: ORUDA upstream merge, OManager GO, OProjectLeader Build Request.
