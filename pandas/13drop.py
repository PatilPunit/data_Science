import pandas as  pd
import numpy as np

#drop method is use to drop means remove the columns or rows
df=pd.read_csv('/home/punit/Documents/Ds/pandas/players_20.csv')
df=df[['short_name','long_name','age','dob','height_cm','weight_kg','club']]
df.set_index('short_name',inplace=True)
df.drop(index=['L. Messi'],axis=0,inplace=True)
df.drop('Neymar Jr',inplace=True)
print(df)
df.drop(columns=['long_name'],axis=0,inplace=True)
df.drop('age',axis=1,inplace=True)
print(df)