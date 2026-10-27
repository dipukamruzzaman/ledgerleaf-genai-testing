# HO-2.2.2a — Functional test cases for US-05 (chaining + structured + meta)

Use ONE chat (ChatGPT or Gemini) for steps 1–2. Step 3 can be a new chat.

---

## Step 1 — Structured prompt: generate functional test cases
```text
ROLE: You are a senior test analyst for online-banking web applications.

CONTEXT: LedgerLeaf Bank is a fictional bank used for test practice. Release 1.0 is in
system test. Demo customer: alex.tester@ledgerleaf.test / Passw0rd!, who owns
Chequing 100-001 (balance $12,500.00) and Savings 100-002 (balance $800.00).
Another customer owns account 100-003.

INSTRUCTION: Design functional test cases for the user story below. Use equivalence
partitioning and boundary value analysis on the amount.

INPUT – User story US-05 Transfer money
As a logged-in customer, I want to transfer money from my account to another LedgerLeaf
account so that I can move or pay money quickly.
AC1 The customer chooses one of their own accounts, enters the destination account number and an amount.
AC2 Transfers are allowed up to $5,000.00 per transfer (inclusive). There is no daily limit.
AC3 The amount must be at least $0.01 and have at most two decimal places.
AC4 The customer cannot transfer more than the available balance.
AC5 A confirmation with a reference number is shown after a successful transfer.
AC6 An optional memo (max 140 characters) can be added.
AC7 A transfer to the same account, or to an account number that does not exist, is rejected.

CONSTRAINTS:
- Use only the rules above. Do not invent requirements.
- Use exact amounts and account numbers from the context.
- At most 15 test cases.

OUTPUT FORMAT: Markdown table
| ID | Title | Preconditions | Steps | Test data | Expected result | AC |
```

---

## Step 2 — Chaining: verify coverage
```text
Create a coverage table for the test cases above:
| AC | Test case IDs that cover it | Covered? (Yes/Partly/No) | What is missing |
Then list any test case that does not trace to an AC.
If an AC is not fully covered, propose the missing test cases in the same format as before.
```

---

## Step 3 — Meta prompting: a prompt for an end-to-end test procedure
```text
I want an LLM to write an end-to-end test procedure for LedgerLeaf Bank covering this
journey: log in → check balances → transfer money → verify confirmation and new balances
→ log out. Write the best possible structured prompt (role, context, instruction, input
data, constraints, output format) for this task. Then ask me 3 questions that would help
you improve the prompt.
```
Answer its 3 questions, ask it to update the prompt, then RUN the final prompt.
