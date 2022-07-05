'''23. Write a program that extends the class Shape to calculate
the area of a circle and a cone .(use super to inherit base class methods'''

class Shape():
    PI=3.14
    def __init__(self,radius=None):
        self.radius=int(input("Enter Radius = "))

class Circle(Shape):
    def area(self):
        return Shape.PI*self.radius*self.radius

class Cone(Shape):
    def get_data(self):
        self.s=int(input("Enter slant height = "))
    def area(self):
        return Shape.PI*self.radius*(self.radius+self.s)

C=Circle()
print("The Area of the circle is = ",C.area())
cone=Cone()
cone.get_data()
print("The Area of the cone is = ",cone.area())
    
