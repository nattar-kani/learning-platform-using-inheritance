from user import User


class Student(User):
    """Student user with learning-related functionality."""

    def __init__(self, name, email, user_id, course):
        super().__init__(name, email, user_id)
        self.course = course
        self.completed_assignments = []

    def submit_assignment(self, assignment):
        """Submit an assignment."""
        self.completed_assignments.append(assignment)

    def display_info(self):
        """Override User.display_info()."""
        print("=== Student ===")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.user_id}")
        print(f"Course: {self.course}")
        print(f"Completed Assignments: {self.completed_assignments}")