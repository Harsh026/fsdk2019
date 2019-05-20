import numpy as np 
from scipy import stats

x = np.array([ 13, 18, 13, 14, 13, 16, 14, 21, 13]) 
print (type(x))
print (x)



print("Sum is: ", x.sum())
print("Average/Mean value is: ", x.mean())
print("Max value is: ", x.max())
print("Min value is: ", x.min())
print("median is :",np.median(x))
print("mode is:", stats.mode(x))
print("range is:", x.max()-x.min())