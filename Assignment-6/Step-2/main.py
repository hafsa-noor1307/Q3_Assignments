class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    
    @classmethod 
    def method(cls):
        print(f"{cls.count} Times object has been created till now!")

counter = Counter()
counter = Counter()
counter = Counter()
counter.method()