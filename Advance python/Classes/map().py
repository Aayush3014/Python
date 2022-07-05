def square(x):
    return x*x
l1 = [2,4,6,8]
t = map(square,l1)
for i in range(len(l1)):
    print(next(t),end=' ')