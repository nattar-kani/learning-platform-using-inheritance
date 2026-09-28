from user import User


class Admin(User):
    """Admin user with platform management functionality."""

    def __init__(self, name, email, user_id, permissions):
        super().__init__(name, email, user_id)
        self.permissions = permissions

    def manage_users(self):
        """Manage users on the learning platform."""
        print(f"{self.name} is managing platform users.")

    def display_info(self):
        """Override User.display_info()."""
        print("=== Admin ===")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.user_id}")
        print(f"Permissions: {self.permissions}")