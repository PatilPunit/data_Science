import pandas as pd
from IPython.display import display , HTML
import cufflinks as cf
import matplotlib.pyplot as plt
import plotly.express as ex
import numpy as np
cf.set_config_file(sharing='public',theme='ggplot',offline=True)

df=pd.read_csv('/home/punit/Documents/Ds/data_visulization/population_total.csv')

df.dropna(inplace=True)

dfpop=df.pivot(index='year',columns='country',values='population')
print(dfpop)

dfpop5=dfpop[['United States','India','Brazil','Indonesia','China']]
print(dfpop5)

# dfpop5.iplot(kind='line',colors='red')
# plt.show()
"""
fig = ex.line(dfpop5)
fig.show()

dfpop5=dfpop5[dfpop5.index.isin([2020])]
dfpop5=dfpop5.T
fig=ex.bar(dfpop5)
fig.show()
"""

dfpop5=dfpop5[dfpop5.index.isin([1970,1980,1990,2000,2020])]
# dfpop5=dfpop5.T
fig=ex.bar(dfpop5)
fig.show()