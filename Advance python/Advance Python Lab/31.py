'''31. Write a program to create a new list containing
the first letters of every element in an already existing list.'''

A=input("Enter String : ").split()
mylist=[str(i) for i in A]
def first_letter(mylist):
    for i in mylist:
        return i[0]
    
newlist=list(map(first_letter,mylist))

print("Old List = ",mylist)
print("New List = ",newlist)
