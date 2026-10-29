# Product Owner clarifications (Release 1.0 / 1.1)

These answers were given by the Product Owner during refinement. Where they differ from the
original user stories, the clarification wins.

## Clarifications for US-01 Open an account
- "Adult" means 18 or older on the day of registration (the 18th birthday counts), using the bank's
  local date (Eastern Time).
- Password: 8 to 64 characters, at least one upper-case letter, one lower-case letter and one digit.
  Special characters are allowed but not required.
- The duplicate-email check is case-insensitive.

## Clarifications for US-02 Log in
- The account is locked after 3 consecutive failed log-in attempts.

## Clarifications for US-03 Reset password
- A reset link is valid for 30 minutes (still valid at exactly 30:00, expired from 30:01) and can be used only once.

## Clarifications for US-05 Transfer money
- The limit is $5,000.00 PER TRANSFER and is inclusive (exactly $5,000.00 is allowed).
  There is NO daily limit in Release 1.0 — the "daily limit" in the original story is wrong.
- The minimum amount is $0.01.
- Transfers to the same account or to an account number that does not exist are rejected.
