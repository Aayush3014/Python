#find marks
marks =[85,96,45,58,96,74]

def finter_vowel(marks):
    vowels = ["a","e","i","o","u"]
    if marks > 80 :
        return True
    else: 
        return False

filter_vowel = filter(finter_vowel,marks)
l1 = list(filter_vowel)
print(l1)
print(filter_vowel)