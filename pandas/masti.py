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
print(df.loc['L. Messi','overall'])
print(df.loc['Wang Haijian','potential'])

print(df.loc[:,'potential'])
print(df.loc[df['potential']>90,'overall'])

