#WAP to display sum of natural numbers.
first_term = int(input("Enter the first term : ")) 
last_term = int(input("Enter the last term : ")) 
s = 0 
print("Sum of natural numbers is printed below upto last term:")
for i in range(first_term,last_term+1):
    s+=i
print(s) 