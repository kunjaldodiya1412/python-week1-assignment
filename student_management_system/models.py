class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Course: {self.course} | Marks: {self.marks}")