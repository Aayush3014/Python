# Q4.	Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a constructor which takes the parameters x and y (these should all be numbers).
#   a.	Write an instance  method called add which returns the sum of the attributes x and y.
#   b.	Write a class method called multiply, which takes a single number parameter a and returns the product of a and MULTIPLIER.
#   c.	Write a static method called subtract, which takes two number parameters, b and c, and returns b - c.
#   d.	Write a method called value which returns a tuple containing the values of x and y.

class Numbers:
    MULTIPLIER = 15
    
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def add(self):
        s = self.x + self.y
        print(f"Sum : {s}")
    
    @classmethod
    def multiply(cls,a):
        cls.a = a
        mul = (Numbers.MULTIPLIER * cls.a)
        print(f"Multiplication : {mul}")

    def subtract(b,c):
        sub = b - c
        print(f"Subtraction : {sub}")        

    def values(self):
        t = (self.x,self.y)
        print(f"Values : {t}")

# Objects
obj1 = Numbers(5,10)
obj1.add()
obj1.multiply(5)
Numbers.subtract(10,5)
obj1.values()