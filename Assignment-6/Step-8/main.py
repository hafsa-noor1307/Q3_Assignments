class Person:
    def __init__(self):
        self.name = "Ahmed"

class Teacher(Person):
    def __init__(self):
        super().__init__()  
        self.subject = "English"
        print(f"{self.name} teaches {self.subject}")

student = Teacher()
