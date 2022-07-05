#Python program to check whether two numbers are divisible by one another.

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

if num1 % num2 == 0:
    print(f"First number {num1} is divisible by Second number {num2}")
else:
    print(f"First number {num1} is not divisible by Second number {num2}")
