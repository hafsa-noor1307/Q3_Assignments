class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student name is {self.name} and student marks is {self.marks}")

student = Student("Ahmed", 85)
student.display()
        