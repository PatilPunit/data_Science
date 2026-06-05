import pandas as pd
import matplotlib.pyplot as pl

df=pd.read_csv('/home/punit/Documents/Ds/pandas/netflix.csv')
print(df.head())

df['duration']=df['duration'].str.extract(r'(\d+)')
df['duration']=pd.to_numeric(df['duration'],errors='coerce')

df['duration'].plot(kind='hist')
pl.show()

print(df['duration'].value_counts(bins=10).sort_index())
print(df[(df['duration']>32)&(df['duration']<280)])


df['duration'].plot(kind='box')
pl.show()

#IQR = Q3-Q1

print(df.describe())
min=2-1.5*(106-2)
max=106+1.5*(106-2)
print('Min : ',min,' Max : ',max)

print(df[~((df['duration']>-154)&(df['duration']<262))])