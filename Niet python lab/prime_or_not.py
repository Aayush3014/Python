#WAP to find whether the entered number are prime or not.

num = int(input("Enter the number : "))
for i in range(1,num+1):
    flag = 0 
    for j in range(2,num//2):
        if i % j == 0:
            flag+=1
if flag == 0 :
    print("Entered number is prime number.")
else:
    print("Entered number is not a prime number.")