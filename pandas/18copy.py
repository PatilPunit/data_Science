import pandas as pd
import numpy as np

path='/home/punit/Documents/Ds/pandas/players_20.csv'
df=pd.read_csv(path)
df.set_index('short_name',inplace=True)
df=df[['long_name','age','club','dob','height_cm','weight_kg','nationality']]


print(df)


#this methid is to use to make a copy of dataframe 
# deep = True is the default parameter, no changes were made or modify the copied dataframe basically now copied dataframe has seprate existence
dfc=df.copy()
df.loc['L. Messi','height_cm']=100
print(df)
print(dfc)

#now the deep = False is the prameter use to make a modiefiable copy called Shallow copy so basically this copy also get modiefied when original copy get
dfd=df.copy(deep=False)
df.loc['L. Messi','weight_kg']=91
print(df)
print(dfd)

# simple assignemt as copy
dfq=df
print(dfq)

# this method replcae the sshallow copy as the both copies are dependent
# actully is a shallow copy
df.loc['L. Messi','height_cm']=120
print(df)
print(dfq)