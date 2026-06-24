import pandas as pd
import numpy as np
from scipy.stats import f_oneway
import seaborn as sea

df=sea.load_dataset('titanic')

df=df[['age','pclass']].dropna()

class_1=df[df['pclass']==1]['age']
class_2=df[df['pclass']==2]['age']
class_3=df[df['pclass']==3]['age']

f_statistic, p_value = f_oneway(class_1, class_2, class_3)

print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in means")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in means")