# Q14.	Create a BankAccount class. Your class should support the following methods:
#   a.	__init__(self, account_no)
#   b.	deposit (self, account_no, amount)
#   c.	withdraw (self, account_no, amount)
#   d.	get_balance (self, account_no)

class BankAccount:

    def __init__(self,account_no):
        self.account_no = account_no
        self.amount = 0

    def deposit(self, account_no, amount):
        self.account_no = account_no
        self.amount += amount

    def withdraw(self, account_no, amount):
        self.account_no = account_no
        self.amount -= amount

    def get_balance(self, account_no):
        self.account_no = account_no
        print(f"Account Number is : {self.account_no}")
        print(f"Total balance : {self.amount}")
        print("----------------------------")


a1 = BankAccount(100222110145605)
a1.deposit(100222110145605,100)
a1.withdraw(100222110145605,40)
a1.get_balance(100222110145605)
a2 = BankAccount(200222110145605)
a2.deposit(200222110145605,150)
a2.withdraw(200222110145605,50)
a2.get_balance(200222110145605)