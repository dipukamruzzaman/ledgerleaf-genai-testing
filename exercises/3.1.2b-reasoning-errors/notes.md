# HO-3.1.2b — Experiment with reasoning errors (test effort estimation)

**Syllabus link:** GenAI-3.1.2 · HO-3.1.2b (H1) · **Models:** llama3.2:3b (SLM), llama3.1:8b (LLM), deepseek-r1:8b (reasoning), temperature 0 · **Date:** 2026-10-27
V1 = plain question · V2 = "work step by step, check every calculation"

## Correct answer (calculated by me — the oracle)
| Step | Calculation | Result |
|---|---|---|
| PERT T1–T4 | 7 + 11 + 17 + 9 | 44 h |
| T5 | 50% of T4's PERT estimate (9) | 4.5 h |
| Total + 20% contingency | 48.5 × 1.2 | **58.2 h** |
| Working days | 58.2 ÷ 12 h/day = 4.85 → round up | **5 days** |
| Finish date | Mon 2, Tue 3, (Wed 4 offsite), Thu 5, Fri 6, Mon 9 | **Monday 9 November 2026** |

## Results
| Value | Correct | 3b V1 | 3b V2 | 8b V1 | 8b V2 | r1 V1 | r1 V2 |
|---|---|---|---|---|---|---|---|
| Total effort (h) | 58.2 | 58 ✅ | 58 ✅ | 58 ✅ | 63 ❌ | no clear answer | no clear answer |
| Working days | 5 | 6 ❌ | 4 ❌ | 5 ✅ | – | – | – |
| Finish date | Mon 9 Nov | 12 Nov ❌ | 5 Nov ❌ | 6 Nov ❌ | 6 Nov ❌ | – | – |
| Time to answer | – | 25 s | 18 s | 15 s | 22 s | ~8 min | ~36 min |
| **Fully correct?** | | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

## Where it went wrong (first error)
- 3b V1: days 6 — wrong capacity/rounding step; finish date off by days.
- 3b V2: days 4 — rounded 4.85 **down** instead of up; finish date 5 Nov.
- 8b V1: hours and days correct, but finish date 6 Nov — **ignored the offsite day**.
- 8b V2: total 63 h — step-by-step introduced an arithmetic error; date also ignored the offsite.
- deepseek-r1 (reasoning): after `--hidethinking`, `num_ctx 8192` and a forced FINAL line, still no usable answer
  in 8 min (V1) and 36 min (V2).

## Findings
1. **No model produced the fully correct plan.** The arithmetic (PERT, contingency) was mostly right; the
   **logic steps** — rounding up, applying the offsite day to the calendar — failed.
2. Every model that gave a date ignored or mishandled the non-working day: calendar reasoning is a weak point.
3. "Work step by step and check" (V2) did **not** help: the 8b model got worse (63 h instead of 58).
4. The reasoning model was impractical on a 16 GB laptop: long thinking, 8–36 minutes, no clear final answer.
   Reasoning models reduce, but do not remove, reasoning errors — and cost much more time and tokens.
5. Test planning numbers from AI must be recalculated by a human (or a spreadsheet) before use.
