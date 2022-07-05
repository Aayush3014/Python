#WAP to reverse a number and check if it is a palindrome or not.

num = int(input("Enter the digit : "))
num1 = num
rev = 0 
while num > 0:
    d = num % 10
    rev = rev * 10 + d
    num=num//10
print(f"Reverse of given number is : {rev}")
if rev == num1:
    print("Yes,it is a palindrome.")
else:
    print("No,it is not a palindrome.")
