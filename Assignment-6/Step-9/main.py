from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        print("Hello From Shape")

class Rectangle(Shape):
    def area(self):
        print("Hello From Rectangle")


abstract_2 = Rectangle()
abstract_2.area()