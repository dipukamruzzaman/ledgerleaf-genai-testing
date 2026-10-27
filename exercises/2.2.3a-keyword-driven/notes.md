# HO-2.2.3a — Few-shot prompting for keyword-driven test scripts

**Syllabus link:** GenAI-2.2.3 (K3) · HO-2.2.3a (H2) · **Tools:** ChatGPT/Gemini (generation), Ollama llama3.1:8b (debugging), Robot Framework + SeleniumLibrary · **Date:** 2026-10-26

## Part 0 — Verify the few-shot examples first
| Run | Result | Cause |
|---|---|---|
| examples.robot, first run | 1 passed, 1 failed | Race condition in the library: result checked before the page loaded |
| After fix (Wait Until Element Is Visible) | 2 passed | — |
Lesson: few-shot examples are copied faithfully — a bug in an example would have been copied into every generated script.

## Part 1 — Generate, validate, run (transfers.robot)
| Check | Result |
|---|---|
| Scripts generated | 6 (TC-05-03 … TC-05-08) |
| Used only library keywords? | Yes |
| First run | 6 tests: 4 passed, 2 failed |
| TC-05-03 (exactly $5,000.00) | ❌ FAIL — real defect **DEF-001** (expected; now a regression test) |
| TC-05-04 ($4,999.99) | ❌ FAIL — script assumption: AI expected "$4,999.99", app shows "$4999.99" |
| After correcting TC-05-04 | 6 tests: 5 passed, 1 failed (DEF-001) ✅ |

**OBS-001 (question for PO):** the transfer confirmation shows amounts without a thousands separator ("$4999.99"),
while balances use one ("$12,500.00"). Inconsistent formatting — defect or accepted?

Why the TC-05-04 assumption slipped through: the examples only showed $100.00 (no amount ≥ 1,000), and the AI's
self-review (Prompt 2) could not know the real format. Only execution against the app revealed it.

## Part 2 — Debugging assistant (system prompt, llama3.1:8b, temperature 0)
broken.robot contains 5 planted bugs.
| # | Planted bug | Found? |
|---|---|---|
| 1 | `Log In As Demo User` — keyword does not exist | ✅ |
| 2 | Expected balance $12,350.00 — should be $12,250.00 (12,500 − 250) | ❌ (right line, wrong reason: "rounding") |
| 3 | `Transfer Money    10.00    100-001    100-001` — arguments in wrong order | ❌ |
| 4 | `Transfer Should Fail With Choose two…` — single space, keyword and argument merged | ❌ |
| 5 | `Insufficient funds` — missing period (exact match) | ❌ |
| | **Found: 1 / 5 · False alarms: 7** | |

False alarms: "memo argument missing" ×3 (memo is optional), "Log In As Demo Customer is not valid" (it is listed
in the system prompt), "text/balance may vary" ×3.
Harmful fixes: "remove the expected message and only check that the transfer fails" — would weaken the test and hide bug 5.

## Findings
1. Few-shot prompting produced 6 scripts in the house style using only library keywords.
2. Few-shot copies flaws too: examples must be tested before use, and must cover the data ranges you need (amounts ≥ 1,000).
3. AI self-review is not verification; running the scripts against the app found the format assumption.
4. Automation now catches DEF-001 on every run (regression test).
5. A small local model with a system prompt found 1/5 bugs, raised 7 false alarms, contradicted its own system prompt,
   and suggested fixes that weaken assertions. Never accept "make it pass" fixes without review.
6. Robot Framework ignores case and spaces in keyword names ("Login As" = "Log In As") — a typo there is not a bug;
   a tool's rules matter when judging an AI review.
