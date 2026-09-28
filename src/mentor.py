from user import User


class Mentor(User):
    """Mentor user with mentoring-related functionality."""

    def __init__(self, name, email, user_id, expertise):
        super().__init__(name, email, user_id)
        self.expertise = expertise
        self.students_assigned = 0

    def assign_student(self):
        """Assign a student to the mentor."""
        self.students_assigned += 1

    def display_info(self):
        """Override User.display_info()."""
        print("=== Mentor ===")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.user_id}")
        print(f"Expertise: {self.expertise}")
        print(f"Students Assigned: {self.students_assigned}")