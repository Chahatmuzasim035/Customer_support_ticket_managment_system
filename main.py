import json
import os
import re
from datetime import datetime

from modules.customer import Customer
from modules.ticket import Ticket
from modules.support_agent import SupportAgent


# ============================================================
# FILE PATHS
# ============================================================

CUSTOMER_FILE = "data/customers.json"
TICKET_FILE = "data/tickets.json"
AGENT_FILE = "data/support_agents.json"


# ============================================================
# DEFAULT SUPPORT AGENTS
# ============================================================

default_agents = [
    {
        "id": "A001",
        "name": "Arjun",
        "email": "arjun@company.com",
        "specialization": "Technical",
        "availability": "Available"
    },
    {
        "id": "A002",
        "name": "Priya",
        "email": "priya@company.com",
        "specialization": "Billing",
        "availability": "Available"
    },
    {
        "id": "A003",
        "name": "Rahul",
        "email": "rahul@company.com",
        "specialization": "Network",
        "availability": "Available"
    },
    {
        "id": "A004",
        "name": "Neha",
        "email": "neha@company.com",
        "specialization": "Software",
        "availability": "Available"
    }
]


# ============================================================
# CREATE DATA FOLDER AND FILES
# ============================================================

try:

    os.makedirs("data", exist_ok=True)

except OSError as error:

    print("ERROR: Unable to create data folder.")
    print("Details:", error)


if not os.path.exists(CUSTOMER_FILE):

    try:

        with open(CUSTOMER_FILE, "w") as file:
            json.dump([], file, indent=4)

    except OSError as error:

        print("ERROR: Unable to create customers file.")
        print("Details:", error)


if not os.path.exists(TICKET_FILE):

    try:

        with open(TICKET_FILE, "w") as file:
            json.dump([], file, indent=4)

    except OSError as error:

        print("ERROR: Unable to create tickets file.")
        print("Details:", error)


if not os.path.exists(AGENT_FILE):

    try:

        with open(AGENT_FILE, "w") as file:
            json.dump(default_agents, file, indent=4)

    except OSError as error:

        print("ERROR: Unable to create support agents file.")
        print("Details:", error)


# ============================================================
# LOAD CUSTOMERS
# ============================================================

def load_customers():

    try:

        with open(CUSTOMER_FILE, "r") as file:
            data = json.load(file)

        if isinstance(data, list):

            return data

        print("WARNING: Customer data format is invalid.")
        return []

    except FileNotFoundError:

        print("WARNING: Customer file not found.")
        return []

    except json.JSONDecodeError:

        print("ERROR: Customer file contains invalid JSON.")
        return []

    except OSError as error:

        print("ERROR: Unable to read customer file.")
        print("Details:", error)
        return []

    except Exception as error:

        print("ERROR: Unexpected error while loading customers.")
        print("Details:", error)
        return []


# ============================================================
# LOAD TICKETS
# ============================================================

def load_tickets():

    try:

        with open(TICKET_FILE, "r") as file:
            data = json.load(file)

        if isinstance(data, list):

            return data

        print("WARNING: Ticket data format is invalid.")
        return []

    except FileNotFoundError:

        print("WARNING: Ticket file not found.")
        return []

    except json.JSONDecodeError:

        print("ERROR: Ticket file contains invalid JSON.")
        return []

    except OSError as error:

        print("ERROR: Unable to read ticket file.")
        print("Details:", error)
        return []

    except Exception as error:

        print("ERROR: Unexpected error while loading tickets.")
        print("Details:", error)
        return []


# ============================================================
# LOAD SUPPORT AGENTS
# ============================================================

def load_agents():

    try:

        with open(AGENT_FILE, "r") as file:
            data = json.load(file)

        if isinstance(data, list):

            return data

        print("WARNING: Support agent data format is invalid.")
        return default_agents.copy()

    except FileNotFoundError:

        print("WARNING: Support agent file not found.")
        return default_agents.copy()

    except json.JSONDecodeError:

        print("ERROR: Support agent file contains invalid JSON.")
        return default_agents.copy()

    except OSError as error:

        print("ERROR: Unable to read support agent file.")
        print("Details:", error)
        return default_agents.copy()

    except Exception as error:

        print("ERROR: Unexpected error while loading support agents.")
        print("Details:", error)
        return default_agents.copy()


# ============================================================
# LOAD DATA INTO MEMORY
# ============================================================

customers = load_customers()
tickets = load_tickets()
support_agents = load_agents()


# ============================================================
# SAVE CUSTOMERS
# ============================================================

def save_customers():

    try:

        with open(CUSTOMER_FILE, "w") as file:

            json.dump(customers, file, indent=4)

        return True

    except OSError as error:

        print("\nERROR: Unable to save customer data.")
        print("Details:", error)
        return False

    except Exception as error:

        print("\nERROR: Unexpected error while saving customers.")
        print("Details:", error)
        return False


# ============================================================
# SAVE TICKETS
# ============================================================

def save_tickets():

    try:

        with open(TICKET_FILE, "w") as file:

            json.dump(tickets, file, indent=4)

        return True

    except OSError as error:

        print("\nERROR: Unable to save ticket data.")
        print("Details:", error)
        return False

    except Exception as error:

        print("\nERROR: Unexpected error while saving tickets.")
        print("Details:", error)
        return False


# ============================================================
# SAVE SUPPORT AGENTS
# ============================================================

def save_agents():

    try:

        with open(AGENT_FILE, "w") as file:

            json.dump(support_agents, file, indent=4)

        return True

    except OSError as error:

        print("\nERROR: Unable to save support agent data.")
        print("Details:", error)
        return False

    except Exception as error:

        print("\nERROR: Unexpected error while saving support agents.")
        print("Details:", error)
        return False


