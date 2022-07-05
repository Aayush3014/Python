# Q9.	Write a program that has a class called Fraction with attributes 
#       numerator and denominator.
#   a.	Write a method called getdata to enter the values of the attributes.
#   b.	Write a method show to print the fraction in simplified form.

from math import gcd

class Fraction:
    numerator = 0
    denominator = 0 

    def getdata():
        Fraction.numerator = int(input("Enter the Numerator : "))
        Fraction.denominator = int(input("Enter the Denominator : "))


    def show(): 
        d = gcd(Fraction.numerator,Fraction.denominator)
        x = Fraction.numerator // d
        y = Fraction.denominator // d
        print(f"Simplified Form is : {x} / {y}")
        

Fraction.getdata()
Fraction.show()
