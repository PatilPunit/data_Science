import numpy as np
import scipy.stats as stats

sample1 = np.array([172, 171, 190, 121, 181, 162, 109, 178, 182, 171])
sample2 = np.array([165, 170, 175, 160, 180, 155, 190, 185, 175, 160])

t_test,p_value = stats.ttest_ind(sample1, sample2)

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The two samples have significantly different means.")
else:
    print("Fail to reject the null hypothesis: The two samples do not have significantly different means.")