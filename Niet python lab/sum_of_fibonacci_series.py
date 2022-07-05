# WAP to display the Sum of Fibonacci series using user defined function.

def fibo_sum(n):
    a = -1
    b = 1 
    s = 0 
    print("Sum of Fibonacci Series : ",end=' ')
    for i in range(1,n+1):
        c = a + b
        s += c
        a = b
        b = c
    print(s)
n = int(input("Enter the number of terms : "))
fibo_sum(n)