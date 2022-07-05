# Q2.	Write a program to implement default constructor, parameterized constructor, and destructor.

class A:
    def __init__(self):        # Default constructor 
        print("Class A")
class B:
    def __init__(self, name, age):     # Parameterised Constructor
        self.name = name
        self.age = age
        print(f"Name : {self.name} \nAge : {self.age}")

a1 = A()
b1 = B("Aayush",18)
del B                   # Destructor
