# AccessPay Fellowship

> Deploying Open Payments in the non-profit and digital-inclusion sector in the EU. Research, technical integrations, and advocacy.

**Status:** proposal stage for the Interledger Foundation [2026 Fellowship Program](https://github.com/interledger/Grants/wiki/Fellowship).

## What this is

A 12-month Fellowship project, September 2026 to August 2027, at 32 hours per week. Three tracks running in parallel:

- **Research (about 14 hours per week, 45%)**: a structured study of how Open Payments can land in the European non-profit and digital-inclusion sector. Interviews with 10 to 15 entities (municipalities, foundations, patient associations, digital rights groups), a public findings paper in English and Spanish, and per-case sketches of where Open Payments would unlock value.
- **Technical work (about 13 hours per week, 40%)**: two working integrations of Open Payments in production SaaS already running in the Spanish non-profit sector. [Contestia](https://contestia.co) (WhatsApp AI receptionist for health clinics) and AGING-AI (digital inclusion pilot for elderly users in the Vallès, co-funded by DKV Impacta 2026).
- **Advocacy (about 5 hours per week, 15%)**: two conference talks (FOSDEM 2027, Open Source Summit Europe 2026, or an NLnet/NGI event), plus a public practitioner's guide documenting what we learned integrating Open Payments in production impact-focused software.

## Why this

The European non-profit and digital-inclusion sector runs on payment rails that don't serve it well. Donations go through closed-source gateways with high fees. Micropayments for small services are economically unviable. Cross-border transfers between partner NGOs are slow and manual. Meanwhile Open Payments exists, is open, and nobody is deploying it in this space.

There are two reasons nobody is. First, there's no playbook: research gaps (what's the opportunity actually look like in the EU third sector?) and technical gaps (how do you plug Open Payments into an existing health/inclusion product?). Second, there's no bridge: the Interledger ecosystem and the European impact-focused non-profit ecosystem don't overlap much today. The fellowship is an attempt to start closing both gaps.

## Repository layout

```
accesspay-fellowship/
├── docs/
│   ├── proposal.md              Fellowship application draft
│   ├── research-plan.md         Research methodology, entity shortlist, outputs
│   ├── technical-plan.md        Contestia and AGING-AI integration plans
│   ├── advocacy-plan.md         Talks, guide, community engagement plan
│   ├── roadmap.md               12-month milestones, reporting cadence
│   └── ai-use.md                AI disclosure (Badge AI + prompt log)
└── .github/
    ├── workflows/ci.yml
    └── PR_TEMPLATE.md
```

## License

MIT © Basics Tech · Infinite Labs OÜ.

## Contact

Diego Torres · diego@pdata.org · [BasicsTech.org](https://basicstech.org) · [GitHub](https://github.com/diegotorreslopez81)
