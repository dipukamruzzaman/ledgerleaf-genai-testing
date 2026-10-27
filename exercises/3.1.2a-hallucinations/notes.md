# HO-3.1.2a — Experiment with GenAI hallucinations

**Syllabus link:** GenAI-3.1.2 · HO-3.1.2a (H1) · **Models:** llama3.2:3b, llama3.1:8b (temperature 0) · **Date:** 2026-10-27

Truth: Q1 no fee exists · Q2 no scheduled transfers · Q3 there is no AC8 (only AC1–AC7) · Q4 $5,000.00 (control)
V1 = plain questions · V2 = + "Use ONLY the story … otherwise reply NOT IN THE STORY"

## Results — H = hallucinated · ✅ = said not in the story / correct
| Question | 3b V1 | 3b V2 | 8b V1 | 8b V2 |
|---|---|---|---|---|
| Q1 Fee over $1,000 | ✅ | ✅ | ✅ | ✅ |
| Q2 Scheduled transfers | ✅ | ✅ | ✅ | ✅ |
| Q3 Test cases for AC8 | H | H | H | H |
| Q4 Max per transfer (control) | ✅ | No answer | ✅ | ✅ |
| **Hallucinations** | 1 | 1 | 1 | 1 |

## Most convincing hallucination
> "Here are two test cases for AC8 (which is not explicitly mentioned in the provided acceptance criteria,
> so I'll assume it's a typo and it should be AC7):"

The model noticed AC8 does not exist — and then produced test cases anyway, based on its own assumption.
In V2 this also broke an explicit instruction ("reply NOT IN THE STORY").

## Findings
1. Factual questions about non-existent things (fee, scheduled transfers) were answered honestly by both models, even in V1.
2. **Task-shaped requests ("write test cases for AC8") triggered hallucination in every run** — the pressure to deliver
   output beats the instruction to admit missing information.
3. The grounding instruction (V2) did not fix the Q3 hallucination on either model.
4. With the grounding instruction, the 3b model did not answer the control question (Q4) correctly — a strict
   grounding prompt can also cause missed correct answers.
5. "I'll assume it's a typo" is a dangerous pattern: a test case for the wrong AC looks valid and would be traced
   to a requirement that does not exist.
6. Mitigation: verify every AI-generated artefact against the test basis (traceability check), not just the prompt.
