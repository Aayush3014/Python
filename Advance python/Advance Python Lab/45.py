'''45. Write a NumPy program to compute the multiplication of two given matrixes.'''

import numpy as np
mat1 = [[1, 0, 1], [0, 1, 1],[1,1,1]]
mat2 = [[1, 2], [3, 4],[5,6]]
#Showing origianl Matrix
print("original matrix:")
print(mat1)
print(mat2)
result = np.dot(mat1,mat2)
print("Result of the said matrix multiplication:")
print(result)

