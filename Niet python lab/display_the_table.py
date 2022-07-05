#WAP to print the table of given number.
num = int(input("Enter the number : "))
prod = num
print("Table of give number is : ")
for i in range(1,11):
    prod=num * i
    print(f'{num} * {i} = {prod}')
