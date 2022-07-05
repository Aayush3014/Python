def f(x):
 for i in range(5):
    yield i
g=f(8)
print(list(g))