'''26. Write a program to compare two-person object
based on their age by overloading > operator.'''

print("Hello User ! A person is 18 year 8 month and 8 days old, Hence Enter the value Accordingly")
print("Enter the Date of birth to compare AGE from the foramt DD/MM/YYYY")
class Person():
    def __init__(self):
        self.d=self.m=self.y=0
        
    def get(self):
        self.d = int(input("Enter the Day = "))
        self.m = int(input("Enter the Month = "))
        self.y = int(input("Enter the Year = "))
    def __gt__(self,P):    #__gt__ > and __It__ <
        Flag = False
        if self.y>P.y:
            if self.m>P.m:
                if self.d>P.d:
                    Flag = True
        return Flag

P1=Person()
P1.get()
P2=Person()
P2.get()
print("P1 > P2",P1>P2)
    
        
        
