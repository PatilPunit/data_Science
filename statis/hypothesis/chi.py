import numpy as np
from scipy.stats import chi2_contingency
import pandas as pd
import seaborn as sea

df = sea.load_dataset('titanic')

contingecy_table = pd.crosstab(df['sex'], df['survived'])

chi2,p_value,dof,expected = chi2_contingency(contingecy_table)

print(expected)
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant association")
else:
    print("Fail to reject the null hypothesis: There is no significant association")