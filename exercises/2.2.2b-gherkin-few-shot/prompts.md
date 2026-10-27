# HO-2.2.2b — Few-shot prompting: user story → test conditions → Gherkin

Run each prompt in a NEW chat (ChatGPT or Gemini).

---

## Prompt 1 — Zero-shot baseline (no examples)
```text
Write Gherkin test scenarios for this user story.

US-03 Reset password
As a customer who forgot my password, I want to reset it by email so that I can access my account again.
AC1 The customer enters their email on the "Forgot password" page.
AC2 The message "If an account exists for this email, a reset link has been sent." is shown whether or not the email is registered.
AC3 A reset link is sent to the registered email address (in the demo, it appears on the /outbox page).
AC4 The link expires after 30 minutes and can be used only once. An expired or used link shows "This reset link is invalid."
AC5 The new password must be 8–64 characters with at least one upper-case letter, one lower-case letter and one digit.
AC6 After a successful reset, "Your password has been changed. You can now log in." is shown, the account is unlocked and the customer can log in with the new password.
```

---

## Prompt 2 — Few-shot (2 examples)
```text
ROLE: You are a test analyst who writes BDD scenarios in Gherkin for LedgerLeaf Bank,
a fictional online bank used for test practice.

INSTRUCTION: For the NEW user story at the end, first list the test conditions, then
write Gherkin scenarios. Follow the two examples EXACTLY: same structure, tags,
step style and conventions.

=== EXAMPLE 1 ===
USER STORY: US-02 Log in
AC1 Valid email and password take the customer to the Accounts page.
AC2 Invalid credentials show "Invalid email or password." whether or not the email exists.
AC3 The account is locked after 3 consecutive failed attempts and shows "Your account is locked. Reset your password to unlock it."

TEST CONDITIONS:
TCOND-02-1 Valid credentials give access (AC1)
TCOND-02-2 Wrong password or unknown email give the same generic error (AC2)
TCOND-02-3 Lockout happens exactly at the 3rd consecutive failure, not before (AC3)

GHERKIN:
@US-02
Feature: Log in

  Background:
    Given the demo data is reset
    And the customer "alex.tester@ledgerleaf.test" exists with password "Passw0rd!"

  @TC-02-01 @AC1
  Scenario: Customer logs in with valid credentials
    When the customer logs in with "alex.tester@ledgerleaf.test" and "Passw0rd!"
    Then the Accounts page is shown

  @TC-02-02 @AC2
  Scenario Outline: Invalid credentials show one generic error
    When the customer logs in with "<email>" and "<password>"
    Then the message "Invalid email or password." is shown

    Examples:
      | email                         | password   |
      | alex.tester@ledgerleaf.test   | WrongPass1 |
      | nobody@ledgerleaf.test        | Passw0rd!  |

  @TC-02-03 @AC3
  Scenario Outline: Account locks exactly at the 3rd failed attempt
    Given the customer has failed to log in <failures> times in a row
    When the customer logs in with "alex.tester@ledgerleaf.test" and "WrongPass1"
    Then the message "<message>" is shown

    Examples:
      | failures | message                                                    |
      | 1        | Invalid email or password.                                 |
      | 2        | Your account is locked. Reset your password to unlock it.  |

=== EXAMPLE 2 ===
USER STORY: US-04 View accounts
AC1 After log-in, the customer sees each of their accounts with type, number and balance.
AC2 Balances are shown with a $ sign and two decimals.
AC3 A customer sees only their own accounts.

TEST CONDITIONS:
TCOND-04-1 All own accounts are listed with type, number and balance (AC1)
TCOND-04-2 Balance format is $ with two decimals, including zero (AC2)
TCOND-04-3 Other customers' accounts are never shown (AC3)

GHERKIN:
@US-04
Feature: View accounts

  Background:
    Given the demo data is reset
    And the customer "alex.tester@ledgerleaf.test" is logged in

  @TC-04-01 @AC1 @AC2
  Scenario Outline: Own accounts are listed with formatted balances
    Then the account "<number>" of type "<type>" shows the balance "<balance>"

    Examples:
      | number  | type     | balance    |
      | 100-001 | Chequing | $12,500.00 |
      | 100-002 | Savings  | $800.00    |

  @TC-04-02 @AC3
  Scenario: Another customer's account is not shown
    Then the account "100-003" is not shown

=== NEW USER STORY ===
USER STORY: US-03 Reset password
AC1 The customer enters their email on the "Forgot password" page.
AC2 The message "If an account exists for this email, a reset link has been sent." is shown whether or not the email is registered.
AC3 A reset link is sent to the registered email address (in the demo, it appears on the /outbox page).
AC4 The link expires after 30 minutes and can be used only once. An expired or used link shows "This reset link is invalid."
AC5 The new password must be 8–64 characters with at least one upper-case letter, one lower-case letter and one digit.
AC6 After a successful reset, "Your password has been changed. You can now log in." is shown, the account is unlocked and the customer can log in with the new password.

TEST CONDITIONS:
GHERKIN:
```
