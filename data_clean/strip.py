import pandas as pd
df=pd.read_csv('/home/punit/Documents/Ds/pandas/netflix.csv')
print(df.head())

movie_title='   Titanic  '
print('.',movie_title,'.')
print('.',movie_title.rstrip(),'.')
print('.',movie_title.lstrip(),'.')
print('.',movie_title.strip(),'.')

df['title'].str.strip()
print(df['title'])