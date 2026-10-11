# LedgerLeaf Bank — GenAI-Assisted Testing Project

A complete software-testing project in which **Generative AI is used as a testing assistant** across the whole test process: analysis, design, automation, monitoring, risk management and adoption.

The system under test is **LedgerLeaf Bank**, a small fictional online-banking web app with a UI and a JSON API.

> Aligned with the learning objectives of the ISTQB® Certified Tester – Testing with Generative AI (CT-GenAI) syllabus v1.1. This is an independent project; it is not affiliated with or endorsed by ISTQB®.

## What is inside

| Folder | Contents |
|---|---|
| `app/` | LedgerLeaf Bank (Flask): login, registration, password reset, accounts, transfers |
| `docs/requirements/` | Product backlog (the test basis) |
| `docs/wireframes/` | Wireframes used for multimodal prompting |
| `prompts/` | Reusable prompt library |
| `exercises/` | One folder per hands-on exercise: prompts, AI output, review notes |
| `tests/` | Automated tests (pytest, Behave, Robot Framework) |
| `test-data/` | Synthetic test data generated with GenAI |
| `reports/` | Test reports, metrics and analyses |

## Run the app

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app/app.py
```
Open http://127.0.0.1:5000 and log in as `alex.tester@ledgerleaf.test` / `Passw0rd!`.

Run the smoke tests: `python -m pytest -q`

## Useful endpoints
| Endpoint | Purpose |
|---|---|
| `/outbox` | Simulated mailbox showing password-reset emails |
| `POST /api/test/reset` | Restore the demo data before a test run |
| `POST /api/login`, `POST /api/register`, `GET /api/accounts/<email>`, `POST /api/transfers`, `POST /api/password-reset` | JSON API |

## Author
Md Kamruzzaman — dipukamruzzaman1@gmail.com · [LinkedIn](https://www.linkedin.com/in/kamruzzaman-sqa) · [GitHub](https://github.com/dipukamruzzaman) · [Portfolio](https://mk-qa-engineer.netlify.app/)
