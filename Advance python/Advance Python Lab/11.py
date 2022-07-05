# Q11.	Write a program that has a class Point with attributes x and y.
#   a.	Write a method called midpoint that returns a midpoint of a line joining two points.
#   b.	Write a method called length that returns the length of a line joining two points.

import math

class Point:
    
    x1 = int(input("Enter the x1 coordinate : "))
    y1 = int(input("Enter the y1 coordinate : "))
    x2 = int(input("Enter the x2 coordinate : "))
    y2 = int(input("Enter the y2 coordinate : "))

    def midpoint(self):
        x = (Point.x1 + Point.x2)//2
        y = (Point.y1 + Point.y2)//2
        print(f"Midpoint og given line  is ({x},{y})")

    def length(self):
        
        d = math.sqrt((Point.x2 - Point.x1)**2 + (Point.y2 - Point.y1)**2)
        print(f"Length of the line is {round(d,2)}")

line1 = Point()
line1.midpoint()
line1.length()