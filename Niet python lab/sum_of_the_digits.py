#WAP to find the sum of digits.

num = int(input("Enter the digit : "))
s = 0
print(f"Sum of digits of {num} is : ",end=' ')
while num > 0:
    d = num % 10
    s+=d
    num//=10
print(s)  