# ============================================================
# DATE AND TIME
# ============================================================

def current_datetime():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def current_date():

    return datetime.now().strftime("%Y-%m-%d")


# ============================================================
# CUSTOMER VALIDATION
# ============================================================

def valid_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email) is not None


def valid_mobile(mobile):

    return mobile.isdigit() and len(mobile) == 10


def get_valid_name():

    while True:

        name = input("Enter Name: ").strip()

        if name == "":

            print("ERROR: Name cannot be empty.")

        elif not name.replace(" ", "").isalpha():

            print("ERROR: Name should contain only letters.")

        else:

            return name


def get_valid_email():

    while True:

        email = input("Enter Email: ").strip()

        if email == "":

            print("ERROR: Email cannot be empty.")

        elif not valid_email(email):

            print("ERROR: Enter a valid email address.")

        else:

            return email


def get_valid_mobile():

    while True:

        mobile = input("Enter Mobile: ").strip()

        if not mobile.isdigit():

            print("ERROR: Mobile number must contain only digits.")

        elif len(mobile) != 10:

            print("ERROR: Mobile number must contain exactly 10 digits.")

        else:

            return mobile


# ============================================================
# CREATE CUSTOMER
# ============================================================

def create_customer():

    print("\n===== ADD CUSTOMER =====")

    customer_id = "C" + str(len(customers) + 1).zfill(3)

    name = get_valid_name()

    while True:

        email = get_valid_email()

        email_exists = False

        for customer in customers:

            if customer.get("email", "").lower() == email.lower():

                email_exists = True
                break

        if email_exists:

            print("ERROR: Email already exists.")

        else:

            break

    while True:

        mobile = get_valid_mobile()

        mobile_exists = False

        for customer in customers:

            if customer.get("mobile", "") == mobile:

                mobile_exists = True
                break

        if mobile_exists:

            print("ERROR: Mobile number already exists.")

        else:

            break

    customer = Customer(
        customer_id,
        name,
        email,
        mobile
    )

    customers.append(customer.to_dict())

    if save_customers():

        print("\nCustomer created successfully.")
        print("Customer ID :", customer_id)


# ============================================================
# VIEW CUSTOMERS
# ============================================================

def view_customers():

    print("\n===== VIEW CUSTOMERS =====")

    if len(customers) == 0:

        print("No customers found.")
        return

    for customer in customers:

        print("\n-----------------------------")
        print("Customer ID :", customer.get("id", ""))
        print("Name        :", customer.get("name", ""))
        print("Email       :", customer.get("email", ""))
        print("Mobile      :", customer.get("mobile", ""))

    print("\n-----------------------------")


# ============================================================
# SEARCH CUSTOMER
# ============================================================

def search_customer():

    print("\n===== SEARCH CUSTOMER =====")

    if len(customers) == 0:

        print("No customers found.")
        return

    search_value = input(
        "Enter Customer ID, Name, Email or Mobile: "
    ).strip().lower()

    if search_value == "":

        print("ERROR: Search value cannot be empty.")
        return

    found = False

    for customer in customers:

        if (
            search_value in customer.get("id", "").lower()
            or search_value in customer.get("name", "").lower()
            or search_value in customer.get("email", "").lower()
            or search_value in customer.get("mobile", "").lower()
        ):

            print("\n-----------------------------")
            print("Customer ID :", customer.get("id", ""))
            print("Name        :", customer.get("name", ""))
            print("Email       :", customer.get("email", ""))
            print("Mobile      :", customer.get("mobile", ""))

            found = True

    if not found:

        print("\nCustomer not found.")


# ============================================================
# UPDATE CUSTOMER
# ============================================================

def update_customer():

    print("\n===== UPDATE CUSTOMER =====")

    if len(customers) == 0:

        print("No customers found.")
        return

    customer_id = input("Enter Customer ID: ").strip().upper()

    selected_customer = None

    for customer in customers:

        if customer.get("id", "") == customer_id:

            selected_customer = customer
            break

    if selected_customer is None:

        print("ERROR: Customer not found.")
        return

    print("\nCurrent Customer Details")
    print("Customer ID :", selected_customer.get("id", ""))
    print("Name        :", selected_customer.get("name", ""))
    print("Email       :", selected_customer.get("email", ""))
    print("Mobile      :", selected_customer.get("mobile", ""))

    print("\nEnter New Details")

    new_name = get_valid_name()

    while True:

        new_email = get_valid_email()

        email_exists = False

        for customer in customers:

            if (
                customer.get("email", "").lower() == new_email.lower()
                and customer.get("id", "") != customer_id
            ):

                email_exists = True
                break

        if email_exists:

            print("ERROR: Email already exists.")

        else:

            break

    while True:

        new_mobile = get_valid_mobile()

        mobile_exists = False

        for customer in customers:

            if (
                customer.get("mobile", "") == new_mobile
                and customer.get("id", "") != customer_id
            ):

                mobile_exists = True
                break

        if mobile_exists:

            print("ERROR: Mobile number already exists.")

        else:

            break

    selected_customer["name"] = new_name
    selected_customer["email"] = new_email
    selected_customer["mobile"] = new_mobile

    if save_customers():

        print("\nCustomer updated successfully.")


# ============================================================
# CUSTOMER MANAGEMENT
# ============================================================

def customer_management():

    while True:

        print("\n================================")
        print("       CUSTOMER MANAGEMENT")
        print("================================")

        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            create_customer()

        elif choice == "2":

            view_customers()

        elif choice == "3":

            search_customer()

        elif choice == "4":

            update_customer()

        elif choice == "5":

            print("\nReturning to previous menu...")
            break

        else:

            print("\nERROR: Invalid choice.")
            print("Please enter a number from 1 to 5.")


