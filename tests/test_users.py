import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from admin import Admin
from mentor import Mentor
from student import Student


def test_student_inherits_from_user():
    student = Student(
        "Test Student",
        "student@example.com",
        "S001",
        "Python",
    )

    assert student.name == "Test Student"
    assert student.email == "student@example.com"
    assert student.user_id == "S001"
    assert student.course == "Python"


def test_student_submit_assignment():
    student = Student(
        "Test Student",
        "student@example.com",
        "S002",
        "Python",
    )

    student.submit_assignment("OOP")

    assert "OOP" in student.completed_assignments


def test_mentor_assign_student():
    mentor = Mentor(
        "Test Mentor",
        "mentor@example.com",
        "M001",
        "AI",
    )

    mentor.assign_student()

    assert mentor.students_assigned == 1


def test_admin_permissions():
    admin = Admin(
        "Test Admin",
        "admin@example.com",
        "A001",
        ["manage_users"],
    )

    assert "manage_users" in admin.permissions