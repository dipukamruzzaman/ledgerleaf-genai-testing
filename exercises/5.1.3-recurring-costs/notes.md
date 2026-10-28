# HO-5.1.3 — Estimate the recurring costs of GenAI for test tasks

**Syllabus link:** GenAI-5.1.3 · HO-5.1.3 (H1) · **Date:** 2026-10-27

## Assumptions (one QA team, one year)
| Test task | Requests / year | Input tokens / request | Output tokens / request | Input / year | Output / year |
|---|---|---|---|---|---|
| A. Generate test cases (like 2.2.2a) | 110,000 (10 testers × 50/day × 220 days) | 1,200 | 1,500 | 132 M | 165 M |
| B. Nightly regression report analysis (like 2.2.3b) | 220 | 3,000 | 800 | 0.66 M | 0.18 M |
| **Total** | | | | **132.66 M** | **165.18 M** |

## Prices (looked up 2026-10-27 — prices change often)
| Option | Type | Input / 1M tokens | Output / 1M tokens | Source |
|---|---|---|---|---|
| 1. Mistral Large (API) | Commercial, pay per token | $0.50 | $1.50 | mistral.ai/pricing (official FAQ example) |
| 2. Mistral Small (API) | Commercial, pay per token | $0.10–0.15 | $0.30–0.60 | Third-party price lists (not on the official pricing page) — to verify |
| 3. Llama 3.1 8B self-hosted on AWS g5.xlarge (NVIDIA A10G, 24 GB) | Open-source licence, pay per hour | $1.006 / hour (on-demand, us-east-1) | — | doit.com price list |

## Calculation
Pay-per-token: 132.66 × input price + 165.18 × output price
Self-hosted: $/hour × 8 h × 220 days = 1,760 hours (no token fees)

| Option | Yearly cost (USD) |
|---|---|
| 1. Mistral Large | 132.66 × 0.50 + 165.18 × 1.50 = **$314** |
| 2. Mistral Small | **$63 – $119** (depending on the price source) |
| 3. Llama 3.1 8B self-hosted, 8 h/day | 1.006 × 1,760 = **$1,771** (24/7 would be **$8,813**) |

## Hidden / extra recurring costs
- Re-runs because of non-deterministic or wrong output (2.3.2 needed 3 prompt versions).
- Reasoning models: thinking tokens are billed as output (3.1.2b: ~10,000 tokens per request ≈ 6–7× a normal request).
- Self-hosting: maintenance, monitoring, model updates, security patching, staff time.
- **Human review time** — e.g. 2 minutes per request × 110,000 = ~3,700 hours/year; far larger than any token bill.
- Enterprise plans for privacy / no data retention (3.2.3) can change the price model.

## Findings
1. Output tokens dominate the bill: output is priced 3–4× higher than input, and we produce more output than input.
2. At this volume the APIs are much cheaper than self-hosting ($63–$314 vs $1,771 per year).
3. Self-hosting an open-source model is justified by **privacy and control** (3.2.3), not by cost, unless volume is much higher.
4. Model size again multiplies cost: Large ≈ 3–5× Small for the same work (same pattern as energy in 3.3.1).
5. The real recurring cost of GenAI in testing is people: reviewing, correcting and re-running AI output.
6. Prices change frequently and sources disagree — always record the source and date of every price.
