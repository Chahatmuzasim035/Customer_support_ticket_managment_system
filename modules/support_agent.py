class SupportAgent:
    def _init_(
        self,
        agent_id,
        name,
        email,
        specialization,
        availability
    ):
        self.agent_id = agent_id
        self.name = name
        self.email = email
        self.specialization = specialization
        self.availability = availability

    def to_dict(self):
        return {
            "id": self.agent_id,
            "name": self.name,
            "email": self.email,
            "specialization": self.specialization,
            "availability": self.availability
        }

    def update_details(self, name, email, specialization, availability):
        self.name = name
        self.email = email
        self.specialization = specialization
        self.availability = availability