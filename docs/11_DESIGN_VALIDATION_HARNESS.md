# KNLSOFT Design Validation Harness v0.1

## Gate sequence
G0 Strategy → G1 Claims → G2 Assets/Rights → G3 Art Direction → G4 Hero → G5 Product Sections → G6 Design System → G7 Responsive → G8 Content/SEO → G9 Accessibility/Performance → G10 Release Readiness.

A later gate cannot compensate for a failed earlier gate.

## G0 Strategy
Pass when audience, purpose, positioning, product roles, and conversion goals are explicit.

## G1 Claims
Pass when all public claims are CONFIRMED or explicitly labeled OPTION/ROADMAP. PROHIBITED claims must be absent.

## G2 Assets and rights
Pass when logo, BI, photography, UI, customer evidence, and licenses have owners, versions, rights, and source files.

## G3 Art direction
Pass when the visual system is distinctive, enterprise credible, consistent, implementable, and free of template/slide aesthetics.

## G4 Hero
Test with executive, DBA, security, and procurement roles:
- five-second comprehension
- correct product-role recall
- trust perception
- AI interpretation
- CTA clarity
- no false-feature inference

## G5 Product sections
Pass when each product has a distinct visual scene, problem/value narrative, verified evidence, and technical depth path.

## G6 Design system
Pass when tokens, components, imagery, UI treatment, and motion remain consistent across pages.

## G7 Responsive
Validate 1440, 1280, 1024, 768, 390, and 360 widths. Check line breaks, image crops, navigation, tables, forms, touch areas, and product evidence legibility.

## G8 Content and SEO
Validate titles, descriptions, headings, canonical URLs, redirects, structured data, Korean search intent, document versions, and no duplicate product definitions.

## G9 Accessibility and performance
- WCAG AA contrast
- keyboard and visible focus
- semantic headings and landmarks
- alt text and labels
- reduced motion
- no information by color alone
- responsive optimized images
- agreed Core Web Vitals target
- no blocking Hero video

## G10 Release readiness
Require legal/privacy review, form routing test, analytics consent, security review, backup/rollback, content owner sign-off, redirect test, and production evidence.

## Anti-false-pass rules
- Design review screenshots do not prove responsive behavior.
- A build does not prove visual quality.
- A polished concept does not prove claim truth.
- Placeholder logos/screens are not publication-ready.
- Lighthouse alone does not prove accessibility.
- Internal approval does not replace customer-logo permission.

## Failure routing
Record failure ID, gate, observable evidence, root cause, owner, correction, regression test, and resume trigger. Block only the dependent lane; continue independent work.

## Current result
G0 PASS candidate; G1 PARTIAL; G2 BLOCKED; G3 PASS candidate at brief level only; G4–G10 NOT EXECUTED.
