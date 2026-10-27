# HO-2.2.2b — Few-shot prompting: Gherkin from user stories

**Syllabus link:** GenAI-2.2.2 (K3) · HO-2.2.2b (H2) · **Tool:** <chatbot> · **Date:** 2026-10-26
**New story:** US-03 Reset password · **Examples given:** US-02 Log in, US-04 View accounts (few-shot = 2)

## Scorecard — did the output follow the conventions in the examples?
| # | Convention shown in the examples | Zero-shot (P1) | Few-shot (P2) |
|---|---|---|---|
| 1 | Test conditions listed first (TCOND-03-n) | ❌ | ✅ |
| 2 | Feature tagged @US-03 | ❌ | ✅ |
| 3 | Every scenario tagged @TC-03-nn and @AC-n | ❌ | ✅ |
| 4 | Background used for common setup | ❌ | ✅ |
| 5 | Scenario Outline + Examples for data variations | ❌ | ✅ |
| 6 | Exact messages in quotes | ❌ | ✅ |
| 7 | Business-level steps, not UI clicks | ❌ | ✅ |
| 8 | Boundaries for AC4 (minutes) and AC5 (password length) | ❌ | ❌ → ✅ after refinement |
| 9 | Invented rules or messages | None | None |
|  | **Score (1–8)** | **0/8** | **7/8 → 8/8 after refinement** |

## Refinement (step 4)
Prompt: "for every numeric limit, apply BVA with Scenario Outlines — just below, at, just above".
Result: added 29/30/31 minutes and 7/8/64/65 characters.

| Boundary | AI expected | PO decision | Verdict |
|---|---|---|---|
| Exactly 30:00 minutes | Expired | Still valid (expired from 30:01) | ❌ Silent assumption — corrected by tester |

## Findings
1. Few-shot transferred the house style almost perfectly (0/8 zero-shot → 7/8 few-shot) with the same story and model.
2. Few-shot teaches **format** reliably, but **technique** only if the examples make it explicit:
   Example 1 tested a boundary implicitly, yet no boundaries appeared for US-03.
3. One refinement instruction fixed it — the syllabus refine loop ("if results are inaccurate, refine the prompt or examples").
4. Better fix for next time: add an explicit BVA Scenario Outline to an example, so the technique is shown, not told.
5. The AI resolved an ambiguity ("expires after 30 minutes" at exactly 30:00) without flagging it. Boundary
   expectations must be checked against the PO, not accepted from the AI.
6. Output saved as features/password_reset.feature for BDD automation later (Behave).
