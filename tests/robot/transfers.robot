*** Settings ***
Documentation     Automated test suite for US-05 transfers in LedgerLeaf Bank.
Resource          resources/ledgerleaf.resource
Suite Setup       Open LedgerLeaf
Suite Teardown    Close LedgerLeaf
Test Setup        Reset Demo Data

*** Test Cases ***
TC-05-03 Transfer exactly 5000.00 from 100-001 to 100-002 succeeds (retest of DEF-001)
    [Documentation]     US-05 — transferring exactly $5,000.00 succeeds (retest of DEF-001) and updates both balances.
    [Tags]              US-05     DEF-001     smoke
    Log In As Demo Customer
    Transfer Money      100-001     100-002     5000.00
    Transfer Should Succeed     Transferred $5,000.00 from 100-001 to 100-002
    Balance Should Be   100-001     $7,500.00
    Balance Should Be   100-002     $5,800.00

TC-05-04 Transfer 4999.99 succeeds
    [Documentation]     US-05 — transferring $4,999.99 succeeds and updates both balances correctly.
    [Tags]              US-05     boundary
    Log In As Demo Customer
    Transfer Money      100-001     100-002     4999.99
    # OBS-001: confirmation has no thousands separator, unlike balances – asked PO
    Transfer Should Succeed     Transferred $4999.99 from 100-001 to 100-002
    Balance Should Be   100-001     $7,500.01
    Balance Should Be   100-002     $5,799.99

TC-05-05 Transfer 5000.01 is rejected with "The maximum per transfer is $5,000.00."
    [Documentation]     US-05 — transferring $5,000.01 is rejected with the maximum limit message and balances remain unchanged.
    [Tags]              US-05     negative     boundary
    Log In As Demo Customer
    Transfer Money      100-001     100-002     5000.01
    Transfer Should Fail With     The maximum per transfer is $5,000.00.
    Balance Should Be   100-001     $12,500.00
    Balance Should Be   100-002     $800.00

TC-05-06 Transfer from 100-001 to 100-001 is rejected with "Choose two different accounts."
    [Documentation]     US-05 — transferring to the same account is rejected and balances remain unchanged.
    [Tags]              US-05     negative
    Log In As Demo Customer
    Transfer Money      100-001     100-001     100.00
    Transfer Should Fail With     Choose two different accounts.
    Balance Should Be   100-001     $12,500.00
    Balance Should Be   100-002     $800.00

TC-05-07 Transfer to 100-999 is rejected with "The destination account does not exist."
    [Documentation]     US-05 — transferring to a non-existent destination account is rejected and balances remain unchanged.
    [Tags]              US-05     negative
    Log In As Demo Customer
    Transfer Money      100-001     100-999     100.00
    Transfer Should Fail With     The destination account does not exist.
    Balance Should Be   100-001     $12,500.00
    Balance Should Be   100-002     $800.00

TC-05-08 Transfer with the memo "Rent October" succeeds
    [Documentation]     US-05 — transfer with a memo succeeds and updates both balances correctly.
    [Tags]              US-05     memo
    Log In As Demo Customer
    Transfer Money      100-001     100-002     100.00    Rent October
    Transfer Should Succeed     Transferred $100.00 from 100-001 to 100-002
    Balance Should Be   100-001     $12,400.00
    Balance Should Be   100-002     $900.00