class fruit:
    def __init__(self,price):
        self.price=price
obj=fruit(50)
obj.qty=10
obj.bag=2
print(obj.qty+len(obj.__dict__))
