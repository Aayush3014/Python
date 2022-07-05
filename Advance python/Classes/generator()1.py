def mygen():
    yield "a"
    yield "b"
    yield "c"

g = mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))