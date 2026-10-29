# HO-4.1.2 — Experiment with RAG: "ask the requirements"

**Syllabus link:** GenAI-4.1.2 · HO-4.1.2 (H1) · **Tool:** tools/rag_backlog.py · **Models:** nomic-embed-text (embeddings), llama3.1:8b (answers) · **Date:** 2026-10-28
**Knowledge base:** docs/requirements/user-stories.md + docs/requirements/po-clarifications.md

Test the two halves separately: **Retrieval** (did it fetch the right chunk?) and **Generation** (is the answer right and grounded?).

## Oracle — what a correct answer must say
| Q | Question | Correct answer | Right source to retrieve |
|---|---|---|---|
| 1 | Maximum transfer amount | $5,000.00 **per transfer**, inclusive, no daily limit (story says "daily" — clarification wins) | US-05 + Clarifications for US-05 |
| 2 | Age to open an account | 18 or older (story only says "adults") | Clarifications for US-01 |
| 3 | Failed log-ins before lock | 3 consecutive | Clarifications for US-02 |
| 4 | How many payees | NOT FOUND (not in these documents) | — |
| 5 | Transfer fee | NOT FOUND (no fee exists) | — |
| 6 | Reset link validity | 30 minutes, single use | Clarifications for US-03 |

## Results — R = right chunk retrieved? (Y/N) · A = answer correct? (✅ / ❌ / ⚠️ partly)
| Q | Run 1: sections, top-3 — R | Run 1 — A | Run 2: 200 chars, top-1 — R | Run 2 — A |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |
| **Score (A ✅ of 6)** | | | | |

## Special checks
| Check | Result |
|---|---|
| Q1: did it say "daily limit" (old story) or "per transfer" (clarification)? Did it notice the conflict? |  |
| Q4/Q5: did it answer NOT FOUND, or invent a number? |  |
| Did every answer cite a source in [brackets]? Was the cited source really the one that says it? |  |

## Findings
