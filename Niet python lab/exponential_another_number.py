#WAP to find the exponential of a number w.r.t. another number.

def power(base,expo):
    return f"Exponential of given paramteres are : {base**expo}"

base = int(input("Enter the base value : "))
expo = int(input("Enter the exponent value : "))
print(power(base,expo))