# ============================================================
# SUPPORT AGENT VALIDATION
# ============================================================

def get_valid_agent_name():

    while True:

        name = input("Enter Agent Name: ").strip()

        if name == "":

            print("ERROR: Agent name cannot be empty.")

        elif not name.replace(" ", "").isalpha():

            print("ERROR: Agent name should contain only letters.")

        else:

            return name


def get_valid_agent_email():

    while True:

        email = input("Enter Agent Email: ").strip()

        if email == "":

            print("ERROR: Email cannot be empty.")

        elif not valid_email(email):

            print("ERROR: Enter a valid email address.")

        else:

            return email


def get_valid_specialization():

    while True:

        print("\nSpecializations:")
        print("1. Technical")
        print("2. Billing")
        print("3. Network")
        print("4. Software")
        print("5. Hardware")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            return "Technical"

        elif choice == "2":

            return "Billing"

        elif choice == "3":

            return "Network"

        elif choice == "4":

            return "Software"

        elif choice == "5":

            return "Hardware"

        else:

            print("ERROR: Invalid specialization choice.")


def get_valid_availability():

    while True:

        print("\nAvailability:")
        print("1. Available")
        print("2. Busy")
        print("3. On Leave")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            return "Available"

        elif choice == "2":

            return "Busy"

        elif choice == "3":

            return "On Leave"

        else:

            print("ERROR: Invalid availability choice.")


# ============================================================
# GENERATE NEXT AGENT ID
# ============================================================

def get_next_agent_id():

    highest_number = 0

    for agent in support_agents:

        agent_id = agent.get("id", "")

        if agent_id.startswith("A"):

            try:

                number = int(agent_id[1:])

                if number > highest_number:

                    highest_number = number

            except ValueError:

                continue

    return "A" + str(highest_number + 1).zfill(3)


# ============================================================
# ADD SUPPORT AGENT
# ============================================================

def add_support_agent():

    print("\n===== ADD SUPPORT AGENT =====")

    agent_id = get_next_agent_id()

    name = get_valid_agent_name()

    while True:

        email = get_valid_agent_email()

        email_exists = False

        for agent in support_agents:

            if agent.get("email", "").lower() == email.lower():

                email_exists = True
                break

        if email_exists:

            print("ERROR: Email already exists.")

        else:

            break

    specialization = get_valid_specialization()

    availability = get_valid_availability()

    agent = SupportAgent(
        agent_id,
        name,
        email,
        specialization,
        availability
    )

    support_agents.append(agent.to_dict())

    if save_agents():

        print("\nSupport Agent created successfully.")
        print("Agent ID          :", agent_id)
        print("Agent Name        :", name)
        print("Specialization    :", specialization)
        print("Availability      :", availability)


# ============================================================
# VIEW SUPPORT AGENTS
# ============================================================

def view_support_agents():

    print("\n===== VIEW SUPPORT AGENTS =====")

    if len(support_agents) == 0:

        print("No support agents found.")
        return

    for agent in support_agents:

        print("\n========================================")
        print("Agent ID          :", agent.get("id", ""))
        print("Name              :", agent.get("name", ""))
        print("Email             :", agent.get("email", ""))
        print("Specialization    :", agent.get("specialization", ""))
        print("Availability      :", agent.get("availability", ""))

    print("\n========================================")


# ============================================================
# SEARCH SUPPORT AGENT
# ============================================================

def search_support_agent():

    print("\n===== SEARCH SUPPORT AGENT =====")

    if len(support_agents) == 0:

        print("No support agents found.")
        return

    search_value = input(
        "Enter Agent ID, Name, Email or Specialization: "
    ).strip().lower()

    if search_value == "":

        print("ERROR: Search value cannot be empty.")
        return

    found = False

    for agent in support_agents:

        if (
            search_value in agent.get("id", "").lower()
            or search_value in agent.get("name", "").lower()
            or search_value in agent.get("email", "").lower()
            or search_value in agent.get("specialization", "").lower()
        ):

            print("\n========================================")
            print("Agent ID          :", agent.get("id", ""))
            print("Name              :", agent.get("name", ""))
            print("Email             :", agent.get("email", ""))
            print("Specialization    :", agent.get("specialization", ""))
            print("Availability      :", agent.get("availability", ""))

            found = True

    if not found:

        print("\nSupport agent not found.")


# ============================================================
# UPDATE SUPPORT AGENT
# ============================================================

def update_support_agent():

    print("\n===== UPDATE SUPPORT AGENT =====")

    if len(support_agents) == 0:

        print("No support agents found.")
        return

    agent_id = input("Enter Agent ID: ").strip().upper()

    selected_agent = None

    for agent in support_agents:

        if agent.get("id", "") == agent_id:

            selected_agent = agent
            break

    if selected_agent is None:

        print("ERROR: Support agent not found.")
        return

    print("\nCurrent Agent Details")
    print("Agent ID          :", selected_agent.get("id", ""))
    print("Name              :", selected_agent.get("name", ""))
    print("Email             :", selected_agent.get("email", ""))
    print("Specialization    :", selected_agent.get("specialization", ""))
    print("Availability      :", selected_agent.get("availability", ""))

    print("\nEnter New Details")

    new_name = get_valid_agent_name()

    while True:

        new_email = get_valid_agent_email()

        email_exists = False

        for agent in support_agents:

            if (
                agent.get("email", "").lower() == new_email.lower()
                and agent.get("id", "") != agent_id
            ):

                email_exists = True
                break

        if email_exists:

            print("ERROR: Email already exists.")

        else:

            break

    new_specialization = get_valid_specialization()

    new_availability = get_valid_availability()

    selected_agent["name"] = new_name
    selected_agent["email"] = new_email
    selected_agent["specialization"] = new_specialization
    selected_agent["availability"] = new_availability

    if save_agents():

        print("\nSupport agent updated successfully.")


