class User:
    """Parent class representing a platform user."""

    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    def display_info(self):
        """Display common user information."""
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.user_id}")