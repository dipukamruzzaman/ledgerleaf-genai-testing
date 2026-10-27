# HO-2.3.2 — A/B test two prompts, then refine iteratively

Run in Ollama:  ollama run llama3.1:8b   →   /set parameter temperature 0
Use /clear between prompts. Wrap each prompt in """ … """.

---

## Prompt A — base version
```text
Write boundary value test cases for the transfer amount of a banking app.
The maximum transfer is $5,000.
```

---

## Prompt B — structured version
```text
ROLE: You are a senior test analyst for online-banking applications.

CONTEXT: LedgerLeaf Bank (fictional). Customer accounts: Chequing 100-001 with $12,500.00,
Savings 100-002 with $800.00.

INSTRUCTION: Design test cases for the transfer AMOUNT using equivalence partitioning and
boundary value analysis.

INPUT – rules for the amount:
- Minimum $0.01.
- Maximum $5,000.00 per transfer, inclusive (exactly $5,000.00 is allowed). No daily limit.
- At most two decimal places.
- Cannot exceed the balance of the source account.

CONSTRAINTS:
- Cover every valid and invalid partition and every boundary exactly once — no duplicates.
- Use only these rules; do not invent other rules or features (no currencies, no fees).
- State the source account for every test.

OUTPUT FORMAT: | ID | Test condition | Amount | From account | Expected (Accepted/Rejected) |
```

---

## Prompt B2 — your refinement (iterative prompt modification)
After scoring B, copy Prompt B and add ONE or TWO lines to fix what was missing or wrong
(output analysis → refine). Example: "Also include a non-numeric amount and an amount exactly
equal to the source balance." Run it and score again.
