import pandas as pd
df=pd.read_csv('/home/punit/Documents/Ds/pandas/netflix.csv')
print(df.head())

print(df['title'])
print(df['title'].str.upper())
print(df['title'].str.lower())
print(df['title'].str.title())

df['title']=df['title'].str.upper()
print(df['title'])

df['title']=df['title'].apply(lambda x : x.title())
print(df['title'])