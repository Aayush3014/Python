#Case 4 : we can call IM+CM+SM of parent class in child class with the help of super()---> Valid.

class p:
    
    def __init__(self):
        print("Parent constructor ")
    
    #Instance method
    def m1(self):
        print("Parent instance method ")
    
    @classmethod
    def m2(cls):
        print("Parent class method")
    
    @staticmethod
    def m3():
        print("Parent static method")

class c(p):
    
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    
    def m4(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

t = c()
t.m4()