#here we will learn about how to add columns in pandas
\
import numpy as np
import pandas as pd
#1. by squre  brackets

df = pd.read_csv("/home/punit/Documents/Ds/pandas/StudentsPerformance.csv")
df['Launguage'] = 70 # all  rows got the same value 70
print(df.head())

# add columns with an array         

laungauge_score = np.arange(0,1000) # a functions use to ake sequential series of numbers
df['Launguage'] = laungauge_score
print(df)

# add columns with random values 

laungauge_score = np.random.randint(1,100,size=1000)
df['Launguage'] = laungauge_score
print(df)

# assign method

score1 = np.random.randint(1,100,size=1000)

score2 = np.random.randint(1,100,size=1000)

s1=pd.Series(score1,index=np.arange(0,1000))
s2=pd.Series(score1,index=np.arange(0,1000))

print(df.assign(score2 = s2 , score1 = s1))

# insert () is use to insert a columns at specefic position

df.insert(2,"Test",pd.Series(score1,index=np.arange(0,1000)))
print(df)