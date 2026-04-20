# AI Use Disclosure

> Required by the Interledger Foundation AI policy.
> Policy reference: https://docs.google.com/document/d/1gpln1E3NKQSaxoD1yza02ZeniIuBs6rfETyYDWJYPm4/edit

The living record of how generative AI is used in this fellowship. Updated on every release and on every PR that includes AI-assisted output.

## Badge AI

Designations per the [Badge AI](https://badgeai.org) scheme, updated at each release:

- Research and exploration (literature review, desk work): AI-used.
- Interview analysis and coding: AI-assisted, human-reviewed (human does coding, AI helps with thematic aggregation).
- Research paper drafting: AI-assisted, human-reviewed.
- Technical implementation (Contestia and AGING-AI integrations): AI-assisted, human-reviewed.
- Documentation and guide: AI-assisted, human-reviewed.
- Upstream PRs to Rafiki, Open Payments, Arazzo, Kiota: AI-assisted, disclosed per-PR, 100% human-reviewed before submission.

## Models in use

| Model | Provider | Role | Period |
|---|---|---|---|
| Claude Opus 4.7 | Anthropic | Drafting, review, code synthesis, spec reading, interview analysis support | From April 2026 |

New models or major version changes get added here with a dated note.

## Responsibility

I take 100% responsibility for every line of code, documentation, research finding, and PR filed out of this fellowship. AI is used to compress iteration time and surface patterns, not to stand in for capability or judgement. Every AI-assisted artefact is read, understood, and edited by me before it lands.

For research specifically: AI never substitutes for the interview itself, the coding decisions, or the interpretation. It helps aggregate across transcripts, spot recurring themes, and catch grammar. Every finding is traceable to a human decision.

## Prompt log

Prompts that materially shaped committed artefacts go into `docs/prompt-log/`, one file per day, append-only. Each entry has:

- Date
- Model and version
- What it touched (file path, PR link, commit SHA, or finding ID)
- The prompt text
- A one-line note on what I changed before committing

Retention: kept for the full 12-month fellowship window, linked from the final report to the Foundation.

## How PRs are disclosed

Every upstream pull request (into Rafiki, OpenAPI, Arazzo, Kiota, etc.) includes a footer like:

```
AI disclosure: AI-assisted. Drafted with Claude Opus 4.7, human-reviewed before submission.
Prompt log: https://github.com/diegotorreslopez81/accesspay-fellowship/blob/main/docs/prompt-log/<date>.md
```

## How research publications are disclosed

The findings paper and case sketches carry a disclosure paragraph in the methodology section: which models were used, for what tasks, and the prompt log URL. Follows the same transparency principle as the PRs.

## Review protocol

Before any commit or publication that includes AI output:

1. Read every line top to bottom. If something doesn't land, rewrite.
2. For anything that touches spec interpretation or research findings, cross-check against the source (RFC, interview transcript, or primary source).
3. For code: run it locally against the sandbox. AI-generated code that hasn't been executed doesn't get merged.
4. For research: every claim is traceable to a specific transcript or document. AI can help spot patterns, but attribution and interpretation are human.
5. For documentation: read aloud. If a sentence doesn't sound like something I'd actually say, rewrite.

## Changes to this policy

Material changes are logged in the project changelog and referenced in the next monthly report to the Foundation.

---

*v0.1, April 2026*
