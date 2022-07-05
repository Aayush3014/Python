#WAP to find largest number among three numbers using function.

def largest(a,b,c):
    if a>b:
        if a>c:
            return f"{a} is the largest amongst three."
    elif b>c:
        return f"{b} is the largest amongst three."
    else:
        return f"{c} is the largest amongst three."

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
print(largest(a,b,c))