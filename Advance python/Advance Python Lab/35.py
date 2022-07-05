'''35. Write a program that create a custom iterator to create even numbers.'''
class Even():
    def __iter__(self):
        self.num=0
        return self
    def __next__(self):
        num=self.num
        self.num+=2
        return num

e=Even()
i=iter(e)
enter=int(input("Enter a Number of terms : "))
for x in i:
    if x>enter:
        break
    else:
        print(x)
print("Operate next(i) to create even number iterator")