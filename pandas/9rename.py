# here is how rename and overwrite columns

import numpy as np
import pandas as pd

df = pd.read_csv("/home/punit/Documents/Ds/pandas/StudentsPerformance.csv")

print(df.rename(columns={"gender":"Gender"}))
print(df.rename(columns={"gender":"Gender","math score" : "MS","reading score": "rs"}))

# to rename index
df.rename(index={0:"Gen" ,1: "ma",2: "fg"},inplace=True)
print(df)