from models import Student
from student import StudentManager
from utils import get_valid_int

manager = StudentManager()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        age = get_valid_int("Enter Age: ", "Age")
        course = input("Enter Course: ")
        marks = get_valid_int("Enter Marks: ", "Marks")

        s = Student(sid, name, age, course, marks)
        manager.add_student(s)

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        sid = input("Search for a student by ID or name: ")
        manager.search_student(sid)

    elif choice == "4":
         sid = input("Enter ID to update: ")
         manager.update_student(sid)

    elif choice == "5":
        sid = input("Enter ID to delete: ")
        manager.delete_student(sid)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")