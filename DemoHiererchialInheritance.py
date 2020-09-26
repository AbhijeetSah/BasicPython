#hiererchial Inheritance
class Shape:
    def setValue(self, s):
       self.s=s

class Square(Shape):
    def area(self):
        return self.s*self.s

class Circle(Shape):
    def area(self):
        return 3.14*self.s*self.s


sq= Square()
s= int(input("Enter the side of square "))
sq.setValue(s)
print("Area of square",sq.area())

cr= Circle()
r= int(input("Enter the radius of circle "))
cr.setValue(r)
print("Area of circle : ", cr.area())