#WAP to compute the C(n,r) using function.
import math

def cnr(n,r):
    c = (math.factorial(n))/((math.factorial(r))*((math.factorial(n-r))))
    return f"After computation C(n,r) is {c}"

n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))
print(cnr(n,r))
