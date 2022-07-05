# Q15.	Write a program to illustrate the use of following built-in methods:
#   a.	hasattr(obj,attr)
#   b.	getattr(object, attribute_name [, default])
#   c.	setattr(object, name, value)
#   d.	delattr(class_name, name)

class Student:
    age = 18
    name = 'John'

student = Student()

#hasattr
print('Student has age?:', hasattr(Student, 'age'))
print('Student has marks?:', hasattr(Student, 'marks'))

#getattar
print('The age is:', getattr(Student, "age"))
print('The age is:', Student.age)

#setattr
print('Before modification:', Student.name)
setattr(Student, 'name', 'Aayush')
print('After modification:', Student.name)

#delattr
print(delattr(Student, Student.name)) #this will show error because the name Adam has been deleted by using (delattr)