# ============================================================
# REMOVE SUPPORT AGENT
# ============================================================

def remove_support_agent():

    print("\n===== REMOVE SUPPORT AGENT =====")

    if len(support_agents) == 0:

        print("No support agents found.")
        return

    agent_id = input("Enter Agent ID: ").strip().upper()

    selected_agent = None

    for agent in support_agents:

        if agent.get("id", "") == agent_id:

            selected_agent = agent
            break

    if selected_agent is None:

        print("ERROR: Support agent not found.")
        return

    print("\nAgent Details")
    print("Agent ID       :", selected_agent.get("id", ""))
    print("Name           :", selected_agent.get("name", ""))
    print("Email          :", selected_agent.get("email", ""))
    print("Specialization :", selected_agent.get("specialization", ""))
    print("Availability   :", selected_agent.get("availability", ""))

    confirmation = input(
        "\nAre you sure you want to remove this agent? (Y/N): "
    ).strip().upper()

    if confirmation == "Y":

        support_agents.remove(selected_agent)

        if save_agents():

            print("\nSupport agent removed successfully.")

    elif confirmation == "N":

        print("\nRemoval cancelled.")

    else:

        print("\nERROR: Please enter Y or N.")


# ============================================================
# SUPPORT AGENT MANAGEMENT
# ============================================================

