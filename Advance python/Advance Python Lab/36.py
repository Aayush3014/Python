'''36. Write a program to create a generator that starts counting
from 0 and raise an exception when counter is equal to 10.'''

import time
def counting():
    num=0
    print("Counting Begins ---->>>> ")
    while True:
        yield num
        num=num+1
        

for i in counting():
    if i==10:
        raise StopIteration
    else:
        print(i)
        time.sleep(0.5)