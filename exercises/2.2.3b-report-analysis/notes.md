# HO-2.2.3b — Structured prompts for regression report analysis

**Syllabus link:** GenAI-2.2.3 (K3) · HO-2.2.3b (H2) · **Tool:** <chatbot> · **Date:** 2026-10-26
**Input:** test-spec.md (20 tests) · regression-report.txt (build 1.0.2) · known-anomalies.md
**Chain (one conversation):** results vs spec → cluster failures → update known anomalies → cross-check + go/no-go

## Trap scorecard (AI vs answer key)
| # | Trap | Correct answer | AI | Result |
|---|---|---|---|---|
| 1 | Count spec tests only | 19 executed, 11 passed, 8 failed | 19 / 11 (57.9%) / 8 | ✅ |
| 2 | Spec test not executed | TC-API-03 (Critical!) | TC-API-03, headline item | ✅ |
| 3 | Executed test not in spec | TC-99 debug_print_session | TC-99 | ✅ |
| 4 | Report SUMMARY "20 run" misleading | Counts TC-99, hides missing TC-API-03 | Counted independently | ✅ |
| 5 | Product-defect clusters | 4: age, lockout, $5,000, API negative amount | DEF-001…DEF-004 | ✅ |
| 6 | TC-02-03 / TC-02-05 / TC-03-04 | One root cause (lockout), 3 symptoms | One defect (DEF-003) | ✅ |
| 7 | TC-04-01 / TC-04-02 ConnectionError | Environment, not a defect | Environment | ✅ |
| 8 | Flaky test | TC-05-08 (passed only on retry) | FLAKY-001 | ✅ |
| 9 | DEF-000 (log-out link) | Fixed – close (TC-NAV-01 passes) | Fixed – close | ✅ |
| 10 | New defects | Age check, lockout, API negative amount | DEF-002, DEF-003, DEF-004 | ✅ |
| 11 | Go / no-go | No-go | No-go, risk-based reasons | ✅ |
| | **Score** | | | **11 / 11** |

## Updated known anomalies (after build 1.0.2)
| ID | Summary | Status |
|---|---|---|
| DEF-000 | Log-out link missing on the Transfer page | Fixed – close |
| DEF-001 | Transfer of exactly $5,000.00 rejected | Confirmed open |
| DEF-002 | 17-year-old can register | New |
| DEF-003 | Account not locked at the 3rd failed attempt (3 failing tests) | New |
| DEF-004 | API accepts a negative transfer amount | New |
| OBS-001 | Confirmation has no thousands separator | Open question to PO |
| FLAKY-001 | TC-05-08 memo transfer — timeout on attempt 1 | Watch |

## Human review — what I would sharpen
1. "8 failed, 57.9% pass rate" mixes product and environment failures: really 6 product failures + 2 blocked.
   Reporting them together makes the build look worse and hides that a rerun is needed.
2. US-04 had **zero** effective coverage this run (TC-04-01/02 blocked, TC-API-03 not executed).
   The AI reported each item but did not connect them.
3. Action: fix the environment and rerun TC-04-01, TC-04-02, TC-API-03 before the meeting.

## Findings
1. Structured prompts with explicit rules ("count yourself", "do not log environment failures as defects",
   "flaky → Watch") produced an accurate analysis: 11/11 traps handled.
2. Linking the steps in one conversation let each step reuse the previous result (clusters → anomalies → cross-check).
3. Contrast with 2.2.2c: there the AI's reasoning broke its own strategy; here explicit rules kept it on track.
   Rules in the prompt matter more than the model's "judgement".
4. The AI is good at classification; the human still adds synthesis (US-04 coverage gap) and audience framing
   (product vs environment failures).
