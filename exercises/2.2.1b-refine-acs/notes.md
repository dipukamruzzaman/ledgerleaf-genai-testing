# HO-2.2.1b — Refine acceptance criteria with prompt chaining + human verification

**Syllabus link:** GenAI-2.2.1 (K3) · Hands-on HO-2.2.1b (H2)
**Input:** US-01 Open an account · **Tool:** <chatbot> · **Date:** 2026-10-24
**Roles:** tester (me) · Product Owner (instructor) · LLM

## The chain
Step 1 Ambiguities → 🛑 human check + PO answers → Step 2 Testability → 🛑 human check + correction → Step 3 Completeness → 🛑 accept/reject

## Step 1 — Ambiguities: PO answers
| Q | AC | PO answer |
|---|---|---|
| Q1 | AC2 | Adult = 18+ on the day of registration, from date of birth. No regional variation. |
| Q2 | AC2 | 18th birthday counts (inclusive); day before rejected. "Today" = Eastern Time (America/Toronto). |
| Q3 | AC2 | Under 18 → on submit: "You must be at least 18 years old to open an account." No account created. |
| Q4 | AC1 | Name 2–100 chars (trimmed); letters incl. accents, spaces, hyphens, apostrophes; no digits/symbols; non-Latin not supported; single-word OK. |
| Q5 | AC3 | Password 8–64 chars; ≥1 upper, ≥1 lower, ≥1 digit; special chars allowed, not required. |
| Q6 | AC5 | Accounts created immediately. No email verification/KYC (out of scope). "Welcome to LedgerLeaf"; no auto-login. |
| Q7 | AC1 | Validation on submit only; all errors together; values kept except password. |
| Q8 | AC5 | All-or-nothing creation. Failure: "We couldn't open your account right now. Please try again later." |
| — | AC4 | Case-sensitivity of duplicate check: **skipped by tester** (left open). |

Observation: 3 of my first questions were all on AC2 — coverage across ACs matters as much as depth.

## Step 2 — Testability: human verification
| Check | Result |
|---|---|
| Values and messages match Q1–Q8 | ✅ Match (first check was done by the AI on itself — redone by eye; self-checks prove little) |
| AC4 left ambiguous, not invented | ✅ AI marked "STILL AMBIGUOUS" — the escape-route constraint worked |
| Partial failure (Q8) testable at system level? | ❌ AI said **Yes**. Wrong: a partial failure cannot be triggered via the UI. **Corrected by tester** → "No – needs fault injection / mocking / integration tests". AI accepted the correction. |

## Step 3 — Completeness: tester decisions
| # | Gap proposed by AI | Decision | Resolution |
|---|---|---|---|
| AC6 | Duplicate-email message, enumeration risk | ✅ (after PO) | "An account with this email already exists." Comparison is **case-insensitive**. |
| AC7 | Email format and trimming | ✅ (after PO) | Basic format name@domain.tld, trimmed, max 254 chars. |
| AC8 | Zero-balance display format | ✅ | $0.00, two decimals (consistent with US-04). |
| AC9 | Double-click submit | ✅ (after PO) | Button disabled after first click; at most one account created. |
| AC10 | Account numbers on success page | ✅ (after PO) | Not on success page; shown on Accounts page after login, format 100-NNN. |
| AC11 | Back button after registration | ❌ Rejected | Low value; re-submit already covered by AC6. |

Format drift: asked for new ACs in Given/When/Then, AI returned **questions** labelled AC6–AC11.
Scope held: AI did not propose email verification or KYC.

## Findings
1. Chaining split one hard task (fix an untestable story) into three checkable steps; each step started from a clean, verified result.
2. The human checkpoint caught a real error: the AI got the content right (exact failure message) but the judgement wrong (testability of AC5b).
3. "Do not guess — mark STILL AMBIGUOUS" worked: no invented case rule for AC4.
4. The AI later surfaced the AC4 gap itself in Step 3 (AC6) — a skipped question came back as a completeness gap.
5. Asking the AI to verify its own output is not verification; the check must be independent (human, or another source).
6. Constraints are not guaranteed: Step 3 output format drifted from Given/When/Then to questions.
7. Follow-up for test execution: PO says duplicate check is case-insensitive → test registering `Alex.Tester@ledgerleaf.test`.
