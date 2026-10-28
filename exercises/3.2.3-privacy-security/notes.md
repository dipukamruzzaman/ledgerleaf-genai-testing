# HO-3.2.3 — Recognize data privacy and security risks in a GenAI-for-testing case study

**Syllabus link:** GenAI-3.2.x · HO-3.2.3 (H0) · **Input:** case-study.md · **Date:** 2026-10-27

## Answer key vs my first attempt
| Event | Risk | Syllabus category | Mitigation (3.2.3) | My first attempt |
|---|---|---|---|---|
| 0 (intro) | No AI policy, no training | Missing training / policy | Training & policies | ✅ (added as my row 1) |
| 1 | Production customer data pasted into a public chatbot | Unintentional data exposure + compliance risk (privacy law) | Data minimization; anonymization / synthetic test data; approved tool only | ✅ |
| 2 | Free-plan terms allow storing and training on inputs | Lack of control over data usage | Secure operational environment (commercial secure offering, secure cloud or on-premises) | 🟠 (called it compliance/training) |
| 3 | Production log with session tokens and payment API key pasted | Unintentional data exposure (secrets) | Data minimization: redact/mask secrets before sharing; rotate the leaked key | 🟠 (right idea, wrong category) |
| 4 | Generated code sends session cookies to an external IP; committed unreviewed | Malicious code generation (backdoor / data exfiltration) | Systematic review of generated output; security scanning | ✅ |
| 5 | Hidden text in a wiki page makes the RAG assistant report "all tests passed" | **Request manipulation** (indirect prompt injection) | Review output against source data; access control on wiki edits; monitoring | ❌ (I said context manipulation) |
| 6 | Leaving contractor gives fake 5-star ratings used for fine-tuning | Data poisoning | Access control and review of feedback data; audits | ✅ category / 🟠 mitigation |
| 7 | 300-page paste makes the assistant leak HR salary fragments | **Context manipulation** | Access control on indexed data; monitoring; regular security audits | ❌ (I said lack of control) |
| 8 | QA Assistant API has no authentication | Unauthorized access to LLM-powered test infrastructure | Access control; regular security audits | Missing (rows shifted) |

## Exam trap: context vs request manipulation
- **Context manipulation** = overload the context window (very long input) to make the AI reveal data → secrets come **out**.
- **Request manipulation** = input data that disrupts / misleads the output (hidden text, misleading images) → bad output goes **in**.

## Findings
1. Most incidents came from people, not the model: no policy, no training, no review.
2. Two privacy leaks (events 1, 3) were avoidable with data minimization and redaction before prompting.
3. Generated code must be reviewed like any third-party code — it can contain exfiltration backdoors.
4. RAG assistants inherit the trust level of their sources: anyone who can edit the wiki can steer the output.
5. Feedback used for fine-tuning is an attack surface (data poisoning) and needs access control.
6. Learn the syllabus attack-vector names precisely; my intuition swapped context and request manipulation.
