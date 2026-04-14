import pandas as pd
import numpy as np

df = pd.read_csv("/home/punit/Documents/Ds/pandas/StudentsPerformance.csv")
dfq = pd.read_csv("/home/punit/Documents/Ds/pandas/StudentsPerformance.csv")

#we use head and tail as a data frame selecter

print(df.head()) #first five rows
print(df.tail()) #last five rows

# as we can see the 5 is default value by we can edit thatas a argument
print(df.head(10))
print(df.head(200)) 

# to get dimensions of csv file
print(df.shape) #1000 x 8

# to display n rows


#print(df.to_string())
#print(df.to_string())

a=pd.array([12,3,3,2])
b=np.array([54,2,23,84])
print(a)
print(b)

print(type(a))
print(type(b))