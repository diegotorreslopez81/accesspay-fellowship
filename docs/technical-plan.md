# Technical plan

Technical component of the AccessPay fellowship, roughly 40% of the work. Paired with [proposal.md](proposal.md).

Two production integrations of Open Payments in products I already operate. The point is to show what Open Payments looks like outside a demo: in a SaaS with paying customers, and in a pilot with real vulnerable users.

## Integration 1: Contestia

**What Contestia is:** a WhatsApp AI receptionist for Spanish health clinics. In production, paying customers. Current payment layer is Stripe, handling recurring subscriptions from clinics and one-off charges from some patients.

**What the Open Payments track looks like:** add a second payment rail for one specific flow, behind a feature flag, opt-in only. Candidate flows (to be chosen in month 2 based on first-wave research):

- **Patient appointment deposits.** Patient books via WhatsApp, system requests a small deposit to reduce no-shows. Currently only possible via Stripe card for patients who have one. Open Payments could let patients pay via a wallet they're getting through a bank or a local wallet provider, without needing a card.
- **Clinic-to-clinic referral payments.** One clinic refers a patient to another, small fee flows. Today this is manual and off-platform. A micropayment rail fits naturally.
- **Recurring tiny subsidies.** A municipality or foundation sponsors a patient's appointments and sends small recurring transfers to the clinic on that patient's behalf. Closer to the AGING-AI use case.

Whichever flow is chosen, the integration ships as:
- An open-source module in its own public MIT repo, consumable by other SaaS in the space.
- Feature-flagged in Contestia production. One pilot clinic opts in first. If it holds, a second.
- A post-mortem doc in month 6 covering what worked, what broke, what's still rough about the Open Payments developer experience in production.

**Stack:** Node (TypeScript) on Hono, Postgres, Rafiki sandbox for local dev, a real wallet provider (TBD, candidates include Gate Hub and any Spanish bank joining Open Payments) for staging and production.

**Definition of done for month 8:** one Contestia clinic has completed a real Open Payments transaction end-to-end in production, ideally multiple.

## Integration 2: AGING-AI

**What AGING-AI is:** a digital-inclusion pilot funded by DKV Impacta 2026. 50 elderly users in the Vallès Occidental, supported by two Catalan municipalities, running mid to late 2026. The pilot provides AI-assisted guidance through WhatsApp to help seniors navigate digital services.

**What the Open Payments angle is:** AGING-AI itself isn't about payments. The question is whether it can serve as a front-end for **pushing small subsidies to vulnerable users** through a channel they already use (WhatsApp). Municipalities run micro-subsidy programmes (medication reimbursements, elder-care vouchers, transport discounts). Those programmes today run via bureaucratic processes that exclude the very users they're supposed to help.

**What I'll build:** a proof-of-concept subsidy-distribution flow. A partner municipality or foundation initiates a small transfer to a specific user through the AGING-AI interface; the user receives a notification in WhatsApp; accepts or declines; and if accepted, the transfer lands in the user's wallet.

This is where honesty matters. The research may conclude that Open Payments is not yet ready for this use case (elder users without existing wallets, KYC gaps, language and accessibility issues in wallet UX). If so, the deliverable is a well-documented proof-of-concept plus a written account of exactly what's missing and what would need to happen for the flow to work in a year or two.

**Stack:** Python (FastAPI) on the AGING-AI side (existing), Node module reused from Contestia integration, Rafiki sandbox for development, real wallet provider for the staged pilot.

**Definition of done for month 10:** an end-to-end proof-of-concept runs against the sandbox with at least one real elderly test user, results documented publicly.

## Shared infrastructure

A single public MIT repository (candidate name: `openpay-impact`) holds the reusable integration module, consumed by both Contestia and AGING-AI. That way the technical work produces something any other EU non-profit SaaS could pick up.

## Upstream contributions

Expected signals to file as the work progresses:
- Rafiki sandbox ergonomics (this surfaced in the openpay-kit SDK grant too).
- Open Payments spec ambiguities specific to small-amount, one-off, or recurring flows.
- Kiota integration findings if I end up using the Kiota-built SDK once Arazzo support lands there.
- Wallet provider conformance notes: which EU wallets are ready for Open Payments, which aren't, what's blocking adoption.

All disclosed per Badge AI conventions when AI-assisted.

---

*v0.1, April 2026*
