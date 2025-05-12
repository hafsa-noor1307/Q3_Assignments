class A:
    def show(self):
        print("Hello From A")

class B(A):
    def show(self):
        print("Hello From B")

class C(A):
    def show(self):
        print("Hello From C")
    
class D(B,C):
    pass

D_Object = D()
D_Object.show()