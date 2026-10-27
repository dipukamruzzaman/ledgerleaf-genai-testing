# Reference set (test oracle) — US-05 transfer AMOUNT, 10 test conditions
Written by a senior tester. Demo data: Chequing 100-001 $12,500.00 · Savings 100-002 $800.00.
Rules: min $0.01 · max $5,000.00 per transfer (inclusive) · max 2 decimals · not more than balance.

| Ref | Test condition | Example value | Expected |
|---|---|---|---|
| R1 | Below minimum | 0.00 | Rejected |
| R2 | Minimum | 0.01 | Accepted |
| R3 | Just below maximum | 4,999.99 | Accepted |
| R4 | Maximum (inclusive) | 5,000.00 | Accepted |
| R5 | Just above maximum | 5,000.01 | Rejected |
| R6 | Negative amount | -1.00 | Rejected |
| R7 | More than 2 decimals | 10.005 | Rejected |
| R8 | More than balance | 800.01 from Savings | Rejected |
| R9 | Exactly the balance | 800.00 from Savings | Accepted |
| R10 | Not a number | abc | Rejected |
