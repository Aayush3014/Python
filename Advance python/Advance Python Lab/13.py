'''13.Write a Program to illustrate the use of
__str__(), __repr__(), __new__,  __doc__, __dict__, __name__ and __bases__ methods.'''

class Builtin():
    '''This is the  documentation of class'''
    
    def __new__(cls,var1,var2):   #Use of static method __new__()
        print("__new__() method is called")
        inst=object.__new__(cls)
        return inst

    def __init__(self,var1,var2):    #Use of __init__ and __new__() method
        print("__init__() method is called")
        self.var1=var1
        self.var2=var2

    def __repr__(self):
        return "var1=%s,var2=%s"%(self.var1,self.var2)

    def __str__(self):
        return "var1 is %s and var2 is %s"%(self.var1,self.var2)

B=Builtin(40,50)
print("__str__() method",B)   #This will call __str__() method.
print("__repr__() method",[B])  #This will call __repr__() method.

print(" __doc__ method Called by object.__doc__: ",B.__doc__)
print(" __dict__ method Called by object.__dict__: ",B.__dict__)
print(" __name__ method Called by class.__name__: ",Builtin.__name__)
print(" __bases__ method Called by class.__bases__: ",Builtin.__bases__)