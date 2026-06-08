import json

class StudentManager:
    
    def __init__(self):
        self.students = []
        self.load_from_file()
    
    def save_to_file(self):
        data = []
        for s in self.students:
            data.append({
                "student_id": s.student_id,
                "name": s.name,
                "age": s.age,
                "course": s.course,
                "marks": s.marks
            })

        with open("students.json", "w") as f:
            json.dump(data, f)


    def load_from_file(self):
        try:
            with open("students.json", "r") as f:
                data = json.load(f)
                self.students = []

                from models import Student

                for d in data:
                    s = Student(
                        d["student_id"],
                        d["name"],
                        d["age"],
                        d["course"],
                        d["marks"]
                    )
                    self.students.append(s)

        except FileNotFoundError:
            self.students = []

    def add_student(self, student):
        # Check if ID already exists
        for s in self.students:
            if s.student_id == student.student_id:
                print("Error: Student ID already exists!")
                return

        # If ID is unique, add student
        self.students.append(student)
        self.save_to_file()
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
        for s in self.students:
            s.display()

    def search_student(self, search):
        found = False
        for s in self.students:
            if s.student_id == search or s.name.lower() == search.lower():
                s.display()
                found = True

        if not found:
            print("Student not found.")

    def delete_student(self, search_id):
        for s in self.students:
            if s.student_id == search_id:
                confirm = input("Are you sure? (yes/no): ")
                if confirm == "yes":
                    self.students.remove(s)
                    self.save_to_file()
                    print("Deleted successfully.")
                return
        print("Student not found.")

    def update_student(self, search_id):
        for s in self.students:
            if s.student_id == search_id:
                print("Student found. Leave blank to keep old value.\n")

                # Update Name
                new_name = input(f"Enter Name ({s.name}): ")
                if new_name.strip():
                    s.name = new_name

                # Update Age (with validation)
                from utils import validate_int
                while True:
                    age_input = input(f"Enter Age ({s.age}): ")
                    if not age_input.strip():
                        break  # keep old value
                    age = validate_int(age_input, "Age")
                    if age is not None:
                        s.age = age
                        break

                # Update Course
                new_course = input(f"Enter Course ({s.course}): ")
                if new_course.strip():
                    s.course = new_course

                # Update Marks (with validation)
                while True:
                    marks_input = input(f"Enter Marks ({s.marks}): ")
                    if not marks_input.strip():
                        break  # keep old value
                    marks = validate_int(marks_input, "Marks")
                    if marks is not None:
                        s.marks = marks
                        break

                print("Student updated successfully!")
                return

        print("Student not found.")