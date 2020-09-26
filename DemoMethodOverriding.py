#WAP TO DEMONSTRATE THE CONCEPT OF METHOD OVERRIDING IN PYTHON
class A:
    def m1(self):
        print("m1 is from A")
    def m2(self):
        print("m2 is from A")
class B(A):
    def m1(self):
        print("m1 is from B")
    def m3(self):
        print("m3 is from B")

a1=A()
a1.m1()
a1.m2()
b1=B()
b1.m1()
b1.m2()
b1.m3()