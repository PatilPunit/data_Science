#query is a method to filter data
#instead of using comapre and logical operaters we will use query method

import pandas as pd
import numpy as np

df  = pd.read_csv("/home/punit/Documents/Ds/pandas/players_20.csv")
df.set_index('short_name')
df=df[['long_name','age','club','dob','height_cm','weight_kg','nationality']]

age_34= df.query('age > 34') #expression in query methods
print(age_34)
print(df[df['age']>34])  #expression in boolean slicing

age_nat=df.query("age>34 & nationality=='Argentina' ")
print(age_nat)
age_nat=df.query("age>34 and nationality=='Argentina' ")
print(age_nat)

print(df[(df['age']>34)&(df['nationality']=='Italy')])

age_not34=df.query("not (age > 34)")
print(age_34)

#players born after 1990
# import datetime as dt
df['dob']=df['dob'].astype('datetime64[s]')
born_1990=df.query('dob.dt.year > 1990')
print(born_1990)