'''18.  Write a program that has a class Point.
Define another class Location which has two objects (Location and destination)
of class Point. Also, define a function in Location that prints the reflection on the y-axis'''

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get(self):
        return self.x,self.y
class Location(Point):
    def __init__(self,x1,y1,x2,y2):
        self.Location=Point(x1,y1)
        self.Destination=Point(x2,y2)

    def show(self):
        print("Location = ",self.Location.get())
        print("Destination = ",self.Destination.get())

    def Reflection(self):
        self.Destination.x=-self.Destination.x
        print("Reflection = ",self.Destination.x,self.Destination.y)
L=Location(1,2,3,4)
L.show()
L.Reflection()
