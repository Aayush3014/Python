#WAP to swap the values of variables.
def swap(a,b):
    t = a
    a = b 
    b = t 
    return f"value of a is {a} and value of b is {b} "
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
print(f"value of a is {a} and value of b is {b}")
print(swap(a,b))
