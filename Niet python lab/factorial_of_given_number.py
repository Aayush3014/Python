#WAP to calculate the factorial of given number.
num = int(input("Enter the number : "))
fact = 1
for i in range(1,num+1):
    fact*=i
print(f"Factorial of given number is : {fact}")