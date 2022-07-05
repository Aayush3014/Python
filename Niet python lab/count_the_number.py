#WAP to count the number of digit. 

num = int(input("Enter the digit : "))
count = 0
print(f"The number of digits in {num} is :",end=' ')
while num > 0:
    num=num//10
    count+=1
print(count)