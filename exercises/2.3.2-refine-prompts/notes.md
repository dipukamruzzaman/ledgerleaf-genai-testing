# HO-2.3.2 — Evaluate and refine a prompt (A/B testing + iterative refinement)

**Syllabus link:** GenAI-2.3.2 (K2) · HO-2.3.2 (H1) · **Tool:** Ollama llama3.1:8b, temperature 0 · **Date:** 2026-10-27
**Scored against:** exercises/2.3.1-metrics/reference.md (R1–R10)

## Scorecard (✅ = condition present WITH correct expected result)
| Ref | Condition | A | B | B2 |
|---|---|---|---|---|
| R1 | 0.00 → Rejected | ✅ |  | ✅ |
| R2 | 0.01 → Accepted |  | ✅ | ✅ |
| R3 | 4,999.99 → Accepted |  |  | ✅ |
| R4 | 5,000.00 → Accepted | ✅ | ✅ | ✅ |
| R5 | 5,000.01 → Rejected |  | ✅ | ✅ |
| R6 | Negative → Rejected |  |  | ✅ |
| R7 | 3 decimals → Rejected |  |  | ✅ |
| R8 | > balance → Rejected |  |  | ✅ |
| R9 | = balance → Accepted |  |  | ✅ |
| R10 | Not a number → Rejected |  |  | ✅ |
| | **Recall** | **20%** | **30%** | **100%** |
| | Wrong expected results | 1 | 2 | 0 |
| | Invented rules/features | 1 | 2 | 0 |
| | Duplicates | 0 | 3 | 0 |

## Prompt versions
- **A (base):** one line, "maximum $5,000". No decimals in the rule → model used whole-dollar boundaries.
- **B (structured):** six-part prompt with all rules + "cover every partition once, no duplicates, do not invent".
- **B2 (refined):** B, with "cover every partition" replaced by an explicit list of the 10 required test conditions
  ("exactly one row for each … and no other rows").

## What I changed in B2 (and why)
The constraint clearly defined what the output should be: it listed the boundaries to consider, gave specific
guidance on decimals, and named the edge cases, negative and invalid cases.

## Findings
1. A/B testing with the same metrics made the comparison objective: A 20% → B 30% → B2 100% recall.
2. Structure alone (B) helped only where rules were explicit (decimal boundaries, inclusive maximum).
3. Abstract instructions ("cover every partition") and negative constraints ("no duplicates", "do not invent")
   were largely ignored by the 8B model; B even had more errors than A.
4. Output analysis → one targeted change (an explicit checklist) fixed recall, errors, invented rules and duplicates at once.
5. Trade-off: with an explicit checklist the human has done the test design — recall can no longer exceed the
   tester's own list, and the AI stops exploring conditions the tester didn't think of.
6. Single run at temperature 0; a real evaluation would repeat each prompt several times (non-determinism).
