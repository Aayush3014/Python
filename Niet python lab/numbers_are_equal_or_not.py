#WAP to check whether given two numbers are equal or not.

def equal(num1,num2):
    if num1 == num2:
        return "Yes. Both are equal."
    else:
        return "No. Both are not equal."
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(equal(num1,num2))