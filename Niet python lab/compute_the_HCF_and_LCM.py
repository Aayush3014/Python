#WAP to compute HCF and LCM using function. 
def hcf(num1,num2):
    if num1>num2:
        greater = num1
    else:
        greater = num2
    while greater>0:
        if num1%greater==0 and num2%greater==0:
            return f"HCF of {num1} and {num2} is {greater}."
        else:
            greater-=1

def lcm(num1,num2):
    if num1<num2:
        smaller = num1
    else:
        smaller  = num2
    while True:
        if smaller%num1==0 and smaller%num2==0:
            return f"LCM of {num1} and {num2} is {smaller}."
        else:
            smaller += 1

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(hcf(num1,num2))
print(lcm(num1,num2))


