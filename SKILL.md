---
name: digital-accessibility
description: |
  Audit and generate accessible digital content that meets WCAG 2.2, ADA, AODA,
  ACA (European Accessibility Act), and Section 508 standards. Use this skill
  whenever the user mentions accessibility, a11y, WCAG, ARIA, screen readers,
  ADA compliance, AODA, VPAT, accessible design, alt text, color contrast,
  keyboard navigation, focus management, or any request to make code, content,
  or documents more inclusive. Also trigger when the user asks to review or
  create HTML, React, Vue, or any web UI — accessibility should be checked even
  if not explicitly requested. If someone asks to build a form, a nav bar, a
  modal, a table, or any interactive component, this skill applies. When the
  user asks about compliance documentation, VPATs, or accessibility statements,
  use this skill too.
---

# Digital Accessibility Skill

You help users audit existing code/content for accessibility compliance AND generate new accessible code from scratch. Every recommendation you make should be grounded in real standards — not vague "best practices."

## Quick-Start Decision Tree

1. **User wants to audit existing code/content** → Jump to the Audit Workflow
2. **User wants to generate new accessible code** → Jump to the Generation Workflow
3. **User wants compliance documentation** → Jump to the Documentation section
4. **User wants to understand a standard** → Check references/ for the relevant framework

## Core Standards (Know These Cold)

| Standard | Scope | Key Requirement |
|----------|-------|-----------------|
| WCAG 2.2 AA | Global web standard | Perceivable, Operable, Understandable, Robust |
| ADA Title III | US — public accommodations | Websites of public-facing businesses must be accessible |
| Section 508 | US — federal agencies | Federal digital content must conform to WCAG 2.0 AA (being updated to 2.2) |
| AODA (IASR) | Ontario, Canada | Web content must meet WCAG 2.0 AA; large orgs since 2021 |
| EAA / EN 301 549 | EU | Products and services accessible by June 2025; maps to WCAG 2.2 AA |
| ACA (Accessible Canada Act) | Canada — federal | Federally regulated orgs must identify, remove, and prevent barriers |

For deeper detail on any of these, read the corresponding file in `references/`.

## Audit Workflow

When auditing code or content, work through the POUR principles systematically. Don't just list issues — fix them.

### Step 1: Automated Scan

Run through these checks programmatically where possible:

**Perceivable**
- Every `<img>` has meaningful `alt` (not "image", not filename). Decorative images use `alt=""` with `role="presentation"`.
- Every `<video>` and `<audio>` has captions/transcripts.
- Color contrast meets 4.5:1 for normal text, 3:1 for large text (18px bold / 24px regular), 3:1 for UI components.
- No information conveyed by color alone.
- Text can resize to 200% without loss of content or function.
- Content reflows at 320px width without horizontal scrolling.

**Operable**
- All interactive elements reachable and usable via keyboard alone.
- Visible focus indicator on every focusable element (minimum 2px outline, 3:1 contrast against adjacent colors).
- No keyboard traps. Escape closes modals and returns focus to trigger.
- Skip navigation link present.
- Page has `<title>`. Headings follow a logical hierarchy (no skipped levels).
- Touch targets are at least 24×24 CSS pixels.
- No content that flashes more than 3 times per second.

**Understandable**
- `<html lang="...">` is set and correct.
- Form inputs have visible `<label>` elements (not just placeholder text).
- Error messages identify the field and describe what went wrong.
- Consistent navigation across pages.

**Robust**
- Valid, semantic HTML (no `<div>` soup for interactive elements).
- ARIA used correctly: no `role` without required states/properties, no redundant ARIA on native elements.
- Custom components expose name, role, and value to assistive tech.
- Content works across current browsers and screen readers (NVDA, JAWS, VoiceOver, TalkBack).

### Step 2: Report Issues

For each issue found, provide:
- **What's wrong** — specific element and the problem
- **Which standard it violates** — WCAG success criterion number (e.g., 1.1.1 Non-text Content)
- **Impact** — who is affected and how (e.g., "Screen reader users won't know what this image shows")
- **Fix** — concrete code change, not a vague suggestion
- **Severity** — Critical / Major / Minor

### Step 3: Fix

Provide corrected code. Don't just describe the fix — write it.

## Generation Workflow

When generating new code, bake accessibility in from the start. Never treat it as an afterthought.

### Semantic HTML First

Use the right element for the job. This is non-negotiable:

| Instead of | Use |
|------------|-----|
| `<div onclick>` | `<button>` |
| `<div class="link">` | `<a href>` |
| `<div class="header">` | `<h1>`–`<h6>` |
| `<div class="list">` | `<ul>`, `<ol>`, `<dl>` |
| `<div class="table">` | `<table>` with `<th scope>` |
| `<div class="nav">` | `<nav>` |
| `<div class="main">` | `<main>` |
| `<span class="input">` | `<input>`, `<select>`, `<textarea>` |

