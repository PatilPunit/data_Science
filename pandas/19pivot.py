# A  pivot table is data analysis tool which summerize large databases into summerized and understandable rows and columns
# in pandas pivot() and pivot_table() methid is used to make pivot tables

#pivot() reshape data based on columns
# It does not support aggregation

#pivot_table() create spread sheet type pivot table
#Supports Aggregation

import pandas as pd
df = pd.read_csv('/home/punit/Documents/Ds/pandas/gdp.csv',encoding="unicode_escape")
print(df)

gdp_pivot = df.pivot(index='year',columns='country',values='gdppc')
print(gdp_pivot)


#pivot table
dfx=pd.read_excel('/home/punit/Documents/Ds/pandas/supermarket_sales.xlsx')
print(dfx)

dfx.drop(columns=['Time'],axis=0,inplace=True)
#only numerical data can be sum
gender_sum=dfx.pivot_table(index='Gender',values=['Unit price','cogs','gross margin percentage','gross income','Tax 5%','Rating'],aggfunc='sum')
print(gender_sum)

gender_max=dfx.pivot_table(index='Gender',values=['Rating','Unit price','cogs'],aggfunc="max")
print(gender_max)

gender_product=dfx.pivot_table(index='Gender',columns='Product line',values='Total',aggfunc='sum')
print(gender_product)