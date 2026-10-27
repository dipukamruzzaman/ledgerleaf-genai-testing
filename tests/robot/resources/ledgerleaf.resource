*** Settings ***
Documentation     Keyword library for LedgerLeaf Bank (keyword-driven UI tests).
...               Business-level keywords only: tests call these, never raw locators.
Library           SeleniumLibrary

*** Variables ***
${BASE_URL}       http://127.0.0.1:5000
${BROWSER}        chrome
${BROWSER_OPTIONS}    ${NONE}
${DEMO_EMAIL}     alex.tester@ledgerleaf.test
${DEMO_PASSWORD}  Passw0rd!

*** Keywords ***
Open LedgerLeaf
    [Documentation]    Opens the browser on the login page and resets the demo data.
    Open Browser    ${BASE_URL}/login    ${BROWSER}    options=${BROWSER_OPTIONS}
    Reset Demo Data

Close LedgerLeaf
    [Documentation]    Closes all browsers.
    Close All Browsers

Reset Demo Data
    [Documentation]    Restores the seeded demo users, accounts and balances (POST /api/test/reset).
    Execute Async Javascript
    ...    var done = arguments[arguments.length - 1];
    ...    fetch('/api/test/reset', {method: 'POST'}).then(() => done('ok'));

Log In As
    [Documentation]    Logs in with the given email and password (does not check the result).
    [Arguments]    ${email}    ${password}
    Go To    ${BASE_URL}/login
    Input Text        css:[data-testid="login-email"]       ${email}
    Input Password    css:[data-testid="login-password"]    ${password}
    Click Button      css:[data-testid="login-submit"]

Log In As Demo Customer
    [Documentation]    Logs in as Alex Tester (owner of 100-001 and 100-002).
    Log In As    ${DEMO_EMAIL}    ${DEMO_PASSWORD}
    Accounts Page Should Be Shown

Accounts Page Should Be Shown
    [Documentation]    Checks that the accounts table is visible.
    Wait Until Element Is Visible    css:[data-testid="accounts-table"]

Login Error Should Be
    [Documentation]    Checks the error message on the login page.
    [Arguments]    ${message}
    Page Should Contain    ${message}

Balance Should Be
    [Documentation]    Checks the balance shown for an account on the Accounts page, e.g. "$12,500.00".
    [Arguments]    ${account}    ${expected}
    Go To    ${BASE_URL}/dashboard
    Element Text Should Be    css:[data-testid="balance-${account}"]    ${expected}

Transfer Money
    [Documentation]    Fills in and submits the transfer form. ${memo} is optional.
    [Arguments]    ${from}    ${to}    ${amount}    ${memo}=${EMPTY}
    Go To    ${BASE_URL}/transfer
    Select From List By Value    css:[data-testid="transfer-from"]    ${from}
    Input Text    css:[data-testid="transfer-to"]        ${to}
    Input Text    css:[data-testid="transfer-amount"]    ${amount}
    Input Text    css:[data-testid="transfer-memo"]      ${memo}
    Click Button  css:[data-testid="transfer-submit"]

Transfer Should Succeed
    [Documentation]    Checks the confirmation, e.g. "Transferred $100.00 from 100-001 to 100-002".
    [Arguments]    ${expected_text}
    Wait Until Element Is Visible    css:[data-testid="transfer-success"]
    Element Should Contain    css:[data-testid="transfer-success"]    ${expected_text}
    Element Should Contain    css:[data-testid="transfer-success"]    Reference #

Transfer Should Fail With
    [Documentation]    Checks the error message shown on the transfer page.
    [Arguments]    ${message}
    Wait Until Element Is Visible    css:[data-testid="transfer-error"]
    Element Text Should Be    css:[data-testid="transfer-error"]    ${message}
