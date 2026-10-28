# HO-4.1.3 — Observe an LLM-powered agent automating a repetitive test task

**Syllabus link:** GenAI-4.1.3 · HO-4.1.3 (H0) · **Agent:** tools/transfer_agent.py · **Model:** llama3.1:8b (Ollama, temperature 0) · **Date:** 2026-10-28
Agent = LLM + tools + loop. The LLM DECIDES (which tool, which arguments, what is expected); Python EXECUTES (real API calls).
Tools: `reset_data()` and `transfer(amount)` → POST /api/transfers (100-001 → 100-002).

## Run 1 — open task ("test the US-05 amount rules")
| Observation | Result |
|---|---|
| Steps until final report | 1 |
| Amounts tested | 0.01 only |
| reset_data before each transfer? | Never called |
| Found DEF-001 / negative amount? | No — never tested them |
| Final report | One sentence: "The transfer of $0.01 was accepted" — no table, no defects |
| Stopped by itself? | Yes — **premature termination**: declared success after one easy test |

## Run 2 — guided (explicit list of 8 amounts, "don't report until all 8 are tested")
All 15 tool calls were issued in **one step** (batched): the agent planned everything up front instead of
looking at each result before deciding. The first transfer ran before the first reset.

| Amount | Correct expected (US-05) | Actual (tool log) | Agent's expected | Agent's verdict | Correct verdict |
|---|---|---|---|---|---|
| 0.00 | 400 (min 0.01) | **201** | 201 ❌ | Pass | **FAIL – zero accepted** |
| 0.01 | 201 | 201 | 201 | Pass | Pass |
| 4999.99 | 201 | 201 | 201 | Pass | Pass |
| 5000.00 | 201 (inclusive) | **400** | 400 ❌ | Pass | **FAIL – DEF-001** |
| 5000.01 | 400 | 400 | 400 | Pass | Pass |
| -1 | 400 | **201** | 400 | Fail ✅ | **FAIL – negative accepted (DEF-004)** |
| 10.005 | 400 (max 2 decimals) | **201** (silently rounded to 10.00) | 201 ❌ | Pass | **FAIL – new defect** |
| 12500.01 | 400 | 400 | 400 | Pass | Pass (but rejected by the max rule — the balance rule was never really tested) |
| **Defects** | | | | **1 reported** | **4 real** |

The raw tool log was 100% accurate — the errors are all in the LLM's **expected results** (its judgement), even though
the system prompt said explicitly "exactly 5000.00 must be accepted".

## New defect found
**DEF-005 — API silently rounds amounts with more than two decimals** (10.005 → 10.00, HTTP 201); US-05 AC3 says
such amounts must be rejected. (Zero amount accepted via the API is part of DEF-004.)

## Findings
1. With an open goal, the small agent stopped after one easy test — premature termination.
2. A concrete plan (explicit test list) made the agent execute every test — the same fix as 2.3.2.
3. The agent batched all actions in one step, so it never reacted to results — not a real observe-and-decide loop.
4. **The agent hid 3 of 4 real defects** by setting its own wrong expected results (zero, 5,000.00, 3 decimals) —
   the oracle problem again (2.3.1 #3, 4.2.1 example 4).
5. Tools are deterministic and trustworthy; the LLM's judgement is not. Keep the oracle (expected results)
   outside the LLM — e.g. a fixed reference table — and let the agent only execute and report.
6. Even a correct test design can miss a rule: 12,500.01 hits the max rule first, so the balance rule needs
   an amount ≤ 5,000 above the balance (e.g. 800.01 from savings).
