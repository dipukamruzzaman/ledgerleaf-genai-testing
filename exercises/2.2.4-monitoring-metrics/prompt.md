# HO-2.2.4 — Prompt: test monitoring metrics from test data

```text
ROLE: You are a test manager reporting to the release steering group.

CONTEXT: LedgerLeaf Bank (fictional), Release 1.0.2 system test, week 1 of 1.
Release decision is on Monday. 120 regression tests are planned for the week.
Open defects at the start of the week: 1. Open defects by severity on Friday evening:
Critical 1, Major 3, Minor 4.

INSTRUCTION: From the daily test data below, calculate test monitoring metrics,
identify trends and risks, and recommend test control actions.

INPUT DATA (CSV, daily values, not cumulative):
<paste test-data.csv>

CONSTRAINTS:
- Show how each metric is calculated (formula + numbers).
- Check the data for inconsistencies before using it, and say how you handled them.
- Do not invent data that is not in the input.

OUTPUT FORMAT:
1. Metrics table: | Metric | Formula | Value |
   (execution progress vs plan, pass rate, blocked rate, defects opened vs closed, open defects, remaining tests)
2. Data quality issues found.
3. Top 3 risks.
4. Top 3 test control actions.
5. A 4-line summary for non-technical stakeholders.
6. If you can, a simple chart of planned vs executed per day.
```
