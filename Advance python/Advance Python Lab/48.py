'''48.Write a program to count number of missing values in each column.'''

import pandas as pd
import numpy as np
cars_data1 = pd.read_csv('C:\\Users\\kritin23\\Toyota1.csv')
df = pd.DataFrame(cars_data1)
print(df)

#Showing the NaN value or boolean DataFrame
print("Show the boolean Dataframe: \n \n",df.isnull())
#Count total NaN at each column :
print("NaN value in each column: ",df.isnull().sum())
