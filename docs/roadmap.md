# Roadmap

Twelve-month plan for AccessPay. Paired with [proposal.md](proposal.md). The three tracks (research, technical, advocacy) run in parallel, not sequential, at 32 hours per week total.

## Dates

- **Start:** 1 September 2026 (standard Fellowship cohort start).
- **End:** 31 August 2027.
- **Final report:** due 30 September 2027 (30 days after project end).

## Weekly allocation

32 hours per week, split across the three tracks:
- Research: roughly 14 hours per week (about 45%).
- Technical: roughly 13 hours per week (about 40%).
- Advocacy and community: roughly 5 hours per week (about 15%).

Week shape: Mondays and Fridays are research-heavy (interviews tend to cluster in those days in the Spanish third sector), Tuesdays to Thursdays are technical-heavy, Wednesday afternoons reserved for Foundation check-ins and community calls.

## Month-by-month

### M1. September 2026. Framing

- **Research:** literature review (Open Payments academic papers, prior Foundation outputs, adjacent EU third-sector payment research), draft interview guide, ethics and consent templates, pre-registered study design published on the repo.
- **Technical:** bootstrap `openpay-impact` shared module, Rafiki sandbox local via docker-compose, first stub integration in Contestia (behind feature flag, off).
- **Advocacy:** first monthly progress post on the Interledger Community Forum. Attend weekly Program Team check-in.
- **Public output:** repo tag `v0.1`, first monthly post, interview guide v0.1.

### M2. October 2026. First wave prep + OSSEU CFP

- **Research:** shortlist finalised for wave 1 (5 entities), outreach emails sent, first 2 interviews scheduled, interview guide refined.
- **Technical:** Contestia flow candidate selected based on early research signals. Wallet provider shortlist for staging (Interledger test wallet, plus 1-2 EU wallets if available).
- **Advocacy:** monthly post. **OSSEU 2026 CFP submission** if still open, otherwise target 2027 edition.
- **Public output:** `v0.2` tag with wave 1 plan public, consent template published.

### M3. November 2026. Wave 1 fieldwork begins

- **Research:** interviews 1, 2, 3 of wave 1 completed. Raw transcripts in secure storage.
- **Technical:** Contestia integration reaches end-to-end in the Rafiki sandbox. Shared `openpay-impact` module extracted.
- **Advocacy:** monthly post.

### M4. December 2026. Wave 1 ends, first analysis, Progress Report

- **Research:** interviews 4, 5 of wave 1 completed. Analysis of wave 1, first case sketches drafted. Member-checking with interviewees.
- **Technical:** first pilot clinic opt-in for Contestia integration, staging tests with real money small amounts.
- **Advocacy:** monthly post. **Progress Report to the Program Team** (if required mid-year by the grant agreement).
- **Public output:** wave 1 case sketches drafted (shared with interviewees first, not public yet).

### M5. January 2027. Wave 2 begins, Contestia goes live

- **Research:** wave 2 outreach, first 2 interviews done. Interview guide refined based on wave 1 learnings. First non-Spanish interviewee in this wave.
- **Technical:** Contestia integration live in one pilot clinic. First real Open Payments transactions in production (small deposits for appointments, for example).
- **Advocacy:** monthly post. **FOSDEM 2027 attendance** (if talk accepted from M8 submission, delivery is here, see M8).

### M6. February 2027. Contestia post-mortem + community milestone

- **Research:** wave 2 interviews 3, 4, 5 done. First public snippet of findings in a mid-Fellowship blog post.
- **Technical:** Contestia post-mortem written and published: what worked, what broke, what's still rough about Open Payments developer experience in production.
- **Advocacy:** monthly post. Mid-Fellowship community engagement (host or co-host one Interledger community call on findings to date).
- **Public output:** Contestia integration post-mortem published; mid-Fellowship check-in post.

### M7. March 2027. Wave 3 prep, AGING-AI integration begins

- **Research:** wave 2 analysis, saturation-check decision, refined research framework. Wave 3 outreach targeting pan-European entities, at least 2 non-Spanish confirmed.
- **Technical:** AGING-AI integration scoping with DKV pilot team. First proof-of-concept subsidy flow against Rafiki sandbox.
- **Advocacy:** monthly post.

