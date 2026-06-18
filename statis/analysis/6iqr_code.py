import numpy as np

arr=np.array([2,3,4,5,7,9,11,14,17,20,27,31,24,201])
q1=np.percentile(arr,25)
q3=np.percentile(arr,75)

iqr=q3-q1
uf=q3+1.5*iqr
lf=q1-1.5*iqr

l=[]
for i in arr:
    if i >=lf and i <= uf:
        l.append(i)
        
print(l)

import seaborn as sea
import matplotlib.pyplot as plt

sea.boxplot(x=arr)
plt.show()

sea.boxplot(x=l)
plt.show()