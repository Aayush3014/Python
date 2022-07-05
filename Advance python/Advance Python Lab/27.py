'''27. Write a program to overload in Operator'''
class Popular():
    def __init__(self):
        self.max_popularity = {'Python':100,"Java":90,"Ruby":70,"c++":95,"Perl":50}
    def __contains__(self,lan):
        if lan in self.max_popularity:
            return True
        else:
            return False
    def __getitem__(self,lan):
        return self.max_popularity[lan]
    def __str__(self):
        return "The Dictionary has name of Language and its popularity percentage alloted to them"

P=Popular()
print(str(P))
lan = input("Enter the language for which you want to know popularity : ")
if lan in P:
    print("The popularity of Language",lan,"is = ",P[lan])
    