def support_agent_management():

    while True:

        print("\n================================")
        print("     SUPPORT AGENT MANAGEMENT")
        print("================================")

        print("1. Add Support Agent")
        print("2. View Support Agents")
        print("3. Search Support Agent")
        print("4. Update Support Agent")
        print("5. Remove Support Agent")
        print("6. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            add_support_agent()

        elif choice == "2":

            view_support_agents()

        elif choice == "3":

            search_support_agent()

        elif choice == "4":

            update_support_agent()

        elif choice == "5":

            remove_support_agent()

        elif choice == "6":

            print("\nReturning to previous menu...")
            break

        else:

            print("\nERROR: Invalid choice.")
            print("Please enter a number from 1 to 6.")


# ============================================================
# TICKET VALIDATION
# ============================================================

def get_valid_ticket_customer():

    while True:

        customer_id = input("Enter Customer ID: ").strip().upper()

        for customer in customers:

            if customer.get("id", "") == customer_id:

                return customer_id

        print("ERROR: Customer ID does not exist.")


def get_valid_subject():

    while True:

        subject = input("Enter Subject: ").strip()

        if subject == "":

            print("ERROR: Subject cannot be empty.")

        else:

            return subject


def get_valid_description():

    while True:

        description = input("Enter Description: ").strip()

        if description == "":

            print("ERROR: Description cannot be empty.")

        else:

            return description


def get_valid_category():

    while True:

        print("\nCategories:")
        print("1. Technical")
        print("2. Billing")
        print("3. Network")
        print("4. Software")
        print("5. Hardware")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            return "Technical"

        elif choice == "2":

            return "Billing"

        elif choice == "3":

            return "Network"

        elif choice == "4":

            return "Software"

        elif choice == "5":

            return "Hardware"

        else:

            print("ERROR: Invalid category choice.")


def get_valid_priority():

    while True:

        print("\nPriority:")
        print("1. Low")
        print("2. Medium")
        print("3. High")
        print("4. Critical")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            return "Low"

        elif choice == "2":

            return "Medium"

        elif choice == "3":

            return "High"

        elif choice == "4":

            return "Critical"

        else:

            print("ERROR: Invalid priority choice.")


# ============================================================
# GENERATE NEXT TICKET ID
# ============================================================

def get_next_ticket_id():

    highest_number = 0

    for ticket in tickets:

        ticket_id = ticket.get("id", "")

        if ticket_id.startswith("T"):

            try:

                number = int(ticket_id[1:])

                if number > highest_number:

                    highest_number = number

            except ValueError:

                continue

    return "T" + str(highest_number + 1).zfill(3)


# ============================================================
# AUTOMATIC TICKET ASSIGNMENT
# ============================================================

def automatically_assign_ticket(category):

    selected_agent = None

    for agent in support_agents:

        specialization = agent.get("specialization", "")
        availability = agent.get("availability", "")

        if (
            availability.lower() == "available"
            and specialization.lower() == category.lower()
        ):

            selected_agent = agent
            break

    if selected_agent is None:

        for agent in support_agents:

            if agent.get("availability", "").lower() == "available":

                selected_agent = agent
                break

    if selected_agent is None:

        return None

    return selected_agent


# ============================================================
# CREATE TICKET
# ============================================================

def create_ticket():

    print("\n===== CREATE TICKET =====")

    if len(customers) == 0:

        print("ERROR: No customers available.")
        print("Please create a customer first.")
        return

    ticket_id = get_next_ticket_id()

    customer_id = get_valid_ticket_customer()

    subject = get_valid_subject()

    description = get_valid_description()

    category = get_valid_category()

    priority = get_valid_priority()

    selected_agent = automatically_assign_ticket(category)

    if selected_agent is not None:

        assigned_person = selected_agent.get("name", "")

        assignment_details = (
            "Ticket automatically assigned to "
            + selected_agent.get("name", "")
            + " ("
            + selected_agent.get("id", "")
            + ")"
        )

    else:

        assigned_person = "Not Assigned"

        assignment_details = "No available support agent"

    created_time = current_datetime()

    history = [
        {
            "date": created_time,
            "action": "Ticket Created",
            "details": "Ticket created successfully"
        }
    ]

    if selected_agent is not None:

        history.append(
            {
                "date": created_time,
                "action": "Ticket Automatically Assigned",
                "details": assignment_details
            }
        )

    else:

        history.append(
            {
                "date": created_time,
                "action": "Assignment Pending",
                "details": assignment_details
            }
        )

    ticket = Ticket(
        ticket_id,
        customer_id,
        subject,
        description,
        category,
        priority,
        assigned_person,
        "Open",
        created_time,
        "",
        "",
        "",
        history,
        created_time
    )

    tickets.append(ticket.to_dict())

    if save_tickets():

        print("\nTicket created successfully.")
        print("Ticket ID       :", ticket_id)
        print("Customer ID     :", customer_id)
        print("Subject         :", subject)
        print("Description     :", description)
        print("Category        :", category)
        print("Priority        :", priority)
        print("Assigned Person :", assigned_person)
        print("Status          : Open")
        print("Created Date    :", created_time)

        if selected_agent is not None:

            print("\nAutomatic Assignment")
            print("Agent ID        :", selected_agent.get("id", ""))
            print("Agent Name      :", selected_agent.get("name", ""))
            print(
                "Specialization  :",
                selected_agent.get("specialization", "")
            )
            print("Assignment      : Automatic")

        else:

            print("\nAssignment")
            print("Agent           : Not Assigned")
            print("Assignment      : Pending")


# ============================================================
# VIEW TICKETS
# ============================================================

def view_tickets():

    print("\n===== VIEW TICKETS =====")

    if len(tickets) == 0:

        print("No tickets found.")
        return

    for ticket in tickets:

        print("\n========================================")
        print("Ticket ID       :", ticket.get("id", ""))
        print("Customer ID     :", ticket.get("customer_id", ""))
        print("Subject         :", ticket.get("subject", ""))
        print("Description     :", ticket.get("description", ""))
        print("Category        :", ticket.get("category", ""))
        print("Priority        :", ticket.get("priority", ""))
        print("Assigned Person :", ticket.get("assigned_person", ""))
        print("Status          :", ticket.get("status", ""))
        print("Created Date    :", ticket.get("created_date", ""))
        print("Closed Date     :", ticket.get("closed_date", ""))
        print("Resolution      :", ticket.get("resolution", ""))
        print("Comment         :", ticket.get("comment", ""))
        print("Last Updated    :", ticket.get("last_updated", ""))

    print("\n========================================")


# ============================================================
# SEARCH TICKET
# ============================================================

def search_ticket():

    print("\n===== SEARCH TICKET =====")

    if len(tickets) == 0:

        print("No tickets found.")
        return

    search_value = input(
        "Enter Ticket ID, Customer ID, Subject, Category, "
        "Priority, Status or Assigned Person: "
    ).strip().lower()

    if search_value == "":

        print("ERROR: Search value cannot be empty.")
        return

    found = False

    for ticket in tickets:

        if (
            search_value in ticket.get("id", "").lower()
            or search_value in ticket.get("customer_id", "").lower()
            or search_value in ticket.get("subject", "").lower()
            or search_value in ticket.get("category", "").lower()
            or search_value in ticket.get("priority", "").lower()
            or search_value in ticket.get("status", "").lower()
            or search_value in ticket.get("assigned_person", "").lower()
        ):

            print("\n========================================")
            print("Ticket ID       :", ticket.get("id", ""))
            print("Customer ID     :", ticket.get("customer_id", ""))
            print("Subject         :", ticket.get("subject", ""))
            print("Description     :", ticket.get("description", ""))
            print("Category        :", ticket.get("category", ""))
            print("Priority        :", ticket.get("priority", ""))
            print("Assigned Person :", ticket.get("assigned_person", ""))
            print("Status          :", ticket.get("status", ""))
            print("Created Date    :", ticket.get("created_date", ""))
            print("Closed Date     :", ticket.get("closed_date", ""))
            print("Resolution      :", ticket.get("resolution", ""))
            print("Comment         :", ticket.get("comment", ""))
            print("Last Updated    :", ticket.get("last_updated", ""))

            found = True

    if not found:

        print("\nTicket not found.")


# ============================================================
# CHANGE TICKET PRIORITY
# ============================================================

def change_priority():

    print("\n===== CHANGE TICKET PRIORITY =====")

    if len(tickets) == 0:

        print("No tickets found.")
        return

    ticket_id = input("Enter Ticket ID: ").strip().upper()

    selected_ticket = None

    for ticket in tickets:

        if ticket.get("id", "") == ticket_id:

            selected_ticket = ticket
            break

    if selected_ticket is None:

        print("ERROR: Ticket not found.")
        return

    if selected_ticket.get("status", "").lower() == "closed":

        print("ERROR: Closed tickets cannot be modified.")
        return

    print("\nTicket Details")
    print("Ticket ID       :", selected_ticket.get("id", ""))
    print("Subject         :", selected_ticket.get("subject", ""))
    print("Current Priority:", selected_ticket.get("priority", ""))
    print("Status          :", selected_ticket.get("status", ""))

    print("\nSelect New Priority")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("4. Critical")

    choice = input("Enter choice: ").strip()

    if choice == "1":

        new_priority = "Low"

    elif choice == "2":

        new_priority = "Medium"

    elif choice == "3":

        new_priority = "High"

    elif choice == "4":

        new_priority = "Critical"

    else:

        print("ERROR: Invalid priority choice.")
        return

    old_priority = selected_ticket.get("priority", "")

    if old_priority == new_priority:

        print("Priority is already set to", new_priority)
        return

    updated_time = current_datetime()

    selected_ticket["priority"] = new_priority
    selected_ticket["last_updated"] = updated_time

    if "history" not in selected_ticket:

        selected_ticket["history"] = []

    selected_ticket["history"].append(
        {
            "date": updated_time,
            "action": "Priority Changed",
            "details": (
                "Priority changed from "
                + old_priority
                + " to "
                + new_priority
            )
        }
    )

    save_tickets()

    print("\nTicket priority updated successfully.")
    print("Ticket ID       :", ticket_id)
    print("Old Priority    :", old_priority)
    print("New Priority     :", new_priority)
    print("Last Updated    :", updated_time)


# ============================================================
# UPDATE TICKET STATUS
# ============================================================

def update_status():

    print("\n===== UPDATE TICKET STATUS =====")

    if len(tickets) == 0:

        print("No tickets found.")
        return

    ticket_id = input("Enter Ticket ID: ").strip().upper()

    selected_ticket = None

    for ticket in tickets:

        if ticket.get("id", "") == ticket_id:

            selected_ticket = ticket
            break

    if selected_ticket is None:

        print("ERROR: Ticket not found.")
        return

    current_status = selected_ticket.get("status", "")

    if current_status.lower() == "closed":

        print("ERROR: Closed tickets cannot be modified.")
        return

    print("\nTicket Details")
    print("Ticket ID       :", selected_ticket.get("id", ""))
    print("Subject         :", selected_ticket.get("subject", ""))
    print("Assigned Person :", selected_ticket.get("assigned_person", ""))
    print("Current Status  :", current_status)

    print("\nSelect New Status")
    print("1. Open")
    print("2. In Progress")
    print("3. Resolved")

    choice = input("Enter choice: ").strip()

    if choice == "1":

        new_status = "Open"

    elif choice == "2":

        new_status = "In Progress"

    elif choice == "3":

        new_status = "Resolved"

    else:

        print("ERROR: Invalid status choice.")
        return

    if current_status == new_status:

        print("Status is already set to", new_status)
        return

    updated_time = current_datetime()

    selected_ticket["status"] = new_status
    selected_ticket["last_updated"] = updated_time

    if "history" not in selected_ticket:

        selected_ticket["history"] = []

    selected_ticket["history"].append(
        {
            "date": updated_time,
            "action": "Status Changed",
            "details": (
                "Status changed from "
                + current_status
                + " to "
                + new_status
            )
        }
    )

    save_tickets()

    print("\nTicket status updated successfully.")
    print("Ticket ID       :", ticket_id)
    print("Old Status      :", current_status)
    print("New Status      :", new_status)
    print("Last Updated    :", updated_time)


# ============================================================
# ADD TICKET RESOLUTION
# ============================================================

def add_resolution():

    print("\n===== ADD TICKET RESOLUTION =====")

    if len(tickets) == 0:

        print("No tickets found.")
        return

    ticket_id = input("Enter Ticket ID: ").strip().upper()

    selected_ticket = None

    for ticket in tickets:

        if ticket.get("id", "") == ticket_id:

            selected_ticket = ticket
            break

    if selected_ticket is None:

        print("ERROR: Ticket not found.")
        return

    current_status = selected_ticket.get("status", "")

    if current_status.lower() == "closed":

        print("ERROR: Closed tickets cannot be modified.")
        return

    print("\nTicket Details")
    print("Ticket ID          :", selected_ticket.get("id", ""))
    print("Subject            :", selected_ticket.get("subject", ""))
    print("Status             :", current_status)
    print(
        "Current Resolution :",
        selected_ticket.get("resolution", "")
    )

    while True:

        resolution = input("\nEnter Resolution: ").strip()

        if resolution == "":

            print("ERROR: Resolution cannot be empty.")

        else:

            break

    updated_time = current_datetime()

    selected_ticket["resolution"] = resolution
    selected_ticket["last_updated"] = updated_time

    if "history" not in selected_ticket:

        selected_ticket["history"] = []

    selected_ticket["history"].append(
        {
            "date": updated_time,
            "action": "Resolution Added",
            "details": "Resolution added to ticket"
        }
    )

    save_tickets()

    print("\nResolution added successfully.")
    print("Ticket ID       :", ticket_id)
    print("Resolution      :", resolution)
    print("Last Updated    :", updated_time)


# ============================================================
# CLOSE TICKET
# ============================================================

def close_ticket():

    print("\n===== CLOSE TICKET =====")

    if len(tickets) == 0:

        print("No tickets found.")
        return

    ticket_id = input("Enter Ticket ID: ").strip().upper()

    selected_ticket = None

    for ticket in tickets:

        if ticket.get("id", "") == ticket_id:

            selected_ticket = ticket
            break

    if selected_ticket is None:

        print("ERROR: Ticket not found.")
        return

    current_status = selected_ticket.get("status", "")

    if current_status.lower() == "closed":

        print("ERROR: Ticket is already closed.")
        return

    print("\nTicket Details")
    print("Ticket ID       :", selected_ticket.get("id", ""))
    print("Subject         :", selected_ticket.get("subject", ""))
    print("Assigned Person :", selected_ticket.get("assigned_person", ""))
    print("Status          :", current_status)
    print("Resolution      :", selected_ticket.get("resolution", ""))

    resolution = selected_ticket.get("resolution", "").strip()

    if resolution == "":

        print("\nERROR: Ticket cannot be closed.")
        print("Please add a resolution before closing the ticket.")
        return

    confirmation = input(
        "\nAre you sure you want to close this ticket? (Y/N): "
    ).strip().upper()

    if confirmation == "N":

        print("\nTicket closing cancelled.")
        return

    if confirmation != "Y":

        print("\nERROR: Please enter Y or N.")
        return

    closed_time = current_datetime()

    selected_ticket["status"] = "Closed"
    selected_ticket["closed_date"] = closed_time
    selected_ticket["last_updated"] = closed_time

    if "history" not in selected_ticket:

        selected_ticket["history"] = []

    selected_ticket["history"].append(
        {
            "date": closed_time,
            "action": "Ticket Closed",
            "details": "Ticket closed successfully"
        }
    )

    save_tickets()

    print("\nTicket closed successfully.")
    print("Ticket ID       :", ticket_id)
    print("Status          : Closed")
    print("Closed Date     :", closed_time)
    print("Last Updated    :", closed_time)


# ============================================================
# VIEW TICKET HISTORY
# ============================================================

def view_ticket_history():

    print("\n===== TICKET HISTORY =====")

    if len(tickets) == 0:

        print("No tickets found.")
        return

    ticket_id = input("Enter Ticket ID: ").strip().upper()

    selected_ticket = None

    for ticket in tickets:

        if ticket.get("id", "") == ticket_id:

            selected_ticket = ticket
            break

    if selected_ticket is None:

        print("ERROR: Ticket not found.")
        return

    print("\nTicket ID       :", selected_ticket.get("id", ""))
    print("Subject         :", selected_ticket.get("subject", ""))
    print("Current Status  :", selected_ticket.get("status", ""))

    print("\n----------------------------------------")
    print("ACTIVITY HISTORY")
    print("----------------------------------------")

    history = selected_ticket.get("history", [])

    if len(history) == 0:

        print("No history available for this ticket.")
        return

    for item in history:

        print("\nDate    :", item.get("date", ""))
        print("Action  :", item.get("action", ""))
        print("Details :", item.get("details", ""))

    print("\n----------------------------------------")


# ============================================================
# REPORT 1: VIEW OPEN TICKETS
# ============================================================

def view_open_tickets():

    print("\n===== OPEN TICKETS =====")

    found = False

    for ticket in tickets:

        status = ticket.get("status", "")

        if status.lower() != "closed":

            print("\n========================================")
            print("Ticket ID       :", ticket.get("id", ""))
            print("Customer ID     :", ticket.get("customer_id", ""))
            print("Subject         :", ticket.get("subject", ""))
            print("Category        :", ticket.get("category", ""))
            print("Priority        :", ticket.get("priority", ""))
            print("Assigned Person :", ticket.get("assigned_person", ""))
            print("Status          :", ticket.get("status", ""))
            print("Created Date    :", ticket.get("created_date", ""))

            found = True

    if not found:

        print("\nNo open tickets found.")


# ============================================================
# REPORT 2: VIEW CLOSED TICKETS
# ============================================================

def view_closed_tickets():

    print("\n===== CLOSED TICKETS =====")

    found = False

    for ticket in tickets:

        status = ticket.get("status", "")

        if status.lower() == "closed":

            print("\n========================================")
            print("Ticket ID       :", ticket.get("id", ""))
            print("Customer ID     :", ticket.get("customer_id", ""))
            print("Subject         :", ticket.get("subject", ""))
            print("Category        :", ticket.get("category", ""))
            print("Priority        :", ticket.get("priority", ""))
            print("Assigned Person :", ticket.get("assigned_person", ""))
            print("Status          :", ticket.get("status", ""))
            print("Created Date    :", ticket.get("created_date", ""))
            print("Closed Date     :", ticket.get("closed_date", ""))
            print("Resolution      :", ticket.get("resolution", ""))

            found = True

    if not found:

        print("\nNo closed tickets found.")


# ============================================================
# REPORT 3: VIEW HIGH-PRIORITY TICKETS
# ============================================================

def view_high_priority_tickets():

    print("\n===== HIGH-PRIORITY TICKETS =====")

    found = False

    for ticket in tickets:

        priority = ticket.get("priority", "")

        if (
            priority.lower() == "high"
            or priority.lower() == "critical"
        ):

            print("\n========================================")
            print("Ticket ID       :", ticket.get("id", ""))
            print("Customer ID     :", ticket.get("customer_id", ""))
            print("Subject         :", ticket.get("subject", ""))
            print("Category        :", ticket.get("category", ""))
            print("Priority        :", ticket.get("priority", ""))
            print("Assigned Person :", ticket.get("assigned_person", ""))
            print("Status          :", ticket.get("status", ""))
            print("Created Date    :", ticket.get("created_date", ""))

            found = True

    if not found:

        print("\nNo high-priority tickets found.")


# ============================================================
# REPORT 4: VIEW TICKETS BY CATEGORY
# ============================================================

def view_tickets_by_category():

    print("\n===== TICKETS BY CATEGORY =====")

    print("\nCategories:")
    print("1. Technical")
    print("2. Billing")
    print("3. Network")
    print("4. Software")
    print("5. Hardware")

    choice = input("\nEnter category choice: ").strip()

    if choice == "1":

        selected_category = "Technical"

    elif choice == "2":

        selected_category = "Billing"

    elif choice == "3":

        selected_category = "Network"

    elif choice == "4":

        selected_category = "Software"

    elif choice == "5":

        selected_category = "Hardware"

    else:

        print("\nERROR: Invalid category choice.")
        return

    print(
        "\n===== "
        + selected_category.upper()
        + " TICKETS ====="
    )

    found = False

    for ticket in tickets:

        category = ticket.get("category", "")

        if category.lower() == selected_category.lower():

            print("\n========================================")
            print("Ticket ID       :", ticket.get("id", ""))
            print("Customer ID     :", ticket.get("customer_id", ""))
            print("Subject         :", ticket.get("subject", ""))
            print("Category        :", ticket.get("category", ""))
            print("Priority        :", ticket.get("priority", ""))
            print("Assigned Person :", ticket.get("assigned_person", ""))
            print("Status          :", ticket.get("status", ""))
            print("Created Date    :", ticket.get("created_date", ""))

            found = True

    if not found:

        print(
            "\nNo tickets found in "
            + selected_category
            + " category."
        )


# ============================================================
# REPORT 5: VIEW TICKETS BY ASSIGNED PERSON
# ============================================================

def view_tickets_by_assigned_person():

    print("\n===== TICKETS BY ASSIGNED PERSON =====")

    if len(support_agents) == 0:

        print("No support agents found.")
        return

    print("\nSupport Agents:")

    number = 1

    for agent in support_agents:

        print(
            str(number)
            + ". "
            + agent.get("name", "")
            + " ("
            + agent.get("id", "")
            + ")"
        )

        number = number + 1

    choice = input("\nEnter agent choice: ").strip()

    if not choice.isdigit():

        print("\nERROR: Please enter a valid agent number.")
        return

    selected_number = int(choice)

    if selected_number < 1 or selected_number > len(support_agents):

        print("\nERROR: Invalid agent choice.")
        return

    selected_agent = support_agents[selected_number - 1]

    selected_agent_name = selected_agent.get("name", "")

    print(
        "\n===== TICKETS ASSIGNED TO "
        + selected_agent_name.upper()
        + " ====="
    )

    found = False

    for ticket in tickets:

        assigned_person = ticket.get("assigned_person", "")

        if assigned_person.lower() == selected_agent_name.lower():

            print("\n========================================")
            print("Ticket ID       :", ticket.get("id", ""))
            print("Customer ID     :", ticket.get("customer_id", ""))
            print("Subject         :", ticket.get("subject", ""))
            print("Category        :", ticket.get("category", ""))
            print("Priority        :", ticket.get("priority", ""))
            print("Assigned Person :", ticket.get("assigned_person", ""))
            print("Status          :", ticket.get("status", ""))
            print("Created Date    :", ticket.get("created_date", ""))

            found = True

    if not found:

        print("\nNo tickets assigned to this person.")


# ============================================================
# REPORT 6: TICKET SUMMARY
# ============================================================

def ticket_summary():

    print("\n===== TICKET SUMMARY =====")

    total_tickets = len(tickets)

    open_tickets = 0
    in_progress_tickets = 0
    resolved_tickets = 0
    closed_tickets = 0

    low_priority = 0
    medium_priority = 0
    high_priority = 0
    critical_priority = 0

    for ticket in tickets:

        status = ticket.get("status", "").lower()
        priority = ticket.get("priority", "").lower()

        if status == "open":

            open_tickets = open_tickets + 1

        elif status == "in progress":

            in_progress_tickets = in_progress_tickets + 1

        elif status == "resolved":

            resolved_tickets = resolved_tickets + 1

        elif status == "closed":

            closed_tickets = closed_tickets + 1

        if priority == "low":

            low_priority = low_priority + 1

        elif priority == "medium":

            medium_priority = medium_priority + 1

        elif priority == "high":

            high_priority = high_priority + 1

        elif priority == "critical":

            critical_priority = critical_priority + 1

    print("\n----------------------------------------")
    print("Total Tickets       :", total_tickets)
    print("----------------------------------------")

    print("\nStatus Summary")
    print("Open Tickets        :", open_tickets)
    print("In Progress Tickets :", in_progress_tickets)
    print("Resolved Tickets    :", resolved_tickets)
    print("Closed Tickets      :", closed_tickets)

    print("\nPriority Summary")
    print("Low Priority        :", low_priority)
    print("Medium Priority     :", medium_priority)
    print("High Priority       :", high_priority)
    print("Critical Priority   :", critical_priority)

    print("\n----------------------------------------")


# ============================================================
# REPORTS MENU
# ============================================================

def reports_menu():

    while True:

        print("\n================================")
        print("          TICKET REPORTS")
        print("================================")

        print("1. View Open Tickets")
        print("2. View Closed Tickets")
        print("3. View High-Priority Tickets")
        print("4. View Tickets by Category")
        print("5. View Tickets by Assigned Person")
        print("6. Ticket Summary")
        print("7. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            view_open_tickets()

        elif choice == "2":

            view_closed_tickets()

        elif choice == "3":

            view_high_priority_tickets()

        elif choice == "4":

            view_tickets_by_category()

        elif choice == "5":

            view_tickets_by_assigned_person()

        elif choice == "6":

            ticket_summary()

        elif choice == "7":

            print("\nReturning to Ticket Management...")
            break

        else:

            print("\nERROR: Invalid choice.")
            print("Please enter a number from 1 to 7.")


# ============================================================
# TICKET MANAGEMENT
# ============================================================

def ticket_management():

    while True:

        print("\n================================")
        print("        TICKET MANAGEMENT")
        print("================================")

        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Search Ticket")
        print("4. Change Priority")
        print("5. Update Status")
        print("6. Add Resolution")
        print("7. Close Ticket")
        print("8. View Ticket History")
        print("9. Reports")
        print("10. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            create_ticket()

        elif choice == "2":

            view_tickets()

        elif choice == "3":

            search_ticket()

        elif choice == "4":

            change_priority()

        elif choice == "5":

            update_status()

        elif choice == "6":

            add_resolution()

        elif choice == "7":

            close_ticket()

        elif choice == "8":

            view_ticket_history()

        elif choice == "9":

            reports_menu()

        elif choice == "10":

            print("\nReturning to previous menu...")
            break

        else:

            print("\nERROR: Invalid choice.")
            print("Please enter a number from 1 to 10.")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 50)
        print(" CUSTOMER SUPPORT TICKET MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Customer Management")
        print("2. Support Agent Management")
        print("3. Ticket Management")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            customer_management()

        elif choice == "2":

            support_agent_management()

        elif choice == "3":

            ticket_management()

        elif choice == "4":

            print("\nThank you for using the system.")
            break

        else:

            print("\nERROR: Invalid choice.")
            print("Please enter a number from 1 to 4.")


# ============================================================
# START PROGRAM
# ============================================================

main()