
import pandas as pd

path='/home/punit/Documents/Ds/pandas/imdb/IMDb movies copy.csv'
pathq='/home/punit/Documents/Ds/pandas/imdb/IMDb ratings.csv'
df = pd.read_csv(path)
dfq=pd.read_csv(pathq)

#concatnate horizontally
print(df.shape)
print(dfq.shape)
df_con_horz=pd.concat([df,dfq],axis=1)
df_con_ver=pd.concat([df,dfq],axis=0)
print(df_con_horz.shape)
print(df_con_ver.shape)

print(df.merge(how='inner',right=dfq))

#concanate vertically

print(pd.concat([df,dfq],ignore_index=True))

df =df[['imdb_title_id','title','genre','country','year']]
dfq=dfq[['imdb_title_id','total_votes','mean_vote']]

df_sam=df.sample(frac=0.5)
print(df)
print(df.shape)
print(df_sam.shape)

print(pd.concat([df,df_sam],axis=0))

df_innneer=df.merge(dfq,how='inner',on='imdb_title_id')
df_oiter=df.merge(dfq,how='outer',on='imdb_title_id')
print(df.shape)
print(dfq.shape)
print(df_innneer.shape)
print(df_oiter.shape)

#inner

df_innneer=df.merge(dfq,how='inner',on='imdb_title_id')

#exclusive inner
df_innneer=df.merge(dfq,how='inner',on='imdb_title_id',indicator=True).query("_merge!='both'")
print(df_innneer)

#outer

df_outer=df.merge(dfq,how='outer',on='imdb_title_id')

#exclusive outer
df_outer=df.merge(dfq,how='inner',on='imdb_title_id',indicator=True).query("_merge!='left' and _merge!='right'")
print(df_outer)



#right

df_right=df.merge(dfq,how='right',on='imdb_title_id')

#exclusive right
df_right=df.merge(dfq,how='right',on='imdb_title_id',indicator=True).query("_merge!='left'")
print(df_right)

#left

df_left=df.merge(dfq,how='left',on='imdb_title_id')

#exclusive left
df_left=df.merge(dfq,how='inner',on='imdb_title_id',indicator=True).query("_merge!='right'")
print(df_left)