#Python program to compute distance between two points.

import math

x1=float(input("Enter X1 : "))
x2=float(input("Enter X2 : "))
y1=float(input("Enter Y1 : "))
y2=float(input("Enter Y2 : "))

distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

print(f"Distance between the given two lines is = {distance} ")
