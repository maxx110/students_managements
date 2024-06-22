# main.py
from student_management import add_student, update_student, calculate_average_grade, save_students, load_students, append_student

def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Calculate Average Grade")
        print("4. Save Students to File")
        print("5. Load Students from File")
        print("6. Append Student to File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            student_id = int(input("Enter student's ID: "))
            grades = input("Enter student's grades (comma-separated): ").split(',')
            grades = list(map(int, grades))
            add_student(name, student_id, grades)
            print("Student added successfully.")

        elif choice == "2":
            student_id = int(input("Enter student's ID to update: "))
            name = input("Enter updated name (leave blank to skip): ")
            grades_input = input("Enter updated grades (comma-separated, leave blank to skip): ")
            grades = list(map(int, grades_input.split(','))) if grades_input else None
            update_student(student_id, name, grades)
            print("Student updated successfully.")

        elif choice == "3":
            student_id = int(input("Enter student's ID to calculate average grade: "))
            avg_grade = calculate_average_grade(student_id)
            if avg_grade is not None:
                print(f"Average grade for student {student_id}: {avg_grade:.2f}")
            else:
                print("Student not found.")

        elif choice == "4":
            filename = input("Enter filename to save students (e.g., students.csv): ")
            save_students(filename)
            print(f"Students saved to {filename}.")

        elif choice == "5":
            filename = input("Enter filename to load students from (e.g., students.csv): ")
            load_students(filename)
            print(f"Students loaded from {filename}.")

        elif choice == "6":
            filename = input("Enter filename to append student to (e.g., students.csv): ")
            name = input("Enter student's name: ")
            student_id = int(input("Enter student's ID: "))
            grades = input("Enter student's grades (comma-separated): ").split(',')
            grades = list(map(int, grades))
            student = {"name": name, "id": student_id, "grades": grades}
            append_student(filename, student)
            print(f"Student appended to {filename}.")

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
