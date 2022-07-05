#Python program to solve Quadritic equation

''' General form of Quadritic Equation'''

import cmath

a=float(input("Enter First Number: "))
b=float(input("Enter First Number: "))
c=float(input("Enter First Number: "))

d = (b**2) - (4*a*c)

x = (-b+cmath.sqrt(d))/(2*a)
y = (-b-cmath.sqrt(d))/(2*a)

print(f'The solution of given Quadritic Equation \n {x} \n {y} ')