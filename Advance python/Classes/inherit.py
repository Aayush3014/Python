class user:
    def sign_in(self):
        print("logged in ")
    def attack(self):
        print("do nothing!!!")
class wizard(user):
    def __init__(self,name,power):
        self.name = name 
        self.power = power
    def attack(self):
        user.attack(self)
        print("magic attack")
class archer(user):
    def __init__(self,name,no_of_arrow):
        self.name = name 
        self.no_of_arrow = no_of_arrow
    def attack(self):
        print(f"{self.name} has {self.no_of_arrow} arrows ")
wiz1 = wizard("merlin" , "kudos")
archer1 = archer("queen", 20)
wiz1.attack()
archer1.attack()
