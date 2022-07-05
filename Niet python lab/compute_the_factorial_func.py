#WAP to compute the factorial of the given number.
def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f"Factorial of {n} is {f}. "
n = int(input("Enter the number : "))
print(fact(n))