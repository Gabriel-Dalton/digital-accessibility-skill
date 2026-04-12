# Digital Accessibility Skill for Claude

A Claude skill for auditing, generating, and documenting accessible digital experiences using real standards such as WCAG 2.2, ADA, Section 508, AODA, ACA, and EAA / EN 301 549.

## What this skill does

This skill helps Claude:

- audit existing HTML, React, Vue, and other web UI for accessibility issues
- generate accessible components from scratch
- explain accessibility requirements in plain language
- map issues to WCAG 2.2 success criteria
- support documentation such as accessibility statements, VPAT-style outputs, AODA reports, and ACA accessibility plans

It is designed to be practical, standards-based, and useful for both audits and implementation work.

## Included files

```text
.
├── SKILL.md
├── digital-accessibility.skill
└── references/
    ├── accessibility-statement-template.md
    ├── component-patterns.md
    ├── legal-frameworks.md
    ├── testing-guide.md
    └── wcag-checklist.md
```

## Reference library

- **wcag-checklist.md**: WCAG 2.2 AA checklist with implementation guidance
- **component-patterns.md**: accessible UI patterns with keyboard and ARIA guidance
- **legal-frameworks.md**: accessibility laws and frameworks across multiple jurisdictions
- **accessibility-statement-template.md**: reusable accessibility statement template
- **testing-guide.md**: testing workflow and screen reader validation guidance

## Best use cases

Use this skill when you want Claude to:

- review a page, component, or design for accessibility issues
- fix keyboard, focus, labeling, contrast, structure, or ARIA issues
- build accessible forms, modals, tabs, accordions, navigation, tables, and dialogs
- write accessibility documentation for a business, nonprofit, or public-facing organization
- explain which laws or standards apply to a site or product

## Example prompts

- Audit this React component for WCAG 2.2 AA issues
- Fix the focus order and keyboard navigation in this modal
- Build an accessible tab component with proper ARIA and keyboard support
- Write an accessibility statement for our Canadian nonprofit
- What accessibility requirements apply to a US public-facing ecommerce site?

## Standards covered

- **WCAG 2.2**
- **ADA**
- **Section 508**
- **AODA / IASR**
- **ACA**
- **EAA / EN 301 549**

## Why this repo exists

Many accessibility prompts stay too generic. This skill gives Claude a stronger, more structured base so responses are tied to actual standards, clear remediation advice, and reusable documentation patterns.

## Installation

Add the skill to Claude using the included `digital-accessibility.skill` file and keep the reference files available alongside it.

## Suggested topics

Accessibility, a11y, WCAG, ARIA, screen readers, keyboard navigation, focus management, alt text, accessible forms, accessibility statements, VPATs, AODA, ADA compliance.

## License

MIT
