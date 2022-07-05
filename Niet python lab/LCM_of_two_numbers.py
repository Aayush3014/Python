#WAP to find the LCM of given two numbers.

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

if num1<num2:
    smaller = num1

else:
    smaller = num2

while smaller>0:
    
    if smaller%num1==0 and smaller%num2==0:
        print(f"LCM of given two numbers is : {smaller}")
        break
    
    else:
        smaller+=1
