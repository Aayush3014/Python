#Program to find the reverse of a given number:
a=int(input("enter the number:"))
rev=0
while a>0:
    d=a%10
    a=a//10
    rev=rev*10+d
print(rev)
    
    
