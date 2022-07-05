#WAP to implement calculator on arithmetic operaions.

operation = input("""Enter the choice of operation.\nYou want to implement.\n
+ for addition 
- for subtraction
* for multiplication 
/ for division\n """)

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if operation == '+':
    add = num1 + num2
    print(f"{num1} + {num2} = {add}")
elif operation == '-':
    sub = num1 - num2
    print(f"{num1} - {num2} = {sub}")
elif operation == '*':
    mul = num1 * num2
    print(f"{num1} * {num2} = {mul}")
elif operation == '/':
    div = num1 + num2
    print(f"{num1} / {num2} = {div}")