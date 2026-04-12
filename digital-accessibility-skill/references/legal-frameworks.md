# Legal Frameworks for Digital Accessibility

Detailed breakdown of accessibility legislation by jurisdiction. Use this when users ask about compliance requirements for a specific law.

## Table of Contents
- [ADA — Americans with Disabilities Act (US)](#ada--americans-with-disabilities-act-us)
- [Section 508 (US Federal)](#section-508-us-federal)
- [AODA — Accessibility for Ontarians with Disabilities Act (Canada, Ontario)](#aoda--accessibility-for-ontarians-with-disabilities-act-canada-ontario)
- [ACA — Accessible Canada Act (Canada, Federal)](#aca--accessible-canada-act-canada-federal)
- [EAA — European Accessibility Act / EN 301 549 (EU)](#eaa--european-accessibility-act--en-301-549-eu)
- [Other Jurisdictions](#other-jurisdictions)

---

## ADA — Americans with Disabilities Act (US)

### What It Covers
- Title II: state and local government services (including websites)
- Title III: public accommodations (businesses open to the public — including their websites and mobile apps)

### Technical Standard
- No explicit technical standard written into the law itself.
- DOJ has consistently pointed to WCAG 2.1 AA as the benchmark. The April 2024 final rule for Title II explicitly adopts WCAG 2.1 AA for state and local government web content and mobile apps.
- Title III: courts have broadly accepted WCAG 2.1 AA as the standard. No final DOJ rule yet for Title III, but it is the de facto expectation.
- **Safe baseline: WCAG 2.1 AA minimum. Aim for WCAG 2.2 AA.**

### Who Must Comply
- All state and local government entities (Title II) — compliance deadline: April 2026 for large entities (50,000+ population), April 2027 for smaller ones.
- All businesses that are "places of public accommodation" (Title III) — this has been interpreted to include websites, especially those connected to a physical location (hotels, retailers, restaurants, banks, healthcare providers, etc.). Courts have also applied it to online-only businesses.

### Enforcement
- Private lawsuits — individuals can sue. This is the primary enforcement mechanism.
- DOJ investigations and consent decrees.
- Structured Negotiation (voluntary, out-of-court process).
- No statutory cap on damages under Title III in private suits (injunctive relief only), but Title II and pattern-or-practice DOJ cases can include compensatory damages.
- ADA lawsuit volume: thousands per year. Majority target retail, food service, and hospitality.

### Key Case Law and Settlements
- Robles v. Domino's Pizza (2019): 9th Circuit held that ADA applies to websites and apps of places of public accommodation.
- NAD v. Netflix (2012): Streaming service required to caption all content.
- DOJ settlements with universities, healthcare systems, government agencies.

---

## Section 508 (US Federal)

### What It Covers
- All ICT (information and communication technology) developed, procured, maintained, or used by federal agencies.
- Includes websites, web applications, software, hardware, documents, multimedia, and telecommunications products.
- Also applies to contractors and vendors selling ICT to the federal government.

### Technical Standard
- Revised Section 508 (2017 refresh) incorporates WCAG 2.0 AA by reference for web content and non-web software.
- Electronic documents (PDF, Word, Excel, PPT) must also be accessible.
- Update to reference WCAG 2.2 is anticipated but not yet finalized. **Target WCAG 2.2 AA to be future-proof.**

### Who Must Comply
- All US federal agencies.
- Organizations that build or sell ICT to the federal government (vendors, contractors).
- Covered by Section 508 of the Rehabilitation Act.

### Enforcement
- Administrative complaints filed with the relevant federal agency.
- Agency-specific accessibility coordinators and Section 508 program offices.
- Procurement requirements: agencies should require VPATs/ACRs (Accessibility Conformance Reports) from vendors.
- GSA provides the Trusted Tester process and oversees government-wide compliance.

### VPAT / ACR
- Voluntary Product Accessibility Template (VPAT) is the standard format for documenting conformance.
- Current version: VPAT 2.5 (supports WCAG 2.2, Section 508, EN 301 549).
- VPATs should be completed by the vendor and made publicly available.
- Include conformance level per criterion: Supports, Partially Supports, Does Not Support, Not Applicable, Not Evaluated.

---

## AODA — Accessibility for Ontarians with Disabilities Act (Canada, Ontario)

### What It Covers
- The Integrated Accessibility Standards Regulation (IASR) under AODA addresses: information and communications, employment, transportation, design of public spaces, and customer service.
- The information and communications standard includes web content.

### Technical Standard
- WCAG 2.0 Level AA for web content (websites and web-based content).
- Applies to new and significantly refreshed websites.
- Ontario has not yet updated to WCAG 2.1 or 2.2 in the regulation, but the Human Rights Tribunal and courts may consider newer standards.

### Who Must Comply
- All organizations in Ontario with 1+ employees (public sector, private sector, non-profits).
- Large organizations (50+ employees): must file accessibility compliance reports, have multi-year accessibility plans, make websites WCAG 2.0 AA conformant.
- Small organizations (1-49 employees): have compliance obligations but fewer documentation requirements.

### Key Deadlines (All Past)
- January 1, 2014: new websites — WCAG 2.0 Level A
- January 1, 2021: all websites and web content — WCAG 2.0 Level AA

### Enforcement
- Accessibility Directorate of Ontario conducts audits and can issue compliance orders.
- Penalties: up to $100,000/day for corporations; up to $50,000/day for individuals.
- Human Rights Tribunal of Ontario (HRTO) complaints are also possible under the Ontario Human Rights Code.

---

## ACA — Accessible Canada Act (Canada, Federal)

### What It Covers
- Aims to achieve a barrier-free Canada by 2040.
- Covers: employment, built environment, ICT, communication (other than ICT), procurement of goods and services, delivery of programs and services, and transportation.
- ICT includes websites, software, hardware, digital content.

### Technical Standard
- The Act itself does not specify WCAG, but the Canadian Digital Service and Treasury Board Secretariat require WCAG 2.1 AA for Government of Canada websites.
- CAN/ASC - EN 301 549:2024 (Canadian adoption of the European standard) is the emerging technical standard.
- **Target WCAG 2.2 AA for federally regulated organizations.**

### Who Must Comply
- Federally regulated organizations: banks, telecommunications companies, transportation providers (airlines, rail, marine), broadcasters, the federal government itself, Crown corporations, and organizations in federal jurisdiction.
- Parliament of Canada.

### Requirements
- Prepare and publish accessibility plans (initial plan within specified timeframes).
- Establish feedback processes for receiving and responding to accessibility feedback.
- Prepare and publish progress reports.
- Consult with persons with disabilities in preparing plans.

### Enforcement
- Accessibility Commissioner (within the Canadian Human Rights Commission) handles complaints and compliance orders.
- Canadian Transportation Agency handles transportation-specific complaints.
- CRTC handles broadcasting and telecom complaints.
- Administrative monetary penalties for non-compliance.

---

## EAA — European Accessibility Act / EN 301 549 (EU)

### What It Covers
- Directive (EU) 2019/882 — the European Accessibility Act.
- Covers products and services: computers, smartphones, tablets, self-service terminals (ATMs, ticketing), e-readers, e-commerce, banking services, e-books, and more.
- Web Accessibility Directive (EU) 2016/2102 covers public sector websites and apps (already in effect).

### Technical Standard
- EN 301 549 v3.2.1 — the harmonized European standard for ICT accessibility.
- EN 301 549 maps directly to WCAG 2.1 AA for web content (clauses 9, 10, 11) and adds requirements for non-web software, hardware, and documentation.
- **EN 301 549 is the standard; WCAG 2.1 AA is embedded within it for web content.**

### Who Must Comply
- Private sector: any business placing products/services covered by the EAA on the EU market (even if the company is based outside the EU).
- Public sector: already required under the Web Accessibility Directive (websites since 2019, mobile apps since 2021).
- Microenterprises (fewer than 10 employees and turnover under €2M) are exempt from the EAA for services, but NOT for products.

### Key Deadlines
- June 28, 2025: EAA applies to all new products and services placed on the market.
- June 28, 2030: existing products and services must comply (transition period for service contracts entered before June 2025).

### Enforcement
- Each EU member state designates market surveillance authorities and creates enforcement mechanisms.
- Penalties vary by country — must be "effective, proportionate, and dissuasive."
- Individuals can seek remedies under national law.

---

## Other Jurisdictions

### United Kingdom
- Equality Act 2010 applies to digital services (service providers must make reasonable adjustments).
- Public Sector Bodies Accessibility Regulations 2018 require WCAG 2.1 AA for public sector websites and apps.

### Australia
- Disability Discrimination Act 1992 (DDA) covers digital accessibility.
- Maguire v. SOCOG (2000) was a landmark case — the Sydney Olympics website was found inaccessible.
- Australian Government Digital Service Standard requires WCAG 2.1 AA.

### Israel
- Israeli Standard 5568 mandates WCAG 2.0 AA for websites.
- Equal Rights for People with Disabilities Law applies.

### Japan
- JIS X 8341-3 maps to WCAG. Public sector compliance is expected.
- Revised Act on Elimination of Discrimination Against Persons with Disabilities (2024): private businesses now obligated to make reasonable accommodations.

### South Korea
- Act on the Promotion of Information and Communications Network Utilization and Information Protection.
- Korean Web Content Accessibility Guidelines based on WCAG.

### India
- Rights of Persons with Disabilities Act 2016.
- GIGW (Guidelines for Indian Government Websites) requires WCAG 2.0 AA.
