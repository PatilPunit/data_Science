import pandas as pd
from IPython.display import display , HTML
import cufflinks as cf
import matplotlib.pyplot as plt
import plotly.express as ex
cf.set_config_file(sharing='public',theme='ggplot',offline=True)

df=pd.read_csv('/home/punit/Documents/Ds/data_visulization/population_total.csv')

df.dropna(inplace=True)

dfpop=df.pivot(index='year',columns='country',values='population')
print(dfpop)

dfpop5=dfpop[['United States','India','Brazil','Indonesia','China']]
print(dfpop5)


fig = ex.line(dfpop5)
fig.show()