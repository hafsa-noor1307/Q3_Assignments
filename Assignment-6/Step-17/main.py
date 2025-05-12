def add_greeting(cls):
    def greet(self):
        return("Hello From Decorater!")
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    
person = Person("Ahmed")
print(person.greet())


