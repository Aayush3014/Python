class person:
    def m1(self):
        print("I am a person.")
class student(person):
    def m1(self):
        print("I am a student.")
class teacher(student):
    def __init__(self):
        super(teacher,self).m1()
    def m1(self):
        print("I am a teacher.")

t = teacher()