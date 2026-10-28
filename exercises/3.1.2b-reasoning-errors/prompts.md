# HO-3.1.2b — Experiment with reasoning errors in a test planning task

Models (three types): llama3.2:3b (small LM) · llama3.1:8b (LLM) · deepseek-r1:8b (reasoning model).
For each model: /set parameter temperature 0, run V1, /clear, run V2. Wrap prompts in """ … """.
deepseek-r1 "thinks" first — it is slow; give it a few minutes.

---

## V1 — plain
```text
We are planning testing for LedgerLeaf Release 1.1 (Payees) and need an effort estimate.

Use three-point (PERT) estimation: E = (Optimistic + 4 × Most likely + Pessimistic) / 6.

Tasks (hours):
- T1 Test analysis:   O=4, M=6,  P=14
- T2 Test design:     O=6, M=10, P=20
- T3 Test automation: O=8, M=15, P=34
- T4 Test execution:  O=5, M=8,  P=17
- T5 Regression re-run after fixes: 50% of the PERT estimate of T4

Add 20% contingency to the total of T1–T5.
The team has 2 testers, each with 6 productive hours per day; work can be shared freely.
Testing starts on Monday 2 November 2026. Wednesday 4 November is a team offsite (no testing).
Count only Monday–Friday as working days.

What is the total estimated effort in hours (with contingency), how many working days are needed,
and on which date will testing finish?
```

---

## V2 — step by step + self-check
Copy V1 and add at the end:
```text
Work step by step: show the PERT calculation for each task, then the total, the contingency,
the number of working days (round up to whole days), and the calendar day by day.
Then check every calculation once more before giving the final answer.
```
