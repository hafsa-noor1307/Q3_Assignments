class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"Woah Woah From {self.name}")
    
dog = Dog("Puppy", "Kashmir")
dog.bark()