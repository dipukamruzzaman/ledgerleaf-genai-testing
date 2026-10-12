ROLE: You are a senior software tester reviewing a banking web app.

CONTEXT: The attached image is a screenshot of the "Transfer money" page of
LedgerLeaf Bank, a fictional test app. Below is the user story it implements.

INPUT – User story US-05 Transfer money
As a logged-in customer, I want to transfer money from my account to another
LedgerLeaf account so that I can move or pay money quickly.
Acceptance criteria
1. The customer chooses one of their own accounts, enters the destination account number and an amount.
2. Transfers are allowed up to the daily limit of $5,000.
3. The amount must be positive and have at most two decimal places.
4. The customer cannot transfer more than the available balance.
5. A confirmation with a reference number is shown after a successful transfer.
6. An optional memo can be added.

INSTRUCTION:
1. List every mismatch or ambiguity between the screenshot and the user story.
2. Suggest 8 test cases for this page.

CONSTRAINTS:
- For every finding, say whether it is VISIBLE in the screenshot or INFERRED
  (a guess about behaviour you cannot see). Quote the on-screen text as evidence.
- Do not invent fields, buttons or messages that are not in the image.

OUTPUT FORMAT:
Table 1 – Findings: | # | Finding | Visible/Inferred | Evidence | Related AC |
Table 2 – Test cases: | ID | Title | Steps | Test data | Expected result | AC |
