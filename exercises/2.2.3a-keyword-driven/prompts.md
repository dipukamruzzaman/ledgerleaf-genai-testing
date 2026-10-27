# HO-2.2.3a — Few-shot prompting for keyword-driven test scripts (Robot Framework)

## PART 1 — Create, validate, expand

### Prompt 1 — Generate scripts (few-shot) — ChatGPT or Gemini, new chat
Paste the FULL content of the two files where indicated.
```text
ROLE: You are a test automation engineer using Robot Framework (keyword-driven testing).

CONTEXT: LedgerLeaf Bank is a fictional bank used for test practice. Below is our keyword
library (the ONLY keywords you may use, besides Robot Framework built-ins) and two finished
test scripts that show our house style.

KEYWORD LIBRARY (resources/ledgerleaf.resource):
<paste ledgerleaf.resource>

EXAMPLE SCRIPTS (examples.robot):
<paste examples.robot>

INSTRUCTION: Write a new file transfers.robot in exactly the same style, automating these test cases
for US-05 (demo customer: 100-001 Chequing $12,500.00, 100-002 Savings $800.00; transfer limit
$5,000.00 per transfer INCLUSIVE; same-account and unknown-account transfers are rejected):
TC-05-03 Transfer exactly 5000.00 from 100-001 to 100-002 succeeds (retest of DEF-001)
TC-05-04 Transfer 4999.99 succeeds
TC-05-05 Transfer 5000.01 is rejected with "The maximum per transfer is $5,000.00."
TC-05-06 Transfer from 100-001 to 100-001 is rejected with "Choose two different accounts."
TC-05-07 Transfer to 100-999 is rejected with "The destination account does not exist."
TC-05-08 Transfer with the memo "Rent October" succeeds

CONSTRAINTS:
- Use only keywords from the library and Robot Framework built-ins. Never use raw locators.
- Same Settings, Tags and Documentation style as the examples.
- After every successful transfer, check BOTH balances; calculate them exactly.

OUTPUT FORMAT: one Robot Framework file in a single code block.
```

### Prompt 2 — AI validates the scripts (same chat)
```text
Review transfers.robot as a strict code reviewer. Check: (1) every keyword exists in the
library with the right number and order of arguments, (2) at least two spaces between a
keyword and its arguments, (3) every expected balance is arithmetically correct,
(4) every expected message matches exactly. List problems as a table and give the fixed file.
```

### Run it (PowerShell, app running in another window)
```powershell
robot --outputdir reports\robot tests\robot\transfers.robot
```
Open reports\robot\report.html.

---

## PART 2 — A debugging assistant with a SYSTEM prompt (Ollama)

```powershell
ollama run llama3.1:8b
```
Inside Ollama, set the system prompt (one line):
```text
/set system You are a Robot Framework debugging assistant for LedgerLeaf Bank. Valid keywords: Open LedgerLeaf; Close LedgerLeaf; Reset Demo Data; Log In As (email, password); Log In As Demo Customer; Accounts Page Should Be Shown; Login Error Should Be (message); Balance Should Be (account, expected e.g. $12,500.00); Transfer Money (from, to, amount, memo=optional); Transfer Should Succeed (expected_text); Transfer Should Fail With (message, exact match). Demo data: 100-001 Chequing $12,500.00, 100-002 Savings $800.00. Rules: keywords and arguments are separated by at least two spaces. For each problem you find, answer with: Line, Problem, Fix. Do not rewrite lines that are correct.
```
Then:
```text
/set parameter temperature 0
```
Then paste the content of broken.robot wrapped in triple quotes:
```text
"""
<paste broken.robot>
"""
```
