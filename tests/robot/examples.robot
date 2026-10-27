*** Settings ***
Documentation     Few-shot EXAMPLES for HO-2.2.3a — two finished test scripts in our house style.
Resource          resources/ledgerleaf.resource
Suite Setup       Open LedgerLeaf
Suite Teardown    Close LedgerLeaf
Test Setup        Reset Demo Data

*** Test Cases ***
TC-05-01 Transfer 100.00 from chequing to savings
    [Documentation]    US-05 AC1, AC5 — a normal transfer succeeds and both balances change.
    [Tags]    US-05    AC1    AC5    smoke
    Log In As Demo Customer
    Transfer Money    100-001    100-002    100.00
    Transfer Should Succeed    Transferred $100.00 from 100-001 to 100-002
    Balance Should Be    100-001    $12,400.00
    Balance Should Be    100-002    $900.00

TC-05-02 Transfer more than the available balance is rejected
    [Documentation]    US-05 AC4 — savings holds $800.00; $800.01 must be rejected and balances unchanged.
    [Tags]    US-05    AC4    negative
    Log In As Demo Customer
    Transfer Money    100-002    100-001    800.01
    Transfer Should Fail With    Insufficient funds.
    Balance Should Be    100-002    $800.00
