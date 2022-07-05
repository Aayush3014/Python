#using lambda
from functools import reduce

score = [100,200,300,400,500,600]
total = reduce(lambda a,b:a+b,score)
print(total)