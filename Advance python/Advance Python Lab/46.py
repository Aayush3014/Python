'''46. Write a Program to create a series from a list, numpy array and dict'''

import pandas as pd
import numpy as np

#sample List
mylist = ['Photon','in','Double','Slit']
list2Series = pd.Series(mylist,index=['a','b','c','d'])
print("Creating Series from list : ")
print("Original List : ",mylist)
print(list2Series)
print('---'*10+">>>>><<<<<"+'---'*10)
#Sample Numpy Array
myarr = np.array(['M','O','R','P','H','O'])
arr2Series = pd.Series(myarr)
print("Creating Series from Numpy Array : ")
print("Original Array : ",myarr)
print(arr2Series)
print('---'*10+">>>>><<<<<"+'---'*10)
#Sample Dictionary
mydict= {'Russia' : 1, 'Canada' : 2, 'US' : 3, 'China' : 4, 'Brazil' : 5, 'India' :7}
dict2series = pd.Series(mydict,index=['a','b','c','d','e','f'])
print("Creating Series from Dictionary : ")
print("Original Dictionary : ",mydict)
print(dict2series)
print('---'*10+">>>>><<<<<"+'---'*10)
print('---'*10+">>>>><<<<<"+'---'*10)