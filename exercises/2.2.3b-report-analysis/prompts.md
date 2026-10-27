# HO-2.2.3b — Structured prompts for regression report analysis (ONE chat, 4 linked steps)

## Step 1 — Results vs specification
```text
ROLE: You are a senior test analyst preparing the regression summary for a release meeting.

CONTEXT: LedgerLeaf Bank (fictional test app), build 1.0.2, nightly regression run.

INSTRUCTION: Compare the regression report with the test specification.

INPUT DATA:
--- TEST SPECIFICATION ---
<paste test-spec.md>
--- REGRESSION REPORT ---
<paste regression-report.txt>

CONSTRAINTS:
- Base every statement on the input data only; quote the test ID for every claim.
- Do not trust the report's own SUMMARY line — count yourself.

OUTPUT FORMAT:
1. Table: | Metric | Value | — specified tests, executed spec tests, passed, failed,
   spec tests NOT executed, executed tests NOT in the spec.
2. Table of failed tests: | ID | Risk | Failure message (short) |
```

## Step 2 — Cluster the failures
```text
Cluster the failed tests by likely ROOT CAUSE (not by symptom).
For each cluster: | Cluster | Test IDs | Likely root cause | Type: Product defect / Environment / Test issue | Evidence |
Each failed test must be in exactly one cluster. Also list tests that look flaky, with evidence.
```

## Step 3 — Update the known anomalies list
```text
Here is the known anomalies list before this build:
<paste known-anomalies.md>

Produce the UPDATED list: | ID | Summary | Status (Open / Confirmed open / Fixed – close / New) | Linked tests | Evidence |
Rules: confirm known defects that still fail, propose closing those whose tests now pass,
add new product defects (IDs DEF-002, DEF-003 …), do NOT log environment failures as defects,
and add flaky tests as FLAKY-001 … with status "Watch".
```

## Step 4 — Cross-check
```text
Cross-check your own answers from steps 1–3:
- Do the counts in step 1 add up? (passed + failed = executed)
- Is every failed test in exactly one cluster, and every product-defect cluster in the anomalies list?
- Is any Critical or High risk test missing from the results?
List every inconsistency you find, then give a 5-line summary for the release meeting
with a go / no-go recommendation and the reason.
```
