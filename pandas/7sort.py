import numpy as np
import pandas as pd
#1. by squre  brackets

df = pd.read_csv("/home/punit/Documents/Ds/pandas/StudentsPerformance.csv")

print(df['gender'].sort_values())
print(df['math score'].sort_values())

print(df.sort_values(by="gender"))
print(df.sort_values(by="math score"))

print(df.sort_values(by="gender",ascending= False))
print(df.sort_values(by="math score",ascending=False))

print(df.sort_values(by=["gender","lunch"],ascending= False))
print(df.sort_values(by=["math score",'reading score'],ascending=False))

print(df.sort_values(by=["gender","lunch"],ascending= False,inplace=True))
print(df.sort_values(by=["math score",'reading score'],ascending=False,inplace=True)) # to update original data frame


# for lambda operations 
print(df.sort_values(by=["gender","lunch"],ascending= False,key= lambda col : col.str.lower()))
print(df.sort_values(by=["math score"],ascending=False,key= lambda col : col % 10 == 0))