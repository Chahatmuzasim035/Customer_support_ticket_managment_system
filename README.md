# CUSTOMER SUPPORT TICKET MANAGEMENT SYSTEM

## 1. Project Overview

The **Customer Support Ticket Management System** is a Python-based console application designed to manage customer support requests efficiently.

The system allows users to manage customers, support agents, and support tickets. It provides features for creating, searching, updating, assigning, resolving, and closing tickets while maintaining data using JSON files.

The project demonstrates important Python programming concepts such as **Object-Oriented Programming, file handling, validation, exception handling, data structures, functions, and modular programming**.

---

## 2. Problem Statement

Companies receive multiple customer support requests that need to be recorded, prioritized, assigned, tracked, and resolved.

Managing these requests manually can make it difficult to track ticket status, assigned support agents, customer information, and resolutions.

This project provides a simple console-based system to organize and manage customer support tickets.

---

## 3. Objectives

The main objectives of this project are:

- Manage customer information.
- Manage support agent information.
- Create and manage support tickets.
- Automatically assign tickets to suitable support agents.
- Track ticket priority and status.
- Record ticket resolutions.
- Maintain ticket history.
- Generate useful ticket reports.
- Validate user input.
- Handle file-related exceptions.
- Store data permanently using JSON files.

---

## 4. Key Features

### Customer Management

- Add Customer
- View Customers
- Search Customers
- Update Customer
- Validate customer name, email, and mobile number
- Prevent duplicate email and mobile numbers

### Support Agent Management

- Add Support Agent
- View Support Agents
- Search Support Agent
- Update Support Agent
- Remove Support Agent
- Validate agent details
- Manage agent specialization and availability

### Ticket Management

- Create Ticket
- View Tickets
- Search Tickets
- Change Ticket Priority
- Update Ticket Status
- Add Resolution
- Close Ticket
- View Ticket History

### Automatic Ticket Assignment

When a ticket is created, the system automatically assigns it to an available support agent based on the ticket category and agent specialization.

If no matching specialist is available, the system assigns another available agent.

If no agent is available, the ticket is marked as **Not Assigned**.

### Reports

The system provides:

- Open Tickets
- Closed Tickets
- High-Priority Tickets
- Tickets by Category
- Tickets by Assigned Person
- Ticket Summary

---

## 5. Technologies Used

- **Programming Language:** Python
- **Data Storage:** JSON
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

No external database is required.

---

## 6. Python Concepts Used

The project demonstrates the following Python concepts:

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- Classes and objects
- Object-Oriented Programming
- Modules and imports
- File handling
- JSON handling
- Exception handling
- Regular expressions
- Input validation
- String operations
- Date and time handling

---

## 7. Project Structure

