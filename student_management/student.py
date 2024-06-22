# student_management/student.py

# Global list to store student dictionaries
students = []

def add_student(name, student_id, grades):
    """Add a new student with their grades."""
    student = {
        "name": name,
        "id": student_id,
        "grades": grades if isinstance(grades, list) else []
    }
    students.append(student)

def remove_student(student_id):
    """Remove a student by their ID."""
    global students
    students = [s for s in students if s["id"] != student_id]

def update_student(student_id, name=None, grades=None):
    """Update a student's name or grades."""
    for student in students:
        if student["id"] == student_id:
            if name is not None:
                student["name"] = name
            if grades is not None:
                student["grades"] = grades if isinstance(grades, list) else student["grades"]
            break

def get_student(student_id):
    """Retrieve a student's information by their ID."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None
