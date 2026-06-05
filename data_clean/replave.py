import pandas as pd
df=pd.read_csv('/home/punit/Documents/Ds/pandas/netflix.csv')
print(df.head())

#fillna() with mode , mean

mode = df['rating'].mode()[0]#categorical  data

df.fillna({'rating':mode},inplace=True)
# print(df['rating'].fillna(mode,inplace=True))
print(df['rating'].isnull().sum())

# fillna with arbitary number

df.fillna({'duration':'0'},inplace=True)
print(df['duration'].isnull().sum())

df['director']=df['director'].ffill(inplace=True)
print(df['director'].isnull().sum())


