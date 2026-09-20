class Ticket:
    def __init__(
        self,
        ticket_id,
        customer_id,
        subject,
        description,
        category,
        priority,
        assigned_person,
        status,
        created_date,
        closed_date,
        resolution,
        comment,
        history,
        last_updated
    ):
        self.ticket_id = ticket_id
        self.customer_id = customer_id
        self.subject = subject
        self.description = description
        self.category = category
        self.priority = priority
        self.assigned_person = assigned_person
        self.status = status
        self.created_date = created_date
        self.closed_date = closed_date
        self.resolution = resolution
        self.comment = comment
        self.history = history
        self.last_updated = last_updated

    def to_dict(self):
        return {
            "id": self.ticket_id,
            "customer_id": self.customer_id,
            "subject": self.subject,
            "description": self.description,
            "category": self.category,
            "priority": self.priority,
            "assigned_person": self.assigned_person,
            "status": self.status,
            "created_date": self.created_date,
            "closed_date": self.closed_date,
            "resolution": self.resolution,
            "comment": self.comment,
            "history": self.history,
            "last_updated": self.last_updated
        }

    def is_closed(self):
        return self.status.lower() == "closed"