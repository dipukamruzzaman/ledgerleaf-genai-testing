# HO-3.3.1 — Energy and CO₂ of GenAI test tasks (simulator)

**Syllabus link:** GenAI-3.3.1 · HO-3.3.1 (H1) · **Simulator:** EcoLogits calculator, Expert mode
(https://huggingface.co/spaces/genai-impact/ecologits-calculator) · **Date:** 2026-10-27
**Models:** Small = Mistral Small · Large = Mistral Large (same provider, so model size is the main difference)

## Step 1 — Single requests
| Test task (from this project) | Output tokens | Small: Wh | Small: gCO₂eq | Large: Wh | Large: gCO₂eq |
|---|---|---|---|---|---|
| T1 Quick question | 100 | 0.026 | 0.013 | 0.320 | 0.162 |
| T2 Regression report analysis (2.2.3b) | 800 | 0.201 | 0.098 | 2.45 | 1.22 |
| T3 Generate 15 test cases (2.2.2a) | 1,500 | 0.376 | 0.183 | 4.58 | 2.29 |
| T4 Reasoning-model estimate incl. thinking (3.1.2b) | 10,000 | 2.5 | 1.21 | 30.4 | 15.2 |

## Step 2 — One QA team, one year (10 testers × 50 requests/day × 220 days = 110,000 requests, average = T3)
| | Small (Mistral Small) | Large (Mistral Large) |
|---|---|---|
| Energy per year | 0.376 Wh × 110,000 = **41.4 kWh** | 4.58 Wh × 110,000 = **503.8 kWh** |
| CO₂ per year | 0.183 g × 110,000 = **20.1 kg** | 2.29 g × 110,000 = **251.9 kg** |

## Step 3 — What changed the result most?
| Factor | Effect in the data |
|---|---|
| Output tokens | Linear: 100× more tokens (100 → 10,000) ≈ 96× more energy |
| Model size | Large vs small, same tokens ≈ **12×** more energy and CO₂ |
| Reasoning ("thinking") tokens | T4 vs T3 ≈ 6.7× more — one reasoning request on the large model ≈ 30 Wh |

## Findings
1. Energy scales almost linearly with output tokens — verbose answers and "thinking" tokens have a real cost.
2. Model size multiplies everything: the large model used ~12× the energy for the same task.
3. One request is negligible; the team-year is not: ~504 kWh and ~252 kg CO₂ with the large model vs ~41 kWh / ~20 kg with the small one.
4. Best practices (syllabus): limit unnecessary interactions, use the smallest model that does the job, ask for concise
   output, and reserve reasoning models for tasks that need them (3.1.2b showed they don't guarantee better answers).
5. These are simulator estimates; real figures depend on hardware, data centre and energy mix.
