# LedgerLeaf Bank — Product Backlog (Release 1.0)

*Written by the Product Owner. This is the test basis for the project.*
*Note for testers: this backlog has not been reviewed yet.*

---

## US-01 Open an account
**As a** new customer, **I want to** open an online account **so that** I can bank with LedgerLeaf.

Acceptance criteria
1. The customer enters full name, email, date of birth and password.
2. Only adults can open an account.
3. The password must be strong.
4. An email address can only be used once.
5. After registration the customer gets a Chequing and a Savings account with a zero balance.

## US-02 Log in
**As a** customer, **I want to** log in with my email and password **so that** I can see my accounts.

Acceptance criteria
1. Valid email and password take the customer to the Accounts page.
2. Invalid credentials show an error that does not reveal whether the email exists.
3. The account is locked after too many failed attempts.
4. A locked account can be unlocked by resetting the password.

## US-03 Reset password
**As a** customer who forgot my password, **I want to** reset it by email **so that** I can access my account again.

Acceptance criteria
1. The customer enters their email on the "Forgot password" page.
2. The same confirmation message is shown whether or not the email is registered.
3. A reset link is sent to the registered email address.
4. The link should expire after a reasonable time.
5. The new password must follow the same rules as at registration.

## US-04 View accounts
**As a** logged-in customer, **I want to** see my accounts and balances **so that** I know how much money I have.

Acceptance criteria
1. The Accounts page lists each account with its number, type and balance.
2. Balances are shown in dollars with two decimal places.
3. Customers can only see their own accounts.

## US-05 Transfer money
**As a** logged-in customer, **I want to** transfer money from my account to another LedgerLeaf account **so that** I can move or pay money quickly.

Acceptance criteria
1. The customer chooses one of their own accounts, enters the destination account number and an amount.
2. Transfers are allowed up to the daily limit of $5,000.
3. The amount must be positive and have at most two decimal places.
4. The customer cannot transfer more than the available balance.
5. A confirmation with a reference number is shown after a successful transfer.
6. An optional memo can be added.

---

### Demo data
| Customer | Email | Password | Accounts |
|---|---|---|---|
| Alex Tester | alex.tester@ledgerleaf.test | Passw0rd! | 100-001 Chequing ($12,500.00), 100-002 Savings ($800.00) |
| Sam Saver | sam.saver@ledgerleaf.test | Savings123 | 100-003 Chequing ($0.00), 100-004 Savings ($0.00) |
