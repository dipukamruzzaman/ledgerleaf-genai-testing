# HO-2.1.1 — Structure of prompts (six components)

**Syllabus link:** GenAI-2.1.1 (K2) · Hands-on HO-2.1.1 (H0)
**Input:** prompts.md (Prompts A, B, C)
**Date:** 2026-10-12

## Part 1 — Component analysis

### Prompt A
| Component | Present? (Yes/No/Weak) | Text that provides it |
|---|---|---|
| Role |yes  |You are an experienced test analyst for online-banking web applications.|
| Context |yes  | LedgerLeaf Bank is a fictional bank used for test practice. Release 1.0 is in system test.
The Product Owner has confirmed that an account must lock after 3 consecutive failed login attempts. |
| Instruction | yes | Using boundary value analysis, design test cases for the login lockout rule. |
| Input data | yes |User story US-02 Log in
As a customer, I want to log in with my email and password so that I can see my accounts.
1. Valid email and password take the customer to the Accounts page.
2. Invalid credentials show an error that does not reveal whether the email exists.
3. The account is locked after too many failed attempts.
4. A locked account can be unlocked by resetting the password.  |
| Constraints | yes |  Use only the rules given here and do not invent requirements. Write at most 6 test cases.
Use the demo user alex.tester@ledgerleaf.test.
|
| Output format |yes  | Return your answer as a Markdown table with the columns: ID | Attempt no. | Input | Expected result. |

### Prompt B
| Component | Present? (Yes/No/Weak) | Text that provides it |
|---|---|---|
| Role | No |  |
| Context |  No|  |
| Instruction | weak | write test cases for the password reset feature |
| Input data |  No|  |
| Constraints | No |  |
| Output format |weak  | Put them in a table |

### Prompt C
| Component | Present? (Yes/No/Weak) | Text that provides it |
|---|---|---|
| Role | yes | Act as a QA lead who coaches junior testers. |
| Context | Yes | Our team follows the ISTQB defect report template, and user story US-05 says transfers are allowed up to $5,000  |
| Instruction | yes |  Rewrite the report so a developer can reproduce the problem.|
| Input data |  yes but weak | A junior tester wrote this bug report: "Transfer of 5000 fails. Fix asap. |
| Constraints | yes | Keep it under 150 words and do not add steps that cannot be inferred from the original report. |
| Output format | yes  | Give it back as headed sections: Title, Steps to reproduce, Expected result, Actual result, Severity |

### Questions
1. Which prompt is most likely to cause the AI to **invent requirements**? Why?
Prompt B. Because no role, context, input data, constraints and output format provided. Without input data AI will be confused and start generating wrong information or no information.
2. Prompt C asks for **Severity**. Can the AI know it from the input? What should the prompt say?
No, Ai wont be able to know the Severity. need to provide Severity guidance based on the risk matrix or any other source. without that instruction AI will either generate wrong information or wont generate anything.

## Part 2 — Prediction (before running)
Prompt B will invent: role, context, input data, constraints and output format

## Part 2 — Results (Prompt B vs Prompt B+)
| Check | Prompt B (lazy) | Prompt B+ (six-part) |
|---|---|---|
| Number of test cases | 8 (no limit given) |  |
| Invented rules | Yes: password history (TC6), "link not sent" error (TC4), specific-error for invalid email (TC2), MySQL/Chrome/Win10 environment |  |
| Used the real US-03 ACs? | No. AC2 contradicted (TC2); AC5 rules guessed, 2 expected results wrong (TC7, TC8) |  |
| Format as asked? | Table yes, plus unrequested extras (environment, steps, notes) |  |

### Prompt B+ Password reset
ROLE: You are an experienced test analyst for online-banking web applications.

CONTEXT: LedgerLeaf Bank is a fictional bank used for test practice. Release 1.0 is in
system test. Reset e-mails are not really sent; they appear on the demo /outbox page.
A related rule from US-02: a locked account is unlocked by resetting the password.

INSTRUCTION: Design test cases for the password reset feature. Cover every acceptance
criterion at least once and include negative cases.

INPUT – User story US-03 Reset password
As a customer who forgot my password, I want to reset it by email so that I can access
my account again.
1. The customer enters their email on the "Forgot password" page.
2. The same confirmation message is shown whether or not the email is registered.
3. A reset link is sent to the registered email address.
4. The link should expire after a reasonable time.
5. The new password must follow the same rules as at registration.

