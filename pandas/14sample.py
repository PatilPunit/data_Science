import pandas as pd
import numpy as np

df=pd.read_csv('/home/punit/Documents/Ds/pandas/players_20.csv')
df=df[['short_name','long_name','age','dob','height_cm','weight_kg','club','nationality']]
df.set_index('short_name',inplace=True)

#sample method is use to extract the limited and selective data and series from dataframe
#sample make random set of data as collection

nat_sam=df['nationality'].sample(10)
print(nat_sam)

nat_samq=df['nationality'].sample(10,random_state=99) #to not change the random elements we use this paramenter run for given  numbers
print(nat_samq)

perc_sam=df.sample(frac=0.2) #frac is use to  extract 20% of sample so basicallly to collect data as per percentage
print(perc_sam)

#upsample : is the process to increase the number of data as sample
up_sam=df.sample(frac=2,replace=True)
print(up_sam)