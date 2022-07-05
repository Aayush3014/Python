'''50. Write a Pandas program to create a line plot of the opening,
closing stock prices of Alphabet Inc. between two specific dates.
Use the alphabet_stock_data.csv file to extract data.'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\Users\kritin23\Downloads\advance_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-09-30')                         
df['Date'] = pd.to_datetime(df['Date']) 
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df2 = df.loc[new_df]
plt.figure(figsize=(10,10))
df2.plot(x='Date', y=['Open', 'Close'])
plt.suptitle('Opening/Closing stock prices of Alphabet Inc.,\n 01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.xlabel("Date",fontsize=12, color='black')
plt.ylabel("$ price", fontsize=12, color='black')
plt.show()