# HO-2.2.1a — Three prompt versions (attach add-payee-wireframe.png to EVERY one)

Run each version in a NEW chat (ChatGPT or Gemini). Save each answer as ai-output-v1.md, -v2.md, -v3.md.

---

## V1 — Minimal (image only)
```text
Write acceptance criteria for this screen.
```

---

## V2 — Structured prompt: image + user story
```text
ROLE: You are a senior test analyst on an agile team at a retail bank.

CONTEXT: LedgerLeaf Bank is a fictional online bank used for test practice. Release 1.1
adds a "Payees" feature. The attached image is the approved wireframe for the
"Add a payee" page. Yellow sticky notes are comments from the designer.

INSTRUCTION: Write acceptance criteria for the user story below, using both the user
story and the wireframe.

INPUT – User story US-06 Add a payee
As a logged-in customer, I want to add another LedgerLeaf customer as a payee so that
I can send them money later without retyping their details.

CONSTRAINTS:
- Cover only adding a payee. Do not write criteria for editing or deleting payees.
- Do not invent values (lengths, limits, formats) that are not in the story or the wireframe.
- Tag each criterion with its source: [Story], [Wireframe] or [Assumption].
- If something is unclear, add it to "Open questions for the PO" instead of guessing.

OUTPUT FORMAT:
1. Numbered acceptance criteria in Given / When / Then form.
2. A list titled "Open questions for the PO".
```

---

## V3 — V2 + business rules (text)
Copy V2 exactly, and add this block just before CONSTRAINTS:
```text
BUSINESS RULES (confirmed by the PO):
- Payee name: 2–50 characters; letters, spaces, hyphens and apostrophes only.
- Account number: format NNN-NNN; must be an existing LedgerLeaf account;
  a customer cannot add their own account as a payee.
- Nickname: optional, at most 20 characters.
- A customer can have at most 20 payees.
```
Also change the source tags to: [Story], [Wireframe], [Rules] or [Assumption].

ROLE: You are a senior test analyst on an agile team at a retail bank.

CONTEXT: LedgerLeaf Bank is a fictional online bank used for test practice. Release 1.1
adds a "Payees" feature. The attached image is the approved wireframe for the
"Add a payee" page. Yellow sticky notes are comments from the designer.

INSTRUCTION: Write acceptance criteria for the user story below, using both the user
story and the wireframe.

INPUT – User story US-06 Add a payee
As a logged-in customer, I want to add another LedgerLeaf customer as a payee so that
I can send them money later without retyping their details.

BUSINESS RULES (confirmed by the PO):
- Payee name: 2–50 characters; letters, spaces, hyphens and apostrophes only.
- Account number: format NNN-NNN; must be an existing LedgerLeaf account;
  a customer cannot add their own account as a payee.
- Nickname: optional, at most 20 characters.
- A customer can have at most 20 payees.

CONSTRAINTS:
- Cover only adding a payee. Do not write criteria for editing or deleting payees.
- Do not invent values (lengths, limits, formats) that are not in the story or the wireframe.
- Tag each criterion with its source: [Story], [Wireframe] [Rules] or [Assumption].
- If something is unclear, add it to "Open questions for the PO" instead of guessing.

OUTPUT FORMAT:
1. Numbered acceptance criteria in Given / When / Then form.
2. A list titled "Open questions for the PO