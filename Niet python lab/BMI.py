#WAP to calculate BMI of  a person.
weight = float(input("Enter weight in Kgs. : "))
height = float(input("Enter height in meters. : "))
b = weight/(height)**2
print("BMI of the person is :",b)
if b<18.5:
    print("Person is underweight")
elif 18.5<=b<=24.9:
    print("Person is Normal")
elif 25<=b<=29.9:
    print("Personn is overweight.")
else:
    print("Person is obese.")
