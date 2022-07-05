#finding largest and smallest from list 

from functools import reduce

def large(a,b):
    greater = 0
    if a>b:
        greater = a
    else: 
        greater = b

    return greater

def small(a,b):
    smaller = 0
    if a<b:
        smaller = a
    else:
        smaller = b
    return smaller

score = [1100,5200,3100,5400,5500,600]

#using lambda
#largest = reduce(lambda a,b:a if a>b else b,score)
#smallest = reduce(lambda a,b:a if a<b else b,score)

#Normal
largest = reduce(large,score)
smallest = reduce(small,score)
print(f"Largest : {largest}")
print(f"Smallest : {smallest}")
