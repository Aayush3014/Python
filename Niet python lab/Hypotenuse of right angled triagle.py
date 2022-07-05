#Python Program to Calculate Hypotenuse of right-angled triangle
# h = ((p*p) + (b*b))**(0.5)

p = float(input("Enter Perpendicular : "))
b = float(input("Enter Base : "))

h = ((p * p) + (b * b)) ** (0.5)

print(f"Hypotenuse is : {h}")
