# Q5.	Create a class named as Student to store the name and marks in three subjects. Use List to store the marks. 
#   a.	Write an instance method called compute to compute total marks and average marks of a student.
#   b.	Write a method called display to display student information.

class Student:
    
    def info(self):
        self.name =  input("Enter Name : ")
        self.mark1,self.mark2,self.mark3 = input("Enter three marks : ").split()

    def compute(self):
        self.total = int(self.mark1) + int(self.mark2) + int(self.mark3)
        avg = int(self.total)/3
        self.avg = round(avg,2)
    
    def display(self):
        print(f"Name : {self.name}")
        print(f"Marks : {self.mark1} {self.mark2} {self.mark3}")
        print(f"Total marks : {self.total}")
        print(f"Average marks : {self.avg}")

student1 = Student()
student1.info()
student1.compute()
student1.display()