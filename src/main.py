from admin import Admin
from mentor import Mentor
from student import Student


def main():
    student = Student(
        "Nattarkani",
        "nattarkani@example.com",
        "S001",
        "Python Programming",
    )

    mentor = Mentor(
        "Priya",
        "priya@example.com",
        "M001",
        "Python and AI",
    )

    admin = Admin(
        "Arun",
        "arun@example.com",
        "A001",
        ["manage_users", "manage_courses"],
    )

    student.submit_assignment("Inheritance Assignment")
    mentor.assign_student()

    users = [student, mentor, admin]

    for user in users:
        user.display_info()
        print()

    admin.manage_users()


if __name__ == "__main__":
    main()