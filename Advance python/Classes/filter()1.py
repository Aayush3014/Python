letters = ["a","b","c","d","e","f","g","h"]

def finter_vowel(letters):
    vowels = ["a","e","i","o","u"]
    if letters in vowels:
        return True
    else: 
        return False

filter_vowel = filter(finter_vowel,letters)
l1 = list(filter_vowel)
print(l1)
print(filter_vowel)