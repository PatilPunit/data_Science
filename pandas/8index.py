
#we can use indexing to sort the df as index
#in industry to give index or id to dsta is common practice so we should be able sort them according to index

# to create index

import pandas as pd
import numpy as np
import random as rd
df = pd.read_csv("/home/punit/Documents/Ds/pandas/StudentsPerformance.csv")

index =np.arange(0,1000)
rd.shuffle(index)

print(index)
df["index"]= index # created column called index


# to set index 
df.set_index('index',inplace=True)
print(df) #as this methid create as copy we can use the inplace argument

print(df.sort_index())