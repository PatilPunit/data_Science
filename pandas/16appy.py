import pandas as pd
import numpy as np

path='/home/punit/Documents/Ds/pandas/players_20.csv'
df=pd.read_csv(path)
df.set_index('short_name',inplace=True)
df=df[['long_name','age','club','dob','height_cm','weight_kg','nationality']]


print(df)

#apply method is use to apply diffrent inbuilt or user function

sq_age=df['age'].apply(np.sqrt)
print(sq_age)

#to show BMI of every player

def calc_BMI(row):
    return row['weight_kg']/(row['height_cm']/100)**2

play_bmi=df.apply(calc_BMI,axis=1)
print(play_bmi)