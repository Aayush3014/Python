import random
import time

name = ["rohit","mohit","sourav","soham"]
subjects = ["java","python","data science","AI"]
def people_lst(num):
    result = []
    for i in range(num):
        person = {
            "id":i,
            "name": random.choice(name),
            "subject": random.choice(subjects)
            }
        result.append(person)
    return result

def people_gen(num):
    for i in range(num):
        person = {
            "id":i,
            "name": random.choice(name),
            "subject": random.choice(subjects)
            }

        yield person

t1 = time.time()
people = people_lst(100000)
t2 = time.time()
print("time taken by list ",t2-t1)

t3 = time.time()
people = people_gen(100000)
print(next(people))
print(next(people))
print(next(people))

t4 = time.time()
print("time taken by generator ",t4-t3)