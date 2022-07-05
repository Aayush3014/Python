# 3.	Create a class Theory with variables: name, m1, m2, m3 to store marks in three # # subjects and a method getdata. Define another class Lab with variables: p1, p2 to store marks in two labs and a method getdata. Define a class Student that extends the above two classes and have a method display to display name, total marks obtained in theory and labs and average marks.

class Theory:

    def getdata(self):
        name = input("Enter Name : ")
        m1, m2, m3 = input("Enter the marks : ").split()

        return (name, m1, m2, m3)


class Lab(Theory):

    def getdata(self):
        p1, p2 = input("Enter Lab marks : ").split()

        return (list(super().getdata()), p1, p2)


class Student(Lab, Theory):

    def display(self):
        p = list(super().getdata())
        name, m1, m2, m3, p1, p2 = p[0][0], int(p[0][1]), int(
            p[0][2]), int(p[0][3]), int(p[1]), int(p[2])

        total_th = m1+m2+m3
        total_lb = p1+p2
        avg_total = (total_th/3) + (total_lb/2)
        print(
            f"Name : {name} \n Total marks in theory : {total_th} \n Total marks in lab : {total_lb} \n Average Marks : {avg_total}")


t = Student()
t.display()
