# Q3.	Create a Python class named Rectangle constructed by a length and width.
#  a.	Create a method called area which will compute the area of a rectangle.

class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        ar = self.l * self.b
        print(f"Area of Rectangle : {ar}")

a1 = Rectangle(5,4)
a1.area()