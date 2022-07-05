'''19. WAP that create a class Student having attribute as name and age and
Marks class inheriting Students class with its own attributes marks1,
marks2 and marks3 as marks in 3 subjects. Also, define the class Result
that inherits the  Marks class with its own attribute total.
Every class has its own display() method to display the corresponding details.
Use __init__() and super() to implement the above classes.'''
class Student():
    def __init__(self,name=None,age=None):
        self.name=input("Enter Name of student: ")
        self.age=int(input("Enter age: "))
    def display(self):
        print("Name of Student : ",self.name)
        print("Age : ",self.age)
        

class Marks(Student):
    
    def get_marks(self,m1=None,m2=None,m3=None):
        self.m1=int(input("Enter the marks in Subject 1 = "))
        self.m2=int(input("Enter the marks in Subject 2 = "))
        self.m3=int(input("Enter the marks in Subject 3 = "))
            
    def display(self):
        super().display()
        print("Marks in Subject 1 = ",self.m1)
        print("Marks in Subject 2 = ",self.m2)
        print("Marks in Subject 3 = ",self.m3)
        
class Result(Marks):
    def display(self,total=None,avg=None):
        self.total=self.m1+self.m2+self.m3
        self.avg=(self.total)/3

        super().display()
        print("Total Marks Obtained By Student is = ",self.total)
        print("Average Marks Of Student is = ",self.avg)

r=Result()
r.get_marks()
r.display()