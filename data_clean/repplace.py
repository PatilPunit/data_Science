import pandas as pd
df=pd.read_csv('/home/punit/Documents/Ds/pandas/netflix.csv')
print(df.head())
print(df['title'].head(20))

df['title'].str.replace(['^\w\s'],'',regex=True)
print(df['title'].head(20))