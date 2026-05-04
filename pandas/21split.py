import pandas as pd

path='/home/punit/Documents/Ds/pandas/Car_sales.csv'
df = pd.read_csv(path)
print(df)

df = df[['Manufacturer','Model','Sales_in_thousands','Vehicle_type','Price_in_thousands','Engine_size','Horsepower']]

pass_filter=df['Vehicle_type']=='Passenger'
car_filter=df['Vehicle_type']=='Car'

pass_avg=df[pass_filter] ['Sales_in_thousands'].mean()

car_avg=df[car_filter] ['Sales_in_thousands'].mean()

avg=pd.DataFrame({'Vehicle_type':['Car_average','Pass_average'],'Mean':[car_avg,pass_avg]})
print(avg)
