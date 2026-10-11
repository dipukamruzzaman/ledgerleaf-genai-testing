# HO-1.1.2 — Tokenization, token count and the context window

**Syllabus link:** GenAI-1.1.2 (K2) Explain the basics of generative AI and LLMs · Hands-on HO-1.1.2 (H1)
**System under test:** LedgerLeaf Bank backlog and a synthetic LedgerLeaf regression log
**Tools:** OpenAI Tokenizer (Part A) · Ollama `llama3.2:3b`, temperature 0, seed 42 (Part B) · `tools/context_overflow.py`
**Date:** 2026-10-10

---

## Part A — Token counts

| # | Input | Characters | Tokens | Characters per token |
|---|---|---|---|---|
| 1 | Plain sentence: "The customer cannot transfer more than the available balance." | 62 | 10 | 6.2 |
| 2 | Test data: "Transfer $4,999.99 from 100-001 to 100-002 with password Passw0rd!" | 67 | 24 | 2.8 |
| 3 | US-05 Transfer money (full story) | 579 | 125 | 4.6 |
| 4 | Entire product backlog (`user-stories.md`) | 2,754 | 664 | 4.1 |

### How test data is split

| Value | Approximate split | Tokens |
|---|---|---|
| `$4,999.99` | `$` · `4` · `,` · `999` · `.` · `99` | ~6 |
| `100-001` | `100` · `-` · `001` | ~3 |
| `Passw0rd!` | `Pass` · `w` · `0` · `rd` · `!` | ~5 |

Common English words (`Transfer`, `from`, `with`, `password`) are one token each.

### Part A findings
1. Inputs 1 and 2 are almost the same length, but the test-data line uses **2.4× as many tokens**.
2. The whole backlog is only ~660 tokens and fits any model's context window.
3. Token-heavy input costs more on paid APIs, which bill per input and output token (see HO-5.1.3).

**Conclusion (in my words):** account numbers and amounts are tokenized into odd fragments, so an LLM can garble them.
**Testing practice:** always verify exact values (amounts, account numbers, boundaries) in AI-generated test data.

---

## Part B — Context-window overflow

**Set-up:** one failure (`ERR-4471`) hidden on line 3 of a synthetic regression log. The model is asked to name the failed test and its error code, or answer `NONE`.

### Predictions (written before running)

| Run | Log size (estimate) | num_ctx | Prediction | Actual |
|---|---|---|---|---|
| 1 | 50 lines (~1,600 tokens) | 2,048 | YES | **NO** |
| 2 | 50 lines (~1,600 tokens) | 8,192 | NO → corrected to YES | YES |
| 3 | 200 lines (~6,000 tokens) | 2,048 | NO | NO |
| 4 | 200 lines (~6,000 tokens) | 8,192 | YES | **NO** |
| 5 | 800 lines (~24,000 tokens) | 2,048 | NO | NO |
| 6 | 800 lines (~24,000 tokens) | 8,192 | NO | NO |

Score: 4 of 6. Both misses were caused by underestimating the log's token count.

### Results

| Log lines | num_ctx | Tokens the model read | Found ERR-4471? | Model answer | Seconds |
|---|---|---|---|---|---|
| 50 | 2,048 | 1,026 | NO | NONE | 14.0 |
| 50 | 8,192 | 2,306 | **YES** | test_transfer_to_savings \| ERR-4471 | 39.0 |
| 200 | 2,048 | 1,026 | NO | NONE | 13.2 |
| 200 | 8,192 | 4,098 | NO | NONE | 77.2 |
| 800 | 2,048 | 1,026 | NO | NONE | 12.9 |
| 800 | 8,192 | 4,098 | NO | NONE | 75.2 |
| 200 | 32,768 | 9,031 | **YES** | test_transfer_to_savings \| ERR-4471 | 106.6 |
| 800 | 32,768 | 16,386 | NO | **test_transfers_case_0778** (a PASSED test) | 311.6 |

### Part B findings

1. **The "4 characters per token" rule underestimates test data.** The log measured ~2.7 characters per token
   (~46 tokens per line), matching the 2.8 found in Part A. Estimate for 200 lines: ~9,200 tokens; measured: 9,031.
2. **Only about half the window was used for input.** With num_ctx 2,048 / 8,192 / 32,768 the model read
   1,026 / 4,098 / 16,386 tokens. The rest of the log was dropped from the top — exactly where the failure was.
3. **Truncation was silent.** No error or warning was shown. In 5 runs the model confidently answered `NONE`
   while a real failure existed: a false "all tests passed".
4. **Worse than silence: a hallucinated failure.** In the 800-line / 32,768 run the model named a test that had
   PASSED (`test_transfers_case_0778`) as the failure. It produced a confident, wrong answer (see Chapter 3, hallucinations).
5. **A bigger window costs time.** The same question took 13 s at 2,048 and 312 s at 32,768 on a 16 GB laptop.

### Testing practice (lessons for using GenAI on logs)
- Measure the real token count before trusting an answer; use the model's own count (`prompt_eval_count`).
- Set `num_ctx` large enough for the input, remembering that the usable input may be smaller than the setting.
- Do not paste whole logs: filter first (for example only ERROR/FAILED lines), or split the log and ask in steps (prompt chaining).
- Always verify an AI "no failures" verdict against the test tool's own pass/fail summary.
