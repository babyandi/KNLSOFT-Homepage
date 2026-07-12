# KNLSOFT Website Content Model v0.1

## Core content entities

### Product
Fields: name, one-line definition, audience, problem, value, verified features, optional features, roadmap, supported DBMS, deployment models, security, integrations, screenshots, cases, documents, support, claim status, version, owner, review date.

### Feature
Fields: product, feature name, user problem, input, process, output, benefit, evidence, screenshot, supported environment, limitations, claim status, owner.

### AI capability
Fields: product, capability, input data, deterministic component, AI component, output, evidence/explanation, human decision, deployment model, data handling, limitations, maturity, verification evidence, publication status.

### Case study
Fields: industry, approved customer name/logo, initial problem, environment, applied product/features, implementation scope, outcome, measurement method, quote, approval record, publication expiration.

### Supported technology
Fields: DBMS/technology, product, version range, operating system, supported functions, limitations, validation date, owner.

### Document
Fields: title, product, type, version, language, audience, file, checksum, publication state, effective date, superseded-by, owner.

### Support article
Fields: product, version, category, symptom/question, resolution, attachments, related articles, review date, visibility.

### Trust credential
Fields: type, title, issuer, registration number, effective/expiry date, public asset, evidence file, approval.

## Page content contract
Every marketing claim must link to a claim status and evidence owner. Every screenshot must include product version, capture date, masking state, and rights status. Every number must include measurement method and approval.

## Content lifecycle
Draft → Technical review → Claim review → Legal/publication review → Approved → Published → Superseded/Expired.

## Freshness
- Product and AI: review each release
- DBMS support: quarterly or release-driven
- Cases and credentials: semiannual
- Guides/release notes: release-driven
- Contact/company data: quarterly
