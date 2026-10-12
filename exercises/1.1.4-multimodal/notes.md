# HO-1.1.4 — Multimodal LLM: transfer page screenshot vs US-05

**Syllabus link:** GenAI-1.1.4 · Hands-on HO-1.1.4
**Input:** transfer-page.png + US-05 Transfer money
**Tool:** <chatbot name>
**Date:** 2026-10-11

## Predictions (written before running)
- **P1:** per transfer vs daily limit
Information provided about limit $5000.00 per transfer. does not mention daily limit. that might confuse users that they might be able to tranbsfer more than $5000.00 if they do multiple transfers and should allow more than the daily limit of $5000.00, which was defined in the acceptance criteria. 

- **P2:** Confirmation wont be possible from the screenshot as it would require to click on the transfer button before transfer executed.

## Verification
| # | Tool | AI finding | AI label | AC | Really visible? | Verdict |
|---|---|---|---|---|---|---|
| C1 | ChatGPT | From dropdown present; can't tell if only own accounts are listed | Visible / Inferred | AC1 | Yes | Correct: honest about its limit |
| C2 | ChatGPT | To-account field present; can't tell if invalid, non-existent or same account is rejected | Visible / Inferred | AC1 | Yes | Correct |
| C4 | ChatGPT | "Per transfer" on screen vs "daily limit" in story | Visible / Inferred | AC2 | Yes | Correct: key mismatch found |
| G1 | Gemini | "Per transfer" on screen vs "daily limit" in story | Visible | AC2 | Yes | Correct: key mismatch found |
| C11 | ChatGPT | Can't tell if daily limit resets, how transfers add up, or if failed ones count | Inferred | AC2 | n/a | Correct: good question for the PO |
| C3 | ChatGPT | No visible rule that the amount must be positive | Visible / Inferred | AC3 | Yes | Correct |
| C5 | ChatGPT | No guidance on a maximum of 2 decimal places | Visible / Inferred | AC3 | Yes | Correct |
| G3 | Gemini | No validation rules, helper text **or input constraints** for positive amounts or 2 decimals | Visible | AC3 | Partly | Partly wrong: overclaim (see note 1) |
| C6 | ChatGPT | Balance $12,400.00 shown; over-balance blocking unknown | Visible / Inferred | AC4 | Yes | Correct: read the number exactly |
| G4 | Gemini | Balance $12,400.00 shown; over-balance blocking unknown | Inferred | AC4 | Yes | Correct |
| C8 | ChatGPT | Transfer button present; can't tell if a confirmation follows | Visible / Inferred | AC5 | Yes | Correct: avoided the P2 trap |
| C9 | ChatGPT | No confirmation on the current page; can't tell from a static image | Visible / Inferred | AC5 | Yes | Correct: duplicate of C8 |
| G2 | Gemini | Confirmation and reference number can't be seen on the input form | Inferred | AC5 | n/a | Correct: avoided the P2 trap |
| C7 | ChatGPT | Memo field present and marked optional | Visible | AC6 | Yes | Correct |
| C10 | ChatGPT | No validation messages visible for empty or invalid input | Visible / Inferred | AC1, 3, 4 | Yes | Correct |
| C12 | ChatGPT | Risk of a duplicate transfer from a double-click or refresh | (cut off, no label) | none | n/a | Can't tell: plausible real risk (see note 2) |

## Findings
## Findings
| | ChatGPT | Gemini |
|---|---|---|
| Findings | 12 | 4 |
| Correct | 11 | 3 |
| Partly wrong / overclaim | 0 | 1 (G3) |
| Invented | 0 | 0 |
| Followed label format | No (split labels, 1 missing) | Yes |
| Caught key mismatch (AC2 daily vs per transfer) | Yes | Yes |
| Fell for the AC5 trap (P2) | No | No |

1. Both models caught the main mismatch: "daily limit" (US-05 AC2) vs "$5,000.00 per transfer" on screen. → Question for the PO.
2. Neither fell for my P2 trap: both said AC5 can't be checked from a static image. Good prompt design ("Visible/Inferred" + "do not invent") helped.
3. ChatGPT was more thorough but repetitive (C8/C9 say the same thing) and broke the output format. Gemini was concise and followed the format, but overclaimed once (G3).
4. A screenshot shows **current state**, not seed data: balance $12,400.00 (not $12,500.00) because of my earlier $100 test transfer.
5. Hidden constraints (HTML `min`, `step`, `maxlength`) are invisible to a VLM. "Not visible" ≠ "not there."
6. Neither model raised my usability point (P1: the "100-002" placeholder looks pre-filled). Human review still adds value.
7. ChatGPT C12 (duplicate submit on refresh) is a possible real defect → test later.
