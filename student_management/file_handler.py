# student_management/file_handler.py
import csv
from .student import students, add_student

def save_students(filename):
    """Save all students to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "id", "grades"])
        for student in students:
            grades = student.get("grades", [])
            writer.writerow([student["name"], student["id"], ','.join(map(str, grades))])

def load_students(filename):
    """Load students from a CSV file and print their data."""
    global students
    students = []  # Reset the current list
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, student_id, grades_str = row
            grades = list(map(int, grades_str.split(',')))
            add_student(name, int(student_id), grades)
            print(f"Loaded student: Name={name}, ID={student_id}, Grades={grades}")
    
    print(f"All students loaded from {filename}.")

def append_student(filename, student):
    """Append a single student's data to a CSV file."""
    grades = student.get("grades", [])
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student["name"], student["id"], ','.join(map(str, grades))])
