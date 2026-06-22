import numpy as np
from scipy.stats import norm

sample=np.array([172,171,190,121,181,162,109,178,182,171])
std=sample.std()
mean=sample.mean()
pop_std=6
pop_mean=170
n=len(sample)

z_score=(mean-pop_mean)/(pop_std-np.sqrt(n))

p_value=2*(1-norm.cdf(abs(z_score)))

if p_value<0.05:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

print("Z-score:", z_score)