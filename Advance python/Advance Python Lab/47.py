'''47. Write a Program to convert a numpy array to a dataframe of given shape.'''

import pandas as pd
import numpy as np
myarr = np.array([[10,20,30,20,10],
                  [40,50,60,50,40],
                  [70,80,90,80,70]])
#Converting into Dataframe
df = pd.DataFrame(data = myarr)
print(df)
