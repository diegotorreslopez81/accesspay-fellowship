# Fellowship Proposal: AccessPay

> Draft for the Interledger Foundation 2026 Fellowship Program.
> Program guide: https://github.com/interledger/Grants/wiki/Fellowship
> Submission portal: https://submit.interledger.org/submit/352640/2026-interledger-fellowship

Duration: 12 months, September 2026 to August 2027. 32 hours per week.
Stipend: $72,000 USD. Project budget: $20,000 USD.

Focus areas (from the program guide, projects may span more than one):
- Ecosystem and Community Connection: bridge between the Interledger ecosystem and the European non-profit / digital-inclusion community.
- Technology Stewardship and Knowledge Sharing: public research paper, practitioner's guide, upstream contributions, and two integrations shared as open-source modules.

---

## 1. Background and Expertise

I'm Diego Torres Lopez. Twenty years in production software engineering, currently running a portfolio of small SaaS products under Infinite Labs OÜ (Estonia) and presiding over Basics Tech, a Spanish non-profit (asociación sin ánimo de lucro, Catalonia) whose mission is bringing AI and digital tooling to groups left behind by digitalisation.

**Why I'm positioned to do this Fellowship:**

My link to the Interledger ecosystem starts with the Moncon team, a Grant for the Web alumni project. Moncon built a payment-gated content SaaS on top of Web Monetization. I was responsible for significant parts of the stack, which put me inside the Web Monetization and Open Payments conversation early and gave me hands-on experience with the protocols' predecessors.

Since then, two production products I operate today put me in daily contact with the real-world concerns this Fellowship aims to address:

