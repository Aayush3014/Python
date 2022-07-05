#Program to calculate mid points of a line segment.

x1 = float(input("Enter X1: "))
x2 = float(input("Enter X2: "))
y1 = float(input("Enter Y1: "))
y2 = float(input("Enter Y2: "))

mid_point_x = (x1 + x2)/2
mid_point_y = (y1 + y2)/2

print(f'Mid Points of Given Line Segment is {mid_point_x} and {mid_point_y}')
