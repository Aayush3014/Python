'''37. Write a program to create a generator to print the Fibonacci number.'''

def Fibonacci(terms):
    x,y=0,1
    print(x,end=' ')
    for _ in range(terms):
        x,y=y,x+y
        yield x
for i in Fibonacci(10):
    print(i,end=' ')
    
#This is an Example of PipeLine Generator
