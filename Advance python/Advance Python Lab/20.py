'''20. Write a program that create a class Distance with members km and metres.
Derive classes School and office which store the distance
from your house to school and office along with other details.'''

class Distance():
    def __init__(self,km=None,metre=None,speed=None,time=None,choice=None):
        self.speed = int(input("Enter speed in km/h = "))
        self.time = float(input("Enter time in hour = "))
        self.km = self.speed*self.time
        self.metre = ((5/18)*self.speed)*(self.time*3600)
       
    def display(self):
        print(round(self.km,3),"KM or",round(self.metre,3),"metre")
        
        
class School(Distance):
    def __init__(self):
        print("Calculating Distance of School from House")
        super().__init__()
    def display(self):
        print("The Distance of School from House is : ",end='')
        super().display()
        
class Office(Distance):
    def __init__(self):
        print("Calculating Distance of Office: ")
        super().__init__()
    def display(self):
        print("The Distance of Office from House is: ",end='')
        super().display()

o=Office()
o.display()
s=School()
s.display()