class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name, employee_name):
        self.depart = department_name
        self.employee = employee_name

    def show_details(self):
        print(f"Department Name is {self.depart}") 
        print(f"Employee name is {self.employee.name}")


employee = Employee("Ahmed")
depart = Department("HR", employee)
depart.show_details()