```text
Customer_support_ticket_managment_system
│
├── main.py
├── README.md
│
├── data
│   ├── agents.json
│   ├── customers.json
│   ├── support_agents.json
│   └── tickets.json
│
├── modules
│   ├── __init__.py
│   ├── customer.py
│   ├── ticket.py
│   └── support_agent.py
│
└── tests
    └── test_cases.md
File Description
main.py – Main application containing menus, functions, validation, business logic, and program flow.
customer.py – Contains the Customer class.
ticket.py – Contains the Ticket class.
support_agent.py – Contains the SupportAgent class.
customers.json – Stores customer information.
support_agents.json – Stores support agent information.
tickets.json – Stores ticket information.
test_cases.md – Contains project testing documentation.
README.md – Contains project documentation.



 8. Module Description
Customer Module

The Customer module manages customer information.

Each customer contains:

Customer ID
Name
Email
Mobile Number

The Customer class also provides a to_dict() method to convert customer objects into dictionary format for JSON storage.

Ticket Module

The Ticket module represents support tickets.

Each ticket contains:

Ticket ID
Customer ID
Subject
Description
Category
Priority
Assigned Person
Status
Created Date
Closed Date
Resolution
Comment
History
Last Updated
Support Agent Module

The Support Agent module manages support agents.

Each agent contains:

Agent ID
Name
Email
Specialization
Availability
9. Data Storage

The application uses JSON files for persistent data storage.

The main JSON files are:

customers.json
support_agents.json
tickets.json

Whenever customer, agent, or ticket information is added or updated, the changes are saved to the corresponding JSON file.

This allows the data to remain available even after restarting the application.

10. Ticket Workflow

The general ticket workflow is:

Create Ticket
      ↓
Validate Customer
      ↓
Select Category
      ↓
Select Priority
      ↓
Automatic Assignment
      ↓
Ticket Created
      ↓
Open
      ↓
In Progress
      ↓
Resolved
      ↓
Add Resolution
      ↓
Closed

Closed tickets cannot be modified as active tickets.

A resolution must be provided before a ticket can be closed.

11. Automatic Ticket Assignment

The system automatically assigns a newly created ticket to a suitable support agent.

The assignment process is:

The ticket category is checked.
The system searches for an available agent with a matching specialization.
If a matching specialist is available, that agent is assigned.
If no matching specialist is available, another available agent is selected.
If no support agent is available, the ticket is marked as Not Assigned.
The assignment is recorded in the ticket history.

This reduces the need for manual ticket assignment.

12. Validation and Exception Handling

The application validates user input before performing operations.

Validation Includes
Customer ID
Ticket ID
Support Agent ID
Customer name
Agent name
Email address
Mobile number
Ticket subject
Ticket description
Category
Priority
Status
Resolution
Menu choices
Exception Handling

The application handles common file-related exceptions such as:

FileNotFoundError
JSONDecodeError
OSError
General exceptions

The system displays appropriate error messages instead of terminating unexpectedly.

13. Business Rules

The project follows the following business rules:

Customer IDs must be valid.
Ticket IDs must be unique.
Tickets must belong to existing customers.
Ticket priorities must use predefined values.
Ticket statuses must use predefined values.
Closed tickets cannot be modified.
A resolution must be added before closing a ticket.
Duplicate customer email addresses are not allowed.
Duplicate customer mobile numbers are not allowed.
Only available support agents can be automatically assigned.
Ticket history is recorded when important ticket changes occur.
14. Reports

The system provides several reports to help monitor support activities.

Available Reports
Open Tickets
Closed Tickets
High-Priority Tickets
Tickets by Category
Tickets by Assigned Person
Ticket Summary

The Ticket Summary provides counts for:

Total Tickets
Open Tickets
In Progress Tickets
Resolved Tickets
Closed Tickets
Low Priority
Medium Priority
High Priority
Critical Priority
15. How to Run the Project
Step 1: Open the Project

Open the project folder in Visual Studio Code.

Step 2: Open the Terminal

Open the VS Code terminal and navigate to the project folder.

Step 3: Run the Application

Use:

python main.py
Step 4: Use the Main Menu

The application displays:

===== CUSTOMER SUPPORT TICKET MANAGEMENT SYSTEM =====

1. Customer Management
2. Support Agent Management
3. Ticket Management
4. Exit

Select the required option and follow the instructions displayed by the application.

16. Testing

The project was tested for functional requirements, validation, exception handling, persistence, and navigation.

Testing included:

Adding valid and invalid customers
Searching and updating customers
Adding, updating, searching, and removing support agents
Creating valid and invalid tickets
Automatic ticket assignment
Changing ticket priority
Updating ticket status
Adding resolutions
Closing tickets
Preventing modification of closed tickets
Viewing ticket history
Testing reports
Testing invalid menu choices
Testing invalid IDs
Testing duplicate customer information
Testing JSON file persistence
Testing application navigation
Testing file-related exception handling

Detailed test cases are available in:

tests/test_cases.md
Final Testing Result

STATUS: PASS

All major functional requirements, validation tests, exception handling tests, persistence tests, report tests, and navigation tests were successfully completed.

17. Sample Error Handling

The application provides clear messages for invalid input.

Examples:

ERROR: Customer not found.
ERROR: Email already exists.
ERROR: Mobile number must contain exactly 10 digits.
ERROR: Invalid priority choice.
ERROR: Closed tickets cannot be modified.
ERROR: Ticket cannot be closed. Please add a resolution before closing the ticket.

These validations help prevent incorrect data from being stored.

18. Future Enhancements

The project can be enhanced in the future by adding:

Graphical User Interface
Database integration
User authentication
Role-based access control
Email notifications
Advanced analytics
Ticket response-time tracking
More detailed dashboards
Exporting reports to CSV or Excel
19. Conclusion

The Customer Support Ticket Management System provides a structured way to manage customers, support agents, and support tickets using Python.

The project demonstrates practical implementation of:

Object-Oriented Programming
Modular programming
File handling
JSON data storage
Input validation
Exception handling
Automatic ticket assignment
Business logic
Ticket tracking
Reporting

The system successfully meets the major functional requirements and demonstrates the use of core Python concepts in a practical real-world application.

20. Project Status

Project Status: Completed

The application has been tested for:

Customer Management
Support Agent Management
Ticket Management
Automatic Ticket Assignment
Ticket History
Reports
Validation
Exception Handling
File Persistence
Navigation
Final Status

PASS