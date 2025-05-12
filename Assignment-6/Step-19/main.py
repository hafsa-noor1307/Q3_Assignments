class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor


multiply_by_5 = Multiplier(5)

result = multiply_by_5(10)   

print(result)  

print(callable(multiply_by_5))  
