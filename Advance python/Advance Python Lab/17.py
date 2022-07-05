'''17. WAP that extends the class Employee. Derive two classes
Manager and Team Leader from Employee class.
Display all the details of the employee working under a particular Manager and Team Leader. '''
class Employee():
    empCount=0
    def __init__(self,name=None,age=None,exp=None,dept=None,contact=None,qual=None):
        self.name=input("Enter name of Employ: ")
        self.age=int(input("Enter Age of Employee: "))
        self.exp=int(input("Enter experience of Employee in Year: "))
        self.dept=input("Enter department of Employee: ")
        self.contact=input("Enter Contact Number: ")
        self.qual=input("Enter Highest Qualification: ")
        Employee.empCount+=1
    def display(self):
        print("Name of Employee : ",self.name)
        print("Age : ",self.age)
        print("Experince: ",self.exp)
        print("Department: ",self.dept)
        print("Contact: ",self.contact)
        print("Qualification: ",self.qual)
        print("\n")

class Manager(Employee):
    def __init__(self,name1=None):
        self.name1=input("Enter the name of Manager: ")
        Employee.__init__(self)
    def displayData(self):
        print("Detail of Employee Working Under Manager Mr "+self.name1+" are : ")
        super().display()
        
class Team_Leader(Employee):
    def __init__(self,name2=None):
        self.name2=input("Enter the name of Team_leader: ")
        Employee.__init__(self)
        
        
    def DisplayData(self):
        print("Detail of Employee Working Under Team_Leader Mr "+self.name2+" are : ")
        super().display()
        

t=Team_Leader()
t.DisplayData()
m=Manager()
m.displayData()
print("The Total number of Employee is: ",Employee.empCount)