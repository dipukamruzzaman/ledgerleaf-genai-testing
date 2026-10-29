# HO-4.1.2 — Experiment with RAG: "ask the requirements"

**Syllabus link:** GenAI-4.1.2 · HO-4.1.2 (H1) · **Tool:** tools/rag_backlog.py · **Models:** nomic-embed-text (embeddings), llama3.1:8b (answers) · **Date:** 2026-10-28
**Knowledge base:** docs/requirements/user-stories.md + docs/requirements/po-clarifications.md
Retrieval (right chunk?) and Generation (right, grounded answer?) scored separately.

## Oracle
| Q | Question | Correct answer | Right source |
|---|---|---|---|
| 1 | Maximum transfer amount | $5,000.00 per transfer, inclusive, no daily limit | US-05 + Clarifications for US-05 |
| 2 | Age to open an account | 18 or older | Clarifications for US-01 |
| 3 | Failed log-ins before lock | 3 consecutive | Clarifications for US-02 |
| 4 | How many payees | NOT FOUND | — |
| 5 | Transfer fee | NOT FOUND | — |
| 6 | Reset link validity | 30 minutes, single use | Clarifications for US-03 |

## Results (R = right chunk retrieved · A = answer correct)
| Q | Run 1: sections, top-3 — R | Run 1 — A | Run 2: 200 chars, top-1 — R | Run 2 — A |
|---|---|---|---|---|
| 1 | Y (clarification 0.770 + story 0.736) | ✅ | Y | ✅ |
| 2 | Y | ✅ | Y | ✅ |
| 3 | Y | ✅ | Y | ✅ |
| 4 | n/a (nothing to retrieve) | ✅ NOT FOUND | n/a | ✅ NOT FOUND |
| 5 | n/a | ✅ NOT FOUND | n/a | ✅ NOT FOUND |
| 6 | Y | ✅ | Y (po-clarifications.md#4, 0.832) | ⚠️ right fact, **wrong citation** |
| **Score** | | **6/6** | | **5/6 + 1 partly** |

(First draft marked Q6 run 2 as "not retrieved / wrong" and Q4/Q5 as "n" — corrected: the right chunk WAS retrieved;
the error was in the generated citation. For NOT FOUND questions there is no right chunk, so R is n/a.)

## Special checks
| Check | Result |
|---|---|
| Q1 conflict ("daily" in story vs "per transfer" in clarification) | Both runs answered "$5,000.00 [po-clarifications.md#5]" — used the clarification, but resolved the conflict **silently** and very briefly (did not say "per transfer, inclusive, no daily limit") |
| Q4/Q5 gaps | Both runs: "NOT FOUND IN THE DOCUMENTS" — no invented numbers |
| Citations | Run 1: all correct. Run 2 Q6: cited [user-stories.md#6] although the only retrieved chunk was po-clarifications.md#4 — a **hallucinated citation** |

## Findings
1. With clean, specific documents and a strict "answer only from context / else NOT FOUND" prompt, the 8B model
   answered 6/6 correctly and never invented a fee or a payee limit — grounding works much better here than
   in 3.1.2a, where the model had no retrieval and was asked to write content.
2. Scoring retrieval and generation separately located the only error precisely: retrieval was right,
   generation mis-cited. Without that split it would look like a retrieval problem.
3. Smaller chunks + top-1 reduced context and produced a citation pointing to a document that was not in the
   context — citations must be validated automatically against the retrieved set.
4. Conflicting sources were resolved silently. It was right here only because the clarification file states that
   it wins; a RAG system used for testing should flag conflicts in the test basis, not hide them.
5. RAG quality depends on the knowledge base: adding po-clarifications.md fixed the vague "adults", "too many
   attempts" and "reasonable time" answers that the stories alone could not give.
