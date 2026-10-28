# HO-4.2.1 — Observe a fine-tuning process

**Syllabus link:** GenAI-4.2.1 · HO-4.2.1 (H0) · **Input:** walkthrough.md, train.jsonl · **Date:** 2026-10-28
Process observed: select model (Llama 3.2 3B + LoRA) → dataset (train.jsonl) → framework (Hugging Face TRL/PEFT) → prompt and discuss output.

## 1. Bad training examples
| Example id | What is wrong | What the fine-tuned model would learn |
|---|---|---|
| 4 | Contradicts its own input: AC2 says $5,000.00 is allowed (inclusive), the scenario expects it to be **rejected** — it encodes DEF-001 as correct behaviour | To ignore the constraint in the story and reproduce the bug's behaviour in future tests (same trap as 2.3.1 test #3) |
| 5 | Not Gherkin: plain-text UI clicks, no tags, no exact message | That the house format is optional; inconsistent output |

## 2. Questions
| Question | Answer |
|---|---|
| Why hold back 20% as a test split? | To evaluate the model on data it has never seen — during training (eval loss per epoch) and after — so overfitting becomes visible |
| Train loss falls, eval loss rises after epoch 2? | Overfitting: the model memorises the training examples. Stop earlier (fewer epochs) and add more, more varied, high-quality data |
| Few-shot reached 8/8 in 2.2.2b — when is fine-tuning still worth it? | Very high volume (examples re-sent in every prompt cost tokens), many conventions that don't fit in a prompt, and when a small/offline model must behave consistently |

## 3. Output of the fine-tuned model for US-05 AC2 (my guess = expected result)
```gherkin
@US-05 @AC2
Scenario: Transfer of exactly the maximum is rejected
  Given the customer "alex.tester@ledgerleaf.test" is logged in
  When the customer transfers "5000.00" from "100-001" to "100-002"
  Then the message "The maximum per transfer is $5,000.00." is shown
```
Perfect house style — and a wrong expected result learned from example 4.

## Findings
1. Fine-tuning reproduces whatever is in the training data — style and errors alike ("garbage in, garbage out").
2. One wrong example is enough to bake a known defect into every future test for that rule, with no prompt to blame (opacity).
3. Training data must be reviewed against the test basis before training — data quality is the main risk, not the code.
4. Held-out evaluation data and eval loss are the guard against overfitting.
5. Few-shot already achieved the house style; fine-tuning is an optimisation for scale, consistency and cost — not a first step.
