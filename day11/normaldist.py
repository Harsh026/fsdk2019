import numpy as np
import matplotlib.pyplot as plt
normally = np.random.normal(150.0, 20.0, 1000)


plt.hist(normally,bins=100)
plt.show()
np.std(normally)
np.var(normally)