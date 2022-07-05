#Python program to find smallest number among three numbers.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
if num1<num2:
    if num1<num3:
        print(f'{num1} is smallest among three. ')
elif num2<num3:
    print(f'{num2} is smallest among three. ')
else:
    print(f'{num3} is smallest among three. ')
