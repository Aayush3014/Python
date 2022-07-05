'''33. Write a program that convert a list of temperatures in Celsius
into Fahrenheit using map() function.'''

mytemp=input("Enter temprature in Celcius seperated by space : ").split()
myTemp=[int(i) for i in mytemp]

def toFarenheit(temp):
    return (temp*(9/5))+32

tempF=list(map(toFarenheit,myTemp))

print("The temperature(s) Entered By User in Celcius----->>>>>")
print(myTemp)
print("The temperature(s) converted in Farenheit are ------>>>>>>")
print(tempF)
