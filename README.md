# Digital Accessibility Skill

A skill for auditing, fixing, building and documenting accessible web UI against WCAG 2.2 and the laws that reference it: ADA, Section 508, AODA, the Accessible Canada Act, the European Accessibility Act with EN 301 549, and the UK public sector regulations.

It follows the open [Agent Skills](https://agentskills.io/specification) format, so it works with any agent that reads `SKILL.md` files, including Claude Code, Codex, Cursor and Gemini CLI.

## What it does

- audits HTML, React, Vue and other web UI and names the WCAG 2.2 success criterion for every finding
- writes the corrected code, not just a description of the fix
- builds accessible components from the ARIA Authoring Practices patterns, native HTML first
- answers "which law applies to us" with the instrument, the WCAG version it points at, and the dates
- drafts VPAT 2.5Rev conformance reports, accessibility statements, AODA reports and Accessible Canada Act plans

## Evidence

Every legal and technical claim in the skill was checked against a primary source on 2026-09-15, and the source URL sits next to the claim. Facts that changed recently and are reflected here:

| Claim | Current position (2026-09-15) | Source |
|---|---|---|
| ADA Title II compliance dates | 26 April 2027 (population 50,000+) and 26 April 2028 (smaller entities), after the DOJ interim final rule of 20 April 2026 | [Federal Register](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web) |
| EAA technical standard | EN 301 549 v3.2.1 (WCAG 2.1 AA) remains the harmonised standard; v4.1.1 (WCAG 2.2) was published in September 2026 and awaits Official Journal citation | [AccessibleEU](https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en) |
| Accessible Canada Act ICT rules | Regulations published 17 December 2025; in force 5 December 2027 (federal public sector) and 5 December 2028 (private sector, 100+ employees); standard is CAN/ASC-EN 301 549:2024 | [Canada Gazette Part II](https://gazette.gc.ca/rp-pr/p2/2025/2025-12-17/html/sor-dors255-eng.html) |
| Section 508 | Still references WCAG 2.0 AA | [US Access Board](https://www.access-board.gov/ict/) |
| UK public sector | WCAG 2.2 AA, monitored by GDS since October 2024 | [GOV.UK](https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps) |
| VPAT template | VPAT 2.5Rev (April 2025), four editions | [ITI](https://www.itic.org/policy/accessibility/vpat) |
| Automated test coverage | 30 to 40% of criteria (GOV.UK 2017), 57% of issues by volume (Deque 2021) | linked in `references/testing-guide.md` |
| Overlay compliance claims | FTC final order against accessiBe, US$1 million, April 2025 | [FTC](https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-approves-final-order-requiring-accessibe-pay-1-million) |

Dates move. If you are reading this long after the check date, treat the legal tables as a starting point and re-check the linked source.

## Install

With the [skills CLI](https://github.com/vercel-labs/skills) (works for Claude Code, Codex, Cursor, Gemini CLI and others):

```bash
npx skills add Gabriel-Dalton/digital-accessibility-skill
```

Manually, for Claude Code: copy the `digital-accessibility/` folder into `~/.claude/skills/` (personal) or `.claude/skills/` inside a project.

For the claude.ai web app: upload `digital-accessibility.skill` from the latest release, or build it with `bash scripts/build-skill.sh`.

Once installed, the skill loads itself whenever a request mentions accessibility, WCAG, ARIA, screen readers, keyboard navigation, contrast, VPATs or accessibility statements, and whenever you ask for a form, modal, tab set, table or navigation component.

## Example prompts

- Audit this React component for WCAG 2.2 AA issues and fix them
- Which accessibility law applies to a Canadian bank's customer portal, and by when?
- Build an accessible combobox with keyboard support
- Write an accessibility statement for an Ontario non-profit
- Draft the WCAG edition of a VPAT for our SaaS product

## Layout

```text
.
├── digital-accessibility/
│   ├── SKILL.md
│   └── references/
│       ├── accessibility-statement-template.md
│       ├── component-patterns.md
│       ├── legal-frameworks.md
│       ├── testing-guide.md
│       └── wcag-checklist.md
├── scripts/
│   └── build-skill.sh        builds digital-accessibility.skill (a zip) from the folder
├── tests/
│   └── test_skill.py         validates the frontmatter, links, criteria and layout
├── LICENSE
└── README.md
```

## Tests

```bash
python tests/test_skill.py
```

The tests validate the `SKILL.md` frontmatter with the reference validator from agentskills.io, check that every file the skill references exists, that every WCAG criterion cited in the references is a real 2.2 criterion at Level A or AA, that `SKILL.md` stays under 500 lines, and that no legal date claim lacks a "checked" date.

## Contributing

Corrections with a primary source are welcome. Open an issue with the claim, the source, and the date you checked it.

## License

MIT
