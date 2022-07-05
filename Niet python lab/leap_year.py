#Python program to check whether the entered year is leap year or not.

year = int(input("Enter the year : "))
if (year % 100 != 0) and (year % 4 == 0) or (year % 400 == 0):
    print(f"Entered Year {year} is a Leap Year ")
else:
    print(f"Entered Year {year} is not a Leap Year ")
