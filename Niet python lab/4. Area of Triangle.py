#Python program to print area of triangle

import math

a=float(input("Enter first side: "))
b=float(input("Enter second side: "))
c=float(input("Enter third side: "))

s=(a+b+c)/2

area=math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f' Area of Triangle of given sides is {area}')
