
import pandas as pd

path='/home/punit/Documents/Ds/pandas/imdb/IMDb movies copy.csv'
pathq='/home/punit/Documents/Ds/pandas/imdb/IMDb ratings.csv'
df = pd.read_csv(path)
dfq=pd.read_csv(pathq)

print(df.shape)
print(dfq.shape)
df_con_horz=pd.concat([df,dfq],axis=1)
df_con_ver=pd.concat([df,dfq],axis=0)
print(df_con_horz.shape)
print(df_con_ver.shape)