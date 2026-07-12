# KNLSOFT WebSite Baseline Documents

## Active baseline

The active working baseline is now `ORUDA-Native Execution Baseline v1.0 Candidate`. The previous v0.2 digital-service documents are retained as `ORUDA_INTAKE_INPUT_CANDIDATE` and must be reprocessed by the ORUDA program chain before they can become approved outputs.

| No. | ORUDA control document | Purpose | State |
|---:|---|---|---|
| 27 | ORUDA-Native Execution Baseline | project identity, baseline, entry program, boundary | ACTIVE CONTROL CANDIDATE |
| 28 | Program · Artifact · Handoff Map | end-to-end ownership and output transfer | ACTIVE CONTROL CANDIDATE |
| 29 | Gate · State Ledger | fail-closed stage status and triggers | ACTIVE |
| 30 | Delegation Spine · OBuilder Team Routing | OProjectManager/OProjectLeader delegation and development teams | ACTIVE CONTROL CANDIDATE |

Machine-readable control:

- `oruda/project/KNLSOFT_WEBSITE_PROJECT.v1.0.0.json`
- `oruda/project/KNLSOFT_WEBSITE_ARTIFACT_MAP.v1.0.0.json`
- `oruda/project/KNLSOFT_WEBSITE_GATE_LEDGER.v1.0.0.json`
- `scripts/validate_knlsoft_oruda_project.py`
- `scripts/test_knlsoft_oruda_project_mutations.py`

Current true hard gate: `OBP-ENTRY`. `OBusinessPlanning`, `OBusinessAdmin`, `ORFP`, `OAcceptance`, `OProjectManager`, `OProjectLeader`, and the required `OVisual` binding were not found in the current ORUDA main program methodology matrix. The required delegation spine is `OBusinessPlanning → OBusinessAdmin → Formal GO/HOLD → OProjectManager → OProjectLeader → OBuilder internal teams`. No downstream design/build gate may pass until these dependencies are registered and validated.

## ORUDA intake inputs

| No. | Document | Purpose | State |
|---:|---|---|---|
| 13 | WebSite Strategy & Evidence Blueprint | W00–W14 control and service outcomes | ACTIVE CANDIDATE |
| 14 | User · Role · Buying Journey | roles, contexts, buying decisions | PASS CANDIDATE |
| 15 | aTops · SPACEMON · AI Boundary | product and AI truth boundaries | PASS CANDIDATE / facts partial |
| 16 | Claim–Data–Evidence Matrix | public truth, sources, owners, proof | PARTIAL/BLOCKED |
| 17 | Scenario Catalog | normal, exception, recovery | PASS CANDIDATE |
| 18 | Functional Architecture | capabilities and scope boundaries | PASS CANDIDATE |
| 19 | IA · Navigation · Task · State | findability, flows, states | PASS CANDIDATE |
| 20 | Page · Section Responsibility | page decisions and section contracts | PASS CANDIDATE |
| 21 | Policy · Permission · Security | RBAC, privacy, security | PASS CANDIDATE |
| 22 | UX · Interaction Specification | behavior, reflow, accessibility | PASS CANDIDATE |
| 23 | Content & Evidence Gate | wireframe/design/build/publication entry | ACTIVE |
| 24 | RCA · Decision Ledger | failure prevention and next sequence | ACTIVE |
| 25 | Public Source · Legacy URL Inventory | evidence recovery seed and migration risks | PARTIAL |
| 26 | Existing Content Risk Register | quarantine unverified current-site claims | ACTIVE |

## Superseded design-first baseline

Documents 01–12 remain as `v0.1 REFERENCE_BASELINE`. They preserve useful strategy, asset, benchmark, Hero, content-model, and validation material but do not authorize Visual Design or implementation.

The published Sites version 8, its Hero/Visual Assets, accumulated `globals.css`, and lower-page layout are `DEPRECATED_REFERENCE`. Do not continue with CSS overrides.

## Current gate summary

- CEG-0 Intake Integrity: PARTIAL.
- CEG-1 Strategy Integrity: PASS CANDIDATE.
- CEG-2 Claim Integrity: PARTIAL.
- CEG-3 Service Integrity: PASS CANDIDATE.
- CEG-WF Wireframe Entry: NOT GRANTED.
- CEG-VD/IM/PB: BLOCKED.

## Decision

- Apply now: v0.2 documents, evidence recovery, claim confirmation, operational fact confirmation.
- Do not apply now: wireframes, Visual Design, CSS edits, implementation, production deployment, main merge.
- Defer: W09–W14.
- Trigger: the unresolved checklist in `23_CONTENT_EVIDENCE_GATE.md`.
