#WAP to check leap year or not using function.
def leap(year):
    if year%100!=0 and year%4==0 or year%400 == 0 :
        return f"{year} is a leap year."
    else:
        return f"{year} is not a leap year."
year = int(input("Enter the year : "))
print(leap(year))