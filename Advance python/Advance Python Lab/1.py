#  Q1. Write a program illustrating class definition and accessing class members.

class Student:
    num_of_student = 50              # Class Variable
    class_teacher = "Sandeep"        # Class Variable

    def __init__(self, rno, name, mks):      # Constructor
        self.rollno = rno                    # Instance Variable
        self.name = name                     # Instance Variable
        self.marks = mks                     # Instance Variable

    def student_info(self):                  # Instance Method
        print("Name :", self.name)
        print("Roll_No :", self.rollno)
        print("Marks :", self.marks)
        print("--------------")


st1 = Student(30, "Martin", 56)
st2 = Student(35, "Franklin", 68)
st1.student_info()
st2.student_info()
print(f" Class Teacher : {Student.class_teacher}")
print(f" Class Strength : {Student.num_of_student}")