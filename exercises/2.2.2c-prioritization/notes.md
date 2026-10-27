# HO-2.2.2c — Prompt chaining for test prioritization

**Syllabus link:** GenAI-2.2.2 (K3) · HO-2.2.2c (H2) · **Tool:** <chatbot> · **Date:** <date>
**Input:** test-suite.md (12 tests, 71 min total, risks + dependencies)

## Step 1 — Risk-based order
| Check | Result |
|---|---|
| Rank 1 test (should be the only Critical one) |  Only T07 listed, T03 and T05 should be listed there as well|
| Dependency violations? (test listed before what it depends on) — which? | Yes T09 listed before T06 |

## Step 2 — Dependency-aware order
| Check | Result |
|---|---|
| All dependencies respected? | yes |
| Tests "pulled forward" (which?) | Yes T06 |

## Step 3 — 60-minute time-box
| Check | Result |
|---|---|
| Tests selected (IDs) | T07, T08, T03, T04, T06, T09, T01, T02, T10, T12, T11 |
| AI's final total (min) |36 minutes  |
| My recalculated total (min) | 36 minutes |
| Arithmetic correct? | Yes |
| Deferred tests (IDs) | T05 |
| Did the AI notice that T05 is mostly *waiting* (35 min) and could run in parallel? | It did and added as additional context: Active Execution Time (All 12 tests): $36 \text{ min (11 tests)} + 5 \text{ min active (T05)} = 41 \text{ minutes}$. |

## Findings
