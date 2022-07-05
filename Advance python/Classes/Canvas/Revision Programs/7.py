def f(x):
    yield x+1
    print("test")
    yield x+2
g=f(10)
print(next(g))
print(next(g))
