import pandas as pd
df=pd.read_csv('/home/punit/Documents/Ds/pandas/netflix.csv')
print(df.head())

df_movie=df[df['type']=='Movie']
print(df_movie)

print(df_movie['duration'].str.split())
print(df_movie['duration'].str.split(expand=True))