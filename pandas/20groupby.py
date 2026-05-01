import pandas as pd

path='/home/punit/Documents/Ds/pandas/Car_sales.csv'
df = pd.read_csv(path)
print(df)

df = df[['Manufacturer','Model','Sales_in_thousands','Vehicle_type','Price_in_thousands','Engine_size','Horsepower']]
dfsum=df.agg('sum')
print(dfsum)
print('_'*130)
dfmean=df.drop(['Manufacturer','Model','Vehicle_type'],axis=1)
dfmean=dfmean.agg('mean')
print(dfmean)


