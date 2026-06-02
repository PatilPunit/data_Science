import pandas as pd
df=pd.read_csv('/home/punit/Documents/Ds/pandas/netflix.csv')
print(df.head())


#checking datatypes
print(df.dtypes) #one column is int rest all are strings

#validating shape
print(df.shape)
