# Q6.	Create a class Employee that keeps a track of the number of employees in an organization and also stores their name, designation and salary details.
#   a.	Write a method called getdata to take input (name, designation, salary) from user.
#   b.	Write a method called average to find average salary of all the employees in the organization.
#   c.	Write a method called display to print all the information of an employee.

class Employee:
    count = 0
    sum = 0
    def getdata(self):
        self.name = input("Enter Name of Employee : ")
        self.designation = input("Enter Designation of Employee : ")
        self.salary = int(input("Enter Salary of Employee : "))
        Employee.sum += self.salary
        Employee.count += 1
    
    def average():
        avg = (Employee.sum)/(Employee.count)
        print(f"Average Salary : {avg}")
        print(f"Total Employees : {Employee.count}")
        
    def display(self):
        print(f"Name : {self.name}")
        print(f"Designation : {self.designation}")
        print(f"Salary : {self.salary}")

emp1 = Employee()
emp1.getdata()
emp1.display()