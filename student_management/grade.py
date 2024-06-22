from .student import get_student

def calculate_average_grade(student_id):
    
    student = get_student(student_id)
    if student:
        grades = student["grades"]
        return sum(grades) / len(grades)
    return None

def calculate_highest_grade(student_id):
    
    student = get_student(student_id)
    if student:
        return max(student["grades"])
    return None

def calculate_lowest_grade(student_id):
    
    student = get_student(student_id)
    if student:
        return min(student["grades"])
    return None
