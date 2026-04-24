import numpy as np
import matplotlib.pyplot as mt
import pandas as pd
import random as rd
import pymongo as pm
df = pd.read_csv("/home/punit/Documents/Ds/pandas/players_20.csv")

df=df[['short_name','overall','potential','preferred_foot','skill_moves','international_reputation']]
print(df)
df.set_index('short_name',inplace=True)
print(df)

wow_sam=df[['overall','potential','preferred_foot','skill_moves','international_reputation']].sample(6,random_state=99,weights="overall")
print(wow_sam)

print(df.iloc[[1,2,3],:])
print(df.iloc[[list((df['overall']>80 ) & (df['potential']>75))],[1,2,3]])