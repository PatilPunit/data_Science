import pandas as pd
df=pd.read_csv('/home/punit/Documents/Ds/pandas/netflix.csv')
print(df.head())

#checking null vallues
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sort_values(ascending=False))

#checking the percentage of null values in coliumns
for i in df :
    per = df[i].isnull().mean()
    print(i + ' : ' +str(round(per*100)))