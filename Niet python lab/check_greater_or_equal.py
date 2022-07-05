#Program to find greater among two numbers also check if they are equal.


def check(x,y):
    if x>=y:
        if x==y:
            print("both number are equal")
        else:
            print(x,"is greater than",y)
    else:
        print(y,"is greater than",x)
    return 

    
x=float(input("enter first number:"))
y=float(input("enter second number:"))
print(check(x,y))