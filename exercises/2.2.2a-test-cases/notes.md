# HO-2.2.2a — Functional test cases from US-05 (chaining + structured + meta)

**Syllabus link:** GenAI-2.2.2 (K3) · HO-2.2.2a (H2) · **Tools:** ChatGPT/Gemini (steps 1–2), Gemini (step 3) · **Date:** 2026-10-26

## The chain
Step 1 Structured prompt → test cases · Step 2 Coverage check → gaps filled · Step 3 Meta prompt → E2E procedure · Step 4 Execute in the app

## Step 1 — Generated test cases
| Check | Result |
|---|---|
| Number of test cases | 13 |
| Boundaries for AC2 present? | Yes (incl. exactly 5,000.00) |
| Any invented rule? | No — clear rules + "use only the rules above" held |

## Step 2 — Coverage check (chaining)
| Check | Result |
|---|---|
| ACs not fully covered | AC2, AC5, AC6 "Partly" → AI added 2 test cases (13 → 15) |
| My spot check of AC7 | Really covered (same account + non-existent account) |
| Tests not traceable to an AC | None |

## Step 3 — Meta prompting (Gemini)
**AI's questions and my answers**
1. Output format? → Hybrid BDD (Gherkin) + steps + assertion checkpoints, convertible to Playwright/pytest.
2. Negative / edge cases in the journey? → Yes, input validation alongside the happy path.
3. API and state checks? → HTTP 200/201 checks and database/UI balance synchronization.

**What the improved prompt added:** automation-framework role (Playwright/pytest); edge cases and backend state in context;
Gherkin + executable steps + API checks; valid/invalid/edge amounts as input; constraints for negative paths, robust locators,
arithmetic assertions, teardown; structured Markdown output (metadata, preconditions, scenarios, step table, teardown).

| Check on the final E2E procedure | Result |
|---|---|
| Real demo user and accounts | ❌ Not used — the meta prompt never contained them |
| Balance arithmetic | ✅ Correct |
| Selectors | ✅ Matched real data-testid values (to re-verify against app/templates) |
| Database steps | ❌ Invented `ledger_transactions` table query — LedgerLeaf has no DB. Came from my own Q3 answer |
| Status codes | 🟠 Transfer 200 ✅, API 201 ✅, login (302) not checked |
| **Executable as written?** | **No** |

## Step 4 — Execution in the app (from 100-001, fresh data)
| # | Test | Expected | Actual | Result |
|---|---|---|---|---|
| 1 | 4,999.99 → 100-002 | Success + reference | Transferred $4999.99 … Reference #1 | ✅ Pass |
| 2 | 5,000.00 → 100-002 | Success (AC2 inclusive) | "The maximum per transfer is $5,000.00." | ❌ **FAIL → DEF-001** |
| 3 | 5,000.01 → 100-002 | Rejected | "The maximum per transfer is $5,000.00." | ✅ Pass |
| 4 | 0.01 → 100-002 | Success | Transferred $0.01 … Reference #2 | ✅ Pass |
| 5 | 100-001 → 100-001 | Rejected | "Choose two different accounts." | ✅ Pass |
| 6 | → 100-999 | Rejected | "The destination account does not exist." | ✅ Pass |

## DEF-001 — Transfer of exactly $5,000.00 is rejected
- **Severity:** Major · **Priority:** High (customer-reported; blocks a valid transfer)
- **Environment:** LedgerLeaf Release 1.0, local (python app/app.py), demo data
- **Steps:** 1. Log in as alex.tester@ledgerleaf.test. 2. Transfer. From 100-001, To 100-002, Amount 5000.00. 3. Submit.
- **Expected:** Transfer succeeds with a reference number (US-05 AC2: up to $5,000.00 per transfer, inclusive).
- **Actual:** Error "The maximum per transfer is $5,000.00." — the message contradicts the behaviour.
- **Evidence:** Tests 1 (4,999.99 passes) and 3 (5,000.01 rejected) bracket the boundary.
- **Likely cause (for dev):** limit check uses `>=` instead of `>`.
- **Found by:** AI-generated BVA test case (step 1), executed manually.

## Findings
1. A structured prompt with a complete, clarified rule list produced 13 relevant test cases with no invented rules.
2. Chaining added value: the coverage step found 3 partly covered ACs and added 2 test cases.
3. Meta prompting improved prompt **structure** a lot, but cannot add **facts**: no demo data in → generic data out.
4. The tester's own answers become the AI's facts: "database sync" → an invented `ledger_transactions` table.
5. AI-designed boundary tests found a real defect (DEF-001) — but only because a human ran them against the app.
6. Closes the PO ticket from 1.1.4 / 2.1.2a: "a customer couldn't transfer $5,000".
