#  WAP that accepts the marks of 5 subjects and finds the percentage marks obtained by
# the student. It also prints grades according to the following criteria:
# Between 90-100%-----------Print 'A'
# 80-90%------------------------Print 'B'
# 60-80%------------------------Print 'C'
# 50-60%------------------------Print 'D'
# 40-50%------------------------Print 'E'
# Below 40%-------------------Print 'F’

print('\t \t ------Percentage Caculator--------')
eng = float(input("Enter marks obtained in English : "))
hin = float(input("Enter marks obtained in Hindi : "))
mat = float(input("Enter marks obtained in Maths : "))
sci = float(input("Enter marks obtained in Science : "))
sst = float(input("Enter marks obtained in S.st : "))
Total_marks = 500
obtained_marks = eng + hin + mat + sci + sst
percentage = (obtained_marks/Total_marks) * 100
print(f" Total Percentage obtained by the student is {percentage}")
if 90 <= percentage <= 100:
    print('Grade A')
elif  80 <= percentage <= 90:
    print('Grade B')
elif 70 <= percentage <= 80:
    print('Grade C')
elif 60 <= percentage <= 70:
    print('Grade D')
elif 50 <= percentage <= 60:
    print('Grade E')
elif 40 <= percentage <= 50:
    print('Grade F')