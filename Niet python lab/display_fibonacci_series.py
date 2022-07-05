#WAP to dispaly fibonacci series.
num = int(input("Enter number of terms to be printed : "))
a = -1
b = 1
print("Fibonacci series : ",end=' ')
for i in range(1,num+1):
    c = a + b
    print(c,end=' ')
    a = b 
    b = c