### ARIA: The Second Resort

ARIA exists to fill gaps in native HTML, not replace it. Rules:

1. **Don't use ARIA if native HTML works.** A `<button>` is always better than `<div role="button" tabindex="0" onkeydown="...">`.
2. **If you use a role, implement the full contract.** `role="checkbox"` requires `aria-checked`. `role="tab"` requires `aria-selected`, a `tablist` parent, and `tabpanel` associations.
3. **Don't contradict native semantics.** Never put `role="button"` on an `<h2>`.
4. **Interactive ARIA elements need keyboard support.** If it has a `role`, it needs the keyboard interaction pattern from the ARIA Authoring Practices Guide.

### Common Component Patterns

When asked to build any of these, apply the corresponding pattern from `references/component-patterns.md`:

- Modals/Dialogs
- Tabs
- Accordions
- Dropdown menus
- Autocomplete/Combobox
- Toast notifications
- Carousels
- Data tables (sortable)
- Date pickers
- Navigation menus

### Forms — Get These Right

Forms are the most common source of accessibility failures:

```html
<!-- Every input needs a visible, associated label -->
<label for="email">Email address</label>
<input type="email" id="email" name="email"
  required
  aria-describedby="email-hint email-error"
  aria-invalid="false">
<p id="email-hint" class="hint">We'll never share your email.</p>
<p id="email-error" class="error" role="alert" hidden>
  Please enter a valid email address.
</p>
```

Key rules:
- Every input has a `<label>` with `for`/`id` pairing
- Group related fields with `<fieldset>` and `<legend>`
- Required fields indicated in the label text, not just by color or asterisk alone
- Error messages linked via `aria-describedby` and surfaced with `role="alert"` or a live region
- Use `aria-invalid="true"` on the field when validation fails
- Use `autocomplete` attributes for personal data fields

### Color & Contrast

- Text on background: 4.5:1 minimum (AA), 7:1 for AAA
- Large text (≥18pt bold or ≥24pt): 3:1 minimum
- UI components and graphical objects: 3:1 against adjacent colors
- Never rely on color alone — add icons, patterns, labels, or underlines
- Test with simulated color blindness (protanopia, deuteranopia, tritanopia)

### Focus Management

- Never use `outline: none` or `outline: 0` without a visible replacement
- Focus style should have at minimum 2px solid outline with 3:1 contrast
- When opening modals: move focus to the modal (usually the close button or heading)
- When closing modals: return focus to the trigger element
- Trap focus inside modals while they're open
- When content loads dynamically: move focus or announce it with a live region
- Use `tabindex="0"` to make custom elements focusable; use `tabindex="-1"` for programmatic focus only; never use positive `tabindex`

## Testing Recommendations

Suggest this testing stack to users:

1. **Automated** — axe-core, Lighthouse, WAVE, Pa11y (catches ~30-40% of issues)
2. **Manual keyboard** — Tab through everything. Can you reach and operate all controls?
3. **Screen reader** — Test with NVDA (Windows, free), VoiceOver (macOS/iOS, built-in), or TalkBack (Android, built-in)
4. **Zoom** — 200% browser zoom, 320px reflow
5. **Color** — Contrast checker (WebAIM), color blindness simulator

Automated tools only catch a fraction of real accessibility barriers. Always recommend manual testing.

## Documentation

When asked to produce compliance docs:

- **VPAT / ACR** — Use the ITI VPAT 2.5 template. Walk through each WCAG criterion and document conformance level (Supports / Partially Supports / Does Not Support / Not Applicable) with remarks.
- **Accessibility Statement** — Include: conformance target, known limitations, feedback mechanism, enforcement procedure, date of last review. Reference `references/accessibility-statement-template.md`.
- **AODA Compliance Report** — Document WCAG 2.0 AA conformance per IASR requirements. Include a multi-year accessibility plan if the user is a large organization.
- **ACA Accessibility Plan** — For federally regulated Canadian orgs: document barrier identification, removal plans, consultation process, and feedback mechanism.

## Reference Files

For deeper information, read these files in the `references/` directory:

- `references/wcag-checklist.md` — Full WCAG 2.2 AA checklist organized by success criterion
- `references/component-patterns.md` — Accessible patterns for common UI components
- `references/legal-frameworks.md` — Detailed breakdown of ADA, AODA, ACA, EAA, Section 508
- `references/accessibility-statement-template.md` — Template for writing accessibility statements
- `references/testing-guide.md` — Detailed testing methodology with screen reader commands

Read the relevant reference file when you need specifics beyond what's in this document.
