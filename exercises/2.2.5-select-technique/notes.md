# HO-2.2.5 — Selecting context-appropriate prompting techniques

**Syllabus link:** GenAI-2.2.5 (K3) · HO-2.2.5 (H1) · **Date:** 2026-10-27

## Selection rule (syllabus 2.2.5)
| Task characteristic | Technique |
|---|---|
| Complex, needs precision, human verification at each step | Prompt chaining |
| Repetitive, or a specific/constrained output format (Gherkin, keyword scripts, report template) | Few-shot prompting |
| Flexible/new task, unsure how to craft the prompt (e.g. anomaly detection, report analysis) | Meta prompting |
| Large real-world task | Combine: meta → few-shot → chaining |

## Quiz — 6 test tasks
Score: **6 / 6** (previous technique quiz in 2.1.2b: 50%)

## My choice for a real task
**Task:** start testing the new Payees feature (US-06): refine ACs, write Gherkin in house style, team new to AI.

**My answer:** Meta prompting to generate the prompt, then prompt chaining to refine the ACs, and few-shot prompting
(with a few house-style examples) for the Gherkin scenarios.

**Why each:**
- Meta — the team has never done this with AI, so co-create the first prompt with the LLM.
- Chaining — refining ACs is complex and needs precision: ambiguities → testability → completeness, checked by a human at each step (as in 2.2.1b).
- Few-shot — Gherkin with house tags/Background is a constrained, repetitive format (2.2.2b: 0/8 zero-shot vs 7/8 few-shot).
- The few-shot Gherkin step is itself the final link of the chain, so the three techniques combine into one workflow.

## Findings
1. Choosing a technique is driven by the task's nature: precision vs repetitive format vs novelty.
2. Real tasks usually need a combination, in the order the syllabus gives: meta → few-shot → chaining.
3. Hands-on practice in 2.2.1–2.2.4 turned the technique quiz from 50% to 100%.
