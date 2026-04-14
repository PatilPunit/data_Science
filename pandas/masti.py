import numpy as np
import matplotlib.pyplot as mt
import pandas as pd
import random as rd

df = pd.read_csv("/home/punit/Documents/Ds/pandas/StudentsPerformance.csv")

df['r'] =df['gender'].isin(['female'])
print(df)
print(df.value_counts('r'))