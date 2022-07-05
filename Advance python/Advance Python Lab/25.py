'''25. Write a program to overload + operator to multiply to
fraction object of fraction class which contain two instance
variable numerator and denominator.Also, define the instance
method  simplify() to simplify the fraction objects'''


class Fraction():
    def __init__(self):
        self.num = 0
        self.deno = 1  # Since denominator cant be zero

    def get(self):
        self.num = int(input("Enter the numenator = "))
        self.deno = int(input("Enter the denomenator = "))

    def simplify(self):  # to simplyfy the fraction object
        common_divisor = Fraction.GCD(self.num, self.deno)
        self.num = self.num//common_divisor
        self.deno = self.deno//common_divisor

    @staticmethod
    def GCD(num, deno):
        if deno == 0:
            return num
        else:
            return Fraction.GCD(deno, num % deno)

    def __add__(self, F):
        Temp = Fraction()
        Temp.num = (self.num*F.deno)+(F.num*self.deno)
        Temp.deno = self.deno*F.deno
        return Temp

    def display(self):
        self.simplify()
        return str(self.num)+"/"+str(self.deno)


F1 = Fraction()
F1.get()
F2 = Fraction()
F2.get()
F3 = Fraction()
F3 = F1+F2
print("Resultant Fraction is = ", F3.display())
