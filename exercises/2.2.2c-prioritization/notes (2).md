# HO-2.2.2c — Prompt chaining for test prioritization

**Syllabus link:** GenAI-2.2.2 (K3) · HO-2.2.2c (H2) · **Tool:** <chatbot> · **Date:** 2026-10-26
**Input:** test-suite.md (12 tests, 71 min total, risks + dependencies) · **Budget:** 60 minutes

## Step 1 — Risk-based order
| Check | Result |
|---|---|
| Rank 1 test | T07 — correct, it is the only Critical test (T03/T05 are High) |
| Dependency violations? | Yes — T09 ranked before T06 (T09 depends on T06) |

## Step 2 — Dependency-aware order
| Check | Result |
|---|---|
| All dependencies respected? | Yes |
| Tests "pulled forward" | T06 (Low) pulled forward for T09 (High) |

## Step 3 — 60-minute time-box
| Check | Result |
|---|---|
| Tests selected | T07, T08, T03, T04, T06, T09, T01, T02, T10, T12, T11 |
| AI's total / my total | 36 / 36 min — arithmetic correct |
| Deferred | T05 (High risk, 35 min) |
| Strategy followed? | ❌ No. It deferred a High-risk test and ran Medium/Low ones instead (maximised test count, not risk), leaving 24 min unused |
| T05 waiting time noticed? | Yes, in a side note: start T05, run all others during the wait → all 12 in ~41 min. But the recommendation still deferred T05 — explanation contradicts decision |
| Assumption flagged? | No — "5 min active" for T05 was assumed, not given |

## Better plan (tester)
Start T05 first (generate the reset link, start the 30-minute clock), then run in risk/dependency order during the wait:
T07 → T03 → T04 → T08 → T06 → T09 → T12 → T01 → T02 → T10 → T11, then finish T05 at ~30–35 min.
All 12 tests in ~41 min (if T05 really has ~5 min of active work) — nothing deferred.
Strict risk-based alternative without parallelism: Critical + High (56 min) + T12 + T11 = 60 min; defer T01, T02, T10 (Medium).

## Findings
1. Chaining worked as designed: step 1 broke a dependency (T09 before T06), step 2 fixed it and pulled T06 forward.
2. Arithmetic was correct — but correct numbers do not mean correct reasoning.
3. The time-box decision contradicted the chosen strategy: a High-risk test was deferred for Low-risk ones.
4. The LLM's own explanation contained the better plan (parallel waiting) but its recommendation ignored it.
5. My first check wrongly expected T03/T05 at rank 1 — always re-read the input data before judging the AI.
6. Bonus for later: T05 will likely FAIL when executed (the reset link may never expire) — a candidate defect.
