# LedgerLeaf regression suite — Release 1.0.1 (input for HO-2.2.2c)

Context: build 1.0.1 contains the fix for DEF-001 ($5,000.00 transfer rejected).
Risk level = likelihood × impact, agreed with the PO. Durations are for manual execution.

| ID | Test case | Story | Risk | Duration (min) | Depends on |
|---|---|---|---|---|---|
| T01 | Register new customer "Jamie Fox" | US-01 | Medium | 5 | – |
| T02 | Log in as Jamie | US-02 | Medium | 3 | T01 |
| T03 | Account locks after 3 failed log-ins | US-02 | High | 4 | – |
| T04 | Password reset unlocks a locked account | US-03 | High | 6 | T03 |
| T05 | Reset link expires after 30 minutes | US-03 | High | 35 | – |
| T06 | View own accounts and note the balances | US-04 | Low | 2 | – |
| T07 | Accounts API does not return other customers' data | US-04 | Critical | 3 | – |
| T08 | Transfer exactly $5,000.00 (retest DEF-001) | US-05 | High | 3 | – |
| T09 | Transfer more than the available balance is rejected | US-05 | High | 3 | T06 |
| T10 | Jamie (zero balance) cannot transfer $0.01 | US-05 | Medium | 3 | T02 |
| T11 | Memo longer than 140 characters is handled | US-05 | Low | 2 | – |
| T12 | Transfer to the same account is rejected | US-05 | Medium | 2 | – |
