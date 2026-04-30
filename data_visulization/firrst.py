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

dfpop5.plot(kind='line',xlabel='Year',ylabel='Population',title='Population Growth (1920-2020)',figsize=(14,12))
plt.show()


#selecting only 2020
dfyear=dfpop5[dfpop5.index.isin([2020])]
dfyear = dfyear.T

dfyear.plot(kind='bar',color='orange')
plt.show()

#selecting n years

dfyearn=dfpop5[dfpop5.index.isin([1980,1990,2000,2020])]
# dfyearn =dfyearn.T

dfyearn.plot(kind='bar')
plt.show()