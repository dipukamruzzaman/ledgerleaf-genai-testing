# Regression test specification — LedgerLeaf Release 1.0.2 (20 tests)

| ID | Test case | Story | Risk |
|---|---|---|---|
| TC-01-01 | Register a valid adult customer | US-01 | Medium |
| TC-01-02 | Duplicate email is rejected | US-01 | Medium |
| TC-01-03 | Weak password is rejected | US-01 | Medium |
| TC-01-04 | A 17-year-old cannot register | US-01 | High |
| TC-02-01 | Valid log-in shows the Accounts page | US-02 | High |
| TC-02-02 | Invalid log-in shows one generic error | US-02 | Medium |
| TC-02-03 | Account locks at the 3rd failed attempt | US-02 | High |
| TC-02-05 | A locked account shows the "locked" message | US-02 | Medium |
| TC-03-01 | Same message for an unregistered email | US-03 | High |
| TC-03-02 | Reset link appears in the outbox | US-03 | Medium |
| TC-03-04 | Password reset unlocks a locked account | US-03 | High |
| TC-04-01 | Customer sees own accounts | US-04 | Medium |
| TC-04-02 | Balances use $ and two decimals | US-04 | Low |
| TC-05-01 | Transfer $100.00 succeeds | US-05 | High |
| TC-05-03 | Transfer exactly $5,000.00 succeeds | US-05 | High |
| TC-05-04 | Transfer $4,999.99 succeeds | US-05 | Medium |
| TC-05-08 | Transfer with a memo succeeds | US-05 | Low |
| TC-NAV-01 | Log-out link is shown on the Transfer page | US-02 | Low |
| TC-API-02 | API rejects a negative transfer amount | US-05 | High |
| TC-API-03 | Accounts API requires log-in | US-04 | Critical |
