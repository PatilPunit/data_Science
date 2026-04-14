import numpy as np
import pandas as pd
#1. by squre  brackets

df = pd.read_csv("/home/punit/Documents/Ds/pandas/StudentsPerformance.csv")


# math operations

print(df['math score'].max())
print(df['math score'].count())

print(df['math score'].min())
print(df['math score'].mean())
print(df['math score'].std())

# operations on rows

print(df['math score'] + df['reading score'] + df['writing score'])
dfq=(df['math score'] + df['reading score'] + df['writing score'])/3
print(dfq)

print(df['gender'].count())
print(df['gender'].value_counts())

print(df['parental level of education'].value_counts())