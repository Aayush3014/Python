#WAP to find prime number from 1 to n.

lower = int(input("Enter the lower number : "))
upper = int(input("Enter the upper number : "))
for i in range(lower,upper+1):
    if i>1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i,end=' ')