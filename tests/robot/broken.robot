*** Settings ***
Documentation     Test scripts written by a junior tester. They do not work. (HO-2.2.3a part 2)
Resource          resources/ledgerleaf.resource
Suite Setup       Open LedgerLeaf
Suite Teardown    Close LedgerLeaf
Test Setup        Reset Demo Data

*** Test Cases ***
TC-05-10 Transfer 250.00 from chequing to savings
    [Tags]    US-05    AC1    AC5
    Log In As Demo User
    Transfer Money    100-001    100-002    250.00
    Transfer Should Succeed    Transferred $250.00 from 100-001 to 100-002
    Balance Should Be    100-001    $12,350.00

TC-05-11 Transfer to the same account is rejected
    [Tags]    US-05    AC7    negative
    Log In As Demo Customer
    Transfer Money    10.00    100-001    100-001
    Transfer Should Fail With Choose two different accounts.

TC-05-12 Savings cannot send more than its balance
    [Tags]    US-05    AC4    negative
    Log In As Demo Customer
    Transfer Money    100-002    100-001    900.00
    Transfer Should Fail With    Insufficient funds
