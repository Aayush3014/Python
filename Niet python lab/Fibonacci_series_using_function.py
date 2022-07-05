# WAP to display the Fibonacci series using user defined function.

def fibo_fun(n):
    a = -1
    b = 1 
    print("Fibonacci Series : ")
    for i in range(1,n+1):
        c = a + b
        print(c,end=' ')
        a = b
        b = c
n = int(input("Enter the number of terms : "))
fibo_fun(n)