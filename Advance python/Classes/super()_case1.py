class person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

class student(person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks
    def display(self):
        print("name =",self.name)
        print("age =",self.age)
        print("rollno =",self.rollno)
        print("marks =",self.marks)

class teacher(person):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age)
        self.salary = salary
        self.subject = subject
    def display(self):
        print("name =",self.name)
        print("age =",self.age)
        print("salary =",self.salary)
        print("subject =",self.subject)


s = student("Ayush",18,37,98)
s.display()