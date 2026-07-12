# KNLSOFT Asset Evidence Gap Register v0.1

## Purpose
Separate verified assets, recoverable assets, missing assets, publication approvals, and true design blockers.

## Status
- READY: verified and usable
- RECOVER: exists but original or metadata must be recovered
- VERIFY: accuracy/current-version check required
- APPROVAL: publication permission required
- CREATE: must be newly produced
- BLOCKER: prevents final design approval
- HOLD: not required for the current milestone

## Register
| ID | Asset/evidence | Status | Owner | Required for | Resume trigger |
|---|---|---|---|---|---|
| AE-001 | Official KNLSOFT vector logo | RECOVER/BLOCKER | Management | Brand-final Hero | AI/SVG original received |
| AE-002 | Official CI color/spacing guide | RECOVER | Management | Design-system lock | Official guide received |
| AE-003 | aTops vector BI | RECOVER/BLOCKER | Product owner | Product visual lock | Vector and usage rule received |
| AE-004 | SPACEMON vector BI | RECOVER/BLOCKER | Product owner | Product visual lock | Vector and usage rule received |
| AE-005 | Current aTops feature specification | VERIFY/BLOCKER | R&D | Claim lock | Current version approved |
| AE-006 | Current SPACEMON feature specification | VERIFY/BLOCKER | R&D | Claim lock | Current version approved |
| AE-007 | aTops high-resolution UI set | CREATE | Product/R&D | Product section | Sanitized captures delivered |
| AE-008 | SPACEMON high-resolution UI set | CREATE | Product/R&D | Product section | Sanitized captures delivered |
| AE-009 | aTops production AI example | VERIFY/BLOCKER | AI owner | AI claim and visual | Working input/output evidence |
| AE-010 | SPACEMON production AI example | VERIFY/BLOCKER | AI owner | AI claim and visual | Working input/output evidence |
| AE-011 | Supported DBMS/version matrix | VERIFY | Support/R&D | Technical confidence | Matrix signed off |
| AE-012 | On-Premise/closed-network architecture | CREATE/VERIFY | Architecture/Security | Security section | Approved architecture |
| AE-013 | Customer logo list | APPROVAL | Sales | Trust strip | Written publication approval |
| AE-014 | Customer case narratives | CREATE/APPROVAL | Sales | Case section | Problem/action/outcome approved |
| AE-015 | Measured outcomes | VERIFY | Customer/Sales | Quantitative proof | Method and result approved |
| AE-016 | Certifications/patents | RECOVER/VERIFY | Management | Corporate trust | Valid documents confirmed |
| AE-017 | Support and maintenance model | CREATE/VERIFY | Support | Support section | Scope/SLA approved |
| AE-018 | Corporate/engineering photography | CREATE | Management/Design | Hero and company pages | Shoot or license completed |
| AE-019 | Current address/contact details | VERIFY | Administration | Footer/contact | Official confirmation |
| AE-020 | Asset rights and license records | CREATE/BLOCKER | Legal/Design | Publication | Rights manifest complete |

## Design-entry gate
Internal composition may start with clearly marked placeholders when AE-001–006 are assigned and recoverable. Final Hero approval is blocked until AE-001–006, AE-018, and AE-020 are resolved. AI visuals remain blocked until AE-009 or AE-010 is verified.

## Non-blocking work
Information architecture, content templates, responsive grid, accessibility rules, asset-capture instructions, and visual-reference analysis may continue.
