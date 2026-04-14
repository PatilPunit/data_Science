# there are attributes methods and functions for pandas
#1. Attributs are the associated value to an object , accesd by . operater  ex. df.columns
#2.function is the group of realted statements - max() ,min()
# methods are the functions within the class - 

import pandas as pd
import numpy as np
df = pd.read_csv("/home/punit/Documents/Ds/pandas/StudentsPerformance.csv")


#attributes - (df nantar je pana sarkha dista te sagle attributes ahet)
print(df.shape)

print(df.columns)

print(df.empty)

print(df.index)

print(df.ndim)

print(df.plot)

print(df.size)

print(df.dtypes)

print(df.at[9,'lunch'])  # use to  acces specefic cell by rwo and coluns

r = df.loc[:,['lunch']] #retruns all rows or columns selected
r = df.loc['4',['lunch']]
r = df.loc[[4],['lunch']] #with row and column
print(r)

#methods  (df nantar je 3d box sarkha disel te methods)

print(df.head() )

print(df.tail())

print(df.all())

print(df.info())

print(df.describe())

#functions


print(len(df))
print(max(df))
print(min(df))
print(sorted(df))