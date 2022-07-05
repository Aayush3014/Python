'''16. Write a program to create class Employee. Display the personal information and
salary details of 5 employees using single inheritance.'''
class Employee():
    empCount=0
    def __init__(self,name,deg,dep,contact,sal):
        self.name=name
        self.deg=deg
        self.dep=dep
        self.contact=contact
        self.sal=sal
        Employee.empCount+=1
        
class Information(Employee):
    def personal(self):
        print("Personal information of Employee "+str(Employee.empCount))
        print("Name of Employee: ",self.name)
        print("Degination: ",self.deg)
        print("Department: ",self.dep)
        print("Contact: ",self.contact)
        print("Salary :",self.sal)
    

i1=Information("Ayush Singh","SD","IT","9162994620",60000)
i1.personal()
i2=Information("Amit Singh","CA","Account","9876543210",50000)
i2.personal()
i3=Information("Pandu Chauhan","GD","Product","9999543210",51000)
i3.personal()
print("There are total "+str(Employee.empCount)+" Employee")