'''44. Write a NumPy program to create an array of (3, 4)
shape, multiply every element value by 3 and display the new array.'''

import numpy as np
arr1=np.arange(1,13)
arr1=arr1.reshape(3,4)
print("Array of shape (3,4)---->>>\n",arr1)
print()
newarr=arr1*3
print("Array after multiplying every element by e --->>>>\n",newarr)