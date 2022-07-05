#WAP to display a series of natural number.

last_term = int(input("Enter the last term : ")) 
print("Series of natural numbers is printed below :")
for i in range(0,last_term):
    i+=1
    print(i,end=' ') 