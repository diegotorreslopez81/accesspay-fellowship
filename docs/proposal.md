# Fellowship Proposal: AccessPay

> Draft for submission to the Interledger Foundation 2026 Fellowship Program.
> Program: https://github.com/interledger/Grants/wiki/Fellowship
> Submission portal: https://submit.interledger.org/submit/352640/2026-interledger-fellowship

---

## Summary

I want to spend 12 months making Open Payments a viable payment layer for the European non-profit and digital-inclusion sector. The work is a mix of research (roughly 45%), technical integration in two production products I already operate (roughly 40%), and advocacy (roughly 15%).

The research maps the opportunity space: interviews and case studies with 10 to 15 European third-sector entities on where Open Payments could unlock value (donations, small-service micropayments, cross-border partner transfers, digital-inclusion pilots). Output: a public findings paper plus per-entity case sketches.

The technical work builds two real integrations. Contestia (WhatsApp AI receptionist for Spanish health clinics, in production with paying customers) and AGING-AI (digital-inclusion pilot for 50 elderly users in the Vallès, funded by DKV Impacta 2026). Both are existing, running, and in the non-profit or impact space. Integrating Open Payments into them is a concrete way to show what it looks like outside a technology demo.

The advocacy work connects the two ecosystems that don't talk today. Two conference talks (targeting FOSDEM, Open Source Summit Europe, or an NLnet/NGI event) and one public practitioner's guide about integrating Open Payments in production impact software.

## Problem

The European non-profit and digital-inclusion sector runs on payment infrastructure that doesn't serve it well. Donations go through closed-source gateways with 2 to 5 percent fees. Micropayments for small services are economically unviable. Cross-border transfers between partner NGOs, especially from EU funders to LATAM or Africa implementers, are slow, expensive, and manual.

Open Payments exists, is open, and has the right primitives for this sector (incoming payments, grants for continuation, composable flows). But nobody is deploying it here, for two reasons.

First, there's no playbook. The research gap is real: what parts of a European NGO's payment stack could Open Payments replace today, which ones next year, and which never? The technical gap is real too: how do you plug Open Payments into a production health SaaS with paying clients, or into a digital-inclusion pilot running over WhatsApp?

Second, there's no bridge between ecosystems. The Interledger community and the European impact-focused non-profit community don't overlap. The Interledger Foundation has strong research and technical work in North America and Africa, and partnerships with universities across 10+ countries. Europe's third-sector networks (NLnet/NGI, Fundación La Caixa's Observatorio Social, NGO umbrella groups in Brussels) are not yet part of that conversation.

This fellowship is an attempt to start closing both gaps.

## What I'm proposing to do

### Research (about 45%)

A structured, 12-month study: *Deploying Open Payments in the European non-profit and digital-inclusion sector.* Field work based on interviews and archive analysis with 10 to 15 entities, split across three waves (months 3-4, 5-6, 7-8).

Entity shortlist by type:

- Municipalities deploying digital-inclusion programmes (Terrassa, Sabadell, and 2 to 3 others in the Vallès Occidental).
- Health and care non-profits (ASICRE, small regional clinic networks).
- NGO umbrella groups handling cross-border transfers (candidate: Oxfam Intermón).
- Digital-rights and open-standards bodies (NLnet, Eticas, Algorithm Watch).
- Small fundraising platforms that could move off closed gateways.
- At least two non-Spanish entities to avoid a single-country bias.

Methodology follows established qualitative research practice (semi-structured interviews, thematic analysis, member-checking with interviewees before publication). Every interview produces a short case sketch; together they produce the findings paper.

Outputs:

- Public findings paper, English + Spanish, creative-commons licensed.
- Per-entity case sketches, anonymised where requested.
- A map of where Open Payments fits, where it doesn't yet, and what's missing in the spec or tooling for this sector.

Details and methodology in [docs/research-plan.md](research-plan.md).

### Technical work (about 40%)

Two production integrations of Open Payments in products I already operate under Basics Tech and Infinite Labs OÜ:

**Contestia** (production, paying customers): health-clinic AI receptionist with Stripe as the current payment layer. I'll add an Open Payments track for a specific flow (candidate: one-off appointment deposits from patients without cards, or clinic-to-clinic referral payments). Feature-flagged behind an opt-in, so production doesn't break; public MIT repo hosting the integration module.

