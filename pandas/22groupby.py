#now the groupby method is use to replce the split statergy
# groupby method directly made datafraem as the filter

import pandas as pd

path='/home/punit/Documents/Ds/pandas/Car_sales.csv'
df = pd.read_csv(path)
print(df)

df = df[['Manufacturer','Model','Sales_in_thousands','Vehicle_type','Price_in_thousands','Engine_size','Horsepower']]
dfNum=df[['Sales_in_thousands','Vehicle_type','Price_in_thousands','Engine_size','Horsepower']]
vehicle_avg=dfNum.groupby('Vehicle_type').mean()
print(vehicle_avg)
vehicle_avg=dfNum.groupby('Vehicle_type',as_index=False).mean()
print(vehicle_avg)

#the groupby method creates a group object
group_obj=df.groupby('Manufacturer')
print(group_obj)

