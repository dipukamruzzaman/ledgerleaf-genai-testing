# HO-2.3.1 — Observe: metrics for evaluating GenAI results

**Syllabus link:** GenAI-2.3.1 (K2) · HO-2.3.1 (H0) · **Date:** 2026-10-27
**Input:** ai-output.md (12 AI test cases) scored against reference.md (10 conditions = test oracle)

## Step 1 — Mark each AI test case
| # | Matches Ref | Expected correct? | Duplicate? | Invented? | Note |
|---|---|---|---|---|---|
| 1 | R2 | Y | N | N | |
| 2 | – | Y | N | N | Valid partition, not in reference |
| 3 | R4 | **N** | N | N | Expects 5,000.00 rejected — rule says accepted |
| 4 | R5 | Y | N | N | |
| 5 | R3 | Y | N | N | |
| 6 | R1 | Y | N | N | |
| 7 | R6 | Y | N | N | |
| 8 | R8 | Y | N | N | |
| 9 | R3 | Y | **Y** | N | Duplicate of #5 |
| 10 | – | N (strict) | N | **Y** | Outcome right, reason invented ("daily limit") |
| 11 | – | N | N | **Y** | Invented feature (currency conversion) |
| 12 | R2 | Y | **Y** | N | Duplicate of #1 |

## Step 2 — Metrics
| Metric | How measured | Value |
|---|---|---|
| Recall | Reference conditions covered ÷ 10 (R1–R6, R8) | **70%** — missing R7 (3 decimals), R9 (= balance), R10 (not a number) |
| Accuracy | Correct expected results ÷ 12 | **75%** strict (9/12) · 83% if #10 accepted |
| Precision | Relevant test cases (no invented rule/feature) ÷ 12 | **83%** (10/12) |
| Diversity | Unique test cases ÷ 12 | **83%** (10/12) |
| Relevance / contextual fit | Test cases with invented rules/features | **2** (#10, #11) |
| Time efficiency | AI ~20 s vs human ~20 min | ~60× faster |

My first calculation gave Recall 80% (miscounted distinct references) and expressed Relevance as a % — corrected.

## Step 3 — Most dangerous test case: #3
#3 looks like a perfect boundary test, but its expected result ("5,000.00 rejected") matches the behaviour of
DEF-001. Run against the buggy app it PASSES — hiding the defect. #11 (currency) is obviously wrong and gets caught
in review; #3 is plausible and silently encodes the bug.

## Findings
1. Metrics need a reference (oracle); without one, plausible-looking output feels "correct".
2. Each metric shows a different weakness: recall → missing conditions; diversity → duplicates; relevance → invented rules.
3. A wrong expected result that matches the bug's behaviour is the most dangerous error: it turns a test into a defect-hider.
4. Fast output (60×) is only valuable after evaluation; one run is not enough — metrics should use statistically relevant data.
