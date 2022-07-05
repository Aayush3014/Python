#WAP to check whether the entered number is prime or not using function.

def prime(n):
    for i in range(1,n+1):
        flag = 0 
        for j in range(2,n//2):
            if i % j == 0 :
                flag+=1
    if flag == 0 :
        print(f"Given number {n} is prime.")
    else:
        print(f"Given number {n} is not a prime.")

n = int(input("Enter the number : "))
prime(n)