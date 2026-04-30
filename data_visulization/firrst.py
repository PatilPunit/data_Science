import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path='/home/punit/Documents/Ds/data_visulization/population_total.csv'
df=pd.read_csv(path)

print(df)

#dropping  null values
df.dropna(inplace=True)

dfpop=df.pivot(index='year',columns='country',values='population')
print(dfpop)

dfpop5=dfpop[['United States','India','Brazil','Indonesia','China']]
print(dfpop5)
"""
dfpop5.plot(kind='line',xlabel='Year',ylabel='Population',title='Population Growth (1920-2020)',figsize=(14,12))
plt.show()


#selecting only 2020
dfyear=dfpop5[dfpop5.index.isin([2020])]
dfyear = dfyear.T

dfyear.plot(kind='bar',color='orange')
plt.show()

#selecting n years

dfyearn=dfpop5[dfpop5.index.isin([1980,1990,2000,2020])]
dfyearn.plot(kind='bar')
plt.show()

#piechart
# Making int to str

dfyear.rename(columns={2020:'2020'},inplace=True)
dfyear.plot(kind='pie',y='2020')
plt.show()

dfpop5['United States'].plot(kind='box')
plt.show()


dfpop5.plot(kind='box')
plt.show()
"""
#histogram

dfpop5['Indonesia'].plot(kind='hist')
plt.show()

dfpop5[['Indonesia','India']].plot(kind='hist')
plt.show()