CONSTRAINTS:
- Use only the rules given here. Do not invent requirements.
- If a rule is vague or a value is missing, do NOT guess a value. Write the test with
  "<TBD>" and add the question to an "Open questions for the Product Owner" list.
- Write at most 6 test cases. Use the demo user alex.tester@ledgerleaf.test.

OUTPUT FORMAT:
1. Markdown table: | ID | Title | Steps | Test data | Expected result | AC |
2. A list titled "Open questions for the Product Owner".

## Findings

Prompt B
>>> /set parameter temperature 0
Set parameter 'temperature' to '0'
>>> "Write test cases for the password reset feature. Put them in a table."
>>> Write test cases for the password reset feature. Put them in a table.
**Password Reset Test Cases**
=====================================

The following test cases cover the password reset feature to ensure it functions as expected.

| **Test Case ID** | **Test Case Description** | **Expected Result** | **Actual Result** |
| --- | --- | --- | --- |
| **TC1: Successful Password Reset** | User attempts to reset password with valid email and new password. | User receives email with password reset link, can reset password successfully. |  |
| **TC2: Invalid Email** | User attempts to reset password with invalid email. | System displays error message indicating invalid email. |  |
| **TC3: Password Reset Link Expired** | User clicks on expired password reset link. | System displays error message indicating link has expired. |  |
| **TC4: Password Reset Link Not Sent** | User attempts to reset password but does not receive email with link. | System displays error message indicating link not sent. |  |
| **TC5: Password Reset with Weak Password** | User attempts to reset password with weak password (e.g., "password123"). | System displays error message indicating weak password. |  |
| **TC6: Password Reset with Existing Password** | User attempts to reset password with existing password. | System displays error message indicating password is already in use. |  |
| **TC7: Password Reset with Special Characters** | User attempts to reset password with special characters (e.g., "!@#$%^&*()"). | System allows password reset with special characters. |  |
| **TC8: Password Reset with Long Password** | User attempts to reset password with long password (e.g., "verylongpassword"). | System allows password reset with long password. |  |

**Test Environment**

* Browser: Google Chrome
* Operating System: Windows 10
* Database: MySQL

**Test Data**

* Valid email: `test@example.com`
* Invalid email: `invalidemail`
* Weak password: `password123`
* Existing password: `existingpassword`
* Special characters: `!@#$%^&*()`
* Long password: `verylongpassword`

**Test Steps**

1. Log in to the application with a valid user account.
2. Navigate to the password reset page.
3. Enter a valid email address and click "Reset Password".
4. Verify that an email with a password reset link is sent to the user's email address.
5. Click on the password reset link and enter a new password.
6. Verify that the password is reset successfully.

**Test Notes**

* The test cases cover various scenarios to ensure the password reset feature functions as expected.
* The test environment and test data are specified to ensure consistency across tests.
* The test steps are detailed to ensure that each test case is executed correctly.


Prompt B+ 
| Check | Prompt B (lazy) | Prompt B+ (six-part) |
|---|---|---|
| Number of test cases | 8 (no limit given) | 6 (limit respected) |
| Invented rules | Yes: password history, "link not sent" error, specific invalid-email error, MySQL/Chrome/Win10 | None invented; 1 reasonable assumption (link reuse, 1.6) |
| Used the real US-03 ACs? | No: AC2 contradicted, 2 wrong expected results | Yes: AC2 correct, AC4/AC5 raised as PO questions; AC tags wrong in 1.2 and 1.5 |
| Format as asked? | Table plus unrequested extras | Yes; but ignored the `<TBD>` instruction |

## Findings
1. Same model, same temperature, same feature, only the prompt changed: B produced 8 professional-looking
   cases, ~5 wrong or invented, and it **contradicted AC2** (a security rule). B+ produced 6 grounded cases.
2. Missing input data → the model fills gaps with generic "typical app" rules, stated confidently.
3. A "do not invent" constraint works only with an escape route ("mark <TBD>, list open questions").
   B+ asked the PO about expiry and password rules instead of guessing.
4. Constraints are not guaranteed: B+ ignored "<TBD>" and mis-tagged ACs (1.2, 1.5). Always review the output.
5. Context can leak: the lock/unlock rule appeared in unrelated expected results.
6. My draft of B+ had 3 bugs (US-02 rule added into US-03, copied "Attempt no." column, no escape route).
   Prompts need review just like test cases.
7. Prediction check: the instructor predicted an invented expiry time (e.g. "24 h"); it did not happen.
