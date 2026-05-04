import pandas as pd

path='/home/punit/Documents/Ds/pandas/Car_sales.csv'
df = pd.read_csv(path)
print(df)

df = df[['Manufacturer','Model','Sales_in_thousands','Vehicle_type','Price_in_thousands','Engine_size','Horsepower']]
dfsum=df.agg('sum')
print(dfsum)
print('_'*130)
dfmean=df.drop(['Manufacturer','Model','Vehicle_type'],axis=1)
dfmean1=dfmean.agg('mean')
print(dfmean1)
print('_'*130)
dfmeancount1=dfmean.agg(['mean','count'])
print(dfmeancount1)
print('_'*130)
dfmeancount2=dfmean.apply(['mean','count'])
print(dfmeancount2)
print('_'*130)
dfcol=dfmean.agg({'Sales_in_thousands':['sum','mean'],'Horsepower':['max','min']})
print(dfcol)
print('_'*130)
print(df[['Sales_in_thousands','Price_in_thousands']].agg('sum',axis=1))

#renaming index
print(df.agg(x=('Sales_in_thousands','sum'),y=('Horsepower','mean')))