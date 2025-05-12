class Countdown:
    def __init__(self, num):
        self.num = num
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num < 0:
            raise StopIteration
        current = self.num
        self.num -= 1
        return current
    
countdown = Countdown(10)
for i in countdown:
    print(i)