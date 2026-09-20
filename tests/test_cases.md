# Test Cases

## 1. Customer Management Testing

| Test ID | Test Case | Input | Expected Result | Status |
|--------|-----------|-------|-----------------|--------|
| C001 | Add valid customer | Valid name, email and mobile | Customer added successfully | PASS |
| C002 | Empty customer name | Empty name | Error message displayed | PASS |
| C003 | Invalid customer name | `chahat123` | Error message displayed | PASS |
| C004 | Invalid email | `bubby@` | Error message displayed | PASS |
| C005 | Invalid mobile | `fd` | Error message displayed | PASS |
| C006 | Incorrect mobile length | 9-digit number | Error message displayed | PASS |
| C007 | Duplicate email | Existing email | Duplicate email error | PASS |
| C008 | Duplicate mobile | Existing mobile | Duplicate mobile error | PASS |
| C009 | Search by customer ID | `C001` | Correct customer displayed | PASS |
| C010 | Search by name | `chahat` | Matching customers displayed | PASS |
| C011 | Search by email | `chahat@gmail.com` | Correct customer displayed | PASS |
| C012 | Search by mobile | `9963747969` | Correct customer displayed | PASS |
| C013 | Search invalid customer | `C999` | Customer not found | PASS |
| C014 | Update customer | Update C001 | Customer updated successfully | PASS |
| C015 | Update invalid customer | `C999` | Error message displayed | PASS |

---

## 2. Support Agent Management Testing

| Test ID | Test Case | Input | Expected Result | Status |
|--------|-----------|-------|-----------------|--------|
| A001 | View support agents | View option | All agents displayed | PASS |
| A002 | Add valid agent | Valid agent details | Agent added successfully | PASS |
| A003 | Empty agent name | Empty name | Error message displayed | PASS |
| A004 | Invalid agent name | `9` | Error message displayed | PASS |
| A005 | Invalid email | `nani@gmail` | Error message displayed | PASS |
| A006 | Invalid specialization | Invalid choice | Error message displayed | PASS |
| A007 | Invalid availability | Invalid choice | Error message displayed | PASS |
| A008 | Duplicate email | Existing email | Duplicate email error | PASS |
| A009 | Search by agent ID | `A005` | Correct agent displayed | PASS |
| A010 | Search by name | `nani` | Matching agent displayed | PASS |
| A011 | Search by email | Agent email | Correct agent displayed | PASS |
| A012 | Search by specialization | `Billing` | Matching agents displayed | PASS |
| A013 | Search invalid agent | `A999` | Agent not found | PASS |
| A014 | Update agent | Update valid agent | Agent updated successfully | PASS |
| A015 | Update invalid agent | `A999` | Error message displayed | PASS |
| A016 | Remove agent | Valid agent | Agent removed successfully | PASS |
| A017 | Cancel removal | `N` | Removal cancelled | PASS |

---

## 3. Ticket Management Testing

