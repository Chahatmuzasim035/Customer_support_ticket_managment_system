class Customer:
    def __init__(self, customer_id, name, email, mobile):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.mobile = mobile

    def to_dict(self):
        return {
            "id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "mobile": self.mobile
        }

    def update_details(self, name, email, mobile):
        self.name = name
        self.email = email
        self.mobile = mobile