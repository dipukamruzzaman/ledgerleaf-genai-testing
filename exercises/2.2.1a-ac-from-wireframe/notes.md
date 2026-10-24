# HO-2.2.1a — Acceptance criteria from a wireframe (multimodal)

**Syllabus link:** GenAI-2.2.1 (K3) · Hands-on HO-2.2.1a (H2)
**Input:** US-06 + add-payee-wireframe.png (+ business rules in V3)
**Tool:** <chatbot> · **Date:** <date>

## Predictions (before running)
- Which version will cover the most items? ...
- Will V1 notice the $1,000 limit in the info box? ...

## Scorecard — tick ✅ if the AI covered the item, ❌ if missed, ⚠️ if it guessed a value
| # | Item a good AC set must cover | Where it comes from | V1 | V2 | V3 |
|---|---|---|---|---|---|
| 1 | Payee name and account number are required | Wireframe (*) | ✅ |✅  | ✅ |
| 2 | Error if the account number does not exist | Sticky note | ✅ | ❌ |  ✅|
| 3 | Account number format NNN-NNN | Wireframe placeholder / Rules |  | ❌ |  ✅| 
| 4 | Nickname is optional | Wireframe |✅  | ❌ | ✅ |
| 5 | Payee type options (only "Person" visible) → question or AC | Wireframe |❌  | ❌ | ✅ |
| 6 | "Save as favourite" behaviour | Wireframe |❌  | ❌ | ✅ |
| 7 | New payee limited to $1,000 in the first 24 hours | Wireframe info box |❌  | ❌ | ✅ |
| 8 | Maximum 20 payees | Wireframe "3 of 20" / Rules |❌  | ❌ | ✅ |
| 9 | Duplicate payee → open question (not invented) | Sticky note |❌  | ❌ | ✅ |
| 10 | Cannot add own account | Rules only |❌  | ❌ | ✅ |
| 11 | Cancel returns without saving | Wireframe |❌  | ❌ | ✅ |
| 12 | Success: new payee appears in "Your payees" | Wireframe + Story |❌  | ❌ | ✅ |
|  | **Score (out of 12)** |  |  |  |  |
|  | Invented values / out-of-scope ACs (e.g. delete) — count |  |  |  |  |
|  | Given/When/Then used? |  |✅  | ✅ | ✅ |

## Findings
