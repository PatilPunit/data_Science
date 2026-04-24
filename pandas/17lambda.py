import pandas as pd
import numpy as np

path='/home/punit/Documents/Ds/pandas/players_20.csv'
df=pd.read_csv(path)
df.set_index('short_name',inplace=True)
df=df[['long_name','age','club','dob','height_cm','weight_kg','nationality']]


print(df)

#lambda is the function which one lined simple function

#normal function
def sum(a,b):
    return a+b

sum=lambda a,b:a+b
print(sum(5,10))

#lambda is useful due tto its simplicity
hm=df['height_cm'].apply(lambda x : x/100)
print(hm)

long_upper=df['long_name'].apply(lambda x : str.upper(x))
print(long_upper)


df['dob']=df['dob'].astype('datetime64[s]')
print(df.dtypes)
dob_year=df['dob'].apply(lambda x:x.year)
print(dob_year)