| Test ID | Test Case | Input | Expected Result | Status |
|--------|-----------|-------|-----------------|--------|
| T001 | Create valid ticket | Valid ticket details | Ticket created successfully | PASS |
| T002 | Invalid customer ID | `C999` | Customer not found | PASS |
| T003 | Empty subject | Empty subject | Error message displayed | PASS |
| T004 | Empty description | Empty description | Error message displayed | PASS |
| T005 | Invalid category | Invalid choice | Error message displayed | PASS |
| T006 | Invalid priority | Invalid choice | Error message displayed | PASS |
| T007 | Automatic assignment | Valid category | Matching agent assigned automatically | PASS |
| T008 | View tickets | View option | Tickets displayed | PASS |
| T009 | Search by ticket ID | `T003` | Correct ticket displayed | PASS |
| T010 | Search by customer ID | `C001` | Matching tickets displayed | PASS |
| T011 | Search by subject | `fan problem` | Matching ticket displayed | PASS |
| T012 | Search by category | `Technical` | Matching tickets displayed | PASS |
| T013 | Search by priority | `High` | Matching tickets displayed | PASS |
| T014 | Search by status | `Open` | Matching tickets displayed | PASS |
| T015 | Search by assigned person | `Arjun` | Matching tickets displayed | PASS |
| T016 | Search invalid ticket | `T999` | Ticket not found | PASS |
| T017 | Change priority | T003 | Priority changed successfully | PASS |
| T018 | Change closed ticket priority | T002 | Modification rejected | PASS |
| T019 | Update status | T003 | Status updated successfully | PASS |
| T020 | Invalid status | Invalid choice | Error message displayed | PASS |
| T021 | Update closed ticket | T002 | Modification rejected | PASS |
| T022 | Add resolution | T003 | Resolution added successfully | PASS |
| T023 | Empty resolution | Empty input | Error message displayed | PASS |
| T024 | Add resolution to closed ticket | T002 | Modification rejected | PASS |
| T025 | Close ticket without resolution | T001 | Closing rejected | PASS |
| T026 | Close ticket with resolution | T001 | Ticket closed successfully | PASS |
| T027 | Close already closed ticket | T003 | Error message displayed | PASS |
| T028 | Close invalid ticket | `T999` | Ticket not found | PASS |
| T029 | View ticket history | T003 | Complete history displayed | PASS |
| T030 | View invalid ticket history | `T999` | Ticket not found | PASS |

---

## 4. Reports Testing

| Test ID | Report | Expected Result | Status |
|--------|--------|-----------------|--------|
| R001 | Open Tickets | T001 displayed | PASS |
| R002 | Closed Tickets | T002 and T003 displayed | PASS |
| R003 | High-Priority Tickets | T001, T002 and T003 displayed | PASS |
| R004 | Tickets by Category | Correct category tickets displayed | PASS |
| R005 | Tickets by Assigned Person | Correct assigned tickets displayed | PASS |
| R006 | Ticket Summary | Correct ticket counts displayed | PASS |

### Final Ticket Summary

- Total Tickets: 3
- Open Tickets: 1
- In Progress Tickets: 0
- Resolved Tickets: 0
- Closed Tickets: 2
- Low Priority: 0
- Medium Priority: 0
- High Priority: 2
- Critical Priority: 1

---

## 5. Validation Testing

The application validates:

- Customer IDs
- Ticket IDs
- Support Agent IDs
- Customer names
- Agent names
- Email addresses
- Mobile numbers
- Ticket subjects
- Ticket descriptions
- Categories
- Priorities
- Status values
- Resolution text
- Menu choices

Invalid inputs display appropriate error messages instead of causing the application to terminate unexpectedly.

---

## 6. Exception Handling Testing

The application handles common file-related exceptions including:

- `FileNotFoundError`
- `JSONDecodeError`
- `OSError`
- General exceptions

Invalid or missing JSON data is handled without crashing the application.

---

## 7. File Persistence Testing

| Test | Action | Expected Result | Status |
|------|--------|-----------------|--------|
| P001 | Add/update customer and restart | Data remains available | PASS |
| P002 | Create/update ticket and restart | Data remains available | PASS |
| P003 | Add/update agent and restart | Data remains available | PASS |
| P004 | Load JSON files | Data loaded successfully | PASS |

The project uses JSON files for persistent data storage.

---

## 8. Navigation Testing

| Test ID | Test | Expected Result | Status |
|--------|------|-----------------|--------|
| N001 | Customer Management → Back | Returns to Main Menu | PASS |
| N002 | Support Agent Management → Back | Returns to Main Menu | PASS |
| N003 | Ticket Management → Back | Returns to Main Menu | PASS |
| N004 | Reports → Back | Returns to Ticket Management | PASS |
| N005 | Main Menu → Exit | Application terminates normally | PASS |

---

## 9. Final Testing Result

All major functional requirements were tested successfully.

### Overall Result

**STATUS: PASS**

The Customer Support Ticket Management System successfully passed functional testing, validation testing, exception handling testing, file persistence testing, report testing, and navigation testing.