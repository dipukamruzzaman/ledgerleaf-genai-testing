# HO-2.2.4 — Observe: test monitoring metrics prepared by GenAI

**Syllabus link:** GenAI-2.2.4 (K3) · HO-2.2.4 (H0) · **Tool:** <chatbot> · **Date:** 2026-10-27

## Spot-check the AI's numbers (calculated by me first)
| Metric | My calculation | AI's value | Match? |
|---|---|---|---|
| Executed vs planned (week) | 90 / 120 = 75% (30 tests behind) | 75% | ✅ |
| Defects opened vs closed (week) | 10 opened / 3 closed | 10 / 3 | ✅ |
| Open defects on Friday | 1 + 10 − 3 = 8 | 8 | ✅ |

## Did the AI notice…
| Insight | Result |
|---|---|
| Wednesday's numbers don't add up (13 + 2 + 1 = 16 ≠ 18 executed) | ✅ Yes — reported as a data quality issue (2 tests unaccounted for) |
| Thursday's 100% pass rate is meaningless (only 7 of 24 ran — CI outage) | ❌ No — reported the outage and a retest need, but did not warn that the 100% is misleading |
| Open-defect backlog is growing (opened > closed) | ✅ Yes — 10 opened vs 3 closed |
| Open defects from the data (8) match the severity breakdown (1+3+4) | ✅ Yes |
| **Score** | **3 / 4** |

## Findings
1. Arithmetic on clean, small data was correct; the prompt's "show the formula" made every number checkable.
2. "Check the data for inconsistencies" worked: Wednesday's gap was found without a hint.
3. The AI reported facts but missed an **interpretation trap**: a 100% daily pass rate from 7 of 24 tests looks like the
   best day of the week, but it is the worst for progress. Ratios must always be read with their denominators.
4. Test control action the human adds: reschedule Thursday's 17 unexecuted tests and the 30 remaining tests; at the
   average rate (18/day) that needs ~2 more days — the Monday decision is at risk.
5. Monitoring metrics are only as good as the input data: always validate the data before trusting the dashboard.
