'''30. WAP to inspect the program code using the functions of inspect module.'''

#1. isclass()
import inspect
class A(object):
    pass
print(inspect.isclass(A))

#2. ismodule()
import numpy
print(inspect.ismodule(numpy))

#3. isfunction()
def fun(a):
    return 2*a
print(inspect.isfunction(fun))

#4. ismethod()
import collections
print(inspect.ismethod(collections.Counter))

#5. getmro()
class A(object):
    pass
class B(A):
    pass
class C(B):
    pass
print(inspect.getmro(C))  

#6. getmembers()
import inspect
import math
print(inspect.getmembers(math))

#7. sinnature()
import collections
print(inspect.signature(collections.Counter))

#8. stack()
def Fibonacci(n):
    if n < 0:
        return 0
  
    elif n == 0:
        return 0
  
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
Fibonacci(12)
print(inspect.stack())

#9. getsource()
def fun(a,b):
    return a*b
print(inspect.getsource(fun))

#10. getdoc()
import inspect
from tkinter import *
root = Tk()
root.title('Ayush')
print(inspect.getdoc(root))
root.mainloop()