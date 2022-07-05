from functools import reduce

def sum(a,b):
    print(f"a = {a}, b = {b} , {a} + {b} = {a+b}")
    return a+b

score = [100,200,300,400,500,600]
total = reduce(sum,score)
print(total)