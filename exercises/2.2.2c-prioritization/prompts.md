# HO-2.2.2c — Prompt chaining for test prioritization

Use ONE chat (ChatGPT or Gemini). Paste the whole of test-suite.md where it says <SUITE>.

---

## Step 1 — Risk-based order
```text
You are a test manager. Below is our regression suite for LedgerLeaf Release 1.0.1.
Order ALL test cases using a risk-based strategy (highest risk first).
Output a table: | Rank | ID | Test case | Risk | Reason |

<SUITE>
```
🛑 Check: does any test appear BEFORE a test it depends on? (see "Depends on" column)

---

## Step 2 — Respect dependencies
```text
Re-order the list so that every test runs after the tests it depends on, while keeping
the highest-risk tests as early as possible. If a high-risk test depends on a
lower-risk test, move that dependency forward and mark it "(pulled forward)".
Output the same table plus a column "Depends on".
```
🛑 Check: every dependency respected? Which tests were pulled forward?

---

## Step 3 — Time-box
```text
We only have 60 minutes of test execution today. Using your dependency-aware order,
select the tests to run. Show a running total of minutes after each test, do not
exceed 60 minutes, never run a test without its dependencies, and list the deferred
tests with the reason. Explain your selection in 2–3 sentences.
```
🛑 Check: is the running total arithmetic correct? Is the selection the best use of 60 minutes?
