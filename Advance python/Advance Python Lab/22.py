'''22.Write a program that has a class Polygon.
Derive two classes Rectangle and triangle from polygon and write
methods to get the details of their dimensionsand  hence calculate the area'''

class Polygon():
    def get_data(self):
        raise NotImplementedError()
    def area(self):
        raise NotImplementedError()

class Rectangle(Polygon):
    def get_data(self):
        self.length=float(input("Length of Rectnagle   = "))
        self.breadth=float(input("Breadth of Rectabgle = "))
    def area(self):
        return self.length*self.breadth

class Triangle(Polygon):
    def get_data(self):
        self.a=float(input("Enter side a = "))
        self.b=float(input("Enter side b = "))
        self.c=float(input("Enter side c = "))
        self.s=(self.a+self.b+self.c)/2

    def area(self):
        return (self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))**0.5

R=Rectangle()
R.get_data()
print(" Area of Rectangle is =",R.area())
T=Triangle()
T.get_data()
print(" Area of Triangle is =",T.area())
