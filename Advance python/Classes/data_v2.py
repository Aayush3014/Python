import matplotlib.pyplot as p
import pandas as pd
data = pd.read_csv("C:\\Users\\kritin23\\Toyota1.csv")
p.scatter(data["Age"],data["Price"],c = "red")
p.title("AIB Scatter")
p.xlabel("Age")
p.ylabel("Price")
p.show()