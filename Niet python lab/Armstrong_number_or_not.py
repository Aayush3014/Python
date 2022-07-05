#WAP to check whether the entered number is armstrong or not.

num = int(input("Enter the number : "))
num1,num2 = num,num
count = 0 
s = 0
while num>0:
    num = num//10
    count+=1
while num1>0:
    d = num1 % 10
    s = s + d**(count)
    num1 = num1//10 
if s == num2:
    print("Given number is armstrong number.")
else:
    print("Given number is not an armstrong number.")