- **Contestia** (https://contestia.co): a WhatsApp AI receptionist for Spanish health clinics, in production with paying customers. Stack: Python (FastAPI) + Next.js + Postgres + Google Gemini + WhatsApp Business API. Currently using Stripe as the payment layer.
- **AGING-AI**: a digital-inclusion pilot for 50 elderly users in the Vallès Occidental (Catalonia), co-funded by DKV Impacta 2026 and two Catalan municipalities. Launched pilot July-December 2026. Focus on elderly populations excluded from digital services.

I'm also active in the Interledger community today: I recently applied to the 2026 SDK Grant Program for `openpay-kit` (Arazzo workflows for Open Payments) on 20 April 2026, after an open scope discussion with Program Officer Jeremiah Lee in #cfp-sdk. The `openpay-kit` repo is public at https://github.com/diegotorreslopez81/openpay-kit.

**Familiarity with Interledger Protocol and Open Payments:** I have worked through the Open Payments specification (https://openpayments.dev/), Rafiki setup and sandbox, the GNAP RFC (9635), and the Arazzo specification in preparing the SDK grant proposal. I can read and trace a grant request + continuation flow end-to-end in the current spec and I'm comfortable setting up a local Rafiki playground.

**Communities I engage with:**

- Interledger community (Slack, Community Forum, GitHub).
- Spanish non-profit / third-sector ecosystem (Basics Tech, ASICRE, municipalities in the Vallès).
- European digital rights and open-standards community (NLnet/NGI, Eticas).
- EU healthtech small clinics (via Contestia customer base).

**How this Fellowship aligns with my professional trajectory:**

The Fellowship gives me a focused 12-month window to do the bridging work that I can't do inside the day-to-day of running the products. That's the piece I can't shoehorn into 4 hours a week: the research with other entities, the technical integrations with public MIT releases, the advocacy in the right venues. The outcome I'm after is a public body of work that makes Open Payments a real option for the European non-profit sector, and that opens a door between two ecosystems that don't talk today.

---

## 2. Project Title and Overview

**Title:** AccessPay: Open Payments for the European Non-Profit and Digital-Inclusion Sector.

**One-sentence version:** twelve months of research, technical integration, and advocacy to make Open Payments a viable payment layer for the European non-profit and digital-inclusion sector, using two production SaaS I already operate (Contestia and AGING-AI) as real deployment grounds.

**What I will do during the 12 months:**

Three tracks running in parallel across the Fellowship:

1. **Research (about 45% of the time):** a structured qualitative study of 10 to 15 European third-sector entities (municipalities, health non-profits, NGO umbrella groups, digital-rights bodies), asking where Open Payments could create value today, what's blocking it, and what would need to change. Output: a public findings paper (CC BY-SA, English and Spanish), per-entity case sketches, and a set of recommendations for the Interledger Foundation, the Open Payments spec, and the European third sector.

2. **Technical work (about 40%):** two production integrations of Open Payments. Contestia (health clinics SaaS, paying customers) gets an Open Payments track for a specific flow such as patient appointment deposits or recurring small subsidies, behind a feature flag. AGING-AI (elderly digital-inclusion pilot) becomes a proof-of-concept front-end for municipalities or foundations to push small subsidies (medication reimbursements, elder-care vouchers) to vulnerable users through WhatsApp, using Open Payments as the payment rail. Both integrations ship as open-source MIT modules in a shared repo called `openpay-impact`, designed for other EU non-profit SaaS to pick up.

3. **Advocacy (about 15%):** two conference talks (primary targets: FOSDEM 2027, Open Source Summit Europe 2026) and one public practitioner's guide in English and Spanish. The goal is to connect the Interledger ecosystem with the European third-sector ecosystem, which today don't overlap, and to make the practical integration knowledge available to other implementers.

**Why this work matters:**

The European non-profit and digital-inclusion sector runs on payment infrastructure that doesn't serve it well: 2 to 5 percent fees on closed-source donation gateways, uneconomic micropayments, slow manual cross-border transfers. Open Payments has the right primitives for this sector, but nobody is deploying it here today, for two reasons. First, there's no playbook (research gap on where it fits, technical gap on how to integrate). Second, there's no bridge between the Interledger community and the European third-sector community.

Interledger Foundation has strong research and technical work in North America (Sheena Allen's Southern US study) and in Africa (multiple current Ambassadors). The European third-sector perspective is a geography that's currently underserved in the portfolio, and it matters because Europe is where several adjacent regulatory frameworks (AI Act, EAA, NIS2) are reshaping how digital financial services get deployed in civil society.

**Who benefits:**

- European NGOs, municipalities, and third-sector entities currently stuck with payment infrastructure that doesn't fit their needs.
- Vulnerable populations served by those entities (elderly digital-inclusion programmes, patient associations, low-income communities) who could access micro-subsidies or low-fee transfers through channels they already use.
- The Interledger Foundation itself: a new geography and sector in the portfolio with detailed research and two real integrations to show.
- Other implementers in the Open Payments ecosystem who could reuse the integration modules or build on the research.

**How this builds on my expertise:**

I ship in this sector today (Contestia, AGING-AI). I'm part of the Interledger ecosystem today (Moncon alumni, 2026 SDK grant applicant). I operate a Spanish non-profit whose remit is exactly "digital tooling for underserved groups". The Fellowship lets me bring these three threads together for a sustained 12-month effort.

---

## 3. Goals, Objectives, and Approach

### Specific objectives (achievable in 12 months)

1. **Publish a public findings paper**, in English and Spanish, CC BY-SA, based on qualitative interviews with 10 to 15 European third-sector entities, covering where Open Payments could create value, what's blocking it, and what needs to change. Target: 8,000 to 12,000 words plus case sketches.

2. **Ship two open-source Open Payments integration modules** (`openpay-impact` repo, MIT license): one live in a Contestia pilot clinic with real transactions, one as a proof-of-concept subsidy-distribution flow on top of AGING-AI. Both shipped with README, runnable demos, and honest post-mortems.

3. **Deliver two conference talks** (primary: FOSDEM 2027, Open Source Summit Europe 2026) and one public practitioner's guide in English and Spanish, hosted on BasicsTech.org and the fellowship repo.

4. **File at least two upstream contributions** to Rafiki, the Open Payments specification, or Kiota, surfaced during the integration work. Each disclosed per Badge AI conventions.

5. **Run monthly public progress posts** on the Interledger Community Forum and monthly reports to the Program Team, demonstrating a visible cadence that the community can follow.

### Approach and methods

**Research track (qualitative, mixed methods):**
- Literature review and framing in the first two months.
- Semi-structured interviews, 45 to 60 minutes, in three waves of 5 entities each.
- Thematic coding across transcripts, member-checking of case sketches with interviewees before publication.
- Peer review of the final paper by 2 or 3 Interledger community reviewers and 2 or 3 third-sector reviewers.
- Ethics: informed consent, data encryption, no personal data about beneficiaries, only entity-level information. Consent template published in month 1.

**Technical track:**
- Shared MIT module (`openpay-impact`) consumed by both integrations, so the work produces something reusable.
- Contestia integration behind a feature flag, staged rollout to one pilot clinic first.
- AGING-AI integration as a proof-of-concept against the live pilot, documented end-to-end.
- Stack: Node (TypeScript) for the shared module, Rafiki sandbox for dev, a real wallet provider for staging and production (candidate: Interledger test wallet initially, then a production-ready EU wallet once selected).
- Upstream PRs filed within the same week as the issue surfaces.

**Advocacy track:**
- Talk 1 (FOSDEM 2027): submitted month 7 or 8, delivered early February 2027 if accepted.
- Talk 2 (OSSEU 2026): submitted month 4 or 5, delivered October 2026 if accepted.
- Practitioner's guide drafted months 10 and 11, published month 12.

### Feasibility assessment

- **Research:** I already have warm contacts with 5 entities I can recruit from day one (Basics Tech network, DKV Impacta pilot partners, Vallès municipalities). Three waves of 5 interviews each over months 3 to 8 is a comfortable pace at 14 hours per week on the track.
- **Technical:** I operate both Contestia and AGING-AI directly. I don't need to negotiate access or build something from scratch. 13 hours per week is enough for two integrations that already have a host product.
- **Advocacy:** 5 hours per week across 12 months is enough for one guide and two CFP submissions. Conference travel is the main concrete expense.
- **Time:** 32 hours per week over 12 months totals about 1,560 hours. The proposed deliverables fit within that.

### Infrastructure and resources available

- Existing production systems (Contestia, AGING-AI) as deployment grounds.
- Basics Tech's network of municipal and non-profit partners for research recruitment.
- Infinite Labs OÜ infrastructure (Hetzner Frankfurt, Coolify, CI, monitoring).
- Open repos already in place (openpay-kit for SDK grant, accesspay-fellowship for this work).
- Active relationship with the Interledger community (Jeremiah Lee DM and #cfp-sdk posts since 15 and 20 April 2026).
- Fluent English and native Spanish, enabling research in both languages.

### Expected outcomes

- One findings paper published under CC BY-SA, in two languages.
- Two open-source integration modules, MIT licensed, with at least one live production deployment.
- Two delivered conference talks or one talk plus one recorded community session.
- One practitioner's guide in two languages.
- At least two upstream PRs or issues filed.
- A persistent relationship between the Interledger ecosystem and a set of European third-sector entities, surviving the Fellowship.

---

## 4. Community Engagement and Interledger Integration

**How I'll engage communities with the Interledger ecosystem:**

- **Direct introductions.** The research interviews put me in front of 10 to 15 entities in the European third sector that don't currently know what Open Payments is. After each interview, the entity receives a short, tailored brief on what Open Payments could mean for them, plus a pointer to the Interledger Community Forum and the Foundation's work. Where appropriate, I introduce them directly to Interledger staff or Community members working on adjacent problems.

- **Technical work as proof.** Contestia and AGING-AI have real users. The integrations make Open Payments a live option inside Spanish health clinics and a pilot of 50 elderly users. Other EU third-sector operators who see the demos get concrete evidence, not slides.

- **Public advocacy in shared venues.** FOSDEM and OSSEU are where EU open-source practitioners show up. The talks surface Open Payments to audiences that today only see closed payment rails.

- **Ongoing presence in Interledger channels.** Monthly progress posts in the Community Forum. Active in #cfp-sdk. Two appearances per quarter on community calls if the schedule fits, happy to host one community call myself on the findings.

**How the work supports experimentation and adoption of Open Payment Standards:**

- `openpay-impact` (the shared MIT module) is designed for reuse. Any EU non-profit SaaS integrating a payment flow can start from it, skipping the steep first-integration curve.
- The practitioner's guide explicitly addresses the questions I'd need answered to integrate Open Payments into a production system: Rafiki sandbox setup, wallet provider selection, feature-flagging a new rail behind an existing one, compliance and KYC for small EU non-profits.
- The research output names concrete spec gaps, surfacing them where the Foundation and spec contributors can act on them.

**How I'll prepare community members for Interledger Foundation programs and funding:**

- Every interviewed entity that expresses interest gets pointed to current Foundation programs (Fellowship, SDK Grant, Interledger on Campus where relevant, Ambassador if reinstated).
- During the Fellowship I identify 2 or 3 European entities as particularly strong future Foundation applicants and help them scope potential proposals in the final quarter of the project.
- The practitioner's guide includes a brief "how to apply for Interledger Foundation support" section so that technical readers see the on-ramp.

---

## 5. Impact and Success Metrics

### Concrete, measurable changes targeted

**Research impact:**
- 1 findings paper published, downloadable and citable.
- 10 to 15 case sketches published (anonymised where requested), each a reusable reference.
- At least 3 recommendations for the Open Payments spec or the Interledger ecosystem that the Foundation can act on (e.g., missing primitives for small recurring transfers, wallet ergonomics for elderly users).

**Technical impact:**
- 1 production clinic live on Contestia with Open Payments transactions, with measurable transaction volume at Fellowship end.
- 1 proof-of-concept subsidy flow on AGING-AI, documented end-to-end, with at least 5 real elderly user tests.
- 1 shared MIT module (`openpay-impact`) with at least 1 external reuse or reference by another EU non-profit or developer.

**Advocacy impact:**
- 2 conference talks delivered, video recordings available.
- 1 practitioner's guide in English and Spanish, with at least 500 unique page views within 60 days of publication.
- At least 2 upstream PRs or issues filed to Rafiki, Open Payments, or Kiota, disclosed per Badge AI.

**Ecosystem impact:**
- 3+ European third-sector entities introduced to the Interledger ecosystem and maintaining an ongoing relationship with the Foundation or Community beyond the Fellowship.
- 1 follow-on Foundation application scoped by a European entity that would not have applied without the Fellowship's introduction.

### Tracking

- Public monthly progress posts in the Community Forum capture qualitative progress.
- Technical metrics (transaction volume, user tests, repo stars and external contributors) captured in the final report.
- Research KPIs (number of interviews completed, case sketches published, paper downloads) tracked in the monthly reports to the Program Team.

### Policy relevance

The findings paper will address how Open Payments interacts with the EU regulatory frame: the AI Act (for AI-assisted payment flows in Contestia and AGING-AI), the EAA (accessibility of wallet UX, critical for elderly users), GDPR (payment data handling), and PSD2 where relevant. This is the layer where Europe differs most from the North American and African contexts currently in the Interledger portfolio.

### How the work continues benefiting communities after the Fellowship

- Repos stay public and MIT-licensed. Issues and PRs accepted indefinitely.
- Findings paper and practitioner's guide stay hosted on BasicsTech.org.
- Basics Tech, as a Spanish non-profit, commits to maintaining the `openpay-impact` module as part of its regular roadmap for at least 18 months beyond the Fellowship end.
- The relationships between the European third-sector entities and the Interledger Community persist past the Fellowship because the Fellowship built them on concrete work, not on introductions that go cold.

---

## 6. Key Questions and Inquiry

The Fellowship investigates three questions, one per track:

### Research question

*Where can Open Payments create value in the European non-profit and digital-inclusion sector, what's blocking that today, and what would need to change (spec, tooling, policy, infrastructure) for those flows to be viable?*

I approach this through 10 to 15 semi-structured interviews across three waves (months 3-4, 5-6, 7-8), thematic analysis, and cross-case comparison. I expect to learn which payment flows in the sector are genuinely stuck on the current infrastructure (donations with high-fee gateways, cross-border transfers, micropayments for services), and which are blocked on factors beyond payments (wallet access, KYC, accessibility of wallet UX for elderly users, regulatory uncertainty in the EU).

Findings will be shared as a public paper (CC BY-SA, English and Spanish), per-entity case sketches, and direct briefings to the Foundation Program Team.

### Technical question

*What does it actually take to integrate Open Payments into a production impact-focused SaaS with paying customers today, and into a digital-inclusion pilot for vulnerable users, and what's the developer experience gap?*

I approach this through two concrete integrations: Contestia (production, paying clinics) and AGING-AI (pilot with elderly users). I expect to learn which parts of the current Rafiki and Open Payments stack are ready for small production deployments, where the wallet ecosystem is the bottleneck rather than the protocol, and what a non-Interledger-native developer needs to know before integrating.

Findings will be shared as open-source modules (`openpay-impact`, MIT), a written post-mortem per integration, and upstream PRs or issues to Rafiki, Open Payments, or Kiota where gaps surface.

### Community question

*How do the Interledger ecosystem and the European third-sector ecosystem connect, and what does a sustainable bridge between them look like?*

I approach this through sustained presence in both communities for 12 months, direct introductions where research surfaces opportunities, and public artefacts (paper, guide, talks) designed to lower the cost of entry from either side.

Findings will be shared as part of the final report to the Foundation, with concrete recommendations on which European entities are promising long-term community members or future funding applicants.

### How I'll share findings

- Monthly progress posts in the Interledger Community Forum.
- Monthly reports to the Program Team.
- A mid-Fellowship check-in post at month 6, sharing early research signals and technical post-mortems.
- Publication of the findings paper at month 12, followed by direct email to each interviewed entity.
- Two conference talks in the Fellowship window.
- Practitioner's guide in two languages.
- Final report 30 days after Fellowship end.

---

## Community engagement commitments (program requirements)

- Attend weekly check-ins with the Program Team.
- Attend Interledger community calls on a regular basis.
- Attend Interledger Summit 2026 or 2027 if the schedule allows.
- Publish monthly blog posts on the Interledger Community Forum.
- Present findings during community engagements at least twice during the Fellowship.

## Budget summary

The $20,000 project budget is allocated across the 7 approved categories in the program guide. Full breakdown in the Budget Template (uploaded separately); summary here:

| Category | Allocation | Purpose |
|---|---|---|
| Books, Toolkits, and Research | $3,500 | Academic paper access, Spanish-English translation services, interview transcription (Otter.ai or similar), analysis tools, compliance and regulatory database access. |
| Microgrants and Pilot Projects | $4,500 | Field research expenses (travel to 2-3 entities for in-person interviews), user testing compensation for AGING-AI PoC, small-scale pilot materials. |
| Professional Services and Skill Development | $2,500 | Expert consultation for research ethics review, EU compliance expert consultation for AGING-AI subsidy flows, grant-writing review for the findings paper submission. |
| Conferences and Seminars | $5,000 | FOSDEM 2027 travel and lodging, Open Source Summit Europe 2026 travel and lodging, registration fees, travel insurance, visa fees where applicable. |
| Tools and Equipment | $2,500 | High-performance laptop (loan basis per program policy) for the technical integration work on Contestia and AGING-AI, returnable at Fellowship end with option to purchase at market value. |
| Marketing and Awareness | $1,500 | Video production for the demo walkthrough of the integrations (month 10-11), content development for the practitioner's guide illustration, ILF merchandise coordinated through the ILF team. |
| Events | $500 | Contribution to a community gathering or co-hosted session if the opportunity surfaces during the Fellowship. |
| **Total** | **$20,000** | |

The $72,000 stipend covers 12 months at 32 hours per week.

## Timeline summary

Full month-by-month plan in [docs/roadmap.md](roadmap.md) and in the Timeline Template (uploaded separately).

| Phase | Months | Focus |
|---|---|---|
| Framing | Sep-Oct 2026 (M1-M2) | Literature review, interview guide, ethics templates, repo scaffolding, Contestia stub integration |
| Wave 1 | Nov-Dec 2026 (M3-M4) | 5 interviews, analysis, case sketches. Contestia integration end-to-end in sandbox. OSSEU CFP submission. |
| Wave 2 + Contestia live | Jan-Feb 2027 (M5-M6) | 5 interviews, Contestia live in one pilot clinic, post-mortem. FOSDEM CFP submission. |
| Wave 3 + AGING-AI | Mar-Apr 2027 (M7-M8) | 5 interviews, AGING-AI PoC in sandbox. Talk delivery. |
| Drafting | May-Jun 2027 (M9-M10) | Research paper drafting, AGING-AI PoC live, peer review. |
| Publication | Jul-Aug 2027 (M11-M12) | Paper published (EN+ES), practitioner's guide, final report. |

## AI disclosure

Full policy in [docs/ai-use.md](ai-use.md). Primary model: Claude Opus 4.7. Badge AI: AI-assisted, human-reviewed. Per-day prompt log. 100% human responsibility for every committed artefact.

## Diversity, equity, and inclusion

Diego is a Spanish researcher and developer working in Catalonia. The Fellowship explicitly targets European third-sector entities serving underserved populations: elderly users in the Vallès (AGING-AI), patients of small regional clinics (Contestia), digital-rights communities, NGOs handling cross-border transfers to LATAM and Africa. Research outputs are published in English and Spanish to widen the circle of who can engage with them. The geographic focus (European non-profit sector) is currently underrepresented in the Foundation's funded portfolio, which skews toward North America and Africa.

## References (uploaded separately)

Two letters of reference are uploaded with the application:
- (Reference 1: to be confirmed)
- (Reference 2: to be confirmed)

---

*Draft v0.2, April 2026*
