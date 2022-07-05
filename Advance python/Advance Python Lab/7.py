# Q7.	Create a Python class named Circle constructed by a radius. Use a class variable to define the value of constant PI. 
#   a.	Write two methods to be named as area and circum to compute the area and the perimeter of a circle respectively by using class variable PI. 
#   b.	Write a method called display to print area and perimeter.

class Circle:
    PI = 3.14
    
    def __init__(self,r):
        self.r = r
    
    def area(self):
        self.ar = Circle.PI * self.r * self.r

    def circum(self):
        self.cr = round((2 * Circle.PI * self.r),4)

    def display(self):
        print(f"Area : {self.ar}")
        print(f"Circumference : {self.cr}")

c1 = Circle(5)
c1.area()
c1.circum()
c1.display()
