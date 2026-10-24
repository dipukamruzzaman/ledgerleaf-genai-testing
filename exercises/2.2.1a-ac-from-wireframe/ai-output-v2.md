Acceptance Criteria
Given a customer is logged in, when they navigate to the "Add a payee" page, then they should see the "Add a payee" form containing mandatory fields for "Payee name" and "LedgerLeaf account number", an optional "Nickname" field, a "Payee type" dropdown, a "Save as favourite" checkbox, an informational note stating that new payees can receive up to $1,000 in the first 24 hours, and "Add payee" and "Cancel" buttons [Wireframe].

Given a logged-in customer is on the "Add a payee" page, when they enter valid details for the required fields and click the "Add payee" button, then the payee is successfully added so that the customer can send them money later without retyping their details [Story, Wireframe].

Given a customer is on the "Add a payee" page, when they enter a LedgerLeaf account number that does not exist and submit, then an error is shown [Wireframe].

Given a customer is on the "Add a payee" page, when they click the "Cancel" button, then the add payee action is aborted/exited [Wireframe].

Open questions for the PO
Can a customer add the same payee twice (e.g., duplicate account numbers or duplicate names)? [Wireframe]

What is the system behavior and restriction when a user reaches the maximum limit of 20 payees (indicated as "3 of 20") and attempts to add another? [Wireframe]

What are the specific validation rules, character limits, or accepted formats for "Payee name", "LedgerLeaf account number", and "Nickname"? [Wireframe]

What exact options are included in the "Payee type" dropdown selection besides "Person"? [Wireframe]

What is the exact error message text that should be displayed when a non-existent account number is entered? [Wireframe]