class demo:
    def __check(self):
        return "demo"
    def display(self):
        print(self.__check())

class derive(demo):
    def __check(self):
        return "derived"

demo().display()
derive.display()