**AGING-AI** (pilot funded by DKV Impacta 2026, 50 elderly users in the Vallès): the pilot itself is about digital inclusion, not payments. The Open Payments angle is different: how can AGING-AI serve as a front-end to let NGOs or municipalities push small subsidies (medication reimbursements, elder-care vouchers) to vulnerable users through a channel they already use (WhatsApp)? I'll build a proof-of-concept subsidy-distribution flow and document whether the Open Payments rail is ready for this use case today, what's missing if not, and what would need to change.

Both integrations ship as open-source modules with a README, a runnable demo, and a post-mortem of what worked and what didn't. When I hit spec ambiguities or Rafiki papercuts, PRs and issues go upstream within the same week.

Details in [docs/technical-plan.md](technical-plan.md).

### Advocacy (about 15%)

Two conference talks and one public guide:

- Talk 1 target: **FOSDEM 2027** (Open Source track, Payments or Web Monetization devroom) or **NLnet/NGI annual gathering**. Subject: "Open Payments in the European third sector, what we learned".
- Talk 2 target: **Open Source Summit Europe 2026** or **Interledger Summit**. Subject: "Integrating Open Payments into a production health SaaS, honest notes".
- Public practitioner's guide, hosted on the fellowship repo and BasicsTech.org, English + Spanish. Roughly 3,000 to 5,000 words, with code samples.

Details in [docs/advocacy-plan.md](advocacy-plan.md).

## Approach summary

Public from day one. Repo already scaffolded at https://github.com/diegotorreslopez81/accesspay-fellowship, monthly public progress notes in the Interledger community forum and in #cfp-sdk, monthly reports to the Fellowship Program Officer. Every upstream PR discloses AI usage per Badge AI conventions.

## Timeline

Twelve monthly milestones, detailed in [docs/roadmap.md](roadmap.md). Research, technical, and advocacy tracks run in parallel, not sequential. Every month ends with a public artefact: a tag, a publication, or a progress report.

## Budget

- Fellowship stipend: $72,000 (12 months of personal time at fellowship level).
- Project stipend: $20,000 (broken down in [docs/roadmap.md](roadmap.md)): $8K research activities (transcription, translation, analysis tools, fieldwork travel), $7K technical (infrastructure, development sandboxes, open-source tooling), $4K advocacy (two conferences and publication design), $1K buffer.

Total: $92,000 over 12 months.

## Why me

Twenty years in production software. Grant for the Web alumni via Moncon (relevant priors in the Interledger ecosystem). Currently operating two products in the Spanish non-profit and health sector (Contestia, AGING-AI). President of Basics Tech, a Spanish non-profit whose explicit mission is bringing AI and digital tooling to groups left behind by digitalisation. Active in #cfp-sdk, recently submitted an SDK grant for openpay-kit (Arazzo workflows for Open Payments), public scope post on 20 April 2026.

I'm at the right intersection: enough technical depth to ship real integrations, enough non-profit operational experience to do the research with credibility, and an existing relationship with the Interledger ecosystem to translate findings back.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Research participants hard to recruit in the EU third sector | I already have warm contacts via Basics Tech, DKV Impacta, and municipal partners in the Vallès. First wave uses these contacts; later waves expand outward. |
| Open Payments not yet ready for some proposed flows | The research is designed to surface exactly this. Findings paper is valuable even if the answer is "not yet, here's what's missing". |
| Contestia integration breaks production | Feature-flagged, opt-in only, behind an internal toggle. Staged rollout to one pilot clinic first. |
| AGING-AI pilot ends before month 12 | DKV pilot is 6 months, starts mid-2026. Integration work happens during the live pilot window. Post-pilot the integration remains in the codebase as a reference. |
| Conference CFPs don't accept my talks | Back-up targets in a wider pool (5+ candidate venues). If nothing lands, a self-hosted online session with the Interledger community. |
| Solo developer risk | Monthly public reports give early warning on slippage. Research track can continue if technical slips, and vice versa. |

## AI disclosure

See [docs/ai-use.md](ai-use.md). Summary: Claude Opus 4.7 as primary model, Badge AI "AI-assisted, human-reviewed", per-day prompt log, 100% human responsibility for every committed line.

---

*Draft v0.1, April 2026*
