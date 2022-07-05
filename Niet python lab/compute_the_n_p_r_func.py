#WAP to compute the P(n,r) using function.
import math

def pnr(n,r):
    c = (math.factorial(n))/((math.factorial(n-r)))
    return f"After computation P(n,r) is {c}"

n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))
print(pnr(n,r))
