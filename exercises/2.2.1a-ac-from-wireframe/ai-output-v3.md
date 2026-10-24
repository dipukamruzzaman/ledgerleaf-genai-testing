Acceptance Criteria

Display of Add a Payee Page and Components

Given the customer is logged in and navigates to the Payees section,

When they access the "Add a payee" page,

Then the page displays form fields for Payee name (), LedgerLeaf account number (), Nickname (optional), Payee type dropdown, a "Save as favourite" checkbox, an information message stating "New payees can receive up to $1,000 in the first 24 hours.", an "Add payee" button, a "Cancel" link, and a sidebar showing "Your payees" with the current count (e.g., 3 of 20).

Successful Addition of a Valid Payee

Given the customer is on the "Add a payee" page and has fewer than 20 payees,

When they enter a valid payee name (2–50 characters consisting of letters, spaces, hyphens, and apostrophes), a valid existing LedgerLeaf account number in NNN-NNN format belonging to another customer, an optional nickname (up to 20 characters), select a payee type, and click "Add payee",

Then the payee is successfully added, the payee list count updates, and the new payee appears in the "Your payees" sidebar.

Payee Name Character and Length Validation

Given the customer is on the "Add a payee" page,

When they enter a payee name shorter than 2 characters, longer than 50 characters, or containing numbers/invalid special characters,

Then the system displays a validation error and prevents the form from being submitted.

Account Number Format Validation

Given the customer is on the "Add a payee" page,

When they enter a LedgerLeaf account number that does not follow the NNN-NNN format,

Then the system displays a validation error and prevents the form from being submitted.

Non-Existent Account Number Validation

Given the customer is on the "Add a payee" page,

When they enter a LedgerLeaf account number that does not exist in the system,

Then an error is shown indicating that the account number doesn't exist and the payee cannot be added.

Self-Account Restriction Validation

Given the customer is logged in with their account,

When they enter their own LedgerLeaf account number into the account number field,

Then the system displays an error and prevents them from adding their own account as a payee.

Nickname Length Validation

Given the customer is on the "Add a payee" page,

When they enter a nickname exceeding 20 characters,

Then the system displays a validation error and prevents the form from being submitted.

Maximum Payee Limit Enforcement

Given the customer already has the maximum limit of 20 payees saved,

When they attempt to add a new payee,

Then the system prevents adding the payee and displays an error message.

Cancel Action Functionality

Given the customer is on the "Add a payee" page,

When they click the "Cancel" link,

Then the action is cancelled and they are navigated away from the form without saving a new payee.

Open questions for the PO
Can a customer add the exact same payee/account twice (as noted in the wireframe sticky note)?

What specific error messages should be displayed for each validation failure (e.g., invalid name format, non-existent account number, self-account addition, exceeding 20 payees)?

What other options are available in the "Payee type" dropdown besides "Person", and what is the default selected value?

Where is the customer redirected or what UI state is shown upon successfully adding a payee?