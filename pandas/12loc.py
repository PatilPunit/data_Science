#loc and iloc are the method use to extract data . so basically to get exact dat by any argument is data extarction.
#loc is method used and extract data by c=specyfying column and row
#iloc is the mrthid where we need to specify the integer value which is 0 based value

import pandas as pd
import numpy as np

link = "/home/punit/Documents/Ds/pandas/players_20.csv"
df = pd.read_csv(link,encoding="ISO-8859-1") 

# niw  we can set index as the shirt name of player
df.set_index('short_name',inplace=True)

df = df[['long_name','age','dob','height_cm','weight_kg','nationality','club']]
print(df)

# to extract the values if given row
print(df.loc['L. Messi'])

# to extract data by given row and column
print(df.loc['L. Messi','long_name'])
print(df.loc['Cristiano Ronaldo','dob'])
print(df.loc['Pan Ximing','nationality'])

#to get all elemnts in a specefic column
print(df.loc[:,'dob'])
print(df.loc[:,'weight_kg'])

# to get all columns corresponds to sepcefic index
print(df.loc['L. Messi',:])

# to slect multiple rows
print(df.loc[['L. Messi','Cristiano Ronaldo']])
# to select theri specefic columns 
print(df.loc[['L. Messi','Cristiano Ronaldo'],['dob']])
# to select multiple columns of specefic row
print(df.loc['L. Messi',['dob','weight_kg']])
# multiple rows and mutliple columns
print(df.loc[['L. Messi','Cristiano Ronaldo'],['dob','club']])

#seleting range of data by slicing

playes=['L. Messi','Cristiano Ronaldo']
print(df.loc[playes,'age':'club'])

#selecting top 10 players
print(df.index[:10]) 
cols=['age','dob','height_cm','weight_kg','club']
players=['L. Messi', 'Cristiano Ronaldo', 'Neymar Jr', 'J. Oblak', 'E. Hazard',
       'K. De Bruyne', 'M. ter Stegen', 'V. van Dijk', 'L. ModriÄ',
       'M. Salah']

print(df.loc['L. Messi':'M. Salah',cols])

#selecting rows with specefic condition

print(df.loc[df['height_cm']>180,cols])
print(df.loc[(df['height_cm']>180) & (df['nationality']=='Argentina'),cols])

#selecting one row in iloc

print(df.iloc[0])

#slecting one row one col
print(df.iloc[0,2])
print(df.iloc[2,1])
#selecitng all elemnts in  specefic cols
print(df.iloc[0,:5])

#selecting all rows woth all or specefic cols

print(df.iloc[:,:2])
print(df.iloc[:10,:4])
print(df.iloc[:,3])

# selecting with list of values
print(df.iloc[[0,1,2],[1,2]])
print(df.iloc[[1,2],[1]])
print(df.iloc[[1],[1,2,3]])
print(df.iloc[[1,2,3],:])

#get data  with slicing

print(df.iloc[0:11,:])
print(df.iloc[1:6,2:4])

# conditions
columns=[1,2,3,4]
print(df.iloc[list(df['age']>30),columns])
print(df.iloc[list((df['age']>30) & (df['club']=='Juventus')),columns])

#set the value in one cell

df.loc['Cristiano Ronaldo','age']=45
df.loc['L. Messi','age']=23
print(df['age'])

#set value to entire columns
df.loc[:,['height_cm']]=900
print(df['height_cm'])

#set values to multiple data
df.loc[['Cristiano Ronaldo','Neymar Jr','J. Oblak'],['club']]='KKR'
print(df['club'])

#set values as condition

df.loc[df['age']>25,'height_cm']=187
print(df[['height_cm','age']])