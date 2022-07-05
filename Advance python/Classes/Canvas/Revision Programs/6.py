def f(x):
    def f1(a, b):
        print("hello")
        if b==0:
            print("NO")
            return
        return f(a, b)
    return f1
@f
def f(a, b):
    return a%b
f(4,0)