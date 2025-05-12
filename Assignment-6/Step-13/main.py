class Engine:
    def start(self):
        print("Engine Starting...")

class Car(Engine):
    def __init__(self):
        self.start()

engine = Car()
