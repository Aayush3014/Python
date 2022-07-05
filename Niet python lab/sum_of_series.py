# WAP compute the sum of the series using user defined function

def sumOfSeries(num): 

    res = 0
    fact = 1
      
    for i in range(1, num+1): 
        fact *= i 
        res = res + (i/ fact) 
          
    return res 
      
n = int(input("Enter number:"))
print("Sum: ", sumOfSeries(n))