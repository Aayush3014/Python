#WAP to find the sum of digits of given number.

def sum_digit(n):
    m = n 
    s = 0 
    for i in range(1,n+1):
        d = m % 10  
        s = s + d
        m = m//10
    print("Sum of digits of given number is :",s)
n = int(input("Enter the number : "))
sum_digit(n)