# Q8.	Create a class called String that stores a string and all its status details such as number of uppercase letters, lowercase letters, vowels ,consonants and space in instance variables.
#   a.	Write methods named as count_uppercase, count_lowercase, count_vowels, count_consonants and count_space to count corresponding values.
#   b.	Write a method called display to print string along with all the values computed by methods in (a).

class String:

    def __init__(self):
        self.s = input("Enter the string : ")

    
    def count_uppercase(self):
        self.count = 0
        for i in range(len(self.s)):
            if self.s[i].isupper():
                self.count += 1
        print(f"Number of uppercase : {self.count}")

    
    def count_lowercase(self):
        self.count = 0
        for i in range(len(self.s)):
            if self.s[i].islower():
                self.count += 1
        print(f"Number of lowercasecase : {self.count}")

    
    def count_vowels(self):
        self.count = 0
        for i in range(len(self.s)):
            if self.s[i] in 'aeiouAEIOU':
                self.count += 1
        print(f"Number of vowels : {self.count}")

    
    def count_consonants(self):
        self.count = 0
        for i in range(len(self.s)):
            if self.s[i] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                self.count += 1
        print(f"Number of consonants : {self.count}")

    
    def count_space(self):
        self.count = 0
        for i in range(len(self.s)):
            if self.s[i] == ' ' :
                self.count += 1
        print(f"Number of spaces : {self.count}")


s1 = String()
print("--------------------")
s1.count_uppercase()
s1.count_lowercase()
s1.count_vowels()
s1.count_consonants()
s1.count_space()
print("--------------------")

