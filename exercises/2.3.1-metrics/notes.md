# HO-2.3.1 — Observe: metrics for evaluating GenAI results

**Syllabus link:** GenAI-2.3.1 (K2) · HO-2.3.1 (H0) · **Date:** 2026-10-27
**Input:** ai-output.md (12 AI test cases) scored against reference.md (10 conditions)

## Step 1 — Mark each AI test case
| # | Matches Ref (R1–R10 or –) | Expected result correct? (Y/N) | Duplicate? (Y/N) | Invented rule/feature? (Y/N) |
|---|---|---|---|---|
| 1 | R2 |  Y | N | N |
| 2 | - | Y | N | N |
| 3 | R4 | N | N | N |
| 4 | R5 | Y | N | N |
| 5 |  R3| Y | N | N |
| 6 |  R1 | Y | N | N |
| 7 | R6 |  Y | N | N |
| 8 |  R8| Y | N | N |
| 9 | - |  Y | Y | N |      Duplicate to TC05 "Just below maximum"
| 10 | - | Y | N | Y |      Not mentioned in reference: [daily limit exceeded]
| 11 | - | N | N | Y |      Nothing referenced.
| 12 | R2 | Y | Y | N |     Duplicate of TC01

## Step 2 — Calculate the metrics
| Metric (syllabus) | How we measure it here | Value |
|---|---|---|
| **Recall** | Ref conditions covered ÷ 10 | 80% |
| **Accuracy** | Test cases with a correct expected result ÷ 12 | 10/12=83% |
| **Precision** | Test cases that are relevant (no invented rule/feature) ÷ 12 | 10/12=83% |
| **Diversity** | Unique test cases (not duplicates) ÷ 12 | 10/12=83% |
| **Relevance / contextual fit** | Number of test cases with invented rules or features | 10/12=83% |
| **Time efficiency** | AI ~20 s vs human ~20 min | ~60× faster |

## Step 3 — Which single test case is the most dangerous, and why?
(Hint: think about DEF-001.)
TC011 - NOTHING DOCUMENTED REGARDING THAT. 
## Findings
