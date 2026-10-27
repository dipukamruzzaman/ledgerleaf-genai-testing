# AI-generated test cases — US-05 transfer amount (output to evaluate)

| # | Test | Amount | From | Expected result |
|---|---|---|---|---|
| 1 | Minimum amount | 0.01 | 100-001 | Accepted |
| 2 | Typical amount | 100.00 | 100-001 | Accepted |
| 3 | Maximum amount | 5,000.00 | 100-001 | Rejected – exceeds the limit |
| 4 | Just above maximum | 5,000.01 | 100-001 | Rejected – exceeds the limit |
| 5 | Just below maximum | 4,999.99 | 100-001 | Accepted |
| 6 | Zero amount | 0.00 | 100-001 | Rejected |
| 7 | Negative amount | -50.00 | 100-001 | Rejected |
| 8 | More than balance | 800.01 | 100-002 | Rejected – insufficient funds |
| 9 | Upper boundary check | 4,999.99 | 100-001 | Accepted |
| 10 | Large transfer | 10,000.00 | 100-001 | Rejected – daily limit exceeded |
| 11 | Foreign currency | 100.00 EUR | 100-001 | Accepted and converted to CAD |
| 12 | Smallest possible amount | 0.01 | 100-001 | Accepted |
