'''32 .Write a program using reduce() function to calculate
the sum of first 10 natural numbers'''

from functools import reduce
def add(x,y):
    return x+y
natural_num=[int(i) for i in range(1,11)]
print("First 10 Natural Numbers are----->>>>")
print(natural_num)

result=reduce(add,natural_num)
print("The Sum of first 10 Natural Number is ---->>>> ",result)