#Case:3 access static method of parent class using super()
class p:
    a = 10    #Static variable
    b = 30    #Static variable
    def __init__(self):
        self.c = 20    #Instance variable
class c(p):
    def m1(self):
        print(super().b)

v = c()
v.m1()