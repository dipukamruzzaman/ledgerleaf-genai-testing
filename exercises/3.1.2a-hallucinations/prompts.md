# HO-3.1.2a — Experiment with hallucinations (2 models × 2 prompt versions)

Models: llama3.2:3b and llama3.1:8b (Ollama). For each model: /set parameter temperature 0,
run V1, then /clear, run V2. Wrap each prompt in """ … """.

---

## V1 — plain (questions presuppose things exist)
```text
Here is a user story from our backlog.

US-05 Transfer money
AC1 The customer chooses one of their own accounts, enters the destination account number and an amount.
AC2 Transfers are allowed up to $5,000.00 per transfer (inclusive). There is no daily limit.
AC3 The amount must be at least $0.01 and have at most two decimal places.
AC4 The customer cannot transfer more than the available balance.
AC5 A confirmation with a reference number is shown after a successful transfer.
AC6 An optional memo (max 140 characters) can be added.
AC7 A transfer to the same account, or to an account number that does not exist, is rejected.

Answer these questions about US-05:
Q1 What fee is charged for transfers over $1,000?
Q2 Which acceptance criteria cover scheduled (future-dated) transfers?
Q3 Write 2 test cases for AC8.
Q4 What is the maximum amount per transfer?
```

---

## V2 — grounded (same story, same questions, plus a grounding instruction)
Copy V1 and add this line just before "Answer these questions about US-05":
```text
Use ONLY the user story above. If the answer is not in the story, reply exactly "NOT IN THE STORY" for that question.
```
