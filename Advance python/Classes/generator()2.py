#implement countdown
import time
def countdown(num):
    print("Countdown Starting.......")
    while num>0:
        yield num
        num-=1

value = countdown(100)
for i in value:
    print(i)
    time.sleep(1)