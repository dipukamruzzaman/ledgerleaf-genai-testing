# HO-2.1.1 — Three prompts to analyse

Label the six components in each prompt: **Role · Context · Instruction · Input data · Constraints · Output format**.
Some prompts are complete, some are not, and the components are not always in the usual order.

---

## Prompt A — Login lockout test design

```text
Return your answer as a Markdown table with the columns: ID | Attempt no. | Input | Expected result.

You are an experienced test analyst for online-banking web applications.

LedgerLeaf Bank is a fictional bank used for test practice. Release 1.0 is in system test.
The Product Owner has confirmed that an account must lock after 3 consecutive failed login attempts.

Use only the rules given here and do not invent requirements. Write at most 6 test cases.
Use the demo user alex.tester@ledgerleaf.test.

Using boundary value analysis, design test cases for the login lockout rule.

User story US-02 Log in
As a customer, I want to log in with my email and password so that I can see my accounts.
1. Valid email and password take the customer to the Accounts page.
2. Invalid credentials show an error that does not reveal whether the email exists.
3. The account is locked after too many failed attempts.
4. A locked account can be unlocked by resetting the password.
```

---

## Prompt B — Password reset

```text
Write test cases for the password reset feature. Put them in a table.
```

---

## Prompt C — Improve a bug report

```text
A junior tester wrote this bug report: "Transfer of 5000 fails. Fix asap." Act as a QA lead
who coaches junior testers. Our team follows the ISTQB defect report template, and user story
US-05 says transfers are allowed up to $5,000. Rewrite the report so a developer can reproduce
the problem. Keep it under 150 words and do not add steps that cannot be inferred from the
original report. Give it back as headed sections: Title, Steps to reproduce, Expected result,
Actual result, Severity.
```
