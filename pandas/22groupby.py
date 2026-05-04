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

#group attributes

print(group_obj.groups)
print('_'*130)
print(group_obj.ngroups)
print('_'*130)
print(group_obj.groups.items())
print('_'*130)
print(group_obj.groups.keys())
print('_'*130)
print(group_obj.groups.pop('Acura'))
print('_'*130)
print(group_obj.get_group('Ford'))
print('_'*130)

vehicle=dfNum.groupby('Vehicle_type').mean()
print(vehicle)
print('_'*130)
vehicle=dfNum.groupby('Vehicle_type').sum()
print(vehicle)
print('_'*130)
vehicle=dfNum.groupby('Vehicle_type').value_counts()
print(vehicle)
vehicle=dfNum.groupby('Vehicle_type').count()
print(vehicle)
vehicle=dfNum.groupby('Horsepower',dropna=False).count()
print(vehicle)
#find null values

null_sum=df.isnull().sum()
print(null_sum)