### M8. April 2027. Wave 3 fieldwork + FOSDEM CFP

- **Research:** 3 of 5 wave 3 interviews done.
- **Technical:** AGING-AI PoC end-to-end in sandbox. First real elderly test user in a controlled staging environment.
- **Advocacy:** monthly post. **FOSDEM 2028 CFP submission** for a post-Fellowship talk.

### M9. May 2027. Saturation check, AGING-AI live test

- **Research:** wave 3 complete. Saturation assessment, possible 1 or 2 additional interviews if key perspectives are missing. Cross-case analysis begins.
- **Technical:** AGING-AI integration staged with 5 real elderly test users. Results documented transparently including what's not ready yet.
- **Advocacy:** monthly post.

### M10. June 2027. Drafting

- **Research:** findings paper first full draft. Peer review requests sent to 2 to 3 Interledger reviewers and 2 to 3 third-sector reviewers.
- **Technical:** AGING-AI real-world test completed, document findings on what's ready and what isn't.
- **Advocacy:** practitioner's guide drafted, English version first.
- **Public output:** findings paper draft shared with reviewers.

### M11. July 2027. Refining

- **Research:** findings paper v2 based on reviewer feedback. Spanish translation begins.
- **Technical:** AGING-AI final documentation. `openpay-impact` module tagged v1.0.0.
- **Advocacy:** practitioner's guide polished, Spanish translation.
- **Public output:** findings paper ready for publication, `openpay-impact` 1.0.0 released.

### M12. August 2027. Publish and close out

- **Research:** findings paper published (CC BY-SA), English and Spanish versions. Case sketches publicly archived on the repo.
- **Technical:** upstream contributions filed to Rafiki, OpenAPI, Arazzo, or Kiota based on what surfaced during the year. Repo tagged `v1.0.0`.
- **Advocacy:** practitioner's guide published. If FOSDEM 2027 talk was delivered in February, the Fellowship wraps with a final community engagement (recorded Interledger community session or blog post retrospective).
- **Public output:** final report to the Foundation 30 days after project end (due 30 September 2027).

## Budget split ($20K project stipend)

Allocated per the seven approved categories in the Fellowship program guide:

| Category | Allocation | Notes |
|---|---|---|
| Books, Toolkits, and Research | $3,500 | Academic paper access, Spanish-English translation services, interview transcription (Otter.ai or similar), analysis tools, compliance and regulatory database access. |
| Microgrants and Pilot Projects | $4,500 | Field research expenses (travel to 2-3 entities for in-person interviews), user testing compensation for AGING-AI PoC, small-scale pilot materials. |
| Professional Services and Skill Development | $2,500 | Research ethics expert review, EU compliance expert consultation for AGING-AI subsidy flows, peer-review support for the findings paper. |
| Conferences and Seminars | $5,000 | FOSDEM 2027 travel and lodging, Open Source Summit Europe 2026 travel and lodging, registration fees, travel insurance, visa fees where applicable. |
| Tools and Equipment | $2,500 | High-performance laptop (loan basis per program policy), returnable at Fellowship end with option to purchase at market value. |
| Marketing and Awareness | $1,500 | Video production for the demo walkthrough of the integrations, content development illustration for the practitioner's guide, ILF merchandise coordinated through the ILF team. |
| Events | $500 | Contribution to a community gathering or co-hosted session if the opportunity surfaces. |
| **Total** | **$20,000** | |

## Reporting cadence

- **Weekly** check-ins with the Program Team (video call).
- **Monthly** public progress post on the Interledger Community Forum, mirrored in #cfp-sdk where relevant.
- **Monthly** short update to the Program Officer, same content reformatted.
- **Quarterly** slightly longer check-in (months 3, 6, 9) covering pace, risks, and budget review.
- **Mid-Fellowship** public check-in post at month 6.
- **Final report** due 30 September 2027 (30 days after 31 August 2027 end).

## Public-first

The repo is public from day one. All commits, proposal drafts, research notes (anonymised where required by consent), technical work, and advocacy materials live in the open. Every upstream PR is disclosed per Badge AI conventions. This aligns with the Foundation's emphasis on observable, community-facing work.

---

*v0.2, April 2026*
