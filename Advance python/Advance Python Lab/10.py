 # Q10.	Write a program that has a class Numbers with a list as an instance variable.
#  a.	Write a method called insert_element that takes values from user. 
#  b.	Write a class method called find_max to find and print largest value in the list.

class Numbers:
    
    def __init__(self):
        self.l = []

    def insert_element(self):
        self.l.append(int(input("Enter the element to be inserted : ")))

    def find_max(self):
        print(f"Largest value in the list is {max(self.l)} ")


n = int(input("Enter the number of elements to be inserted : "))
l1 = Numbers()
for i in range(n):
    l1.insert_element()
l1.find_max()