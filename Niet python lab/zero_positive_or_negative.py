#Python program to check whether the given number is positive negative or zero.

num = float(input("Enter the number : "))
if num > 0:
    print(f'{num} is positive. ')
elif num < 0:
    print(f'{num} is negative. ')
else:
    print(f'{num} is zero. ')
