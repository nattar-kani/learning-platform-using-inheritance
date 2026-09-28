# Inheritance-Based Learning Platform

A small Python learning platform demonstrating **inheritance** and **method overriding** using different user roles.

## Class Structure

```text
User
├── Student
├── Mentor
└── Admin
```

## Classes

### User

The parent class containing common properties:

* Name
* Email
* User ID

It also provides a `display_info()` method.

### Student

Inherits from `User`.

Additional functionality:

* Course
* Completed assignments
* Submit assignment

`Student` overrides the `display_info()` method.

### Mentor

Inherits from `User`.

Additional functionality:

* Area of expertise
* Number of students assigned
* Assign student

`Mentor` overrides the `display_info()` method.

### Admin

Inherits from `User`.

Additional functionality:

* Permissions
* Manage users

`Admin` overrides the `display_info()` method.

## Inheritance

The child classes reuse the common properties and functionality of the parent `User` class.

```python
class Student(User):
    pass
```

The `super()` function is used to call the parent constructor.

```python
super().__init__(name, email, user_id)
```

## Method Overriding

Each child class provides its own implementation of:

```python
display_info()
```

Although the method has the same name, each class displays role-specific information.

## Project Structure

```text
inheritance-learning-platform/
│
├── src/
│   ├── user.py
│   ├── student.py
│   ├── mentor.py
│   ├── admin.py
│   └── main.py
│
├── tests/
│   └── test_users.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## How to Run

Run the application:

```bash
python src/main.py
```

Run the tests:

```bash
python -m pytest
```

## Expected Output

```text
=== Student ===
Name: Nattarkani
Course: Python Programming
Completed Assignments: ['Inheritance Assignment']

=== Mentor ===
Name: Priya
Expertise: Python and AI
Students Assigned: 1

=== Admin ===
Name: Arun
Permissions: ['manage_users', 'manage_courses']

Arun is managing platform users.
```
