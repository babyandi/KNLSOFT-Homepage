# KNLSOFT Design Token Specification v0.1

This specification defines roles, not final brand values. Final values require official CI/BI assets.

## Color roles
- color.brand.primary: corporate authority
- color.brand.action: primary interaction
- color.brand.surface: light editorial canvas
- color.brand.dark: high-contrast technology section
- color.atops.primary: pre-operation quality
- color.spacemon.primary: live-operation performance
- color.ai.insight: limited analytical highlight
- color.status.success/warning/danger/info
- color.text.primary/secondary/inverse
- color.border.subtle/strong

## Typography roles
- display.hero
- display.section
- heading.product
- heading.component
- body.lead
- body.default
- body.technical
- label.meta
- data.metric
- code.sql

Final Korean and Latin fonts require license, performance, and rendering review.

## Spacing
Base unit: 4px.
Semantic scale: 4, 8, 12, 16, 24, 32, 48, 64, 80, 120, 160.
Page sections must use semantic tokens rather than arbitrary values.

## Grid
- Desktop: 12 columns, 1240–1320px content
- Tablet: 8 columns
- Mobile: 4 columns
- Minimum mobile side padding: 20px
- Breakpoints set by content failure, not device marketing labels

## Shape
- Enterprise surfaces use restrained radius
- Do not apply one radius to all components
- Product evidence frames remain rectangular and precise
- Pills reserved for status/filter/tag semantics

## Elevation
Use no more than three levels. Prefer borders, contrast, and spacing over heavy shadows or glassmorphism.

## Motion
- fast: 120–180ms
- standard: 180–320ms
- narrative: 600–900ms
- easing must be consistent
- reduced-motion tokens mandatory

## Component families
Header, mega menu, buttons, text links, product role label, evidence strip, case story, feature narrative, supported-technology list, document card, tabs, accordions, form controls, alerts, tables, modal, footer.

## Prohibited
Uncontrolled gradients, neon glow, generic glass cards, arbitrary shadows, repeated floating cards, inaccessible contrast, decorative status colors, and embedding text into raster images.
