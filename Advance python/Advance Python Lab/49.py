'''49. Write a program to replace missing values in a column of a
dataframe by the mean value of that column'''

import pandas as pd
import numpy as np

#loading the csv file
car_data=pd.read_csv('C:\\Users\\kritin23\\Toyota1.csv')
#Creating a dataframe
df = pd.DataFrame(car_data)
print(df)
#Findig Means Value of column having NaN
mean_value=df['Age'].mean()
print("The Means Value of Age Column is : ",round(mean_value,3))

#Replacing NaNs in column Age with the means values in the same column
df['Age'].fillna(value=mean_value,inplace=True)
print('Updated DataFrame : ')
print(df)