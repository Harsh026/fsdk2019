import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)
incomes=np.append(incomes,5000000)
plt.hist(incomes,bins=50)
plt.show()
incomes.mean()