class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("kitty" , 5)
cat2 = Cat("kitto" , 8)
cat3 = Cat("kittu" , 7)

def oldest(*args):
    return max(args)

print(f'"The oldest cat is {oldest(cat1.age,cat2.age,cat3.age)} years old."')