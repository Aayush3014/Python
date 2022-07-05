'''24. Write a program to demonstrate hybrid inheritance and show MRO for each class'''

class School():
    def func1(self):
        print("In School")
class Student1(School):
    def func2(self):
        print("In student 1")
class Student2(School):
    def func3(self):
        print("In student 2")
class Student3(Student1,Student2):
    def func4(self):
        print("In Student 3")

print("MRO for each class")
print(School.mro())
print(Student1.mro())
print(Student2.mro())
print(Student3.mro())

# Hybrid Inheritence
S=Student3()
S.func1()
S.func2()
S.func3()
S.func4()
