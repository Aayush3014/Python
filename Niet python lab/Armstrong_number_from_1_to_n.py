#WAP to find Armstrong number from 1 to n terms.
num1 = int(input("Enter first term : "))
num2 = int(input("Enter last term : "))
for value in range(num1,num2+1):
    
    #Finding length of value
    count = len(str(value))
    
    s = 0
    arms = value 
    while value>0:
        d = value % 10
        s += d**count
        value = value // 10
    if arms == s:
            print(s) 