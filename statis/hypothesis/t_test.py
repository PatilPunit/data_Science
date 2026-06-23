import numpy as np
from scipy import stats

sample = np.array([172,171,190,121,181,162,109,178,182,171])
samp_mean = np.mean(sample)
samp_std = np.std(sample,ddof=1)
n = len(sample)
mean_pop=170

t_statistic = (samp_mean - mean_pop) / (samp_std / np.sqrt(n))

p_value = 1 - stats.t.cdf(t_statistic, df=n-1)

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis: The sample mean is not significantly different from the population mean.")