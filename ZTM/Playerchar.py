class playercharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print("run")

player1 = playercharacter("aayush",30)

print(player1.name)
print(player1.age)