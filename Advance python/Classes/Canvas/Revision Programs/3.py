class A:
    def one(self):
        return self.two()

    def two(self):
        return "A"

class B(A):
    def two(self):
        return "B"

ob1=A()
ob2=B()
print(ob1.two(),ob2.two())
print(ob1.one())