#WAP to find the HCF of given two numbers.

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

if num1>num2:
    greater = num1

else:
    greater = num2

while greater>0:
    
    if num1%greater==0 and num2%greater==0:
        print(f"HCF of given two numbers is : {greater}")
        break
    
    else:
        greater-=1
